# Active context — Fire_Varna

**Date:** 2026-09-05 · **HEAD:** A.2-4 = this commit (its parent is `a694c7e`, A.2-3) · **branch:** `main` · **signed:** __

> One page. Every number below is the output of the command next to it, run on the date above; a number without a command does not enter. The chronicle of 03–04.09 (ЛОТ 1, 1в-А, 1в-Б, 1в-В, the pre-rebase hash table) is frozen in [archive/activeContext_2026-09-04.md](archive/activeContext_2026-09-04.md); the one before it in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is

The public mobile-first web app that shows a Varna-oblast firefighter the nearest working hydrant, with no install and no account. Live: <https://petar1984.github.io/Fire_Varna/> (GitHub Pages, `main`, path `/`). Field reports are moderated by Petar before they change data. Governance: `AGENTS.md`; executor rules: `CLAUDE.md`.

## Where the work stands (05.09)

**Фаза A of `plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` (signed 05.09 02:50) + its four amendments: F12 (а–з) and A.2 (1–4) are executed and wait for Petar.** F12 copies the P7 delivery of varna_3d (М2 + М3 + М6) into `data/`, re-pins the three SHA constants, bumps the places cache to v6, opens the closed client lists for the three codes the delivery carries (`mladost`, `briz`, `morska_gradina`), adds the М7 „bare place“ branch on both sides, moves the two bundle tests onto the delivered numbers (F12-д), narrows М7 to significant tokens (F12-е) and makes every manifest anchor that names a commit the bytes of the **blob** at that commit (F12-ж).

**A.2 built the release machinery** (амандамент №4): `gates/release.py` — проверка 6 — binds the frozen reference, the engine candidate, the pinned inputs and the manifests by digest and refuses every delta that no signed queue row covers; `gates/sign.py` applies „да/не“ to a queue row and to the artefact it governs and refuses to run while the git identity is an agent's; проверка 7 reads back with `git log -S` who INTRODUCED each signature; the pre-push hook now runs the suite AND the gates and has no break-glass at all; and every delivery-dependent expectation left the code for one signable body, `scratch/places_search/expectations.json`. **Nothing is frozen and nothing is published.**

Four things are waiting for Petar's own hand — none of them may be written by an agent:

1. `gates/baseline/MANIFEST.json` → `signed_by: "Петър"` („подписвам baseline f06ac06“).
2. `gates/allow/2026-09-05_lot1v_v.json` — 150 named rows in four reason classes (`hull_artifact` 80 · `no_witness` 56 · `resort_pending` 8 · `m6_changed` 6).
3. `scratch/places_search/lot1v_v_manifest_BASE_P7.json` and `…_P7_F12.json` — the two diffs, every row shown; the P7→F12 one also carries the two controls of gate 6 („приморски“, „владислав варненчик“) as a signable delta.
4. `scratch/places_search/m7_trigger_tokens.json` — **33 triggering words**, waiting for a signature.
5. `scratch/places_search/expectations.json` — the ONE body every delivery-dependent expectation now lives in (the answers of the 78 gate questions, the §10 sweep, the П7 measure, 15 claims, the three bucket anchors, the replay counts, and the „before“ of every question as the frozen reference answered it). `python -m gates.sign <id> да` writes the signature; an agent writes only `pending — Петър`.
6. `scratch/places_search/ЗА_ПОДПИС_<дата>.md` — the queue itself (A.3, not written yet). Until it exists проверка 6 is RED with „няма опашка“, which is the fail-closed answer, not a defect. F12-е closed the short-prefix defect: the eight type prefixes (`к`, `кв`, `ж`, `м`, `с`, `о`, `т`, `зона`) no longer fire the branch; the 45 measured candidates stay in the file with `triggers: false` so what was thrown out stays visible.

The 8 resort conflicts (ДАЛИЯ ГАРДЪН · Фрегата · МАГНОЛИЯ 1 И 2 · Маяк · НЕПТУН · Романтика · РУСАЛКА · СТРАНДЖА) stay `pending_signature`: the map shows them as „район X“ until he decides each one.

## Current state

| Какво | Стойност | Команда |
|---|---|---|
| commits on `main` | 327 | `git rev-list --count main` |
| commits ahead of `origin/main` (Petar alone pushes) | 46 | `git rev-list --count origin/main..main` |
| commits on `origin/main` not on `main` | 0 | `git rev-list --count main..origin/main` |
| last pushed commit | 6da5d9a 2026-09-04 | `git log -1 --format='%h %cs' origin/main` |
| records in `data/hydrants.json` | 7407 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| records per origin | [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 151), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| `index.html` bytes (557270 before F12; 560365 after F12-з) | 560855 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1315276 | `wc -c < data/hydrants.json` |
| first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | 1876131 B = 1,79 MB | `python -c "import os;print(os.path.getsize('index.html')+os.path.getsize('data/hydrants.json'))"` |
| `data/hotels.json` (225 rows × 17 keys; 142543 B before F12) | 148685 B · sha `46a44ce82f15…` | `wc -c < data/hotels.json` · `git show HEAD:data/hotels.json \| sha256sum` |
| `data/places.json` (150 rows × 13 keys; 121621 B before F12) | 122089 B · sha `329310f577e8…` | `wc -c < data/places.json` · `git show HEAD:data/places.json \| sha256sum` |
| `data/place_categories.json` (64831 B before F12) | 75818 B · sha `874e33cd00e2…` | `wc -c < data/place_categories.json` · `git show HEAD:data/place_categories.json \| sha256sum` |
| typed locations on the 375 delivered rows: quarter · locality · district (140 · 8 · 375 before F12) | 201 · 12 · 375 | `PYTHONIOENCODING=utf-8 python -c "import json;r=[x for f,k in (('data/places.json','places'),('data/hotels.json','hotels')) for x in json.load(open(f,encoding='utf-8'))[k]];print(sum(1 for x in r if x['quarter']), sum(1 for x in r if x['locality']), sum(1 for x in r if x['district']))"` |
| dictionary: forms · `legacy_by_row` · zones (283 · 209 · 19 before F12) | 283 · 18 · 20 | `PYTHONIOENCODING=utf-8 python -c "import json;c=json.load(open('data/place_categories.json',encoding='utf-8'));print(c['_meta']['n_forms'], len(c['legacy_by_row']), len(c['zones']))"` |
| search reference `scratch/places_search/recall_sweep_rows.json` — NOT frozen by F12 (report-only) | 140 rows, untouched since `148c731` (the commit before F12-а) | `git diff --stat 148c731 -- scratch/places_search/recall_sweep_rows.json` |
| manifest anchor of `lot1v_v_manifest_BASE_P7.json`: the **blob** at the named commit, not the file on disk (F12-ж) | `f06ac06` → `0bc7a189f408…` · 256070 B (the CRLF twin on a Windows worktree is 266021 B and the same OID) | `python scratch/places_search/manifest_anchor_gate.py` · `git show f06ac06:scratch/places_search/recall_sweep_rows.json \| sha256sum` |
| tests (241 after F9; 259 before A.2-4) · red | Ran 266 · FAILED (failures=6) = 6 red, all in `tests/test_places_search_gate.py` (see the split below) | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| gates | ⛔ ЧЕРВЕНО: проверка 6 (release) — 173 delta between the frozen reference and the engine candidate and no queue to cover them; проверка 4 ⚠ waits for two signatures; 1, 2, 3, 5, 7 green | `python -m gates.run_gates` |
| release gate: reference ↔ candidate | reference 140 queries / 2121 rows · candidate 203 / 3160 · 173 delta · 0 covered (no queue yet) | `python -m gates.release` |
| `scratch/places_search/expectations.json` | 321040 B · `signed_by: "pending — Петър"` · 78 gate questions · 62 + 10 sweep rows · 15 claims · 3 bucket anchors | `PYTHONIOENCODING=utf-8 python scratch/places_search/recall_sweep.py --manifest` |
| coverage of the delivery against the signed baseline `f06ac06` | places zone_named 127 → 49 · hotels 199 → 152 · uncovered 0 · exit 5 (unsigned allow) | `python -m gates.coverage --places-base git:f06ac06:data/places.json --places-candidate data/places.json --hotels-base git:f06ac06:data/hotels.json --hotels-candidate data/hotels.json --allow gates/allow/2026-09-05_lot1v_v.json` |
| Worker deploy version (repo-declared) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| local branches (traces of closed cycles; work happens on `main`) | backup/pre-c17-split · backup/pre-c32-split · hydrants-c32 · lot1-client · main | `git branch --format='%(refname:short)'` |

Two rows of the previous page are NOT re-measured here because they need the network (satellite link): the open/closed issue counts (`gh issue list …`) and the Pages status code (`curl …`). Read them from the archive with their date, or run the command.

### The red tests: 21 before A.2-4, 6 after (амандамент №4 т. 1 и т. 7)

The class is decided by **where the expectation lives**, measured by reading each test:
`PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -v 2>&1 | grep -E '^(FAIL|ERROR): '`.

**BEFORE A.2-4 — 21 red in three classes:**

- **(а) — 1.** The expectation lived in an artefact that carries `signed_by`:
  `Lot1vVGateTest::test_the_old_zone_words_are_load_bearing` (it read
  `_meta.signed_by` of `lot1v_v_manifest_BASE_P7.json` and said so).
- **(б) — 17.** The expectation was a literal in the code or in the test: the six
  pinned gate constants (`P7_GAINS/CONTROLS`, `LOT1_*`, `LOT1V_A_*`, `LOT1V_B_*`,
  `LOT1V_V_*`, the „7 tokens in 6 zones“ spec), five literals in the test file
  (`test_the_branch_stands_after_the_zone_and_before_the_fuzzy_path`,
  `test_the_collision_rule_is_load_bearing`, `test_added_tokens_are_the_measured_seven`,
  `test_no_added_token_is_a_name_token`, `test_the_foreign_token_guard_is_load_bearing`),
  three pinned anchor COMMITS (`test_the_kind_of_every_frozen_record_is_unchanged` ×2,
  `test_haskey_could_not_have_moved_and_agrees_with_every_branch`) and the three
  ERRORs below.
- **(в) — 3.** The three „replay“ tests compared the engine with the frozen
  reference, which has no `signed_by` at all: `FrozenDiffTest::test_the_live_engine_replays_the_artefact`,
  `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket`,
  `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket`.

The three ERRORs of class (б) named engine attributes that ЛОТ 1в-В had already
removed — `REF.ZONE_PHRASES`, `rec.zph`, `rec.ztk`. They were repaired
mechanically to what the engine carries today (`REF.LOC_PHRASES`; `qph`/`lph`/`gph`;
`qtk`/`ltk`/`legtk`/`ktk`) — an edit, never a signature, exactly as амандамент №4
said. All three are green.

**AFTER A.2-4 — 6 red, one class.** Every delivery-dependent expectation left the
code for `scratch/places_search/expectations.json`; the suite compares the engine
with that tracked body (which can and does fail: move the engine, forget the
artefact, and it is red), and whether Petar has SIGNED it is the release gate's
question — план v2 §0.4 („очакване, което чака подпис, е ред в опашката, не
червен тест“) and §A.2 („готовността на доставката отива в release-гейта“).

The six that remain are one claim in six places: **the frozen reference is still
the one of лот Б and the engine has moved past it** — they go green with the ONE
`--freeze` Petar's signature unlocks, and with nothing else:

- `FrozenDiffTest::test_the_live_engine_replays_the_artefact` · `::test_rows_carry_the_p7_measure`
- `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket` · `::test_the_bucket_is_the_signed_answers`
- `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket` · `::test_the_bucket_is_the_signed_answers`

Every one of them reads `expectations.json` (grep: `require_expectations`, `EXP[`,
`gate_answers(`, `anchor_block(`, `claim(`). Proved in an isolated clone of this
commit: sign `expectations.json` and the two manifests, run `--freeze` once, run
the suite → **0 red**; the clone is thrown away. `ReleaseGateSignatureTest` is the
one test that reads `signed_by`, and it is the fixture the plan asked for:
an unsigned artefact → `gates.release` BLOCKED.

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
