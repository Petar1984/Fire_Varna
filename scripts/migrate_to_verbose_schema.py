#!/usr/bin/env python3
"""
Migrate data/hydrants.json from compact runtime schema to verbose canonical schema.

Per docs/audits/cleanup_execution_plan_20260508.md Sections 2A-2H.

Inputs:
  --input data/hydrants.json                  Current compact runtime data
  --field-reports field_reports.json          Field-report archive (deleted on live run)

Outputs (live run only; --dry-run prints summary and writes nothing):
  --output data/hydrants.json                 Rewritten verbose canonical data
  --provenance data/hydrants_provenance.json  NEW source provenance archive
  --report docs/audits/cleanup_migration_report_20260508.json  NEW per-record reconciliation

Halts with nonzero exit on any assertion failure.
"""

import argparse
import json
import math
import os
import sys
import tempfile
from collections import Counter, OrderedDict, defaultdict


# Earth radius (m) used for Haversine — matches data_audit methodology
EARTH_RADIUS_M = 6371008.8
DEDUP_RADIUS_M = 5.0

# Varna conservative coordinate bbox
LON_MIN, LON_MAX = 26.5, 28.5
LAT_MIN, LAT_MAX = 42.7, 44.0

# Expected input invariants (plan Section 2C step 1)
EXPECTED_INPUT_COUNT = 6082
EXPECTED_ORIGINS_INPUT = {"vik": 3661, "national": 2407, "field_report": 14}
EXPECTED_LEGACY_STATUS_INPUT = {"verified": 23, "reported": 2}
EXPECTED_LEGACY_STATUS_ABSENT = 6057

# Expected output invariants (plan Section 2C summary)
EXPECTED_OUTPUT_COUNT = 5901
EXPECTED_OUTPUT_ORIGINS = {"field_report": 14, "national": 2345, "vik": 3542}
EXPECTED_TYPES = {"надземен": 1144, "подземен": 1147}
EXPECTED_TYPE_ABSENT = 3610
EXPECTED_C3_RECORDS = 27
EXPECTED_MERGED_DELTA = 181

# Q13A — 17 records whose raw type is ambiguous; surviving canonical records get type=null
Q13A_OLD_IDS = frozenset({
    "VIK-VARNA_IZTOK-0200", "VIK-VARNA_IZTOK-0201", "VIK-VARNA_IZTOK-0203",
    "VIK-VARNA_IZTOK-0204", "VIK-VARNA_IZTOK-0205", "VIK-VARNA_IZTOK-0206",
    "VIK-VARNA_IZTOK-0207", "272", "273", "277", "VIK-VARNA_ZAPAD-0149",
    "VIK-VARNA_ZAPAD-0203", "VIK-VARNA_ZAPAD-0204", "VIK-VARNA_ZAPAD-0205",
    "VIK-VARNA_ZAPAD-0207", "600", "398",
})

# Type normalization (plan Section 4 + Petar 2026-05-09)
TYPE_DIRECT_MAP = {
    "ground": "надземен",
    "underground": "подземен",
    "ПКн": "надземен",
    "ПХ 70/80": "надземен",
    "ПХ DN 80": "надземен",
    "70/80": None,   # Q13A — deferred
    "ПК1": None,     # Q13A — deferred
}

# Origin priority for duplicate winner selection (lower wins)
ORIGIN_PRIORITY = {"field_report": 0, "national": 1, "vik": 2}


# ---------- Geo + clustering ----------

def haversine_m(lon1, lat1, lon2, lat2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * EARTH_RADIUS_M * math.asin(math.sqrt(a))


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


# ---------- Type normalization ----------

def normalize_type(raw):
    """Return normalized Bulgarian type, None (Q13A / empty), or raise on unknown."""
    if raw is None:
        return None
    s = str(raw).strip()
    if s == "":
        return None
    if s in TYPE_DIRECT_MAP:
        return TYPE_DIRECT_MAP[s]
    # case-insensitive Bulgarian substring fallback
    lower = s.lower()
    if "надземен" in lower:
        return "надземен"
    if "подземен" in lower:
        return "подземен"
    raise ValueError(f"unexpected type value: {s!r}")


# ---------- Input validation ----------

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_input(records, field_reports):
    """Assert all input invariants from plan Section 2C step 1."""
    assert len(records) == EXPECTED_INPUT_COUNT, (
        f"input count {len(records)} != expected {EXPECTED_INPUT_COUNT}")

    origins = Counter(r["o"] for r in records)
    for origin, expected in EXPECTED_ORIGINS_INPUT.items():
        assert origins.get(origin, 0) == expected, (
            f"origin {origin}: got {origins.get(origin, 0)}, expected {expected}")
    extra = set(origins) - set(EXPECTED_ORIGINS_INPUT)
    assert not extra, f"unexpected origins: {extra}"

    status_present = Counter(r["status"] for r in records if "status" in r)
    status_absent = sum(1 for r in records if "status" not in r)
    for st, expected in EXPECTED_LEGACY_STATUS_INPUT.items():
        assert status_present.get(st, 0) == expected, (
            f"legacy status {st}: got {status_present.get(st, 0)}, expected {expected}")
    assert status_absent == EXPECTED_LEGACY_STATUS_ABSENT, (
        f"legacy status absent: got {status_absent}, expected {EXPECTED_LEGACY_STATUS_ABSENT}")

    ids = [r["i"] for r in records]
    assert len(set(ids)) == len(ids), "duplicate i values found"

    for r in records:
        c = r["c"]
        assert isinstance(c, list) and len(c) == 2, f"bad coord on {r['i']}: {c}"
        lon, lat = c[0], c[1]
        assert isinstance(lon, (int, float)) and isinstance(lat, (int, float)), (
            f"non-numeric coord on {r['i']}: {c}")
        assert math.isfinite(lon) and math.isfinite(lat), (
            f"non-finite coord on {r['i']}: {c}")
        assert LON_MIN <= lon <= LON_MAX and LAT_MIN <= lat <= LAT_MAX, (
            f"coord out of Varna bbox on {r['i']}: {c}")

    # field_reports equivalence
    rt_by_id = {r["i"]: r for r in records}
    for fr in field_reports:
        m = rt_by_id.get(fr["i"])
        assert m is not None, f"field_report {fr['i']} not present in runtime data"
        ja = json.dumps(fr, sort_keys=True, ensure_ascii=False)
        jb = json.dumps(m, sort_keys=True, ensure_ascii=False)
        assert ja == jb, f"field_report {fr['i']} differs byte-wise from runtime record"


# ---------- Cluster detection ----------

def exact_coord_clusters(records, decimals=6):
    fmt = f"%.{decimals}f"
    grouped = defaultdict(list)
    for idx, r in enumerate(records):
        lon, lat = r["c"]
        key = (fmt % lon, fmt % lat)
        grouped[key].append(idx)
    return grouped


def detect_c3_clusters(records, exact_clusters):
    """A C3 cluster has size>=2 AND contains both raw `ground` and `underground` t values."""
    c3 = []
    for key, idxs in exact_clusters.items():
        if len(idxs) < 2:
            continue
        types = {records[i].get("t", "") for i in idxs}
        if "ground" in types and "underground" in types:
            c3.append((key, list(idxs)))
    return c3


def build_5m_components(records, c3_indices):
    """Union-find over <=5m pairs, excluding C3 records (preserved individually).

    Uses a fixed-grid spatial index keyed by 0.001-degree cells (~111 m).
    Two points within 5 m must lie in same or adjacent grid cell.
    """
    n = len(records)
    uf = UnionFind(n)
    cell = 0.001
    grid = defaultdict(list)
    for i, r in enumerate(records):
        if i in c3_indices:
            continue
        lon, lat = r["c"]
        grid[(int(lon / cell), int(lat / cell))].append(i)
    for i, r in enumerate(records):
        if i in c3_indices:
            continue
        lon, lat = r["c"]
        gx, gy = int(lon / cell), int(lat / cell)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for j in grid.get((gx + dx, gy + dy), ()):
                    if j <= i:
                        continue
                    lj, laj = records[j]["c"]
                    if haversine_m(lon, lat, lj, laj) <= DEDUP_RADIUS_M:
                        uf.union(i, j)
    components = defaultdict(list)
    for i in range(n):
        if i in c3_indices:
            continue
        components[uf.find(i)].append(i)
    return list(components.values())


# ---------- Winner selection ----------

def safe_normalized_type(raw):
    """Like normalize_type but returns None on unknown (used only for scoring)."""
    try:
        return normalize_type(raw)
    except ValueError:
        return None


def score_record(r):
    """Higher score = richer record. Tiebreaker within same origin priority."""
    s = 0
    status = r.get("status")
    if status == "verified":
        s += 1000
    elif status == "reported":
        s += 100
    if safe_normalized_type(r.get("t")) is not None:
        s += 50
    if r.get("a"):
        s += 10
    if r.get("r"):
        s += 5
    if r.get("i_original"):
        s += 2
    if r.get("replaced_vik"):
        s += 2
    if r.get("st"):
        s += 1
    if r.get("z"):
        s += 1
    return s


def pick_winner(records, indices):
    """Return the index of the winning record per origin > score > stable order."""
    return min(
        indices,
        key=lambda i: (ORIGIN_PRIORITY[records[i]["o"]], -score_record(records[i]), i),
    )


# ---------- Verbose record construction ----------

def build_verbose_record(records, winner_idx, all_indices, force_type_null, c3_suffix_old_id=None):
    """Construct the verbose runtime record for a (possibly merged) component."""
    w = records[winner_idx]
    lon, lat = w["c"]
    canonical_id = f"coord_{lon:.5f}_{lat:.5f}"
    if c3_suffix_old_id is not None:
        canonical_id = f"{canonical_id}__{c3_suffix_old_id}"

    out = {
        "id": canonical_id,
        "coords": [lon, lat],
        "origin": w["o"],
    }

    legacy = []
    for i in all_indices:
        legacy.append(records[i]["i"])
        rep_id = records[i].get("report_id")
        if rep_id and rep_id not in legacy:
            legacy.append(rep_id)
    # Always emit legacy_ids; downstream adapter relies on it for old issue dedupe
    out["legacy_ids"] = legacy

    addr = w.get("a")
    if addr:
        out["address"] = addr

    if not force_type_null:
        norm_t = normalize_type(w.get("t"))
        if norm_t is not None:
            out["type"] = norm_t
    # else: omit type entirely (Q13A / C3)

    legacy_status = w.get("status")
    if legacy_status == "verified":
        out["existence_status"] = "verified"
    elif legacy_status == "reported":
        out["review_status"] = "reported"

    region = w.get("r")
    if region:
        out["region"] = region

    rep_id = w.get("report_id")
    if rep_id:
        out["report_id"] = rep_id
    reported_at = w.get("reported_at")
    if reported_at:
        out["reported_at"] = reported_at

    return out


def build_provenance_entry(records, all_indices, winner_idx):
    """Construct the provenance archive entry for an output record."""
    refs = []
    for i in all_indices:
        r = records[i]
        ref = {
            "old_id": r["i"],
            "old_coord": list(r["c"]),
            "raw_type": r.get("t") if r.get("t") != "" else None,
            "raw_status": r.get("status"),
            "s": r.get("s") if r.get("s") != "" else None,
            "st": r.get("st") if r.get("st") != "" else None,
            "z": r.get("z") if r.get("z") != "" else None,
            "i_original": r.get("i_original"),
            "duplicate_distance_m": r.get("duplicate_distance_m"),
            "replaced_vik": r.get("replaced_vik"),
            "replaced_vik_coord": r.get("replaced_vik_coord"),
            "merge_action": "winner" if i == winner_idx else "merged_loser",
            "conflict_flags": [],
        }
        # strip Nones for compactness, but keep merge_action and conflict_flags
        ref = {k: v for k, v in ref.items()
               if v is not None or k in ("merge_action", "conflict_flags", "old_id", "old_coord")}
        refs.append(ref)
    return {"source_refs": refs}


# ---------- Migration ----------

def migrate(records):
    """Run the full migration pipeline. Returns (output, provenance, report)."""
    exact = exact_coord_clusters(records, decimals=6)
    c3_clusters = detect_c3_clusters(records, exact)
    c3_indices = set()
    for _, idxs in c3_clusters:
        c3_indices.update(idxs)

    components = build_5m_components(records, c3_indices)

    output = []
    provenance = OrderedDict()
    record_actions = {}   # old_id -> action info
    cluster_id_for_q13a = {}  # old_id -> cluster_id (5m cluster) if part of one
    seen_canonical_ids = set()

    # Process <=5m components (including singletons), excluding C3
    cluster_counter = 0
    for comp in components:
        if len(comp) >= 2:
            cluster_counter += 1
            cluster_label = f"dup5m_{cluster_counter:04d}"
        else:
            cluster_label = None
        winner_idx = pick_winner(records, comp) if len(comp) > 1 else comp[0]
        winner_old_id = records[winner_idx]["i"]
        force_null = winner_old_id in Q13A_OLD_IDS
        verbose = build_verbose_record(records, winner_idx, comp, force_type_null=force_null)
        cid = verbose["id"]
        if cid in seen_canonical_ids:
            raise RuntimeError(f"canonical id collision (non-C3): {cid}")
        seen_canonical_ids.add(cid)
        output.append(verbose)
        provenance[cid] = build_provenance_entry(records, comp, winner_idx)

        action = "merged" if len(comp) >= 2 else "kept"
        reason = "duplicate_5m" if len(comp) >= 2 else "no_duplicate"
        member_old_ids = [records[i]["i"] for i in comp]
        for i in comp:
            old_id = records[i]["i"]
            record_actions[old_id] = {
                "old_id": old_id,
                "new_id": cid,
                "action": action,
                "reason": reason,
                "winner": (i == winner_idx),
                "source_records_preserved": member_old_ids,
            }
            if old_id in Q13A_OLD_IDS:
                cluster_id_for_q13a[old_id] = cluster_label

    # Process C3 records — each preserved individually
    for _, idxs in c3_clusters:
        for i in idxs:
            old_id = records[i]["i"]
            verbose = build_verbose_record(
                records, i, [i],
                force_type_null=True,
                c3_suffix_old_id=old_id,
            )
            cid = verbose["id"]
            if cid in seen_canonical_ids:
                raise RuntimeError(f"canonical id collision (C3): {cid}")
            seen_canonical_ids.add(cid)
            output.append(verbose)
            provenance[cid] = build_provenance_entry(records, [i], i)
            record_actions[old_id] = {
                "old_id": old_id,
                "new_id": cid,
                "action": "kept_c3",
                "reason": "c3_preservation",
                "winner": True,
                "source_records_preserved": [old_id],
            }

    # Q13A reconciliation
    q13a_records = []
    q13a_null_in_output_count = 0
    for old_id in sorted(Q13A_OLD_IDS):
        act = record_actions.get(old_id)
        assert act is not None, f"Q13A old id {old_id} not found in any action record"
        cluster_id = cluster_id_for_q13a.get(old_id)
        if act["action"] == "kept":
            q_action = "kept_standalone_type_null"
            q13a_null_in_output_count += 1
        elif act["action"] == "merged" and act["winner"]:
            q_action = "merged_type_null_in_survivor"
            q13a_null_in_output_count += 1
        elif act["action"] == "merged" and not act["winner"]:
            q_action = "dropped_because_of_conflict"
        elif act["action"] == "kept_c3":
            # Q13A in C3 not expected, but handle defensively
            q_action = "kept_standalone_type_null"
            q13a_null_in_output_count += 1
        else:
            raise RuntimeError(f"unexpected Q13A action for {old_id}: {act}")
        q13a_records.append({
            "old_id": old_id,
            "new_id": act["new_id"],
            "action": q_action,
            "cluster_id": cluster_id,
            "type_result": None,
            "notes": "Q13A ambiguous type preserved as unknown in survivor/provenance",
        })

    # Type-null totals across output
    output_total_type_null = sum(1 for o in output if "type" not in o)
    other_reasons_type_null = output_total_type_null - q13a_null_in_output_count

    report = {
        "summary": {
            "input_count": len(records),
            "output_count": len(output),
            "merged_count": len(records) - len(output),
            "c3_preserved_records": len(c3_indices),
        },
        "q13a_reconciliation": {
            "input_count": len(Q13A_OLD_IDS),
            "output_type_null_due_to_q13a_count": q13a_null_in_output_count,
            "output_type_null_due_to_other_reasons_count": other_reasons_type_null,
            "records": q13a_records,
        },
        "records": [record_actions[r["i"]] for r in records],
    }

    return output, provenance, report


# ---------- Output assertions (plan Section 2E) ----------

def assert_output(output, provenance, report, records):
    """Verify all plan Section 2E test assertions."""
    results = []

    # Count
    n_out = len(output)
    results.append(("output_count", n_out == EXPECTED_OUTPUT_COUNT,
                    f"got {n_out}, expected {EXPECTED_OUTPUT_COUNT}"))

    # Origins
    origins = Counter(o["origin"] for o in output)
    for k, v in EXPECTED_OUTPUT_ORIGINS.items():
        results.append((f"origin_{k}", origins.get(k, 0) == v,
                        f"got {origins.get(k, 0)}, expected {v}"))

    # Types
    types = Counter(o.get("type") for o in output)
    for k, v in EXPECTED_TYPES.items():
        results.append((f"type_{k}", types.get(k, 0) == v,
                        f"got {types.get(k, 0)}, expected {v}"))
    n_absent_type = sum(1 for o in output if "type" not in o)
    results.append(("type_absent", n_absent_type == EXPECTED_TYPE_ABSENT,
                    f"got {n_absent_type}, expected {EXPECTED_TYPE_ABSENT}"))

    # No compact keys in runtime
    compact_keys = {"i", "c", "o", "a", "r", "s", "st", "z", "t", "status"}
    for o in output:
        bad = compact_keys & set(o.keys())
        results.append((f"no_compact_keys[{o['id']}]", not bad,
                        f"compact keys present: {bad}" if bad else ""))
        if bad:
            break  # one example is enough; halt
    else:
        results.append(("no_compact_keys_any", True, ""))

    # Required fields present, unique ids, valid coords
    ids = [o["id"] for o in output]
    results.append(("ids_unique", len(set(ids)) == len(ids),
                    f"duplicates: {len(ids) - len(set(ids))}"))
    for o in output:
        assert "id" in o and "coords" in o and "origin" in o, f"missing required field on {o}"
        c = o["coords"]
        assert isinstance(c, list) and len(c) == 2
        lon, lat = c[0], c[1]
        assert LON_MIN <= lon <= LON_MAX and LAT_MIN <= lat <= LAT_MAX
    results.append(("required_fields_and_coords", True, ""))

    # Alias assertion: every old id resolves via id or legacy_ids
    alias_index = {}
    for o in output:
        alias_index[o["id"]] = o["id"]
        for la in o.get("legacy_ids", []):
            alias_index[la] = o["id"]
    missing_aliases = [r["i"] for r in records if r["i"] not in alias_index]
    results.append(("alias_coverage", not missing_aliases,
                    f"missing aliases: {len(missing_aliases)}"))

    # Q13A reconciliation count
    qrec = report["q13a_reconciliation"]
    results.append(("q13a_input_count", qrec["input_count"] == 17,
                    f"got {qrec['input_count']}"))
    q_ids_in_report = {r["old_id"] for r in qrec["records"]}
    results.append(("q13a_all_reconciled", q_ids_in_report == Q13A_OLD_IDS,
                    f"missing: {Q13A_OLD_IDS - q_ids_in_report}"))

    # Duplicate assertion: no <=5m duplicate components except C3 same-coord groups
    by_coord = defaultdict(list)
    for o in output:
        by_coord[(round(o["coords"][0], 6), round(o["coords"][1], 6))].append(o)
    # C3 records share the same rounded coord across multiple output ids; that's allowed
    c3_count_in_groups = 0
    for coord_key, group in by_coord.items():
        if len(group) > 1:
            # All must be C3 (have __ suffix)
            for o in group:
                if "__" not in o["id"]:
                    results.append(("no_residual_5m_dup", False,
                                    f"non-C3 duplicate coord at {o['id']}"))
                    break
            else:
                c3_count_in_groups += len(group)
    results.append(("c3_grouped_count", c3_count_in_groups == EXPECTED_C3_RECORDS,
                    f"got {c3_count_in_groups}, expected {EXPECTED_C3_RECORDS}"))

    # Provenance: one archive entry per runtime record
    results.append(("provenance_one_per_id", set(provenance.keys()) == set(ids),
                    f"asymmetry: {len(set(provenance.keys()) ^ set(ids))}"))

    # Every old id appears in some source_refs
    old_ids_in_provenance = set()
    for entry in provenance.values():
        for ref in entry["source_refs"]:
            old_ids_in_provenance.add(ref["old_id"])
    all_old_ids = {r["i"] for r in records}
    results.append(("provenance_covers_all_old_ids",
                    old_ids_in_provenance == all_old_ids,
                    f"missing: {len(all_old_ids - old_ids_in_provenance)}"))

    # Report: every old `i` appears exactly once in records
    report_old_ids = [rec["old_id"] for rec in report["records"]]
    results.append(("report_records_one_per_input",
                    len(report_old_ids) == len(records) and
                    set(report_old_ids) == all_old_ids,
                    f"len={len(report_old_ids)}, set_diff={len(set(report_old_ids) ^ all_old_ids)}"))

    return results


def mojibake_scan(text):
    """Return True if any UTF-8 mojibake pattern detected."""
    import re
    return bool(re.search(r"[ÐÑÂ][-ÿ]", text))


# ---------- Atomic write ----------

def atomic_write_json(path, obj, indent=None):
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=indent)
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


# ---------- CLI ----------

def summarize_migration(output, provenance, report, dry_run=False):
    s = report["summary"]
    banner = "DRY RUN" if dry_run else "LIVE RUN"
    print(f"=== {banner} — migration summary ===")
    print(f"input_count:        {s['input_count']}")
    print(f"output_count:       {s['output_count']}")
    print(f"merged_count:       {s['merged_count']}")
    print(f"c3_preserved:       {s['c3_preserved_records']}")
    print()
    print("Output origins:")
    for k, v in sorted(Counter(o["origin"] for o in output).items()):
        print(f"  {k:14s} {v}")
    print()
    print("Output type distribution:")
    type_counter = Counter(o.get("type") for o in output)
    for k in ("надземен", "подземен"):
        print(f"  {k:14s} {type_counter.get(k, 0)}")
    print(f"  {'(absent)':14s} {sum(1 for o in output if 'type' not in o)}")
    print()
    print("Output existence_status / review_status:")
    print(f"  existence_status=verified: {sum(1 for o in output if o.get('existence_status') == 'verified')}")
    print(f"  review_status=reported:   {sum(1 for o in output if o.get('review_status') == 'reported')}")
    print()
    q = report["q13a_reconciliation"]
    print("Q13A reconciliation:")
    print(f"  input_count: {q['input_count']}")
    print(f"  output_type_null_due_to_q13a:    {q['output_type_null_due_to_q13a_count']}")
    print(f"  output_type_null_due_to_other:   {q['output_type_null_due_to_other_reasons_count']}")
    q_actions = Counter(r["action"] for r in q["records"])
    for k, v in sorted(q_actions.items()):
        print(f"    {k}: {v}")
    print()
    # Cluster info
    cluster_counts = Counter()
    for rec in report["records"]:
        cluster_counts[rec["action"]] += 1
    print("Per-record actions:")
    for k, v in sorted(cluster_counts.items()):
        print(f"  {k}: {v}")


def main():
    # Force UTF-8 stdout so Cyrillic labels print on Windows consoles (cp1252 default)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", required=True)
    p.add_argument("--field-reports", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--provenance", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    records = load_json(args.input)
    field_reports = load_json(args.field_reports)

    validate_input(records, field_reports)
    output, provenance, report = migrate(records)

    results = assert_output(output, provenance, report, records)
    failed = [r for r in results if not r[1]]
    if failed:
        print("ASSERTION FAILURES:", file=sys.stderr)
        for name, _, detail in failed:
            print(f"  FAIL {name}: {detail}", file=sys.stderr)
        sys.exit(2)

    # mojibake scan on serialized JSON
    for name, obj in (("output", output), ("provenance", provenance), ("report", report)):
        text = json.dumps(obj, ensure_ascii=False)
        if mojibake_scan(text):
            print(f"MOJIBAKE DETECTED in {name}", file=sys.stderr)
            sys.exit(3)

    if args.dry_run:
        summarize_migration(output, provenance, report, dry_run=True)
        print()
        print(f"All assertions passed ({len(results)} checks).")
        print("Dry run — no files written.")
        return

    atomic_write_json(args.output, output)
    atomic_write_json(args.provenance, provenance)
    atomic_write_json(args.report, report, indent=2)

    # Remove field_reports.json — per plan Section 2C step 9
    try:
        os.remove(args.field_reports)
    except FileNotFoundError:
        pass

    summarize_migration(output, provenance, report, dry_run=False)
    print()
    print(f"All assertions passed ({len(results)} checks).")
    print(f"Wrote: {args.output}")
    print(f"Wrote: {args.provenance}")
    print(f"Wrote: {args.report}")
    print(f"Removed: {args.field_reports}")


if __name__ == "__main__":
    main()
