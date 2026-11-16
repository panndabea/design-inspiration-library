# Usage Examples

## Searching

```bash
$ python scripts/search_library.py --query "interactive educational timeline" --limit 3
[reference] ref-erask  (score 14.0)
    Erask
    references/entries/ref-erask.yaml  https://erask.org/
    related: pat-geo-temporal-atlas
    matched: timeline
[pattern] pat-annotated-timeline  (score 13.0)
    Annotated Timeline
    patterns/narrative/pat-annotated-timeline.md
    related: ref-tactical-tech-gafam-empire
    matched: timeline
...
```

Useful variants:

```bash
python scripts/search_library.py -q "dependencies relationships network" --type pattern
python scripts/search_library.py -q "uncertainty provenance ai" --json      # for agents
python scripts/search_library.py -q "transformer" --category ml-education
python scripts/search_library.py --list-categories
```

Tips: query the *content objects* ("dependencies", "events", "uncertainty") and the *job* ("decide", "explain", "compare"), not only the product type. Run 3–5 queries and open the returned files.

## Starting a new project with Devin

Paste the prompt from [prompt-template.md](prompt-template.md). Devin then fills the templates in your project's `docs/design/`, presents three directions and waits for your choice.

## Worked examples

See [`examples/`](../examples/README.md): AI-history explainer, portfolio management app, global technology trends platform.
