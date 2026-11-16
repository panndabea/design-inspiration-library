# Design Inspiration Library

A file-based, agent-readable library that turns two Deep Research reports into reusable design inspiration for AI-driven software projects – so that new projects start from research-backed, original design directions instead of generic SaaS defaults.

**New project idea → Project analysis → Relevant design inspiration → Visual concepts → User approval → Implementation**

| Source report | Focus | Preserved at |
|---|---|---|
| Report 18 – *Die schönsten visuellen und interaktiven Lernwebseiten im Internet* (`interactive-learning`) | explorable explanations, visual essays, simulations, interactive learning | `research/original/interactive-learning/` |
| Report 19 – *Beyond Dashboards – Die Zukunft visueller Informationssysteme* (`beyond-dashboards`) | narrative, spatial, relational and AI-native information interfaces | `research/original/beyond-dashboards/` |

## What is inside

| Path | Contents |
|---|---|
| `research/original/` | Both reports, byte-for-byte unmodified |
| `research/processed/` | Readable versions without tool citation markers + raw catalogues of every table row (221 rows, with provenance and SHA-256 of the original) |
| `references/entries/` | 53 curated references (YAML): categories, visual/interaction traits, why it works, suitable projects, limitations, report excerpt, URL check |
| `references/index.yaml`, `references/url-checks.yaml` | Generated index; HTTP check of all 171 report URLs |
| `patterns/` | 25 reusable patterns in 6 groups ([index](patterns/README.md)) |
| `principles/` | Beyond-Dashboard manifesto, visual / interaction / information design, accessibility & performance, anti-patterns |
| `workflows/`, `templates/` | New-project design process and fill-in templates |
| `skills/design-inspiration/SKILL.md` | The agent skill (mirrored to `.agents/skills/` for auto-discovery) |
| `examples/` | Three validation scenarios with three directions each |
| `scripts/` | Extraction, URL check, index build, search, validation |
| `docs/` | [Setup](docs/setup.md), [Devin integration](docs/devin-integration.md), [prompt template](docs/prompt-template.md), [adding research](docs/adding-research.md), [usage examples](docs/usage-examples.md), [PRD](docs/PRD.md) |

## Quick start

```bash
pip install -r requirements.txt
python scripts/search_library.py --query "interactive educational timeline"
python scripts/search_library.py --query "portfolio dependencies decision" --type pattern
python scripts/validate_library.py
```

To use it in a new project, paste the prompt from [docs/prompt-template.md](docs/prompt-template.md) into Devin, or say *"Use the design-inspiration skill"*. See [docs/devin-integration.md](docs/devin-integration.md).

## Honesty and provenance

- Every curated reference URL occurs verbatim in an original report (enforced by `validate_library.py`); descriptions paraphrase the reports.
- All entries are marked `visual: not-visually-verified`: URLs were checked automatically (HTTP, 2026-11-16), but no site was manually reviewed for this MVP.
- Statements are labelled as research-derived (Report 18/19) or as inference/general guidance.
- The library inspires original work; it must not be used to reproduce third-party designs. No third-party content or screenshots are stored.

## Deviations from the PRD structure

- **Pattern groups** follow the structure that emerged from the research (`learning-by-manipulation`, `narrative`, `perspective-and-comparison`, `spatial-and-relational`, `decision-and-exploration`, `ai-native`) instead of the PRD's suggested folders (visual-storytelling, motion-design, …); motion and layout are treated as properties of patterns rather than patterns of their own.
- **`patterns/README.md`** replaces `patterns/index.md` (GitHub renders it automatically) and is generated together with `patterns/index.yaml`.
- **`principles/accessibility-and-performance.md`** replaces `accessibility.md` because the PRD pairs both requirements; **`principles/beyond-dashboard-manifesto.md`** was added for Report 19's manifesto.
- **`.agents/skills/design-inspiration/SKILL.md`** mirrors the skill so Devin discovers it automatically when this repository is cloned.
- Extra scripts: `extract_references.py`, `check_urls.py`, `build_index.py`.
