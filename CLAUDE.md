# CLAUDE.md

> **Canonical current state:** see `docs/activeContext.md` (last updated commit hash and sprint status). If this file conflicts with `activeContext.md`, the latter wins.
>
> Instructions for **Claude Code** working in this repo.
> Read `AGENTS.md` first for project context, dataset rules, and constraints.

---

## Your Role

You are the **executor** in a tri-agent workflow. See `AGENTS.md` § Tri-agent workflow.

| | Claude (chat) | Codex | **Claude Code (you)** |
|---|---|---|---|
| Decides | yes | no | **no** |
| Plans | yes | yes | **no** |
| Edits files | no | yes after handoff | **yes** |

If you receive a task without an approved plan from Codex, or signed off by Petar in chat, stop and ask. Do not improvise architecture.

---

## Hard Rules

1. **Do not change the runtime dataset casually.** `data/hydrants.json` is the app data file; `hydrants_varna.json` is the original KMZ-derived reference. Dataset/source changes require fresh Codex analysis and explicit Petar approval.
2. **Do not change Bulgarian UI labels** without explicit permission.
3. **Do not introduce dependencies** without Petar approval. No new CDNs, npm packages, or remote fonts.
4. **Preserve static hosting.** GitHub Pages serves `index.html` plus `data/hydrants.json`; no runtime build step.
5. **Stay under the size budget.** Current frontend first load is ~1,259,811 bytes (`index.html` 292,281 + `data/hydrants.json` 967,530). Hard cap is 2 MB.
6. **Mobile-first.** Touch targets >= 44px. Test at 375px viewport width. No hover-dependent workflows.
7. **HTTPS-required APIs are non-negotiable.** Geolocation, DeviceOrientation, and Worker `fetch` report submission must keep working.

---

## Code Style

This codebase is read primarily by AI agents and a non-CS-trained owner.

- Clear names over short names.
- Comments explain **why**, not **what**.
- No clever one-liners. No premature abstraction.
- One concern per function.
- No dead code. If you replace something, delete the old version.

---

## Specific Gotchas

- **`deviceorientation` fires at 100-200Hz on Android.** EMA must run on `requestAnimationFrame`, reading the latest stored raw heading. Do not EMA inside the event handler. `HEADING_SMOOTHING = 0.10`.
- **All map markers use `L.divIcon`**, never `L.icon`.
- **`L.markerClusterGroup` is used only in "Всички" mode.** Other modes use plain numbered pins. Do not unify this.
- **Map auto-fit happens only twice:** first GPS lock and mode change. Never on routine GPS updates.
- **Tap and long-press differ intentionally.** Tap selects/activates a hydrant; long-press opens the report menu.
- **`updateCard()` rebuilds the card HTML on every refresh.** Listeners are re-attached after `innerHTML`; preserve that unless a refactor explicitly changes it.
- **Polling interval is fixed at 15 s (`POLL_INTERVAL_MS`).** Do not lower without coordinating Worker KV cache TTL (currently 30 s) and reviewing the rate math in `docs/plans/commit_15_worker_get.md`.
- **Polling must never block the UI thread.** All work happens inside `async pollIssues()` with a `setTimeout` schedule. Do not call `refresh()` from polling and do not introduce synchronous JSON-walking over the full `HYDRANTS` array.
- **Polling pauses while the tab is hidden** (`document.hidden`) and fires one immediate catch-up poll on return. Preserve both halves — losing the catch-up means stale pins after long backgrounding.
- **Polling updates pins via `marker.setIcon` and `marker.setLatLng`, never by rebuilding** the cluster or calling `refresh()`. Marker tags `_hydrantId` / `_pinKind` / `_rank` / `_isActivePin` are set in `refresh()` and consumed by the polling code; mutating them outside `refresh()` will leak the active-pin flag across transitions.
- **`lastPollSince` only advances on a successful, parseable response.** Failures (network, non-2xx, invalid JSON) keep the cursor where it was so the next poll re-requests the same window.

---

## Field Report Ingest Rules

- **`wrong_location` reports:** update the existing record's `c` coordinate in place. Do **not** create a new `field_*` record. Set `status` to `"verified"` after the coord update.
- For canonical IDs, edit `data/hydrants.json` only.
- For `field_*` IDs, edit both `field_reports.json` and `data/hydrants.json`.
- Log old coords in the commit message for audit trail.
- **`new_hydrant` reports:** only these create new `field_*` records.

See `AGENTS.md` § Wrong-Location Ingest Rule for the full table.

---

## Report Flow

Reports are submitted via `fetch` POST to Cloudflare Worker `varna-hydrants-proxy.petar-dikov2019.workers.dev`. Worker creates a labeled GitHub issue in this repo. Reports queue locally if offline.

Worker source currently lives only in Cloudflare dashboard. TODO commit 17: extract it to `worker/` with deploy notes. Until then, treat the live Worker as canonical.

---

## Verification

No CI yet. Before reporting done:

1. Serve locally over HTTP:

   ```powershell
   python -m http.server 8000
   ```

2. Open at 375px viewport width and check:
   - Map renders within 3 seconds.
   - Browser console has no runtime errors.
   - `data/hydrants.json` loads with HTTP 200.
   - `JSON.parse(document.getElementById('hydrantData').textContent).length === 6079`.
   - GPS lock works, or graceful error pill with retry/manual controls appears.
   - All 3 view modes render correctly: "Близо", "Топ 5", "Всички".
   - Cluster mode shows clusters when zoomed out.
   - Bottom sheet expands/collapses.
   - Compass cone rotates with simulated `deviceorientation` events.
   - FAB `+` opens the report-type menu.
   - Long-press on a verified pin opens the report menu.
   - Follow mode recenters; user pan exits follow mode.
   - Manual position mode accepts a map click.
   - Report submit uses Worker `fetch` POST and queues locally if offline.

3. Report `index.html` and `data/hydrants.json` sizes after changes.

---

## Windows Dev Environment

Defender exclusions applied (2026-05-06):

- ExclusionPath: `C:\Projects\Varna_hydrants`, `C:\Users\Petar\Desktop\Fire_Varna_deploy2`
- ExclusionProcess: `git.exe`, `git-remote-https.exe`, `node.exe`

Primary workflow: edit + commit + push from `C:\Projects\Varna_hydrants` directly. Deploy clone `Fire_Varna_deploy2` is deprecated.

Fallback, only if exclusions fail: Python pre-place blob recovery technique. See git history for full procedure, search "blob corruption".

Verify exclusions monthly:

```powershell
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

---

## What Requires Going Back To Humans

| Situation | Go to |
|---|---|
| Architecture / file layout question | Claude (chat) |
| Data source change | Codex (fresh analysis) |
| Build pushes past 2 MB cap | Petar |
| Bulgarian wording change | Petar |
| New dependency proposal | Petar |
| Anything load-bearing and unclear | Petar |

Asking is cheap. Reverting commits is not.

---

## Workflow Expectations

- **One logical change per commit.**
- **Commit messages in English.**
- Code comments in English. UI strings in Bulgarian.
- Before refactoring, confirm there is an approved Codex plan describing the target structure.
- After any change to the deployable, state files changed, file sizes, and any constraint that came close to being violated.
