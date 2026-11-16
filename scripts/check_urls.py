#!/usr/bin/env python3
"""Check every URL in the raw reference catalogues and record the result.

Writes references/url-checks.yaml. A 401/403/429 usually means bot
protection or a login wall, not a dead link, and is recorded as "blocked".

    python scripts/check_urls.py            # check all raw URLs
"""
from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def all_urls() -> list[str]:
    urls: set[str] = set()
    for path in sorted((ROOT / "research/processed").glob("*-raw-references.yaml")):
        for ref in yaml.safe_load(path.read_text(encoding="utf-8"))["references"]:
            if ref.get("url"):
                urls.add(ref["url"])
    return sorted(urls)


def check(url: str, verify_tls: bool = True) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    ctx = None if verify_tls else ssl._create_unverified_context()  # noqa: S323 - reachability only
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            code, final = resp.status, resp.geturl()
    except urllib.error.HTTPError as exc:
        code, final = exc.code, exc.geturl() or url
    except Exception as exc:  # noqa: BLE001 - record any network failure
        if verify_tls and isinstance(getattr(exc, "reason", None), ssl.SSLError):
            result = check(url, verify_tls=False)
            result["note"] = "reachable only without TLS certificate verification"
            return result
        return {"url": url, "status": "unreachable", "http_code": None, "error": type(exc).__name__}
    if 200 <= code < 300:
        status = "live"
    elif 300 <= code < 400:
        status = "live"
    elif code in (401, 403, 429):
        status = "blocked"
    else:
        status = "error"
    result = {"url": url, "status": status, "http_code": code}
    if final.rstrip("/") != url.rstrip("/"):
        result["final_url"] = final
    return result


def main() -> None:
    urls = all_urls()
    with cf.ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(check, urls))
    doc = {
        "checked_on": dt.date.today().isoformat(),
        "method": "HTTP GET with browser user agent, redirects followed (scripts/check_urls.py)",
        "summary": {s: sum(r["status"] == s for r in results) for s in ("live", "blocked", "error", "unreachable")},
        "results": results,
    }
    out = ROOT / "references/url-checks.yaml"
    out.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print(doc["summary"])
    bad = [r for r in results if r["status"] in ("error", "unreachable")]
    for r in bad:
        print("  ", r["status"], r["url"], r.get("http_code") or r.get("error"))
    sys.exit(0)


if __name__ == "__main__":
    main()
