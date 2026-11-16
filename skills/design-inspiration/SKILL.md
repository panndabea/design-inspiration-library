---
name: design-inspiration
description: Use before designing the UI of a new project, product, website, app, dashboard, explainer or major new screen. Consults the Design Inspiration Library (panndabea/design-inspiration-library) – curated references, patterns and principles from two research reports on interactive learning and beyond-dashboard information interfaces – to produce three original, research-backed design directions and get approval before implementation.
---

# Design Inspiration

> **Before designing the interface for a new project, consult the Design Inspiration Library and identify relevant references and patterns. Generate multiple original design directions, explain the rationale behind each, and obtain approval before full implementation unless the user explicitly requests otherwise.**

Flow: **New project idea → Project analysis → Relevant design inspiration → Visual concepts → User approval → Implementation.**

## When to activate

Activate when any of these is true:
- A new project, product, website, app or prototype needs a user interface.
- A major new screen, view, feature area or redesign is requested.
- The brief mentions explaining, teaching, storytelling, data, dashboards, analytics, monitoring, portfolios, knowledge, AI assistants or decision support.
- The user says "use the design inspiration library / skill" or uses the prompt in `docs/prompt-template.md`.

Do **not** activate for bug fixes, backend-only work, small tweaks inside an existing design system, or when the user explicitly opts out. If the user says "just build it", still run steps 1–4 briefly, state the chosen direction and its references, then implement without waiting.

## 0. Locate the library

The library is a separate repository; do not copy it into the target project.

```bash
LIB=~/repos/design-inspiration-library
[ -d "$LIB" ] || git clone https://github.com/panndabea/design-inspiration-library "$LIB"   # or: gh repo clone panndabea/design-inspiration-library "$LIB"
git -C "$LIB" pull --ff-only
pip install -q pyyaml   # only dependency of the scripts
```

Key files: `references/index.yaml` (catalogue), `references/entries/*.yaml` (one per reference), `patterns/README.md` (pattern index), `principles/*.md`, `workflows/*.md`, `templates/*.md`, `examples/` (three worked scenarios).

## 1. Analyse the project brief

Fill `templates/project-design-brief.md` (save it in the target project as `docs/design/01-brief.md`). Pin down:
- audience and their prior knowledge; the one thing they must understand, decide or do;
- the content objects (concepts, events, entities, relationships, metrics, decisions, uncertainty);
- usage mode: one-time story, repeated tool, or both;
- constraints: devices, accessibility target (WCAG 2.2 AA by default), performance budget, data availability, brand.

Then classify into 1–3 archetypes: **explain/learn**, **narrate/inform**, **explore/analyse**, **decide/operate**, **create/author**. Archetypes map to pattern groups:

| Archetype | Start with pattern groups |
|---|---|
| explain/learn | `learning-by-manipulation`, `narrative` |
| narrate/inform | `narrative`, `perspective-and-comparison` |
| explore/analyse | `spatial-and-relational`, `perspective-and-comparison` |
| decide/operate | `decision-and-exploration`, `ai-native` |
| create/author | `ai-native`, `learning-by-manipulation` |

## 2. Search the reference catalogue

Run several queries – from the domain, the content objects, the archetype and the desired feeling:

```bash
python "$LIB/scripts/search_library.py" --query "interactive educational timeline"
python "$LIB/scripts/search_library.py" --query "dependencies portfolio decision" --type pattern
python "$LIB/scripts/search_library.py" --query "history ai" --category ml-education --json
python "$LIB/scripts/search_library.py" --list-categories
```

Results contain stable IDs (`ref-…`, `pat-…`) and file paths. **Open the files** of the top hits – the ranking is keyword-based and only a starting point. Read `why_it_works`, `limitations`, `best_suited_for` and the `verification` block. Follow `workflows/inspiration-selection.md` and fill `templates/inspiration-shortlist.md` (5–10 references, 4–8 patterns, including the queries you ran and why each item was kept or dropped).

Honesty rules:
- Cite only IDs that exist in the library. Never invent references, URLs or traits.
- Entries are `not-visually-verified` unless stated otherwise; their descriptions paraphrase the reports. If you can open a URL in a browser, you may look at it – say so explicitly when you do.
- Treat `url-unreachable-at-check` / `archived` entries as conceptual inspiration only.

## 3. Select patterns

For each candidate pattern, check its `suitable_for` **and** `unsuitable_for` against the brief, and the "Accessibility and performance" section against your constraints. Prefer patterns that serve the core message over patterns that are merely impressive. Combine 2–4 patterns per direction; a direction is a composition, not a single pattern.

## 4. Generate three design directions

Follow `workflows/design-direction-review.md` and `templates/design-directions.md`. The three directions must differ on at least two of these axes: **organising metaphor** (story, map, instrument, workspace, conversation…), **primary interaction** (scroll, direct manipulation, comparison, query, simulation), **design language** (the five in `principles/visual-design.md`), **information density**.

For each direction give: name and one-line concept; visual language (type, colour, layout, motion); UX concept and the key screen/moment; interaction patterns (pattern IDs); supporting references (ref IDs, and *what specifically* is borrowed – a principle, never a look); fit with the brief; accessibility and performance plan; risks and what would make it fail. Then **recommend one** and justify the recommendation.

At least one direction must be a non-obvious, research-driven option. Low-fidelity sketches, wireframes or a static HTML mock per direction are welcome if cheap; full prototypes come after approval.

## 5. Avoid generic UI defaults

Before presenting, check every direction against `principles/anti-patterns.md`:
- Not the default sidebar + KPI cards + table + chart grid, unless the brief truly is high-frequency monitoring – and then justify it explicitly.
- Lead with meaning (what changed, why it matters, what to do) rather than an inventory of widgets (`principles/beyond-dashboard-manifesto.md`).
- Interaction must reveal something; motion must explain state change; 3D/space only when space means something.
- Separate fact from inference and make evidence addressable when AI or analysis is involved (`pat-visual-provenance`).
- Keyboard, contrast, reduced motion, screen-reader alternatives and mobile layout are designed in, not added later (`principles/accessibility-and-performance.md`).
- Do not reproduce a referenced site's layout, illustrations, copy or brand.

## 6. Obtain approval

Present the three directions concisely (a table plus one paragraph each, plus any sketches) and ask the user to choose, combine or redirect. **Wait** – do not start full implementation before approval unless the user explicitly asked you to proceed without it.

## 7. Document the decision

Fill `templates/design-decision.md` in the target project (`docs/design/04-decision.md`): chosen direction, rejected alternatives and why, references and patterns used (IDs + library commit hash), accessibility/performance commitments, open questions. Project-specific decisions live in the project; the library stays shared.

## 8. Move from approval to implementation

Follow `workflows/implementation-handoff.md`:
1. Turn the direction into design tokens (type scale, colour roles, spacing, motion durations with reduced-motion fallbacks) and a component inventory.
2. Build the single most important moment/screen first as a vertical slice and show it.
3. Implement the rest; keep pattern IDs in code comments or the design doc only where they explain non-obvious structure.
4. Verify keyboard paths, contrast, reduced motion, screen-reader output and performance budget before calling it done.
5. If the implementation diverges from the approved direction, tell the user and update the decision record.

## Improving the library

If you discover a strong new reference or pattern during a project, do not edit the library silently: propose it to the user, then follow `docs/adding-research.md` in a PR to the library repository.
