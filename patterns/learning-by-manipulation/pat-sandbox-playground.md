---
id: pat-sandbox-playground
name: Sandbox Playground
group: learning-by-manipulation
source_reports:
- interactive-learning
provenance: derived from Report 18 (TensorFlow Playground, GAN Lab, Red Blob Games, Mathigon Polypad, Seeing Theory
  experiments)
supporting_references:
- ref-gan-lab
- ref-mathigon
- ref-polo-club-explainers
- ref-red-blob-games
- ref-seeing-theory
- ref-tensorflow-playground
suitable_for:
- AI/ML education
- configuration-heavy products
- simulation tools
unsuitable_for:
- first contact with a topic without guidance
- audiences that need a single answer
keywords:
- a-star
- ai history
- attention
- bayes
- cnn
- configuration
- course
- d3
- diffusion
- fractals
- games
- gan
- generative ai
- geometry
- grids
---

# Sandbox Playground

## Description
An open environment where users configure a live model and observe its behaviour in real time.

## UX goal
Support experimentation and self-directed discovery after the basics are understood.

## Visual characteristics
Configuration panel + large live output; clear separation of inputs, process and output.

## Interaction behavior
Play/pause/step, reset, presets that encode interesting starting points.

## Suitable project types
- AI/ML education
- configuration-heavy products
- simulation tools

## Unsuitable project types
- first contact with a topic without guidance
- audiences that need a single answer

## Implementation considerations
Provide curated presets; run heavy computation in a Web Worker; start paused.

## Accessibility and performance
Keyboard-accessible controls and text readouts of key outputs; cap frame rate and stop when tab is hidden.

## Anti-patterns and risks
- blank canvas without presets
- auto-playing heavy computation on load

## Supporting references
- `ref-gan-lab` – [GAN Lab](https://poloclub.github.io/ganlab/) (`references/entries/ref-gan-lab.yaml`)
- `ref-mathigon` – [Mathigon](https://mathigon.org/) (`references/entries/ref-mathigon.yaml`)
- `ref-polo-club-explainers` – [Polo Club explainers (Transformer, Diffusion, CNN Explainer)](https://poloclub.github.io/transformer-explainer/) (`references/entries/ref-polo-club-explainers.yaml`)
- `ref-red-blob-games` – [Red Blob Games](https://www.redblobgames.com/) (`references/entries/ref-red-blob-games.yaml`)
- `ref-seeing-theory` – [Seeing Theory](https://seeing-theory.brown.edu/) (`references/entries/ref-seeing-theory.yaml`)
- `ref-tensorflow-playground` – [TensorFlow Playground](https://playground.tensorflow.org/) (`references/entries/ref-tensorflow-playground.yaml`)

## Source provenance
derived from Report 18 (TensorFlow Playground, GAN Lab, Red Blob Games, Mathigon Polypad, Seeing Theory experiments)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
