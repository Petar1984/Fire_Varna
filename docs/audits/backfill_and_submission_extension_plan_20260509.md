# Backfill Verified Type And Submission Flow Extension Plan

Target document: `docs/audits/backfill_and_submission_extension_plan_20260509.md`.

## Protocol Preamble

Request scope: read-only investigation for two linked concerns: one-shot `type: "надземен"` backfill for verified records missing type, and a future submission-flow extension for canonical `type` + `operational_status`. Out of scope: implementation, 10m duplicate threshold widening, display redesign beyond existing pin color rules, reverse geocoding, and moderation except where Worker extraction is a dependency.

Current repo state observed during planning: `HEAD 142a494 refactor(adapter): Phase 3 remove compact-schema compatibility`; working tree clean. `activeContext.md` is stale relative to current `HEAD`; parsed repo data is authoritative for this plan.

Deterministic inventory scope: full filesystem under `C:\Projects\Varna_hydrants`, excluding `.git`.

Files read during planning: `AGENTS.md`, `docs/activeContext.md`, `docs/audits/cleanup_execution_plan_20260508.md`, `docs/audits/submission_status_and_moderation_plan_20260508.md`, `docs/audits/issue_ingest_plan_20260508.md`, `docs/audits/cleanup_migration_report_20260508.json`, `data/hydrants.json`, `data/hydrants_provenance.json`, `index.html`, `audit/apply_field_reports.py`, `scripts/migrate_to_verbose_schema.py`, and commit metadata for `d6cbcd5`, `10bb67a`, `142a494`.

Negative findings:

| Category | Finding |
|---|---|
| Target plan file | `docs/audits/backfill_and_submission_extension_plan_20260509.md` missing before this write. |
| Verified national without type | No match; the single verified national record already has `type:"надземен"`. |
| Verified missing type | Exactly 8 records, all `origin:"vik"`. |
| Operational runtime data | 0 records currently have `operational_status`. |
| Compact runtime keys | 0 records have compact keys `i`, `c`, `t`, or legacy `status`. |
| `field_reports.json` | Missing after Phase 2 cleanup, expected. |
| Worker source | No `worker/` directory; live Worker remains external. |
| Ingest parser | No repo script currently parses GitHub issue bodies into verbose `data/hydrants.json`. |
| Runtime/build structure | No `package.json`, `src/`, `dist`, or CI workflow. |
| Source archives | Present but not content-inspected; not used as evidence. |

Declared metadata / authority notes:

- `AGENTS.md`: live Cloudflare Worker is canonical until commit 17 extracts `worker/`.
- `AGENTS.md`: Bulgarian labels require Petar approval; no new dependencies without approval; 2 MB first-load hard cap.
- `cleanup_execution_plan_20260508.md`: verbose schema uses `type`, `existence_status`, `operational_status`, `review_status`; renderer already supports `works`, `not_working`, `not_tested`.
- `cleanup_migration_report_20260508.json`: current migrated output is 5,901 records.

Decision ledger:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Backfill only verified records with absent `type` | Petar preference + scan | 8 VIK missing type; 15 verified already typed | Remove added fields | Ratified |
| Preserve existing typed records | Repo data | Field-report and national verified types already populated | Reversible | Ratified |
| Use script for backfill | Auditability | Assertions and provenance needed | Script can stay as audit tool | Ratified |
| Use canonical YAML fields only | Petar amendment | Avoid dual source: no `hydrant_type` / `operational` duplicates | Reversible via parser migration | Ratified |
| Normalize picker value to `не съм проверявал` | Petar amendment | Damaged and confirmation flows align | Backward-compatible parser handles old suffix | Ratified |
| Hide completed pickers in `exists_confirmed` | Petar amendment | Reduces friction when fields already populated | UI-only revert | Ratified |
| Extract Worker before contract change | Repo constraint | Worker source external, parser unconfirmable | Reorder commits | Ratified |

Approval-gate check: Section A is a data edit requiring Petar approval and one commit. Section B changes UI wording, Worker contract, Worker repo layout, and ingest behavior; it requires a multi-session approved sprint. No runtime/build dependency is proposed.

## Section A: Backfill Investigation

Empirical scan of `data/hydrants.json`:

```text
total_records: 5901
verified_count: 23
verified_missing_type_count: 8

verified by origin/type:
field_report | надземен | 14
national     | надземен | 1
vik          | <absent> | 8
```

Petar's 23 verified count is confirmed. The "8 VIK + 1 national" missing-type expectation is not confirmed in current data; current missing-type set is exactly 8 VIK records. The verified national record `coord_27.84744_43.24699` already has `type:"надземен"`.

Records needing backfill:

| id | coords | address | region | legacy_ids |
|---|---:|---|---|---|
| `coord_27.90237_43.21801` | `[27.902373,43.218008]` | absent | absent | `VIK-VARNA_ZAPAD-0158` |
| `coord_27.90313_43.21833` | `[27.903127,43.218328]` | absent | absent | `VIK-VARNA_ZAPAD-0159` |
| `coord_27.90397_43.21860` | `[27.903968,43.218596]` | absent | `14-ТИ ПОДРАЙОН` | `877-ZP` |
| `coord_27.90493_43.21885` | `[27.90493,43.218849]` | absent | absent | `VIK-VARNA_IZTOK-0167` |
| `coord_27.90614_43.21898` | `[27.90614,43.218982]` | absent | absent | `VIK-VARNA_IZTOK-0173` |
| `coord_27.90733_43.21900` | `[27.907334,43.218998]` | absent | absent | `VIK-VARNA_IZTOK-0169` |
| `coord_27.93420_43.21373` | `[27.934205,43.213728]` | absent | `КВ. ЧАЙКА; 19 М.Р; ЧАСТ 1` | `271` |
| `coord_27.93447_43.21327` | `[27.934473,43.213267]` | `Ул. Никола Вапцаров` | `КВ. ЧАЙКА; 19 М.Р; ЧАСТ 1` | `913` |

Backfill scope decision: use A2-A, only records with absent `type`; preserve existing `field_report` and national values verbatim. Do not force-rewrite all 23 verified records.

Backfill execution:

- Add `scripts/backfill_verified_type_20260509.py`, standard library only, default dry-run.
- CLI supports `--input`, `--provenance`, `--report`, `--timestamp`, `--dry-run`, `--apply`.
- Assert: 5,901 records, 23 verified, exactly the 8 expected missing-type IDs, each `origin:"vik"`, `existence_status:"verified"`, and `type` absent before.
- Set `type:"надземен"` only on those 8 records.
- Append provenance `source_refs` entry per changed record with `manual_field:"type"`, `old_value:null`, `new_value:"надземен"`, timestamp, and Petar physical-verification attribution.
- Write `docs/audits/backfill_verified_type_report_20260509.json`.

Post-apply assertions:

```text
record count: 5901
verified count: 23
verified missing type: 0
global type counts: <absent>=3602, надземен=1152, подземен=1147
coords/ids/origins/statuses unchanged except added type fields
```

Commit:

```text
chore(data): backfill type for verified hydrants

Set type="надземен" on 8 verified VIK records whose type was absent.

Source: Petar physical verification; all currently verified records are physically надземни.
Scope: absent type only; existing field_report and national type values preserved.
Report: docs/audits/backfill_verified_type_report_20260509.json
```

Section A is tonight-feasible single-commit work.

## Section B: Submission Flow Extension Investigation

Current UI state:

- `exists_confirmed`: reporter + optional free text only; no type or operational capture.
- `new_hydrant`: manual location + type picker + optional description; no operational capture.
- `missing`: captures `hydrant_type_at_location`; keep as report-specific expected-type evidence, not canonical record `type`.
- `damaged`: captures damage description and operational picker, currently with text `не съм проверявал, само видимо`.
- `wrong_location`: corrected coords + description; no type or operational fields.

Canonical payload model:

Use only canonical verbose-schema keys in new YAML payloads:

```text
type: "надземен" | "подземен" | null
operational_status: "works" | "not_working" | "not_tested" | null
```

Do not emit duplicate `hydrant_type`, `operational`, or Bulgarian operational fields for the extended flows. Frontend displays Bulgarian labels at render time through lookup helpers. Worker parser maps these canonical YAML keys directly into canonical report JSON fields.

Operational picker normalization:

- All flows use exactly: `да`, `не`, `не съм проверявал`.
- Update the existing damaged modal to drop the suffix `само видимо`.
- Backward compatibility: Worker/ingest parser should still accept old issue bodies containing `не съм проверявал, само видимо` and map them to `not_tested`.

Mapping:

```text
type picker:
надземен -> type:"надземен"
подземен -> type:"подземен"
не знам -> type:null

operational picker:
да -> operational_status:"works"
не -> operational_status:"not_working"
не съм проверявал -> operational_status:"not_tested"
old missing field -> operational_status absent/null
```

`exists_confirmed` UI:

- On modal open, inspect target record.
- Hide type picker if `hydrant.type` is populated.
- Hide operational picker if `hydrant.operational_status` is populated.
- If both are populated, show only reporter + optional free text, matching current friction level.
- If either is absent, show only the missing picker(s).
- Required validation applies only to visible pickers.
- Opt-out values `не знам` and `не съм проверявал` satisfy required validation without writing canonical `type` for unknown type.

`new_hydrant` UI:

- Keep type picker, but require explicit selection.
- Add operational picker with the same values and required explicit selection.
- Emit canonical `type` and `operational_status` only.

Worker contract impact:

- Extract Worker source first into `worker/`, with deploy notes, before changing behavior.
- POST can continue accepting `{title, body, labels}` if Worker only creates GitHub issues.
- GET `/issues` parser must read canonical YAML keys `type` and `operational_status`, return them in report JSON, and preserve old issue compatibility.
- Issue Markdown body should display Bulgarian labels derived from canonical values, but YAML remains canonical.
- Existing CORS/cache/`since`/`limit` behavior must remain unchanged.

Ingest pipeline impact:

Do not extend `audit/apply_field_reports.py`; it is stale and compact-schema oriented. Add `scripts/apply_approved_reports.py` for verbose data.

Required ingest behavior:

- Parse canonical YAML fields `type` and `operational_status`.
- `exists_confirmed`: set `existence_status:"verified"`, add `type` only if non-null, add `operational_status` if non-null.
- `new_hydrant`: create approved `field_report` record with canonical `type` and `operational_status` when present.
- `damaged`: keep `review_status:"reported"` and apply `operational_status` if present.
- `missing`: keep `review_status:"reported"`; do not convert `hydrant_type_at_location` into canonical `type`.
- `wrong_location`: update coords in place, never create a new field record, set `existence_status:"verified"`.
- Old issues without canonical fields remain valid.

Display impact:

Current rendering already supports:

```text
operational_status:"works" -> green .h-pin.operational
operational_status:"not_working" -> black .h-pin.broken
verified + absent/not_tested -> red .h-pin.verified
review_status:"reported" -> yellow precedence
```

No additional pin CSS is required. Textual card/list display for operational status is optional and should use existing label lookup tables if added.

Test plan:

- Submit `exists_confirmed` with missing `type`, choose `надземен`, operational `да`; verify issue YAML, Worker GET report, green polling update, and static ingest.
- Submit `exists_confirmed` with missing `type`, choose `подземен`, operational `не`; verify black pin after approved report.
- Submit `exists_confirmed` with `не знам` + `не съм проверявал`; verify `type:null`, `operational_status:"not_tested"`, red verified pin.
- Open `exists_confirmed` for record with both fields populated; verify both pickers hidden.
- Open `exists_confirmed` for record with only one field missing; verify only that picker appears and validation only applies there.
- Submit `new_hydrant` with explicit type + operational status; verify canonical YAML and ingest.
- Submit damaged flow; verify picker text is normalized and parser still accepts old suffix in fixtures.
- Worker GET regression: old issues, new issues, CORS, cache headers, `since`, and `limit`.
- Encoding scan all changed `.html`, `.js`, `.py`, `.json`, `.md`.
- Phone verification after frontend change, Worker deploy, and first ingest dry-run/apply.

Sequencing:

Section B is a multi-session sprint, realistically 3-4 separate sessions because it spans Worker extraction, manual Cloudflare deploy, frontend validation/UI work, Worker contract deploy, ingest script/test fixtures, and phone verification gates.

Recommended commit/session order:

1. Worker extraction, no behavior change: add `worker/index.js` and deploy notes; confirm dashboard/source parity.
2. Worker parser/contract update: parse canonical `type` and `operational_status`; deploy and record Worker version.
3. Frontend UI + polling: conditional pickers, normalized damaged value, canonical YAML emission, polling merge.
4. Ingest script + fixtures: add `scripts/apply_approved_reports.py`; dry-run old and new issue fixtures.
5. First approved data ingest only after phone verification.

## Section C: Open Questions For Petar

Defaults locked by amendments:

| Question | Default |
|---|---|
| Force selection vs defaults | Force explicit selection only for visible pickers; opt-out choices allowed. |
| Operational opt-out text | `не съм проверявал` everywhere. |
| Canonical YAML fields | Emit `type` and `operational_status` only for canonical fields. |
| Skip completed pickers | Yes, hide `exists_confirmed` pickers when target fields are already populated. |
| Backfill attribution | ISO-8601 local timestamp plus Petar physical-verification attribution. |
| Worker extraction timing | First step of Section B sprint. |
| Damaged/missing type prompt | Do not add canonical type prompt to damaged/missing in this sprint. |
| Old pending issues | Do not migrate manually; parser remains backward-compatible. |
| `activeContext.md` stale state | Sync after next implementation commit. |
