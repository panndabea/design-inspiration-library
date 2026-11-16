# Reusable Prompt for Future Projects

Copy, fill in the brackets, and send to Devin (or another coding agent) at the start of a project.

```text
New project: [one-sentence idea]
Audience: [who]   Goal: [what they should understand / decide / do]
Constraints: [stack, devices, accessibility level, timeline]

Before designing the interface, use the Design Inspiration Library
(https://github.com/panndabea/design-inspiration-library, skill: design-inspiration):
1. Fill templates/project-design-brief.md for this project.
2. Search the library (scripts/search_library.py) and create an inspiration shortlist
   of relevant references and patterns, citing their IDs.
3. Generate three distinct, original design directions (templates/design-directions.md)
   with rationale, accessibility and performance notes. Avoid generic dashboard defaults
   unless justified.
4. Show me the directions and wait for my approval before full implementation.
```

Short form: `Use the design-inspiration skill for this project before building any UI.`

## Long form (from the PRD)

```text
Build the following project: [PROJECT IDEA].

Before implementation, consult my Design Inspiration Library
(https://github.com/panndabea/design-inspiration-library, skill: design-inspiration).

Analyze the project and identify the most relevant visual design references and interaction
patterns from both research reports.

Propose three distinctive design directions.

Explain the visual language, UX concept, interaction patterns and supporting references for each.

Recommend the strongest direction.

Create a visual prototype after I select a direction.

Do not start full implementation until the design is approved.

The final experience should feel original, polished, intuitive and appropriate for the project,
rather than resembling a generic SaaS template.
```
