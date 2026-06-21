#!/usr/bin/env python3
"""Supplementary replay: which historical new_hydrant issues would the H1
spatial matcher classify differently?

Per docs/plans/h1_shared_core_spatial_dedup.md ("Supplementary historical
check"). This is read-only and is NOT the primary parity proof — that is the
code-vs-code synthetic test (tests/test_apply_approved_reports_parity.py). It
reconstructs each historical new_hydrant reported coordinate from the audit
ingest reports and runs the H1 matcher against the pre-ingest dataset snapshot
to show the UPDATE / FLAG / ADD class each would now fall into.

Important framing required by the plan: this reconstruction does NOT prove
historical Worker payload parity. It only surfaces the class of entries the new
logic would resolve differently. Reads only; writes nothing.

Run:
    python scripts/replay_historical_new_hydrant.py
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.hydrant_core import (  # noqa: E402
    DEFAULT_RF_M,
    DEFAULT_RM_M,
    match_point,
)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "data")
AUDIT = os.path.join(REPO, "audit", "ingest_reports")

# Pre-ingest dataset snapshot (5,901 records, before the May 28 ingest of these
# issues). The created records are absent here, so each report's nearest match
# is a genuine pre-existing hydrant — exactly what the planning probe measured.
SNAPSHOT = os.path.join(DATA, "hydrants.json.pre_address_backfill.json")
INGEST_REPORTS = [
    os.path.join(AUDIT, "ingest_2026-05-28.json"),
    os.path.join(AUDIT, "ingest_2026-05-28_batch.json"),
]


def reconstruct_new_hydrant_points():
    """(issue_number, (lon, lat), provenance_note) for every historical report
    that was — originally — a new_hydrant, recovered from the audit reports."""
    points = []
    for path in INGEST_REPORTS:
        report = json.load(open(path, encoding="utf-8"))
        for row in report.get("records", []):
            if row.get("report_type") == "new_hydrant" and row.get("action") == "applied":
                coords = row.get("changes", {}).get("created", {}).get("coords")
                if coords:
                    points.append((row["issue_number"], tuple(coords),
                                   "applied as new_hydrant"))
        # Overrides record issues whose ORIGINAL report was new_hydrant but which
        # were applied differently. Recover the reported coordinate from the
        # rationale text when it is the only place it survives (e.g. #46).
        for ovr in report.get("overrides", []):
            if ovr.get("original_report_type") == "new_hydrant":
                pt = _coord_from_rationale(ovr.get("rationale", ""))
                if pt is not None:
                    points.append((ovr["issue_number"], pt,
                                   "original new_hydrant, applied as "
                                   + ovr.get("applied_report_type", "?")))
    return points


def _coord_from_rationale(text):
    """Pull a `[lon, lat]` pair out of an override rationale string."""
    start = text.find("[")
    end = text.find("]", start)
    if start == -1 or end == -1:
        return None
    try:
        lon, lat = (float(x) for x in text[start + 1:end].split(","))
    except ValueError:
        return None
    return (lon, lat)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    if not os.path.exists(SNAPSHOT):
        print(f"Snapshot not found: {SNAPSHOT}", file=sys.stderr)
        return 1

    records = json.load(open(SNAPSHOT, encoding="utf-8"))
    points = reconstruct_new_hydrant_points()

    rows = []
    for issue, point, note in points:
        m = match_point(point, records, rm_m=DEFAULT_RM_M, rf_m=DEFAULT_RF_M)
        nearest = m.nearest_record["id"] if m.nearest_record else None
        rows.append((issue, m.decision, nearest, m.distance_m, note))
    rows.sort(key=lambda r: r[0])

    print("Historical new_hydrant replay vs H1 spatial matcher "
          f"(Rm={DEFAULT_RM_M:.0f} m, Rf={DEFAULT_RF_M:.0f} m)")
    print(f"Dataset snapshot: {os.path.relpath(SNAPSHOT, REPO)} "
          f"({len(records)} records)")
    print("Supplementary reconstruction only; NOT a historical parity proof.")
    print()
    print(f"{'issue':>6}  {'decision':<8}  {'nearest_existing':<28}  "
          f"{'distance_m':>10}  note")
    print("-" * 92)
    for issue, decision, nearest, dist, note in rows:
        dist_s = f"{dist:.2f}" if dist is not None else "n/a"
        print(f"{('#' + str(issue)):>6}  {decision:<8}  {str(nearest):<28}  "
              f"{dist_s:>10}  {note}")

    diverging = [r for r in rows if r[1] != "ADD"]
    print()
    print("Entries the H1 logic would resolve as NOT a plain ADD "
          "(i.e. differently from the historical add-only path):")
    if diverging:
        for issue, decision, nearest, dist, note in diverging:
            print(f"  #{issue}: {decision} @ {dist:.2f} m -> {nearest}  ({note})")
    else:
        print("  (none)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
