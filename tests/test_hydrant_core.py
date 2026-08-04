#!/usr/bin/env python3
"""Tests for the H1 shared core: spatial matcher, new_hydrant UPDATE/FLAG/ADD,
and the safety invariants from docs/plans/h1_shared_core_spatial_dedup.md.

Standard library unittest only. All writes go to temporary directories; no test
reads or writes the real data/*.json files except to assert they stay untouched.
"""

from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import math
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCRIPTS = os.path.join(REPO, "scripts")
for _p in (REPO, SCRIPTS, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lib import hydrant_core as core  # noqa: E402
import apply_approved_reports as adapter  # noqa: E402


TIMESTAMP = "2026-06-21T00:00:00+03:00"
APPROVER = "petar"


def point_north(lon, lat, meters):
    """A point exactly `meters` due north of (lon, lat) under core.distance_m.

    A pure-latitude offset has zero east/west term, so core.distance_m returns
    the offset back exactly (modulo float rounding) — handy for building points
    at a known distance."""
    return (lon, lat + math.degrees(meters / core.EARTH_RADIUS_M))


def make_state(records, provenance=None):
    """Build the in-memory state dict the handlers operate on."""
    records = copy.deepcopy(records)
    if provenance is None:
        provenance = {r["id"]: {"source_refs": []} for r in records}
    else:
        provenance = copy.deepcopy(provenance)
    return {
        "records": records,
        "provenance": provenance,
        "alias": core.build_alias_index(records),
    }


# --------------------------------------------------------------------------
# Spatial matcher
# --------------------------------------------------------------------------

class SpatialMatcherTest(unittest.TestCase):
    def test_distance_north_offset_is_exact(self):
        a = (27.9, 43.2)
        b = point_north(27.9, 43.2, 12.0)
        self.assertAlmostEqual(core.distance_m(a, b), 12.0, places=6)

    def test_classify_boundaries(self):
        # <= Rm UPDATE, (Rm, Rf] FLAG, > Rf ADD; None -> ADD.
        self.assertEqual(core.classify_spatial_match(0.0), core.SpatialDecision.UPDATE)
        self.assertEqual(core.classify_spatial_match(5.0), core.SpatialDecision.UPDATE)
        self.assertEqual(core.classify_spatial_match(5.0 + 1e-9), core.SpatialDecision.FLAG)
        self.assertEqual(core.classify_spatial_match(20.0), core.SpatialDecision.FLAG)
        self.assertEqual(core.classify_spatial_match(20.0 + 1e-9), core.SpatialDecision.ADD)
        self.assertEqual(core.classify_spatial_match(None), core.SpatialDecision.ADD)

    def test_match_point_1m_update(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                 "origin": "vik", "legacy_ids": []}]
        m = core.match_point(point_north(27.9, 43.2, 1.0), recs)
        self.assertEqual(m.decision, core.SpatialDecision.UPDATE)
        self.assertAlmostEqual(m.distance_m, 1.0, places=4)
        self.assertEqual(m.nearest_record["id"], "coord_27.90000_43.20000")

    def test_match_point_6m_flag(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                 "origin": "vik", "legacy_ids": []}]
        m = core.match_point(point_north(27.9, 43.2, 6.0), recs)
        self.assertEqual(m.decision, core.SpatialDecision.FLAG)
        self.assertAlmostEqual(m.distance_m, 6.0, places=4)

    def test_match_point_25m_add(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                 "origin": "vik", "legacy_ids": []}]
        m = core.match_point(point_north(27.9, 43.2, 25.0), recs)
        self.assertEqual(m.decision, core.SpatialDecision.ADD)

    def test_match_point_no_records_add(self):
        m = core.match_point((27.9, 43.2), [])
        self.assertEqual(m.decision, core.SpatialDecision.ADD)
        self.assertIsNone(m.nearest_record)
        self.assertIsNone(m.distance_m)

    def test_tie_break_by_id(self):
        # Two records equidistant (north/south); nearest must be the smaller id.
        north = point_north(27.9, 43.2, 7.0)
        south = (27.9, 43.2 - (north[1] - 43.2))
        recs = [
            {"id": "id_b", "coords": list(north), "origin": "vik", "legacy_ids": []},
            {"id": "id_a", "coords": list(south), "origin": "vik", "legacy_ids": []},
        ]
        nearest, dist = core.find_nearest_hydrant((27.9, 43.2), recs)
        self.assertEqual(nearest["id"], "id_a")
        # Order independence.
        nearest2, _ = core.find_nearest_hydrant((27.9, 43.2), list(reversed(recs)))
        self.assertEqual(nearest2["id"], "id_a")
        self.assertAlmostEqual(dist, 7.0, places=4)


# --------------------------------------------------------------------------
# new_hydrant UPDATE  (distance <= Rm)
# --------------------------------------------------------------------------

class NewHydrantUpdateTest(unittest.TestCase):
    def setUp(self):
        self.existing = {
            "id": "coord_27.90000_43.20000",
            "coords": [27.90000, 43.20000],
            "origin": "vik",
            "legacy_ids": [],
            "type": "подземен",
            "operational_status": "not_working",
            "review_status": "reported",
        }
        self.state = make_state([self.existing])
        self.report = {
            "issue_number": 321,
            "report_type": "new_hydrant",
            "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            "reported_coord": list(point_north(27.90000, 43.20000, 1.0)),
            "type": "надземен",
            "operational_status": "works",
        }
        self.res = core.apply_new_hydrant(self.state, self.report, TIMESTAMP, APPROVER)
        self.rec = self.state["records"][0]

    def test_record_count_unchanged(self):
        self.assertEqual(len(self.state["records"]), 1)

    def test_existing_id_and_coords_unchanged(self):
        self.assertEqual(self.rec["id"], "coord_27.90000_43.20000")
        self.assertEqual(self.rec["coords"], [27.90000, 43.20000])

    def test_review_status_untouched(self):
        self.assertEqual(self.rec["review_status"], "reported")

    def test_aliases_added_exactly_once(self):
        self.assertEqual(
            self.rec["legacy_ids"],
            ["aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee", "field_aaaaaaaa"])

    def test_existence_status_verified(self):
        self.assertEqual(self.rec["existence_status"], "verified")

    def test_report_wins_type(self):
        self.assertEqual(self.rec["type"], "надземен")

    def test_report_wins_operational_status(self):
        self.assertEqual(self.rec["operational_status"], "works")

    def test_provenance_appended_to_matched_id(self):
        refs = self.state["provenance"]["coord_27.90000_43.20000"]["source_refs"]
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["report_type"], "new_hydrant")
        self.assertEqual(refs[0]["old_id"], "coord_27.90000_43.20000")
        self.assertEqual(refs[0]["old_coord"], [27.90000, 43.20000])

    def test_provenance_contains_old_values(self):
        ref = self.state["provenance"]["coord_27.90000_43.20000"]["source_refs"][0]
        # Multiple fields changed -> old_value is the dict of old values.
        self.assertEqual(ref["manual_field"], "multiple")
        self.assertEqual(ref["old_value"]["type"], "подземен")
        self.assertEqual(ref["old_value"]["operational_status"], "not_working")

    def test_provenance_contains_distance(self):
        ref = self.state["provenance"]["coord_27.90000_43.20000"]["source_refs"][0]
        self.assertIn("distance_m", ref)
        self.assertAlmostEqual(ref["distance_m"], 1.0, places=2)

    def test_result_row(self):
        self.assertEqual(self.res["action"], "applied")
        self.assertEqual(self.res["spatial_decision"], "UPDATE")
        self.assertIn("distance_m", self.res)
        self.assertEqual(self.res["target_id_before"], "coord_27.90000_43.20000")
        self.assertEqual(self.res["target_id_after"], "coord_27.90000_43.20000")

    def test_ingested_includes_issue(self):
        self.assertIn(321, core.ingested_issue_numbers([self.res]))


# --------------------------------------------------------------------------
# new_hydrant FLAG  (Rm < distance <= Rf)
# --------------------------------------------------------------------------

class NewHydrantFlagTest(unittest.TestCase):
    def setUp(self):
        self.existing = {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                         "origin": "vik", "legacy_ids": []}
        self.state = make_state([self.existing])
        self.before_records = copy.deepcopy(self.state["records"])
        self.before_prov = copy.deepcopy(self.state["provenance"])
        self.report = {
            "issue_number": 654,
            "report_type": "new_hydrant",
            "id": "ffffffff-0000-1111-2222-333333333333",
            "reported_coord": list(point_north(27.9, 43.2, 6.0)),
            "type": "надземен",
        }
        self.res = core.apply_new_hydrant(self.state, self.report, TIMESTAMP, APPROVER)

    def test_record_count_unchanged(self):
        self.assertEqual(len(self.state["records"]), 1)

    def test_records_object_unchanged(self):
        self.assertEqual(self.state["records"], self.before_records)

    def test_provenance_unchanged(self):
        self.assertEqual(self.state["provenance"], self.before_prov)

    def test_result_is_flagged(self):
        self.assertEqual(self.res["action"], "flagged")
        self.assertEqual(self.res["flag_reason"], "spatial_near_match")
        self.assertEqual(self.res["nearest_id"], "coord_27.90000_43.20000")
        self.assertAlmostEqual(self.res["distance_m"], 6.0, places=2)

    def test_build_report_includes_flagged_count_only_when_flagged(self):
        rep = core.build_report(
            [self.report], [self.res], approver_id=APPROVER, timestamp=TIMESTAMP,
            input_count=1, output_count=1)
        self.assertEqual(rep["summary"]["flagged_count"], 1)
        self.assertEqual(rep["summary"]["flagged_reasons"], {"spatial_near_match": 1})
        # A run with no flagged results must not carry the flagged keys.
        applied = {"issue_number": 1, "report_type": "missing", "action": "applied",
                   "target_id_before": "x", "target_id_after": "x", "changes": {}}
        rep2 = core.build_report(
            [], [applied], approver_id=APPROVER, timestamp=TIMESTAMP,
            input_count=1, output_count=1)
        self.assertNotIn("flagged_count", rep2["summary"])
        self.assertNotIn("flagged_reasons", rep2["summary"])

    def test_flagged_issue_not_ingested(self):
        self.assertNotIn(654, core.ingested_issue_numbers([self.res]))


# --------------------------------------------------------------------------
# new_hydrant ADD  (distance > Rf)
# --------------------------------------------------------------------------

class NewHydrantAddTest(unittest.TestCase):
    def setUp(self):
        # An existing record far away (100 m) so the report is a genuine ADD.
        self.existing = {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                         "origin": "vik", "legacy_ids": []}
        self.state = make_state([self.existing])
        self.report = {
            "issue_number": 777,
            "report_type": "new_hydrant",
            "id": "12345678-aaaa-bbbb-cccc-dddddddddddd",
            "reported_coord": list(point_north(27.9, 43.2, 100.0)),
            "type": "надземен",
            "operational_status": "works",
            "reported_at": "2026-05-11T15:55:12+03:00",
        }
        self.res = core.apply_new_hydrant(self.state, self.report, TIMESTAMP, APPROVER)
        self.new_id = self.res["target_id_after"]

    def test_record_count_increases_by_one(self):
        self.assertEqual(len(self.state["records"]), 2)

    def test_new_record_shape(self):
        rec = next(r for r in self.state["records"] if r["id"] == self.new_id)
        self.assertEqual(rec["origin"], "field_report")
        self.assertEqual(rec["existence_status"], "verified")
        self.assertEqual(rec["type"], "надземен")
        self.assertEqual(rec["operational_status"], "works")
        self.assertEqual(rec["report_id"], "12345678-aaaa-bbbb-cccc-dddddddddddd")
        self.assertEqual(rec["reported_at"], "2026-05-11T15:55:12+03:00")
        self.assertEqual(
            rec["legacy_ids"],
            ["12345678-aaaa-bbbb-cccc-dddddddddddd", "field_12345678"])

    def test_aliases_registered(self):
        self.assertIn(self.new_id, self.state["alias"])
        self.assertIn("12345678-aaaa-bbbb-cccc-dddddddddddd", self.state["alias"])
        self.assertIn("field_12345678", self.state["alias"])

    def test_new_provenance_shape(self):
        refs = self.state["provenance"][self.new_id]["source_refs"]
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0]["report_type"], "new_hydrant")
        self.assertIsNone(refs[0]["old_id"])
        self.assertIsNone(refs[0]["old_coord"])
        # ADD provenance keeps the legacy new-record shape: no distance_m.
        self.assertNotIn("distance_m", refs[0])

    def test_result_keeps_legacy_add_shape(self):
        self.assertEqual(self.res["action"], "applied")
        self.assertIsNone(self.res["target_id_before"])
        self.assertIn("created", self.res["changes"])
        # ADD result row is the pre-H1 shape (no spatial_decision key).
        self.assertNotIn("spatial_decision", self.res)

    def test_add_when_dataset_empty(self):
        state = make_state([])
        report = dict(self.report, issue_number=778,
                      reported_coord=[27.9, 43.2])
        res = core.apply_new_hydrant(state, report, TIMESTAMP, APPROVER)
        self.assertEqual(res["action"], "applied")
        self.assertEqual(len(state["records"]), 1)


# --------------------------------------------------------------------------
# Idempotency: exact-id collision still skips
# --------------------------------------------------------------------------

class IdempotencyTest(unittest.TestCase):
    def test_exact_id_collision_skips(self):
        existing = {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                    "origin": "vik", "legacy_ids": []}
        state = make_state([existing])
        before = copy.deepcopy(state["records"])
        report = {"issue_number": 999, "report_type": "new_hydrant",
                  "id": "dup", "reported_coord": [27.90000, 43.20000]}
        res = core.apply_new_hydrant(state, report, TIMESTAMP, APPROVER)
        self.assertEqual(res["action"], "skipped")
        self.assertEqual(res["skip_reason"], "id_collision")
        self.assertEqual(state["records"], before)


# --------------------------------------------------------------------------
# Damaged handler (renders 'broken' / black)
# --------------------------------------------------------------------------

class DamagedTest(unittest.TestCase):
    """apply_damaged marks the target verified + not_working and clears the
    review gate so it renders as the 'broken' (black) status. Supersedes the old
    B6 behaviour that left damaged hydrants stuck at review_status='reported'
    (yellow) with no path to black."""

    def _run(self, existing):
        state = make_state([existing])
        report = {"issue_number": 55, "report_type": "damaged",
                  "hydrant_id": existing["id"], "operational_status": "not_working"}
        res = core.apply_damaged(state, report, TIMESTAMP, APPROVER)
        return res, state["records"][0]

    @staticmethod
    def _status_class(h):
        # Mirrors index.html hydrantStatusClass precedence.
        if h.get("review_status") in ("reported", "pending_review"):
            return "reported"
        if h.get("existence_status") == "verified" and h.get("operational_status") == "works":
            return "operational"
        if h.get("existence_status") == "verified" and h.get("operational_status") == "not_working":
            return "broken"
        if h.get("existence_status") == "verified":
            return "verified"
        return "canonical"

    def test_sets_verified_and_not_working(self):
        res, rec = self._run(
            {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
             "origin": "vik", "legacy_ids": []})
        self.assertEqual(res["action"], "applied")
        self.assertEqual(rec["existence_status"], "verified")
        self.assertEqual(rec["operational_status"], "not_working")

    def test_clears_review_status(self):
        # A previously reported (yellow) hydrant loses the review gate.
        _, rec = self._run(
            {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
             "origin": "vik", "legacy_ids": [], "review_status": "reported"})
        self.assertNotIn("review_status", rec)

    def test_renders_broken_black(self):
        _, rec = self._run(
            {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
             "origin": "vik", "legacy_ids": [], "review_status": "reported"})
        self.assertEqual(self._status_class(rec), "broken")


# --------------------------------------------------------------------------
# Safety invariants
# --------------------------------------------------------------------------

class SafetyTest(unittest.TestCase):
    def test_missing_never_removes_record(self):
        rec = {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
               "origin": "vik", "legacy_ids": []}
        state = make_state([rec])
        report = {"issue_number": 10, "report_type": "missing",
                  "hydrant_id": "coord_27.90000_43.20000"}
        res = core.apply_missing(state, report, TIMESTAMP, APPROVER)
        self.assertEqual(res["action"], "applied")
        self.assertEqual(len(state["records"]), 1)
        self.assertEqual(state["records"][0]["review_status"], "reported")

    def test_bbox_guard_rejects_invalid_new_hydrant(self):
        state = make_state([])
        for bad in ([99.0, 99.0], [27.9], None, "x", [27.9, "y"]):
            report = {"issue_number": 11, "report_type": "new_hydrant",
                      "id": "x", "reported_coord": bad}
            res = core.apply_new_hydrant(state, report, TIMESTAMP, APPROVER)
            self.assertEqual(res["action"], "skipped")
            self.assertEqual(res["skip_reason"], "missing_or_invalid_coord")
        self.assertEqual(len(state["records"]), 0)

    def test_bbox_guard_rejects_invalid_wrong_location(self):
        rec = {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
               "origin": "vik", "legacy_ids": []}
        state = make_state([rec])
        report = {"issue_number": 12, "report_type": "wrong_location",
                  "hydrant_id": "coord_27.90000_43.20000",
                  "reported_coord": [99.0, 99.0]}
        res = core.apply_wrong_location(state, report, TIMESTAMP, APPROVER)
        self.assertEqual(res["skip_reason"], "missing_or_invalid_coord")
        self.assertEqual(state["records"][0]["coords"], [27.9, 43.2])

    def test_atomic_write_only_in_given_temp_dir(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "out.json")
            core.atomic_write_json(path, {"k": "надземен"})
            self.assertTrue(os.path.exists(path))
            self.assertEqual(os.path.commonpath([d, os.path.abspath(path)]), d)
            with open(path, encoding="utf-8") as f:
                self.assertEqual(json.load(f), {"k": "надземен"})

    def test_real_data_files_untouched_by_full_cycle(self):
        # Running a full process + write cycle against temp copies must not
        # touch the real data/*.json files.
        real = [os.path.join(REPO, "data", "hydrants.json"),
                os.path.join(REPO, "data", "hydrants_provenance.json")]
        present = [p for p in real if os.path.exists(p)]
        if not present:
            self.skipTest("real data files not present")
        before = {p: _sha256(p) for p in present}
        with tempfile.TemporaryDirectory() as d:
            recs = [{"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                     "origin": "vik", "legacy_ids": []}]
            reports = [{"issue_number": 1, "report_type": "new_hydrant",
                        "id": "z", "reported_coord": list(point_north(27.9, 43.2, 50.0))}]
            state, results = core.process(reports, recs, {p["id"]: {"source_refs": []} for p in recs},
                                          timestamp=TIMESTAMP, approver_id=APPROVER)
            core.atomic_write_json(os.path.join(d, "hydrants.json"), state["records"])
            core.atomic_write_json(os.path.join(d, "provenance.json"), state["provenance"])
        after = {p: _sha256(p) for p in present}
        self.assertEqual(before, after)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# --------------------------------------------------------------------------
# Adapter CLI: dry-run default, --apply writes, mutual exclusion
# --------------------------------------------------------------------------

class AdapterCliTest(unittest.TestCase):
    def _setup_files(self, d):
        inp = os.path.join(d, "hydrants.json")
        prov = os.path.join(d, "provenance.json")
        rep = os.path.join(d, "report.json")
        core.atomic_write_json(inp, [])
        core.atomic_write_json(prov, {})
        return inp, prov, rep

    def _run_main(self, argv):
        old_argv = sys.argv
        old_fetch = adapter.fetch_approved_reports
        # Stub the network: one new_hydrant report into an empty dataset -> ADD.
        adapter.fetch_approved_reports = lambda url: [{
            "issue_number": 5, "report_type": "new_hydrant", "id": "cli-uuid",
            "reported_coord": [27.9, 43.2], "type": "надземен"}]
        try:
            sys.argv = argv
            with contextlib.redirect_stdout(io.StringIO()):
                return adapter.main()
        finally:
            sys.argv = old_argv
            adapter.fetch_approved_reports = old_fetch

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            inp, prov, rep = self._setup_files(d)
            rc = self._run_main(["x", "--input", inp, "--provenance", prov,
                                 "--report", rep, "--timestamp", TIMESTAMP])
            self.assertEqual(rc, 0)
            self.assertFalse(os.path.exists(rep), "dry-run must not write the report")
            with open(inp, encoding="utf-8") as f:
                self.assertEqual(json.load(f), [])  # input untouched
            with open(prov, encoding="utf-8") as f:
                self.assertEqual(json.load(f), {})  # provenance untouched

    def test_apply_writes_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            inp, prov, rep = self._setup_files(d)
            rc = self._run_main(["x", "--input", inp, "--provenance", prov,
                                 "--report", rep, "--timestamp", TIMESTAMP, "--apply"])
            self.assertEqual(rc, 0)
            self.assertTrue(os.path.exists(rep))
            with open(inp, encoding="utf-8") as f:
                records = json.load(f)
            self.assertEqual(len(records), 1)  # the ADD landed
            self.assertEqual(records[0]["origin"], "field_report")

    def test_apply_and_dry_run_mutually_exclusive(self):
        proc = subprocess.run(
            [sys.executable, os.path.join(SCRIPTS, "apply_approved_reports.py"),
             "--input", "i", "--provenance", "p", "--report", "r",
             "--apply", "--dry-run"],
            capture_output=True, text=True)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("mutually exclusive", proc.stderr)


# --------------------------------------------------------------------------
# Encoding: serialized mojibake scan
# --------------------------------------------------------------------------

class EncodingTest(unittest.TestCase):
    def test_clean_cyrillic_passes(self):
        core.mojibake_scan("ok", {"type": "надземен", "op": "подземен"})

    def test_mojibake_detected(self):
        # Build the bad sequence from code points (U+00D0 then U+00FF) so this
        # source file carries no literal mojibake bytes for the repo scanner.
        bad = chr(0x00D0) + chr(0x00FF)
        with self.assertRaises(AssertionError):
            core.mojibake_scan("bad", {"t": bad})


# --------------------------------------------------------------------------
# verifier_note: the reporter's free text has to survive ingest
# --------------------------------------------------------------------------

class VerifierNoteTest(unittest.TestCase):
    """Before this, a reporter's note only lived in the transient open-issue
    feed and vanished the moment the report was ingested and the issue closed.
    The handlers now persist it as `verifier_note`, which the frontend popup
    already knows how to render."""

    BASE = [{"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
             "origin": "vik", "legacy_ids": []}]

    def _apply(self, report, records=None):
        state = make_state(records if records is not None else self.BASE)
        res = core.apply_exists_confirmed(state, report, TIMESTAMP, APPROVER)
        return state, res

    def test_note_is_persisted(self):
        state, _ = self._apply({"issue_number": 1, "hydrant_id": self.BASE[0]["id"],
                                "report_type": "exists_confirmed",
                                "comment": "деформиран, но работи"})
        self.assertEqual(state["records"][0]["verifier_note"], "деформиран, но работи")

    def test_note_is_trimmed(self):
        state, _ = self._apply({"issue_number": 1, "hydrant_id": self.BASE[0]["id"],
                                "report_type": "exists_confirmed",
                                "comment": "  капакът е затрупан  "})
        self.assertEqual(state["records"][0]["verifier_note"], "капакът е затрупан")

    def test_absent_or_blank_note_writes_nothing(self):
        for comment in (None, "", "   ", 42):
            with self.subTest(comment=comment):
                state, _ = self._apply({"issue_number": 1, "hydrant_id": self.BASE[0]["id"],
                                        "report_type": "exists_confirmed", "comment": comment})
                self.assertNotIn("verifier_note", state["records"][0])

    def test_later_note_replaces_earlier(self):
        """Petar's rule (2026-08-01): newest information wins; the old value
        stays recoverable through the provenance entry."""
        existing = copy.deepcopy(self.BASE)
        existing[0]["verifier_note"] = "стара бележка"
        state, res = self._apply({"issue_number": 2, "hydrant_id": existing[0]["id"],
                                  "report_type": "exists_confirmed",
                                  "comment": "нова бележка"}, records=existing)
        self.assertEqual(state["records"][0]["verifier_note"], "нова бележка")
        self.assertEqual(res["changes"]["verifier_note"]["old"], "стара бележка")

    def test_missing_report_keeps_note_with_yellow_flag(self):
        state = make_state(self.BASE)
        core.apply_missing(state, {"issue_number": 3, "hydrant_id": self.BASE[0]["id"],
                                   "report_type": "missing",
                                   "comment": "няма и следа от шахта"}, TIMESTAMP, APPROVER)
        rec = state["records"][0]
        self.assertEqual(rec["review_status"], "reported")
        self.assertEqual(rec["verifier_note"], "няма и следа от шахта")

    def test_new_hydrant_add_carries_note(self):
        state = make_state(self.BASE)
        far = point_north(27.9, 43.2, 500)
        res = core.apply_new_hydrant(state, {"issue_number": 4, "report_type": "new_hydrant",
                                             "reported_coord": [far[0], far[1]],
                                             "comment": "зад трафопоста"}, TIMESTAMP, APPROVER)
        created = res["changes"]["created"]
        self.assertEqual(created["verifier_note"], "зад трафопоста")

    def test_golden_and_core_agree_on_notes(self):
        """The parity fixtures do not exercise notes, so pin the two
        implementations together explicitly — an edit to one without the other
        would otherwise slip through."""
        import golden_apply_v0 as golden
        report = {"issue_number": 5, "hydrant_id": self.BASE[0]["id"],
                  "report_type": "exists_confirmed", "comment": "  еднакво  "}
        c_state = make_state(self.BASE)
        core.apply_exists_confirmed(c_state, report, TIMESTAMP, APPROVER)
        g_records = copy.deepcopy(self.BASE)
        g_state = {"records": g_records, "provenance": {r["id"]: {"source_refs": []} for r in g_records},
                   "alias": golden.build_alias_index(g_records)}
        golden.apply_exists_confirmed(g_state, report, TIMESTAMP, APPROVER)
        self.assertEqual(json.dumps(c_state["records"], ensure_ascii=False, sort_keys=True),
                         json.dumps(g_state["records"], ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
