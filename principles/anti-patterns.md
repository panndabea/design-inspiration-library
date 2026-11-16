# Anti-Patterns

Agents must check every proposed direction against this list. Items tagged [R19] are from the Report 19 manifesto and pattern risks; [R18] from Report 18; [G] general.

## Generic UI defaults to avoid unless justified
- Grid of equally weighted KPI cards as the start page ("25 gleichgewichtete KPI-Karten"). [R19]
- Standard left sidebar + top bar + cards + table as the automatic first idea. [G, from PRD motivation]
- Data tables as the only representation of relationships. [R19 "isolated metrics"]
- Start page as data inventory instead of changes. [R19]
- Fixed navigation for every question. [R19]

## Decoration instead of meaning
- Decorative 3D, spinning globes, particle backgrounds. [R19]
- Motion that does not encode change. [R18 / G]
- Arbitrary 3D worlds / spatial layouts without semantic positions. [R19]

## Interaction failures
- Only story or only sandbox. [R19]
- Everything at once instead of progressive disclosure. [R19]
- Many unrelated controls on one figure; interactivity that covers too much material. [R18]
- Scroll-jacking; hover-only information. [G]

## AI-specific failures
- Unchangeable AI answer. [R19]
- "AI says…" without provenance. [R19]
- Generated interpretation treated as fact. [R19]
- Chat as throw-away UI; insights lost in the conversation stream. [R19]
- Hallucinated or inconsistent KPIs computed differently each time. [R19]

## Pattern-specific risks (Report 19 pattern table)
- Relationship graphs: hairball problem. Timelines: correlation shown as cause. Insight feeds: alert fatigue. Simulations: model over-trust. Semantic landscapes: spatial metaphors need learning / semantic mis-clusters. Generative composition: inconsistent UX.

## Copying
- Reproducing a reference's visual identity, layout or illustrations. References explain *why* something works; designs must be original. [PRD]
