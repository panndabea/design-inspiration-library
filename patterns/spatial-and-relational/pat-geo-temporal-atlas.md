---
id: pat-geo-temporal-atlas
name: Geo-Temporal Atlas
group: spatial-and-relational
source_reports:
- beyond-dashboards
- interactive-learning
provenance: derived from Report 18 (Erask 3D globe with time reference; Epoch Lives maps and primary sources); Report
  19 "Situation Map"
supporting_references:
- ref-epoch-lives
- ref-erask
suitable_for:
- history sites
- global trends
- regional comparisons
unsuitable_for:
- topics where geography is irrelevant (report warns geography can gain irrelevant dominance)
keywords:
- 3d
- geography
- globe
- history
- maps
- primary sources
- scrollytelling
- time
---

# Geo-Temporal Atlas

## Description
Events are explored by place and time together on a map or globe.

## UX goal
Give historical or global phenomena geographic context.

## Visual characteristics
Map/globe plus time control; event markers with source cards.

## Interaction behavior
Select time range and region; open event details.

## Suitable project types
- history sites
- global trends
- regional comparisons

## Unsuitable project types
- topics where geography is irrelevant (report warns geography can gain irrelevant dominance)

## Implementation considerations
Prefer 2D maps; use 3D globes only when spherical context matters.

## Accessibility and performance
List/table alternative per time range; heavy map libraries should be lazy-loaded.

## Anti-patterns and risks
- spinning globe as decoration

## Supporting references
- `ref-epoch-lives` – [Epoch Lives](https://pastlives.site/) (`references/entries/ref-epoch-lives.yaml`)
- `ref-erask` – [Erask](https://erask.org/) (`references/entries/ref-erask.yaml`)

## Source provenance
derived from Report 18 (Erask 3D globe with time reference; Epoch Lives maps and primary sources); Report 19 "Situation Map"

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
