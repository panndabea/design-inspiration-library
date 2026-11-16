---
id: pat-multimodal-representation
name: Multimodal Representation
group: ai-native
source_reports:
- beyond-dashboards
- interactive-learning
provenance: Report 19 pattern table ("Multimodal Representation"), manifesto "Design multimodally"; Umwelt; Report
  18 Seeing Circles, Sines and Signals (visual + audio)
supporting_references:
- ref-jezzamon-fourier
- ref-mit-umwelt
- ref-seeing-circles-sines-signals
suitable_for:
- public-sector and education sites
- accessible data products
- mobile/ambient contexts
unsuitable_for:
- projects without budget for the extra renderers (high effort per report)
keywords:
- accessibility
- audio
- blind
- drawing
- dsp
- fourier
- multimodal
- playful
- screen reader
- signal processing
- sonification
- sound
---

# Multimodal Representation

## Description
One semantic data model drives several equal renderers – visual, textual, auditory.

## UX goal
Inclusive and context-adaptive understanding.

## Visual characteristics
Visual and textual views side by side; optional sonification controls.

## Interaction behavior
Switch or combine modalities; navigate data structure by keyboard.

## Suitable project types
- public-sector and education sites
- accessible data products
- mobile/ambient contexts

## Unsuitable project types
- projects without budget for the extra renderers (high effort per report)

## Implementation considerations
Separate semantic model from renderers; generate text descriptions from the same spec.

## Accessibility and performance
This pattern is itself an accessibility strategy, not an add-on alt text.

## Anti-patterns and risks
- accessibility as an afterthought alt text (manifesto anti-pattern)

## Supporting references
- `ref-jezzamon-fourier` – [An Interactive Introduction to Fourier Transforms](https://jezzamon.com/fourier/) (`references/entries/ref-jezzamon-fourier.yaml`)
- `ref-mit-umwelt` – [Umwelt](https://vis.mit.edu/pubs/umwelt/) (`references/entries/ref-mit-umwelt.yaml`)
- `ref-seeing-circles-sines-signals` – [Seeing Circles, Sines and Signals](https://jackschaedler.github.io/circles-sines-signals/) (`references/entries/ref-seeing-circles-sines-signals.yaml`)

## Source provenance
Report 19 pattern table ("Multimodal Representation"), manifesto "Design multimodally"; Umwelt; Report 18 Seeing Circles, Sines and Signals (visual + audio)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
