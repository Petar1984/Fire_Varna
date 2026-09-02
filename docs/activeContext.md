# Active context — Fire_Varna

**Date:** 2026-09-02 · **last verified against commit** 0e563bd (`main`; ahead of `origin/main` by the 2026-09-01 plan's and the places-search cycle's commits until Petar's push — see the table) · verified by: Opus (executor), audited by: Opus (auditor, C6) · signed: __
> Every number here is the output of the command next to it, run on the date above (`verify_numbers.py` checks it). A number without a command does not enter.
> The previous chronicle (state as of 2026-07-04) is frozen in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is
Public mobile-first web app (README calls it a PWA; there is no web manifest — see the table row below and В-12): the nearest fire hydrant for Varna-oblast firefighters, with field reports moderated by Petar before they change data. Live: https://petar1984.github.io/Fire_Varna/ (GitHub Pages, branch `main`, path `/`).

## Trunk
`main`; `origin/main` is behind it by the plan's commits (table row “commits ahead of `origin/main`”) until Petar pushes. Local branch `backup/pre-c17-split` (commits only there: see the table) stays by decision Р-13 of the 2026-09-01 plan; the merged `hydrants-c17` was deleted under the same decision (`git branch` lists two local branches).

## Open theme
- The next moderation cycle (after cycle #30 in `docs/moderation_log.md`): the open reports (count in the table; `gh issue list -R Petar1984/Fire_Varna --state open`) — run through `/firehydrants`, not part of the ordering plan.
- ADR 005 service-worker cache lifecycle — `Proposed — awaiting Petar (Gate 1)` (`decisions/005_sw_cache_lifecycle.md`, 2026-08-11).
- Places (hotels) in the search — plan v2.6 executed locally: C0–C5 + C4-pre (07ee724 … 0e563bd), audit C6 ГОДНО; waiting for Gate 2, Petar's local probe (report §3) and push. Report: audits/ДОКЛАД_03.09_търсачка_места.md.

## Waiting for signature
- `plans/hotels_search_plan.md` (2026-08-22) and `plans/sw_cache_lifecycle_fixes.md` (2026-08-11): `DRAFT — AWAITING PETAR SIGNATURE (Gate 1)`.
- Gate 2 on C1–C5 + C7 of the places-search cycle; the answers listed in the report §7; the one-line fixture fix for the flaky `tests/test_etr_kmz_adapter.py::DeterminismTest::test_two_runs_byte_identical` (ZIP timestamp).

## Last report
- `moderation_log.md` — cycle #30 (dated in the log: see the table; committed 2026-09-01 as 06cdada) · last data commit 06cdada.
- `audits/ДОКЛАД_03.09_търсачка_места.md` — the night shift of 02→03.09: the places (hotels) search C0–C6, the resorts, the Roman numerals, phase 2.

## Current State
| Какво | Стойност | Команда |
|---|---|---|
| records in `data/hydrants.json` | 7403 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| open reports (issues) | 18 | `gh issue list -R Petar1984/Fire_Varna --state open --limit 200 --json number --jq length` |
| closed reports | 709 | `gh api "search/issues?q=repo:Petar1984/Fire_Varna+is:issue+is:closed" --jq .total_count` |
| commits on `main` | 222 | `git rev-list --count main` |
| last pushed commit | 06cdada 2026-09-01 | `git log -1 --format='%h %cs' origin/main` |
| commits ahead of `origin/main` (the 2026-09-01 plan + the places-search cycle, unpushed) | 8 | `git rev-list --count origin/main..main` |
| last data commit (moderation cycle) | 2026-09-01 data: cycle #30 — 15 reports, and the Golden Sands import left alone | `git log -1 --format='%cs %s' -- data/hydrants.json docs/moderation_log.md` |
| `index.html` bytes | 508556 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1311397 | `wc -c < data/hydrants.json` |
| `data/hotels.json` bytes | 78601 | `wc -c < data/hotels.json` |
| hotels in `data/hotels.json` | 226 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('data/hotels.json',encoding='utf-8'))['_meta']['count'])"` |
| `data/place_categories.json` bytes | 36203 | `wc -c < data/place_categories.json` |
| tests | Ran 150 tests · OK | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| Pages | 200 | `curl -s -o /dev/null -w '%{http_code}' https://petar1984.github.io/Fire_Varna/` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| commits only on `backup/pre-c17-split` | 5 | `git rev-list --count main..backup/pre-c17-split` |
| cycle #30 date in `docs/moderation_log.md` | 2026-08-31 | `grep -m1 -oE '^## [0-9-]+ — цикъл #30' docs/moderation_log.md \| cut -c4-13` |
| records per origin (AGENTS.md § Data model points here for the per-origin counts) | [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 147), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| Worker deploy version (repo-declared in `worker/README.md`; `worker/DEPLOY_E2.md` says to record it here) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |

> The two commit-count rows (“commits on `main`” and “commits ahead of `origin/main`”) move by +1 with every commit — including the one that writes this file; the reconciliation is against the commit in line 3 (= `git rev-parse --short HEAD~1` right after that commit). The `tests` row records the count and the verdict; the duration printed by the command varies per run. `verify_numbers.py` (line 4) does not exist in this repo yet — it is a convention borrowed from varna_3d; until it does, the commands above are run by hand.

## Forbidden here
- `git push`, Worker deploy, any publish — Petar only. Personal data in `data/`, issues or docs (`reporters_private.md` is gitignored on purpose). New runtime/build dependencies, Bulgarian UI wording changes, first load > 5 MB — without Petar's approval. Cross-repo edits from here.

## Where things are
- `data/hydrants.json` (runtime dataset) · `data/search_index.json` + `data/address_rows.json` are **built in Varna_buildings** (last payload: ADR 063 reattribution, commit c0db844, 2026-08-31) · `details/` gitignored (served from R2) · `worker/` Cloudflare Worker source · `sw.js` service worker (ADR 002/005) · `scratch/` evidence of closed cycles (LOT 1 of the 2026-09-01 plan).
- Doctrine shared with Varna_buildings: ADR 004 → Varna_buildings ADR 058. varna_3d consumes the hydrants for its 3D map (`web/hydrants.js` there).
