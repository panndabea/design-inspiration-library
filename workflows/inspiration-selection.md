# Workflow: Inspiration Selection

1. Derive 3–6 search queries from the brief: topic words ("history", "portfolio"), interaction words ("timeline", "simulation", "compare"), audience/purpose words ("executive", "learning").
2. Run them:
   ```bash
   python scripts/search_library.py --query "interactive educational timeline"
   python scripts/search_library.py --query "portfolio dependencies decision" --type pattern
   python scripts/search_library.py --list-categories
   ```
3. Read the top hits (`references/entries/*.yaml`, `patterns/**/*.md`). Check `limitations`, `availability` and `verification` – do not rely on archived/blocked links without saying so.
4. Select **5–10 references** and **4–8 patterns**. For each, write one sentence: *what principle transfers to this project* (not what it looks like).
5. Add at least one reference from outside the project's obvious domain (e.g. a learning explorable for an enterprise tool) – cross-domain transfer is where originality comes from.
6. Pull relevant principles from `principles/`.
7. Record queries, picks and rejections in `templates/inspiration-shortlist.md`.

Rules: never invent references or properties not in the library; if something is not in the library, label it as outside knowledge. Visual properties are **not visually verified** unless you opened the site yourself – say so.
