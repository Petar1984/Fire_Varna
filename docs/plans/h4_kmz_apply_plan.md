# H4 KMZ Apply Plan

Status: final plan for execution review.
Authoring date: 2026-06-22.
Mode: PLAN ONLY. This document authorizes no implementation, no real apply, no
commit, and no push. The only file written by this task is this plan.

## Request Scope

User request: produce a Codex plan, read the repository directly, do not
implement, do not commit, do not push, and save the final plan at
`Fire_Varna/docs/plans/h4_kmz_apply_plan.md`.

H4 implementation scope after later approval:

1. Extend `scripts/import_etr_kmz.py` with an explicit `--apply` path.
2. Preserve current behavior without `--apply`: dry-run remains default.
3. Apply only confident KMZ outcomes:
   - `UPDATE` (`<=5 m`, expected 3,170): append ETR alias to `legacy_ids` and
     append provenance saying existence was confirmed by ETR.
   - `ADD` (`>20 m`, expected 1,306): append a new record with only
     `{id, coords, origin, legacy_ids}`.
   - `FLAG` (`5-20 m`, expected 317): do not apply; write queue file only.
4. Mutate only:
   - `data/hydrants.json`
   - `data/hydrants_provenance.json`
   - audit/report artifacts under `docs/audits/`
5. Write `docs/audits/h2_kmz_flag_queue.json` for the deferred FLAG rows.
6. Write a post-apply report with before/after counts and SHA256 hashes.
7. Add tests using synthetic temp data for apply behavior and idempotency.

Out of scope:

- Applying GitHub issue reports. Issue apply remains separate and label-gated by
  `approved`.
- Worker, frontend, UI wording, map behavior, dependency changes, stable-ID
  migration, commits, and pushes.
- Applying FLAG rows to `data/hydrants.json`.
- Changing existing hydrant coordinates, existence status, type, address,
  operational status, review status, origin, or ids during ETR UPDATE.

## Deterministic Inventory

Inventory scope: task-scoped H4 planning inventory under `C:\git\Fire_Varna`,
limited to the H1/H2 code, plans, reports, current data targets, KMZ source
archives, and test files needed to specify the apply contract.

Observed repo state:

```text
repo: C:/git/Fire_Varna
HEAD: c5f2b2dea059c5d243dfc102918f2cb99811739c
status: ?? docs/plans/h2_kmz_adapter_plan.md
target existed before write: docs/plans/h4_kmz_apply_plan.md = False
```

Relevant files and hashes:

```text
AGENTS.md	16305	741D24018EE1D03FACE53C91B129D46185BFA730CE3401084FC7A648B7865A7F
docs/activeContext.md	23855	D8044A393FF9BD60903205996AB4A2BF9160D8F71627B8A08D8D5FC99BE6B376
docs/plans/h1_shared_core_spatial_dedup.md	26543	DD94B1BF4F1B14088EC2E9FB6439A6ACC0773AD7C0078D78D06C367F20A11631
docs/plans/h2_kmz_adapter_plan.md	30450	C708A5FCCDA65C927E663C3B12BABCEBB32680F502C1BA86CEA9E39EABB3C58C
docs/audits/h2_kmz_consolidation_dry_run.json	1121708	DA613B3E9EA1035116C9147505284ABC07524BA7425CCFF067CE02028EBB9A27
docs/audits/h2_kmz_consolidation_dry_run.md	71585	3865A1AD791928447A06CFA373194427F8874C4EACF48666E6B7C59B9F88D2E6
scripts/import_etr_kmz.py	36026	E527BFE938B548946260BE6FA0C247D67F383CF93D86C0A0E49FA5C741CC9925
scripts/lib/hydrant_core.py	21713	763825326F6D6BA58232A9D86DEF9977D5D934C0F96FA523A1F6722F4F789CFF
scripts/apply_approved_reports.py	5997	AF100085D409EE5769C21779AD85ECD536E9EF9E1D638178571A26C0F20926A6
tests/test_etr_kmz_adapter.py	28015	375D3A860913686BDD7FB0B2F89CC0B21A540B3CD960DA64BF9F7C144DCA0347
tests/test_hydrant_core.py	22539	0B2880003C611942580F5678E0932093EEDD465267A6BF6FB7066958B3BB4CBD
data/hydrants.json	874593	65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B
data/hydrants_provenance.json	1364172	894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E
data/hydrants_17_06_26/Пожарни хидранти ЕТР Варна.kmz	189099	DAD33C8A59299F084E7B584625D03417C6D3C6F5AB1DE360A985824D971D2E8B
data/hydrants_17_06_26/Пожарни хидранти ЕТР Девня.kmz	8158	741AC5112D2B9DEB18BA97467841FC6049E9829D08A551FDECC46B724FF7690B
data/hydrants_17_06_26/Пожарни хидранти ЕТР Долни Чифлик.kmz	28707	B2F96E41D2993AEB7F5A330EA2869F47CE46AE4BEE452F37BE00BBFD9E55F90C
data/hydrants_17_06_26/Пожарни хидранти ЕТР Провадия.kmz	57196	0CFF65A686E9E3698AAE97F5DE6ACC81D9BCEE29466B6B66A4E5EB0F885E0BFC
```

Runtime data probe:

```text
data/hydrants.json record_count=5911
records_with_etr_alias=0
duplicate_ids=0
first_record={"id":"coord_27.66965_43.31090","coords":[27.669648,43.310904],"origin":"vik","legacy_ids":["10122-DV"]}
data/hydrants_provenance.json provenance_key_count=5911
missing_source_refs=0
empty_source_refs=0
first_key=coord_27.66965_43.31090
first_value={"source_refs":[{"old_id":"10122-DV","old_coord":[27.669648,43.310904],"s":"DEVNIa","i_original":"10122","merge_action":"winner","conflict_flags":[]}]}
```

H2 dry-run report probe:

```text
schema_version=h2_kmz_dry_run_v1
mode=dry_run
generated_at=2026-06-22T00:00:00+03:00
input_count=5911
input_sha=65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B
prov_count=5911
prov_sha=894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E
updated=3170
flagged=317
added=1306
projected=7217
flags_len=317
add_groups_len=1306
```

KMZ archive/content inspection used `.NET System.IO.Compression.ZipFile` and
streamed each inner `doc.kml` without extracting files to disk:

```text
FILE: Пожарни хидранти ЕТР Варна.kmz
  entries: 4DDCA331DEFC4D159ECBD8727AB163F4.xsl, doc.kml, Layer0_Symbol_135a2db0_0.png
  kml_entries: 1 (doc.kml)
  header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  document_name: Пожарен хидрант_2005
  placemark/point/coordinates: 2681 / 2681 / 2681
  extended/schema: 0 / 0
  first_name: УЛ. "МАРА ГИДИК"
  first_coord:  27.8919611480698,43.17796325765485,0
FILE: Пожарни хидранти ЕТР Девня.kmz
  entries: 6F05DDCD0BBD4D96ADED19AF6522A99C.xsl, doc.kml, Layer0_Symbol_ed8450_0.png
  kml_entries: 1 (doc.kml)
  header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  document_name: gisn_0306.mariya.Devnya_PH_D_2005
  placemark/point/coordinates: 118 / 118 / 118
  extended/schema: 0 / 0
  first_name: ALBENA@SRVGIS2.GISN_0306
  first_coord:  27.62785779096259,43.36714421053241,0
FILE: Пожарни хидранти ЕТР Долни Чифлик.kmz
  entries: 3718E6CB11694F2A94AD1E6C6805AE94.xsl, doc.kml, Layer0_Symbol_1465d048_0.png
  kml_entries: 1 (doc.kml)
  header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  document_name: gisn_0306.mariya.DC_PH_Dc_2005
  placemark/point/coordinates: 639 / 639 / 639
  extended/schema: 0 / 0
  first_name: ALBENA@SRVGIS2.GISN_0306
  first_coord:  27.72435957567142,42.99676794414151,0
FILE: Пожарни хидранти ЕТР Провадия.kmz
  entries: B9BDBC232A814A6B891BE44C56872F68.xsl, doc.kml, Layer0_Symbol_b096588_0.png
  kml_entries: 1 (doc.kml)
  header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  document_name: gisn_0306.mariya.Provadia_PH_P_2005
  placemark/point/coordinates: 1422 / 1422 / 1422
  extended/schema: 0 / 0
  first_name:
  first_coord:  27.44281254053192,43.18480684005301,0
```

## Files Read

- `AGENTS.md`
- `docs/activeContext.md`
- `docs/plans/h1_shared_core_spatial_dedup.md`
- `docs/plans/h2_kmz_adapter_plan.md`
- `docs/audits/h2_kmz_consolidation_dry_run.json`
- `docs/audits/h2_kmz_consolidation_dry_run.md`
- `scripts/import_etr_kmz.py`
- `scripts/lib/hydrant_core.py`
- `scripts/apply_approved_reports.py`
- `tests/test_etr_kmz_adapter.py`
- `tests/test_hydrant_core.py`
- `data/hydrants.json`
- `data/hydrants_provenance.json`
- `data/hydrants_17_06_26/Пожарни хидранти ЕТР Варна.kmz!/doc.kml`
- `data/hydrants_17_06_26/Пожарни хидранти ЕТР Девня.kmz!/doc.kml`
- `data/hydrants_17_06_26/Пожарни хидранти ЕТР Долни Чифлик.kmz!/doc.kml`
- `data/hydrants_17_06_26/Пожарни хидранти ЕТР Провадия.kmz!/doc.kml`

## Negative Findings Matrix

| Check | Finding |
|---|---|
| Existing H4 plan | `docs/plans/h4_kmz_apply_plan.md` did not exist before this task. |
| Existing `--apply` in KMZ adapter | `scripts/import_etr_kmz.py` explicitly says there is deliberately no `--apply`; current tests assert `--apply` is rejected. |
| Existing ETR aliases in current data | `records_with_etr_alias=0`; first H4 apply should perform the expected UPDATE/ADD work, and a second run should be no-op. |
| Existing duplicate ids | `duplicate_ids=0`; H4 must preserve uniqueness while appending 1,306 ADD records. |
| Existing FLAG queue | No H4 queue artifact is present in the inventory; H4 should create `docs/audits/h2_kmz_flag_queue.json`. |
| Existing post-apply report | No H4 post-apply report exists; H4 should create one under `docs/audits/`. |
| KMZ source metadata beyond coordinates/name | All inspected KMZ `doc.kml` files have `ExtendedData=0` and `SchemaData=0`; no type/status/address/source-id can be inferred. |
| Real-data apply authorization in this task | Not present. This is plan-only; no mutation of `data/hydrants.json` or provenance now. |
| Dependency manifest | No dependency change is needed; H4 should remain standard-library only. |
| Issue apply authorization | Explicitly separate; H4 KMZ apply must not fetch or apply GitHub issues. |
| Commit/push authorization | Explicitly forbidden. |

## Quoted Declared Metadata

From `AGENTS.md`, Codex Plan Preamble Checklist:

```text
Every Codex plan/proposal must include: request scope, deterministic inventory,
files read, negative-findings matrix, quoted declared metadata, decision ledger,
approval-gate check, and open questions.
```

From `AGENTS.md`, binary file rule:

```text
KMZ means unzip/list archive and inspect inner KML/doc.kml.
```

From `docs/activeContext.md`:

```text
data/hydrants.json: 5,911 records
```

From `scripts/import_etr_kmz.py`:

```text
there is no --apply flag (H4 owns signed apply)
```

From `scripts/lib/hydrant_core.py`:

```text
DEFAULT_RM_M = 5.0
DEFAULT_RF_M = 20.0
```

From `scripts/lib/hydrant_core.py`, spatial decision contract:

```text
Signed thresholds (Petar, 2026-06-21): UPDATE <= Rm, FLAG (Rm, Rf], ADD > Rf.
```

From `scripts/lib/hydrant_core.py`, stable-id scope:

```text
H1 stub only: real stable-id assignment and migration of existing coord_ ids is H3 scope.
```

From `docs/audits/h2_kmz_consolidation_dry_run.md`:

```text
UPDATE | 3170
FLAG | 317
ADD (after <5 m cluster) | 1306
projected output count if applied | 7217
```

From Petar decisions in the H4 request:

```text
Приложи само УВЕРЕНОТО: UPDATE (<=5m, ~3,170) + ADD (>20m, ~1,306).
FLAG (5-20m, ~317) НЕ се прилагат.
```

From Petar decisions in the H4 request:

```text
ЕТР UPDATE = само `etr` запис в legacy_ids + provenance "confirmed by ETR";
БЕЗ промяна на existence_status или други полета.
```

From Petar decisions in the H4 request:

```text
ADD = нов запис {id (H1 coord-id stub), coords, origin=etr_<община>,
legacy_ids}; без тип/статус.
```

## Decision Ledger

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Add `--apply` to `scripts/import_etr_kmz.py`; keep dry-run default without it | User H4 scope + current H2 script | H2 script says H4 owns signed apply; issue adapter already uses opt-in `--apply` | Reversible by removing flag | Approved for H4 plan, not executed |
| `--apply` writes only `data/hydrants.json`, `data/hydrants_provenance.json`, `docs/audits/h2_kmz_flag_queue.json`, and post-apply report(s) | User constraint | Request says `--apply` writes only data + provenance + queue/report | Reversible from git/pre-apply backups | Approved |
| Recompute the H2 classification from KMZ/input at apply time instead of trusting stale report rows | Determinism and safety | Current report records input hashes; live data may drift | Reversible before execution | Planned |
| Require input SHA/count precondition by default for real apply | H2 report metadata | H2 report input SHA/count are known; current data matches | Reversible with explicit override later, not in H4 | Planned |
| Apply only UPDATE and ADD; write FLAG queue only | Petar 2026-06-22 | Precision-first decision in request | FLAGs remain reviewable | Approved |
| UPDATE mutates only `legacy_ids` and provenance | Petar 2026-06-22 | ETR confirms existence only, no other attributes | Reversible through provenance + git | Approved |
| UPDATE provenance attribution says `confirmed by ETR` | Petar 2026-06-22 | Required wording | Reversible by editing provenance before commit | Approved |
| UPDATE idempotency skips existing ETR aliases | Idempotency requirement | Current data has 0 ETR aliases; second run must no-op | Reversible | Planned |
| ADD record shape is exactly `{id, coords, origin, legacy_ids}` | Petar 2026-06-22 | No type/status in KMZ | Reversible by deleting new records before commit | Approved |
| ADD keeps real KMZ representative coordinate, not centroid | Petar 2026-06-22 | Request states real KMZ coordinate | Reversible before apply | Approved |
| ADD id uses H1 `CoordIdRegistry` coord-id stub | Petar + H1 scope | Stable ID migration is H3 | Reversible after H3 migration | Approved |
| ADD idempotency skips when id or ETR alias already exists | Idempotency requirement | Prevents duplicate appends on rerun | Reversible | Planned |
| FLAG queue schema is versioned and contains full H2 FLAG rows | Auditability | 317 rows are deferred for manual review | Reversible | Planned |
| Post-apply report is versioned separately from H2 dry-run | Clarity | H4 mutates data; report needs before/after SHA/counts | Reversible | Planned |
| Mojibake scan runs before any apply write | H1 core safety | `hydrant_core.mojibake_scan` exists and H2 already uses it | Reversible | Planned |
| Use `core.atomic_write_json` for both mutated data files and JSON reports | H1 core safety | Atomic writer already exists | Reversible | Planned |
| Tests write only temp files; real data apply occurs only via manual `--apply` | User constraint | Existing test style follows temp dirs and SHA guards | Reversible | Approved |
| No commit or push | User constraint | Request says never push and no commit | N/A | Approved |

## Apply Contract

### CLI

Extend the existing parser with one explicit flag:

```powershell
python scripts/import_etr_kmz.py `
  --source-dir data/hydrants_17_06_26 `
  --input data/hydrants.json `
  --provenance data/hydrants_provenance.json `
  --json-report docs/audits/h2_kmz_consolidation_dry_run.json `
  --md-report docs/audits/h2_kmz_consolidation_dry_run.md `
  --flag-queue docs/audits/h2_kmz_flag_queue.json `
  --apply-report docs/audits/h4_kmz_apply_report.json `
  --timestamp 2026-06-22T00:00:00+03:00 `
  --apply
```

Recommended parser additions:

- `--apply`, `action="store_true"`.
- `--flag-queue`, default `docs/audits/h2_kmz_flag_queue.json`.
- `--apply-report`, default `docs/audits/h4_kmz_apply_report.json`.
- Keep `--json-report` and `--md-report` for dry-run outputs; in apply mode
  either rewrite the dry-run reports from the same run or leave them unchanged
  only if implementation documents that choice. Preferred: rewrite them so the
  classification report and apply report share the same timestamp/input hashes.

### Preflight

Before mutating anything:

1. Load `--input` and `--provenance`.
2. Compute SHA256 and record counts.
3. Verify current first-apply baseline unless already-applied idempotency is
   detected:
   - hydrants count: `5911`
   - provenance key count: `5911`
   - hydrants SHA:
     `65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B`
   - provenance SHA:
     `894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E`
4. Build alias index with `core.build_alias_index(records)`.
5. Assert no duplicate record ids.
6. Assert every record has `legacy_ids`; if missing, fail loud rather than
   normalizing silently.
7. Assert every provenance key has `source_refs`.
8. Parse the exact four KMZ files through the existing H2 parser.
9. Run the existing H2 consolidation pipeline to produce UPDATE/FLAG/ADD sets.
10. Assert planned H4 counts match the current signed batch:
    - `updated=3170`
    - `flagged=317`
    - `added=1306`
    - projected first-apply output `7217`
11. If the data already has ETR aliases/new ADD ids from a prior apply, allow a
    no-op result only when all expected aliases/ids are already present and no
    partial-apply inconsistency is found.

Partial-apply detection must fail loud. Examples:

- Some but not all UPDATE aliases exist.
- Some but not all ADD records exist.
- New ADD record exists without provenance.
- Provenance exists without corresponding record.
- Existing record has ETR alias but provenance lacks H4 source ref.

### UPDATE Semantics

For each classified `UPDATE` component:

1. Target the nearest existing record returned by H1 matching.
2. For every source UID in the component, compute alias format:
   `etr_<municipality>:<lon8>,<lat8>`.
3. If all aliases already exist on the target record and matching H4 provenance
   refs already exist, count as `noop_update`.
4. If an alias exists on a different record, abort as `alias_collision`.
5. Otherwise append missing aliases to `legacy_ids` in deterministic member
   order.
6. Do not modify any other target record field.
7. Append one provenance ref per target update. Recommended shape:

```json
{
  "old_id": "coord_27.88875_43.17953",
  "old_coord": [27.888754199975118, 43.17953159976118],
  "manual_field": "legacy_ids",
  "old_value": ["existing-alias"],
  "new_value": ["existing-alias", "etr_varna:27.88881074,43.17949215"],
  "attribution": "confirmed by ETR",
  "timestamp": "2026-06-22T00:00:00+03:00",
  "merge_action": "kmz_etr_update",
  "source_origin": "etr_varna",
  "source_file": "data/hydrants_17_06_26/Пожарни хидранти ЕТР Варна.kmz",
  "source_uids": ["etr_varna:27.88881074,43.17949215"],
  "distance_m": 4.123,
  "conflict_flags": []
}
```

If the source component has multiple member aliases, `source_uids` should list
only aliases newly appended in this run. For a no-op rerun, do not append a new
provenance ref.

### FLAG Semantics

For each classified `FLAG` component:

1. Do not mutate records.
2. Do not mutate provenance.
3. Write it to `docs/audits/h2_kmz_flag_queue.json`.
4. Preserve the H2 row fields and add queue metadata.

Recommended queue row fields:

```json
{
  "flag_id": "FLAG-0001",
  "queue_status": "pending_manual_review",
  "source_uid": "etr_varna:27.88881074,43.17949215",
  "source_file": "Пожарни хидранти ЕТР Варна.kmz",
  "municipality": "varna",
  "origin": "etr_varna",
  "placemark_index": 10,
  "name": "raw name or blank",
  "lon": 27.88881073732622,
  "lat": 43.1794921505898,
  "nearest_existing_id": "coord_27.88875_43.17953",
  "nearest_existing_origin": "national",
  "nearest_existing_lon": 27.888754199975118,
  "nearest_existing_lat": 43.17953159976118,
  "distance_m": 6.345,
  "member_count": 1,
  "member_uids": ["etr_varna:27.88881074,43.17949215"],
  "reason": "spatial_near_match"
}
```

The queue file must be rewritten deterministically on every run. A second apply
run should produce the same queue rows and report `queued_flags=317`.

### ADD Semantics

For each H2 `add_group`:

1. Take `group["record"]` from the H2 pipeline as the candidate record.
2. Candidate record must have exactly:
   - `id`
   - `coords`
   - `origin`
   - `legacy_ids`
3. Candidate `coords` must equal the real representative KMZ coordinate.
4. Candidate `origin` must equal `etr_<municipality>`.
5. If the id or any ETR alias already resolves to an existing record with the
   same coords/origin/aliases, count as `noop_add`.
6. If the id or alias resolves to a different record, abort as collision.
7. Otherwise append the new record to `records`.
8. Create provenance at `provenance[new_id]`. Recommended shape:

```json
{
  "source_refs": [
    {
      "old_id": null,
      "old_coord": null,
      "manual_field": "new_record",
      "old_value": null,
      "new_value": {
        "id": "coord_27.44281_43.18481",
        "coords": [27.44281254053192, 43.18480684005301],
        "origin": "etr_provadia",
        "legacy_ids": ["etr_provadia:27.44281254,43.18480684"]
      },
      "attribution": "confirmed by ETR",
      "timestamp": "2026-06-22T00:00:00+03:00",
      "merge_action": "kmz_etr_add",
      "source_origin": "etr_provadia",
      "source_file": "data/hydrants_17_06_26/Пожарни хидранти ЕТР Провадия.kmz",
      "source_uids": ["etr_provadia:27.44281254,43.18480684"],
      "conflict_flags": []
    }
  ]
}
```

Do not add type/status/address fields to ADD records or provenance changes.

### Write Order

Construct all mutated objects in memory first. Then:

1. `core.mojibake_scan("hydrants", new_records)`
2. `core.mojibake_scan("provenance", new_provenance)`
3. `core.mojibake_scan("flag_queue", flag_queue)`
4. `core.mojibake_scan("apply_report", apply_report)`
5. Write `data/hydrants.json` with `core.atomic_write_json`.
6. Write `data/hydrants_provenance.json` with `core.atomic_write_json`.
7. Write `docs/audits/h2_kmz_flag_queue.json` with `core.atomic_write_json`.
8. Write `docs/audits/h4_kmz_apply_report.json` with `core.atomic_write_json`.
9. Re-read and hash all four written files.
10. Print a concise summary with before/after hashes and no-op counts.

The two data files should be written before reports only after all validation
passes. If any write fails, atomic temp-file replacement should prevent partial
JSON files, but git diff must still be inspected manually before any commit.

## Post-Apply Report Format

Default path: `docs/audits/h4_kmz_apply_report.json`.

Schema:

```json
{
  "schema_version": "h4_kmz_apply_v1",
  "mode": "apply",
  "generated_at": "2026-06-22T00:00:00+03:00",
  "inputs": {
    "hydrants_json": {
      "path": "data/hydrants.json",
      "sha256_before": "65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B",
      "sha256_after": "<computed>",
      "record_count_before": 5911,
      "record_count_after": 7217
    },
    "provenance_json": {
      "path": "data/hydrants_provenance.json",
      "sha256_before": "894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E",
      "sha256_after": "<computed>",
      "record_count_before": 5911,
      "record_count_after": 7217
    },
    "h2_dry_run_report": {
      "path": "docs/audits/h2_kmz_consolidation_dry_run.json",
      "sha256": "DA613B3E9EA1035116C9147505284ABC07524BA7425CCFF067CE02028EBB9A27"
    },
    "kmz_files": ["same metadata as H2 report"]
  },
  "thresholds_m": {
    "rm_update_lte": 5.0,
    "rf_flag_lte": 20.0,
    "intra_batch_dedup_strict_lt": 2.0,
    "add_candidate_cluster_strict_lt": 5.0
  },
  "summary": {
    "planned_updates": 3170,
    "planned_adds": 1306,
    "planned_flags": 317,
    "applied_updates": 3170,
    "applied_adds": 1306,
    "queued_flags": 317,
    "noop_updates": 0,
    "noop_adds": 0,
    "record_count_before": 5911,
    "record_count_after": 7217,
    "expected_record_count_after": 7217,
    "provenance_count_before": 5911,
    "provenance_count_after": 7217,
    "collisions": 0,
    "partial_apply_detected": false
  },
  "output_files": {
    "hydrants_json": "data/hydrants.json",
    "provenance_json": "data/hydrants_provenance.json",
    "flag_queue": "docs/audits/h2_kmz_flag_queue.json",
    "apply_report": "docs/audits/h4_kmz_apply_report.json"
  },
  "per_file": [
    {
      "source_file": "Пожарни хидранти ЕТР Варна.kmz",
      "municipality": "varna",
      "applied_updates": 1634,
      "applied_adds": 764,
      "queued_flags": 216,
      "noop_updates": 0,
      "noop_adds": 0
    }
  ],
  "validation": {
    "dry_run_default_preserved": true,
    "only_allowed_paths_written": true,
    "mojibake_scan_passed": true,
    "duplicate_ids_after": 0,
    "missing_provenance_after": 0,
    "unexpected_field_mutations": 0
  }
}
```

For a second idempotent run, expected summary:

```json
{
  "applied_updates": 0,
  "applied_adds": 0,
  "queued_flags": 317,
  "noop_updates": 3170,
  "noop_adds": 1306,
  "record_count_before": 7217,
  "record_count_after": 7217
}
```

Optional Markdown companion: `docs/audits/h4_kmz_apply_report.md` with the same
summary, before/after hashes, per-file table, and a warning that FLAG rows were
queued only.

## Implementation Plan

1. Update H2 tests that currently assert no `--apply`; replace with tests that
   assert dry-run is default and `--apply` is explicit.
2. Add pure apply helpers to `scripts/import_etr_kmz.py`:
   - `build_apply_plan(report, previews, records, provenance)`
   - `apply_update(...)`
   - `apply_add(...)`
   - `build_flag_queue(...)`
   - `build_apply_report(...)`
   - `validate_apply_state(...)`
3. Keep `run_consolidation(...)` pure and reusable. It should not write data.
4. Make `main()` branch only at the final write phase:
   - no `--apply`: current dry-run behavior and protected-file SHA assertion.
   - `--apply`: apply UPDATE/ADD in memory, queue FLAG, validate, atomic write.
5. Add idempotency checks against alias index and provenance refs.
6. Add post-apply report generation.
7. Add tests with synthetic KMZ and temp input/provenance files.
8. Run unit tests and encoding scans.
9. Stop with local diffs only. No commit and no push.

## Test Plan

All tests must use `tempfile.TemporaryDirectory()` for writable files. Real data
is written only by a manually invoked `--apply`, never by tests.

Add or modify tests in `tests/test_etr_kmz_adapter.py`:

1. `test_dry_run_default_still_writes_only_reports`
   - Run without `--apply` over temp input/provenance.
   - Assert input/provenance JSON are byte-identical after run.
2. `test_apply_updates_append_only_etr_alias_and_provenance`
   - Synthetic existing record with type/status/address/status fields.
   - Synthetic ETR point within 5 m.
   - Assert only `legacy_ids` changes on record.
   - Assert provenance ref appended with `merge_action="kmz_etr_update"`.
3. `test_update_does_not_change_record_count`
   - One UPDATE, no ADD.
   - Count before equals count after.
4. `test_add_shape_and_real_coordinate`
   - One ADD beyond 20 m.
   - Assert new record keys exactly `{id, coords, origin, legacy_ids}`.
   - Assert coords equal KMZ coordinate, not centroid or nearest existing.
5. `test_add_creates_provenance`
   - Assert new provenance key exists and has one `source_refs` entry.
6. `test_flag_not_applied_and_queue_written`
   - One source point at 6 m.
   - Assert record/provenance unchanged.
   - Assert queue has one pending row.
7. `test_apply_first_run_counts`
   - Synthetic batch with known UPDATE/FLAG/ADD counts.
   - Assert report `applied_updates`, `applied_adds`, and `queued_flags`.
8. `test_apply_idempotent_second_run_noop`
   - Run apply twice over the same temp files.
   - Assert second run has `applied_updates=0`, `applied_adds=0`,
     `noop_updates=<first planned updates>`, `noop_adds=<first planned adds>`,
     and unchanged record count.
9. `test_alias_collision_aborts`
   - Preload an ETR alias on a different record.
   - Assert apply exits nonzero or raises a controlled error before writing.
10. `test_add_id_collision_aborts`
    - Preload candidate ADD id with different coords.
    - Assert no files are modified.
11. `test_partial_apply_detected`
    - Preload some but not all ETR aliases/provenance.
    - Assert fail loud rather than appending the rest silently.
12. `test_only_allowed_paths_written`
    - Run apply with temp paths.
    - Assert only temp input/provenance/queue/report paths changed.
13. `test_apply_report_shape`
    - Assert `schema_version`, before/after SHA/counts, per-file rows,
      validation block, and output file paths.
14. `test_mojibake_scan_runs_on_apply_outputs`
    - Include Cyrillic filenames/names in synthetic KMZ.
    - Assert scan passes clean Cyrillic and catches constructed bad sequence.

Recommended verification commands after H4 implementation:

```powershell
python -m unittest tests.test_etr_kmz_adapter
python -m unittest discover -s tests
Select-String -Path scripts\import_etr_kmz.py,tests\test_etr_kmz_adapter.py,docs\plans\h4_kmz_apply_plan.md -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8
```

Manual real apply command after approval:

```powershell
python scripts/import_etr_kmz.py --source-dir data/hydrants_17_06_26 --input data/hydrants.json --provenance data/hydrants_provenance.json --json-report docs/audits/h2_kmz_consolidation_dry_run.json --md-report docs/audits/h2_kmz_consolidation_dry_run.md --flag-queue docs/audits/h2_kmz_flag_queue.json --apply-report docs/audits/h4_kmz_apply_report.json --apply
```

Post-apply manual checks:

```powershell
git diff -- data/hydrants.json data/hydrants_provenance.json docs/audits/h2_kmz_flag_queue.json docs/audits/h4_kmz_apply_report.json
python scripts/import_etr_kmz.py --source-dir data/hydrants_17_06_26 --input data/hydrants.json --provenance data/hydrants_provenance.json --flag-queue docs/audits/h2_kmz_flag_queue.json --apply-report docs/audits/h4_kmz_apply_report_second_run.json --apply
```

Expected first real apply:

```text
record_count_before=5911
applied_updates=3170
applied_adds=1306
queued_flags=317
record_count_after=7217
```

Expected second real apply:

```text
applied_updates=0
applied_adds=0
noop_updates=3170
noop_adds=1306
queued_flags=317
record_count_before=7217
record_count_after=7217
```

## Acceptance Criteria

H4 implementation is acceptable only if all are true:

1. Without `--apply`, current dry-run behavior remains the default.
2. With `--apply`, UPDATE mutates only `legacy_ids` and provenance.
3. UPDATE does not change count, coords, id, origin, type, address,
   `existence_status`, `operational_status`, or `review_status`.
4. ADD appends exactly 1,306 records on first real apply.
5. ADD records have only `{id, coords, origin, legacy_ids}`.
6. ADD coords are real KMZ coordinates.
7. FLAG rows are not applied and are written to `h2_kmz_flag_queue.json`.
8. First real apply goes from 5,911 to 7,217 records.
9. Provenance count also goes from 5,911 to 7,217 keys.
10. No duplicate ids or alias collisions exist after apply.
11. Second apply is no-op for UPDATE/ADD and keeps count 7,217.
12. Post-apply report records SHA/count before and after.
13. All writes use `core.atomic_write_json`.
14. Mojibake scan passes.
15. Tests pass.
16. No commit and no push are performed.

## Approval-Gate Check

| Gate | Status |
|---|---|
| Architecture/file layout | Minor CLI/report/test extension planned; no code change in this task. |
| Data mutation | H4 will mutate real data only when `--apply` is explicitly run after approval; this planning task does not. |
| Runtime/build dependency | No new dependency planned. |
| UI labels/frontend | Not touched. |
| Worker/GitHub issue ingest | Not touched; issue apply is separate and label-gated. |
| Stable-ID migration | Not touched; ADD uses H1 coord-id stub. |
| FLAG review | Deferred to queue file; no data mutation. |
| Commit | Not authorized. |
| Push | Forbidden. |

## Open Questions

No blocker remains for H4 implementation planning. Execution still needs an
explicit follow-up instruction to implement and a separate explicit instruction
to run real `--apply`.

One implementation choice to confirm during execution review: whether to write
an optional Markdown companion for `h4_kmz_apply_report.json`. The JSON report
is the required contract; Markdown is convenience only.
