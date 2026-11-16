---
id: pat-visual-provenance
name: Visual Provenance & Fact/Inference Separation
group: ai-native
source_reports:
- beyond-dashboards
- interactive-learning
provenance: Report 19 pattern table ("Visual Provenance"), manifesto "Make reasoning inspectable", "Make evidence
  addressable", "Separate fact from inference"; WaitGPT, StoryFacets, DataNarrative; Report 18 Epoch Lives primary
  sources
supporting_references:
- ref-datanarrative
- ref-epoch-lives
- ref-owid-grapher
- ref-storyfacets
- ref-waitgpt
suitable_for:
- AI-generated reports
- regulated decisions
- research
- history with sources
unsuitable_for:
- none in principle – scale the depth to the stakes
keywords:
- agents
- audit
- chart map table
- chat
- code
- conversational analytics
- data story
- generation
- global data
- history
- llm
- maps
- primary sources
- provenance
- scrollytelling
---

# Visual Provenance & Fact/Inference Separation

## Description
Every statement carries an anchor to its data or source, and the analysis path is visible; measured values, model outputs and hypotheses are visually distinguished.

## UX goal
Trust and auditability, especially for AI-generated content.

## Visual characteristics
Consistent markers for fact / model / hypothesis; source chips; expandable analysis steps.

## Interaction behavior
Click statement → see evidence and steps; edit steps where possible.

## Suitable project types
- AI-generated reports
- regulated decisions
- research
- history with sources

## Unsuitable project types
- none in principle – scale the depth to the stakes

## Implementation considerations
Store provenance with each generated object; never render generated text without its evidence links.

## Accessibility and performance
Markers must not rely on colour alone.

## Anti-patterns and risks
- "AI says…" without origin
- generated interpretation treated as fact

## Supporting references
- `ref-datanarrative` – [DataNarrative (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.1073/) (`references/entries/ref-datanarrative.yaml`)
- `ref-epoch-lives` – [Epoch Lives](https://pastlives.site/) (`references/entries/ref-epoch-lives.yaml`)
- `ref-owid-grapher` – [Our World in Data Grapher](https://ourworldindata.org/grapher) (`references/entries/ref-owid-grapher.yaml`)
- `ref-storyfacets` – [StoryFacets](https://vis.khoury.northeastern.edu/pubs/Park2022StoryfacetsDesignStudy/) (`references/entries/ref-storyfacets.yaml`)
- `ref-waitgpt` – [WaitGPT](https://arxiv.org/abs/2408.01703) (`references/entries/ref-waitgpt.yaml`)

## Source provenance
Report 19 pattern table ("Visual Provenance"), manifesto "Make reasoning inspectable", "Make evidence addressable", "Separate fact from inference"; WaitGPT, StoryFacets, DataNarrative; Report 18 Epoch Lives primary sources

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
