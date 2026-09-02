# Active context — Fire_Varna

**Date:** 2026-09-02 · **last verified against commit** bc18d54 (`main`; ahead of `origin/main` by the 2026-09-01 plan's commits until Petar's push — see the table) · verified by: Opus (executor), audited by: <auditor> · signed: __
> Every number here is the output of the command next to it, run on the date above (`verify_numbers.py` checks it). A number without a command does not enter.
> The previous chronicle (state as of 2026-07-04) is frozen in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is
Public mobile-first web app (README calls it a PWA; there is no web manifest — see the table row below and В-12): the nearest fire hydrant for Varna-oblast firefighters, with field reports moderated by Petar before they change data. Live: https://petar1984.github.io/Fire_Varna/ (GitHub Pages, branch `main`, path `/`).

## Trunk
`main`; `origin/main` is behind it by the plan's commits (table row “commits ahead of `origin/main`”) until Petar pushes. Local branch `backup/pre-c17-split` (commits only there: see the table) stays by decision Р-13 of the 2026-09-01 plan; the merged `hydrants-c17` was deleted under the same decision (`git branch` lists two local branches).

## Open theme
- Moderation cycle #31: the open reports (count in the table; `gh issue list -R Petar1984/Fire_Varna --state open`) — run through `/firehydrants`, not part of the ordering plan.
- ADR 005 service-worker cache lifecycle — `Proposed — awaiting Petar (Gate 1)` (`decisions/005_sw_cache_lifecycle.md`, 2026-08-11).

## Waiting for signature
- `plans/hotels_search_plan.md` (2026-08-22) and `plans/sw_cache_lifecycle_fixes.md` (2026-08-11): `DRAFT — AWAITING PETAR SIGNATURE (Gate 1)`.

## Last report
- `moderation_log.md` — cycle #30 (dated in the log: see the table; committed 2026-09-01 as 06cdada) · last data commit 06cdada.

## Current State
| Какво | Стойност | Команда |
|---|---|---|
| records in `data/hydrants.json` | 7403 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| open reports (issues) | 18 | `gh issue list -R Petar1984/Fire_Varna --state open --limit 200 --json number --jq length` |
| closed reports | 709 | `gh api "search/issues?q=repo:Petar1984/Fire_Varna+is:issue+is:closed" --jq .total_count` |
| commits on `main` | 211 | `git rev-list --count main` |
| last pushed commit | 06cdada 2026-09-01 | `git log -1 --format='%h %cs' origin/main` |
| commits ahead of `origin/main` (the 2026-09-01 plan, unpushed) | 6 | `git rev-list --count origin/main..main` |
| last data commit (moderation cycle) | 2026-09-01 data: cycle #30 — 15 reports, and the Golden Sands import left alone | `git log -1 --format='%cs %s' -- data/hydrants.json docs/moderation_log.md` |
| `index.html` bytes | 475446 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1311397 | `wc -c < data/hydrants.json` |
| Pages | 200 | `curl -s -o /dev/null -w '%{http_code}' https://petar1984.github.io/Fire_Varna/` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| commits only on `backup/pre-c17-split` | 5 | `git rev-list --count main..backup/pre-c17-split` |
| cycle #30 date in `docs/moderation_log.md` | 2026-08-31 | `grep -m1 -oE '^## [0-9-]+ — цикъл #30' docs/moderation_log.md \| cut -c4-13` |

## Forbidden here
- `git push`, Worker deploy, any publish — Petar only. Personal data in `data/`, issues or docs (`reporters_private.md` is gitignored on purpose). New runtime/build dependencies, Bulgarian UI wording changes, first load > 5 MB — without Petar's approval. Cross-repo edits from here.

## Where things are
- `data/hydrants.json` (runtime dataset) · `data/search_index.json` + `data/address_rows.json` are **built in Varna_buildings** (last payload: ADR 063 reattribution, commit c0db844, 2026-08-31) · `details/` gitignored (served from R2) · `worker/` Cloudflare Worker source · `sw.js` service worker (ADR 002/005) · `scratch/` evidence of closed cycles (LOT 1 of the 2026-09-01 plan).
- Doctrine shared with Varna_buildings: ADR 004 → Varna_buildings ADR 058. varna_3d consumes the hydrants for its 3D map (`web/hydrants.js` there).
