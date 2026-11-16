# AGENTS.md

Instructions for AI coding agents (Devin, Codex, Claude Code, Cursor, …).

## If you are designing a UI for another project

Use the skill in `skills/design-inspiration/SKILL.md` (mirrored at `.agents/skills/design-inspiration/SKILL.md` for automatic discovery). In short:

> Before designing the interface for a new project, consult the Design Inspiration Library and identify relevant references and patterns. Generate multiple original design directions, explain the rationale behind each, and obtain approval before full implementation unless the user explicitly requests otherwise.

Start with `workflows/new-project-design.md`; search with `python scripts/search_library.py --query "..."`. Store filled templates in the *target* project (`docs/design/`), not here.

## If you are maintaining this library

- Setup: `pip install -r requirements.txt` (PyYAML only; Python ≥ 3.9). Tests need `pytest`.
- **Never edit `research/original/`.** Processed reports and raw catalogues are generated: `python scripts/extract_references.py`.
- After editing `references/entries/` or `patterns/`, run `python scripts/build_index.py` (regenerates `references/index.yaml`, `patterns/index.yaml`, `patterns/README.md`).
- Edit the skill only in `skills/design-inspiration/SKILL.md`, then `cp skills/design-inspiration/SKILL.md .agents/skills/design-inspiration/SKILL.md`.
- Before committing: `python scripts/validate_library.py && python -m pytest -q && flake8 scripts tests` (CI runs the first two).
- Every reference URL must occur verbatim in an original report; do not invent references, traits or screenshots. Mark anything not personally viewed as `not-visually-verified`.
- Label research-derived statements vs. general guidance/inference (the files use "Report 18/19 …" vs. "Inference"/"General guidance").
- Adding new research: `docs/adding-research.md`.
