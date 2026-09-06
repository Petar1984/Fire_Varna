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
session id: 01a0755d-5441-76f1-88c7-47775b5f98eb
--------
user
S21 — REFUTE the night-shift plan docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md (v1, unsigned; Part A = read-only measures Н0–Н5, Part B = results Б1–Б4 gated on Petar signing decision block Б0 in §6). Lens: MECHANICS, EXECUTABILITY TONIGHT, REGRESSIONS. Read: the plan; docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md (rev 2б); docs/decisions/010_signed_quarter_boundaries.md (D1, D4, D6, D7, D13, D16, G4, G17); the state file docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md; Fire_Varna index.html around the closed lists QUARTER_SRC / QUARTER_CODES / LOCALITY_CODES / DISTRICT_CODES / PLACES_CACHE and validatePlaces2; tests/ and gates/ (run_gates, release/sign, expectations.json); scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json (structure only). You may ALSO read C:/git/varna_3d (private repo on this machine): src/fire_varna_locations.py (LEDGER, the channels), src/qa_fire_varna_places_export.py (META_KEYS, row keys), src/place_identity.py, gates/release.py, data/fire_varna_location_inputs.json — read-only. Questions: (1) Is every gate in Part A and Part B a command that can run TONIGHT with the files on disk, with a negative fixture that fails? Name each that cannot. (2) Б2: the new dated ledger + LEDGER path change + G17 against  — is base_rev definable tonight (the ledger has no _meta.base_rev)? Give the exact definition or say STOP. (3) Б2 coordinates: D10 has 0/375 lat/lon — where does today's channel get coordinates for the export? If nowhere, Б2 is a measure only — say so. (4) Б3: QUARTER_CODES +41, PLACES_CACHE v7, the 10th _meta key, expectations.json, release/sign — list the exact edit points and the order that keeps validatePlaces2 from silently emptying places2; name the fixture that proves a foreign code fails LOUDLY. (5) D16/G4: the executor stages data/quarters_signed.geojson for Petar's commit while Б2 reads it by sha — does anything downstream (pins, expectations) break because the blob is uncommitted? (6) Parent/child: Б0 т. 9 signs 10 nested pairs as facts — is the 'smallest containing wins' rule + 'undeclared double containment → disputed' consistent and total (every place gets exactly one outcome)? (7) What is the realistic order and the STOP points so that a red gate at 03:00 leaves all three repos green for Petar's morning push? Verdict ГОДНО/НЕГОДНО for A and B separately, with named fixes; at most 1400 words; Bulgarian with English identifiers; cite file:line.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя плана спрямо файловете и изпълнимите gates на диска. Ще разделя проверката между механиката на release/sign, frontend регресиите и собствените ми проверки на ledger, координатите и реда за изпълнение. Всичко остава read-only.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git status -sb; Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 100" in C:\git\Fire_Varna
 succeeded in 141ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 38, behind 2]
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
?? scratch/places_search/granitsi_brief_astra.md
?? scratch/places_search/granitsi_brief_kimi.md
?? scratch/places_search/granitsi_night_astra_S21_06.09.md
?? scratch/places_search/granitsi_night_kimi_K22_06.09.md
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
paths=[Path('docs/activeContext.md'),Path('docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'),Path('docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md'),Path('docs/decisions/010_signed_quarter_boundaries.md'),Path('docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md'),Path('scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json')]
for f in sorted(paths,key=lambda p:str(p)):
 print(f'{f.as_posix()} | exists={f.exists()} | bytes={f.stat().st_size if f.exists() else 0} | lines={len(f.read_text(encoding=\"utf-8\").splitlines()) if f.exists() else 0}')
for f in sorted([Path('C:/git/varna_3d')/s for s in ['AGENTS.md','src/fire_varna_locations.py','src/qa_fire_varna_places_export.py','src/place_identity.py','gates/release.py','data/fire_varna_location_inputs.json']]):
 print(f'{f.as_posix()} | exists={f.exists()} | bytes={f.stat().st_size if f.exists() else 0} | lines={len(f.read_text(encoding=\"utf-8\").splitlines()) if f.exists() else 0}')
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 succeeded in 0ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
p=Path('docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md')
for n,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
 if 1<=n<=150: print(f'{n}: {s}')
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 exited 1 in 18ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding=[System.Text.UTF8Encoding]::new()
@'"'
from pathlib import Path
for f in sorted([Path('docs/plans')/s for s in ['ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md','ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md']]+[Path('docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md')]):
 print(f'{f.as_posix()} | exists={f.exists()} | bytes={f.stat().st_size if f.exists() else 0} | lines={len(f.read_text(encoding=\"utf-8\").splitlines()) if f.exists() else 0}')
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 succeeded in 9ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' -Encoding UTF8 | Select-Object -First 150 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/varna_3d/AGENTS.md' -Encoding UTF8 -TotalCount 150" in C:\git\Fire_Varna
 succeeded in 0ms:
# AGENTS.md — governance for Varna 3D

Same pipeline as `Varna_buildings`. This file is the short version; the
machine-wide invariants live in `~/.claude/CLAUDE.md` and take precedence over
anything here.

## What this repo is

Varna 3D sits ABOVE `Varna_buildings` and `Fire_Varna`: they decide *where the
address is*, this one decides *what the city looks like*. Nothing that already
exists is touched — Varna 3D is a consumer of their outputs, not their heir.
(Translated from `README.md`, lines 5–7, which are in Bulgarian.)

## The trunk

- Working branch: `rezhimi`. Every commit of the running cycles lands there.
- GitHub's default branch is `main`
  (`git symbolic-ref refs/remotes/origin/HEAD`). It is a strict ancestor of
  `rezhimi` (`git merge-base --is-ancestor main rezhimi`, plus a non-zero
  `git rev-list --count main..rezhimi`); the profile-ordering plan of
  01.09.2026 (`C:\git\plan.md` today; LOT 4 brings it into `docs/plans/`)
  brings `main` level with `origin/rezhimi` in its LOT 3.
- Which of the two is the trunk from here on is Petar's open question В-1 of
  that plan. Until he answers: work on `rezhimi`, push nothing (hard rule 1).

## Entry point

`docs/activeContext.md` — the state of the repo, one truth per document. LOT 5
of the 01.09 plan writes it and freezes the chronicle. Until then the state is
`СЪСТОЯНИЕ.md` in the repo root, which LOT 4 moves to `docs/СЪСТОЯНИЕ.md`.
Read whichever of the two exists before anything else here.

## Live numbers

**No state number enters this file** — no record counts, no file counts, no
commit counts, no byte sizes, no "last updated" dates. Every one of them lives
in the entry point above. Until LOT 5 the entry point is a dated chronicle, not
a number-to-command table: a number read from it is re-measured with the
command beside it (hard rule 5). Numbers that are **rules** — an EPSG code, a
read cap, a byte ceiling — stay here, because a rule is not state.

## Roles

| Role | Who | Does | Never |
|---|---|---|---|
| **Planner** | Claude Code (read-only) | measures, architects, drafts `ПЛАН_<тема>.md` (there is no `plan.md` here — one plan file per theme; `git ls-files \| grep "ПЛАН_"`) | edits, commits |
| **Researcher** | Sol (`codex exec`, via `C:\git\bridge`) | external evidence with citations | decides |
| **Executor** | Claude Code | implements a signed plan, local commits | plans, expands scope, pushes |
| **Auditor** | Claude Code (read-only, adversarial) | refutes the Executor's claims | edits |
| **Orchestrator** | **Petar** | signs plans (Gate 1), reviews diffs (Gate 2), pushes | — |

## Hard rules

1. **Never `git push`.** Petar pushes. No exceptions, no "just this once".
2. **No cadastral identifiers leave `C:\git\m6000_private`.** A 3D scene carries
   geometry + floor counts, never `cadnum`. Any scene that could be shared is
   anonymous by construction: the `cadnum` column is never read into the mesh,
   and the `no_cadastral_identifier` entry in the gates of `src/build_lod1.py`
   records that as a declared invariant (`"pass": True`), not as a check —
   the check over everything git tracks is `python src/qa_no_cad_ids.py`.
   Tracked evidence files were not anonymous: the audit of 21.08
   found the rule broken there, and `src/scrub_cad_ids.py` cleaned them
   afterwards. The code exceptions it deliberately leaves are named in its own
   docstring.
3. **BGS2005 vs WGS84 must be explicit** in every coordinate that touches disk.
   KAIS is BGS2005 (≈EPSG:7801); web output is WGS84; metric work is EPSG:32635.
   Mixing them silently is the single largest correctness risk inherited from
   `Varna_buildings`.
4. **Phase 0 (licensing) gates everything.** No mesh is built for public use
   before the licence question is answered in writing with citations.
5. **Measure before you claim.** Every number in a document carries the date it
   was measured and the command that produced it.
6. **Never modify `Varna_buildings` or `Fire_Varna` from here.** This project
   reads their outputs. Changes there go through their own pipelines.
7. **Fail loud.** A reprojection that lands outside the Varna bounding box stops
   the build; it does not write output and hope.

## Gates

- **Gate 1 — signed plan.** Petar signs before any build step runs.
- **Gate 2 — diff review.** Petar reads the diff before it is committed upstream.
- **Acceptance is machine-checkable.** "Looks right" is not a gate. The gates
  `src/build_lod1.py` evaluates before a single byte is written are
  `building_count`, `reprojection_in_varna_bbox`, `no_cadastral_identifier`,
  `built_volume_Mm3`, `tallest_building_m` and `no_osm_artifacts`, plus the
  terrain gate of the run — `seated_on_terrain` and
  `terrain_covers_every_building` under `--seat`, otherwise `mesh_sits_on_zero`
  (list them from the source, not from memory:
  `awk '/^    gates = \{/{f=1} /^    metrics/{f=0} f' src/build_lod1.py | grep -oE '^        "[A-Za-z0-9_]+"|gates\["[A-Za-z0-9_]+"\]' | grep -oE '"[A-Za-z0-9_]+"' | sort -u`).
  One failing gate stops the build and writes no product — only
  `varna_lod1_metrics.json` with the verdicts (`grep -n -A2 'STOPPED' src/build_lod1.py`).
  Vertex count is **not** a gate — it is only reported (in `metrics` and in the console log)
  (`git grep -n -iE 'vertex|vertices' -- src/build_lod1.py`) — and a
  reprojection-residual check does not exist at all
  (`git grep -n -i -E 'reproject.{0,25}residual|residual.{0,25}reproject' -- src`
  returns nothing).

## The repo's gates

These scripts guard the repo itself, not the model of the city. Names and what
they protect only — the counts they print are state and live in the entry point.

- `src/qa_no_cad_ids.py` — the gate behind hard rule 2: ZERO cadastral
  identifiers in every file git tracks, not only in the published output. The
  exceptions are enumerated with their reason in its `ALLOW` block.
- `src/qa_no_extrude.py` — judges `data/no_extrude_verdicts.json`, the one
  place that tells the web page which cadastral bodies NOT to draw; the three
  classes of verdict are judged separately, by the strength of their grounds.
- `src/scrub_cad_ids.py` — a cleaner, not a gate: it replaces a cadastral
  identifier in tracked evidence files with a per-file serial while keeping the
  audit trail. Without `--apply` it only reports. It never touches code.
- The build's own gates are in `src/build_lod1.py` and are evaluated before a
  single byte is written (see § Gates).
- The rest of the family: `ls src/qa_*.py`.

## Scratch and artefacts

- Generated meshes, DEM tiles, and textures are **never** committed. See
  `.gitignore`. Two families were force-added past those rules and are tracked
  today: `.png` probe screenshots under `scratch/web_probes/`, and the tracked
  reports, the dry-run JSON files and the dry-run GeoJSON under `output/` (`git ls-files | grep -icE "\.png$"`;
  `git ls-files output`). `git add -f` is a signed decision, not a routine
  command; how many there are is state and lives in the entry point.
- Session-temp scripts start with `_` and are meant to be deleted by the
  session that made them once their findings are written down. The tree does
  not match that rule: `_`-files accumulate, and a large batch of them entered
  git as evidence with the LOT 1 commit of the 01.09 plan
  (`git log --format='%h %s' --grep='ЛОТ 1 (загуба)'`). Today's
  count: `git ls-files | awk -F/ '{print $NF}' | grep -c "^_"`.

## Where the documents live

The project's documents live under `docs/` (LOT 4 of the 01.09 plan moved them
there from the repo root with `git mv`, so history follows — `git log --follow <file>`);
working material under `scratch/` and generated reports under `output/` stay where
they are. The root keeps `README.md`, `AGENTS.md`, `CLAUDE.md`, `DATA.md` and
`ПЛАН_П2в_терена.md` (`git ls-files | grep -E '^[^/]+\.md$'`); `docs/Наредба_7_2003_МРРБ.pdf`
sits beside the sub-folders (`ls docs/`):

| Pattern | Lives in |
|---|---|
| `ПЛАН_*.md` | `docs/plans/` |
| `ДОКЛАД_*.md` | `docs/audits/` |
| `ПРОМПТ_*.md` | `docs/sessions/` |
| research write-ups | `docs/research/` |
| decision documents | `docs/decisions/` (index: `docs/decisions/README.md`) |
| `МЯРКА_*.md` | `docs/measurement/` |
| `СЪСТОЯНИЕ.md` | `docs/` |

Under Р-9 (а) of the 01.09 plan (signed 02.09), `ПЛАН_П2в_терена.md` stays in the root: it is pipeline input, read by

 succeeded in 0ms:
1: # ПЛАН НОЩНА СМЯНА · Границите (06→07.09.2026) — v1 за подпис
2: 
3: **Клас: 🔴 Архитектурен. Статус: НЕПОДПИСАН.** Нищо оттук не тръгва без думата на Петър. Топология: планировчик → три вътрешни оборвания (Opus) → Кими + Astra → подпис → изпълнител → независим одитор на всеки лот → Петър.
4: 
5: **Строеж на плана.** **ЧАСТ А** (лотове Н0–Н5) е нощ от **мерки** — тръгва при подпис на плана и не иска нито едно ново решение; така е след трите вътрешни оборвания (D1 е затворен набор от 21 полета; D2 заключва метода „по улици“; D13 затворени публични набори; G17). **ЧАСТ Б** (лотове Б1–Б4) е нощ от **резултати** — подписан файл с граници, присвояване на квартал, търсене по квартал — и тръгва САМО ако Петър подпише тази вечер и **блока решения Б0** (§6), защото всяко от тях е негово по ADR 010 и амандамент №2. Ако Б0 не е подписан, нощта е само А. Ако Б0 е подписан, А се изпълнява първа (числата ѝ де-рискуват Б), после Б.
6: 
7: **Принципът на Петър за данните (06.09, вечерта):** „дори имената на адресите да лъжат — геокоординатите не лъжат“. Кварталът на място се определя от координатата му спрямо потвърдените полигони; адресните низове са свидетели, не съдии; спор (записан ≠ полигон) е ред в леджер, никога презапис. Раздел §7 „Конфликти и нормализация“ прави от това мярка.
8: 
9: **Водещата промяна спрямо чернова 1:** тази нощ НЕ се ражда канонична подписана геометрия. Нощта произвежда **мерки и кандидати** — никой файл не се казва `quarters_signed.geojson` и никой не твърди „подписано“. Причината е измерена: D1 (`docs/decisions/010_signed_quarter_boundaries.md:38`) е ЗАТВОРЕН набор от 21 полета с „липсващо поле = STOP“, а внесен уикимапийски полигон няма `drawn_by/drawn_at/basemap/viewport/screenshot_sha256/approval_digest/witnesses`. Схемата за ВНЕСЕНА геометрия е амандамент за подпис, не решение на изпълнител.
10: 
11: ## 0 · Червени редове (важат за всеки лот, без изключение)
12: 
13: 1. **Агентите не пушат.** Никога, с никакъв флаг, без `--no-verify`.
14: 2. **Нула геометрия в проследен файл на Fire_Varna.** Публично пътуват само име, код и картата за атрибуция.
15: 3. **`Varna_buildings/config/quarter_registry.json` не се пипа.** Ваялар→alias, Евксиноград/Траката, Цветен квартал, 16-те без решение, липсващите `parents` — всичко отива в сутрешния списък (§5).
16: 4. **Написан квартал не се променя** (D18/G17). Спорът е ред в леджера, не редакция.
17: 5. **Малки, обратими комити**, изчерпателен write-set, дословно съобщение, автор `Claude Executor <executor@local>`; подписаната геометрия и решенията чакат комит на `Petar1984` (D16, G4 е fail-closed).
18: 6. **Всеки гейт е команда с изход ≠ 0 и с отрицателна фикстура, която ТРЯБВА да падне.** Паднал гейт СПИРА лота; нощта продължава само с лотовете, които не зависят от него.
19: 7. **Само Opus** — изпълнители и одитори; всеки `agent()` с `model: "opus"`.
20: 8. **Одиторът е друг агент** (read-only) за всеки лот. Самопотвърждение не е доказателство.
21: 
22: **Две обявени отклонения (искат подпис заедно с плана):** (а) `ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md §0.1` иска един лот в движение до пуш — измерено: Fire_Varna 37 ahead, varna_3d 41, Varna_buildings 1; нощта отваря шест лота в три репа, всичките мерки. (б) `§0.3` иска Kimi и Astra преди изпълнение — този план минава през Astra преди първия ред код; при недостъпност нощта се свива до Н0 и Н4.
23: 
24: ## 1 · Мярка преди плана (прочетено тази вечер, read-only)
25: 
26: - `granitsi_decisions_3_2026-09-06_proba.json`: 68 реда, `choice` = wikimapia 60 · deferred 6 · declared_streets 1 · alias_of 1. Ключове на реда: code, display, kind, choice, wm_id, wm_polygon_sha256, wm_title, reason, decided_by, decided_at. **`precision_m` — 0/68.** Договорът в амандамент №2 §4 не познава `declared_streets` и `alias_of` → G26 се разширява (обявено отклонение).
27: - Файлът е **ПРОСЛЕДЕН И КОМИТНАТ ОТ АГЕНТ**: `b6e627d`, автор `Claude Architect`. Значи състоянието не е „некомитнат“, а `agent_committed_proba` — амандамент №2 §4 иска блоб, комитнат от Петър.
28: - `wm_polygon_sha256` в решенията е **СУРОВ** хеш на компактния `{"type","coordinates"}`, не канонизацията по D1 (6 знака, CCW, ротация, подредба по площ). Мерено: `abatko` = `c2e0662d…`, `mladost2` = `80f40ee1…`.
29: - `agkk_au5_varna.geojson`: 5 Feature-а **без `properties`**; ключове `nationalcode` ("10135-01"…"10135-05"), `upper`, `area_km2`, `n_places`, `district_codes_inside`. **Словесен код на район в този файл НЯМА.** Словесните са `index.html:6315` (`DISTRICT_CODES`).
30: - `index.html:6313` `QUARTER_SRC`, `:6317-6321` `QUARTER_CODES` = **затворен списък от 20 кода**; **41 от 61-те потвърдени кода ги няма** в него, а `morska_gradina`, `sveti_nikola`, `zelenika` са в `LOCALITY_CODES` (`:6322`) — друг клас. Непознат код умира мълчаливо по същия път като непознат `src`.
31: - `varna_3d/src/fire_varna_locations.py:76`: `LEDGER = scratch/refactor/_addr/lot1v_locations_375.json` — **проследен**; той е базата на G17. Всеки прогон на канала го презаписва.
32: - `_meta.base_rev` **не съществува** в днешния леджер, а D18/G17 (`ADR:72,:131`) четат `git show <base_rev>:…`. Променливата е недефинирана.
33: - `varna_3d/.gitignore:4` `data/*`, `:23` `*.geojson` → `data/place_identity.json` е игнориран; `place_identity.py:602` чете предишния файл, `:1261` го презаписва — това е СЪСТОЯНИЕ, не производна.
34: - `web/varna_buildings_info.json` е таблица без геометрия; телата са `web/varna_buildings_3d.geojson` (29.9 MB).
35: - Вложеност между 60-те полигона: **10 вложени двойки, 7 НЕДЕКЛАРИРАНИ** (rozova_dolina⊂asparuhovo, kokardzha_generic⊂izgrev_kv, abatko⊂kk_konstantin_elena, saltanat⊂morska_gradina, vazrazhdane1/2/3⊂vazrazhdane). `parents` в регистъра са **дисплей-низове** и има само 6; `borovets` няма потвърден полигон.
36: - `varna_3d` = PRIVATE (`gh` не е в PATH; работи с `C:\Program Files\GitHub CLI\gh.exe`). `ФАЗА_0_лицензи.md:4` = „⏳ чака подпис“ → G21 държи заключено.
37: - Шестте фикстури S17 ги няма в `Fire_Varna/tests/`; днешният набор е 310 теста, зелен.
38: 
39: ## 2 · Лотовете
40: 
41: | Лот | Репо | Изчерпателен write-set | Дословно съобщение | Откат |
42: |---|---|---|---|---|
43: | Н0 пинове | Fire_Varna | `scratch/places_search/noshtna_pins_06.09.json`, `scratch/places_search/qa_night_pins.py` | `measure: pin night-shift inputs, base_rev and ignore proofs (06.09)` | `git revert <sha>` |
44: | Н1 кандидат | varna_3d | `src/build_quarters_candidate.py`, `src/qa_quarters_candidate.py` (изходът `scratch/granitsi/quarters_candidate_07.09.geojson` е игнориран по `.gitignore:23` и НЕ се стейджва) | `measure: candidate quarter geometry from pinned decisions (no signed artifact)` | `git revert <sha>` + изтриване на изхода по назован път |
45: | Н2-0 координати | varna_3d | `src/measure_place_coords.py` (изход `scratch/granitsi/place_coords_07.09.json`, непроследен) | `measure: derive place coordinates read-only, no identity mutation` | същото |
46: | Н2 присвояване | varna_3d | `src/measure_polygon_assign.py` (изход `scratch/granitsi/assign_measure_07.09.json`) | `measure: polygon-vs-written quarter, ledger untouched` | същото |
47: | Н3-а фикстури | Fire_Varna | `tests/test_granitsi_fixtures.py`, `scratch/places_search/granitsi_fixtures_06.09.json` | `tests: five S17 fixtures against today's frozen behaviour` | `git revert <sha>` |
48: | Н4 сгради | varna_3d | `src/measure_kais_quar_vs_polygons.py` | `measure: KAIS quar vs candidate polygons, read-only` | `git revert <sha>` |
49: | Н5 доклад | Fire_Varna | `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` | `docs: night-shift report 07.09` | `git revert <sha>` |
50: 
51: Зависимости: Н0 → всичко. Н1 → Н2, Н4. Н2-0 → Н2. Н3-а е независим. Пада ли Н1 — Н2 и Н4 отпадат, Н3-а и Н5 продължават.
52: 
53: ## 3 · Лот по лот
54: 
55: ### Н0 · Предусловия и пинове
56: `noshtna_pins_06.09.json` (нула координати) пинва `sha256` на: решенията (**плюс комита `b6e627d` и автора `Claude Architect`**), `frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson` (`b53a3322…`) **и** `granitsi_preview_05.09/wikimapia_quarters_frozen_2026-09-06_v2.geojson` — двете копия са байт-еднакви, **веригата се доказва по sha, не по име**; суровия снапшот; `m2_1_candidates_v2.json` (`1331130e…`, обявен вход на решенията); `wikimapia_extra_2026-09-06.geojson` (Евксиноград 5729429, **извън обявения frozen манифест** — записва се изрично); `mladost2_streets_proposal.geojson`; `agkk_au5_varna.geojson`; `quarter_registry.json`; `lot1v_locations_375.json`; **`base_rev` = точният комит, от който се чете леджер-блобът**. Записва се и, че `based_on` предшественикът `granitsi_decisions_2_…` липсва на диска — веригата назад е скъсана (ред в доклада, не мълчание). Плюс `git rev-list --count origin/…` за трите репа и **G19**: `"C:\Program Files\GitHub CLI\gh.exe" repo view varna_3d --json visibility` → трябва `PRIVATE`; празен изход или `PUBLIC` = СТОП за целия varna_3d фронт.
57: 
58: **Гейт Н0 (червен).** `qa_night_pins.py` преизчислява всеки sha и повтаря git-проверките. Фикстури: обърнат hex знак → ≠ 0; **`git add -f` върху копие на geometry-файл в еднократно worktree → гейтът за G29 трябва да падне ТАМ и да е зелен в реалното дърво** (`git add -n` е dry-run и не доказва нищо); подменено ИМЕ при съвпадащ sha → зелено, подменен sha → червено.
59: 
60: ### Н1 · Кандидат-геометрия (varna_3d, частно, НЕподписано)
61: Един Feature на **уикимапийски** потвърден код: **60 кода** (59 + Евксиноград). **Младост 2 НЕ влиза** — D2 (`ADR:40`) казва „по улици“ → ЗАКЛЮЧЕН ВИНАГИ, отключва се само с изричен подписан ключ, а G1 има точно тази отрицателна фикстура; излиза като `deferred` и поименно в §5. Полета: `code`, `name`, `kind`, `source: "wikimapia"`, `wm_id`, **`raw_geometry_sha256`** (пренесен от решенията) **и** `wm_polygon_sha256_d1` (пресметнат по канонизацията на D1) — двете правила се записват отделно, разликата е обявено отклонение за Петър; `url`, `fetched_at`, `confirmed_by/at`, `chosen_reason`; **`licence` дословно** по амандамент №2 §3.8 и К21 т. 3–4: `"CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)"` + етикета за доброволци/неофициален извор/URL на условията/дата; `attribution` низът; `parent` от регистъра след **явна стъпка дисплей→код с гейт** (непознат дисплей = червено), а за код с родител без полигон (`borovets_sever`, `borovets_yug`) — `parent_geometry_check: "няма родителски полигон"`. **`precision_m` НЕ се измисля** (0/68 в решенията) — Feature-ът носи `precision_m: null` и лотът не го замества с литерал. **`district` НЕ се пише** (виж §5 т. 4); вместо това мярка: за всеки кандидат кой `nationalcode` го съдържа. `_meta`: `artifact_class: "candidate_not_signed"`, `decisions_state: "agent_committed_proba (b6e627d, Claude Architect)"`, манифест на входовете, `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict, position}`, `registry_pending` с **16-те кода без решение поименно**.
62: 
63: **Гейт Н1 (червен).** Предгейтове: **G19** (частно репо), **G3** (`qa_no_cad_ids.py` — задължителен преди всеки комит по CLAUDE.md на varna_3d). Фикстури: подменен връх при непроменен sha (за ВСЕКИ от двата хеш-ключа поотделно, всеки срещу своя източник) · подменен `wm_id` · `deferred` код с Feature и Feature без ред · **жилищен код от регистъра без ред в решенията → ✗, поименно** · координата във файла с решения · липсващ ред за атрибуция · **не-уикимапийски ред с непразно `wm_*` → ✗** · **входен Feature със `source: "declared_local_knowledge"` → ✗** (етикетът е отменен от амандамент №2 §3.7) · голо „CC BY-SA“ или липсващ `terms` → ✗ · една геометрия към два несравними кода · BOM/CRLF/несортирани ключове · две сглобявания дават байт-еднакъв файл · **`_meta.artifact_class ≠ "candidate_not_signed"` → ✗**.
64: 
65: ### Н2-0 · Координати — МЯРКА, без мутация
66: `place_identity.json` **не се докосва** (игнориран, състояние, генераторът чете сам себе си). Отделен скрипт извежда `place_id → lat/lon` от същите връзки, които идентичността вече носи (`site_id`/`kais_i` → представителна точка на тяло в `web/varna_buildings_3d.geojson`), и пише САМО в `scratch/granitsi/place_coords_07.09.json`. Място без връзка → `no_coord`, брои се, не се гади. **Гейт:** 375 реда; всяка координата в кутията 43.13–43.35 / 27.65–28.10; sha256 на `data/place_identity.json` идентичен преди и след. Фикстури: координата извън кутията → ✗; липсващ `place_id` → ✗.
67: 
68: ### Н2 · Присвояване — САМО ЧИСЛА, нула запис
69: Скриптът чете **блоба** `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json` (не работния файл), кандидат-полигоните и координатите, и брои. `fire_varna_locations.py` **не се редактира**; леджерът **не се презаписва**. Правила на мярката: празен квартал + точно един полигон → „би получил“; **място в ≥ 2 полигона БЕЗ декларирано родство → `disputed`** (7-те недекларирани вложености); „най-малкият печели, детето преди родителя“ важи САМО за 6-те декларирани двойки; написан ≠ полигон → `disputed`; **няма полигон → редът си остава с вече написания район** (нищо не се извежда от АГКК); ръбът се брои в **три ленти 50/100/250 m** и трите числа влизат в доклада, докато Петър не подпише `precision_m`. **Гейт:** sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` **идентични преди и след**; `git status --porcelain` в varna_3d празен извън write-set-а.
70: 
71: **Десетият ключ на `_meta` НЕ се специфицира и НЕ се пуска.** Причина: подписваният източник го нарича с ДВЕ имена — амандамент №2 §3.3 (`licence_quarter_boundary`) и §5/G27 (`quarter_attribution`), а фикстурата на G27 отхвърля `_meta` с 11 ключа. Едното трябва да умре с думата на Петър (§5 т. 5).
72: 
73: ### Н3-а · Фикстури (Fire_Varna) — днешното поведение, не приемане
74: Пет фикстури: `street_collision`, `district_retention`, `mladost_kind_collision`, `order_identity`, **`parent_child` върху двойка с ДНЕС регистрирано родство** (`mladost`/`mladost2`) — версията с Възраждане се отлага, защото vazrazhdane1..4 нямат `parents`. **`client_cache_matrix` се отлага** с назована причина: браузърно поведение, а единственият node-изпълнител в `tests/` е `test_data_ascii_mojibake.py`; лотът не назовава втори. Всяка фикстура пада върху нарочно счупен кандидат и мутацията влиза дословно в доклада. **Гейт:** `python -m unittest discover -s tests` (310+ зелени) И `python -m gates.run_gates` без червено — иначе сутрешният пуш на Петър е блокиран от собствената му кука. Записва се изрично: **това фиксира ДНЕШНОТО поведение; утре F13 ще ги направи кандидат-очаквания, не приемане.**
75: 
76: **Н3-б СПИРА (нарочно).** Търсенето по квартал и редът за атрибуция в картончето не тръгват: нов `src` или нов код без подредената тройка на D13 изхвърля 150 места мълчаливо, а измереното е по-лошо от очакваното — **41 кода липсват в `QUARTER_CODES`**, три от тях са днес местности.
77: 
78: ### Н4 · Сградите — САМО мярка
79: Вход: `web/varna_buildings_info.json` (речниково кодирана колона `quar`, `build_places.py:78-96`) + **`web/varna_buildings_3d.geojson`** (телата, поименно) + кандидат-полигоните. За всяка сграда с непразен `quar`: съвпада / не съвпада / няма полигон / само район. Изход: **stdout**; нула кадастрални идентификатори, нула координати. **Гейт (червен):** AST-проверка за извикване на пишеща функция (не grep — `json.dump(obj, fp)`, `Path.open("w")`, `shutil.copy` минават през списък от низове), с фикстура-вариант, който пише през `json.dump` → ✗; плюс sha256-манифест на **всичко под `data/` и `web/`** преди и след и `git status --porcelain` празен.
80: 
81: ### Н5 · Одит и доклад
82: Одитор (Opus, read-only, различен агент) на всеки лот: преизпълнява гейтовете, сверява дифа срещу write-set-а (**всеки допълнителен файл = находка**), проверява автора, съобщението и `git log --format=%an -1 --` върху пътя на решенията срещу `_meta`. **Разделение:** одиторът дава числата, изпълнителят ги записва без да ги тълкува. Докладът носи: числата на Н1, Н2 (по трите ленти), Н3-а (5/5 + доказаните падания + двете отложени), Н4, всички sha, поименния списък на спрелите лотове с причината, и §„Какво прави Петър сутринта“.
83: 
84: **Атрибуция в проследените артефакти:** всеки нощен проследен файл на Fire_Varna, който назовава уикимапийски обект, носи ред за атрибуция по §3.8 (ключ `attribution` в JSON, заглавен ред в MD) — ToS §1.G важи и когато github.com рендерира файла в браузър. Вече комитнатият `granitsi_decisions_3_…json` (60 `wm_id` + заглавия) няма такъв ред: **това е сутрешен дълг, не нощна поправка.**
85: 
86: ## 4 · Нарушения, които спират нощта веднага
87: 
88: Опит за `git push` · геометрия в проследен файл на Fire_Varna · редакция на регистъра · промяна на написан квартал · запис в `lot1v_locations_375.json`, `place_identity.json` или `data/fire_varna_*.json` · файл на име `quarters_signed.geojson` · Feature по метод „по улици“ · нов публичен `src` **или нов квартален КОД** без разширен `QUARTER_CODES` и подредената тройка на D13 · низът `10135` в **публична** доставка (в частния провенанс и в мярката е позволен — иначе АГКК изворът е неназовим) · зелен гейт без падаща отрицателна фикстура.
89: 
90: ## 5 · Сутринта (решенията за Петър, ако Б0 НЕ е подписан тази вечер)
91: 
92: 1. **Схемата за ВНЕСЕНА геометрия** (кои от 21-те полета на D1 отпадат и с какво се заместват) — амандамент, без който няма подписан артефакт.
93: 2. **Кое правило е `wm_polygon_sha256`** — суровият хеш (днешният в решенията) или канонизацията на D1.
94: 3. **Младост 2**: подписан ключ по D2 + лиценз (ODbL, „© OpenStreetMap contributors“) + под на `precision_m` за уличен метод.
95: 4. **Районът**: от нашия `district.code` (375/375 съгласие) с явен `district_src`, или от АГКК — тогава `_meta.source_terms["agkk_inspire_au5"]` се попълва и G22/G23 стават червени предгейтове.
96: 5. **Едно име за десетия ключ** (`licence_quarter_boundary` или `quarter_attribution`) и низът за атрибуция; картата да е независима от извора `{code:{src,url,label,licence}}`, за да носи и ODbL, и АГКК.
97: 6. **`precision_m`** — стойност и довод (от нея зависи кой е `edge_pending`).
98: 7. **Разширяването на `QUARTER_CODES`** с 41-те кода и какво става с `morska_gradina`, `sveti_nikola`, `zelenika`, които днес са местности.
99: 8. **Решенията**: `git mv` на днешния блоб под подписан път (не втори блоб с втора sha) или подпис на днешния път.
100: 9. Регистърът: Ваялар→alias, Евксиноград/Траката, Цветен квартал, `parents` за Възраждане 1–4 и Розова долина, 16-те без решение.
101: 10. Дългове: D10 твърди, че `_check_pins` (`:623-639`) сверява `inputs` — не ги сверява; `_meta.base_rev` липсва в леджера; `granitsi_decisions_3` няма ред за атрибуция.
102: 
103: 
104: ## 6 · ЧАСТ Б — нощ от резултати (тръгва само с подписан блок Б0)
105: 
106: ### Б0 · Блокът решения, който Петър подписва тази вечер (препоръките са на архитекта; всяко „да“ е негово)
107: 1. **Схема за ВНЕСЕНА геометрия (промяна на D1, обявена).** За Feature с `source ∈ {wikimapia, declared_streets}` полетата `drawn_by · drawn_at · basemap · viewport · visible_layers · screenshot_sha256 · approval_digest` са `null` по договор (гейт за взаимна изключителност: или ръка, или внос); `approved_by = "Petar"`, `approved_at = decided_at` от решенията; `signed_by = "Petar"` става валидно с подписа на този план по sha на решенията (т. 8); `witnesses[]` = [{kind: "wikimapia_object", url, fetched_at, raw_response_sha256}] (за Младост 2: {kind: "osm_carriageways", ways по име, fetched: 2026-09-06}); `version: 1`; `note = reason`. Останалите 14 полета на D1 остават задължителни. Препоръка: да.
108: 2. **`wm_polygon_sha256` = канонизацията на D1** (6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; MultiPolygon по правилото на амандамент №2 §4). Суровият хеш от решенията се пренася като `raw_geometry_sha256` и гейтът сверява и двата. Препоръка: да.
109: 3. **Младост 2 — изричен подписан ключ по D2** за `code = mladost2`, `method = "street_bounded_face"`, лиценз `"ODbL © OpenStreetMap contributors"` (осите), `precision_m = 50`, четирите улици дословно в `witnesses`. Само този код; всеки друг Feature с този метод = червено. Препоръка: да.
110: 4. **Районът** се пише от НАШИЯ `district.code` на мястото (375/375 съгласие с АГКК, мерено 05.09), `district_src: "fire_varna_district"`; в Feature-ите на кварталите районът е изведен по представителна точка срещу същите наши 5 района, не от АГКК INSPIRE (G22 остава заключен). Резервата „място без квартал → районът“ пише `quarter = {name: <име на района>, code: <словесният код от DISTRICT_CODES>, src: "DISTRICT_FALLBACK"}`. Препоръка: да.
111: 5. **Десетият ключ на `_meta` се казва `quarter_attribution`** (името в §3.3 на амандамент №2 отпада); форма `{<code>: {src, url, label, licence}}` — независима от извора, носи Wikimapia, ODbL и бъдещи; UI низът: „квартал по Wikimapia.org · обектът“ (двете като връзки) под името на квартала в картончето, само за кодове с запис в картата. Препоръка: да.
112: 6. **`precision_m`**: 100 за `wikimapia`, 50 за `street_bounded_face`; ръб = `max(50, precision_m)` по D7 → `edge_pending`. Препоръка: да.
113: 7. **`QUARTER_CODES` се разширява** с 41-те потвърдени кода, които днес липсват; `morska_gradina`, `sveti_nikola`, `zelenika` остават в `LOCALITY_CODES` (търсят се като местности); `QUARTER_SRC` получава `SIGNED_POLYGON` и `DISTRICT_FALLBACK`; `PLACES_CACHE` v6→v7; пиновете и `expectations.json` — в подредената доставка varna_3d → Fire_Varna. Препоръка: да.
114: 8. **Решенията**: Петър подписва `granitsi_decisions_3_2026-09-06_proba.json` **по sha256 на блоба в b6e627d** (`git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json | sha256sum`), с добавен от изпълнителя ред `attribution` (ToS §1.G) в СЪЩИЯ файл в нов комит, чийто sha той препотвърждава сутринта. Препоръка: да — това е Г2-б без нов блоб.
115: 9. **Родството** — 10-те вложени двойки (6 декларирани в регистъра + 7 недекларирани, измерени: rozova_dolina ⊂ asparuhovo, kokardzha_generic ⊂ izgrev_kv, abatko ⊂ kk_konstantin_elena, saltanat ⊂ morska_gradina, vazrazhdane1/2/3 ⊂ vazrazhdane; druzhba ⊂ asparuhovo, kaisieva ⊂ vladislavovo, mladost1/2 ⊂ mladost) се подписват като **геометрични факти за присвояването** („детето печели“), без да се пипа регистърът (`parents` там е сутрешен дълг). Препоръка: да.
116: 10. **Ваялар** остава без граница тази нощ (`alias_of` → регистър сутринта); **Евксиноград** = 5729429 с бележката за конфликта на имена; **16-те без решение** → `deferred` в `_meta.registry_pending`. Препоръка: да.
117: 
118: ### Б1 · Сглобяване (varna_3d, частно) — `data/quarters_signed.geojson`
119: Изпълнител: Claude Executor. Write-set: `src/build_quarters_signed.py`, `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`, `.gitignore` (`!data/quarters_signed.geojson`), `data/quarters_signed.geojson`. Съобщения: `build: assemble quarters_signed.geojson from decisions 3 (sha <…>) with D1 schema for imported geometry` · `gates: qa_quarters_signed with negative fixtures`. Съдържание: 61 Feature (60 Уикимапия + Младост 2 по ключа от Б0 т. 3), полетата по Б0 т. 1–4, 6; `_meta`: `artifact_class: "signed_by_plan_signature"`, `decisions_sha256`, `decisions_commit`, манифест на входовете (frozen v2, extra 5729429, mladost2 face, agkk_au5 само като свидетел), `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict: "allowed_with_conditions", position}`, `parent_child[]` (Б0 т. 9), `registry_pending[]`. Байтове по G30 (UTF-8 без BOM, sorted keys, compact, финален LF; две сглобявания = байт-еднакви). **Гейт (червен):** предгейтове G19 (`gh repo view varna_3d --json visibility` = PRIVATE) и G3 (`qa_no_cad_ids.py`); G25-а (двата хеша поотделно, подменен връх → ✗, подменен `wm_id` → ✗), G26 (биекция решения ↔ трите множества на D4 с `declared_streets`→polygon, `alias_of`/`deferred`→`_meta`; всеки код от регистъра има решение или е в `registry_pending`, поименно), G27(а) (низът по амандамент №2 §3.8 във всеки Feature), D1 (21 полета, `null` само където Б0 т. 1 позволява; `drawn_*` непразно при внос → ✗), лиценз (голо „CC BY-SA“ → ✗), една геометрия към два кода → ✗, `precision_m` липсва → ✗, метод „по улици“ без `mladost2` → ✗. Комитът на `data/quarters_signed.geojson` е **на Петър** по D16/G4: изпълнителят го оставя стейджнат с готово съобщение (`data: signed quarter boundaries v1 (decisions 3, sha <…>)`) и го записва в доклада; всичко след Б1 чете файла по sha, не по комит.
120: 
121: ### Б2 · Присвояване P8-а (varna_3d)
122: Write-set: `src/fire_varna_locations.py` (каналът `SIGNED_POLYGON` + `DISTRICT_FALLBACK`, четене на `quarters_signed.geojson` по sha; `LEDGER` сочи НОВ датиран леджер `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` с `_meta.base_rev` = комитът на стария; старият не се пипа), `src/qa_p8a.py`, `data/fire_varna_places.json`, `data/fire_varna_hotels.json` (износът), `data/fire_varna_location_inputs.json` (пиновете, вкл. `quarters_signed.geojson` sha), новият леджер. Съобщения: `feat(p8a): SIGNED_POLYGON channel with district fallback, new dated ledger, written quarters untouched` · `data: places export with quarter_attribution (decisions 3)`. Правила: само ПРАЗЕН квартал се пише; най-малкият съдържащ полигон; двойка без подписано родство и място в двата → `disputed`, не се пише; ръб `max(50, precision_m)` → `edge_pending`; без полигон → районът (Б0 т. 4); записан ≠ полигон → леджер `disputed`, редът непроменен (G17). Координати: от пиннатия вход по D10 — **ако `place_identity.json` няма lat/lon (0/375), Б2 чете координатите от износа по същия път, по който ги чете днешният канал** (изпълнителят го измерва и записва; ако днешният канал няма координати, Б2 спира и остава като мярка Н2). Десетият ключ по Б0 т. 5, `META_KEYS` 10, двата преписа и пиновете на D13 в същия комит. **Гейт (червен):** G17 (всеки записан квартал в стария леджер-блоб `git show <base_rev>:…` е байт-равен в новия износ), G4 (fail-closed без подпис → тук подписът е този план + sha на решенията, записани в `_meta`), `qa_fire_varna_places_export.py` с 10 ключа, брой присвоени = броят „би получил“ от Н2 (мярката и резултатът трябва да съвпадат до място), `edge_pending` и `disputed` в леджера поименно, `python -m unittest` зелен.
123: 
124: ### Б3 · Търсене по квартал F13 (Fire_Varna)
125: Write-set: `index.html` (`QUARTER_SRC`, `QUARTER_CODES` +41, `PLACES_CACHE` v7, нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`), `data/places.json`, `data/hotels.json` (доставката от Б2 по подредената тройка на D13: пинове + `expectations.json` + двата преписа), `tests/test_granitsi_fixtures.py` (шестте S17 фикстури, вкл. `client_cache_matrix` в node — изпълнителят назовава изпълнителя), `release/sign` артефактите по гейта на доставката от 05.09. Съобщения: `feat(search): quarter search over signed boundaries, attribution row, QUARTER_CODES +41, cache v7` · `data: places delivery with quarter_attribution (D13 ordered)` · `tests: S17 fixtures fail on broken candidates`. **Гейт (червен):** замразената референция на търсенето (нула изгубени резултати; всяка нова печалба поименно), шестте фикстури падат върху нарочно счупен кандидат и минават след, `python -m unittest discover -s tests` и `python -m gates.run_gates` зелени, `validatePlaces2` върху доставката = 375 (нито едно място изхвърлено мълчаливо — фикстура с непознат код → трябва да падне ШУМНО, не тихо), размерът ≤ 5 MB, никаква геометрия в дифа (grep за `coordinates` в проследените файлове на Fire_Varna → 0 извън `data/hydrants.json`).
126: 
127: ### Б4 · Одит на Б1–Б3 и докладът
128: Одитор (Opus, read-only, друг агент) на всеки лот: гейтовете преизпълнени, дифът срещу write-set-а (всеки допълнителен файл = находка), авторите, съобщенията, sha веригата решения → граници → леджер → износ → доставка. Докладът `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna) носи числата на А и Б, всички sha, спрелите лотове с причината, и §„Какво прави Петър сутринта“: комит на `quarters_signed.geojson` (G4), препотвърждаване на решенията по sha, преглед на дифа в трите репа, регистърът (Ваялар, Евксиноград/Траката, Цветен квартал, `parents`, 16-те), Gate 2, пуш.
129: 
130: **Ред на изпълнение при подписан Б0:** Н0 → Н1 → Н2-0 → Н2 → Н3-а → Н4 (ЧАСТ А, мерки) → Б1 → Б2 → Б3 → Б4. Паднал гейт спира лота и всичко след него; докладът излиза винаги.
131: 
132: ## 7 · Конфликти и нормализация (мярка, влиза в Н2/Н4 и в доклада)
133: - **Леджер на конфликтите по поле** за всяко от 375-те места: какво твърди всеки извор за квартала — регистровият запис (REG/KAIS/НТР, ранг), адресният низ (парсиран: „бул. Владислав Варненчик“ ≠ „кв. Владиславово“ — булевард и квартал носят едно име), кадастралният `quar` на най-близкото тяло, потвърденият полигон (координата), районът; колона `resolution` по правилото „координатата решава квартала; името е свидетел“, и колона `conflict_kind` ∈ {none, name_vs_polygon, parent_vs_child, pin_outside_all, written_outside_polygon}. Изход: `scratch/granitsi/conflict_ledger_07.09.json` (varna_3d, непроследен) + числата по вид в доклада. Нищо не се презаписва от този леджер; той е списъкът за Петър.
134: - **Сградите (Н4)** носят същите колони: кадастрален `quar` срещу полигона по координатата на тялото; несъгласията по вид (адрес на булевард с име на квартал; Кайсиева/Владиславово; Акчелар/Виница; курорт/квартал Чайка).
135: - **Правилото за бъдещето** (в доклада, за амандамент): всеки нов извор влиза с ранг и с колона в леджера; никой извор не презаписва друг; координатата е арбитърът за полето „квартал“; имената се нормализират през регистъра (alias-и), не през редакции на данните.
136: 
137: ## Какво подписва Петър
138: 
139: **ЧАСТ А (винаги):** подписваш **една нощ от мерки**: шест лота, които четат — пинове с доказана верига (Н0), кандидат-геометрия от 60-те уикимапийски кода в частното репо, която НЕ е подписан артефакт и умира с една команда (Н1), координати и присвояване, преброени срещу непокътнат леджер и три ленти на неточността (Н2-0, Н2), пет фикстури, които фиксират ДНЕШНОТО поведение на търсенето (Н3-а), мярката за ~10k сгради (Н4) и доклад, чиито числа идват от одитора (Н5) — плюс двете обявени отклонения от `ПЛАН_ИЗЧИСТВАНЕ_v2 §0.1` и `§0.3` и десетте решения в §5, които остават твои и на които нито един агент няма право да отговори през нощта.
140: 
141: **ЧАСТ Б (само с блок Б0):** подписваш и десетте решения в §6 Б0 — тогава нощта произвежда `quarters_signed.geojson` (стейджнат за твоя комит), присвояване на квартал за празните места с района като резерва, търсене по квартал с реда за атрибуция, и одитиран доклад; всичко локално, обратимо, без пуш.
142: 
143: ## Какво НЕ се пипа тази нощ (ЧАСТ А; при подписан Б0 изключенията са изброени в Б1–Б3)
144: 
145: `quarter_registry.json` · написаните 201 квартала · `lot1v_locations_375.json` · `place_identity.json` и `data/fire_varna_*.json` · `fire_varna_locations.py` и каналът `SIGNED_POLYGON` · `.gitignore` на varna_3d (разигнорирането чака комита на Петър по G4) · `index.html` (нито `QUARTER_SRC`, нито `QUARTER_CODES`, нито картончето, нито `PLACES_CACHE`) · `_meta` на износа и десетият ключ · Младост 2 като Feature · полето `district` в геометрията · `precision_m` като число · `origin` на което и да е от трите репа.

codex
Вече има два конкретни блокера: новите gate-скриптове още липсват, а `validatePlaces2` проверява 150 места и връща boolean — условието „= 375“ не е изпълнимо така. Проверявам и дали обещаното нощно присвояване има реален източник на координати.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'LEDGER|lat|lon|CHANNEL|base_rev|INPUT|identity' C:/git/varna_3d/src/fire_varna_locations.py C:/git/varna_3d/src/qa_fire_varna_places_export.py C:/git/varna_3d/src/place_identity.py C:/git/varna_3d/data/fire_varna_location_inputs.json" in C:\git\Fire_Varna
 succeeded in 0ms:
C:/git/varna_3d/data/fire_varna_location_inputs.json
C:/git/varna_3d/src/place_identity.py
C:/git/varna_3d/src/qa_fire_varna_places_export.py
C:/git/varna_3d/src/fire_varna_locations.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath '"'docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md' -Encoding UTF8 -TotalCount 100 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=64; Get-Content -LiteralPath '"'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' -Encoding UTF8 | Select-Object -Skip 64 -First 55 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
1: # СЪСТОЯНИЕ · ЛОТ „Границите“ към 06.09.2026, ~08:00 (по часовника на машината) — „вече може да се каже, че имаме кварталите“ (Петър)
2: 
3: Входна точка за следващата сесия. Нищо тук не е публикувано; нищо не е пушнато (Fire_Varna `main` е 36 комита пред `origin/main`, всичките документи, мерки и записи — нула геометрия, нула промени в картата или в `data/`).
4: 
5: ## 1 · Какво имаме
6: - **Изворът на границите е решен от Петър:** човешките полигони от Уикимапия („точно това е границата“ за Кайсиева; „прегледах районите — нека ползваме тях“). Стълбата на изворите v3 и всичко около нея е в `docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md` (ревизия 2б; минал Кими К15–К21 и Astra S14–S20; **неподписан**).
7: - **Замразено тяло:** обходът на Уикимапия (667 проби, 11 303 места) → извод v2 288 полигона, sha256 `b53a3322…` (`scratch/boundary_gallery/frozen_2026-09-06/`, игнорирана папка; отпечатъците и броевете в `scratch/places_search/wikimapia_frozen_measure_06.09.md`).
8: - **Решенията на Петър:** `scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json` (проба, без геометрия): **61 граници** — 32 квартала/комплекса, 26 местности/с.о., 3 зони/паркове/курорти; Младост 2 по четирите му улици (оси от OSM); Бриз = големият полигон (измерен 0 m до четирите страни, които описа); Акчелар = уикимапийската „Белица“ (94 % от кадастралната обвивка); Евксиноград = 5729429 (EN „Euxinograd“ = BG „Траката - разширение“). Без граница: 6 отложени, Ваялар (второ име на Средна Трака), 16 без решение.
9: - **Ефект върху 375-те места** (координати от пробата, правило „най-малкият съдържащ полигон, ръб 100 m“): получават квартал 71 · съгласие 186 · спор 7 · ръб 62 · извън 49.
10: - **Пробите за гледане** (локален сървър `granitsi-preview`, порт 8792, игнорирана папка `scratch/boundary_gallery/granitsi_preview_05.09/`): `wikimapia.html` (събраното), `board.html` (бордът: да/не/отложи, износ JSON), `result.html` (картата на резултата).
11: 
12: ## 2 · Защо ни бяха кварталите (замисълът от `ПРОМПТ_нова_тема_Границите.md` и `ПЛАН_ЛОТ_Границите.md`)
13: Търсачката на Fire_Varna намира места по име и адрес; кварталът е начинът, по който хората (обаждащият се, колегата) назовават мястото. Мярката от 05.09: **174 от 375 места без квартал; 14 от 32 квартала без нито едно място; търсенето пада на съюзи/точки и на 7 думи, които са и имена; „Цветен квартал“ не беше в регистъра.** Целта: всяко място да има квартал по един и същ, проверим начин, и търсене „училище Възраждане 3“ / „Кайсиева градина“ да връща всичко ВЪТРЕ в границата, не само местата с този квартал в адреса. Границата е човешкото понятие, превърнато във факт, който машината проверява.
14: 
15: ## 3 · Как продължаваме (редът от амандамент №2, ревизия 2б)
16: 1. **Gate 1** — Петър подписва амандамент №2 (8 решения; повечето вече взети на практика: стълбата v3, лиценз на ниво Feature, обхватът = регистърът с местностите, атрибуцията по ToS §1.G). Открито: текстът на реда „квартал по Wikimapia.org“ в картата на мястото; реален API ключ (негов акт); редът на М2-3.
17: 2. **Г2-б** — Петър комитва сам файла с решенията (решения 3, след преглед) като подписани решения; бордът-проба е свършил работата на борда.
18: 3. **Г2-в** — изпълнител (Opus) сглобява `varna_3d/data/quarters_signed.geojson` с провенанс (wm_id, отпечатъци, потвърждение, лиценз на ниво Feature), гейтове G25–G30; одитор проверява.
19: 4. **Р** — регистърът: Ваялар → alias на Средна Трака; Евксиноград/Траката конфликтът; Цветен квартал; 16-те без решение.
20: 5. **P8-а** — присвояване: 71-те празни места получават квартал, записаните не се променят (G17), ръбът чака, споровете се показват.
21: 6. **F13** — търсене по квартал + редът за атрибуция; регресионните фикстури (S17) минават.
22: 7. **Gate 2 + пуш** (Петър).
23: Паркирано зад Границите: Ред (Фаза E), Ф0-б, амандамент №10 (A.2-11).

 succeeded in 12ms:
86: ## 4 · Нарушения, които спират нощта веднага88: Опит за `git push` · геометрия в проследен файл на Fire_Varna · редакция на регистъра · промяна на написан квартал · запис в `lot1v_locations_375.json`, `place_identity.json` или `data/fire_varna_*.json` · файл на име `quarters_signed.geojson` · Feature по метод „по улици“ · нов публичен `src` **или нов квартален КОД** без разширен `QUARTER_CODES` и подредената тройка на D13 · низът `10135` в **публична** доставка (в частния провенанс и в мярката е позволен — иначе АГКК изворът е неназовим) · зелен гейт без падаща отрицателна фикстура.
89: 
90: ## 5 · Сутринта (решенията за Петър, ако Б0 НЕ е подписан тази вечер)
91: 
92: 1. **Схемата за ВНЕСЕНА геометрия** (кои от 21-те полета на D1 отпадат и с какво се заместват) — амандамент, без който няма подписан артефакт.
93: 2. **Кое правило е `wm_polygon_sha256`** — суровият хеш (днешният в решенията) или канонизацията на D1.
94: 3. **Младост 2**: подписан ключ по D2 + лиценз (ODbL, „© OpenStreetMap contributors“) + под на `precision_m` за уличен метод.
95: 4. **Районът**: от нашия `district.code` (375/375 съгласие) с явен `district_src`, или от АГКК — тогава `_meta.source_terms["agkk_inspire_au5"]` се попълва и G22/G23 стават червени предгейтове.
96: 5. **Едно име за десетия ключ** (`licence_quarter_boundary` или `quarter_attribution`) и низът за атрибуция; картата да е независима от извора `{code:{src,url,label,licence}}`, за да носи и ODbL, и АГКК.
97: 6. **`precision_m`** — стойност и довод (от нея зависи кой е `edge_pending`).
98: 7. **Разширяването на `QUARTER_CODES`** с 41-те кода и какво става с `morska_gradina`, `sveti_nikola`, `zelenika`, които днес са местности.
99: 8. **Решенията**: `git mv` на днешния блоб под подписан път (не втори блоб с втора sha) или подпис на днешния път.
100: 9. Регистърът: Ваялар→alias, Евксиноград/Траката, Цветен квартал, `parents` за Възраждане 1–4 и Розова долина, 16-те без решение.
101: 10. Дългове: D10 твърди, че `_check_pins` (`:623-639`) сверява `inputs` — не ги сверява; `_meta.base_rev` липсва в леджера; `granitsi_decisions_3` няма ред за атрибуция.
102: 
103: 
104: ## 6 · ЧАСТ Б — нощ от резултати (тръгва само с подписан блок Б0)
105: 
106: ### Б0 · Блокът решения, който Петър подписва тази вечер (препоръките са на архитекта; всяко „да“ е негово)
107: 1. **Схема за ВНЕСЕНА геометрия (промяна на D1, обявена).** За Feature с `source ∈ {wikimapia, declared_streets}` полетата `drawn_by · drawn_at · basemap · viewport · visible_layers · screenshot_sha256 · approval_digest` са `null` по договор (гейт за взаимна изключителност: или ръка, или внос); `approved_by = "Petar"`, `approved_at = decided_at` от решенията; `signed_by = "Petar"` става валидно с подписа на този план по sha на решенията (т. 8); `witnesses[]` = [{kind: "wikimapia_object", url, fetched_at, raw_response_sha256}] (за Младост 2: {kind: "osm_carriageways", ways по име, fetched: 2026-09-06}); `version: 1`; `note = reason`. Останалите 14 полета на D1 остават задължителни. Препоръка: да.
108: 2. **`wm_polygon_sha256` = канонизацията на D1** (6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; MultiPolygon по правилото на амандамент №2 §4). Суровият хеш от решенията се пренася като `raw_geometry_sha256` и гейтът сверява и двата. Препоръка: да.
109: 3. **Младост 2 — изричен подписан ключ по D2** за `code = mladost2`, `method = "street_bounded_face"`, лиценз `"ODbL © OpenStreetMap contributors"` (осите), `precision_m = 50`, четирите улици дословно в `witnesses`. Само този код; всеки друг Feature с този метод = червено. Препоръка: да.
110: 4. **Районът** се пише от НАШИЯ `district.code` на мястото (375/375 съгласие с АГКК, мерено 05.09), `district_src: "fire_varna_district"`; в Feature-ите на кварталите районът е изведен по представителна точка срещу същите наши 5 района, не от АГКК INSPIRE (G22 остава заключен). Резервата „място без квартал → районът“ пише `quarter = {name: <име на района>, code: <словесният код от DISTRICT_CODES>, src: "DISTRICT_FALLBACK"}`. Препоръка: да.
111: 5. **Десетият ключ на `_meta` се казва `quarter_attribution`** (името в §3.3 на амандамент №2 отпада); форма `{<code>: {src, url, label, licence}}` — независима от извора, носи Wikimapia, ODbL и бъдещи; UI низът: „квартал по Wikimapia.org · обектът“ (двете като връзки) под името на квартала в картончето, само за кодове с запис в картата. Препоръка: да.
112: 6. **`precision_m`**: 100 за `wikimapia`, 50 за `street_bounded_face`; ръб = `max(50, precision_m)` по D7 → `edge_pending`. Препоръка: да.
113: 7. **`QUARTER_CODES` се разширява** с 41-те потвърдени кода, които днес липсват; `morska_gradina`, `sveti_nikola`, `zelenika` остават в `LOCALITY_CODES` (търсят се като местности); `QUARTER_SRC` получава `SIGNED_POLYGON` и `DISTRICT_FALLBACK`; `PLACES_CACHE` v6→v7; пиновете и `expectations.json` — в подредената доставка varna_3d → Fire_Varna. Препоръка: да.
114: 8. **Решенията**: Петър подписва `granitsi_decisions_3_2026-09-06_proba.json` **по sha256 на блоба в b6e627d** (`git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json | sha256sum`), с добавен от изпълнителя ред `attribution` (ToS §1.G) в СЪЩИЯ файл в нов комит, чийто sha той препотвърждава сутринта. Препоръка: да — това е Г2-б без нов блоб.
115: 9. **Родството** — 10-те вложени двойки (6 декларирани в регистъра + 7 недекларирани, измерени: rozova_dolina ⊂ asparuhovo, kokardzha_generic ⊂ izgrev_kv, abatko ⊂ kk_konstantin_elena, saltanat ⊂ morska_gradina, vazrazhdane1/2/3 ⊂ vazrazhdane; druzhba ⊂ asparuhovo, kaisieva ⊂ vladislavovo, mladost1/2 ⊂ mladost) се подписват като **геометрични факти за присвояването** („детето печели“), без да се пипа регистърът (`parents` там е сутрешен дълг). Препоръка: да.
116: 10. **Ваялар** остава без граница тази нощ (`alias_of` → регистър сутринта); **Евксиноград** = 5729429 с бележката за конфликта на имена; **16-те без решение** → `deferred` в `_meta.registry_pending`. Препоръка: да.
117: 
118: ### Б1 · Сглобяване (varna_3d, частно) — `data/quarters_signed.geojson`
119: Изпълнител: Claude Executor. Write-set: `src/build_quarters_signed.py`, `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`, `.gitignore` (`!data/quarters_signed.geojson`), `data/quarters_signed.geojson`. Съобщения: `build: assemble quarters_signed.geojson from decisions 3 (sha <…>) with D1 schema for imported geometry` · `gates: qa_quarters_signed with negative fixtures`. Съдържание: 61 Feature (60 Уикимапия + Младост 2 по ключа от Б0 т. 3), полетата по Б0 т. 1–4, 6; `_meta`: `artifact_class: "signed_by_plan_signature"`, `decisions_sha256`, `decisions_commit`, манифест на входовете (frozen v2, extra 5729429, mladost2 face, agkk_au5 само като свидетел), `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict: "allowed_with_conditions", position}`, `parent_child[]` (Б0 т. 9), `registry_pending[]`. Байтове по G30 (UTF-8 без BOM, sorted keys, compact, финален LF; две сглобявания = байт-еднакви). **Гейт (червен):** предгейтове G19 (`gh repo view varna_3d --json visibility` = PRIVATE) и G3 (`qa_no_cad_ids.py`); G25-а (двата хеша поотделно, подменен връх → ✗, подменен `wm_id` → ✗), G26 (биекция решения ↔ трите множества на D4 с `declared_streets`→polygon, `alias_of`/`deferred`→`_meta`; всеки код от регистъра има решение или е в `registry_pending`, поименно), G27(а) (низът по амандамент №2 §3.8 във всеки Feature), D1 (21 полета, `null` само където Б0 т. 1 позволява; `drawn_*` непразно при внос → ✗), лиценз (голо „CC BY-SA“ → ✗), една геометрия към два кода → ✗, `precision_m` липсва → ✗, метод „по улици“ без `mladost2` → ✗. Комитът на `data/quarters_signed.geojson` е **на Петър** по D16/G4: изпълнителят го оставя стейджнат с готово съобщение (`data: signed quarter boundaries v1 (decisions 3, sha <…>)`) и го записва в доклада; всичко след Б1 чете файла по sha, не по комит.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'LEDGER|lat|lon|CHANNEL|base_rev|def main|INPUT|identity' C:/git/varna_3d/src/fire_varna_locations.py" in C:\git\Fire_Varna
 succeeded in 0ms:
6:    data/place_identity.json        (котвата: place_id → kais_i)      ┐
15:байт по байт от `src/qa_fire_varna_location_isolation.py` (G-ISO).
63:from place_identity import skel                       # noqa: E402
69:IDENTITY = ROOT / "data" / "place_identity.json"
76:LEDGER = ROOT / "scratch" / "refactor" / "_addr" / "lot1v_locations_375.json"
77:INPUTS = ROOT / "data" / "fire_varna_location_inputs.json"
83:# artefacts must come out of the run byte for byte the same.  `output/` belongs
91:RECORDED_INPUTS = ("data/place_identity.json", "data/registry_manifest.json",
102:# this table is quarantine, never a translated „район X“ (К3 of В3).
134:# channel may fill a field.  Two unrelated valid values from ONE channel stop
142:CHANNELS = (CH_REG_TOCITY, CH_REG_TOADDR, CH_REG_MANIFEST,
144:CHANNEL_RANK = {CH_REG_TOCITY: 0, CH_REG_TOADDR: 0, CH_REG_MANIFEST: 0,
149:CHANNEL_SRC = {CH_REG_TOCITY: SRC_REG, CH_REG_TOADDR: SRC_REG,
159:    "Златни пясъци": "zlatni_pyasatsi",
314:    The type is part of the identity: `match_key` alone folds „кв. Чайка“ and
358:        """The keys one written form answers to: as written, and dots flattened.
362:        flattening is done here — on BOTH sides, so it cannot invent a match.
477:    def held_out(self, eid: str, lat: float, lon: float) -> str | None:
483:            lo_lat, lo_lon, hi_lat, hi_lon = h["bbox"]
484:            if lo_lat <= lat <= hi_lat and lo_lon <= lon <= hi_lon:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'META_KEYS|ROW_KEYS|lat|lon|_check_pins|def main' C:/git/varna_3d/src/qa_fire_varna_places_export.py" in C:\git\Fire_Varna
 succeeded in 0ms:
60:ROW_KEYS = {"name", "kind", "lat", "lon", "zone", "quarter", "district",
62:META_KEYS = {"generated", "count", "by_kind", "by_zone_src", "licence_osm",
166:# same two words alone would be a private practice, i.e. a personal datum.
451:def main() -> None:
455:        print(f"ГРЕШКА: няма {OUT.relative_to(ROOT)} — пусни "
550:    check(set(meta) == META_KEYS, f"_meta има точно {len(META_KEYS)} ключа",
552:    bad_keys = [r.get("name") for r in rows if set(r) != ROW_KEYS]
553:    check(not bad_keys, f"всеки ред има точно {len(ROW_KEYS)}-те ключа",
555:          else " · ".join(sorted(ROW_KEYS)))
631:    out_box = [f"{r.get('name')} ({r.get('lat')}, {r.get('lon')})" for r in rows
632:               if not (isinstance(r.get("lat"), (int, float))
633:                       and isinstance(r.get("lon"), (int, float))
634:                       and LAT0 <= r["lat"] <= LAT1 and LON0 <= r["lon"] <= LON1)]

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath '"'C:/git/varna_3d/src/fire_varna_locations.py' -Encoding UTF8 -TotalCount 140 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
1: """ЛОТ 1в-В (P6) — КВАРТАЛЪТ, РАЙОНЪТ И ДОПЪЛНИТЕЛНОТО, всяко с извора си.
2: 
3: `Fire_Varna/docs/plans/ПЛАН_ЛОТ1в-В_кварталите.md` §3г (правилото на Петър) ·
4: §3е (В3) · §3ж (В4, окончателната механика) · §3з (Gate 1-В е подписан).
5: 
6:     data/place_identity.json        (котвата: place_id → kais_i)      ┐
7:     web/varna_buildings_info.json   (КАИС `quar` и `reg` на тялото)   ├→ quarter
8:     data/registry_manifest.json     (регистровият адрес на реда)      │  district
9:     Varna_buildings/config/quarter_registry.json (канонът + типът)    ┘  locality
10: 
11: FIRE-EXPORT-ONLY (S7-1).  `src/place_zones.py` е ГЛОБАЛЕН resolver: по него
12: вървят 576-те реда на майстора и `build_public_buildings_geojson.py` на другата
13: тема.  Затова тази стълба НЕ го пипа и НЕ го замества — тя е ПОСЛЕДЕН resolver
14: само за двата износителя към Fire_Varna.  Че майсторът не е мръднал се доказва
15: байт по байт от `src/qa_fire_varna_location_isolation.py` (G-ISO).
16: 
17: ПРАВИЛОТО (§3г, подписано):
18: 
19:   * `quarter` — САМО жилищно ниво по регистъра и САМО с човешки написан извор:
20:     регистровият адресен сегмент (REG) или кадастралният квартал на закотвеното
21:     тяло (KAIS).  Няма извор → няма квартал.  Нищо не се гади.
22:   * `locality` — допълнителното местоположение (промишлена зона, парк,
23:     местност, микрорайон) от същите два извора; никога на мястото на квартала.
24:   * `district` — районът, САМО от КАИС `reg` на тялото, код от затворения
25:     списък на петте градски района (S4).  Празен/чужд `reg` = карантина.
26:   * `zone` — съвместимост до G-ZERO-ZONE (S6-5): `quarter?.name` иначе
27:     „район <име>“.
28: 
29: НИЩО НАРИСУВАНО, НИЩО OSM-ПРОИЗВОДНО (§3г т. 6).  Чертаните обвивки (IoU 0,128
30: срещу подписан праг 0,70), етикет-точките и районният полигон са OSM-производни
31: или нарисувани — те не решават нито едно от трите полета.  Слоят на кварталите
32: и полигонът влизат САМО като сравнителни колони в маскирания ledger.
33: 
34: ЕДИН ИЗВЛИЧАЩ ЗА ДВАТА ИЗВОРА (S1).  Кварталният низ се признава само с ИЗРИЧЕН
35: типов префикс в началото, ключът е ТИПИЗИРАН — (kind_norm, match_key(име)) —
36: защото `match_key` сам по себе си не различава „кв. Чайка“ от „к.к. Чайка“.
37: Композит (две квартални думи в един низ) не е токен и не решава: „кв.
38: „Аспарухово“, ж.к. „Дружба““ назовава две места, а регистърът забранява цепенето
39: по запетая (`matcher_constraints`).
40: 
41: ПЕТ НАИМЕНУВАНИ КАНАЛА (М6, P7-б).  Свидетелите са REG-TOCity и REG-TOAddress
42: (Националният туристически регистър по УИН), REG-manifest (регистровият адрес),
43: KAIS-quar (кадастралната клетка) и KAIS-addr (свободният адресен текст през
44: ЗАТВОРЕНА таблица).  Рангът е {REG-TOCity = REG-TOAddress = REG-manifest} >
45: KAIS-quar > KAIS-addr; всеки id минава `classify` ПРЕДИ подреждането.
46: Родител↔дете се решава в полза на ДЕТЕТО (ж.к. Възраждане 1 бие ж.к.
47: Възраждане); две несвързани валидни стойности СПИРАТ билда — това е въпрос за
48: подпис, не за монета.
49: 
50:     python src/fire_varna_locations.py        # мярката, нищо не пише
51:     python src/fire_varna_locations.py --ledger   # пише маскирания ledger
52: """
53: from __future__ import annotations
54: 
55: import argparse
56: import hashlib
57: import json
58: import re
59: import sys
60: from pathlib import Path
61: 
62: sys.path.insert(0, str(Path(__file__).resolve().parent))
63: from place_identity import skel                       # noqa: E402
64: 
65: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
66: sys.stderr.reconfigure(encoding="utf-8", errors="replace")
67: 
68: ROOT = Path(__file__).resolve().parent.parent
69: IDENTITY = ROOT / "data" / "place_identity.json"
70: BODIES_INFO = ROOT / "web" / "varna_buildings_info.json"
71: MANIFEST = ROOT / "data" / "registry_manifest.json"
72: PLACES_EXPORT = ROOT / "data" / "fire_varna_places.json"
73: HOTELS_EXPORT = ROOT / "data" / "fire_varna_hotels.json"
74: REGISTRY = Path(r"C:\git\Varna_buildings\config\quarter_registry.json")
75: FOLD_TOOLS = Path(r"C:\git\Varna_buildings\tools")
76: LEDGER = ROOT / "scratch" / "refactor" / "_addr" / "lot1v_locations_375.json"
77: INPUTS = ROOT / "data" / "fire_varna_location_inputs.json"
78: NTR_RAW = ROOT / "scratch" / "refactor" / "_addr" / "ntr_hoteli_raw.json"
79: 
80: # --- G-ISO · the BASE this lot must not move (S5) ----------------------------
81: # The global ladder feeds the master (576 rows) and the public-buildings theme.
82: # This lot is Fire-export-only, so those five files and the two generated
83: # artefacts must come out of the run byte for byte the same.  `output/` belongs
84: # to the parallel theme: it is READ here, never written.
85: BASE_SOURCES = ("src/place_zones.py", "src/build_places.py", "src/apply_zones.py",
86:                 "src/build_public_buildings_geojson.py", "data/places.json")
87: BASE_GENERATED = ("output/public_buildings_2026-09-03.geojson",
88:                   "output/public_buildings_2026-09-03.csv")
89: # Recorded, not frozen: they move on their own cycles and this file says which
90: # version answered the questions of лот В.
91: RECORDED_INPUTS = ("data/place_identity.json", "data/registry_manifest.json",
92:                    "web/varna_buildings_info.json")
93: KAIS_MANIFEST = ROOT / "data" / "kais_open" / "2026-07-24" / "manifest.json"
94: 
95: # The comparison-only layers (§3г т. 6): they never decide, they only get a
96: # column in the ledger so that a disagreement is visible instead of silent.
97: QUARTERS_LAYER = Path(r"C:\git\m6000_private\number_viewer\quarters_layer.geojson")
98: DRAWN_LAYER = Path(r"C:\git\m6000_private\number_viewer\quarters_drawn_v1.geojson")
99: 
100: # --- the closed list of the five city districts (S4) -------------------------
101: # `district` is published, so its code must be allow-listed: a value outside
102: # this table is quarantine, never a translated „район X“ (К3 of В3).
103: DISTRICTS: dict[str, tuple[str, str]] = {
104:     "район Приморски": ("primorski", "Приморски"),
105:     "район Одесос": ("odesos", "Одесос"),
106:     "район Младост": ("mladost", "Младост"),
107:     "район Аспарухово": ("asparuhovo", "Аспарухово"),
108:     "район Владислав Варненчик": ("vladislav_varnenchik", "Владислав Варненчик"),
109: }
110: 
111: # --- the signed table `registry kind → quarter | locality | DROP` (S6-1) -----
112: # Signed at Gate 1-В as it stands.  There is no „by decision at runtime“: a
113: # registry kind outside this table stops the build.
114: KIND_NORM = {"жк": "жк", "кв": "кв", "кк": "кк", "со": "со", "с.о.": "со",
115:              "вз": "вз", "в.з.": "вз", "м-т": "местност", "местност": "местност",
116:              "махала": "махала", "зона": "зона", "пз": "пз", "парк": "парк",
117:              "мр": "мр"}
118: KIND_CLASS = {"жк": "quarter", "кв": "quarter", "кк": "quarter",
119:               "со": "quarter", "вз": "quarter",
120:               "местност": "locality", "зона": "locality", "пз": "locality",
121:               "парк": "locality", "мр": "locality",
122:               "махала": "DROP"}
123: 
124: # The three sources a published field may carry (S1 · К6-2 of В3).
125: SRC_REG = "REG"
126: SRC_KAIS = "KAIS"
127: SRC_SIGNED = "SIGNED_OVERRIDE"
128: QUARTER_SRC = (SRC_REG, SRC_KAIS, SRC_SIGNED)
129: DISTRICT_SRC = (SRC_KAIS, SRC_SIGNED)
130: 
131: # --- М6 · the four new witness channels + the existing one (P7-б) ----------
132: # A channel is a NAMED witness, not a source of truth: every id it offers is
133: # classified BEFORE anything is ordered, and the rank below decides which
134: # channel may fill a field.  Two unrelated valid values from ONE channel stop
135: # the build (амандамент №1 A.1); two channels that disagree name a
136: # collision.  Neither is ever settled by taking `[0]`.
137: CH_REG_TOCITY = "REG-TOCity"
138: CH_REG_TOADDR = "REG-TOAddress"
139: CH_REG_MANIFEST = "REG-manifest"
140: CH_KAIS_QUAR = "KAIS-quar"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=30; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 30 -First 28 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 12ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=590; Get-Content -LiteralPath '"'C:/git/varna_3d/src/fire_varna_locations.py' -Encoding UTF8 | Select-Object -Skip 590 -First 70 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 37ms:
591: 
592:         # The frozen history: the zone word each row was delivered with BEFORE
593:         # this lot.  It lives in the pinned inputs, not in the identity file —
594:         # the identity is regenerated from the NEW delivery and would otherwise
595:         # answer „what is“ to a question that asks „what was“.
596:         self.legacy: dict[str, str] = {}
597:         if INPUTS.exists():
598:             frozen = json.loads(INPUTS.read_text(encoding="utf-8"))
599:             self.legacy = {k: v["zone"]
600:                            for k, v in (frozen.get("legacy_zones") or {}).items()}
601: 
602:         # М6 (P7-б): the fourth and fifth witnesses, and the pins that keep
603:         # them honest.  The pins are checked on EVERY run, not only when they
604:         # are written: a table or a raw file that moved silently is a lie the
605:         # ledger would otherwise repeat.
606:         self.ntr, self.ntr_stats = load_ntr()
607:         self.table_shas = {"NTR_CITY": table_sha(NTR_CITY),
608:                            "KAIS_ADDR_ABBREV": table_sha(
609:                                [list(t) for t in KAIS_ADDR_ABBREV])}
610:         self._check_pins()
611: 
612:         # The signed overrides are resolved to `place_id` ONCE, here (P7-в).
613:         self.signed = self._resolve_signed()
614: 
615:         self.rows: dict[str, dict] = {}
616:         self.quarantine: list[dict] = []
617:         self.pending_signature: list[dict] = []
618:         for pid, o in self.objects.items():
619:             self.rows[pid] = self._resolve_one(pid, o, cell, i_quar, i_reg,
620:                                                i_addr)
621: 
622:     # -- the pins of М6 --------------------------------------------------------
623:     def _check_pins(self) -> None:
624:         """The pinned НТР file and the two closed tables, verified every run."""
625:         if not INPUTS.exists():
626:             return
627:         frozen = json.loads(INPUTS.read_text(encoding="utf-8"))
628:         want = frozen.get("ntr")
629:         if want:
630:             for key in ("sha256", "bytes", "rows", "uins", "dup_groups"):
631:                 if key in want and want[key] != self.ntr_stats.get(key):
632:                     die(f"НТР пинът не се възпроизвежда: {key} е "
633:                         f"{self.ntr_stats.get(key)!r}, а закованото казва "
634:                         f"{want[key]!r} — вход, който е мръднал мълчаливо")
635:         for name, got in self.table_shas.items():
636:             pinned = (frozen.get("m6_tables") or {}).get(name)
637:             if pinned and pinned != got:
638:                 die(f"затворената таблица {name} е мръднала: {got} срещу "
639:                     f"закованото {pinned} — таблица, която решава, се пинва")
640: 
641:     def _resolve_signed(self) -> dict[str, dict]:
642:         """`SIGNED_QUARTER` by `place_id`, resolved ONCE at build (P7-в).
643: 
644:         A signature that lives on a NAME dies the day somebody edits the name.
645:         `place_id_of` is the same anchor the whole lot joins on and it STOPS on
646:         anything but exactly one match — so the signature stops too.
647:         """
648:         out: dict[str, dict] = {}
649:         for (file, name), rec in SIGNED_QUARTER.items():
650:             pid = self.place_id_of(file, name)
651:             if pid in out:
652:                 die(f"подписаният квартал сочи два пъти един и същи ред ({pid})")
653:             out[pid] = dict(rec, name=name, file=file)
654:         return out
655: 
656:     # -- the join --------------------------------------------------------------
657:     def place_id_of(self, file: str, name: str, uins=None) -> str:
658:         """The `place_id` of one exported row — by evidence, never by zone."""
659:         for uin in (uins or []):
660:             if uin in self.by_uin:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=945; Get-Content -LiteralPath '"'C:/git/varna_3d/src/fire_varna_locations.py' -Encoding UTF8 | Select-Object -Skip 945 -First 110 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 22ms:
957:     return CAD.sub("10135.***", text) if isinstance(text, str) else text
958: 
959: 
960: def comparison_columns(book: LocationBook) -> dict[str, dict]:
961:     """The drawn hull and the quarter layer — COLUMNS, never a decision.
962: 
963:     They are OSM-derived or hand-drawn (IoU 0,128 against a signed 0,70), and
964:     §3г т. 6 keeps them out of every published field.  They are read here so a
965:     disagreement is visible in the ledger instead of silent.
966:     """
967:     out: dict[str, dict] = {}
968:     try:
969:         sys.path.insert(0, str(Path(__file__).resolve().parent))
970:         import place_zones                                   # noqa: E402
971:     except Exception as e:                                   # pragma: no cover
972:         return {"_error": {"why": f"сравнителните слоеве не се четат: {e}"}}
973:     pins = {}
974:     for path, key in ((PLACES_EXPORT, "places"), (HOTELS_EXPORT, "hotels")):
975:         if not path.exists():
976:             continue
977:         doc = json.loads(path.read_text(encoding="utf-8"))
978:         for r in doc.get("places", []) + doc.get("hotels", []):
979:             pid = book.place_id_of(key, r["name"], r.get("uins") or [])
980:             pins[pid] = (r["lat"], r["lon"])
981:     mismatch: list[str] = []
982:     for pid, (lat, lon) in pins.items():
983:         row = {"layer_polygon": place_zones.quarter_of(lat, lon), "hull": None}
984:         # S4: the district polygon is OSM-derived, so it never DECIDES — but a
985:         # disagreement with the КАИС `reg` is a STOP until somebody signs which
986:         # one is wrong.  Measured 04.09: 371 rows carry a district polygon and
987:         # all 371 agree; the other 4 fall outside every polygon of the layer.
988:         poly = row["layer_polygon"]
989:         got = book.rows[pid]
990:         if (poly and poly.startswith("район") and got["district"]
991:                 and poly != got["reg_raw"]):
992:             mismatch.append(f"„{got['name']}“: полигонът казва „{poly}“, "
993:                             f"КАИС reg — „{got['reg_raw']}“")
994:         try:
995:             display, status, why = place_zones.zone_from_drawn(lat, lon)
996:             row["hull"] = display
997:             row["hull_status"] = status
998:         except SystemExit:                                   # pragma: no cover
999:             row["hull_status"] = "слоят липсва"
1000:         out[pid] = row
1001:     if mismatch:
1002:         die("районният полигон и КАИС `reg` се разминават — това иска подписано "
1003:             "решение, не мълчание (S4): " + " · ".join(mismatch[:5]))
1004:     out["_compared"] = {"district_polygon_rows":
1005:                         sum(1 for v in out.values()
1006:                             if isinstance(v, dict)
1007:                             and str(v.get("layer_polygon") or "").startswith("район")),
1008:                         "district_mismatches": 0}
1009:     return out
1010: 
1011: 
1012: # The three rows whose reason was written by hand and came out wrong (audit of
1013: # лот В, finding 5).  Their reason is DERIVED from the row's own fields here, or
1014: # it is not a reason.  М2 (05.09) re-examined it: УМБАЛ „Света Марина“ still
1015: # takes its quarter from the REGISTRY segment (its КАИС `quar` is empty), but
1016: # ДГ 32 / ДГ 36 no longer lose anything to `map_label: false` — they now carry
1017: # „ж.к. Младост“ by REG, so the sample keeps them to witness the new reason.
1018: FIX_SAMPLE_NAMES = (
1019:     "„Университетска многопрофилна болница за активно лечение „Света Марина““ ЕАД",
1020:     "ДГ 32 \"Моряче\"",
1021:     "ДГ 36 \"Морска звездица\"",
1022: )
1023: 
1024: 
1025: def why_of(row: dict) -> str:
1026:     """Едно изречение за реда — само от неговите собствени полета."""
1027:     where = f"район {row['district']['name']}" if row["district"] else "без район"
1028:     if row["quarter"]:
1029:         q = row["quarter"]
1030:         kais = (f"КАИС quar: „{row['kais_quar_raw']}“" if row["kais_quar_raw"]
1031:                 else "КАИС quar е празен")
1032:         return f"квартал „{q['name']}“ по {q['src']} · {kais} · {where}"
1033:     if row["dropped"]:
1034:         fell = " · ".join(f"{d['channel']} „{d['entry']}“ пада по {d['why']}"
1035:                           for d in row["dropped"])
1036:         return f"без квартал · {fell} · {where}"
1037:     return f"без квартал (никой извор не го дава) · {where}"
1038: 
1039: 
1040: def build_ledger(book: LocationBook) -> dict:
1041:     compare = comparison_columns(book)
1042:     compared = compare.pop("_compared", {})
1043:     rows = []
1044:     for pid, r in sorted(book.rows.items(), key=lambda kv: (kv[1]["file"],
1045:                                                             kv[1]["name"])):
1046:         cmp_row = compare.get(pid) or {}
1047:         rows.append({
1048:             "place_id": pid,
1049:             "file": r["file"],
1050:             "name": mask(r["name"]),
1051:             "kind": r["kind"],
1052:             "old_zone": r["old_zone"],
1053:             "new_zone": (r["quarter"]["name"] if r["quarter"]
1054:                          else (f"район {r['district']['name']}"
1055:                                if r["district"] else None)),

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=1135; Get-Content -LiteralPath '"'C:/git/varna_3d/src/fire_varna_locations.py' -Encoding UTF8 | Select-Object -Skip 1135 -First 150 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=58; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 58 -First 17 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
1136:                 "n_rows_still_dropped_by_the_flag": len(map_label_rows),
1137:                 "n_with_registry_segment": n_reg_label,
1138:                 "rows": [{"name": r["name"], "new_zone": r["new_zone"],
1139:                           "dropped": [d for d in r["dropped"]
1140:                                       if d["why"] == "map_label:false"]}
1141:                          for r in map_label_rows],
1142:             },
1143:         },
1144:         "rows": rows,
1145:         "quarantine": book.quarantine,
1146:     }
1147: 
1148: 
1149: def sha256_of(path: Path) -> dict:
1150:     """The pin of a file: SHA-256 and length with CRLF folded to LF.
1151: 
1152:     The house rule is that the SHA of a delivery is `git show HEAD:<path>` —
1153:     the blob in the history, not the bytes on this disk.  The repo checks out
1154:     with LF (`.gitattributes`) while Windows text mode writes CRLF, so one and
1155:     the same file has two SHAs depending on whether it was just written or just
1156:     checked out.  A pin that cannot be reproduced from the repository is not a
1157:     pin: folding CRLF to LF makes it one number in a working tree and in a
1158:     fresh worktree alike.
1159:     """
1160:     raw = path.read_bytes().replace(b"\r\n", b"\n")
1161:     return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
1162: 
1163: 
1164: def kais_generation() -> dict:
1165:     """The generation of the КАИС extract against the update (К6-3 of В3).
1166: 
1167:     Measured, never assumed, and never a live fetch: the published date is the
1168:     name of the folder, the download date is inside its own manifest, and the
1169:     generation the house builds on is the one `src/generation.py` publishes.
1170:     """
1171:     out = {"generation": None, "published": None, "fetched": None,
1172:            "phase0_quoted": "12.05.2026",
1173:            "verdict": None}
1174:     try:
1175:         sys.path.insert(0, str(Path(__file__).resolve().parent))
1176:         import generation                                   # noqa: E402
1177:         out["generation"] = generation.DEFAULT
1178:         gen = generation.GENERATIONS[generation.DEFAULT]
1179:         out["published"] = gen.label
1180:         out["expected_buildings"] = gen.expected_buildings
1181:     except Exception as e:                                   # pragma: no cover
1182:         out["verdict"] = f"поколението не се чете: {e}"
1183:         return out
1184:     if KAIS_MANIFEST.exists():
1185:         man = json.loads(KAIS_MANIFEST.read_text(encoding="utf-8"))
1186:         out["fetched"] = man.get("fetched")
1187:         out["source"] = man.get("source")
1188:     out["verdict"] = (
1189:         "поколението 24.07.2026 е ПО-НОВО от обновата, която ФАЗА_0 цитира "
1190:         "(ZIP 12.05.2026) → пресваляне не се налага по критерия на К6-3. "
1191:         "Дали КАИС е публикувал НОВА извадка след 24.07 не се проверява оттук: "
1192:         "това е мрежова заявка, а мярката не гадае."
1193:     )
1194:     return out
1195: 
1196: 
1197: def build_inputs(book: LocationBook) -> dict:
1198:     """The pinned inputs of лот В — the BASE that G-ISO measures against.
1199: 
1200:     `legacy_zones` is FROZEN: the zone word each row was delivered with before
1201:     this lot.  It is captured once and preserved verbatim on every later run,
1202:     because it is history, not a computation — recomputing it would need the
1203:     very ladder this lot retired.
1204:     """
1205:     old = json.loads(INPUTS.read_text(encoding="utf-8")) if INPUTS.exists() else {}
1206:     legacy = old.get("legacy_zones") or {}
1207:     captured = old.get("legacy_captured_from") or old.get("_captured_from") or {}
1208:     if not legacy:
1209:         die(f"{INPUTS.name} е без замразения блок `legacy_zones` — старите "
1210:             f"зонови думи са история, не сметка, и не се изчисляват наново")
1211:     missing = sorted(set(book.rows) - set(legacy))
1212:     extra = sorted(set(legacy) - set(book.rows))
1213:     if missing or extra:
1214:         die(f"`legacy_zones` не покрива точно 375-те записа: липсват "
1215:             f"{len(missing)}, излишни {len(extra)}")
1216:     master = json.loads((ROOT / "data" / "places.json").read_text(encoding="utf-8"))
1217:     return {
1218:         "_meta": {
1219:             "what": "закованите входове на ЛОТ 1в-В (P6) и BASE-ът на G-ISO",
1220:             "plan": "Fire_Varna/docs/plans/ПЛАН_ЛОТ1в-В_кварталите.md §3ж S5",
1221:             "command": "python src/fire_varna_locations.py --inputs",
1222:             "rule_base": "лот В е Fire-export-only: петте изворни файла, "
1223:                          "майсторът (576 реда) и двата генерирани артефакта "
1224:                          "излизат от прогона БАЙТ ЗА БАЙТ същите; различен "
1225:                          "байт = STOP (`src/qa_fire_varna_location_isolation.py`)",
1226:             "rule_output": "output/ е на паралелната тема: чете се, не се пише",
1227:             "rule_sha": "всеки SHA тук е SHA-то на LF-нормализираните байтове "
1228:                         "— тоест на блоба (`git show HEAD:<път>`), а не на "
1229:                         "байтовете на този диск; пин, който не се възпроизвежда "
1230:                         "от репото, не е пин",
1231:             "rule_legacy": "`legacy_zones` е замразена история — доставената "
1232:                            "зона на всеки ред ПРЕДИ лот В; не се изчислява "
1233:                            "наново, само се пази",
1234:             "rule_m6": "суровият НТР файл и двете ЗАТВОРЕНИ таблици на М6 се "
1235:                        "пинват тук и се проверяват при ВСЯКО пускане "
1236:                        "(`LocationBook._check_pins`); разлика = СТОП. Таблица, "
1237:                        "която решава, е вход като всеки друг файл",
1238:             "contains_cadastral_id": False,
1239:         },
1240:         "legacy_captured_from": captured,
1241:         "base": {
1242:             "sources": {p: sha256_of(ROOT / p) for p in BASE_SOURCES},
1243:             "generated": {p: sha256_of(ROOT / p) for p in BASE_GENERATED
1244:                           if (ROOT / p).exists()},
1245:             "master_rows": len(master["places"]),
1246:         },
1247:         "inputs": {p: sha256_of(ROOT / p) for p in RECORDED_INPUTS
1248:                    if (ROOT / p).exists()},
1249:         "registry": {"path": REGISTRY.as_posix(), **sha256_of(REGISTRY),
1250:                      "entries": book.reg.n_entries},
1251:         "ntr": {"path": NTR_RAW.relative_to(ROOT).as_posix(), **book.ntr_stats},
1252:         "m6_tables": dict(book.table_shas),
1253:         "kais_generation": kais_generation(),
1254:         "legacy_zones": {k: legacy[k] for k in sorted(legacy)},
1255:     }
1256: 
1257: 
1258: def main(argv: list[str]) -> None:
1259:     ap = argparse.ArgumentParser()
1260:     ap.add_argument("--ledger", action="store_true",
1261:                     help="пише маскирания ledger на 375-те")
1262:     ap.add_argument("--inputs", action="store_true",
1263:                     help="пише закованите входове (BASE-ът на G-ISO)")
1264:     a = ap.parse_args(argv)
1265: 
1266:     book = load()
1267:     n = len(book.rows)
1268:     q = sum(1 for r in book.rows.values() if r["quarter"])
1269:     loc = sum(1 for r in book.rows.values() if r["locality"])
1270:     print(f"{n} записа · квартал {q} · допълнително {loc} · "
1271:           f"район {n - len(book.quarantine)}")
1272:     by_src: dict[str, int] = {}
1273:     for r in book.rows.values():
1274:         if r["quarter"]:
1275:             code = r["quarter"]["src"]
1276:             by_src[code] = by_src.get(code, 0) + 1
1277:     print("  кварталът по извор: " + " · ".join(
1278:         f"{k} {v}" for k, v in sorted(by_src.items())))
1279:     if book.quarantine:
1280:         print(f"  КАРАНТИНА: {len(book.quarantine)} реда без валиден район")
1281:         for r in book.quarantine[:5]:
1282:             print(f"    {r['name']} — {r['why']}")
1283:     changed = [r for r in book.rows.values()
1284:                if r["old_zone"] != (r["quarter"]["name"] if r["quarter"]
1285:                                     else f"район {r['district']['name']}")]

 succeeded in 3ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import json,subprocess,hashlib,collections
r=Path('C:/git/varna_3d')
relpaths=['docs/activeContext.md','scratch/refactor/_addr/lot1v_locations_375.json','data/place_identity.json','data/fire_varna_places.json','data/fire_varna_hotels.json']
for s in sorted(relpaths):
 p=r/s
 print(f'INVENTORY {p.as_posix()} exists={p.exists()} bytes={p.stat().st_size if p.exists() else 0}')
s='scratch/refactor/_addr/lot1v_locations_375.json'
rev=subprocess.check_output(['git','-C',str(r),'rev-parse','HEAD'],text=True).strip()
last=subprocess.check_output(['git','-C',str(r),'log','-1','--format=%H %an','HEAD','--',s],text=True).strip()
b=subprocess.check_output(['git','-C',str(r),'show',rev+':'+s])
w=(r/s).read_bytes(); d=json.loads(b)
print('HEAD',rev,'last_ledger_commit',last,'blob_oid',subprocess.check_output(['git','-C',str(r),'rev-parse',rev+':'+s],text=True).strip(),'sha256',hashlib.sha256(b).hexdigest(),'worktree_equal_LF',b==w.replace(b'\\r\\n',b'\\n'))
print('ledger_top_keys',list(d),'meta_keys',list(d.get('_meta',{})))
rows=d.get('rows',[])
print('ledger_rows',len(rows),'row_keys',list(rows[0]),'written',sum(bool(x.get('quarter')) for x in rows))
for s in ['data/place_identity.json','data/fire_varna_places.json','data/fire_varna_hotels.json','data/fire_varna_location_inputs.json']:
 d=json.loads((r/s).read_text(encoding='utf-8'))
 print(s,'top_keys',list(d),'meta_keys',list(d.get('_meta',{})))
 for k,v in d.items():
  if isinstance(v,list) and v and isinstance(v[0],dict):
   print('rows',k,len(v),'latlon',sum('lat' in x and 'lon' in x for x in v),'first_row_keys',list(v[0]))
 if s.endswith('inputs.json'):
  print('input_keys',list(d.get('inputs',{})))
p=Path('scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json');d=json.loads(p.read_text(encoding='utf-8'))
print('decisions STRUCTURE ONLY top',list(d),'meta_keys',list(d.get('_meta',{})))
for k,v in d.items():
 if isinstance(v,list): print('array',k,'len',len(v),'row_keysets',collections.Counter(tuple(sorted(x)) for x in v if isinstance(x,dict)))
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 exited 1 in 28ms:
fatal: detected dubious ownership in repository at 'C:/git/varna_3d'
'C:/git/varna_3d' is owned by:
	PETAR/Petar (S-1-5-21-1992376794-12164101-10249461-1001)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/varna_3d
INVENTORY C:/git/varna_3d/data/fire_varna_hotels.json exists=True bytes=148685
INVENTORY C:/git/varna_3d/data/fire_varna_places.json exists=True bytes=122089
INVENTORY C:/git/varna_3d/data/place_identity.json exists=True bytes=194672
INVENTORY C:/git/varna_3d/docs/activeContext.md exists=True bytes=15488
INVENTORY C:/git/varna_3d/scratch/refactor/_addr/lot1v_locations_375.json exists=True bytes=554596
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
  File "C:\Program Files\Python310\lib\subprocess.py", line 420, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "C:\Program Files\Python310\lib\subprocess.py", line 524, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['git', '-C', 'C:\\git\\varna_3d', 'rev-parse', 'HEAD']' returned non-zero exit status 128.

codex
Координати има в днешния износ: `comparison_columns()` ги чете от двата export файла. Но D7 изрично забранява този източник за полигонното присвояване, така че резервният път на Б2 противоречи на ADR. Отделно G4 изисква комит от Петър; стейджнат файл с правилен SHA не изпълнява това условие.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import json,subprocess,hashlib,collections
r=Path('C:/git/varna_3d'); git=['git','-c','safe.directory=C:/git/varna_3d','-C',str(r)]
s='scratch/refactor/_addr/lot1v_locations_375.json'
rev=subprocess.check_output(git+['rev-parse','HEAD'],text=True).strip()
last=subprocess.check_output(git+['log','-1','--format=%H %an','HEAD','--',s],text=True).strip()
b=subprocess.check_output(git+['show',rev+':'+s]);w=(r/s).read_bytes(); d=json.loads(b)
print('HEAD',rev,'last_ledger_commit',last,'blob_oid',subprocess.check_output(git+['rev-parse',rev+':'+s],text=True).strip(),'sha256',hashlib.sha256(b).hexdigest(),'worktree_equal_LF',b==w.replace(b'\\r\\n',b'\\n'))
print('ledger_top_keys',list(d),'meta_keys',list(d.get('_meta',{})))
rows=d.get('rows',[])
print('ledger_rows',len(rows),'row_keys',list(rows[0]),'written',sum(bool(x.get('quarter')) for x in rows))
for s in ['data/place_identity.json','data/fire_varna_places.json','data/fire_varna_hotels.json','data/fire_varna_location_inputs.json']:
 d=json.loads((r/s).read_text(encoding='utf-8'))
 print(s,'top_keys',list(d),'meta_keys',list(d.get('_meta',{})))
 for k,v in d.items():
  if isinstance(v,list) and v and isinstance(v[0],dict): print('rows',k,len(v),'latlon',sum('lat' in x and 'lon' in x for x in v),'first_row_keys',list(v[0]))
 if s.endswith('inputs.json'): print('input_keys',list(d.get('inputs',{})))
p=Path('scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json');d=json.loads(p.read_text(encoding='utf-8'))
print('decisions STRUCTURE ONLY top',list(d),'meta_keys',list(d.get('_meta',{})))
for k,v in d.items():
 if isinstance(v,list): print('array',k,'len',len(v),'row_keysets',collections.Counter(tuple(sorted(x)) for x in v if isinstance(x,dict)))
print(subprocess.check_output(git+['status','-sb','-uno'],text=True))
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 succeeded in 93ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
HEAD 8d60aebb365fb8e74ccc863d3b3db90b74180a3b last_ledger_commit 31db7b9d68c9bcbde7604c6c2a3627310f828ec4 Petar1984 blob_oid c1b81efc5129ac1c1e57c619ea31077423715141 sha256 d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075 worktree_equal_LF True
ledger_top_keys ['_meta', 'rows', 'quarantine'] meta_keys ['what', 'plan', 'command', 'private', 'masked', 'rule', 'rule_m6', 'pins_m6', 'comparison_only', 'district_polygon_check', 'counts', 'pending_signature', 'fix_sample_why', 'answered_question_map_label']
ledger_rows 375 row_keys ['place_id', 'file', 'name', 'kind', 'old_zone', 'new_zone', 'quarter', 'district', 'locality', 'kais_quar_raw', 'kais_reg_raw', 'kais_mode', 'registry_segments', 'witness', 'channels', 'kais_addr_raw', 'pending_signature', 'signed_vs_witness', 'dropped', 'note', 'compare_layer_polygon', 'compare_drawn_hull', 'compare_drawn_status'] written 201
data/place_identity.json top_keys ['_meta', 'objects', 'sites', 'retired'] meta_keys ['what', 'baseline', 'command', 'private', 'rule_id', 'rule_anchor', 'rule_key', 'rule_migration', 'rule_site', 'projection', 'engine', 'sources', 'counts']
rows objects 375 latlon 0 first_row_keys ['place_id', 'key', 'file', 'name', 'kind', 'zone', 'site_id', 'matched_by', 'evidence']
rows sites 3 latlon 0 first_row_keys ['site_id', 'type', 'board_ref', 'why', 'members_by_name', 'members']
rows retired 8 latlon 0 first_row_keys ['place_id', 'key', 'file', 'name', 'kind', 'zone', 'site_id', 'evidence', 'status', 'reason', 'merged_into']
data/fire_varna_places.json top_keys ['_meta', 'places'] meta_keys ['generated', 'count', 'by_kind', 'by_zone_src', 'licence_osm', 'licence_registry', 'licence_wikidata', 'licence_address', 'excluded']
rows places 150 latlon 150 first_row_keys ['name', 'kind', 'lat', 'lon', 'zone', 'quarter', 'district', 'locality', 'src', 'old_names', 'old_names_src', 'status', 'address']
data/fire_varna_hotels.json top_keys ['_meta', 'hotels'] meta_keys ['generated', 'count', 'by_zone_src', 'licence', 'licence_osm', 'licence_address', 'excluded']
rows hotels 225 latlon 225 first_row_keys ['name', 'kind', 'no_uin', 'cat', 'beds', 'lat', 'lon', 'zone', 'quarter', 'district', 'locality', 'uins', 'old_names', 'old_names_src', 'status', 'src', 'address']
data/fire_varna_location_inputs.json top_keys ['_meta', 'legacy_captured_from', 'base', 'inputs', 'registry', 'ntr', 'm6_tables', 'kais_generation', 'legacy_zones'] meta_keys ['what', 'plan', 'command', 'rule_base', 'rule_output', 'rule_sha', 'rule_legacy', 'rule_m6', 'contains_cadastral_id']
input_keys ['data/place_identity.json', 'data/registry_manifest.json', 'web/varna_buildings_info.json']
decisions STRUCTURE ONLY top ['schema_version', 'board', 'based_on', 'inputs', 'exported_at', 'changes', 'decisions'] meta_keys []
array changes len 5 row_keysets Counter()
array decisions len 68 row_keysets Counter({('choice', 'code', 'decided_at', 'decided_by', 'display', 'kind', 'reason', 'wm_id', 'wm_polygon_sha256', 'wm_title'): 66, ('choice', 'code', 'decided_at', 'decided_by', 'display', 'kind', 'reason', 'streets', 'wm_id', 'wm_polygon_sha256', 'wm_title'): 1, ('alias_of', 'choice', 'code', 'decided_at', 'decided_by', 'display', 'kind', 'reason', 'wm_id', 'wm_polygon_sha256', 'wm_title'): 1})
## rezhimi...origin/rezhimi [ahead 41]
 M scratch/place_bodies/qa_place_bodies.md


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=195; Get-Content -LiteralPath '"'C:/git/varna_3d/src/place_identity.py' -Encoding UTF8 | Select-Object -Skip 195 -First 45 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }
$i=580; Get-Content -LiteralPath '"'C:/git/varna_3d/src/place_identity.py' -Encoding UTF8 | Select-Object -Skip 580 -First 48 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 37ms:
196: 
197:     groups: dict[str, list[dict]] = {}
198:     for r in recs:
199:         groups.setdefault(r["base"], []).append(r)
200:     for base, members in groups.items():
201:         if len(members) == 1:
202:             members[0]["key"] = base
203:             continue
204:         for n, r in enumerate(sorted(members, key=lambda m: (m["lat"], m["lon"])), 1):
205:             r["key"] = f"{base}#{n}"
206:     recs.sort(key=lambda r: r["key"])
207:     keys = [r["key"] for r in recs]
208:     if len(set(keys)) != len(keys):
209:         die("ключовете на износа не са уникални след разковничето")
210:     return recs
211: 
212: 
213: # =============================================================================
214: # The geometry: the nearest КАИС body, every ring
215: # =============================================================================
216: LAT0, LON0 = 43.22, 27.92
217: M_PER_DEG = 111320.0
218: 
219: 
220: def make_projection():
221:     """(lon, lat) → метри, и името на проекцията.
222: 
223:     EPSG:32635 (UTM 35N) през `pyproj`; ако `pyproj` липсва — локалната
224:     equirectangular около (43.22, 27.92) с 111 320 m/градус и `cos(lat)` по x,
225:     СЪЩОТО приближение, с което конвейерът мери своите 60 m
226:     (`export_fire_varna_places.py:dist_m`).  Разликата между двете върху Варна
227:     е под 0.1 % и не мести нито един праг.
228:     """
229:     try:
230:         from pyproj import Transformer
231:         t = Transformer.from_crs("EPSG:4326", "EPSG:32635", always_xy=True)
232:         return (lambda lon, lat: t.transform(lon, lat)), "EPSG:32635 (pyproj)"
233:     except ImportError:
234:         kx = M_PER_DEG * math.cos(math.radians(LAT0))
235:         return ((lambda lon, lat: ((lon - LON0) * kx, (lat - LAT0) * M_PER_DEG)),
236:                 "equirectangular @ (43.22, 27.92), 111 320 m/градус — pyproj липсва")
237: 
238: 
239: class Bodies:
240:     """Индекс над `web/varna_buildings_3d.geojson` — 80 497 полигона.
581:                 f"„shared“ не бива да носи такъв")
582:         members: list[str] = []
583:         for n in names:
584:             got = by_name.get(n) or []
585:             if len(got) != 1:
586:                 die(f"декларираната площадка „{why[:40]}…“ иска ЕДИН „{n}“ в "
587:                     f"износа, а той е {len(got)} пъти")
588:             members.append(got[0]["place_id"])
589:         sid = was.get(tuple(names)) or str(uuid.uuid4())
590:         sites.append({"site_id": sid, "type": decl["type"],
591:                       "board_ref": decl["board_ref"], "why": why,
592:                       "members_by_name": list(names), "members": members})
593:     ids = [s["site_id"] for s in sites]
594:     if len(set(ids)) != len(ids):
595:         die("две декларирани площадки носят едно `site_id`")
596:     return sites
597: 
598: 
599: def build_identity() -> dict:
600:     """Присвоява липсващите id-та и записва файла; върнатият doc е записаният."""
601:     recs = load_union()
602:     old = json.loads(IDENTITY.read_text(encoding="utf-8")) if IDENTITY.exists() else {}
603:     olds = list(old.get("objects") or [])
604:     retired_before = list(old.get("retired") or [])
605:     seen_keys: set[str] = set()
606:     for entry in olds + retired_before:
607:         if entry["key"] in seen_keys:
608:             die(f"ключът „{entry['key']}“ стои два пъти в {IDENTITY.name}")
609:         seen_keys.add(entry["key"])
610:         if not UUID4.match(entry["place_id"]):
611:             die(f"„{entry['key']}“ носи id, което не е UUID4: {entry['place_id']}")
612: 
613:     bodies = Bodies()
614:     for r in recs:
615:         i, d = bodies.nearest(r["lat"], r["lon"])
616:         r["kais_i"], r["kais_d_m"] = i, round(d, 2)
617:         r["anchors"] = anchors_of(r["file"], r["name"], r["zone"], r["rid"],
618:                                   r["uins"], i)
619:     for e in olds:
620:         ev = e.get("evidence") or {}
621:         e["anchors"] = anchors_of(e["file"], e["name"], e["zone"],
622:                                   ev.get("rid"), list(ev.get("uins") or []),
623:                                   ev.get("kais_i"))
624: 
625:     # --- МИГРАЦИИТЕ, преди котвите ------------------------------------------
626:     by_key = {e["key"]: j for j, e in enumerate(olds)}
627:     rec_of_name: dict[tuple[str, str], list[int]] = {}
628:     for k, r in enumerate(recs):

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=100; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | Select-Object -Skip 100 -First 40 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 26ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import subprocess,hashlib,json
from pathlib import Path
git=['git','-c','safe.directory=C:/git/varna_3d','-C','C:/git/varna_3d'];r='31db7b9d68c9bcbde7604c6c2a3627310f828ec4'
for s in ['scratch/refactor/_addr/lot1v_locations_375.json','data/fire_varna_places.json','data/fire_varna_hotels.json']:
 b=subprocess.check_output(git+['show',r+':'+s]); h=subprocess.check_output(git+['show','HEAD:'+s]); print(s,'equal_at_last_ledger_vs_HEAD',b==h,'sha256',hashlib.sha256(b).hexdigest())
print(subprocess.check_output(git+['show','-s','--format=%H %cs %an %s',r],text=True,encoding='utf-8'))
for s in ['data/fire_varna_location_inputs.json','scratch/refactor/_addr/lot1v_locations_375.json']:
 lines=(Path('C:/git/varna_3d')/s).read_text(encoding='utf-8').splitlines()
 for i,line in enumerate(lines,1):
  if any(x in line for x in ['\"inputs\":','\"rule_sha\":','\"data/place_identity.json\"','\"pins_m6\":','\"counts\":']): print(s,i,line[:200])
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 | Select-Object -First 32 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 17ms:
1: # Амандамент №2 към ПЛАН „Границите“ v2 — **ревизия 2** (06.09.2026, ~01:13 **по часовника на машината**) — след присъдата на Петър, след намирането на човешките полигони (Уикимапия), след одита в три лещи и след оборването от Кими (К15–К20) и Astra (S14–S19). Статус: **за Gate 1 — едно четиво за Петър. НЕПОДПИСАН.** (Ревизия 2б, ~01:24: К21 на Кими и проверката S20 на Astra са вградени — виж дневника.)
2: 
3: Нов датиран файл по §0.2 на `docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md:9`. Не редактира плана v2, ADR 010 и амандамент №1; казва какво се променя в тях и защо. Не открива лота, не пипа живата карта, не комитва геометрия.
4: 
5: ## Дневник на ревизиите
6: 
7: - **Ревизия 1** (06.09, ~00:40) — вътрешен одит в три лещи (Opus). Приложено: мярка само върху **замразено** тяло (§0), поправка на собствената мярка („1 обект / `_meta.note`“ е невярно), думите на Петър от ~00:50 като ВЗЕТО решение №1, стълбата v3 с отделно стъпало (1-б), G25–G28. Отхвърлено: спиране на самото събиране — то е поръчано от Петър и спирането му би оставило твърдението „20+ квартала“ непроверено.
8: - **Ревизия 2** (тази, 06.09, ~01:00–01:13) — след двете външни присъди: **Кими К15–К20** (лицензна леща, `scratch/places_search/granitsi_am2_kimi_K15-K20_06.09.md`) и **Astra S14–S19** (механична леща, `scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md`). Преработени: §2, §3 (изцяло), §4 (редът и договорът на решенията), §5, §6, §7; §8 сменя „чака“ с **записаните присъди** и списъците приложено/отхвърлено. Текстът е на Opus-планировчик по двете присъди; архитектът добави в §3.4(а) и §3.5 прочетените след това условия на Уикимапия (`scratch/places_search/wikimapia_terms_2026-09-06.md`). **Статусът НЕ се променя: пак „за Gate 1“, пак неподписан.** Записаните думи и решения на Петър запазват смисъла си дословно.
9: - **Ревизия 2а** (06.09, ~01:16) — **Кими К21** (`scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md`) върху попълнените входове: `verdict = allowed_with_conditions` със седем условия; най-тежкото — **публичната атрибуция е задължителна по ToS §1.G** (договорна клауза, независима от лицензния анализ по §3.2). Променени: §3.3, §3.5, G27, G28, §7 (ново решение 8), §8.
10: - **Ревизия 2б** (06.09, ~01:24) — **Astra S20** (`scratch/places_search/granitsi_am2_astra_S20_verify_06.09.md`): S14/S16/S17/S18 RESOLVED, S15/S19 PARTIALLY, четири нови дефекта. Поправени тук: (1) публичният път до URL-а на обекта — договорена карта `_meta.quarter_attribution[code]`; (2) затвореният `_meta` става **10 ключа** с изрична промяна на D13 и **подредена доставка** (varna_3d първо, Fire_Varna после — не „в същия комит“ през две репа); (3) редът на ходовете включва Г1-б и независимия одит преди Г2; (4) решение 7 назовава генератора; (5) S15-остатъкът — правилото за `MultiPolygon` и трите SHA обхвата са записани дословно.
11: 
12: ## 0 · Червен ред преди всичко останало
13: 
14: Тече `wikimapia_sweep.py` (обход по `place.getnearest`, 163 начални точки + мрежа 500 m, ~28 s на заявка), който събира полигони в `scratch/boundary_gallery/granitsi_preview_05.09/wikimapia_quarters.geojson`. Файлът РАСТЕ — **към 01:10: 86 от 163 начални точки, 180 полигона с квартална големина; мрежовият проход (504 точки) е още предстоящ.** Това е СЪБИРАНЕ, не мярка, и е поръчано от Петър („нека ползваме тях“). Обходът се оставя да завърши; **но нищо не се мери, не се показва в борд и не се цитира, преди тялото да бъде замразено**: копие с дата, `sha256` на целия файл, брой обекти, записани в мярката. **Нито едно число в този амандамент не е цитирано като окончателно.**
15: 
16: **Измерено поведение на API-то (06.09).** С ключ `example` работят `place.getbyid` и `place.getnearest` (`count=100`, `data_blocks=geometry,location`); `place.getbyarea` (със и без `coordsby=bbox`, със и без `category=4621 „квартал“`), `place.search` и филтрите по категория връщат `found=0`; скорост ~една заявка на 28 s. Следствие: **обходът е само-`getnearest`** — площен обход няма как да се направи, значи пълнотата се доказва по кодове (М2-1б), не по площ.
17: 
18: **Поправка на собствена мярка.** Ранната чернова твърдеше „1 обект, `_meta.note`: дроселиран ключ“. И двете са неверни: обектите бяха деветдесет по време на одита, а `_meta` носи ключове `{attribution, licence, min_km2, not_for_publication, what}` — ключ `note` няма. Правилото: **входовете на борда са пиннати снапшоти, не течащи файлове.**
19: 
20: ## 1 · Какво реши Петър
21: 
22: Дословно: „нищо няма да чертая аз“ · за КАИС-изведените граници — „много са объркани… направо са грешни“ · „данните от OSM са по-точни; маркирай кварталите според тях; аз ще потвърдя“ · за хибрида — „много е зле… провери във форуми“ · и върху полигона на кв. Кайсиева градина от Уикимапия (id 1851926, CC BY-SA 3.0, 0,42 km²): **„точно това е границата“**.
23: 
24: **Какво отпада.** Целият производен клон — обвивките от юли, КАИС-изведените полигони, OSM-Voronoi, уличният вариант, хибридът. Отпада и **чертането** като метод: план v2 §2 (Г1 → Г2, `ПЛАН_ЛОТ_Границите_v2_05.09.md:104-146`) стъпваше върху „Петър чертае“.
25: 
26: **След одита (06.09, ~00:50) Петър добави:** „прегледах районите от уикимапиа — доста добре съм — нека ползваме тях“. Той е прегледал сам кварталите на сайта — това е неговата извадка по собствения му протокол и решение №1 е ВЗЕТО от него, не чака. Бордът все пак започва с извадката от §7 т. 1, защото там са измерените дефекти.
27: 
28: **Какво НЕ следва автоматично.** Едно потвърждение на екрана не е присъда по квартал в нашия регистър: всяко „да“ се дава по квартал, върху замразения полигон, със записан `wm_id`.
29: 
30: ## 2 · Стълбата на изворите v3 — за ГРАНИЦАТА
31: 
32: Номерацията на D0 (`010_signed_quarter_boundaries.md:36`) се пренарежда: степени (1) и (2) определят **линията**; написаният извор за **мястото** (REG/KAIS/НТР, рангове 0–2) и `POST-2018` остават непроменени.

 succeeded in 135ms:
scratch/refactor/_addr/lot1v_locations_375.json equal_at_last_ledger_vs_HEAD True sha256 d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075
data/fire_varna_places.json equal_at_last_ledger_vs_HEAD False sha256 35aaf0cd5811e3e56181912f280e3beae39e8c5f1867898e023ca00a11d3cbc9
data/fire_varna_hotels.json equal_at_last_ledger_vs_HEAD False sha256 c30f7333d1a9a845b90ca46db0e41496cb722aa2640b6c862ccb8b211bd30100
31db7b9d68c9bcbde7604c6c2a3627310f828ec4 2026-09-05 Petar1984 места: подписаните квартали по place_id; неподписан сблъсък = pending_signature, не монета и не мълчание (P7-в)

data/fire_varna_location_inputs.json 8   "rule_sha": "всеки SHA тук е SHA-то на LF-нормализираните байтове — тоест на блоба (`git show HEAD:<път>`), а не на байтовете на този диск; пин, който не се възпроизвежда от репото, не е пин",
data/fire_varna_location_inputs.json 49  "inputs": {
data/fire_varna_location_inputs.json 50   "data/place_identity.json": {
scratch/refactor/_addr/lot1v_locations_375.json 10   "pins_m6": {
scratch/refactor/_addr/lot1v_locations_375.json 29   "counts": {

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/varna_3d/docs/activeContext.md' -Encoding UTF8 -TotalCount 45" in C:\git\Fire_Varna
 succeeded in 0ms:
# Varna 3D — входна точка

**Дата:** 02.09.2026 · **последно сверено срещу комит** 9f55c08 (`rezhimi`; напред спрямо `origin/rezhimi` с комитите на плана от 01.09 до пуша на Петър — таблицата) · сверил: Opus (executor), одитирал: <одитор> · подпис: __
> Всяко число тук е изходът на командата до него, пусната на датата горе (`verify_numbers.py` го проверява). Число без команда не влиза.
> Хрониката по дати е замразена в [СЪСТОЯНИЕ.md](СЪСТОЯНИЕ.md) (до 01.09.2026). Изворите са описани в [../DATA.md](../DATA.md) (мерени 30.07.2026).

## Какво е това
Триизмерен модел на Варна от КАИС „Отворени данни" — стои НАД `Varna_buildings` (данните за сградите) и `Fire_Varna` (хидрантите), чете техните изходи, не ги пипа. Публикуваното е `web/` (карта: `Varna 3D.bat` → http://127.0.0.1:8791).

## Стволът
- Работен клон: `rezhimi`. Клонът по подразбиране в GitHub: `main` (изравнен с `origin/rezhimi` в ЛОТ 3 на плана от 01.09; проследява `origin/main`; занапред — В-1/Р-12).

## Тема „търговско-обществените сгради" (03.09.2026, сесия git-65 / Fable) — сурови данни във файл, нищо в картата
- **Състояние:** Ф0 мярка (`b8141ec`) → план v1.1 подписан по думите на Петър (`docs/plans/ПЛАН_търговско-обществени.md`, §11 амандаменти) → лотове А0/А1 (`c74bad0`, `a7f1a68`), А4 (`0ccc525`), А3 (`12b082f`), А5 + бордът (`7a4bed5`). По амандамент №1 („за сега инфото на файл") `build_places.py` НЕ е пускан, износ към Fire_Varna няма; А2/А6/Б/В чакат преценката на Петър. Докладът: [audits/ДОКЛАД_03.09_търговско-обществени.md](audits/ДОКЛАД_03.09_търговско-обществени.md); бордът: [audits/БОРД_търговско-обществени_2026-09-03.md](audits/БОРД_търговско-обществени_2026-09-03.md).
- **Живи числа на темата** (03.09.2026):

| Какво | Стойност | Команда |
|---|---|---|
| OSM места (сурови) | 1848 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_public_osm_places.json',encoding='utf-8'))['places']))"` |
| НТР ЗХР места (сурови) | 373 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_ntr_zhr_places.json',encoding='utf-8'))['places']))"` |
| Wikidata места (сурови) | 44 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_wikidata_places.json',encoding='utf-8'))['places']))"` |
| официални сайтове (Сол, сурови) | 5 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_web_places.json',encoding='utf-8'))['places']))"` |
| тела в геофайла / с име | 10367 / 1538 | `PYTHONIOENCODING=utf-8 python src/build_public_buildings_geojson.py \| grep '^bodies'` (изходът е в `output/`, извън git) |
| мастерът `places.json` недокоснат от темата | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |

## Тема „ЛОТ 1в за Fire_Varna" (04.09.2026, сесия git-08) — имената, адресите, кварталите
- **Състояние:** лот А (псевдонимите с извор, `1d5ec9a`, `859dbe5`) → лот Б (адресът с извор на всеки запис, `25a6d79`) → **лот В (P6): кварталът, районът и допълнителното с извор.** Планът и подписът са на Fire_Varna: `Fire_Varna/docs/plans/ПЛАН_ЛОТ1в-В_кварталите.md` (Gate 1-В подписан, §3з); ADR `Fire_Varna/docs/decisions/008_places_aliases_and_addresses.md`. Във Fire_Varna не е пипано нищо оттук — прави се САМО артефактът.
- **Правилото (§3г, подписано):** кварталът е САМО жилищно ниво по регистъра на кварталите и САМО с човешки написан извор — регистровият адресен сегмент (`REG`) или кадастралният квартал на закотвеното тяло (`KAIS`); без извор → честно „район X". Районът идва САМО от КАИС `reg` (петте градски района, затворен списък). Допълнителното (`locality`) носи промишлените зони, парковете и местностите. **Нищо нарисувано и нищо OSM-производно не решава** — обвивките, етикет-точките и районният полигон са само сравнителни колони в маскирания ledger `../scratch/refactor/_addr/lot1v_locations_375.json`.
- **Изолация:** новата стълба (`src/fire_varna_locations.py`) е Fire-export-only. Глобалната `src/place_zones.py`, майсторът и артефактите на паралелната тема не мърдат — доказва го `src/qa_fire_varna_location_isolation.py` (G-ISO) срещу закованите входове `data/fire_varna_location_inputs.json`.
- **Чака подпис:** манифестът old → new (209 реда) преди замразяването на референцията във Fire_Varna; фикс-извадката за окото на Петър е в ledger-а.
- **Хигиена след одита на лот В (P6-б):** SHA-то на доставка се смята върху LF-нормализирани байтове — тоест е SHA-то на блоба (`git show HEAD:<път>`), не на байтовете на този диск (прясно записаният износ е CRLF, прясно изтегленият — LF); затова гейтът (g) на `qa_place_zone_aliases.py` и G-ISO отговарят еднакво в работното дърво и в чист worktree. `data/registry_manifest.json` е комитнат (22 стойности `zone` в `grandfathered`/`board_queue`; секцията `rows` е идентична с P6), затова пинът му вече сочи блоб от историята. Ledger-ът носи `_meta.fix_sample_why` (доводите се ИЗВЕЖДАТ от полетата на реда) и `_meta.open_question_map_label`: 6 реда губят квартала си по `map_label:false`, 5 от тях с човешки написан регистров сегмент (ДГ 32, ДГ 36) — за решение на Петър.
- **Живи числа на темата** (04.09.2026):

| Какво | Стойност | Команда |
|---|---|---|
| доставени записа (места + хотели) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| с квартал (REG 34 · KAIS 94 · подписан override 12) | 140 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| с допълнително местоположение | 8 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| с район (100 % покритие, нула карантина) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| сменят зона спрямо доставеното (манифестът) | 209 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| tail -1` |
| G-ISO: глобалната стълба и чуждата тема непокътнати | минава | `PYTHONIOENCODING=utf-8 python src/qa_fire_varna_location_isolation.py \| tail -1` |
| самоличности с непроменен `place_id` | 375 (0 нови) | `PYTHONIOENCODING=utf-8 python src/place_identity.py \| grep 'обекта'` |

## Отворена тема (към 01.09.2026, по СЪСТОЯНИЕ.md § 01.09)
- **Секции от апартаменти v1.3** — одит ГОДНО, **чака Gate 2** върху [извадката](../scratch/refactor/_addr/ПРЕГЛЕД_извадка_секции_01.09.md) (броят места е по документа; непроверено 01.09.2026); след „давай" — Ф4-сливане. Дали Gate 2 е даден след 01.09: непроверено (01.09.2026), В-2.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --files C:/git/varna_3d/src --glob '*fire_varna*' --glob '*place_categories*' --glob '*p8a*' --glob '*quarters*' --glob '*measure_place_coords*' --glob '*measure_polygon_assign*' --glob '*measure_kais*' --glob '*written_quarters*' --glob '*quarter*' | Sort-Object" in C:\git\Fire_Varna
 succeeded in 9ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=85; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 | Select-Object -Skip 85 -First 39 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
86: | Г2-б решения | Fire_Varna | **Petar1984** | `docs/granitsi/granitsi_decisions_<ISO дата>.json` (проследен, нула координати) | `data: signed quarter decisions <дата>` |
87: | Г2-в сглобяване | varna_3d | Claude Executor → комитът на geojson-а е на **Petar1984** | `src/build_quarters_signed.py`; после `data/quarters_signed.geojson` | `build: assemble quarters_signed.geojson from signed decisions` · `data: signed quarter boundaries v1` |
88: 
89: **Г1-б отменя §6а т. 20 на план v2 (`:230`) и амандамент №12 към №4 т. 6**, който връзваше реда с инструмента.
90: 
91: **Договорът на файла с решения (S15) — затворена схема.** `_meta`: `schema_version`, `board_sha256`, **подписан** `registry_sha256`, манифест със SHA на **всеки** вход, версия на канонизацията, `attribution` (низът от §3.8). Ред: `code`, `choice ∈ {official, reconstructed, wikimapia, none, deferred}`, **квалифициран идентификатор на изворния Feature**, `geometry_sha`, препратка към подписания crosswalk, `reason`, `decided_by`, неизменен `decided_at`. Само при Уикимапия: `wm_id` + пълен `wm_polygon_sha256`; при останалите — `null`. **`fetched_at` ≠ `decided_at`.** Три отделни определения: SHA на суровия снапшот, SHA на каноничната геометрия, SHA на доставката. **Правилото за `MultiPolygon` (S15/S20):** компонентите се подреждат по (площ в EPSG:32635 намаляващо, после лексикографски по първия връх на канонизирания външен пръстен); във всеки компонент външният пръстен е по D1 (6 знака, обратно на часовника, ротация към лексикографски най-малкия връх), вътрешните пръстени — по часовника, подредени по същия лексикографски ключ. **Трите SHA обхвата дословно:** `raw_snapshot_sha256` = sha256 на байтовете на замразения файл от обхода; `wm_polygon_sha256` = sha256 на каноничния GeoJSON-геометричен обект по правилото горе (само `type` + `coordinates`, compact JSON, UTF-8); `delivery_sha256` = D3, върху доставения blob. **Одобрението не се доказва с два записани `decisions_sha256`:** изпълнителят чете **точния комитнат от Петър блоб**, сверява го с подписания въпрос с видимо `тяло: <sha256>` и проверява веригата `code → изворен идентификатор → замразена геометрия`.
92: 
93: **Г2-в · провенансът.** `geometry_origin` · `imported_from` · `fetched_at` · `chosen_source` · `chosen_reason` · `confirmed_by` · `confirmed_at`; **`drawn_by` / `drawn_at` / `viewport` / `screenshot_sha256` са `null` при внесена геометрия** (гейт за взаимна изключителност). Промяна в D1 → §7 т. 2.
94: 
95: **Бордът.** Показва по код официалните и човешките полигони, написаните места, **блоковете на КАИС с номера като слой-проверка** (амандамент №1 §5 т. 3 — те НЕ отпадат), площ, IoU, извор, дата. Бутони „да“ / „не“ / „отложи“. **Няма код за чертане, няма `POST`. Подложката е локална** (PMTiles/КАИС) — днешната проба тегли `tile.openstreetmap.org` на живо (`index.html:68`), което D2 не допуска. Бордът **не е** инструментът по D11.
96: 
97: **Предгейтовете остават дословно:** **G19** (частно репо — М0.15 и до днес НЕ Е ИЗМЕРЕНО) и **G21** (ФАЗА_0). **DWG** — отложено (§7).
98: 
99: ## 5 · Гейтове
100: 
101: - **G25-а · пинът.** `wm_polygon_sha256` се преизчислява от проследената геометрия; фикстура: подменен връх при непроменен sha. **Ново (S15): G25 отхвърля подменен `wm_id`, дори геометричният SHA да съвпада** — фикстура. **G25-б** е ръчна датирана МЯРКА, не гейт.
102: - **G26 · пълнота и биекция (поправено по S15).** Ревизия 1 казваше „всеки Feature има ред и обратно“ — **това е грешно**: валиден `deferred` няма Feature. Правилната биекция е решения ↔ **трите множества на D4**: `official/reconstructed/wikimapia → polygon`; `none → no_boundary` с `geometry: null`; `deferred → _meta.deferred`. **`reconstructed` беше изпуснат — добавя се.** Всеки жилищен код от подписания регистър има решение; липсващо = ЧЕРВЕНО, поименно. Фикстури: `deferred` код с Feature; Feature без ред; **координата във файла с решения**.
103: - **G27 · атрибуцията (пренастроен по К21).** Две половини, двете червени при липса: (а) билд-гейт във varna_3d върху `quarters_signed.geojson` + `_meta.attribution` на файла с решения — точният низ от §3.8; (б) **публичната половина (по S20 т. 1–2).** Публичният ред остава `{name, code, src: SIGNED_POLYGON}` — D0 не публикува `Feature.source`, затова UI няма откъде да вземе URL-а на обекта. Договорът: доставката носи `_meta.quarter_attribution` = `{<code>: {"src": "wikimapia", "url": "https://wikimapia.org/<wm_id>/", "label": "<низът, одобрен по §7 т. 8>"}}` само за кодовете с уикимапийски полигон; UI показва реда, когда `quarter.code` има запис в картата. Затвореният `_meta` на доставката става **10 ключа** (`qa_fire_varna_places_export.py` `META_KEYS` + двата преписа + пиновете на D13) — това е **изрична промяна на D13**, записана тук, не мълчаливо „десети ключ“. **Редът на доставката по D13, не „в същия комит“:** (i) varna_3d — `META_KEYS`, преписите, пиновете, `quarter_attribution` в износа; (ii) Fire_Varna — UI низът, който чете `_meta.quarter_attribution`; UI без запис в картата не показва нищо и не пада. Фикстури: ред с уикимапийски квартал без запис в `quarter_attribution` → ✗; запис с `url` без `wm_id` формат → ✗; `_meta` с 11 ключа или с 9 при наличен уикимапийски квартал → ✗.
104: - **G28 · fail-closed.** Отваря се само при **разрешаващ** `verdict ∈ {"allowed", "allowed_with_conditions"}` **И** изпълнени условия 1–3 на К21 (машинно проверими: G29 зелен, G27 (а)+(б) зелени, `license` на всеки уикимапийски Feature попълнен); празен, `blocked` или непознат `verdict` = ЧЕРВЕНО и износът на редове с уикимапийски квартал е блокиран. Днес `verdict` е записан (К21), условия 2–3 още нямат код → клонът е **все още затворен**.
105: - **G22** се разширява по механизъм на `_meta.source_terms[<source>]`, но **изброяването на К8 се запазва дословно**.
106: - **G18** става статична проверка: в борда няма код, който пише връх, **и подложката е от разрешен списък** (фикстура: борд с `tile.openstreetmap.org` или Esri URL → ✗) → решение §7 т. 3.
107: - **G29 · игнорирането (нов).** `git check-ignore -v` за точните пътища + `git ls-files scratch/boundary_gallery` = 0, преди всеки пуш на Fire_Varna; отрицателна фикстура: нарочно проследен файл с геометрия.
108: - **G30 · байтовете (нов, S15).** Каноничен JSON (UTF-8 без BOM, sorted keys, compact, финален LF), байт-равен на `git cat-file blob :<път>`, `sha256` равен на показания от борда; **две сглобявания от едни входове дават байт-еднакъв резултат.** Проверката е **скрипт с фикстура** (BOM, CRLF, стар download), не еднократен ред в конзолата.
109: - **Непроменени:** G1, G17, G19, G21, G23, G24.
110: 
111: ## 6 · Мерките ПРЕДИ борда
112: 
113: - **М2-1 · покритие върху ЗАМРАЗЕНОТО тяло.** Твърдението „20+ от 25 квартала имат полигон“ е на Кими и е опровергано от собствена мярка към 00:36 (по нормализирано име: 15 съвпадения с дефекти — двата „Район Младост“, с.о. „Изгрев“, само „Бриз - юг“ 0,19 km², двусмислената „Комплекс Чайка“; 14 кода без полигон, сред тях `tsentar`, `maksuda`, `kolhozen_pazar`, `kv_levski`, `troshevo`, `hristo_botev`, `rozova_dolina`, `trakia`, `sv_ivan_rilski`, `mladost1`, `mladost2`). Тогава обходът беше на ~30 от 163 семена; повтаря се върху замразения файл и се цитира с неговия sha.
114: - **М2-1б · проверка за пълнота (нова, S14).** Мрежата 500 m гарантира най-близка проба до 353,55 m само в покритите клетки и не дава горна граница на конкуриращите центрове; пропускат се голям полигон с център между пробите, компонент на `MultiPolygon`, курорт извън bbox, полигон под филтъра 0,04 km². Затова: **за всеки регистров код без еднозначен кандидат — `count=100` при регистровата точка и четири метрични отмествания ±300 m (включително извън bbox); запазени заявки, отговори и SHA; ненамереното остава „неустановено“.** При 14 кода ≤ 70 заявки ≈ 33 минути. Тича **след** обхода и **преди** замразяването да се обяви за окончателно. **G26 доказва решение за код, не изчерпателност на Уикимапия.**
115: - **М2-2 · припокриване** (IoU, разлика в площ, симетрична разлика) срещу АГКК. Честно: сравними двойки днес са само Аспарухово/Галата/Чайка; с Одесос МР — нула, докато crosswalk-ът не е подписан. `shapely` 2.1.2 + `pyproj` 3.6.1 — нула нови зависимости.
116: - **М2-3 · местата вътре — днес НЕИЗПЪЛНИМА, и с цикъл (S19).** Популацията е 159, не 174. Координатите трябва да дойдат от пиннатия вход по D10 (`lat`/`lon` в `place_identity.json` — мерено: 375 обекта, **0** с координата); `places_375_hybrid.geojson` е негоден. **Цикълът:** мярката иска P8-а, а план v2 го поставя СЛЕД Г2. Двата изхода са в §7 т. 7: (а) отделен **coordinate-only ход** преди борда, чийто единствен write-set е `lat`/`lon` в `place_identity.json`, покрит от **G9**; или (б) **М2-3 се обявява изрично за след борда** и бордът тръгва без нея.
117: 
118: **Обхватът 38 задължава** преизмерване на уникалността по D12 върху ИЗНЕСЕНИЯ речник + фикстура за сблъсък с немаркирана улица (S7 е).
119: 
120: **Задължителни регресионни фикстури (S17), всяка падаща върху нарочно счупен кандидат:** `street_collision` · `district_retention` · `mladost_kind_collision` · `parent_child` · `order_identity` · `client_cache_matrix`. Положителната „училище св св константин и елена“ трябва да стигне до подписаната идентичност на Френското училище. **Числото „около 150“ отпада като цел** — 159 е допустима популация, не обещана печалба.
121: 
122: ## 7 · Решенията за Петър (седем отворени + едно взето)
123: 
124: 1. **Тръгваме ли по уикимапийския път?** — **ВЗЕТО от Петър** („прегледах районите от уикимапиа… нека ползваме тях“, 06.09 ~00:50). Остава процедурата: бордът започва с **5–6 полигона** с измерени дефекти (двата „Район Младост“, „Комплекс Чайка“, Кайсиева, Аспарухово, Бриз).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=35; Get-Content -LiteralPath '"'C:/git/varna_3d/src/qa_fire_varna_places_export.py' -Encoding UTF8 | Select-Object -Skip 35 -First 37 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 5ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=1255; Get-Content -LiteralPath '"'C:/git/varna_3d/src/place_identity.py' -Encoding UTF8 | Select-Object -Skip 1255 -First 10 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 2ms:
codex
`base_rev` може да се определи еднозначно чрез пиннатия HEAD при Н0. Последният комит на стария ledger обаче съдържа различни export файлове от днешните и не е безопасен заместител на тази база. Остава още един дефект в приемането: Н2 и Б2 използват различни полигони и правила, но планът изисква резултатите им да съвпаднат до място.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'quarter|_meta|fire_varna_locations|write_text|write_json|legacy_bundle_sha' C:/git/varna_3d/src/export_fire_varna_hotels.py C:/git/varna_3d/src/export_fire_varna_places.py C:/git/varna_3d/src/build_place_categories.py C:/git/varna_3d/src/qa_fire_varna_export.py C:/git/varna_3d/src/qa_fire_varna_m6.py" in C:\git\Fire_Varna
 succeeded in 0ms:
C:/git/varna_3d/src/qa_fire_varna_m6.py
C:/git/varna_3d/src/qa_fire_varna_export.py
C:/git/varna_3d/src/build_place_categories.py
C:/git/varna_3d/src/export_fire_varna_places.py
C:/git/varna_3d/src/export_fire_varna_hotels.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re
for f,pat in [('export_fire_varna_places.py',r'"'^def |"_meta"|"quarter":|fire_varna_locations|"licence_wikidata"'"'),('export_fire_varna_hotels.py',r'"'^def |"_meta"|"quarter":|fire_varna_locations|"licence_osm"'"'),('build_place_categories.py',r'"'^def |legacy_bundle_sha|"_meta"|"locations"|"zone_generic_words"'"'),('qa_fire_varna_export.py',r'QUARTER_SRC|valid.*location|quarter_src|SIGNED_OVERRIDE'),('qa_fire_varna_m6.py',r'LEDGER|QUARTER_SRC|SIGNED_OVERRIDE')]:
 p=Path('C:/git/varna_3d/src')/f
 print('FILE',p.as_posix())
 matches=[(i,s) for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1) if re.search(pat,s)]
 for i,s in matches[-15:]: print(f'{i}: {s[:200]}')
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 succeeded in 0ms:
FILE C:/git/varna_3d/src/export_fire_varna_places.py
70: from fire_varna_locations import load as load_locations   # noqa: E402
393: def skel(name: str) -> str:
403: def die(msg: str) -> None:
408: def load_name_aliases(which: str) -> dict[str, list[dict]]:
420:     meta = doc.get("_meta") or {}
458: def kais_quarters() -> dict[int, str]:
479: def dist_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
487: def main() -> None:
493:     attribution = (poi_doc.get("_meta") or {}).get("attribution")
651:     # извори.  Сега ЕДИН resolver отговаря за всичките: `fire_varna_locations`
816:         "_meta": {
823:             "licence_wikidata": LICENCE_WIKIDATA,
882: def make_row(name: str, kind: str, lat: float, lon: float, src: str,
923:         # Попълват се СЛЕД като всички редове са налице — от `fire_varna_locations`
926:         "quarter": None,
FILE C:/git/varna_3d/src/export_fire_varna_hotels.py
55: from fire_varna_locations import load as load_locations   # noqa: E402
110: def excluded_why(p: dict) -> str:
179: def die(msg: str) -> None:
184: def load_name_aliases(which: str) -> dict[str, list[dict]]:
195:     meta = doc.get("_meta") or {}
222: def apply_merges(rows: list[dict], excluded: list[dict],
270: def old_names_of(note: str) -> list[tuple[str, str]]:
296: def main() -> None:
345:             # Попълват се СЛЕД сливанията — от `fire_varna_locations` по
348:             "quarter": None,
420:         "_meta": {
425:             "licence_osm": LICENCE_OSM,
FILE C:/git/varna_3d/src/build_place_categories.py
109: def noun_forms(w: str) -> tuple[list[str], str]:
203: def chip_forms(chip: str) -> tuple[list[str], str, list[str], str]:
263: def zone_aliases() -> tuple[dict, list[str], dict]:
332: def sha256_lf(raw: bytes) -> str:
345: def legacy_word_survives(book, rec: dict, old: str) -> tuple[bool, str]:
370: def location_dictionaries() -> tuple[dict, dict, dict, dict]:
449: def main() -> None:
549:         "_meta": {
566:             "zone_generic_words": ZONE_GENERIC_WORDS,
587:             "legacy_bundle_sha": bundle_sha,
599:         "locations": locations,
FILE C:/git/varna_3d/src/qa_fire_varna_export.py
191: LOC_SRC = {"REG", "KAIS", "SIGNED_OVERRIDE"}
192: DISTRICT_SRC = {"KAIS", "SIGNED_OVERRIDE"}
FILE C:/git/varna_3d/src/qa_fire_varna_m6.py
48: LEDGER = ROOT / "scratch" / "refactor" / "_addr" / "lot1v_locations_375.json"
60: SIGNED_SRC = "SIGNED_OVERRIDE"
180:     for p in (LEDGER, INPUTS, NTR_RAW, REGISTRY):
186:     ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'lot1v_locations_375.json' C:/git/varna_3d/src --glob '*.py'" in C:\git\Fire_Varna
 succeeded in 0ms:
C:/git/varna_3d/src\qa_fire_varna_m6.py
C:/git/varna_3d/src\lot1v_v_manifest.py
C:/git/varna_3d/src\fire_varna_locations.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=640; Get-Content -LiteralPath '"'C:/git/varna_3d/src/export_fire_varna_places.py' -Encoding UTF8 | Select-Object -Skip 640 -First 29 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }
$i=809; Get-Content -LiteralPath '"'C:/git/varna_3d/src/export_fire_varna_places.py' -Encoding UTF8 | Select-Object -Skip 809 -First 24 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }
$i=415; Get-Content -LiteralPath '"'C:/git/varna_3d/src/export_fire_varna_hotels.py' -Encoding UTF8 | Select-Object -Skip 415 -First 24 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 9ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath '"'C:/git/varna_3d/src/lot1v_v_manifest.py' -Encoding UTF8 -TotalCount 90 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 0ms:
1: """Манифестът BASE → P7: покритието по (файл, поле), чакащите подпис, allow-списъкът.
2: 
3: `Fire_Varna/docs/plans/ПЛАН_ЛОТ0_гейтове_P7_F12.md` §P7-д.  Скриптът е
4: REPORT-ONLY: чете двете доставки (BASE-а от историята, кандидата от диска) и
5: ledger-а, и пише два артефакта — нищо в `data/` не се пипа.
6: 
7: Алгоритъмът на покритието е КОПИЕ на `Fire_Varna/gates/coverage.py` (§P7-д го
8: изисква дословно: копие на логиката, не импорт през репото — двете репа не се
9: внасят едно в друго).  Съединяването е по `(файл, име)`, поредният номер е само
10: разделител вътре в дублирано име (РОЯЛ ×2); `before`/`after` се броят върху
11: ВСИЧКИ редове на всяка страна, не върху двойките, за да не може изтрит ред да
12: се скрие в тях.
13: 
14: Класовете по (файл, поле): `lost` (именувано → нищо / „район X“) · `changed`
15: (именувано → друго именувано) · `gained` · `unchanged` · `reordered`, плюс
16: структурните `row_missing` / `row_added`.
17: 
18:     python src/lot1v_v_manifest.py
19:     python src/lot1v_v_manifest.py --base-rev c1fc541
20: """
21: from __future__ import annotations
22: 
23: import argparse
24: import json
25: import subprocess
26: import sys
27: from pathlib import Path
28: 
29: ROOT = Path(__file__).resolve().parent.parent
30: LEDGER = ROOT / "scratch" / "refactor" / "_addr" / "lot1v_locations_375.json"
31: INPUTS = ROOT / "data" / "fire_varna_location_inputs.json"
32: OUT_JSON = ROOT / "scratch" / "refactor" / "_addr" / "lot1v_v_manifest_BASE_P7.json"
33: OUT_MD = ROOT / "scratch" / "refactor" / "_addr" / "lot1v_v_manifest_BASE_P7.md"
34: # The delivery BASE: the last commit before P7 touched anything (P6-б).
35: BASE_REV = "c1fc541"
36: FILES = ("places", "hotels")
37: FIELDS = ("zone_named", "quarter", "locality", "district")
38: DISTRICT_MARK = "район "
39: SIGNED_NAMES = ("ЕЛЕНА", "НИМФА", "ВИВА КЛУБ", "ПЛИСКА", "Вихрен", "ПРЕСЛАВ",
40:                 "ХОЛИДЕЙ ПАРК", "Империя", "ГРАДИНА", "ДОЛЧЕ ВИТА",
41:                 "ЛОТОС/LOTOS", "ОАЗИС/OAZIS")
42: 
43: 
44: def git_show(rev: str, path: str) -> str:
45:     out = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True,
46:                          cwd=str(ROOT))
47:     if out.returncode != 0:
48:         raise SystemExit(f"СПИРАМ: git show {rev}:{path} падна — "
49:                          f"{out.stderr.decode('utf-8', 'replace').strip()}")
50:     return out.stdout.decode("utf-8")
51: 
52: 
53: def field_value(row: dict, field: str):
54:     """The comparable value of a field, or None when the row carries nothing.
55: 
56:     A typed field is compared by its `code`, not by its printed name.
57:     `zone_named` is the compat label and counts only as a real zone name —
58:     „район Приморски“ is the honest absence, not a value.
59:     """
60:     if field == "zone_named":
61:         zone = row.get("zone")
62:         if not isinstance(zone, str) or not zone or zone.startswith(DISTRICT_MARK):
63:             return None
64:         return zone
65:     value = row.get(field)
66:     if not isinstance(value, dict):
67:         return None
68:     code = value.get("code")
69:     return code if isinstance(code, str) and code else None
70: 
71: 
72: def name_positions(rows: list) -> dict:
73:     index: dict = {}
74:     for i, row in enumerate(rows):
75:         index.setdefault(row.get("name"), []).append(i)
76:     return index
77: 
78: 
79: def join_by_name(base_rows: list, cand_rows: list):
80:     """(pairs, missing, added) — the ordinal only splits a duplicated name."""
81:     base_index, cand_index = name_positions(base_rows), name_positions(cand_rows)
82:     pairs, missing, added = [], [], []
83:     for name, base_ords in base_index.items():
84:         cand_ords = cand_index.get(name, [])
85:         for k, b in enumerate(base_ords):
86:             if k < len(cand_ords):
87:                 pairs.append((b, cand_ords[k]))
88:             else:
89:                 missing.append({"name": name, "ordinal": b})
90:     for name, cand_ords in cand_index.items():

codex
**А: НЕГОДНО във v1 — поправимо. Б: НЕГОДНО — Б0 сам не отключва изпълнима доставка.**

Позоваванията „Н“ са към [нощния план](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:1). Проверихме read-only, с независимо оборване и Node проба върху реалните валидатори. Пълно зелено не удостоверявам: `run_gates` има нужда от запис/temporary directory; проверки 4/6 спряха поради sandbox ограниченията, не доказана продуктова регресия.

**1. Не всеки gate е изпълним днес с падаща negative fixture.**

| Лот | Конкретният недостиг |
|---|---|
| Н0 | Липсват `qa_night_pins.py`, pins JSON и изпълнител за G29 негативите. За PowerShell G19 трябва `&` пред quoted executable и пълно `Petar1984/varna_3d`. [Н:58](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:58) |
| Н1 | Липсват candidate builder/QA и всички изброени fixtures. Условието „регистров код без решение → ✗“ противоречи на разрешените 16 `registry_pending`, ако изключението не бъде формализирано. [Н:61](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:61) |
| Н2-0 | Липсват `measure_place_coords.py` и executable проверки за coverage/bbox/непроменена identity. [Н:66](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:66) |
| Н2 | Липсва `measure_polygon_assign.py`; hash/status gate няма отрицателна фикстура. [Н:69](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:69) |
| Н3-а | Общите unittest/gates съществуват; новите пет fixtures и файловете им липсват. [Н:74](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:74) |
| Н4 | Measurement script липсва; AST checker няма файл, CLI или write-set. [Н:79](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:79) |
| Н5/Б4 | Одиторска процедура, без команден acceptance manifest или собствени негативи. [Н:82](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:82), [Н:128](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:128) |
| Б1 | Липсват signed builder/QA/fixtures; G25–G30 остават спецификации. `qa_no_cad_ids.py` съществува. [Н:119](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:119) |
| Б2 | Липсват `qa_p8a.py`, `qa_written_quarters_stable.py`, `qa_quarters_author.py`; последните два липсват и от write-set. [Н:122](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:122) |
| Б3 | Няма шестте fixtures/Node runner. `validatePlaces2 =375` е грешен критерий. `grep coordinates →0` също: самият проследен план съдържа думата. [Н:125](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:125) |

Липсващ бъдещ скрипт е допустим deliverable, но трябва подписан интерфейс, точна команда, очакван exit code и fixture. Тук липсват и тези договори.

**2. `base_rev` е определим тази вечер.**

Точно определение: **пълният HEAD на varna_3d, замразен при Н0 преди промени**, при доказано съвпадение на ledger/export blob-овете с приетия baseline. Измереният сега е:

`8d60aebb365fb8e74ccc863d3b3db90b74180a3b`

Новият ledger записва него в `_meta.base_rev`; G17 чете **стария фиксиран път**, независимо от новата `LEDGER` константа. Манифестът използва същата ревизия. Това изпълнява [D10/D18](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:56).

Не избирайте автоматично последния ledger commit `31db7b9…`: ledger-ът е идентичен, но двата export blob-а там **се различават** от днешните. Старият ledger има 375 реда, 201 непразни квартала; липсващото старо `_meta.base_rev` не пречи на това определение.

Смяната само на `fire_varna_locations.LEDGER` оставя **QA и manifest върху стария ledger**: [qa_fire_varna_m6.py:48](C:/git/varna_3d/src/qa_fire_varna_m6.py:48), [lot1v_v_manifest.py:30](C:/git/varna_3d/src/lot1v_v_manifest.py:30). Нужни са изрични candidate/base входове.

**3. Координати има, но предложеният път е забранен.**

`place_identity.objects`: **0/375** с lat/lon. Износът: **150/150 places +225/225 hotels** с координати. `comparison_columns()` ги чете от двата export файла и свързва чрез `place_id_of` — това е **сравнителен**, не присвояващ канал. [fire_varna_locations.py:974](C:/git/varna_3d/src/fire_varna_locations.py:974)

[D7:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50) изрично забранява тези изнесени координати за polygon assignment. Следователно **Б2 STOP; засега само Н2 мярка**, докато има одобрен source-coordinate вход/G9 или изричен амандамент на D7. `_check_pins` днес проверява NTR/таблиците, **не** общия `inputs` блок. [fire_varna_locations.py:623](C:/git/varna_3d/src/fire_varna_locations.py:623)

**4. Б3 изисква по-голям и подреден write-set.**

Първо varna_3d: resolver/pins; двата exporter `_meta` блока; `META_KEYS`; export QA/M6; categories generator за типове, родители и polygon provenance. Конкретно: [places exporter:816](C:/git/varna_3d/src/export_fire_varna_places.py:816), [hotels exporter:420](C:/git/varna_3d/src/export_fire_varna_hotels.py:420), [META_KEYS:62](C:/git/varna_3d/src/qa_fire_varna_places_export.py:62), [categories:549](C:/git/varna_3d/src/build_place_categories.py:549). Днес `_meta` е **9 ключа при places, 7 при hotels**; добавянето дава 10/8, не универсални 10.

После **един съгласуван Fire_Varna commit**:

- Трите data файла, включително пропуснатия `data/place_categories.json`.
- `PLACES_CACHE`, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци: [index.html:6265](C:/git/Fire_Varna/index.html:6265).
- Валидиране/зареждане, запазване на attribution metadata, D12/index/search и popup: [index.html:6528](C:/git/Fire_Varna/index.html:6528), [6657](C:/git/Fire_Varna/index.html:6657), [7253](C:/git/Fire_Varna/index.html:7253).
- Двата съществуващи bundle теста с SHA/bytes/gzip/codes/counts: [places:55](C:/git/Fire_Varna/tests/test_places_public_bundle.py:55), [hotels:61](C:/git/Fire_Varna/tests/test_hotels_public_bundle.py:61).
- `expectations.json`, трите манифеста, reference/parity corpus, baseline/allow/queue и Python search parity — по изчерпателния [D13:62](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:62).

`DISTRICT_FALLBACK` изисква отделно типово правило: три district кода не са quarter кодове; попълненият fallback нарушава днешното `!quarter` условие за районно търсене. [index.html:7064](C:/git/Fire_Varna/index.html:7064)

**Доказваща LOUDLY fixture няма.** Node пробата: foreign code → `false`, без exception; loader прави `places2=[]`, докато хотелите остават. Дори хвърлена грешка се поглъща. [index.html:6604](C:/git/Fire_Varna/index.html:6604)

Нужна именувана fixture: `client_cache_matrix.foreign_code_while_other_bundle_valid`, с валидни hotels, cache v6/v7, crypto on/off и наблюдаем отказ. Acceptance: двата boolean валидатора минават и **150+225 реда действително се индексират**.

**5. Некомитнатият blob позволява SHA четене, но не доставка.**

Стейджването удовлетворява `git ls-files`, но няма автор в историята: **G4 е червен**. План+SHA не заменят изисквания Petar commit. [ADR:118](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:118)

Release чете HEAD blob-ове само във Fire_Varna; чуждата геометрия не става проверена чрез записан digest в expectations. [release.py:177](C:/git/Fire_Varna/gates/release.py:177), [226](C:/git/Fire_Varna/gates/release.py:226). Новите делти/артефакти искат конкретни човешки подписи; executor не може да изпълни `sign`. [sign.py:139](C:/git/Fire_Varna/gates/sign.py:139)

Допълнително Б0.8 подписва стар blob, после добавя attribution: това създава **нов blob/SHA**, чието препотвърждение е чак сутринта. [Н:114](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:114)

**6. Родството не е последователно и тотално.**

„10 двойки“ изброява **11**; „6+7“ дава 13. [Н:115](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:115)

Контрапример: написан родител + съдържащо дете е `compatible` по D6, но `disputed` по нощното „написан ≠ полигон“. При `A⊂B⊂C` липсва правило за транзитивност. Няма приоритет за `no_coord`, pending, override, ръб, point/body disagreement и locality. [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48)

Поправка: точен подписан DAG, доказано съдържание, транзитивна сравнимост и взаимно изключваща се outcome таблица. Равенството Н2=Б2 отпада: различни полигони, родители, edge правила и fallback. Нужна е отделна прогноза със **същата конфигурация като Б2**.

**7. Реалистичният ред и STOP.**

Н0 първо запазва HEAD/index/dirty baseline. Сега Fire_Varna е **ahead38/behind2**, varna_3d **ahead41 с чужд tracked diff**; празен `status` е неподходящ gate. Третото repo не е независимо удостоверено.

След поправен договор: CLI+негативи → Н0 → Н1/Н2-0 → Н2/Н4; Н3-а независимо; Н5 винаги. **STOP преди Б2** на координатния договор/G4. Б кандидатите остават изолирани от последните зелени release HEAD-ове.

Сутрин: Petar geometry/decision commits → Б2 → атомна Б3 → конкретни подписи/freeze → suite+7/7 → одит → Petar push. При 03:00 червено се запазват чуждите промени и последният зелен release; общо `git revert` при стейджната геометрия не е достатъчен rollback договор.
tokens used
122,030
**А: НЕГОДНО във v1 — поправимо. Б: НЕГОДНО — Б0 сам не отключва изпълнима доставка.**

Позоваванията „Н“ са към [нощния план](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:1). Проверихме read-only, с независимо оборване и Node проба върху реалните валидатори. Пълно зелено не удостоверявам: `run_gates` има нужда от запис/temporary directory; проверки 4/6 спряха поради sandbox ограниченията, не доказана продуктова регресия.

**1. Не всеки gate е изпълним днес с падаща negative fixture.**

| Лот | Конкретният недостиг |
|---|---|
| Н0 | Липсват `qa_night_pins.py`, pins JSON и изпълнител за G29 негативите. За PowerShell G19 трябва `&` пред quoted executable и пълно `Petar1984/varna_3d`. [Н:58](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:58) |
| Н1 | Липсват candidate builder/QA и всички изброени fixtures. Условието „регистров код без решение → ✗“ противоречи на разрешените 16 `registry_pending`, ако изключението не бъде формализирано. [Н:61](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:61) |
| Н2-0 | Липсват `measure_place_coords.py` и executable проверки за coverage/bbox/непроменена identity. [Н:66](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:66) |
| Н2 | Липсва `measure_polygon_assign.py`; hash/status gate няма отрицателна фикстура. [Н:69](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:69) |
| Н3-а | Общите unittest/gates съществуват; новите пет fixtures и файловете им липсват. [Н:74](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:74) |
| Н4 | Measurement script липсва; AST checker няма файл, CLI или write-set. [Н:79](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:79) |
| Н5/Б4 | Одиторска процедура, без команден acceptance manifest или собствени негативи. [Н:82](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:82), [Н:128](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:128) |
| Б1 | Липсват signed builder/QA/fixtures; G25–G30 остават спецификации. `qa_no_cad_ids.py` съществува. [Н:119](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:119) |
| Б2 | Липсват `qa_p8a.py`, `qa_written_quarters_stable.py`, `qa_quarters_author.py`; последните два липсват и от write-set. [Н:122](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:122) |
| Б3 | Няма шестте fixtures/Node runner. `validatePlaces2 =375` е грешен критерий. `grep coordinates →0` също: самият проследен план съдържа думата. [Н:125](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:125) |

Липсващ бъдещ скрипт е допустим deliverable, но трябва подписан интерфейс, точна команда, очакван exit code и fixture. Тук липсват и тези договори.

**2. `base_rev` е определим тази вечер.**

Точно определение: **пълният HEAD на varna_3d, замразен при Н0 преди промени**, при доказано съвпадение на ledger/export blob-овете с приетия baseline. Измереният сега е:

`8d60aebb365fb8e74ccc863d3b3db90b74180a3b`

Новият ledger записва него в `_meta.base_rev`; G17 чете **стария фиксиран път**, независимо от новата `LEDGER` константа. Манифестът използва същата ревизия. Това изпълнява [D10/D18](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:56).

Не избирайте автоматично последния ledger commit `31db7b9…`: ledger-ът е идентичен, но двата export blob-а там **се различават** от днешните. Старият ledger има 375 реда, 201 непразни квартала; липсващото старо `_meta.base_rev` не пречи на това определение.

Смяната само на `fire_varna_locations.LEDGER` оставя **QA и manifest върху стария ledger**: [qa_fire_varna_m6.py:48](C:/git/varna_3d/src/qa_fire_varna_m6.py:48), [lot1v_v_manifest.py:30](C:/git/varna_3d/src/lot1v_v_manifest.py:30). Нужни са изрични candidate/base входове.

**3. Координати има, но предложеният път е забранен.**

`place_identity.objects`: **0/375** с lat/lon. Износът: **150/150 places +225/225 hotels** с координати. `comparison_columns()` ги чете от двата export файла и свързва чрез `place_id_of` — това е **сравнителен**, не присвояващ канал. [fire_varna_locations.py:974](C:/git/varna_3d/src/fire_varna_locations.py:974)

[D7:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50) изрично забранява тези изнесени координати за polygon assignment. Следователно **Б2 STOP; засега само Н2 мярка**, докато има одобрен source-coordinate вход/G9 или изричен амандамент на D7. `_check_pins` днес проверява NTR/таблиците, **не** общия `inputs` блок. [fire_varna_locations.py:623](C:/git/varna_3d/src/fire_varna_locations.py:623)

**4. Б3 изисква по-голям и подреден write-set.**

Първо varna_3d: resolver/pins; двата exporter `_meta` блока; `META_KEYS`; export QA/M6; categories generator за типове, родители и polygon provenance. Конкретно: [places exporter:816](C:/git/varna_3d/src/export_fire_varna_places.py:816), [hotels exporter:420](C:/git/varna_3d/src/export_fire_varna_hotels.py:420), [META_KEYS:62](C:/git/varna_3d/src/qa_fire_varna_places_export.py:62), [categories:549](C:/git/varna_3d/src/build_place_categories.py:549). Днес `_meta` е **9 ключа при places, 7 при hotels**; добавянето дава 10/8, не универсални 10.

После **един съгласуван Fire_Varna commit**:

- Трите data файла, включително пропуснатия `data/place_categories.json`.
- `PLACES_CACHE`, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци: [index.html:6265](C:/git/Fire_Varna/index.html:6265).
- Валидиране/зареждане, запазване на attribution metadata, D12/index/search и popup: [index.html:6528](C:/git/Fire_Varna/index.html:6528), [6657](C:/git/Fire_Varna/index.html:6657), [7253](C:/git/Fire_Varna/index.html:7253).
- Двата съществуващи bundle теста с SHA/bytes/gzip/codes/counts: [places:55](C:/git/Fire_Varna/tests/test_places_public_bundle.py:55), [hotels:61](C:/git/Fire_Varna/tests/test_hotels_public_bundle.py:61).
- `expectations.json`, трите манифеста, reference/parity corpus, baseline/allow/queue и Python search parity — по изчерпателния [D13:62](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:62).

`DISTRICT_FALLBACK` изисква отделно типово правило: три district кода не са quarter кодове; попълненият fallback нарушава днешното `!quarter` условие за районно търсене. [index.html:7064](C:/git/Fire_Varna/index.html:7064)

**Доказваща LOUDLY fixture няма.** Node пробата: foreign code → `false`, без exception; loader прави `places2=[]`, докато хотелите остават. Дори хвърлена грешка се поглъща. [index.html:6604](C:/git/Fire_Varna/index.html:6604)

Нужна именувана fixture: `client_cache_matrix.foreign_code_while_other_bundle_valid`, с валидни hotels, cache v6/v7, crypto on/off и наблюдаем отказ. Acceptance: двата boolean валидатора минават и **150+225 реда действително се индексират**.

**5. Некомитнатият blob позволява SHA четене, но не доставка.**

Стейджването удовлетворява `git ls-files`, но няма автор в историята: **G4 е червен**. План+SHA не заменят изисквания Petar commit. [ADR:118](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:118)

Release чете HEAD blob-ове само във Fire_Varna; чуждата геометрия не става проверена чрез записан digest в expectations. [release.py:177](C:/git/Fire_Varna/gates/release.py:177), [226](C:/git/Fire_Varna/gates/release.py:226). Новите делти/артефакти искат конкретни човешки подписи; executor не може да изпълни `sign`. [sign.py:139](C:/git/Fire_Varna/gates/sign.py:139)

Допълнително Б0.8 подписва стар blob, после добавя attribution: това създава **нов blob/SHA**, чието препотвърждение е чак сутринта. [Н:114](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:114)

**6. Родството не е последователно и тотално.**

„10 двойки“ изброява **11**; „6+7“ дава 13. [Н:115](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:115)

Контрапример: написан родител + съдържащо дете е `compatible` по D6, но `disputed` по нощното „написан ≠ полигон“. При `A⊂B⊂C` липсва правило за транзитивност. Няма приоритет за `no_coord`, pending, override, ръб, point/body disagreement и locality. [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48)

Поправка: точен подписан DAG, доказано съдържание, транзитивна сравнимост и взаимно изключваща се outcome таблица. Равенството Н2=Б2 отпада: различни полигони, родители, edge правила и fallback. Нужна е отделна прогноза със **същата конфигурация като Б2**.

**7. Реалистичният ред и STOP.**

Н0 първо запазва HEAD/index/dirty baseline. Сега Fire_Varna е **ahead38/behind2**, varna_3d **ahead41 с чужд tracked diff**; празен `status` е неподходящ gate. Третото repo не е независимо удостоверено.

След поправен договор: CLI+негативи → Н0 → Н1/Н2-0 → Н2/Н4; Н3-а независимо; Н5 винаги. **STOP преди Б2** на координатния договор/G4. Б кандидатите остават изолирани от последните зелени release HEAD-ове.

Сутрин: Petar geometry/decision commits → Б2 → атомна Б3 → конкретни подписи/freeze → suite+7/7 → одит → Petar push. При 03:00 червено се запазват чуждите промени и последният зелен release; общо `git revert` при стейджната геометрия не е достатъчен rollback договор.
