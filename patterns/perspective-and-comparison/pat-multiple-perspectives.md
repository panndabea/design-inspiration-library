---
id: pat-multiple-perspectives
name: Multiple Perspectives on One Dataset
group: perspective-and-comparison
source_reports:
- beyond-dashboards
- interactive-learning
provenance: derived from Report 19 (Data Clocks – a dataset has no single correct chart; Mirador) and Report 18
  (t-SNE small multiples)
supporting_references:
- ref-fathom-mirador
- ref-misread-tsne
- ref-pudding-data-clocks
suitable_for:
- exploratory tools
- AI-generated views
- data literacy
unsuitable_for:
- audiences that need one decisive answer quickly
keywords:
- clocks
- dimensionality reduction
- exploration
- generative
- high-dimensional
- open source
- parameters
- patterns
- perspectives
- same data
- small multiples
- t-sne
---

# Multiple Perspectives on One Dataset

## Description
The same data is offered through several visual rules or encodings, each answering a different question.

## UX goal
Prevent one chart from silently framing the interpretation.

## Visual characteristics
Small multiples or switchable lenses with shared legend.

## Interaction behavior
Switch or compare lenses; each lens labelled by the question it answers.

## Suitable project types
- exploratory tools
- AI-generated views
- data literacy

## Unsuitable project types
- audiences that need one decisive answer quickly

## Implementation considerations
Define lenses as declarative specs over one data model.

## Accessibility and performance
Each lens needs a textual takeaway.

## Anti-patterns and risks
- many arbitrary chart types without stated purpose

## Supporting references
- `ref-fathom-mirador` – [Mirador](https://www.fathom.info/mirador/) (`references/entries/ref-fathom-mirador.yaml`)
- `ref-misread-tsne` – [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) (`references/entries/ref-misread-tsne.yaml`)
- `ref-pudding-data-clocks` – [Data Clocks](https://pudding.cool/projects/clocks/) (`references/entries/ref-pudding-data-clocks.yaml`)

## Source provenance
derived from Report 19 (Data Clocks – a dataset has no single correct chart; Mirador) and Report 18 (t-SNE small multiples)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
