# Scenario C – Interactive platform explaining global technological trends

Validation run of `skills/design-inspiration/SKILL.md` (PRD scenario C, *Hybrid Experience*: educational storytelling + sophisticated exploration). All reference IDs exist in `references/entries/`; all are `not-visually-verified`.

## 1. Brief (condensed)

| Field | Value |
|---|---|
| Audience | Interested public, policy makers, educators; mixed data literacy |
| Core message | Technologies (e.g. AI, renewables, mobile internet, EVs) spread along S-curves at very different speeds across regions; diffusion depends on infrastructure, cost and policy |
| Content objects | trends, indicators over time × country, relationships between technologies and companies, regional differences, uncertainty in forecasts |
| Usage mode | Story entry (5–10 min) + repeated exploration; embeddable charts |
| Constraints | Mobile-first, WCAG 2.2 AA, open data with sources, forecasts must show uncertainty |
| Archetypes | **narrate/inform** + **explore/analyse** + **explain/learn** → `narrative`, `spatial-and-relational`, `perspective-and-comparison` |

## 2. Search log (actual output, top hits)

| Query | Top results |
|---|---|
| `global technology trends` | ref-owid-grapher, ref-glocal-climate-change, pat-personalised-data-experience, pat-scroll-driven-construction, pat-annotated-timeline, ref-tactical-tech-gafam-empire, pat-geo-temporal-atlas |
| `trend change over time map` | pat-semantic-landscape, ref-map-of-mathematics, ref-owid-grapher, pat-geo-temporal-atlas, pat-annotated-timeline, ref-erask |
| `ecosystem market landscape` | ref-accurat-data-landscape-venice, ref-tactical-tech-gafam-empire, pat-semantic-landscape, ref-map-of-mathematics, pat-relationship-graph |
| `personalised data story` | ref-glocal-climate-change, ref-the-pudding, pat-personalised-data-experience, ref-pudding-judge-my-music, ref-datanarrative, pat-narrate-then-explore |
| `explore world data` | ref-owid-grapher, pat-narrate-then-explore, ref-the-pudding, ref-reuters-2025-in-graphics, pat-multiple-perspectives |

## 3. Shortlist

| ID | Why it is relevant (from the entry) |
|---|---|
| ref-owid-grapher | Narrative embedding separated from optional exploration – "Context before precision" |
| ref-glocal-climate-change | Global topic made personal by anchoring it in the reader's place |
| ref-the-pudding | Data-editorial storytelling on cultural/social topics |
| ref-map-of-mathematics | Spatial position encodes relationships; orientation before detail |
| ref-fathom-laniakea | Spatial orientation in topic clusters in addition to search |
| ref-tactical-tech-gafam-empire | Tech ecosystem as network + timeline |
| ref-erask | Time and place explored together |
| ref-reuters-2025-in-graphics | Editorial hierarchy for a complex world |
| ref-datanarrative | Explicit verification step separating fact from inference |
| ref-mit-umwelt | Multimodal (visual/text/sonification) representation for accessibility |
| pat-narrate-then-explore, pat-personalised-data-experience, pat-geo-temporal-atlas, pat-semantic-landscape, pat-relationship-graph, pat-multiple-perspectives, pat-visual-provenance, pat-multimodal-representation | |

## 4. Three design directions

### Direction A – "Your Place in the Curve" (personalised narrate-then-explore)
- **Concept:** The reader picks their country (or it is suggested); the story then shows how fast each technology arrived *there* compared with the world – each chapter ends in a live chart the reader can take over and explore.
- **Patterns:** `pat-personalised-data-experience` (entry), `pat-narrate-then-explore` (structure), `pat-visual-provenance` (source and uncertainty on every chart).
- **References → what transfers:** ref-glocal-climate-change (global → personal anchor), ref-owid-grapher (story embedding + optional explorer with sources), ref-the-pudding (data-editorial dramaturgy).
- **Signature interaction:** "Guess first": the reader draws their guess of mobile-internet adoption in their country, then the real curve appears over it.
- **Visual language:** *data-editorial*; large display type, one colour for "your country", grey for the world; forecasts as fading bands.
- **Accessibility/performance:** Drawn guess has a numeric-input alternative; every chart has a data table and text summary; static SVG charts, explorer loaded on demand.
- **Risks:** Country data gaps → honest "no data" states.
- **Choose when:** Broad public audience and media sharing.

### Direction B – "Diffusion Atlas" (geo-temporal atlas + multiple perspectives)
- **Concept:** A world atlas with a time scrubber: technologies spread across the map as S-curves; side panels compare two regions or two technologies; a "lens" switch shows the same data per capita, absolute, or by income group.
- **Patterns:** `pat-geo-temporal-atlas` (primary), `pat-multiple-perspectives`, `pat-annotated-timeline` (milestones on the scrubber), `pat-multimodal-representation`.
- **References → what transfers:** ref-erask (time and place together), ref-owid-grapher (indicator explorer conventions, sources), ref-mit-umwelt (sonified time series and text descriptions as equal alternatives to the map).
- **Signature interaction:** Scrub 1990 → 2025 while two technologies are selected – the reader sees leapfrogging (e.g. regions that skipped landlines).
- **Visual language:** *technical-spatial* in 2D: equal-area projection, sequential colour scale with a colour-blind-safe palette, annotations pinned to places and years.
- **Accessibility/performance:** Map has a sortable table twin and per-country text; scrubber is a slider with keyboard steps; vector tiles + Canvas, no 3D globe (space is geographic but 3D adds nothing).
- **Risks:** Choropleth biases toward large countries; needs per-capita lens by default.
- **Choose when:** Policy and education users who will return and compare.

### Direction C – "Technology Landscape" (semantic landscape + relationship graph)
- **Concept:** A navigable landscape where technologies are regions placed by relatedness (AI near semiconductors and cloud; batteries near EVs and solar); elevation encodes adoption momentum, and a timeline lets the landscape shift over decades. Companies and policies appear as linked nodes when zoomed in.
- **Patterns:** `pat-semantic-landscape` (primary), `pat-relationship-graph` (zoomed-in level), `pat-narrate-then-explore` (guided tours through the landscape).
- **References → what transfers:** ref-map-of-mathematics and ref-fathom-laniakea (orientation by spatial relatedness), ref-tactical-tech-gafam-empire (companies as an ecosystem network), ref-accurat-data-landscape-venice (data as landscape – noting the report's lower transferability rating).
- **Signature interaction:** Guided tour "How the smartphone pulled other technologies along" moves the camera across connected regions; then free exploration.
- **Visual language:** *playful-systemic*: illustrated contour landscape, soft pastel regions, labels in a strong grotesk; motion limited to camera moves.
- **Accessibility/performance:** Landscape mirrored as a hierarchical list of technology families with relations; camera moves replaced by cuts in reduced motion; 2.5D SVG, no WebGL by default.
- **Risks:** Layout/semantic mis-clustering (Latent Lab caveat) – placements must be explained and editorially reviewed; least precise for numbers.
- **Choose when:** Goal is understanding how trends relate, not exact values.

## 5. Comparison and recommendation

| | A Your Place in the Curve | B Diffusion Atlas | C Technology Landscape |
|---|---|---|---|
| Best for | public storytelling | comparison & reference | systemic understanding |
| Effort | medium | high | high |
| Main risk | data gaps | map bias | mis-clustering, imprecision |

**Recommendation: A as the story layer on top of B as the exploration layer** – this is exactly Report 19's "Narrate, then let me explore" and the OWID separation of narrative embedding and optional exploration; C is the most original and works as a later "connections" chapter. *(Awaiting user approval in a real project.)*

## 6. Traceability

Research used: Report 19 (OWID Grapher, Reuters, GAFAM Empire, Laniakea, Accurat, Umwelt, DataNarrative; manifesto "Context before precision", "Make uncertainty visible", "Use space when space means something"), Report 18 (Glocal Climate Change, The Pudding, Erask, Map of Mathematics). Combines educational storytelling with exploration as required by the PRD scenario.
