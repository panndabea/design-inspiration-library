# Beyond-Dashboard Design Manifesto

Source: Report 19, section "Beyond-Dashboard Design Manifesto" (`research/original/beyond-dashboards/deep-research-report-19.md`). The principle names are quoted from the report; meaning, positive reference and anti-pattern are translated from the German table.

| # | Principle | Meaning | Positive reference pattern | Anti-pattern |
|---|---|---|---|---|
| 1 | **Lead with meaning** | Statement before raw number | The Pudding, Information is Beautiful | 25 equally weighted KPI cards |
| 2 | **Show change, not inventory** | Prioritise changes | Reuters, Situation Brief | Start page as data warehouse |
| 3 | **Context before precision** | Orientation first, then detail | Our World in Data | Exact values without meaning |
| 4 | **Relationships are first-class** | Model dependencies explicitly | Connected China | Isolated metrics |
| 5 | **Narrate, then let me explore** | Combine guidance and discovery | Segel & Heer | Only story or only sandbox |
| 6 | **Progressively disclose complexity** | Detail levels on demand | OWID Grapher | Everything at once |
| 7 | **Preserve agency** | User can change AI suggestions | Pluto | Unchangeable AI answer |
| 8 | **Make reasoning inspectable** | Analysis path visible | WaitGPT | "AI says…" without origin |
| 9 | **Make evidence addressable** | Every statement has a data/source anchor | StoryFacets | Loose summary |
| 10 | **Separate fact from inference** | Mark measurement, model and hypothesis | DataNarrative verification | Generated interpretation treated as fact |
| 11 | **Compose around intent** | Presentation follows the task | Generative UI | Fixed navigation for every question |
| 12 | **Keep semantics stable** | Define metrics/entities centrally | Semantic layer | AI computes the same KPI differently |
| 13 | **Use visual grammar, not visual decoration** | Form carries meaning | IIB, DensityDesign | Decorative 3D graphics |
| 14 | **Design multimodally** | Text, visual, audio as equals | Umwelt | Accessibility as an afterthought alt text |
| 15 | **Use space when space means something** | Spatial UI only with semantic function | MIT Latent Lab | Arbitrary 3D worlds |
| 16 | **Make uncertainty visible** | Show model limits and confidence | Simulation/Forecast | Falsely precise future values |
| 17 | **Keep state persistent** | Keep insights across sessions | InsightLens | Chat as throw-away UI |
| 18 | **Decision before dashboard** | UI ends in action/decision | CrisisReady | Pure observation without next option |

## Hypothesis verdicts (Report 19, summarised)

- *Information instead of metrics* – strongly confirmed, but **metrics are evidence, not automatically the primary interface structure**.
- *Narrative instead of dashboard* – partially confirmed: aim for a **narrative default interface with exploratory branches**.
- *Exploration instead of filters* – confirmed with limits: **manipulation and semantic navigation for discovery, filters for precision**.
- *Relationships instead of single values* – strongly confirmed for complex problems; large graphs overload.
- *Adaptivity instead of static UI* – plausible, not yet universally validated; adaptive must not mean unpredictable.
- *AI-native instead of BI-native* – confirmed as direction: **AI-orchestrated, semantically grounded, human-verifiable**.
- "Chat darf nicht die gesamte Benutzeroberfläche werden" – chat must not become the whole UI; it should create and manipulate structured objects.

## Reference architecture (Report 19)

`Raw Data → Semantic Layer → Analytical Services → Insight Graph → AI Orchestrator → UI Specification → Deterministic Renderer`

Use this when a project generates information views with AI: the model proposes a constrained UI specification, a deterministic renderer draws it.
