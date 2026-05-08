# Cleanup Execution Plan - 2026-05-08

Target document: `docs/audits/cleanup_execution_plan_20260508.md`. This is the ratified, execution-ready plan body.

## Protocol Preamble

Request scope: synthesize Petar-ratified cleanup decisions into a concrete multi-phase execution plan. Out of scope: cleanup execution, data edits, UI redesign, submission-flow changes beyond compatibility handling, reverse geocoding, Worker extraction, moderation implementation, and runtime dependency changes.

Current repo state observed during planning: `HEAD 128a740`; audit file last committed at `66962d8`.

Deterministic inventory for cleanup-plan scope, sorted repo file list excluding `.git`:

```text
AGENTS.md
CLAUDE.md
README.md
audit\apply_field_reports.py
audit\plans\2026-05-05_navigation_accuracy_fix.md
audit\plans\2026-05-05_volunteer_ready_ux_sprint1.md
audit\verify_browser.js
audit\verify_report_feature.js
audit\worker_post_commit15.js
audit\worker_pre_commit15.js
data\hydrants.json
docs\activeContext.md
docs\architecture\data_roadmap_20260508.md
docs\audits\bug_fixes_plan_20260508.md
docs\audits\data_architecture_audit_20260508.md
docs\audits\data_audit_and_target_schema_20260508.md
docs\audits\governance_proposal_20260508.md
docs\audits\issue_ingest_plan_20260508.md
docs\audits\submission_status_and_moderation_plan_20260508.md
docs\plans\commit_15_worker_get.md
docs\plans\sprint_1_5_polish.md
extract_hydrants.py
field_reports.json
geo_fire_hydrants.json
geo_fire_hydrants.kml
hydrants_varna.json
index.html
wfsrequest.txt
```

Target/missing-path checks:

```text
MISSING docs/audits/cleanup_execution_plan_20260508.md
MISSING data/hydrants_provenance.json
MISSING data/hydrants.json.pre_cleanup_snapshot.json
MISSING scripts/migrate_to_verbose_schema.py
MISSING scripts
MISSING package.json
MISSING src
MISSING dist
MISSING .github/workflows
```

Files read in this session:

- `AGENTS.md`
- `docs/activeContext.md`
- `docs/audits/data_audit_and_target_schema_20260508.md`
- `index.html`, targeted app regions around data load, marker rendering, labels, list/card display, report modal, and polling merge
- `data/hydrants.json`, parsed fully
- `field_reports.json`, parsed fully

Negative findings matrix:

| Category / pattern in scope | Finding |
|---|---|
| Target cleanup plan file | No existing `docs/audits/cleanup_execution_plan_20260508.md`. |
| Provenance archive | No existing `data/hydrants_provenance.json`. |
| Snapshot file | No existing `data/hydrants.json.pre_cleanup_snapshot.json`. |
| Migration script/location | No `scripts/` directory and no `scripts/migrate_to_verbose_schema.py`. |
| Build/runtime structure | No `package.json`, `src/`, `dist/`, or `.github/workflows`. |
| Worker source | No `worker/` directory in inventory; live Worker remains external. |
| Current runtime verbose fields | `data/hydrants.json` has no `existence_status`, `operational_status`, `review_status`, `legacy_ids`, or `source_refs` fields. |
| New pin classes | No existing `.h-pin.operational` or `.h-pin.broken` CSS classes. |
| Encoding scan | No mojibake regex matches in files read using `[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]` with UTF-8 decoding. |
| Binary/source archives | KMZ/SHP/DBF source archive contents were not inspected and are not used as evidence in this plan. |

Quoted declared metadata treated as authoritative:

> `Last updated: 2026-05-08 at commit 2d8b767`

> `data/hydrants.json: 968,365 bytes (6,082 records — 8 field reports ingested in commit 2dcab73)`

> `field_reports.json: 5,085 bytes (14 records)`

> `Status counts: 23 verified, 2 reported, 6,057 canonical (in repo; runtime can grow via polled new_hydrant reports)`

> `First load now 1,271,722 bytes, well under the 2 MB hard cap`

Audit evidence used:

> `data/hydrants.json` parsed successfully as a JSON array of 6,082 objects.

> Exact duplicate coordinates: `109 clusters / 301 records / 192 excess records`.

> Near duplicates at `<= 5m`: `626` pairs, `119` connected clusters, `324` records, `205` excess records, `2` cross-origin clusters.

> `field_reports.json` contains 14 records, all duplicated identically in `data/hydrants.json`.

Decision ledger:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Use three-phase rollout | Petar ratification | Phase 1 adapter, Phase 2 migration, Phase 3 adapter removal specified in request | Revert per phase | Approved |
| Set 17 deferred type records to unknown | Petar ratification + audit §13A | 16 `70/80`, 1 `ПК1` listed and verified present | Field reports can promote later | Approved |
| Drop `field_reports.json` | Petar ratification + audit §9 | 14 byte-equivalent records already in runtime data | Recoverable from Git history | Approved |
| Auto-merge C1/C2 duplicates | Petar ratification + audit §3 | Exact and <=5m duplicate counts reproduced | Revert Phase 2 | Approved |
| Preserve C3 conflict records | Petar ratification | 3 exact-coordinate national type-conflict clusters; recomputed as 27 records / 24 extra preserved records | Field-resolution later | Approved |
| C3 unique IDs use coordinate base plus old ID suffix | Petar answer in planning | Prevents coordinate-derived ID collision while preserving C3 records | Reversible after field resolution | Approved |
| Add runtime `legacy_ids` | Petar answer in planning | Needed so old open GitHub issues and old report IDs dedupe after coordinate-ID migration | Removable after old issues are closed/filtered | Approved |
| Use `existence_status`, `operational_status`, `review_status` | Petar ratification | English code vocab supplied in request | Schema migration reversible | Approved |
| Add green/black pin classes | Petar ratification | Exact CSS classes supplied in request | Revert Phase 1/3 | Approved |
| Move rich provenance to `data/hydrants_provenance.json` | Petar ratification | `z`, `s`, `st`, `i_original`, duplicate/replacement fields listed | Archive remains in repo | Approved |
| Keep Worker source external | Repo evidence | `AGENTS.md` says live Worker canonical until commit 17 | Add `worker/` later | Existing approved state |

Approval-gate check:

- Data source change: allowed only after this fresh Codex analysis and Petar approval; Phase 2 still needs explicit execution handoff.
- UI labels: only Petar-ratified Bulgarian labels are introduced.
- Dependencies: no runtime/build dependency; Python script uses standard library only.
- File layout: `scripts/` is new; this plan makes it explicit and dev-only.
- Hard cap: read-only estimate with verbose runtime records plus `legacy_ids` is about `808,476` data bytes and `1,113,091` bytes with current `index.html`, below the 2 MB hard cap.
- Architecture: static GitHub Pages architecture remains unchanged.

## Section 1: Phase 1 Detailed Plan - Frontend Adapter

### 1A. Files Touched

- `index.html` only.

### 1B. Adapter Logic

Add `normalizeHydrantRecord(raw)` immediately after JSON parsing. It accepts compact or verbose records and returns the existing in-memory compact-compatible shape plus new semantic fields:

```js
{
  i,                  // canonical runtime id, from raw.id ?? raw.i
  c,                  // [lon, lat], from raw.coords ?? raw.c
  o, a, r, t,         // compatibility fields for current code paths
  existence_status,   // from raw.existence_status or legacy raw.status
  operational_status, // raw.operational_status or null
  review_status,      // raw.review_status or legacy raw.status === "reported"
  legacy_ids          // array, includes old ids/report ids when supplied
}
```

Rules:

- Compact `status:"verified"` maps to `existence_status:"verified"`.
- Compact `status:"reported"` maps to `review_status:"reported"`.
- Missing compact/verbose existence means unverified.
- Missing/null operational state means not tested/unknown.
- Invalid missing IDs or coords are skipped with a console warning; no user-facing UI copy change.
- Build `HYDRANTS_BY_ID` with both `h.i` and every `h.legacy_ids[]`.
- Add `resolveHydrantById(id)` and use it in polling paths instead of direct `HYDRANTS_BY_ID[id]`.
- In `applyReports`, normalize runtime-created `new_hydrant` records and dedupe against full UUID, `field_<8>`, canonical id, and `legacy_ids`.

### 1C. New CSS Classes

Add exactly:

```css
.h-pin.operational { background:#2e7d32; color:white; }
.h-pin.broken { background:#212121; color:white; }
```

### 1D. Bulgarian Label Lookup Table

Add non-invasive lookup helpers:

```js
const EXISTENCE_LABELS = {
  verified: 'Проверен',
  unverified: 'Непроверен',
  missing: 'Липсва'
};

const OPERATIONAL_LABELS = {
  works: 'Работи',
  not_working: 'Не работи',
  not_tested: 'Не е тестван'
};
```

Do not add review-status display labels in this phase.

### 1E. Pin Rendering Logic

Replace `hydrantStatusClass(h)` with semantic precedence:

1. `review_status` of `reported` or `pending_review` -> `reported` yellow.
2. `existence_status === "missing"` -> not expected in data; if encountered, skip rendering.
3. `existence_status === "verified"` and `operational_status === "works"` -> `operational` green.
4. `existence_status === "verified"` and `operational_status === "not_working"` -> `broken` black.
5. `existence_status === "verified"` -> `verified` red.
6. Default -> `canonical` gray.

Keep `L.divIcon` for all markers.

### 1F. Test Plan And Stop Trigger

Before applying Phase 1, Claude Code must grep all callers of `hydrantStatusClass` in `index.html` and verify the function signature and return shape change do not break any caller.

Stop and ask if any caller expects a different return shape, passes anything other than a hydrant record, or uses the return value outside CSS class construction.

Then verify:

- Serve locally with `python -m http.server 8000`.
- Phone smoke test: load over HTTP, allow GPS, confirm map loads and current compact data shows same gray/red/yellow behavior as before.
- Exercise modes: `Близо <100м`, `Топ 5`, `Всички`.
- Tap pin, long-press pin, open report picker, cancel.
- Confirm active target line/card/arrow still update.
- Confirm polling does not duplicate already-ingested `field_*` reports.
- Desktop console: no data-load errors; `meta` still shows `6082 точки`.
- Run UTF-8 mojibake scan on `index.html`.

### 1G. Rollback

Revert the single Phase 1 `index.html` commit.

### 1H. Estimated Diff Size

Approximately `+130` to `+190` lines, mostly adapter, alias lookup, semantic status helper, and CSS.

## Section 2: Phase 2 Detailed Plan - Data Migration

### 2A. Migration Script Design

Add `scripts/migrate_to_verbose_schema.py` using only Python standard library.

CLI shape:

```powershell
python scripts/migrate_to_verbose_schema.py `
  --input data/hydrants.json `
  --field-reports field_reports.json `
  --output data/hydrants.json `
  --provenance data/hydrants_provenance.json `
  --report docs/audits/cleanup_migration_report_20260508.json
```

Implementation requirements:

- Write outputs through temporary files, then replace only after all assertions pass.
- Support `--dry-run` that writes no tracked files and prints summary counts.
- Halt with nonzero exit on any unexpected validation failure.

### 2B. Backup Strategy

First Phase 2 commit is snapshot-only:

- Add `data/hydrants.json.pre_cleanup_snapshot.json` as an exact byte snapshot of current `data/hydrants.json`.
- Do not modify runtime data in that commit.

### 2C. Migration Sequence With Assertions

1. Load and validate input:
   - Assert `data/hydrants.json` count `6082`.
   - Assert origins: `vik:3661`, `national:2407`, `field_report:14`.
   - Assert legacy status counts: `verified:23`, `reported:2`, absent `6057`.
   - Assert no duplicate old `i`, no invalid coords, all coords in Varna sanity bounds.
   - Assert all 14 `field_reports.json` records are byte-equivalent to matching runtime records.

2. Detect duplicate clusters:
   - Exact rounded-6 coordinate clusters: `109`, records `301`, excess `192`.
   - <=5m connected clusters: `119`, records `324`, excess `205`.
   - C3 type-conflict clusters: `3`, records `27`, preserved extra `24`.

3. Apply duplicate policy:
   - C3 records are kept individually, set `type` absent and `operational_status` absent, and get IDs like `coord_27.31791_42.98300__NAT-6761`.
   - All other <=5m duplicate components merge to one survivor.
   - Winner priority: `field_report` verified records first, then `national`, then `vik`; within same priority choose richer record by verified/reported status, normalized type, address, region, provenance, then stable original order.
   - National beats VIK for national+VIK <=5m conflicts.
   - Preserve all old IDs/report IDs in runtime `legacy_ids` and rich `source_refs` in provenance.

4. Apply Q13A:
   - The 17 listed records get `type` absent if they survive directly.
   - If a listed record is merged, its unknown raw type is recorded only in provenance.
   - Each Q13A old ID must be reconciled in the migration report under `q13a_reconciliation`.

5. Normalize remaining type values:
   - `ground` -> `надземен`
   - `underground` -> `подземен`
   - contains `надземен` -> `надземен`
   - contains `подземен` -> `подземен`
   - `ПКн`, `ПХ 70/80`, `ПХ DN 80` -> `надземен`
   - unexpected populated values halt the script.

6. Migrate compact keys to verbose runtime records:
   - Required: `id`, `coords`, `origin`.
   - Optional: `legacy_ids`, `address`, `type`, `existence_status`, `operational_status`, `review_status`, `region`, `report_id`, `reported_at`.
   - Omit unverified and not-tested defaults unless explicitly present.
   - Legacy `status:"verified"` -> `existence_status:"verified"`.
   - Legacy `status:"reported"` -> `review_status:"reported"`.
   - Records with `existence_status:"missing"` are dropped from runtime and recorded in the migration report; none are expected in current input.

7. Derive coordinate IDs after dedup:
   - Normal: `coord_${lon.toFixed(5)}_${lat.toFixed(5)}`.
   - C3 exception: append `__${old_id}`.
   - Any remaining ID collision halts.

8. Extract provenance:
   - Create `data/hydrants_provenance.json`, object keyed by new `id`.
   - Each value contains `source_refs` with old IDs, old coords, raw type/status, `s`, `st`, `z`, `i_original`, `duplicate_distance_m`, `replaced_vik`, `replaced_vik_coord`, merge action, and conflict flags.
   - Provenance is not fetched by the app.

9. Drop `field_reports.json`.

Expected output under current data and this winner policy:

- Runtime records: `5901`.
- Delta: `6082 - 181`, where `181 = 205 <=5m excess - 24 C3 preserved extra records`.
- Origins: `field_report:14`, `national:2345`, `vik:3542`.
- Existence/review: `verified:23`, `review_status reported:2`, unverified/absent `5878`.
- Type: `надземен:1144`, `подземен:1147`, absent `3610`.

### 2D. Migration Report Format

Write `docs/audits/cleanup_migration_report_20260508.json`:

```json
{
  "summary": {
    "input_count": 6082,
    "output_count": 5901,
    "merged_count": 181,
    "c3_preserved_records": 27
  },
  "q13a_reconciliation": {
    "input_count": 17,
    "output_type_null_due_to_q13a_count": 14,
    "output_type_null_due_to_other_reasons_count": 3596,
    "records": [
      {
        "old_id": "VIK-VARNA_IZTOK-0207",
        "new_id": "coord_27.90405_43.20722",
        "action": "merged",
        "cluster_id": "dup5m_0009",
        "type_result": null,
        "notes": "Q13A ambiguous type preserved as unknown in survivor/provenance"
      }
    ]
  },
  "records": [
    {
      "old_id": "VIK-VARNA_IZTOK-0207",
      "new_id": "coord_27.90405_43.20722",
      "action": "merged",
      "reason": "duplicate_5m",
      "winner": false,
      "source_records_preserved": ["VIK-VARNA_IZTOK-0207", "VIK-VARNA_ZAPAD-0205"]
    }
  ]
}
```

Requirements:

- Every old `i` appears exactly once in `records`.
- All 17 Q13A old IDs appear exactly once in `q13a_reconciliation.records`.
- Per Q13A record, action is one of:
  - `kept_standalone_type_null`
  - `merged_type_null_in_survivor`
  - `dropped_because_of_conflict`
- `q13a_reconciliation` reports both the input count and the output count of canonical records whose `type` is null due to Q13A versus other reasons.

### 2E. Test Plan

- JSON parse: runtime data, provenance archive, migration report.
- Runtime schema assertion: no compact keys `i`, `c`, `o`, `a`, `r`, `s`, `st`, `z`, `t`, or legacy `status`.
- Required fields: every runtime record has unique `id`, valid `coords`, and `origin`.
- Alias assertion: every old ID and report UUID resolves through either canonical `id` or `legacy_ids`.
- Count assertions match Section 2C.
- Q13A assertion: `q13a_reconciliation.input_count === 17`; all listed old IDs are reconciled; output type-null counts match runtime data.
- Duplicate assertion: no <=5m duplicate components remain except the three C3 same-coordinate conflict groups.
- Provenance assertion: one archive entry per runtime record; every dropped/merged source record preserved in some `source_refs`.
- Encoding: UTF-8 parse and mojibake scan for all changed `.html`, `.json`, `.py`, `.md`.
- Size: first load remains below 2 MB.

### 2F. Phone Verification

- Serve locally and hard-refresh phone.
- Confirm app loads via Phase 1 adapter and shows `5901 точки`.
- Confirm gray/red/yellow current semantics.
- Check known Q13A records render gray if visible.
- Check a normalized national `ground` record displays `Надземен`; an `underground` record displays `Подземен`.
- Check an existing verified record remains red.
- Check an existing reported record remains yellow.
- Verify C3 conflict records are visible as gray clustered/same-coordinate records with unique IDs.
- Confirm report polling does not duplicate old field reports because `legacy_ids` aliases resolve old IDs.
- Pin colors green (`operational_status:"works"`) and black (`operational_status:"not_working"`) cannot be verified against real records during Phase 2 because no records carry `operational_status` values yet. CSS classes and rendering logic are deployed in Phase 1 and ready for use, but visual verification is deferred to the first real record populated after the future Section E submission-flow extension.

### 2G. Rollback

Preferred rollback is `git revert` of Phase 2 commits. If manual recovery is needed, restore `data/hydrants.json` from the committed snapshot, restore `field_reports.json` from Git history, and remove the generated provenance/report files in a rollback commit.

### 2H. Estimated Record Count Delta

Input `6082` -> expected output `5901` with current data. If `data/hydrants.json` changes before execution, rerun dry-run and update expected counts before applying.

## Section 3: Phase 3 Detailed Plan - Adapter Removal

### 3A. Files Touched

- `index.html` only.

### 3B. Specific Code Paths To Remove

Remove compact-schema compatibility after Phase 2 phone verification passes:

- Delete compact reads in `normalizeHydrantRecord`: `raw.i`, `raw.c`, `raw.o`, `raw.a`, `raw.r`, `raw.t`, `raw.status`.
- Replace internal usage:
  - `h.i` -> `h.id`
  - `h.c` -> `h.coords`
  - `h.o` -> `h.origin`
  - `h.a` -> `h.address`
  - `h.r` -> `h.region`
  - `h.t` -> `h.type`
- Keep `legacy_ids` alias indexing for old report compatibility.
- Make polling create verbose records directly: `id`, `coords`, `origin`, `review_status`.
- Make `hydrantStatusClass` read only `existence_status`, `operational_status`, and `review_status`.
- Simplify `hydrantTypeLabel` to expect normalized Bulgarian type only.
- Remove list/card/report-modal fallback references to source fields `s` and `st`.

### 3C. Test Plan

- Local desktop smoke and phone smoke match end of Phase 2.
- Confirm all three modes, active target, navigation, long-press report picker, manual placement, and polling.
- Confirm no compact-key access errors in console.
- Confirm old issue/report aliases still dedupe via `legacy_ids`.
- Run mojibake scan and size check.

### 3D. Rollback

Revert the single Phase 3 `index.html` commit. Phase 2 data remains valid because Phase 1 adapter can read verbose records.

## Section 4: Inter-Phase Decision Gates

| Boundary | Must verify before proceeding | Failure requiring rollback | Time between phases |
|---|---|---|---|
| Phase 1 -> Phase 2 | Caller audit clean; phone smoke clean; current compact data visually unchanged; no polling duplicate; no console errors; first load below cap | App fails to load, pin colors regress, GPS/list/card/report picker breaks, polling duplicates field reports, `hydrantStatusClass` caller mismatch | Separate session; at least one full phone pass, about 30-60 min |
| Phase 2 -> Phase 3 | All migration assertions pass; output count `5901`; Q13A reconciliation complete; provenance and report complete; phone smoke clean; old report aliases dedupe | Count mismatch, ID collision, lost provenance, Q13A mismatch, app load failure, duplicate old reports, wrong pin status | Separate session; expect 60-90 min verification |
| After Phase 3 | Behavior unchanged from Phase 2; no compact-key console errors; phone smoke clean | Any behavior that worked at Phase 2 fails after adapter removal | Separate session; about 30-45 min |

## Section 5: Risk Catalog

| Risk | Mitigation | Detection | Recovery |
|---|---|---|---|
| Adapter introduces subtle rendering regression | Phase 1 changes code only, data unchanged; semantic helper has explicit precedence; caller audit before patch | Phone visual comparison against current pins; console check; grep caller audit | Revert Phase 1 |
| Migration script corrupts data | Snapshot first; temp-file writes; dry-run; strict assertions; migration report maps every old ID | JSON/count/schema/provenance assertions | Revert Phase 2 or restore snapshot |
| Coordinate ID collision after dedup | Normal collision halts; C3 uses approved `coord_*__old_id` suffix | ID uniqueness assertion | Fix script or revert Phase 2 |
| Q13A records silently misclassified | Dedicated `q13a_reconciliation` report key and assertions | Compare 17 expected old IDs against report and runtime type-null counts | Fix script before commit or revert Phase 2 |
| Provenance archive loses needed data | Store full source refs for every old record and every merge/drop | Assert every old ID appears once in migration report and provenance | Rebuild from snapshot/Git history |
| Adapter removal exposes incomplete migration | Keep Phase 3 separate; test after Phase 2 first | Compact-key access errors, missing list/card values | Revert Phase 3 only |
| Old open GitHub issues duplicate records after coordinate IDs | Runtime `legacy_ids` aliases for old IDs/report UUIDs | Polling smoke after Phase 2 | Revert Phase 2 or add missing aliases |
| First load grows too large | Move rich provenance out of runtime; omit default fields | Byte-size check before commit | Reduce runtime optional fields or revert |
| Green/black rendering untested against real data in Phase 2 | Document deferral until Section E creates real `operational_status` records | First real post-Section E record with `works`/`not_working` | Fix CSS/status helper in that sprint if needed |

## Section 6: Open Questions For Petar

No blocking open questions remain after this planning session.

Defaults locked by this plan:

- Provenance archive filename: `data/hydrants_provenance.json`.
- Migration script path: `scripts/migrate_to_verbose_schema.py`.
- Migration report path: `docs/audits/cleanup_migration_report_20260508.json`.
- Adapter function names: `normalizeHydrantRecord`, `resolveHydrantById`, `hydrantStatusClass`, `hydrantTypeLabel`.
- Assertion failure behavior: halt with nonzero exit and write no final outputs.
- C3 ID collision handling: coordinate-derived base plus old-ID suffix.
- Old report compatibility: runtime `legacy_ids` retained in verbose data.
