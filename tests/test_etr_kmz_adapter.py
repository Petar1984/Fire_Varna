#!/usr/bin/env python3
"""Tests for the H2 KMZ adapter (scripts/import_etr_kmz.py).

Covers the Test Plan in docs/plans/h2_kmz_adapter_plan.md: parser, intra-batch
dedup, match classification, UPDATE/FLAG/ADD previews, ADD clustering, dry-run
safety, report shape/determinism, mojibake, and the real-data guard.

Standard library unittest/tempfile/zipfile only. All writes go to temporary
directories; the real data/*.json files are only SHA-guarded, never written.
"""

from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import math
import os
import sys
import tempfile
import unittest
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SCRIPTS = os.path.join(REPO, "scripts")
for _p in (REPO, SCRIPTS, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lib import hydrant_core as core  # noqa: E402
import import_etr_kmz as adapter  # noqa: E402


TIMESTAMP = "2026-06-22T00:00:00+03:00"


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def point_north(lon, lat, meters):
    """A point exactly `meters` due north of (lon, lat) under core.distance_m."""
    return (lon, lat + math.degrees(meters / core.EARTH_RADIUS_M))


def write_kmz(path, placemarks, *, kml_entry="doc.kml", extra_entries=None,
              with_extended=False):
    """Write a synthetic KMZ. placemarks: list of dicts with optional 'name' and
    optional 'coord'=(lon, lat, alt|None). Omitting 'coord' yields a placemark
    with no Point (a missing-coordinate case)."""
    body = []
    for pm in placemarks:
        parts = ["<Placemark>"]
        if pm.get("name") is not None:
            parts.append(f"<name>{pm['name']}</name>")
        coord = pm.get("coord")
        if coord is not None:
            lon, lat, alt = coord
            c = f"{lon},{lat}" + ("" if alt is None else f",{alt}")
            if with_extended:
                parts.append('<ExtendedData><Data name="note">'
                             '<value>ignore-me</value></Data></ExtendedData>')
            parts.append(f"<Point><coordinates>{c}</coordinates></Point>")
        parts.append("</Placemark>")
        body.append("".join(parts))
    kml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>t</name>'
           + "".join(body) + "</Document></kml>")
    with zipfile.ZipFile(path, "w") as z:
        if kml_entry is not None:
            z.writestr(kml_entry, kml.encode("utf-8"))
        for name, content in (extra_entries or []):
            z.writestr(name, content)


def make_point(lon, lat, *, idx, basename="Пожарни хидранти ЕТР Варна.kmz",
               municipality="varna", alt=None, name=""):
    origin = adapter.origin_for_municipality(municipality)
    return adapter.KmzSourcePoint(
        source_uid=adapter.source_uid_for(origin, lon, lat),
        source_file=basename, source_sha256="DEAD", municipality=municipality,
        origin=origin, placemark_index=idx, name=name, lon=lon, lat=lat, alt=alt)


def make_file(points, *, basename="Пожарни хидранти ЕТР Варна.kmz",
              municipality="varna"):
    origin = adapter.origin_for_municipality(municipality)
    return adapter.KmzFile(
        path=basename, basename=basename, municipality=municipality, origin=origin,
        sha256="DEAD", kml_entry="doc.kml", placemarks=len(points),
        points=len(points), extended_data=0, schema_data=0, missing_coords=0,
        source_points=list(points))


def single_component(point):
    return adapter.SourceComponent(
        representative=point, members=[point], member_uids=[point.source_uid],
        member_names=[point.name], cross_file=False)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_real_named_source_dir(d):
    """Create the four known KMZ basenames in dir d with small synthetic data.
    Returns the dir path. Designed to yield >=1 UPDATE, >=1 FLAG, several ADD
    when matched against the records from build_records()."""
    varna = [
        {"name": 'УЛ. "ТЕСТ"', "coord": (27.900, 43.200, 0)},          # UPDATE (on R1)
        {"name": "", "coord": (*point_north(27.900, 43.200, 6.0), 0)},  # FLAG (~6 m)
        {"name": " ", "coord": (27.950, 43.250, 0)},                    # ADD (far)
    ]
    provadia = [{"name": "", "coord": (27.44281, 43.18480, 0)}]          # ADD
    dolni = [{"name": "ALBENA@SRVGIS2", "coord": (27.72436, 42.99677, 0)}]  # ADD
    devnya = [{"name": "ALBENA@SRVGIS2", "coord": (27.62786, 43.36714, 0)}]  # ADD
    write_kmz(os.path.join(d, "Пожарни хидранти ЕТР Варна.kmz"), varna)
    write_kmz(os.path.join(d, "Пожарни хидранти ЕТР Провадия.kmz"), provadia)
    write_kmz(os.path.join(d, "Пожарни хидранти ЕТР Долни Чифлик.kmz"), dolni)
    write_kmz(os.path.join(d, "Пожарни хидранти ЕТР Девня.kmz"), devnya)
    return d


def build_records():
    return [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
             "origin": "vik", "legacy_ids": []}]


def build_provenance(records):
    return {r["id"]: {"source_refs": []} for r in records}


def run_main_over_temp(d, *, timestamp=TIMESTAMP):
    """Set up temp input/provenance/source-dir, run main(), return (rc, paths)."""
    src = os.path.join(d, "src")
    os.makedirs(src, exist_ok=True)
    build_real_named_source_dir(src)
    inp = os.path.join(d, "hydrants.json")
    prov = os.path.join(d, "provenance.json")
    jrep = os.path.join(d, "out", "report.json")
    mrep = os.path.join(d, "out", "report.md")
    records = build_records()
    core.atomic_write_json(inp, records)
    core.atomic_write_json(prov, build_provenance(records))
    argv = ["--source-dir", src, "--input", inp, "--provenance", prov,
            "--json-report", jrep, "--md-report", mrep, "--timestamp", timestamp]
    with contextlib.redirect_stdout(io.StringIO()):
        rc = adapter.main(argv)
    return rc, {"input": inp, "provenance": prov, "json": jrep, "md": mrep}


# --------------------------------------------------------------------------
# 1. Parser: one doc.kml, KML namespace, lon,lat,alt order
# --------------------------------------------------------------------------

class ParserTest(unittest.TestCase):
    def test_parses_point_lon_lat_alt_order(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [{"name": 'УЛ. "МАРА ГИДИК"', "coord": (27.9, 43.2, 5.0)}])
            f = adapter.parse_kmz(p, "varna")
            self.assertEqual(f.kml_entry, "doc.kml")
            self.assertEqual(f.points, 1)
            sp = f.source_points[0]
            self.assertEqual(sp.lon, 27.9)   # lon first
            self.assertEqual(sp.lat, 43.2)   # lat second
            self.assertEqual(sp.alt, 5.0)    # alt third, kept as context
            self.assertEqual(sp.origin, "etr_varna")
            self.assertEqual(sp.name, 'УЛ. "МАРА ГИДИК"')
            self.assertEqual(sp.source_uid, "etr_varna:27.90000000,43.20000000")

    def test_alt_optional(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [{"name": "x", "coord": (27.9, 43.2, None)}])
            f = adapter.parse_kmz(p, "varna")
            self.assertIsNone(f.source_points[0].alt)

    def test_missing_coordinates_counted(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [{"name": "has", "coord": (27.9, 43.2, 0)},
                          {"name": "none"}])  # second placemark has no Point
            f = adapter.parse_kmz(p, "varna")
            self.assertEqual(f.placemarks, 2)
            self.assertEqual(f.points, 1)
            self.assertEqual(f.missing_coords, 1)
            # placemark_index must remain the true 0-based element position.
            self.assertEqual(f.source_points[0].placemark_index, 0)


# --------------------------------------------------------------------------
# 2. Parser fails loud on missing / multiple KML
# --------------------------------------------------------------------------

class ParserFailLoudTest(unittest.TestCase):
    def test_missing_kml_raises(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [], kml_entry=None, extra_entries=[("readme.txt", "x")])
            with self.assertRaises(adapter.KmzParseError):
                adapter.parse_kmz(p, "varna")

    def test_multiple_kml_raises(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [{"name": "x", "coord": (27.9, 43.2, 0)}],
                      extra_entries=[("doc2.kml", "<kml/>")])
            with self.assertRaises(adapter.KmzParseError):
                adapter.parse_kmz(p, "varna")


# --------------------------------------------------------------------------
# 3. ExtendedData/SchemaData counted, never inferred from
# --------------------------------------------------------------------------

class ExtendedDataTest(unittest.TestCase):
    def test_extended_data_counted_not_inferred(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [{"name": "x", "coord": (27.9, 43.2, 0)}],
                      with_extended=True)
            f = adapter.parse_kmz(p, "varna")
            self.assertEqual(f.extended_data, 1)
            sp = f.source_points[0]
            # No type/status/address inferred — KmzSourcePoint carries none.
            self.assertFalse(hasattr(sp, "type"))
            self.assertFalse(hasattr(sp, "operational_status"))
            self.assertFalse(hasattr(sp, "address"))

    def test_zero_counts_like_real_files(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "a.kmz")
            write_kmz(p, [{"name": "x", "coord": (27.9, 43.2, 0)}])
            f = adapter.parse_kmz(p, "varna")
            self.assertEqual(f.extended_data, 0)
            self.assertEqual(f.schema_data, 0)


# --------------------------------------------------------------------------
# 4. Municipality mapping from exact basenames
# --------------------------------------------------------------------------

class MunicipalityMappingTest(unittest.TestCase):
    def test_known_basenames_yield_etr_origins(self):
        mapping = dict(adapter.KNOWN_KMZ)
        expected = {
            "Пожарни хидранти ЕТР Варна.kmz": "etr_varna",
            "Пожарни хидранти ЕТР Девня.kmz": "etr_devnya",
            "Пожарни хидранти ЕТР Долни Чифлик.kmz": "etr_dolni_chiflik",
            "Пожарни хидранти ЕТР Провадия.kmz": "etr_provadia",
        }
        for basename, origin in expected.items():
            self.assertIn(basename, mapping)
            self.assertEqual(
                adapter.origin_for_municipality(mapping[basename]), origin)


# --------------------------------------------------------------------------
# 5. Out-of-bbox coords reported invalid, excluded from matching
# --------------------------------------------------------------------------

class BboxGuardTest(unittest.TestCase):
    def test_out_of_bbox_excluded(self):
        good = make_point(27.9, 43.2, idx=0)
        bad = make_point(99.0, 99.0, idx=1)  # far outside Varna bbox
        f = make_file([good, bad])
        components, invalid_by_file = adapter.dedup_source_points([f])
        self.assertEqual(invalid_by_file[f.basename], 1)
        reps = {c.representative.source_uid for c in components}
        self.assertIn(good.source_uid, reps)
        self.assertNotIn(bad.source_uid, reps)


# --------------------------------------------------------------------------
# 6. Intra-batch dedup: strict <2 m connected components
# --------------------------------------------------------------------------

class DedupTest(unittest.TestCase):
    def test_collapses_under_2m(self):
        a = make_point(27.9, 43.2, idx=0)
        b = make_point(*point_north(27.9, 43.2, 1.0), idx=1)
        components, _ = adapter.dedup_source_points([make_file([a, b])])
        self.assertEqual(len(components), 1)
        self.assertEqual(len(components[0].members), 2)

    def test_transitive_chain_one_component(self):
        # A-B 1.5 m and B-C 1.5 m (A-C 3 m) must still be ONE component.
        a = make_point(27.9, 43.2, idx=0)
        b = make_point(*point_north(27.9, 43.2, 1.5), idx=1)
        c = make_point(*point_north(27.9, 43.2, 3.0), idx=2)
        components, _ = adapter.dedup_source_points([make_file([a, b, c])])
        self.assertEqual(len(components), 1)
        self.assertEqual(len(components[0].members), 3)

    def test_strict_boundary_at_2m(self):
        base = (27.9, 43.2)
        a = make_point(*base, idx=0)
        # clearly inside -> collapse
        near = make_point(*point_north(*base, 2.0 - 1e-3), idx=1)
        comps, _ = adapter.dedup_source_points([make_file([a, near])])
        self.assertEqual(len(comps), 1)
        # clearly beyond -> two components
        far = make_point(*point_north(*base, 2.0 + 1e-3), idx=1)
        comps, _ = adapter.dedup_source_points([make_file([a, far])])
        self.assertEqual(len(comps), 2)
        # exactly at the threshold follows strict-< semantics
        exact_xy = point_north(*base, 2.0)
        d = core.distance_m(base, exact_xy)
        exact = make_point(*exact_xy, idx=1)
        comps, _ = adapter.dedup_source_points([make_file([a, exact])])
        self.assertEqual(len(comps), 1 if d < 2.0 else 2)


# --------------------------------------------------------------------------
# 7. Representative deterministic under shuffled input
# --------------------------------------------------------------------------

class DedupDeterminismTest(unittest.TestCase):
    def test_representative_stable_under_shuffle(self):
        pts = [make_point(*point_north(27.9, 43.2, 0.5 * i), idx=i) for i in range(5)]
        # All within <2 m of neighbours -> one component; rep = lowest index.
        expected_rep = pts[0].source_uid
        for order in ([0, 1, 2, 3, 4], [4, 3, 2, 1, 0], [2, 0, 4, 1, 3]):
            shuffled = [pts[i] for i in order]
            comps, _ = adapter.dedup_source_points([make_file(shuffled)])
            self.assertEqual(len(comps), 1)
            self.assertEqual(comps[0].representative.source_uid, expected_rep)


# --------------------------------------------------------------------------
# 8. Classification uses H1 boundaries (Rm=5, Rf=20)
# --------------------------------------------------------------------------

class ClassificationTest(unittest.TestCase):
    def setUp(self):
        self.records = [{"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
                         "origin": "vik", "legacy_ids": []}]

    def _decide(self, meters):
        rep = make_point(*point_north(27.9, 43.2, meters), idx=0)
        cc = adapter.classify_components([single_component(rep)], self.records)[0]
        return cc

    def test_in_band_decisions(self):
        self.assertEqual(self._decide(3.0).decision, core.SpatialDecision.UPDATE)
        self.assertEqual(self._decide(6.0).decision, core.SpatialDecision.FLAG)
        self.assertEqual(self._decide(25.0).decision, core.SpatialDecision.ADD)

    def test_boundaries_match_core(self):
        # The adapter must classify exactly as the H1 core would at the measured
        # distance; this pins Rm=5/Rf=20 wiring without float fragility.
        for target in (5.0, 5.0 + 1e-6, 20.0, 20.0 + 1e-6):
            cc = self._decide(target)
            self.assertEqual(
                cc.decision,
                core.classify_spatial_match(cc.distance_m,
                                            rm_m=adapter.RM_UPDATE_LTE_M,
                                            rf_m=adapter.RF_FLAG_LTE_M))

    def test_empty_dataset_is_add(self):
        rep = make_point(27.9, 43.2, idx=0)
        cc = adapter.classify_components([single_component(rep)], [])[0]
        self.assertEqual(cc.decision, core.SpatialDecision.ADD)


# --------------------------------------------------------------------------
# 9. UPDATE preview: only legacy aliases + provenance, nothing else
# --------------------------------------------------------------------------

class UpdatePreviewTest(unittest.TestCase):
    def test_appends_only_aliases_and_provenance(self):
        rec = {"id": "coord_27.90000_43.20000", "coords": [27.9, 43.2],
               "origin": "vik", "legacy_ids": ["VIK-1"], "type": "надземен",
               "operational_status": "works", "existence_status": "verified"}
        before = copy.deepcopy(rec)
        rep = make_point(*point_north(27.9, 43.2, 1.0), idx=0)
        cc = adapter.ClassifiedComponent(
            component=single_component(rep), decision=core.SpatialDecision.UPDATE,
            nearest_record=rec, distance_m=1.0)
        preview = adapter.build_update_preview(cc, timestamp=TIMESTAMP)
        # The target record itself is NOT mutated by a preview.
        self.assertEqual(rec, before)
        # Only legacy_ids changes; the ETR alias is appended after existing ones.
        self.assertEqual(preview["old_legacy_ids"], ["VIK-1"])
        self.assertEqual(preview["new_legacy_ids"], ["VIK-1", rep.source_uid])
        self.assertEqual(preview["added_aliases"], [rep.source_uid])
        ref = preview["provenance_ref"]
        self.assertEqual(ref["manual_field"], "legacy_ids")
        self.assertEqual(ref["new_value"], ["VIK-1", rep.source_uid])
        self.assertEqual(ref["merge_action"], "kmz_etr_update_preview")
        self.assertEqual(ref["conflict_flags"], [])
        # No type/status/address/coords/origin keys in the proposed change.
        for forbidden in ("type", "operational_status", "existence_status",
                          "address", "coords", "origin"):
            self.assertNotIn(forbidden, ref.get("new_value", {}) if isinstance(
                ref.get("new_value"), dict) else {})


# --------------------------------------------------------------------------
# 10. FLAG preview mutates nothing; emits nearest id + distance
# --------------------------------------------------------------------------

class FlagPreviewTest(unittest.TestCase):
    def test_flag_leaves_data_identical(self):
        records = build_records()
        provenance = build_provenance(records)
        records_before = copy.deepcopy(records)
        prov_before = copy.deepcopy(provenance)
        rep = make_point(*point_north(27.9, 43.2, 6.0), idx=0)
        f = make_file([rep])
        report, _ = adapter.run_consolidation(
            [f], records, provenance, timestamp=TIMESTAMP)
        self.assertEqual(records, records_before)
        self.assertEqual(provenance, prov_before)
        self.assertEqual(len(report["flags"]), 1)
        row = report["flags"][0]
        self.assertEqual(row["nearest_existing_id"], "coord_27.90000_43.20000")
        self.assertEqual(row["reason"], "spatial_near_match")
        self.assertAlmostEqual(row["distance_m"], 6.0, places=2)
        self.assertTrue(row["flag_id"].startswith("FLAG-"))


# --------------------------------------------------------------------------
# 11. ADD preview emits only id, coords, origin, legacy_ids
# --------------------------------------------------------------------------

class AddPreviewTest(unittest.TestCase):
    def test_add_record_shape(self):
        rep = make_point(27.95, 43.25, idx=0)
        rec = adapter.build_add_record(rep, [rep.source_uid], core.CoordIdRegistry())
        self.assertEqual(set(rec.keys()), {"id", "coords", "origin", "legacy_ids"})
        self.assertEqual(rec["id"], core.canonical_coord_id(27.95, 43.25))
        self.assertEqual(rec["coords"], [27.95, 43.25])
        self.assertEqual(rec["origin"], "etr_varna")
        self.assertEqual(rec["legacy_ids"], [rep.source_uid])


# --------------------------------------------------------------------------
# 12. ADD clustering: strict <5 m collapse
# --------------------------------------------------------------------------

class AddClusterTest(unittest.TestCase):
    def _add_cc(self, lon, lat, idx):
        rep = make_point(lon, lat, idx=idx)
        return adapter.ClassifiedComponent(
            component=single_component(rep), decision=core.SpatialDecision.ADD,
            nearest_record=None, distance_m=None)

    def test_strict_5m_boundary(self):
        base = (27.95, 43.25)
        f = make_file([])  # only basename/file_order needed
        # 4 m apart -> one cluster
        cands = [self._add_cc(*base, 0),
                 self._add_cc(*point_north(*base, 4.0), 1)]
        groups = adapter.cluster_add_candidates(
            cands, registry=core.CoordIdRegistry(), files=[f])
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["candidate_count"], 2)
        # 5 m + epsilon apart -> two clusters
        cands = [self._add_cc(*base, 0),
                 self._add_cc(*point_north(*base, 5.0 + 1e-3), 1)]
        groups = adapter.cluster_add_candidates(
            cands, registry=core.CoordIdRegistry(), files=[f])
        self.assertEqual(len(groups), 2)
        # exactly 5 m follows strict-< semantics
        exact_xy = point_north(*base, 5.0)
        d = core.distance_m(base, exact_xy)
        cands = [self._add_cc(*base, 0), self._add_cc(*exact_xy, 1)]
        groups = adapter.cluster_add_candidates(
            cands, registry=core.CoordIdRegistry(), files=[f])
        self.assertEqual(len(groups), 1 if d < 5.0 else 2)


# --------------------------------------------------------------------------
# 13. Dry-run CLI: no --apply; never writes input/provenance
# --------------------------------------------------------------------------

class CliDryRunTest(unittest.TestCase):
    def test_apply_flag_present_and_dry_run_default(self):
        # H4 added an explicit --apply; dry-run is still the default (no flag).
        parser = adapter.build_parser()
        option_strings = [s for a in parser._actions for s in a.option_strings]
        self.assertIn("--apply", option_strings)
        self.assertIn("--flag-queue", option_strings)
        self.assertIn("--apply-report", option_strings)
        self.assertFalse(parser.parse_args([]).apply)        # default dry-run
        self.assertTrue(parser.parse_args(["--apply"]).apply)  # explicit opt-in

    def test_input_and_provenance_untouched(self):
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_main_over_temp(d)
            self.assertEqual(rc, 0)
            with open(paths["input"], encoding="utf-8") as f:
                self.assertEqual(json.load(f), build_records())
            with open(paths["provenance"], encoding="utf-8") as f:
                self.assertEqual(json.load(f), build_provenance(build_records()))
            # Reports were written.
            self.assertTrue(os.path.exists(paths["json"]))
            self.assertTrue(os.path.exists(paths["md"]))


# --------------------------------------------------------------------------
# 14. Report JSON contains summary, per-file, E0 reconciliation, FLAG rows
# --------------------------------------------------------------------------

class ReportShapeTest(unittest.TestCase):
    def test_report_sections_present(self):
        with tempfile.TemporaryDirectory() as d:
            _, paths = run_main_over_temp(d)
            with open(paths["json"], encoding="utf-8") as f:
                report = json.load(f)
        self.assertEqual(report["schema_version"], adapter.SCHEMA_VERSION)
        self.assertEqual(report["mode"], "dry_run")
        for key in ("summary", "per_file", "e0_reconciliation", "flags",
                    "add_groups", "inputs", "thresholds_m"):
            self.assertIn(key, report)
        self.assertTrue(report["update_groups_summary_only"])
        self.assertEqual(len(report["per_file"]), 4)
        s = report["summary"]
        for key in ("raw_kmz_points", "deduped_source_points", "updated",
                    "flagged", "added", "add_candidates_collapsed",
                    "intra_batch_duplicates_collapsed",
                    "projected_output_count_if_applied"):
            self.assertIn(key, s)
        e0 = report["e0_reconciliation"]
        for key in ("e0_raw_independent", "h2_post_dedup", "deltas",
                    "reduction_attribution", "explanation"):
            self.assertIn(key, e0)
        self.assertEqual(e0["e0_raw_independent"]["updated"], 3237)
        self.assertEqual(e0["e0_raw_independent"]["flagged"], 318)
        self.assertEqual(e0["e0_raw_independent"]["added"], 1305)
        # The synthetic batch produces >=1 UPDATE, >=1 FLAG, >=1 ADD.
        self.assertGreaterEqual(s["updated"], 1)
        self.assertGreaterEqual(s["flagged"], 1)
        self.assertGreaterEqual(s["added"], 1)
        self.assertEqual(len(report["flags"]), s["flagged"])
        # Per-file rows reconcile: reps == updated + flagged + add_candidates.
        for pf in report["per_file"]:
            self.assertEqual(
                pf["dedup_representatives"],
                pf["updated"] + pf["flagged"] + pf["add_candidates"])


# --------------------------------------------------------------------------
# 15. Report sort order deterministic across runs
# --------------------------------------------------------------------------

class DeterminismTest(unittest.TestCase):
    def test_two_runs_byte_identical(self):
        # Same inputs + same paths + same timestamp must produce byte-identical
        # output. (Different temp dirs would differ only in the recorded paths,
        # which is not what "deterministic sort order" means.)
        with tempfile.TemporaryDirectory() as d:
            _, paths = run_main_over_temp(d)
            first_json = _sha256(paths["json"])
            first_md = _sha256(paths["md"])
            rc, _ = run_main_over_temp(d)  # rebuild + rerun over the same paths
            self.assertEqual(rc, 0)
            self.assertEqual(_sha256(paths["json"]), first_json)
            self.assertEqual(_sha256(paths["md"]), first_md)


# --------------------------------------------------------------------------
# 16. Mojibake scan passes reports with Cyrillic content
# --------------------------------------------------------------------------

class MojibakeTest(unittest.TestCase):
    def test_cyrillic_report_passes_scan(self):
        with tempfile.TemporaryDirectory() as d:
            _, paths = run_main_over_temp(d)
            with open(paths["json"], encoding="utf-8") as f:
                report = json.load(f)
        # Names/filenames are Cyrillic; the scan must not raise.
        core.mojibake_scan("report", report)
        self.assertIn("Варна", json.dumps(report, ensure_ascii=False))


# --------------------------------------------------------------------------
# 17. Real-data guard (mirrors H1): real data/*.json untouched by a full cycle
# --------------------------------------------------------------------------

class RealDataGuardTest(unittest.TestCase):
    def test_real_data_files_untouched_by_full_cycle(self):
        real = [os.path.join(REPO, "data", "hydrants.json"),
                os.path.join(REPO, "data", "hydrants_provenance.json")]
        present = [p for p in real if os.path.exists(p)]
        if not present:
            self.skipTest("real data files not present")
        before = {p: _sha256(p) for p in present}
        with tempfile.TemporaryDirectory() as d:
            rc, _ = run_main_over_temp(d)
            self.assertEqual(rc, 0)
        after = {p: _sha256(p) for p in present}
        self.assertEqual(before, after)


# --------------------------------------------------------------------------
# H4 signed apply (docs/plans/h4_kmz_apply_plan.md). All writes go to temp dirs;
# the synthetic batch uses adapter.NO_FIXED_EXPECTATIONS so any size is allowed.
# --------------------------------------------------------------------------

KMZ_BASENAMES = {
    "varna": "Пожарни хидранти ЕТР Варна.kmz",
    "provadia": "Пожарни хидранти ЕТР Провадия.kmz",
    "dolni_chiflik": "Пожарни хидранти ЕТР Долни Чифлик.kmz",
    "devnya": "Пожарни хидранти ЕТР Девня.kmz",
}


def write_source_dir(d, *, varna=(), provadia=(), dolni=(), devnya=()):
    """Write the four required KMZ basenames with caller-supplied placemarks.
    Any municipality may be empty; load_source_dir still needs all four files."""
    write_kmz(os.path.join(d, KMZ_BASENAMES["varna"]), list(varna))
    write_kmz(os.path.join(d, KMZ_BASENAMES["provadia"]), list(provadia))
    write_kmz(os.path.join(d, KMZ_BASENAMES["dolni_chiflik"]), list(dolni))
    write_kmz(os.path.join(d, KMZ_BASENAMES["devnya"]), list(devnya))
    return d


def run_apply_over_temp(d, *, records, provenance=None, timestamp=TIMESTAMP,
                        expected=None, varna=(), provadia=(), dolni=(), devnya=(),
                        via_main=False, apply_report_name="apply_report.json"):
    """Set up temp input/provenance/source-dir, run the apply path, return
    (rc_or_exc, paths). Uses NO_FIXED_EXPECTATIONS unless overridden."""
    src = os.path.join(d, "src")
    os.makedirs(src, exist_ok=True)
    write_source_dir(src, varna=varna, provadia=provadia, dolni=dolni, devnya=devnya)
    inp = os.path.join(d, "hydrants.json")
    prov = os.path.join(d, "provenance.json")
    jrep = os.path.join(d, "out", "h2_report.json")
    mrep = os.path.join(d, "out", "h2_report.md")
    fq = os.path.join(d, "out", "flag_queue.json")
    arep = os.path.join(d, "out", apply_report_name)
    if provenance is None:
        provenance = build_provenance(records)
    core.atomic_write_json(inp, records)
    core.atomic_write_json(prov, provenance)
    argv = ["--source-dir", src, "--input", inp, "--provenance", prov,
            "--json-report", jrep, "--md-report", mrep,
            "--flag-queue", fq, "--apply-report", arep,
            "--timestamp", timestamp, "--apply"]
    paths = {"input": inp, "provenance": prov, "json": jrep, "md": mrep,
             "flag_queue": fq, "apply_report": arep, "src": src}
    if via_main:
        with contextlib.redirect_stdout(io.StringIO()):
            rc = adapter.main(argv)
        return rc, paths
    args = adapter.build_parser().parse_args(argv)
    with contextlib.redirect_stdout(io.StringIO()):
        rc = adapter.run_apply(args, timestamp,
                               expected=expected or adapter.NO_FIXED_EXPECTATIONS)
    return rc, paths


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# A standard mixed batch against build_records() (one R1 at 27.900, 43.200):
#   varna: UPDATE on R1, FLAG ~6 m, ADD far; + one ADD per other municipality.
STD_VARNA = [
    {"name": 'УЛ. "ТЕСТ"', "coord": (27.900, 43.200, 0)},            # UPDATE (0 m)
    {"name": "", "coord": (*point_north(27.900, 43.200, 6.0), 0)},   # FLAG (~6 m)
    {"name": " ", "coord": (27.950, 43.250, 0)},                     # ADD (far)
]
STD_PROVADIA = [{"name": "", "coord": (27.44281, 43.18480, 0)}]      # ADD
STD_DOLNI = [{"name": "x", "coord": (27.72436, 42.99677, 0)}]        # ADD
STD_DEVNYA = [{"name": "y", "coord": (27.62786, 43.36714, 0)}]       # ADD
STD_BATCH = dict(varna=STD_VARNA, provadia=STD_PROVADIA,
                 dolni=STD_DOLNI, devnya=STD_DEVNYA)
# This batch yields: applied_updates=1, applied_adds=4, queued_flags=1.


class ApplyUpdateTest(unittest.TestCase):
    def test_apply_updates_append_only_etr_alias_and_provenance(self):
        rec = {"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
               "origin": "vik", "legacy_ids": ["VIK-1"], "type": "надземен",
               "operational_status": "works", "existence_status": "verified",
               "address": "ул. Тест 1", "review_status": "reported"}
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=[copy.deepcopy(rec)],
                varna=[{"name": "n", "coord": (27.900, 43.200, 0)}])
            self.assertEqual(rc, 0)
            out = _load(paths["input"])
            self.assertEqual(len(out), 1)            # UPDATE never adds a record
            target = out[0]
            alias = "etr_varna:27.90000000,43.20000000"
            # Every field except legacy_ids is byte-identical to the original.
            for k, v in rec.items():
                if k == "legacy_ids":
                    continue
                self.assertEqual(target[k], v, f"field {k} must not change")
            self.assertEqual(set(target.keys()), set(rec.keys()))  # no new fields
            self.assertEqual(target["legacy_ids"], ["VIK-1", alias])  # appended
            # Provenance: exactly one appended ref, kmz_etr_update, ETR-attributed.
            refs = _load(paths["provenance"])["coord_27.90000_43.20000"]["source_refs"]
            self.assertEqual(len(refs), 1)
            ref = refs[0]
            self.assertEqual(ref["merge_action"], "kmz_etr_update")
            self.assertEqual(ref["attribution"], "confirmed by ETR")
            self.assertEqual(ref["manual_field"], "legacy_ids")
            self.assertEqual(ref["old_value"], ["VIK-1"])
            self.assertEqual(ref["new_value"], ["VIK-1", alias])
            self.assertEqual(ref["source_uids"], [alias])
            self.assertEqual(ref["conflict_flags"], [])

    def test_duplicate_coordinate_sources_append_alias_once(self):
        # ArcGIS KMZ exports repeat placemarks at identical coordinates; both
        # share one source_uid and must not land in legacy_ids more than once.
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": ["VIK-1"]}]
        alias = "etr_varna:27.90000000,43.20000000"
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=copy.deepcopy(recs),
                varna=[{"name": "a", "coord": (27.900, 43.200, 0)},   # same coord
                       {"name": "b", "coord": (27.900, 43.200, 0)},   # twice
                       {"name": "c", "coord": (27.900, 43.200, 0)}])  # thrice
            self.assertEqual(rc, 0)
            out = _load(paths["input"])
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0]["legacy_ids"], ["VIK-1", alias])  # exactly once
            refs = _load(paths["provenance"])["coord_27.90000_43.20000"]["source_refs"]
            self.assertEqual(refs[0]["source_uids"], [alias])  # provenance single

    def test_update_does_not_change_record_count(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": []}]
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=copy.deepcopy(recs),
                varna=[{"name": "n", "coord": (27.900, 43.200, 0)}])  # only UPDATE
            self.assertEqual(rc, 0)
            out = _load(paths["input"])
            self.assertEqual(len(out), len(recs))   # 1 -> 1
            report = _load(paths["apply_report"])
            self.assertEqual(report["summary"]["applied_updates"], 1)
            self.assertEqual(report["summary"]["applied_adds"], 0)
            self.assertEqual(report["summary"]["record_count_after"], 1)


class ApplyAddTest(unittest.TestCase):
    def test_add_shape_and_real_coordinate(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": []}]
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=copy.deepcopy(recs),
                varna=[{"name": "z", "coord": (27.950, 43.250, 0)}])  # one far ADD
            self.assertEqual(rc, 0)
            out = _load(paths["input"])
            self.assertEqual(len(out), 2)
            added = [r for r in out if r["id"] != "coord_27.90000_43.20000"][0]
            # Exactly the four allowed keys, real KMZ coordinate, etr_ origin.
            self.assertEqual(set(added.keys()), {"id", "coords", "origin", "legacy_ids"})
            self.assertEqual(added["coords"], [27.950, 43.250])
            self.assertEqual(added["id"], core.canonical_coord_id(27.950, 43.250))
            self.assertEqual(added["origin"], "etr_varna")
            self.assertEqual(added["legacy_ids"], ["etr_varna:27.95000000,43.25000000"])

    def test_add_creates_provenance(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": []}]
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=copy.deepcopy(recs),
                varna=[{"name": "z", "coord": (27.950, 43.250, 0)}])
            self.assertEqual(rc, 0)
            prov = _load(paths["provenance"])
            new_id = core.canonical_coord_id(27.950, 43.250)
            self.assertIn(new_id, prov)
            refs = prov[new_id]["source_refs"]
            self.assertEqual(len(refs), 1)
            self.assertEqual(refs[0]["merge_action"], "kmz_etr_add")
            self.assertEqual(refs[0]["attribution"], "confirmed by ETR")
            self.assertEqual(refs[0]["manual_field"], "new_record")
            self.assertEqual(refs[0]["new_value"]["id"], new_id)


class ApplyFlagTest(unittest.TestCase):
    def test_flag_not_applied_and_queue_written(self):
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": []}]
        prov = build_provenance(recs)
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=copy.deepcopy(recs), provenance=copy.deepcopy(prov),
                varna=[{"name": "f", "coord": (*point_north(27.900, 43.200, 6.0), 0)}])
            self.assertEqual(rc, 0)
            # Record + provenance unchanged (FLAG mutates nothing).
            self.assertEqual(_load(paths["input"]), recs)
            self.assertEqual(_load(paths["provenance"]), prov)
            queue = _load(paths["flag_queue"])
            self.assertEqual(queue["schema_version"], adapter.FLAG_QUEUE_SCHEMA_VERSION)
            self.assertEqual(queue["count"], 1)
            row = queue["flags"][0]
            self.assertEqual(row["queue_status"], "pending_manual_review")
            self.assertTrue(row["flag_id"].startswith("FLAG-"))
            self.assertEqual(row["nearest_existing_id"], "coord_27.90000_43.20000")


class ApplyCountsTest(unittest.TestCase):
    def test_apply_first_run_counts(self):
        recs = build_records()
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(d, records=copy.deepcopy(recs), **STD_BATCH)
            self.assertEqual(rc, 0)
            s = _load(paths["apply_report"])["summary"]
            self.assertEqual(s["applied_updates"], 1)
            self.assertEqual(s["applied_adds"], 4)
            self.assertEqual(s["queued_flags"], 1)
            self.assertEqual(s["noop_updates"], 0)
            self.assertEqual(s["noop_adds"], 0)
            self.assertEqual(s["record_count_after"], 1 + 4)
            self.assertEqual(s["provenance_count_after"], 1 + 4)


class ApplyIdempotencyTest(unittest.TestCase):
    def test_apply_idempotent_second_run_noop(self):
        recs = build_records()
        with tempfile.TemporaryDirectory() as d:
            rc1, paths = run_apply_over_temp(d, records=copy.deepcopy(recs), **STD_BATCH)
            self.assertEqual(rc1, 0)
            data_after_first = _sha256(paths["input"])
            prov_after_first = _sha256(paths["provenance"])
            queue_after_first = _sha256(paths["flag_queue"])
            first = _load(paths["apply_report"])["summary"]
            self.assertEqual(first["applied_updates"], 1)
            self.assertEqual(first["applied_adds"], 4)

            # Second run over the SAME (already-applied) temp files.
            src = paths["src"]
            args = adapter.build_parser().parse_args(
                ["--source-dir", src, "--input", paths["input"],
                 "--provenance", paths["provenance"],
                 "--json-report", paths["json"], "--md-report", paths["md"],
                 "--flag-queue", paths["flag_queue"],
                 "--apply-report", paths["apply_report"],
                 "--timestamp", TIMESTAMP, "--apply"])
            with contextlib.redirect_stdout(io.StringIO()):
                rc2 = adapter.run_apply(args, TIMESTAMP,
                                        expected=adapter.NO_FIXED_EXPECTATIONS)
            self.assertEqual(rc2, 0)
            second = _load(paths["apply_report"])["summary"]
            self.assertEqual(second["applied_updates"], 0)
            self.assertEqual(second["applied_adds"], 0)
            self.assertEqual(second["noop_updates"], 1)
            self.assertEqual(second["noop_adds"], 4)
            self.assertEqual(second["queued_flags"], 1)
            self.assertEqual(second["record_count_before"], 5)
            self.assertEqual(second["record_count_after"], 5)
            # Data + provenance + queue are byte-identical after the no-op run.
            self.assertEqual(_sha256(paths["input"]), data_after_first)
            self.assertEqual(_sha256(paths["provenance"]), prov_after_first)
            self.assertEqual(_sha256(paths["flag_queue"]), queue_after_first)


class ApplyCollisionTest(unittest.TestCase):
    def test_alias_collision_aborts(self):
        alias = "etr_varna:27.90000000,43.20000000"
        recs = [
            {"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
             "origin": "vik", "legacy_ids": []},                  # UPDATE target
            {"id": "coord_27.80000_43.10000", "coords": [27.800, 43.100],
             "origin": "vik", "legacy_ids": [alias]},             # alias bound here
        ]
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(adapter.ApplyError):
                run_apply_over_temp(
                    d, records=copy.deepcopy(recs),
                    varna=[{"name": "n", "coord": (27.900, 43.200, 0)}])
            # Nothing was written to the protected files (still the originals).
            self.assertEqual(_load(os.path.join(d, "hydrants.json")), recs)
            self.assertFalse(os.path.exists(os.path.join(d, "out", "apply_report.json")))

    def test_add_id_collision_aborts(self):
        coll_id = core.canonical_coord_id(27.950, 43.250)
        recs = [
            {"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
             "origin": "vik", "legacy_ids": []},
            {"id": coll_id, "coords": [27.960, 43.260],   # same id, DIFFERENT coords
             "origin": "vik", "legacy_ids": []},
        ]
        prov = build_provenance(recs)
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(adapter.ApplyError):
                run_apply_over_temp(
                    d, records=copy.deepcopy(recs), provenance=copy.deepcopy(prov),
                    varna=[{"name": "z", "coord": (27.950, 43.250, 0)}])
            self.assertEqual(_load(os.path.join(d, "hydrants.json")), recs)
            self.assertEqual(_load(os.path.join(d, "provenance.json")), prov)
            self.assertFalse(os.path.exists(os.path.join(d, "out", "apply_report.json")))


class ApplyPartialTest(unittest.TestCase):
    def test_partial_apply_detected(self):
        # Two source points <2 m apart collapse into one UPDATE component with two
        # member aliases. Preload only ONE of them -> some-but-not-all -> abort.
        a1 = "etr_varna:27.90000000,43.20000000"
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": [a1]}]   # only the first alias
        p1 = (27.900, 43.200, 0)
        p2 = (*point_north(27.900, 43.200, 1.0), 0)      # 1 m -> same component
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(adapter.ApplyError):
                run_apply_over_temp(
                    d, records=copy.deepcopy(recs),
                    varna=[{"name": "a", "coord": p1}, {"name": "b", "coord": p2}])
            self.assertEqual(_load(os.path.join(d, "hydrants.json")), recs)

    def test_alias_present_without_provenance_detected(self):
        # Record already carries the ETR alias but provenance lacks the H4 ref:
        # an inconsistent partial state that must abort, not silently re-noop.
        alias = "etr_varna:27.90000000,43.20000000"
        recs = [{"id": "coord_27.90000_43.20000", "coords": [27.900, 43.200],
                 "origin": "vik", "legacy_ids": [alias]}]
        prov = {"coord_27.90000_43.20000": {"source_refs": []}}   # no kmz_etr_update
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(adapter.ApplyError):
                run_apply_over_temp(
                    d, records=copy.deepcopy(recs), provenance=copy.deepcopy(prov),
                    varna=[{"name": "n", "coord": (27.900, 43.200, 0)}])


class ApplyBaselineGuardTest(unittest.TestCase):
    def test_main_uses_signed_baseline_by_default(self):
        # main() routes --apply through SIGNED_EXPECTATIONS; synthetic data is not
        # the signed 5911/SHA baseline, so the real-data guard must fire.
        recs = build_records()
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(adapter.ApplyError):
                run_apply_over_temp(d, records=copy.deepcopy(recs),
                                    via_main=True, **STD_BATCH)


class ApplyAllowedPathsTest(unittest.TestCase):
    def test_only_allowed_paths_written(self):
        recs = build_records()
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(d, records=copy.deepcopy(recs), **STD_BATCH)
            self.assertEqual(rc, 0)
            # The four allowed outputs exist...
            for key in ("input", "provenance", "flag_queue", "apply_report"):
                self.assertTrue(os.path.exists(paths[key]), key)
            # ...and the H2 dry-run reports were NOT written by apply mode.
            self.assertFalse(os.path.exists(paths["json"]))
            self.assertFalse(os.path.exists(paths["md"]))


class ApplyReportShapeTest(unittest.TestCase):
    def test_apply_report_shape(self):
        recs = build_records()
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(d, records=copy.deepcopy(recs), **STD_BATCH)
            self.assertEqual(rc, 0)
            report = _load(paths["apply_report"])
        self.assertEqual(report["schema_version"], adapter.APPLY_SCHEMA_VERSION)
        self.assertEqual(report["mode"], "apply")
        hj = report["inputs"]["hydrants_json"]
        for key in ("sha256_before", "sha256_after", "record_count_before",
                    "record_count_after"):
            self.assertIn(key, hj)
        self.assertEqual(hj["record_count_before"], 1)
        self.assertEqual(hj["record_count_after"], 5)
        self.assertNotEqual(hj["sha256_before"], hj["sha256_after"])
        pj = report["inputs"]["provenance_json"]
        self.assertEqual(pj["record_count_before"], 1)
        self.assertEqual(pj["record_count_after"], 5)
        self.assertEqual(len(report["per_file"]), 4)
        for pf in report["per_file"]:
            for key in ("source_file", "municipality", "applied_updates",
                        "applied_adds", "queued_flags", "noop_updates", "noop_adds"):
                self.assertIn(key, pf)
        val = report["validation"]
        self.assertTrue(val["dry_run_default_preserved"])
        self.assertTrue(val["only_allowed_paths_written"])
        self.assertTrue(val["mojibake_scan_passed"])
        self.assertEqual(val["duplicate_ids_after"], 0)
        self.assertEqual(val["missing_provenance_after"], 0)
        self.assertEqual(val["unexpected_field_mutations"], 0)
        for key in ("hydrants_json", "provenance_json", "flag_queue", "apply_report"):
            self.assertIn(key, report["output_files"])
        # Per-file rows reconcile with the summary totals.
        self.assertEqual(sum(pf["applied_updates"] for pf in report["per_file"]),
                         report["summary"]["applied_updates"])
        self.assertEqual(sum(pf["applied_adds"] for pf in report["per_file"]),
                         report["summary"]["applied_adds"])
        self.assertEqual(sum(pf["queued_flags"] for pf in report["per_file"]),
                         report["summary"]["queued_flags"])


class ApplyMojibakeTest(unittest.TestCase):
    def test_mojibake_scan_runs_on_apply_outputs(self):
        # Cyrillic placemark names + filenames must pass the scan clean.
        recs = build_records()
        with tempfile.TemporaryDirectory() as d:
            rc, paths = run_apply_over_temp(
                d, records=copy.deepcopy(recs),
                varna=[{"name": 'УЛ. "МАРА ГИДИК"', "coord": (27.900, 43.200, 0)},
                       {"name": "Хидрант №7", "coord": (27.950, 43.250, 0)}],
                provadia=STD_PROVADIA, dolni=STD_DOLNI, devnya=STD_DEVNYA)
            self.assertEqual(rc, 0)
            for key in ("input", "provenance", "flag_queue", "apply_report"):
                obj = _load(paths[key])
                core.mojibake_scan(key, obj)   # must not raise on clean Cyrillic
            self.assertIn("Варна", json.dumps(_load(paths["apply_report"]),
                                              ensure_ascii=False))
        # The scan still catches a constructed mojibake byte sequence:
        # U+00D0 immediately followed by U+00FF matches core's regex.
        with self.assertRaises(AssertionError):
            core.mojibake_scan("bad", {"x": "\u00d0\u00ff"})


if __name__ == "__main__":
    unittest.main()
