#!/usr/bin/env python3
"""Apply GitHub-issue reports labeled 'approved' (and not 'ingested') to
data/hydrants.json + provenance. Per Section B6 of
docs/audits/backfill_and_submission_extension_plan_20260509.md.

Default is dry-run; --apply writes. Single-admin: --approver-id ("petar")
goes into every provenance entry. Multi-admin extension points: grep
MULTI-ADMIN.

H1 refactor (docs/plans/h1_shared_core_spatial_dedup.md): the reusable
match/merge/provenance/pipeline logic now lives in scripts/lib/hydrant_core.py.
This file remains the issue adapter: Worker fetch, argparse, summary printing,
and dry-run/apply write selection.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

# Make scripts/lib importable whether this file is run directly or imported as
# a module (e.g. by the test suite) from any working directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.hydrant_core import (  # noqa: E402
    atomic_write_json,
    build_report,
    default_timestamp,
    ingested_issue_numbers,
    load_json,
    mojibake_scan,
    process,
)


DEFAULT_WORKER_URL = "https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues"

# Worker per_page upper bound. Pagination is not supported; if the approved
# backlog ever exceeds this, ingest must run more frequently or the Worker
# needs a paging contract.
WORKER_MAX_REPORTS = 100


# ---------- Worker fetch ----------

def fetch_approved_reports(worker_url: str) -> list[dict]:
    """GET /issues, return reports labeled 'approved' and not 'ingested'."""
    sep = "&" if "?" in worker_url else "?"
    url = f"{worker_url}{sep}limit={WORKER_MAX_REPORTS}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "apply_approved_reports/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                raise SystemExit(f"Worker GET failed: HTTP {resp.status}")
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise SystemExit(f"Worker GET failed: {exc}")
    reports = payload.get("reports")
    if not isinstance(reports, list):
        raise SystemExit("Worker response missing 'reports' array")
    return [
        r for r in reports
        if "approved" in (r.get("labels") or []) and "ingested" not in (r.get("labels") or [])
    ]


# ---------- Summary printing ----------

def print_summary(s):
    print("Apply approved reports summary")
    for k in ("worker_url", "approver_id", "timestamp", "fetched_count",
              "applied_count", "skipped_count", "input_count", "output_count"):
        print(f"  {k+':':16s} {s.get(k, '')}")
    for label, key in (("skip_reasons", "skipped_reasons"),
                       ("by_report_type", "by_report_type")):
        if s.get(key):
            print(f"  {label}:")
            for k, v in sorted(s[key].items()):
                print(f"    {k}: {v}")


# ---------- CLI ----------

def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--worker-url", default=DEFAULT_WORKER_URL)
    parser.add_argument("--input", required=True)
    parser.add_argument("--provenance", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--timestamp", default=None,
                        help="ISO-8601 timestamp recorded in provenance entries. "
                             "Defaults to current local time.")
    parser.add_argument("--approver-id", default="petar",
                        help="Approver identity recorded in provenance. "
                             "Single-admin model; multi-admin sprint will "
                             "derive this from authenticated user.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if args.apply and args.dry_run:
        parser.error("--apply and --dry-run are mutually exclusive")
    timestamp = args.timestamp or default_timestamp()

    records = load_json(args.input)
    provenance = load_json(args.provenance)
    input_count = len(records)

    reports = fetch_approved_reports(args.worker_url)
    state, result_records = process(
        reports, records, provenance,
        timestamp=timestamp, approver_id=args.approver_id,
    )

    mojibake_scan("hydrants", state["records"])
    mojibake_scan("provenance", state["provenance"])
    report = build_report(
        reports, result_records,
        approver_id=args.approver_id, timestamp=timestamp,
        input_count=input_count, output_count=len(state["records"]),
    )
    mojibake_scan("report", report)

    s = dict(report["summary"])
    s["worker_url"] = args.worker_url
    print_summary(s)

    if args.apply:
        atomic_write_json(args.input, state["records"])
        atomic_write_json(args.provenance, state["provenance"])
        atomic_write_json(args.report, report, indent=2)
        print(f"Wrote: {args.input}")
        print(f"Wrote: {args.provenance}")
        print(f"Wrote: {args.report}")
        ingested = ingested_issue_numbers(result_records)
        if ingested:
            print()
            print("After review of these changes, manually add label 'ingested'")
            print("and remove label 'approved' on these issues in GitHub:")
            for n in ingested:
                print(f"  #{n}")
    else:
        print()
        print("Dry run only; no files written. Use --apply to write changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
