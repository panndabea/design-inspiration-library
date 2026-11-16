---
id: pat-scroll-driven-construction
name: Scroll-Driven Construction
group: narrative
source_reports:
- beyond-dashboards
- interactive-learning
provenance: derived from Report 18 (R2D3 builds a decision tree while scrolling; Glocal Climate Change; Epoch Lives;
  The Pudding)
supporting_references:
- ref-epoch-lives
- ref-glocal-climate-change
- ref-mlu-explain
- ref-r2d3-visual-intro-ml
- ref-the-pudding
suitable_for:
- narrative explainers
- history stories
- campaign or report sites
- global-trend stories
unsuitable_for:
- tools used repeatedly
- content that users need to scan quickly
keywords:
- benchmark
- climate
- culture
- data journalism
- decision tree
- editorial
- global trends
- history
- local
- machine learning
- maps
- minimal
- music
- narrative
- personalised
---

# Scroll-Driven Construction

## Description
Scrolling advances a narrative in which the visual is constructed step by step – data points move, group and form the model or argument.

## UX goal
Turn passive reading into the experience of watching (and mentally performing) a construction.

## Visual characteristics
Sticky graphic with text steps scrolling past; transitions that preserve object identity (the same marks move rather than being replaced).

## Interaction behavior
Scroll position maps to narrative step; optional free exploration at the end.

## Suitable project types
- narrative explainers
- history stories
- campaign or report sites
- global-trend stories

## Unsuitable project types
- tools used repeatedly
- content that users need to scan quickly

## Implementation considerations
Use IntersectionObserver-based step triggers rather than scroll-jacking; keep each step's state declarative so it can be rendered without scrolling.

## Accessibility and performance
Reduced-motion users get discrete state changes; every step must also exist as readable text; avoid layout thrashing in scroll handlers.

## Anti-patterns and risks
- scroll-jacking
- motion that does not encode anything
- story that cannot be skipped

## Supporting references
- `ref-epoch-lives` – [Epoch Lives](https://pastlives.site/) (`references/entries/ref-epoch-lives.yaml`)
- `ref-glocal-climate-change` – [Glocal Climate Change](https://www.sheldon.studio/works/glocal-climate-change/) (`references/entries/ref-glocal-climate-change.yaml`)
- `ref-mlu-explain` – [MLU-Explain](https://mlu-explain.github.io/) (`references/entries/ref-mlu-explain.yaml`)
- `ref-r2d3-visual-intro-ml` – [R2D3 – A Visual Introduction to Machine Learning](https://r2d3.us/visual-intro-to-machine-learning-part-1/) (`references/entries/ref-r2d3-visual-intro-ml.yaml`)
- `ref-the-pudding` – [The Pudding](https://pudding.cool/) (`references/entries/ref-the-pudding.yaml`)

## Source provenance
derived from Report 18 (R2D3 builds a decision tree while scrolling; Glocal Climate Change; Epoch Lives; The Pudding)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
