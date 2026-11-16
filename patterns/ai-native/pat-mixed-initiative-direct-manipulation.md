---
id: pat-mixed-initiative-direct-manipulation
name: Mixed-Initiative Direct Manipulation
group: ai-native
source_reports:
- beyond-dashboards
provenance: Report 19 pattern table ("Direct Manipulation"), manifesto "Preserve agency"; Pluto
supporting_references:
- ref-mit-pluto
suitable_for:
- authoring tools
- analytics
- AI-assisted editing
unsuitable_for:
- touch-only contexts with hidden complex gestures
keywords:
- agency
- ai authoring
- mixed initiative
- text chart
---

# Mixed-Initiative Direct Manipulation

## Description
Users select, drag or mark elements of a visual and the system responds (e.g. generating text); system suggestions can always be edited or rejected.

## UX goal
High agency while still benefiting from automation.

## Visual characteristics
Selections and system suggestions visually distinct; editable suggestion surfaces.

## Interaction behavior
Brush/select → suggestion → accept/edit/reject.

## Suitable project types
- authoring tools
- analytics
- AI-assisted editing

## Unsuitable project types
- touch-only contexts with hidden complex gestures

## Implementation considerations
Suggestions never overwrite user content automatically.

## Accessibility and performance
Every gesture needs a keyboard/menu equivalent.

## Anti-patterns and risks
- unchangeable AI answer (manifesto anti-pattern)

## Supporting references
- `ref-mit-pluto` – [Pluto](https://vis.mit.edu/pubs/pluto/) (`references/entries/ref-mit-pluto.yaml`)

## Source provenance
Report 19 pattern table ("Direct Manipulation"), manifesto "Preserve agency"; Pluto

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
