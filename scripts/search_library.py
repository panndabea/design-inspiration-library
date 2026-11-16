#!/usr/bin/env python3
"""Keyword search over references and patterns.

    python scripts/search_library.py --query "interactive educational timeline"
    python scripts/search_library.py --query "dependencies portfolio" --type pattern --limit 5
    python scripts/search_library.py --query "ai history" --category ml-education --json
    python scripts/search_library.py --list-categories

Searches titles, descriptions, categories, keywords, project types, visual
characteristics and interaction patterns. Prints stable IDs and file paths.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter

from library import load_entries, load_patterns

# Field weights: how strongly a match in a field counts.
REF_FIELDS = {
    "title": 4, "keywords": 3, "categories": 3, "design_language": 2, "best_suited_for": 3,
    "interaction_patterns": 2, "visual_characteristics": 2, "description": 1.5, "why_it_works": 1,
    "patterns": 1, "creator": 1, "limitations": 0.5,
}
PAT_FIELDS = {
    "name": 4, "keywords": 2, "group": 2, "suitable_for": 3, "_body": 1, "id": 1,
}
STOP = {"a", "an", "and", "the", "of", "for", "to", "in", "on", "with", "or", "app", "application",
        "website", "site", "web", "interactive", "modern", "platform"}
SYNONYMS = {
    "educational": ["education", "learning", "explorable", "explainer", "course"],
    "learn": ["learning", "education", "explorable"],
    "timeline": ["time", "history", "chronological", "temporal"],
    "history": ["timeline", "historical", "time"],
    "ai": ["machine", "learning", "llm", "neural", "transformer", "ml"],
    "dashboard": ["kpi", "briefing", "monitoring", "analytics"],
    "portfolio": ["project", "projects", "decision", "dependencies", "scenario"],
    "trends": ["trend", "global", "change", "technology"],
    "map": ["landscape", "atlas", "spatial"],
    "network": ["graph", "relationships", "ecosystem"],
    "compare": ["comparison", "split", "scenario"],
    "story": ["narrative", "storytelling", "scrollytelling", "essay"],
    "accessible": ["accessibility", "multimodal", "screen"],
}


def tokens(text: str) -> list[str]:
    out = []
    for tok in re.findall(r"[a-z0-9äöüß]+", text.lower()):
        if tok in STOP or len(tok) < 2:
            continue
        out.append(tok[:-1] if len(tok) > 4 and tok.endswith("s") else tok)
    return out


def flatten(value) -> str:
    if isinstance(value, (list, tuple)):
        return " ".join(flatten(v) for v in value)
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    return "" if value is None else str(value)


def query_terms(query: str) -> dict[str, float]:
    terms: dict[str, float] = {}
    for tok in tokens(query):
        terms[tok] = max(terms.get(tok, 0), 1.0)
        for syn in SYNONYMS.get(tok, []):
            for s in tokens(syn):
                terms.setdefault(s, 0.4)
    return terms


def score(item: dict, fields: dict[str, float], terms: dict[str, float]) -> tuple[float, list[str]]:
    total, matched = 0.0, set()
    for field, weight in fields.items():
        counts = Counter(tokens(flatten(item.get(field))))
        for term, tw in terms.items():
            hits = sum(c for t, c in counts.items() if t == term or (len(term) > 3 and t.startswith(term)))
            if hits:
                total += weight * tw * (1 + 0.2 * min(hits - 1, 5))
                if tw == 1.0:
                    matched.add(term)
    primary = [t for t, w in terms.items() if w == 1.0]
    if primary:
        total *= 0.5 + len(matched) / len(primary)
    return round(total, 2), sorted(matched)


def search(query: str, kind: str = "all", category: str | None = None, limit: int = 10) -> list[dict]:
    terms = query_terms(query)
    results = []
    if kind in ("all", "reference"):
        for e in load_entries():
            if category and category not in e.get("categories", []):
                continue
            s, m = score(e, REF_FIELDS, terms)
            if s > 0:
                results.append({
                    "type": "reference", "id": e["id"], "title": e["title"], "path": e["_path"],
                    "url": e["url"], "score": s, "matched": m,
                    "patterns": e.get("patterns", []), "url_status": e["verification"]["status"],
                })
    if kind in ("all", "pattern"):
        for p in load_patterns():
            if category and category != p.get("group"):
                continue
            s, m = score(p, PAT_FIELDS, terms)
            if s > 0:
                results.append({
                    "type": "pattern", "id": p["id"], "title": p["name"], "path": p["_path"],
                    "score": s, "matched": m, "references": p.get("supporting_references", []),
                })
    results.sort(key=lambda r: (-r["score"], r["id"]))
    return results[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--query", "-q", help="free-text query")
    parser.add_argument("--type", choices=["all", "reference", "pattern"], default="all")
    parser.add_argument("--category", help="reference category or pattern group filter")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--list-categories", action="store_true")
    args = parser.parse_args()

    if args.list_categories:
        cats = Counter(c for e in load_entries() for c in e.get("categories", []))
        groups = Counter(p.get("group") for p in load_patterns())
        print("Reference categories:")
        for c, n in sorted(cats.items()):
            print(f"  {c} ({n})")
        print("Pattern groups:")
        for g, n in sorted(groups.items()):
            print(f"  {g} ({n})")
        return
    if not args.query:
        parser.error("--query is required (or use --list-categories)")

    results = search(args.query, args.type, args.category, args.limit)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    if not results:
        print("No matches. Try broader terms or --list-categories.")
        return
    for r in results:
        print(f"[{r['type']}] {r['id']}  (score {r['score']})")
        print(f"    {r['title']}")
        print(f"    {r['path']}" + (f"  {r['url']}" if r.get("url") else ""))
        related = r.get("patterns") or r.get("references")
        if related:
            print(f"    related: {', '.join(related)}")
        print(f"    matched: {', '.join(r['matched'])}")


if __name__ == "__main__":
    main()
