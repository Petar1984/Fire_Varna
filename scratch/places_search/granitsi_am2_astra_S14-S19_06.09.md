Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git\Fire_Varna
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a0738e-0d09-7683-bfde-65c5c537e1d2
--------
user
Read scratch/places_search/granitsi_am2_brief_astra.md and execute it exactly: REFUTE the mechanics of docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md on questions S14–S19, citing file:line from docs/decisions/010_signed_quarter_boundaries.md, docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md and docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md. Read-only; no file changes; at most 1500 words; answer in Bulgarian with English identifiers.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще прочета brief-а и посочените документи, ще проверя механиката по S14–S19 и ще върна опровержения с точни препратки файл:ред. Работя само за четене.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 100" in C:\git\Fire_Varna
 succeeded in 0ms:
# Active context â€” Fire_Varna

> **05.09.2026 16:55 â€” Ð”ÐžÐ¡Ð¢ÐÐ’ÐšÐ A ÐŸÐ£Ð‘Ð›Ð˜ÐšÐ£Ð’ÐÐÐ:** ÐŸÐµÑ‚ÑŠÑ€ Ð¿ÑƒÑˆÐ½Ð° `6da5d9a..fd13907` Ð¿Ñ€ÐµÐ· ÐºÑƒÐºÐ°Ñ‚Ð° (306 Ñ‚ÐµÑÑ‚Ð° OK, 7/7 Ð³ÐµÐ¹Ñ‚Ð°). ÐŸÑƒÐ±Ð»Ð¸ÐºÑƒÐ²Ð°Ð½Ð¸Ñ‚Ðµ blob-Ð¾Ð²Ðµ = Ð»Ð¾ÐºÐ°Ð»Ð½Ð¸Ñ‚Ðµ (hotels 46a44ce82f15, places 329310f577e8, categories 874e33cd00e2, index.html 3d3bf79b58bf). Ð–Ð¸Ð²Ð°Ñ‚Ð° ÐºÐ°Ñ€Ñ‚Ð°: Ñ…Ð¾Ñ‚ÐµÐ»Ð¸ Ñ ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð» 152/225, ÐÐ”ÐœÐ˜Ð ÐÐ› = Ðº.Ðº. Ð—Ð»Ð°Ñ‚Ð½Ð¸ Ð¿ÑÑÑŠÑ†Ð¸ (REG). Ð¡Ð»ÐµÐ´Ð²Ð°Ñ‰ Ð»Ð¾Ñ‚: â€žÐ“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµâ€œ (`docs/sessions/ÐŸÐ ÐžÐœÐŸÐ¢_Ð½Ð¾Ð²Ð°_Ñ‚ÐµÐ¼Ð°_Ð“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµ.md`); Ð¿Ñ€ÐµÐ´Ð¸ ÑÐ»ÐµÐ´Ð²Ð°Ñ‰Ð°Ñ‚Ð° Ð´Ð¾ÑÑ‚Ð°Ð²ÐºÐ° â€” A.2-11 (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–10).


**Date:** 2026-09-05 Â· **HEAD:** A.2-4 = this commit (its parent is `a694c7e`, A.2-3) Â· **branch:** `main` Â· **signed:** __

> One page. Every number below is the output of the command next to it, run on the date above; a number without a command does not enter. The chronicle of 03â€“04.09 (Ð›ÐžÐ¢ 1, 1Ð²-Ð, 1Ð²-Ð‘, 1Ð²-Ð’, the pre-rebase hash table) is frozen in [archive/activeContext_2026-09-04.md](archive/activeContext_2026-09-04.md); the one before it in [archive/activeContext_2026-07-04.md](archive/activeContext_2026-07-04.md).

## What this repo is

The public mobile-first web app that shows a Varna-oblast firefighter the nearest working hydrant, with no install and no account. Live: <https://petar1984.github.io/Fire_Varna/> (GitHub Pages, `main`, path `/`). Field reports are moderated by Petar before they change data. Governance: `AGENTS.md`; executor rules: `CLAUDE.md`.

## Where the work stands (05.09)

**Ð¤Ð°Ð·Ð° A of `plans/ÐŸÐ›ÐÐ_Ð˜Ð—Ð§Ð˜Ð¡Ð¢Ð’ÐÐÐ•_v2_05.09.md` (signed 05.09 02:50) + its four amendments: F12 (Ð°â€“Ð·) and A.2 (1â€“4) are executed and wait for Petar.** F12 copies the P7 delivery of varna_3d (Ðœ2 + Ðœ3 + Ðœ6) into `data/`, re-pins the three SHA constants, bumps the places cache to v6, opens the closed client lists for the three codes the delivery carries (`mladost`, `briz`, `morska_gradina`), adds the Ðœ7 â€žbare placeâ€œ branch on both sides, moves the two bundle tests onto the delivered numbers (F12-Ð´), narrows Ðœ7 to significant tokens (F12-Ðµ) and makes every manifest anchor that names a commit the bytes of the **blob** at that commit (F12-Ð¶).

**A.2 built the release machinery** (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4): `gates/release.py` â€” Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 6 â€” binds the frozen reference, the engine candidate, the pinned inputs and the manifests by digest and refuses every delta that no signed queue row covers; `gates/sign.py` applies â€žÐ´Ð°/Ð½Ðµâ€œ to a queue row and to the artefact it governs and refuses to run while the git identity is an agent's; Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 7 reads back with `git log -S` who INTRODUCED each signature; the pre-push hook now runs the suite AND the gates and has no break-glass at all; and every delivery-dependent expectation left the code for one signable body, `scratch/places_search/expectations.json`. **Nothing is frozen and nothing is published.**

Four things are waiting for Petar's own hand â€” none of them may be written by an agent:

1. `gates/baseline/MANIFEST.json` â†’ `signed_by: "ÐŸÐµÑ‚ÑŠÑ€"` (â€žÐ¿Ð¾Ð´Ð¿Ð¸ÑÐ²Ð°Ð¼ baseline f06ac06â€œ).
2. `gates/allow/2026-09-05_lot1v_v.json` â€” 150 named rows in four reason classes (`hull_artifact` 80 Â· `no_witness` 56 Â· `resort_pending` 8 Â· `m6_changed` 6).
3. `scratch/places_search/lot1v_v_manifest_BASE_P7.json` and `â€¦_P7_F12.json` â€” the two diffs, every row shown; the P7â†’F12 one also carries the two controls of gate 6 (â€žÐ¿Ñ€Ð¸Ð¼Ð¾Ñ€ÑÐºÐ¸â€œ, â€žÐ²Ð»Ð°Ð´Ð¸ÑÐ»Ð°Ð² Ð²Ð°Ñ€Ð½ÐµÐ½Ñ‡Ð¸Ðºâ€œ) as a signable delta.
4. `scratch/places_search/m7_trigger_tokens.json` â€” **33 triggering words**, waiting for a signature.
5. `scratch/places_search/expectations.json` â€” the ONE body every delivery-dependent expectation now lives in (the answers of the 78 gate questions, the Â§10 sweep, the ÐŸ7 measure, 15 claims, the three bucket anchors, the replay counts, and the â€žbeforeâ€œ of every question as the frozen reference answered it). `python -m gates.sign <id> Ð´Ð°` writes the signature; an agent writes only `pending â€” ÐŸÐµÑ‚ÑŠÑ€`.
6. `scratch/places_search/Ð—Ð_ÐŸÐžÐ”ÐŸÐ˜Ð¡_<Ð´Ð°Ñ‚Ð°>.md` â€” the queue itself (A.3, not written yet). Until it exists Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 6 is RED with â€žÐ½ÑÐ¼Ð° Ð¾Ð¿Ð°ÑˆÐºÐ°â€œ, which is the fail-closed answer, not a defect. F12-Ðµ closed the short-prefix defect: the eight type prefixes (`Ðº`, `ÐºÐ²`, `Ð¶`, `Ð¼`, `Ñ`, `Ð¾`, `Ñ‚`, `Ð·Ð¾Ð½Ð°`) no longer fire the branch; the 45 measured candidates stay in the file with `triggers: false` so what was thrown out stays visible.

The 8 resort conflicts (Ð”ÐÐ›Ð˜Ð¯ Ð“ÐÐ Ð”ÐªÐ Â· Ð¤Ñ€ÐµÐ³Ð°Ñ‚Ð° Â· ÐœÐÐ“ÐÐžÐ›Ð˜Ð¯ 1 Ð˜ 2 Â· ÐœÐ°ÑÐº Â· ÐÐ•ÐŸÐ¢Ð£Ð Â· Ð Ð¾Ð¼Ð°Ð½Ñ‚Ð¸ÐºÐ° Â· Ð Ð£Ð¡ÐÐ›ÐšÐ Â· Ð¡Ð¢Ð ÐÐÐ”Ð–Ð) stay `pending_signature`: the map shows them as â€žÑ€Ð°Ð¹Ð¾Ð½ Xâ€œ until he decides each one.

## Current state

| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| commits on `main` | 327 | `git rev-list --count main` |
| commits ahead of `origin/main` (Petar alone pushes) | 46 | `git rev-list --count origin/main..main` |
| commits on `origin/main` not on `main` | 0 | `git rev-list --count main..origin/main` |
| last pushed commit | 6da5d9a 2026-09-04 | `git log -1 --format='%h %cs' origin/main` |
| records in `data/hydrants.json` | 7407 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"` |
| records per origin | [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 151), ('pozarna_gz', 99), ('etr_devnya', 78)] | `PYTHONIOENCODING=utf-8 python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"` |
| `index.html` bytes (557270 before F12; 560365 after F12-Ð·) | 560855 | `wc -c < index.html` |
| `data/hydrants.json` bytes | 1315276 | `wc -c < data/hydrants.json` |
| first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | 1876131 B = 1,79 MB | `python -c "import os;print(os.path.getsize('index.html')+os.path.getsize('data/hydrants.json'))"` |
| `data/hotels.json` (225 rows Ã— 17 keys; 142543 B before F12) | 148685 B Â· sha `46a44ce82f15â€¦` | `wc -c < data/hotels.json` Â· `git show HEAD:data/hotels.json \| sha256sum` |
| `data/places.json` (150 rows Ã— 13 keys; 121621 B before F12) | 122089 B Â· sha `329310f577e8â€¦` | `wc -c < data/places.json` Â· `git show HEAD:data/places.json \| sha256sum` |
| `data/place_categories.json` (64831 B before F12) | 75818 B Â· sha `874e33cd00e2â€¦` | `wc -c < data/place_categories.json` Â· `git show HEAD:data/place_categories.json \| sha256sum` |
| typed locations on the 375 delivered rows: quarter Â· locality Â· district (140 Â· 8 Â· 375 before F12) | 201 Â· 12 Â· 375 | `PYTHONIOENCODING=utf-8 python -c "import json;r=[x for f,k in (('data/places.json','places'),('data/hotels.json','hotels')) for x in json.load(open(f,encoding='utf-8'))[k]];print(sum(1 for x in r if x['quarter']), sum(1 for x in r if x['locality']), sum(1 for x in r if x['district']))"` |
| dictionary: forms Â· `legacy_by_row` Â· zones (283 Â· 209 Â· 19 before F12) | 283 Â· 18 Â· 20 | `PYTHONIOENCODING=utf-8 python -c "import json;c=json.load(open('data/place_categories.json',encoding='utf-8'));print(c['_meta']['n_forms'], len(c['legacy_by_row']), len(c['zones']))"` |
| search reference `scratch/places_search/recall_sweep_rows.json` â€” NOT frozen by F12 (report-only) | 140 rows, untouched since `148c731` (the commit before F12-Ð°) | `git diff --stat 148c731 -- scratch/places_search/recall_sweep_rows.json` |
| manifest anchor of `lot1v_v_manifest_BASE_P7.json`: the **blob** at the named commit, not the file on disk (F12-Ð¶) | `f06ac06` â†’ `0bc7a189f408â€¦` Â· 256070 B (the CRLF twin on a Windows worktree is 266021 B and the same OID) | `python scratch/places_search/manifest_anchor_gate.py` Â· `git show f06ac06:scratch/places_search/recall_sweep_rows.json \| sha256sum` |
| tests (241 after F9; 259 before A.2-4) Â· red | Ran 266 Â· FAILED (failures=6) = 6 red, all in `tests/test_places_search_gate.py` (see the split below) | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests 2>&1 \| tail -3` |
| gates | â›” Ð§Ð•Ð Ð’Ð•ÐÐž: Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 6 (release) â€” 173 delta between the frozen reference and the engine candidate and no queue to cover them; Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° 4 âš  waits for two signatures; 1, 2, 3, 5, 7 green | `python -m gates.run_gates` |
| release gate: reference â†” candidate | reference 140 queries / 2121 rows Â· candidate 203 / 3160 Â· 173 delta Â· 0 covered (no queue yet) | `python -m gates.release` |
| `scratch/places_search/expectations.json` | 321040 B Â· `signed_by: "pending â€” ÐŸÐµÑ‚ÑŠÑ€"` Â· 78 gate questions Â· 62 + 10 sweep rows Â· 15 claims Â· 3 bucket anchors | `PYTHONIOENCODING=utf-8 python scratch/places_search/recall_sweep.py --manifest` |
| coverage of the delivery against the signed baseline `f06ac06` | places zone_named 127 â†’ 49 Â· hotels 199 â†’ 152 Â· uncovered 0 Â· exit 5 (unsigned allow) | `python -m gates.coverage --places-base git:f06ac06:data/places.json --places-candidate data/places.json --hotels-base git:f06ac06:data/hotels.json --hotels-candidate data/hotels.json --allow gates/allow/2026-09-05_lot1v_v.json` |
| Worker deploy version (repo-declared) | 5accc88e | `sed -n '20p' worker/README.md \| grep -oE '[0-9a-f]{8}'` |
| web manifest (`rel="manifest"`) in `index.html` | 0 | `grep -c 'rel="manifest"' index.html` |
| local branches (traces of closed cycles; work happens on `main`) | backup/pre-c17-split Â· backup/pre-c32-split Â· hydrants-c32 Â· lot1-client Â· main | `git branch --format='%(refname:short)'` |

Two rows of the previous page are NOT re-measured here because they need the network (satellite link): the open/closed issue counts (`gh issue list â€¦`) and the Pages status code (`curl â€¦`). Read them from the archive with their date, or run the command.

### The red tests: 21 before A.2-4, 6 after (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4 Ñ‚. 1 Ð¸ Ñ‚. 7)

The class is decided by **where the expectation lives**, measured by reading each test:
`PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -v 2>&1 | grep -E '^(FAIL|ERROR): '`.

**BEFORE A.2-4 â€” 21 red in three classes:**

- **(Ð°) â€” 1.** The expectation lived in an artefact that carries `signed_by`:
  `Lot1vVGateTest::test_the_old_zone_words_are_load_bearing` (it read
  `_meta.signed_by` of `lot1v_v_manifest_BASE_P7.json` and said so).
- **(Ð±) â€” 17.** The expectation was a literal in the code or in the test: the six
  pinned gate constants (`P7_GAINS/CONTROLS`, `LOT1_*`, `LOT1V_A_*`, `LOT1V_B_*`,
  `LOT1V_V_*`, the â€ž7 tokens in 6 zonesâ€œ spec), five literals in the test file
  (`test_the_branch_stands_after_the_zone_and_before_the_fuzzy_path`,
  `test_the_collision_rule_is_load_bearing`, `test_added_tokens_are_the_measured_seven`,
  `test_no_added_token_is_a_name_token`, `test_the_foreign_token_guard_is_load_bearing`),
  three pinned anchor COMMITS (`test_the_kind_of_every_frozen_record_is_unchanged` Ã—2,
  `test_haskey_could_not_have_moved_and_agrees_with_every_branch`) and the three
  ERRORs below.
- **(Ð²) â€” 3.** The three â€žreplayâ€œ tests compared the engine with the frozen
  reference, which has no `signed_by` at all: `FrozenDiffTest::test_the_live_engine_replays_the_artefact`,
  `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket`,
  `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket`.

The three ERRORs of class (Ð±) named engine attributes that Ð›ÐžÐ¢ 1Ð²-Ð’ had already
removed â€” `REF.ZONE_PHRASES`, `rec.zph`, `rec.ztk`. They were repaired
mechanically to what the engine carries today (`REF.LOC_PHRASES`; `qph`/`lph`/`gph`;
`qtk`/`ltk`/`legtk`/`ktk`) â€” an edit, never a signature, exactly as Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4
said. All three are green.

**AFTER A.2-4 â€” 6 red, one class.** Every delivery-dependent expectation left the
code for `scratch/places_search/expectations.json`; the suite compares the engine
with that tracked body (which can and does fail: move the engine, forget the
artefact, and it is red), and whether Petar has SIGNED it is the release gate's
question â€” Ð¿Ð»Ð°Ð½ v2 Â§0.4 (â€žÐ¾Ñ‡Ð°ÐºÐ²Ð°Ð½Ðµ, ÐºÐ¾ÐµÑ‚Ð¾ Ñ‡Ð°ÐºÐ° Ð¿Ð¾Ð´Ð¿Ð¸Ñ, Ðµ Ñ€ÐµÐ´ Ð² Ð¾Ð¿Ð°ÑˆÐºÐ°Ñ‚Ð°, Ð½Ðµ
Ñ‡ÐµÑ€Ð²ÐµÐ½ Ñ‚ÐµÑÑ‚â€œ) and Â§A.2 (â€žÐ³Ð¾Ñ‚Ð¾Ð²Ð½Ð¾ÑÑ‚Ñ‚Ð° Ð½Ð° Ð´Ð¾ÑÑ‚Ð°Ð²ÐºÐ°Ñ‚Ð° Ð¾Ñ‚Ð¸Ð²Ð° Ð² release-Ð³ÐµÐ¹Ñ‚Ð°â€œ).

The six that remain are one claim in six places: **the frozen reference is still
the one of Ð»Ð¾Ñ‚ Ð‘ and the engine has moved past it** â€” they go green with the ONE

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
 succeeded in 0ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 13, behind 1]
?? scratch/places_search/agkk_inspire_2026-09-05/agkk_au5_varna.geojson
?? scratch/places_search/agkk_inspire_2026-09-05/agkk_geonames.json
?? scratch/places_search/agkk_inspire_2026-09-05/agkk_gn_points_varna.json
?? scratch/places_search/agkk_inspire_2026-09-05/agkk_gn_surfaces_varna.geojson
?? scratch/places_search/agkk_inspire_2026-09-05/agkk_layers_meta.json
?? scratch/places_search/agkk_inspire_2026-09-05/agkk_services.json
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md
?? scratch/places_search/granitsi_am2_brief_astra.md
?? scratch/places_search/granitsi_am2_brief_kimi.md
?? scratch/places_search/granitsi_am2_kimi_K15-K20_06.09.md
?? scratch/places_search/granitsi_brief_astra.md
?? scratch/places_search/granitsi_brief_kimi.md
?? scratch/places_search/lot1_reference_preview.md
?? scratch/places_search/lot1g_brief_kimi.md
?? scratch/places_search/lot1g_brief_sol.md
?? scratch/places_search/lot1v_v2_brief_kimi.md
?? scratch/places_search/lot1v_v2_brief_sol.md
?? scratch/places_search/lot1v_v_m6_brief_kimi.md
?? scratch/places_search/lot1v_v_m6_brief_sol.md
?? scratch/places_search/lot1v_v_m6_fix_sample.md
?? scratch/places_search/osm_hints_brief_astra.md
?? scratch/places_search/osm_hints_brief_kimi.md
?? scratch/places_search/osm_quarters_brief_astra.md
?? scratch/places_search/osm_quarters_brief_kimi.md
?? scratch/places_search/ОТЧЕТ_A210_05.09.md
?? scratch/places_search/ОТЧЕТ_A25_05.09.md
?? scratch/places_search/ОТЧЕТ_A26_05.09.md
?? scratch/places_search/ОТЧЕТ_A27_05.09.md
?? scratch/places_search/ОТЧЕТ_A29_05.09.md
?? scratch/places_search/ОТЧЕТ_A2_05.09.md
?? scratch/places_search/ОТЧЕТ_A3_05.09.md
?? scratch/places_search/ОТЧЕТ_A4_freeze_05.09.md
?? scratch/places_search/ОТЧЕТ_F0zh_05.09.md
?? scratch/places_search/ОТЧЕТ_F12_05.09.md
?? scratch/places_search/ОТЧЕТ_F12de_05.09.md
?? scratch/places_search/ОТЧЕТ_F12zh_05.09.md
?? scratch/places_search/ОТЧЕТ_ЛОТ0-fix_05.09.md
?? scratch/places_search/ОТЧЕТ_ЛОТ0_05.09.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$targets = @('"'scratch/places_search/granitsi_am2_brief_astra.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md'); "'$targets | Sort-Object | ForEach-Object { $f=Get-Item -LiteralPath $_; '"'{0} | {1} bytes | {2} lines' -f "'$_,$f.Length,(Get-Content -LiteralPath $_ | Measure-Object -Line).Lines }' in C:\git\Fire_Varna
 succeeded in 21ms:
docs/decisions/010_signed_quarter_boundaries.md | 53242 bytes | 95 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md | 61905 bytes | 203 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | 26249 bytes | 61 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | 30160 bytes | 61 lines
scratch/places_search/granitsi_am2_brief_astra.md | 4915 bytes | 8 lines

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'scratch/places_search/granitsi_am2_brief_astra.md' -TotalCount 150 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # Brief for Astra (Codex, GPT-6, ultra) Â· REFUTE the mechanics of Amendment â„–2 to ÐŸÐ›ÐÐ â€žÐ“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµâ€œ v2 (06.09.2026). Lens: MECHANICS and REGRESSIONS (not licence â€” Kimi covers that). Read-only; no file changes; at most 1500 words; cite file:line; exact, runnable checks.
   2: 
   3: Context (do not repeat): the owner confirmed that the human-drawn quarter polygons of Varna on Wikimapia are the boundaries he wants (â€žÐ¿Ñ€ÐµÐ³Ð»ÐµÐ´Ð°Ñ… Ñ€Ð°Ð¹Ð¾Ð½Ð¸Ñ‚Ðµ Ð¾Ñ‚ ÑƒÐ¸ÐºÐ¸Ð¼Ð°Ð¿Ð¸Ð° â€” Ð½ÐµÐºÐ° Ð¿Ð¾Ð»Ð·Ð²Ð°Ð¼Ðµ Ñ‚ÑÑ…â€œ); he draws nothing. The amendment replaces the drawing tool (Ð“1/Ð“2 of plan v2) with a REVIEW BOARD (local HTML in the ignored scratch folder; yes/no/defer per quarter; produces granitsi_decisions_DATE.json that Petar commits) and an ASSEMBLY step Ð“2-Ð° in varna_3d turning decisions + pinned polygons into data/quarters_signed.geojson (D1 provenance; wm_polygon_sha256; precision_m at least 100 m for wikimapia; Feature-level licences). Sources ranked: official polygon (ÐÐ“ÐšÐš INSPIRE GN, 6 codes; municipal ArcGIS â€žÐšÐ²Ð°Ñ€Ñ‚Ð°Ð»Ð¸â€œ, 52 polygons, locked) > reconstructed official plan (ÐžÐ´ÐµÑÐ¾Ñ 11 micro-districts georeferenced by affine fit on 15 cadastral-region centroids, rms 11 m; numbers not names) > Wikimapia human polygon confirmed per quarter > written source per place (unchanged). Collection: Wikimapia API demo key, place.getnearest at about 670 probe points, about 28 s per call, keep polygons of at least 0.04 kmÂ²; after the sweep the file is frozen (copy + sha256) and only the frozen body is measured. Files to read: docs/plans/ÐŸÐ›ÐÐ_Ð›ÐžÐ¢_Ð“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµ_v2_Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚_2_06.09.md (the amendment), docs/decisions/010_signed_quarter_boundaries.md (ADR 010), docs/plans/ÐŸÐ›ÐÐ_Ð›ÐžÐ¢_Ð“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµ_v2_05.09.md Â§2, docs/plans/ÐŸÐ›ÐÐ_Ð›ÐžÐ¢_Ð“Ñ€Ð°Ð½Ð¸Ñ†Ð¸Ñ‚Ðµ_v2_Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚_1_05.09.md.
   4: 
   5: S14. **Coverage risk of the collection method.** place.getnearest returns the 100 nearest places by centre distance; a quarter polygon appears only when its centre is among the 100 nearest to some probe point. With probes at 163 quarter centres plus a 500 m grid over 27.84â€“27.985 E Ã— 43.170â€“43.262 N: name the concrete failure modes (large polygons whose centre falls between probes; dense block areas where 100 buildings crowd out the quarter; polygons with centre outside the bbox â€” resorts Ð—Ð»Ð°Ñ‚Ð½Ð¸ Ð¿ÑÑÑŠÑ†Ð¸ / Ð¡Ð². ÐšÐ¾Ð½ÑÑ‚Ð°Ð½Ñ‚Ð¸Ð½; multipolygons) and ONE cheap completeness check (for example re-probe at the centroid of every registry quarter without a match, count=100, then at four points 300 m off). Is a 500 m grid sufficient given 100 results per call? Give the arithmetic.
   6: S15. **The board without drawing.** Refute the decisions-file design: what must granitsi_decisions_DATE.json carry so that Ð“2-Ð° is deterministic and auditable (wm_id, wm_polygon_sha256 of the frozen body, registry code, choice in {official, reconstructed, wikimapia, none, deferred}, reason, board page sha256, data sha256, decided_at) â€” what is missing, what is superfluous, and how the Blob + download-link path can fail on Windows/Edge (filename, encoding, CRLF) in a way that breaks the sha256 chain. Propose the exact check the executor runs before commit.
   7: S16. **D6 write rules with two boundary classes.** Polygon-to-place writing: only empty, undisputed rows; edge 50 m; written quarter never changed (G17). With wikimapia precision_m at least 100 m, is the 50 m edge still coherent (should edge be at least precision_m?) â€” give the rule and a fixture. Conflicts: human vs human (two â€žÐ Ð°Ð¹Ð¾Ð½ ÐœÐ»Ð°Ð´Ð¾ÑÑ‚â€œ polygons), one polygon vs two codes (â€žÐšÐ¾Ð¼Ð¿Ð»ÐµÐºÑ Ð§Ð°Ð¹ÐºÐ°â€œ vs chaika_kv / chaika_kk), wrong kind (Ñ€Ð°Ð¹Ð¾Ð½ / Ñ.Ð¾. vs ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð»). Refute the amendment's handling; state the minimal deterministic rule.
   8: S17. **Regression matrix S7 under the new ladder.** Frozen search reference (375 places, quarter search) â€” which regressions become possible when SIGNED_POLYGON writes about 150 empty rows at once (search collisions with unmarked streets; â€žÐœÐ»Ð°Ð´Ð¾ÑÑ‚â€œ matching both the Ñ€Ð°Ð¹Ð¾Ð½ polygon and the Ð¶Ðº codes; ordering of results). Name the fixtures that must fail before and pass after.
   9: S18. **Georeferencing honesty.** The ÐžÐ´ÐµÑÐ¾Ñ micro-districts (affine fit, 15 control points from cadastral-region face centroids, rms 11 m / max 21 m; polygons vectorised from a rasterised PDF at 2 pt per pixel) â€” is rms on centroids a valid accuracy claim for the BOUNDARY line; what should precision_m be (3Ã—rms? max residual + raster cell?), and what single independent check (for example distance from the vectorised ÐœÐ  boundary to the nearest KAIS parcel edge along a sample of 20 vertices) proves the line, not the fit.
  10: S19. **Verdict:** Ð“ÐžÐ”ÐÐž / ÐÐ•Ð“ÐžÐ”ÐÐž for Â§2, Â§4, Â§5, Â§6 with named fixes; and one sentence: what must be true before Petar signs.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$targets = @('"'docs/activeContext.md','scratch/places_search/granitsi_am2_brief_astra.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md'); "'$targets | Sort-Object -CaseSensitive | ForEach-Object { $f=Get-Item -LiteralPath $_; '"'{0} | {1} bytes | {2} lines' -f "'$_,$f.Length,@(Get-Content -LiteralPath $_ -Encoding UTF8).Count }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 42" in C:\git\Fire_Varna
 succeeded in 0ms:
# Active context — Fire_Varna

> **05.09.2026 16:55 — ДОСТАВКА A ПУБЛИКУВАНА:** Петър пушна `6da5d9a..fd13907` през куката (306 теста OK, 7/7 гейта). Публикуваните blob-ове = локалните (hotels 46a44ce82f15, places 329310f577e8, categories 874e33cd00e2, index.html 3d3bf79b58bf). Живата карта: хотели с квартал 152/225, АДМИРАЛ = к.к. Златни пясъци (REG). Следващ лот: „Границите“ (`docs/sessions/ПРОМПТ_нова_тема_Границите.md`); преди следващата доставка — A.2-11 (амандамент №10).


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

 succeeded in 27ms:
docs/activeContext.md | 15557 bytes | 132 lines
docs/decisions/010_signed_quarter_boundaries.md | 53242 bytes | 142 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md | 61905 bytes | 264 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | 26249 bytes | 75 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | 30160 bytes | 107 lines
scratch/places_search/granitsi_am2_brief_astra.md | 4915 bytes | 10 lines

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'scratch/places_search/granitsi_am2_brief_astra.md' -Encoding UTF8 -TotalCount 150 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # Brief for Astra (Codex, GPT-6, ultra) · REFUTE the mechanics of Amendment №2 to ПЛАН „Границите“ v2 (06.09.2026). Lens: MECHANICS and REGRESSIONS (not licence — Kimi covers that). Read-only; no file changes; at most 1500 words; cite file:line; exact, runnable checks.
   2: 
   3: Context (do not repeat): the owner confirmed that the human-drawn quarter polygons of Varna on Wikimapia are the boundaries he wants („прегледах районите от уикимапиа — нека ползваме тях“); he draws nothing. The amendment replaces the drawing tool (Г1/Г2 of plan v2) with a REVIEW BOARD (local HTML in the ignored scratch folder; yes/no/defer per quarter; produces granitsi_decisions_DATE.json that Petar commits) and an ASSEMBLY step Г2-а in varna_3d turning decisions + pinned polygons into data/quarters_signed.geojson (D1 provenance; wm_polygon_sha256; precision_m at least 100 m for wikimapia; Feature-level licences). Sources ranked: official polygon (АГКК INSPIRE GN, 6 codes; municipal ArcGIS „Квартали“, 52 polygons, locked) > reconstructed official plan (Одесос 11 micro-districts georeferenced by affine fit on 15 cadastral-region centroids, rms 11 m; numbers not names) > Wikimapia human polygon confirmed per quarter > written source per place (unchanged). Collection: Wikimapia API demo key, place.getnearest at about 670 probe points, about 28 s per call, keep polygons of at least 0.04 km²; after the sweep the file is frozen (copy + sha256) and only the frozen body is measured. Files to read: docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md (the amendment), docs/decisions/010_signed_quarter_boundaries.md (ADR 010), docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md §2, docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md.
   4: 
   5: S14. **Coverage risk of the collection method.** place.getnearest returns the 100 nearest places by centre distance; a quarter polygon appears only when its centre is among the 100 nearest to some probe point. With probes at 163 quarter centres plus a 500 m grid over 27.84–27.985 E × 43.170–43.262 N: name the concrete failure modes (large polygons whose centre falls between probes; dense block areas where 100 buildings crowd out the quarter; polygons with centre outside the bbox — resorts Златни пясъци / Св. Константин; multipolygons) and ONE cheap completeness check (for example re-probe at the centroid of every registry quarter without a match, count=100, then at four points 300 m off). Is a 500 m grid sufficient given 100 results per call? Give the arithmetic.
   6: S15. **The board without drawing.** Refute the decisions-file design: what must granitsi_decisions_DATE.json carry so that Г2-а is deterministic and auditable (wm_id, wm_polygon_sha256 of the frozen body, registry code, choice in {official, reconstructed, wikimapia, none, deferred}, reason, board page sha256, data sha256, decided_at) — what is missing, what is superfluous, and how the Blob + download-link path can fail on Windows/Edge (filename, encoding, CRLF) in a way that breaks the sha256 chain. Propose the exact check the executor runs before commit.
   7: S16. **D6 write rules with two boundary classes.** Polygon-to-place writing: only empty, undisputed rows; edge 50 m; written quarter never changed (G17). With wikimapia precision_m at least 100 m, is the 50 m edge still coherent (should edge be at least precision_m?) — give the rule and a fixture. Conflicts: human vs human (two „Район Младост“ polygons), one polygon vs two codes („Комплекс Чайка“ vs chaika_kv / chaika_kk), wrong kind (район / с.о. vs квартал). Refute the amendment's handling; state the minimal deterministic rule.
   8: S17. **Regression matrix S7 under the new ladder.** Frozen search reference (375 places, quarter search) — which regressions become possible when SIGNED_POLYGON writes about 150 empty rows at once (search collisions with unmarked streets; „Младост“ matching both the район polygon and the жк codes; ordering of results). Name the fixtures that must fail before and pass after.
   9: S18. **Georeferencing honesty.** The Одесос micro-districts (affine fit, 15 control points from cadastral-region face centroids, rms 11 m / max 21 m; polygons vectorised from a rasterised PDF at 2 pt per pixel) — is rms on centroids a valid accuracy claim for the BOUNDARY line; what should precision_m be (3×rms? max residual + raster cell?), and what single independent check (for example distance from the vectorised МР boundary to the nearest KAIS parcel edge along a sample of 20 vertices) proves the line, not the fit.
  10: S19. **Verdict:** ГОДНО / НЕГОДНО for §2, §4, §5, §6 with named fixes; and one sentence: what must be true before Petar signs.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 -TotalCount 150 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # Амандамент №2 към ПЛАН „Границите“ v2 (06.09.2026, ~00:40 **по часовника на машината**) — след присъдата на Петър върху изведените граници, след намирането на човешките полигони (Уикимапия) и след одита в три лещи. Статус: **за Gate 1 — едно четиво за Петър**
   2: 
   3: Нов датиран файл по §0.2 на `docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md:9`. Не редактира плана v2, ADR 010 и амандамент №1; казва какво се променя в тях и защо. Не открива лота, не пипа живата карта, не комитва геометрия.
   4: 
   5: ## 0 · Червен ред преди всичко останало
   6: 
   7: В момента на писане тече `wikimapia_sweep.py` (обход по `place.getnearest`, 163 начални точки + мрежа 500 m, ~28 s на заявка), който събира полигони в `scratch/boundary_gallery/granitsi_preview_05.09/wikimapia_quarters.geojson`. Файлът РАСТЕ (одиторите измериха 88 → 89 → 90 обекта за четири минути) — това е СЪБИРАНЕ, не мярка, и е поръчано от Петър („нека ползваме тях“). Затова обходът се оставя да завърши; **но нищо не се мери, не се показва в борд и не се цитира, преди тялото да бъде замразено**: копие с дата, `sha256` на целия файл, брой обекти, записани в мярката. Дотогава всяко число по-долу е „към 00:36, 90 обекта, НЕЗАМРАЗЕНО“ и **не е годно за подпис**. (Архитектът промени този параграф спрямо синтеза на одиторите, който искаше спиране на процеса: точката им — мярка само върху замразено тяло — е приета изцяло; спирането на самото събиране би оставило Кими-твърдението „20+ квартала“ непроверено.)
   8: 
   9: **Поправка на собствена мярка.** Ранната чернова твърдеше „1 обект, `_meta.note`: дроселиран ключ“. И двете са неверни: обектите бяха деветдесет по време на одита, а `_meta` носи ключове `{attribution, licence, min_km2, not_for_publication, what}` — ключ `note` няма. Правилото оттук: **входовете на борда са пиннати снапшоти, не течащи файлове.**
  10: 
  11: ## 1 · Какво реши Петър
  12: 
  13: Дословно: „нищо няма да чертая аз“ · за КАИС-изведените граници — „много са объркани… направо са грешни“ · „данните от OSM са по-точни; маркирай кварталите според тях; аз ще потвърдя“ · за хибрида — „много е зле… провери във форуми“ · и върху полигона на кв. Кайсиева градина от Уикимапия (id 1851926, CC BY-SA 3.0, 0,42 km²): **„точно това е границата“**.
  14: 
  15: **Какво отпада.** Целият производен клон — обвивките от юли, КАИС-изведените полигони, OSM-Voronoi, уличният вариант, хибридът. Отпада и **чертането** като метод: план v2 §2 (Г1 инструмент → Г2 вечерта на Петър, `ПЛАН_ЛОТ_Границите_v2_05.09.md:104-146`) стъпваше върху „Петър чертае“.
  16: 
  17: **След одита (06.09, ~00:50) Петър добави:** „прегледах районите от уикимапиа — доста добре съм — нека ползваме тях“. Той е прегледал сам кварталите на сайта на Уикимапия — това е неговата извадка по собствения му протокол (5–6 примера) и решение №1 по-долу е ВЗЕТО от него, не чака. Бордът все пак започва с извадката от §7 т. 1 (двата „Район Младост“, „Комплекс Чайка“, Кайсиева, Аспарухово, Бриз), защото там са измерените дефекти.
  18: 
  19: **Какво НЕ следва автоматично.** Едно потвърждение на екрана на Уикимапия не е присъда по квартал в нашия регистър: всяко „да“ се дава по квартал в борда, върху замразения полигон, със записан `wm_id`. Обобщението „човешките полигони съвпадат с картата в главата му“ е точно стъпката без мярка, която роди петте отхвърлени предложения. По неговия собствен протокол (5–6 конкретни примера) стълбата не се пипа, преди да види извадка — вж. §7 т. 1.
  20: 
  21: ## 2 · Стълбата на изворите v3 — за ГРАНИЦАТА
  22: 
  23: Номерацията на D0 (`010_signed_quarter_boundaries.md:36`) се пренарежда: степени (1) и (2) определят **линията**; написаният извор за **мястото** (REG/KAIS/НТР, рангове 0–2) и `POST-2018` остават непроменени.
  24: 
  25: **(1) Официален полигон.** (а) **АГКК INSPIRE `Geo_Names` Surface** — 6 кода, `source: "agkk_inspire_gn"`; заключен по G22/К8. (б) **Общинският слой „Квартали“** (ArcGIS Online `ce83fb2fc9d7416c9778d75f9a98e5dc`, 52 полигона; `municipal_kvartali_layer_05.09.md:4-10`) — **днес заключен** (`SB_0005 Subscription is disabled`), проверката е скрипт `check_municipal_kvartali.py`, не писмо. При отключване — `source: "municipal_arcgis"`, същия G22-механизъм.
  26: 
  27: **(1-б) Реконструиран официален план — ОТДЕЛНО, ПО-НИСКО стъпало.** Одесоските 11 микрорайона са извадени от PDF **по цвят** и закачени с афинна трансформация (rms 11 m без КР 1502, max 21 m; 15 контролни точки) — това е **изведена от агент геометрия**, същият клас, който Петър отхвърли пет пъти. Полетата носят **номера** (МР 1,3,4,7–14), не имена: измерено, `odesos_mr_official.geojson` дава `code: "odesos_mr_7"` / `name: "МР 7"`. **Днес това са 0 кода за G26.** Съответствието МР → регистров код става **собствен подписан ред** в опашката (както Ф0-б crosswalk-а); без него полигонът е само свидетел в леджера. Кайсиева ПУП (rms 8 m по 82 сгради) е частичен — регулационната линия не се затваря — и не влиза като граница.
  28: 
  29: **(2) Човешки полигон — Уикимапия** (CC BY-SA 3.0), `source: "wikimapia"`, `method: "human_polygon"`. Пиннат с **`wm_polygon_sha256`** (ново име: `polygon_sha256` вече е зает от D3 за доставъчния пин, `:42`; на диска днес стои отрязан `poly_sha256_16` — производителят пише пълни 64 hex), плюс `wm_id`, `fetched`, `url`. Канонизацията е **дословно тази на D1** (6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх). **Валиден САМО след изричното „да“ на Петър за ТОЗИ квартал**, придружено с подписан ред от crosswalk-а „заглавие ↔ регистров код“ — никакъв автоматичен матчер.
  30: 
  31: **Конфликтите (разширено D6).** Освен официален ↔ човешки, правилото покрива и три измерени класа: (а) **човешки ↔ човешки** — „Район Младост“ е **два** полигона с различна геометрия (13,22 и 12,34 km²); Петър избира `wm_id`, отхвърленият е свидетел; (б) **един полигон ↔ два кода** — „Комплекс Чайка“ пасва и на `chaika_kv`, и на `chaika_kk`; (в) **грешен вид** — „Район Младост“ е РАЙОН, „Селищно образувание Изгрев“ е с.о.; `classify(code) == field` (D6 `:48`) с падаща фикстура. Заглавията минават през нормализатор (в данните стои `&amp;quot;`, а най-големият обект е „Βарна“ 84,3 km² с **гръцка бета**).
  32: 
  33: **`precision_m` за чужда геометрия.** Днес няма правило и подът 50 подценява реалната неточност. Въвежда се: `district_map_georef` ≥ 3×rms; `wikimapia` ≥ 100 m до доказано друго; Feature без явен `precision_m` = червено; фикстура „rms 11 при `precision_m` 50“.
  34: 
  35: **Какво може да напише полигонът** — непроменено по D6/D7: празен, безспорен, неръбов ред, точно един полигон; **написаният квартал не се променя никога (G17/D18)**.
  36: 
  37: ## 3 · Лицензът — ОТВОРЕНО, с назован въпрос към Кими
  38: 
  39: **Прието третиране:** геометрията остава в `varna_3d/data` и **никога не се публикува** (D3 `:42`); публичният ред остава 13/17 ключа с `quarter: {name, code, src}`. Публикуването на **име** на квартал по място не е адаптация — резултатът не носи израз от полигона, а факт и кратко име; това е логиката на приетия К1.
  40: 
  41: **Отхвърля се** формулировката „файлът става CC BY-SA в мига на първия уикимапийски Feature“. Тя противоречи на приетия К3 („нито един файл не се декларира целият под един лиценз; всяка изворна група със свой лицензов ред“) и е **неизпълнима**: същият файл ще носи АГКК полигони с **неустановени** условия (G22), които не могат да бъдат релицензирани. Затова: **лиценз на ниво Feature** (полето `license` вече е в D1) + `_meta.licences[]`. Това променя §6а т. 3 на план v2 и реда „лицензът на ФАЙЛА е най-строгият участник“ в D2 `:40` → решение §7 т. 4.
  42: 
  43: **ОТВОРЕНО — Кими, лицензна леща (два въпроса, не три):**
  44: 1. **Sui generis право върху база данни.** CC BY-SA 3.0 Unported не лицензира изрично това право (влиза чак в 4.0), а чл. 7(5) на Директива 96/9 забранява **повтарящо се и систематично** извличане дори на несъществени части. Кутиевият обход е точно това. Въпросът не е „съществена извадка ли са 20 полигона“.
  45: 2. **ToS/API.** Условията на сайта и API-то на Уикимапия са **отделен договорен слой** над лиценза; ключът е демо („example“).
  46: 
  47: Присъдата се записва в `_meta.source_terms["wikimapia"] = {url, checked_on, terms, verdict}`.
  48: 
  49: **Резервният път „декларирано местно знание“ ОТПАДА.** Копирана геометрия със `source: "declared_local_knowledge"` не гаси нито BY, нито SA — сменя се етикетът, не произходът. По-лошо: D2 сверява **съгласие между две самообявени полета**, тоест гейтът ще светне зелено върху лъжа, а по таблицата „по памет → CC0-1.0“ ще впише и фалшив лиценз. Петър потвърди линия, но изрично отказа да чертае — координатите остават чужди. `declared_local_knowledge` важи само за линия, изразена от него без чуждата геометрия под ръка. Ако share-alike захапе: или се приема пълната цена, или уикимапийският клон отпада и остават официалните извори.
  50: 
  51: **Етикетът** (К12 важи за декларирана граница и е неверен тук) става дословно: „граница по Уикимапия (обект <id>, свалена <дата>), очертана от доброволци — неофициален извор; CC BY-SA 3.0 (creativecommons.org/licenses/by-sa/3.0/); потвърдена от Петър на <дата>; официален полигон няма (проверено 06.09.2026: АГКК, община — заключена, район, ПУП)“. Потвърждението е **отделно поле**, никога авторство. Уикимапия влиза в йерархията на К13 **под** общинска публикация, **над** OSM възел.
  52: 
  53: **D2 се допълва** (изисква S8): редове `official_polygon` → лицензът на съответния извор; `human_polygon` → CC BY-SA 3.0 с URI и обектен URL; `georef_reconstruction` → лицензът на изходния план; падаща фикстура за всяка нова двойка. Без тях G1-фикстурата „лиценз, несъгласен с метода“ няма какво да сверява. **Пояснение:** забраната „никога Esri“ в D2 е за **подложка**; общинската услуга е данни със свои условия и минава през `source_terms`.
  54: 
  55: ## 4 · Какво се променя в ходовете
  56: 
  57: **Р (регистърът) е ПРЕДИ борда.** Измерено: `Varna_buildings/config/quarter_registry.json` носи 84 записа, жилищни (кв 18 + жк 11 + кк 3) = **32**, **без** `tsveten_kvartal` и без Вл. Варненчик I–V. G26 чете обхвата от **подписания** регистър; при обхват 38 Р-1 минава пръв.
  58: 
  59: **Г1-а · БОРД ЗА ПРЕГЛЕД (Fire_Varna).** Локална страница, която за всеки жилищен код показва официалните и човешките полигони, написаните места вътре, **блоковете на КАИС с номера като слой-проверка** (амандамент №1 §5 т. 3, Б1/Б5 — те НЕ отпадат: без чертане проверката „полигонът съдържа блоковете, които таблицата му приписва, и нито един чужд“ е още по-важна), площ, IoU, извор и дата. Бутони „да“ / „не“ / „отложи“ → `granitsi_decisions_<дата>.json` (Blob + `<a download>`), носещ `sha256` на страницата и на данните ѝ. **Няма код за чертане, няма `POST`.** Живее в игнорирания `scratch` и **не се комитва**. Подложката е **локална** (PMTiles/КАИС) — днешната проба тегли `tile.openstreetmap.org` на живо (`index.html:68`), което D2 не допуска и харчи сателита по време на решаващата сесия. Бордът **не е** инструментът по D11 (няма чертане) — това се обявява изрично; Leaflet остава втора картна библиотека само в scratch.
  60: 
  61: **Г1-б · гейтове и `.gitignore` (varna_3d).** Редът `!data/quarters_signed.geojson` влиза тук — **това отменя §6а т. 20 на план v2 (`:230`) и амандамент №12 към №4 т. 6**, който го връзваше с инструмента.
  62: 
  63: **Г2-а · СГЛОБЯВАНЕ (varna_3d) — новият, дотук неназован ход.** Решенията са JSON във Fire_Varna, геометрията — във varna_3d; `SIGNABLE` (`gates/release.py:175-183`) е затворена шесторка с местни пътища, тоест решенията **не могат** да са подписан артефакт. Затова: `_meta.decisions_sha256` в geojson-а И в `expectations._meta`, плюс гейт „всеки Feature има ред в решенията и обратно“ (отрицателна фикстура: Feature без решение). Всеки от Г1-а, Г1-б, Г2-а получава **репо, изпълнител, изчерпателен write-set, дословно съобщение**.
  64: 
  65: **Г2-б · сесия по потвърждаване.** По квартал: официален / реконструиран / уикимапийски / никакъв. Провенансът на D1 се допълва с `geometry_origin` · `imported_from` · `fetched_at` · `chosen_source` · `chosen_reason` · `confirmed_by` · `confirmed_at`; **`drawn_by` / `drawn_at` / `viewport` / `screenshot_sha256` са `null` при внесена геометрия** (гейт за взаимна изключителност: или ръка, или внос, никога и двете). Това е промяна в D1: черновата запазваше `screenshot_sha256` задължителен, докато маха единствения му производител (условния `preserveDrawingBuffer`), а Leaflet няма нито канва без нова зависимост, нито `bearing`/`pitch` — първият Feature би паднал на G1-фикстурата „липсващо задължително property“. Влиза в §7 т. 2.
  66: 
  67: **Предгейтовете остават дословно:** **G19** (частно репо — М0.15 и до днес НЕ Е ИЗМЕРЕНО) и **G21** (ФАЗА_0) важат за всяко приземяване в `varna_3d/data`.
  68: 
  69: **DWG** — 15 ПУП чертежа R14 на Drive-а на АГУП; три пътя: **QGIS** (вграден libdxfrw, R14; нова инсталация), **LibreDWG** (GPLv3, `dwg2dxf`), **ODA File Converter** (собственически). Решение §7 т. 5.
  70: 
  71: ## 5 · Гейтове
  72: 
  73: - **G25-а · пинът (офлайн, детерминистичен).** `wm_polygon_sha256` се преизчислява от **проследената** геометрия. Фикстура: подменен връх при непроменен sha. **G25-б** е ръчна датирана МЯРКА (не гейт), с път за преподписване (нов `fetched` + довод) — Уикимапия няма поле за версия, а мрежов гейт при демо ключ през сателит е недетерминистичен.
  74: - **G26 · пълнота.** Всеки жилищен код от **подписания регистър** има решение. Преобразува `official` и `wikimapia` в `polygon` — D4 `:44` познава **три** множества (`polygon` / `no_boundary` / `deferred`); разликата живее в колоната `source`. Липсващо решение = ЧЕРВЕНО, поименно.
  75: - **G27 · атрибуцията.** Черновата беше неизпълнима: публикуваният ред няма как да каже, че идва от Уикимапия (`src = SIGNED_POLYGON` по D0), а `_meta` на доставката е **затворен 9-ключов набор** (`qa_fire_varna_places_export.py:62`, налаган на `:550`). Затова G27 се пише като **билд-гейт във varna_3d върху `quarters_signed.geojson`** и сверява **точния низ** от §3. Ако Петър иска реда в публичното приложение, това е нов български UI низ → отделно негово одобрение + `licence_quarter_boundary` в `META_KEYS`, в пиновете на D13 и в двата преписа, в СЪЩИЯ комит.
  76: - **G28 · fail-closed за неприсъдения лиценз.** Feature със `source: "wikimapia"` и празен `_meta.source_terms["wikimapia"].verdict` = ЧЕРВЕНО; износът на редове с уикимапийски квартал е блокиран. Без този гейт „да, условно“ е дума без механизъм (§0.4 „червено = блокирано“).
  77: - **G22 се разширява по механизъм** на `_meta.source_terms[<source>]`, но **изброяването на К8 се запазва дословно** за всеки извор (`terms ∈ {"published:<url>", "none_published_open_by_default"}`); само „празен низ = червено“ би разхлабило приета присъда.
  78: - **G18** не се маха мълчаливо — той е единственото машинно налагане на „никога Esri“. Става статична проверка „в борда няма код, който пише връх“ (пада на нарочно вкаран чертожен код) → решение §7 т. 3.
  79: - **Непроменени:** G1, G17, G19, G21, G23, G24.
  80: 
  81: ## 6 · Мерките ПРЕДИ борда
  82: 
  83: - **М2-1 · покритие, измерено, не цитирано.** Твърдението „20+ от 25 квартала имат полигон“ е на Кими и е **опровергано от собствена мярка**. Върху незамразения файл (90 обекта): по нормализирано име срещу 29-те кода кв+жк съвпадат **15**, но с дефекти: `mladost` → два „Район Младост“ (13,2 и 12,3 km² — район, не жк), `izgrev_kv` → с.о., `briz` → само „Бриз - юг“ 0,19 km², `chaika_kv` ↔ двусмислената „Комплекс Чайка“. **Без полигон са 14 кода**, сред тях точно тези без официален извор: `tsentar`, `maksuda`, `kolhozen_pazar`, `kv_levski`, `troshevo`, `hristo_botev`, `rozova_dolina`, `trakia`, `sv_ivan_rilski`, `mladost1`, `mladost2`. Мярката се повтаря върху замразения файл и се цитира с неговия sha **преди** решенията.
  84: - **М2-2 · припокриване** (IoU, разлика в площ, симетрична разлика) срещу АГКК повърхнините. **Честно днес: сравними двойки са само Аспарухово/Галата/Чайка; с Одесос МР — нула, докато crosswalk-ът не е подписан.** `shapely` 2.1.2 + `pyproj` 3.6.1 (D7) — нула нови зависимости.
  85: - **М2-3 · местата вътре — днес НЕИЗПЪЛНИМА, обявено.** Популацията е **159**, не 174 (D6 `:48`), с поименен списък на изключените. Координатите трябва да дойдат от пиннатия вход по D10 (`lat`/`lon` в `place_identity.json` — мерено: 375 обекта, **0** с координата), а `places_375_hybrid.geojson` е негоден: `_meta` е празен, папката е игнорирана, координатите му съвпадат с изнесените (D7 `:50` забранява четенето им), а properties носят етикети от **отхвърления** хибрид (`derived: "osm:цветен_квартал"`). Мярката чака P8-а.
  86: 
  87: **Обхватът 38 задължава** преизмерване на уникалността по D12 върху ИЗНЕСЕНИЯ речник + фикстура за сблъсък с немаркирана улица (S7 е).
  88: 
  89: ## 7 · Решенията за Петър (четири отворени + едно взето)
  90: 
  91: 1. **Тръгваме ли по уикимапийския път?** — **ВЗЕТО от Петър** („прегледах районите от уикимапиа… нека ползваме тях“, 06.09 ~00:50). Остава процедурата: бордът започва с извадката от **5–6 полигона** с измерени дефекти (двата „Район Младост“, „Комплекс Чайка“, Кайсиева, Аспарухово, Бриз), преди останалите.
  92: 2. **Стълбата v3 и D1** (§2, §4) — чужда геометрия с провенанс вместо ръка; `drawn_*` и `screenshot_sha256` стават `null` при внос. Препоръка: **да**.
  93: 3. **G18** — превръща се в статична проверка „борд без чертожен код“ вместо да отпадне. Препоръка: **да**.
  94: 4. **Лицензът на файла** — на ниво Feature (`_meta.licences[]`) вместо „най-строгият участник“; това променя D2 и §6а т. 3. Препоръка: **да** — иначе АГКК полигонът е нерелицензируем. Уикимапийският клон остава **блокиран от G28** до присъдата на Кими.
  95: 5. **Обхватът 32 или 38 и заглавното обещание.** Честно: при новата стълба **Център, Максуда, Колхозен пазар, Левски, Цветен квартал** нямат нито официален, нито човешки полигон — отиват в `no_boundary`/`deferred`, а проверката „училище цветен квартал“ след пуша става **НЕПРИЛОЖИМА** (план v2 §6 т. 4 я обявява за провал на целта). Препоръка: **38**, с изричен запис, че обещанието пада — или **32** и лотът се преформулира.
  96: 
  97: **(Отложено, не решение сега.)** DWG-инструмент: препоръка **не сега**; отваря се само ако след борда останат комплекси без приемлива граница, и тогава по реда QGIS → LibreDWG → ODA.
  98: 
  99: ## 8 · Оборване (чака)
 100: 
 101: **Кими — лицензна леща:** двата въпроса от §3 (sui generis при 3.0 Unported + чл. 7(5) на Дир. 96/9; ToS/демо ключ), плюс ЗДПД/ЗДОИ за общинския слой и районните карти. **Astra — механична леща:** борд без чертане, форматът на решенията, честността на геореференцията (rms, контролни точки, МР ↔ име), регресиите по S7, G25-а/G26/G27/G28. Само Astra и Кими; никакъв Sol.
 102: 
 103: ## 9 · Какво НЕ се променя и кога тръгва
 104: 
 105: Нищо от §4 не тръгва преди Gate 1 **и** Г0-б **и** пуша. Измерено сега: Fire_Varna `main` е **ahead 12, behind 1** спрямо origin (локалното не е дори наравно с публикуваното), varna_3d `rezhimi` — ahead 41. §0.1 казва „нищо ново не се отваря, докато текущият не е пушнат“. Никаква геометрия публично. Никакви кадастрални идентификатори. Един лот в движение. Агентите не пушат.
 106: 
 107: **Докосванията на Петър** (план v2 §3 брои единайсет) стават **тринайсет**: + комитът на `granitsi_decisions_<дата>.json`, + комитът на сглобената геометрия. Списъкът се преброява наново в Г0-б.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md' -Encoding UTF8 -TotalCount 150 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # Амандамент №1 към ПЛАН „Границите“ v2 (05.09.2026, 21:25) — след оборването на v2 от Кими (К8–К14) и Astra (S7–S13) и след атаката на идеята „микрорайонът = блоковете си“ (Кими Б1–Б6, Astra B1–B6). Статус: **за Gate 1 — едно четиво за Петър**
   2: 
   3: Нов датиран файл по §0.2 на ПЛАН „ИЗЧИСТВАНЕ“ v2. Не редактира плана v2 и ADR 010; казва какво се променя в тях и защо. Присъдите дословно: `scratch/places_search/granitsi_v2_kimi_K8-K14_05.09.md`, `granitsi_v2_astra_S7-S13_05.09.md`, `granitsi_blocks_kimi_B1-B6_05.09.md`, `granitsi_blocks_astra_B1-B6_05.09.md`. Мерките от вечерта: `agkk_inspire_measure_05.09.md`, `ОТЧЕТ_Ф0б_05.09.md`, §4 тук.
   4: 
   5: **Думите на Петър тази вечер:** „искам да имаме ясно обособени граници на кварталите… искам да можем да ги намираме в търсачката“; „Възраждане 1, 2, 3 ти го дадох като пример“; „станаха много идеи, а нито една не работи както ми се иска“; „не искам регресии, а само подобрения“.
   6: 
   7: ## 1 · Присъдата в едно изречение
   8: **Всички пътища без твоята ръка са изчерпани и измерени: официални граници има само за петте района и шест квартала (АГКК); за комплексите и центъра никой извор не носи граница, КАИС блоковете и съседните адреси са подложка и проверка, не граница; затова границите ги чертаеш ти, върху карта с всички данни под писалката, автоматично идват шестте на АГКК, а търсенето се поправя с нормализатора и йерархията.** Това е планът v2 (Г1 инструмент → Г2 твоята вечер), потвърден от двамата одитори след като обориха всяка алтернатива. Разликата спрямо сутринта: вечерта ти е с подложка от данни (блокове с номера, адреси на съседните сгради, официалните полигони и точки на АГКК, OSM възлите, редовете на пощите), затова методът е „по сгради/по улици“, не „по памет“.
   9: 
  10: Кими за (i) комплексите предпочете „таблица блокове + обвивка“, Astra — „Петър чертае, блоковете проверяват“. Приемам **Astra**, защото Astra измери, а Кими предположи: блоковите номера се повтарят между комплексите (2, 3, 4, 6, 56 са и във Възраждане, и в Младост), „№ 83“ стои върху 211 отпечатъка, а само 11 от 375 места са на ≤ 60 m от блок с номер. Обвивка от такива блокове би била измислена територия. Блоковете остават като **слой-проверка**: всеки подписан полигон трябва да съдържа блоковете, които таблицата (ако Петър я подпише) му приписва, и нито един чужд.
  11: 
  12: ## 2 · Какво се приема от атаките и какво се променя (по номера)
  13: Всички присъди са приети; където Кими и Astra се разминават, печели по-строгата.
  14: 
  15: **Кими К8–К14 (v2):**
  16: - **К8 → ADR D0, G22.** До записани условия за повторна употреба официалният полигон на АГКК е САМО сравнителен свидетел в леджера (12-те печалби са кандидати, не се пишат). G22 приема `_meta.agkk_terms.terms ∈ {"published:<url>", "none_published_open_by_default"}` с дословен текст и дата; празен низ = червено. След отключване атрибуцията „АГКК INSPIRE GN 10-2019-v0“ е ред в картончето. Правната опора (Кими провери): ЗДПД чл. 11, ал. 1, т. 6–7 (условията са задължителен елемент на метаданните — АГКК не ги е публикувала), чл. 15, чл. 17; ЗДОИ чл. 3а, ал. 2, чл. 6, ал. 2, т. 5, чл. 15, ал. 4, чл. 41а. Без писма: записваме презумпцията с атрибуция.
  17: - **К9 → D0.** Обектът с двойно име („Чайка“ = „Св. Св. Константин И Елена“) се изяснява по `localid` ПРЕДИ Г2; влиза с двата `localid` в `witnesses[]` и дословен `note`; `deferred` с този довод е валиден отговор.
  18: - **К10 → D0 степен (3).** Всяка присъда от пощенския указател носи `source_snapshot: "2018-05-17"`; **не пише** в картата без по-нов свидетел за същата улица (REG адрес) — остава кандидат/свидетел №2. Празно квартално поле = мълчание.
  19: - **К11 → D0/D6.** Разминаване написан извор ↔ пощи (Св. Марина) не се решава по ранг: `disputed`, леджер-само, с двата извора дословно и „следваща проверка“ (за Св. Марина: правилото в §3а).
  20: - **К12 → D1/D3, отчет Ф0-б §6 т. 2.** „Зона 9000“ в картончето ОТПАДА; пощенският код е само леджер. Декларираната граница носи дословен етикет: „граница, очертана от Петър (дата), по местно знание/по сгради; официален извор няма (проверено 05.09.2026: АГКК, пощи, община)“.
  21: - **К13 → D5.** Свидетелят за ново име трябва да назовава ТОЧНО името; именни различия („Левски“ ↔ „Васил Левски“) се връзват само през подписан crosswalk/`aliases`; йерархия за втори свидетел: АГКК точка > пощенски ред ≥ общинска публикация > OSM възел.
  22: - **К14 → D10, Ф0-б.** `source_snapshot` за всяка външна присъда; при нова версия на АГКК/указателя съответствието се премерва; именният crosswalk обхваща и АГКК имената.
  23: 
  24: **Astra S7–S13 (v2):**
  25: - **S7 → G11 (регресиите).** Матрицата на пътищата към влошаване влиза в G11 като задължителни фикстури: (а) написан квартал изчезва/сменя код/уточнява се → G17; (б) полигон пише при спор/ръб/грешен вид → G1/G8 върху реалния resolver; (в) сгрешени начални `lat/lon` в същия район → нова проверка в G9 (координатата се сверява с тялото, не само с полето); (г) променени `name/src/locality/zone` при запазен код → G17 сравнява ЦЕЛИЯ публичен ред, не само кода; (д) нов квартал маха ред от търсене по район → всички 140 замразени заявки + новите се сравняват по подредени идентичности; **загуба на валиден резултат = STOP, поправка на стар грешен резултат само с конкретно доказателство**; (е) нов квартален токен блокира немаркирана улица в A3-street → фикстура улица-сблъсък; (ж) стар/нов клиент × стари/нови/смесени данни при студен/топъл кеш → изрична матрица, четирите комбинации се пускат преди пуша.
  26: - **S8 → D0/D6.** Без нов ранг над KAIS/REG за официалния полигон; двата полигонни извора са една адюдикация ранг 3; схемите `source/method` в D1/D2 се допълват с `agkk_inspire_gn/official_polygon`. Фикстура: 3 ОУ „Ангел Кънчев“ — пощите казват `kv_levski`, заглавното обещание казва „Цветен квартал“; **противоречиво приемно обещание блокира подписа до изрично решение на Петър** (§6 т. 1).
  27: - **S9 → Ф0-б/G24 (съединяването).** Присвояване по указателя само при: пиннат ред/страница, подписан crosswalk, **съвпадащ вид на улицата (ул./бул./пл.)**, точно нормализирана улица или индивидуално подписан fuzzy alias, еднозначен пълен `house_key` (с буквата) в диапазона/списъка/четността; „всички“ важи само когато е записано; приложими редове с различни кодове = без присвояване; бройките се затварят по идентичност (таблицата в отчета §2 се преизчислява: 153 адресирани срещу 28 + 105 + 40 = 173 — смесени общи и подгрупови бройки, поправя се). Фикстури: неподписан fuzzy при 0,86; неизвестна четност; конфликт „всички“/диапазон; **ул. срещу бул. със същото име (Св. Марина)**.
  28: - **S10 → D12/G11.** Пробата се пуска `--mode after` с назована кандидат-референция и с digest + среда на живия `before.json`; ADDRESS сценариите байт-равни; старите A3-street заявки запазват подредените идентичности и клонове (`streetRows` отхвърля немаркирана улица при сблъсък със `zkset`, който новите квартали разширяват — фикстура). Дословно от Astra: този лот **не** добавя липсващи адреси, не подобрява разпознаването на улица/номер и правописа, не пипа интерфейса за адресно търсене — това е отделен лот след Границите, ако Петър го поиска.
  29: - **S11 → редът.** „Ред“ (Фаза E) НЕ се вмъква преди Границите: противоречи на §6.1 (Границите преди B–E) и мести файлове, които Г0-б пипа. Остава паркиран до след пуша на Границите (черновата и оборването ѝ са записани: `scratch/places_search/ЧЕРНОВА_ПЛАН_Ред_05.09.md`, `ОБОРВАНЕ_ПЛАН_Ред_05.09.md`). A.2-11 е изпълнен (`38e9dd9`, одит ГОДНО, 310 теста, 7/7); архивирането на опашка A е спряно честно — виж §6 т. 5.
  30: - **S12 → D19/G20.** Преди F13-а изпълнителят записва точните unittest ID-та и очакваните падащи assertions от изолиран кандидат (сигурно: `test_places_search_gate.Lot1GateTest.test_a_phrase_is_the_canonical_zone_or_an_accepted_p7_form`; условни: `Lot1vAGateTest.test_gate`, `Lot1GateTest.test_the_zone_phrase_override_is_load_bearing`, `FrozenDiffTest.test_the_live_engine_replays_the_artefact`, `Lot1vABucketTest`/`Lot1vBBucketTest.test_the_live_engine_replays_the_new_bucket`); без wildcard. Докосвания 1+2, 2+3 и 8–10 могат да делят сесия; G19 не иска човек.
  31: - **S13 → write-set-овете.** F13-в изброява expectations/паритетния корпус; `qa_district_official.py` (G23) получава стъпка P8-б′; G11 командата носи `--mode`; §7 включва всички гейтове.
  32: 
  33: **Идеята „блокове“ (Кими Б1–Б6, Astra B1–B6):**
  34: - **Б1/B1.** Готов официален списък „блок → микрорайон“ няма; общински документи назовават „2-ри микрорайон“ по улици, ЦИК дава адрес → секция (никога не се преобразува в микрорайон). Блоковите номера не са ключове (повторения между комплексите). → Таблицата, ако Петър я поиска, е **слой-проверка** за неговите полигони, не извор на граница; всеки ред с документ или с подпис.
  35: - **Б2/B2.** Обвивка от блокове = измислена територия; КАИС-производна геометрия е под G21 (ФАЗА_0). → Не се публикува hull; блоковите очертания се показват в инструмента като подложка.
  36: - **Б3/B3.** Училищата и градините стоят МЕЖДУ блоковете — точно те са целта. → Границата е на Петър; „precision_m ≥ 50“ и ръбът по D7 остават.
  37: - **Б4/B4.** Съседството по КАИС адреси: Кими го прие като пишещ канал с прагове, Astra го обори като автоматичен (числата 181/3/17 не са независимо възпроизведени; знаменателят крие неизвестните). → Приемам по-строгото: канал `NEIGHBOUR-KAIS` дава само `CANDIDATE` в леджера и слой в инструмента; пише само след подписани параметри и независима проверка — **отложено извън този лот**.
  38: - **Б5/B5.** Търсенето: нормализаторът ПАЗИ числата, `parents` за Възраждане 1–4 влизат в регистъра (Р-0), детето избира само себе си, родителят — себе си плюс регистрираните деца, без съименници и без районни резултати; проверяват се идентичности („възраждане 3“, „възраждане“, „училище младост 2“ → ПГИ „Д-р Иван Богоров“).
  39: - **Б6/B6.** Обхват: списъкът от 32 не включва Цветен квартал и Вл. Варненчик I–V м.р.; с тях са **38** — решение на Петър (§6 т. 1). „Готово“ = подписаният обхват съвпада с публично показаните И търсимите квартали; частна геометрия, `deferred` и неподписан hull не изпълняват целта — влиза в §7 на плана.
  40: 
  41: ## 3 · Нови правила от вечерта (доказани с мярка)
  42: - **3а · Регистров сегмент само от адреса на пина** (Св. Марина). ИАМН регистърът носи четирите адреса на болницата, разделени с „;“; единственият типов сегмент е на филиала в к.к. Св. Св. Константин и Елена, и той стана квартал на главната сграда. Правило за `_resolve_one`: сегмент от канал REG-manifest важи само ако е в СЪЩИЯ адрес („;“-част), чиято улица съвпада с КАИС адреса на тялото, или ако регистърът има един адрес. Измерено: 39 реда с квартал от този канал; 1 с няколко адреса (Св. Марина) → пада до „район Приморски“; в целия регистров манифест 6 от 186 реда имат няколко адреса. Фикстура: адрес с „;“ и типов сегмент в друг филиал → полето остава празно. Влиза в P8-а.
  43: - **3б · Видът на улицата участва във всяко адресно съединяване** (ул. „Христо Смирненски“ ≠ бул. „Христо Смирненски“). Влиза в Ф0-б правилото (S9) и в бъдещия нормализатор на адреси.
  44: - **3в · Света Марина днес.** До P8 на живата карта стои курортният етикет. Пътят е като при Адмирал: подписан факт по идентификатор (квартал „няма“ → район Приморски, или кодът, който Петър каже: Сотира е OSM възел на 564 m, не официален; Изгрев е най-близката АГКК точка на 738 m). Решение §6 т. 3.
  45: 
  46: ## 4 · Мерките от вечерта (влизат в §0 на плана като М0.24–М0.28)
  47: - **М0.24** КАИС сгради 80 497; собствен квартален код от КАИС текста при 19 000; двусмислени 1 824; без 59 673. По код: Виница 2 217 · Манастирски рид 1 896 · Изгрев 1 757 · Бриз 1 743 · Галата 1 512 · … · Владиславово 678 · Възраждане 647 · Младост 114 · Чайка кв. 179 · Трошево 72 · Победа 56 · **Възраждане 1/2/3/4: 1/1/0/8 · Младост 1/2: 5/0 · Левски 0**. Команда: `src/fire_varna_locations.py` `TypedRegistry.resolve` върху `dict.quar` (allow_untyped) и типовите сегменти на `dict.addr` от `web/varna_buildings_info.json`.
  48: - **М0.25** Блокови номера в КАИС адреса: Възраждане 225 (Astra: 228 отпечатъка / 86 различни ключа), Владислав Варненчик 625 (199 / 58 без булеварда), Младост 294 / 66, Чайка 79 / 77, Трошево 25, Победа 18, Изгрев 7, Бриз 7, Левски 0; места на ≤ 60 m от такъв блок: 11 от 375.
  49: - **М0.26** Съседство по КАИС адреси (≥ 8 сгради, ≥ 80 %, 250 m, центроиди в EPSG:32635): срещу 201 написани — 181 съгласие, 3 разминавания (Хоспис Филаретова borovets_yug↔galata; ДЯ №11 „Иглика“ troshevo↔mladost; РИВИЕРА БИЙЧ zlatni↔chaika_kk), 17 без консенсус; за 174 празни — 40 кандидати, 134 без; Astra: числата не са независимо възпроизведени → само кандидати.
  50: - **М0.27** Ф0-б (отчетът): 1 064 реда за Варна; +28 назовани (kv_levski 13); 105 само код; 40 неразпознати улици; 6 спора, от които 1 = грешка на канала (3а) и 1 = грешка на съединяването (3б).
  51: - **М0.28** Регистров манифест: 186 реда, 6 с няколко адреса („;“), 2 от тях поставени; 39 места с квартал от REG-manifest.
  52: 
  53: ## 5 · Какво се променя в реда на плана v2 §2
  54: 1. **A.2-11 ✓** (`38e9dd9`, одит ГОДНО с 3 minor-а за Gate 2: тестовият файл извън write-set-а, промененото съобщение, архивът отложен).
  55: 2. **Г0-б** чака: оборването е налице (този амандамент), остават думата на Петър и отговорите в §6.
  56: 3. **Г1 · инструментът** получава задължителни слоеве-подложка: КАИС блокове с номера (етикет на блока), адресите на съседните сгради (цвят по квартален код), официалните полигони и точки на АГКК, OSM възлите, пощенските редове по улица; всяка подложка с извор и дата в панела, за да стане `method: "по сгради"/"по улици"` честен. Часове: 10–14 вместо 8–10.
  57: 4. **Ф0-б ✓ измерено**; канал `POST-2018` в P8 **не** влиза сега (К10, S9): указателят е свидетел №2 и борд.
  58: 5. **Р · регистърът:** + `parents` за Възраждане 1–4; + `tsveten_kvartal` и Вл. Варненчик I–V само ако обхватът стане 38 (§6 т. 1).
  59: 6. **Г2 · вечерта:** 26 полигона при обхват 32 (32 при 38), шестте на АГКК се одобряват; блоковата таблица е по желание, като проверка.
  60: 7. **P8:** + правило 3а; + `NEIGHBOUR-KAIS` като кандидат-колона; + `qa_district_official.py` (G23) като стъпка.
  61: 8. **F13:** + S7 матрицата в G11; + S12 списъкът; + write-set-овете от S13; + 3б в нормализатора на адреси.
  62: 9. **„Ред“** остава паркиран до след пуша (S11).
  63: 
  64: ## 6 · Решенията за Петър (пет; препоръка към всяко)
  65: 1. **Обхватът:** 32 квартала на регистъра, или **38** с Цветен квартал и Владислав Варненчик I–V м.р.? Препоръка: **38** — Цветен квартал е заглавното обещание, а без микрорайоните „Вл. Варненчик“ е един полигон от 2,3 km² (АГКК) и хората не го търсят така. Ако „Цветен квартал“ остане вън, заглавното обещание се сменя на „училище левски → 3 ОУ Ангел Кънчев“ (пощите го поставят там).
  66: 2. **Чертаеш ли ти границите на комплексите и центъра, с подложката от данни?** Това е единственият път, който двамата одитори оставиха. Препоръка: **да**; Г1 тръгва веднага след думата ти (10–14 изпълнителски часа), вечерта ти е след него.
  67: 3. **Света Марина:** подписан факт сега (квартал „няма“ → район Приморски, или код по твое знание), или изчакваш правилото 3а в P8 да я поправи с класа ѝ? Препоръка: **изчакай P8** (същата доставка), освен ако не искаш живата карта поправена по-рано — тогава ред в опашката.
  68: 4. **Трите обявени отклонения от приетите атаки** (К2 `disputed` леджер-само; К5 `SIGNED_POLYGON_BORDER` не се публикува; К6 уточнителят отложен) — като блок. Препоръка: **да**.
  69: 5. **Архивът на опашка A (амандамент №12 към ИЗЧИСТВАНЕ v2):** (А) регистърът на опашките включва `docs/archive/queues/`, но само една АКТИВНА в `scratch/places_search`; или (Б) замразена доставка без делти има право на 0 опашки. Препоръка: **(А)** — правилото „една опашка в HEAD“ остава буквално вярно, архивът е видим за гейта и никога не се брои като активен.
  70: 
  71: ## 7 · Часове (изпълнителски, след думата)
  72: Г1 10–14 · одит 1,5 · Р-0 1,5 + Кими/Astra · Г2 = вечерта на Петър · P8 9–11 · F13 9–11 · одити 3 · подпис → пуш 1 · Г3 0,5. **Общо ~40 изпълнителски часа + вечерта.** Astra оценява цялото на 56–80 човекочаса с участието на Петър — приемам числото като честно.
  73: 
  74: ## 8 · Какво НЕ се променя
  75: Нищо на живата карта преди подписаната опашка Г, единственото `--freeze` и пуша на Петър; никаква геометрия публично; никакво трето семейство одитор (само Astra и Кими); никакъв Sol.

codex
Открих несъответствие в правилото за точност: примерът „rms 11 при `precision_m` 50“ покрива обявения минимум `3×rms`, затова сам по себе си не може да бъде падаща фикстура. Проверявам също връзката между решенията, подписа и сглобената геометрия; отделни агенти проверяват покритието и възпроизводимостта.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=60; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 | Select-Object -Skip 60 -First 47 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 14ms:
  63: **Г2-а · СГЛОБЯВАНЕ (varna_3d) — новият, дотук неназован ход.** Решенията са JSON във Fire_Varna, геометрията — във varna_3d; `SIGNABLE` (`gates/release.py:175-183`) е затворена шесторка с местни пътища, тоест решенията **не могат** да са подписан артефакт. Затова: `_meta.decisions_sha256` в geojson-а И в `expectations._meta`, плюс гейт „всеки Feature има ред в решенията и обратно“ (отрицателна фикстура: Feature без решение). Всеки от Г1-а, Г1-б, Г2-а получава **репо, изпълнител, изчерпателен write-set, дословно съобщение**.
  64: 
  65: **Г2-б · сесия по потвърждаване.** По квартал: официален / реконструиран / уикимапийски / никакъв. Провенансът на D1 се допълва с `geometry_origin` · `imported_from` · `fetched_at` · `chosen_source` · `chosen_reason` · `confirmed_by` · `confirmed_at`; **`drawn_by` / `drawn_at` / `viewport` / `screenshot_sha256` са `null` при внесена геометрия** (гейт за взаимна изключителност: или ръка, или внос, никога и двете). Това е промяна в D1: черновата запазваше `screenshot_sha256` задължителен, докато маха единствения му производител (условния `preserveDrawingBuffer`), а Leaflet няма нито канва без нова зависимост, нито `bearing`/`pitch` — първият Feature би паднал на G1-фикстурата „липсващо задължително property“. Влиза в §7 т. 2.
  66: 
  67: **Предгейтовете остават дословно:** **G19** (частно репо — М0.15 и до днес НЕ Е ИЗМЕРЕНО) и **G21** (ФАЗА_0) важат за всяко приземяване в `varna_3d/data`.
  68: 
  69: **DWG** — 15 ПУП чертежа R14 на Drive-а на АГУП; три пътя: **QGIS** (вграден libdxfrw, R14; нова инсталация), **LibreDWG** (GPLv3, `dwg2dxf`), **ODA File Converter** (собственически). Решение §7 т. 5.
  70: 
  71: ## 5 · Гейтове
  72: 
  73: - **G25-а · пинът (офлайн, детерминистичен).** `wm_polygon_sha256` се преизчислява от **проследената** геометрия. Фикстура: подменен връх при непроменен sha. **G25-б** е ръчна датирана МЯРКА (не гейт), с път за преподписване (нов `fetched` + довод) — Уикимапия няма поле за версия, а мрежов гейт при демо ключ през сателит е недетерминистичен.
  74: - **G26 · пълнота.** Всеки жилищен код от **подписания регистър** има решение. Преобразува `official` и `wikimapia` в `polygon` — D4 `:44` познава **три** множества (`polygon` / `no_boundary` / `deferred`); разликата живее в колоната `source`. Липсващо решение = ЧЕРВЕНО, поименно.
  75: - **G27 · атрибуцията.** Черновата беше неизпълнима: публикуваният ред няма как да каже, че идва от Уикимапия (`src = SIGNED_POLYGON` по D0), а `_meta` на доставката е **затворен 9-ключов набор** (`qa_fire_varna_places_export.py:62`, налаган на `:550`). Затова G27 се пише като **билд-гейт във varna_3d върху `quarters_signed.geojson`** и сверява **точния низ** от §3. Ако Петър иска реда в публичното приложение, това е нов български UI низ → отделно негово одобрение + `licence_quarter_boundary` в `META_KEYS`, в пиновете на D13 и в двата преписа, в СЪЩИЯ комит.
  76: - **G28 · fail-closed за неприсъдения лиценз.** Feature със `source: "wikimapia"` и празен `_meta.source_terms["wikimapia"].verdict` = ЧЕРВЕНО; износът на редове с уикимапийски квартал е блокиран. Без този гейт „да, условно“ е дума без механизъм (§0.4 „червено = блокирано“).
  77: - **G22 се разширява по механизъм** на `_meta.source_terms[<source>]`, но **изброяването на К8 се запазва дословно** за всеки извор (`terms ∈ {"published:<url>", "none_published_open_by_default"}`); само „празен низ = червено“ би разхлабило приета присъда.
  78: - **G18** не се маха мълчаливо — той е единственото машинно налагане на „никога Esri“. Става статична проверка „в борда няма код, който пише връх“ (пада на нарочно вкаран чертожен код) → решение §7 т. 3.
  79: - **Непроменени:** G1, G17, G19, G21, G23, G24.
  80: 
  81: ## 6 · Мерките ПРЕДИ борда
  82: 
  83: - **М2-1 · покритие, измерено, не цитирано.** Твърдението „20+ от 25 квартала имат полигон“ е на Кими и е **опровергано от собствена мярка**. Върху незамразения файл (90 обекта): по нормализирано име срещу 29-те кода кв+жк съвпадат **15**, но с дефекти: `mladost` → два „Район Младост“ (13,2 и 12,3 km² — район, не жк), `izgrev_kv` → с.о., `briz` → само „Бриз - юг“ 0,19 km², `chaika_kv` ↔ двусмислената „Комплекс Чайка“. **Без полигон са 14 кода**, сред тях точно тези без официален извор: `tsentar`, `maksuda`, `kolhozen_pazar`, `kv_levski`, `troshevo`, `hristo_botev`, `rozova_dolina`, `trakia`, `sv_ivan_rilski`, `mladost1`, `mladost2`. Мярката се повтаря върху замразения файл и се цитира с неговия sha **преди** решенията.
  84: - **М2-2 · припокриване** (IoU, разлика в площ, симетрична разлика) срещу АГКК повърхнините. **Честно днес: сравними двойки са само Аспарухово/Галата/Чайка; с Одесос МР — нула, докато crosswalk-ът не е подписан.** `shapely` 2.1.2 + `pyproj` 3.6.1 (D7) — нула нови зависимости.
  85: - **М2-3 · местата вътре — днес НЕИЗПЪЛНИМА, обявено.** Популацията е **159**, не 174 (D6 `:48`), с поименен списък на изключените. Координатите трябва да дойдат от пиннатия вход по D10 (`lat`/`lon` в `place_identity.json` — мерено: 375 обекта, **0** с координата), а `places_375_hybrid.geojson` е негоден: `_meta` е празен, папката е игнорирана, координатите му съвпадат с изнесените (D7 `:50` забранява четенето им), а properties носят етикети от **отхвърления** хибрид (`derived: "osm:цветен_квартал"`). Мярката чака P8-а.
  86: 
  87: **Обхватът 38 задължава** преизмерване на уникалността по D12 върху ИЗНЕСЕНИЯ речник + фикстура за сблъсък с немаркирана улица (S7 е).
  88: 
  89: ## 7 · Решенията за Петър (четири отворени + едно взето)
  90: 
  91: 1. **Тръгваме ли по уикимапийския път?** — **ВЗЕТО от Петър** („прегледах районите от уикимапиа… нека ползваме тях“, 06.09 ~00:50). Остава процедурата: бордът започва с извадката от **5–6 полигона** с измерени дефекти (двата „Район Младост“, „Комплекс Чайка“, Кайсиева, Аспарухово, Бриз), преди останалите.
  92: 2. **Стълбата v3 и D1** (§2, §4) — чужда геометрия с провенанс вместо ръка; `drawn_*` и `screenshot_sha256` стават `null` при внос. Препоръка: **да**.
  93: 3. **G18** — превръща се в статична проверка „борд без чертожен код“ вместо да отпадне. Препоръка: **да**.
  94: 4. **Лицензът на файла** — на ниво Feature (`_meta.licences[]`) вместо „най-строгият участник“; това променя D2 и §6а т. 3. Препоръка: **да** — иначе АГКК полигонът е нерелицензируем. Уикимапийският клон остава **блокиран от G28** до присъдата на Кими.
  95: 5. **Обхватът 32 или 38 и заглавното обещание.** Честно: при новата стълба **Център, Максуда, Колхозен пазар, Левски, Цветен квартал** нямат нито официален, нито човешки полигон — отиват в `no_boundary`/`deferred`, а проверката „училище цветен квартал“ след пуша става **НЕПРИЛОЖИМА** (план v2 §6 т. 4 я обявява за провал на целта). Препоръка: **38**, с изричен запис, че обещанието пада — или **32** и лотът се преформулира.
  96: 
  97: **(Отложено, не решение сега.)** DWG-инструмент: препоръка **не сега**; отваря се само ако след борда останат комплекси без приемлива граница, и тогава по реда QGIS → LibreDWG → ODA.
  98: 
  99: ## 8 · Оборване (чака)
 100: 
 101: **Кими — лицензна леща:** двата въпроса от §3 (sui generis при 3.0 Unported + чл. 7(5) на Дир. 96/9; ToS/демо ключ), плюс ЗДПД/ЗДОИ за общинския слой и районните карти. **Astra — механична леща:** борд без чертане, форматът на решенията, честността на геореференцията (rms, контролни точки, МР ↔ име), регресиите по S7, G25-а/G26/G27/G28. Само Astra и Кими; никакъв Sol.
 102: 
 103: ## 9 · Какво НЕ се променя и кога тръгва
 104: 
 105: Нищо от §4 не тръгва преди Gate 1 **и** Г0-б **и** пуша. Измерено сега: Fire_Varna `main` е **ahead 12, behind 1** спрямо origin (локалното не е дори наравно с публикуваното), varna_3d `rezhimi` — ahead 41. §0.1 казва „нищо ново не се отваря, докато текущият не е пушнат“. Никаква геометрия публично. Никакви кадастрални идентификатори. Един лот в движение. Агентите не пушат.
 106: 
 107: **Докосванията на Петър** (план v2 §3 брои единайсет) стават **тринайсет**: + комитът на `granitsi_decisions_<дата>.json`, + комитът на сглобената геометрия. Списъкът се преброява наново в Г0-б.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 -TotalCount 73 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # ADR 010 · Граници, подписани от човек
   2: 
   3: **Статус:** Proposed (05.09.2026) — **чернова: необорена, неподписана.** Става `Accepted` в комита Г0-б на плана, СЛЕД оборването от Кими и Astra и СЛЕД Gate 1; до него този файл не пипа `docs/plans/PARKED.md` и `docs/activeContext.md`. Лотът се открива само по изричната дума на Петър, цитирана дословно в комита Г0-б.
   4: 
   5: **Предусловия — всяко проверимо, нито едно обещано:**
   6: 
   7: 1. Доставка A е пушната (`fd13907`, 05.09 16:55) **и четирите публикувани хеша са сверени с локалните** — `docs/activeContext.md:3`: hotels `46a44ce82f15`, places `329310f577e8`, categories `874e33cd00e2`, **index.html `3d3bf79b58bf`**. Това е условието на S5, не само пушът.
   8: 2. **A.2-11 е изпълнен и одитиран като ЗАТВАРЯЩА стъпка на Фаза A**, под собствения си подписан план (`ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` + амандаменти №10/№11), преди този лот да се обяви. A.2-11 не се комитва по този ADR и не чака него.
   9: 3. **P1 е отпушен от Петър** (`PARKED.md:9`). Този ADR + ПЛАН v2 СА датираният план по `PARKED.md` „Как се вади ред оттук“ т. 3; §8 на плана е неговото оборване; редът се маха в Г0-б.
  10: 4. **ФАЗА_0 е подписана или условие 4 е потвърдено изрично.** `varna_3d/docs/decisions/ФАЗА_0_лицензи.md:4` = „⏳ чака подпис · нищо не се строи преди подпис“ (мерено). Докато този ред стои така, `_meta.faza0_signed` **не може** да е `true` — това е гейт G21, не самообявено поле — и G1 отказва И „по сгради“, И „по улици“.
  11: 5. **Видимостта на `github.com/Petar1984/varna_3d` — НЕ Е ИЗМЕРЕНО** (М0.15, иска мрежа). Гейт **G19** я мери преди Г2; публично репо събаря D3 и отваря решение §6.3.
  12: 6. **Редът на Фаза B–E спрямо „Границите“ е обявен от Петър** (решение §6.2).
  13: 7. **Непушнатото е преброено:** varna_3d 41 ahead, Varna_buildings **1 ahead**, Fire_Varna 1 ahead (М0.16) — лотът ги изпраща заедно (§3 т. 7–9).
  14: 8. **Официалните извори са проверени преди чертането** (05.09, 16:40–17:50; по думите на Петър „намери административните граници на кварталите… не съм сигурен, че тези квартали, които имаме, отговарят точно“): Astra, трети опит (`scratch/places_search/granitsi_astra_official_boundaries_05.09.md`) и пряка проверка на АГКК INSPIRE оттук (`scratch/places_search/agkk_inspire_measure_05.09.md`). Резултатът е **D0** (стълбата на изворите), **Ф0-б** в плана (пощенският указател като кандидат-свидетел), гейтове **G22–G24** и по-малка вечер за Петър.
  15: 
  16: Допълва ADR 008 D9 и ADR 006; не пипа ADR 007; не изпреварва ADR 009 (Фаза B). D3, D6–D11, D14 и D19 важат за `varna_3d` и `Varna_buildings`: канонът е този файл, а `varna_3d/docs/decisions/README.md` получава указателен ред в комита на **своя** изпълнител (правило 6).
  17: 
  18: ## Контекст
  19: 
  20: **Думите на Петър (05.09):** „не виждам училища в Цветния квартал, а знам, че там има… училището в Св. Св. Константин и Елена не излиза, като напиша «училище св св константин и елена»… искам да имаме ясните граници на кварталите и всичко, което е в тези квартали, да излиза в търсачката… искам да изследваме целия клас такива грешки и да ги изчистваме по траен и фундаментален начин.“
  21: 
  22: **Всяко число тук има команда в §0 на плана.**
  23: 
  24: **Клас A · няма граници.** 174 от 375 реда без квартал; **159 без нито един канален id**, 8 `pending_signature`, 7 само с `locality` (М0.2). 14 от 32-та жилищни кода носят нула реда (М0.3). „Цветен квартал“ не е в регистъра; около `node/9664925200` стоят **15** места на ≤ 900 m (не 14, както казва v1 §1), най-близкото 3 ОУ „Ангел Кънчев“ на **132,6 m**, всички с `quarter = null` (М0.11).
  25: 
  26: **Клас B · търсенето не намира и това, което ИМА квартал.** Индексът гради фразите през `significant_tokens` (`scratch/places_search/recall_sweep.py:424-442`, `:515-533`), заявката слепва суровия остатък (`:1120`). `училище св св константин и елена` → M2, 12 чужди реда; същата **без** „и“ → A3-location, 1 ред = Френското училище (М0.8). Две поправки на v1: **сблъсъчните токени са 11, не 7** (+`1`,`2`,`i`,`s`, защото `Rec._loc_tokens:664-679` чете суровите токени) и **типовият префикс е поредица токени с две арности** (`к.к.`→`[k,k]` срещу `кк`→`[k]`; `ж.к.`→`[zh,k]` срещу `жк`→`[zhk]`; `с.о.`→`[s,o]`; `м-т`→`[m,t]`; `кв.`→`[kv]`) (М0.6).
  27: 
  28: **Клас C · живата карта** беше стара; затворен с публикацията на A.
  29: 
  30: **Никой отворен извор не носи жилищните граници.** OSM: **13 полигона `place=suburb|neighbourhood|quarter`, всички вилни зони и местности, нито един жилищен квартал**; източник `scratch/places_search/osm_quarters_measure_05.09.md:7`, Overpass снапшот `2026-09-04T21:46Z`, bbox 43.13–43.33 / 27.80–28.10 — **днес НЕПРОСЛЕДЕН, влиза в git с Г0-а (М0.17)**; до този комит присъдата няма проследим извор и не се цитира извън него. Само 27 от 32-та кода имат дори възел; трите курорта нямат — 131 от 201 типизирани реда без OSM свидетел (М0.11). Машинният път е пенсиониран: `m6000_private/number_viewer/quarters_drawn_v1.geojson` — **126 обвивки** (М0.18), **IoU 0,13** срещу праг 0,70 (`docs/plans/ПЛАН_ЛОТ_Границите.md:25`). За центъра остава един извор — назован човек. **За петте района и за шест квартала обаче има официален полигон** (по-долу).
  31: 
  32: **Официалните извори, проверени 05.09 (Astra трети опит + АГКК INSPIRE пряко; М0.19–М0.23).** Присъдата на Astra по 10 извора: *„Не установих проверен публичен набор с пълни официални граници на именуваните жилищни квартали във Варна.“* Граници носят ДРУГИ единици: петте района (ЗТДСОГГ 1995, чл. 4, по улици), полицейските микрорайони на МВР, устройствените зони на ОУП, проектното каре „17-ти микрорайон“ в Левски, ПУП-ПРЗ на ж.к. Чайка (публикуван, контурът неинспектиран). Само присвояване адрес → квартал дават: пощенският указател на „Български пощи“ (копие при КРС, PDF 17.05.2018, 11 344 012 B: жилищен район · улица · номера от/до; напр. ул. „Нарцис“ → ж.к. „Васил Левски“), изборният класификатор 29.10.2023, блоковете на МВР, общински публикации, адресната номенклатура на ГРАО (набор с означение CC0; улица/ж.к./квартал са АЛТЕРНАТИВНИ единици). **АГКК INSPIRE (`inspire.cadastre.bg/arcgis/rest/services`, снимка `10-2019-v0`), проверено оттук:** `Administrative_Unit` 5-ти ред = петте района (кодове `10135-01…05`) — **375 от 375 места в правилния район, 0 разминавания** с нашия `district.code`; `Geo_Names` Surface = официални полигони за **Владиславово, Виница, Галата, Аспарухово, Златни пясъци, Чайка** (последният носи и второ име „Св. Св. Константин И Елена“ върху СЪЩАТА геометрия, 3,07 km², и лежи между курортите: нашите 34 от 35 хотела с `kk_konstantin_elena` са извън всяка градска повърхнина на АГКК) — където и ние, и АГКК имаме квартал, съгласие **109 от 110**; единственият спор е ПАРК ХОТЕЛ БЕЛВЮ (REG Златни пясъци, вътре в „Чайка“); чисти печалби, ако полигонът е свидетел: **12 места** (Аспарухово 8, Владиславово 1, Виница 1, Златни 2), спорни 8 в „Чайка“ (4 от тях са висящите сблъсъци); центърът е ЕДИН полигон „Варна“ 19,53 km² със 134 от 174-те празни реда и без подквартали; `Geo_Names` Point = 722 официални ИМЕНА без граница, 53 от 84-те кода на регистъра имат такава точка (вкл. **Левски** и **Максуда**), 14 жилищни нямат, „Цветен квартал“ го няма и като точка. Условията за повторна употреба на INSPIRE услугата **не са установени** (Astra: „специален лиценз не установих“; страниците на КАИС и геопортала не носят лицензен ред — проверено 05.09 17:45) → G22.
  33: 
  34: ## Решения
  35: 
  36: **D0 · Стълбата на изворите за квартал (добавено 05.09, 17:50, след проверката на официалните извори).** Четири степени, от най-силната: **(1) официален полигон на АГКК** (INSPIRE `Geo_Names` Surface; днес 6 кода) — влиза като Feature в СЪЩИЯ файл `quarters_signed.geojson` със `source: "agkk_inspire_gn"`, `method: "official_polygon"`, `drawn_by: "АГКК INSPIRE GN 10-2019-v0"`, `localid` на АГКК в `witnesses[]`, `approved_by: Петър` (той одобрява включването, не рисува); **ЗАКЛЮЧЕН, докато `_meta.agkk_terms` не носи URL + дата на проверени условия за повторна употреба (G22)**; **(2) написан извор** REG / KAIS / НТР — както днес, рангове 0–2, непроменени; **(3) официално адресно присвояване** (пощенският указател 2018; номенклатурата на ГРАО) — КАНДИДАТ-канал `POST-2018` в ранг 2 до `KAIS-addr`, който влиза САМО след мярката Ф0-б на плана и с подписан от Петър crosswalk „жилищен район“ ↔ регистров код; преди отчета никакъв код за него; **(4) деклариран полигон** (`source: "declared_local_knowledge"`) — ранг 3, D6. Полигоните (1) и (4) минават през ЕДИН канал `SIGNED_POLYGON` с еднакви гейтове (G1) и еднакво правило „пише само в празен, безспорен, неръбов ред“; **`source` на Feature-а е колона в леджера и ред в картончето** („по официален полигон на АГКК“ / „по местно знание, Петър, дата“), не нов публикуван `src`. За ЕДИН код не може да има едновременно официален и деклариран полигон — кодът е в точно едно множество на D4 със своя `source`; Петър може да ЗАМЕНИ официалния с деклариран само с довод в `note` (напр. АГКК „Чайка“ с две имена). Спор официален полигон ↔ написан извор (днес 1: ПАРК ХОТЕЛ БЕЛВЮ) е `disputed` по D6 — никога автоматичен победител. **Районът получава контролен гейт (G23):** АГКК AU5 ↔ `district.code` = 375/375 днес; всяко бъдещо разминаване = STOP. Суровите отговори на АГКК (`scratch/places_search/agkk_inspire_2026-09-05/`) остават **непроследени** до G22 и никога не влизат в публичен файл.
  37: 
  38: **D1 · Класът на извора и ЗАДЪЛЖИТЕЛНИТЕ полета (К1 + S3).** Всеки Feature носи затворен подреден набор `properties`, чието ПРИСЪСТВИЕ се проверява преди коя да е стойност: `code` · `name` · `kind` · `parent` (или `null`) · `source: "declared_local_knowledge"` · `signed_by` · `drawn_by` · `approved_by` · `drawn_at` · `approved_at` (ISO `2026-09-05`, никога точкувани) · `method` · `basemap` · `precision_m` · `version` · `license` · `viewport {center, zoom, bearing, pitch, width, height}` · `visible_layers {id: stamp}` · `screenshot_sha256` · `approval_digest` · `witnesses[]` · `note`. Липсващо поле = STOP. Дайджестът: фиксиран подреден списък в `_meta.digest_fields`, координати като низ с 6 знака, външен пръстен обратно на часовника, ротиран към лексикографски най-малкия връх, каноничен JSON, `sha256("v1\n" + геометрия + "\n" + json)`.
  39: 
  40: **D2 · Лицензът се решава ТУК (К4).** Таблица `method` → лиценз, проверявана за СЪГЛАСИЕ: „по памет“ / „по огради“ → **CC0-1.0**; „по сгради“ → **КАИС „Отворени данни“, атрибуция АГКК, CC0 не се твърди — ЗАКЛЮЧЕН, докато `_meta.faza0_signed` не е `true`, а той не може да е `true`, докато `ФАЗА_0_лицензи.md:4` носи „чака подпис“ (G21)**; „по улици“ → **ЗАКЛЮЧЕН винаги** (нарушава условие 4, `ФАЗА_0_лицензи.md:25-26`), отключва се само с изричен подписан ключ. **Лицензът на ФАЙЛА е най-строгият участник.** Подложка: нашата PMTiles основа (ADR 002 D8) или КАИС; **никога Esri** — инструментът отказва връх, докато `map.getLayoutProperty("sat","visibility") === "visible"` (`varna_3d/web/index.html:880`), проверено от G18.
  41: 
  42: **D3 · Къде живее геометрията и как е вързана.** Каноничен файл: **`varna_3d/data/quarters_signed.geojson`**, версиониран в git. `m6000_private` НЕ е git репо; `Fire_Varna/data/` е публичната папка и отпада по S5; **това решение стои върху предусловие 5 и не е валидно, докато G19 не покаже частно репо.** Файлът се хваща от `varna_3d/.gitignore:4` и `:23` → иска `!data/quarters_signed.geojson` **след ред 23** (М0.9). **Публикува се само `quarter: {name, code, src}` и изведеният `zone`; геометрия никога.** К5 ↔ S5: следвам S5 за РЕДА и К5 за ВЕРСИЯТА — `polygon_version` и `polygon_sha256` са ЗАДЪЛЖИТЕЛНИ в `expectations.json._meta` и в `data/place_categories.json._meta`, **никога на ред** (редът е 13/17 ключа, `index.html:6275`, `:6281`; `_meta` на доставката е затворен 9-ключов набор, `qa_fire_varna_places_export.py:62`, налаган на `:550`). **Ограничение, мерено:** `SIGNABLE` (`gates/release.py:175-183`) е затворена шесторка с пътища спрямо Fire_Varna, а `blob_at` (`:223`) чете блоб от ТОВА репо — **чужд път е недостъпен, значи геометрията НЕ може да получи ред клас „артефакт“.** Дайджестът ѝ пътува през `expectations._meta.polygon_sha256` + ред клас „въпрос“ с видимо `тяло: <sha256>` + G4 и G7. Разширяването на `SIGNABLE`/`blob_at` към чуждо репо е **съзнателно отложено за Фаза C**.
  43: 
  44: **D4 · Регистър ↔ полигон: три декларирани множества.** Всеки жилищен код (kind ∈ {кв, жк, кк}, ЧЕТЕН ОТ РЕГИСТЪРА, никога от литерал) попада в точно едно от `polygon` · `no_boundary` (Feature с `geometry: null`, RFC 7946, с довод и подпис) · `deferred` (`_meta.deferred`, с довод и дата, броен дълг). Липса и в трите = ЧЕРВЕНО. К7 т. 1: празен квартал носи `_meta.no_places: [{code, why, signed_by, signed_at}]`; гейтът сравнява МНОЖЕСТВА: „жилищни кодове с нула доставени реда ⊆ `no_places` ∪ `deferred`“, падайки поименно. **Ако `tsveten_kvartal` попадне в `no_boundary`/`deferred`, проверката след пуша №2 става НЕПРИЛОЖИМА и това се записва в отчета** (решение §6.28).
  45: 
  46: **D5 · Ново име само с ≥ 2 свидетеля (К3) и обратим път.** „Цветен квартал“: свидетел 1 = подписът на Петър; свидетел 2 = `node/9664925200` с 15 места на ≤ 900 m. Втори свидетел може да е и АГКК именувана точка (Левски и Максуда имат; М0.21), ред от пощенския указател или общинска публикация с адрес (М0.22) — по-силни от OSM възел, защото са официални. При ЕДИН свидетел името е `alias`, не код. **Отмяна:** ред клас „въпрос“ + обратен диф с двоен запис + махане на кода от петте затворени списъка в един комит на Fire_Varna; фикстура: код в доставка, който вече не е в регистъра → червено. Записът влиза през конвейера на Varna_buildings (D14).
  47: 
  48: **D6 · `SIGNED_POLYGON` — свидетел ранг 3 (S1/К2).** Нов канал под `REG-*` (0), `KAIS-quar` (1), `KAIS-addr` (2). ОТДЕЛЕН блок в `varna_3d/src/fire_varna_locations.py` **между ред 873 и 875** — след записа на `picked` в `out` (867–873), преди `if signed:` (875) — и **никога в цикъла `offered/ranked/conflict` (785–853)**, където `conflict` бланкира вече написано поле (`:834`, `:852`) и вкарва реда в `pending_signature`. **Шест състояния:** `confirmed` · `compatible` (деклариран родител/дете, БЕЗ замяна и без уточняване) · `disputed` · `edge_pending` (D7) · `override_noted` · `written`. Пише САМО в ред без нито един свидетел, без `pending`, извън ръба, в точно един полигон (или в декларираното дете), с `witness=[CH_SIGNED_POLYGON]` и кода в `channels[CH_SIGNED_POLYGON].ids` (`qa_fire_varna_m6.py:304-308`). Полигон-местност никога не пълни `quarter` — `classify(code) == field` (`KIND_CLASS:118`), с падаща фикстура. `_narrow` (`:907-917`) уточнява САМО вътре в полигонния канал. **`SIGNED_OVERRIDE` се пази безусловно (S1):** при 12-те подписани хотела блокът само сравнява и пише `override_noted` в леджера; никога не мени полето, никога не влиза в `signed_vs_witness`, а `CHANNEL_RANK` не получава ключ `SIGNED_OVERRIDE`. **`disputed` е ЛЕДЖЕР-САМО:** редът остава дословно както е, отива в `polygon_review`, нищо публично не се мени. Това е **обявено ОТКЛОНЕНИЕ от К2** (решение §6.4): `LOC_KEYS` са точно 3 (`index.html:6311`, `:6531-6533`), няма ключ за `winner`/`reason`, а „падане до район“ би изтрило написан от по-силен канал квартал. Таблицата на К2 е входна карта за реда в опашката; спорът се версионира (`polygon_review[i].polygon_version`). **159 е ДОПУСТИМАТА популация, не write-set.** 8-те сблъсъка не се решават от полигона.
  49: 
  50: **D7 · Ръбът: `max(50, precision_m)` в EPSG:32635 върху пиннати ИЗВОРНИ координати (S2 + К5).** `_meta.precision_floor_m = 50`; гейтът отказва `precision_m < 50`. Забранено е да се четат изнесените координати (`fire_varna_locations.py:968-982` прави точно това и се маха от полигонния път). Мери се И точката, И закотвеното тяло (`evidence.kais_i`); разминаване → `edge_pending`. Формулата е `shapely.geometry.shape(f["geometry"]).boundary.distance(point)` — през `shape`, защото подписан квартал реалистично е MultiPolygon. Проекция: `place_identity.make_projection()` (`:219-236`); `pyproj` 3.6.1, `shapely` 2.1.2 — нула нови зависимости. **Никакво местене, никакъв snap.** `SIGNED_POLYGON_BORDER` НЕ става публикуван `src` — **обявено ОТКЛОНЕНИЕ от К5** (решение §6.16).
  51: 
  52: **D8 · Йерархията — само подписана и геометрично доказана.** Родство се чете единствено от `parents` (днес 6 записа), ациклично И доказано: **дете ⊆ родител в рамките на `precision_m` буфер**; фалшив `parent` = червено. **Числовата опашка в `is_child` (`:488-503`) не е родство при полигони.** „≤ 1 полигон на място“ важи между НЕСРАВНИМИ квартали. **В ПРАЗЕН ред пише детето; в ред с написан квартал полигонът НИКОГА не уточнява.** Възраждане 1–4 нямат `parents` — поправка в регистъра, ПРЕДИ кода (D14).
  53: 
  54: **D9 · Версии, диф и откат (К5, S1).** **ВСЯКА нова версия иска подпис на Петър.** Прагове: > 2 места сменят квартал ИЛИ > 10 % площ → двоен запис преди/след и пълно преизмерване; под тях — обикновен отчет. `--diff <предишна>` е ГЕЙТ с изход ≠ 0 над праговете (G15). **Версия 1: диф-гейтът е НЕПРИЛОЖИМ, не червен.** **Откат на лоша версия:** предишната подписана версия се връща като НОВА версия (`version` расте, `previous_version` сочи отхвърлената, `note` носи довода), минава пълния G1+G15 и се комитва от Петър; никакво `git revert` върху геометрия и никакво тихо редактиране. Всеки диф се предава като ред клас „въпрос“ (по D3 не може да е „артефакт“).
  55: 
  56: **D10 · Леджерът и пиновете (S1, S2).** Към **23-те колони** (М0.4): точка/тяло + CRS, кандидат-полигони, канал, `dist_to_edge_m`, състояние по D6, старо/ново по КОД, хешове на геометрия/регистър/алгоритъм, `approval_digest`. В `_meta`: `pins_polygons` до `pins_m6` (`:1111`), `polygon_review` до `pending_signature` (`:1140`), и **`base_rev` — ревизията P7, срещу която се мерят D18 и манифестът-данни**. **Координатата идва от `lat`/`lon`, добавени в `data/place_identity.json`** (мерено: 375 обекта, 0 с координата) като НОВ ПИНАТ вход в `RECORDED_INPUTS` (`:91-92`), с гейт G9. **Пиновете на `quarters_signed.geojson`, `place_identity.json` и `web/varna_buildings_3d.geojson` влизат в `build_inputs` (`:1247-1253`) И СЕ СВЕРЯВАТ в `_check_pins` (`:623-639`) и в G-M6.** `--inputs` (`:1305-1310`) е ПИСАТЕЛ, пуска се веднъж.
  57: 
  58: **D11 · Инструментът и provenance (S3).** Свой „режим граница“ във `varna_3d/web`, **нула нови runtime зависимости** (`web/vendor` държи само maplibre-gl **5.7.2** — `web/vendor/maplibre-gl.js:3` — и pmtiles 4.3.0; М0.18). `pitch = 0` + `map.setTerrain(null)` (`web/index.html:1962-1963`), `#pitch` disabled, кликът отговаря ПРЕДИ хидранта (`:4571`). Лентата на неточността: `line-width` по `156543.03392·cos(43,2°)/2^z` → z13 3,6 · z16 28,7 · z18 114,9 px за 50 m (М0.13). Слоеве-свидетели: КАИС телата, 375-те пина, OSM етикет-точките, **предишната версия като отделен слой**. Записва целия набор на D1. `preserveDrawingBuffer` — **един условен ред** зад `?granitsa` (`:828-841`). **STOP:** безусловен `preserveDrawingBuffer`; какъвто и да е `POST` в `serve.py`. Износ = Blob + `<a download>`.
  59: 
  60: **D12 · Търсенето (клас B) — К6 + S4.** Идемпотентен `location_key(toks) -> (type, phrase)`, приложен ИДЕНТИЧНО върху индекса и остатъка, дефиниран върху **СПИСЪК ОТ ТОКЕНИ**. Типовият префикс е поредица с двете си арности. Хвърля съюза „и“ и префикса, **пази числата** и затворен списък посоки. Правило: остатъкът == пълната фраза на ТОЧНО ЕДИН запис, иначе уникална СЪСЕДНА подфраза; пазач: число / посока / „sveti“ никога не квалифицира. **Областта е ИЗНЕСЕНИЯТ речник**, премерен наново преди подпис. **Типът СТЕСНЯВА само когато е изричен И съвпада с поне един кандидат.** **Двусмислието не ражда нов видим текст** (`AGENTS.md:138`) — **обявено ОТКЛОНЕНИЕ от К6**: уточнителят при двусмислие е отложен, защото иска дословен български текст от Петър (решение §6.20); днешното поведение при двусмислие се запазва и се пази от замразена заявка. **Родител ⊃ дете живее в ИЗНОСА** (per-code `type` и `parents` по КОДОВЕ); затворените списъци → `_meta` до `zone_generic_words` (`build_place_categories.py:566`), fail-closed. **Паритет:** `window.__places.locationKey(q)` влиза в корпуса `probe_out/token_parity.json` (**759 низа**, М0.18). **11 подписани вектора** + проби съюз, точкувана форма, число, посока, двусмислие, йерархия. Манифест по `bundle:ordinal` („РОЯЛ“ ×2; `release.compare()` сравнява по име, `gates/release.py:780-823`). **Смяна на КЛОН при непроменени редове = делта от първи ред.**
  61: 
  62: **D13 · Атомност през ТРИ репа (S5/S6).** Един комит през две репа не съществува. **Подредената тройка важи за ДАННИТЕ, не за инструмента:** инструментът (Г1) и гейтовете му са предпоставка и стоят извън тройката. Тройката е: **(1) Varna_buildings** — записът, `parents`, преподписаната константа (D14); **(2) varna_3d** — резолверът, двата износни гейта (`qa_fire_varna_export.py:191`, `qa_fire_varna_places_export.py:323`), вторият препис (`qa_fire_varna_m6.py:58-64`), износът; **(3) Fire_Varna** — **блобовете влизат в СЪЩИЯ комит със затворените списъци**: `QUARTER_SRC` (`index.html:6313`), `QUARTER_CODES` (`:6317`), `LOCALITY_CODES` (`:6322`), трите SHA пина (`:6288-6290`), `LEGACY_BUNDLE_SHA` (`:6301`), `PLACES_CACHE` v6 → **v7** (`:6265`), и поименно пиновете на двата теста: `PLACES_SHA256`/`BYTES` 122089/`GZIP9` 13728, `HOTELS_*` 148685/13084, `CATEGORIES_*` 75818/9104, `QUARTER_BY_SRC` (точно равенство), `QUARTER_CODES`, `LOCALITY_CODES`, `LOCATION_COUNTS` {quarter 20, district 5, locality 5}, `LEGACY_ROWS` 18, `LOCALITY_COUNT`; плюс baseline → `fd13907` (`signed_by: "pending — Петър"`) и подмяната на allow-файла. Числата се ПРЕМЕРВАТ след чертането. Тихата смърт, доказана: непознат `src` → `validLocation` false (`:6528-6534`) → `validTypedLocation` (`:6535-6541`) → `validatePlaces2` (`:6569-6576`) → `null` → `places2 = []`, хотелите остават (`:6627-6640`) — **150 места изчезват мълчаливо**; `accept` сверява SHA само при `crypto.subtle` (`:6605`) → кешът задължително на v7. **Манифестите са ТРИ** (`gates/release.py:157-159`): `lot1v_v_manifest_BASE_P7.json` = дифът на ДАННИТЕ (P7→P8 по `place_id`), `lot1v_v_manifest_P7_F12.json` = дифът на ПОВЕДЕНИЕТО, `lot1v_v_reference_manifest.json` = манифестът на референцията; и трите се преизползват в съществуващите слотове с `_meta.what` и изричен ред „името е остаряло“. Имената живеят на **ПЕТ ръчни места**: `gates/release.py:157-159`, `:175-183`, `manifest_anchor_gate.py:42-44`, `recall_sweep.py:3070-3071`, `recall_sweep.py:2661`. **Замразените тела са ТРИ** (амандамент №11 т. 4): референцията `recall_sweep_rows.json` (вързана през `expectations._meta.reference`), `expectations.json`, и паритетният корпус `probe_out/token_parity.json`, който **днес не е вързан от нищо** и влиза в `expectations._meta.inputs`.
  63: 
  64: **D14 · Регистърът е подписано тяло (S5).** `Varna_buildings/js/lib_quarter_registry.mjs:35` заключва `schema_version`, `id`, `display`, `kind`, `aliases`, `parents`; `:45` държи `REGISTRY_SIGNED_SHA256`; `:121-127` хвърля „never patch the constant to make a build pass“. Затова: (1) промяната е **СОБСТВЕН датиран план в Varna_buildings със собствен §7 (дефиниция за готово)**, минаващ през неговите Approval gates (`AGENTS.md:273-275`) **и през Кими и Astra** (§0.3), чиято присъда влиза в **собствен амандамент — нов датиран файл** в същата папка; (2) константата се преизчислява и **подписва от Петър, в негов комит**, заедно с данните; (3) `node js/test_quarter_registry.mjs` тича в кръга (G5); (4) **агент никога не пипа константата**. Преди комита: нула съвпадения на новото име в 449 `quar` + 19 813 `addr` и нула сблъсък на `match_key` (М0.14); след комита `qa_fire_varna_location_isolation.py` зелено (G6/G10) — `place_zones._registry:252-255` индексира БЕЗ вид.
  65: 
  66: **D15 · Гейт 0 преди опашката.** `ЗА_ПОДПИС_Г.md` не се ПИШЕ, преди да е зелено: `release.find_queue` е рекурсивната версия; в HEAD има точно една опашка; в `gates/allow/` има точно един json (`run_gates.py:199-217`). Архивът на опашките е **извън** `scratch/places_search`. G0 е гейт-ред на всяка стъпка, чийто write-set пипа опашка или allow-файл.
  67: 
  68: **D16 · Идентичности и write-set-ове.** Всеки комит носи изчерпателен write-set и дословно съобщение (таблицата е в плана §2). `Claude Architect` за планове и решения, `Claude Executor` за изпълнение, `Petar1984` само за `gates.sign`, подписаната геометрия и регистъра. Ръчният комит на Петър във varna_3d/Varna_buildings е **втори, назован клас** до амандамент №4 т. 6 и влиза като **амандамент — нов датиран файл**.
  69: 
  70: **D17 · Дайджестът на тялото за доставка Г.** Амандамент №11 приема вариант (а) изрично „за доставка A“. За доставка Г вариантът се **преобявява** (решение §6.5): важи (а) — несъвпадение се прощава само когато последният комит по артефакта е на `Petar1984` — и G12 проверява точно това.
  71: 
  72: **D18 · Написаният квартал не се променя.** След P8 всеки от **201-те** реда с написан квартал (М0.4) ЗАПАЗВА кода си. Базата „преди“ е назована: `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`, където `<base_rev>` е `_meta.base_rev` на леджера (D10) — същата ревизия, която храни манифеста-данни. Проверката е команда с изход ≠ 0 (G17).
  73: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md' -Encoding UTF8 -TotalCount 23 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # Амандамент №1 към ПЛАН „Границите“ v2 (05.09.2026, 21:25) — след оборването на v2 от Кими (К8–К14) и Astra (S7–S13) и след атаката на идеята „микрорайонът = блоковете си“ (Кими Б1–Б6, Astra B1–B6). Статус: **за Gate 1 — едно четиво за Петър**
   2: 
   3: Нов датиран файл по §0.2 на ПЛАН „ИЗЧИСТВАНЕ“ v2. Не редактира плана v2 и ADR 010; казва какво се променя в тях и защо. Присъдите дословно: `scratch/places_search/granitsi_v2_kimi_K8-K14_05.09.md`, `granitsi_v2_astra_S7-S13_05.09.md`, `granitsi_blocks_kimi_B1-B6_05.09.md`, `granitsi_blocks_astra_B1-B6_05.09.md`. Мерките от вечерта: `agkk_inspire_measure_05.09.md`, `ОТЧЕТ_Ф0б_05.09.md`, §4 тук.
   4: 
   5: **Думите на Петър тази вечер:** „искам да имаме ясно обособени граници на кварталите… искам да можем да ги намираме в търсачката“; „Възраждане 1, 2, 3 ти го дадох като пример“; „станаха много идеи, а нито една не работи както ми се иска“; „не искам регресии, а само подобрения“.
   6: 
   7: ## 1 · Присъдата в едно изречение
   8: **Всички пътища без твоята ръка са изчерпани и измерени: официални граници има само за петте района и шест квартала (АГКК); за комплексите и центъра никой извор не носи граница, КАИС блоковете и съседните адреси са подложка и проверка, не граница; затова границите ги чертаеш ти, върху карта с всички данни под писалката, автоматично идват шестте на АГКК, а търсенето се поправя с нормализатора и йерархията.** Това е планът v2 (Г1 инструмент → Г2 твоята вечер), потвърден от двамата одитори след като обориха всяка алтернатива. Разликата спрямо сутринта: вечерта ти е с подложка от данни (блокове с номера, адреси на съседните сгради, официалните полигони и точки на АГКК, OSM възлите, редовете на пощите), затова методът е „по сгради/по улици“, не „по памет“.
   9: 
  10: Кими за (i) комплексите предпочете „таблица блокове + обвивка“, Astra — „Петър чертае, блоковете проверяват“. Приемам **Astra**, защото Astra измери, а Кими предположи: блоковите номера се повтарят между комплексите (2, 3, 4, 6, 56 са и във Възраждане, и в Младост), „№ 83“ стои върху 211 отпечатъка, а само 11 от 375 места са на ≤ 60 m от блок с номер. Обвивка от такива блокове би била измислена територия. Блоковете остават като **слой-проверка**: всеки подписан полигон трябва да съдържа блоковете, които таблицата (ако Петър я подпише) му приписва, и нито един чужд.
  11: 
  12: ## 2 · Какво се приема от атаките и какво се променя (по номера)
  13: Всички присъди са приети; където Кими и Astra се разминават, печели по-строгата.
  14: 
  15: **Кими К8–К14 (v2):**
  16: - **К8 → ADR D0, G22.** До записани условия за повторна употреба официалният полигон на АГКК е САМО сравнителен свидетел в леджера (12-те печалби са кандидати, не се пишат). G22 приема `_meta.agkk_terms.terms ∈ {"published:<url>", "none_published_open_by_default"}` с дословен текст и дата; празен низ = червено. След отключване атрибуцията „АГКК INSPIRE GN 10-2019-v0“ е ред в картончето. Правната опора (Кими провери): ЗДПД чл. 11, ал. 1, т. 6–7 (условията са задължителен елемент на метаданните — АГКК не ги е публикувала), чл. 15, чл. 17; ЗДОИ чл. 3а, ал. 2, чл. 6, ал. 2, т. 5, чл. 15, ал. 4, чл. 41а. Без писма: записваме презумпцията с атрибуция.
  17: - **К9 → D0.** Обектът с двойно име („Чайка“ = „Св. Св. Константин И Елена“) се изяснява по `localid` ПРЕДИ Г2; влиза с двата `localid` в `witnesses[]` и дословен `note`; `deferred` с този довод е валиден отговор.
  18: - **К10 → D0 степен (3).** Всяка присъда от пощенския указател носи `source_snapshot: "2018-05-17"`; **не пише** в картата без по-нов свидетел за същата улица (REG адрес) — остава кандидат/свидетел №2. Празно квартално поле = мълчание.
  19: - **К11 → D0/D6.** Разминаване написан извор ↔ пощи (Св. Марина) не се решава по ранг: `disputed`, леджер-само, с двата извора дословно и „следваща проверка“ (за Св. Марина: правилото в §3а).
  20: - **К12 → D1/D3, отчет Ф0-б §6 т. 2.** „Зона 9000“ в картончето ОТПАДА; пощенският код е само леджер. Декларираната граница носи дословен етикет: „граница, очертана от Петър (дата), по местно знание/по сгради; официален извор няма (проверено 05.09.2026: АГКК, пощи, община)“.
  21: - **К13 → D5.** Свидетелят за ново име трябва да назовава ТОЧНО името; именни различия („Левски“ ↔ „Васил Левски“) се връзват само през подписан crosswalk/`aliases`; йерархия за втори свидетел: АГКК точка > пощенски ред ≥ общинска публикация > OSM възел.
  22: - **К14 → D10, Ф0-б.** `source_snapshot` за всяка външна присъда; при нова версия на АГКК/указателя съответствието се премерва; именният crosswalk обхваща и АГКК имената.
  23: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=74; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 74 -First 68 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 22ms:
  75: 
  76: **D20 · Затварящият документен комит.** Новите четири хеша се вписват в `docs/activeContext.md` СЛЕД пуша, в отделен комит на `Claude Architect` (Г3), който Петър пуска втори път. Локалното ≠ пушнатото за времето между двата пуша е очаквано и е назовано в §3 на плана.
  77: 
  78: ## Как е изпълнена всяка приета атака
  79: 
  80: | Атака | Къде | Отклонение |
  81: |---|---|---|
  82: | К1 задължителни свойства | D1 | — |
  83: | К2 спорът | D6 | **ДА** — леджер-само; без `winner`/`reason`; редът не пада до район → §6.4 |
  84: | К3 два свидетеля | D5 | — |
  85: | К4 лицензът в лота | D2, G21 | — |
  86: | К5 версия, диф, откат | D3, D7, D9, G15 | **ДА** — `SIGNED_POLYGON_BORDER` не се публикува → §6.16 |
  87: | К6 нормализатор + вектори | D12 | **ДА** — уточнителят при двусмислие отложен → §6.20 |
  88: | К7 празен квартал / припокриване | D4, D8 | — |
  89: | S1 ранг 3 + `SIGNED_OVERRIDE` се пази | D6, D8, D10 | — |
  90: | S2 ръбът | D7 | — |
  91: | S3 provenance | D1, D11 | — |
  92: | S4 идентичности | D12 | — |
  93: | S5 атомност и „varna_3d не се приема за частно“ | D3, D13, D14 | **ДА (условно)** — канонът е varna_3d при доказано частно репо; **G19 мери преди Г2** → §6.3 |
  94: | S6 четирите счупвания | D6, D8, D12, D13 | — |
  95: 
  96: Таблицата се сверява от одитора на Г0 (read-only) и от Кими/Astra при оборването: всеки ред има **или** непразна клетка „къде“, **или** маркер „ДА“ с номер на решение в §6; ред без едно от двете е находка. Скрипт за това не се пише — архитектът не пише код, а стойност за картата няма (решение на архитекта, §6а т. 22 на плана).
  97: 
  98: ## Последствия
  99: 
 100: **+** Петте района са доказано верни спрямо официалната граница (375/375); шест квартала получават официален полигон без нито един нарисуван връх; 12 места получават квартал с извор АГКК още преди вечерта; 159 реда без нито един написан свидетел могат да получат квартал по проследим път; 201-те написани получават второ око, чието несъгласие остава ВИДИМО и чийто код е защитен от гейт (D18); „училище цветен квартал“ и „училище св св константин и елена“ стават възможни.
 101: 
 102: **−** Честните цени: една вечер на Петър — по-къса след D0 (остатъкът: 26 жилищни кода без официален полигон, от които центърът няма НИКАКЪВ официален извор), но с непроверима дължина (144,80 km² изпъкнала обвивка); **единайсет негови докосвания**; 8-те сблъсъка остават `pending` и G-M6 остава изход 3 (G8); всяка нова версия е нов подпис; шест затворени списъка, три манифеста и три репа мърдат в подредена тройка; регистърът иска собствен план, собствено оборване и преподписана константа; геометрията не може да е подписан артефакт по днешния `SIGNABLE`; лицензът на „по улици“ може да отнеме CC0; обявен червен интервал (D19).
 103: 
 104: ## Какво НЕ е
 105: 
 106: Не е връщане към машинните обвивки (126 обвивки, IoU 0,13). Не е OSM като съдия. **Не е замяна на регистъра с АГКК:** официалният полигон пише само в празни редове, спорът с написан извор е видим, а суровите отговори на АГКК не се публикуват и не се проследяват преди G22. Не е сваляне на пощенския указател „за всеки случай“ — Ф0-б тръгва само с думата на Петър (11,3 MB през сателита). Не е нова зависимост — `terra-draw`/`mapbox-gl-draw` отпадат, **geojson.io също отпада** (празната подложка е входът, който роди обвивките). Не е поправка на едно училище: поправят се съюзът, префиксът, числата, посоките и 11-те сблъсъчни думи. **Не решава 8-те `pending_signature`.** Не публикува геометрия, `place_id`, `SIGNED_POLYGON_BORDER` или нов ключ в реда. Не е промяна на ADR 007 и не е ADR 009. **Съзнателно отложено, с име и дата:** разширяването на `SIGNABLE`/`blob_at` към чуждо репо и преименуването на манифестните слотове (Фаза C); `POST` в `serve.py`; `place_id` в блобовете (ADR 009, Фаза B); уточнителят при двусмислие (иска дословен текст от Петър); изнасянето на фрази за всичките 32 кода; кодовете в `_meta.deferred` — **броен дълг**, не мълчание.
 107: 
 108: ## Гейтове
 109: 
 110: Всеки ред е команда с изход ≠ 0, с назован файл и с отрицателна фикстура, която ТРЯБВА да падне преди да се пипнат данни. Планът §7 изброява всичките.
 111: 
 112: | # | Команда (файл) | Отрицателна фикстура |
 113: |---|---|---|
 114: | G0 | `python -m gates.release` (Fire_Varna) | втора опашка, **комитната** в scratch-клонинг → блок; два json в `gates/allow/` → ✗. Таблицата „Как е изпълнена всяка приета атака“ се сверява от одитора на Г0 и от Кими/Astra (ред без „къде“ и без „ДА“ + §6 номер = находка), не от скрипт |
 115: | G1 | `python src/qa_quarters_signed.py` (нов, varna_3d) | 17 фикстури в `--break-me`: самопресичане · дублиран код · код извън регистъра · жилищен код извън трите множества · припокриване > `max(50, precision_m)` · деклариран родител без съдържание · дете без деклариран родител · полигон-местност за `quarter` · `method:"по улици"` без ключ · `method:"по сгради"` при `faza0_signed:false` · `basemap`/`visible_layers` = `sat` · лиценз, несъгласен с метода · липсващо задължително property · `precision_m` = 25 · разминат `approval_digest` · липсващ/празен файл = ЧЕРВЕНО · `--diff`: версия, мърдаща 3 места, и версия, мърдаща 11 % площ |
 116: | G2 | `python src/qa_quarters_license.py` | `.geojson` с кадастрален низ ВЪТРЕ в координатен масив (+ доказателство, че СТАРИЯТ гейт е зелен) · `cadnum` в `properties` · `2026.09.05` червено / `2026-09-05` зелено. Поправят се `data_files()` (`:85-86`) и `walk_coords` (`:106-118`) |
 117: | G3 | `python src/qa_no_cad_ids.py` | новият проследен файл е ВЪТРЕ в обхвата, не в `ALLOW` |
 118: | G4 | `python src/qa_quarters_author.py` (нов): `git ls-files --error-unmatch data/quarters_signed.geojson` **и** `git log --format='%an' -1 -- …` == `Petar1984` | празен изход или непроследен път = ЧЕРВЕНО (fail-closed) |
 119: | G5 | `node js/test_quarter_registry.mjs` (Varna_buildings) | регистър без преподписан `REGISTRY_SIGNED_SHA256` → червено |
 120: | G6 | `python src/qa_registry_name_clash.py` (нов): 0 съвпадения в 449 `quar` + 19 813 `addr`, 0 сблъсъка на `match_key` | псевдоним, който прави стар запис двусмислен → G-ISO ✗ |
 121: | G7 | четящ прогон `python src/fire_varna_locations.py` през `_check_pins` | подменен байт в `quarters_signed.geojson` / `place_identity.json` → `die` |
 122: | G8 | `python src/qa_fire_varna_m6.py` → **изход 3, `fails` = 0, точно 8 `pending` (същите осем имена)** | девети `pending` или ≥ 1 `fail` = STOP. Публикацията остава забранена от Фаза A (`ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` §A.4) и се отпушва само от Фаза D — решение §6.29. Петте нови избора се ДОБАВЯТ към `choices` (`:173-176`): `channel`, `polycode`, `edge`, `dispute`, `child`; `CHANNEL_RANK` се чете с `.get` (`:310`, `:314` днес хвърлят `KeyError`) |
 123: | G9 | сверка на прегенерирания `place_identity.json` | ≥ 1 разминат `place_id`/`kais_i`/`kais_d_m` → STOP |
 124: | G10 | `python src/qa_fire_varna_location_isolation.py` → 4/4 | мръднат чужд артефакт → ✗ |
 125: | G11 | `python scratch/places_search/recall_sweep.py` (report-only) срещу назован изход: 140 замразени в 6 кофи + `tokens` 45 / `trigger_today` 33 (`m7_trigger_tokens.json._meta.measured`) + 0 непокрити делти; `node scratch/places_search/probe_places_fv.mjs` над 759 низа + `locationKey`; **контролните заявки се мерят ТУК, преди пуша** | нарочно разминат JS клон → паритетът пада |
 126: | G12 | `python -m gates.release` | делта без подписан ред; ред „да“ без видимо поле `тяло`; блок „да“ с най-нов комит на агент; дайджест по D17; мутиран `probe_out/token_parity.json` → `_meta.inputs` ✗ |
 127: | G13 | `python -m gates.run_gates` | **G13-а (преди подписа):** допустими жълти са ТОЧНО „4 · покритие спрямо подписания baseline“ и „6 · release“, докато артефактите носят `pending — Петър`; всяко друго жълто и всяко червено = STOP. **G13-б (след подписа):** 7/7 зелени, 0 жълти |
 128: | G14 | `python -m unittest discover -s tests` → 0 червени | извън интервала на D19; `QUARTER_BY_SRC` е точно равенство |
 129: | G15 | `python src/qa_quarters_signed.py --diff <предишна>` | над праговете на D9 изход ≠ 0; версия 1 = неприложим; откат = нова версия по D9 |
 130: | G16 | куката `.git/hooks/pre-push` + пушът | само Петър; без `--no-verify` |
 131: | G17 | `python src/qa_written_quarters_stable.py` (нов) — 201 написани реда срещу `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json` | нарочно сменен код на един написан ред → изход ≠ 0 |
 132: | G18 | `node web/quarters.guard.test.mjs` (нов) | пазачът при `visibility === "visible"` на `sat` не отказва връх → ✗ |
 133: | G19 | `gh repo view Petar1984/varna_3d --json visibility,url` → `PRIVATE` | празен изход / `PUBLIC` = STOP преди Г2; D3 пада и §6.3 се преотваря |
 134: | G20 | `python -m unittest discover -s tests 2>&1` при отваряне и при затваряне на интервала D19 | набор падащи тестове ⊄ назования в плана §2 → STOP; след `--freeze` наборът не е празен → STOP |
 135: | G21 | `python src/qa_faza0_signed.py` (нов): `_meta.faza0_signed` може да е `true` само ако `docs/decisions/ФАЗА_0_лицензи.md:4` вече не носи „чака подпис“ | `faza0_signed: true` при днешния ред 4 → ✗ |
 136: | G22 | вътре в `qa_quarters_signed.py`: Feature със `source: "agkk_inspire_gn"` се приема само ако `_meta.agkk_terms = {url, checked_on, terms}` е попълнено и `witnesses[]` носи `localid` на АГКК | официален полигон без `_meta.agkk_terms` → ✗; `localid`, който го няма в суровия отговор → ✗ |
 137: | G23 | `python src/qa_district_official.py` (нов, varna_3d): всяко доставено място в АГКК AU5 полигона на своя `district.code` (днес 375/375, М0.19) | нарочно разменен код на район на един ред → изход ≠ 0 |
 138: | G24 | отчетът на Ф0-б съществува ПРЕДИ Г2 и носи възпроизводими числа (SHA на PDF-а, брой редове за Варна, покритие на 174-те, съгласие с 201-те, черновата на crosswalk-а) | липсващ отчет или PDF с друг SHA → Г2 не тръгва |
 139: 
 140: ## Оборване
 141: 
 142: Кими (К8+) и Astra (S7+) атакуват ТОЗИ документ и плана преди изпълнение (§0.3); същото важи и за собствения план на Varna_buildings (D14). Присъдите влизат като **амандамент — нов датиран файл** (`docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md`), а този раздел получава редакция в комита Г0-б, който сменя статуса на `Accepted`. Решенията за Петър са номерирани в §6 на плана и се отговарят на Gate 1.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md' -Encoding UTF8 -TotalCount 23 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
   1: # Амандамент №1 към ПЛАН „Границите“ v2 (05.09.2026, 21:25) — след оборването на v2 от Кими (К8–К14) и Astra (S7–S13) и след атаката на идеята „микрорайонът = блоковете си“ (Кими Б1–Б6, Astra B1–B6). Статус: **за Gate 1 — едно четиво за Петър**
   2: 
   3: Нов датиран файл по §0.2 на ПЛАН „ИЗЧИСТВАНЕ“ v2. Не редактира плана v2 и ADR 010; казва какво се променя в тях и защо. Присъдите дословно: `scratch/places_search/granitsi_v2_kimi_K8-K14_05.09.md`, `granitsi_v2_astra_S7-S13_05.09.md`, `granitsi_blocks_kimi_B1-B6_05.09.md`, `granitsi_blocks_astra_B1-B6_05.09.md`. Мерките от вечерта: `agkk_inspire_measure_05.09.md`, `ОТЧЕТ_Ф0б_05.09.md`, §4 тук.
   4: 
   5: **Думите на Петър тази вечер:** „искам да имаме ясно обособени граници на кварталите… искам да можем да ги намираме в търсачката“; „Възраждане 1, 2, 3 ти го дадох като пример“; „станаха много идеи, а нито една не работи както ми се иска“; „не искам регресии, а само подобрения“.
   6: 
   7: ## 1 · Присъдата в едно изречение
   8: **Всички пътища без твоята ръка са изчерпани и измерени: официални граници има само за петте района и шест квартала (АГКК); за комплексите и центъра никой извор не носи граница, КАИС блоковете и съседните адреси са подложка и проверка, не граница; затова границите ги чертаеш ти, върху карта с всички данни под писалката, автоматично идват шестте на АГКК, а търсенето се поправя с нормализатора и йерархията.** Това е планът v2 (Г1 инструмент → Г2 твоята вечер), потвърден от двамата одитори след като обориха всяка алтернатива. Разликата спрямо сутринта: вечерта ти е с подложка от данни (блокове с номера, адреси на съседните сгради, официалните полигони и точки на АГКК, OSM възлите, редовете на пощите), затова методът е „по сгради/по улици“, не „по памет“.
   9: 
  10: Кими за (i) комплексите предпочете „таблица блокове + обвивка“, Astra — „Петър чертае, блоковете проверяват“. Приемам **Astra**, защото Astra измери, а Кими предположи: блоковите номера се повтарят между комплексите (2, 3, 4, 6, 56 са и във Възраждане, и в Младост), „№ 83“ стои върху 211 отпечатъка, а само 11 от 375 места са на ≤ 60 m от блок с номер. Обвивка от такива блокове би била измислена територия. Блоковете остават като **слой-проверка**: всеки подписан полигон трябва да съдържа блоковете, които таблицата (ако Петър я подпише) му приписва, и нито един чужд.
  11: 
  12: ## 2 · Какво се приема от атаките и какво се променя (по номера)
  13: Всички присъди са приети; където Кими и Astra се разминават, печели по-строгата.
  14: 
  15: **Кими К8–К14 (v2):**
  16: - **К8 → ADR D0, G22.** До записани условия за повторна употреба официалният полигон на АГКК е САМО сравнителен свидетел в леджера (12-те печалби са кандидати, не се пишат). G22 приема `_meta.agkk_terms.terms ∈ {"published:<url>", "none_published_open_by_default"}` с дословен текст и дата; празен низ = червено. След отключване атрибуцията „АГКК INSPIRE GN 10-2019-v0“ е ред в картончето. Правната опора (Кими провери): ЗДПД чл. 11, ал. 1, т. 6–7 (условията са задължителен елемент на метаданните — АГКК не ги е публикувала), чл. 15, чл. 17; ЗДОИ чл. 3а, ал. 2, чл. 6, ал. 2, т. 5, чл. 15, ал. 4, чл. 41а. Без писма: записваме презумпцията с атрибуция.
  17: - **К9 → D0.** Обектът с двойно име („Чайка“ = „Св. Св. Константин И Елена“) се изяснява по `localid` ПРЕДИ Г2; влиза с двата `localid` в `witnesses[]` и дословен `note`; `deferred` с този довод е валиден отговор.
  18: - **К10 → D0 степен (3).** Всяка присъда от пощенския указател носи `source_snapshot: "2018-05-17"`; **не пише** в картата без по-нов свидетел за същата улица (REG адрес) — остава кандидат/свидетел №2. Празно квартално поле = мълчание.
  19: - **К11 → D0/D6.** Разминаване написан извор ↔ пощи (Св. Марина) не се решава по ранг: `disputed`, леджер-само, с двата извора дословно и „следваща проверка“ (за Св. Марина: правилото в §3а).
  20: - **К12 → D1/D3, отчет Ф0-б §6 т. 2.** „Зона 9000“ в картончето ОТПАДА; пощенският код е само леджер. Декларираната граница носи дословен етикет: „граница, очертана от Петър (дата), по местно знание/по сгради; официален извор няма (проверено 05.09.2026: АГКК, пощи, община)“.
  21: - **К13 → D5.** Свидетелят за ново име трябва да назовава ТОЧНО името; именни различия („Левски“ ↔ „Васил Левски“) се връзват само през подписан crosswalk/`aliases`; йерархия за втори свидетел: АГКК точка > пощенски ред ≥ общинска публикация > OSM възел.
  22: - **К14 → D10, Ф0-б.** `source_snapshot` за всяка външна присъда; при нова версия на АГКК/указателя съответствието се премерва; именният crosswalk обхваща и АГКК имената.
  23: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=40; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 40 -First 6 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 5ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=78; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md' -Encoding UTF8 | Select-Object -Skip 78 -First 64 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 14ms:
  94: 
  95: ### Г0 · Документите (Fire_Varna · Claude Architect · 2 комита, разделени от Gate 1)
  96: **Г0-а · чернова.** Write-set: `docs/decisions/010_signed_quarter_boundaries.md`, `docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md`, `scratch/places_search/osm_quarters_measure_05.09.md` (М0.17 — изворът на присъдата „никой отворен извор не носи границите“), `scratch/places_search/agkk_inspire_measure_05.09.md` (М0.19–М0.21, М0.23), `scratch/places_search/granitsi_astra_official_boundaries_05.09.md` (М0.22). Суровите отговори на АГКК (`scratch/places_search/agkk_inspire_2026-09-05/`) остават НЕПРОСЛЕДЕНИ до G22. **Не пипа `PARKED.md` и `activeContext.md`.**
  97: Съобщение: `docs: ADR 010 draft — signed quarter boundaries as a rank-3 witness + plan Границите v2 (unrefuted, unsigned) (Г0-а)`
  98: Гейт **G0**: `python -m gates.release` (една опашка в HEAD, един allow); таблицата „Как е изпълнена всяка приета атака“ се сверява от одитора и от Кими/Astra (ред без „къде“ и без „ДА“ + §6 номер = находка), не от скрипт.
  99: **После:** Кими и Astra оборват ADR 010 + този план (§8). **Gate 1 = подписът на Петър** + отговорите на §6.
 100: **Г0-б · откриването (само след Gate 1).** Write-set: `docs/decisions/010_signed_quarter_boundaries.md` (**статус → `Accepted`, §Оборване попълнено**), `docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md` (**присъдата на Кими/Astra върху v2 — нов датиран файл по §0.2**), `docs/plans/PARKED.md` (маха се P1, лотът в движение = Границите), `docs/activeContext.md`, `docs/plans/ПЛАН_ЛОТ_Границите.md` (само статус), `docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_12_05.09.md` (ръчният комит на Петър във varna_3d/Varna_buildings като втори назован клас до амандамент №4 т. 6), `scratch/places_search/granitsi_brief_kimi.md`, `granitsi_brief_astra.md`, `granitsi_v2_brief_kimi.md`, `granitsi_v2_brief_astra.md`.
 101: Съобщение: `docs: lot „Границите“ opened on Petar's word — P1 unparked, ADR 010 accepted, amendments 1 and 12 (Г0-б)`
 102: Гейт **G0** (опашката и allow-файлът не са пипани, но G0 доказва, че HEAD носи точно една опашка); одиторът сверява таблицата на атаките в обновения ADR.
 103: 
 104: ### Г1 · Инструментът и гейтовете (varna_3d, клон `rezhimi` · Claude Executor „varna_3d“ · 4 комита + одит)
 105: **Г1-0 · указателят.** Write-set: `docs/decisions/УКАЗАТЕЛ_ADR_010_граници.md`, `docs/decisions/README.md`.
 106: Съобщение: `решения: указател към ADR 010 (Fire_Varna) — какво важи за това репо (Г1-0)`
 107: Гейт: `git status --short` чист извън write-set-а; редът в `README.md` сочи съществуващ файл (изход ≠ 0 при счупен път).
 108: 
 109: **Г1-а · режимът.** `web/quarters.js` (~300 реда по калъпа на `hydrants.js`): бутон в `.modes`, `MODE.gran`, `addLayerBefore`; **кликът отговаря ПРЪВ** (`index.html:4571`); **pitch 0 + `map.setTerrain(null)` + `#pitch` disabled**; лента по М0.13; слоеве-свидетели: КАИС телата, 375-те пина (на живо), OSM етикет-точките, **предишната версия като отделен слой**; износ = Blob + `<a download>`; `preserveDrawingBuffer` **само** зад `?granitsa`; отказ да запише връх при видим `sat`; „по улици“ и (при `faza0_signed:false`) „по сгради“ заключени; provenance по D1/D11.
 110: Write-set: `web/quarters.js`, `web/index.html`, `web/quarters.guard.test.mjs`, `.gitignore` (**редът `!data/quarters_signed.geojson` след ред 23 влиза ТУК и никъде другаде**).
 111: Съобщение: `места: режим „граница“ — рисуване и одобрение с провенанс, наклон 0, заключени методи, износ през браузъра (Г1-а)`
 112: Гейт: `git check-ignore -v data/quarters_signed.geojson` → **rc=1**; **G18**. **STOP:** безусловен `preserveDrawingBuffer`; какъвто и да е `POST` в `serve.py`.
 113: 
 114: **Г1-б · гейтовете на геометрията.** `src/qa_quarters_signed.py` с 17-те фикстури на **G1**, `--diff` като ГЕЙТ (**G15**), „липсващ файл = ЧЕРВЕНО“; `src/qa_quarters_author.py` (**G4**); `src/qa_registry_name_clash.py` (**G6**); `src/qa_written_quarters_stable.py` (**G17**); `src/qa_faza0_signed.py` (**G21**). Жилищните кодове се четат от регистъра, не от литерал.
 115: Write-set: `src/qa_quarters_signed.py`, `src/qa_quarters_author.py`, `src/qa_registry_name_clash.py`, `src/qa_written_quarters_stable.py`, `src/qa_faza0_signed.py`, `tests/` фикстурите.
 116: Съобщение: `места: гейтове на подписаните граници — геометрия, три множества, родство, лиценз, дайджест, диф, автор, стабилност, ФАЗА_0 (Г1-б)`
 117: Гейт: `--break-me <всяка от 17-те>` → **17 от 17 червени**; **G21** върху фикстура `faza0_signed:true`.
 118: 
 119: **Г1-в · слепият лицензен гейт.** `data_files()` хваща и `*.geojson`; `walk_coords` обхожда координатните МАСИВИ; правило „всички дати ISO“.
 120: Write-set: `src/qa_quarters_license.py`, фикстурите.
 121: Съобщение: `места: лицензният гейт вижда .geojson и координатните масиви; датите са ISO (Г1-в)`
 122: Гейт **G2** — трите фикстури + **доказателството, че СТАРИЯТ гейт е зелен**.
 123: **Одит на Г1 (read-only, Opus)** — трети агент върху целия инструмент и петте нови гейта.
 124: 
 125: ### Ф0-б · Пощенският указател като свидетел — МЯРКА преди вечерта (varna_3d · Claude Executor „varna_3d“ · 0 комита с данни, 1 отчет)
 126: **Тръгва само с думата на Петър** (решение §6.3: 11,3 MB през сателита, веднъж). Свалянето: `curl -L -o scratch/refactor/_addr/post_codes_all_2018.pdf https://www.crc.bg/files/_bg/post_codes_all__4_-_2018_17.05.2018.pdf`; SHA256 и байтовете (очаквани 11 344 012) в отчета; PDF-ът е НЕПРОСЛЕДЕН. Извличане на редовете за Варна (жилищен район · улица · блокове · номера от/до · четност) с наличния PDF-текстов път (без нова зависимост; ако няма такъв — STOP и въпрос); нормализация на улиците през същия `street_phrase` калъп като адресите (ADR 008 D5); съединяване с 375-те по `address.street_phrase` + `house_key` (адрес има при 179 реда; за останалите — мълчание, не догадка). Отчет `scratch/places_search/ОТЧЕТ_Ф0б_<дата>.md`: колко от 174-те получават „жилищен район“ (по улица + номер в диапазона; без диапазон = без отговор); колко от 201-те се съгласяват / спорят с написания квартал; **черновата на crosswalk-а** „жилищен район“ на пощите ↔ регистров код (напр. „ж.к. Васил Левски“ ↔ `kv_levski`; празни полета = без ред), за подпис от Петър; кои редове за Варна носят празен жилищен район.
 127: Write-set: `scratch/places_search/ОТЧЕТ_Ф0б_<дата>.md` (+ скриптът на мярката в `scratch/refactor/_addr/`, без данни в `data/`).
 128: Съобщение: `мярка: пощенският указател 2018 като свидетел за квартал — покритие на 174-те, съгласие с 201-те, чернова на crosswalk (Ф0-б)`
 129: Гейт **G24**: отчетът съществува ПРЕДИ Г2 с възпроизводими числа; SHA на PDF-а различен от записания → STOP. **Решение след отчета (амандамент, нов датиран файл):** каналът `POST-2018` влиза в P8 (D0 степен 3) само ако покритието е ненулево И crosswalk-ът е подписан; иначе указателят остава свидетел №2 за имена (D5) и нищо повече. Дотогава Г2 чертае остатъка без да чака P8.
 130: 
 131: ### Р · Регистърът (Varna_buildings · собствен датиран план · Петър комитва)
 132: **Р-0 (Claude Architect на Varna_buildings · 1 комит).** Датиран план по Approval gates („Data-source change“, `AGENTS.md:273-275`) с **собствен §7 (дефиниция за готово: G5 зелен, G6 зелен преди и G10 4/4 след, преподписана константа, нула съвпадения по М0.14)**: `parents` за Възраждане 1–4 → `vazrazhdane`; запис `tsveten_kvartal` (`kind: "кв"`, `aliases`, `why` с двата свидетеля, `source: "declared_local_knowledge"`). **Планът минава през Кими и Astra преди изпълнение; присъдата им влиза в `docs/plans/ПЛАН_регистър_Границите_амандамент_1_05.09.md`** (нов датиран файл) и има собствен Gate 1.
 133: Write-set: `docs/plans/ПЛАН_регистър_Границите_05.09.md`.
 134: Съобщение: `план: регистърът за лот „Границите“ — родителите на Възраждане 1–4 и „Цветен квартал“ (Р-0)`
 135: Гейт **G0-аналог**: планът назовава write-set, дословното съобщение, преподписването на `REGISTRY_SIGNED_SHA256`, собствен §7 и файла на своя амандамент; липса на което и да е → изход ≠ 0 при ревюто.
 136: **Р-1 (Petar1984 · 1 негов комит).** `config/quarter_registry.json` + **`js/lib_quarter_registry.mjs` с преизчисления `REGISTRY_SIGNED_SHA256`**.
 137: Гейт **преди**: **G6** (М0.14: 0/0). Гейт **след**: **G5**; изпълнителят на varna_3d пуска **G10** → 4/4 байт-равно. STOP при ≥ 1 съвпадение или мръднал чужд артефакт.
 138: **Р е ПРЕДИ Г2** — иначе Петър чертае код, който още не съществува. По D13 Р е ход (1) от тройката на ДАННИТЕ; Г1 е инструмент и стои извън нея.
 139: 
 140: ### Г2 · Вечерта на Петър (Petar1984, varna_3d · 1 негов комит)
 141: **Гейт ПРЕДИ:** **G19** `gh repo view Petar1984/varna_3d --json visibility,url` → `PRIVATE`; `PUBLIC` или празно = STOP и §6.3 се преотваря. **G21** зелен.
 142: **Първо одобрява шестте официални полигона на АГКК** (`source: "agkk_inspire_gn"`, при зелен G22; без рисуване; „Чайка“ с двете имена — с довод в `note` дали е `chaika_kk`, `kk_konstantin_elena`, или спорен → `deferred`). **После чертае само ОСТАТЪКА:** 26 жилищни кода без официален полигон — комплексите (mladost/1/2, vazrazhdane/1–4, briz, chaika_kv, izgrev_kv, troshevo, pobeda, druzhba, kaisieva, evksinograd, trakia, rozova_dolina, hristo_botev, sv_ivan_rilski) и центърът без никакъв официален извор (tsentar, grackata_mahala, kolhozen_pazar, maksuda, kv_levski, tsveten_kvartal). Ако отчетът на Ф0-б вече е дал пощенски свидетел за улиците на даден код, той е подложка-свидетел, не граница. Всеки жилищен код → `polygon` | `no_boundary` (с довод) | `deferred` (с довод и дата); празните кодове → `_meta.no_places`; **втори кръг „сух диф“** — мърда една граница, пуска `--diff`, вижда площ/членство/симетрична разлика/изместване.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=142; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md' -Encoding UTF8 | Select-Object -Skip 142 -First 49 | ForEach-Object { "'$n++; '"'{0,4}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 12ms:
codex
Има два блокиращи пропуска: `deferred` няма `Feature`, но новият гейт изисква двупосочно съответствие; мярката преди борда чака координати от P8-а, който е след потвърждаването. D7 вече задава правилния ръб `max(50, precision_m)` — тук е нужна проверка на изпълнението, а не ново правило.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import math
lat=math.radians((43.170+43.262)/2)
w=(27.985-27.84)*111320*math.cos(lat)
h=(43.262-43.170)*111320
r=500/math.sqrt(2)
print(f'bbox_approx_km={w/1000:.3f} x {h/1000:.3f}; area_km2={w*h/1e6:.3f}')
print(f'grid_max_distance_m={r:.6f}; disc_km2={math.pi*r*r/1e6:.6f}; 100/disc={100/(math.pi*r*r/1e6):.3f}/km2')
print(f'670_calls_at_28s_hours={670*28/3600:.6f}; five_extra_calls_per_missing_code_seconds={5*28}')
print(f'precision_fixture_passes={50 >= max(50,3*11)}; edge_75m_with_precision_100_is_pending={75 <= max(50,100)}')
'@ | python -" in C:\git\Fire_Varna
 succeeded in 0ms:
bbox_approx_km=11.763 x 10.241; area_km2=120.475
grid_max_distance_m=353.553391; disc_km2=0.392699; 100/disc=254.648/km2
670_calls_at_28s_hours=5.211111; five_extra_calls_per_missing_code_seconds=140
precision_fixture_passes=True; edge_75m_with_precision_100_is_pending=True

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import hashlib,re
paths=['docs/activeContext.md','scratch/places_search/granitsi_am2_brief_astra.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md']
for p in sorted(paths):
    b=Path(p).read_bytes(); s=b.decode('utf-8'); assert s.encode('utf-8')==b
    print(p, 'sha256='+hashlib.sha256(b).hexdigest(), 'utf8=OK', 'mojibake='+str(bool(re.search(r'[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]',s))))
'@ | python -" in C:\git\Fire_Varna
 exited 1 in 10ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$targets = @('"'docs/activeContext.md','scratch/places_search/granitsi_am2_brief_astra.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md'); "'$utf8Strict = New-Object System.Text.UTF8Encoding($false,$true); $targets | Sort-Object -CaseSensitive | ForEach-Object { $b=[System.IO.File]::ReadAllBytes((Join-Path (Get-Location) $_)); $s=$utf8Strict.GetString($b); $round=[Convert]::ToBase64String($b) -ceq [Convert]::ToBase64String($utf8Strict.GetBytes($s)); '"'{0} | UTF8-roundtrip={1} | mojibake={2} | sha256={3}' -f "'$_,$round,($s -match '"'[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]'),(Get-FileHash -LiteralPath "'$_ -Algorithm SHA256).Hash.ToLowerInvariant() }' in C:\git\Fire_Varna
 succeeded in 72ms:
docs/activeContext.md | UTF8-roundtrip=True | mojibake=False | sha256=90995e6721e5952df61289dabd4d7d4931816418c10495a43f5d915e327f7339
docs/decisions/010_signed_quarter_boundaries.md | UTF8-roundtrip=True | mojibake=False | sha256=0e6adfdb127f1e7cdac3777a3ff511bd75c590c7ea0bff72e27ad158ac66cdd2
docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md | UTF8-roundtrip=True | mojibake=False | sha256=eb4eb0142aa10b19ab677634100c9ff6f286888f03028ce6e85dda42ef7f8e25
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | UTF8-roundtrip=True | mojibake=False | sha256=a0ef558182e711203f36f614863b3d5f508ad4969f800655081f781f488c0c86
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | UTF8-roundtrip=True | mojibake=False | sha256=c91a820608b457520fc102cc1644677276ff47c988226339df2b2fb2d13e0088
scratch/places_search/granitsi_am2_brief_astra.md | UTF8-roundtrip=True | mojibake=False | sha256=6c8a37bf45293537bf91d8011419535a959d4f9cc6d60f7d84af7b0739563818

codex
**НЕГОДНО за изпълнение в сегашния вид.** Прегледът е read-only; файлове не са променяни. Аритметиката е проверена; геометрични тела и browser export не са изпитвани.

Прочетеният документен обхват е следният; `V2`, `A1`, `A2` по-долу означават съответните планове. Извън него няма инспектирани JSON/GeoJSON/PDF или изпълним код.

```text
docs/activeContext.md | 15557 bytes | 132 lines
docs/decisions/010_signed_quarter_boundaries.md | 53242 bytes | 142 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md | 61905 bytes | 264 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | 26249 bytes | 75 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | 30160 bytes | 107 lines
scratch/places_search/granitsi_am2_brief_astra.md | 4915 bytes | 10 lines
```

Декларираният статус на A2 е „за Gate 1“. Всички шест документа преминаха UTF-8 round-trip и проверката за mojibake.

**S14. Мрежата не доказва пълнота.** При зададеното в brief-а подреждане по центрове, 500 m квадратна мрежа гарантира най-близка проба на най-много `500/√2 = 353,55 m` **в покритите клетки**. Дискът е `0,3927 km²`; 100 по-близки центъра могат да изместят квартала — еквивалентна гъстота около `255/km²`. Това е контрапример, не измерена гъстота във Варна. Допълнителните 163 точки не осигуряват горна граница на конкуриращите центрове.

Пропускат се голям полигон с център между пробите, квартал сред плътни сгради, курорт с център извън bbox, компонент на `MultiPolygon`, чийто общ център е далеч, и валиден малък полигон под филтъра `0,04 km²`. API centre, centroid и регистрова точка не са непременно една координата. D7 изрично допуска `MultiPolygon`. [ADR:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50)

Една ограничена проверка: за всеки код без еднозначен кандидат — `count=100` при регистровата точка и четири метрични отмествания ±300 m, включително извън bbox; запазени заявки, отговори и SHA. При 14 кода: максимум 70 заявки, приблизително 32,7 минути. Ненамереното остава „неустановено“. G26 доказва решение за код, а не изчерпателност на Wikimapia. [A2:74](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:74), [V2:142](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:142)

**S15. Решенията нямат достатъчно определен договор.** Минимумът е:

- `_meta`: `schema_version`, `board_sha256`, подписан `registry_sha256`, manifest с SHA на всички входове, версия на канонизацията;
- ред: `code`, `choice ∈ {official,reconstructed,wikimapia,none,deferred}`, квалифициран source Feature ID, geometry SHA, подписан crosswalk, `reason`, `decided_by`, неизменен `decided_at`;
- само за Wikimapia: `wm_id`, пълният `wm_polygon_sha256`; при останалите — `null`.

Общ `data_sha256` е достатъчен само ако обвързва целия manifest. Повтарянето на page/data SHA във всеки ред е излишно. `fetched_at` и `decided_at` означават различни събития. Raw snapshot SHA, canonical geometry SHA и delivery SHA трябва да имат отделни определения; за `MultiPolygon` липсват правила за подредбата на компонентите и вътрешните пръстени. [ADR:38](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:38), [A2:59](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:59)

**Пряко противоречие:** „всеки Feature има ред … и обратно“ отхвърля валиден `deferred`, който няма Feature. Правилната биекция е решения ↔ трите множества: `official/reconstructed/wikimapia→polygon`, `none→no_boundary` с null geometry, `deferred→_meta.deferred`. G26 изпуска `reconstructed`. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [ADR:44](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:44)

Два записани `decisions_sha256` не доказват одобрение. Нужни са прочит на точния Petar-committed blob, сверка към подписан въпрос с видимо `тяло`, и проверка `code→source ID→frozen geometry`. G25 трябва да отхвърля подменен `wm_id`, дори геометричният SHA да съвпада. [ADR:42](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:42)

На Windows преименуване или `(1)` само не променя SHA; опасностите са избран стар download, редакторна BOM/CRLF конверсия и Git EOL преобразуване. При предложена канонизация UTF-8 без BOM, sorted keys, compact JSON и финален LF, след staging изпълнителят пуска следното с трите реални аргумента:

```powershell
python -c "import sys,json,hashlib,subprocess,pathlib; b=pathlib.Path(sys.argv[2]).read_bytes(); j=json.loads(b.decode('utf-8')); assert b==(json.dumps(j,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8'); assert b==subprocess.check_output(['git','cat-file','blob',':'+sys.argv[1]]); assert hashlib.sha256(b).hexdigest()==sys.argv[3]; print('OK')" "<repo-relative-path>" "<exact-download-path>" "<SHA-shown-by-board>"
```

Това проверява байтовете; schema/approval проверката остава отделна. Две сглобявания от едни входове трябва да дадат байт-еднакъв резултат.

**S16. Ръбът вече е правилно дефиниран.** D7 изисква `edge=max(50,precision_m)` в EPSG:32635. При Wikimapia минимум 100 m фиксиран ръб 50 m би нарушил съществуващия договор. Фикстура: празен безспорен ред, точка и тяло на 75 m навътре, `precision_m=100` → `edge_pending`, без присвояване; на повече от 100 m и без други пречки → допустимо `written`. [ADR:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50)

Конфликтните класове са назовани, но `classify(code)==field` не доказва вида на **изворния полигон**: район може погрешно да получи валиден квартален code и да премине проверката. Минималното правило е подписан source-kind crosswalk, точно един избран source Feature за code, забранено двойно присвояване на една геометрия към несравними кодове; неразрешено двусмислие → без писане. Нормализираното заглавие не решава „Чайка“ и двата „Младост“. Родител/дете се допуска само по подписано и геометрично проверено родство. [A2:31](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:31), [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [ADR:52](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52)

**S17. „Около 150“ не е приемно число.** Декларираните 159 са допустима популация, не обещана печалба. S7 вече изисква подредени идентичности и целия публичен ред. [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [A1:25](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25)

Задължителни фикстури:

- `street_collision`: нов квартален токен не премахва немаркирана A3-street улица; ADDRESS остава байт-равен.
- `district_retention`: нов `quarter` не губи валидни резултати от търсене по район.
- `mladost_kind_collision`: районният полигон не добавя чужди редове към „училище младост 2“.
- `parent_child`: „възраждане 3“ избира детето; „възраждане“ — родителя и регистрираните деца.
- `order_identity`: запазва подредените `bundle:ordinal`; смяна на branch е отделна делта.
- `client_cache_matrix`: old/new client × old/new/mixed bundles × cold/warm cache.

Регресионните фикстури трябва да падат върху нарочно счупен кандидат; положителната „училище св св константин и елена“ трябва да премине към подписаната идентичност на Френското училище след поправката. Новите печалби не оправдават загуба на валиден стар резултат. [A1:28](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:28), [A1:38](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:38), [V2:168](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:168)

**S18. RMS не доказва точността на линията.** Остатъкът върху използваните центроиди измерва fit-а. Не включва грешното съответствие, растеризацията, сегментацията и поведението между контролите. `2 pt/pixel` не дава метри без метричния affine Jacobian.

Фикстурата rms 11/`precision_m=50` **минава**: `max(50,3×11)=50`. Отрицателен пример е rms 20/precision 50. [A2:27](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:27), [A2:33](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:33)

`max(50,3*rms,max_residual+raster_error)` е предпазен минимум, не установена точност. Независимата проверка трябва да сравнява 20 предварително избрани точки по периметъра с доказано **същата** граница и да отчита `dmax/p95`. Най-близкият произволен KAIS parcel edge може да даде фалшив успех. Извадката проверява извадката; без независима референция реконструкцията остава свидетел. MR→code подписът решава идентичност, не точност.

**S19. Присъди по раздели:**

| Раздел | Присъда | Необходима поправка |
|---|---|---|
| §2 | НЕГОДНО | Source-kind проверка, еднозначен crosswalk, честен precision floor и работещи фикстури. |
| §4 | НЕГОДНО | Затворена decisions схема; конкретни write-set/изпълнител/съобщение; потвърждаване → decisions commit → assembly. |
| §5 | НЕГОДНО | Правилна биекция, проверена approval chain; G18 да проверява и разрешените подложки; G28 да допуска само разрешаващ verdict. |
| §6 | НЕГОДНО | Предварителен coordinate-only ход с G9, после М2-3 и борд. |

§4 само обещава write-set-овете. §6 има цикъл: мярката **преди борда** чака P8-а, който V2 поставя **след Г2**. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [A2:85](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:85), [V2:149](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:149)

Преди Петър да подпише, договорът трябва да има изпълним ред без цикли, проверима SHA/approval chain, поименни отрицателни фикстури и изрично приет обхват на непокритите квартали.
tokens used
65,925
**НЕГОДНО за изпълнение в сегашния вид.** Прегледът е read-only; файлове не са променяни. Аритметиката е проверена; геометрични тела и browser export не са изпитвани.

Прочетеният документен обхват е следният; `V2`, `A1`, `A2` по-долу означават съответните планове. Извън него няма инспектирани JSON/GeoJSON/PDF или изпълним код.

```text
docs/activeContext.md | 15557 bytes | 132 lines
docs/decisions/010_signed_quarter_boundaries.md | 53242 bytes | 142 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md | 61905 bytes | 264 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | 26249 bytes | 75 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | 30160 bytes | 107 lines
scratch/places_search/granitsi_am2_brief_astra.md | 4915 bytes | 10 lines
```

Декларираният статус на A2 е „за Gate 1“. Всички шест документа преминаха UTF-8 round-trip и проверката за mojibake.

**S14. Мрежата не доказва пълнота.** При зададеното в brief-а подреждане по центрове, 500 m квадратна мрежа гарантира най-близка проба на най-много `500/√2 = 353,55 m` **в покритите клетки**. Дискът е `0,3927 km²`; 100 по-близки центъра могат да изместят квартала — еквивалентна гъстота около `255/km²`. Това е контрапример, не измерена гъстота във Варна. Допълнителните 163 точки не осигуряват горна граница на конкуриращите центрове.

Пропускат се голям полигон с център между пробите, квартал сред плътни сгради, курорт с център извън bbox, компонент на `MultiPolygon`, чийто общ център е далеч, и валиден малък полигон под филтъра `0,04 km²`. API centre, centroid и регистрова точка не са непременно една координата. D7 изрично допуска `MultiPolygon`. [ADR:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50)

Една ограничена проверка: за всеки код без еднозначен кандидат — `count=100` при регистровата точка и четири метрични отмествания ±300 m, включително извън bbox; запазени заявки, отговори и SHA. При 14 кода: максимум 70 заявки, приблизително 32,7 минути. Ненамереното остава „неустановено“. G26 доказва решение за код, а не изчерпателност на Wikimapia. [A2:74](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:74), [V2:142](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:142)

**S15. Решенията нямат достатъчно определен договор.** Минимумът е:

- `_meta`: `schema_version`, `board_sha256`, подписан `registry_sha256`, manifest с SHA на всички входове, версия на канонизацията;
- ред: `code`, `choice ∈ {official,reconstructed,wikimapia,none,deferred}`, квалифициран source Feature ID, geometry SHA, подписан crosswalk, `reason`, `decided_by`, неизменен `decided_at`;
- само за Wikimapia: `wm_id`, пълният `wm_polygon_sha256`; при останалите — `null`.

Общ `data_sha256` е достатъчен само ако обвързва целия manifest. Повтарянето на page/data SHA във всеки ред е излишно. `fetched_at` и `decided_at` означават различни събития. Raw snapshot SHA, canonical geometry SHA и delivery SHA трябва да имат отделни определения; за `MultiPolygon` липсват правила за подредбата на компонентите и вътрешните пръстени. [ADR:38](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:38), [A2:59](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:59)

**Пряко противоречие:** „всеки Feature има ред … и обратно“ отхвърля валиден `deferred`, който няма Feature. Правилната биекция е решения ↔ трите множества: `official/reconstructed/wikimapia→polygon`, `none→no_boundary` с null geometry, `deferred→_meta.deferred`. G26 изпуска `reconstructed`. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [ADR:44](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:44)

Два записани `decisions_sha256` не доказват одобрение. Нужни са прочит на точния Petar-committed blob, сверка към подписан въпрос с видимо `тяло`, и проверка `code→source ID→frozen geometry`. G25 трябва да отхвърля подменен `wm_id`, дори геометричният SHA да съвпада. [ADR:42](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:42)

На Windows преименуване или `(1)` само не променя SHA; опасностите са избран стар download, редакторна BOM/CRLF конверсия и Git EOL преобразуване. При предложена канонизация UTF-8 без BOM, sorted keys, compact JSON и финален LF, след staging изпълнителят пуска следното с трите реални аргумента:

```powershell
python -c "import sys,json,hashlib,subprocess,pathlib; b=pathlib.Path(sys.argv[2]).read_bytes(); j=json.loads(b.decode('utf-8')); assert b==(json.dumps(j,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8'); assert b==subprocess.check_output(['git','cat-file','blob',':'+sys.argv[1]]); assert hashlib.sha256(b).hexdigest()==sys.argv[3]; print('OK')" "<repo-relative-path>" "<exact-download-path>" "<SHA-shown-by-board>"
```

Това проверява байтовете; schema/approval проверката остава отделна. Две сглобявания от едни входове трябва да дадат байт-еднакъв резултат.

**S16. Ръбът вече е правилно дефиниран.** D7 изисква `edge=max(50,precision_m)` в EPSG:32635. При Wikimapia минимум 100 m фиксиран ръб 50 m би нарушил съществуващия договор. Фикстура: празен безспорен ред, точка и тяло на 75 m навътре, `precision_m=100` → `edge_pending`, без присвояване; на повече от 100 m и без други пречки → допустимо `written`. [ADR:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50)

Конфликтните класове са назовани, но `classify(code)==field` не доказва вида на **изворния полигон**: район може погрешно да получи валиден квартален code и да премине проверката. Минималното правило е подписан source-kind crosswalk, точно един избран source Feature за code, забранено двойно присвояване на една геометрия към несравними кодове; неразрешено двусмислие → без писане. Нормализираното заглавие не решава „Чайка“ и двата „Младост“. Родител/дете се допуска само по подписано и геометрично проверено родство. [A2:31](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:31), [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [ADR:52](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52)

**S17. „Около 150“ не е приемно число.** Декларираните 159 са допустима популация, не обещана печалба. S7 вече изисква подредени идентичности и целия публичен ред. [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [A1:25](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25)

Задължителни фикстури:

- `street_collision`: нов квартален токен не премахва немаркирана A3-street улица; ADDRESS остава байт-равен.
- `district_retention`: нов `quarter` не губи валидни резултати от търсене по район.
- `mladost_kind_collision`: районният полигон не добавя чужди редове към „училище младост 2“.
- `parent_child`: „възраждане 3“ избира детето; „възраждане“ — родителя и регистрираните деца.
- `order_identity`: запазва подредените `bundle:ordinal`; смяна на branch е отделна делта.
- `client_cache_matrix`: old/new client × old/new/mixed bundles × cold/warm cache.

Регресионните фикстури трябва да падат върху нарочно счупен кандидат; положителната „училище св св константин и елена“ трябва да премине към подписаната идентичност на Френското училище след поправката. Новите печалби не оправдават загуба на валиден стар резултат. [A1:28](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:28), [A1:38](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:38), [V2:168](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:168)

**S18. RMS не доказва точността на линията.** Остатъкът върху използваните центроиди измерва fit-а. Не включва грешното съответствие, растеризацията, сегментацията и поведението между контролите. `2 pt/pixel` не дава метри без метричния affine Jacobian.

Фикстурата rms 11/`precision_m=50` **минава**: `max(50,3×11)=50`. Отрицателен пример е rms 20/precision 50. [A2:27](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:27), [A2:33](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:33)

`max(50,3*rms,max_residual+raster_error)` е предпазен минимум, не установена точност. Независимата проверка трябва да сравнява 20 предварително избрани точки по периметъра с доказано **същата** граница и да отчита `dmax/p95`. Най-близкият произволен KAIS parcel edge може да даде фалшив успех. Извадката проверява извадката; без независима референция реконструкцията остава свидетел. MR→code подписът решава идентичност, не точност.

**S19. Присъди по раздели:**

| Раздел | Присъда | Необходима поправка |
|---|---|---|
| §2 | НЕГОДНО | Source-kind проверка, еднозначен crosswalk, честен precision floor и работещи фикстури. |
| §4 | НЕГОДНО | Затворена decisions схема; конкретни write-set/изпълнител/съобщение; потвърждаване → decisions commit → assembly. |
| §5 | НЕГОДНО | Правилна биекция, проверена approval chain; G18 да проверява и разрешените подложки; G28 да допуска само разрешаващ verdict. |
| §6 | НЕГОДНО | Предварителен coordinate-only ход с G9, после М2-3 и борд. |

§4 само обещава write-set-овете. §6 има цикъл: мярката **преди борда** чака P8-а, който V2 поставя **след Г2**. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [A2:85](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:85), [V2:149](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:149)

Преди Петър да подпише, договорът трябва да има изпълним ред без цикли, проверима SHA/approval chain, поименни отрицателни фикстури и изрично приет обхват на непокритите квартали.
