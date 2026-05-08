# Data Architecture Audit 2026-05-08

## Executive summary

Top 5 findings:
- Runtime dataset has **6,082** records: `{'vik': 3661, 'national': 2407, 'field_report': 14}`.
- `hydrants_varna.json` has 3,934 records, matching the five KMZ placemark total; it is a derived VIK reference, not the full runtime corpus.
- NAT coordinates are declared EPSG:3857 but need inverse EPSG:3857 plus axis swap to resolve to Bulgaria.
- The five VIK KMZ files have no `ExtendedData/Data/value`; attributes are in HTML description tables.
- Runtime IDs remain heterogeneous across numeric VIK, suffix VIK, namespaced VIK, NAT, field short-hash, and split regional numeric forms.

Top 3 risks:
- Dedup/ID unification can break report references because there is no alias/history field.
- Address search is source-asymmetric: NAT has address-like `name`, VIK runtime `a` is mostly empty, field reports are free text.
- Stale ingest code still targets old embedded `index.html` JSON.

Key decision points needed: canonical ID/alias policy; address-source policy; report-history storage location.

## Required preamble

Scope: read-only audit per Petar brief ?Data Architecture Audit 2026-05-08? plus accepted corrections. Only repo write target: `docs/audits/data_architecture_audit_20260508.md`.

DBF execution choice: **choice (a)**. `dbfread` was installed successfully and used for `geo_fire_hydrants.dbf`; low-level DBF header parsing was also used.

KML parser note: KMZ files parsed with `ElementTree` path; `geo_fire_hydrants.kml` parser path `regex-fallback` because raw national KML contains XML-invalid/control-like text.

Deterministic filesystem inventory:
```text
.claude/settings.local.json 328
AGENTS.md 14669
audit/apply_field_reports.py 8439
CLAUDE.md 5572
data/hydrants.json 968365
DEVNIa.kmz 6825
docs/activeContext.md 14106
docs/audits/governance_proposal_20260508.md 12889
docs/audits/issue_ingest_plan_20260508.md 16659
DOLNI_ChIFLIK.kmz 21976
extract_hydrants.py 1677
field_reports.json 5085
geo_fire_hydrants.dbf 16417749
geo_fire_hydrants.json 11661151
geo_fire_hydrants.kml 25696980
geo_fire_hydrants.prj 749
geo_fire_hydrants.shp 503004
geo_fire_hydrants.shx 143796
hydrants_varna.json 433069
index.html 304192
PROVADIIa.kmz 48139
README.md 8912
VARNA_IZTOK.kmz 50946
VARNA_ZAPAD.kmz 53395
wfsrequest.txt 430
Първа РС сев от бул Левски  23.06.25г.kml 305286
```

Files read in this session:
```text
AGENTS.md
CLAUDE.md
README.md
docs/activeContext.md
docs/audits/governance_proposal_20260508.md
docs/audits/issue_ingest_plan_20260508.md
extract_hydrants.py
audit/apply_field_reports.py
index.html
data/hydrants.json
field_reports.json
hydrants_varna.json
geo_fire_hydrants.json
geo_fire_hydrants.kml
geo_fire_hydrants.prj
geo_fire_hydrants.shp
geo_fire_hydrants.dbf
geo_fire_hydrants.shx
wfsrequest.txt
DEVNIa.kmz
DOLNI_ChIFLIK.kmz
PROVADIIa.kmz
VARNA_IZTOK.kmz
VARNA_ZAPAD.kmz
Първа РС сев от бул Левски  23.06.25г.kml
```

Negative findings matrix:
| Category | Finding |
|---|---|
| *.csv | no files matching `*.csv` found in scope |
| *.gpx | no files matching `*.gpx` found in scope |
| root apply_field_reports.py | no root file found; untracked `audit/apply_field_reports.py` found |
| ogrinfo | not installed; used dbfread + binary parsers |
| KMZ .prj | no .prj sidecars inside KMZ archives |
| KMZ ExtendedData | no `kml:ExtendedData/kml:Data/kml:value` fields in five KMZ files |
| source archive git history | KMZ/KML/SHP/DBF/PRJ/TXT source files untracked |

Quoted declared metadata:
`wfsrequest.txt`:
```text
http://iis.bgfire.eu/geoserver/wfs?service=WFS&version=1.1.0&request=GetFeature&typename=gdpbzn%3Ageo_fire_hydrants&outputFormat=shape-zip&srsname=EPSG%3A3857&maxFeatures=100000&userId=1615&sessionUuid=c478c0e1-7b0b-40bc-8cf0-aa9050154859&appln=NULL&incidentId=NULL&mapCode=BASE_MAP&viewparams=p_user_id%3A1615%3Bp_session_uuid%3Ac478c0e1-7b0b-40bc-8cf0-aa9050154859%3Bp_appln%3ANULL%3Bp_incident_id%3ANULL%3Bp_map_code%3ABASE_MAP
```
`geo_fire_hydrants.prj`:
```text
PROJCS["WGS 84 / Pseudo-Mercator", GEOGCS["WGS 84", DATUM["World Geodetic System 1984", SPHEROID["WGS 84", 6378137.0, 298.257223563, AUTHORITY["EPSG","7030"]], AUTHORITY["EPSG","6326"]], PRIMEM["Greenwich", 0.0, AUTHORITY["EPSG","8901"]], UNIT["degree", 0.017453292519943295], AXIS["Geodetic longitude", EAST], AXIS["Geodetic latitude", NORTH], AUTHORITY["EPSG","4326"]], PROJECTION["Popular Visualisation Pseudo Mercator", AUTHORITY["EPSG","1024"]], PARAMETER["semi_minor", 6378137.0], PARAMETER["latitude_of_origin", 0.0], PARAMETER["central_meridian", 0.0], PARAMETER["scale_factor", 1.0], PARAMETER["false_easting", 0.0], PARAMETER["false_northing", 0.0], UNIT["m", 1.0], AXIS["Easting", EAST], AXIS["Northing", NORTH], AUTHORITY["EPSG","3857"]]
```
KML headers:
```text
geo_fire_hydrants.kml: <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
Първа РС сев от бул Левски  23.06.25г.kml: <?xml version="1.0" encoding="UTF-8"?>
DEVNIa.kmz/doc.kml: <?xml version="1.0" encoding="UTF-8"?>
DOLNI_ChIFLIK.kmz/doc.kml: <?xml version="1.0" encoding="UTF-8"?>
PROVADIIa.kmz/doc.kml: <?xml version="1.0" encoding="UTF-8"?>
VARNA_IZTOK.kmz/doc.kml: <?xml version="1.0" encoding="UTF-8"?>
VARNA_ZAPAD.kmz/doc.kml: <?xml version="1.0" encoding="UTF-8"?>
```
KMZ archive members:
```text
DEVNIa.kmz
  6B770F0DF2844F38ADC4FD8E0B3935BC.xsl 5485
  doc.kml 134161
  Layer0_Symbol_1aeae350_0.png 252
DOLNI_ChIFLIK.kmz
  5B5FDAE9781640809CB6229A29FE3C69.xsl 5485
  doc.kml 697341
  Layer0_Symbol_bdd2fa8_0.png 191
PROVADIIa.kmz
  8236EBD4FFE04179A905F7EA4F45CD9D.xsl 5485
  doc.kml 1706070
  Layer0_Symbol_bdd4460_0.png 191
VARNA_IZTOK.kmz
  D90AD99BB4E648AEAAE57C540DBCF3E1.xsl 5485
  doc.kml 1635709
  Layer0_Symbol_bd19cb0_0.png 214
VARNA_ZAPAD.kmz
  1A2C29A2CA0848C1A511611D90AC8D58.xsl 5485
  doc.kml 1728984
  Layer0_Symbol_1c0bd1c8_0.png 214
```
Encoding scan results:
```text
Command form: Select-String -Path <read text files> -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8
Result: no matches returned for scanned UTF-8 text files in scope.
```

## Section 1: File Inventory

| Path | Format | Size | Records | CRS | Capture/date evidence | Lineage | Git history |
|---|---:|---:|---:|---|---|---|---|
| `.claude/settings.local.json` | JSON | 328 | n/a | n/a | unknown | support/non-hydrant | untracked/no git history in this repo |
| `AGENTS.md` | MD | 14669 | n/a | n/a | unknown | support/non-hydrant | ef47a64 2026-05-08 governance: ratify proposal 20260508 (de-dup, codex protocol, README corrections) dfd7aa9 2026-05-07 docs: sync after commit 16 2535920 2026-05-06 sync AGENTS.md and CLAUDE.md to runtime reality 79f2517 2026-05-06 fix(data): remove 2 VIK duplicate records, document wrong_location ingest rule b253c4b 2026-05-05 feat(schema): add status field, backfill 4 verified hydrants 39acc92 2026-05-05 feat: initial import of Varna hydrants project |
| `audit/apply_field_reports.py` | PY | 8439 | n/a | n/a | unknown | support/non-hydrant | untracked/no git history in this repo |
| `CLAUDE.md` | MD | 5572 | n/a | n/a | unknown | support/non-hydrant | ef47a64 2026-05-08 governance: ratify proposal 20260508 (de-dup, codex protocol, README corrections) dfd7aa9 2026-05-07 docs: sync after commit 16 2535920 2026-05-06 sync AGENTS.md and CLAUDE.md to runtime reality 79f2517 2026-05-06 fix(data): remove 2 VIK duplicate records, document wrong_location ingest rule 39acc92 2026-05-05 feat: initial import of Varna hydrants project |
| `data/hydrants.json` | JSON | 968365 | 6082 | WGS84 [lon,lat] | git 2026-05-06..2026-05-08 | derived runtime vik+national+field_report | 2dcab73 2026-05-08 ingest: 8 field reports (issues #29-#36) 25289ea 2026-05-06 extract hydrant data to data/hydrants.json (6,079 records) |
| `DEVNIa.kmz` | KMZ | 6825 | 100 | KML WGS84 lon,lat,alt | mtime 2026-05-04 | VIK KMZ source | untracked/no git history in this repo |
| `docs/activeContext.md` | MD | 14106 | n/a | n/a | unknown | support/non-hydrant | 0fcea12 2026-05-08 docs: update activeContext post-ingest #29-#36 + cleanup ef47a64 2026-05-08 governance: ratify proposal 20260508 (de-dup, codex protocol, README corrections) c82ea26 2026-05-07 docs: sync after Sprint 1.5 a89a9af 2026-05-07 docs: point Last Known Good at sprint 1.5 plan and link plan as next planned work 9ec694f 2026-05-07 docs: record commit G hash as Last Known Good dfd7aa9 2026-05-07 docs: sync after commit 16 84bc536 2026-05-07 mark commit 15 deployed: Worker GET /issues + KV cache live dffc634 2026-05-06 update active context final commit hash 2535920 2026-05-06 sync AGENTS.md and CLAUDE.md to runtime reality |
| `docs/audits/governance_proposal_20260508.md` | MD | 12889 | n/a | n/a | unknown | support/non-hydrant | ef47a64 2026-05-08 governance: ratify proposal 20260508 (de-dup, codex protocol, README corrections) |
| `docs/audits/issue_ingest_plan_20260508.md` | MD | 16659 | n/a | n/a | unknown | support/non-hydrant | untracked/no git history in this repo |
| `DOLNI_ChIFLIK.kmz` | KMZ | 21976 | 541 | KML WGS84 lon,lat,alt | mtime 2026-05-04 | VIK KMZ source | untracked/no git history in this repo |
| `extract_hydrants.py` | PY | 1677 | n/a | n/a | unknown | support/non-hydrant | 25289ea 2026-05-06 extract hydrant data to data/hydrants.json (6,079 records) |
| `field_reports.json` | JSON | 5085 | 14 | WGS84 [lon,lat] | git 2026-05-05..2026-05-08 | field-survey state | 2dcab73 2026-05-08 ingest: 8 field reports (issues #29-#36) c43d6f4 2026-05-06 feat(data): apply 15 field reports — 7 new, 6 confirmations, 2 coord fixes b253c4b 2026-05-05 feat(schema): add status field, backfill 4 verified hydrants eac820a 2026-05-05 feat(data): add 1 field-reported hydrant (#13) abbe36d 2026-05-05 feat(data): add 3 field-reported hydrants near block 408 (#10 #11 #12) |
| `geo_fire_hydrants.dbf` | DBF | 16417749 | 17962 | no geometry | mtime 2026-05-04 | NAT WFS DBF attributes | untracked/no git history in this repo |
| `geo_fire_hydrants.json` | JSON | 11661151 | 17962 | declared EPSG:3857; inverse+swap | 2026-05-04T12:12:20.537Z | NAT WFS JSON | untracked/no git history in this repo |
| `geo_fire_hydrants.kml` | KML | 25696980 | 17962 | KML text lat,lon empirically | mtime 2026-05-04 | NAT WFS KML | untracked/no git history in this repo |
| `geo_fire_hydrants.prj` | PRJ | 749 | 1 CRS | EPSG:3857 declared | mtime 2026-05-04 | NAT sidecar | untracked/no git history in this repo |
| `geo_fire_hydrants.shp` | SHP | 503004 | 4 | PRJ EPSG:3857; inverse+swap | mtime 2026-05-04 | NAT WFS SHP geometry | untracked/no git history in this repo |
| `geo_fire_hydrants.shx` | SHX | 143796 | 17962 | inherits .prj | mtime 2026-05-04 | NAT index | untracked/no git history in this repo |
| `hydrants_varna.json` | JSON | 433069 | 3934 | WGS84 [lon,lat] | mtime 2026-05-04; git import 2026-05-05 | derived VIK reference | 39acc92 2026-05-05 feat: initial import of Varna hydrants project |
| `index.html` | HTML | 304192 | n/a | n/a | unknown | support/non-hydrant | 7412878 2026-05-07 feat(ux): all-mode cluster guard + ID-based active target 8e549e1 2026-05-07 fix(ux): welcome screen 2 text + report modal type display 06c46b1 2026-05-07 feat(realtime): client polling of /issues every 15s with marker status merge 25289ea 2026-05-06 extract hydrant data to data/hydrants.json (6,079 records) 79f2517 2026-05-06 fix(data): remove 2 VIK duplicate records, document wrong_location ingest rule 9340041 2026-05-06 feat(ux): color-only status visualization + legend 8ec76e8 2026-05-06 fix(ux): prepick banner visible despite hidden attribute c7d122a 2026-05-06 feat(ux): pre-pick mode for global + button and simplified placement banner 2665ced 2026-05-06 fix(ux): make marker long-press work on touch devices c43d6f4 2026-05-06 feat(data): apply 15 field reports — 7 new, 6 confirmations, 2 coord fixes 0205cd8 2026-05-06 feat(ux): long-press hydrant pin for report menu 893f1a4 2026-05-06 feat(ux): tap hydrant pin opens report menu directly 9e9153c 2026-05-06 fix(ux): wrong_location placement requires actual user input eef3af5 2026-05-06 fix(ux): auto-enter placement mode for wrong_location reports b168df9 2026-05-06 feat(ux): remove bottom card report button, relabel popup button ae9d3f1 2026-05-05 feat(ux): expand + button to report menu, update welcome text, add placement banner ed11f09 2026-05-05 feat(ux): add 3-screen welcome modal for first-time onboarding b253c4b 2026-05-05 feat(schema): add status field, backfill 4 verified hydrants da15548 2026-05-05 fix(nav): resolve orientation source race in compass handler eac820a 2026-05-05 feat(data): add 1 field-reported hydrant (#13) abbe36d 2026-05-05 feat(data): add 3 field-reported hydrants near block 408 (#10 #11 #12) aa00869 2026-05-05 feat: rename merged HTML to index.html for GitHub Pages |
| `PROVADIIa.kmz` | KMZ | 48139 | 1320 | KML WGS84 lon,lat,alt | mtime 2026-05-04 | VIK KMZ source | untracked/no git history in this repo |
| `README.md` | MD | 8912 | n/a | n/a | unknown | support/non-hydrant | ef47a64 2026-05-08 governance: ratify proposal 20260508 (de-dup, codex protocol, README corrections) 219cf7a 2026-05-07 Fix number of hydrants listed in README b23017f 2026-05-07 Update total hydrants count in README 607cd8c 2026-05-05 Update README.md 224e846 2026-05-05 Revise warnings and data ownership in README d29a701 2026-05-05 Revise target users section in README 39acc92 2026-05-05 feat: initial import of Varna hydrants project |
| `VARNA_IZTOK.kmz` | KMZ | 50946 | 959 | KML WGS84 lon,lat,alt | mtime 2026-05-04 | VIK KMZ source | untracked/no git history in this repo |
| `VARNA_ZAPAD.kmz` | KMZ | 53395 | 1014 | KML WGS84 lon,lat,alt | mtime 2026-05-04 | VIK KMZ source | untracked/no git history in this repo |
| `wfsrequest.txt` | TXT | 430 | 1 URL | srsname=EPSG:3857 | mtime 2026-05-04 | NAT provenance | untracked/no git history in this repo |
| `Първа РС сев от бул Левски  23.06.25г.kml` | KML | 305286 | 654 | KML WGS84 lon,lat,alt | filename 23.06.25?; mtime 2026-05-07 | unknown local KML | untracked/no git history in this repo |

Schemas:
### `data/hydrants.json`
| Field | Types | 2 samples |
|---|---|---|
| `a` | string:6082 | ; ул. ''Проф. Константин Ирече |
| `c` | array:6082 | [27.669648, 43.310904]; [27.671834, 43.352484] |
| `duplicate_distance_m` | float:271 | 11.5575; 7.8538 |
| `i` | string:6082 | 10122-DV; 10123 |
| `i_original` | string:1081 | 10122; 10124 |
| `o` | string:6082 | vik; national |
| `r` | string:6082 | ; 14-ти подрайон |
| `replaced_vik` | string:271 | 8526-DV; 8531-DV |
| `replaced_vik_coord` | array:271 | [27.773072, 43.20094]; [27.777523, 43.202102] |
| `report_id` | string:14 | ba91e3ff-f28a-4499-82ba-61d850a051a4; 3326a776-516a-4e34-8e34-efd4773c5e80 |
| `reported_at` | string:14 | 2026-05-05T11:06:15Z; 2026-05-05T11:05:14Z |
| `s` | string:6082 | DEVNIa;  |
| `st` | string:6082 | ; заснето от Ботев |
| `status` | string:25 | verified; reported |
| `t` | string:6082 | ; underground |
| `z` | string:6082 | ; uin=5877; created=2021-06-08T08:50:26.365Z; updated=; geo_region=73 |

### `hydrants_varna.json`
| Field | Types | 2 samples |
|---|---|---|
| `a` | string:3934 | ; ул. ''Проф. Константин Ирече |
| `c` | array:3934 | [27.669648, 43.310904]; [27.671834, 43.352484] |
| `i` | string:3934 | 10122; 10123 |
| `r` | string:3934 | ; 14-ти подрайон |
| `s` | string:3934 | DEVNIa; DOLNI_ChIFLIK |
| `st` | string:3934 | ; заснето от Ботев |
| `t` | string:3934 | ; ПХ 70/80 |
| `z` | string:3934 | ; БДС EN 14384 |

### `field_reports.json`
| Field | Types | 2 samples |
|---|---|---|
| `a` | string:14 | Пред бл. 408 вх 13; Пред бл. 408 вх.17 |
| `c` | array:14 | [27.847417, 43.250208]; [27.848389, 43.250078] |
| `i` | string:14 | field_ba91e3ff; field_3326a776 |
| `o` | string:14 | field_report |
| `r` | string:14 |  |
| `report_id` | string:14 | ba91e3ff-f28a-4499-82ba-61d850a051a4; 3326a776-516a-4e34-8e34-efd4773c5e80 |
| `reported_at` | string:14 | 2026-05-05T11:06:15Z; 2026-05-05T11:05:14Z |
| `s` | string:14 |  |
| `st` | string:14 |  |
| `status` | string:14 | verified |
| `t` | string:14 | надземен |
| `z` | string:14 |  |

### `geo_fire_hydrants.json` properties / DBF
| Field | JSON types/samples | DBF types/samples |
|---|---|---|
| `address_id` | null:12299, int:5663; 2202; 2203 | null:12299, int:5663; 2202; 2203 |
| `created_by` | int:17962; 34; 710 | int:17962; 34; 710 |
| `created_on` | string:17962; 2022-03-23T10:10:56.486Z; 2022-03-23T10:10:56.771Z | date:17962; "2022-03-23"; "2022-02-09" |
| `geo_region` | ;  | int:17921, null:41; 5; 198 |
| `geo_region_structure_id` | int:17921, null:41; 5; 198 | ;  |
| `id` | int:17962; 12651; 12652 | int:17962; 12651; 12652 |
| `is_active` | bool:17962; true; false | bool:17962; true; false |
| `is_importe` | ;  | bool:17962; false |
| `is_imported` | bool:17962; false | ;  |
| `n_fire_hy0` | ;  | int:17962; 1; 2 |
| `n_fire_hyd` | ;  | int:17961, null:1; 4; 3 |
| `n_fire_hydrant_status_id` | int:17962; 1; 2 | ;  |
| `n_fire_hydrant_type_id` | int:17961, null:1; 4; 3 | ;  |
| `name` | string:17960, null:2; Улица Захари Зограф 14А, 1415 София, България; Улица Екзарх Йосиф 46, 1000 София, България | string:17962; ????? ?????? ?????? 14?, 1415 ?????, ????????; ????? ?????? ????? 46, 1000 ?????, ???????? |
| `notes` | string:17956, null:6; null; тест | string:17962; ; ???? |
| `uin` | string:17923, null:39; 1000000; 1000001 | string:17962; 1000000; 1000001 |
| `updated_by` | null:16731, int:1231; 34; null | null:16731, int:1231; 34; null |
| `updated_on` | null:16731, string:1231; 2022-03-23T10:11:06.189Z; 2022-03-23T10:11:06.338Z | null:16731, date:1231; "2022-03-23"; null |

DBF header fields: `[('id', 'N', 19, 0), ('name', 'C', 254, 0), ('geo_region', 'N', 19, 0), ('notes', 'C', 254, 0), ('address_id', 'N', 19, 0), ('created_by', 'N', 19, 0), ('created_on', 'D', 8, 0), ('updated_by', 'N', 19, 0), ('updated_on', 'D', 8, 0), ('n_fire_hyd', 'N', 19, 0), ('is_active', 'L', 1, 0), ('n_fire_hy0', 'N', 19, 0), ('uin', 'C', 254, 0), ('is_importe', 'L', 1, 0)]`.

## Section 2: ID Convention Analysis

| Pattern | Regex | Count | 3 samples | Suspected origin | Determinism |
|---|---|---:|---|---|---|
| numeric VIK | `^\d+$` | 2580 | `10123, 10125, 10126` | [('vik', 2580)] | deterministic-looking |
| NAT | `^NAT-\d+$` | 2407 | `NAT-5877, NAT-5875, NAT-5580` | [('national', 2407)] | deterministic-looking |
| namespaced VIK | `^VIK-[A-Z_]+-\d+$` | 644 | `VIK-VARNA_IZTOK-0001, VIK-VARNA_IZTOK-0002, VIK-VARNA_IZTOK-0003` | [('vik', 644)] | deterministic-looking |
| numeric VIK + region suffix | `^\d+-[A-Z]{2}$` | 432 | `10122-DV, 10124-DV, 10523-DV` | [('vik', 432)] | deterministic-looking |
| field report short hash | `^field_[0-9a-f]{8}$` | 14 | `field_ba91e3ff, field_3326a776, field_1a6e6d56` | [('field_report', 14)] | UUID-derived/non-deterministic |
| split regional numeric | `^\d+-[A-Z]{2}-\d+$` | 5 | `83-IZ-1, 83-IZ-2, 1106-ZP-1` | [('vik', 5)] | deterministic-looking |

Exact runtime ID collisions: `[]`.
Numeric-base cross-pattern collisions: 200; samples `{"10122": ["10122-DC", "10122-DV"], "10124": ["10124-DC", "10124-DV"], "10523": ["10523-DC", "10523-DV"], "10923": ["10923-DC", "10923-DV"], "10924": ["10924-DC", "10924-DV"], "10925": ["10925-DC", "10925-DV"], "10926": ["10926-DC", "10926-DV"], "11322": ["11322-DV", "11322-PR"], "11323": ["11323-DV", "11323-PR"], "11324": ["11324-DV", "11324-PR"]}`.

`hydrants_varna.json`:
| Pattern | Regex | Count | 3 samples |
|---|---|---:|---|
| numeric VIK | `^\d+$` | 3934 | `10122, 10123, 10124` |

`field_reports.json`:
| Pattern | Regex | Count | 3 samples |
|---|---|---:|---|
| field report short hash | `^field_[0-9a-f]{8}$` | 14 | `field_ba91e3ff, field_3326a776, field_1a6e6d56` |

`geo_fire_hydrants.json properties.id`:
| Pattern | Regex | Count | 3 samples |
|---|---|---:|---|
| numeric VIK | `^\d+$` | 17962 | `12651, 12652, 12653` |

KMZ ID-like fields:
| File | Fields/counts | First 3 IDs |
|---|---|---|
| `DEVNIa.kmz` | `{'objectid': 100, 'FID': 8}` | `10522, 10523, 10524` |
| `DOLNI_ChIFLIK.kmz` | `{'FID': 455, 'objectid': 541}` | `8123, 13335, 9722` |
| `PROVADIIa.kmz` | `{'FID': 1065, 'objectid': 1320}` | `1, 2, 3` |
| `VARNA_IZTOK.kmz` | `{'FID': 934, 'objectid': 959, 'id': 959}` | `2, 3, 8` |
| `VARNA_ZAPAD.kmz` | `{'FID': 945, 'objectid': 1014, 'id': 1014}` | `1, 4, 5` |

## Section 3: Cross-File Duplication Analysis

Bulgaria sanity envelope lat `[41.2,44.3]`, lon `[22.3,28.7]`; excluded records are counted here.
| Source | Total | Valid | Excluded |
|---|---:|---:|---:|
| `data/hydrants.json` | 6082 | 6082 | 0 |
| `hydrants_varna.json` | 3934 | 3934 | 0 |
| `field_reports.json` | 14 | 14 | 0 |
| `geo_fire_hydrants.json` | 17962 | 4 | 17958 |
| `geo_fire_hydrants.shp` | 17960 | 4 | 17956 |
| `geo_fire_hydrants.kml` | 17962 | 4 | 17958 |
| `DEVNIa.kmz` | 100 | 100 | 0 |
| `DOLNI_ChIFLIK.kmz` | 541 | 541 | 0 |
| `PROVADIIa.kmz` | 1320 | 1320 | 0 |
| `VARNA_IZTOK.kmz` | 959 | 959 | 0 |
| `VARNA_ZAPAD.kmz` | 1014 | 1014 | 0 |
| `Първа РС сев от бул Левски  23.06.25г.kml` | 654 | 654 | 0 |

Cross-file pair counts within 50 m:
| A | B | [0,0.1m] | (0.1,1m] | (1,5m] | (5,15m] | (15,50m] |
|---|---|---:|---:|---:|---:|---:|
| `data/hydrants.json` | `hydrants_varna.json` | 3936 | 4 | 92 | 264 | 1227 |
| `data/hydrants.json` | `field_reports.json` | 14 | 0 | 0 | 0 | 4 |
| `data/hydrants.json` | `geo_fire_hydrants.json` | 0 | 0 | 0 | 0 | 0 |
| `data/hydrants.json` | `geo_fire_hydrants.shp` | 0 | 0 | 0 | 0 | 0 |
| `data/hydrants.json` | `geo_fire_hydrants.kml` | 0 | 0 | 0 | 0 | 0 |
| `data/hydrants.json` | `DEVNIa.kmz` | 98 | 0 | 0 | 2 | 21 |
| `data/hydrants.json` | `DOLNI_ChIFLIK.kmz` | 526 | 0 | 4 | 15 | 79 |
| `data/hydrants.json` | `PROVADIIa.kmz` | 1278 | 2 | 5 | 42 | 238 |
| `data/hydrants.json` | `VARNA_IZTOK.kmz` | 1121 | 0 | 27 | 69 | 467 |
| `data/hydrants.json` | `VARNA_ZAPAD.kmz` | 913 | 3 | 55 | 135 | 423 |
| `data/hydrants.json` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 6 | 113 | 223 | 284 |
| `hydrants_varna.json` | `field_reports.json` | 0 | 0 | 0 | 0 | 2 |
| `hydrants_varna.json` | `geo_fire_hydrants.json` | 0 | 0 | 0 | 0 | 0 |
| `hydrants_varna.json` | `geo_fire_hydrants.shp` | 0 | 0 | 0 | 0 | 0 |
| `hydrants_varna.json` | `geo_fire_hydrants.kml` | 0 | 0 | 0 | 0 | 0 |
| `hydrants_varna.json` | `DEVNIa.kmz` | 100 | 0 | 0 | 0 | 8 |
| `hydrants_varna.json` | `DOLNI_ChIFLIK.kmz` | 541 | 0 | 2 | 2 | 28 |
| `hydrants_varna.json` | `PROVADIIa.kmz` | 1320 | 0 | 0 | 8 | 116 |
| `hydrants_varna.json` | `VARNA_IZTOK.kmz` | 1177 | 0 | 10 | 30 | 346 |
| `hydrants_varna.json` | `VARNA_ZAPAD.kmz` | 1078 | 0 | 6 | 22 | 228 |
| `hydrants_varna.json` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 6 | 111 | 197 | 217 |
| `field_reports.json` | `geo_fire_hydrants.json` | 0 | 0 | 0 | 0 | 0 |
| `field_reports.json` | `geo_fire_hydrants.shp` | 0 | 0 | 0 | 0 | 0 |
| `field_reports.json` | `geo_fire_hydrants.kml` | 0 | 0 | 0 | 0 | 0 |
| `field_reports.json` | `DEVNIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `field_reports.json` | `DOLNI_ChIFLIK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `field_reports.json` | `PROVADIIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `field_reports.json` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 1 |
| `field_reports.json` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 1 |
| `field_reports.json` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 1 |
| `geo_fire_hydrants.json` | `geo_fire_hydrants.shp` | 4 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `geo_fire_hydrants.kml` | 4 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `DEVNIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `DOLNI_ChIFLIK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `PROVADIIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.json` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `geo_fire_hydrants.kml` | 4 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `DEVNIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `DOLNI_ChIFLIK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `PROVADIIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.shp` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.kml` | `DEVNIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.kml` | `DOLNI_ChIFLIK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.kml` | `PROVADIIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.kml` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.kml` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 0 |
| `geo_fire_hydrants.kml` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 0 |
| `DEVNIa.kmz` | `DOLNI_ChIFLIK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DEVNIa.kmz` | `PROVADIIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DEVNIa.kmz` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DEVNIa.kmz` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DEVNIa.kmz` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 0 |
| `DOLNI_ChIFLIK.kmz` | `PROVADIIa.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DOLNI_ChIFLIK.kmz` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DOLNI_ChIFLIK.kmz` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 0 |
| `DOLNI_ChIFLIK.kmz` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 0 |
| `PROVADIIa.kmz` | `VARNA_IZTOK.kmz` | 0 | 0 | 0 | 0 | 0 |
| `PROVADIIa.kmz` | `VARNA_ZAPAD.kmz` | 0 | 0 | 0 | 0 | 0 |
| `PROVADIIa.kmz` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 0 | 0 |
| `VARNA_IZTOK.kmz` | `VARNA_ZAPAD.kmz` | 50 | 0 | 0 | 0 | 18 |
| `VARNA_IZTOK.kmz` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 1 | 43 | 103 | 107 |
| `VARNA_ZAPAD.kmz` | `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 6 | 67 | 94 | 110 |

Representative cross-file samples, up to 5 per non-empty bucket:
### `data/hydrants.json` ? `hydrants_varna.json`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `10122-DV` | `[27.669648, 43.310904]` | `10122` | `[27.669648, 43.310904]` |
| [0, 0.1m] | 0.000 | `10123` | `[27.671834, 43.352484]` | `10123` | `[27.671834, 43.352484]` |
| [0, 0.1m] | 0.000 | `10124-DV` | `[27.665997, 43.353007]` | `10124` | `[27.665997, 43.353007]` |
| [0, 0.1m] | 0.000 | `10125` | `[27.667264, 43.353561]` | `10125` | `[27.667264, 43.353561]` |
| [0, 0.1m] | 0.000 | `10126` | `[27.674792, 43.352808]` | `10126` | `[27.674792, 43.352808]` |
| (0.1, 1m] | 0.635 | `NAT-6911` | `[27.43755799, 43.1856936]` | `74` | `[27.437553, 43.185698]` |
| (0.1, 1m] | 0.747 | `NAT-5809` | `[27.81799812, 43.26253557]` | `0` | `[27.818, 43.262529]` |
| (0.1, 1m] | 0.842 | `NAT-6014` | `[27.86389876, 43.23659468]` | `1050` | `[27.863909, 43.236596]` |
| (0.1, 1m] | 0.596 | `NAT-6002` | `[27.85692062, 43.23632783]` | `1055` | `[27.856916, 43.236332]` |
| (1, 5m] | 2.173 | `NAT-17471` | `[27.827019, 43.11135]` | `16128` | `[27.827042, 43.11134]` |
| (1, 5m] | 4.686 | `24572` | `[27.76732, 42.951804]` | `24573` | `[27.767281, 42.951773]` |
| (1, 5m] | 4.686 | `24573` | `[27.767281, 42.951773]` | `24572` | `[27.76732, 42.951804]` |
| (1, 5m] | 3.543 | `NAT-6687` | `[27.71730525, 42.99157678]` | `28963` | `[27.717263, 42.991569]` |
| (1, 5m] | 4.994 | `NAT-6871` | `[27.42922829, 43.31181347]` | `20586` | `[27.429252, 43.311772]` |
| (5, 15m] | 11.558 | `NAT-5877` | `[27.77293348, 43.20096465]` | `8526` | `[27.773072, 43.20094]` |
| (5, 15m] | 7.854 | `NAT-5875` | `[27.77743347, 43.20212901]` | `8531` | `[27.777523, 43.202102]` |
| (5, 15m] | 14.826 | `NAT-5580` | `[27.7868495, 43.12240298]` | `10524` | `[27.786694, 43.122333]` |
| (5, 15m] | 6.927 | `NAT-5544` | `[27.825649, 43.115084]` | `15353` | `[27.825733, 43.115073]` |
| (5, 15m] | 11.740 | `NAT-5566` | `[27.827388, 43.113098]` | `16123` | `[27.827507, 43.113158]` |
| (15, 50m] | 23.135 | `10127` | `[27.669076, 43.356312]` | `10128` | `[27.669069, 43.35652]` |
| (15, 50m] | 23.135 | `10128` | `[27.669069, 43.35652]` | `10127` | `[27.669076, 43.356312]` |
| (15, 50m] | 23.684 | `10132` | `[27.674161, 43.35665]` | `10133` | `[27.673878, 43.356595]` |
| (15, 50m] | 23.684 | `10133` | `[27.673878, 43.356595]` | `10132` | `[27.674161, 43.35665]` |
| (15, 50m] | 37.818 | `10524-DV` | `[27.728646, 43.281849]` | `10529` | `[27.728709, 43.282186]` |

### `data/hydrants.json` ? `field_reports.json`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `field_ba91e3ff` | `[27.847417, 43.250208]` | `field_ba91e3ff` | `[27.847417, 43.250208]` |
| [0, 0.1m] | 0.000 | `field_3326a776` | `[27.848389, 43.250078]` | `field_3326a776` | `[27.848389, 43.250078]` |
| [0, 0.1m] | 0.000 | `field_1a6e6d56` | `[27.848635, 43.250045]` | `field_1a6e6d56` | `[27.848635, 43.250045]` |
| [0, 0.1m] | 0.000 | `field_228b7518` | `[27.848088, 43.250588]` | `field_228b7518` | `[27.848088, 43.250588]` |
| [0, 0.1m] | 0.000 | `field_a641fc26` | `[27.875344, 43.239089]` | `field_a641fc26` | `[27.875344, 43.239089]` |
| (15, 50m] | 40.454 | `VIK-VARNA_IZTOK-0227` | `[27.931197, 43.211627]` | `field_a183a467` | `[27.930768, 43.211441]` |
| (15, 50m] | 49.303 | `VIK-VARNA_ZAPAD-0221` | `[27.879823, 43.239587]` | `field_9e4cbe81` | `[27.880378, 43.239405]` |
| (15, 50m] | 20.259 | `field_3326a776` | `[27.848389, 43.250078]` | `field_1a6e6d56` | `[27.848635, 43.250045]` |
| (15, 50m] | 20.259 | `field_1a6e6d56` | `[27.848635, 43.250045]` | `field_3326a776` | `[27.848389, 43.250078]` |

### `data/hydrants.json` ? `DEVNIa.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.037 | `10122-DV` | `[27.669648, 43.310904]` | `10122` | `[27.66964755, 43.31090396]` |
| [0, 0.1m] | 0.007 | `10123` | `[27.671834, 43.352484]` | `10123` | `[27.67183397, 43.35248394]` |
| [0, 0.1m] | 0.050 | `10124-DV` | `[27.665997, 43.353007]` | `10124` | `[27.6659971, 43.35300655]` |
| [0, 0.1m] | 0.054 | `10125` | `[27.667264, 43.353561]` | `10125` | `[27.66726392, 43.35356051]` |
| [0, 0.1m] | 0.043 | `10126` | `[27.674792, 43.352808]` | `10126` | `[27.67479238, 43.35280773]` |
| (5, 15m] | 11.543 | `NAT-5877` | `[27.77293348, 43.20096465]` | `8526` | `[27.77307179, 43.20093993]` |
| (5, 15m] | 7.874 | `NAT-5875` | `[27.77743347, 43.20212901]` | `8531` | `[27.7775234, 43.20210225]` |
| (15, 50m] | 23.139 | `10127` | `[27.669076, 43.356312]` | `10128` | `[27.66906913, 43.35652004]` |
| (15, 50m] | 23.097 | `10128` | `[27.669069, 43.35652]` | `10127` | `[27.66907595, 43.35631235]` |
| (15, 50m] | 23.686 | `10132` | `[27.674161, 43.35665]` | `10133` | `[27.67387798, 43.35659495]` |
| (15, 50m] | 23.707 | `10133` | `[27.673878, 43.356595]` | `10132` | `[27.67416132, 43.35664996]` |
| (15, 50m] | 37.809 | `10524-DV` | `[27.728646, 43.281849]` | `10529` | `[27.72870859, 43.28218596]` |

### `data/hydrants.json` ? `DOLNI_ChIFLIK.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.040 | `10122-DC` | `[27.856242, 43.081654]` | `10122` | `[27.85624245, 43.08165387]` |
| [0, 0.1m] | 0.044 | `10124-DC` | `[27.786065, 43.120827]` | `10124` | `[27.78606516, 43.12082738]` |
| [0, 0.1m] | 0.023 | `10523-DC` | `[27.787022, 43.122547]` | `10523` | `[27.78702205, 43.12254679]` |
| [0, 0.1m] | 0.016 | `10923-DC` | `[27.791287, 43.112649]` | `10923` | `[27.79128693, 43.11264887]` |
| [0, 0.1m] | 0.023 | `10924-DC` | `[27.790789, 43.113325]` | `10924` | `[27.79078929, 43.11332501]` |
| (1, 5m] | 2.140 | `NAT-17471` | `[27.827019, 43.11135]` | `16128` | `[27.82704191, 43.11134049]` |
| (1, 5m] | 4.734 | `24572` | `[27.76732, 42.951804]` | `24573` | `[27.76728068, 42.95177263]` |
| (1, 5m] | 4.668 | `24573` | `[27.767281, 42.951773]` | `24572` | `[27.76732037, 42.95180353]` |
| (1, 5m] | 3.507 | `NAT-6687` | `[27.71730525, 42.99157678]` | `28963` | `[27.71726331, 42.99156943]` |
| (5, 15m] | 14.804 | `NAT-5580` | `[27.7868495, 43.12240298]` | `10524` | `[27.78669436, 43.12233295]` |
| (5, 15m] | 6.905 | `NAT-5544` | `[27.825649, 43.115084]` | `15353` | `[27.82573273, 43.11507302]` |
| (5, 15m] | 11.708 | `NAT-5566` | `[27.827388, 43.113098]` | `16123` | `[27.82750689, 43.11315762]` |
| (5, 15m] | 6.424 | `NAT-17472` | `[27.827298, 43.112271]` | `16126` | `[27.82736558, 43.11224093]` |
| (5, 15m] | 13.108 | `NAT-5716` | `[27.83080703, 43.10776788]` | `16137` | `[27.83092475, 43.10768719]` |
| (15, 50m] | 35.687 | `10523-DC` | `[27.787022, 43.122547]` | `10524` | `[27.78669436, 43.12233295]` |
| (15, 50m] | 21.257 | `NAT-5580` | `[27.7868495, 43.12240298]` | `10523` | `[27.78702205, 43.12254679]` |
| (15, 50m] | 24.511 | `16136` | `[27.832049, 43.107418]` | `16141` | `[27.83175262, 43.10746008]` |
| (15, 50m] | 24.514 | `16141` | `[27.831753, 43.10746]` | `16136` | `[27.83204945, 43.10741805]` |
| (15, 50m] | 35.246 | `16148` | `[27.826107, 43.103509]` | `16149` | `[27.82650878, 43.10362909]` |

### `data/hydrants.json` ? `PROVADIIa.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.041 | `1-PR` | `[27.442813, 43.184807]` | `1` | `[27.44281254, 43.18480684]` |
| [0, 0.1m] | 0.037 | `10-PR` | `[27.439451, 43.168455]` | `10` | `[27.43945061, 43.16845518]` |
| [0, 0.1m] | 0.026 | `10117` | `[27.516909, 43.260491]` | `10117` | `[27.51690918, 43.26049081]` |
| [0, 0.1m] | 0.040 | `10118` | `[27.520139, 43.25852]` | `10118` | `[27.5201385, 43.25852001]` |
| [0, 0.1m] | 0.017 | `10119` | `[27.51562, 43.261304]` | `10119` | `[27.51562021, 43.26130399]` |
| (0.1, 1m] | 0.983 | `NAT-7080` | `[27.32790661, 43.192151]` | `6117` | `[27.32790418, 43.19215966]` |
| (0.1, 1m] | 0.601 | `NAT-6911` | `[27.43755799, 43.1856936]` | `74` | `[27.43755328, 43.18569777]` |
| (1, 5m] | 4.995 | `NAT-6871` | `[27.42922829, 43.31181347]` | `20586` | `[27.42925189, 43.31177196]` |
| (1, 5m] | 4.116 | `NAT-7043` | `[27.34155369, 43.12581188]` | `4573` | `[27.34150689, 43.12582615]` |
| (1, 5m] | 4.099 | `NAT-6917` | `[27.44783354, 43.15843673]` | `46` | `[27.44783033, 43.15847351]` |
| (1, 5m] | 3.867 | `NAT-6922` | `[27.32735944, 43.19470091]` | `6126` | `[27.32738715, 43.1946726]` |
| (1, 5m] | 4.484 | `NAT-6999` | `[27.45650244, 43.22871566]` | `6527` | `[27.4564877, 43.2286768]` |
| (5, 15m] | 12.117 | `NAT-7162` | `[27.43272197, 43.31547475]` | `12128` | `[27.43276129, 43.3153696]` |
| (5, 15m] | 10.302 | `12529` | `[27.555242, 43.40765]` | `9728` | `[27.55511707, 43.4076686]` |
| (5, 15m] | 11.866 | `1286-PR` | `[27.317118, 42.983018]` | `1287` | `[27.31714073, 42.98291259]` |
| (5, 15m] | 11.852 | `1287-PR` | `[27.317141, 42.982913]` | `1286` | `[27.31711755, 42.9830182]` |
| (5, 15m] | 13.409 | `1290-PR` | `[27.316847, 42.982062]` | `1291` | `[27.31685673, 42.98194162]` |
| (15, 50m] | 40.282 | `11-PR` | `[27.441218, 43.167488]` | `12` | `[27.44157288, 43.16723454]` |
| (15, 50m] | 34.587 | `11319` | `[27.432174, 43.318294]` | `11320` | `[27.43228052, 43.31799277]` |
| (15, 50m] | 34.546 | `11320` | `[27.432281, 43.317993]` | `11319` | `[27.43217369, 43.31829371]` |
| (15, 50m] | 40.279 | `12-PR` | `[27.441573, 43.167235]` | `11` | `[27.44121762, 43.16748804]` |
| (15, 50m] | 49.527 | `NAT-7162` | `[27.43272197, 43.31547475]` | `12129` | `[27.43220126, 43.31570895]` |

### `data/hydrants.json` ? `VARNA_IZTOK.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.029 | `VIK-VARNA_IZTOK-0001` | `[28.008344, 43.231426]` | `13` | `[28.00834384, 43.23142624]` |
| [0, 0.1m] | 0.026 | `VIK-VARNA_IZTOK-0002` | `[27.987026, 43.238606]` | `489` | `[27.98702568, 43.23860602]` |
| [0, 0.1m] | 0.035 | `VIK-VARNA_IZTOK-0003` | `[27.905298, 43.21472]` | `1266` | `[27.90529789, 43.2147203]` |
| [0, 0.1m] | 0.003 | `VIK-VARNA_IZTOK-0004` | `[27.915199, 43.173313]` | `1274` | `[27.91519903, 43.17331298]` |
| [0, 0.1m] | 0.045 | `VIK-VARNA_IZTOK-0005` | `[27.914171, 43.173783]` | `1276` | `[27.91417054, 43.17378323]` |
| (1, 5m] | 3.389 | `NAT-5629` | `[27.90726376, 43.17733043]` | `1314` | `[27.90729581, 43.17734999]` |
| (1, 5m] | 3.640 | `NAT-5301` | `[27.93521237, 43.21252779]` | `1455` | `[27.93524354, 43.21255136]` |
| (1, 5m] | 4.217 | `NAT-5482` | `[27.92539549, 43.20640882]` | `1472` | `[27.92538955, 43.20637114]` |
| (1, 5m] | 4.927 | `NAT-5453` | `[27.98075092, 43.24520403]` | `21517` | `[27.9807757, 43.24516357]` |
| (1, 5m] | 1.150 | `NAT-14086` | `[27.93721, 43.163133]` | `39916` | `[27.93719669, 43.16312944]` |
| (5, 15m] | 12.899 | `NAT-5503` | `[27.9350112, 43.2202817]` | `1280` | `[27.93485588, 43.22025626]` |
| (5, 15m] | 7.987 | `VIK-VARNA_IZTOK-0031` | `[27.921147, 43.210286]` | `703` | `[27.92113247, 43.21035704]` |
| (5, 15m] | 8.735 | `VIK-VARNA_IZTOK-0036` | `[27.910699, 43.203599]` | `738` | `[27.91078839, 43.20355512]` |
| (5, 15m] | 5.512 | `VIK-VARNA_IZTOK-0039` | `[28.010456, 43.232324]` | `979` | `[28.01039453, 43.23230276]` |
| (5, 15m] | 13.115 | `NAT-5433` | `[27.94101667, 43.2225475]` | `1385` | `[27.94109538, 43.22265056]` |
| (15, 50m] | 32.363 | `VIK-VARNA_IZTOK-0001` | `[28.008344, 43.231426]` | `898` | `[28.00870929, 43.23130821]` |
| (15, 50m] | 19.428 | `VIK-VARNA_IZTOK-0009` | `[27.910263, 43.217062]` | `1283` | `[27.91003888, 43.21712405]` |
| (15, 50m] | 49.574 | `VIK-VARNA_IZTOK-0012` | `[27.970367, 43.230216]` | `543` | `[27.97092766, 43.23039458]` |
| (15, 50m] | 30.276 | `VIK-VARNA_IZTOK-0017` | `[27.909967, 43.175531]` | `876` | `[27.90983066, 43.17527752]` |
| (15, 50m] | 43.773 | `VIK-VARNA_IZTOK-0017` | `[27.909967, 43.175531]` | `55918` | `[27.90943986, 43.1756158]` |

### `data/hydrants.json` ? `VARNA_ZAPAD.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.035 | `VIK-VARNA_IZTOK-0003` | `[27.905298, 43.21472]` | `1266` | `[27.90529789, 43.2147203]` |
| [0, 0.1m] | 0.012 | `VIK-VARNA_IZTOK-0022` | `[27.905266, 43.178666]` | `1316` | `[27.90526601, 43.17866589]` |
| [0, 0.1m] | 0.049 | `VIK-VARNA_IZTOK-0023` | `[27.903667, 43.179714]` | `1317` | `[27.90366721, 43.17971441]` |
| [0, 0.1m] | 0.022 | `VIK-VARNA_IZTOK-0024` | `[27.90445, 43.179202]` | `1318` | `[27.90444978, 43.17920188]` |
| [0, 0.1m] | 0.026 | `VIK-VARNA_IZTOK-0122` | `[27.906039, 43.226555]` | `8316` | `[27.90603873, 43.22655513]` |
| (0.1, 1m] | 0.745 | `NAT-5809` | `[27.81799812, 43.26253557]` | `57917` | `[27.81800046, 43.2625291]` |
| (0.1, 1m] | 0.847 | `NAT-6014` | `[27.86389876, 43.23659468]` | `1186` | `[27.86390908, 43.23659592]` |
| (0.1, 1m] | 0.595 | `NAT-6002` | `[27.85692062, 43.23632783]` | `1195` | `[27.85691558, 43.23633173]` |
| (1, 5m] | 4.442 | `NAT-14780` | `[27.905727, 43.209578]` | `65` | `[27.90567864, 43.20955919]` |
| (1, 5m] | 2.438 | `NAT-5428` | `[27.90398073, 43.21323935]` | `1265` | `[27.90399165, 43.21321892]` |
| (1, 5m] | 4.610 | `NAT-5943` | `[27.87086446, 43.23949227]` | `9916` | `[27.87088583, 43.2395307]` |
| (1, 5m] | 1.547 | `NAT-6057` | `[27.87905507, 43.24149495]` | `15516` | `[27.87906113, 43.24148176]` |
| (1, 5m] | 1.336 | `NAT-5638` | `[27.9015882, 43.17954847]` | `26316` | `[27.90157934, 43.17953834]` |
| (5, 15m] | 5.339 | `VIK-VARNA_ZAPAD-0004` | `[27.868643, 43.227307]` | `1178` | `[27.868629, 43.22726008]` |
| (5, 15m] | 7.890 | `NAT-5838` | `[27.82308726, 43.249664]` | `1288` | `[27.82314023, 43.24972355]` |
| (5, 15m] | 14.801 | `NAT-5953` | `[27.85136417, 43.25243249]` | `1294` | `[27.85143294, 43.25255582]` |
| (5, 15m] | 7.747 | `NAT-5445` | `[27.90255916, 43.21289725]` | `1328` | `[27.90246931, 43.21287348]` |
| (5, 15m] | 13.498 | `NAT-5939` | `[27.87123976, 43.23878883]` | `1334` | `[27.87120073, 43.23867082]` |
| (15, 50m] | 20.124 | `VIK-VARNA_IZTOK-0188` | `[27.905399, 43.210592]` | `644` | `[27.90515121, 43.21060367]` |
| (15, 50m] | 35.785 | `VIK-VARNA_IZTOK-0188` | `[27.905399, 43.210592]` | `759` | `[27.9053946, 43.2109138]` |
| (15, 50m] | 36.542 | `VIK-VARNA_IZTOK-0188` | `[27.905399, 43.210592]` | `761` | `[27.90576492, 43.21039999]` |
| (15, 50m] | 45.686 | `VIK-VARNA_IZTOK-0266` | `[27.904576, 43.153267]` | `1325` | `[27.90405374, 43.15311322]` |
| (15, 50m] | 40.710 | `VIK-VARNA_IZTOK-0268` | `[27.905038, 43.153411]` | `75516` | `[27.90457632, 43.15326749]` |

### `data/hydrants.json` ? `Първа РС сев от бул Левски  23.06.25г.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (0.1, 1m] | 0.877 | `301` | `[27.913148, 43.222114]` | `Belite Lilii 6 пх?` | `[27.913143, 43.222121]` |
| (0.1, 1m] | 0.895 | `VIK-VARNA_ZAPAD-0011` | `[27.888106, 43.24076]` | `пх вик` | `[27.88809794, 43.24076551]` |
| (0.1, 1m] | 0.558 | `VIK-VARNA_ZAPAD-0014` | `[27.888803, 43.238526]` | `пх вик` | `[27.88879949, 43.23853031]` |
| (0.1, 1m] | 0.778 | `VIK-VARNA_ZAPAD-0037` | `[27.893401, 43.216605]` | `Zhk Sveti Ivan Rilski 27 ПХ` | `[27.893401, 43.216612]` |
| (0.1, 1m] | 0.840 | `34-ZP` | `[27.884123, 43.233607]` | `Zhk Mladost 130 пх?` | `[27.884133, 43.233609]` |
| (1, 5m] | 2.830 | `VIK-VARNA_IZTOK-0012` | `[27.970367, 43.230216]` | `пх?` | `[27.970341, 43.230199]` |
| (1, 5m] | 3.376 | `VIK-VARNA_IZTOK-0044` | `[27.966717, 43.219184]` | `ПХ` | `[27.96667714, 43.21919281]` |
| (1, 5m] | 3.962 | `VIK-VARNA_IZTOK-0050` | `[27.942403, 43.222673]` | `ПХ ул. Prof. D-R Ivanka Nikola` | `[27.94238889, 43.22263889]` |
| (1, 5m] | 1.085 | `VIK-VARNA_IZTOK-0074` | `[27.971631, 43.227869]` | `пх до дом за стари хора Здравец` | `[27.97163889, 43.22786111]` |
| (1, 5m] | 4.727 | `VIK-VARNA_IZTOK-0075` | `[27.972269, 43.228591]` | `пх вик` | `[27.97225338, 43.22863196]` |
| (5, 15m] | 8.859 | `NAT-5503` | `[27.9350112, 43.2202817]` | `ПХ` | `[27.93492326, 43.22023437]` |
| (5, 15m] | 7.457 | `VIK-VARNA_IZTOK-0010` | `[27.930132, 43.224171]` | `Studentska ПХ` | `[27.930041, 43.224181]` |
| (5, 15m] | 11.940 | `VIK-VARNA_IZTOK-0025` | `[27.956327, 43.221139]` | `пх вик` | `[27.95624021, 43.22122577]` |
| (5, 15m] | 7.616 | `VIK-VARNA_IZTOK-0026` | `[27.977309, 43.223822]` | `пх вик` | `[27.97728006, 43.22388717]` |
| (5, 15m] | 9.071 | `VIK-VARNA_IZTOK-0027` | `[27.977227, 43.223959]` | `пх вик` | `[27.97728006, 43.22388717]` |
| (15, 50m] | 15.090 | `VIK-VARNA_IZTOK-0008` | `[27.920662, 43.224261]` | `Evlogi Georgiev 37 пх?` | `[27.920643, 43.224396]` |
| (15, 50m] | 22.846 | `VIK-VARNA_IZTOK-0010` | `[27.930132, 43.224171]` | `Studentska пх?` | `[27.929856, 43.224213]` |
| (15, 50m] | 44.965 | `VIK-VARNA_IZTOK-0010` | `[27.930132, 43.224171]` | `Mir 52 ПХ Нов` | `[27.930108, 43.224575]` |
| (15, 50m] | 21.028 | `VIK-VARNA_IZTOK-0011` | `[27.974074, 43.230815]` | `Trakata 550 пх?` | `[27.9743, 43.230908]` |
| (15, 50m] | 22.032 | `VIK-VARNA_IZTOK-0026` | `[27.977309, 43.223822]` | `пх вик` | `[27.97720077, 43.22400377]` |

### `hydrants_varna.json` ? `field_reports.json`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (15, 50m] | 40.454 | `0` | `[27.931197, 43.211627]` | `field_a183a467` | `[27.930768, 43.211441]` |
| (15, 50m] | 49.303 | `0` | `[27.879823, 43.239587]` | `field_9e4cbe81` | `[27.880378, 43.239405]` |

### `hydrants_varna.json` ? `DEVNIa.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.037 | `10122` | `[27.669648, 43.310904]` | `10122` | `[27.66964755, 43.31090396]` |
| [0, 0.1m] | 0.007 | `10123` | `[27.671834, 43.352484]` | `10123` | `[27.67183397, 43.35248394]` |
| [0, 0.1m] | 0.050 | `10124` | `[27.665997, 43.353007]` | `10124` | `[27.6659971, 43.35300655]` |
| [0, 0.1m] | 0.054 | `10125` | `[27.667264, 43.353561]` | `10125` | `[27.66726392, 43.35356051]` |
| [0, 0.1m] | 0.043 | `10126` | `[27.674792, 43.352808]` | `10126` | `[27.67479238, 43.35280773]` |
| (15, 50m] | 23.139 | `10127` | `[27.669076, 43.356312]` | `10128` | `[27.66906913, 43.35652004]` |
| (15, 50m] | 23.097 | `10128` | `[27.669069, 43.35652]` | `10127` | `[27.66907595, 43.35631235]` |
| (15, 50m] | 23.686 | `10132` | `[27.674161, 43.35665]` | `10133` | `[27.67387798, 43.35659495]` |
| (15, 50m] | 23.707 | `10133` | `[27.673878, 43.356595]` | `10132` | `[27.67416132, 43.35664996]` |
| (15, 50m] | 37.809 | `10524` | `[27.728646, 43.281849]` | `10529` | `[27.72870859, 43.28218596]` |

### `hydrants_varna.json` ? `DOLNI_ChIFLIK.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.040 | `10122` | `[27.856242, 43.081654]` | `10122` | `[27.85624245, 43.08165387]` |
| [0, 0.1m] | 0.044 | `10124` | `[27.786065, 43.120827]` | `10124` | `[27.78606516, 43.12082738]` |
| [0, 0.1m] | 0.023 | `10523` | `[27.787022, 43.122547]` | `10523` | `[27.78702205, 43.12254679]` |
| [0, 0.1m] | 0.030 | `10524` | `[27.786694, 43.122333]` | `10524` | `[27.78669436, 43.12233295]` |
| [0, 0.1m] | 0.016 | `10923` | `[27.791287, 43.112649]` | `10923` | `[27.79128693, 43.11264887]` |
| (1, 5m] | 4.734 | `24572` | `[27.76732, 42.951804]` | `24573` | `[27.76728068, 42.95177263]` |
| (1, 5m] | 4.668 | `24573` | `[27.767281, 42.951773]` | `24572` | `[27.76732037, 42.95180353]` |
| (5, 15m] | 12.528 | `18563` | `[27.72047, 42.994354]` | `8122` | `[27.72058379, 42.99442994]` |
| (5, 15m] | 12.545 | `8122` | `[27.720584, 42.99443]` | `18563` | `[27.72047009, 42.99435392]` |
| (15, 50m] | 35.687 | `10523` | `[27.787022, 43.122547]` | `10524` | `[27.78669436, 43.12233295]` |
| (15, 50m] | 35.693 | `10524` | `[27.786694, 43.122333]` | `10523` | `[27.78702205, 43.12254679]` |
| (15, 50m] | 24.511 | `16136` | `[27.832049, 43.107418]` | `16141` | `[27.83175262, 43.10746008]` |
| (15, 50m] | 24.514 | `16141` | `[27.831753, 43.10746]` | `16136` | `[27.83204945, 43.10741805]` |
| (15, 50m] | 35.246 | `16148` | `[27.826107, 43.103509]` | `16149` | `[27.82650878, 43.10362909]` |

### `hydrants_varna.json` ? `PROVADIIa.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.041 | `1` | `[27.442813, 43.184807]` | `1` | `[27.44281254, 43.18480684]` |
| [0, 0.1m] | 0.037 | `10` | `[27.439451, 43.168455]` | `10` | `[27.43945061, 43.16845518]` |
| [0, 0.1m] | 0.026 | `10117` | `[27.516909, 43.260491]` | `10117` | `[27.51690918, 43.26049081]` |
| [0, 0.1m] | 0.040 | `10118` | `[27.520139, 43.25852]` | `10118` | `[27.5201385, 43.25852001]` |
| [0, 0.1m] | 0.017 | `10119` | `[27.51562, 43.261304]` | `10119` | `[27.51562021, 43.26130399]` |
| (5, 15m] | 10.302 | `12529` | `[27.555242, 43.40765]` | `9728` | `[27.55511707, 43.4076686]` |
| (5, 15m] | 11.866 | `1286` | `[27.317118, 42.983018]` | `1287` | `[27.31714073, 42.98291259]` |
| (5, 15m] | 11.852 | `1287` | `[27.317141, 42.982913]` | `1286` | `[27.31711755, 42.9830182]` |
| (5, 15m] | 13.409 | `1290` | `[27.316847, 42.982062]` | `1291` | `[27.31685673, 42.98194162]` |
| (5, 15m] | 13.387 | `1291` | `[27.316857, 42.981942]` | `1290` | `[27.31684686, 42.98206216]` |
| (15, 50m] | 40.282 | `11` | `[27.441218, 43.167488]` | `12` | `[27.44157288, 43.16723454]` |
| (15, 50m] | 34.587 | `11319` | `[27.432174, 43.318294]` | `11320` | `[27.43228052, 43.31799277]` |
| (15, 50m] | 34.546 | `11320` | `[27.432281, 43.317993]` | `11319` | `[27.43217369, 43.31829371]` |
| (15, 50m] | 40.279 | `12` | `[27.441573, 43.167235]` | `11` | `[27.44121762, 43.16748804]` |
| (15, 50m] | 38.166 | `12128` | `[27.432761, 43.31537]` | `20569` | `[27.4323581, 43.31519145]` |

### `hydrants_varna.json` ? `VARNA_IZTOK.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.029 | `0` | `[28.008344, 43.231426]` | `13` | `[28.00834384, 43.23142624]` |
| [0, 0.1m] | 0.026 | `0` | `[27.987026, 43.238606]` | `489` | `[27.98702568, 43.23860602]` |
| [0, 0.1m] | 0.035 | `0` | `[27.905298, 43.21472]` | `1266` | `[27.90529789, 43.2147203]` |
| [0, 0.1m] | 0.003 | `0` | `[27.915199, 43.173313]` | `1274` | `[27.91519903, 43.17331298]` |
| [0, 0.1m] | 0.045 | `0` | `[27.914171, 43.173783]` | `1276` | `[27.91417054, 43.17378323]` |
| (1, 5m] | 2.143 | `130` | `[27.923232, 43.217937]` | `145` | `[27.92321523, 43.21792209]` |
| (1, 5m] | 2.143 | `130` | `[27.923232, 43.217937]` | `161` | `[27.92321523, 43.21792209]` |
| (1, 5m] | 2.128 | `131` | `[27.923215, 43.217922]` | `144` | `[27.92323207, 43.21793654]` |
| (1, 5m] | 2.128 | `131` | `[27.923215, 43.217922]` | `160` | `[27.92323207, 43.21793654]` |
| (1, 5m] | 2.143 | `147` | `[27.923232, 43.217937]` | `145` | `[27.92321523, 43.21792209]` |
| (5, 15m] | 7.987 | `0` | `[27.921147, 43.210286]` | `703` | `[27.92113247, 43.21035704]` |
| (5, 15m] | 8.735 | `0` | `[27.910699, 43.203599]` | `738` | `[27.91078839, 43.20355512]` |
| (5, 15m] | 5.512 | `0` | `[28.010456, 43.232324]` | `979` | `[28.01039453, 43.23230276]` |
| (5, 15m] | 12.346 | `0` | `[27.918257, 43.198071]` | `79116` | `[27.91828165, 43.19796144]` |
| (5, 15m] | 7.193 | `0` | `[27.983494, 43.247752]` | `254` | `[27.98346546, 43.24769074]` |
| (15, 50m] | 32.363 | `0` | `[28.008344, 43.231426]` | `898` | `[28.00870929, 43.23130821]` |
| (15, 50m] | 19.428 | `0` | `[27.910263, 43.217062]` | `1283` | `[27.91003888, 43.21712405]` |
| (15, 50m] | 49.574 | `0` | `[27.970367, 43.230216]` | `543` | `[27.97092766, 43.23039458]` |
| (15, 50m] | 30.276 | `0` | `[27.909967, 43.175531]` | `876` | `[27.90983066, 43.17527752]` |
| (15, 50m] | 43.773 | `0` | `[27.909967, 43.175531]` | `55918` | `[27.90943986, 43.1756158]` |

### `hydrants_varna.json` ? `VARNA_ZAPAD.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.035 | `0` | `[27.905298, 43.21472]` | `1266` | `[27.90529789, 43.2147203]` |
| [0, 0.1m] | 0.012 | `0` | `[27.905266, 43.178666]` | `1316` | `[27.90526601, 43.17866589]` |
| [0, 0.1m] | 0.049 | `0` | `[27.903667, 43.179714]` | `1317` | `[27.90366721, 43.17971441]` |
| [0, 0.1m] | 0.022 | `0` | `[27.90445, 43.179202]` | `1318` | `[27.90444978, 43.17920188]` |
| [0, 0.1m] | 0.026 | `0` | `[27.906039, 43.226555]` | `8316` | `[27.90603873, 43.22655513]` |
| (1, 5m] | 4.356 | `0` | `[27.900746, 43.182776]` | `453` | `[27.9007631, 43.18273886]` |
| (1, 5m] | 1.627 | `1026` | `[27.89407, 43.180468]` | `993` | `[27.89408939, 43.18046422]` |
| (1, 5m] | 1.632 | `1083` | `[27.894089, 43.180464]` | `955` | `[27.89406956, 43.18046782]` |
| (1, 5m] | 3.517 | `212` | `[27.872173, 43.234047]` | `39` | `[27.87214289, 43.23406978]` |
| (1, 5m] | 3.535 | `22` | `[27.872143, 43.23407]` | `212` | `[27.87217306, 43.23404696]` |
| (5, 15m] | 5.339 | `0` | `[27.868643, 43.227307]` | `1178` | `[27.868629, 43.22726008]` |
| (5, 15m] | 7.268 | `0` | `[27.890059, 43.236767]` | `563` | `[27.89007155, 43.23683172]` |
| (5, 15m] | 10.281 | `0` | `[27.895977, 43.179961]` | `42318` | `[27.89608951, 43.17991837]` |
| (5, 15m] | 10.279 | `0` | `[27.89609, 43.179918]` | `42317` | `[27.89597748, 43.17996059]` |
| (5, 15m] | 9.287 | `0` | `[27.895801, 43.225323]` | `1424` | `[27.89571547, 43.2252674]` |
| (15, 50m] | 20.124 | `0` | `[27.905399, 43.210592]` | `644` | `[27.90515121, 43.21060367]` |
| (15, 50m] | 35.785 | `0` | `[27.905399, 43.210592]` | `759` | `[27.9053946, 43.2109138]` |
| (15, 50m] | 36.542 | `0` | `[27.905399, 43.210592]` | `761` | `[27.90576492, 43.21039999]` |
| (15, 50m] | 45.686 | `0` | `[27.904576, 43.153267]` | `1325` | `[27.90405374, 43.15311322]` |
| (15, 50m] | 40.710 | `0` | `[27.905038, 43.153411]` | `75516` | `[27.90457632, 43.15326749]` |

### `hydrants_varna.json` ? `Първа РС сев от бул Левски  23.06.25г.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (0.1, 1m] | 0.877 | `301` | `[27.913148, 43.222114]` | `Belite Lilii 6 пх?` | `[27.913143, 43.222121]` |
| (0.1, 1m] | 0.895 | `0` | `[27.888106, 43.24076]` | `пх вик` | `[27.88809794, 43.24076551]` |
| (0.1, 1m] | 0.558 | `0` | `[27.888803, 43.238526]` | `пх вик` | `[27.88879949, 43.23853031]` |
| (0.1, 1m] | 0.778 | `0` | `[27.893401, 43.216605]` | `Zhk Sveti Ivan Rilski 27 ПХ` | `[27.893401, 43.216612]` |
| (0.1, 1m] | 0.840 | `34` | `[27.884123, 43.233607]` | `Zhk Mladost 130 пх?` | `[27.884133, 43.233609]` |
| (1, 5m] | 2.830 | `0` | `[27.970367, 43.230216]` | `пх?` | `[27.970341, 43.230199]` |
| (1, 5m] | 5.000 | `0` | `[27.941095, 43.222651]` | `ПХ` | `[27.94114158, 43.22262151]` |
| (1, 5m] | 3.376 | `0` | `[27.966717, 43.219184]` | `ПХ` | `[27.96667714, 43.21919281]` |
| (1, 5m] | 3.962 | `0` | `[27.942403, 43.222673]` | `ПХ ул. Prof. D-R Ivanka Nikola` | `[27.94238889, 43.22263889]` |
| (1, 5m] | 1.085 | `0` | `[27.971631, 43.227869]` | `пх до дом за стари хора Здравец` | `[27.97163889, 43.22786111]` |
| (5, 15m] | 5.957 | `0` | `[27.934856, 43.220256]` | `ПХ` | `[27.93492326, 43.22023437]` |
| (5, 15m] | 7.457 | `0` | `[27.930132, 43.224171]` | `Studentska ПХ` | `[27.930041, 43.224181]` |
| (5, 15m] | 11.940 | `0` | `[27.956327, 43.221139]` | `пх вик` | `[27.95624021, 43.22122577]` |
| (5, 15m] | 7.616 | `0` | `[27.977309, 43.223822]` | `пх вик` | `[27.97728006, 43.22388717]` |
| (5, 15m] | 9.071 | `0` | `[27.977227, 43.223959]` | `пх вик` | `[27.97728006, 43.22388717]` |
| (15, 50m] | 15.090 | `0` | `[27.920662, 43.224261]` | `Evlogi Georgiev 37 пх?` | `[27.920643, 43.224396]` |
| (15, 50m] | 22.846 | `0` | `[27.930132, 43.224171]` | `Studentska пх?` | `[27.929856, 43.224213]` |
| (15, 50m] | 44.965 | `0` | `[27.930132, 43.224171]` | `Mir 52 ПХ Нов` | `[27.930108, 43.224575]` |
| (15, 50m] | 21.028 | `0` | `[27.974074, 43.230815]` | `Trakata 550 пх?` | `[27.9743, 43.230908]` |
| (15, 50m] | 22.032 | `0` | `[27.977309, 43.223822]` | `пх вик` | `[27.97720077, 43.22400377]` |

### `field_reports.json` ? `VARNA_IZTOK.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (15, 50m] | 40.486 | `field_a183a467` | `[27.930768, 43.211441]` | `52316` | `[27.93119738, 43.2116271]` |

### `field_reports.json` ? `VARNA_ZAPAD.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (15, 50m] | 49.327 | `field_9e4cbe81` | `[27.880378, 43.239405]` | `48716` | `[27.87982285, 43.2395873]` |

### `field_reports.json` ? `Първа РС сев от бул Левски  23.06.25г.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (15, 50m] | 24.761 | `field_c1eff605` | `[27.889152, 43.227634]` | `Zhk Mladost Бриколаж` | `[27.888953, 43.227465]` |

### `geo_fire_hydrants.json` ? `geo_fire_hydrants.shp`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `12651` | `[23.31652692, 42.62799044]` | `1` | `[23.31652692, 42.62799044]` |
| [0, 0.1m] | 0.000 | `12652` | `[23.32916279, 42.70053201]` | `2` | `[23.32916279, 42.70053201]` |
| [0, 0.1m] | 0.000 | `12653` | `[23.32466204, 42.70456095]` | `3` | `[23.32466204, 42.70456095]` |
| [0, 0.1m] | 0.000 | `12654` | `[23.32519983, 42.70511777]` | `5` | `[23.32519983, 42.70511777]` |

### `geo_fire_hydrants.json` ? `geo_fire_hydrants.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `12651` | `[23.31652692, 42.62799044]` | `12651` | `[23.31652692, 42.62799044]` |
| [0, 0.1m] | 0.000 | `12652` | `[23.32916279, 42.70053201]` | `12652` | `[23.32916279, 42.70053201]` |
| [0, 0.1m] | 0.000 | `12653` | `[23.32466204, 42.70456095]` | `12653` | `[23.32466204, 42.70456095]` |
| [0, 0.1m] | 0.000 | `12654` | `[23.32519983, 42.70511777]` | `12654` | `[23.32519983, 42.70511777]` |

### `geo_fire_hydrants.shp` ? `geo_fire_hydrants.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `1` | `[23.31652692, 42.62799044]` | `12651` | `[23.31652692, 42.62799044]` |
| [0, 0.1m] | 0.000 | `2` | `[23.32916279, 42.70053201]` | `12652` | `[23.32916279, 42.70053201]` |
| [0, 0.1m] | 0.000 | `3` | `[23.32466204, 42.70456095]` | `12653` | `[23.32466204, 42.70456095]` |
| [0, 0.1m] | 0.000 | `5` | `[23.32519983, 42.70511777]` | `12654` | `[23.32519983, 42.70511777]` |

### `VARNA_IZTOK.kmz` ? `VARNA_ZAPAD.kmz`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `15` | `[27.90497448, 43.21249981]` | `15` | `[27.90497448, 43.21249981]` |
| [0, 0.1m] | 0.000 | `65` | `[27.90567864, 43.20955919]` | `65` | `[27.90567864, 43.20955919]` |
| [0, 0.1m] | 0.000 | `66` | `[27.9048837, 43.2094369]` | `66` | `[27.9048837, 43.2094369]` |
| [0, 0.1m] | 0.000 | `459` | `[27.90537247, 43.21692558]` | `459` | `[27.90537247, 43.21692558]` |
| [0, 0.1m] | 0.000 | `461` | `[27.90636446, 43.21526108]` | `461` | `[27.90636446, 43.21526108]` |
| (15, 50m] | 33.583 | `15` | `[27.90497448, 43.21249981]` | `1236` | `[27.90538571, 43.21246256]` |
| (15, 50m] | 24.999 | `461` | `[27.90636446, 43.21526108]` | `927` | `[27.90608961, 43.21536318]` |
| (15, 50m] | 39.728 | `644` | `[27.90515121, 43.21060367]` | `759` | `[27.9053946, 43.2109138]` |
| (15, 50m] | 20.085 | `644` | `[27.90515121, 43.21060367]` | `37517` | `[27.90539851, 43.21059181]` |
| (15, 50m] | 39.728 | `759` | `[27.9053946, 43.2109138]` | `644` | `[27.90515121, 43.21060367]` |

### `VARNA_IZTOK.kmz` ? `Първа РС сев от бул Левски  23.06.25г.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (0.1, 1m] | 0.833 | `292` | `[27.9131477, 43.22211434]` | `Belite Lilii 6 пх?` | `[27.913143, 43.222121]` |
| (1, 5m] | 4.870 | `205` | `[27.9081858, 43.21965914]` | `пх кръстовище на ул.Атанас Михов и ул.Кестен` | `[27.90812576, 43.21965717]` |
| (1, 5m] | 2.164 | `272` | `[27.95273136, 43.21741286]` | `D-R Stoyno Yordanov 6 п` | `[27.952713, 43.217427]` |
| (1, 5m] | 2.148 | `278` | `[27.93761316, 43.22241645]` | `пх` | `[27.937593, 43.222429]` |
| (1, 5m] | 3.929 | `280` | `[27.91859186, 43.2220964]` | `Nikola Kozlev 7 пх?` | `[27.918582, 43.222131]` |
| (1, 5m] | 4.138 | `286` | `[27.91012803, 43.22106185]` | `Lyulyak 1 пх?` | `[27.910131, 43.221099]` |
| (5, 15m] | 11.130 | `9` | `[27.9328092, 43.22243364]` | `Tsani Kalaydzhiev пх?` | `[27.932704, 43.222498]` |
| (5, 15m] | 6.169 | `10` | `[27.9490672, 43.22624077]` | `Zhk Briz пх?` | `[27.949038, 43.226292]` |
| (5, 15m] | 11.662 | `204` | `[27.90748977, 43.21925397]` | `Byala Mura 26 пх?` | `[27.907632, 43.21927]` |
| (5, 15m] | 10.237 | `266` | `[27.94040036, 43.21963697]` | `ПХ до бензиностанция ЕКО` | `[27.94036994, 43.21972633]` |
| (5, 15m] | 8.535 | `267` | `[27.94135765, 43.21950521]` | `ПХ` | `[27.94134729, 43.2195816]` |
| (15, 50m] | 44.149 | `17` | `[27.95552995, 43.21792765]` | `D-R Hristian Hranova 88` | `[27.955027, 43.217775]` |
| (15, 50m] | 26.175 | `17` | `[27.95552995, 43.21792765]` | `пх?` | `[27.955798, 43.218059]` |
| (15, 50m] | 33.797 | `204` | `[27.90748977, 43.21925397]` | `ПХ бул.Левски` | `[27.90733333, 43.21897222]` |
| (15, 50m] | 47.218 | `205` | `[27.9081858, 43.21965914]` | `пх Атанас Михов 3` | `[27.90830765, 43.21924389]` |
| (15, 50m] | 44.514 | `205` | `[27.9081858, 43.21965914]` | `Atanas Mihov 8 пх?` | `[27.908411, 43.219294]` |

### `VARNA_ZAPAD.kmz` ? `Първа РС сев от бул Левски  23.06.25г.kml`
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (0.1, 1m] | 0.836 | `51` | `[27.88412297, 43.23360722]` | `Zhk Mladost 130 пх?` | `[27.884133, 43.233609]` |
| (0.1, 1m] | 0.816 | `326` | `[27.90021027, 43.22974525]` | `пх?` | `[27.90020744, 43.22973821]` |
| (0.1, 1m] | 0.904 | `1244` | `[27.88810594, 43.24075985]` | `пх вик` | `[27.88809794, 43.24076551]` |
| (0.1, 1m] | 0.598 | `1247` | `[27.88880326, 43.23852569]` | `пх вик` | `[27.88879949, 43.23853031]` |
| (0.1, 1m] | 0.963 | `1248` | `[27.88844885, 43.23779835]` | `пх вик` | `[27.8884439, 43.23780622]` |
| (1, 5m] | 1.483 | `49` | `[27.88668044, 43.23172198]` | `пх вик` | `[27.8866773, 43.23173512]` |
| (1, 5m] | 4.320 | `52` | `[27.88384083, 43.23291191]` | `пх вик` | `[27.8838128, 43.23294496]` |
| (1, 5m] | 3.260 | `54` | `[27.88285881, 43.23116822]` | `пх вик` | `[27.88285297, 43.23119722]` |
| (1, 5m] | 1.100 | `55` | `[27.88262489, 43.23035596]` | `пх вик` | `[27.88261827, 43.2303646]` |
| (1, 5m] | 1.031 | `61` | `[27.88888398, 43.23033813]` | `Zhk Mladost 140 пх?` | `[27.888872, 43.230335]` |
| (5, 15m] | 5.477 | `48` | `[27.87975244, 43.23152701]` | `Bul. Republika пх?` | `[27.879715, 43.231486]` |
| (5, 15m] | 8.761 | `50` | `[27.88548664, 43.22884576]` | `Zhk Mladost ПХ` | `[27.885593, 43.22886]` |
| (5, 15m] | 7.876 | `57` | `[27.88827156, 43.23235841]` | `Zhk Mladost 134 пх?` | `[27.888211, 43.232303]` |
| (5, 15m] | 5.270 | `58` | `[27.88836232, 43.23178372]` | `Zhk Mladost пх` | `[27.888413, 43.231754]` |
| (5, 15m] | 9.662 | `59` | `[27.88775384, 43.22906507]` | `Zhk Mladost пх?` | `[27.887779, 43.22915]` |
| (15, 50m] | 29.307 | `49` | `[27.88668044, 43.23172198]` | `Zhk Mladost 141 пх?` | `[27.886343, 43.231627]` |
| (15, 50m] | 22.605 | `55` | `[27.88262489, 43.23035596]` | `пх?` | `[27.882611, 43.230559]` |
| (15, 50m] | 42.919 | `198` | `[27.90162352, 43.21828579]` | `Chinar 2 пх?` | `[27.901984, 43.218003]` |
| (15, 50m] | 35.223 | `200` | `[27.89923797, 43.21799116]` | `Atanas Hristov 6 пх?` | `[27.89889, 43.218181]` |
| (15, 50m] | 49.555 | `201` | `[27.89659078, 43.21615546]` | `ОМВ ПХ` | `[27.896109, 43.215881]` |

Intra-file pair counts within 50 m:
| File | [0,0.1m] | (0.1,1m] | (1,5m] | (5,15m] | (15,50m] |
|---|---:|---:|---:|---:|---:|
| `data/hydrants.json` | 609 | 1 | 16 | 74 | 1116 |
| `hydrants_varna.json` | 141 | 0 | 9 | 31 | 363 |
| `field_reports.json` | 0 | 0 | 0 | 0 | 1 |
| `DEVNIa.kmz` | 0 | 0 | 0 | 0 | 4 |
| `DOLNI_ChIFLIK.kmz` | 0 | 0 | 1 | 1 | 14 |
| `PROVADIIa.kmz` | 0 | 0 | 0 | 4 | 58 |
| `VARNA_IZTOK.kmz` | 84 | 0 | 5 | 15 | 164 |
| `VARNA_ZAPAD.kmz` | 7 | 0 | 3 | 11 | 105 |
| `Първа РС сев от бул Левски  23.06.25г.kml` | 0 | 0 | 0 | 10 | 122 |

Representative intra-file samples:
### `data/hydrants.json` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `VIK-VARNA_IZTOK-0003` | `[27.905298, 43.21472]` | `VIK-VARNA_ZAPAD-0017` | `[27.905298, 43.21472]` |
| [0, 0.1m] | 0.000 | `VIK-VARNA_IZTOK-0022` | `[27.905266, 43.178666]` | `VIK-VARNA_ZAPAD-0031` | `[27.905266, 43.178666]` |
| [0, 0.1m] | 0.000 | `VIK-VARNA_IZTOK-0023` | `[27.903667, 43.179714]` | `VIK-VARNA_ZAPAD-0032` | `[27.903667, 43.179714]` |
| [0, 0.1m] | 0.000 | `VIK-VARNA_IZTOK-0024` | `[27.90445, 43.179202]` | `VIK-VARNA_ZAPAD-0033` | `[27.90445, 43.179202]` |
| [0, 0.1m] | 0.000 | `VIK-VARNA_IZTOK-0122` | `[27.906039, 43.226555]` | `VIK-VARNA_ZAPAD-0098` | `[27.906039, 43.226555]` |
| (0.1, 1m] | 0.341 | `NAT-15311` | `[27.649486, 43.454709]` | `NAT-15312` | `[27.649482, 43.454708]` |
| (1, 5m] | 4.686 | `24572` | `[27.76732, 42.951804]` | `24573` | `[27.767281, 42.951773]` |
| (1, 5m] | 4.733 | `NAT-5319` | `[27.91497511, 43.20209194]` | `53-IZ` | `[27.914942, 43.202127]` |
| (1, 5m] | 4.733 | `NAT-5319` | `[27.91497511, 43.20209194]` | `77-IZ` | `[27.914942, 43.202127]` |
| (1, 5m] | 2.163 | `130` | `[27.923232, 43.217937]` | `131` | `[27.923215, 43.217922]` |
| (1, 5m] | 2.163 | `130` | `[27.923232, 43.217937]` | `148` | `[27.923215, 43.217922]` |
| (5, 15m] | 12.545 | `18563` | `[27.72047, 42.994354]` | `8122-DC` | `[27.720584, 42.99443]` |
| (5, 15m] | 10.316 | `12529` | `[27.555242, 43.40765]` | `9728` | `[27.555117, 43.407669]` |
| (5, 15m] | 11.824 | `1286-PR` | `[27.317118, 42.983018]` | `1287-PR` | `[27.317141, 42.982913]` |
| (5, 15m] | 13.368 | `1290-PR` | `[27.316847, 42.982062]` | `1291-PR` | `[27.316857, 42.981942]` |
| (5, 15m] | 8.949 | `19328` | `[27.435997, 43.11967]` | `3715` | `[27.435985, 43.11959]` |
| (15, 50m] | 23.135 | `10127` | `[27.669076, 43.356312]` | `10128` | `[27.669069, 43.35652]` |
| (15, 50m] | 23.684 | `10132` | `[27.674161, 43.35665]` | `10133` | `[27.673878, 43.356595]` |
| (15, 50m] | 22.258 | `10132` | `[27.674161, 43.35665]` | `NAT-6220` | `[27.67439169, 43.35675924]` |
| (15, 50m] | 45.369 | `10133` | `[27.673878, 43.356595]` | `NAT-6220` | `[27.67439169, 43.35675924]` |
| (15, 50m] | 37.818 | `10524-DV` | `[27.728646, 43.281849]` | `10529` | `[27.728709, 43.282186]` |

### `hydrants_varna.json` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `0` | `[27.905298, 43.21472]` | `0` | `[27.905298, 43.21472]` |
| [0, 0.1m] | 0.000 | `0` | `[27.905266, 43.178666]` | `0` | `[27.905266, 43.178666]` |
| [0, 0.1m] | 0.000 | `0` | `[27.903667, 43.179714]` | `0` | `[27.903667, 43.179714]` |
| [0, 0.1m] | 0.000 | `0` | `[27.90445, 43.179202]` | `0` | `[27.90445, 43.179202]` |
| [0, 0.1m] | 0.000 | `0` | `[27.906039, 43.226555]` | `0` | `[27.906039, 43.226555]` |
| (1, 5m] | 4.686 | `24572` | `[27.76732, 42.951804]` | `24573` | `[27.767281, 42.951773]` |
| (1, 5m] | 2.163 | `130` | `[27.923232, 43.217937]` | `131` | `[27.923215, 43.217922]` |
| (1, 5m] | 2.163 | `130` | `[27.923232, 43.217937]` | `148` | `[27.923215, 43.217922]` |
| (1, 5m] | 2.163 | `131` | `[27.923215, 43.217922]` | `147` | `[27.923232, 43.217937]` |
| (1, 5m] | 2.163 | `147` | `[27.923232, 43.217937]` | `148` | `[27.923215, 43.217922]` |
| (5, 15m] | 12.545 | `18563` | `[27.72047, 42.994354]` | `8122` | `[27.720584, 42.99443]` |
| (5, 15m] | 10.316 | `12529` | `[27.555242, 43.40765]` | `9728` | `[27.555117, 43.407669]` |
| (5, 15m] | 11.824 | `1286` | `[27.317118, 42.983018]` | `1287` | `[27.317141, 42.982913]` |
| (5, 15m] | 13.368 | `1290` | `[27.316847, 42.982062]` | `1291` | `[27.316857, 42.981942]` |
| (5, 15m] | 8.949 | `19328` | `[27.435997, 43.11967]` | `3715` | `[27.435985, 43.11959]` |
| (15, 50m] | 23.135 | `10127` | `[27.669076, 43.356312]` | `10128` | `[27.669069, 43.35652]` |
| (15, 50m] | 23.684 | `10132` | `[27.674161, 43.35665]` | `10133` | `[27.673878, 43.356595]` |
| (15, 50m] | 37.818 | `10524` | `[27.728646, 43.281849]` | `10529` | `[27.728709, 43.282186]` |
| (15, 50m] | 49.044 | `12125` | `[27.740571, 43.196822]` | `12126` | `[27.740671, 43.197257]` |
| (15, 50m] | 35.706 | `10523` | `[27.787022, 43.122547]` | `10524` | `[27.786694, 43.122333]` |

### `field_reports.json` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (15, 50m] | 20.259 | `field_3326a776` | `[27.848389, 43.250078]` | `field_1a6e6d56` | `[27.848635, 43.250045]` |

### `DEVNIa.kmz` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (15, 50m] | 37.776 | `10524` | `[27.72864648, 43.28184925]` | `10529` | `[27.72870859, 43.28218596]` |
| (15, 50m] | 23.100 | `10128` | `[27.66906913, 43.35652004]` | `10127` | `[27.66907595, 43.35631235]` |
| (15, 50m] | 23.710 | `10133` | `[27.67387798, 43.35659495]` | `10132` | `[27.67416132, 43.35664996]` |
| (15, 50m] | 48.994 | `12126` | `[27.7406711, 43.19725659]` | `12125` | `[27.74057127, 43.19682203]` |

### `DOLNI_ChIFLIK.kmz` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (1, 5m] | 4.716 | `24572` | `[27.76732037, 42.95180353]` | `24573` | `[27.76728068, 42.95177263]` |
| (5, 15m] | 12.528 | `8122` | `[27.72058379, 42.99442994]` | `18563` | `[27.72047009, 42.99435392]` |
| (15, 50m] | 23.687 | `8123` | `[27.72435958, 42.99676794]` | `22606` | `[27.7240861, 42.99669466]` |
| (15, 50m] | 35.675 | `10523` | `[27.78702205, 43.12254679]` | `10524` | `[27.78669436, 43.12233295]` |
| (15, 50m] | 35.240 | `16148` | `[27.82610691, 43.10350931]` | `16149` | `[27.82650878, 43.10362909]` |
| (15, 50m] | 24.546 | `16136` | `[27.83204945, 43.10741805]` | `16141` | `[27.83175262, 43.10746008]` |
| (15, 50m] | 42.698 | `16163` | `[27.83147023, 43.10630868]` | `16164` | `[27.83196858, 43.10618589]` |

### `PROVADIIa.kmz` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (5, 15m] | 11.893 | `1287` | `[27.31714073, 42.98291259]` | `1286` | `[27.31711755, 42.9830182]` |
| (5, 15m] | 13.428 | `1291` | `[27.31685673, 42.98194162]` | `1290` | `[27.31684686, 42.98206216]` |
| (5, 15m] | 8.967 | `3715` | `[27.43598546, 43.11958964]` | `19328` | `[27.43599693, 43.11966985]` |
| (5, 15m] | 10.277 | `9728` | `[27.55511707, 43.4076686]` | `12529` | `[27.55524168, 43.40764995]` |
| (15, 50m] | 40.307 | `11` | `[27.44121762, 43.16748804]` | `12` | `[27.44157288, 43.16723454]` |
| (15, 50m] | 47.117 | `14` | `[27.44269588, 43.16857772]` | `67` | `[27.44221447, 43.16834052]` |
| (15, 50m] | 32.010 | `16` | `[27.44335753, 43.16580985]` | `66` | `[27.44301115, 43.16567186]` |
| (15, 50m] | 48.723 | `27` | `[27.44249688, 43.16982102]` | `28` | `[27.44189615, 43.16982742]` |
| (15, 50m] | 32.224 | `48` | `[27.44644412, 43.16303721]` | `49` | `[27.4467744, 43.16319827]` |

### `VARNA_IZTOK.kmz` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `2` | `[27.91638533, 43.20009708]` | `107` | `[27.91638533, 43.20009708]` |
| [0, 0.1m] | 0.000 | `2` | `[27.91638533, 43.20009708]` | `130` | `[27.91638533, 43.20009708]` |
| [0, 0.1m] | 0.000 | `3` | `[27.9149419, 43.20212724]` | `69` | `[27.9149419, 43.20212724]` |
| [0, 0.1m] | 0.000 | `3` | `[27.9149419, 43.20212724]` | `92` | `[27.9149419, 43.20212724]` |
| [0, 0.1m] | 0.000 | `108` | `[27.91574691, 43.20016363]` | `84` | `[27.91574691, 43.20016363]` |
| (1, 5m] | 2.107 | `144` | `[27.92323207, 43.21793654]` | `145` | `[27.92321523, 43.21792209]` |
| (1, 5m] | 2.107 | `144` | `[27.92323207, 43.21793654]` | `161` | `[27.92321523, 43.21792209]` |
| (1, 5m] | 2.107 | `145` | `[27.92321523, 43.21792209]` | `160` | `[27.92323207, 43.21793654]` |
| (1, 5m] | 2.107 | `160` | `[27.92323207, 43.21793654]` | `161` | `[27.92321523, 43.21792209]` |
| (1, 5m] | 2.530 | `809` | `[27.92848288, 43.21181954]` | `810` | `[27.92850989, 43.21180814]` |
| (5, 15m] | 7.171 | `254` | `[27.98346546, 43.24769074]` | `12716` | `[27.98349449, 43.24775166]` |
| (5, 15m] | 5.119 | `277` | `[27.93087829, 43.22027609]` | `1147` | `[27.93086777, 43.2202307]` |
| (5, 15m] | 14.769 | `316` | `[27.90759683, 43.21210476]` | `317` | `[27.90750838, 43.21198863]` |
| (5, 15m] | 12.651 | `351` | `[27.91099234, 43.20450356]` | `1290` | `[27.91112324, 43.20444159]` |
| (5, 15m] | 14.800 | `352` | `[27.91243463, 43.20341616]` | `353` | `[27.91225227, 43.20340942]` |
| (15, 50m] | 36.465 | `3` | `[27.9149419, 43.20212724]` | `71` | `[27.91526198, 43.20235767]` |
| (15, 50m] | 36.465 | `3` | `[27.9149419, 43.20212724]` | `94` | `[27.91526198, 43.20235767]` |
| (15, 50m] | 36.465 | `3` | `[27.9149419, 43.20212724]` | `117` | `[27.91526198, 43.20235767]` |
| (15, 50m] | 32.385 | `13` | `[28.00834384, 43.23142624]` | `898` | `[28.00870929, 43.23130821]` |
| (15, 50m] | 33.583 | `15` | `[27.90497448, 43.21249981]` | `1236` | `[27.90538571, 43.21246256]` |

### `VARNA_ZAPAD.kmz` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| [0, 0.1m] | 0.000 | `189` | `[27.89192753, 43.18392669]` | `194` | `[27.89192753, 43.18392669]` |
| [0, 0.1m] | 0.000 | `190` | `[27.89329923, 43.18455958]` | `195` | `[27.89329923, 43.18455958]` |
| [0, 0.1m] | 0.000 | `191` | `[27.89082818, 43.17999415]` | `196` | `[27.89082818, 43.17999415]` |
| [0, 0.1m] | 0.000 | `192` | `[27.89331266, 43.17911107]` | `197` | `[27.89331266, 43.17911107]` |
| [0, 0.1m] | 0.000 | `1113` | `[27.86710639, 43.24096305]` | `1114` | `[27.86710639, 43.24096305]` |
| (1, 5m] | 3.524 | `39` | `[27.87214289, 43.23406978]` | `212` | `[27.87217306, 43.23404696]` |
| (1, 5m] | 4.329 | `453` | `[27.9007631, 43.18273886]` | `95116` | `[27.90074639, 43.18277584]` |
| (1, 5m] | 1.657 | `955` | `[27.89406956, 43.18046782]` | `993` | `[27.89408939, 43.18046422]` |
| (5, 15m] | 5.374 | `12` | `[27.86864309, 43.22730731]` | `1178` | `[27.868629, 43.22726008]` |
| (5, 15m] | 7.606 | `201` | `[27.89659078, 43.21615546]` | `202` | `[27.89654398, 43.21609617]` |
| (5, 15m] | 14.004 | `238` | `[27.88576917, 43.21657701]` | `1435` | `[27.88574204, 43.21670138]` |
| (5, 15m] | 7.283 | `563` | `[27.89007155, 43.23683172]` | `1420` | `[27.89005884, 43.23676688]` |
| (5, 15m] | 12.991 | `565` | `[27.87267191, 43.23559576]` | `566` | `[27.87262409, 43.23548425]` |
| (15, 50m] | 28.953 | `1` | `[27.87134549, 43.22975218]` | `64` | `[27.87099536, 43.22980432]` |
| (15, 50m] | 40.130 | `4` | `[27.8252618, 43.24865293]` | `5` | `[27.82499639, 43.24834819]` |
| (15, 50m] | 38.698 | `11` | `[27.90253092, 43.20687018]` | `45517` | `[27.90300407, 43.20682347]` |
| (15, 50m] | 33.583 | `15` | `[27.90497448, 43.21249981]` | `1236` | `[27.90538571, 43.21246256]` |
| (15, 50m] | 42.590 | `20` | `[27.85318272, 43.24625767]` | `1069` | `[27.85325061, 43.24663748]` |

### `Първа РС сев от бул Левски  23.06.25г.kml` intra-file
| Bucket | m | A id | A coord | B id | B coord |
|---|---:|---|---|---|---|
| (5, 15m] | 9.028 | `Сирма Войвода 9 пх` | `[27.94299657, 43.22333153]` | `Сирма Войвода 9 пх` | `[27.94292205, 43.22339189]` |
| (5, 15m] | 10.391 | `ПХ` | `[27.93118056, 43.22005293]` | `Vasil Petleshkov пх?` | `[27.931054, 43.220068]` |
| (5, 15m] | 10.059 | `пх Атанас Михов 3` | `[27.90830765, 43.21924389]` | `Atanas Mihov 8 пх?` | `[27.908411, 43.219294]` |
| (5, 15m] | 5.262 | `пх Атанас Михов 3` | `[27.90830765, 43.21924389]` | `ПХ` | `[27.90830859, 43.21919657]` |
| (5, 15m] | 5.229 | `Zhk Vasil Levski пх?` | `[27.915273, 43.2217]` | `Люляк 31 ПХ` | `[27.915271, 43.221653]` |
| (15, 50m] | 33.647 | `ПХ Кимекс ООД` | `[27.86343443, 43.21249832]` | `ПХ` | `[27.8632283, 43.21276099]` |
| (15, 50m] | 26.675 | `пх вик` | `[27.909026, 43.22304111]` | `ПХ` | `[27.90897222, 43.22327778]` |
| (15, 50m] | 15.406 | `Studentska ПХ` | `[27.930041, 43.224181]` | `Studentska пх?` | `[27.929856, 43.224213]` |
| (15, 50m] | 44.146 | `Studentska ПХ` | `[27.930041, 43.224181]` | `Mir 52 ПХ Нов` | `[27.930108, 43.224575]` |
| (15, 50m] | 43.175 | `ПХ` | `[27.89638889, 43.22394444]` | `Petko Staynov пх?` | `[27.895976, 43.223699]` |

## Section 4: Schema Coverage Matrix

| Origin | Field | Records | Populated | % | Distinct | Top 5 |
|---|---|---:|---:|---:|---:|---|
| `field_report` | `i` | 14 | 14 | 100.0 | 14 | field_ba91e3ff (1); field_3326a776 (1); field_1a6e6d56 (1); field_228b7518 (1); field_a641fc26 (1) |
| `field_report` | `c` | 14 | 14 | 100.0 | 14 | [27.847417, 43.250208] (1); [27.848389, 43.250078] (1); [27.848635, 43.250045] (1); [27.848088, 43.250588] (1); [27.875344, 43.239089] (1) |
| `field_report` | `a` | 14 | 11 | 78.6 | 11 | Пред бл. 408 вх 13 (1); Пред бл. 408 вх.17 (1); До игрището (1); Пред бл 17 вх 1 (1); На велоалеята (1) |
| `field_report` | `s` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `r` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `z` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `t` | 14 | 14 | 100.0 | 1 | надземен (14) |
| `field_report` | `st` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `o` | 14 | 14 | 100.0 | 1 | field_report (14) |
| `field_report` | `status` | 14 | 14 | 100.0 | 1 | verified (14) |
| `field_report` | `report_id` | 14 | 14 | 100.0 | 14 | ba91e3ff-f28a-4499-82ba-61d850a051a4 (1); 3326a776-516a-4e34-8e34-efd4773c5e80 (1); 1a6e6d56-f977-46b9-8a96-2adf698d133a (1); 228b7518-bf56-465b-bdda-2f8e2681e8cb (1); a641fc26-7c60-404d-9a51-844a0b9af3e7 (1) |
| `field_report` | `reported_at` | 14 | 14 | 100.0 | 14 | 2026-05-05T11:06:15Z (1); 2026-05-05T11:05:14Z (1); 2026-05-05T11:04:11Z (1); 2026-05-05T13:22:16Z (1); 2026-05-05T16:40:45Z (1) |
| `field_report` | `duplicate_distance_m` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `i_original` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `replaced_vik` | 14 | 0 | 0.0 | 0 |  |
| `field_report` | `replaced_vik_coord` | 14 | 0 | 0.0 | 0 |  |
| `national` | `i` | 2407 | 2407 | 100.0 | 2407 | NAT-5877 (1); NAT-5875 (1); NAT-5580 (1); NAT-5544 (1); NAT-5566 (1) |
| `national` | `c` | 2407 | 2407 | 100.0 | 2327 | [27.13751780009524, 43.00376530025505] (18); [27.317913200369684, 42.98299650014794] (16); [27.184332800441208, 43.002830600307625] (16); [27.255345699832567, 43.005941799821805] (9); [27.121508200273144, 42.985465399836926] (7) |
| `national` | `a` | 2407 | 55 | 2.3 | 23 | Водоем (18); Естествени водоизточници (14); не (2); 0 (2); на кръстовището (1) |
| `national` | `s` | 2407 | 0 | 0.0 | 0 |  |
| `national` | `r` | 2407 | 0 | 0.0 | 0 |  |
| `national` | `z` | 2407 | 2407 | 100.0 | 2407 | uin=5877; created=2021-06-08T08:50:26.365Z; ? (1); uin=5875; created=2021-06-08T08:50:26.365Z; ? (1); uin=5580; created=2021-06-08T08:50:26.365Z; ? (1); uin=5544; created=2021-06-08T08:50:26.365Z; ? (1); uin=5566; created=2021-06-08T08:50:26.365Z; ? (1) |
| `national` | `t` | 2407 | 2355 | 97.8 | 2 | underground (1185); ground (1170) |
| `national` | `st` | 2407 | 0 | 0.0 | 0 |  |
| `national` | `o` | 2407 | 2407 | 100.0 | 1 | national (2407) |
| `national` | `status` | 2407 | 1 | 0.0 | 1 | verified (1) |
| `national` | `report_id` | 2407 | 0 | 0.0 | 0 |  |
| `national` | `reported_at` | 2407 | 0 | 0.0 | 0 |  |
| `national` | `duplicate_distance_m` | 2407 | 271 | 11.3 | 271 | 11.5575 (1); 7.8538 (1); 14.8263 (1); 6.9271 (1); 11.7396 (1) |
| `national` | `i_original` | 2407 | 0 | 0.0 | 0 |  |
| `national` | `replaced_vik` | 2407 | 271 | 11.3 | 271 | 8526-DV (1); 8531-DV (1); 10524-DC (1); 15353-DC (1); 16123 (1) |
| `national` | `replaced_vik_coord` | 2407 | 271 | 11.3 | 271 | [27.773072, 43.20094] (1); [27.777523, 43.202102] (1); [27.786694, 43.122333] (1); [27.825733, 43.115073] (1); [27.827507, 43.113158] (1) |
| `vik` | `i` | 3661 | 3661 | 100.0 | 3661 | 10122-DV (1); 10123 (1); 10124-DV (1); 10125 (1); 10126 (1) |
| `vik` | `c` | 3661 | 3661 | 100.0 | 3549 | [27.91485, 43.202896] (3); [27.915262, 43.202358] (3); [27.916328, 43.200808] (3); [27.917166, 43.202156] (3); [27.916894, 43.202822] (3) |
| `vik` | `a` | 3661 | 557 | 15.2 | 352 | БУЛ. "ПРИМОРСКИ" (12); бул. 1-ви май (8); БУЛ. "ЦАР ОСВОБОДИТЕЛ" (8); ул. "Цар Борис III" (6); УЛ. "КЛИМЕНТ" (6) |
| `vik` | `s` | 3661 | 3661 | 100.0 | 5 | PROVADIIa (1278); VARNA_IZTOK (909); VARNA_ZAPAD (850); DOLNI_ChIFLIK (526); DEVNIa (98) |
| `vik` | `r` | 3661 | 1338 | 36.5 | 294 | 8 ПОДРАЙОН; ЧАСТ 2 (76); 6 ПОДРАЙОН (31); 9 ПОДРАЙОН; ИЗТОК-1 (31); ТОПОЛИТЕ; ЧАСТ 1 (29); С.О. Боровец-юг (27) |
| `vik` | `z` | 3661 | 219 | 6.0 | 74 | оглед (56); платно (18); не е открит (13); 10/41 (8); кл.5 - III зона (8) |
| `vik` | `t` | 3661 | 27 | 0.7 | 9 | 70/80 (16); ПКн (4); ПХ 70/80 (1); 70/80 надземен (1); DN 80 надземен (1) |
| `vik` | `st` | 3661 | 88 | 2.4 | 38 | заснето от Ботев (17); от Проект Левски (9); геодез. екзек. Ботев (7); геодез. засн. Ж (6); реални коорд. (5) |
| `vik` | `o` | 3661 | 3661 | 100.0 | 1 | vik (3661) |
| `vik` | `status` | 3661 | 10 | 0.3 | 2 | verified (8); reported (2) |
| `vik` | `report_id` | 3661 | 0 | 0.0 | 0 |  |
| `vik` | `reported_at` | 3661 | 0 | 0.0 | 0 |  |
| `vik` | `duplicate_distance_m` | 3661 | 0 | 0.0 | 0 |  |
| `vik` | `i_original` | 3661 | 1081 | 29.5 | 226 | 0 (644); 8522 (3); 8523 (3); 8525 (3); 8527 (3) |
| `vik` | `replaced_vik` | 3661 | 0 | 0.0 | 0 |  |
| `vik` | `replaced_vik_coord` | 3661 | 0 | 0.0 | 0 |  |

Normalization flags:
- Empty strings by field: `{'st': 5994, 'a': 5459, 'r': 4744, 't': 3686, 'z': 3456, 's': 2421}`.
- Nulls by field: `{}`.
- Mojibake marker samples in runtime strings: 0 `[]`.
- Cyrillic/Latin mixed samples: 0 `[]`.

## Section 5: Address Coverage Audit

| Origin | Records | `a` populated | % | Top values | 10 samples |
|---|---:|---:|---:|---|---|
| `field_report` | 14 | 11 | 78.6 | [["Пред бл. 408 вх 13", 1], ["Пред бл. 408 вх.17", 1], ["До игрището", 1], ["Пред бл 17 вх 1", 1], ["На велоалеята", 1], ["Срещу каса на easypay до дърво", 1], ["В парка до велоалеята", 1], ["До магазин бурлекс", 1], ["До входа на подземният паркинг", 1], ["С? | ["Пред бл. 408 вх 13", "Пред бл. 408 вх.17", "До игрището", "Пред бл 17 вх 1", "На велоалеята", "Срещу каса на easypay до дърво", "В парка до велоалеята", "До магазин бурлекс", "До входа на подземният паркинг", "Срещу магазин Тръпкови и diad clima, до трафопост 2313"] |
| `national` | 2407 | 55 | 2.3 | [["Водоем", 18], ["Естествени водоизточници", 14], ["не", 2], ["0", 2], ["на кръстовището", 1], ["На тротоара.", 1], ["На тротоара до спирка \"Звезда\".", 1], ["На тротоара пред адреса. Средно налягане. ", 1], ["На тротоара на улицата. Добро налягане. ", 1], ? | ["на кръстовището", "На тротоара.", "не", "На тротоара до спирка \"Звезда\".", "На тротоара пред адреса. Средно налягане. ", "На тротоара на улицата. Добро налягане. ", "На тротоара на адрес ул. Райко Даскалов 8. Средно налягане. ", "0", "не", "в градинката до Билла "] |
| `vik` | 3661 | 557 | 15.2 | [["БУЛ. \"ПРИМОРСКИ\"", 12], ["бул. 1-ви май", 8], ["БУЛ. \"ЦАР ОСВОБОДИТЕЛ\"", 8], ["ул. \"Цар Борис III\"", 6], ["УЛ. \"КЛИМЕНТ\"", 6], ["УЛ. \"ХР. КАБАКЧИЕВ\"", 6], ["УЛ. \"ХАН КРУМ\"", 6], ["УЛ. \"ВАРДАР\"", 6], ["УЛ. \"НИКУЛИЦЕЛ\"", 6], ["ул. \"Атанас Хр? | ["ул. ''Проф. Константин Ирече", "ул.\"Евлоги Георгиев\"", "бул. ''Цар Освободител''", "ул. \"Студентска\"", "бул. 1-ви май", "бул. 1-ви май", "бул. 1-ви май", "бул. 1-ви май", "бул. 1-ви май", "бул. 1-ви май"] |

KMZ ExtendedData parser: namespace-aware `ElementTree`, Placemark ? ExtendedData ? Data/value. Result: no `Data/value` ExtendedData fields in any of the five KMZ files; attributes are in description tables.
| KMZ | ExtendedData fields | Description fields | Address/type/status search hits |
|---|---|---|---|
| `DEVNIa.kmz` | no ExtendedData fields present | ["FID", "objectid", "rayon", "с. Баново FID", "с. Дръндар FID", "с. Езерово FID", "с. Изгрев FID", "с. Калиманци FID", "с. Николаевка FID", "с. Просечен FID"] | [] |
| `DOLNI_ChIFLIK.kmz` | no ExtendedData fields present | ["FID", "objectid", "rayon", "засн. Ботев FID", "не работи FID", "с. Булаир FID", "с. Венелин FID", "с. Голица FID", "с. Детелина FID", "с. Нова Шипка FID", "с. Ново Оряхово FID", "с. Рудник FID"] | [] |
| `PROVADIIa.kmz` | no ExtendedData fields present | ["FID", "objectid", "rayon", "Община Ветрино FID", "Община Дългопол FID", "Община Провадия FID", "с. Бояна FID", "с. Брестак FID", "с. Ветрино FID", "с. Момчилово FID", "с. Средно село FID"] | [] |
| `VARNA_IZTOK.kmz` | no ExtendedData fields present | ["0 FID", "22 FID", "23 FID", "24 FID", "26 FID", "27У FID", "29 FID", "33 FID", "45 FID", "70/80 FID", "FID", "adres", "id", "n_px", "objectid", "rajon", "rajon_1", "sastoqnie", "tip", "zabelegka", "т. 8 FID"] | [] |
| `VARNA_ZAPAD.kmz` | no ExtendedData fields present | ["0 FID", "1 FID", "10 FID", "11 FID", "12 FID", "125 FID", "128 FID", "129 FID", "13 FID", "132 FID", "133 FID", "14 FID", "142А FID", "15 FID", "152 FID", "153 FID", "16 FID", "166 FID", "167 FID", "17 FID", "18 FID", "2 FID", "21 FID", "23 FID", "24 FID", "25 FID", "30 FID", "31 FID", "35 FID", "36 FID", "38 FID", "39 FID", "40 FID", "41 FID", "42 FID", "44 FID", "47 FID", "5 FID", "50 FID", "51 FID", "55 FID", "? | [] |
### `DEVNIa.kmz` samples
ExtendedData evidence: no `kml:ExtendedData/kml:Data/kml:value` dictionaries found.
Description-table samples:
```json
[
  [
    "с. Калиманци",
    {
      "с. Калиманци FID": "0",
      "objectid": "10522",
      "rayon": "с. Калиманци"
    }
  ],
  [
    "с. Калиманци",
    {
      "с. Калиманци FID": "1",
      "objectid": "10523",
      "rayon": "с. Калиманци"
    }
  ],
  [
    "с. Калиманци",
    {
      "с. Калиманци FID": "2",
      "objectid": "10524",
      "rayon": "с. Калиманци"
    }
  ]
]
```
### `DOLNI_ChIFLIK.kmz` samples
ExtendedData evidence: no `kml:ExtendedData/kml:Data/kml:value` dictionaries found.
Description-table samples:
```json
[
  [
    "",
    {
      "FID": "0",
      "objectid": "8123",
      "rayon": ""
    }
  ],
  [
    "",
    {
      "FID": "1",
      "objectid": "13335",
      "rayon": ""
    }
  ],
  [
    "",
    {
      "FID": "2",
      "objectid": "9722",
      "rayon": ""
    }
  ]
]
```
### `PROVADIIa.kmz` samples
ExtendedData evidence: no `kml:ExtendedData/kml:Data/kml:value` dictionaries found.
Description-table samples:
```json
[
  [
    "",
    {
      "FID": "0",
      "objectid": "1",
      "rayon": ""
    }
  ],
  [
    "",
    {
      "FID": "1",
      "objectid": "2",
      "rayon": ""
    }
  ],
  [
    "",
    {
      "FID": "2",
      "objectid": "3",
      "rayon": ""
    }
  ]
]
```
### `VARNA_IZTOK.kmz` samples
ExtendedData evidence: no `kml:ExtendedData/kml:Data/kml:value` dictionaries found.
Description-table samples:
```json
[
  [
    "",
    {
      "FID": "0",
      "objectid": "2",
      "id": "68",
      "n_px": "",
      "adres": "УЛ. \"ВАРДАР\"",
      "rajon": "8 ПОДРАЙОН; ЧАСТ 2",
      "zabelegka": "",
      "tip": "",
      "sastoqnie": "",
      "rajon_1": ""
    }
  ],
  [
    "",
    {
      "FID": "1",
      "objectid": "3",
      "id": "101",
      "n_px": "",
      "adres": "",
      "rajon": "8 ПОДРАЙОН; ЧАСТ 2",
      "zabelegka": "",
      "tip": "",
      "sastoqnie": "",
      "rajon_1": ""
    }
  ],
  [
    "",
    {
      "FID": "2",
      "objectid": "8",
      "id": "865",
      "n_px": "",
      "adres": "",
      "rajon": "",
      "zabelegka": "",
      "tip": "",
      "sastoqnie": "",
      "rajon_1": ""
    }
  ]
]
```
### `VARNA_ZAPAD.kmz` samples
ExtendedData evidence: no `kml:ExtendedData/kml:Data/kml:value` dictionaries found.
Description-table samples:
```json
[
  [
    "",
    {
      "FID": "0",
      "objectid": "1",
      "id": "46",
      "n_px": "",
      "adres": "",
      "rajon": "Ж.К. МЛАДОСТ; 1 М.Р; ЧАСТ 0",
      "zabelegka": "",
      "tip": "",
      "sastoqnie": "",
      "rajon_1": ""
    }
  ],
  [
    "",
    {
      "FID": "1",
      "objectid": "4",
      "id": "0",
      "n_px": "",
      "adres": "",
      "rajon": "",
      "zabelegka": "",
      "tip": "",
      "sastoqnie": "",
      "rajon_1": ""
    }
  ],
  [
    "",
    {
      "FID": "2",
      "objectid": "5",
      "id": "0",
      "n_px": "",
      "adres": "",
      "rajon": "",
      "zabelegka": "",
      "tip": "",
      "sastoqnie": "",
      "rajon_1": ""
    }
  ]
]
```
NAT address-bearing fields:
| Source | Field | Populated | Distinct | 10 samples |
|---|---|---:|---:|---|
| `geo_fire_hydrants.json properties` | `name` | 17960 | 1700 | ["Улица Захари Зограф 14А, 1415 София, България", "Улица Екзарх Йосиф 46, 1000 София, България", "Булевард Сливница 174, 1202 София, България", "тест", "Булевард Сливница 239, 1202 София, България", "не", "Разград, преди паркинга на Вила дела роса, до ГРЗП", "с.Бисерци ул. Здравец 29", "с. Беловец вътре в Стопански двор ИнСтрой", "с. Беловец ул. Хан Аспарух? |
| `geo_fire_hydrants.json properties` | `address_id` | 5663 | 5663 | [2202, 2203, 2204, 1938, 2205, 32499, 35448, 38600, 38611, 38613] |
| `geo_fire_hydrants.json properties` | `notes` | 17956 | 15151 | ["тест", "не", "Разград, преди паркинга на Вила дела роса, до ГРЗП", "с.Бисерци ул. Здравец 29", "с. Беловец вътре в Стопански двор ИнСтрой", "с. Беловец ул. Хан Аспарух до трафопост", "с. Божурово до базата на Г. Костадинов", "с. Божурово ул. Урал 7", "Голям, син хидрант. От новите големи надземни хидранти по водния цикъл.", "с. Звънарци ул. Освобождение 4? |
| `geo_fire_hydrants.dbf` | `name` | 17958 | 1549 | ["????? ?????? ?????? 14?, 1415 ?????, ????????", "????? ?????? ????? 46, 1000 ?????, ????????", "???????? ???????? 174, 1202 ?????, ????????", "????", "???????? ???????? 239, 1202 ?????, ????????", "??", "???????, ????? ???????? ?? ???? ???? ????, ?? ????", "?.??????? ??. ??????? 29", "?. ??????? ????? ? ????????? ???? ???????", "?. ??????? ??. ??? ???????? |
| `geo_fire_hydrants.dbf` | `address_id` | 5663 | 5663 | [2202, 2203, 2204, 1938, 2205, 32499, 35448, 38600, 38611, 38613] |
| `geo_fire_hydrants.dbf` | `notes` | 17954 | 13537 | ["????", "??", "???????, ????? ???????? ?? ???? ???? ????, ?? ????", "?.??????? ??. ??????? 29", "?. ??????? ????? ? ????????? ???? ???????", "?. ??????? ??. ??? ??????? ?? ?????????", "?. ???????? ?? ?????? ?? ?. ??????????", "?. ???????? ??. ???? 7", "?????, ??? ???????. ?? ?????? ?????? ???????? ???????? ?? ?????? ?????.", "?. ???????? ??. ???????????? 4? |

## Section 6: Coordinate Field Audit

| Source | Valid | Format | Lon precision distribution | Lat precision distribution | CRS/raw status |
|---|---:|---|---|---|---|
| `data/hydrants.json` | 6082 | [lon,lat] | [(6, 3312), (12, 2158), (5, 330), (11, 220), (4, 33), (10, 26), (9, 2), (2, 1)] | [(6, 3313), (12, 2157), (5, 332), (11, 231), (4, 29), (10, 16), (3, 2), (9, 1)] | WGS84 app schema |
| `hydrants_varna.json` | 3934 | [lon,lat] | [(6, 3541), (5, 357), (4, 34), (3, 1), (2, 1)] | [(6, 3548), (5, 352), (4, 32), (3, 2)] | WGS84 by range |
| `field_reports.json` | 14 | [lon,lat] | [(6, 14)] | [(6, 14)] | WGS84 app schema |
| `geo_fire_hydrants.json` | 4 | raw [x,y] EPSG:3857; inverse+axis swap | [(12, 4)] | [(12, 3), (11, 1)] | declared EPSG:3857 |
| `geo_fire_hydrants.shp` | 4 | Point x/y EPSG:3857; inverse+axis swap | [(12, 4)] | [(12, 4)] | geo_fire_hydrants.prj EPSG:3857 |
| `geo_fire_hydrants.kml` | 4 | KML text lat,lon empirically | [(12, 4)] | [(12, 4)] | KML header only |
| `DEVNIa.kmz` | 100 | KML lon,lat,alt | [(12, 88), (11, 12)] | [(12, 91), (11, 8), (10, 1)] | WGS84 KML/range |
| `DOLNI_ChIFLIK.kmz` | 541 | KML lon,lat,alt | [(12, 477), (11, 61), (10, 3)] | [(12, 488), (11, 48), (10, 5)] | WGS84 KML/range |
| `PROVADIIa.kmz` | 1320 | KML lon,lat,alt | [(12, 1201), (11, 105), (10, 12), (9, 2)] | [(12, 1192), (11, 115), (10, 11), (9, 1), (8, 1)] | WGS84 KML/range |
| `VARNA_IZTOK.kmz` | 959 | KML lon,lat,alt | [(12, 854), (11, 99), (10, 5), (9, 1)] | [(12, 856), (11, 91), (10, 12)] | WGS84 KML/range |
| `VARNA_ZAPAD.kmz` | 1014 | KML lon,lat,alt | [(12, 922), (11, 86), (10, 6)] | [(12, 909), (11, 96), (10, 6), (9, 2), (8, 1)] | WGS84 KML/range |
| `Първа РС сев от бул Левски  23.06.25г.kml` | 654 | KML lon,lat,alt | [(12, 363), (6, 227), (5, 27), (11, 23), (10, 5), (3, 5), (4, 4)] | [(12, 363), (6, 224), (11, 27), (5, 25), (4, 11), (3, 2), (10, 1), (2, 1)] | WGS84 KML/range |

NAT CRS empirical check:
| Check | Result |
|---|---|
| Declared raw sample | `[4745326.1888, 2670342.3607]`, CRS `{'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:EPSG::3857'}}` |
| Normal EPSG:3857 inverse | lon `42.627990`, lat `23.316527` => outside Bulgaria |
| Inverse + axis swap | lon `23.316527`, lat `42.627990` => matches `Улица Захари Зограф 14А, 1415 София, България` |
| KML first coordinate | `42.62799043508328,23.316526916953066`; interpreted as lat,lon gives same point |

## Section 7: Pipeline Trace

| Path | Observed role | Evidence | Status |
|---|---|---|---|
| `extract_hydrants.py` | old extraction | finds `<script id="hydrantData">`, writes `data/hydrants.json` | historical |
| `index.html` | current runtime loader | `fetch('data/hydrants.json')`; `HYDRANTS_BY_ID` map | active |
| `field_reports.json` | canonical field report state | 14 `field_report` records | active |
| `audit/apply_field_reports.py` | old scripted ingest | writes `field_reports.json` and old embedded `index.html` JSON | stale/untracked |
| `docs/audits/issue_ingest_plan_20260508.md` | recent ingest evidence | states current target is `data/hydrants.json`; flags stale script | evidence |
| `index.html` polling | runtime report merge | `applyReports`, `new_hydrant`, `wrong_location`, `HYDRANTS_BY_ID` | in-memory only |

## Section 8: Schema Extensibility Assessment

| Future need | Current fit | Options/trade-offs, descriptive only |
|---|---|---|
| `operational_status` | Flat field fits compact JSON | Must not collide with visual `status` or raw `st`. |
| `last_inspection_date` | Flat ISO date fits | Captures latest state only unless paired with history. |
| Nested report history | Not currently modeled | Array per record keeps context local but grows first load; separate ledger is leaner but needs joins. |
| ID stability after dedup | Not handled | Aliases/mapping/merged IDs are possible patterns; current schema has none. |
| Comparable systems | Asset registry + event ledger | Assets keep stable hydrants; events store reports/inspections/status changes. |
No recommendation is made here.

## Section 9: Address Search Feasibility

| Approach | Preconditions | Depends on Section 5 | Trade-offs |
|---|---|---|---|
| Local fuzzy text search | populated normalized address field | strong if NAT/enriched `a` is canonical; weak for VIK empties | offline/static, needs Cyrillic normalization |
| Forward geocode query ? coords ? nearest | Nominatim reachable and scoped | works when addresses absent | network/rate-limit/ambiguity handling |
| Hybrid | local index plus geocode fallback | depends on per-origin coverage | broader but more branching |
| Street index from source fields | reliable street/name fields | NAT `name` helps; KMZ lacks explicit address ExtendedData | fast if normalized |

## Section 10: Identified Risks and Gaps

- No explicit runtime schema version.
- `status` / `st` / future `operational_status` semantics can collide.
- NAT CRS axis issue must be preserved in future imports.
- VIK source attributes require HTML-description parsing.
- Source archives are untracked and lack repo provenance.
- Stale untracked ingest script targets old architecture.
- Polling ID format mismatch remains full UUID vs `field_<8chars>`.
- Nested history in main array threatens first-load size.

## Section 11: Open Questions

- Which ID is authoritative after dedup?
- Should old IDs remain aliases after merges?
- Is NAT `name` acceptable as address data or provenance only?
- Should VIK HTML-description fields be normalized into runtime data?
- Where should report history live under the 2 MB cap?
- Should untracked source archives be committed or documented as acquisition steps?
- What is the policy for source vs volunteer type/status conflicts?
