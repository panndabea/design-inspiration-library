---
id: pat-inline-reactive-figure
name: Inline Reactive Figure
group: learning-by-manipulation
source_reports:
- beyond-dashboards
- interactive-learning
provenance: derived from Report 18 (Distill "native to the web", editorial-minimalist design language of MLU-Explain/Distill/Seeing
  Theory/Setosa) and Report 19 (Pluto text ↔ chart linking)
supporting_references:
- ref-ciechanowski-explorable-essays
- ref-communicating-interactive-articles
- ref-distill
- ref-immersive-linear-algebra
- ref-mit-pluto
- ref-mlu-explain
- ref-pair-explorables
- ref-seeing-circles-sines-signals
- ref-setosa-explained-visually
suitable_for:
- articles
- documentation
- research communication
- reports
unsuitable_for:
- dense operational tools
- mobile-only micro interactions where text width is very small
keywords:
- 3d
- agency
- ai
- ai authoring
- archive
- audio
- benchmark
- design guidance
- dsp
- editorial
- eigenvectors
- engineering
- essay
- explorables
- fourier
---

# Inline Reactive Figure

## Description
Figures live inside the reading flow and react to the text around them – hovering or selecting a term highlights the matching part of the figure and vice versa.

## UX goal
Keep argument and evidence in the same visual field so the reader never has to jump between text and illustration.

## Visual characteristics
Editorial column with figures at text width or slightly wider; shared colour coding between words in the text and marks in the figure.

## Interaction behavior
Linked highlighting (text ↔ figure), small inline controls embedded in sentences, figures update as the reader progresses.

## Suitable project types
- articles
- documentation
- research communication
- reports

## Unsuitable project types
- dense operational tools
- mobile-only micro interactions where text width is very small

## Implementation considerations
Use a shared state store between prose components and figures; define a small colour/term vocabulary up front.

## Accessibility and performance
Colour coding must be paired with text/shape cues; linked highlights need focusable equivalents; lazy-load figures below the fold.

## Anti-patterns and risks
- decorative hero animation unrelated to the text
- figures that only work on hover

## Supporting references
- `ref-ciechanowski-explorable-essays` – [Bartosz Ciechanowski – explorable essays](https://ciechanow.ski/) (`references/entries/ref-ciechanowski-explorable-essays.yaml`)
- `ref-communicating-interactive-articles` – [Communicating with Interactive Articles](https://distill.pub/2020/communicating-with-interactive-articles/) (`references/entries/ref-communicating-interactive-articles.yaml`)
- `ref-distill` – [Distill](https://distill.pub/) (`references/entries/ref-distill.yaml`)
- `ref-immersive-linear-algebra` – [Immersive Linear Algebra](https://immersivemath.com/ila/) (`references/entries/ref-immersive-linear-algebra.yaml`)
- `ref-mit-pluto` – [Pluto](https://vis.mit.edu/pubs/pluto/) (`references/entries/ref-mit-pluto.yaml`)
- `ref-mlu-explain` – [MLU-Explain](https://mlu-explain.github.io/) (`references/entries/ref-mlu-explain.yaml`)
- `ref-pair-explorables` – [Google PAIR AI Explorables](https://pair.withgoogle.com/explorables/) (`references/entries/ref-pair-explorables.yaml`)
- `ref-seeing-circles-sines-signals` – [Seeing Circles, Sines and Signals](https://jackschaedler.github.io/circles-sines-signals/) (`references/entries/ref-seeing-circles-sines-signals.yaml`)
- `ref-setosa-explained-visually` – [Explained Visually (Setosa)](https://setosa.io/ev/) (`references/entries/ref-setosa-explained-visually.yaml`)

## Source provenance
derived from Report 18 (Distill "native to the web", editorial-minimalist design language of MLU-Explain/Distill/Seeing Theory/Setosa) and Report 19 (Pluto text ↔ chart linking)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
