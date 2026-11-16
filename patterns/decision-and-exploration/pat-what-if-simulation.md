---
id: pat-what-if-simulation
name: What-if Simulation World
group: decision-and-exploration
source_reports:
- beyond-dashboards
- interactive-learning
provenance: Report 19 pattern table ("Simulation / What-if World"), manifesto "Make uncertainty visible"; Report
  18 simulations (Complexity Explorables, LOOPY, Seeing Theory)
supporting_references:
- ref-complexity-explorables
- ref-earth-a-primer
- ref-evolution-of-trust
- ref-loopy
- ref-pair-explorables
- ref-seeing-theory
suitable_for:
- planning
- risk
- portfolio and resource decisions
- complex-systems education
unsuitable_for:
- situations without a credible model
keywords:
- ai
- app
- bayes
- causal
- complex systems
- cooperation
- d3
- drawing
- dynamics
- earth science
- epidemics
- explorables
- feedback loops
- game
- game theory
---

# What-if Simulation World

## Description
Users change assumptions and immediately see consequences, including the range of uncertainty.

## UX goal
Support planning and risk decisions by making cause, effect and uncertainty tangible.

## Visual characteristics
Assumption controls next to outcome views; uncertainty shown as bands, distributions or ensembles rather than single lines.

## Interaction behavior
Adjust parameters, save and compare scenarios, reset to baseline.

## Suitable project types
- planning
- risk
- portfolio and resource decisions
- complex-systems education

## Unsuitable project types
- situations without a credible model

## Implementation considerations
Keep the model explicit and documented; show which assumptions drive the result (sensitivity).

## Accessibility and performance
Provide numeric summaries of scenario outcomes; avoid recomputation on every pixel of slider travel.

## Anti-patterns and risks
- falsely precise forecasts
- hidden model assumptions (report risk – "Modellgläubigkeit")

## Supporting references
- `ref-complexity-explorables` – [Complexity Explorables](https://complexity-explorables.org/) (`references/entries/ref-complexity-explorables.yaml`)
- `ref-earth-a-primer` – [Earth: A Primer](https://earthprimer.com/) (`references/entries/ref-earth-a-primer.yaml`)
- `ref-evolution-of-trust` – [The Evolution of Trust](https://ncase.me/trust/) (`references/entries/ref-evolution-of-trust.yaml`)
- `ref-loopy` – [LOOPY](https://ncase.me/loopy/) (`references/entries/ref-loopy.yaml`)
- `ref-pair-explorables` – [Google PAIR AI Explorables](https://pair.withgoogle.com/explorables/) (`references/entries/ref-pair-explorables.yaml`)
- `ref-seeing-theory` – [Seeing Theory](https://seeing-theory.brown.edu/) (`references/entries/ref-seeing-theory.yaml`)

## Source provenance
Report 19 pattern table ("Simulation / What-if World"), manifesto "Make uncertainty visible"; Report 18 simulations (Complexity Explorables, LOOPY, Seeing Theory)

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
