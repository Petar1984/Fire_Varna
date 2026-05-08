# Volunteer-Ready UX Sprint 1 Plan

## Executive Summary
- Modify only `index.html`, `field_reports.json`, and `AGENTS.md`; do not touch `hydrants_varna.json`, `audit/` history files, Worker code, dependencies, service worker, or build structure.
- All Bulgarian text is locked. Sprint 1 commit order is fixed. Pick-mode for non-new reports is deferred to Sprint 2.
- Current `index.html` is `1,243,208` bytes with `6,074` embedded hydrant records and `0` `status` fields; projected deployable size after Sprint 1 is about `1.26-1.27 MB`, safely below the `2 MB` hard cap.
- Use one atomic commit per item, with schema/data first and the largest behavior change near the end.
- Preserve existing per-hydrant report buttons, rAF compass smoothing, iOS compass permission flow, and manual position mode.

## Item 1: Welcome Modal

Files: `index.html:960-1031`, `index.html:1242-1251`, `index.html:1850-1875`, `index.html:2646`.

Specific changes:
- Reuse the existing `#modalBackdrop` modal shell instead of adding a second modal system.
- Add modal CSS near existing `.modal-*` rules using `.welcome-flow`, `.welcome-step`, `.welcome-progress`, `.welcome-copy`.
- Add `WELCOME_SEEN_KEY = 'welcome_seen'`, `WELCOME_FORCE_HASH = '#welcome'`, `WELCOME_SKIP_HASH = '#skip-welcome'`.
- Replace final boot call `startTracking()` with `bootApp()`: show welcome first when `localStorage.getItem('welcome_seen') !== '1'`, then call `startTracking()` only after `Скип` or `Готов`.

Locked Bulgarian text:
- Screen 1: `Хидранти Варна — карта на пожарни хидранти за пожарникари и доброволци`
- Screen 2: `Разреши локация, за да видиш най-близките хидранти. Бутон 🚨 отваря сигнал.`
- Screen 3: `За нов хидрант — ползвай „📍 Тук съм" или влечи pin-а за корекция. Zoom-ни за по-точно поставяне.`

Edge cases:
- If `localStorage` throws, show welcome once per current page session using an in-memory flag.
- `#skip-welcome` bypasses without setting storage; `#welcome` forces the modal for testing.

Interactions:
- Welcome appears before geolocation permission, but after map/modal DOM is ready.
- Report modal behavior remains unchanged.

Backward compatibility:
- Users with `welcome_seen=1` go straight to existing GPS flow.

Phone verification:
- Clear site data or use `#welcome`.
- Verify 375px viewport fits without scroll, buttons are at least 44px, and `Скип`/`Готов` trigger GPS prompt after close.

Risk: Medium, because delaying `startTracking()` changes boot timing.

## Item 2: FAB Consolidation

Files: `index.html:787-798`, `index.html:1189-1192`, `index.html:1909-1933`, `index.html:2540-2548`.

Specific changes:
- Replace current `#addHydrantBtn` `+` button in the right-side `.controls` stack with `id="reportFab"`.
- Use icon-only `🚨`, no visible text label.
- Set `title="Докладвай"` and `aria-label="Докладвай"`.
- Style with report semantic color `#ff5722`, matching `.card-btn.report`.
- Remove the direct `addHydrantBtn` placement handler and wire `reportFab` to `showReportTypePicker(null)`.
- Refactor `showReportTypePicker(hydrant)` to accept `null`; no-hydrant mode renders all 5 report types, per-hydrant mode keeps the existing 4 existing-hydrant types.
- When global `showReportTypePicker(null)` selects `new_hydrant`, close modal and call `enterLocationPlacementMode(null, callback)`.
- When global `showReportTypePicker(null)` selects `exists_confirmed`, `missing`, `damaged`, or `wrong_location`, show `Тапни хидрант на картата, за да докладваш` and close modal.

Important deferred behavior:
- Do not pre-store the selected report type for the next map tap.
- Do not implement interactive pick mode in Sprint 1.
- User must manually tap a hydrant and repeat report type selection through the existing per-hydrant flow.
- Pick-mode is deferred to Sprint 2 backlog.

Edge cases:
- No hydrant context must not call `targetCardHTML()` with assumptions.
- Existing per-hydrant card/list/popup 🚨 buttons continue calling `showReportTypePicker(hydrant)` unchanged.

Backward compatibility:
- Existing GitHub issue report payloads are unchanged.

Phone verification:
- Tap global 🚨, choose `Нов хидрант`, place a pin, submit form.
- Tap global 🚨, choose `Повреден`, verify instruction appears and modal closes.
- Tap an existing hydrant afterward and verify existing per-hydrant flow still works.

Risk: Medium, because this is the largest behavior change.

## Item 3: `📍 Тук съм` Placement Button

Files: `index.html:1103-1117`, `index.html:1196-1200`, `index.html:2435-2458`, `index.html:2502-2538`.

Specific changes:
- Add `<button class="placement-btn here" id="placementHere">📍 Тук съм</button>` after `placementClear`; final order: `Изчисти`, `📍 Тук съм`, `Отказ`, `Продължи ▶`.
- Add `.placement-btn.here { background:#1976d2; color:white; }`; reuse existing disabled styling.
- Add `const placementHereBtn = document.getElementById('placementHere')`.
- On entering placement mode, set disabled state from `!lastFix`; when disabled, set `title`/`aria-label` to `Няма GPS`.
- On click with `lastFix`, call existing marker logic with `L.latLng(lastFix.lat, lastFix.lon)`.
- Pin remains draggable.

Constants:
- None.

Edge cases:
- Allow use even when `lastFix.acc > 100`; volunteer can drag to refine.

Interactions:
- Uses the same `setPlacementMarker()` path as long-press, so confirm/clear buttons are enabled consistently.

Backward compatibility:
- Long-press and existing location placement link still work.

Phone verification:
- With GPS lock, enter new-hydrant placement, tap `Тук съм`, drag pin, clear, place again.
- Without GPS, verify disabled state.

Risk: Low.

## Item 4: Auto-Zoom During Placement

Files: `index.html:1255-1261`, `index.html:2502-2514`.

Specific changes:
- Add constants near existing app constants:
  - `PLACEMENT_MIN_ZOOM = 17`
  - `PLACEMENT_TARGET_ZOOM = 18`
  - `PLACEMENT_FLY_DURATION_SEC = 0.6`
- In `enterLocationPlacementMode()`, compute focus center: `initialCoord` if present, else `lastFix`, else `map.getCenter()`.
- If current zoom is below `17`, call `map.flyTo(center, 18, { animate:true, duration:0.6 })`.
- If current zoom is already `17+` and `initialCoord` exists, pan to the initial pin without zooming out.

Edge cases:
- Never reduce zoom from `19` to `18`.
- No GPS uses current map center.

Interactions:
- Improves global new-hydrant flow and wrong-location placement.
- Does not affect normal GPS refresh auto-fit.

Backward compatibility:
- Leaflet `flyTo()` is already available; no dependency change.

Phone verification:
- Enter placement from zoom 13 and confirm smooth zoom to 18.
- Enter from zoom 19 and confirm it does not zoom out.

Risk: Low to Medium, mostly motion feel.

## Item 5: Draggable Pin Hint

Files: `index.html:1095-1127`, `index.html:2430-2483`.

Specific changes:
- Add CSS `.placement-drag-hint` near placement CSS: pointer-events none, readable white/dark treatment, fade-in `200ms`, fade-out `400ms`, above Leaflet marker pane and below `.placement-actions`.
- Add constants:
  - `PLACEMENT_HINT_SESSION_KEY = 'hydrants_placement_drag_hint_seen'`
  - `PLACEMENT_HINT_VISIBLE_MS = 3000`
- Refactor `setPlacementMarker(latlng, options)` to accept `{ showHint: true }`.
- Pass `showHint:true` from long-press/contextmenu and `Тук съм`; pass false for initial auto-placement from existing report forms.
- Use locked hint text: `Влечи pin-а за корекция`.
- Use `placementMarker.bindTooltip(..., { permanent:true, direction:'top', className:'placement-drag-hint', interactive:false })`, then fade and unbind after 3 seconds.

Edge cases:
- If `sessionStorage` throws, use in-memory suppression for the page session.

Interactions:
- Hint never blocks dragging or action buttons.

Backward compatibility:
- No report payload/data changes.

Phone verification:
- First placement shows hint once, hint fades, second placement in same session does not show it.

Risk: Low.

## Item 6: Status Visualization

Files: `index.html:1138-1152`, `index.html:1184-1186`, `index.html:1277-1292`, `index.html:1446-1480`.

Specific changes:
- Insert a hidden inline SVG sprite at the top of `<body>`, near `#map`.
- Use a `<symbol>` for the uploaded Material Symbols hydrant, `viewBox="0 -960 960 960"`, path fill changed to `currentColor`.
- Reference the symbol via `<use>` inside `divIcon` HTML.
- Avoid duplicating path data across markers.
- Refactor `makePin()` to `makePin(rank, hydrant, isActive)` and update all call sites.
- CSS states:
  - `.h-pin.canonical`: red `#c41e3a`, 28x28, rank number visible.
  - `.h-pin.reported`: yellow `#fdd835`, 28x28, rank number visible.
  - `.h-pin.verified`: SVG hydrant icon, red `#c41e3a`, 32x32, no rank number.
- Move active halo to wrapper class `.h-pin-frame.first` so it applies around all three states without changing inner color.
- Keep `.h-pin.dim` cluster markers visually gray in `Всички` mode; only active highlighted marker in all-mode gets status visualization.
- Preserve cluster mode behavior and MarkerCluster use only in `Всички`.

Constants:
- `HYDRANT_STATUS_VERIFIED = 'verified'`
- `HYDRANT_STATUS_REPORTED = 'reported'`

Edge cases:
- Unknown `status` falls back to canonical red numbered pin.
- Existing `st` field is not reused or renamed.

Interactions:
- Render still rebuilds visible markers on `refresh()`.
- No live status mutation added in Sprint 1.
- Future single-status changes should call `marker.setIcon()` for affected visible markers only.

Backward compatibility:
- Records without `status` preserve current marker behavior.

Verification gate:
- Explicitly verify active halo and status rendering in all three modes: `Близо <100м`, `Топ 5`, `Всички`.
- In `Всички`, test cluster zoom-in/zoom-out cycles because cluster icons replace normal divIcons until spiderfy/expand.
- Confirm status visualization survives after clusters expand and after returning to clustered view.

Phone verification:
- After Item 8, the four field hydrants render as SVG hydrants.
- Canonical pins remain numbered red.
- Active target halo works over canonical, reported, and verified shapes.

Risk: Medium, because icon anchoring, halo alignment, and MarkerCluster behavior need map verification.

## Item 7: Smooth Follow Re-Center

Files: `index.html:1255-1261`, `index.html:1355-1368`, `index.html:2585-2605`.

Specific changes:
- Add constants:
  - `FOLLOW_EDGE_THRESHOLD_PCT = 0.30`
  - `FOLLOW_PAN_THROTTLE_MS = 1500`
  - `FOLLOW_PAN_DURATION_SEC = 0.5`
- Add `let lastFollowPanTs = 0`.
- Replace follow-mode `map.setView()` inside `onLocation()` with `maybePanForFollow()`.
- `maybePanForFollow()` converts `lastFix` to container point and pans only when inside the outer 30% edge band and throttle allows.
- Use `map.panTo([lastFix.lat,lastFix.lon], { animate:true, duration:0.5 })`.
- Locate button keeps immediate centering via existing `setView()` and is not throttled; update `lastFollowPanTs` after manual locate center.

Edge cases:
- No `lastFix`, missing marker, or zero map size returns without pan.

Interactions:
- Existing `dragstart` handler still exits follow mode when user drags.
- Programmatic pan should not disable follow.
- No map rotation; deferred backlog.

Backward compatibility:
- Follow toggle semantics and `.tracking` visual state remain unchanged.

Phone verification:
- Enable follow, walk/drive until marker nears edge, confirm smooth recenter no more than every 1.5s.
- Drag map and verify follow exits.
- This item is last because it requires movement-based verification that may not be practical between earlier commits.

Risk: Medium, because threshold tuning affects perceived tracking.

## Item 8: Schema Migration And Backfill

Files: `field_reports.json:1-60`, `index.html:1240`, `AGENTS.md:52-70`.

Specific changes:
- Add optional `status` field with allowed values `verified` and `reported`.
- Do not touch or reinterpret existing compact `st`.
- Backfill exactly four IDs with `"status":"verified"` in both `field_reports.json` and embedded `hydrantData`:
  - `field_ba91e3ff`
  - `field_3326a776`
  - `field_1a6e6d56`
  - `field_228b7518`
- Preserve embedded JSON as a single line inside `<script id="hydrantData">`.
- Update `AGENTS.md` schema documentation in the same commit as the data migration; this is an atomic schema change.
- Clarify in docs that `status` is Sprint 1 app-level visual status, while `st` remains source/raw status.

Idempotency:
- Migration script must be re-runnable.
- Match by `i` field.
- If a record already has `status:"verified"`, do nothing.
- If missing or different for one of the four locked IDs, set/update to `verified`.
- Never append duplicate records.

Backup strategy:
- Create local untracked `.bak.<timestamp>` copies before mutation during execution.
- Do not commit backups.

Validation:
- Embedded count remains `6,074`.
- `field_reports.json` count remains `4`.
- Exactly `4` records carry `status:"verified"`.
- `hydrants_varna.json` remains unchanged.

Interactions:
- Item 6 uses this field for visual state.
- Report submission payload is unchanged.

Backward compatibility:
- Older code ignores unknown `status`.
- Canonical upstream file stays clean.

Phone verification:
- After reload, app still shows `6074 точки`.
- Four field reports visually verify once Item 6 is present.

Risk: Low to Medium, because editing the embedded JSON megaline is easy to botch without parser-based mutation.

## Recommended Commit Order

1. Item 8: Schema migration + backfill, data only and invisible.
2. Item 1: Welcome modal, visible but opt-out.
3. Item 6: Status visualization, 3-tier rendering.
4. Item 3: `Тук съм` placement button.
5. Item 4: Auto-zoom при placement.
6. Item 5: Drag pin hint.
7. Item 2: FAB consolidation, largest behavior change.
8. Item 7: Smooth follow re-center.

Rationale:
- Data/schema goes first so visual rendering has a stable field.
- Welcome modal is Step 2 so volunteers who open the link mid-sprint see onboarding before later visual/behavior changes.
- FAB consolidation is late because it changes the main reporting entry point.
- Smooth follow is last because it requires movement-based verification.

## Risk Assessment

| Item | Risk | Main rollback reason |
|---|---:|---|
| Item 8: Schema/backfill | Low-Medium | Embedded JSON edit mistakes |
| Item 1: Welcome modal | Medium | Geolocation prompt delayed or modal layout cramped |
| Item 6: Status visualization | Medium | SVG/anchor/halo or MarkerCluster regressions |
| Item 3: `Тук съм` | Low | Disabled/mobile tooltip behavior unclear |
| Item 4: Auto-zoom | Low-Medium | Motion feels too slow or jarring |
| Item 5: Drag hint | Low | Hint overlaps pin/action bar |
| Item 2: FAB consolidation | Medium | Volunteers confused by global vs per-hydrant signal flow |
| Item 7: Smooth follow | Medium | Recenter feels too eager or too late |

## Sprint 2 Backlog Note

- Interactive pick-mode for global non-new reports is deferred.
- Future behavior may store selected report type and let the next hydrant tap continue directly into that report form.
- Sprint 1 intentionally does not store pending report type; it only instructs the user to tap a hydrant and use the existing per-hydrant flow.

## Estimated File Size Impact

- Start: `index.html` `1,243,208` bytes; embedded JSON `965,686` bytes; hard cap `2 MB`.
- Estimated growth: welcome `+5-8 KB`, FAB/report picker `+1-2 KB`, placement improvements `+3-5 KB`, status SVG/CSS `+2-4 KB`, follow mode `+1 KB`, status data `+100-200 B`.
- Target deployable: about `1.26-1.27 MB`, leaving roughly `730+ KB` before the `2 MB` hard cap.
