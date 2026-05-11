# Address Backfill Via Reverse Geocoding Plan

Target document: `docs/audits/address_backfill_plan_20260511.md`.

## Protocol Preamble

Request scope: read-only investigation and implementation plan for backfilling missing `address` values in canonical `data/hydrants.json` via reverse geocoding. Out of scope: verification workflow changes, Section B sprint completion, schema redesign, display redesign, runtime dependencies, and live geocoding calls during planning.

Ratification note: Petar accepted the prior plan with three amendments: exact Nominatim `User-Agent`, explicit Photon fallback criterion, and optional `--skip-origin field_report`. After this plan is written, Commit 1 is ratified.

Current repo state observed during planning: `HEAD 2950cc8 chore(data): snapshot of 23 verified records before address backfill sprint`; `3246e75` is in history, but current `HEAD` is newer. `data/hydrants.json` has 5,901 records.

Deterministic inventory scope: `AGENTS.md`, `docs/activeContext.md`, `data/*.json`, `docs/audits/*`, and `scripts/*.py`.

Deterministic inventory:

```text
.\AGENTS.md                                                        14669 2026-05-08 01:02:13
.\data\hydrants.json                                              870255 2026-05-11 02:14:27
.\data\hydrants.json.pre_cleanup_snapshot.json                    968365 2026-05-08 01:52:44
.\data\hydrants_provenance.json                                  1350082 2026-05-11 02:14:27
.\docs\activeContext.md                                            19768 2026-05-11 04:20:17
.\docs\audits\backfill_and_submission_extension_plan_20260509.md   14693 2026-05-11 02:04:32
.\docs\audits\backfill_verified_type_report_20260509.json           2644 2026-05-11 02:14:27
.\docs\audits\bug_fixes_plan_20260508.md                           15293 2026-05-08 19:34:10
.\docs\audits\cleanup_execution_plan_20260508.md                   23986 2026-05-09 01:51:31
.\docs\audits\cleanup_migration_report_20260508.json             1449567 2026-05-11 00:00:25
.\docs\audits\data_architecture_audit_20260508.md                  98219 2026-05-08 03:31:23
.\docs\audits\data_audit_and_target_schema_20260508.md             51949 2026-05-09 00:14:01
.\docs\audits\governance_proposal_20260508.md                      12889 2026-05-08 00:54:03
.\docs\audits\issue_ingest_plan_20260508.md                        16659 2026-05-08 01:48:05
.\docs\audits\submission_status_and_moderation_plan_20260508.md     7044 2026-05-08 21:23:13
.\docs\audits\verified_records_snapshot_20260511.json               9841 2026-05-11 17:15:26
.\scripts\apply_approved_reports.py                                18917 2026-05-11 16:24:26
.\scripts\backfill_verified_type_20260509.py                       12123 2026-05-11 02:14:09
.\scripts\migrate_to_verbose_schema.py                             26878 2026-05-11 00:00:36
```

Files read during planning: `AGENTS.md`, `docs/activeContext.md`, `data/hydrants.json`, `data/hydrants_provenance.json`, `docs/audits/verified_records_snapshot_20260511.json`, `docs/audits/backfill_and_submission_extension_plan_20260509.md`, `docs/audits/backfill_verified_type_report_20260509.json`, `docs/audits/cleanup_migration_report_20260508.json`, `docs/audits/data_audit_and_target_schema_20260508.md`, `docs/audits/data_architecture_audit_20260508.md`, `docs/audits/cleanup_execution_plan_20260508.md`, `scripts/backfill_verified_type_20260509.py`, `scripts/migrate_to_verbose_schema.py`, and `scripts/apply_approved_reports.py`.

Negative findings matrix:

| Pattern / category | Finding |
|---|---|
| Target plan file | `docs/audits/address_backfill_plan_20260511.md` did not exist before this write. |
| Existing address-backfill script | No `address_backfill`, `backfill_addresses`, `nominatim`, `mapbox`, or `photon` file-path matches found. |
| `field_reports.json` | Missing, expected after cleanup migration. |
| `package.json` / build system | Missing; no JS build dependency context. |
| Compact runtime keys | 0 records have `i`, `a`, `c`, `o`, or legacy `status`; current data is verbose schema. |
| Empty/null addresses | 0 empty-string addresses and 0 null addresses; populated means non-empty `address` string. |
| Live geocoding calls | No coordinate reverse-geocoding API calls were made during planning. |

Declared metadata / authority notes:

- `docs/audits/verified_records_snapshot_20260511.json`: `"source_data_file": "data/hydrants.json"`, `"description": "Snapshot of all verified records before address backfill sprint"`, `"verified_count": 23`.
- `docs/audits/data_audit_and_target_schema_20260508.md`: "Cleanup should preserve non-empty `a` unchanged. Reverse geocoding empty addresses is a separate future sprint."
- `docs/audits/backfill_and_submission_extension_plan_20260509.md`: existing provenance pattern appends `source_refs` entries for manual backfills.
- `AGENTS.md`: data changes, data-source changes, new dependencies, UI wording changes, and first-load-size risk require approval gates.

Decision ledger:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Use observed coverage counts | Current data + Petar choice | Parsed 555 addressed / 5,346 missing; Petar selected observed counts | Recompute anytime | Approved |
| Preserve all existing `address` values | Prior audit + data safety | 555 existing addresses include human field descriptions | Reversible by restore | Approved |
| Backfill all missing origins by default | Runtime data | Missing: 3 field_report, 2,291 national, 3,052 vik | Can use `--skip-origin` | Approved |
| Use Nominatim as primary provider | Budget + policy fit | Free, OSM-based, explicit 1 req/sec policy | Provider flag can change | Approved |
| Add exact User-Agent format | Petar amendment | OSM compliance | Script-only change | Approved |
| Add exact Photon fallback trigger | Petar amendment | Removes judgment call | Reversible | Approved |
| Add optional `--skip-origin field_report` | Petar amendment | Lets execution preserve field-report style if desired | CLI flag | Approved |
| Store compact accepted address | First-load hard cap | Current first load 1,184,739 bytes; 815,261 bytes remain | Re-run formatter | Approved |
| Append provenance per accepted change | User requirement + current provenance | Existing `source_refs` pattern | Restore snapshot | Approved |

Approval-gate check: this is a data-source/data-edit sprint, so Petar approval is required before any API run and before any `--apply`. No runtime/build dependency is proposed. No Bulgarian UI labels change. Script addition under existing `scripts/` is not a runtime architecture change. The script must estimate `index.html + data/hydrants.json` and stop before apply if projected first load exceeds 1,900,000 bytes, with the 2,000,000 byte hard cap as non-negotiable.

Open questions: none blocking for implementation. Default locked: require a real identifying `User-Agent` and require `--contact-email` for uncached runs over 100 records.

## Section 1: Empirical State

Current address coverage in `data/hydrants.json`:

| Metric | Count |
|---|---:|
| Total records | 5,901 |
| Records with populated `address` | 555 |
| Records без address | 5,346 |
| Coverage | 9.41% |

Coverage by origin:

| Origin | Total | With address | Без address | Coverage |
|---|---:|---:|---:|---:|
| `vik` | 3,542 | 490 | 3,052 | 13.83% |
| `national` | 2,345 | 54 | 2,291 | 2.30% |
| `field_report` | 14 | 11 | 3 | 78.57% |

Address style heuristic over the 555 existing addresses:

| Style | Count | Share | Examples |
|---|---:|---:|---|
| Street-based | 449 | 80.9% | `ул. ...`, `бул. ...` |
| Human descriptive, no street token | 64 | 11.5% | `до блок 303`, `На тротоара.`, `магазин Явор` |
| Mixed street + landmark | 19 | 3.4% | street plus `бл.` or nearby object |
| Other unclassified | 18 | 3.2% | `ЮПЗ`, `РИОСВ`, local place names |
| Numbered unclassified | 5 | 0.9% | includes two `0` values |

Existing field-report addresses are mostly human-descriptive, so `--skip-origin field_report` is available if Petar wants style consistency for the 3 missing field reports.

Geographic distribution на records без address:

- Missing-address bbox: lon `27.114973` to `28.049802`, lat `42.832464` to `43.541805`.
- Missing-address centroid: lon `27.676242`, lat `43.181417`.
- Largest 0.05-degree missing-address cells:
  - 560 records: lon `27.85-27.90`, lat `43.20-43.25`
  - 435 records: lon `27.90-27.95`, lat `43.20-43.25`
  - 184 records: lon `27.40-27.45`, lat `43.15-43.20`
  - 145 records: lon `27.95-28.00`, lat `43.20-43.25`
  - 141 records: lon `27.90-27.95`, lat `43.15-43.20`
- Coarse concentration: 1,660 missing records fall in lon `27.8-28.1`, lat `43.2-43.35`, the densest eastern/coastal Varna-area band.
- `region` is absent on 4,589 of 5,346 missing-address records; top present regions include `Св.Св.Константин и Елена`, `С.О. Боровец-юг`, `9 ПОДРАЙОН; ИЗТОК-1`, and `ЮПЗ`.

## Section 2: Reverse Geocoding Source Options

Nominatim / OSM:

- Official policy/docs: https://operations.osmfoundation.org/policies/nominatim/ and https://nominatim.org/release-docs/latest/api/Reverse/
- Varna coverage is likely good in central street-mapped areas and weaker in industrial zones, villages, fields, and unnamed roads. Nominatim warns reverse geocoding returns the closest suitable OSM object, not necessarily the exact address.
- Public service max: 1 req/sec. For 5,346 uncached records, minimum wall time is about 89 minutes; plan for 2-3 hours with retries and pauses.
- Cost: free, with OSM attribution/ODbL obligations.
- Reliability: acceptable for one identified, cached, single-threaded run.

Mapbox:

- Docs/pricing: https://docs.mapbox.com/api/search/geocoding/ and https://www.mapbox.com/pricing
- Fast and likely high quality, but stored repo backfill requires Permanent Geocoding, not Temporary Geocoding.
- Estimated permanent cost for 5,346 records: about `$26.73` at `$5 / 1,000`.
- Not recommended unless Petar explicitly approves paid permanent geocoding.

Photon:

- Docs: https://github.com/komoot/photon
- OSM-based; public demo has no strong availability/rate guarantee.
- Exact fallback trigger: if Nominatim acceptance rate on the full dry-run is `< 50%`, run Photon on a 100-record sample for comparison. If Photon acceptance is `>10 percentage points` higher, discuss with Petar whether to switch providers before `--apply`; otherwise proceed with Nominatim.
- Self-hosting Photon is out of scope unless Petar requests infrastructure work.

Recommendation: use Nominatim first.

## Section 3: Quality Concerns

- Preserve all existing `address` values unchanged because they include reviewed human descriptions like block/entrance/landmark notes that reverse geocoding cannot recreate.
- Accept that new values will be more OSM/street-style, for example `ул. Васил Левски 145`; avoid mixing by never overwriting human descriptions.
- Use `accept-language=bg,en`; prefer Cyrillic output. Reject or flag Latin-only results unless no Bulgarian equivalent exists and the result is clearly street-level.
- Reject generic results such as only `Варна, България`, only municipality/country, only postcode/county, or fewer than three meaningful address components.
- Accept only street/building-level results: Nominatim `address` must include a street-like component such as `road`, `pedestrian`, `residential`, `footway`, or `path`, or an `addresstype` of `road`, `house`, `building`, or `address`, plus a Bulgarian settlement/country context.
- Reject stale/implausible results where the provider result coordinate is more than 150m from the hydrant coordinate, unless explicitly reviewed.
- Normalize lightly only: trim whitespace, collapse repeated spaces, normalize quotes, and assemble compact address as `street + house_number` plus optional district/suburb. Do not transliterate or invent Bulgarian abbreviations.
- Report all rejected/generic results so Petar can judge whether a second provider or manual pass is needed.

## Section 4: Backfill Script Design

Add `scripts/backfill_addresses_20260511.py`.

Use standard library only: `argparse`, `json`, `urllib.request`, `urllib.error`, `time`, `datetime`, `tempfile`, `os`, `pathlib`, `hashlib`, and small local helpers. No new dependency.

CLI examples:

```powershell
python scripts/backfill_addresses_20260511.py --dry-run --limit 100 --contact-email <email>
python scripts/backfill_addresses_20260511.py --dry-run --contact-email <email> --report docs/audits/address_backfill_dry_run_20260511.json
python scripts/backfill_addresses_20260511.py --dry-run --contact-email <email> --skip-origin field_report
python scripts/backfill_addresses_20260511.py --apply --limit 100 --contact-email <email> --report docs/audits/address_backfill_apply_sample_20260511.json
python scripts/backfill_addresses_20260511.py --apply --contact-email <email> --report docs/audits/address_backfill_full_apply_20260511.json
```

Required Nominatim identity header:

```text
User-Agent: Fire_Varna address backfill (https://github.com/Petar1984/Fire_Varna, contact: <email>)
```

Core behavior:

- Default to `--dry-run`; `--apply` is required for data/provenance mutation.
- Inputs default to `data/hydrants.json` and `data/hydrants_provenance.json`.
- Skip every record with existing non-empty `address`.
- Target all 5,346 missing-address records by default.
- `--skip-origin field_report` is optional and defaults off; when used, it excludes the 3 missing field-report records to preserve field-report style consistency.
- Query Nominatim reverse endpoint with `format=jsonv2`, `addressdetails=1`, `zoom=18`, `layer=address`, `accept-language=bg,en`, exact `User-Agent`, and `email`.
- Enforce one uncached request every at least 1.1 seconds; handle `429` via `Retry-After` or exponential backoff; single thread only.
- Cache compact provider responses by rounded `lon,lat` and provider params so resume never re-queries successful coordinates.
- Maintain progress state with processed IDs, accepted IDs, rejected IDs, errors, and last successful timestamp.
- Atomic-write only on `--apply`; dry-run may write reports/cache but must not modify `data/hydrants.json` or provenance.
- Run mojibake scan before writing any UTF-8 file.

Quality filter output per record:

- `accepted`: stores compact `address`.
- `rejected_generic`: provider returned only city/region/country-level result.
- `rejected_no_street`: no street/building-level component.
- `rejected_distance`: provider result too far away.
- `error`: timeout, 429 exhaustion, malformed response, or no result.

Migration report format:

```json
{
  "summary": {
    "input_count": 5901,
    "addressed_before": 555,
    "missing_before": 5346,
    "candidate_count": 5346,
    "provider": "nominatim",
    "http_requests": 0,
    "cache_hits": 0,
    "accepted_count": 0,
    "rejected_count": 0,
    "error_count": 0,
    "projected_data_bytes": 0,
    "projected_first_load_bytes": 0,
    "timestamp": "..."
  },
  "records": [
    {
      "id": "...",
      "origin": "vik",
      "coords": [27.0, 43.0],
      "old_address": null,
      "new_address": "...",
      "quality_status": "accepted",
      "quality_reason": "street_component",
      "provider_result": {
        "osm_type": "way",
        "osm_id": 0,
        "addresstype": "road",
        "category": "highway",
        "type": "residential"
      },
      "provenance_appended": true
    }
  ]
}
```

Per accepted record, append a `source_refs` provenance entry with `manual_field:"address"`, old/new values, provider metadata, requested coordinate, timestamp, `merge_action:"address_backfill"`, and `conflict_flags`.

Example provenance entry:

```json
{
  "old_id": "coord_...",
  "old_coord": [27.0, 43.0],
  "manual_field": "address",
  "old_value": null,
  "new_value": "...",
  "source": "osm_reverse_geocode_address_backfill_20260511",
  "provider": "nominatim",
  "provider_url": "https://nominatim.openstreetmap.org/reverse",
  "provider_osm_type": "way",
  "provider_osm_id": 0,
  "provider_addresstype": "road",
  "requested_coord": [27.0, 43.0],
  "timestamp": "...",
  "merge_action": "address_backfill",
  "conflict_flags": []
}
```

## Section 5: Recovery Strategy

- Before any apply, create both snapshots:
  - `data/hydrants.json.pre_address_backfill.json`
  - `data/hydrants_provenance.json.pre_address_backfill.json`
- Keep `docs/audits/verified_records_snapshot_20260511.json` as the verified-record recovery anchor.
- Rollback procedure: restore both snapshots, rerun record-count/address-count/provenance-count checks, then review `git diff -- data/hydrants.json data/hydrants_provenance.json`.
- Partial run failure: resume from cache/progress; do not rerun successful provider requests. If failure happens during `--apply`, atomic writes prevent half-written JSON.
- Quality review checkpoint: after full dry-run report, Petar reviews accepted/rejected counts, a 100-record sample on map, generic rejects, Latin-only flags, Photon trigger if applicable, and projected byte size before any full apply.
- If sample apply quality is bad, revert only the sample commit or restore snapshots; do not continue to full apply.

## Section 6: Sprint Sequencing

Recommended phased approach because provider limits, ODbL/policy compliance, quality review, and first-load byte risk matter more than raw speed.

1. Commit 1: Plan ratification.
   - Write this document to `docs/audits/address_backfill_plan_20260511.md`.
2. Commit 2: Snapshot + backfill script, no data change.
   - Add snapshots and `scripts/backfill_addresses_20260511.py`.
   - Verify dry-run default makes no data/provenance edits.
3. Commit 3: Full dry-run output committed for review.
   - Run Nominatim once, single-threaded, cached.
   - If Nominatim acceptance is `< 50%`, run Photon 100-record comparison sample.
   - Commit compact report, not oversized raw response dumps.
4. Commit 4: `--apply` sample, e.g. 100 accepted records.
   - Commit data/provenance/report sample only after Petar approves dry-run quality.
5. Commit 5: Quality verification + full apply.
   - Apply remaining accepted records if byte cap remains safe and sample quality is acceptable.
6. Commit 6: Migration report committed.
   - Commit final report, acceptance/rejection totals, source policy notes, and encoding/byte-size verification output.

Expected timing: full uncached Nominatim dry-run for 5,346 targets is about 90 minutes minimum, realistically 2-3 hours with retries. Sample 100 is about 2 minutes plus review.

## Section 7: Out Of Scope

- Verification workflow changes.
- Section B sprint completion.
- Schema modifications; `address` already exists.
- Display redesign.
- Runtime geocoding in the app.
- New runtime or build-time dependencies.
- Overwriting existing human-entered addresses.
- National-scope expansion beyond current Varna oblast runtime data.
