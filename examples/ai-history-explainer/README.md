# Scenario A – Interactive website on the history of artificial intelligence

Validation run of `skills/design-inspiration/SKILL.md` (PRD scenario A, *Interactive Learning*). Library state: this PR. All reference IDs below exist in `references/entries/`; all are `not-visually-verified` – designs are based on the report descriptions, not on viewing the sites.

## 1. Brief (templates/project-design-brief.md, condensed)

| Field | Value |
|---|---|
| Audience | Curious non-experts, students, journalists; no maths beyond school level |
| Core message | AI history is a sequence of ideas (symbolic rules → learning from data → deep networks → transformers/LLMs), each driven by what became computable and what data existed – with recurring hype cycles and "AI winters" |
| Content objects | events (dated), ideas/mechanisms, people/institutions, relationships between ideas, compute/data quantities, primary sources |
| Usage mode | Mostly one-time story (15–30 min), optional revisit for reference |
| Constraints | Mobile + desktop, WCAG 2.2 AA, works without WebGL, public website |
| Archetypes | **explain/learn** + **narrate/inform** → groups `learning-by-manipulation`, `narrative` |

## 2. Search log (actual output of `scripts/search_library.py --limit 8`, top hits)

| Query | Top results |
|---|---|
| `history of artificial intelligence timeline` | ref-erask, ref-tactical-tech-gafam-empire, ref-epoch-lives, pat-annotated-timeline, pat-geo-temporal-atlas, pat-scroll-driven-construction, pat-visual-provenance |
| `neural network learning explorable` | ref-complexity-explorables, ref-activation-atlas, ref-distill, ref-tensorflow-playground, pat-single-mechanism-explorable, pat-relationship-graph |
| `ai education playground` | ref-tensorflow-playground, ref-polo-club-explainers, pat-sandbox-playground, ref-pair-explorables, ref-gan-lab, ref-mlu-explain |
| `historical events narrative scroll` | ref-epoch-lives, ref-r2d3-visual-intro-ml, pat-scroll-driven-construction, ref-segel-heer-narrative-visualization, pat-narrative-briefing |

Dropped after reading the entries: ref-connected-china (unreachable, and an org graph is a weaker fit than an idea graph), ref-complexity-explorables (complex-systems focus), ref-erask (geography matters little for AI history – kept only as a counter-example for *not* using a map).

## 3. Shortlist

| ID | Why it is relevant (from the entry) |
|---|---|
| ref-r2d3-visual-intro-ml | Scroll mapped to *construction of the model*, not decoration |
| ref-tensorflow-playground | Immediate feedback between configuration and outcome |
| ref-polo-club-explainers | Real architecture (transformer) as the interface |
| ref-gan-lab | Learning process observable in real time |
| ref-pair-explorables | Readers probe model behaviour themselves |
| ref-epoch-lives | Primary sources give historical narrative evidence |
| ref-tactical-tech-gafam-empire | Development shown as a network + timeline instead of a chart |
| ref-quantum-country | Memory built into the medium |
| ref-activation-atlas | Multi-scale atlas: overview ↔ detail without losing context |
| pat-annotated-timeline, pat-scroll-driven-construction, pat-single-mechanism-explorable, pat-sandbox-playground, pat-system-anatomy-explorer, pat-relationship-graph, pat-visual-provenance, pat-mnemonic-medium | Patterns cited by the references above |

## 4. Three design directions

### Direction A – "The Machine That Rebuilds Itself" (scroll-driven construction)
- **Concept:** One persistent figure in the centre of the screen is rebuilt era by era as the reader scrolls: a hand-written rule tree (1950s–80s) morphs into a perceptron, then a multi-layer net, then attention heads – the history *is* the evolution of one machine.
- **Patterns:** `pat-scroll-driven-construction` (primary), `pat-single-mechanism-explorable` (each era pauses for one manipulable mechanism, e.g. drag a perceptron's decision line), `pat-annotated-timeline` (thin era rail at the edge).
- **References → what transfers:** ref-r2d3-visual-intro-ml (scroll steps = construction steps), ref-tensorflow-playground (the pause points give immediate configuration → outcome feedback), ref-polo-club-explainers (the final transformer stage shows a real architecture, simplified).
- **Signature interaction:** At each "AI winter" the figure visibly fails on a task (XOR for the perceptron) – the reader tries and fails to fix it, which motivates the next era.
- **Visual language:** *editorial-minimalist*; warm off-white, one accent colour per paradigm used consistently in text and figure; serif body, mono labels for code/weights; SVG/Canvas 2D, no WebGL.
- **Accessibility/performance:** Every scroll step is also a URL-addressable step with "next/previous" buttons; reduced motion → cross-fades between static states; text descriptions of each figure state; < 300 KB JS.
- **Risks:** Strong linear authoring – weak for readers who want to jump; mitigated by the era rail.
- **Choose when:** The goal is *understanding why* each breakthrough happened.

### Direction B – "Idea Genealogy" (relationship graph + annotated timeline)
- **Concept:** A horizontal time axis carrying a genealogy of ideas: nodes are ideas/systems (Logic Theorist, backprop, LeNet, word2vec, transformer), edges show "builds on / reacts to", and funding/hype is a background band that swells and collapses (AI winters).
- **Patterns:** `pat-annotated-timeline` (primary), `pat-relationship-graph`, `pat-visual-provenance` (every node links to a primary source: paper, photo, memo).
- **References → what transfers:** ref-tactical-tech-gafam-empire (history as network + timeline instead of a chart), ref-epoch-lives (primary sources as evidence), ref-activation-atlas (zoom from decade overview to single idea without losing context).
- **Signature interaction:** Select an idea → its ancestry lights up backwards through time and its descendants forwards; a "story mode" button walks curated paths (e.g. "From neurons to ChatGPT").
- **Visual language:** *data-editorial*; dark ink on paper texture, archival photographs in duotone, curved edges, typographic era labels.
- **Accessibility/performance:** Graph mirrored as a nested, keyboard-navigable list ("built on", "led to"); hairball avoided by showing at most 2 generations at once (limitation from ref-connected-china); lazy-load sources.
- **Risks:** Exploration-first can lose novices – needs the story mode as default entry.
- **Choose when:** Reference value and revisits matter; audience includes students and journalists.

### Direction C – "Playable Eras" (sandbox chapters + mnemonic review)
- **Concept:** Five short chapters, each a small playground with the technology of its time: write rules for a chatbot (ELIZA era), train a perceptron, watch a GAN learn, tweak attention weights in a mini-transformer. History text is short and wraps around play. Spaced review cards at the end of each chapter.
- **Patterns:** `pat-sandbox-playground` (primary), `pat-system-anatomy-explorer` (transformer chapter), `pat-mnemonic-medium`.
- **References → what transfers:** ref-tensorflow-playground and ref-gan-lab (configuration → observable learning dynamics), ref-polo-club-explainers (real architecture as interface), ref-pair-explorables (probe model behaviour, e.g. bias), ref-quantum-country (review prompts embedded in the medium).
- **Signature interaction:** The same toy task ("is this a cat?") is attempted in every era – the reader experiences what each paradigm can and cannot do.
- **Visual language:** *playful-systemic*; bright but restricted palette per era, rounded "lab bench" panels, hand-drawn annotations.
- **Accessibility/performance:** Every playground has keyboard controls and a text readout of its state; results are announced via live regions; models run client-side at toy scale (no ML library > 200 KB).
- **Risks:** Highest build effort; history depth is lower.
- **Choose when:** Learning outcomes (classes, workshops) matter more than historical completeness.

## 5. Comparison and recommendation

| | A Rebuilding Machine | B Idea Genealogy | C Playable Eras |
|---|---|---|---|
| Best for | understanding causes | reference, revisits | hands-on learning |
| Effort | medium | medium-high (content curation) | high |
| Main risk | linearity | overload | shallow history |

**Recommendation: A**, with B's genealogy as an optional overview at the end. Report 18 repeatedly locates the strength of explorables in one mechanism per figure and scroll that builds understanding (ref-r2d3-visual-intro-ml); A delivers that with moderate effort and a clear narrative. *(Awaiting user approval in a real project.)*

## 6. Traceability

Research used: Report 18 (R2D3, TensorFlow Playground, Polo Club, GAN Lab, PAIR, Quantum Country, Activation Atlas, Epoch Lives), Report 19 (GAFAM Empire network/timeline; manifesto "Narrate, then let me explore", "Relationships are first-class"). No generic dashboard elements were considered necessary.
