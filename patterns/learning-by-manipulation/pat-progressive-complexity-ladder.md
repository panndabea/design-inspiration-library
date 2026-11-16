---
id: pat-progressive-complexity-ladder
name: Progressive Complexity Ladder
group: learning-by-manipulation
source_reports:
- interactive-learning
provenance: derived from Report 18 (Ciechanowski progression from simple to complex; Mathigon courses; Seeing Theory
  chapters)
supporting_references:
- ref-ciechanowski-explorable-essays
- ref-immersive-linear-algebra
- ref-mathigon
- ref-seeing-circles-sines-signals
- ref-seeing-theory
suitable_for:
- courses
- technical deep dives
- onboarding to complex products
unsuitable_for:
- reference lookups where users jump directly to a detail
keywords:
- 3d
- audio
- bayes
- course
- d3
- dsp
- engineering
- essay
- fourier
- fractals
- gold standard
- linear algebra
- manipulatives
- math
- mechanism
---

# Progressive Complexity Ladder

## Description
Content is staged as a ladder – each step adds one new variable or concept to a figure the user already understands.

## UX goal
Lower cognitive load and make expert-level topics approachable without dumbing them down.

## Visual characteristics
Repeated, recognisable figure that grows in complexity; step indicator; consistent visual vocabulary across steps.

## Interaction behavior
Next-step progression (scroll or explicit "continue"), each step unlocking one more control.

## Suitable project types
- courses
- technical deep dives
- onboarding to complex products

## Unsuitable project types
- reference lookups where users jump directly to a detail

## Implementation considerations
Plan the ladder as a list of (concept, new variable, figure state) before designing screens; allow deep links to each step.

## Accessibility and performance
Provide a table of contents and skip links; keep steps addressable by URL.

## Anti-patterns and risks
- revealing all variables at once
- steps that change the figure style so recognition is lost

## Supporting references
- `ref-ciechanowski-explorable-essays` – [Bartosz Ciechanowski – explorable essays](https://ciechanow.ski/) (`references/entries/ref-ciechanowski-explorable-essays.yaml`)
- `ref-immersive-linear-algebra` – [Immersive Linear Algebra](https://immersivemath.com/ila/) (`references/entries/ref-immersive-linear-algebra.yaml`)
- `ref-mathigon` – [Mathigon](https://mathigon.org/) (`references/entries/ref-mathigon.yaml`)
- `ref-seeing-circles-sines-signals` – [Seeing Circles, Sines and Signals](https://jackschaedler.github.io/circles-sines-signals/) (`references/entries/ref-seeing-circles-sines-signals.yaml`)
- `ref-seeing-theory` – [Seeing Theory](https://seeing-theory.brown.edu/) (`references/entries/ref-seeing-theory.yaml`)

## Source provenance
derived from Report 18 (Ciechanowski progression from simple to complex; Mathigon courses; Seeing Theory chapters)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
