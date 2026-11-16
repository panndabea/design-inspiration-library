---
id: pat-insight-feed
name: Insight Feed
group: decision-and-exploration
source_reports:
- beyond-dashboards
provenance: Report 19 pattern table ("Insight Feed"), manifesto "Show change, not inventory"
supporting_references:
- ref-reuters-2025-in-graphics
suitable_for:
- operations
- management
- portfolio monitoring
unsuitable_for:
- contexts without reliable change detection
keywords:
- briefing
- curation
- editorial
- year in review
---

# Insight Feed

## Description
The system prioritises changes and anomalies and presents them as a ranked feed.

## UX goal
Attention instead of monitoring.

## Visual characteristics
Ranked items with change magnitude and context; quiet treatment for "no change".

## Interaction behavior
Dismiss, snooze, open evidence, convert to task/decision.

## Suitable project types
- operations
- management
- portfolio monitoring

## Unsuitable project types
- contexts without reliable change detection

## Implementation considerations
Explicit ranking rules; explain why an item is shown.

## Accessibility and performance
Avoid real-time reflow that moves content under the cursor.

## Anti-patterns and risks
- alert fatigue (report risk)

## Supporting references
- `ref-reuters-2025-in-graphics` – [Reuters Graphics – 2025 in Graphics](https://www.reuters.com/graphics/what-2025-looked-like-graphics-2026-01-20/) (`references/entries/ref-reuters-2025-in-graphics.yaml`)

## Source provenance
Report 19 pattern table ("Insight Feed"), manifesto "Show change, not inventory"

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
