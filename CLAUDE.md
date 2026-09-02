# CLAUDE.md

> **Canonical current state:** see `docs/activeContext.md` (last updated commit hash and sprint status). If this file conflicts with `activeContext.md`, the latter wins.
>
> Instructions for **Claude Code** working in this repo.
> Read `AGENTS.md` first for project context, dataset rules, and constraints.

---

## Orientation (repo · trunk · forbidden · entry point · live numbers)

- **What this repo is.** `Fire_Varna` — the mobile-first web app that shows a firefighter the nearest working fire hydrant in Varna oblast, in the browser, with no install and no account (`README.md` § Български). The app shell (`index.html`), the dataset (`data/`), the ingest and audit scripts (`scripts/`, `audit/`), the tests (`tests/`), the Cloudflare Worker source (`worker/`) and the governance documents (`docs/`) all live in this one repo.
- **Trunk.** `main` — GitHub's default branch (`git symbolic-ref refs/remotes/origin/HEAD` → `refs/remotes/origin/main`) and the branch the site is published from ([AGENTS.md § What This Project Is](AGENTS.md#what-this-project-is): "Distribution: GitHub Pages from `main`"). Work commits land here; every other branch is a frozen trace of a past cycle, listed by `git branch -avv` and dated by `git for-each-ref --sort=-committerdate --format='%(refname:short) %(committerdate:short)' refs/heads refs/remotes`. Petar alone pushes (Gate 2), so `main` can stand ahead of `origin/main` between his pushes — measure that with `git rev-list --count origin/main..main`, never resolve it with `git push`.
- **What is forbidden here.** § Hard Rules below — never push · never commit secrets · field-report PII gate · destructive-op gate · cross-repo isolation · no automated commits — plus [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). A rule you are about to bend is the signal to stop and ask, not to improvise.
- **Entry point.** [`docs/activeContext.md`](docs/activeContext.md#current-state) — read it before anything else when resuming work. On current state it wins over this file (see the header above).
- **Live numbers.** No state number enters this file. Record counts, byte sizes and commit hashes live in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state) — one truth per document. The numbers that do stay here are rules, not state: the 15 s poll interval (`POLL_INTERVAL_MS`), the 5 MB first-load hard cap ([AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints)), `HEADING_SMOOTHING = 0.10`. If you need a fresh count, run the command — do not write the result into this file.

---

## Your Role

You are the **Executor** in the dual-Claude-Code pipeline. See `AGENTS.md` § Dual-Claude-Code workflow, and ADR [`docs/decisions/003_dual_claude_code_governance.md`](docs/decisions/003_dual_claude_code_governance.md).

| Role | Agent | What it does |
|---|---|---|
| **Planner** | Claude Code — read-only (model per `~/.claude/agents`) | Plans, architects, measures, drafts the plan. Never edits or commits. |
| **Researcher** | Claude Code — read-only (model per `~/.claude/agents`) | Planner sub-phase: gathers evidence and measurements. Never edits. |
| **Executor (you)** | Claude Code (model per `~/.claude/agents`) | Implements the signed plan, edits files, commits locally. Never pushes, never architects. |
| **Auditor** | Claude Code — read-only, adversarial (model per `~/.claude/agents`) | Independently checks the Executor's diff against the plan. Never edits. |
| **Orchestrator** | Petar | Signs plans (Gate 1), reviews diffs (Gate 2), pushes. Sole push authority. |

If you receive a task without an approved plan from the **Planner** (read-only; model per `~/.claude/agents`), signed by Petar, stop and ask. Do not improvise architecture.

---

## Hard Rules

Project-wide constraints (size budget, static hosting, Bulgarian UI labels, dependencies, mobile-first, HTTPS-required APIs, Varna-only scope) are canonical in [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). Stop and ask if an approved plan would violate them.

### Non-negotiable guardrails (harmonized with Varna_buildings)

1. **Never run `git push`.** Petar pushes manually after reviewing commits locally, at Gate 2. This holds with any flag; never use `--no-verify` and never bypass the pre-push hook.
2. **Never commit secrets.** No Cloudflare API tokens, Worker deploy credentials, `wrangler` secrets, `.dev.vars`, or `.env` files ever enter the repo. Verify `.gitignore` covers them before staging if in doubt.
3. **Field-report / PII gate.** Treat field-report submissions as personal data: reject by default, and scrub any identifying content before persisting to `data/` or creating a GitHub issue. Stop and ask before persisting anything that could carry PII.
4. **Destructive-op gate.** If you discover unexpected state — unfamiliar branches, uncommitted changes, files you did not create — investigate before deleting or overwriting. It may be Petar's in-progress work.
5. **Cross-repo isolation.** Do not touch the `Varna_buildings` checkout, or any other repo, from here. Work stays inside `C:\git\Fire_Varna`.
6. **No automated commits.** One logical change per commit, staged with explicit paths, using the exact commit message from the approved plan.

### Per-commit execution protocol

For each commit in an approved plan:

1. Read the commit specification in the plan.
2. Verify dependencies on earlier commits are met.
3. Create or modify only the files the spec names.
4. Stage those files with **explicit paths** (never `git add -A` / `git add .`) and commit with the **exact** message from the plan.
5. Run `git status --short` to confirm only the intended files were committed and pre-existing dirty/untracked files were left untouched.
6. Report commit number, hash, files, and acceptance-check result.
7. If an acceptance check fails, **stop and ask Petar.** Do not roll forward with a broken commit.

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
- **Map auto-fit happens at three sites, never on routine GPS updates:** the first GPS lock (`refresh(!deepLinkFramed)` — skipped when a `?h=` deep link already framed the map on one hydrant), `setMode()`, and the manual-position map click. Routine GPS ticks call `refresh(false)`.
- **Tap and long-press differ intentionally.** Tap selects/activates a hydrant; long-press opens the report menu.
- **`targetCardHTML()` builds the card HTML into `modalBody.innerHTML` at two call sites.** In `showReportModal()` the listeners are re-attached right after by `wireReporterBar()` + `wireFormHandlers()`; in `showReportTypePicker()` by `wireReporterBar()` + the inline `.type-btn` handlers; preserve that unless a refactor explicitly changes it.
- **Polling interval is fixed at 15 s (`POLL_INTERVAL_MS`).** Do not lower without coordinating Worker KV cache TTL (currently 30 s) and reviewing the rate math in `docs/plans/commit_15_worker_get.md`.
- **Polling must never block the UI thread.** All work happens inside `async pollIssues()` with a `setTimeout` schedule. Do not call `refresh()` from polling and do not introduce synchronous JSON-walking over the full `HYDRANTS` array.
- **Polling pauses while the tab is hidden** (`document.hidden`) and fires one immediate catch-up poll on return. Preserve both halves — losing the catch-up means stale pins after long backgrounding.
- **Polling updates pins via `marker.setIcon` and `marker.setLatLng`, never by rebuilding** the cluster or calling `refresh()`. Marker tags `_hydrantId` / `_pinKind` / `_rank` / `_isActivePin` are set in `refresh()` and consumed by the polling code; mutating them outside `refresh()` will leak the active-pin flag across transitions.
- **`lastPollSince` only advances on a successful, parseable response.** Failures (network, non-2xx, invalid JSON) keep the cursor where it was so the next poll re-requests the same window.

---

## Field Report Ingest Rules

See [AGENTS.md § Wrong-Location Ingest Rule](AGENTS.md#wrong-location-ingest-rule) for the canonical table and rules. Stop and ask before any data edit unless the approved plan names the affected report IDs.

A canonical coordinate mutation follows the **Measurement Doctrine** — ADR [`docs/decisions/004_measurement_doctrine.md`](docs/decisions/004_measurement_doctrine.md) (references Varna_buildings ADR 058): clear the acceptance floor before mutating `coords`; Google terrain-eyes may only refute / downgrade / trigger a re-check, never rewrite a coordinate alone, never be cached or fed back to OSM.

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
   - `JSON.parse(document.getElementById('hydrantData').textContent).length` equals the record count declared in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state) — the count is not written here; read it there, or measure `data/hydrants.json` yourself.
   - GPS lock works, or graceful error pill with retry/manual controls appears.
   - All 3 view modes render correctly: "Близо", "Топ 5", "Всички".
   - Cluster mode shows clusters when zoomed out.
   - Building detail sheet (`.detail-sheet`, the C4 search result) opens and closes; the hydrant bottom sheet no longer exists — it was removed in the popup pivot.
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

See [AGENTS.md § Dual-Claude-Code Workflow](AGENTS.md#dual-claude-code-workflow) for the canonical approval gates. Asking is cheap. Reverting commits is not.

---

## Workflow Expectations

- **One logical change per commit.**
- **Commit messages in English.**
- Code comments in English. UI strings in Bulgarian.
- Before refactoring, confirm there is an approved Planner plan signed by Petar describing the target structure.
- After any change to the deployable, state files changed, file sizes, and any constraint that came close to being violated.
- After any governance section rename, run grep for old section names and update Markdown anchor links in the same pass.
