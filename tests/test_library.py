import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import library  # noqa: E402
import search_library  # noqa: E402
import validate_library  # noqa: E402


def test_library_is_valid():
    assert validate_library.validate() == []


def test_counts_within_prd_ranges():
    assert 30 <= len(library.load_entries()) <= 55
    assert 15 <= len(library.load_patterns()) <= 25


def test_search_returns_ids_and_paths():
    results = search_library.search("interactive educational timeline")
    assert results
    for r in results:
        assert r["id"].startswith(("ref-", "pat-"))
        assert (library.ROOT / r["path"]).exists()
    assert "pat-annotated-timeline" in {r["id"] for r in results}


def test_search_type_filter():
    assert all(r["type"] == "pattern" for r in search_library.search("relationships", kind="pattern"))


def test_validator_rejects_invented_url(monkeypatch):
    entries = library.load_entries()
    fake = copy.deepcopy(entries[0])
    fake["id"], fake["_path"] = "ref-invented", "references/entries/ref-invented.yaml"
    fake["url"] = "https://example.com/not-in-any-report"
    monkeypatch.setattr(validate_library, "load_entries", lambda: entries + [fake])
    errors = validate_library.validate()
    assert any("does not occur in any original report" in e for e in errors)


def test_validator_rejects_missing_field(monkeypatch):
    entries = library.load_entries()
    broken = copy.deepcopy(entries[0])
    del broken["why_it_works"]
    monkeypatch.setattr(validate_library, "load_entries", lambda: [broken] + entries[1:])
    assert any("missing field 'why_it_works'" in e for e in validate_library.validate())


def test_validator_rejects_truncated_url(monkeypatch):
    entries = copy.deepcopy(library.load_entries())
    target = next(e for e in entries if e["id"] == "ref-accurat-data-landscape-venice")
    target["url"] = "https://studio.accurat.it/work/data-land"
    monkeypatch.setattr(validate_library, "load_entries", lambda: entries)
    errors = validate_library.validate()
    assert any("does not occur in any original report" in e for e in errors)
