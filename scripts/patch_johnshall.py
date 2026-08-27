#!/usr/bin/env python3
"""Fetch Johnshall sr_top500_whitelist_ad.conf and overlay Siri 2 / Siri 3 rules."""

from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]

TARGETS = [
    {
        "list": ROOT / "siri2.list",
        "out": ROOT / "sr_top500_whitelist_ad_siri2.conf",
        "title": "Siri 2 / Apple Intelligence / ChatGPT",
    },
    {
        "list": ROOT / "siri3.list",
        "out": ROOT / "sr_top500_whitelist_ad_siri3.conf",
        "title": "Siri 3 / iOS 27 Siri AI",
    },
]

UPSTREAMS = [
    "https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_whitelist_ad.conf",
    "https://raw.githubusercontent.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever/release/sr_top500_whitelist_ad.conf",
    "https://cdn.jsdelivr.net/gh/Johnshall/Shadowrocket-ADBlock-Rules-Forever@release/sr_top500_whitelist_ad.conf",
]


def fetch_upstream() -> str:
    last_error = None
    for url in UPSTREAMS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Shadowrocket-AppleIntelligence-bot"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read().decode("utf-8", errors="replace")
            if "[Rule]" not in data or "FINAL," not in data:
                raise ValueError(f"unexpected payload from {url}")
            print(f"fetched: {url} ({len(data)} bytes)")
            return data
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            print(f"failed {url}: {exc}")
    raise RuntimeError(f"all upstreams failed: {last_error}")


def load_ai_rules(path: pathlib.Path) -> str:
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(("DOMAIN", "IP-", "GEOIP", "PROCESS-", "USER-AGENT")):
            if line.count(",") == 1:
                line = f"{line},PROXY"
            lines.append(line)
    if not lines:
        raise RuntimeError(f"no AI rules in {path}")
    return "\n".join(lines)


def patch(base: str, ai_rules: str, now: dt.datetime, title: str) -> str:
    text = base.replace("\r\n", "\n")
    text = text.replace(", *.ls.apple.com", "").replace(",*.ls.apple.com", "")
    text = re.sub(r",\s*\*\.ls\.apple\.com", "", text)

    stamp = now.strftime("%Y-%m-%d %H:%M:%S %Z").strip()
    header = (
        f"# Johnshall sr_top500_whitelist_ad + {title}\n"
        "# base: https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever\n"
        f"# patched: {stamp}\n"
        "#\n"
    )
    idx = text.find("[General]")
    if idx < 0:
        raise RuntimeError("missing [General]")
    text = header + text[idx:]

    block = (
        "\n"
        "# ============================================================\n"
        f"# {title} (priority)\n"
        "# ============================================================\n"
        f"{ai_rules}\n"
        "# ============================================================\n\n"
    )

    marker = "# adblock rules refresh time"
    pos = text.find(marker)
    if pos < 0:
        rule_pos = text.find("[Rule]")
        if rule_pos < 0:
            raise RuntimeError("missing [Rule]")
        nl = text.find("\n", rule_pos)
        text = text[: nl + 1] + block + text[nl + 1 :]
    else:
        text = text[:pos] + block + text[pos:]
    return text


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8)))
    base = fetch_upstream()
    for item in TARGETS:
        rules = load_ai_rules(item["list"])
        patched = patch(base, rules, now, item["title"])
        item["out"].write_text(patched, encoding="utf-8")
        print(f"wrote {item['out']} ({len(patched)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
