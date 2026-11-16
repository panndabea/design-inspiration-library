---
id: pat-relationship-graph
name: Relationship Graph
group: spatial-and-relational
source_reports:
- beyond-dashboards
- interactive-learning
provenance: Report 19 pattern table ("Relationship Graph"), manifesto "Relationships are first-class"; Connected
  China, GAFAM Empire; Report 18 LOOPY
supporting_references:
- ref-connected-china
- ref-loopy
- ref-tactical-tech-gafam-empire
suitable_for:
- stakeholder and organisation maps
- dependencies in portfolios
- ecosystems
- supply chains
unsuitable_for:
- very large dense graphs without aggregation
keywords:
- acquisitions
- big tech
- causal
- drawing
- ecosystem
- entities
- feedback loops
- network
- power
- relationships
- stakeholders
- systems thinking
- technology
---

# Relationship Graph

## Description
Entities and their relationships are the primary information objects instead of isolated values.

## UX goal
Make dependencies, power and risk visible.

## Visual characteristics
Node-link or matrix views with typed edges; focus+context around a selected entity.

## Interaction behavior
Select entity → show neighbourhood, filter edge types, trace paths.

## Suitable project types
- stakeholder and organisation maps
- dependencies in portfolios
- ecosystems
- supply chains

## Unsuitable project types
- very large dense graphs without aggregation

## Implementation considerations
Start from an ego-network around a chosen entity; aggregate clusters; use a graph library only when needed.

## Accessibility and performance
Provide adjacency lists/tables as an alternative; limit visible nodes.

## Anti-patterns and risks
- hairball graphs (report risk)
- decorative network backgrounds

## Supporting references
- `ref-connected-china` – [Connected China](https://china.fathom.info/) (`references/entries/ref-connected-china.yaml`)
- `ref-loopy` – [LOOPY](https://ncase.me/loopy/) (`references/entries/ref-loopy.yaml`)
- `ref-tactical-tech-gafam-empire` – [Tactical Tech – GAFAM Empire](https://tacticaltech.org/projects/) (`references/entries/ref-tactical-tech-gafam-empire.yaml`)

## Source provenance
Report 19 pattern table ("Relationship Graph"), manifesto "Relationships are first-class"; Connected China, GAFAM Empire; Report 18 LOOPY

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
