---
id: pat-single-mechanism-explorable
name: Single-Mechanism Explorable
group: learning-by-manipulation
source_reports:
- interactive-learning
provenance: derived from Report 18 (finding that the best works pick one mechanism and make it manipulable; Setosa
  "interactive = intuitive"; Complexity Explorables one system + one interaction)
supporting_references:
- ref-ciechanowski-explorable-essays
- ref-complexity-explorables
- ref-distill
- ref-explorable-explanations-hub
- ref-jezzamon-fourier
- ref-misread-tsne
- ref-mlu-explain
- ref-red-blob-games
- ref-setosa-explained-visually
- ref-visualizing-algorithms
suitable_for:
- educational explainers
- concept pages in documentation
- product feature explanations
- onboarding
unsuitable_for:
- overview pages that must cover many topics
- transactional workflows
- content without an underlying model
keywords:
- 3d
- a-star
- algorithms
- animation
- archive
- benchmark
- complex systems
- d3
- design patterns
- dimensionality reduction
- directory
- discovery
- drawing
- dynamics
- editorial
---

# Single-Mechanism Explorable

## Description
A page or section is built around exactly one mechanism (an algorithm, a physical law, a model) and gives the user one primary control that changes it.

## UX goal
Build intuition by letting the user cause the effect instead of reading about it.

## Visual characteristics
One dominant figure, minimal chrome, labels attached directly to the moving parts, calm palette so change is the loudest signal.

## Interaction behavior
One primary control (slider, drag handle, toggle) with immediate feedback; optional secondary controls appear only after the first insight.

## Suitable project types
- educational explainers
- concept pages in documentation
- product feature explanations
- onboarding

## Unsuitable project types
- overview pages that must cover many topics
- transactional workflows
- content without an underlying model

## Implementation considerations
Model the mechanism as a pure function of its inputs; render with SVG or Canvas; debounce expensive recomputation; keep the default state meaningful so the page works without interaction.

## Accessibility and performance
Every control must be keyboard operable with visible focus and an aria-live text summary of the result; avoid continuous animation by default; respect prefers-reduced-motion.

## Anti-patterns and risks
- many unrelated sliders on one figure
- interaction that does not change the meaning
- hidden gestures as the only input

## Supporting references
- `ref-ciechanowski-explorable-essays` – [Bartosz Ciechanowski – explorable essays](https://ciechanow.ski/) (`references/entries/ref-ciechanowski-explorable-essays.yaml`)
- `ref-complexity-explorables` – [Complexity Explorables](https://complexity-explorables.org/) (`references/entries/ref-complexity-explorables.yaml`)
- `ref-distill` – [Distill](https://distill.pub/) (`references/entries/ref-distill.yaml`)
- `ref-explorable-explanations-hub` – [Explorable Explanations (directory)](https://explorabl.es/) (`references/entries/ref-explorable-explanations-hub.yaml`)
- `ref-jezzamon-fourier` – [An Interactive Introduction to Fourier Transforms](https://jezzamon.com/fourier/) (`references/entries/ref-jezzamon-fourier.yaml`)
- `ref-misread-tsne` – [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) (`references/entries/ref-misread-tsne.yaml`)
- `ref-mlu-explain` – [MLU-Explain](https://mlu-explain.github.io/) (`references/entries/ref-mlu-explain.yaml`)
- `ref-red-blob-games` – [Red Blob Games](https://www.redblobgames.com/) (`references/entries/ref-red-blob-games.yaml`)
- `ref-setosa-explained-visually` – [Explained Visually (Setosa)](https://setosa.io/ev/) (`references/entries/ref-setosa-explained-visually.yaml`)
- `ref-visualizing-algorithms` – [Visualizing Algorithms](https://bost.ocks.org/mike/algorithms/) (`references/entries/ref-visualizing-algorithms.yaml`)

## Source provenance
derived from Report 18 (finding that the best works pick one mechanism and make it manipulable; Setosa "interactive = intuitive"; Complexity Explorables one system + one interaction)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
