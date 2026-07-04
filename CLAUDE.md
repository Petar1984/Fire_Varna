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

Project-wide constraints (size budget, static hosting, Bulgarian UI labels, dependencies, mobile-first, HTTPS-required APIs, Varna-only scope) are canonical in [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). Stop and ask if an approved plan would violate them.

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

See [AGENTS.md § Wrong-Location Ingest Rule](AGENTS.md#wrong-location-ingest-rule) for the canonical table and rules. Stop and ask before any data edit unless the approved plan names the affected report IDs.

---

## Report Flow

See [AGENTS.md § Report Flow](AGENTS.md#report-flow) and [docs/activeContext.md § Current State](docs/activeContext.md#current-state).

---

## Verification

No CI yet, but tests exist (`tests/`, Python `unittest`). When ingest or shared-core (`scripts/lib/hydrant_core.py`) behavior is relevant, run the suite:

```powershell
python -m unittest discover -s tests
```

For frontend / deployable changes, before reporting done:

1. Serve locally over HTTP:

   ```powershell
   python -m http.server 8000
   ```

2. Open at 375px viewport width and check:
   - Map renders within 3 seconds.
   - Browser console has no runtime errors.
   - `data/hydrants.json` loads with HTTP 200.
   - `JSON.parse(document.getElementById('hydrantData').textContent).length` equals the current expected count declared in [`docs/activeContext.md`](docs/activeContext.md#current-state) (currently `7238`).
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

See [AGENTS.md § Windows Dev Environment](AGENTS.md#windows-dev-environment).

---

## What Requires Going Back To Humans

See [AGENTS.md § Tri-Agent Workflow](AGENTS.md#tri-agent-workflow) for the canonical approval gates. Asking is cheap. Reverting commits is not.

---

## Workflow Expectations

- **One logical change per commit.**
- **Commit messages in English.**
- Code comments in English. UI strings in Bulgarian.
- Before refactoring, confirm there is an approved Codex plan describing the target structure.
- After any change to the deployable, state files changed, file sizes, and any constraint that came close to being violated.
- After any governance section rename, run grep for old section names and update Markdown anchor links in the same pass.
