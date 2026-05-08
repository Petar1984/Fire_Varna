# Data Audit and Target Schema Recommendation - 2026-05-08

## Protocol Preamble

Request scope: empirical data audit and target schema recommendation only, per Petar's 2026-05-08 request. Out of scope: cleanup execution, data edits, UI edits, reverse geocoding, display redesign, submission-flow updates, Worker source extraction, moderation implementation, and operational taxonomy implementation.

Deterministic inventory for this scoped audit:

```text
AGENTS.md
docs\activeContext.md
data\hydrants.json
field_reports.json
index.html
<missing> docs/audits/data_audit_and_target_schema_20260508.md
```

Files read in this session:

- `AGENTS.md`
- `docs/activeContext.md`
- `data/hydrants.json`
- `field_reports.json`
- `index.html`, targeted regions around hydrant data loading, report submission UI, report serialization, and polling merge logic

Negative findings matrix:

| Category / pattern in scope | Finding |
|---|---|
| Target audit file | `docs/audits/data_audit_and_target_schema_20260508.md` did not exist before this write. |
| Worker source | No `worker/` directory exists; live Worker remains external. |
| Structured address fields | No `district`, `municipality`, `street`, or `street_no` fields found in `data/hydrants.json` or `field_reports.json`. |
| Legacy/current metadata fields requested for audit | No `s_v`, `last_reporter`, `last_inspection_date`, or `ВиК идент.` fields found in runtime or field-report JSON. |
| ID integrity | No duplicate `i` values; no missing or empty `i` values. |
| Coordinate validity | No missing, malformed, zero, NaN, or infinite `c` values. |
| Varna-area coordinate sanity | No records outside conservative Varna oblast bounding box `lon 26.5..28.5`, `lat 42.7..44.0`. |
| Mojibake scan | No matches in `data/hydrants.json`, `field_reports.json`, or `index.html` for `[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]` with UTF-8 decoding. |
| Replacement-question-mark text | `index.html` contains `?? ?????? ...` fallback text in the hydrant-data-load failure branch. This is not caught by the mojibake regex, but is still an encoding/content red flag. |

Declared metadata quoted and treated as authoritative unless contradicted by empirical file parsing:

> `Last updated: 2026-05-08 at commit 2d8b767`

> `data/hydrants.json: 968,365 bytes (6,082 records — 8 field reports ingested in commit 2dcab73)`

> `field_reports.json: 5,085 bytes (14 records)`

> `Status counts: 23 verified, 2 reported, 6,057 canonical (in repo; runtime can grow via polled new_hydrant reports)`

Current Git HEAD during this audit was `f959ec8`, so `activeContext.md` has a small metadata drift: its count and byte-size bullets are current, but the "Last updated" commit hash still says `2d8b767`.

Decision ledger:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Use empirical runtime count of 6,082 records | File parse + `activeContext.md` | `data/hydrants.json` parsed to 6,082 records and active context declares the same | Reversible only if data file changes | Existing project state |
| Keep Worker source external for this audit | Repo evidence | `AGENTS.md` says live Worker is canonical until commit 17; no `worker/` directory exists | Reversible by later Worker extraction | Existing approved project state |
| Use verbose ASCII canonical keys | Petar amendment | Petar explicitly prioritizes readability over payload size | Reversible by schema migration | Approved for recommendation |
| Keep parallel existence and operational status | Petar pre-decision | User request states parallel fields, not combined enum | Reversible by later schema migration | Approved for recommendation |
| Defer reverse geocoding | Petar pre-decision | User request says reverse geocoding missing addresses is out of scope | Reversible in future sprint | Approved for this audit |
| Defer ambiguous `70/80` and `ПК1` type mappings | Petar amendment | Values lack explicit position indicator | Reversible after Petar assigns values | Pending domain decision |

Approval-gate check: this document recommends future data and schema changes but does not perform them. Actual cleanup will touch the canonical dataset and therefore needs Petar approval before execution. Any later UI label change, Worker contract change, dependency introduction, or architecture change also remains gated.

Open questions are consolidated in Section 13.

## Methodology

Tools and queries:

- PowerShell `rg --files`, `Get-ChildItem`, `git status`, `git rev-parse`, and `git log` for deterministic inventory and repo state.
- Python 3.10 `json.loads(..., encoding='utf-8')` for full parsing of all 6,082 runtime records and all 14 field-report records.
- Python counters for schema coverage, origin distribution, value distributions, ID checks, field-report equality, and coordinate sanity.
- Haversine distance with radius `6371008.8m` for near-duplicate thresholds. Candidate pairs were pruned with a 50m local grid, then verified with Haversine.
- UTF-8 mojibake scan with:

```powershell
Select-String -Path <path> -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8
```

No sampling was used for statistics. Representative duplicate clusters in Section 3 are examples only; the counts are full-corpus counts.

## Section 1: Schema Inventory

`data/hydrants.json` parsed successfully as a JSON array of 6,082 objects.

| Field | Type(s) | Description | Overall population | Origin coverage, populated / origin | Empty semantics |
|---|---|---|---:|---|---|
| `a` | string | Address or free-text location description. VIK mostly street labels; national and field reports often prose. | 623 / 6082 = 10.24% | vik 557/3661; national 55/2407; field_report 11/14 | Present on every record; empty string means unknown/missing. |
| `c` | array | `[lon, lat]` WGS84 coordinates. | 6082 / 6082 = 100.00% | vik 3661/3661; national 2407/2407; field_report 14/14 | Always present and populated. |
| `duplicate_distance_m` | number | National ingest annotation: distance from a replaced VIK record. | 271 / 6082 = 4.46% | vik 0/3661; national 271/2407; field_report 0/14 | Absent when not a national replacement annotation. |
| `i` | string | Runtime ID. Currently heterogeneous: numeric, suffixed numeric, `VIK-*`, `NAT-*`, and `field_*`. | 6082 / 6082 = 100.00% | vik 3661/3661; national 2407/2407; field_report 14/14 | Always present and populated. |
| `i_original` | string | Original VIK ID before suffix/namespacing during import. | 1081 / 6082 = 17.77% | vik 1081/3661; national 0/2407; field_report 0/14 | Absent except where import preserved old VIK ID. |
| `o` | string | Origin: `vik`, `national`, or `field_report`. | 6082 / 6082 = 100.00% | vik 3661/3661; national 2407/2407; field_report 14/14 | Always present and populated. |
| `r` | string | VIK район / подрайон / local region text. | 1338 / 6082 = 22.00% | vik 1338/3661; national 0/2407; field_report 0/14 | Present on every record; empty string means unknown/missing. |
| `replaced_vik` | string | National ingest annotation naming a VIK record replaced by national data. | 271 / 6082 = 4.46% | vik 0/3661; national 271/2407; field_report 0/14 | Absent when not a replacement annotation. |
| `replaced_vik_coord` | array | Original VIK coordinate for replacement audit trail. | 271 / 6082 = 4.46% | vik 0/3661; national 271/2407; field_report 0/14 | Absent when not a replacement annotation. |
| `report_id` | string | Full UUID for field-report-origin records. | 14 / 6082 = 0.23% | vik 0/3661; national 0/2407; field_report 14/14 | Absent outside field-report records. |
| `reported_at` | string | Field-report timestamp. Mixed `Z` and `+03:00` ISO-like forms. | 14 / 6082 = 0.23% | vik 0/3661; national 0/2407; field_report 14/14 | Absent outside field-report records. |
| `s` | string | Source dataset / VIK export region, not app status. Values include `VARNA_IZTOK`, `VARNA_ZAPAD`, `PROVADIIa`, `DOLNI_ChIFLIK`, `DEVNIa`. | 3661 / 6082 = 60.19% | vik 3661/3661; national 0/2407; field_report 0/14 | Present on every record; empty string means not applicable / missing. |
| `st` | string | Source raw note/status text, mostly VIK provenance notes. | 88 / 6082 = 1.45% | vik 88/3661; national 0/2407; field_report 0/14 | Present on every record; empty string means no note. |
| `status` | string | Current app-level visual state: `verified` or `reported`; absent means canonical/unverified. | 25 / 6082 = 0.41% | vik 10/3661; national 1/2407; field_report 14/14 | Absent means canonical/unverified. No empty strings observed. |
| `t` | string | Hydrant type/source type text. Currently non-normalized. | 2396 / 6082 = 39.39% | vik 27/3661; national 2355/2407; field_report 14/14 | Present on every record; empty string means unknown/missing. |
| `z` | string | Miscellaneous note/source metadata. National records use `uin=...; created=...; updated=...; geo_region=...`. | 2626 / 6082 = 43.18% | vik 219/3661; national 2407/2407; field_report 0/14 | Present on every record; empty string means no note. |

All discovered fields in `data/hydrants.json` are listed above. There are no nested objects.

## Section 2: Origin Distribution

| Origin `o` | Count | Share |
|---|---:|---:|
| `vik` | 3,661 | 60.19% |
| `national` | 2,407 | 39.58% |
| `field_report` | 14 | 0.23% |
| Other / missing | 0 | 0.00% |

### VIK Field Coverage

| Field | Populated / 3661 | Present | Empty string | Absent |
|---|---:|---:|---:|---:|
| `a` | 557 | 3661 | 3104 | 0 |
| `c` | 3661 | 3661 | 0 | 0 |
| `i` | 3661 | 3661 | 0 | 0 |
| `i_original` | 1081 | 1081 | 0 | 2580 |
| `o` | 3661 | 3661 | 0 | 0 |
| `r` | 1338 | 3661 | 2323 | 0 |
| `s` | 3661 | 3661 | 0 | 0 |
| `st` | 88 | 3661 | 3573 | 0 |
| `status` | 10 | 10 | 0 | 3651 |
| `t` | 27 | 3661 | 3634 | 0 |
| `z` | 219 | 3661 | 3442 | 0 |

### National Field Coverage

| Field | Populated / 2407 | Present | Empty string | Absent |
|---|---:|---:|---:|---:|
| `a` | 55 | 2407 | 2352 | 0 |
| `c` | 2407 | 2407 | 0 | 0 |
| `duplicate_distance_m` | 271 | 271 | 0 | 2136 |
| `i` | 2407 | 2407 | 0 | 0 |
| `o` | 2407 | 2407 | 0 | 0 |
| `r` | 0 | 2407 | 2407 | 0 |
| `replaced_vik` | 271 | 271 | 0 | 2136 |
| `replaced_vik_coord` | 271 | 271 | 0 | 2136 |
| `s` | 0 | 2407 | 2407 | 0 |
| `st` | 0 | 2407 | 2407 | 0 |
| `status` | 1 | 1 | 0 | 2406 |
| `t` | 2355 | 2407 | 52 | 0 |
| `z` | 2407 | 2407 | 0 | 0 |

### Field Report Field Coverage

| Field | Populated / 14 | Present | Empty string | Absent |
|---|---:|---:|---:|---:|
| `a` | 11 | 14 | 3 | 0 |
| `c` | 14 | 14 | 0 | 0 |
| `i` | 14 | 14 | 0 | 0 |
| `o` | 14 | 14 | 0 | 0 |
| `r` | 0 | 14 | 14 | 0 |
| `report_id` | 14 | 14 | 0 | 0 |
| `reported_at` | 14 | 14 | 0 | 0 |
| `s` | 0 | 14 | 14 | 0 |
| `st` | 0 | 14 | 14 | 0 |
| `status` | 14 | 14 | 0 | 0 |
| `t` | 14 | 14 | 0 | 0 |
| `z` | 0 | 14 | 14 | 0 |

## Section 3: Duplicate Detection

Duplicate methodology: exact coordinate checks round `lon` and `lat` independently to the requested decimals. Near-duplicate checks use Haversine distance and count both pair counts and connected clusters.

### 3A. ID Duplicates

No duplicate `i` values were found.

| Check | Result |
|---|---:|
| Missing `i` | 0 |
| Empty `i` | 0 |
| Duplicate ID clusters | 0 |
| Records in duplicate-ID clusters | 0 |

Current ID format distribution:

| Format | Count |
|---|---:|
| numeric VIK | 2,580 |
| numeric VIK with suffix | 432 |
| `VIK-*` | 644 |
| `NAT-*` | 2,407 |
| `field_*` | 14 |
| other VIK suffix form such as `83-IZ-1` | 5 |

### 3B. Exact Coordinate Duplicates at 6 Decimals

| Metric | Count |
|---|---:|
| Duplicate coordinate clusters | 109 |
| Records in duplicate clusters | 301 |
| Excess records beyond one per cluster | 192 |
| Pair count inside clusters | 609 |
| Max cluster size | 18 |
| Cross-origin clusters | 0 |
| Origin pair counts | national-national 475; vik-vik 134 |

Representative exact duplicate clusters with full record data:

```json
{"cluster":1,"key6":"27.899331,43.183590","key5":"27.89933,43.18359","notes":"national/national type conflict"}
{"a":"","c":[27.899331000062954,43.18359049972368],"duplicate_distance_m":7.7141,"i":"NAT-5531","o":"national","r":"","replaced_vik":"VIK-VARNA_ZAPAD-0072","replaced_vik_coord":[27.899421,43.183613],"s":"","st":"","t":"underground","z":"uin=5531; created=2021-06-08T08:50:26.365Z; updated=; geo_region=72"}
{"a":"","c":[27.899331000062954,43.18359049972368],"i":"NAT-5781","o":"national","r":"","s":"","st":"","t":"ground","z":"uin=5781; created=2021-06-08T08:50:26.365Z; updated=; geo_region=72"}
{"cluster":2,"key6":"27.902748,43.150517","key5":"27.90275,43.15052"}
{"a":"","c":[27.902748,43.150517],"i":"1152-IZ","i_original":"1152","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_IZTOK","st":"","t":"","z":"кл.67"}
{"a":"","c":[27.902748,43.150517],"i":"1152-ZP","i_original":"1152","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_ZAPAD","st":"","t":"","z":"кл.67"}
{"cluster":3,"key6":"27.903448,43.150924","key5":"27.90345,43.15092"}
{"a":"","c":[27.903448,43.150924],"i":"1156-IZ","i_original":"1156","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_IZTOK","st":"","t":"","z":"кл. 68"}
{"a":"","c":[27.903448,43.150924],"i":"1156-ZP","i_original":"1156","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_ZAPAD","st":"","t":"","z":"кл. 68"}
{"cluster":4,"key6":"27.903454,43.150234","key5":"27.90345,43.15023"}
{"a":"","c":[27.903454,43.150234],"i":"1153-IZ","i_original":"1153","o":"vik","r":"С.О.Боровец-юг","s":"VARNA_IZTOK","st":"","t":"","z":"кл.67"}
{"a":"","c":[27.903454,43.150234],"i":"1153-ZP","i_original":"1153","o":"vik","r":"С.О.Боровец-юг","s":"VARNA_ZAPAD","st":"","t":"","z":"кл.67"}
{"cluster":5,"key6":"27.903635,43.174759","key5":"27.90364,43.17476"}
{"a":"","c":[27.903635,43.174759],"i":"944-IZ","i_original":"944","o":"vik","r":"кв. Аспарухово 29А подрайон,","s":"VARNA_IZTOK","st":"","t":"","z":""}
{"a":"","c":[27.903635,43.174759],"i":"944-ZP","i_original":"944","o":"vik","r":"кв. Аспарухово 29А подрайон,","s":"VARNA_ZAPAD","st":"","t":"","z":""}
{"cluster":6,"key6":"27.903667,43.179714","key5":"27.90367,43.17971"}
{"a":"бул. 1-ви май","c":[27.903667,43.179714],"i":"VIK-VARNA_IZTOK-0023","i_original":"0","o":"vik","r":"29 подрайон","s":"VARNA_IZTOK","st":"заснето от Ботев","t":"","z":""}
{"a":"бул. 1-ви май","c":[27.903667,43.179714],"i":"VIK-VARNA_ZAPAD-0032","i_original":"0","o":"vik","r":"29 подрайон","s":"VARNA_ZAPAD","st":"заснето от Ботев","t":"","z":""}
{"cluster":7,"key6":"27.903837,43.201091","key5":"27.90384,43.20109"}
{"a":"УЛ. ДЕВНЯ","c":[27.903837,43.201091],"i":"813-IZ","i_original":"813","o":"vik","r":"7-МИ ПОДРАЙОН; ЧАСТ 2","s":"VARNA_IZTOK","st":"","t":"","z":""}
{"a":"УЛ. ДЕВНЯ","c":[27.903837,43.201091],"i":"813-ZP","i_original":"813","o":"vik","r":"7-МИ ПОДРАЙОН; ЧАСТ 2","s":"VARNA_ZAPAD","st":"","t":"","z":""}
{"cluster":8,"key6":"27.903954,43.151883","key5":"27.90395,43.15188"}
{"a":"","c":[27.903954,43.151883],"i":"1240-IZ","i_original":"1240","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_IZTOK","st":"","t":"","z":"кл. 62в"}
{"a":"","c":[27.903954,43.151883],"i":"1240-ZP","i_original":"1240","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_ZAPAD","st":"","t":"","z":"кл. 62в"}
{"cluster":9,"key6":"27.904052,43.207221","key5":"27.90405,43.20722","notes":"also one of Petar-deferred 70/80 records"}
{"a":"","c":[27.904052,43.207221],"i":"VIK-VARNA_IZTOK-0207","i_original":"0","o":"vik","r":"10 подрайон","s":"VARNA_IZTOK","st":"","t":"70/80","z":"10/41"}
{"a":"","c":[27.904052,43.207221],"i":"VIK-VARNA_ZAPAD-0205","i_original":"0","o":"vik","r":"10 подрайон","s":"VARNA_ZAPAD","st":"","t":"70/80","z":"10/41"}
{"cluster":10,"key6":"27.904054,43.153113","key5":"27.90405,43.15311"}
{"a":"","c":[27.904054,43.153113],"i":"1145-IZ","i_original":"1145","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_IZTOK","st":"","t":"","z":"кл. 72"}
{"a":"","c":[27.904054,43.153113],"i":"1145-ZP","i_original":"1145","o":"vik","r":"С.О. Боровец-юг","s":"VARNA_ZAPAD","st":"","t":"","z":"кл. 72"}
```

### 3C. Coordinate Near-Duplicates

| Threshold | Pair count | Connected clusters | Records in clusters | Excess records beyond one per cluster | Cross-origin clusters |
|---|---:|---:|---:|---:|---:|
| <= 5m | 626 | 119 | 324 | 205 | 2 |
| <= 10m | 661 | 152 | 391 | 239 | 4 |
| <= 25m | 959 | 385 | 895 | 510 | 137 |
| <= 50m | 1816 | 753 | 1920 | 1167 | 364 |

Pair origin counts by threshold:

| Threshold | national-national | national-vik | vik-vik | field_report-field_report | field_report-vik |
|---|---:|---:|---:|---:|---:|
| <= 5m | 481 | 3 | 142 | 0 | 0 |
| <= 10m | 501 | 6 | 154 | 0 | 0 |
| <= 25m | 584 | 155 | 219 | 1 | 0 |
| <= 50m | 813 | 526 | 474 | 1 | 2 |

Representative near-duplicate pairs with full record data:

```json
{"cluster":1,"pair_distance_m":4.427,"thresholds":"5m/10m/25m/50m","origins":"national-vik"}
{"a":"","c":[27.905727000394307,43.20957800019326],"duplicate_distance_m":4.4269,"i":"NAT-14780","o":"national","r":"","replaced_vik":"49-IZ","replaced_vik_coord":[27.905679,43.209559],"s":"","st":"","t":"underground","z":"uin=0301-14780; created=2023-06-29T16:36:16.194Z; updated=; geo_region=71"}
{"a":"ул.\"Дрин\"","c":[27.905679,43.209559],"i":"49-ZP","i_original":"49","o":"vik","r":"9 ПОДРАЙОН; ИЗТОК-1","s":"VARNA_ZAPAD","st":"","t":"","z":""}
{"cluster":2,"pair_distance_m":5.372,"thresholds":"10m/25m/50m","origins":"vik-national"}
{"a":"ул. ''Сергей Румянцев''","c":[27.89407,43.180468],"i":"1026","o":"vik","r":"27-ми подрайон; част 4","s":"VARNA_ZAPAD","st":"","t":"","z":""}
{"a":"","c":[27.894133117860324,43.18048269578934],"duplicate_distance_m":4.1374,"i":"NAT-5749","o":"national","r":"","replaced_vik":"1083","replaced_vik_coord":[27.894089,43.180464],"s":"","st":"","t":"ground","z":"uin=5749; created=2021-06-08T08:50:26.365Z; updated=; geo_region=72"}
{"cluster":3,"pair_distance_m":14.593,"thresholds":"25m/50m","origins":"national-vik"}
{"a":"","c":[28.0103893278715,43.23220208189509],"duplicate_distance_m":11.231,"i":"NAT-5408","o":"national","r":"","replaced_vik":"1068","replaced_vik_coord":[28.010395,43.232303],"s":"","st":"","t":"ground","z":"uin=5408; created=2021-06-08T08:50:26.365Z; updated=; geo_region=71"}
{"a":"","c":[28.010456,43.232324],"i":"VIK-VARNA_IZTOK-0039","i_original":"0","o":"vik","r":"","s":"VARNA_IZTOK","st":"","t":"","z":""}
{"cluster":4,"pair_distance_m":25.014,"thresholds":"50m","origins":"national-vik"}
{"a":"","c":[27.89278059999551,43.181700200050685],"i":"NAT-5539","o":"national","r":"","s":"","st":"","t":"ground","z":"uin=5539; created=2021-06-08T08:50:26.365Z; updated=; geo_region=72"}
{"a":"ул. ''Злетово''","c":[27.893055,43.181803],"i":"1093","o":"vik","r":"27 подрайон; част 4","s":"VARNA_ZAPAD","st":"","t":"","z":""}
{"cluster":5,"pair_distance_m":20.259,"thresholds":"25m/50m","origins":"field_report-field_report"}
{"a":"Пред бл. 408 вх.17","c":[27.848389,43.250078],"i":"field_3326a776","o":"field_report","r":"","report_id":"3326a776-516a-4e34-8e34-efd4773c5e80","reported_at":"2026-05-05T11:05:14Z","s":"","st":"","status":"verified","t":"надземен","z":""}
{"a":"","c":[27.848635,43.250045],"i":"field_1a6e6d56","o":"field_report","r":"","report_id":"1a6e6d56-f977-46b9-8a96-2adf698d133a","reported_at":"2026-05-05T11:04:11Z","s":"","st":"","status":"verified","t":"надземен","z":""}
{"cluster":6,"pair_distance_m":2.163,"thresholds":"5m/10m/25m/50m","origins":"vik-vik"}
{"a":"УЛ. \"НИКУЛИЦЕЛ\"","c":[27.923232,43.217937],"i":"130","o":"vik","r":"6 ПОДРАЙОН","s":"VARNA_IZTOK","st":"","t":"","z":"кл.5 - III зона"}
{"a":"УЛ. \"НИКУЛИЦЕЛ\"","c":[27.923215,43.217922],"i":"131","o":"vik","r":"6 ПОДРАЙОН","s":"VARNA_IZTOK","st":"","t":"","z":"кл.5 - III зона"}
{"cluster":7,"pair_distance_m":0.341,"thresholds":"5m/10m/25m/50m","origins":"national-national"}
{"a":"","c":[27.649485999858545,43.454708999682964],"i":"NAT-15311","o":"national","r":"","s":"","st":"","t":"underground","z":"uin=0307-15311; created=2023-10-13T08:14:30.351Z; updated=; geo_region=77"}
{"a":"Водоем","c":[27.649481999660583,43.45470800000832],"i":"NAT-15312","o":"national","r":"","s":"","st":"","t":"","z":"uin=0307-15312; created=2023-10-13T08:15:36.280Z; updated=; geo_region=77"}
{"cluster":8,"pair_distance_m":4.733,"thresholds":"5m/10m/25m/50m","origins":"national-vik"}
{"a":"","c":[27.91497510683698,43.202091935822196],"duplicate_distance_m":4.7332,"i":"NAT-5319","o":"national","r":"","replaced_vik":"101","replaced_vik_coord":[27.914942,43.202127],"s":"","st":"","t":"ground","z":"uin=5319; created=2021-06-08T08:50:26.365Z; updated=; geo_region=71"}
{"a":"","c":[27.914942,43.202127],"i":"53-IZ","i_original":"53","o":"vik","r":"8 ПОДРАЙОН; ЧАСТ 2","s":"VARNA_IZTOK","st":"","t":"","z":""}
{"cluster":9,"pair_distance_m":4.733,"thresholds":"5m/10m/25m/50m","origins":"national-vik"}
{"a":"","c":[27.91497510683698,43.202091935822196],"duplicate_distance_m":4.7332,"i":"NAT-5319","o":"national","r":"","replaced_vik":"101","replaced_vik_coord":[27.914942,43.202127],"s":"","st":"","t":"ground","z":"uin=5319; created=2021-06-08T08:50:26.365Z; updated=; geo_region=71"}
{"a":"","c":[27.914942,43.202127],"i":"77-IZ","i_original":"77","o":"vik","r":"8 ПОДРАЙОН; ЧАСТ 2","s":"VARNA_IZTOK","st":"","t":"","z":""}
{"cluster":10,"pair_distance_m":6.870,"thresholds":"10m/25m/50m","origins":"national-vik"}
{"a":"","c":[27.9202134608381,43.19849429966754],"duplicate_distance_m":6.8702,"i":"NAT-5269","o":"national","r":"","replaced_vik":"100","replaced_vik_coord":[27.920276,43.198536],"s":"","st":"","t":"underground","z":"uin=5269; created=2021-06-08T08:50:26.365Z; updated=; geo_region=71"}
{"a":"БУЛ. \"ПРИМОРСКИ\"","c":[27.920276,43.198536],"i":"124","o":"vik","r":"8 ПОДРАЙОН; ЧАСТ 2","s":"VARNA_IZTOK","st":"","t":"","z":""}
```

### 3D. Exact Coordinate Duplicates at 5 Decimals

Petar's target ID precision would collapse the same records as the 6-decimal exact duplicate check.

| Metric | Count |
|---|---:|
| Duplicate 5-dec coordinate clusters | 109 |
| Records in duplicate clusters | 301 |
| Excess records beyond one per cluster | 192 |
| Pair count inside clusters | 609 |
| Max cluster size | 18 |
| Cross-origin clusters | 0 |

The 10 representative clusters listed in Section 3B are also representative for 3D because the 5-decimal and 6-decimal duplicate cluster sets are identical in the current file.

## Section 4: Type Field Analysis

Current helper in `index.html`:

```js
function hydrantTypeLabel(typeValue) {
  if (typeValue == null) return '';
  const raw = String(typeValue).trim().toLowerCase();
  if (raw === 'underground' || raw.includes('подземен')) return 'Подземен';
  if (raw === 'ground' || raw.includes('надземен')) return 'Надземен';
  return '';
}
```

Empirical breakdown:

| Metric | Count |
|---|---:|
| `t` field present | 6,082 |
| `t` populated, non-empty | 2,396 |
| `t` empty string | 3,686 |
| `t` absent | 0 |
| Explicit Cyrillic `надземен` | 15 |
| Explicit Cyrillic `подземен` | 0 |
| Other distinct non-empty values | 10 distinct values, 2,381 records |

Distinct `t` values:

| Value | Count | Origin distribution |
|---|---:|---|
| empty string | 3,686 | vik 3,634; national 52 |
| `underground` | 1,185 | national 1,185 |
| `ground` | 1,170 | national 1,170 |
| `70/80` | 16 | vik 16 |
| `надземен` | 15 | vik 1; field_report 14 |
| `ПКн` | 4 | vik 4 |
| `ПХ 70/80` | 1 | vik 1 |
| `70/80 надземен` | 1 | vik 1 |
| `DN 80 надземен` | 1 | vik 1 |
| `ф 70/80 подземен` | 1 | vik 1 |
| `ПХ DN 80` | 1 | vik 1 |
| `ПК1` | 1 | vik 1 |

Helper-recognition note: the prompt's 0.3% figure appears to describe the visible Cyrillic share, not the current helper's actual recognition. Current code recognizes `ground`, `underground`, and strings containing `надземен` / `подземен`, so it recognizes 2,373 / 2,396 populated `t` values. The 23 populated values not recognized by the current helper are: `70/80` 16, `ПКн` 4, `ПХ 70/80` 1, `ПХ DN 80` 1, `ПК1` 1.

Normalization recommendation:

| Source value / pattern | Target `type` | Confidence | Rationale |
|---|---|---|---|
| `ground` | `надземен` | High | Petar confirmed mapping convention for this project. |
| `underground` | `подземен` | High | Petar confirmed mapping convention for this project. |
| Contains `надземен` | `надземен` | High | Explicit Bulgarian position indicator. |
| Contains `подземен` | `подземен` | High | Explicit Bulgarian position indicator. |
| `ПКн` | `надземен` | High | Petar domain input: suffix `н` is explicit indicator. |
| `ПХ 70/80` | `надземен` | Medium-high | Petar domain input: `ПХ` convention generally indicates surface hydrant here. |
| `ПХ DN 80` | `надземен` | Medium-high | Same convention as above. |
| `70/80` | Defer | Ambiguous | Size code without position indicator. |
| `ПК1` | Defer | Ambiguous | Type number without position indicator. |

Do not auto-map deferred values during cleanup. Section 13 lists all 17 records requiring Petar assignment.

## Section 5: Address Field Analysis

Coverage:

| Origin | `a` populated | `a` empty | Notes |
|---|---:|---:|---|
| vik | 557 / 3661 | 3104 | Mostly street/boulevard labels, often uppercase, truncated, or inconsistent quoting. |
| national | 55 / 2407 | 2352 | Mostly free-text descriptions such as sidewalk/location notes; some contain operational prose. |
| field_report | 11 / 14 | 3 | Volunteer free text near blocks, shops, entrances, park features. |
| Overall | 623 / 6082 | 5459 | 10.24% populated. |

Format observations:

- VIK address values are usually street-like: `ул.`, `УЛ.`, `бул.`, `БУЛ.`, neighborhood labels, or short landmarks.
- National address values are not structured addresses. Examples include `На тротоара.`, `на кръстовището`, `Водоем`, and descriptive notes.
- Field reports are field-worker prose, often useful for navigation even when not a postal address.
- No structured fragments exist in the runtime JSON: `district`, `municipality`, `street`, and `street_no` are absent from all records.

Structured-fragment conclusion: there are no structured fragments to merge with or compare against `a`; `a` is the only current address/location-description field. Cleanup should preserve non-empty `a` unchanged. Reverse geocoding empty addresses is out of scope for this cleanup sprint.

## Section 6: Status / Sub-status Analysis

Fields audited:

- `status`: current app-level visual state.
- `s`: source/export region, not semantic status.
- `s_v`: absent from all records.

`status` values:

| Value | Count | Meaning in current app |
|---|---:|---|
| absent | 6,057 | Canonical/unverified fallback |
| `verified` | 23 | Physically confirmed / rendered red |
| `reported` | 2 | Reported issue / rendered yellow |

`status` coverage by origin:

| Origin | `verified` | `reported` | absent |
|---|---:|---:|---:|
| vik | 8 | 2 | 3,651 |
| national | 1 | 0 | 2,406 |
| field_report | 14 | 0 | 0 |

`s` distinct values:

| `s` value | Count |
|---|---:|
| empty string | 2,421 |
| `PROVADIIa` | 1,278 |
| `VARNA_IZTOK` | 909 |
| `VARNA_ZAPAD` | 850 |
| `DOLNI_ChIFLIK` | 526 |
| `DEVNIa` | 98 |

`st` distinct values: 39 including empty. The non-empty values are mostly provenance notes, not a normalized sub-status: `заснето от Ботев` 17, `от Проект Левски` 9, `геодез. екзек. Ботев` 7, `геодез. засн. Ж` 6, `реални коорд.` 5, `геодез. засн.` 4, `заснето Ботев` 4, `геодезисти-екз.` 3, `екзекутив` 2, `ПХ 70/80` 2, `екз.` 2, plus 28 singleton notes.

Consistency check:

- `s_v` is absent, so no `s` / `s_v` correspondence exists to validate.
- `status` currently conflates app rendering/review state with existence confirmation. The target schema should separate existence `status`, `operational_status`, and `review_status`.
- All 14 field-report-origin records are `status: "verified"`; none carry `last_reporter`.
- 23 verified records have no `last_reporter` because that field does not exist. This is not a contradiction in the current schema, but it is a provenance limitation.

## Section 7: Metadata Field Coverage

Requested metadata fields:

| Field | Runtime coverage | Quality observation |
|---|---:|---|
| `last_reporter` | 0 / 6082 | Field absent. Reporter names are not preserved in runtime records. |
| `last_inspection_date` | 0 / 6082 | Field absent. No normalized inspection date exists. |
| `district` | 0 / 6082 | Field absent. |
| `municipality` | 0 / 6082 | Field absent. |
| `street` | 0 / 6082 | Field absent. |
| `street_no` | 0 / 6082 | Field absent. |
| `r` | 1338 / 6082 | VIK local region/free-text subdistrict, many spelling/case variants and truncations. |
| `ВиК идент.` | 0 / 6082 | Field absent. |

Other discovered metadata fields:

| Field | Coverage | Quality observation |
|---|---:|---|
| `i_original` | 1081 / 6082 | Useful migration/source reference for VIK records; absent elsewhere. |
| `duplicate_distance_m` | 271 / 6082 | Useful national-vs-VIK replacement audit annotation. |
| `replaced_vik` | 271 / 6082 | Useful source reference; should not remain a first-class runtime field after cleanup. |
| `replaced_vik_coord` | 271 / 6082 | Useful audit trail; move under `source_refs`. |
| `report_id` | 14 / 6082 | Field-report provenance; keep or move under `source_refs` depending on final schema. |
| `reported_at` | 14 / 6082 | Mixed timestamp offsets: 11 `Z` values and 3 `+03:00` values. Normalize only if cleanup changes timestamp semantics. |
| `z` | 2626 / 6082 | Mixed-purpose note field. National records encode structured-ish metadata as a semicolon string; VIK records contain short notes, standards, pipe sizes, or operational hints. |

Encoding: the mojibake regex returned zero matches for `data/hydrants.json`, `field_reports.json`, and `index.html`. Separate from mojibake, `index.html` contains replacement-question-mark Bulgarian fallback text in lines 1324-1326.

## Section 8: Data Quality Red Flags

Catalog:

| Red flag | Finding |
|---|---|
| Impossible coordinates | None found. All `c` arrays contain two finite numbers. |
| Coordinates outside broad Bulgaria sanity box | None outside `lon 20..30`, `lat 40..45`. |
| Coordinates outside conservative Varna oblast box | None outside `lon 26.5..28.5`, `lat 42.7..44.0`. |
| Zero coordinates | None. |
| Empty/malformed IDs | No missing or empty IDs. Five VIK IDs use extra suffix forms such as `83-IZ-1`; they are not malformed but add heterogeneity. |
| Duplicate IDs | None. |
| Exact duplicate coordinates | 109 clusters / 301 records / 192 excess records. |
| Near duplicate coordinates | 1,816 pairs within 50m; 753 connected clusters at 50m. |
| Type contradictions | Three exact-coordinate national clusters contain both `ground` and `underground` at the same coordinates. |
| Type ambiguity | 17 records require Petar domain assignment: 16 `70/80`, 1 `ПК1`. |
| Status provenance gap | 23 records are `verified`, but no `last_reporter` field exists. |
| Current `status` semantic overload | `verified` and `reported` are used for app rendering/review state, not a clean existence/operational model. |
| Address quality | 5,459 records have empty `a`; populated values are free text, not normalized addresses. Reverse geocoding is deferred. |
| Runtime/data-count doc drift | `AGENTS.md` still mentions 6,079 in places, while `activeContext.md` and runtime file show 6,082. |
| UI fallback text | `index.html` has `??` replacement fallback text for hydrant-load failure. |

## Section 9: field_reports.json Audit

`field_reports.json` parsed successfully as a JSON array of 14 objects.

Schema:

| Field | Type(s) | Overall population | Empty string | Absent | Notes |
|---|---|---:|---:|---:|---|
| `a` | string | 11 / 14 = 78.57% | 3 | 0 | Volunteer free-text address/location. |
| `c` | array | 14 / 14 = 100.00% | 0 | 0 | `[lon, lat]`. |
| `i` | string | 14 / 14 = 100.00% | 0 | 0 | `field_<8>` IDs. |
| `o` | string | 14 / 14 = 100.00% | 0 | 0 | Always `field_report`. |
| `r` | string | 0 / 14 = 0.00% | 14 | 0 | Empty compatibility field. |
| `report_id` | string | 14 / 14 = 100.00% | 0 | 0 | Full UUID. |
| `reported_at` | string | 14 / 14 = 100.00% | 0 | 0 | Mixed `Z` and `+03:00` offsets. |
| `s` | string | 0 / 14 = 0.00% | 14 | 0 | Empty compatibility field. |
| `st` | string | 0 / 14 = 0.00% | 14 | 0 | Empty compatibility field. |
| `status` | string | 14 / 14 = 100.00% | 0 | 0 | Always `verified`. |
| `t` | string | 14 / 14 = 100.00% | 0 | 0 | Always `надземен`. |
| `z` | string | 0 / 14 = 0.00% | 14 | 0 | Empty compatibility field. |

Comparison to `data/hydrants.json`:

- Every `field_reports.json` record exists in `data/hydrants.json` by identical `i`.
- All 14 matching records are byte-equivalent after JSON object comparison.
- `field_reports.json` is therefore not an independent source of current displayed state. It is either a stale archive/history file or an ingest artifact whose role needs a cleanup-sprint decision.

Naming inconsistencies:

- `field_reports.json` uses the same compact runtime fields (`i`, `c`, `a`, `t`, etc.) rather than a report-submission shape.
- It contains no reporter name, issue number, review state, or raw submission payload.

Sections 1-8 findings for this file:

- No duplicate IDs.
- No invalid coordinates.
- No mojibake regex hits.
- No impossible coordinates.
- Address coverage is much higher than runtime overall because these are volunteer-submitted records.
- The file cannot answer whether records are newly pending, approved, or historical; all are already `verified`.

## Section 10: Submission Flow Capture Inventory

Inspected `index.html` around the report flow (`showReportTypePicker`, `typeFieldsHTML`, `showReportModal`, `buildReportObject`, `buildReportYAML`, `labelsForType`, `submitReport`) and polling merge (`applyReports`).

### 10A. Fields Captured by Report Type

All report types capture:

- `report_id`
- `report_type`
- `timestamp`
- `reporter`
- `hydrant_ref` when tied to an existing hydrant
- `expected_coord` when tied to an existing hydrant
- `reported_coord` for manually placed `new_hydrant` or `wrong_location`
- `location_method`
- `app_version`

Per report type:

| Report type | UI path | Additional fields captured | Required fields beyond reporter |
|---|---|---|---|
| `new_hydrant` | Global `+`, then manual placement | `hydrant_type`, optional `description`, `reported_coord` | Manual location |
| `exists_confirmed` | Existing hydrant report picker | Optional `free_text` | None |
| `missing` | Existing hydrant report picker | `hydrant_type_at_location`, optional `terrain_description` | None beyond default `не знам` type value |
| `wrong_location` | Existing hydrant report picker, then manual placement | Required `description`, `reported_coord` | Description and manual location |
| `damaged` | Existing hydrant report picker | Required `damage_description`, `operational` radio (`да`, `не`, `не съм проверявал, само видимо`) | Damage description |

### 10B. Target-Schema Fields Captured vs Missing

Captured or derivable:

- `coords`: captured for `new_hydrant`; captured as corrected coordinate for `wrong_location`; existing hydrant coords are included as `expected_coord`.
- `type`: captured only for `new_hydrant`; captured as expected type only for `missing`; not captured for `exists_confirmed`.
- `status`: existence confirmation can be inferred from `exists_confirmed` and `wrong_location`; missing/damaged create reported/review state rather than existence status.
- `operational_status`: captured only for `damaged`, under field name `operational`.
- `review_status`: indirectly represented by GitHub labels and polling status, not submitted as a canonical record field.
- `address`: not captured as structured target field; `new_hydrant` has optional `description`, not `address`.
- `region`: not captured.
- `source_refs`: report ID and existing hydrant reference are captured in issue YAML, but current runtime merge does not preserve all of them for polled new hydrants.

Not captured where target schema would benefit:

- Type correction in `exists_confirmed`.
- Operational status in `exists_confirmed` and `new_hydrant`.
- Address/location-description as a named field for `new_hydrant`.
- Review/approval state as a first-class submission field.
- Reporter/provenance in runtime records beyond `report_id` / `reported_at`.

### 10C. Submission Gap Analysis

Future submission-flow sprint should add:

- Type prompt to `exists_confirmed` when current type is empty or uncertain.
- Operational check prompt to `exists_confirmed` and `new_hydrant` if Petar wants field workers to populate `operational_status`.
- A named `address` or `location_description` field for `new_hydrant` instead of overloading `description`.
- Worker/ingest mapping from submitted `operational` values to canonical `operational_status`.
- Explicit review-status handling so volunteer submissions do not directly imply canonical verification without moderation.

No submission UI changes are part of this cleanup audit.

## Section 11: Target Schema Recommendation

Petar pre-decisions carried into this section:

- ID derives from coordinates rounded to 5 decimal places.
- Type normalizes to `надземен` / `подземен`.
- Existence status and operational status are parallel fields.
- Existing 23 verified records keep verified existence; operational state remains unknown/absent until retested.
- Address values are preserved as-is; reverse geocoding is deferred.
- Canonical keys should be verbose ASCII for readability, even if file size grows.

### 11A. Canonical Schema

Recommended canonical record shape:

| Key | Required | Semantics |
|---|---|---|
| `id` | yes | Stable canonical ID derived from rounded coordinates after deduplication. |
| `coords` | yes | `[lon, lat]` WGS84 coordinates. |
| `origin` | yes | Dominant source for the retained record: `vik`, `national`, or `field_report`. |
| `address` | optional | Existing non-empty `a` preserved exactly. Omit when unknown. |
| `type` | optional | Normalized `надземен` or `подземен`. Omit when unknown/deferred. |
| `status` | optional | Existence status. Recommended values: `verified`, `unverified`, `missing`. For payload brevity, omit if canonical unverified is accepted as default. |
| `operational_status` | optional | Water-flow/working state. Recommended values: `works`, `not_working`, `not_tested`, or absent unknown. Final vocabulary needs Petar approval before implementation. |
| `review_status` | optional | Moderation/review state such as `reported` or `pending_review`; distinct from existence status. |
| `region` | optional | Former `r` value where non-empty. |
| `source_refs` | optional | Array/object preserving old IDs, origin-specific metadata, replacement annotations, and old coordinates. |
| `report_id` | optional | Field-report UUID when the record originates from a report. |
| `reported_at` | optional | Field-report timestamp. |

ID derivation rule:

```js
id = `coord_${lon.toFixed(5)}_${lat.toFixed(5)}`
```

Use current coordinate order `[lon, lat]`. Do not assign final coordinate IDs until exact 5-decimal collisions have been resolved; current data would otherwise collapse 301 records into 109 duplicate-ID clusters, dropping 192 excess records.

Empty-value semantics:

- Prefer absent optional fields over empty strings.
- Use explicit `status` / `review_status` only when they carry meaning.
- Use absent `operational_status` for unknown until Petar approves an explicit unknown value.
- Keep `coords` and `id` always present.

Worker compatibility note: current polling merge expects compact runtime-ish data from the Worker (`id`, `coords`, `report_type`, `hydrant_id`) and current app data uses compact keys. If Worker or frontend compatibility requires transitional mapping, implement an adapter. Do not let the current Worker contract dictate the canonical storage schema.

### 11B. Migration Mapping

| Current field | Target disposition | Rule |
|---|---|---|
| `i` | rename / preserve in `source_refs` | New `id` is coordinate-derived. Preserve old `i` under `source_refs.old_id`. |
| `c` | rename to `coords` | Preserve `[lon, lat]`; round only for ID, not necessarily stored coordinate precision. |
| `o` | rename to `origin` | Preserve value. |
| `a` | rename to `address` | Preserve non-empty string unchanged; omit if empty. |
| `t` | rename to `type` after normalization | Apply Section 4 rules; omit deferred/unknown values. |
| `status` | split semantics | `verified` maps to existence `status: "verified"`; `reported` maps to `review_status: "reported"` unless Petar decides otherwise. |
| `r` | rename to `region` | Preserve non-empty string unchanged; omit if empty. |
| `s` | move to `source_refs` | It is source/export region, not target status. |
| `st` | move to `source_refs` | Preserve non-empty source notes. |
| `z` | move to `source_refs` or `notes` | National `z` contains source metadata; VIK `z` contains miscellaneous notes. Preserve, but do not keep as ambiguous top-level key. |
| `i_original` | move to `source_refs` | Preserve as old/source ID. |
| `duplicate_distance_m` | move to `source_refs` | Preserve for audit trail. |
| `replaced_vik` | move to `source_refs` | Preserve replacement provenance. |
| `replaced_vik_coord` | move to `source_refs` | Preserve old coordinate for audit trail. |
| `report_id` | keep | Keep top-level for report-origin records or also mirror in `source_refs`. |
| `reported_at` | keep | Keep top-level for report-origin records. |

Existing 23 verified records:

- Map to existence `status: "verified"`.
- Do not set `operational_status` unless there is field-test evidence.
- Field-report records may keep `report_id` and `reported_at`; VIK/national verified records have no reporter/date provenance in current data.

### 11C. Source Priority Decision Tree for Duplicates

Recommended duplicate resolution order:

1. Field-verified `field_report` records win over unverified source records when they represent the same physical hydrant.
2. National records win over VIK records where there is a spatial collision/near collision, carrying Petar's prior decision that national records were field-verified by colleagues for this project.
3. For national records with `replaced_vik`, preserve the replaced VIK ID and coordinate in `source_refs`.
4. Within the same origin, keep the richest non-conflicting record: prefer populated `address`, normalized `type`, `status: verified`, and provenance fields.
5. If same-coordinate records conflict on normalized type, quarantine for Petar review rather than auto-dropping.
6. For exact 5-dec coordinate collisions, resolve before deriving final IDs.

### 11D. Records-to-Drop / Quarantine Recommendation

Do not directly delete in the cleanup script without producing a review artifact first.

Recommended categories:

- Auto-collapse exact duplicate coordinate clusters only when records are same-origin and non-conflicting after merging source references.
- Quarantine exact coordinate clusters with type conflicts, especially national clusters containing both `ground` and `underground`.
- Quarantine `70/80` and `ПК1` records until Petar assigns type.
- Quarantine impossible coordinates if they appear in future; none exist now.
- Preserve source metadata for any dropped duplicate in `source_refs` or a separate cleanup report so data is recoverable from Git history and the migration report.

### 11E. Schema Versioning Approach

Recommendation: do not add `schema_version` to every record in this cleanup sprint. The per-record payload cost is not worth it.

Preferred approach:

- Add a top-level dataset envelope with schema version only if the app is refactored to load an object rather than a bare array.
- If the app must keep loading a bare array for compatibility, document the schema version in `AGENTS.md` and the cleanup audit/commit message.
- During migration, support both compact and verbose records in app code only if needed for an atomic rollout. Otherwise update data and code in one carefully verified commit.

Backward compatibility:

- Existing app code expects `i`, `c`, `o`, `a`, `t`, `r`, `s`, `st`, `z`, and optional `status`.
- Moving to verbose keys requires an app adapter or coordinated frontend change. This is a real architecture/data contract change and must be approved before implementation.

## Section 12: Cleanup Execution Plan Preview

This is not the full execution plan.

Estimated commit count:

1. Add backup/snapshot and reproducible audit script/output scaffolding.
2. Normalize type values with Petar-approved deferred decisions.
3. Resolve exact duplicate coordinate clusters and preserve source references.
4. Introduce verbose schema and app adapter/update.
5. Verify runtime behavior and update docs.

Estimated effort: 6-10 focused hours for data migration plus verification, assuming Petar resolves the 17 deferred type records before execution.

Critical risk points:

- Coordinate-derived IDs are irreversible if old IDs are not preserved.
- Duplicate collapse can corrupt data if near duplicates are treated as exact physical matches.
- Type mapping mistakes affect emergency field interpretation.
- Verbose schema requires frontend compatibility work; data-only migration would break the current app.
- `status` migration can accidentally turn review reports into existence facts.

Backup strategy:

- Commit or copy a full pre-migration snapshot of `data/hydrants.json` and `field_reports.json` before any mutation.
- Generate a machine-readable migration report listing every old ID, new ID, coordinate, and source_refs merge.

Verification strategy:

- Per-commit JSON parse.
- Count assertions by origin/status/type.
- Coordinate validity assertions.
- Duplicate assertions after exact-collapse commit.
- Field-report equality/disposition assertion once Petar decides file role.
- UTF-8 mojibake scan after every commit containing Cyrillic.
- Manual browser smoke test after app adapter/schema change.

Rollback strategy:

- Prefer `git revert` of migration commits.
- Keep old IDs and old coordinates in `source_refs` and commit messages so individual records can be restored without whole-repo rollback.

Suggested commit boundaries:

- Commit A: audit artifacts / migration script dry-run only.
- Commit B: type normalization only.
- Commit C: exact duplicate collapse and source reference preservation.
- Commit D: schema-key migration plus frontend adapter/update.
- Commit E: docs sync and final verification.

## Section 13: Open Questions for Petar

### 13A. Manual Type Assignment Required

The 17 records below need Petar domain assignment before cleanup. Sixteen have `t: "70/80"` and one has `t: "ПК1"`.

```json
{"i":"VIK-VARNA_IZTOK-0200","t":"70/80","a":"","r":"4 подрайон","s":"VARNA_IZTOK","c":[27.911956,43.209981],"z":""}
{"i":"VIK-VARNA_IZTOK-0201","t":"70/80","a":"","r":"4 подрайон","s":"VARNA_IZTOK","c":[27.911523,43.209866],"z":""}
{"i":"VIK-VARNA_IZTOK-0203","t":"70/80","a":"","r":"","s":"VARNA_IZTOK","c":[27.907937,43.208654],"z":"10/41 - екз"}
{"i":"VIK-VARNA_IZTOK-0204","t":"70/80","a":"","r":"","s":"VARNA_IZTOK","c":[27.90863,43.208873],"z":"10/41"}
{"i":"VIK-VARNA_IZTOK-0205","t":"70/80","a":"","r":"","s":"VARNA_IZTOK","c":[27.906009,43.207989],"z":"10/41"}
{"i":"VIK-VARNA_IZTOK-0206","t":"70/80","a":"","r":"10 подрайон","s":"VARNA_IZTOK","c":[27.90511,43.207694],"z":"10/41"}
{"i":"VIK-VARNA_IZTOK-0207","t":"70/80","a":"","r":"10 подрайон","s":"VARNA_IZTOK","c":[27.904052,43.207221],"z":"10/41"}
{"i":"272","t":"70/80","a":"","r":"КВ. ЧАЙКА; 19,20 М.Р; ЧАСТ 3","s":"VARNA_IZTOK","c":[27.9404,43.219637],"z":""}
{"i":"273","t":"70/80","a":"","r":"КВ. ЧАЙКА; 19,20 М.Р; ЧАСТ 3","s":"VARNA_IZTOK","c":[27.941358,43.219505],"z":""}
{"i":"277","t":"70/80","a":"","r":"КВ. ЧАЙКА; 19,20 М.Р; ЧАСТ 3","s":"VARNA_IZTOK","c":[27.943913,43.21923],"z":""}
{"i":"VIK-VARNA_ZAPAD-0149","t":"70/80","a":"ул. \"Янтра\"","r":"","s":"VARNA_ZAPAD","c":[27.893167,43.17856],"z":"от ситуация"}
{"i":"VIK-VARNA_ZAPAD-0203","t":"70/80","a":"","r":"","s":"VARNA_ZAPAD","c":[27.906009,43.207989],"z":"10/41"}
{"i":"VIK-VARNA_ZAPAD-0204","t":"70/80","a":"","r":"10 подрайон","s":"VARNA_ZAPAD","c":[27.90511,43.207694],"z":"10/41"}
{"i":"VIK-VARNA_ZAPAD-0205","t":"70/80","a":"","r":"10 подрайон","s":"VARNA_ZAPAD","c":[27.904052,43.207221],"z":"10/41"}
{"i":"VIK-VARNA_ZAPAD-0207","t":"70/80","a":"","r":"10 подрайон","s":"VARNA_ZAPAD","c":[27.901958,43.20645],"z":"10/41"}
{"i":"600","t":"70/80","a":"","r":"М-Т КОЧМАР; ЧАСТ 3","s":"VARNA_ZAPAD","c":[27.890072,43.236832],"z":""}
{"i":"398","t":"ПК1","a":"ул.13","r":"С. ЗВЕЗДИЦА; ЧАСТ 2","s":"VARNA_ZAPAD","c":[27.833832,43.153162],"z":"не е открит"}
```

### 13B. field_reports.json Disposition

`field_reports.json` contains 14 records, all duplicated identically in `data/hydrants.json`. Decide whether this file is:

- stale archive,
- immutable history log,
- or future incremental ingest queue.

Cleanup-sprint options:

| Option | Meaning | Tradeoff |
|---|---|---|
| Drop file | Single source of truth becomes `data/hydrants.json`. | Simplest runtime model; loses separate report-origin artifact unless preserved in Git history. |
| Keep as immutable history log | Document that it records already-ingested field reports. | Keeps provenance but can confuse agents unless role is explicit. |
| Convert to ingest queue | Use it only for pending records before canonical merge. | Useful workflow, but needs Worker/ingest discipline and documentation. |

Recommendation is pending Petar's decision after checking whether any current Worker or ingest behavior still writes this file. Repo evidence alone does not show live Worker writes because Worker source is external.

### 13C. Duplicate Resolution Policy

Petar should confirm:

- Are exact same-origin duplicates safe to auto-collapse when type/address/status do not conflict?
- Should 25m or 50m near-duplicate clusters be reviewed manually only, with no auto-collapse?
- For national-national exact duplicates with conflicting `ground` / `underground`, should national source metadata decide, or should they all be field-reviewed?

### 13D. Target Status Vocabulary

Petar pre-decided parallel fields, but final literal values still need approval:

- Existence `status`: suggested `verified`, `unverified`, `missing`.
- Operational `operational_status`: suggested `works`, `not_working`, `not_tested`, or absent unknown.
- Review `review_status`: suggested `reported`, `pending_review`, `approved`, `rejected` if moderation is added later.

### 13E. Verbose Schema Rollout

Petar approved verbose canonical keys for readability. Before execution, decide whether the cleanup sprint should:

- update `index.html` to consume verbose keys directly,
- add a compatibility adapter accepting both compact and verbose records,
- or migrate data and app code in a single atomic commit.

Given GitHub Pages static hosting, an adapter is safer for rollback but adds temporary complexity.
