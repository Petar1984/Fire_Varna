# Active context - Fire_Varna

Last updated: 2026-05-07 at commit <commit-G-hash>
Sprint: 1 (60-volunteer launch in 3-5 days)

## Current State

- index.html: 298,207 bytes (UI shell + libs + app logic + 15 s polling)
- data/hydrants.json: 967,530 bytes (6,079 records)
- Status counts: 18 verified, 0 reported, 6,061 canonical (in repo; runtime can grow via polled new_hydrant reports)
- Deploy: GitHub Pages from main -> https://petar1984.github.io/Fire_Varna/
- Worker: varna-hydrants-proxy.petar-dikov2019.workers.dev
  - POST `/` endpoint: live, creates labeled GitHub issues
  - GET `/issues` endpoint: live as of 2026-05-07 (commit 15), 30s KV-cached
  - Worker version deployed: `50c2b2d2`
  - KV namespace: `varna_hydrants_reports_cache`, binding `REPORTS_CACHE`
  - Rollback version (last POST-only): `e86c90a6`
- Frontend polling: client `GET /issues` every 15 s with `?since=<cached_at>` delta, paused on `document.hidden`, immediate catch-up on visibility return, silent retry on failure (cursor not advanced).

## Sprint 1 Status

Completed:

- Repo cleanup: removed stale report-plan/report-output docs and local cruft.
- Data extraction: moved embedded hydrant JSON from `index.html` to `data/hydrants.json`.
- Doc sync: updated `AGENTS.md`, `CLAUDE.md`, and this active context to runtime reality.
- Commit 15: Worker GET `/issues` + KV cache deployed and validated.
- Commit 16: client polling of GET `/issues` every 15 s with marker status merge deployed and validated.

Remaining: none — Sprint 1 complete, ready for 60-volunteer launch.

## Commit 16 Testing Summary (2026-05-07)

End-to-end real-data validation in lieu of the synthetic checklist:

- Local dev: `python -m http.server 8000`, hard-reload at 375 px viewport.
- Test 1 (cadence + delta): Network panel showed `GET /issues` at ~15 s intervals; request #1 had no query string; subsequent requests carried `?since=<cached_at-from-previous>`. Cadence and cursor delta both verified.
- Test 4 (real status update): Submitted a real `missing` report from phone via existing POST flow. Yellow pin appeared in localhost browser within ~30 s (Worker KV TTL 30 s + 15 s poll interval). Confirms full chain: phone POST -> Worker -> GitHub issue -> Worker GET cache miss -> KV write -> next poll -> `applyReports` -> `marker.setIcon`.
- Tests 2 (visibility), 3 (offline resilience), 5 (existing features): skipped — covered with higher confidence by the production data flow above.

## Known Sprint 2 Inputs (captured during commit 16 testing)

- **Hydrant type field asymmetry:** the `missing` report form prompts for hydrant type, but the `exists_confirmed` form does not. Sprint 2 should align the two forms.
- **Hydrant type display gap:** existing VIK records carry hydrant type metadata that is not surfaced in the info card. Sprint 2 should display it where present.

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

- `<commit-G-hash>` — docs: sync after commit 16
- `06c46b1` — feat(realtime): client polling of /issues every 15s with marker status merge
- `84bc536` — mark commit 15 deployed: Worker GET /issues + KV cache live
- `84587e9` — plan: commit 15 worker GET /issues + KV cache
- `dffc634` — update active context final commit hash
- `2535920` — sync AGENTS.md and CLAUDE.md to runtime reality
- `66f4819` — remove unused report docs and local cruft ignores
- `25289ea` — extract hydrant data to data/hydrants.json (6,079 records)

## Last Known Good Commit

`<commit-G-hash>`

## Known Dev Environment Quirks

- Defender exclusions required for git workflow (see `AGENTS.md`).
- Local testing requires `python -m http.server 8000` because `file://` blocks fetch.
