# Workflow: New Project Design

**New project idea → Project analysis → Relevant design inspiration → Visual concepts → User approval → Implementation**

Use this whenever a new project (or a major new screen/feature) needs an interface. It orchestrates the other workflows.

1. **Analyse the brief** – fill `templates/project-design-brief.md`:
   audience, core message/job-to-be-done, content objects (concepts, events, entities, metrics, decisions), usage mode (one-time story vs. repeated tool), constraints (devices, accessibility, performance, data, brand), success criteria.
2. **Classify the project** – pick 1–3 project archetypes: *explain/learn*, *narrate/inform*, *explore/analyse*, *decide/operate*, *create/author*. This drives which pattern groups are relevant (see `patterns/README.md`).
3. **Search the library** – follow `workflows/inspiration-selection.md`; produce `templates/inspiration-shortlist.md` (5–10 references, 4–8 patterns) with the search queries used.
4. **Generate directions** – follow `workflows/design-direction-review.md`; produce **three** distinct directions in `templates/design-directions.md`. At least one should be non-obvious (not a dashboard/sidebar/card layout).
5. **Check principles** – run each direction against `principles/anti-patterns.md` and `principles/accessibility-and-performance.md`.
6. **Present and obtain approval** – show the directions (text + optional low-fidelity sketches/wireframes) and wait for the user's choice. Do not implement fully before approval unless the user explicitly said so.
7. **Record the decision** – `templates/design-decision.md`.
8. **Hand off to implementation** – `workflows/implementation-handoff.md`.

Store the filled templates in the *target* project (suggested: `docs/design/`), not in this library, unless the project is a library example.
