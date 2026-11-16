---
id: pat-system-anatomy-explorer
name: System Anatomy Explorer
group: learning-by-manipulation
source_reports:
- interactive-learning
provenance: derived from Report 18 (Transformer/Diffusion/CNN Explainer – the real architecture is the interface)
supporting_references:
- ref-polo-club-explainers
suitable_for:
- AI and software architecture explainers
- developer tools
- process documentation
unsuitable_for:
- audiences who need outcomes rather than mechanisms
keywords:
- ai history
- attention
- cnn
- diffusion
- llm
- transformer
---

# System Anatomy Explorer

## Description
The actual structure of a system (architecture, pipeline, organisation) is the navigation surface; users expand components and see real intermediate values.

## UX goal
Make a complex system's internal structure understandable and inspectable.

## Visual characteristics
Architecture diagram as the main canvas, expandable blocks, live values on edges.

## Interaction behavior
Enter own input, expand/collapse components, follow data through the pipeline.

## Suitable project types
- AI and software architecture explainers
- developer tools
- process documentation

## Unsuitable project types
- audiences who need outcomes rather than mechanisms

## Implementation considerations
Derive the diagram from a data description of the system so it stays accurate.

## Accessibility and performance
Provide an outline/tree view equivalent of the diagram.

## Anti-patterns and risks
- simplified fake architecture that contradicts the real one

## Supporting references
- `ref-polo-club-explainers` – [Polo Club explainers (Transformer, Diffusion, CNN Explainer)](https://poloclub.github.io/transformer-explainer/) (`references/entries/ref-polo-club-explainers.yaml`)

## Source provenance
derived from Report 18 (Transformer/Diffusion/CNN Explainer – the real architecture is the interface)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
