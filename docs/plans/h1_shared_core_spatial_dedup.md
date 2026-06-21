# H1 Shared Core + Spatial Dedup Plan

Status: final plan for execution review.  
Authoring date: 2026-06-21.  
Mode: PLAN ONLY. This document authorizes no data apply, no commit, and no push.

## Request Scope

H1 scope is limited to `Fire_Varna`:

1. Refactor the reusable non-network parts of `scripts/apply_approved_reports.py`
   into a shared core module, proposed path `scripts/lib/hydrant_core.py`.
2. Add a deterministic spatial matcher for hydrant points with signed thresholds:
   `Rm = 5 m`, `Rf = 20 m`.
3. Use that matcher only in the `new_hydrant` issue path so nearby reports become:
   `UPDATE` for distance `<= 5 m`, `FLAG` for distance `(5 m, 20 m]`, and `ADD`
   for distance `> 20 m`.
4. Preserve existing behavior byte-identically for existing non-`new_hydrant`
   handlers: `exists_confirmed`, `damaged`, `missing`, `wrong_location`.
5. Keep H1 as refactor plus tests. H1 must not mutate real data. The CLI remains
   dry-run by default.

Out of scope:

- KMZ adapter and KMZ apply. That is H2/H4.
- Stable-ID migration of existing `coord_` ids. That is H3.
- Real `data/hydrants.json` or `data/hydrants_provenance.json` mutation.
- Worker changes, frontend changes, issue relabeling, GitHub operations, commit, or push.

## Deterministic Inventory

Inventory scope: task-scoped inventory for H1 planning, under `C:\git\Fire_Varna`
plus the single cross-repo context plan in `C:\git\Varna_buildings`.

Observed `Fire_Varna` repo state:

```text
repo: C:/git/Fire_Varna
HEAD: 47cd3edf971c895fb365c3a6f1e2830967d04ac8
status: ## main...origin/main
```

Relevant `Fire_Varna` files:

```text
AGENTS.md	14979	6BC705FEE1D4854010C14BD60A2B671FE8A6C35800F7800F7665D9D92A97F0E9
audit/ingest_reports/ingest_2026-05-28.json	2136	3B1157E0E9292C62D4C1FCFE988B0434B4FB7265CA8330E59F320F98E900138B
audit/ingest_reports/ingest_2026-05-28_batch.json	13868	AAF009B1B106E933DE975E4F4FE62B784A3B36DF9710CC76147A7D378330F133
data/hydrants.json	874593	65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B
data/hydrants.json.pre_address_backfill.json	870256	8CD1A95BC02977583B9F79DA38F70E87D305F3426535C2820BBE8C7A6B973AB4
data/hydrants.json.pre_cleanup_snapshot.json	968365	EE92C904DD6EDDCF2625E25F24D1829BECE96E0917B60F21309D19361D55ED2F
data/hydrants_provenance.json	1364172	894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E
data/hydrants_provenance.json.pre_address_backfill.json	1350083	262155B083072C63071535830C4369C193B4A62E5BEBCE10005119C8B4175B3B
docs/activeContext.md	19972	6B7802DC2545063D36E653389225027401FAE14102651068B45E2E2D67B33D9E
docs/audits/backfill_and_submission_extension_plan_20260509.md	14941	E84D262A388DD947FB224C34C4DF9DE01170062D17E0CBDFF8F187B8105F91D0
scripts/apply_approved_reports.py	19430	05A668CD347924699EE3E0E37C1D793CA791BBCE2BEA47E910D1C34E712AD632
scripts/backfill_addresses_20260511.py	28484	750B3F70DFA908FAE3A6546758176603957B743858E58757A81E47FC704EFFEF
scripts/backfill_verified_type_20260509.py	12461	D29AC352CD2B2B4BCC89EFDB7F120FFCEE262414E3D7668D0E22773BA60BA09A
scripts/migrate_to_verbose_schema.py	27607	B23CD131F9606D0F28B656EA0273EB71C9B605614A6BCD45EA5A5DF8D4890FDC
```

Observed `Varna_buildings` context state:

```text
repo: C:/git/Varna_buildings
HEAD: 300a5fee7cee0482d67fd35e26cf420be1c72750
status: dirty, with unrelated scratch/output/research files
```

Relevant `Varna_buildings` files:

```text
AGENTS.md	12430	8B80CC48FF90E3544E50ACA56177FE1CFAC4AE3C761BB66C4C7D0EAE123BE6F2
scratch/hydrant_consolidation_e0_and_pipeline_plan.md	10861	603DC5B23F164524C62CC09D90597CDB1535BBF8E22A8964E6682D911B205230
```

## Files Read

Files read for this plan:

- `Fire_Varna/AGENTS.md`
- `Fire_Varna/docs/activeContext.md`
- `Fire_Varna/docs/audits/backfill_and_submission_extension_plan_20260509.md`
- `Fire_Varna/scripts/apply_approved_reports.py`
- `Fire_Varna/scripts/migrate_to_verbose_schema.py`, selected geo/dedup helper lines
- `Fire_Varna/scripts/backfill_addresses_20260511.py`, selected geo helper lines
- `Fire_Varna/data/hydrants.json`
- `Fire_Varna/data/hydrants_provenance.json`
- `Fire_Varna/data/hydrants.json.pre_address_backfill.json`
- `Fire_Varna/data/hydrants_provenance.json.pre_address_backfill.json`
- `Fire_Varna/audit/ingest_reports/ingest_2026-05-28.json`
- `Fire_Varna/audit/ingest_reports/ingest_2026-05-28_batch.json`
- `Varna_buildings/AGENTS.md`
- `Varna_buildings/scratch/hydrant_consolidation_e0_and_pipeline_plan.md`

## Negative Findings Matrix

| Check | Finding |
|---|---|
| Shared core module | No `scripts/lib/**` exists in `Fire_Varna`. |
| Tests | No `tests/**`, `pytest.ini`, `pyproject.toml`, or requirements file exists in `Fire_Varna`. |
| Spatial dedup in `new_hydrant` | Absent. Current code computes `canonical_coord_id()` and checks only exact id collision with `if new_id in state["alias"]`. |
| Stable-ID registry | No implementation found. H1 must add only an interface/stub; migration is H3. |
| KMZ adapter | No H1 adapter exists. KMZ parsing/apply is out of H1. |
| Runtime dependency support | No project dependency manifest in scope; H1 must use standard library only. |
| Raw Worker payload fixtures for May 28 | Not present. Historical reconstruction from audit reports is allowed only as supplementary analysis, not as proof of historical parity. |
| Real data mutation authorization | Not present for H1. H1 must not run `--apply` against real data. |
| Mojibake in scoped docs/reports | No marker matches found in scoped docs/reports. The only match in `apply_approved_reports.py` is the mojibake scanner regex itself. |

## Quoted Declared Metadata

From `scripts/apply_approved_reports.py` docstring:

```text
Default is dry-run; --apply writes.
```

From `scripts/apply_approved_reports.py`:

```text
# Varna conservative bbox; guards bad coords from new_hydrant / wrong_location.
LON_MIN, LON_MAX = 26.5, 28.5
LAT_MIN, LAT_MAX = 42.7, 44.0
```

From `Varna_buildings/scratch/hydrant_consolidation_e0_and_pipeline_plan.md`
section 4:

```text
Gap: `apply_new_hydrant` dedups only on *exact*
coord-id collision — **no spatial proximity check**.
```

From the same plan, section 6:

```text
`match(point, dataset, Rm=5, Rf=20) → UPDATE | FLAG | ADD`
```

From the same plan, section 8:

```text
All four **SIGNED by Petar, 2026-06-21**:
```

Signed parameters from section 8:

```text
Rm = **5 m** / Rf = **20 m**
```

Signed sequencing from section 8:

```text
H1 before every apply. Never git push.
```

Additional confirmed H1 revision decisions from Petar, 2026-06-21:

1. `new_hydrant` UPDATE leaves `review_status` untouched.
2. Parity proof is code-vs-code on synthetic fixtures: current code versus
   refactored code, same input, byte-identical output. Historical reconstruction
   from audit reports is supplementary only.
3. FLAG result records use `action: "flagged"`, separate from `skipped`.
4. `new_hydrant` UPDATE appends provenance through the existing `_append_ref`
   mechanism and records issue number, report type, match distance, and old values.
5. On `new_hydrant` UPDATE, the report wins for canonical `type` and
   `operational_status`; old values go into provenance.

## Current Behavior Summary

Current reusable pieces in `scripts/apply_approved_reports.py`:

- IO and safety: `load_json`, `atomic_write_json`, `mojibake_scan`.
- Worker fetch: `fetch_approved_reports`.
- Lookup and identity helpers: `build_alias_index`, `canonical_coord_id`,
  `coords_in_bbox`, `field_short_id`.
- Diff helpers: `diff_set`, `diff_del`.
- Provenance helpers: `make_source_ref`, `_append_ref`.
- Result helpers: `_applied`, `_skip`.
- Typed handlers: `apply_exists_confirmed`, `apply_new_hydrant`,
  `apply_damaged`, `apply_missing`, `apply_wrong_location`.
- Pipeline and report: `process`, `build_report`, `ingested_issue_numbers`.
- CLI: argparse, summary printing, dry-run/apply write behavior.

Current issue:

- `apply_new_hydrant` validates bbox, creates `coord_<lon>_<lat>`, checks only
  exact alias/id collision, and otherwise appends a new `field_report` record.
- A report 3 m from an existing hydrant can silently become a duplicate ADD.

## Decision Ledger

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Add shared core at `scripts/lib/hydrant_core.py` plus `scripts/lib/__init__.py` | User request + section 6 | Existing script has reusable non-network code; H2 KMZ adapter will need same core | Easy rename/move | Approved for H1 plan |
| Keep `scripts/apply_approved_reports.py` as issue adapter and CLI | Local architecture | Worker fetch, argparse, printing, label instructions are issue-specific | Reversible | Planned |
| Move reusable match/merge/provenance/bbox/atomic-write/mojibake helpers into core | User request | These functions are currently embedded in one script | Reversible | Planned |
| Use standard library only | AGENTS dependency gate | No dependency manifest; no new deps requested | N/A | Planned |
| Use deterministic local meter distance helper | Existing scripts use stdlib meter helpers | `migrate_to_verbose_schema.py` and `backfill_addresses_20260511.py` already use stdlib geo distance | Reversible | Planned |
| Match thresholds are `UPDATE <= 5 m`, `FLAG (5,20] m`, `ADD > 20 m` | Signed H0 metadata | Petar signed Rm/Rf on 2026-06-21 | Threshold constants can change later | Approved |
| Tie-break nearest matches by `(distance_m, id)` | Determinism requirement | Prevents non-deterministic equal-distance behavior | Reversible | Planned |
| Existing non-`new_hydrant` handlers must be byte-identical | User constraint | Only intentional behavior change is `new_hydrant` spatial dedup | Reversible by localizing changes | Approved |
| `new_hydrant` ADD path keeps current record shape | Backward compatibility | Existing ADD creates `origin:"field_report"`, `existence_status:"verified"`, aliases, optional type/operational/report metadata | Reversible | Planned |
| `new_hydrant` UPDATE leaves `review_status` untouched | Petar 2026-06-21 | Explicit revision decision | Reversible | Approved |
| `new_hydrant` UPDATE report wins for canonical `type` / `operational_status` | Petar 2026-06-21 | Explicit overwrite policy | Reversible through provenance | Approved |
| `new_hydrant` UPDATE appends provenance via `_append_ref` | Petar 2026-06-21 | Full trace required | Reversible | Approved |
| Spatial UPDATE provenance includes `distance_m` only for spatial updates | Provenance need + parity constraint | Existing handlers should not gain new fields | Reversible | Planned |
| FLAG uses `action:"flagged"` | Petar 2026-06-21 | Explicit revision decision | Reversible | Approved |
| FLAG does not mutate records or provenance | Safety | FLAG is manual review queue, not an apply | Reversible | Planned |
| `ingested_issue_numbers` excludes `flagged` | Safety | A flagged issue still needs manual decision | Reversible | Planned |
| Stable-ID registry is stub/interface only | H0/H1/H3 split | Section 8 gates `coord_` migration at H3 | Reversible | Approved |

## Target Module Split

Create:

```text
scripts/lib/__init__.py
scripts/lib/hydrant_core.py
tests/test_hydrant_core.py
tests/test_apply_approved_reports_parity.py
```

Keep:

```text
scripts/apply_approved_reports.py
```

Core should own:

- Constants that are core semantics:
  - `KNOWN_REPORT_TYPES`
  - `CANONICAL_TYPES`
  - `CANONICAL_OPERATIONAL`
  - `LON_MIN`, `LON_MAX`, `LAT_MIN`, `LAT_MAX`
  - `DEFAULT_RM_M = 5.0`
  - `DEFAULT_RF_M = 20.0`
- IO safety:
  - `load_json`
  - `atomic_write_json`
  - `mojibake_scan`
  - `default_timestamp`
- Index and identity:
  - `build_alias_index`
  - `canonical_coord_id`
  - `coords_in_bbox`
  - `field_short_id`
  - `StableIdRegistry` stub/interface
  - `CoordIdRegistry` default implementation for H1
- Spatial matching:
  - `distance_m`
  - `find_nearest_hydrant`
  - `classify_spatial_match`
  - `match_point`
- Diff and provenance:
  - `diff_set`
  - `diff_del`
  - `make_source_ref`
  - `_append_ref`
- Results:
  - `_applied`
  - `_skip`
  - `_flagged`
- Handlers:
  - `apply_exists_confirmed`
  - `apply_new_hydrant`
  - `apply_damaged`
  - `apply_missing`
  - `apply_wrong_location`
- Pipeline and report:
  - `DISPATCH`
  - `process`
  - `build_report`
  - `ingested_issue_numbers`

Issue adapter should own:

- `DEFAULT_WORKER_URL`
- `WORKER_MAX_REPORTS`
- `fetch_approved_reports`
- `print_summary`
- argparse and main CLI
- `--dry-run` / `--apply` write selection
- post-apply user instructions for manual GitHub labels

## Spatial Matcher Design

Use a standard-library local meter distance helper. Recommended form:

```text
distance_m(a, b):
  lon1, lat1 = a
  lon2, lat2 = b
  lat0 = radians((lat1 + lat2) / 2)
  x = radians(lon2 - lon1) * cos(lat0) * EARTH_RADIUS_M
  y = radians(lat2 - lat1) * EARTH_RADIUS_M
  return hypot(x, y)
```

Rationale:

- No new dependency.
- Deterministic and sufficient for 1-25 m comparisons in Varna oblast.
- Matches the local meter projection style used in the planning probe.

Matcher contract:

```text
match_point(point, records, *, rm_m=5.0, rf_m=20.0)
  -> SpatialMatch(decision, nearest_record, distance_m)
```

Decision rules:

```text
distance <= 5.0       -> UPDATE
5.0 < distance <= 20.0 -> FLAG
distance > 20.0 or no records -> ADD
```

Tie-break:

```text
min(candidates, key=(distance_m, record["id"]))
```

Implementation note:

- H1 may scan all records linearly. With 5,911 records and only issue-ingest
  volume, this is small and avoids premature indexing.
- A grid index can be added later if KMZ H2 needs it.

## `new_hydrant` Behavior

### Common validation

For all `new_hydrant` reports:

1. Read `reported_coord`.
2. Apply existing bbox guard through `coords_in_bbox`.
3. If invalid, return existing skip behavior:

```json
{"action": "skipped", "skip_reason": "missing_or_invalid_coord"}
```

### Exact alias/id idempotency

Before spatial ADD, preserve current exact-id guard:

- Compute `new_id = registry.id_for(lon, lat)`.
- If `new_id in state["alias"]`, do not ADD.
- This remains a skip/idempotency guard, unless executor finds an existing
  stronger local pattern in tests.

### UPDATE path: `distance <= 5 m`

When nearest existing record is within `Rm`:

1. Mutate the nearest existing record, not coordinates.
2. Add report aliases from `report["id"]`:
   - full report UUID if present
   - `field_<8>` short id if present and different
   - do not duplicate aliases
3. Set `existence_status` to `"verified"` through `diff_set`.
4. Apply canonical `type` if present and valid. The report wins:
   - if existing value differs, overwrite it
   - old value goes into `old_values`
5. Apply canonical `operational_status` if present and valid. The report wins:
   - if existing value differs, overwrite it
   - old value goes into `old_values`
6. Do not delete or modify `review_status`.
7. Append provenance with `_append_ref`.

Provenance requirements for UPDATE:

- Use existing `make_source_ref` shape for the common fields.
- Include:
  - `issue_number`
  - `report_type: "new_hydrant"`
  - `old_id` as the matched existing id
  - `old_coord` as the matched existing coordinates
  - `changes`
  - `old_values`
  - `approver_id`
  - `timestamp`
  - spatial `distance_m`
- Add `distance_m` only when passed; existing handlers must not gain this field.
- Round `distance_m` to a stable precision such as 3 decimal places.

Expected result row for UPDATE:

```json
{
  "issue_number": 123,
  "report_type": "new_hydrant",
  "action": "applied",
  "target_id_before": "coord_existing",
  "target_id_after": "coord_existing",
  "spatial_decision": "UPDATE",
  "distance_m": 1.234,
  "changes": {}
}
```

The exact `changes` object should follow existing `_applied` conventions and
include only real diffs.

### FLAG path: `5 m < distance <= 20 m`

When nearest existing record is within `Rf` but outside `Rm`:

1. Do not mutate `state["records"]`.
2. Do not mutate `state["provenance"]`.
3. Return a flagged result record.
4. Do not mark the issue ingested.

Expected result row:

```json
{
  "issue_number": 123,
  "report_type": "new_hydrant",
  "action": "flagged",
  "flag_reason": "spatial_near_match",
  "nearest_id": "coord_existing",
  "distance_m": 6.0,
  "changes": {}
}
```

`build_report` should include `flagged_count` and `flagged_reasons` only when at
least one flagged result exists. This preserves byte-identical report output for
old synthetic fixtures with no flagged results.

### ADD path: `distance > 20 m`

When no existing hydrant is within `Rf`:

1. Keep current ADD behavior and record shape.
2. Create a new `field_report` record with:
   - `id`
   - `coords`
   - `origin: "field_report"`
   - `existence_status: "verified"`
   - `legacy_ids`
   - optional canonical `type`
   - optional canonical `operational_status`
   - optional `report_id`
   - optional `reported_at`
3. Add aliases to `state["alias"]`.
4. Create provenance using the existing `make_source_ref` new-record shape.

## Stable-ID Registry Stub

H1 must not migrate existing ids.

Add only a small interface/stub:

```text
class StableIdRegistry:
    def id_for_new_record(self, lon, lat, *, source_ref=None) -> str:
        raise NotImplementedError

class CoordIdRegistry(StableIdRegistry):
    def id_for_new_record(self, lon, lat, *, source_ref=None) -> str:
        return canonical_coord_id(lon, lat)
```

Use `CoordIdRegistry` as the default in H1 so ADD output remains compatible with
current `coord_*.5f` ids.

## Implementation Steps

1. Add `scripts/lib/__init__.py`.
2. Add `scripts/lib/hydrant_core.py`.
3. Move reusable constants/helpers from `scripts/apply_approved_reports.py` into
   the core without changing bodies first.
4. Update `scripts/apply_approved_reports.py` imports so it delegates to the core.
5. Run parity tests at this point before adding spatial changes.
6. Add `SpatialDecision` / `SpatialMatch` using `dataclasses` or named tuples.
7. Add `distance_m`, `find_nearest_hydrant`, `classify_spatial_match`, and
   `match_point`.
8. Add `StableIdRegistry` and `CoordIdRegistry` stub.
9. Update only `apply_new_hydrant` for spatial UPDATE / FLAG / ADD.
10. Extend `_append_ref` / `make_source_ref` with optional `distance_m`, emitted
    only when not `None`.
11. Add `_flagged`.
12. Update `build_report` to account for flagged results only when present.
13. Update `ingested_issue_numbers` so only `action == "applied"` is returned.
14. Add tests.
15. Run all tests and encoding scans.
16. Stop. Do not run real `--apply`; do not commit; do not push.

## Byte-Identical Parity Requirement

Primary parity guarantee:

- Code-vs-code on synthetic fixtures.
- Run the current implementation and the refactored implementation on the same
  synthetic inputs.
- Assert byte-identical JSON serialization for records, provenance, and report
  for existing handlers:
  - `exists_confirmed`
  - `damaged`
  - `missing`
  - `wrong_location`

Important:

- This is the primary proof.
- Historical reconstruction from audit reports is supplementary only.
- Do not claim reconstructed May 28 reports prove historical Worker payload parity.

Recommended parity harness:

1. Before changing behavior, preserve a callable copy/path of current logic inside
   tests or a fixture module, or generate golden outputs from current HEAD in temp
   files.
2. Use fixed timestamp, fixed approver id, and deterministic JSON serialization:

```text
timestamp = "2026-06-21T00:00:00+03:00"
approver_id = "petar"
json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
```

3. Compare serialized bytes.

## Test Plan

Use Python standard library tests:

```powershell
python -m unittest discover -s tests
```

No pytest dependency.

### Unit tests: spatial matcher

Test deterministic boundary behavior using synthetic points:

| Case | Expected |
|---|---|
| report 1 m from existing | `UPDATE` |
| report 6 m from existing | `FLAG` |
| report 25 m from existing | `ADD` |
| two equal-distance candidates | nearest tie breaks by id |
| no records | `ADD` |

### Unit tests: `new_hydrant` UPDATE

Fixture:

- Existing record has id, coords, `type`, `operational_status`, `review_status`.
- Report is 1 m away and carries different valid `type` and
  `operational_status`.

Assertions:

- Record count unchanged.
- Existing record id unchanged.
- Existing coords unchanged.
- `review_status` unchanged.
- Report aliases added exactly once.
- `existence_status` becomes `"verified"` if not already.
- Report `type` overwrites existing `type`.
- Report `operational_status` overwrites existing `operational_status`.
- Provenance appended to matched id.
- Provenance contains old values for overwritten fields.
- Provenance contains `distance_m`.
- Result action is `"applied"` with `spatial_decision:"UPDATE"`.
- `ingested_issue_numbers` includes this issue.

### Unit tests: `new_hydrant` FLAG

Fixture:

- Existing record at 6 m from report.

Assertions:

- Record count unchanged.
- Record object unchanged.
- Provenance unchanged.
- Result action is `"flagged"`.
- Result contains `nearest_id`, `distance_m`, and `flag_reason`.
- `build_report` includes `flagged_count` only for flagged run.
- `ingested_issue_numbers` does not include the flagged issue.

### Unit tests: `new_hydrant` ADD

Fixture:

- No existing record within 20 m.

Assertions:

- Record count increases by 1.
- New record shape matches current ADD behavior.
- New provenance shape matches current new-record provenance.
- Aliases are added.
- Result action is `"applied"`.

### Existing handler parity

Synthetic fixture set:

- `exists_confirmed` target found, with absent fields.
- `exists_confirmed` target found, with existing `review_status`.
- `damaged` with canonical operational status.
- `missing` on existing target.
- `wrong_location` with coordinate change inside bbox.
- `wrong_location` exact id collision case.
- target-not-found skip case.
- invalid coord skip case.

Assertions:

- Current code output bytes equal refactored code output bytes for:
  - resulting records
  - resulting provenance
  - result report

### Supplementary historical check

Use available audit reports only as a supplementary replay report:

- `audit/ingest_reports/ingest_2026-05-28.json`
- `audit/ingest_reports/ingest_2026-05-28_batch.json`
- `data/hydrants.json.pre_address_backfill.json`
- `data/hydrants_provenance.json.pre_address_backfill.json`

Required framing:

- This is not the primary parity proof.
- It can surface which historical `new_hydrant` entries H1 would classify
  differently.

Read-only planning probe already surfaced:

| Issue | H1 classification | Nearest existing | Distance |
|---:|---|---|---:|
| #44 | ADD | `coord_27.86768_43.22266` | 149.14 m |
| #45 | ADD | `coord_27.87177_43.22183` | 33.41 m |
| #46 original `new_hydrant` override | FLAG | `coord_27.89806_43.20868` | 8.99 m |
| #47 | ADD | `coord_27.87952_43.23761` | 127.17 m |
| #48 applied as `new_hydrant` override | ADD | `coord_27.89611_43.22234` | 82.99 m |
| #49 | ADD | `coord_27.87677_43.22910` | 111.33 m |
| #50 | ADD | `coord_27.87929_43.22929` | 139.06 m |
| #51 | ADD | `coord_27.63047_43.19815` | 543.91 m |
| #60 | ADD | `coord_27.84386_43.24628` | 35.69 m |
| #61 | ADD | `coord_27.89908_43.22646` | 111.98 m |
| #63 | ADD | `coord_27.89919_43.22531` | 77.14 m |

The final implementation should generate and print/report this class of
"historical new_hydrant entries that would resolve differently" instead of
hiding it.

### Safety tests

- `missing` never removes a record.
- Bbox guard still rejects invalid/out-of-scope coordinates.
- Dry-run remains default.
- `--apply` and `--dry-run` remain mutually exclusive.
- `atomic_write_json` writes only in temp directories during tests.
- No test writes real `data/hydrants.json` or real provenance.

### Encoding tests

Run the repo-prescribed mojibake scan on changed text files:

```powershell
Select-String -Path <path> -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8
```

Also keep serialized-object scans:

- `mojibake_scan("hydrants", state["records"])`
- `mojibake_scan("provenance", state["provenance"])`
- `mojibake_scan("report", report)`

## Acceptance Criteria

H1 is acceptable only if all are true:

1. `scripts/apply_approved_reports.py` still defaults to dry-run.
2. No real data files are modified by tests or implementation.
3. No new runtime/build/test dependency is introduced.
4. Existing non-`new_hydrant` handler outputs are byte-identical under synthetic
   code-vs-code parity tests.
5. `new_hydrant` 1 m test updates existing record and appends provenance.
6. `new_hydrant` 6 m test flags and mutates nothing.
7. `new_hydrant` 25 m test adds a new record using current ADD shape.
8. `review_status` remains untouched on `new_hydrant` UPDATE.
9. Report canonical `type` and `operational_status` win on `new_hydrant` UPDATE,
   with old values in provenance.
10. FLAG uses `action:"flagged"` and is not treated as skipped or ingested.
11. `missing` still never auto-drops.
12. Bbox guard remains active.
13. Mojibake scans pass, excluding only the scanner regex itself if detected.
14. `git status --short` after implementation shows only intended H1 code/test
    files and this plan file.
15. No commit and no push are performed by the executor unless Petar separately
    instructs that later.

## Approval-Gate Check

| Gate | H1 status |
|---|---|
| Architecture/file layout change | Yes: adds shared core module. This plan is the approval artifact. |
| Data-source change | No. |
| Runtime dependency | No. |
| Build/test dependency | No. Use stdlib `unittest`. |
| Data mutation | No real data mutation in H1. |
| UI wording / Bulgarian labels | No. |
| Worker contract | No. |
| KMZ parsing/apply | No. |
| Stable-ID migration | No. Stub only; H3 handles migration. |
| GitHub issue relabeling | No. |
| Commit | Not authorized by this plan. |
| Push | Forbidden. Petar pushes personally if/when appropriate. |

## Open Questions

None. Petar resolved the remaining H1 questions on 2026-06-21:

- `review_status` remains untouched on `new_hydrant` UPDATE.
- Parity proof is code-vs-code synthetic fixtures; historical reconstruction is
  supplementary only.
- FLAG is `action:"flagged"`.
- UPDATE provenance is required.
- Report canonical fields win on UPDATE, with old values preserved in provenance.

