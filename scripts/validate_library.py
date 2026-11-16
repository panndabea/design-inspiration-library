#!/usr/bin/env python3
"""Validate the library: schema, IDs, cross-links and research provenance.

    python scripts/validate_library.py

Exit code 1 on any error. Checks include:
* every reference entry has the required fields and a matching file name
* every reference URL literally occurs in at least one original report
  (guards against invented references) and its raw_ids exist
* every pattern/reference cross-link resolves in both directions
* original reports still match the SHA-256 recorded in the processed files
* examples cite only existing reference and pattern IDs
* generated index files are up to date
* .agents/skills/design-inspiration/SKILL.md mirrors skills/design-inspiration/SKILL.md
"""
from __future__ import annotations

import hashlib
import re
import sys

import yaml

from build_index import render
from library import ROOT, load_entries, load_patterns, rel

URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")

REPORTS = {
    "interactive-learning": "research/original/interactive-learning/deep-research-report-18.md",
    "beyond-dashboards": "research/original/beyond-dashboards/deep-research-report-19.md",
}
REF_REQUIRED = {
    "id": str, "title": str, "url": str, "source_reports": list, "categories": list,
    "design_language": str, "availability": str, "visual_characteristics": list,
    "interaction_patterns": list, "description": str, "why_it_works": str, "best_suited_for": list,
    "limitations": list, "library_notes": list, "patterns": list, "keywords": list,
    "original_source_reference": list, "verification": dict,
}
PAT_REQUIRED = {
    "id": str, "name": str, "group": str, "source_reports": list, "provenance": str,
    "supporting_references": list, "suitable_for": list, "unsuitable_for": list,
}
PAT_SECTIONS = [
    "Description", "UX goal", "Visual characteristics", "Interaction behavior", "Suitable project types",
    "Unsuitable project types", "Implementation considerations", "Accessibility and performance",
    "Supporting references", "Source provenance",
]
AVAILABILITY = {"live", "archived", "app-primarily", "research-prototype"}
DESIGN_LANGUAGES = {
    "editorial-minimalist", "technical-spatial", "playful-systemic", "data-editorial", "research-native",
}
URL_STATUS = {"url-live", "url-blocked-by-bot-protection", "url-unreachable-at-check", "url-error"}
VISUAL = {"not-visually-verified", "visually-verified"}
OPTIONAL_EMPTY = {"limitations", "library_notes", "visual_characteristics", "interaction_patterns"}
ID_RE = re.compile(r"^(ref|pat)-[a-z0-9]+(-[a-z0-9]+)*$")


def check_types(item: dict, required: dict, where: str, errors: list[str]) -> None:
    for key, typ in required.items():
        if key not in item:
            errors.append(f"{where}: missing field '{key}'")
        elif not isinstance(item[key], typ):
            errors.append(f"{where}: field '{key}' should be {typ.__name__}")
        elif typ in (str, list) and key not in OPTIONAL_EMPTY and not item[key]:
            errors.append(f"{where}: field '{key}' is empty")
    # Non-visual references (papers, directories) may omit visual/interaction traits,
    # but must then explain why in library_notes instead of inventing traits.
    traits = ("visual_characteristics", "interaction_patterns")
    if not item.get("library_notes") and any(item.get(k) == [] for k in traits):
        errors.append(f"{where}: empty visual/interaction traits need an explanation in library_notes")


def validate() -> list[str]:
    errors: list[str] = []
    originals = {slug: (ROOT / path).read_text(encoding="utf-8") for slug, path in REPORTS.items()}
    report_urls = {
        slug: {u.rstrip(".,;:/") for u in URL_RE.findall(text)} for slug, text in originals.items()
    }
    raw_ids = set()
    for slug, text in originals.items():
        raw_path = ROOT / f"research/processed/{slug}-raw-references.yaml"
        raw = yaml.safe_load(raw_path.read_text(encoding="utf-8"))
        raw_ids |= {r["raw_id"] for r in raw["references"]}
        digest = hashlib.sha256((ROOT / REPORTS[slug]).read_bytes()).hexdigest()
        if raw.get("original_sha256") != digest:
            errors.append(f"{slug}: original hash differs from processed catalogue – re-run extract_references.py")
        processed = (ROOT / f"research/processed/{slug}.md").read_text(encoding="utf-8")
        if digest not in processed:
            errors.append(f"research/processed/{slug}.md: provenance header does not match the original's hash")

    entries, patterns = load_entries(), load_patterns()
    ref_ids = {e.get("id") for e in entries}
    pat_ids = {p.get("id") for p in patterns}
    seen_urls: dict[str, str] = {}

    for e in entries:
        where = e["_path"]
        check_types(e, REF_REQUIRED, where, errors)
        if errors and errors[-1].startswith(where + ": missing"):
            continue
        if not ID_RE.match(e["id"]) or not e["id"].startswith("ref-"):
            errors.append(f"{where}: invalid id '{e['id']}'")
        if not where.endswith(f"/{e['id']}.yaml"):
            errors.append(f"{where}: file name does not match id '{e['id']}'")
        url = e["url"].rstrip("/")
        if url in seen_urls:
            errors.append(f"{where}: duplicate URL also used by {seen_urls[url]}")
        seen_urls[url] = e["id"]
        found_in = [s for s, urls in report_urls.items() if e["url"].rstrip(".,;:/") in urls]
        if not found_in:
            errors.append(f"{where}: URL {e['url']} does not occur in any original report")
        for s in e["source_reports"]:
            if s not in REPORTS:
                errors.append(f"{where}: unknown source report '{s}'")
            elif s not in found_in:
                errors.append(f"{where}: claims source '{s}' but URL is not in that report")
        for src in e["original_source_reference"]:
            if src.get("raw_id") not in raw_ids:
                errors.append(f"{where}: unknown raw_id {src.get('raw_id')}")
        if e["availability"] not in AVAILABILITY:
            errors.append(f"{where}: availability must be one of {sorted(AVAILABILITY)}")
        if e["design_language"] not in DESIGN_LANGUAGES:
            errors.append(f"{where}: design_language must be one of {sorted(DESIGN_LANGUAGES)}")
        v = e["verification"]
        for key in ("status", "last_verified", "visual", "method"):
            if key not in v:
                errors.append(f"{where}: verification.{key} missing")
        if v.get("status") not in URL_STATUS:
            errors.append(f"{where}: verification.status must be one of {sorted(URL_STATUS)}")
        if v.get("visual") not in VISUAL:
            errors.append(f"{where}: verification.visual must be one of {sorted(VISUAL)}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(v.get("last_verified", ""))):
            errors.append(f"{where}: verification.last_verified must be YYYY-MM-DD")
        for p in e["patterns"]:
            if p not in pat_ids:
                errors.append(f"{where}: unknown pattern '{p}'")

    for p in patterns:
        where = p["_path"]
        if "_error" in p:
            errors.append(f"{where}: {p['_error']}")
            continue
        check_types(p, PAT_REQUIRED, where, errors)
        if not ID_RE.match(str(p.get("id"))) or not str(p.get("id")).startswith("pat-"):
            errors.append(f"{where}: invalid id '{p.get('id')}'")
        if not where.endswith(f"/{p.get('id')}.md"):
            errors.append(f"{where}: file name does not match id")
        for section in PAT_SECTIONS:
            if f"\n## {section}\n" not in p["_body"]:
                errors.append(f"{where}: missing section '## {section}'")
        for s in p.get("source_reports", []):
            if s not in REPORTS:
                errors.append(f"{where}: unknown source report '{s}'")
        for r in p.get("supporting_references", []):
            if r not in ref_ids:
                errors.append(f"{where}: unknown reference '{r}'")
            elif p["id"] not in next(e for e in entries if e["id"] == r)["patterns"]:
                errors.append(f"{where}: {r} is listed as support but does not list this pattern")
        for e in entries:
            if p.get("id") in e.get("patterns", []) and e["id"] not in p.get("supporting_references", []):
                errors.append(f"{where}: {e['id']} uses this pattern but is not in supporting_references")

    for doc in sorted((ROOT / "examples").glob("**/*.md")):
        text = doc.read_text(encoding="utf-8")
        for ref in sorted(set(re.findall(r"\bref-[a-z0-9]+(?:-[a-z0-9]+)*", text)) - ref_ids):
            errors.append(f"{rel(doc)}: cites unknown reference '{ref}'")
        for pat in sorted(set(re.findall(r"\bpat-[a-z0-9]+(?:-[a-z0-9]+)*", text)) - pat_ids):
            errors.append(f"{rel(doc)}: cites unknown pattern '{pat}'")

    skill, mirror = ROOT / "skills/design-inspiration/SKILL.md", ROOT / ".agents/skills/design-inspiration/SKILL.md"
    if not mirror.exists() or mirror.read_bytes() != skill.read_bytes():
        errors.append(f"{rel(mirror)}: must be an exact copy of {rel(skill)} (cp it)")

    for rel_path, content in render().items():
        path = ROOT / rel_path
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            errors.append(f"{rel_path}: out of date – run python scripts/build_index.py")
    return errors


def main() -> None:
    errors = validate()
    if errors:
        print(f"{len(errors)} problem(s):")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    print(f"OK: {len(load_entries())} references, {len(load_patterns())} patterns validated.")


if __name__ == "__main__":
    main()
