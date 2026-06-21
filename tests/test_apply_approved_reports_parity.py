#!/usr/bin/env python3
"""Code-vs-code byte-identical parity for the existing (non-new_hydrant)
handlers, per docs/plans/h1_shared_core_spatial_dedup.md.

Primary parity proof: run the frozen pre-refactor logic (golden_apply_v0) and
the refactored shared core (scripts/lib/hydrant_core) over the same synthetic
fixtures, then assert byte-identical JSON for the resulting records, provenance,
and report. The spatial change only touches new_hydrant, so these fixtures cover
exactly the handlers that must NOT change: exists_confirmed, damaged, missing,
wrong_location, plus the shared skip paths.
"""

from __future__ import annotations

import copy
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCRIPTS = os.path.join(REPO, "scripts")
for _p in (REPO, SCRIPTS, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import golden_apply_v0 as golden  # noqa: E402  frozen pre-refactor logic
from lib import hydrant_core as core  # noqa: E402  refactored shared core


TIMESTAMP = "2026-06-21T00:00:00+03:00"
APPROVER = "petar"


def _canon(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _base_records() -> list[dict]:
    return [
        # exists_confirmed target with absent canonical fields
        {"id": "coord_27.90000_43.20000", "coords": [27.90000, 43.20000],
         "origin": "vik", "legacy_ids": []},
        # exists_confirmed target that already carries review_status
        {"id": "coord_27.91000_43.21000", "coords": [27.91000, 43.21000],
         "origin": "vik", "legacy_ids": [], "existence_status": "verified",
         "type": "подземен", "review_status": "reported"},
        # damaged target
        {"id": "coord_27.92000_43.22000", "coords": [27.92000, 43.22000],
         "origin": "vik", "legacy_ids": []},
        # missing target
        {"id": "coord_27.93000_43.23000", "coords": [27.93000, 43.23000],
         "origin": "vik", "legacy_ids": []},
        # wrong_location target (coord change inside bbox, id changes)
        {"id": "coord_27.94000_43.24000", "coords": [27.94000, 43.24000],
         "origin": "vik", "legacy_ids": []},
        # wrong_location target that will collide on its new id
        {"id": "coord_27.95000_43.25000", "coords": [27.95000, 43.25000],
         "origin": "vik", "legacy_ids": []},
        # the record the collision case bumps into
        {"id": "coord_27.96000_43.26000", "coords": [27.96000, 43.26000],
         "origin": "vik", "legacy_ids": []},
        # wrong_location target reached with an invalid coord
        {"id": "coord_27.97000_43.27000", "coords": [27.97000, 43.27000],
         "origin": "vik", "legacy_ids": []},
    ]


def _base_provenance() -> dict:
    return {r["id"]: {"source_refs": []} for r in _base_records()}


def _reports() -> list[dict]:
    return [
        # 1. exists_confirmed, absent fields -> sets existence/type/op
        {"issue_number": 101, "report_type": "exists_confirmed",
         "hydrant_id": "coord_27.90000_43.20000",
         "type": "надземен", "operational_status": "works"},
        # 2. exists_confirmed, existing review_status -> clears review_status only
        {"issue_number": 102, "report_type": "exists_confirmed",
         "hydrant_id": "coord_27.91000_43.21000"},
        # 3. damaged with canonical operational status
        {"issue_number": 103, "report_type": "damaged",
         "hydrant_id": "coord_27.92000_43.22000",
         "operational_status": "not_working"},
        # 4. missing on existing target
        {"issue_number": 104, "report_type": "missing",
         "hydrant_id": "coord_27.93000_43.23000"},
        # 5. wrong_location with coordinate change inside bbox (id changes)
        {"issue_number": 105, "report_type": "wrong_location",
         "hydrant_id": "coord_27.94000_43.24000",
         "reported_coord": [27.94500, 43.24500]},
        # 6. wrong_location exact id collision case
        {"issue_number": 106, "report_type": "wrong_location",
         "hydrant_id": "coord_27.95000_43.25000",
         "reported_coord": [27.96000, 43.26000]},
        # 7. target-not-found skip case
        {"issue_number": 107, "report_type": "exists_confirmed",
         "hydrant_id": "coord_does_not_exist"},
        # 8. invalid coord skip case
        {"issue_number": 108, "report_type": "wrong_location",
         "hydrant_id": "coord_27.97000_43.27000",
         "reported_coord": [99.0, 99.0]},
    ]


def _run(module):
    records = copy.deepcopy(_base_records())
    provenance = copy.deepcopy(_base_provenance())
    reports = copy.deepcopy(_reports())
    state, result_records = module.process(
        reports, records, provenance, timestamp=TIMESTAMP, approver_id=APPROVER)
    report = module.build_report(
        reports, result_records, approver_id=APPROVER, timestamp=TIMESTAMP,
        input_count=len(records), output_count=len(state["records"]))
    return state["records"], state["provenance"], report


class ParityTest(unittest.TestCase):
    def setUp(self):
        self.g_records, self.g_prov, self.g_report = _run(golden)
        self.c_records, self.c_prov, self.c_report = _run(core)

    def test_records_byte_identical(self):
        self.assertEqual(_canon(self.g_records), _canon(self.c_records))

    def test_provenance_byte_identical(self):
        self.assertEqual(_canon(self.g_prov), _canon(self.c_prov))

    def test_report_byte_identical(self):
        self.assertEqual(_canon(self.g_report), _canon(self.c_report))

    def test_legacy_handlers_exercised(self):
        # Guard: the parity fixtures must actually drive the four legacy handlers
        # (plus the shared skip paths), or "byte-identical" would prove nothing.
        actions = [(r.get("report_type"), r["action"]) for r in self.c_report["records"]]
        self.assertIn(("exists_confirmed", "applied"), actions)
        self.assertIn(("damaged", "applied"), actions)
        self.assertIn(("missing", "applied"), actions)
        self.assertIn(("wrong_location", "applied"), actions)
        self.assertIn(("wrong_location", "skipped"), actions)
        self.assertIn(("exists_confirmed", "skipped"), actions)

    def test_no_new_hydrant_in_parity_set(self):
        # new_hydrant is intentionally excluded: its behavior changes in H1.
        self.assertNotIn(
            "new_hydrant",
            [r.get("report_type") for r in self.c_report["records"]])


if __name__ == "__main__":
    unittest.main()
