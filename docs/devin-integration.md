# Devin Integration

The library is a **separate shared repository**. Projects reference it; they do not copy it. Each project stores its own brief, shortlist, directions and decision under `docs/design/`.

## How Devin finds the skill (verified 2026-11-16)

- Devin discovers repository skills from `SKILL.md` files in cloned repositories, e.g. `.agents/skills/<name>/SKILL.md` (also `.devin/skills/…`). This repo ships the skill at the PRD path `skills/design-inspiration/SKILL.md` **and** an identical copy at `.agents/skills/design-inspiration/SKILL.md` (kept in sync by `validate_library.py`).
- Tested: with this repository cloned on the Devin machine, a skill search for "design inspiration library new project UI" returned the `design-inspiration` skill.
- Discovery only works if the repository is **on the machine** of that session. A `SKILL.md` alone does not guarantee that Devin uses it – the description tells Devin when it is relevant, but the explicit invocation below is the reliable path.
- Devin also reads `AGENTS.md` in repositories it works in.

## Setup options (simplest first)

1. **Give Devin access to the repository** (Devin settings → Repositories / GitHub integration, include `panndabea/design-inspiration-library`). Optionally add it to the environment/blueprint so it is pre-cloned in every session – then the skill is discovered automatically.
2. **Personal skill (recommended in addition).** Save `skills/design-inspiration/SKILL.md` as a personal Devin plugin skill. It is then available in every session, even when only the project repository is cloned; step 0 of the skill clones the library on demand. Re-save after the skill changes.
3. **Project-level pointer.** In each new project's `AGENTS.md` add:

   ```markdown
   ## Design
   Before designing or redesigning UI, use the Design Inspiration Library
   (https://github.com/panndabea/design-inspiration-library): follow its
   skills/design-inspiration/SKILL.md, store results in docs/design/, and get approval
   of one of three design directions before full implementation.
   ```

4. *(Optional)* Git submodule – not recommended: it pins a stale copy and adds friction; cloning on demand is enough.

## Explicit invocation (always works)

Start the session with the prompt in [`prompt-template.md`](prompt-template.md), or add one line to any task:

> Use the design-inspiration skill (https://github.com/panndabea/design-inspiration-library) before building any UI.

## Other agents

Agents without skill support can follow `AGENTS.md` and the workflows directly; everything is plain Markdown/YAML and the scripts need only Python + PyYAML.
