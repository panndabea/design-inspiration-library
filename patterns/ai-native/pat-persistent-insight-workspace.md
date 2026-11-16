---
id: pat-persistent-insight-workspace
name: Persistent Insight Workspace
group: ai-native
source_reports:
- beyond-dashboards
- interactive-learning
provenance: Report 19 – "Chat darf nicht die gesamte Benutzeroberfläche werden"; pattern table ("Conversational
  Entry", "Insight Graph"); manifesto "Keep state persistent"; InsightLens, WaitGPT, Latent Lab
supporting_references:
- ref-insightlens
- ref-mit-latent-lab
- ref-pudding-judge-my-music
- ref-storyfacets
- ref-waitgpt
suitable_for:
- AI assistants
- analyst tools
- research and project knowledge
unsuitable_for:
- simple single-purpose tasks where a form is faster
keywords:
- ai
- analysts
- audit
- chat
- chat history
- code
- conversational analytics
- dialogue
- documents
- embeddings
- history
- insights
- knowledge
- llm
- music
---

# Persistent Insight Workspace

## Description
Natural language is an entry point, but results become structured, persistent objects (insights, evidence, decisions, entities, scenarios) that live outside the chat stream.

## UX goal
Low entry barrier without losing results in a conversation history.

## Visual characteristics
Conversation panel plus a structured board/graph of insight objects.

## Interaction behavior
Ask → system creates or updates objects → user edits, links, pins.

## Suitable project types
- AI assistants
- analyst tools
- research and project knowledge

## Unsuitable project types
- simple single-purpose tasks where a form is faster

## Implementation considerations
Define the object schema first; chat actions map to object operations.

## Accessibility and performance
Objects must be navigable without the chat.

## Anti-patterns and risks
- chat as throw-away UI (manifesto anti-pattern)
- hallucinated summaries stored as facts

## Supporting references
- `ref-insightlens` – [InsightLens](https://arxiv.org/abs/2404.01644) (`references/entries/ref-insightlens.yaml`)
- `ref-mit-latent-lab` – [MIT Latent Lab](https://www.media.mit.edu/projects/latent-lab/overview/) (`references/entries/ref-mit-latent-lab.yaml`)
- `ref-pudding-judge-my-music` – [How Bad Is Your Streaming Music?](https://pudding.cool/2021/10/judge-my-music/) (`references/entries/ref-pudding-judge-my-music.yaml`)
- `ref-storyfacets` – [StoryFacets](https://vis.khoury.northeastern.edu/pubs/Park2022StoryfacetsDesignStudy/) (`references/entries/ref-storyfacets.yaml`)
- `ref-waitgpt` – [WaitGPT](https://arxiv.org/abs/2408.01703) (`references/entries/ref-waitgpt.yaml`)

## Source provenance
Report 19 – "Chat darf nicht die gesamte Benutzeroberfläche werden"; pattern table ("Conversational Entry", "Insight Graph"); manifesto "Keep state persistent"; InsightLens, WaitGPT, Latent Lab

> Patterns describe generalisable ideas. Do not copy the visual design of the supporting references; use them to understand *why* the pattern works.
