# Setup

Requirements: Python ≥ 3.9 and PyYAML. No server, database or network service is needed.

```bash
git clone https://github.com/panndabea/design-inspiration-library
cd design-inspiration-library
pip install -r requirements.txt      # PyYAML
pip install pytest flake8            # only for development
```

## Commands

| Command | Purpose |
|---|---|
| `python scripts/search_library.py --query "…" [--type reference\|pattern] [--category …] [--limit N] [--json]` | Keyword search over references and patterns |
| `python scripts/search_library.py --list-categories` | List reference categories and pattern groups |
| `python scripts/validate_library.py` | Schema, provenance, cross-link and index checks |
| `python scripts/build_index.py [--check]` | Regenerate (or check) the index files |
| `python scripts/extract_references.py` | Regenerate processed reports and raw catalogues from the originals |
| `python scripts/check_urls.py` | Re-check every report URL (network; ~1 min) and write `references/url-checks.yaml` |
| `python -m pytest -q` | Tests |

CI (`.github/workflows/validate.yml`) runs validation, the index check and the tests on every PR.

## How search works

`search_library.py` tokenises the query, expands a small synonym list (e.g. *timeline → history, temporal*), and scores fields with weights (title and project types highest, descriptions lower). It is a starting point: agents should open the returned files and judge relevance themselves.
