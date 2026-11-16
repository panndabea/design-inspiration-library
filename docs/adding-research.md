# Adding and Maintaining Research

## Add a new research report

1. Put the untouched file in `research/original/<slug>/` (never edit it afterwards).
2. Register it in `scripts/extract_references.py` (`REPORTS`) and `scripts/validate_library.py` (`REPORTS`).
3. Run `python scripts/extract_references.py` → processed Markdown and `research/processed/<slug>-raw-references.yaml`.
4. Run `python scripts/check_urls.py` to record URL status.

## Add a curated reference

1. Choose a row from a raw catalogue; copy the URL exactly (validation requires it to occur in an original report).
2. Create `references/entries/ref-<short-name>.yaml` with the fields of an existing entry (see any file in `references/entries/`). Use the raw catalogue `raw_id`, a short report excerpt and the URL check result. Leave traits empty and explain in `library_notes` rather than inventing them.
3. Set `verification.visual: visually-verified` only if a person or agent actually looked at the site, and say what was checked in `library_notes`.
4. Link patterns in both directions (`patterns:` in the entry, `supporting_references:` in the pattern).
5. `python scripts/build_index.py && python scripts/validate_library.py && python -m pytest -q`, then open a PR.

## Add a pattern

Copy an existing file in `patterns/<group>/`, keep the front matter fields and all `##` sections (validation checks them), cite at least one reference and state the source report provenance. Patterns must generalise across references – not describe one site.

## Periodic maintenance

- Re-run `check_urls.py` (e.g. quarterly), update `verification` in affected entries, mark dead projects `availability: archived` and add an archive link in `library_notes` if one exists in the reports.
- Add learnings from real projects as new `examples/`.
