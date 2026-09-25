# Active context — Fire_Varna

**Date:** 2026-09-25 · **measured at:** `8b80a20` (`data: cycle #45`) = `main` = `origin/main` on that date · **written on:** the review branch `claude/gracious-hamilton-24npor`, branched off `8b80a20` (Petar merges it into `main` at Gate 2) · **signed:** __

> One page. Every number below is the output of the command next to it, run on the date above; a number without a command does not enter. The chronicle of 05–15.09 (Фаза A published; лотове 1, 4б, 4в-А, 4в-Б, 1г, 5, 5в, 6 and О of „Проблемите“) is frozen in [archive/activeContext_2026-09-15.md](archive/activeContext_2026-09-15.md); before it [archive/activeContext_2026-09-04.md](archive/activeContext_2026-09-04.md) and [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md). The documentation audit that produced this page: [audits/ОДИТ_25.09_документация.md](audits/ОДИТ_25.09_документация.md).

## What this repo is

The public mobile-first web app that shows a Varna-oblast firefighter the nearest working hydrant, with no install and no account. Live: <https://petar1984.github.io/Fire_Varna/> (GitHub Pages, `main`, path `/`). Field reports are moderated by Petar before they change data. Governance: `AGENTS.md`; executor rules: `CLAUDE.md`.

## Where the work stands (25.09)

**No lot is in motion.** The last one, лот О („Проблем или идея за приложението“ — the sixth entry of the „+“ menu, an app-feedback issue that never enters the map pipe), closed on 15.09 (v1.4 `5a5069d`, state `d323959`). Since then `main` carries only data cycles — #41 `8d6aa69` (15.09), #42 `89e33b4` (21.09, 7400 → 7399, one duplicate removed), #43 `f512202` (24.09), #44 `928ef5e` (24.09, 7399 → 7400, one new hydrant and one unusable), #45 `8b80a20` (25.09) — each with its entry in [moderation_log.md](moderation_log.md).

**Lot О debts, re-checked 25.09:**

- „the labels are created by Petar in GitHub before the first real report“ — **done**: the `app-feedback` label exists (GitHub API, 25.09).
- the `/feedback` cycle (an agent reads the issues, replays the address queries through the harness, a board for the ideas) — a separate lot, opens after the first reports; none has arrived (0 open issues, 25.09).
- Enter-selection and selection from the entrance strip are not recorded; errors before the recorder starts are not recorded — declared, unchanged.

**Housekeeping of 25.09 (this branch):** the dead root artifacts and the May 2026 data snapshots were retired (`chore: retire dead root artifacts…` — the list is in that commit); the state page was re-measured and the 05–15.09 chronicle frozen; README, AGENTS.md and CLAUDE.md were brought to the measured state; the anchor links of the 08.05 governance proposal were repaired. What was **not** deleted, and why, is a decision table in the audit report above — `scratch/`, `audit/`, the JSON dumps under `docs/audits/`, `docs/sessions/`, the two May remote branches all wait for Petar's word.

## Current state

| Какво | Стойност | Команда |
|---|---|---|
| commits on `main` | 693 | `git rev-list --count main` |
| commits ahead of `origin/main` (Petar alone pushes) | 0 | `git rev-list --count origin/main..main` |
| commits on `origin/main` not on `main` | 0 | `git rev-list --count main..origin/main` |
| last pushed commit | 8b80a20 2026-09-25 | `git log -1 --format='%h %cs' origin/main` |
| records in `data/hydrants.json` | 7400 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| records per origin | [('vik', 3517), ('national', 2322), ('etr_varna', 763), ('etr_provadia', 243), ('etr_dolni_chiflik', 219), ('field_report', 159), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| `existence_status = verified` · `operational_status` works / not_working / not_tested | 749 · 116 / 17 / 561 (`review_status`: none present) | `PYTHONIOENCODING=utf-8 python -c "import json,collections as c;d=json.load(open('data/hydrants.json',encoding='utf-8'));print(c.Counter(r.get('existence_status') for r in d),c.Counter(r.get('operational_status') for r in d),c.Counter(r.get('review_status') for r in d))"` |
| disambiguated duplicate ids (`__NAT-####` suffix) · `field_*` ids | 27 · 0 | `python -c "import json;d=json.load(open('data/hydrants.json',encoding='utf-8'));print(sum(1 for r in d if '__' in r['id']), sum(1 for r in d if r['id'].startswith('field_')))"` |
| `index.html` bytes | 623742 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1325287 | `wc -c < data/hydrants.json` |
| first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | 1949029 B = 1,86 MB (`address_quarters.json` 493305 B, `search_index.json` 11242756 B and `address_rows.json` 5073137 B are lazy, outside the first load) | `python -c "import os;print(os.path.getsize('index.html')+os.path.getsize('data/hydrants.json'))"` |
| `data/hotels.json` (225 rows) | 148685 B · sha `46a44ce82f15…` | `wc -c < data/hotels.json` · `git show HEAD:data/hotels.json \| sha256sum` |
| `data/places.json` (150 rows) | 122089 B · sha `329310f577e8…` | `wc -c < data/places.json` · `git show HEAD:data/places.json \| sha256sum` |
| `data/place_categories.json` | 75818 B · sha `874e33cd00e2…` | `wc -c < data/place_categories.json` · `git show HEAD:data/place_categories.json \| sha256sum` |
| typed locations on the 375 delivered rows: quarter · locality · district | 201 · 12 · 375 | `PYTHONIOENCODING=utf-8 python -c "import json;r=[x for f,k in (('data/places.json','places'),('data/hotels.json','hotels')) for x in json.load(open(f,encoding='utf-8'))[k]];print(sum(1 for x in r if x['quarter']), sum(1 for x in r if x['locality']), sum(1 for x in r if x['district']))"` |
| dictionary: forms · `legacy_by_row` · zones | 283 · 18 · 20 | `PYTHONIOENCODING=utf-8 python -c "import json;c=json.load(open('data/place_categories.json',encoding='utf-8'));print(c['_meta']['n_forms'], len(c['legacy_by_row']), len(c['zones']))"` |
| tests | Ran 481 · FAILED (failures=2) on Linux — both are one cause, see § The red tests; the 15.09 page recorded the same suite green on Windows | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| gates | ✓ всички гейтове зелени — 1–7, release gate (проверка 6) included: 0 delta, 34 signed artefacts/rows verified | `python -m gates.run_gates` |
| Worker deploy version (repo-declared) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |
| Worker KV cache TTL · client poll interval | 30 s · 15 s | `grep -n CACHE_TTL_SECONDS worker/index.js \| head -1` · `grep -n 'POLL_INTERVAL_MS =' index.html` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| `BASEMAP_PMTILES_ENABLED` (committed flag) | `false` | `grep -n 'BASEMAP_PMTILES_ENABLED = ' index.html` |
| report kinds the form can send (`data-type`) | app_feedback · damaged · exists_confirmed · missing · new_hydrant · wrong_location | `grep -o 'data-type="[a-z_]*"' index.html \| sort -u` |
| open issues: `report` · `app-feedback` · all | 0 · 0 · 0 | `gh issue list --label report --state open` · `gh issue list --label app-feedback --state open` · `gh issue list --state open` (measured through the GitHub API on 25.09) |
| `app-feedback` label on the repo | exists | `gh label list \| grep app-feedback` |
| remote branches | `origin/main` · `origin/batch-ingest/2026-05-28` (a4bd946, 2026-05-28) · `origin/ingest/issue-62` (791d817, 2026-05-28) — the two May branches are frozen traces; deleting them is a push, Petar's alone | `git for-each-ref --sort=-committerdate --format='%(refname:short) %(committerdate:short)' refs/remotes` |
| local branches | not measured — this page was written in a fresh clone; the traces on Petar's machine (`backup/pre-c17-split`, `backup/pre-c32-split`, `hydrants-c32`, `lot1-client`) are as the 05.09 page listed them | `git branch --format='%(refname:short)'` |
| Pages status code | not measured — the session's network proxy refuses `github.io` (403 CONNECT); run it from a machine with the satellite link | `curl -s -o /dev/null -w '%{http_code}' https://petar1984.github.io/Fire_Varna/` |

### The red tests: two, one cause, Linux only

`test_address_entrances_under_building.EntranceFoldTest.test_the_row_list_is_byte_equal_to_the_base` and `test_address_search_polygon_quarter.PolygonQuarterTest.test_the_corpus_deltas_are_the_signed_list` both fail with „Ф9 не върна json … Unterminated string“. The probe `tests/address_slice_probe.mjs` ends with `process.stdout.write(JSON.stringify(out)); process.exit(…)` (its last two lines). On a Linux pipe `stdout` is asynchronous, so `process.exit` cuts an answer longer than 64 KiB; on Windows the pipe is synchronous and nothing is cut — which is why the 15.09 page recorded the suite green there. The remaining 479 tests, the seven declared negative halves included, behave as the 15.09 page says. The fix is one line (`process.exitCode = …` and let the process drain), but the probe is a pinned harness (ADR 012 D7 names it), so it enters through a plan row, not through this page.

## Waiting for a signature (status lines re-read 25.09)

- `decisions/002_osm_pmtiles_basemap_offline.md` — `DRAFT — STOP B0, pending Petar signature` (2026-07-05). The basemap release it describes exists under `data/basemaps/` and `sw.js` is in the repo; the flag stays `false`. The status line was never updated after B0 — Petar decides whether it is `Accepted (off by default)` or still open.
- `decisions/005_sw_cache_lifecycle.md` — `Proposed — awaiting Petar (Gate 1)`.
- `decisions/007_address_path_v2.md` — `Proposed — awaiting Petar (Gate 1)`.
- `decisions/008_places_aliases_and_addresses.md` — `Proposed (04.09.2026)`.
- `decisions/010_signed_quarter_boundaries.md` — `Proposed (05.09.2026) — чернова`; `decisions/011_kartata_imot.md` — `Proposed` (08.09), with its own 11.09 note that sub-lot И-А is executed.
- ADR 009 „Идентичност, подписи, гейтове“ — Фаза B of `plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md`, not written.
- `plans/sw_cache_lifecycle_fixes.md` (11.08) and `plans/search_registry_note.md` (12.08) — `DRAFT — AWAITING PETAR SIGNATURE (Gate 1)`.
- `plans/hotels_search_plan.md` (22.08) — still says `DRAFT — AWAITING PETAR SIGNATURE`, but the hotels shipped on 05.09 under ADR 006 and the places delivery; the plan is overtaken, its status line is not. Petar decides whether it is closed or archived.

Parked scope: [plans/PARKED.md](plans/PARKED.md) — P1, P2, P3, P5 unchanged; P4 closed.

## Forbidden here

`git push` to `main`, Worker deploy, any publish — Petar only. Personal data in `data/`, in issues or in docs. New runtime or build-time dependencies, Bulgarian UI wording changes, a first load over 5 MB — not without Petar. Cross-repo edits from this checkout. `--freeze` on the search reference without a signed manifest. Writing `signed_by: "Петър"` — an agent writes `pending — Петър` and nothing else.

## Where things are

`index.html` (the whole app shell) · `data/hydrants.json` (runtime dataset) · `data/hydrants_provenance.json` (per-record provenance) · `data/{places,hotels,place_categories}.json` (the places search, delivered from varna_3d) · `data/search_index.json` + `data/address_rows.json` + `data/address_quarters.json` (the address search, built in Varna_buildings; lazy) · `data/basemaps/` (the PMTiles basemap release, off by default) · `gates/` (the release gates: sha pins, key sets, cadastral scan, coverage, signed facts) · `worker/` (Cloudflare Worker source, README, E2 runbook) · `sw.js` (ADR 002/005) · `scripts/` (ingest, migration, backfill tooling; `scripts/lib/hydrant_core.py` is the shared core) · `tests/` (the unittest suite and the node probes) · `scratch/places_search/` (the reference engine, the manifests, the boards) · `scratch/` otherwise (working material of past cycles) · `audit/` (May 2026 audit snapshots) · `docs/decisions/` (ADRs) · `docs/plans/` (the task contracts) · `docs/audits/` (dated reports and amendments) · `docs/sessions/` (session hand-offs of the Границите cycle) · `docs/archive/` (frozen chronicles).

Doctrine shared with Varna_buildings: ADR 004 → Varna_buildings ADR 058. varna_3d generates the places delivery and consumes the hydrants for its 3D map.
