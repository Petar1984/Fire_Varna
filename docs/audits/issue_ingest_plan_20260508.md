# Issue Ingest Plan 2026-05-08

## Summary

Scope declaration: per Petar's brief, this audit covers open GitHub issues with the `report` label and produces ingest entries for issues #29-#36 only. It also resolves governance Open Q#3 from `docs/audits/governance_proposal_20260508.md` by tracing the current Sprint 1.5 canonical write target. No data-file edits are part of this document.

Current Sprint 1.5 canonical write target is `data/hydrants.json`; `index.html` is not a data-ingest target. New `field_*` hydrants must be added to both `field_reports.json` and `data/hydrants.json`; canonical IDs mutate `data/hydrants.json` only.

## Required Preamble

Deterministic inventory:

```text
AGENTS.md 14669
docs/activeContext.md 13577
docs/audits/governance_proposal_20260508.md 12889
index.html 304192
data/hydrants.json 967530
field_reports.json 4228
audit/apply_field_reports.py 8439
docs/audits/issue_ingest_plan_20260508.md <missing before this write>
```

Issue inventory:

```text
#29 | [missing] VIK-VARNA_ZAPAD-0256 | labels=[report, missing, pending-review] | created=2026-05-06T09:33:36Z | updated=2026-05-06T09:33:36Z
#30 | [missing] 187 | labels=[report, missing, pending-review] | created=2026-05-06T10:50:06Z | updated=2026-05-06T10:50:06Z
#31 | [new_hydrant] @43.211441,27.930768 | labels=[report, new-hydrant, pending-review] | created=2026-05-06T14:20:27Z | updated=2026-05-06T14:20:27Z
#32 | [exists_confirmed] 913 | labels=[report, exists-confirmed, pending-review] | created=2026-05-06T16:35:14Z | updated=2026-05-06T16:35:14Z
#33 | [exists_confirmed] 271 | labels=[report, exists-confirmed, pending-review] | created=2026-05-06T16:35:59Z | updated=2026-05-06T16:35:59Z
#34 | [missing] 187 | labels=[report, missing, pending-review] | created=2026-05-06T23:56:35Z | updated=2026-05-06T23:56:35Z
#35 | [new_hydrant] @43.240082,27.980469 | labels=[report, new-hydrant, pending-review] | created=2026-05-07T10:20:20Z | updated=2026-05-07T10:20:20Z
#36 | [new_hydrant] @43.212598,27.897397 | labels=[report, new-hydrant, pending-review] | created=2026-05-07T18:33:25Z | updated=2026-05-07T18:33:25Z
```

Files read: this brief, `AGENTS.md`, `docs/activeContext.md`, `docs/audits/governance_proposal_20260508.md`, `index.html`, `audit/apply_field_reports.py`, `data/hydrants.json`, `field_reports.json`, and GitHub issue bodies #29-#36.

Negative findings:

```text
no open report issues with report_type wrong_location found
no open report issues with report_type damaged found
field_a183a467 / field_c42352c8 / field_bf18790e not found in data/hydrants.json or field_reports.json
Canonical target IDs (VIK-VARNA_ZAPAD-0256, 187, 913, 271 -- referenced in issues #29/#30/#32/#33/#34) found exactly once in data/hydrants.json; zero occurrences in field_reports.json.
```

Issue body encoding verified clean:

```text
issue #29: no mojibake markers found
issue #30: no mojibake markers found
issue #31: no mojibake markers found
issue #32: no mojibake markers found
issue #33: no mojibake markers found
issue #34: no mojibake markers found
issue #35: no mojibake markers found
issue #36: no mojibake markers found
```

Canonical target evidence from `index.html`:

```js
<script id="hydrantData" type="application/json"></script>
const response = await fetch('data/hydrants.json', { cache: 'no-cache' });
document.getElementById('hydrantData').textContent = text;
const HYDRANTS = JSON.parse(document.getElementById('hydrantData').textContent);
```

Stale script evidence from `audit/apply_field_reports.py`:

```py
FR = ROOT / "field_reports.json"
INDEX = ROOT / "index.html"
INDEX.write_text(new_html, encoding="utf-8")
```

## Governance Decisions

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Bypass `audit/apply_field_reports.py`; Claude Code writes fresh ingest in commit | User-approved this turn | Script has mojibake-corrupted literals, is untracked, and targets stale `index.html` embedded JSON; Sprint 1.5 canonical target is `data/hydrants.json` | Reversible; old script remains in working tree and can be audited separately | Approved by Petar 2026-05-08 |
| Close issues after ingest, with comment `Ingested in commit <hash>` | Code evidence | Worker fetches only `state=open&labels=report`; relabeling `pending-review` to `ingested` alone would still leave open `report` issues in polling | Reversible by reopening issues if needed | Recommended |

Polling evidence:

```js
url.searchParams.set("state", "open");
url.searchParams.set("labels", "report");
if (type === 'new_hydrant' && !report.hydrant_id) {
  if (HYDRANTS_BY_ID[report.id]) continue;
}
if (newStatus && h.status !== newStatus) {
  h.status = newStatus;
}
```

## Ingest Ledger

Coordinate guard: issue coordinate must match canonical coordinate exactly for this batch; verified zero diff, so tolerance is moot. If executor adds a defensive guard, use max absolute lon/lat diff `<= 0.0001`.

| issue # | report_type | target_id | mutation | target_file(s) | evidence | reversibility |
|---|---|---|---|---|---|---|
| #29 | `missing` | `VIK-VARNA_ZAPAD-0256` | Set `status:"reported"`; do not mutate `t` in this ingest | `data/hydrants.json` | issue `[27.903432,43.218761]`; canonical `[27.903432,43.218761]`; diff `[0,0]`; `hydrant_type_at_location:"подземен"` deferred to backfill policy | Remove `status` |
| #30 | `missing` | `187` | Set `status:"reported"` | `data/hydrants.json` | issue `[27.901624,43.218286]`; canonical `[27.901624,43.218286]`; diff `[0,0]`; `hydrant_type_at_location:"не знам"` discardable | Remove `status` |
| #31 | `new_hydrant` | `field_a183a467` | Add record: `c:[27.930768,43.211441]`, `t:"надземен"`, `status:"verified"` | `field_reports.json`, `data/hydrants.json` | issue has `hydrant_type: "надземен"` | Delete new record from both files |
| #32 | `exists_confirmed` | `913` | Set `status:"verified"` | `data/hydrants.json` | issue `[27.934473,43.213267]`; canonical `[27.934473,43.213267]`; diff `[0,0]` | Remove `status` |
| #33 | `exists_confirmed` | `271` | Set `status:"verified"` | `data/hydrants.json` | issue `[27.934205,43.213728]`; canonical `[27.934205,43.213728]`; diff `[0,0]` | Remove `status` |
| #34 | `missing` | `187` | Duplicate audit confirmation of #30; no second mutation | `data/hydrants.json` | same target/type/coord as #30; diff `[0,0]`; `hydrant_type_at_location:"не знам"` discardable | Same rollback as #30 |
| #35 | `new_hydrant` | `field_c42352c8` | Add record: `a:"До сградата на Руси"`, `c:[27.980469,43.240082]`, `t:"надземен"`, `status:"verified"` | `field_reports.json`, `data/hydrants.json` | issue has `description: "До сградата на Руси"` and `hydrant_type: "надземен"` | Delete new record from both files |
| #36 | `new_hydrant` | `field_bf18790e` | Add record: `c:[27.897397,43.212598]`, `t:"надземен"`, `status:"verified"` | `field_reports.json`, `data/hydrants.json` | issue has `hydrant_type: "надземен"` | Delete new record from both files |

For new records, set `r`, `s`, `z`, and `st` to `""` per existing `build_new_record` convention. `status:"verified"` for `new_hydrant` follows existing `apply_field_reports.py` precedent, but this should be documented later in `AGENTS.md` as a governance gap.

Open Question: hydrant-type backfill policy from `missing` / `exists_confirmed` reports is not in scope of this ingest and needs a future governance decision. Issue #29 provides `hydrant_type_at_location:"подземен"`, but this plan deliberately does not back-populate canonical record `t` until Petar approves a general policy.

## Quoted Issue Metadata

### Issue #29

```text
---
report_id: "7ae9b1d5-7875-457f-a2d7-2dcbbe10ef04"
report_type: "missing"
timestamp: "2026-05-06T12:33:31+03:00"
reporter: "Петър"
hydrant_ref: "VIK-VARNA_ZAPAD-0256"
expected_coord: [27.903432, 43.218761]
reported_coord: null
location_method: "hydrant_ref"
app_version: "merged-2026-05-05"
free_text: null
terrain_description: "Не намирам хидрант, няма и знак за хидрант"
description: null
damage_description: null
hydrant_type_at_location: "подземен"
hydrant_type: null
operational: null
---

## Доклад

**Тип:** Хидрант липсва
**Подател:** Петър
**Време:** 2026-05-06T12:33:31+03:00
**Хидрант ID:** VIK-VARNA_ZAPAD-0256
**Координати в базата (lon, lat):** [27.903432, 43.218761]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.218761,27.903432

**Терен:**
> Не намирам хидрант, няма и знак за хидрант
**Очакван тип на място:** подземен

— App: merged-2026-05-05
```

### Issue #30

```text
---
report_id: "3ea44301-845d-45f1-89b0-a26fbb6d6f0c"
report_type: "missing"
timestamp: "2026-05-06T13:50:02+03:00"
reporter: "Петър"
hydrant_ref: "187"
expected_coord: [27.901624, 43.218286]
reported_coord: null
location_method: "hydrant_ref"
app_version: "merged-2026-05-05"
free_text: null
terrain_description: null
description: null
damage_description: null
hydrant_type_at_location: "не знам"
hydrant_type: null
operational: null
---

## Доклад

**Тип:** Хидрант липсва
**Подател:** Петър
**Време:** 2026-05-06T13:50:02+03:00
**Хидрант ID:** 187
**Координати в базата (lon, lat):** [27.901624, 43.218286]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.218286,27.901624
**Очакван тип на място:** не знам

— App: merged-2026-05-05
```

### Issue #31

```text
---
report_id: "a183a467-6454-42e7-8a0d-691fe30d30f8"
report_type: "new_hydrant"
timestamp: "2026-05-06T17:20:21+03:00"
reporter: "Петър"
hydrant_ref: null
expected_coord: null
reported_coord: [27.930768, 43.211441]
location_method: "manual_placement"
app_version: "merged-2026-05-05"
free_text: null
terrain_description: null
description: null
damage_description: null
hydrant_type_at_location: null
hydrant_type: "надземен"
operational: null
---

## Доклад

**Тип:** Нов хидрант
**Подател:** Петър
**Време:** 2026-05-06T17:20:21+03:00
**Поставена локация (lon, lat):** [27.930768, 43.211441]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.211441,27.930768
**Тип хидрант:** надземен

— App: merged-2026-05-05
```

### Issue #32

```text
---
report_id: "9773ca91-429c-4e96-b961-639c3e18baa7"
report_type: "exists_confirmed"
timestamp: "2026-05-06T19:35:09+03:00"
reporter: "Петър"
hydrant_ref: "913"
expected_coord: [27.934473, 43.213267]
reported_coord: null
location_method: "hydrant_ref"
app_version: "merged-2026-05-05"
free_text: "Срещу orange fitness"
terrain_description: null
description: null
damage_description: null
hydrant_type_at_location: null
hydrant_type: null
operational: null
---

## Доклад

**Тип:** Хидрантът е там
**Подател:** Петър
**Време:** 2026-05-06T19:35:09+03:00
**Хидрант ID:** 913
**Координати в базата (lon, lat):** [27.934473, 43.213267]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.213267,27.934473

**Бележка:**
> Срещу orange fitness

— App: merged-2026-05-05
```

### Issue #33

```text
---
report_id: "e9af9bef-c899-4180-a0a8-b0b1e6eac45c"
report_type: "exists_confirmed"
timestamp: "2026-05-06T19:35:54+03:00"
reporter: "Петър"
hydrant_ref: "271"
expected_coord: [27.934205, 43.213728]
reported_coord: null
location_method: "hydrant_ref"
app_version: "merged-2026-05-05"
free_text: "Срещу ТАБЛА на кръстовището"
terrain_description: null
description: null
damage_description: null
hydrant_type_at_location: null
hydrant_type: null
operational: null
---

## Доклад

**Тип:** Хидрантът е там
**Подател:** Петър
**Време:** 2026-05-06T19:35:54+03:00
**Хидрант ID:** 271
**Координати в базата (lon, lat):** [27.934205, 43.213728]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.213728,27.934205

**Бележка:**
> Срещу ТАБЛА на кръстовището

— App: merged-2026-05-05
```

### Issue #34

```text
---
report_id: "63076f64-c1ee-41ec-bb0d-67cccaa32ea1"
report_type: "missing"
timestamp: "2026-05-07T02:56:32+03:00"
reporter: "Петър"
hydrant_ref: "187"
expected_coord: [27.901624, 43.218286]
reported_coord: null
location_method: "hydrant_ref"
app_version: "merged-2026-05-05"
free_text: null
terrain_description: null
description: null
damage_description: null
hydrant_type_at_location: "не знам"
hydrant_type: null
operational: null
---

## Доклад

**Тип:** Хидрант липсва
**Подател:** Петър
**Време:** 2026-05-07T02:56:32+03:00
**Хидрант ID:** 187
**Координати в базата (lon, lat):** [27.901624, 43.218286]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.218286,27.901624
**Очакван тип на място:** не знам

— App: merged-2026-05-05
```

### Issue #35

```text
---
report_id: "c42352c8-d327-46e2-b7d1-35660292ba82"
report_type: "new_hydrant"
timestamp: "2026-05-07T13:20:15+03:00"
reporter: "Петър"
hydrant_ref: null
expected_coord: null
reported_coord: [27.980469, 43.240082]
location_method: "manual_placement"
app_version: "merged-2026-05-05"
free_text: null
terrain_description: null
description: "До сградата на Руси"
damage_description: null
hydrant_type_at_location: null
hydrant_type: "надземен"
operational: null
---

## Доклад

**Тип:** Нов хидрант
**Подател:** Петър
**Време:** 2026-05-07T13:20:15+03:00
**Поставена локация (lon, lat):** [27.980469, 43.240082]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.240082,27.980469

**Описание:**
> До сградата на Руси
**Тип хидрант:** надземен

— App: merged-2026-05-05
```

### Issue #36

```text
---
report_id: "bf18790e-5855-4324-92ef-00a1b161a0a8"
report_type: "new_hydrant"
timestamp: "2026-05-07T21:33:24+03:00"
reporter: "Калоян"
hydrant_ref: null
expected_coord: null
reported_coord: [27.897397, 43.212598]
location_method: "manual_placement"
app_version: "merged-2026-05-05"
free_text: null
terrain_description: null
description: null
damage_description: null
hydrant_type_at_location: null
hydrant_type: "надземен"
operational: null
---

## Доклад

**Тип:** Нов хидрант
**Подател:** Калоян
**Време:** 2026-05-07T21:33:24+03:00
**Поставена локация (lon, lat):** [27.897397, 43.212598]
**Карта:** https://www.google.com/maps/search/?api=1&query=43.212598,27.897397
**Тип хидрант:** надземен

— App: merged-2026-05-05
```

## Test Plan

Auditable pre-ingest status command:

```powershell
(Get-Content data/hydrants.json -Raw | ConvertFrom-Json) | Group-Object status | Select-Object Count, Name | Format-Table -AutoSize | Out-String -Width 200
```

Output:

```text
Count Name
----- ----
 6061
   18 verified
```

Interpretation: blank `Name` is the absent-status group, so absent/canonical is 6061. No `reported` row is present, so `reported=0`. This confirms pre-ingest counts `verified=18`, `reported=0`, absent/canonical `6061`.

Current `field_reports.json` length is empirical, not inferred:

```text
field_reports.json empirical count: 11
```

After Claude Code applies data edits:

- Parse `data/hydrants.json` and `field_reports.json`.
- Confirm `data/hydrants.json` count changes `6079 -> 6082`.
- Confirm `field_reports.json` count changes `11 -> 14`.
- Confirm `data/hydrants.json` status counts change from `verified=18`, `reported=0`, canonical/absent `6061` to `verified=23`, `reported=2`, canonical/absent `6057`.
- Confirm no duplicate IDs for `VIK-VARNA_ZAPAD-0256`, `187`, `913`, `271`, `field_a183a467`, `field_c42352c8`, `field_bf18790e`.
- Confirm commit message references all issues, including `Reported in #30, confirmed in #34`.
- Run mojibake scan on changed files before commit.
- After commit, close #29-#36 with comment `Ingested in commit <hash>`.

## Assumptions And Gates

Petar must review before any data-file edits. No architecture, UI-label, dependency, Worker, or source-archive changes are part of the ingest. `audit/apply_field_reports.py` cleanup is deliberately bypassed and left for a separate governance/refactor discussion.
