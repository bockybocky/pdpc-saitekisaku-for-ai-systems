#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cron_expiry_check.py — Daily check PROVISIONAL charter expiry

Scans agent memory dir for PROVISIONAL charters with `shadow_expiry: YYYY-MM-DD`
in frontmatter, alerts when expiry < 7 days.

Designed for cron / scheduler daily run.

Usage:
    python cron_expiry_check.py --memory-dir ~/.agent/memory --alert-file inbox/expiry.md
"""
from __future__ import annotations
import argparse
import json
import re
from datetime import date, datetime
from pathlib import Path

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---', re.MULTILINE | re.DOTALL)
EXPIRY_RE = re.compile(r'shadow_expiry:\s*(\d{4}-\d{2}-\d{2})')
STATUS_RE = re.compile(r'status:\s*(\w+)')
NAME_RE = re.compile(r'name:\s*([\w-]+)')


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    out = {}
    expiry = EXPIRY_RE.search(block)
    if expiry:
        out['shadow_expiry'] = expiry.group(1)
    status = STATUS_RE.search(block)
    if status:
        out['status'] = status.group(1)
    name = NAME_RE.search(block)
    if name:
        out['name'] = name.group(1)
    return out


def scan_charters(memory_dir: Path) -> list[dict]:
    """Scan all .md files for PROVISIONAL charter with expiry."""
    today = date.today()
    results = []
    for p in memory_dir.rglob("*.md"):
        try:
            text = p.read_text(encoding='utf-8')
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if not fm:
            continue
        if fm.get('status') not in ('PROVISIONAL', 'DRAFT'):
            continue
        if 'shadow_expiry' not in fm:
            continue
        try:
            expiry = datetime.strptime(fm['shadow_expiry'], '%Y-%m-%d').date()
        except ValueError:
            continue
        days_left = (expiry - today).days
        results.append({
            'name': fm.get('name', p.stem),
            'path': str(p.relative_to(memory_dir)),
            'status': fm.get('status'),
            'expiry': fm['shadow_expiry'],
            'days_left': days_left,
        })
    return results


def format_alert(results: list[dict], warning_threshold: int = 7) -> str:
    """Format human-readable alert markdown."""
    expired = [r for r in results if r['days_left'] < 0]
    expiring_soon = [r for r in results if 0 <= r['days_left'] <= warning_threshold]
    healthy = [r for r in results if r['days_left'] > warning_threshold]

    lines = [
        f"# Charter Expiry Check — {date.today().isoformat()}",
        "",
        f"Total PROVISIONAL/DRAFT charters: **{len(results)}**",
        f"- 🔴 Expired: {len(expired)}",
        f"- 🟡 Expiring within {warning_threshold} days: {len(expiring_soon)}",
        f"- 🟢 Healthy (> {warning_threshold} days): {len(healthy)}",
        "",
    ]

    if expired:
        lines.append("## 🔴 Expired (overdue review)")
        for r in expired:
            lines.append(f"- **{r['name']}** ({r['path']}) — expired {-r['days_left']} days ago")
        lines.append("")

    if expiring_soon:
        lines.append(f"## 🟡 Expiring within {warning_threshold} days")
        for r in expiring_soon:
            lines.append(f"- **{r['name']}** ({r['path']}) — {r['days_left']} days left")
        lines.append("")

    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--memory-dir', type=Path, required=True,
                   help='Agent memory dir (e.g., ~/.agent/memory)')
    p.add_argument('--alert-file', type=Path, default=None,
                   help='Write alert markdown to this file (default: stdout)')
    p.add_argument('--warn-days', type=int, default=7,
                   help='Warn when expiring within N days (default: 7)')
    p.add_argument('--json', action='store_true',
                   help='Output JSON instead of markdown')
    args = p.parse_args()

    if not args.memory_dir.exists():
        print(f"ERROR: memory dir not found: {args.memory_dir}")
        return 1

    results = scan_charters(args.memory_dir)

    if args.json:
        output = json.dumps(results, indent=2, ensure_ascii=False)
    else:
        output = format_alert(results, args.warn_days)

    if args.alert_file:
        args.alert_file.parent.mkdir(parents=True, exist_ok=True)
        args.alert_file.write_text(output, encoding='utf-8')
        print(f"Alert written to: {args.alert_file}")
    else:
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
