# Workflow: Design Direction Generation and Review

## Generate three directions
Each direction must differ in at least two of: **primary metaphor** (story, landscape, graph, timeline, simulation, briefing…), **navigation model**, **design language** (see `principles/visual-design.md`), **interaction model**.

For each direction document (template `templates/design-directions.md`):
- Name + one-sentence concept
- Primary patterns (IDs) and supporting references (IDs) with what transfers
- Information architecture and key screens/states
- Signature interaction(s) and what they reveal
- Visual language (type, colour, layout, motion) – original, not copied
- Accessibility plan and performance budget
- Risks / trade-offs, and which anti-patterns were consciously avoided
- Fit: when to choose this direction

## Review checklist
- [ ] Three directions are genuinely distinct (not colour variants)
- [ ] Each cites library IDs; the research is used, not decorative
- [ ] No unjustified generic defaults (KPI card grid, sidebar + table) – if used, justified
- [ ] Interaction reveals meaning; motion encodes change
- [ ] Keyboard, contrast, reduced motion, screen reader, responsive covered
- [ ] Performance proportional to value; 3D/WebGL only if space means something
- [ ] Research-derived vs. general guidance is labelled
- [ ] Recommendation given, but the user decides

Present the directions to the user and ask for a choice or combination.
