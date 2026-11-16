# Scenario B – Modern project portfolio management application

Validation run of `skills/design-inspiration/SKILL.md` (PRD scenario B, *Beyond Dashboards*). All reference IDs exist in `references/entries/`; all are `not-visually-verified`.

## 1. Brief (condensed)

| Field | Value |
|---|---|
| Audience | Portfolio managers, PMO, executives (weekly), project leads (daily) |
| Core job | Decide where to intervene: which projects are at risk, why, what depends on them, and what happens if budget/people are moved |
| Content objects | projects, milestones, dependencies, people/capacity, budget, risks, decisions, status reports (text) |
| Usage mode | Repeated tool – weekly review + ad-hoc drill-down |
| Constraints | Desktop-first, tablet for reviews, WCAG 2.2 AA, enterprise data volumes (~200 projects), AI summaries allowed but must be checkable |
| Archetypes | **decide/operate** + **explore/analyse** → `decision-and-exploration`, `ai-native`, `spatial-and-relational`, `perspective-and-comparison` |

The default answer would be a sidebar + KPI cards (on time / on budget / at risk) + RAG table. Report 19's manifesto ("Decision before dashboard", "Show change, not inventory", "Relationships are first-class") asks to question that.

## 2. Search log (actual output, top hits)

| Query | Top results |
|---|---|
| `project portfolio management decision` | pat-situation-to-decision-brief, pat-insight-feed, pat-narrative-briefing, pat-what-if-simulation, pat-relationship-graph, ref-stamen-crisisready-readymapper |
| `dependencies relationships network` | pat-relationship-graph, ref-connected-china, ref-tactical-tech-gafam-empire |
| `scenario what-if comparison` | pat-comparative-split-view, pat-what-if-simulation, ref-markup-split-screen, ref-loopy |
| `insight briefing change` | ref-reuters-2025-in-graphics, pat-insight-feed, ref-insightlens, pat-narrative-briefing, pat-persistent-insight-workspace |
| `uncertainty provenance ai` | ref-pair-explorables, pat-visual-provenance, ref-waitgpt, pat-mixed-initiative-direct-manipulation |

## 3. Shortlist

| ID | Why it is relevant (from the entry) |
|---|---|
| ref-stamen-crisisready-readymapper | Real-time data composed into a context-specific report for decision makers – "Decision before dashboard" |
| ref-reuters-2025-in-graphics | Editorial selection gives a complex world an information hierarchy – "Show change, not inventory" |
| ref-connected-china | Relationships as the primary information object; caveat: hairball risk (archived, URL unreachable at check – concept only) |
| ref-tactical-tech-gafam-empire | Network instead of a revenue chart; transfers to ecosystem intelligence |
| ref-markup-split-screen | Juxtaposition of parallel realities; transfers to segment/business-unit comparison |
| ref-loopy | Users build causal models themselves |
| ref-insightlens | Insights do not disappear in the chat stream – "Keep state persistent" |
| ref-waitgpt | Analysis steps can be understood, checked and changed – "Make reasoning inspectable" |
| ref-storyfacets | Analysis becomes a traceable story – "Make evidence addressable" |
| ref-mit-latent-lab | Knowledge space instead of file/dashboard hierarchy; caveat: mis-clustering |
| pat-situation-to-decision-brief, pat-insight-feed, pat-relationship-graph, pat-what-if-simulation, pat-comparative-split-view, pat-visual-provenance, pat-persistent-insight-workspace, pat-semantic-landscape | |

## 4. Three design directions

### Direction A – "Monday Brief" (situation-to-decision brief + insight feed)
- **Concept:** The start screen is not a dashboard but a short, ranked brief: *what changed since last review, why it matters, what you could decide* – each item ends in a decision card (approve re-plan, move capacity, escalate, accept risk).
- **Patterns:** `pat-situation-to-decision-brief` (primary), `pat-insight-feed`, `pat-visual-provenance`.
- **References → what transfers:** ref-stamen-crisisready-readymapper (data composed into a decision-maker report), ref-reuters-2025-in-graphics (editorial ranking instead of inventory), ref-waitgpt / ref-storyfacets (every AI-generated sentence expands to the underlying data and steps).
- **Signature interaction:** Each brief item has a "why?" disclosure showing the evidence (milestone slips, dependency, budget delta) with facts and model inferences visually separated (solid vs. hatched/labelled "inference").
- **Visual language:** *editorial-minimalist* for enterprise: large type for the headline change, small inline charts (sparkline of slip days), neutral palette with a single alert colour reserved for decisions.
- **Accessibility/performance:** Pure document structure (headings, lists) – excellent screen-reader story; server-rendered, near-zero JS.
- **Risks:** Wrong AI summaries (ref-insightlens caveat) → mandatory evidence links, human-editable brief.
- **Choose when:** Executives and weekly reviews are the main users.

### Direction B – "Dependency Terrain" (relationship graph + what-if)
- **Concept:** The portfolio is a map of projects connected by dependencies, laid out along time (x) and strategic theme (y). Risk propagates visibly along edges; dragging a delay or moving people shows the ripple through the graph.
- **Patterns:** `pat-relationship-graph` (primary), `pat-what-if-simulation`, `pat-comparative-split-view` (current plan vs. scenario).
- **References → what transfers:** ref-connected-china / ref-tactical-tech-gafam-empire (relationships first-class; network instead of chart), ref-loopy (cause → effect made tangible), ref-markup-split-screen (before/after side by side).
- **Signature interaction:** "Drag milestone +4 weeks" → downstream projects shift and recolour; a split view compares plan A/B with deltas in cost and dates.
- **Visual language:** *technical-spatial* but 2D: light grid, project nodes as capsules sized by budget, edges weighted by criticality; motion only to show propagation.
- **Accessibility/performance:** Graph has a table/tree twin ("blocks / blocked by"), keyboard node traversal along edges, reduced-motion shows final state; WebGL only above ~500 nodes, otherwise SVG/Canvas; show 1–2 dependency hops by default (hairball caveat).
- **Risks:** Needs good dependency data; graph literacy varies.
- **Choose when:** Dependencies and resourcing trade-offs are the real problem.

### Direction C – "Portfolio Room" (persistent insight workspace)
- **Concept:** A workspace where questions, pinned insights, scenario comparisons and decisions persist as objects on a canvas grouped by theme – the PMO's shared memory, with an assistant that proposes but never silently changes.
- **Patterns:** `pat-persistent-insight-workspace` (primary), `pat-mixed-initiative-direct-manipulation`, `pat-semantic-landscape` (themes cluster spatially), `pat-visual-provenance`.
- **References → what transfers:** ref-insightlens (insights persist outside the chat), ref-storyfacets (analysis as traceable story), ref-mit-latent-lab (knowledge space instead of hierarchy), ref-mit-pluto (author stays in control of AI recommendations).
- **Signature interaction:** Ask "Which projects depend on the ERP migration?" → the answer becomes a pinned card with its query and data snapshot; cards can be combined into a decision memo.
- **Visual language:** *research-native*: canvas with soft cards, monospace metadata (source, timestamp, confidence), clear distinction between human notes and AI output.
- **Accessibility/performance:** Canvas also available as an ordered outline; all card actions keyboard-reachable; virtualised rendering.
- **Risks:** Highest conceptual novelty; semantic mis-clustering; needs governance of persisted insights.
- **Choose when:** Analysts/PMO run recurring investigations and need traceable decisions.

## 5. Comparison and recommendation

| | A Monday Brief | B Dependency Terrain | C Portfolio Room |
|---|---|---|---|
| Best for | executives, weekly decisions | planners, trade-offs | PMO analysts |
| Effort | low-medium | medium-high | high |
| Main risk | trust in summaries | data quality, graph literacy | novelty, governance |

**Recommendation: A as the entry point + B as the drill-down** ("decide → understand why → simulate"). This follows Report 19's architecture idea (insights composed for intent, deterministic rendering of evidence) and avoids a KPI-card start page while keeping a familiar, low-risk document form. A conventional table remains available as a secondary "inventory" view – justified for bulk editing, not as the home screen. *(Awaiting user approval in a real project.)*

## 6. Traceability

Research used: Report 19 (ReadyMapper, Reuters, Connected China, GAFAM Empire, Markup split screen, InsightLens, WaitGPT, StoryFacets, Latent Lab, Pluto; manifesto principles "Decision before dashboard", "Separate fact from inference", "Keep state persistent"), Report 18 (LOOPY). The generic KPI dashboard was considered and explicitly demoted with a stated reason.
