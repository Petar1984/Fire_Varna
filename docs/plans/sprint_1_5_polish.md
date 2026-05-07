# Sprint 1.5 Plan: UX Polish Before Broad Launch

## Overview
Plan target: `docs/plans/sprint_1_5_polish.md`.

Fix four pre-launch UX issues in `index.html` only. No Worker changes, no dataset migration, no new dependencies, no build/refactor, and total `index.html` growth should stay under 3 KB.

Issues 1 and 4 are low-risk UI copy/display fixes. Issues 2 and 3 should be implemented together because both touch all-mode cluster interaction and active-target rendering.

## Issue 1: Welcome Modal Text
Current line: `index.html:3080`.

Replace:

`Разреши локация, за да видиш най-близките хидранти. Бутон 🚨 отваря сигнал.`

With:

`Разреши локация, за да видиш най-близките хидранти. Натисни и задръж pin за сигнал; + отваря избор на доклад.`

This removes the stale 🚨 button reference and names the current gestures.

## Issue 2: Cluster Auto-Close In “Всички”
Root cause: GPS updates destroy the active cluster interaction. `watchPosition()` calls `onLocation()`; after first lock, `onLocation()` calls `refresh(false)` on every GPS update. `refresh()` removes `allClusterLayer`, then rebuilds the full cluster, which closes any spiderfied cluster child markers.

Recommended fix:
- Add `allClusterInteractionOpen` state.
- Set it from MarkerCluster `spiderfied` / `unspiderfied` events.
- During routine GPS updates, if `mode === 'all' && allClusterInteractionOpen`, skip full `refresh(false)`.
- While skipping refresh, update only user-dependent visuals: user marker already moves; update dashed line, card info, and arrow via lightweight helpers.
- Do not change MarkerCluster defaults such as `spiderfyOnMaxZoom` or `zoomToBoundsOnClick`.

Bonus: this also reduces “Всички” mode rebuild churn during cluster investigation.

## Issue 3: Tap-To-Activate In “Всички”
Use Option B-lite: add `activeTargetId` as the source of truth, while keeping `activeTargetIdx` as a derived list/rank helper.

Key changes:
- Add helpers: `getActiveTarget()`, `setActiveTargetHydrant(h)`, and a lightweight active-overlay update path for all mode.
- Near/top marker and list selection should set both `activeTargetId` and `activeTargetIdx`.
- All-mode dim marker tap should select any hydrant by ID, even outside the nearest-10 `currentRanked`.
- All-mode long-press should select the hydrant first, then open the report picker.
- If the selected all-mode hydrant is in the visible nearest-10 list, use its rank label; otherwise render the active overlay with a neutral bullet label.
- Prefer direct active-overlay update when tapping a spiderfied child marker, not full `refresh()`, so duplicate investigation can continue.
- Mode switch resets selection to the first item in the new mode, preserving current behavior.
- Tapping the same pin again does not deselect.
- Polling must still update markers via `setIcon()` / `setLatLng()` only. If polling moves the active hydrant, redraw line/card/arrow without calling `refresh()`.

### Function Contracts
`setActiveTargetHydrant(h)`
- Input: hydrant object from `HYDRANTS` / `HYDRANTS_BY_ID`.
- Return: `void`.
- Null handling: if `h` is null/undefined or has no matching `h.i`, do nothing.
- Side effects: sets `activeTargetId = h.i`; derives `activeTargetIdx` from `currentRanked` if present, otherwise leaves it at `0`; updates the active overlay, dashed line, compact card, and arrow without requiring `refresh()`.
- In `mode !== 'all'`, it may delegate to normal `setActiveTarget(idx)` when the hydrant exists in `currentRanked`.

`getActiveTarget()`
- Input: none.
- Return: `{ h, d, idx }` or `null`.
- `h`: selected hydrant.
- `d`: current distance from `lastFix`, recomputed with Haversine.
- `idx`: index in `currentRanked` if found, otherwise `-1`.
- Null handling: return `null` if no `activeTargetId`, no `lastFix`, missing hydrant ID, or invalid coordinates.
- Side effects: none.

Modified `setActiveTarget(idx)`
- Input: integer index into `currentRanked`.
- Return: `void`.
- Null handling: if `idx` is outside `currentRanked`, do nothing.
- Side effects: sets `activeTargetIdx = idx`; sets `activeTargetId = currentRanked[idx].h.i`; then refreshes or updates visuals according to mode.
- In near/top modes, preserve current behavior with `refresh(false)`.
- In all mode during a cluster interaction, avoid full refresh and call the lightweight overlay update helper instead.

`updateAllModeActiveOverlay()`
- Input: none; reads `activeTargetId`, `lastFix`, `currentRanked`, `markersById`, and `allClusterLayer`.
- Return: `void`.
- Null handling: if `getActiveTarget()` returns `null`, remove any existing active overlay and line, then update card/arrow safely.
- Side effects: creates, replaces, or removes the single all-mode active numbered/bullet marker; tags it for polling (`_hydrantId`, `_pinKind`, `_rank`, `_isActivePin`); adds it to `markersById`; redraws dashed line; updates compact card and arrow.
- Must not rebuild `allClusterLayer` and must not call `refresh()`.

### Phase 2 / Phase 3 Interaction
When the user taps a spiderfied child marker while the Phase 2 guard is active:

1. MarkerCluster keeps the spiderfied child markers open because routine GPS `refresh(false)` is skipped.
2. Child marker tap calls `setActiveTargetHydrant(h)`.
3. `setActiveTargetHydrant(h)` sets `activeTargetId`, derives `activeTargetIdx` if possible, and calls `updateAllModeActiveOverlay()`.
4. `updateAllModeActiveOverlay()` creates/updates the active overlay marker, draws the dashed line, updates the compact card, and updates the arrow.
5. No full `refresh()` runs, and `allClusterLayer` is not removed.
6. The spiderfied cluster remains open until the user dismisses it normally by tapping elsewhere, zooming, or another MarkerCluster unspiderfy trigger.

## Issue 4: Type Display In Report Modal
Insert only in `targetCardHTML()` at `index.html:2171-2187`. Do not add type to the compact bottom navigation card.

`escapeHtml()` already exists at `index.html:3059-3064`.

Add `hydrantTypeLabel(hydrant)`:
- Trim and lowercase `h.t`.
- `raw === 'underground' || raw.includes('подземен')` → `Подземен`
- `raw === 'ground' || raw.includes('надземен')` → `Надземен`
- Otherwise return empty string.

Render conditional line after ID/source/subdistrict and before coordinates:

`Тип: <label>`

Skip empty/null/unrecognized values such as `70/80` or `ПКн`.

## Implementation Order And Bundling
Use two independently revertible commits:

1. Cosmetic/display commit:
   - Issue 1 welcome text.
   - Issue 4 report modal type display.

2. All-mode behavior commit:
   - Issue 2 cluster interaction guard.
   - Issue 3 ID-based active target and all-mode overlay selection.

Rationale: Issues 2 and 3 share all-mode active/refresh behavior and should be tested as one behavioral unit.

## Implementation Phases
Claude Code should use approval gates:

1. Phase 1: read + propose
   - Read `AGENTS.md`, `CLAUDE.md`, `docs/activeContext.md`, this plan, and affected `index.html` sections.
   - Restate intended edits and any discovered mismatch.
   - Stop for Petar approval.

2. Phase 2: diff preview
   - Prepare exact code changes without committing.
   - Show focused diff preview for `index.html` and any doc file.
   - Stop for Petar approval.

3. Phase 3: apply + test
   - Apply approved edits.
   - Serve locally with `python -m http.server 8000`.
   - Run localhost/mobile verification checklist.
   - Report file sizes and test results.
   - Stop for Petar approval.

4. Phase 4: doc updates
   - Update only required docs if implementation details differ from plan or active context needs sync.
   - Show doc diff preview.
   - Stop for Petar approval.

5. Phase 5: commit + push
   - Stage only approved files.
   - Commit as planned grouping.
   - Push.
   - Run `git fsck --full`.
   - Report commit hashes, push success, and fsck result.

## Testing Plan
Serve locally over HTTP at 375 px width.

Issue 1:
- Open `#welcome`.
- Verify screen 2 has no 🚨 button reference and Bulgarian text fits.

Issue 2:
- In “Всички”, tap a duplicate/near-duplicate cluster at max zoom.
- Wait longer than a normal GPS update interval; spiderfied child markers should remain.
- Verify polling `setIcon()` updates on spiderfied/active markers do not dismiss the spiderfy state.

Issue 3:
- In “Всички”, tap a visible/spiderfied hydrant outside nearest 10 if possible.
- Verify orange active ring, dashed line, card/nav target.
- Tap another pin; active target transitions cleanly.
- Tap same pin twice; it remains active.
- Switch to “Топ 5”; selection resets to top item.
- Confirm near/top tap and long-press still work.

Issue 4:
- Open report picker for national `ground` / `underground`, field `надземен`, VIK mixed text, and empty/unknown `t`.
- Verify type appears only for recognized values.

Regression:
- GPS lock, follow mode, manual position, FAB menu, long-press report flow, report submit/queue, polling cadence, and mode switching.
- Confirm `index.html` growth is under 3 KB.

## Rollback Plan
Rollback individual commits with `git revert`.

If the branch must return to the approved rollback point, use `9ec694f` as clarified by Petar. Do not force-push without explicit approval.

## Open Questions
None blocking. Petar should review the final Bulgarian welcome wording before implementation.

## Implementation Handoff
Claude Code should implement in a fresh session after Petar approval, reading `AGENTS.md`, `CLAUDE.md`, `docs/activeContext.md`, and this plan first. No architectural expansion, dependencies, Worker changes, or dataset edits.
