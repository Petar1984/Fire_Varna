# H2 KMZ Adapter + Dry-Run Consolidation Report Plan

Status: final plan for execution review.  
Authoring date: 2026-06-22.  
Mode: PLAN ONLY. This document authorizes no implementation, no `--apply`, no
real data mutation, no commit, and no push.

## Request Scope

User request: produce a Codex plan, read the repository directly, and save the
final plan at `Fire_Varna/docs/plans/h2_kmz_adapter_plan.md`.

H2 implementation scope, after approval:

1. Add a standard-library KMZ/KML adapter for the four files in
   `data/hydrants_17_06_26/`.
2. Parse each KMZ `doc.kml` into source points `(lon, lat)` with
   `origin=etr_<municipality>`.
3. Perform batch deduplication first: collapse KMZ source points strictly
   closer than `2 m` into deterministic source clusters.
4. Match deduped source clusters against `data/hydrants.json` through the H1
   core matcher at `Rm=5 m`, `Rf=20 m`.
5. Produce in-memory previews only:
   - `UPDATE` for distance `<=5 m`: add ETR source aliases to `legacy_ids` and
     provenance saying existence was confirmed by ETR; do not alter coords,
     type, address, existence/operational/review status, or any other field.
   - `FLAG` for distance `(5 m, 20 m]`: emit a manual review item; no record or
     provenance mutation.
   - `ADD` for distance `>20 m`: preview a new record with H1 coord-id stub,
     `origin=etr_<municipality>`, `legacy_ids`, and no type/status/address.
   - Collapse ADD candidates strictly closer than `Rm` (`5 m`) into one ADD
     preview before counting/writing the report.
6. Emit a dry-run consolidation report for Petar review before any H4 apply:
   totals, per-file breakdown, full FLAG list, and reconciliation against the E0
   raw independent baseline.
7. Add tests for parser, dedup, match action classification, report shape, and
   dry-run safety. Tests may write only to temporary directories.

Out of scope:

- H4 apply logic or any `--apply` flag.
- Mutation of `data/hydrants.json` or `data/hydrants_provenance.json`.
- Stable-ID registry and migration of existing `coord_` ids; that remains H3.
- GitHub issue ingest changes, Worker/frontend changes, reverse geocoding,
  satellite imagery, photo handling, commits, and pushes.

## Deterministic Inventory

Inventory scope: task-scoped H2 planning inventory under `C:\git\Fire_Varna`,
plus the single cross-repo E0 design file explicitly cited by the request:
`C:\git\Varna_buildings\scratch\hydrant_consolidation_e0_and_pipeline_plan.md`.
The new plan file was absent when the inventory was taken and is the only file
this PLAN-ONLY task writes.

Observed `Fire_Varna` repo state:

```text
repo: C:/git/Fire_Varna
HEAD: f14d5be0789bdf55ef85ac8a5f0efdd181ea00af
status: ## main...origin/main
```

Observed `Varna_buildings` context state:

```text
repo: C:/git/Varna_buildings
HEAD: 9d1bd4cc5f62bfeee85a07d836075989dc8637b0
status: dirty, with unrelated scratch/output/research files
```

Relevant files and hashes:

```text
Fire_Varna\AGENTS.md	16305	741D24018EE1D03FACE53C91B129D46185BFA730CE3401084FC7A648B7865A7F
Fire_Varna\docs\activeContext.md	23855	D8044A393FF9BD60903205996AB4A2BF9160D8F71627B8A08D8D5FC99BE6B376
Fire_Varna\docs\plans\commit_15_worker_get.md	27472	BB5DF4AF634B813139D317AD1684C59770717F36C1151173802A6ED1E4607567
Fire_Varna\docs\plans\h1_shared_core_spatial_dedup.md	26543	DD94B1BF4F1B14088EC2E9FB6439A6ACC0773AD7C0078D78D06C367F20A11631
Fire_Varna\docs\plans\sprint_1_5_polish.md	10098	EDEA2428C35617860FC3FCBD1B4A500A454B5FBED54D51ED9D1834A8A45A6064
Fire_Varna\scripts\apply_approved_reports.py	5997	AF100085D409EE5769C21779AD85ECD536E9EF9E1D638178571A26C0F20926A6
Fire_Varna\scripts\lib\__init__.py	271	64D070AD40AAF26EF70A1B8FDDA4858D6E49DCECA297AAD4E161D01602F666B9
Fire_Varna\scripts\lib\hydrant_core.py	21713	763825326F6D6BA58232A9D86DEF9977D5D934C0F96FA523A1F6722F4F789CFF
Fire_Varna\tests\test_hydrant_core.py	22539	0B2880003C611942580F5678E0932093EEDD465267A6BF6FB7066958B3BB4CBD
Fire_Varna\tests\test_apply_approved_reports_parity.py	6542	DE8E49EEDE22A303E3703CF7A9229C2A9E889A82781294D56B4D9FC14D2B837D
Fire_Varna\tests\golden_apply_v0.py	13181	60F11D61F40A5893A9030CC3BEB96F4C1B7D04D40F500BC37BACEE3FEA4E12F9
Fire_Varna\data\hydrants.json	874593	65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B
Fire_Varna\data\hydrants_provenance.json	1364172	894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E
Fire_Varna\data\hydrants_17_06_26\Пожарни хидранти ЕТР Варна.kmz	189099	DAD33C8A59299F084E7B584625D03417C6D3C6F5AB1DE360A985824D971D2E8B
Fire_Varna\data\hydrants_17_06_26\Пожарни хидранти ЕТР Девня.kmz	8158	741AC5112D2B9DEB18BA97467841FC6049E9829D08A551FDECC46B724FF7690B
Fire_Varna\data\hydrants_17_06_26\Пожарни хидранти ЕТР Долни Чифлик.kmz	28707	B2F96E41D2993AEB7F5A330EA2869F47CE46AE4BEE452F37BE00BBFD9E55F90C
Fire_Varna\data\hydrants_17_06_26\Пожарни хидранти ЕТР Провадия.kmz	57196	0CFF65A686E9E3698AAE97F5DE6ACC81D9BCEE29466B6B66A4E5EB0F885E0BFC
Varna_buildings\scratch\hydrant_consolidation_e0_and_pipeline_plan.md	10861	603DC5B23F164524C62CC09D90597CDB1535BBF8E22A8964E6682D911B205230
```

Runtime data probe:

```text
data/hydrants.json count: 5911
origins: field_report:24, national:2345, vik:3542
records missing legacy_ids: 0
field counts: existence_status:45, review_status:4, operational_status:16, type:2313, address:555
data/hydrants_provenance.json records: 5911
provenance records with source_refs: 5911
```

KMZ archive/content inspection used `.NET System.IO.Compression.ZipFile` and
streamed each inner `doc.kml` without extracting files to disk:

```text
Пожарни хидранти ЕТР Варна.kmz
  entries: 4DDCA331DEFC4D159ECBD8727AB163F4.xsl, doc.kml, Layer0_Symbol_135a2db0_0.png
  doc.kml header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  Document name: Пожарен хидрант_2005
  Placemark/Point/coordinates: 2681 / 2681 / 2681
  ExtendedData/SchemaData: 0 / 0
  first name/coord: УЛ. "МАРА ГИДИК" / 27.8919611480698,43.17796325765485,0

Пожарни хидранти ЕТР Девня.kmz
  entries: 6F05DDCD0BBD4D96ADED19AF6522A99C.xsl, doc.kml, Layer0_Symbol_ed8450_0.png
  doc.kml header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  Document name: gisn_0306.mariya.Devnya_PH_D_2005
  Placemark/Point/coordinates: 118 / 118 / 118
  ExtendedData/SchemaData: 0 / 0
  first name/coord: ALBENA@SRVGIS2.GISN_0306 / 27.62785779096259,43.36714421053241,0

Пожарни хидранти ЕТР Долни Чифлик.kmz
  entries: 3718E6CB11694F2A94AD1E6C6805AE94.xsl, doc.kml, Layer0_Symbol_1465d048_0.png
  doc.kml header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  Document name: gisn_0306.mariya.DC_PH_Dc_2005
  Placemark/Point/coordinates: 639 / 639 / 639
  ExtendedData/SchemaData: 0 / 0
  first name/coord: ALBENA@SRVGIS2.GISN_0306 / 27.72435957567142,42.99676794414151,0

Пожарни хидранти ЕТР Провадия.kmz
  entries: B9BDBC232A814A6B891BE44C56872F68.xsl, doc.kml, Layer0_Symbol_b096588_0.png
  doc.kml header: <?xml version="1.0" encoding="UTF-8"?>
  root/xmlns: kml / http://www.opengis.net/kml/2.2
  Document name: gisn_0306.mariya.Provadia_PH_P_2005
  Placemark/Point/coordinates: 1422 / 1422 / 1422
  ExtendedData/SchemaData: 0 / 0
  first name/coord: blank / 27.44281254053192,43.18480684005301,0
```

## Files Read

- `Fire_Varna/AGENTS.md`
- `Fire_Varna/docs/activeContext.md`
- `Fire_Varna/docs/plans/h1_shared_core_spatial_dedup.md`
- `Fire_Varna/scripts/apply_approved_reports.py`
- `Fire_Varna/scripts/lib/hydrant_core.py`
- `Fire_Varna/tests/test_hydrant_core.py`
- `Fire_Varna/tests/test_apply_approved_reports_parity.py`
- `Fire_Varna/data/hydrants.json`
- `Fire_Varna/data/hydrants_provenance.json`
- `Fire_Varna/data/hydrants_17_06_26/Пожарни хидранти ЕТР Варна.kmz!/doc.kml`
- `Fire_Varna/data/hydrants_17_06_26/Пожарни хидранти ЕТР Девня.kmz!/doc.kml`
- `Fire_Varna/data/hydrants_17_06_26/Пожарни хидранти ЕТР Долни Чифлик.kmz!/doc.kml`
- `Fire_Varna/data/hydrants_17_06_26/Пожарни хидранти ЕТР Провадия.kmz!/doc.kml`
- `Varna_buildings/scratch/hydrant_consolidation_e0_and_pipeline_plan.md`

## Negative Findings Matrix

| Check | Finding |
|---|---|
| Existing H2 plan | No `docs/plans/h2_kmz_adapter_plan.md` existed at inventory time. |
| Existing KMZ adapter | No script/test implementing KMZ ingest exists. `rg` found only H1/E0 references and a core comment saying KMZ H2 can reuse the pipeline. |
| Existing KMZ parser dependency | No `fastkml`, `simplekml`, `pykml`, `lxml`, `shapely`, `geopandas`, `zipfile`, or XML parser usage exists in `scripts/` or `tests/` for this adapter. |
| Python dependency manifest | No `pyproject.toml`, `requirements.txt`, `setup.cfg`, or `setup.py` exists in `Fire_Varna`; H2 should remain standard-library only. |
| KMZ ExtendedData / SchemaData | All four inspected `doc.kml` files have `ExtendedDataCount=0` and `SchemaDataCount=0`; no type/status/source-id can be inferred. |
| KMZ source identity | The only available per-placemark fields observed are `Point/coordinates` and noisy/blank `name`; names are not safe identifiers. |
| Real-data mutation authorization | Not present. H2 must not mutate `data/hydrants.json` or `data/hydrants_provenance.json`. |
| Stable-ID migration | H1 has only `CoordIdRegistry`; H3 owns persistent stable IDs. H2 must not migrate existing ids. |
| Commit/push authorization | Not present. This task explicitly forbids commit and push. |

## Quoted Declared Metadata

From `AGENTS.md`, Codex Plan Preamble Checklist:

```text
Every Codex plan/proposal must include: request scope, deterministic inventory,
files read, negative-findings matrix, quoted declared metadata, decision ledger,
approval-gate check, and open questions.
```

From `AGENTS.md`, binary file reading rule:

```text
KMZ means unzip/list archive and inspect inner KML/doc.kml.
```

From `docs/activeContext.md`, H1 status:

```text
H1 shared hydrant core + spatial dedup (`38ebbad`, 2026-06-22)
```

From `docs/activeContext.md`, runtime data state:

```text
data/hydrants.json: 5,911 records
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

From `scripts/lib/hydrant_core.py`, H1 stable-id scope:

```text
H1 stub only: real stable-id assignment and migration of existing coord_ ids is H3 scope.
```

From `scripts/apply_approved_reports.py`:

```text
Default is dry-run; --apply writes.
```

From E0, source counts:

```text
KMZ batch (`data/hydrants_17_06_26/`) | **4,860** |
Варна 2,681 · Провадия 1,422 · Долни Чифлик 639 · Девня 118
```

From E0, KMZ content:

```text
All four KMZ are ArcGIS exports: each placemark has a `Point` + a `name`,
zero ExtendedData.
```

From E0, signed threshold outcome:

```text
SIGNED (Petar, 2026-06-21) — precision-first: Rm = 5 m, Rf = 20 m.
```

From E0, raw independent baseline:

```text
UPDATE 3,237 ... FLAG 318 ... ADD 1,305
```

From E0, H2/H4 split:

```text
| H2 | KMZ adapter + **dry-run consolidation report** for review | no |
| H4 | Apply approved KMZ batch + approved issues (signed) | **yes — gated** |
```

From E0, push rule:

```text
Never git push.
```

## Current H1 API Reading

H2 should reuse H1 primitives, not the issue-specific `process()` handler:

- Use `load_json`, `mojibake_scan`, `coords_in_bbox`, `distance_m`,
  `find_nearest_hydrant`, `match_point`, `SpatialDecision`,
  `CoordIdRegistry`, and `canonical_coord_id`.
- Do not call `apply_new_hydrant()` for KMZ ADD/UPDATE because that handler is
  field-report-specific: it sets `origin="field_report"`, may set
  `existence_status="verified"`, carries `report_id`, and accepts reporter
  type/operational fields. KMZ has none of those.
- A grid index is optional. With roughly 4,860 KMZ points and 5,911 existing
  records, the H1 linear matcher is acceptable for H2 unless implementation
  profiling proves otherwise. Adding an index should preserve H1 tie-break
  semantics by `(distance_m, record id)`.

## Decision Ledger

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Add a new H2 adapter script, proposed path `scripts/import_etr_kmz.py` | User H2 scope | H1 issue adapter remains issue-specific; KMZ needs source parsing/reporting | Easy rename/move | Planned for H2 |
| H2 adapter has no `--apply` flag | User constraint + E0 H2/H4 split | H2 is dry-run/report only; H4 is signed apply | Reversible only with H4 approval | Approved constraint |
| Use Python standard library only: `zipfile`, `xml.etree.ElementTree`, `argparse`, `json`, dataclasses | AGENTS dependency gate | No dependency manifest; KML is simple Point-only | Reversible with dependency approval | Planned |
| Require the exact four known KMZ basenames unless an explicit `--allow-extra` style option is later approved | Determinism | Prevents silently ingesting stray archives | Reversible | Planned |
| Municipality mapping: `etr_varna`, `etr_devnya`, `etr_dolni_chiflik`, `etr_provadia` | User origin requirement | File names are municipality-specific | Reversible before H4 | Planned |
| Parse only `Point/coordinates`; store `name` only as raw source context | KMZ inspection | Zero ExtendedData/SchemaData; names are noisy/blank | Reversible | Planned |
| Reject or report invalid coordinates through `coords_in_bbox()` | H1 core | Same Varna oblast guard as issue ingest | Reversible | Planned |
| Batch-wide dedup first at strict `<2.0 m` | User H2 scope | E0 says Varna has about 111 internal duplicates | Threshold can change before H4 | Approved constraint |
| Dedup forms connected components, not just nearest pairs | Determinism | A-B and B-C under 2 m should produce one source cluster | Reversible | Planned |
| Dedup representative is the earliest point by explicit file order then placemark index, not a centroid | Traceability | Keeps output coords equal to an observed KMZ point | Reversible before H4 | Planned |
| Source UID format for report/legacy preview: `etr_<municipality>:<lon8>,<lat8>` for each raw placemark | No source ids in KMZ | Coordinate-derived source alias is deterministic and auditable | Reversible before H4 | Recommended; confirm before apply |
| UPDATE preview adds ETR aliases to `legacy_ids` and provenance only | User H2 scope | KMZ confirms existence but carries no type/status | Reversible before H4 | Planned |
| UPDATE preview does not change `coords`, `origin`, `type`, `address`, `existence_status`, `operational_status`, or `review_status` | User H2 scope | "KMZ has no type/status" and update says no other fields | Reversible before H4 | Approved constraint |
| FLAG preview mutates nothing | User H2 scope | Manual review queue | Reversible | Approved constraint |
| ADD preview record shape is `{id, coords, origin, legacy_ids}` plus no type/status/address | User H2 scope | ADD says coord-id through H1 stub, origin ETR, no type/status | Reversible before H4 | Planned |
| ADD id preview uses H1 `CoordIdRegistry` / `coord_<lon>_<lat>` until H3 | H1 scope | Stable ID migration is H3 | Reversible after H3 | Approved constraint |
| ADD candidates strictly closer than `Rm` are collapsed batch-wide into one ADD preview | User H2 scope | Prevents new duplicates inside the incoming batch | Threshold can change before H4 | Approved constraint |
| Dry-run report artifacts should be JSON canonical plus Markdown review view | Petar review need | JSON is replayable; Markdown makes FLAG review easy | Easy to adjust | Planned |
| Generated dry-run reports go under `docs/audits/` by default, not `data/` | Existing repo pattern | Audit/report artifacts already live in `docs/audits/` | Reversible | Planned |
| Tests use synthetic KMZs and temp JSON files; real data files are read only or SHA-guarded | User constraint + H1 test pattern | H1 tests already assert real data untouched | Reversible | Approved constraint |

## Implementation Plan

### 1. Adapter Surface

Add `scripts/import_etr_kmz.py` with a dry-run-only CLI:

```powershell
python scripts/import_etr_kmz.py `
  --source-dir data/hydrants_17_06_26 `
  --input data/hydrants.json `
  --provenance data/hydrants_provenance.json `
  --json-report docs/audits/h2_kmz_consolidation_dry_run.json `
  --md-report docs/audits/h2_kmz_consolidation_dry_run.md `
  --timestamp 2026-06-22T00:00:00+03:00
```

No `--apply` option should exist in H2. The script may write only the requested
report artifacts. It must never write to `--input` or `--provenance`.

### 2. Parse KMZ to Source Points

Define a small `KmzSourcePoint` dataclass:

```text
source_uid
source_file
source_sha256
municipality
origin
placemark_index
name
lon
lat
alt
```

Parsing rules:

- Open each KMZ with `zipfile.ZipFile`.
- Require exactly one inner KML entry, currently `doc.kml`; fail loud if missing
  or ambiguous.
- Parse XML with `xml.etree.ElementTree` namespace wildcards.
- For each `Placemark`, require a `Point/coordinates` value.
- Parse KML coordinate order as `lon,lat,alt`; ignore altitude for matching but
  include it in report source context.
- Treat `Placemark/name` as raw context only; never infer ids, type, status, or
  address from it.
- Count and report invalid/missing coordinates. Current inspected files suggest
  `PlacemarkCount == PointCount == CoordinateElements`.

### 3. Batch Dedup at `<2 m`

Before matching to existing hydrants:

- Sort source points by explicit file order and `placemark_index`.
- Build connected components where any two source points are strictly closer
  than `2.0 m` using `hydrant_core.distance_m()`.
- For each component, choose the earliest source point as representative.
- Preserve all member `source_uid`s and raw names in the component for report
  attribution.
- Attribute per-file dedup drops to the file of the nonrepresentative member.
- Report cross-file components separately if they occur.

This first dedup is the main expected difference from E0's raw independent
`4,860`-point baseline.

### 4. Match Against Existing Data

For each deduped source component representative:

- Call `hydrant_core.match_point((lon, lat), records, rm_m=5.0, rf_m=20.0)`.
- Preserve H1 boundary semantics:
  - `distance <= 5.0`: `UPDATE`
  - `5.0 < distance <= 20.0`: `FLAG`
  - `distance > 20.0` or no existing record: `ADD`
- Sort output deterministically by `(decision_order, source_file_order,
  placemark_index, source_uid)` for reports, while preserving input order for
  any in-memory preview state.

### 5. Preview Updates

For `UPDATE`:

- Target is the nearest existing record returned by H1.
- Preview `legacy_ids` additions:
  - add all component member `source_uid`s not already present;
  - keep existing aliases in original order;
  - append new ETR aliases sorted by component member order.
- Preview provenance only. Suggested source ref:

```json
{
  "old_id": "coord_...",
  "old_coord": [27.0, 43.0],
  "manual_field": "legacy_ids",
  "old_value": ["..."],
  "new_value": ["...", "etr_varna:27.89196115,43.17796326"],
  "attribution": "Dry-run H2 KMZ import: existence confirmed by ETR",
  "timestamp": "2026-06-22T00:00:00+03:00",
  "merge_action": "kmz_etr_update_preview",
  "source_origin": "etr_varna",
  "source_file": "data/hydrants_17_06_26/Пожарни хидранти ЕТР Варна.kmz",
  "source_uids": ["etr_varna:27.89196115,43.17796326"],
  "distance_m": 1.234,
  "conflict_flags": []
}
```

The final H4 apply provenance can reuse this shape after sign-off. H2 should
label it clearly as a preview in the report.

### 6. Preview Flags

For `FLAG`:

- Do not mutate in-memory records or provenance.
- Emit a full review row with:
  - `flag_id`
  - source file, municipality, origin, placemark index, raw name
  - source lon/lat
  - nearest existing id, origin, lon/lat
  - distance in meters rounded to 3 decimals
  - source component member count and member UIDs
  - reason `spatial_near_match`

### 7. Preview Adds

For initial `ADD` candidates:

- Cluster ADD candidates batch-wide where representatives are strictly closer
  than `5.0 m`.
- Choose earliest candidate as the ADD representative.
- Preview one new record per ADD component:

```json
{
  "id": "coord_27.89196_43.17796",
  "coords": [27.8919611480698, 43.17796325765485],
  "origin": "etr_varna",
  "legacy_ids": ["etr_varna:27.89196115,43.17796326"]
}
```

- No `type`, `address`, `existence_status`, `operational_status`, or
  `review_status` should be added by H2.
- If an ADD cluster contains member points from multiple municipalities, report
  it as `cross_municipality_add_cluster=true` and use the representative's
  origin. Such rows should be highlighted for review.

### 8. Dry-Run Safety

Before writing report artifacts:

- Compute SHA256 of input and provenance.
- Run `mojibake_scan()` on preview records, preview provenance snippets, and the
  report object.
- After report write, recompute SHA256 of input and provenance and assert they
  are unchanged.
- Print a summary ending with:

```text
Dry run only; no hydrant/provenance files written. H4 signed apply required.
```

## Dry-Run Report Format

Recommended artifacts:

- `docs/audits/h2_kmz_consolidation_dry_run.json`: canonical machine-readable
  report.
- `docs/audits/h2_kmz_consolidation_dry_run.md`: human review report with full
  FLAG table.

Canonical JSON shape:

```json
{
  "schema_version": "h2_kmz_dry_run_v1",
  "mode": "dry_run",
  "generated_at": "2026-06-22T00:00:00+03:00",
  "thresholds_m": {
    "intra_batch_dedup_strict_lt": 2.0,
    "rm_update_lte": 5.0,
    "rf_flag_lte": 20.0,
    "add_candidate_cluster_strict_lt": 5.0
  },
  "inputs": {
    "hydrants_json": {
      "path": "data/hydrants.json",
      "sha256": "65F4E4CCCE8528E53710BC53EEA3590D6B2BD92DDCABC81803B8DBAFDA93585B",
      "record_count": 5911
    },
    "provenance_json": {
      "path": "data/hydrants_provenance.json",
      "sha256": "894F81F6C2728BEB3356551A9FD6074435A520E3C00CA6AA843E58ED43D1016E",
      "record_count": 5911
    },
    "kmz_files": [
      {
        "path": "data/hydrants_17_06_26/Пожарни хидранти ЕТР Варна.kmz",
        "sha256": "DAD33C8A59299F084E7B584625D03417C6D3C6F5AB1DE360A985824D971D2E8B",
        "municipality": "varna",
        "origin": "etr_varna",
        "kml_entry": "doc.kml",
        "placemarks": 2681,
        "points": 2681,
        "extended_data": 0,
        "schema_data": 0
      }
    ]
  },
  "summary": {
    "raw_kmz_points": 4860,
    "deduped_source_points": 0,
    "intra_batch_duplicates_collapsed": 0,
    "updated": 0,
    "flagged": 0,
    "added": 0,
    "add_candidates_collapsed": 0,
    "projected_output_count_if_applied": 0
  },
  "per_file": [
    {
      "source_file": "Пожарни хидранти ЕТР Варна.kmz",
      "municipality": "varna",
      "origin": "etr_varna",
      "raw_points": 2681,
      "dedup_representatives": 0,
      "dedup_nonrepresentatives": 0,
      "updated": 0,
      "flagged": 0,
      "added": 0
    }
  ],
  "e0_reconciliation": {
    "e0_raw_independent": {
      "raw_points": 4860,
      "updated": 3237,
      "flagged": 318,
      "added": 1305
    },
    "h2_post_dedup": {
      "deduped_source_points": 0,
      "updated": 0,
      "flagged": 0,
      "added": 0
    },
    "deltas": {
      "raw_points": 0,
      "updated": 0,
      "flagged": 0,
      "added": 0
    },
    "explanation": "E0 classified 4,860 raw placemarks independently. H2 first collapses <2 m source components, then collapses ADD candidates <5 m, so duplicate source members no longer produce their own UPDATE/FLAG/ADD rows."
  },
  "flags": [
    {
      "flag_id": "FLAG-0001",
      "source_uid": "etr_varna:27.00000000,43.00000000",
      "source_file": "Пожарни хидранти ЕТР Варна.kmz",
      "municipality": "varna",
      "origin": "etr_varna",
      "placemark_index": 123,
      "name": "raw KML name or blank",
      "lon": 27.0,
      "lat": 43.0,
      "nearest_existing_id": "coord_...",
      "nearest_existing_origin": "vik",
      "nearest_existing_lon": 27.0,
      "nearest_existing_lat": 43.0,
      "distance_m": 6.123,
      "member_count": 1,
      "member_uids": ["etr_varna:27.00000000,43.00000000"]
    }
  ],
  "add_groups": [],
  "update_groups_summary_only": true
}
```

Markdown report layout:

1. Header with mode, timestamp, input hashes, thresholds, and explicit
   "no data was mutated".
2. Summary table: raw points, deduped points, duplicates collapsed, updated,
   flagged, added, projected output count.
3. Per-file table: raw, deduped representatives, dedup drops, updated, flagged,
   added.
4. E0 reconciliation table:

```text
Metric                 E0 raw independent   H2 post-dedup   Delta
raw/deduped points      4860                <actual>        <actual - 4860>
UPDATE                  3237                <actual>        <actual - 3237>
FLAG                    318                 <actual>        <actual - 318>
ADD                     1305                <actual>        <actual - 1305>
```

5. Short reconciliation explanation:
   E0 counted every raw placemark independently. H2 counts source clusters after
   strict `<2 m` dedup first, so nonrepresentative duplicates disappear from the
   operation counts. A second strict `<5 m` clustering pass may additionally
   reduce ADD count. The report must attribute reductions to
   `intra_batch_2m` versus `add_candidate_5m`.
6. Full FLAG list, sorted by source file order then distance descending or
   placemark index. Recommended table columns:

```text
# | source_file | placemark | source_uid | lon | lat | nearest_id | nearest_origin | distance_m | name
```

7. Review notes for cross-file dedup clusters and cross-municipality ADD
   clusters, if any.

## Test Plan

Add `tests/test_etr_kmz_adapter.py` using only standard-library `unittest`,
`tempfile`, and `zipfile`.

Required tests:

1. Parser reads a synthetic KMZ with one `doc.kml`, KML namespace
   `http://www.opengis.net/kml/2.2`, and Point coordinates in `lon,lat,alt`
   order.
2. Parser fails loudly on missing KML and multiple KML entries.
3. Parser records `ExtendedData`/`SchemaData` counts but does not infer fields
   from them; current real files are zero-count.
4. Municipality mapping from exact basenames yields `etr_varna`, `etr_devnya`,
   `etr_dolni_chiflik`, and `etr_provadia`.
5. Coordinates outside H1 bbox are reported as invalid and excluded from match
   classification.
6. Batch dedup collapses connected components with distance `<2.0 m` and does
   not collapse points at exactly `2.0 m`.
7. Dedup representative is deterministic under shuffled input.
8. Spatial classification uses H1 boundary behavior: `5.0 m` is UPDATE,
   `5.0 + epsilon` is FLAG, `20.0 m` is FLAG, `20.0 + epsilon` is ADD.
9. UPDATE preview appends only ETR legacy aliases and provenance preview; no
   type/status/address/coords/origin changes.
10. FLAG preview leaves records and provenance byte-identical and emits nearest
    id plus distance.
11. ADD preview emits only `id`, `coords`, `origin`, and `legacy_ids`; no
    type/status/address fields.
12. ADD candidate clustering collapses candidates `<5.0 m` and does not
    collapse candidates at exactly `5.0 m`.
13. Dry-run CLI has no `--apply` argument and never writes `--input` or
    `--provenance`.
14. Dry-run report JSON contains summary, per-file breakdown, E0 reconciliation,
    and full FLAG rows.
15. Report sort order is deterministic across two runs.
16. Mojibake scan passes generated reports containing Cyrillic filenames/names.
17. Real data guard mirrors H1: if tests read real `data/hydrants.json` for an
    integration smoke, compute SHA256 before/after and assert unchanged. No test
    writes outside `tempfile.TemporaryDirectory()`.

Recommended verification commands after H2 implementation:

```powershell
python -m unittest tests.test_etr_kmz_adapter
python -m unittest discover -s tests
python scripts/import_etr_kmz.py --source-dir data/hydrants_17_06_26 --input data/hydrants.json --provenance data/hydrants_provenance.json --json-report docs/audits/h2_kmz_consolidation_dry_run.json --md-report docs/audits/h2_kmz_consolidation_dry_run.md
git diff -- data/hydrants.json data/hydrants_provenance.json
```

Expected final `git diff -- data/hydrants.json data/hydrants_provenance.json`
output for H2: empty.

## Approval-Gate Check

| Gate | Status |
|---|---|
| Architecture/file layout | New adapter/test files are planned, but no implementation in this task. H2 should be reviewed before execution. |
| Data source change | User explicitly requested the 2026-06-17 ETR KMZ batch; KMZ contents were inspected. |
| Runtime/build dependency | No new dependency planned; standard library only. |
| UI labels / frontend | Not touched. |
| Real data mutation | Forbidden in H2. `data/hydrants.json` and provenance remain unchanged. |
| `--apply` | Forbidden in H2; H4 only after signed approval. |
| Stable IDs | H3 only. H2 uses H1 coord-id stub for preview. |
| Commit/push | Forbidden by request. |
| Personal data | KMZ names are source labels only; no reporter/person field is introduced. |

## Open Questions

None block H2 planning. Recommended defaults above are sufficient for a dry-run
review artifact.

Confirm before H4 apply:

1. Exact ETR `legacy_ids` alias string. Recommended default:
   `etr_<municipality>:<lon8>,<lat8>`.
2. Whether H4 should preserve source representative coordinates or switch ADD
   clusters to a centroid. H2 recommends preserving an actual KMZ coordinate.
3. Whether the canonical review artifact should remain JSON+Markdown or add a
   CSV FLAG export for manual spreadsheet review.

## H2 File Change Envelope

Future H2 implementation should touch only:

- `scripts/import_etr_kmz.py`
- `tests/test_etr_kmz_adapter.py`
- generated dry-run reports under `docs/audits/`

It must not touch:

- `data/hydrants.json`
- `data/hydrants_provenance.json`
- `index.html`
- `worker/`
- Git commit or push state
