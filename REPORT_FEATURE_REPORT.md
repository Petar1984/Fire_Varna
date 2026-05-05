# REPORT_FEATURE_REPORT.md

Execution report for the GitHub Issues volunteer reporting flow defined in
[REPORT_FEATURE_PLAN.md](REPORT_FEATURE_PLAN.md), against
[hydrants_varna_merged.html](hydrants_varna_merged.html).

## Outcome

| Item | Value |
|---|---|
| Modified file | [hydrants_varna_merged.html](hydrants_varna_merged.html) |
| Backup file | [hydrants_varna_merged.html.bak.20260505_025230](hydrants_varna_merged.html.bak.20260505_025230) |
| Final size | **1,238,318 bytes** (1209.3 KB ≈ 1.18 MB) |
| 2 MB hard cap | ✅ under cap |
| Backup size | 1,203,986 bytes (untouched original) |
| 6,070 hydrants load | ✅ confirmed in headless Chromium (`#meta` = `"6070 точки"`) |
| Runtime JS errors | none |
| `hydrants_varna (7).html` | untouched (read-only as instructed) |

Verifier scripts kept in [audit/](audit/) for re-use:
- [audit/verify_report_feature.js](audit/verify_report_feature.js) — static checks: JSON record count, JS parse-validity, size cap, expected/removed token presence.
- [audit/verify_browser.js](audit/verify_browser.js) — Playwright headless Chromium load over a local `http://127.0.0.1:PORT` server, asserts `#meta` shows 6,070 hydrants and the page produces no runtime errors.

## Corrections applied

| Plan said | Actually used | Why |
|---|---|---|
| `GITHUB_API_VERSION = "2026-03-10"` | `GITHUB_API_VERSION = "2022-11-28"` | "2026-03-10" is not a valid GitHub REST API version. Stable version per GitHub docs is `2022-11-28`; sent both as the constant and as the `X-GitHub-Api-Version` header. |
| `Date.toISOString()`-style timestamp | `localISOString()` helper | Plan-corrected per Bulgaria local offset (UTC+02 / UTC+03 EEST). Helper builds ISO string manually with explicit `±HH:MM` offset — no `Z`. |
| `crypto.randomUUID()` only | `uuidv4()` polyfill with `crypto.randomUUID()` fast path | Safari < 15.4 lacks `crypto.randomUUID`; polyfill falls back to `Math.random` UUIDv4. |

## TODO placeholders Petar must fill before deploy

In the new `// ===== Report: GitHub Issues volunteer flow =====` block of
[hydrants_varna_merged.html](hydrants_varna_merged.html):

```js
const GITHUB_REPO_OWNER = "<TODO_PETAR_GITHUB_USERNAME>";  // ← fill
const GITHUB_REPO_NAME  = "Varna_hydrants";                // already set
const GITHUB_PAT        = "<TODO_FINE_GRAINED_PAT>";       // ← fill
```

While these placeholders are present, the code short-circuits before calling
GitHub: it shows "Системата още не е конфигурирана. Свържи се с Петър." and
queues the report into `localStorage` under `hydrants_pending_reports`. Queued
reports retry automatically on the next page load and on the `online` event,
once the placeholders are filled. So a token added later still flushes any
backlog the volunteers accumulated in the meantime.

### Other manual setup before acceptance testing

Per [REPORT_FEATURE_PLAN.md](REPORT_FEATURE_PLAN.md) §"Manual Steps For Petar":

1. **Create fine-grained PAT** named `Varna_hydrants_reports`, repo access
   limited to `Varna_hydrants`, permissions **Issues: read/write** and
   **Metadata: read**, expiration 1 year.
2. **Create labels** in the `Varna_hydrants` repo before acceptance:
   - `report`
   - `exists-confirmed`
   - `missing`
   - `new-hydrant`
   - `wrong-location`
   - `damaged`
   - `pending-review`
   If any are missing, the code falls back automatically: a 422 with a
   "label" message triggers one retry without labels (logged to console),
   and the user sees a soft-warning toast asking them to notify the admin.
3. **Submit one real test report** end-to-end after the PAT is in place;
   verify issue title/body/labels look right; close or delete the test issue.

**Security note** (carried over from plan): embedding a fine-grained PAT in
static HTML exposes it to every user. This is an accepted project risk —
keep permissions minimal (Issues read/write + Metadata read only on
`Varna_hydrants`), and rotate the token if GitHub secret-scanning or abuse
invalidates it.

## CORS / local testing

The deployable **must be served over HTTP(S)**, not `file://`:

- **GitHub Pages** (production) — already HTTPS, no action.
- **Local testing** — start any static file server, e.g.
  `python -m http.server 8080` from the repo root, then open
  `http://localhost:8080/hydrants_varna_merged.html`.
  Or use the verifier helper: `node audit/verify_browser.js` (boots a local
  HTTP server on a random port automatically).

Why `file://` fails:
- Geolocation, DeviceOrientation, `crypto.randomUUID`, and `fetch` to
  `https://api.github.com` all behave differently or refuse to run on the
  `null` origin that browsers assign to `file://` URLs.
- The GitHub Issues API enforces CORS; preflight requests with
  `Origin: null` are rejected.

## What the user sees (flow summary)

Entry points (all four route through `showReportTypePicker(hydrant)` →
`showReportModal(hydrant, reportType)`):

| Entry | Where | Lands on |
|---|---|---|
| Map popup | new `🚨 Докладвай` button inside Leaflet popup (delegated via `popupopen`) | type picker |
| List row | existing `🚨` row button | type picker |
| Active-target card | existing `🚨` card button | type picker |
| `+` Add hydrant | new `addHydrantBtn` next to `📌` | placement mode → `new_hydrant` form (skips picker) |

Type picker offers the four existing-hydrant report types:
`exists_confirmed`, `missing`, `wrong_location`, `damaged`. The
`new_hydrant` flow is reachable **only** from the `+` button per plan.

For `wrong_location` and `new_hydrant`, the form has a "Постави локация на
картата" / "Промени локация" button that hides the modal, switches the map
to long-press placement mode (banner + bottom action bar), and re-opens the
modal with the placed `[lon, lat]` 6-decimal coord once the user taps
`Продължи`. Draft form values are preserved across the placement round-trip.

## Implementation map

All of the following live inside the existing IIFE in the final `<script>`
of [hydrants_varna_merged.html](hydrants_varna_merged.html):

| Plan boundary symbol | Status |
|---|---|
| `showReportModal(hydrant, reportType)` | implemented (3rd `draft` arg added internally for the placement round-trip; still callable as 2-arg) |
| `enterLocationPlacementMode(callback)` | implemented as `enterLocationPlacementMode(initialCoord, callback)`; `initialCoord` is optional, `callback` receives `[lon,lat]` or `null` on cancel |
| `buildReportYAML(report)` | implemented — emits `---`-delimited frontmatter, `null` for absent values, JSON-quoted strings, `[lon,lat]` numeric arrays, and `localISOString()` timestamp |
| `buildIssueTitle(report)` | `[<type>] <hydrant_ref>` for the four existing-hydrant types; `[new_hydrant] @<lat>,<lon>` for new-hydrant reports |
| `submitReport(report)` | POST to `/repos/{owner}/{repo}/issues` with all four required headers; full status-code branching (201 / 401 / 403 / 404 / 410 / 422 / 400 / 503 / network) |
| `queueReport(report)` | implemented (writes to `hydrants_pending_reports`) |
| `retryQueuedReports()` | runs on boot and on `window.online`; transient failures (0/503/403) re-queue, permanent failures drop with a `console.warn` |
| `getReporterName()` / `setReporterName(name)` | implemented (validates length 2–50 before write) |

Spam protection:

- Honeypot input `<input name="website">` rendered with class `.honeypot`
  (positioned `-10000px` off-screen, `tabindex="-1"`, `aria-hidden`); if
  filled, submission is silently discarded.
- 30-second in-memory submit throttle (`SUBMIT_THROTTLE_MS`).
- 5-minute in-memory dedup `Map` keyed by
  `(report_type | hydrant_ref | reporter | reported_coord)`; on hit, asks
  the user to confirm before sending again.

## Constraints status

| Constraint | Status |
|---|---|
| 2 MB hard cap | ✅ 1.18 MB |
| 1 MB ideal | ⚠ exceeded (1.18 MB) — already exceeded by the merged dataset before this change; new code added ~34 KB of script + CSS. No new dependencies. |
| No new runtime/build dependencies | ✅ |
| Mobile-first, ≥ 44px targets | ✅ — type-picker buttons 64px min height, placement action bar 48px, change-name link sized like a chip |
| Bulgarian UI labels | ✅ all new strings in Bulgarian |
| Existing behaviors preserved | ✅ map, GPS, compass, modes, clustering, follow mode, manual position, sheet, popup all untouched (the previous `reportProblem`-only change point) |
| HTTPS-required APIs | ✅ Geolocation/DeviceOrientation/Web Share unaffected; `Web Share` removed (replaced by GitHub Issues) per plan |
| `hydrants_varna (7).html` read-only | ✅ untouched |

## Notes for the next iteration (not blocking)

- `updateCard()` still rebuilds card HTML on every refresh — known tech debt
  in [CLAUDE.md](CLAUDE.md), preserved per the "preserve that pattern unless
  a refactor explicitly addresses it" instruction.
- `hydrants_varna_merged.html` is currently the working target and will need
  to be promoted to `index.html` for GitHub Pages serving (not part of this
  task).
- The new flow does **not** replace existing GPS/navigation/clustering, only
  the report submission path; `navigator.share()` and the SMS fallback have
  been removed as instructed.

— Generated 2026-05-05 by Claude Code (executor).
