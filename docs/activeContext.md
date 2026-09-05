# Active context — Fire_Varna

**Date:** 2026-09-05 · **HEAD:** F12-г = this commit (its parent is `f38c77f`, F12-в) · **branch:** `main` · **signed:** __

> One page. Every number below is the output of the command next to it, run on the date above; a number without a command does not enter. The chronicle of 03–04.09 (ЛОТ 1, 1в-А, 1в-Б, 1в-В, the pre-rebase hash table) is frozen in [archive/activeContext_2026-09-04.md](archive/activeContext_2026-09-04.md); the one before it in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is

The public mobile-first web app that shows a Varna-oblast firefighter the nearest working hydrant, with no install and no account. Live: <https://petar1984.github.io/Fire_Varna/> (GitHub Pages, `main`, path `/`). Field reports are moderated by Petar before they change data. Governance: `AGENTS.md`; executor rules: `CLAUDE.md`.

## Where the work stands (05.09)

**Фаза A of `plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` (signed 05.09 02:50) + its `амандамент_1`: F12 is executed and waits for Petar.** F12 copies the P7 delivery of varna_3d (М2 + М3 + М6) into `data/`, re-pins the three SHA constants, bumps the places cache to v6, opens the closed client lists for the three codes the delivery carries (`mladost`, `briz`, `morska_gradina`), adds the М7 „bare place“ branch on both sides, and produces the two report-only manifests. **Nothing is frozen and nothing is pushed.**

Four things are waiting for Petar's own hand — none of them may be written by an agent:

1. `gates/baseline/MANIFEST.json` → `signed_by: "Петър"` („подписвам baseline f06ac06“).
2. `gates/allow/2026-09-05_lot1v_v.json` — 150 named rows in four reason classes (`hull_artifact` 80 · `no_witness` 56 · `resort_pending` 8 · `m6_changed` 6).
3. `scratch/places_search/lot1v_v_manifest_BASE_P7.json` and `…_P7_F12.json` — the two diffs, every row shown.
4. `scratch/places_search/m7_trigger_tokens.json` — the words that fire М7, and the open question inside it (the short prefix words „кв“, „жк“, „к“ trigger it today).

The 8 resort conflicts (ДАЛИЯ ГАРДЪН · Фрегата · МАГНОЛИЯ 1 И 2 · Маяк · НЕПТУН · Романтика · РУСАЛКА · СТРАНДЖА) stay `pending_signature`: the map shows them as „район X“ until he decides each one.

**Open after F12 (the report `scratch/places_search/ОТЧЕТ_F12_05.09.md` §STOP):** 9 red tests carry the byte sizes, the closed lists and the coverage counts of the PREVIOUS delivery. They are not of the class „waits for a signature“, so F12 stops there and asks instead of rewriting them.

## Current state

| Какво | Стойност | Команда |
|---|---|---|
| commits on `main` | 314 | `git rev-list --count main` |
| commits ahead of `origin/main` (Petar alone pushes) | 35 | `git rev-list --count origin/main..main` |
| commits on `origin/main` not on `main` | 0 | `git rev-list --count main..origin/main` |
| last pushed commit | 6da5d9a 2026-09-04 | `git log -1 --format='%h %cs' origin/main` |
| records in `data/hydrants.json` | 7407 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| records per origin | [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 151), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| `index.html` bytes (557270 before F12) | 559542 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1315276 | `wc -c < data/hydrants.json` |
| first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | 1874818 B = 1,79 MB | `python -c "import os;print(os.path.getsize('index.html')+os.path.getsize('data/hydrants.json'))"` |
| `data/hotels.json` (225 rows × 17 keys; 142543 B before F12) | 148685 B · sha `46a44ce82f15…` | `wc -c < data/hotels.json` · `git show HEAD:data/hotels.json \| sha256sum` |
| `data/places.json` (150 rows × 13 keys; 121621 B before F12) | 122089 B · sha `329310f577e8…` | `wc -c < data/places.json` · `git show HEAD:data/places.json \| sha256sum` |
| `data/place_categories.json` (64831 B before F12) | 75818 B · sha `874e33cd00e2…` | `wc -c < data/place_categories.json` · `git show HEAD:data/place_categories.json \| sha256sum` |
| typed locations on the 375 delivered rows: quarter · locality · district (140 · 8 · 375 before F12) | 201 · 12 · 375 | `PYTHONIOENCODING=utf-8 python -c "import json;r=[x for f,k in (('data/places.json','places'),('data/hotels.json','hotels')) for x in json.load(open(f,encoding='utf-8'))[k]];print(sum(1 for x in r if x['quarter']), sum(1 for x in r if x['locality']), sum(1 for x in r if x['district']))"` |
| dictionary: forms · `legacy_by_row` · zones (283 · 209 · 19 before F12) | 283 · 18 · 20 | `PYTHONIOENCODING=utf-8 python -c "import json;c=json.load(open('data/place_categories.json',encoding='utf-8'));print(c['_meta']['n_forms'], len(c['legacy_by_row']), len(c['zones']))"` |
| search reference `scratch/places_search/recall_sweep_rows.json` — NOT frozen by F12 (report-only) | 140 rows, untouched | `git diff --stat HEAD~4 -- scratch/places_search/recall_sweep_rows.json` |
| tests (241 after F9; 259 since) · red | Ran 259 · FAILED (failures=27, errors=3) = 30 red | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| gates | ⚠ ЖЪЛТО (blocks the push like red): check 4 waits for two signatures; 1, 2, 3, 5 green | `python -m gates.run_gates` |
| coverage of the delivery against the signed baseline `f06ac06` | places zone_named 127 → 49 · hotels 199 → 152 · uncovered 0 · exit 5 (unsigned allow) | `python -m gates.coverage --places-base git:f06ac06:data/places.json --places-candidate data/places.json --hotels-base git:f06ac06:data/hotels.json --hotels-candidate data/hotels.json --allow gates/allow/2026-09-05_lot1v_v.json` |
| Worker deploy version (repo-declared) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| local branches (traces of closed cycles; work happens on `main`) | backup/pre-c17-split · backup/pre-c32-split · hydrants-c32 · lot1-client · main | `git branch --format='%(refname:short)'` |

Two rows of the previous page are NOT re-measured here because they need the network (satellite link): the open/closed issue counts (`gh issue list …`) and the Pages status code (`curl …`). Read them from the archive with their date, or run the command.

## Waiting for a signature

- **Фаза A of the cleanup plan** — the four artefacts listed above; then `--freeze` once, tests green, `run_gates` green, audit, and Petar's push. `docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` §A.4.
- `decisions/007_address_path_v2.md` — `Proposed — awaiting Petar (Gate 1)`.
- `decisions/005_sw_cache_lifecycle.md` — `Proposed — awaiting Petar (Gate 1)`.
- `plans/hotels_search_plan.md`, `plans/sw_cache_lifecycle_fixes.md` — `DRAFT — AWAITING PETAR SIGNATURE (Gate 1)`.
- ADR 009 „Идентичност, подписи, гейтове“ — Фаза B of the cleanup plan, not written yet.

Parked scope (nothing opens until Фаза A is pushed): `plans/PARKED.md`.

## Forbidden here

`git push`, Worker deploy, any publish — Petar only. Personal data in `data/`, in issues or in docs. New runtime or build-time dependencies, Bulgarian UI wording changes, a first load over 5 MB — not without Petar. Cross-repo edits from this checkout. `--freeze` on the search reference without a signed manifest. Writing `signed_by: "Петър"` — an agent writes `pending — Петър` and nothing else.

## Where things are

`index.html` (the whole app shell) · `data/hydrants.json` (runtime dataset) · `data/{places,hotels,place_categories}.json` (the places search, delivered from varna_3d) · `data/search_index.json` + `data/address_rows.json` (built in Varna_buildings) · `gates/` (the release gates: sha pins, key sets, cadastral scan, coverage, signed facts) · `worker/` (Cloudflare Worker source) · `sw.js` (ADR 002/005) · `scratch/places_search/` (the reference engine, the manifests, the boards) · `docs/decisions/` (ADRs) · `docs/plans/` (the task contracts) · `docs/archive/` (frozen chronicles).

Doctrine shared with Varna_buildings: ADR 004 → Varna_buildings ADR 058. varna_3d generates the places delivery and consumes the hydrants for its 3D map.
