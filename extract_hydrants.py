#!/usr/bin/env python3
"""Extract embedded hydrant JSON from index.html. Does NOT modify index.html."""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
INDEX = REPO / "index.html"
DATA_DIR = REPO / "data"
DATA_FILE = DATA_DIR / "hydrants.json"

PATTERN = re.compile(
    r'<script id="hydrantData" type="application/json">(.*?)</script>',
    re.DOTALL
)


def main():
    if not INDEX.exists():
        sys.exit(f"ERROR: {INDEX} not found")
    html = INDEX.read_text(encoding="utf-8")
    print(f"Read index.html: {len(html):,} bytes")
    match = PATTERN.search(html)
    if not match:
        sys.exit("ERROR: hydrantData script tag not found")
    json_text = match.group(1).strip()
    print(f"Extracted JSON: {len(json_text):,} bytes")
    try:
        records = json.loads(json_text)
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: Invalid JSON: {e}")
    if not isinstance(records, list):
        sys.exit(f"ERROR: Expected list, got {type(records).__name__}")
    print(f"Records: {len(records):,}")
    origins, statuses = {}, {}
    for rec in records:
        o = rec.get("o", "?")
        origins[o] = origins.get(o, 0) + 1
        s = rec.get("status", "(none)")
        statuses[s] = statuses.get(s, 0) + 1
    print("\nOrigins:")
    for k, v in sorted(origins.items()):
        print(f"  {k}: {v}")
    print("\nStatuses:")
    for k, v in sorted(statuses.items()):
        print(f"  {k}: {v}")
    DATA_DIR.mkdir(exist_ok=True)
    DATA_FILE.write_text(json_text, encoding="utf-8")
    print(f"\nWrote {DATA_FILE}: {DATA_FILE.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
