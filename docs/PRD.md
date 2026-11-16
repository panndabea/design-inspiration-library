# PRD: Design Inspiration Library for AI-Powered Software Development

**Version:** 1.0  
**Project name:** Design Inspiration Library  
**Suggested GitHub repository:** `design-inspiration-library`  
**Primary implementation agent:** Devin.ai  
**Language:** English for technical files, documentation and agent instructions; preserve original research content and quotations in their source language.  
**Status:** Ready for implementation

---

## 1. Executive Summary

Build a reusable, GitHub-based **Design Inspiration Library** that allows Devin.ai and other AI coding agents to use two existing Deep Research reports as a source of visual inspiration, interaction design patterns, UX principles and creative direction when developing future software projects.

The two reports cover:

1. **Interactive Learning & Beautiful Web Experiences** — visually compelling interactive websites, educational experiences, storytelling, animations, creative interfaces and exploratory learning environments.
2. **Beyond Dashboards** — alternatives to traditional dashboards, innovative information visualization, narrative interfaces, exploratory data experiences, relationship-driven interfaces and new approaches to visual information systems.

The goal is **not** to build a complex research management platform.

The goal is to transform these reports into a practical, curated and reusable **design intelligence resource** that helps Devin create more original, sophisticated and appropriate user experiences.

The library must support an end-to-end workflow:

**New project idea → Project analysis → Relevant design inspiration → Visual concepts → User approval → Implementation**

The user should not need to manually explain or re-upload the two research reports for every new project.

---

## 2. Problem Statement

AI coding agents can build functional software quickly, but often default to generic interface patterns:

- Conventional SaaS dashboards.
- Repetitive card layouts.
- Standard navigation sidebars.
- Generic component-library aesthetics.
- Uninspired data tables and KPI widgets.
- Limited animation and interaction design.
- Visually attractive but conceptually shallow experiences.

The user has already invested in extensive research into innovative web design, visual storytelling, interactive learning and next-generation information interfaces.

However, this knowledge currently exists in standalone research reports and is not systematically available during software development.

We need a lightweight system that makes this research actionable for future projects.

---

## 3. Product Vision

Create a persistent design inspiration resource that acts as a **creative reference library and design-direction assistant** for AI development agents.

The library should help an agent answer:

- What kind of visual experience is appropriate for this project?
- Which existing websites or design projects offer relevant inspiration?
- What makes those references visually or interactively exceptional?
- Which design patterns can be adapted?
- How can multiple inspirations be combined into an original interface?
- Which patterns would be inappropriate for the target users?
- How should the selected visual direction influence implementation?

The library must promote **original, research-informed design**, not copying existing websites.

---

## 4. Primary Users

### 4.1 Product Owner

The product owner provides new project ideas and wants software that is both functional and exceptionally well designed.

The product owner should be able to say:

> Build an interactive educational website about artificial intelligence. Use my Design Inspiration Library to identify suitable visual and interaction concepts. Show me three design directions before implementing the full application.

### 4.2 Devin.ai

Devin uses the library to:

- Discover relevant references.
- Analyze design patterns.
- Generate creative directions.
- Build visual prototypes.
- Implement approved designs.
- Explain which inspirations influenced the result.

### 4.3 Other AI Coding Agents

The library must be usable by other agents through ordinary repository files and documentation.

Avoid vendor-specific data formats and proprietary storage dependencies.

---

## 5. Input Materials

The user will provide two completed Deep Research reports.

Supported input formats:

- Markdown (`.md`) — preferred.
- PDF (`.pdf`).
- Plain text (`.txt`).
- HTML or DOCX where practical.

### Research Report A

**Topic:** Interactive Learning & Beautiful Web Experiences

Expected themes may include:

- Interactive educational websites.
- Scrollytelling.
- Editorial storytelling.
- Immersive digital experiences.
- Motion design.
- Interactive illustrations.
- Creative navigation.
- Exploratory learning.
- Playful interactions.
- Data storytelling.

### Research Report B

**Topic:** Beyond Dashboards

Expected themes may include:

- Alternatives to traditional BI dashboards.
- Exploratory information systems.
- Visual analytics.
- Spatial and relationship-based interfaces.
- Narrative data interfaces.
- Interactive knowledge maps.
- Adaptive information presentation.
- AI-native information experiences.
- Innovative data visualization.

**Critical instruction:** Do not assume the reports contain specific references, findings or URLs until they have been parsed and verified.

Do not invent references, research findings, screenshots or design characteristics.

---

## 6. Scope

### In Scope — MVP

1. Create a private GitHub repository.
2. Import and preserve both research reports.
3. Extract relevant design references and projects.
4. Build a curated reference catalog.
5. Identify reusable design and interaction patterns.
6. Organize patterns into practical categories.
7. Create a machine-readable design knowledge structure.
8. Create reusable agent instructions and skills.
9. Implement a lightweight search and recommendation mechanism.
10. Create a design-direction workflow for future projects.
11. Provide documentation and example prompts.
12. Test the library against representative project ideas.
13. Provide a clear method for updating the library with future research.

### Out of Scope — MVP

- Building a dedicated SaaS application.
- Developing a custom research dashboard.
- Creating a vector database.
- Implementing a complex RAG system.
- Building an MCP server.
- Training or fine-tuning an AI model.
- Building the user's future software projects.
- Automatically reproducing third-party website designs.
- Scraping copyrighted content without appropriate rights.

The MVP should be primarily **repository-based and file-driven**.

---

## 7. GitHub Repository Requirements

Create the following initial structure:

```text
design-inspiration-library/
│
├── README.md
├── AGENTS.md
│
├── research/
│   ├── original/
│   │   ├── interactive-learning/
│   │   └── beyond-dashboards/
│   └── processed/
│       ├── interactive-learning.md
│       └── beyond-dashboards.md
│
├── references/
│   ├── index.yaml
│   └── entries/
│
├── patterns/
│   ├── index.md
│   ├── visual-storytelling/
│   ├── interactive-learning/
│   ├── exploratory-interfaces/
│   ├── information-visualization/
│   ├── spatial-interfaces/
│   ├── motion-design/
│   └── navigation-and-layout/
│
├── principles/
│   ├── visual-design.md
│   ├── interaction-design.md
│   ├── information-design.md
│   ├── accessibility.md
│   └── anti-patterns.md
│
├── workflows/
│   ├── new-project-design.md
│   ├── inspiration-selection.md
│   ├── design-direction-review.md
│   └── implementation-handoff.md
│
├── skills/
│   └── design-inspiration/
│       └── SKILL.md
│
├── templates/
│   ├── project-design-brief.md
│   ├── inspiration-shortlist.md
│   ├── design-directions.md
│   └── design-decision.md
│
├── examples/
│   └── example-project/
│
├── scripts/
│   ├── validate_library.py
│   └── search_library.py
│
└── docs/
    ├── setup.md
    ├── devin-integration.md
    ├── adding-research.md
    └── usage-examples.md
```

The repository must be readable and usable without running a server.

The exact folder structure may be improved if necessary, but changes must be documented and justified.

---

## 8. Research Processing Requirements

### 8.1 Preserve Originals

Store the original reports without modifying their content.

If PDFs are supplied, retain the PDFs and generate readable Markdown extracts.

Preserve:

- Source links.
- Titles.
- Authors, where available.
- Publication dates, where available.
- Relevant descriptions.
- Research context.
- Important caveats.

### 8.2 Extract Design References

Identify concrete websites, projects, studios, visual experiments and interactive experiences mentioned in the reports.

For each relevant reference, create a structured entry.

Required fields:

```yaml
id: REF-001
title: "Reference title"
url: "https://example.com"
source_reports:
  - interactive-learning

categories:
  - interactive-storytelling
  - educational-experience

visual_characteristics:
  - editorial-typography
  - immersive-layout

interaction_patterns:
  - scroll-driven-animation
  - progressive-disclosure

description: >
  Concise description of the experience.

why_it_works: >
  Explanation of the relevant design qualities.

best_suited_for:
  - educational-websites
  - interactive-explainers

limitations:
  - potential-performance-cost
  - accessibility-considerations

original_source_reference: "..."
verification_status: "verified"
last_verified: "YYYY-MM-DD"
```

The example is illustrative. Actual entries must use real research content.

### 8.3 Reference Verification

For each reference:

- Check that the URL is valid when network access is available.
- Prefer direct project URLs over generic homepage URLs.
- Distinguish live projects from archived examples.
- Avoid duplicate references.
- Preserve the source report that introduced the reference.
- Clearly label uncertain information.
- Do not fabricate screenshots or visual descriptions.

If visual analysis is not possible, explicitly mark it as not visually verified.

### 8.4 Reference Prioritization

Create a curated shortlist of approximately **30–50 high-value references**, depending on the quality and scope of the supplied reports.

Do not force the target count if insufficient suitable references exist.

Prioritize:

- Distinctive visual direction.
- Interaction originality.
- Educational or explanatory value.
- Information clarity.
- Transferability to future software projects.
- Accessibility.
- Practical implementation feasibility.

Avoid selecting references solely because they look visually impressive.

---

## 9. Design Pattern Library

Convert the strongest references into reusable design patterns.

Patterns should describe **generalizable design ideas**, not copies of individual websites.

Each pattern must include:

1. Pattern name.
2. Short description.
3. User experience goal.
4. Visual characteristics.
5. Interaction behavior.
6. Suitable project types.
7. Unsuitable project types.
8. Implementation considerations.
9. Accessibility and performance considerations.
10. Supporting references.
11. Source report provenance.

Examples of possible pattern categories:

- Narrative scrollytelling.
- Interactive timelines.
- Guided exploration.
- Spatial navigation.
- Relationship maps.
- Progressive disclosure.
- Interactive simulations.
- Layered information exploration.
- Editorial visual storytelling.
- Animated transitions between information states.
- Interactive comparisons.
- Contextual information overlays.

These are candidate categories, not claims about the contents of the reports.

Aim for approximately **15–25 meaningful patterns**, subject to available evidence.

---

## 10. Design Principles

Extract a practical collection of reusable design principles.

Principles should be concise, actionable and suitable for AI coding agents.

Examples of the desired format:

**Principle: Interaction should reveal meaning**

Use interaction to help users discover relationships, understand changes or explore information.

Avoid animations that do not support comprehension or the intended experience.

**Principle: Visual originality must serve usability**

Unconventional navigation and visual layouts are appropriate only when they support the target users and tasks.

**Principle: Do not default to dashboards**

Consider narrative, spatial, exploratory and relationship-based alternatives before choosing conventional dashboard layouts.

However, dashboards, tables and charts remain valid when they best serve the task.

The final principles must be derived from the supplied research and clearly distinguished from general implementation guidance.

---

## 11. Core Feature: Design Direction Generation

This is the most important functional requirement.

When Devin receives a new project idea, the library must guide it through a structured design discovery process.

### Step 1 — Analyze the Project

Determine:

- Project purpose.
- Target audience.
- Main user tasks.
- Content and data types.
- Desired emotional tone.
- Level of interaction.
- Technical constraints.
- Accessibility requirements.

Ask the product owner for clarification only when essential information is missing.

### Step 2 — Retrieve Relevant Inspiration

Search the Design Inspiration Library.

Select **3–5 highly relevant references**.

For each reference, explain:

- Why it is relevant.
- Which aspects should influence the project.
- Which aspects should not be adopted.
- What would need to change for the new context.

### Step 3 — Generate Three Design Directions

Produce three genuinely different directions.

Each direction must include:

- A descriptive name.
- A concise design concept.
- Intended user experience.
- Relevant reference links.
- Visual design language.
- Typography direction.
- Color direction.
- Layout and navigation concept.
- Motion and interaction approach.
- Information presentation approach.
- Accessibility considerations.
- Technical feasibility.
- Main risks.

The directions must be meaningfully distinct, not merely three color variations.

### Step 4 — Recommend a Direction

Compare the three concepts against the project requirements.

Recommend one direction and explain why.

The product owner makes the final selection.

### Step 5 — Create a Visual Prototype

After direction selection, build a small visual prototype.

The prototype should demonstrate the defining aspects of the selected direction.

For example:

- Homepage or main screen.
- Primary interaction.
- Representative information visualization.
- Motion behavior.
- Responsive behavior.

### Step 6 — Obtain Approval

Do not begin full application implementation until the product owner approves the visual direction or explicitly authorizes autonomous continuation.

### Step 7 — Implement the Project

Once approved, use the selected direction as a reference for the complete application.

Maintain consistency between:

- Initial design concept.
- Visual prototype.
- Components.
- Interaction behavior.
- Final product.

---

## 12. Devin Agent Skill

Create a reusable agent skill at:

`skills/design-inspiration/SKILL.md`

The skill must teach an AI coding agent how to use the repository.

It must include:

- When to activate the skill.
- How to analyze a project brief.
- How to search the reference catalog.
- How to select suitable patterns.
- How to generate alternative design directions.
- How to avoid generic UI defaults.
- How to document design decisions.
- How to move from design approval to implementation.

The skill should explicitly instruct:

> Before designing the interface for a new project, consult the Design Inspiration Library and identify relevant references and patterns. Generate multiple original design directions, explain the rationale behind each, and obtain approval before full implementation unless the user explicitly requests otherwise.

Do not assume that the existence of `SKILL.md` alone guarantees automatic activation.

Also create `AGENTS.md` and integration instructions for Devin.

Verify the currently supported Devin skill or repository-instruction mechanism and document the exact configuration required.

If Devin does not automatically load the skill, provide a reliable explicit invocation method.

---

## 13. Search and Recommendation

Implement a lightweight local search mechanism.

A script such as:

```bash
python scripts/search_library.py \
  --query "interactive educational timeline"
```

should return relevant references and patterns.

Search should consider:

- Titles.
- Descriptions.
- Categories.
- Keywords.
- Suitable project types.
- Visual characteristics.
- Interaction patterns.

A simple Python implementation using structured YAML/Markdown and keyword scoring is sufficient for the MVP.

Avoid unnecessary infrastructure.

Search results should contain stable IDs and file paths so agents can open the original entries.

---

## 14. Reusability Across Projects

The library must be maintained as a **separate GitHub repository**.

Do not embed its complete content into every application repository.

Provide a documented integration method that allows Devin to access it when starting a new project.

Preferred options:

1. Grant Devin access to the shared repository and explicitly reference it in the project task.
2. Use repository-level agent instructions pointing to the library.
3. If appropriate, use a Git submodule or another lightweight synchronization method.

Choose the simplest approach compatible with the actual Devin environment.

Do not introduce a service dependency unless necessary.

Each project should store its own design decisions and selected inspiration references, but the central library should remain shared.

---

## 15. Future Project Prompt Template

Create a reusable prompt template for new projects.

Example:

> Build the following project: [PROJECT IDEA].
>
> Before implementation, consult my Design Inspiration Library.
>
> Analyze the project and identify the most relevant visual design references and interaction patterns from both research reports.
>
> Propose three distinctive design directions.
>
> Explain the visual language, UX concept, interaction patterns and supporting references for each.
>
> Recommend the strongest direction.
>
> Create a visual prototype after I select a direction.
>
> Do not start full implementation until the design is approved.
>
> The final experience should feel original, polished, intuitive and appropriate for the project, rather than resembling a generic SaaS template.

Save this template in the repository documentation.

---

## 16. Quality Requirements

### Visual Design

The system should encourage:

- Strong visual hierarchy.
- Intentional typography.
- Thoughtful color systems.
- Distinctive layouts.
- Meaningful motion.
- Original interaction concepts.
- Responsive design.
- High-quality information presentation.

### Usability

The system must not encourage visual complexity at the expense of usability.

### Accessibility

Recommended designs must consider:

- Keyboard interaction.
- Color contrast.
- Reduced-motion preferences.
- Screen reader compatibility.
- Responsive behavior.
- Clear information hierarchy.

### Performance

Avoid unnecessary 3D rendering, large animation frameworks or expensive effects when they do not materially improve the experience.

### Originality

Use references as inspiration.

Do not reproduce protected artwork, proprietary assets, distinctive layouts or entire websites without appropriate permission.

---

## 17. Acceptance Criteria

The MVP is complete when:

- [ ] A private GitHub repository has been created.
- [ ] Both research reports are preserved.
- [ ] Readable and searchable versions of the reports exist.
- [ ] Relevant references have been extracted.
- [ ] References have structured metadata and source provenance.
- [ ] A curated high-value reference shortlist exists.
- [ ] Reusable design patterns have been documented.
- [ ] Practical design principles have been documented.
- [ ] A working search mechanism exists.
- [ ] `AGENTS.md` is present.
- [ ] A reusable design inspiration skill exists.
- [ ] Devin integration instructions have been tested.
- [ ] Three example project briefs have been evaluated.
- [ ] Each example produces three distinct, research-informed design directions.
- [ ] Design recommendations link back to real references.
- [ ] The library can be reused in another project without re-uploading the reports.
- [ ] The repository includes clear setup and maintenance documentation.

---

## 18. Validation Scenarios

Test the system with three hypothetical projects.

### Scenario A — Interactive Learning

**Project:** An interactive website explaining the history of artificial intelligence.

Expected outcome:

The library should identify relevant educational storytelling, timeline, exploration and interaction patterns.

### Scenario B — Beyond Dashboards

**Project:** A modern project portfolio management application.

Expected outcome:

The library should consider alternatives to conventional KPI dashboards, including relationship-driven and exploratory interfaces where appropriate.

### Scenario C — Hybrid Experience

**Project:** An interactive platform explaining global technological trends.

Expected outcome:

The library should combine educational storytelling with sophisticated information exploration.

For each scenario, generate three design directions and record which references and patterns were selected.

The test should demonstrate actual research use, not merely generic design descriptions.

---

## 19. Implementation Phases

### Phase 1 — Repository Foundation

- Create private GitHub repository.
- Establish directory structure.
- Import research reports.
- Implement schemas and documentation.

### Phase 2 — Research Curation

- Parse reports.
- Extract references.
- Verify available links.
- Deduplicate references.
- Build curated catalog.
- Extract reusable patterns and principles.

### Phase 3 — Agent Integration

- Implement search script.
- Create agent skill.
- Create `AGENTS.md`.
- Configure Devin access.
- Document new-project workflow.

### Phase 4 — Validation

- Run three example scenarios.
- Check relevance and diversity of recommendations.
- Verify traceability to research sources.
- Improve instructions based on observed results.
- Deliver repository and usage guide.

---

## 20. Final Deliverables

Devin must deliver:

1. **GitHub repository URL** — containing the complete Design Inspiration Library.
2. **Research archive** — original and processed reports.
3. **Reference catalog** — curated, structured design inspiration.
4. **Pattern library** — reusable visual and interaction concepts.
5. **Design principles** — actionable guidance.
6. **Agent skill** — reusable instructions for Devin and other agents.
7. **Search mechanism** — simple and functional.
8. **Future project prompt template** — ready to copy into Devin.
9. **Validation examples** — three realistic project scenarios.
10. **Setup and maintenance guide** — explaining how to use and extend the library.

---

## 21. Implementation Instructions for Devin

You are responsible for building the complete MVP described in this PRD.

The user will supply two Deep Research reports.

**Start by:**

1. Inspecting the supplied reports and confirming they are readable.
2. Identifying their structure and relevant reference material.
3. Checking GitHub access and repository permissions.
4. Creating the private repository.
5. Building the library according to the requirements.
6. Implementing and testing the agent integration.
7. Demonstrating the workflow with the three validation scenarios.

Use reasonable implementation decisions without requesting approval for minor technical details.

Ask for user input when required for permissions, credentials, unavailable source material or significant product decisions.

Do not add unnecessary infrastructure.

**The primary success criterion is simple:**

When the user starts a new software project with Devin, Devin should be able to use the two research reports to propose visually compelling, original and contextually appropriate design directions — without requiring the user to manually analyze or re-upload those reports.

The library should become a persistent creative foundation for future software development.

**Build the smallest reliable system that achieves this outcome.**