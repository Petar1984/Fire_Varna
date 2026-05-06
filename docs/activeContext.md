# Active context - Fire_Varna

Last updated: 2026-05-06 at commit 0488185
Sprint: 1 (60-volunteer launch in 3-5 days)

## Current State

- index.html: 292,281 bytes (UI shell + libs + app logic)
- data/hydrants.json: 967,530 bytes (6,079 records)
- Status counts: 18 verified, 0 reported, 6,061 canonical
- Deploy: GitHub Pages from main -> https://petar1984.github.io/Fire_Varna/
- Worker: varna-hydrants-proxy.petar-dikov2019.workers.dev (POST endpoint live; GET endpoint planned for commit 15)

## Pre-Sprint-15 Prep (This Work)

- Repo cleanup: remove stale report-plan/report-output docs and local cruft.
- Data extraction: move embedded hydrant JSON from `index.html` to `data/hydrants.json`.
- Doc sync: update `AGENTS.md`, `CLAUDE.md`, and this active context to runtime reality.

## Sprint 1 Remaining

- Commit 15: Worker GET `/issues` + KV cache.
- Commit 16: client polling every 15 seconds.

## Optional Pre-Launch (After Sprint 1)

- Extract Worker source to `worker/` directory with deploy notes.

## Last Known Good Commit

0488185

## Known Dev Environment Quirks

- Defender exclusions required for git workflow (see `AGENTS.md`).
- Local testing requires `python -m http.server 8000` because `file://` blocks fetch.
