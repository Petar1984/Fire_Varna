# Navigation Accuracy Fix — Implementation Plan

**Author:** Codex (planning), Claude chat (audit)
**Date:** 2026-05-05
**Status:** Approved — awaiting execution
**Scope:** index.html navigation accuracy
**Estimated commits:** 6 (sequential)

## Context

User reports three navigation issues on the live PWA:
1. Direction arrow points wrong way while driving
2. Direction indicator trembles/flickers when stationary
3. GPS feels imprecise

## Root causes identified

- **A.** Orientation source race — both `deviceorientationabsolute` and `deviceorientation` bound to same handler, last-event-wins
- **B.** EMA without deadband — sub-degree noise propagates every frame
- **C.** Snap rotations — no CSS transition between rAF ticks
- **D.** GPS `coords.heading` and `coords.speed` never read
- **E.** `lastFix` accepts every position regardless of accuracy

## Decisions locked

- Driving over walking — emergency vehicle priority (`MOVING_SPEED_ENTER_MPS = 1.4`)
- 3-second movement hold before GPS heading activates (`MOVING_HOLD_TIME_MS = 3000`)
- CSS transitions: 70ms arrow, 80ms marker
- Source-switch snap threshold: 60° angular delta
- Manual-source override: any GPS fix accepted unconditionally after manual mode

## Implementation order

1. **A** — Orientation source race fix
2. **B** — EMA deadband
3. **C** — CSS transitions + source-switch snap
4. **E** — GPS fix filtering
5. **D** — GPS travel heading hybrid
6. **Chevron** — visual replacement of cone

Single commit per issue. Verify on phone between commits.
Rollback strategy: `git revert <hash>` for any failing commit.

## Open items (post-execution)

- Optional Bulgarian calibration hint — pending owner approval
- Magnetometer figure-8 calibration detection on Android — logged for future iteration
- Service worker for offline tile cache — separate workstream

---

## Detailed plan (from Codex, revision 2)

# Revised Navigation Accuracy Fix Plan for `index.html`

## Executive Summary
- Modify only `index.html`; no new files, dependencies, service worker, build step, or dataset changes.
- Fix order is A → B → C → E → D → Chevron, with the orientation race handled first.
- Keep iOS compass permission flow and the existing rAF-batched heading pipeline.
- Prefer GPS travel heading only after stable movement; keep stationary display calm.
- Expected size increase is small; current `index.html` is `1,241,662` bytes, safely under the 2 MB cap.

## A. Orientation Source Race

Files to modify: `index.html:1255-1301`, `index.html:1717-1750`.

Specific changes:
- Replace the anonymous `handler` in `attachOrientation()` with `readOrientationHeading(event)` and `handleCompassHeading(sample)`.
- Prefer `webkitCompassHeading`, then absolute `deviceorientationabsolute`, then relative `deviceorientation` only as fallback.
- Inspect `event.absolute`; do not let non-absolute `deviceorientation` overwrite a recent absolute/webkit heading.
- Inspect `webkitCompassAccuracy`; ignore poor iOS compass samples when a better heading already exists.
- Preserve `needsCompassPerm`, `compassPermBtn`, and `requestCompassPerm()` behavior.

Constants:
- `ABSOLUTE_ORIENTATION_STALE_MS = 1500`
- `WEBKIT_COMPASS_MAX_ACCURACY_DEG = 45`

rAF/EMA interaction:
- Orientation events only store an accepted compass sample and request an rAF update.
- EMA remains inside `scheduleArrowUpdate()` only.

Edge cases:
- Accept iOS `webkitCompassHeading` even when `event.absolute` is missing.
- Allow relative Android heading only before an absolute source appears or after it is stale.
- Ignore invalid heading/accuracy values silently.

Backward compatibility:
- Works on iOS Safari permission-gated compass and older Android `deviceorientation`.
- No listener option or API dependency changes.

Verification:
- On iOS, tap `Активирай компас`; heading should work after permission.
- On Android, rotating while stationary should no longer flip between absolute and relative readings.
- Existing no-compass fallback must still show when no usable heading exists.

Risk:
- Low to medium; most likely tuning risk is rejecting too many low-quality iOS samples.

## B. EMA Deadband

Files to modify: `index.html:1255-1259`, `index.html:1679-1701`.

Specific changes:
- Keep `HEADING_SMOOTHING = 0.10`.
- Add `normalizeDegrees`, `angularDelta`, and `unwrapAngleNear`.
- Update `smoothHeading(raw, alpha)` to use shortest-path math.
- Deadband check must use `Math.abs(angularDelta(raw, smoothedHeading))`, not raw subtraction; this is required for correct `0/360` and `±180°` behavior.
- Track unwrapped display rotation internally so visual rotation can continue through north without long spins.

Constants:
- `HEADING_DEADBAND_DEG = 2`
- `HEADING_SMOOTHING = 0.10`

rAF/EMA interaction:
- Deadband is applied during the single rAF smoothing step.
- Sub-degree sensor noise no longer causes DOM transform writes every frame.

Edge cases:
- First valid heading initializes immediately.
- Crossings like `359° → 1°` use a `2°` delta.
- Large turns still smooth normally.

Backward compatibility:
- Pure math/helper changes; no browser API impact.
- If no heading exists, `smoothedHeading` remains `null`.

Verification:
- Stationary phone should stop trembling.
- Slow rotation below `2°` should hold steady; larger rotation should move smoothly.
- Crossing north should not spin the long way.

Risk:
- Low; only responsiveness tuning risk.

## C. Transform Transition Smoothing

Files to modify: `index.html:857-875`, `index.html:1153-1166`, `index.html:1393-1398`, `index.html:1704-1712`.

Specific changes:
- Add CSS transform transitions to `.arrow-tri` and `.user-cone`.
- Use unwrapped transform values when writing `style.transform`.
- Add `lastArrowRotation` and unwrap target-relative arrow rotations.
- Add reduced-motion override to remove or minimize transitions.
- Make source-switch snapping explicit: when switching between compass and GPS heading sources, if angular delta between current display and new source exceeds `HEADING_SOURCE_SWITCH_SNAP_DEG`, snap with transition temporarily disabled instead of animating the long way around.

Constants:
- `--heading-arrow-transition-ms: 70ms`
- `--heading-marker-transition-ms: 80ms`
- `HEADING_SOURCE_SWITCH_SNAP_DEG = 60`

rAF/EMA interaction:
- rAF still decides each heading value; CSS only eases the visual transform between applied values.
- Short durations avoid visible lag relative to the 16ms rAF cadence.

Edge cases:
- Bottom-card HTML is rebuilt in `updateCard()`; class-based CSS must still apply.
- Reduced-motion users should not get animated rotation.
- No touch target or UI label changes.

Backward compatibility:
- Browsers without CSS transitions fall back to current snapping.
- No new runtime assets.

Verification:
- Rotate slowly and confirm no snap/flicker.
- Confirm no noticeable lag while moving.
- Confirm bottom card buttons still work after `updateCard()` rebuilds HTML.

Risk:
- Low; transition duration is intentionally short.

## E. GPS Fix Filtering

Files to modify: `index.html:1297`, `index.html:1324-1365`, `index.html:1377-1382`, `index.html:2542`.

Specific changes:
- Add `normalizePosition(pos)` to create `{ lat, lon, acc, ts, speed, gpsHeading, source: "gps" }`.
- Add `shouldAcceptFix(candidate, previousFix)` and call it at the start of `onLocation(pos)`.
- Reject invalid coordinates, very inaccurate fixes, stale worse fixes, and implausible jumps when a better recent GPS fix exists.
- If previous fix source is `"manual"`, accept any GPS fix unconditionally regardless of accuracy comparison.
- Rejected fixes must not mutate `lastFix`, move markers, refresh hydrants, alter follow mode, or enqueue GPS heading.
- Manual map click at `index.html:2542` should set `{ source: "manual", ts: Date.now(), speed: null, gpsHeading: null }`.
- Replace geolocation option literals with named constants and reduce watch `maximumAge` from `5000` to `1000`.

Constants:
- `GEOLOCATION_TIMEOUT_MS = 20000`
- `GEOLOCATION_MAXIMUM_AGE_MS = 1000`
- `GPS_ABSOLUTE_MAX_ACCURACY_M = 500`
- `GPS_WORSE_ACCURACY_DELTA_M = 40`
- `GPS_WORSE_ACCURACY_RATIO = 2.5`
- `GPS_STALE_FIX_MS = 15000`
- `GPS_IMPLAUSIBLE_SPEED_MPS = 50`

rAF/EMA interaction:
- Rejected GPS fixes do not feed the heading pipeline.
- Accepted fixes may feed GPS travel heading later in Issue D.

Edge cases:
- First usable GPS fix stays permissive.
- A stale old fix should not block recovery.
- A much more accurate fix can replace a bad location even after a jump.
- No new Bulgarian status text; avoid alert spam.

Backward compatibility:
- Handles missing `accuracy`, `speed`, `heading`, and `timestamp` conservatively.
- Keeps `enableHighAccuracy: true`.

Verification:
- After good outdoor lock, moving indoors should not cause wild jumps.
- Manual mode followed by locate should allow GPS to replace manual position.
- Accuracy circle should reflect only accepted fixes.
- Follow mode should not chase rejected cached/bad fixes.

Risk:
- Medium; over-filtering could hold an old position, mitigated by stale-time and manual-source override.

## D. GPS Travel Heading While Moving

Files to modify: `index.html:1255-1305`, `index.html:1351-1365`, `index.html:1650-1712`, `index.html:1717-1733`.

Specific changes:
- Add movement state: `isMoving`, `movingSinceTs`, `lastHeadingSource`, and latest accepted compass sample.
- Add `extractGpsMotion(candidate, previousFix)` to read `coords.heading` and `coords.speed`.
- Add fallback derived bearing from previous accepted GPS fix when browser GPS heading is missing and movement distance is reliable.
- Use confirmed driving-first threshold: `MOVING_SPEED_ENTER_MPS = 1.4`.
- Require movement to remain active for `MOVING_HOLD_TIME_MS = 3000` before GPS heading activates.
- Exit moving state only below `MOVING_SPEED_EXIT_MPS`, preventing threshold flicker.
- While GPS-heading mode is active, ignore compass samples for display heading.
- When stationary or GPS heading is stale, resume compass display if available.
- `updateArrow()` should use the current display heading source, not specifically compass heading.
- `updateCardInfo()` should show existing `(без компас)` only when there is no display heading at all.

Constants:
- `MOVING_SPEED_ENTER_MPS = 1.4`
- `MOVING_SPEED_EXIT_MPS = 0.8`
- `MOVING_HOLD_TIME_MS = 3000`
- `GPS_DERIVED_HEADING_MIN_DISTANCE_M = 8`
- `GPS_HEADING_SMOOTHING = 0.35`
- `GPS_HEADING_STALE_MS = 4000`
- `HEADING_SOURCE_SWITCH_SNAP_DEG = 60`

rAF/EMA interaction:
- GPS fixes enqueue heading samples into the same rAF pipeline.
- GPS uses `GPS_HEADING_SMOOTHING = 0.35` for faster convergence while driving.
- Source-switch snap rule from Issue C applies when moving between compass and GPS heading sources.

Edge cases:
- Do not trust `coords.heading` when speed is missing, zero, `NaN`, or below moving threshold.
- Brief speed dips should not immediately return to compass because of hysteresis and hold logic.
- Manual-source fixes must not derive travel heading.
- Rotating the phone while driving should not override travel direction.

Backward compatibility:
- If `coords.heading` is missing, derived bearing from accepted fixes still works.
- If `coords.speed` is missing, movement can be inferred from distance/time.
- iOS compass permission remains useful for stationary use.

Verification:
- Drive straight: marker/arrow should align with travel direction, even if phone orientation changes.
- Stop for a few seconds: display should stay stable, not tremble.
- Walk/stand: app should favor stationary behavior, not jump into GPS-heading mode too eagerly.
- Rotate phone while moving: travel direction should remain dominant.

Risk:
- Medium; movement thresholds affect walking behavior, but the confirmed priority is emergency vehicle driving.

## Chevron Direction Marker

Files to modify: `index.html:1153-1166`, `index.html:1369-1373`, `index.html:1387-1398`.

Specific changes:
- Replace the `.user-cone` `clip-path` triangle visual with an inline SVG chevron inside the existing `.user-cone` wrapper.
- Keep divIcon structure as `<div class="user-cone hidden">...svg...</div><div class="user-dot"></div>`.
- Keep `updateUserCone()` selecting `.user-cone`, toggling `.hidden`, and applying `transform` to the wrapper.
- SVG should use `viewBox="0 0 100 100"`, point upward at `0°`, and stay centered on `50,50`.
- Do not use external SVG files, data URLs, icon libraries, or `L.icon`.

Constants:
- Keep existing `iconSize: [100, 100]` and `iconAnchor: [50, 50]`.

rAF/EMA interaction:
- Chevron uses the same display-heading transform as the current cone.
- Existing hidden fallback at `index.html:1393-1395` remains intact.

Edge cases:
- If no heading exists, only the blue dot is visible.
- SVG remains non-interactive with `pointer-events: none`.
- No Bulgarian wording changes.

Backward compatibility:
- Inline SVG stays self-contained and avoids `clip-path` reliance.
- If SVG rendering fails, the user dot remains usable.

Verification:
- With heading available, marker should read as direction-of-travel, Waze-style.
- With no compass/GPS heading, chevron should be hidden.
- Marker must remain centered exactly over the accepted position.

Risk:
- Low; visual interpretation should be checked on an actual phone.

## Recommended Commit Order

1. A: Orientation source race and source priority.
2. B: EMA deadband with shortest-path angular delta.
3. C: Short CSS transitions and source-switch snap behavior.
4. E: GPS fix normalization/filtering and manual-source override.
5. D: GPS travel-heading hybrid with 3-second movement hold.
6. Chevron: Replace cone triangle with inline SVG chevron.

## Final Verification Checklist

- Manual mobile smoke test from `CLAUDE.md`: GPS lock/error pill, all three modes, bottom sheet, compass rotation, report modal, follow mode, manual mode.
- Navigation test: stationary stability, Android/iOS compass, drive test, stop test, poor-GPS rejection, manual-to-GPS recovery.
- 375px viewport check for no overlap and no touch target regression.
- Confirm `index.html` remains self-contained and under 2 MB; report final byte size after implementation.

## Open Owner Decisions

- No new user-facing text is planned.
- Optional calibration hint would require Petar approval. Suggested wording if requested later: `Калибрирайте компаса` or `Завъртете телефона за калибрация на компаса`.

---

## Audit notes (Claude chat)

Implementation reminders not part of the formal plan but to be honored during execution:

### 1. updateCard() rebuild + transitions interaction

`updateCard()` rebuilds bottom-card innerHTML, recreating `.arrow-tri`. With CSS transition active, the new element starts at `transform: rotate(0deg)` (default) and animates to its target value, producing a visible spin on every card rebuild.

**Fix during commit C:** on first transform write after rebuild, temporarily disable transition (`element.style.transition = 'none'`), apply transform, force reflow (`void element.offsetHeight`), re-enable transition. Standard technique. Without it, every card refresh shows a 0° → target spin.

### 2. Transition timing tuning

70ms (arrow) and 80ms (marker) are starting points. With 16ms rAF cadence, this gives 4-5 frames of perceptual lag. If on-phone testing shows visible delay, reduce to 50ms or 40ms. This is parameter tuning, not plan revision.

### 3. Phone verification gate between commits

After commit 1 (Issue A), mandatory testing before commit 2:
- Drive 5–10 minutes on real road, observe arrow direction
- Stand still 30+ seconds, observe stability
- Try iOS compass permission flow if available

If any regression — pause, investigate, do not proceed to next commit.

Same gate after every subsequent commit.

### 4. Constants location convention

All new constants (timing, thresholds, smoothing factors) should be co-located with existing `HEADING_SMOOTHING` constant near `index.html:1258`. Do not scatter them across the file.

### 5. Manual-source override criticality

The rule "if previous fix source is manual, accept any GPS fix unconditionally" is non-obvious but critical. Without it, switching from manual mode to real GPS would be blocked because manual `acc=0` is "perfect" and any real GPS appears worse. Test this transition explicitly during Issue E verification.
