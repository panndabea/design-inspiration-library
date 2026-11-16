"""Shared loaders for the Design Inspiration Library scripts."""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "references" / "entries"
PATTERNS_DIR = ROOT / "patterns"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_entries() -> list[dict]:
    entries = []
    for path in sorted(ENTRIES_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        data["_path"] = rel(path)
        entries.append(data)
    return entries


def load_patterns() -> list[dict]:
    patterns = []
    for path in sorted(PATTERNS_DIR.glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            patterns.append({"_path": rel(path), "_error": "missing YAML front matter"})
            continue
        front, body = text[4:].split("\n---\n", 1)
        data = yaml.safe_load(front) or {}
        data["_path"] = rel(path)
        data["_body"] = body
        patterns.append(data)
    return patterns
