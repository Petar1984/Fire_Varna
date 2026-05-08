# Bug Fixes Plan 2026-05-08

Target audit file: `docs/audits/bug_fixes_plan_20260508.md`.

Execution scope for this write: create this plan file only. No code edits, no data edits, no commits.

## 1. Required Preamble

Scope citation: Petar requested read-only investigation for "Polling Dedupe + Card/Row Type Rendering," with `index.html` primary, no code edits, no commits, and a single write target at `docs/audits/bug_fixes_plan_20260508.md`.

Deterministic inventory:

```text
C:\Projects\Varna_hydrants\AGENTS.md
C:\Projects\Varna_hydrants\docs\activeContext.md
C:\Projects\Varna_hydrants\docs\architecture\data_roadmap_20260508.md
C:\Projects\Varna_hydrants\index.html
C:\Projects\Varna_hydrants\data\hydrants.json
C:\Projects\Varna_hydrants\field_reports.json
C:\Projects\Varna_hydrants\docs\audits\data_architecture_audit_20260508.md
C:\Projects\Varna_hydrants\docs\audits\governance_proposal_20260508.md
C:\Projects\Varna_hydrants\docs\audits\issue_ingest_plan_20260508.md
```

Files read: `AGENTS.md`, `docs/activeContext.md`, `docs/architecture/data_roadmap_20260508.md`, `index.html`, `data/hydrants.json`, `field_reports.json`, `docs/audits/issue_ingest_plan_20260508.md`.

Negative findings:

```text
docs/audits/bug_fixes_plan_20260508.md did not exist before this approved write.
No package.json, src/**, worker/**, scripts/**, *.test.*, *.spec.*, or playwright.config.* found in scoped repo search.
No slice(0,8), substring(0,8), or substr(0,8) truncation logic found in index.html.
No field_ truncation helper found in index.html.
No hydrantTypeLabel usage found in card/list paths; only report-modal target card uses it.
No duplicate i values found in data/hydrants.json.
Mojibake scan returned no matches for AGENTS.md, activeContext, data roadmap, index.html, data/hydrants.json, field_reports.json.
```

Declared metadata:

```text
docs/activeContext.md:6 Last updated: 2026-05-08 at commit 2dcab73
docs/activeContext.md:11 - index.html: 304,192 bytes (...)
docs/activeContext.md:12 - data/hydrants.json: 968,365 bytes (6,082 records - 8 field reports ingested in commit 2dcab73)
docs/activeContext.md:18 - GET `/issues` endpoint: live as of 2026-05-07 (commit 15), 30s KV-cached
docs/architecture/data_roadmap_20260508.md:57 **6. Polling dedupe ID format mismatch.**
docs/architecture/data_roadmap_20260508.md:60 **7. Card/row UI does not display hydrant type field 't'.**
docs/architecture/data_roadmap_20260508.md:467 Both fixes touch only `index.html`. No data file changes. Safe to do before cleanup.
```

Conflict noted: `docs/activeContext.md:86` says polling is idempotent, but current code plus `data/hydrants.json` field IDs show the new-hydrant dedupe only checks full `report.id`, while ingested records use `field_<8chars>`.

Decision ledger:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Fix Bug A in frontend polling only | Code + roadmap | Worker source external; `index.html:3045-3056` owns new-hydrant polling insert | Revert one hunk | Recommended |
| Do not edit data files for Bug A | User constraint + roadmap | Existing data already stores `field_<8>` plus `report_id` full UUID | Reversible by future data sprint | Required |
| Reuse existing type wording for Bug B with surface-specific placement | Existing UI + Petar R1/R3 | Modal stays `<div>Тип: Надземен</div>`; row meta uses `Тип: Надземен`; card name appends ` · Надземен` without `Тип:` | Revert UI hunks | Approved by Petar 2026-05-08 |
| Validate Bug A before closing issues #29-#36 | Petar ratification R2 | Issue closure timing is after deploy and empirical validation | Reversible by closing later | Approved by Petar 2026-05-08 |
| Split commits despite combined feasibility | Rollback safety | Polling behavior and UI rendering are independent | Revert either commit | Recommended |

Approval-gate check: no architecture change, no dependency, no data-source change, no Worker change. Bug B surfaces Bulgarian display text in new places; Petar approved reuse of the existing modal type words "Надземен/Подземен" on 2026-05-08, with R3 approving card-name bare suffix placement.

Encoding scan to run after this file is created:

```powershell
Select-String -Path docs/audits/bug_fixes_plan_20260508.md -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8
```

## 2. Bug A Diagnosis

Relevant current code:

```js
// index.html:1355-1357
const HYDRANTS = JSON.parse(document.getElementById('hydrantData').textContent);
const HYDRANTS_BY_ID = {};
HYDRANTS.forEach(h => { HYDRANTS_BY_ID[h.i] = h; });
```

```js
// index.html:2513-2515
return {
  report_id: uuidv4(),
  report_type: reportType,
```

```js
// index.html:3045-3056
if (type === 'new_hydrant' && !report.hydrant_id) {
  if (!report.id || !Array.isArray(report.coords) || report.coords.length !== 2) continue;
  if (HYDRANTS_BY_ID[report.id]) continue; // already added in a prior poll
  const h = {
    i: report.id,
    c: [Number(report.coords[0]), Number(report.coords[1])],
    o: 'field_report',
    status: 'verified'
  };
  if (!Number.isFinite(h.c[0]) || !Number.isFinite(h.c[1])) continue;
  HYDRANTS.push(h);
  HYDRANTS_BY_ID[h.i] = h;
```

Data evidence:

```text
data/hydrants.json field record example:
i: field_ba91e3ff
report_id: ba91e3ff-f28a-4499-82ba-61d850a051a4
```

Diagnosis: polling receives/uses full UUID as `report.id`, but ingested runtime records are keyed in `HYDRANTS_BY_ID` by truncated `field_<8chars>`. The check at `index.html:3047` misses already-ingested field reports and appends duplicate in-memory pins while the corresponding GitHub issues remain open.

## 3. Bug A Fix Proposal

Recommended: Option A1, polling-side dual-format check.

Patch:

```diff
--- a/index.html
+++ b/index.html
@@ -3043,10 +3043,12 @@
       if (!type) continue;
 
       if (type === 'new_hydrant' && !report.hydrant_id) {
         if (!report.id || !Array.isArray(report.coords) || report.coords.length !== 2) continue;
-        if (HYDRANTS_BY_ID[report.id]) continue; // already added in a prior poll
+        const reportId = String(report.id);
+        const fieldId = reportId.startsWith('field_') ? reportId : 'field_' + reportId.slice(0, 8);
+        if (HYDRANTS_BY_ID[reportId] || HYDRANTS_BY_ID[fieldId]) continue; // already added in a prior poll or ingest
         const h = {
-          i: report.id,
+          i: reportId,
           c: [Number(report.coords[0]), Number(report.coords[1])],
           o: 'field_report',
           status: 'verified'
```

Rationale: fixes the observed mismatch without data edits, Worker edits, or changing live not-yet-ingested report behavior.

Other options:

| Option | Lines | Change | Risk | Reversibility |
|---|---:|---|---|---|
| A1 frontend dual check | 3046-3049 | Check `report.id` and derived `field_<8>` | Very low; inherits existing truncated-ID collision risk | One hunk |
| A2 ingest full UUID | data ingest, not `index.html` | Change canonical data IDs to full UUIDs | High; touches data model, existing records, field_reports, wrong-location rules | Data migration rollback |
| A3 Worker truncates ID | Worker GET `/issues` | Emit `field_<8>` from Worker | Out of scope; Worker source external and deploy risk | Worker rollback only |

## 4. Bug B Diagnosis

Current list rendering omits `h.t`:

```js
// index.html:1737-1749
list_data.forEach((r, i) => {
  const h = r.h;
  const addr = h.a || ('Хидрант ' + h.i);
  const meta = [h.s, h.r].filter(Boolean).join(' · ');
  const row = document.createElement('div');
  row.className = 'row' + (i === activeTargetIdx ? ' active-target' : '');
  row.dataset.idx = i;
  row.innerHTML =
    '<div class="rank">' + (i+1) + '</div>' +
    '<div class="row-info">' +
      '<div class="row-addr">' + escapeHtml(addr) + '</div>' +
      '<div class="row-meta">' + escapeHtml(meta) + ' · ID ' + escapeHtml(h.i) + '</div>' +
```

Current card rendering omits `h.t`:

```js
// index.html:1937-1949
function updateCardInfo() {
  const at = getActiveTarget();
  if (!at) return;
  const distEl = document.getElementById('cardDist');
  const nameEl = document.getElementById('cardName');
  const bearingEl = document.getElementById('cardBearing');
  if (!distEl) return;
  distEl.textContent = formatDist(at.d);
  const label = at.idx >= 0 ? ('#' + (at.idx + 1) + ' ') : '';
  nameEl.textContent = label + (at.h.a || ('Хидрант ' + at.h.i));
  const bear = bearing(lastFix.lat, lastFix.lon, at.h.c[1], at.h.c[0]);
  bearingEl.textContent = cardinal(bear) + ' · ' + Math.round(bear) + '°' +
    (smoothedHeading == null ? ' (без компас)' : '');
}
```

Existing helper and modal usage:

```js
// index.html:2265-2270
function hydrantTypeLabel(hydrant) {
  if (!hydrant || hydrant.t == null) return '';
  const raw = String(hydrant.t).trim().toLowerCase();
  if (raw === 'underground' || raw.includes('подземен')) return 'Подземен';
  if (raw === 'ground' || raw.includes('надземен')) return 'Надземен';
  return '';
}
```

```js
// index.html:2283-2288
const typeLabel = hydrantTypeLabel(hydrant);
return '<div class="modal-target-card">' +
  '<div class="name">' + escapeHtml(hydrant.a || ('Хидрант ' + hydrant.i)) + '</div>' +
  '<div>ID: ' + escapeHtml(hydrant.i) + ' · ' + escapeHtml(hydrant.s) +
    (hydrant.r ? ' · ' + escapeHtml(hydrant.r) : '') + '</div>' +
  (typeLabel ? '<div>Тип: ' + typeLabel + '</div>' : '') +
```

## 5. Bug B Fix Proposal

Recommended display:

- Modal: keep existing structured `Тип: Надземен/Подземен` line unchanged.
- Row meta: add `Тип: Надземен/Подземен` inside the existing joined metadata string.
- Card name: append bare type word to the name line as ` · Надземен` / ` · Подземен`.
- Card bearing line remains untouched and reserved for tactical navigation info.
- Missing, unknown, or `не знам` type values render nothing.

Petar ratified this as R1 and R3 on 2026-05-08.

Patch:

```diff
--- a/index.html
+++ b/index.html
@@ -1737,7 +1737,8 @@
     list_data.forEach((r, i) => {
       const h = r.h;
       const addr = h.a || ('Хидрант ' + h.i);
-      const meta = [h.s, h.r].filter(Boolean).join(' · ');
+      const typeLabel = hydrantTypeLabel(h.t);
+      const meta = [h.s, h.r, typeLabel ? ('Тип: ' + typeLabel) : ''].filter(Boolean).join(' · ');
       const row = document.createElement('div');
@@ -1943,8 +1944,11 @@
     if (!distEl) return;
     distEl.textContent = formatDist(at.d);
     const label = at.idx >= 0 ? ('#' + (at.idx + 1) + ' ') : '';
-    nameEl.textContent = label + (at.h.a || ('Хидрант ' + at.h.i));
+    const typeLabel = hydrantTypeLabel(at.h.t);
+    const baseName = at.h.a || ('Хидрант ' + at.h.i);
+    const nameWithType = baseName + (typeLabel ? ' · ' + typeLabel : '');
+    nameEl.textContent = label + nameWithType;
     const bear = bearing(lastFix.lat, lastFix.lon, at.h.c[1], at.h.c[0]);
     bearingEl.textContent = cardinal(bear) + ' · ' + Math.round(bear) + '°' +
       (smoothedHeading == null ? ' (без компас)' : '');
@@ -2262,10 +2265,10 @@
       default:                 return '🚨 Сигнал за хидрант';
     }
   }
-  function hydrantTypeLabel(hydrant) {
-    if (!hydrant || hydrant.t == null) return '';
-    const raw = String(hydrant.t).trim().toLowerCase();
+  function hydrantTypeLabel(typeValue) {
+    if (typeValue == null) return '';
+    const raw = String(typeValue).trim().toLowerCase();
@@ -2280,7 +2283,7 @@
     }
     if (!hydrant) return '';
-    const typeLabel = hydrantTypeLabel(hydrant);
+    const typeLabel = hydrantTypeLabel(hydrant.t);
```

Rationale:

- Card name line is a single readable phrase; bare type label reads naturally, for example `Хидрант 187 · Надземен`.
- Card bearing line stays semantically pure for navigation.
- Row meta line remains label-prefixed because it joins multiple heterogeneous fields.
- Modal preserves structured `Тип: X`; row preserves `Тип: X`; card asymmetry is intentional UX placement, not terminology fragmentation.

## 6. Commit Strategy

Use two sequential commits, not one combined commit:

1. `fix(realtime): dedupe polled field report ids`
2. `fix(ux): show hydrant type in card and rows`

Combined commit is technically feasible and roadmap-approved because both touch only `index.html`, but split commits give clean rollback if either the polling path or the Bulgarian UI display needs reversal.

The fixes do not interact: Bug A touches only `applyReports()` new-hydrant insertion; Bug B touches `renderList()`, `updateCardInfo()`, and `hydrantTypeLabel()` display formatting.

## 7. Test Plan

Bug A:

- Start local server with `python -m http.server 8000`.
- Load localhost over HTTP, with DevTools open.
- Leave issues #29-#36 open until after deploy, per Petar ratification R2.
- Use existing open ingested `new_hydrant` issues if still available: their full `report.id` values should map to existing `field_<8>` records and skip `HYDRANTS.push`.
- Set a breakpoint around `index.html:3046-3049`; confirm `reportId` is full UUID, `fieldId` is `field_<first8>`, and `HYDRANTS_BY_ID[fieldId]` is truthy for ingested reports.
- Submit one synthetic `new_hydrant` report through the normal `+` flow only if a live end-to-end test is acceptable. Confirm it appears once during polling while not yet ingested, and after ingest/reload it does not duplicate.

Bug B:

- Use a known typed record such as `field_ba91e3ff` (`t:"надземен"`).
- Verify list row displays `Тип: Надземен` before `ID`.
- Select the same hydrant and verify the compact card name line displays a bare suffix, for example `Хидрант ... · Надземен`.
- Verify the compact card bearing line remains `cardinal · degrees` plus optional compass status only, with no `Тип:` prefix.
- Verify a record with missing/unknown `t` shows no type suffix/prefix.
- Re-open report modal and verify existing modal type display still works.

Encoding and smoke:

```powershell
Select-String -Path index.html -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8
```

Also smoke-check `Близо`, `Топ 5`, `Всички`, pin tap, long-press report picker, and polling network cadence.

## 8. Rollback Plan

If Bug A fails: revert commit `fix(realtime): dedupe polled field report ids`, or manually restore `index.html:3046-3049` to the single `HYDRANTS_BY_ID[report.id]` check.

If Bug B fails or wording is rejected: revert commit `fix(ux): show hydrant type in card and rows`, restoring helper signature and removing type display from card/list.

No data rollback is needed because recommended fixes do not touch `data/hydrants.json` or `field_reports.json`.

## 9. Open Questions

- Bulgarian display wording is closed: Petar approved reuse of existing `Надземен/Подземен` type words on 2026-05-08.
- Type placement is closed: modal keeps `Тип: X`, row meta uses `Тип: X`, and card name uses bare ` · X`.
- Issue closure timing is closed: Petar approved closing issues #29-#36 after deploy and empirical Bug A validation.
- No Worker or data-file change is recommended for this sprint.
