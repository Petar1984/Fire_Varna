# Active context - Fire_Varna

> **Audience:** Petar and AI agents resuming work.
> **Purpose:** canonical current repo/runtime state. If this conflicts with README, AGENTS.md, or CLAUDE.md on current state, this file wins.

Last updated: 2026-07-04 (post Address-fill B2 ship + FF-002 cycle; approx search DARK by release doctrine)
Sprint: post-Sprint 1.5. Shipped since: Phase 2 verbose-schema migration, compact-schema compatibility removal, dataset cleanup (6,082 -> 5,911), address backfill, Worker source extraction to `worker/`, label-gated issue ingest, line-ending (EOL) hygiene, and H1 shared-core + spatial dedup. Phase 2 Fire_Varna reintegration into the Varna_buildings map is in planning under ADR 020 Amendment 2 (tracked in the Varna_buildings repo).

## Current State

- Branch: `main`; HEAD at `72b5bcd` (approx flag OFF). B2 shipped a86eeeb→2e2bb43 (ADR 001, bundle, search integration, revised trigger), then FF-002 hotfix chain: kill switch a3cb0da → v1.0.2 bad8dc0 → flag-on 7aa9129 (+retrigger 06e6006) → final flag OFF 72b5bcd.
- index.html: ~417,5xx worktree bytes (2e2bb43 measured 417,515 + one-line flag flips). The earlier 400,524-byte figure was the pre-B2 (`020db19`) snapshot.
- **Approx address search (ADR 001, Accepted): DARK.** `APPROX_ADDRESS_SEARCH_ENABLED = false` — release doctrine (Petar 2026-07-04): feature stays off until B3 distributes clustered positions; re-enable = ONE clean launch through all gates + blind sample. `data/approx_addresses_v1.json` (v1.0.3, 8,361 rows, SHA-guarded by `tests/test_approx_addresses_public_bundle.py`) sits inert in the repo — never fetched while the flag is off (D5 fallback = pre-B2 behavior, verified live). v1.0.4 (8,728 rows, superset after FF-002 root-cause un-merge) exists LOCAL-ONLY in the Varna_buildings pipeline (`m6000_private/r511f289ed552`), NOT published. True-missing baseline after root-cause: 23,632. Canon: `Varna_buildings/scratch/address_fill_phase_b*_codex_plan.md`, `ff002_root_cause_cycle_plan.md`, `field_feedback_log.md` (FF-001/FF-002).
- data/hydrants.json: **7,238 records**, 1,221,809 worktree bytes (gzip level-9 218,351). **Dataset growth 5,911 → 7,238 (+1,327): post-2026-06-21 ЕТР imports** (`etr_varna` 764 + `etr_provadia` 245 + `etr_dolni_chiflik` 219 + `etr_devnya` 78 = 1,306) plus `field_report` 24 → 45 (+21). The earlier 5,911-record / 874,593-byte figure was the pre-import snapshot; the 968,365-byte / 6,082-record file was the older pre-cleanup snapshot.
- data/hydrants_provenance.json: 1,364,172 worktree bytes (cleanup/migration provenance archive).
- `field_reports.json`: not present in the current repo. New `field_*` records live in `data/hydrants.json` only. (Historical mentions of `field_reports.json` in dated docs/plans are point-in-time records.)
- Current schema: verbose hydrant records — `id`, `coords` `[lon,lat]` WGS84, `origin` (`vik`/`national`/`field_report`), `legacy_ids` (all present), plus sparse `type` / `region` / `address` / `existence_status` / `operational_status` / `review_status` / `report_id` / `reported_at`. Compact-schema compatibility has been removed. See [AGENTS.md § Data Model](../AGENTS.md#data-model).
- Status counts (in repo, 7,238-record baseline): 75 verified (`existence_status`), 6 reported/review (`review_status`), 7,157 canonical/unreviewed. Runtime can grow via polled new_hydrant reports.
- Origin counts (7,238-record baseline): `vik` 3,542; `national` 2,345; `etr_varna` 764; `etr_provadia` 245; `etr_dolni_chiflik` 219; `etr_devnya` 78; `field_report` 45. (The `etr_*` origins are the post-2026-06-21 ЕТР imports; AGENTS.md § Data Model still lists only `vik`/`national`/`field_report` — a follow-up doc pass should widen it.)
- Enrichment counts (7,238-record baseline): 555 with address; 2,336 with type; 47 with operational status.
- Deploy: GitHub Pages from main -> https://petar1984.github.io/Fire_Varna/
- Worker: varna-hydrants-proxy.petar-dikov2019.workers.dev
  - POST `/` endpoint: creates labeled GitHub issues.
  - GET `/issues` endpoint: 30s KV-cached.
  - Worker code source of truth is now `worker/` (extracted to repo in `914dc2a`); see `worker/README.md`. Cloudflare deployment remains manual unless another current doc says otherwise.
  - Worker deploy version: repo-declared `5accc88e`.
  - KV namespace: `varna_hydrants_reports_cache`, binding `REPORTS_CACHE`
  - Rollback version (last POST-only): `e86c90a6`
- Endpoint liveness: Pages endpoint liveness verified 2026-06-21; deploy version repo-declared; served 5,911 hydrant points. Worker `GET /issues` endpoint liveness verified 2026-06-21; deploy version repo-declared; 30s KV cache, `stale:false`, `cached_at 2026-06-21`.
- Frontend polling: client `GET /issues` every 15 s with `?since=<cached_at>` delta, paused on `document.hidden`, immediate catch-up on visibility return, silent retry on failure (cursor not advanced).
- Polling dedupe: fixed 2026-05-08, dual-format ID check (8bd123e) — `applyReports` checks both the full-UUID `report.id` and the truncated `field_<8>` form against `HYDRANTS_BY_ID` so polled new_hydrant records do not double-render after ingest.

## Recent Completed Work (since 2026-05-09)

Newest first; commit hashes from `git log`. These post-date the Sprint 1.5 snapshot below.

- **H1 shared hydrant core + spatial dedup (`38ebbad`, 2026-06-22)** — reusable `scripts/lib/hydrant_core.py`; deterministic spatial matcher (`Rm = 5 m`, `Rf = 20 m`) drives the `new_hydrant` path into UPDATE (<=5 m) / FLAG ((5 m, 20 m]) / ADD (>20 m); the other handlers (`exists_confirmed`, `damaged`, `missing`, `wrong_location`) stay byte-identical. Refactor plus tests; CLI dry-run by default. Plan status-stamped in `docs/plans/h1_shared_core_spatial_dedup.md`.
- **Line-ending (EOL) attributes (`47cd3ed`)** — repository line-ending hygiene.
- **Label-gated issue ingest** — batch ingest of 24 approved reports (`a4bd946`); reports #62 and #48 (`791d817`). Moderation now gated via GitHub issue labels.
- **Worker hard cap raised to 5 MB (`aa7897e`).**
- **Address backfill + pre-sprint snapshots (`209bb36`)** — address-backfill script; 555 records now carry an address.
- **Canonical type + operational pickers with moderation gate (`797b357`).**
- **Worker source extracted to repo (`914dc2a`)** — Worker code now lives in `worker/`; the live Worker is no longer the only source.
- **Phase 2 verbose-schema migration (`10bb67a`)** and **compact-schema compatibility removal (`142a494`)** — runtime dataset migrated to verbose records; the dual-schema adapter was retired.
- **Dataset cleanup `6,082 -> 5,911`** — duplicate/invalid records removed during the migration; provenance archived in `data/hydrants_provenance.json`.

## Intentions / Backlog

Documented future intentions (not scheduled; no implementation in this doc-sync pass):

- **Street View on each hydrant detail** — surface a Street View link/view on the per-hydrant detail later.
- **Integrated Phase 2 UI** — an integrated UI built on the Varna_buildings interface, OSM basemap by default, with hydrant data in a separate panel. Tracked cross-repo under ADR 020 Amendment 2 (Varna_buildings repo).

## Sprint 1 Status

Completed:

- Repo cleanup: removed stale report-plan/report-output docs and local cruft.
- Data extraction: moved embedded hydrant JSON from `index.html` to `data/hydrants.json`.
- Doc sync: updated `AGENTS.md`, `CLAUDE.md`, and this active context to runtime reality.
- Commit 15: Worker GET `/issues` + KV cache deployed and validated.
- Commit 16: client polling of GET `/issues` every 15 s with marker status merge deployed and validated.

Remaining: none — Sprint 1 complete.

## Sprint 1.5 Status

Plan: [`docs/plans/sprint_1_5_polish.md`](plans/sprint_1_5_polish.md). Two-commit grouping shipped on 2026-05-07.

Completed:

- **Cosmetic batch (`8e549e1`)** — welcome modal screen-2 text rewritten to name current gestures (long-press for report, `+` for picker); report-modal target card now displays `Тип: Подземен/Надземен` for recognized values via new `hydrantTypeLabel()` helper. `index.html` +527 bytes.
- **Behavior batch (`7412878`)** — all-mode cluster guard + ID-based active target. `allClusterInteractionOpen` flag wired to MarkerCluster `spiderfied` / `unspiderfied` events suppresses routine GPS `refresh(false)` while a spiderfy is open. New `activeTargetId` is the source of truth for the selected hydrant, with `activeTargetIdx` retained as a derived list/rank helper. New helpers: `getActiveTarget`, `setActiveTargetHydrant`, `createActiveOverlayMarker`, `updateAllModeActiveOverlay`, `redrawActiveLine`, `onUserMovedLightweight`. Tap on any 'Всички' pin (including spiderfied children, including hydrants outside the visible nearest-10) selects without rebuilding the cluster; long-press selects then opens the report picker. Polling-driven `wrong_location` moves on the active hydrant redraw the dashed line + card + arrow without `refresh()`. `index.html` +5,985 bytes.

Total Sprint 1.5 footprint: `index.html` 298,207 → 304,192 (+6,512 bytes / +6.36 KB; first load now 1,271,722 bytes, well under the 2 MB hard cap). The original 3 KB self-imposed Sprint 1.5 cap was breached on the behavior batch; treated as a soft planning anchor, not a technical limit.

Tested at 375 px viewport: smoke regression clean (A1-A8), cluster guard verified across a 30 s+ GPS update window (B1), spiderfied child tap activates without dismissing the spiderfy (C4 — the critical Phase 2/Phase 3 interaction edge case from the plan), out-of-list dim-pin tap shows orange overlay + dashed line + recomputed distance + bearing on hydrant 878-IZ (Issue 3 confirmation). Console clean throughout. D2 (real report submission), E1-E2 (follow mode / manual position regression) skipped — lower priority and similar code paths already exercised.

Remaining: none — Sprint 1.5 complete.

### Estimation Accuracy Retrospective

Behavior-batch byte budget overshot estimate by 2-3x:

- Phase 1 estimate: ~1.6-2.0 KB
- Phase 2 estimate (after composing the diff): ~2.6-3.0 KB
- Actual measured growth: 5,985 bytes (~5.85 KB)

Root cause: per-helper comment headers (4 helpers × 3-4 line headers), the nested `detach()` lambda inside `updateAllModeActiveOverlay`, and the closure boilerplate in `createActiveOverlayMarker` accumulated more than counted. Each component looked small in isolation; the sum was material.

Lesson for future sprints: when estimating size, count comment headers and closure boilerplate explicitly, not just executable lines. For sub-3 KB targets, strip non-load-bearing comments before measuring against the cap, or convert the cap to a ~5 KB target and accept richer in-code documentation as the default.

## Phase 1 Cleanup Rollout (2026-05-09)

Phase 1 of the three-phase cleanup plan (`docs/audits/cleanup_execution_plan_20260508.md`) shipped:

- **`d6cbcd5` — Phase 1 cleanup rollout shipped:**
  - Frontend adapter (`normalizeHydrantRecord`, `resolveHydrantById`)
  - Dual-schema reading (compact current + verbose target)
  - Two new pin classes (`.h-pin.operational` green, `.h-pin.broken` black)
  - Bulgarian display label tables (`EXISTENCE_LABELS`, `OPERATIONAL_LABELS`)
  - Semantic precedence in `hydrantStatusClass`
  - Polling dedupe via `legacy_ids` alias index
  - Phase 1 phone verification passed: visible behavior unchanged.
  - Ready for Phase 2 data migration in next session.

## Recent Bug Fixes (2026-05-08)

Three-commit bug fixes sprint shipped after phone verification surfaced regressions and gaps:

- **`8bd123e` — Bug A: polling dedupe.** `applyReports` now matches polled report IDs against both full-UUID and truncated `field_<8>` forms so a polled new_hydrant record already present in `HYDRANTS_BY_ID` (ingested earlier in `data/hydrants.json`) does not render a duplicate runtime pin. Resolves observed double-pins after ingest commits.
- **`9974eb7` — Bug B: card and row type display.** Hydrant type (надземен/подземен) now renders in the bottom-sheet compact card and in nearest-list rows via the existing `hydrantTypeLabel()` helper. Closes the "compact card type display" Sprint 2 backlog item.
- **`2d8b767` — Status fix: polled new hydrants render as `reported`.** Polled new_hydrant records now use the yellow `reported` status pin (under-review) instead of the red `verified` status, matching the volunteer-submitted-but-not-yet-confirmed semantics. Mitigates the "any user can publish a verified pin" exposure (see Submission moderation backlog item below).

## Next Planned Work

- **Broad launch readiness check** — share live URL with the Varna fire department / volunteer pilot group, gather a one-week field feedback window before full rollout. No code work expected unless feedback surfaces a blocker.
- **Optional pre-launch (commit 17)** — extract Worker source from the Cloudflare dashboard to a `worker/` directory in this repo with deploy notes. Until then, the live Worker is canonical.

## Commit 16 Testing Summary (2026-05-07)

End-to-end real-data validation in lieu of the synthetic checklist:

- Local dev: `python -m http.server 8000`, hard-reload at 375 px viewport.
- Test 1 (cadence + delta): Network panel showed `GET /issues` at ~15 s intervals; request #1 had no query string; subsequent requests carried `?since=<cached_at-from-previous>`. Cadence and cursor delta both verified.
- Test 4 (real status update): Submitted a real `missing` report from phone via existing POST flow. Yellow pin appeared in localhost browser within ~30 s (Worker KV TTL 30 s + 15 s poll interval). Confirms full chain: phone POST -> Worker -> GitHub issue -> Worker GET cache miss -> KV write -> next poll -> `applyReports` -> `marker.setIcon`.
- Tests 2 (visibility), 3 (offline resilience), 5 (existing features): skipped — covered with higher confidence by the production data flow above.

## Sprint 2 Backlog

Captured during Sprint 1 / 1.5 testing; ordering is not committed.

- **Hydrant type field asymmetry** — the `missing` report form prompts for hydrant type, but the `exists_confirmed` form does not. Align the two forms.
- **Compact card type display** — VIK records carry hydrant type metadata that is now surfaced in the report modal (Issue 4, `8e549e1`) but not in the bottom navigation compact card. Optional add.
- **All-mode out-of-list selection: list highlight discrepancy** — when the user taps a pin in 'Всички' that is outside the visible nearest-10, the bottom-sheet list still highlights row 0 instead of clearing the highlight. Source of truth (`activeTargetId`) is correct; only the visual fallback is misleading. Documented in `docs/plans/sprint_1_5_polish.md` Issue 3 plan as accepted tradeoff for launch.
- **Visual encoding by hydrant type** — surface ground/underground type in the pin glyph (color tier or shape variant) so type is legible without opening the card.
- **Confirm form: hydrant type prompt** — the `exists_confirmed` form should prompt for type when the field is empty, mirroring the `missing` form.
- **GitHub issue close automation** — issues #29-#36 ingested in `2dcab73` (full hash `2dcab73d27394f34801267cdcf0974ec5977a795`) but not closed on GitHub. Manual close pending OR Worker `/close-issue` endpoint (next sprint). Polling logic is idempotent — `HYDRANTS_BY_ID` dedupes new_hydrant reports, status mutations no-op when `h.status` already matches — so there is no user-visible impact, only a queue-management nuisance.
- **Submission moderation architecture** (Section B of `docs/audits/submission_status_and_moderation_plan_20260508.md`) — any user can publish a pin; the 2026-05-08 yellow-status fix (`2d8b767`) mitigates impact, but there is no admin approval gate. Plan ratifies the M1 label-based gating approach. Future sprint after cleanup planning. Requires the Worker source extraction prep commit (commit 17 placeholder) before implementation.
- **Operational status taxonomy** (Section E of same plan) — the `status` field currently conflates "exists" with "operational/working." Plan ratifies T3: a separate `operational_status` field, extending the `exists_confirmed` and `new_hydrant` flows with a "Работи ли?" question. Future sprint.
- **Type picker absent in `exists_confirmed` ("Хидрантът е там") presence flow.** Field workers cannot specify or correct hydrant type (надземен/подземен) for existing records through the presence-confirmation modal. Phone observation 2026-05-08. Investigation needed; likely bundles with the Section E taxonomy sprint since both extend the same modal.
- **Records with full UUID instead of `field_<8>` ID format observed in data** (e.g. `e3a185db-501d-4162-abf3-c212c657bbf7`). Likely legacy records from before the `field_` truncation convention was adopted. Cleanup sprint scope; pairs with the existing ID-format heterogeneity item under Data Quality Backlog.
- **GCM crash on Windows during git push remains intermittent** — occurred during the Bug A push (`8bd123e`) but not during the combined Bug B + status-fix push. Switch to SSH or reinstall Git Credential Manager when convenient. Tracked under dev-environment quirks.
- **Defender blob corruption recovery technique** — after the 2026-05-06 exclusions, Defender still occasionally corrupts loose objects on commit. Working recovery: `git update-index --force-remove <file>` + `git add` + `git commit` writes a fresh clean blob first try. Faster than the Python pre-place workaround documented in `AGENTS.md`. Both methods kept in the playbook.
- **GCM crash on push remains intermittent** — 3 occurrences during the 2026-05-09 session (Bug A push, Phase 1 push attempt 1 + 2). Crash output is cosmetic noise — git operation actually succeeds on first attempt despite the exception. Long-term fix: `winget upgrade GitHub.GitCredentialManager` or switch to SSH.
- **Phase 2 data migration scope** (per `docs/audits/cleanup_execution_plan_20260508.md` Section 2):
  - Migration script: `scripts/migrate_to_verbose_schema.py`
  - Snapshot first commit: `data/hydrants.json.pre_cleanup_snapshot.json`
  - Output: 6,082 records → 5,901 records
  - Provenance archive: `data/hydrants_provenance.json`
  - Migration report: `docs/audits/cleanup_migration_report_20260508.json`
  - Drop `field_reports.json`
  - Phase 3 (adapter removal) follows after Phase 2 verified.

## Data Quality Backlog (post-launch)

Console analysis of `data/hydrants.json` (6,079 records) during Phase 3 testing surfaced systematic data-quality issues that will affect pilot rollout. Tracked here so field-feedback signal is not polluted by known dataset noise.

- **Near-duplicate hydrants — 817 pairs total (~13% redundancy)**:
  - 610 pairs at ≤ 1 m apart (effectively identical positions; same physical asset captured twice).
  - 169 VIK-VIK pairs at ≤ 15 m apart (water-utility-source overlap).
  - 554 NAT-NAT pairs (national-source archive overlap).
  - 9 cross-source VIK + NAT pairs (same physical hydrant present in both source feeds).
  - Field-visible symptom: 'Всички' mode shows cluster glyphs `2` / `3` at the same address that spiderfy at max zoom — observed during Phase 3 cluster-guard testing.
- **ID format heterogeneity — 5 distinct ID conventions in the runtime dataset** (all three VIK conventions carry origin `o: 'vik'`; heterogeneity is an artifact of per-region KMZ exports having had different naming conventions at original creation time. App handles all formats correctly via the existing schema; cleanup is for operator legibility and future ingest simplicity, not functional necessity):
  - **Numeric VIK (no suffix)**: ~2,580 records — e.g. `10123`, `10125`, `298`, `195`, `679`.
  - **Numeric VIK with regional suffix**: ~437 records — e.g. `10122-DV`, `10523-DV` (`DV` likely encodes Devnya region).
  - **Namespaced VIK**: ~644 records — e.g. `VIK-VARNA_IZTOK-0163`, `VIK-VARNA_ZAPAD-0158`.
  - **National (`NAT-` prefix)**: 2,407 records — e.g. `NAT-5566`, `NAT-17472` — consistent format.
  - **Field reports (UUID-derived)**: 11 records — e.g. `field_ba91e3ff…` — runtime-added from volunteer reports.
  - Total: 6,079 records, matches expected count. Cleanup pass should either normalize to one convention or document them all in `AGENTS.md` § Data Model.
- **Pending additional hydrant data file** — a follow-up data drop is queued but not yet integrated into `data/hydrants.json`. Sequence the dedup pass *after* that ingest so merge logic runs once over the full corpus, not twice.
- **Recommended sequencing — clean before launch, not after.** Field-team pilots seeing visible duplicates or inconsistent IDs will file confused bug reports against the app rather than against the data. A dedicated dedup + ID normalization sprint scheduled *before* broad launch removes that whole class of false-positive feedback.

## Commit 15 Testing Summary (2026-05-07)

Plan: `docs/plans/commit_15_worker_get.md` (canonical, unmodified).

Pre-paste reconciliation: live POST handler snapshotted to `audit/worker_pre_commit15.js` and diffed against the plan's reconstruction. Four live behaviors were preserved verbatim by merging into the plan code before deploy: JSON parse + 400 fallback, required `title`/`body` validation, body field whitelisting (`{title, body, labels}`), and `500 {error: "PAT not configured"}` for missing secret. Plan's expanded CORS allowlist (added `:8000` origins) and stricter ACAO behavior (no fallback for unknown origins) kept as-is.

Tests run:

- Step 3 smoke GET — `200`, 5 reports parsed, `parse-warnings: 0`, `cache: miss/github`.
- Step 4 GitHub Pages CORS — `ACAO: https://petar1984.github.io` echoed correctly.
- Step 5 local CORS ports (4 origins) — ACAO echoed for `localhost:8000`, `127.0.0.1:8000`, `localhost:8080`, `127.0.0.1:8080`.
- Step 6 exposed-header audit — all 5 cache headers present (`X-Cache-Status`, `X-Cache-Layer`, `X-Cached-At`, `X-Parse-Warnings`, `Access-Control-Expose-Headers`).
- Step 7 cache cycle — 35s wait, then `miss/github` followed by immediate `hit/memory` with same `X-Cached-At`. L1 promotion verified.
- Step 8 query params — `limit=1` returned 1 report; `since=2026-05-06T00:00:00Z` returned all 5 (all reported on 2026-05-06); `limit=999` returned `400 invalid_limit`.
- Step 12 Cloudflare Metrics — 0 errors, 0 uncaught exceptions, 7 requests, 5 GitHub subrequests (cache hit rate as expected). Observability events not enabled by default; Metrics is the source of truth.

Skipped (with rationale):

- Step 9 frontend POST + GET integration — production POST already created the 5 issues (#29-#33) seen via GET; effectively validated. End-to-end will reconfirm naturally in commit 16.
- Step 10 multi-line frontmatter parsing — covered implicitly: all 5 real volunteer reports parsed with `parse-warnings: 0`, including Cyrillic free-text and terrain descriptions.
- Step 11 invalid `GITHUB_PAT` stale-fallback test — too risky against production secret. Deferred to a staging Worker in Sprint 2 if the fallback path needs explicit verification.

## Optional Pre-Launch (After Sprint 1)

- Extract Worker source to `worker/` directory with deploy notes (commit 17 placeholder).

## Version History

Most recent commits, newest first:

- `2d8b767` — fix(realtime): polled new hydrants render as reported
- `9974eb7` — fix(ux): show hydrant type in card and rows
- `8bd123e` — fix(realtime): dedupe polled field report ids
- `54eb36c` — docs(roadmap): D7 NAT scope investigation — empirical filter rule
- `7f7a1c4` — docs(roadmap): v2 reflects 2026-05-08 reviews + Petar ratifications
- `7412878` — feat(ux): all-mode cluster guard + ID-based active target
- `8e549e1` — fix(ux): welcome screen 2 text + report modal type display
- `a89a9af` — docs: point Last Known Good at sprint 1.5 plan and link plan as next planned work
- `219cf7a` — Fix number of hydrants listed in README
- `b23017f` — Update total hydrants count in README
- `006eb6b` — plan: sprint 1.5 UX polish fixes (4 issues)
- `9ec694f` — docs: record commit G hash as Last Known Good
- `dfd7aa9` — docs: sync after commit 16
- `06c46b1` — feat(realtime): client polling of /issues every 15s with marker status merge
- `84bc536` — mark commit 15 deployed: Worker GET /issues + KV cache live
- `84587e9` — plan: commit 15 worker GET /issues + KV cache
- `dffc634` — update active context final commit hash
- `2535920` — sync AGENTS.md and CLAUDE.md to runtime reality
- `66f4819` — remove unused report docs and local cruft ignores
- `25289ea` — extract hydrant data to data/hydrants.json (6,079 records)

## Last Known Good Commit

`7412878`

## Known Dev Environment Quirks

- Defender exclusions required for git workflow (see `AGENTS.md`).
- Local testing requires `python -m http.server 8000` because `file://` blocks fetch.
