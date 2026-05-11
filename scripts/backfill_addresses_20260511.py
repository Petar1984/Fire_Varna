#!/usr/bin/env python3
"""Reverse-geocode missing `address` values via Nominatim.

Implements docs/audits/address_backfill_plan_20260511.md.

Default mode is --dry-run; --apply is required to write data/provenance.
Existing non-empty addresses are preserved and skipped. Standard library
only: no requests/httpx and no new runtime dependency.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Optional


NOMINATIM_REVERSE_URL = "https://nominatim.openstreetmap.org/reverse"
USER_AGENT_TEMPLATE = (
    "Fire_Varna address backfill "
    "(https://github.com/Petar1984/Fire_Varna, contact: {email})"
)
PROVIDER_NAME = "nominatim"
MIN_REQUEST_INTERVAL_S = 1.1
MAX_DISTANCE_M = 150.0
STREET_COMPONENT_KEYS = (
    "road",
    "pedestrian",
    "residential",
    "footway",
    "path",
)
STREET_ADDRESSTYPES = ("road", "house", "building", "address")
BG_SETTLEMENT_KEYS = (
    "city",
    "town",
    "village",
    "hamlet",
    "suburb",
    "city_district",
    "municipality",
    "county",
    "state",
)
DEFAULT_INPUT = "data/hydrants.json"
DEFAULT_PROVENANCE = "data/hydrants_provenance.json"
QUALITY_CATEGORIES = (
    "accepted",
    "rejected_generic",
    "rejected_no_street",
    "rejected_distance",
    "error",
)


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def atomic_write_json(path: str, obj, *, indent=None) -> None:
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            json.dump(obj, f, ensure_ascii=False, indent=indent)
            f.write("\n")
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def mojibake_scan_text(name: str, obj) -> None:
    text = json.dumps(obj, ensure_ascii=False)
    if re.search(r"[ÐÑÂ][-ÿ]", text):
        raise AssertionError(f"mojibake pattern detected in serialized {name}")


def iso_now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def has_address(record: dict) -> bool:
    value = record.get("address")
    return isinstance(value, str) and value.strip() != ""


def haversine_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    radius = 6_371_000.0
    rlat1 = math.radians(lat1)
    rlat2 = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2.0) ** 2
        + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon / 2.0) ** 2
    )
    return 2.0 * radius * math.asin(math.sqrt(a))


def normalize_address(parts: list[str]) -> str:
    joined = " ".join(p for p in parts if p)
    collapsed = re.sub(r"\s+", " ", joined).strip()
    collapsed = collapsed.replace("“", '"').replace("”", '"').replace("’", "'")
    return collapsed


def compose_compact_address(address: dict) -> str:
    """Assemble compact `street + house_number` plus optional district/suburb.

    Per plan §3: light normalization only, no transliteration.
    """
    street = None
    for key in STREET_COMPONENT_KEYS:
        if address.get(key):
            street = address[key]
            break
    house = address.get("house_number")
    head = " ".join(p for p in [street, house] if p) if street else ""
    district = address.get("suburb") or address.get("city_district") or address.get("neighbourhood")
    if district and district != street:
        return normalize_address([head, district]) if head else normalize_address([district])
    return normalize_address([head]) if head else ""


def is_latin_only(text: str) -> bool:
    return bool(text) and all(ord(c) < 128 or c.isspace() for c in text)


def classify_result(
    result: Optional[dict],
    requested_lon: float,
    requested_lat: float,
) -> tuple[str, str, str]:
    """Apply quality filter per plan §3.

    Returns (quality_status, quality_reason, compact_address).
    quality_status is one of QUALITY_CATEGORIES (except 'error', which is
    raised by the caller on transport/parse failure).
    """
    if not result or "error" in result:
        return ("error", "no_result", "")

    address = result.get("address") or {}
    addresstype = result.get("addresstype") or ""

    has_settlement_or_country = bool(
        address.get("country") or any(address.get(k) for k in BG_SETTLEMENT_KEYS)
    )
    meaningful_keys = [k for k, v in address.items() if v and k != "country_code"]
    if len(meaningful_keys) < 3 or not has_settlement_or_country:
        return ("rejected_generic", "too_few_components", "")

    has_street_component = any(address.get(k) for k in STREET_COMPONENT_KEYS)
    has_street_addresstype = addresstype in STREET_ADDRESSTYPES
    if not (has_street_component or has_street_addresstype):
        return ("rejected_no_street", "no_street_or_building_component", "")

    try:
        result_lon = float(result.get("lon"))
        result_lat = float(result.get("lat"))
    except (TypeError, ValueError):
        return ("error", "missing_coords", "")
    distance_m = haversine_m(requested_lon, requested_lat, result_lon, result_lat)
    if distance_m > MAX_DISTANCE_M:
        return ("rejected_distance", f"{distance_m:.1f}m_gt_{int(MAX_DISTANCE_M)}m", "")

    compact = compose_compact_address(address)
    if not compact:
        return ("rejected_no_street", "could_not_compose_compact_address", "")
    if is_latin_only(compact):
        # Plan §3: prefer Cyrillic, flag Latin-only unless no Bulgarian equivalent.
        # Conservatively reject; provider was asked for bg first.
        return ("rejected_generic", "latin_only_result", "")

    return ("accepted", "street_component", compact)


def query_nominatim(
    lon: float,
    lat: float,
    contact_email: str,
    timeout_s: float = 10.0,
) -> dict:
    params = {
        "lon": f"{lon:.6f}",
        "lat": f"{lat:.6f}",
        "format": "jsonv2",
        "addressdetails": "1",
        "zoom": "18",
        "layer": "address",
        "accept-language": "bg,en",
        "email": contact_email,
    }
    url = NOMINATIM_REVERSE_URL + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT_TEMPLATE.format(email=contact_email),
            "Accept": "application/json",
            "Accept-Language": "bg,en",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout_s) as response:
        body = response.read().decode("utf-8")
    return json.loads(body)


def build_provenance_ref(
    record: dict,
    new_address: str,
    result: dict,
    timestamp: str,
) -> dict:
    return {
        "old_id": record["id"],
        "old_coord": list(record["coords"]),
        "manual_field": "address",
        "old_value": None,
        "new_value": new_address,
        "source": "osm_reverse_geocode_address_backfill_20260511",
        "provider": PROVIDER_NAME,
        "provider_url": NOMINATIM_REVERSE_URL,
        "provider_osm_type": result.get("osm_type"),
        "provider_osm_id": result.get("osm_id"),
        "provider_addresstype": result.get("addresstype"),
        "requested_coord": list(record["coords"]),
        "timestamp": timestamp,
        "merge_action": "address_backfill",
        "conflict_flags": [],
    }


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=None,
                        help="Defaults to --input (writes back in place on --apply)")
    parser.add_argument("--provenance", default=DEFAULT_PROVENANCE)
    parser.add_argument("--report", default=None,
                        help="Defaults to docs/audits/backfill_report_<ISO>.json")
    parser.add_argument("--limit", type=int, default=None,
                        help="Process at most N eligible records (for smoke/sample)")
    parser.add_argument("--skip-origin", action="append", default=[],
                        help="Skip eligible records with this origin "
                             "(repeatable; e.g. --skip-origin field_report)")
    parser.add_argument("--contact-email", default=None,
                        help="Identifying contact for Nominatim User-Agent; "
                             "required for uncached runs over 100 records per plan")
    parser.add_argument("--dry-run", action="store_true",
                        help="Default; never writes data/provenance")
    parser.add_argument("--apply", action="store_true",
                        help="Required to write data/provenance files")
    args = parser.parse_args()

    if args.apply and args.dry_run:
        parser.error("--apply and --dry-run are mutually exclusive")

    apply_mode = bool(args.apply)
    output_path = args.output or args.input
    report_path = args.report or os.path.join(
        "docs", "audits",
        "backfill_report_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + ".json",
    )

    # Per plan: require contact for >100 records uncached. We do not know cache
    # state here, so enforce on any non-trivial run.
    eligible_threshold = 100
    if not args.contact_email:
        # Use a clearly placeholder identifier; warn loudly.
        contact_email = "unspecified@example.invalid"
        sys.stderr.write(
            "WARNING: --contact-email not provided; using placeholder. "
            "Per plan, real contact is required for uncached runs over "
            f"{eligible_threshold} records.\n"
        )
    else:
        contact_email = args.contact_email

    records = load_json(args.input)
    provenance = load_json(args.provenance)
    addressed_before = sum(1 for r in records if has_address(r))
    missing_before = len(records) - addressed_before

    skip_origins = set(args.skip_origin)
    eligible_indices: list[int] = []
    skipped_by_origin = 0
    preserved_existing = 0
    for index, record in enumerate(records):
        if has_address(record):
            preserved_existing += 1
            continue
        if record.get("origin") in skip_origins:
            skipped_by_origin += 1
            continue
        eligible_indices.append(index)

    if args.limit is not None and args.limit >= 0:
        eligible_indices = eligible_indices[: args.limit]

    if (
        not args.contact_email
        and len(eligible_indices) > eligible_threshold
        and not args.dry_run
        and apply_mode
    ):
        parser.error(
            f"--contact-email required for apply runs over {eligible_threshold} records "
            "(plan §0 default-locked policy)"
        )

    start_ts = iso_now()
    start_wall = time.monotonic()
    last_request_at = 0.0

    report_records: list[dict] = []
    status_counter: Counter = Counter()
    http_requests = 0
    timestamp = start_ts

    for index in eligible_indices:
        record = records[index]
        coords = record.get("coords") or []
        try:
            lon = float(coords[0])
            lat = float(coords[1])
        except (TypeError, ValueError, IndexError):
            entry = {
                "id": record.get("id"),
                "origin": record.get("origin"),
                "coords": coords,
                "old_address": None,
                "new_address": None,
                "quality_status": "error",
                "quality_reason": "bad_coords",
                "provider_result": None,
                "provenance_appended": False,
            }
            report_records.append(entry)
            status_counter["error"] += 1
            continue

        # Rate-limit: ensure ≥ MIN_REQUEST_INTERVAL_S between requests.
        elapsed = time.monotonic() - last_request_at
        if last_request_at and elapsed < MIN_REQUEST_INTERVAL_S:
            time.sleep(MIN_REQUEST_INTERVAL_S - elapsed)

        quality_status = "error"
        quality_reason = "unknown"
        compact = ""
        provider_meta = None
        result: Optional[dict] = None
        try:
            result = query_nominatim(lon, lat, contact_email)
            http_requests += 1
            last_request_at = time.monotonic()
            quality_status, quality_reason, compact = classify_result(result, lon, lat)
            provider_meta = {
                "osm_type": result.get("osm_type") if isinstance(result, dict) else None,
                "osm_id": result.get("osm_id") if isinstance(result, dict) else None,
                "addresstype": result.get("addresstype") if isinstance(result, dict) else None,
                "category": result.get("category") if isinstance(result, dict) else None,
                "type": result.get("type") if isinstance(result, dict) else None,
            }
        except urllib.error.HTTPError as exc:
            last_request_at = time.monotonic()
            quality_status = "error"
            quality_reason = f"http_{exc.code}"
        except urllib.error.URLError as exc:
            last_request_at = time.monotonic()
            quality_status = "error"
            quality_reason = f"url_error_{type(exc.reason).__name__}"
        except (json.JSONDecodeError, ValueError):
            last_request_at = time.monotonic()
            quality_status = "error"
            quality_reason = "parse_error"
        except TimeoutError:
            last_request_at = time.monotonic()
            quality_status = "error"
            quality_reason = "timeout"

        status_counter[quality_status] += 1

        provenance_appended = False
        if quality_status == "accepted" and apply_mode:
            ref = build_provenance_ref(record, compact, result or {}, timestamp)
            record["address"] = compact
            entry = provenance.setdefault(record["id"], {"source_refs": []})
            entry.setdefault("source_refs", []).append(ref)
            provenance_appended = True

        report_records.append(
            {
                "id": record.get("id"),
                "origin": record.get("origin"),
                "coords": list(coords),
                "old_address": None,
                "new_address": compact if quality_status == "accepted" else None,
                "quality_status": quality_status,
                "quality_reason": quality_reason,
                "provider_result": provider_meta,
                "provenance_appended": provenance_appended,
            }
        )

    end_ts = iso_now()
    wall_seconds = round(time.monotonic() - start_wall, 3)

    summary = {
        "input_count": len(records),
        "addressed_before": addressed_before,
        "missing_before": missing_before,
        "candidate_count": len(eligible_indices),
        "preserved_existing": preserved_existing,
        "skipped_by_origin": skipped_by_origin,
        "skip_origins": sorted(skip_origins),
        "provider": PROVIDER_NAME,
        "http_requests": http_requests,
        "accepted_count": status_counter.get("accepted", 0),
        "rejected_generic_count": status_counter.get("rejected_generic", 0),
        "rejected_no_street_count": status_counter.get("rejected_no_street", 0),
        "rejected_distance_count": status_counter.get("rejected_distance", 0),
        "error_count": status_counter.get("error", 0),
        "rejected_count": (
            status_counter.get("rejected_generic", 0)
            + status_counter.get("rejected_no_street", 0)
            + status_counter.get("rejected_distance", 0)
        ),
        "timestamp_start": start_ts,
        "timestamp_end": end_ts,
        "wall_seconds": wall_seconds,
        "args": {
            "input": args.input,
            "output": output_path,
            "provenance": args.provenance,
            "report": report_path,
            "limit": args.limit,
            "skip_origin": sorted(skip_origins),
            "dry_run": not apply_mode,
            "apply": apply_mode,
        },
    }
    report = {"summary": summary, "records": report_records}

    mojibake_scan_text("report", report)
    if apply_mode:
        mojibake_scan_text("hydrants", records)
        mojibake_scan_text("provenance", provenance)

    atomic_write_json(report_path, report, indent=2)

    if apply_mode:
        atomic_write_json(output_path, records)
        atomic_write_json(args.provenance, provenance)
        print(f"APPLIED: wrote {output_path}, {args.provenance}, {report_path}")
    else:
        print(f"DRY RUN: wrote report {report_path}; no data/provenance changes")

    print(f"  input_count: {summary['input_count']}")
    print(f"  addressed_before: {summary['addressed_before']}")
    print(f"  missing_before: {summary['missing_before']}")
    print(f"  candidate_count: {summary['candidate_count']}")
    print(f"  preserved_existing: {summary['preserved_existing']}")
    print(f"  skipped_by_origin: {summary['skipped_by_origin']} {sorted(skip_origins)}")
    print(f"  http_requests: {summary['http_requests']}")
    for category in QUALITY_CATEGORIES:
        count = status_counter.get(category, 0)
        print(f"  {category}: {count}")
    print(f"  wall_seconds: {summary['wall_seconds']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
