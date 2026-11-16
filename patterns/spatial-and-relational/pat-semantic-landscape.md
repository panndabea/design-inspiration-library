---
id: pat-semantic-landscape
name: Semantic Landscape
group: spatial-and-relational
source_reports:
- beyond-dashboards
- interactive-learning
provenance: Report 19 pattern table ("Semantic Landscape"), manifesto "Use space when space means something"; references
  Laniakea, Latent Lab, Atlas of Emotions; Report 18 Map of Mathematics, Activation Atlas
supporting_references:
- ref-accurat-data-landscape-venice
- ref-activation-atlas
- ref-fathom-laniakea
- ref-map-of-mathematics
- ref-mit-latent-lab
- ref-stamen-atlas-of-emotions
suitable_for:
- knowledge bases
- archives
- research landscapes
- curricula
- strategy/trend overviews
unsuitable_for:
- small datasets
- tasks with known exact lookup criteria (use search/filters)
keywords:
- ai
- archive
- atlas
- clusters
- conceptual map
- documents
- embedding
- embeddings
- emotions
- features
- generative
- image analysis
- knowledge
- knowledge landscape
- landscape
---

# Semantic Landscape

## Description
Content items are placed in a 2D landscape so that proximity means semantic similarity; users zoom from regions to individual items.

## UX goal
Give orientation in large corpora and reveal clusters that lists hide.

## Visual characteristics
Map-like regions with labels at multiple zoom levels, density shading, landmarks.

## Interaction behavior
Pan/zoom, query to highlight regions, filter, select to open detail.

## Suitable project types
- knowledge bases
- archives
- research landscapes
- curricula
- strategy/trend overviews

## Unsuitable project types
- small datasets
- tasks with known exact lookup criteria (use search/filters)

## Implementation considerations
Compute positions offline (embeddings + projection or curated layout); label regions; keep layout stable between visits.

## Accessibility and performance
Offer an equivalent hierarchical list view; use Canvas/WebGL only for large item counts.

## Anti-patterns and risks
- arbitrary 3D worlds
- positions without meaning
- layouts that reshuffle on every load

## Supporting references
- `ref-accurat-data-landscape-venice` – [Accurat – Data Landscape Venice](https://studio.accurat.it/work/data-landscapes-venice) (`references/entries/ref-accurat-data-landscape-venice.yaml`)
- `ref-activation-atlas` – [Activation Atlas](https://distill.pub/2019/activation-atlas/) (`references/entries/ref-activation-atlas.yaml`)
- `ref-fathom-laniakea` – [Fathom – Laniakea](https://laniakea.fathom.info/) (`references/entries/ref-fathom-laniakea.yaml`)
- `ref-map-of-mathematics` – [The Map of Mathematics (Quanta Magazine)](https://mathmap.quantamagazine.org/) (`references/entries/ref-map-of-mathematics.yaml`)
- `ref-mit-latent-lab` – [MIT Latent Lab](https://www.media.mit.edu/projects/latent-lab/overview/) (`references/entries/ref-mit-latent-lab.yaml`)
- `ref-stamen-atlas-of-emotions` – [Stamen – Atlas of Emotions](https://stamen.com/data-visualization/) (`references/entries/ref-stamen-atlas-of-emotions.yaml`)

## Source provenance
Report 19 pattern table ("Semantic Landscape"), manifesto "Use space when space means something"; references Laniakea, Latent Lab, Atlas of Emotions; Report 18 Map of Mathematics, Activation Atlas

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
