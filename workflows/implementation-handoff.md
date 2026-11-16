# Workflow: Implementation Handoff

After the user approves a direction:

1. Fill `templates/design-decision.md` (chosen direction, rejected alternatives and why, patterns/references used, open questions).
2. Translate the direction into an implementation plan:
   - Data/content model first (objects, relationships, provenance fields)
   - Component inventory derived from the patterns (e.g. `TimelineAxis`, `EvidenceChip`, `ScenarioPanel`)
   - State model (URL-addressable states for narrative steps and views)
   - Accessibility acceptance criteria per signature interaction
   - Performance budget and library choices (justify any heavy dependency)
3. Build a vertical slice of the signature interaction first and show it to the user before building everything.
4. Keep the decision record updated if the design changes during implementation.
5. Optionally contribute learnings back to this library (new example in `examples/`), via PR.
