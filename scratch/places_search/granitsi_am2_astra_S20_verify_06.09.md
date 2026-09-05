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
session id: 01a073a5-cc3d-7882-a18e-9d52f99d07ec
--------
user
S20 — VERIFY, do not re-review from scratch: docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md is now revision 2a, rewritten after your S14–S19 verdict (your record: scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md, final answer at the end) and after Kimi К21 (scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md, final answer at the end). For each of S14, S15, S16, S17, S18, S19 say RESOLVED / PARTIALLY / NOT, citing the revision's file:line that resolves it, and name any NEW mechanical defect the revision introduced (e.g. G27 public half vs the closed 9-key _meta and 13/17-key row of qa_fire_varna_places_export.py — is adding licence_quarter_boundary to META_KEYS consistent with D13 pins and both transcripts; G28 conditions 1–3 machine-checkable or not; the order Г1-а → Г2-а → Г2-б → Г2-в vs plan v2 §2; decision 7 vs G9). Read-only; at most 900 words; Bulgarian with English identifiers; cite file:line.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя само дали revision 2a затваря S14–S19 и дали поправките въвеждат нови механични дефекти. Ще съпоставя двата предишни verdict-а, плана и относимите проверки, без промени по файловете.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
 succeeded in 39ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 20, behind 2]
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
?? scratch/places_search/granitsi_am2_astra_S20_verify_06.09.md
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 100" in C:\git\Fire_Varna
 succeeded in 18ms:
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p = @('"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md','scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md','scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md'); "'$p | Sort-Object | ForEach-Object { $f = Get-Item -LiteralPath $_; '"'{0} | {1} bytes | {2} lines' -f "'$_, $f.Length, (Get-Content -LiteralPath $_).Count }' in C:\git\Fire_Varna
 succeeded in 53ms:
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | 51902 bytes | 156 lines
scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md | 227011 bytes | 964 lines
scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md | 21069 bytes | 91 lines

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 915 -and $n -le 964) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
915: 
916: Общ `data_sha256` е достатъчен само ако обвързва целия manifest. Повтарянето на page/data SHA във всеки ред е излишно. `fetched_at` и `decided_at` означават различни събития. Raw snapshot SHA, canonical geometry SHA и delivery SHA трябва да имат отделни определения; за `MultiPolygon` липсват правила за подредбата на компонентите и вътрешните пръстени. [ADR:38](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:38), [A2:59](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:59)
917: 
918: **Пряко противоречие:** „всеки Feature има ред … и обратно“ отхвърля валиден `deferred`, който няма Feature. Правилната биекция е решения ↔ трите множества: `official/reconstructed/wikimapia→polygon`, `none→no_boundary` с null geometry, `deferred→_meta.deferred`. G26 изпуска `reconstructed`. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [ADR:44](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:44)
919: 
920: Два записани `decisions_sha256` не доказват одобрение. Нужни са прочит на точния Petar-committed blob, сверка към подписан въпрос с видимо `тяло`, и проверка `code→source ID→frozen geometry`. G25 трябва да отхвърля подменен `wm_id`, дори геометричният SHA да съвпада. [ADR:42](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:42)
921: 
922: На Windows преименуване или `(1)` само не променя SHA; опасностите са избран стар download, редакторна BOM/CRLF конверсия и Git EOL преобразуване. При предложена канонизация UTF-8 без BOM, sorted keys, compact JSON и финален LF, след staging изпълнителят пуска следното с трите реални аргумента:
923: 
924: ```powershell
925: python -c "import sys,json,hashlib,subprocess,pathlib; b=pathlib.Path(sys.argv[2]).read_bytes(); j=json.loads(b.decode('utf-8')); assert b==(json.dumps(j,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8'); assert b==subprocess.check_output(['git','cat-file','blob',':'+sys.argv[1]]); assert hashlib.sha256(b).hexdigest()==sys.argv[3]; print('OK')" "<repo-relative-path>" "<exact-download-path>" "<SHA-shown-by-board>"
926: ```
927: 
928: Това проверява байтовете; schema/approval проверката остава отделна. Две сглобявания от едни входове трябва да дадат байт-еднакъв резултат.
929: 
930: **S16. Ръбът вече е правилно дефиниран.** D7 изисква `edge=max(50,precision_m)` в EPSG:32635. При Wikimapia минимум 100 m фиксиран ръб 50 m би нарушил съществуващия договор. Фикстура: празен безспорен ред, точка и тяло на 75 m навътре, `precision_m=100` → `edge_pending`, без присвояване; на повече от 100 m и без други пречки → допустимо `written`. [ADR:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50)
931: 
932: Конфликтните класове са назовани, но `classify(code)==field` не доказва вида на **изворния полигон**: район може погрешно да получи валиден квартален code и да премине проверката. Минималното правило е подписан source-kind crosswalk, точно един избран source Feature за code, забранено двойно присвояване на една геометрия към несравними кодове; неразрешено двусмислие → без писане. Нормализираното заглавие не решава „Чайка“ и двата „Младост“. Родител/дете се допуска само по подписано и геометрично проверено родство. [A2:31](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:31), [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [ADR:52](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52)
933: 
934: **S17. „Около 150“ не е приемно число.** Декларираните 159 са допустима популация, не обещана печалба. S7 вече изисква подредени идентичности и целия публичен ред. [ADR:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [A1:25](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25)
935: 
936: Задължителни фикстури:
937: 
938: - `street_collision`: нов квартален токен не премахва немаркирана A3-street улица; ADDRESS остава байт-равен.
939: - `district_retention`: нов `quarter` не губи валидни резултати от търсене по район.
940: - `mladost_kind_collision`: районният полигон не добавя чужди редове към „училище младост 2“.
941: - `parent_child`: „възраждане 3“ избира детето; „възраждане“ — родителя и регистрираните деца.
942: - `order_identity`: запазва подредените `bundle:ordinal`; смяна на branch е отделна делта.
943: - `client_cache_matrix`: old/new client × old/new/mixed bundles × cold/warm cache.
944: 
945: Регресионните фикстури трябва да падат върху нарочно счупен кандидат; положителната „училище св св константин и елена“ трябва да премине към подписаната идентичност на Френското училище след поправката. Новите печалби не оправдават загуба на валиден стар резултат. [A1:28](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:28), [A1:38](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:38), [V2:168](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:168)
946: 
947: **S18. RMS не доказва точността на линията.** Остатъкът върху използваните центроиди измерва fit-а. Не включва грешното съответствие, растеризацията, сегментацията и поведението между контролите. `2 pt/pixel` не дава метри без метричния affine Jacobian.
948: 
949: Фикстурата rms 11/`precision_m=50` **минава**: `max(50,3×11)=50`. Отрицателен пример е rms 20/precision 50. [A2:27](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:27), [A2:33](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:33)
950: 
951: `max(50,3*rms,max_residual+raster_error)` е предпазен минимум, не установена точност. Независимата проверка трябва да сравнява 20 предварително избрани точки по периметъра с доказано **същата** граница и да отчита `dmax/p95`. Най-близкият произволен KAIS parcel edge може да даде фалшив успех. Извадката проверява извадката; без независима референция реконструкцията остава свидетел. MR→code подписът решава идентичност, не точност.
952: 
953: **S19. Присъди по раздели:**
954: 
955: | Раздел | Присъда | Необходима поправка |
956: |---|---|---|
957: | §2 | НЕГОДНО | Source-kind проверка, еднозначен crosswalk, честен precision floor и работещи фикстури. |
958: | §4 | НЕГОДНО | Затворена decisions схема; конкретни write-set/изпълнител/съобщение; потвърждаване → decisions commit → assembly. |
959: | §5 | НЕГОДНО | Правилна биекция, проверена approval chain; G18 да проверява и разрешените подложки; G28 да допуска само разрешаващ verdict. |
960: | §6 | НЕГОДНО | Предварителен coordinate-only ход с G9, после М2-3 и борд. |
961: 
962: §4 само обещава write-set-овете. §6 има цикъл: мярката **преди борда** чака P8-а, който V2 поставя **след Г2**. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [A2:85](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:85), [V2:149](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:149)
963: 
964: Преди Петър да подпише, договорът трябва да има изпълним ред без цикли, проверима SHA/approval chain, поименни отрицателни фикстури и изрично приет обхват на непокритите квартали.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 47 -and $n -le 91) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
47:   ## (а) Verdict за `_meta.source_terms["wikimapia"]`
48: 
49:   **`allowed_with_conditions`.** Трите блокера от К20 са попълнени: ToS е цитиран с URL и дата (`scratch/places_search/wikimapia_terms_2026-09-06.md:5-14` → §3.5, амандамент `:57-60`), позицията „не е адаптация" е записана с довод по §1(b) (`docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:48`), игнорирането е измерено (`:68` — `check-ignore` потвърдено, `ls-files` = 0). Точните условия:
50: 
51:   1. **Геометрията никога публично** — остава в `varna_3d/data`, публичният ред е само `{name, code, src}` (`:46`); G29 пази игнорирането преди всеки пуш (`:104`).
52:   2. **Публична атрибуция е задължителна** (виж (б)): нов български UI низ + `licence_quarter_boundary` в `META_KEYS`, в пиновете на D13 и двата преписа, един комит, отделно одобрение на Петър — точно аварийният път, записан в §3.3 (`:50`). G27 се пренастройва да сверява този низ.
53:   3. **Лиценз на ниво Feature** (`_meta.licences[]`), не на файл (§3.6, `:62`), с етикета по §3.8 (`:66`).
54:   4. **Версия „3.0 assumed, по-строгото печели"** (виж (г)).
55:   5. **Дроселът не се заобикаля** — няма паралелни сесии, няма вдигане над 1/28 s (виж (д)).
56:   6. **Реален ключ преди М2-1б**, или изрично записан риск при отказ (§7 т. 6, `:126`).
57:   7. **По-квартално „да" от Петър** върху замразен полигон с `wm_id` — никакъв автоматичен матчер (`:38`, `:26`).
58: 
59:   G28 остава fail-closed и отваря клона само срещу този `verdict` + изпълнени условия 1–3 (`:101`).
60: 
61:   ## (б) Издържа ли §3.2 при ToS §1.G
62: 
63:   **Позицията издържа като лицензен анализ, но §1.G е независима договорна клауза и я заобикаля.** Доводът по §3.2 (`:48`) е коректен по CC BY-SA 3.0: „Adaptation" по §1(b) изисква пренос на израз; point-in-polygon дава факт (пространствено отношение), значи §4(b) ShareAlike не захапва. ODbL-аналогията е правилно отхвърлена — „Produced Work" е термин на ODbL, не на CC.
64: 
65:   Но §1.G не е лицензна клауза, а договорно условие: „**Public use of Wikimapia Data** and it's derivatives requires…" (`scratch/.../wikimapia_terms_2026-09-06.md:9`). Публичният ред носи **име, което само по себе си е Wikimapia Data** — заглавията са User Submissions (§1.B, §1.F, `:11`, `:8`), а полигонът (също данни) определя кое име се присвоява. Тоест дори въпросът „derivative ли е" да се реши с „не", остава първият член на дизюнкцията — публична употреба на самите данни. Приложението се гледа от уеб браузър, значи „if viewed from any web browser" е изпълнено.
66: 
67:   **Минимална публична атрибуция:** (1) „Wikimapia.org" с връзка към http://wikimapia.org; (2) връзка към оригиналния URL на обекта (напр. `wikimapia.org/1851926`) за всеки показан квартал с `src: wikimapia` (§1.G а/б, `:9`). Следствие: §3.3-зависимостта се разрешава в тежкия клон — атрибуцията от условие (а) т. 2 е **задължителна**, независимо че §3.2 издържа.
68: 
69:   ## (в) Чл. 11 на Дир. 96/9 при ToS §3
70: 
71:   **Отпада по същество, с нисковероятна резерва.** Чл. 11(1)–(2) дава sui generis защита само на граждани/резиденти на ЕИП и дружества по правото на държава-членка; чл. 11(3) позволява разширение само по споразумение — между ЕС и САЩ такова няма. ToS §3 заявява: „The SERVICE is controlled and offered by WikiMapia from its facilities in the United States of America" (`wikimapia_terms_2026-09-06.md:12`). Значи производителят е извън ЕИП и базата **не се ползва от sui generis защита в ЕС** — въпросът отпада.
72: 
73:   Резервата е записана в самия амандамент (`:53`): това е собствено твърдение на оператора, не независима проверка на правната форма. Ако съществува ЕС дружество-носител, въпросът се връща — но и тогава пълният тест на чл. 7(5) (`:54`) е на наша страна: ~180 полигона от милиони не са съществена част, а „противоречие с нормалното използване" на безплатна публична база за некомерсиална карта е трудно доказуемо. Условията от (а) пасират и двата случая, затова резервата не блокира.
74: 
75:   ## (г) Версията на CC BY-SA
76: 
77:   ToS казва само „Attribution-ShareAlike", без версия (`wikimapia_terms_2026-09-06.md:14`; §3.5, `:58`). **Приемаме 3.0 Unported като записано допускане**, защото: (1) проектът дотук работи с него (`:20` — id 1851926 е маркиран „CC BY-SA 3.0"; `:14`); (2) целият анализ в §3.2/§3.3 е построен по §1(b), §4(b), §4(c) на 3.0; (3) практическият извод е **идентичен при 4.0** — и двете версии имат BY + SA, и двете дефинират адаптацията чрез пренос на израз, никоя няма „produced work". Записва се `licence: "CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)"` в `source_terms`. Допускането не е блокиращо, защото атрибуцията от (б) покрива и двете версии.
78: 
79:   ## (д) ~670 заявки при 1/28 s — „unreasonable load" ли е
80: 
81:   **Не.** §1.C.g забранява „unreasonable load on WikiMapia's infrastructure" и §1.C.j — „damage, impair, or overburden" (`wikimapia_terms_2026-09-06.md:10`). Скоростта ~1 заявка/28 s е **наложена от самия API** със съобщение „You need to wait for N seconds" (`:29`; `:14` на амандамента) — обходът спазва дросела на оператора, не го заобикаля. ~670 заявки за ~5 часа ≈ 2/минута е натоварване, което операторът сам е определил за допустим темп. Амандаментът правилно отказва да запише нарушение и държи хипотезата на К17 като риск (`:140`). Условието (а) т. 5 фиксира границата: всяко вдигане на скоростта или паралелизиране променя тази присъда.
82: 
83:   ## (е) Реален безплатен ключ — променя ли нещо
84: 
85:   **Подобрява позицията, но не променя анализа.** Ключът `example` е демонстрационен, от примерите в документацията (`:19`) — систематичен обход с него е по-слаба позиция от обход с легитимен ключ. Реален ключ означава регистриран потребител, **изрично приел ToS**, с идентифицируем акаунт: обходът става договорно покрит, а риск-хипотезата „демо ключ извън предназначението" (`:140`) се гаси. Не променя: §1.C.g (скоростта пак е дроселирана), §1.G (атрибуцията си остава), CC-анализа. Регистрацията е акт на Петър (`:19`, `:126`) — **препоръка: да, преди М2-1б**; при „не" вердиктът стои с риск, записан в `source_terms`.
86: 
87:   ---
88: 
89:   **Резюме за гейта:** `verdict = "allowed_with_conditions"`, условия 1–7 от (а); G27 се пренастройва към задължителния публичен низ; G28 отваря клона само след условия 1–3. Присъдата е пост-фактум оценка на вече извършено извличане (`:55`), не разрешение за бъдещо — следващ обход извън записаните параметри изисква нова.
90: 
91: To resume this session: kimi -r session_ab61ba50-809d-464b-b4d0-7cb0d38da3da

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --files --max-count 20 --max-columns 200 -g '*Границите*v2*' -g '*qa_fire_varna_places_export*' -g '*transcript*' -g 'AGENTS.md' -g '*granitsi_am2*' -g '*d13*' -g '*D13*' | Sort-Object" in C:\git\Fire_Varna
 succeeded in 144ms:
AGENTS.md
docs\plans\ПЛАН_ЛОТ_Границите_v2_05.09.md
docs\plans\ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md
docs\plans\ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md
scratch\places_search\granitsi_am2_astra_S14-S19_06.09.md
scratch\places_search\granitsi_am2_astra_S20_verify_06.09.md
scratch\places_search\granitsi_am2_brief_astra.md
scratch\places_search\granitsi_am2_brief_kimi.md
scratch\places_search\granitsi_am2_kimi_K15-K20_06.09.md
scratch\places_search\granitsi_am2_kimi_K21_verdict_06.09.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 28" in C:\git\Fire_Varna
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


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 1 -and $n -le 55) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
1: # Амандамент №2 към ПЛАН „Границите“ v2 — **ревизия 2** (06.09.2026, ~04:00 **по часовника на машината**) — след присъдата на Петър, след намирането на човешките полигони (Уикимапия), след одита в три лещи и след оборването от Кими (К15–К20) и Astra (S14–S19). Статус: **за Gate 1 — едно четиво за Петър. НЕПОДПИСАН.** (Ревизия 2а, ~04:30: присъдата на Кими К21 е вградена — виж дневника.)
2: 
3: Нов датиран файл по §0.2 на `docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md:9`. Не редактира плана v2, ADR 010 и амандамент №1; казва какво се променя в тях и защо. Не открива лота, не пипа живата карта, не комитва геометрия.
4: 
5: ## Дневник на ревизиите
6: 
7: - **Ревизия 1** (06.09, ~00:40) — вътрешен одит в три лещи (Opus). Приложено: мярка само върху **замразено** тяло (§0), поправка на собствената мярка („1 обект / `_meta.note`“ е невярно), думите на Петър от ~00:50 като ВЗЕТО решение №1, стълбата v3 с отделно стъпало (1-б), G25–G28. Отхвърлено: спиране на самото събиране — то е поръчано от Петър и спирането му би оставило твърдението „20+ квартала“ непроверено.
8: - **Ревизия 2** (тази, 06.09, ~03:30–04:00) — след двете външни присъди: **Кими К15–К20** (лицензна леща, `scratch/places_search/granitsi_am2_kimi_K15-K20_06.09.md`) и **Astra S14–S19** (механична леща, `scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md`). Преработени: §2, §3 (изцяло), §4 (редът и договорът на решенията), §5, §6, §7; §8 сменя „чака“ с **записаните присъди** и списъците приложено/отхвърлено. Текстът е на Opus-планировчик по двете присъди; архитектът добави в §3.4(а) и §3.5 прочетените след това условия на Уикимапия (`scratch/places_search/wikimapia_terms_2026-09-06.md`). **Статусът НЕ се променя: пак „за Gate 1“, пак неподписан.** Записаните думи и решения на Петър запазват смисъла си дословно.
9: - **Ревизия 2а** (06.09, ~04:30) — **Кими К21** (`scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md`) върху попълнените входове: `verdict = allowed_with_conditions` със седем условия; най-тежкото — **публичната атрибуция е задължителна по ToS §1.G** (договорна клауза, независима от лицензния анализ по §3.2). Променени: §3.3, §3.5, G27, G28, §7 (ново решение 8), §8.
10: 
11: ## 0 · Червен ред преди всичко останало
12: 
13: Тече `wikimapia_sweep.py` (обход по `place.getnearest`, 163 начални точки + мрежа 500 m, ~28 s на заявка), който събира полигони в `scratch/boundary_gallery/granitsi_preview_05.09/wikimapia_quarters.geojson`. Файлът РАСТЕ — **към 03:50: 86 от 163 начални точки, 180 полигона с квартална големина; мрежовият проход (504 точки) е още предстоящ.** Това е СЪБИРАНЕ, не мярка, и е поръчано от Петър („нека ползваме тях“). Обходът се оставя да завърши; **но нищо не се мери, не се показва в борд и не се цитира, преди тялото да бъде замразено**: копие с дата, `sha256` на целия файл, брой обекти, записани в мярката. **Нито едно число в този амандамент не е цитирано като окончателно.**
14: 
15: **Измерено поведение на API-то (06.09).** С ключ `example` работят `place.getbyid` и `place.getnearest` (`count=100`, `data_blocks=geometry,location`); `place.getbyarea` (със и без `coordsby=bbox`, със и без `category=4621 „квартал“`), `place.search` и филтрите по категория връщат `found=0`; скорост ~една заявка на 28 s. Следствие: **обходът е само-`getnearest`** — площен обход няма как да се направи, значи пълнотата се доказва по кодове (М2-1б), не по площ.
16: 
17: **Поправка на собствена мярка.** Ранната чернова твърдеше „1 обект, `_meta.note`: дроселиран ключ“. И двете са неверни: обектите бяха деветдесет по време на одита, а `_meta` носи ключове `{attribution, licence, min_km2, not_for_publication, what}` — ключ `note` няма. Правилото: **входовете на борда са пиннати снапшоти, не течащи файлове.**
18: 
19: ## 1 · Какво реши Петър
20: 
21: Дословно: „нищо няма да чертая аз“ · за КАИС-изведените граници — „много са объркани… направо са грешни“ · „данните от OSM са по-точни; маркирай кварталите според тях; аз ще потвърдя“ · за хибрида — „много е зле… провери във форуми“ · и върху полигона на кв. Кайсиева градина от Уикимапия (id 1851926, CC BY-SA 3.0, 0,42 km²): **„точно това е границата“**.
22: 
23: **Какво отпада.** Целият производен клон — обвивките от юли, КАИС-изведените полигони, OSM-Voronoi, уличният вариант, хибридът. Отпада и **чертането** като метод: план v2 §2 (Г1 → Г2, `ПЛАН_ЛОТ_Границите_v2_05.09.md:104-146`) стъпваше върху „Петър чертае“.
24: 
25: **След одита (06.09, ~00:50) Петър добави:** „прегледах районите от уикимапиа — доста добре съм — нека ползваме тях“. Той е прегледал сам кварталите на сайта — това е неговата извадка по собствения му протокол и решение №1 е ВЗЕТО от него, не чака. Бордът все пак започва с извадката от §7 т. 1, защото там са измерените дефекти.
26: 
27: **Какво НЕ следва автоматично.** Едно потвърждение на екрана не е присъда по квартал в нашия регистър: всяко „да“ се дава по квартал, върху замразения полигон, със записан `wm_id`.
28: 
29: ## 2 · Стълбата на изворите v3 — за ГРАНИЦАТА
30: 
31: Номерацията на D0 (`010_signed_quarter_boundaries.md:36`) се пренарежда: степени (1) и (2) определят **линията**; написаният извор за **мястото** (REG/KAIS/НТР, рангове 0–2) и `POST-2018` остават непроменени.
32: 
33: **(1) Официален полигон.** (а) **АГКК INSPIRE `Geo_Names` Surface** — 6 кода, `source: "agkk_inspire_gn"`; заключен по G22/К8. (б) **Общинският слой „Квартали“** (52 полигона; `municipal_kvartali_layer_05.09.md:4-10`) — **днес заключен** (`SB_0005 Subscription is disabled`), проверката е скрипт, не писмо.
34: 
35: **(1-б) Реконструиран официален план — ОТДЕЛНО, ПО-НИСКО стъпало.** Одесоските 11 микрорайона са извадени от PDF по цвят и закачени с афинна трансформация (rms 11 m, max 21 m, 15 контролни точки) — **изведена от агент геометрия**. Полетата носят номера, не имена → **0 кода за G26 днес**; съответствието МР → регистров код е собствен подписан ред в опашката.
36: 
37: **Подът на неточността се поправя (S18).** Не „≥ 3×rms“, а `precision_m ≥ max(50, 3×rms, max_residual + raster_error)` — **предпазен минимум, не установена точност**. Фикстурата от ревизия 1 („rms 11 при `precision_m` 50“) е **невярна: тя МИНАВА**, защото `max(50, 33) = 50`. Отрицателната фикстура става **rms 20 при `precision_m` 50**. RMS върху използваните центроиди мери напасването, не линията: не включва грешното съответствие, растеризацията и поведението между контролните точки. **Независима проверка на линията:** 20 предварително избрани точки по периметъра срещу доказано СЪЩАТА граница, отчетени `dmax` и `p95`; най-близкият произволен КАИС ръб на парцел дава фалшив успех и не се брои. Без нея реконструкцията остава **свидетел**, не граница. Подписът МР → код решава идентичност, не точност.
38: 
39: **(2) Човешки полигон — Уикимапия** (CC BY-SA), `source: "wikimapia"`, `method: "human_polygon"`. Пиннат с **`wm_polygon_sha256`** (пълни 64 hex; `polygon_sha256` е зает от D3), плюс `wm_id`, `fetched_at`, `url`. Канонизацията е дословно тази на D1. **Валиден САМО след изричното „да“ на Петър за ТОЗИ квартал**, с подписан ред от crosswalk-а „заглавие ↔ регистров код“ — никакъв автоматичен матчер.
40: 
41: **Конфликтите (разширено D6, поправено по S16).** Три измерени класа: (а) **човешки ↔ човешки** — „Район Младост“ е два полигона (13,22 и 12,34 km²); (б) **един полигон ↔ два кода** — „Комплекс Чайка“ пасва и на `chaika_kv`, и на `chaika_kk`; (в) **грешен вид** — „Район Младост“ е РАЙОН, „Изгрев“ е с.о. **`classify(code) == field` НЕ доказва вида на изворния полигон** — районен полигон може да получи валиден квартален код и да мине проверката. Минималното правило, което влиза в D6: **подписан source-kind crosswalk; точно един избран изворен Feature на код; една геометрия никога към два несравними кода; неразрешено двусмислие → без писане.** Нормализаторът на заглавия (в данните стои `&amp;quot;`, най-големият обект е „Βарна“ с гръцка бета) **не решава** „Чайка“ и двата „Младост“. Родител/дете — само по подписано И геометрично проверено родство (D8).
42: 
43: **`precision_m` за чужда геометрия.** `district_map_georef` по формулата горе; `wikimapia` ≥ 100 m до доказано друго; Feature без явен `precision_m` = червено. **Ръбът е по D7: `edge = max(50, precision_m)`** (ревизия 1 пишеше „ръб 50 m“ — невярно при `precision_m` 100). Фикстура: празен безспорен ред, точка и тяло на 75 m навътре, `precision_m` 100 → `edge_pending`, без присвояване; на повече от 100 m и без други пречки → допустимо `written`.
44: 
45: ## 3 · Лицензът — присъдата на Кими е ЗАПИСАНА; клонът остава блокиран от G28
46: 
47: **3.1 Прието третиране.** Геометрията остава в `varna_3d/data` и **никога не се публикува** (D3 `:42`); публичният ред остава 13/17 ключа с `quarter: {name, code, src}`.
48: 
49: **3.2 „Публикуването на име не е адаптация“ е ПОЗИЦИЯ с довод, не консенсус (К16).** Довод: §1(b) на CC BY-SA 3.0 определя Adaptation като произведение, основано върху Произведението (превод, преработка, аранжировка). Point-in-polygon **не пренася израз** от полигона — резултатът е факт (пространствено отношение) плюс предсъществуващо кратко име; имената са факти. Значи §4(b) ShareAlike не захапва изнесените редове. **ODbL-аналогията „produced work“ е изрично невалидна:** „Produced Work“ е дефиниран термин на ODbL (§1.0, §4.3–4.4), създаден защото ODbL покрива правата върху бази; CC BY-SA няма такава категория — анализът при CC е само „Adaptation или не“. Позицията влиза дословно в `_meta.source_terms["wikimapia"].position`.
50: 
51: **3.3 Зависимостта на G27 (К18).** §4(c) на CC BY-SA 3.0 се задейства при разпространение. Частният geojson не се разпространява — атрибуцията там е provenance. Публичните редове, **АКО позицията по 3.2 издържи**, не са Adaptation → публична атрибуция не се изисква по лиценза. **Но ToS §1.G на Уикимапия** (по-долу, 3.5) иска при „public use of Wikimapia Data and it's derivatives“ връзка към оригиналния обект и „Wikimapia.org“ — дали присвоеното име е „derivative“ по смисъла на §1.G е част от присъдата на Кими (К18). **Присъда К21 (Кими, 06.09 ~04:20): тежкият клон се задейства.** Позицията по 3.2 издържа като лицензен анализ, но §1.G е **договорна клауза**, не лицензна: „Public use of Wikimapia Data and it's derivatives requires…“ — публикуваното име на квартал само по себе си е Wikimapia Data (заглавията са User Submissions по §1.B/§1.F), а полигонът определя кое име се присвоява; приложението се гледа в браузър, тоест „if viewed from any web browser“ е изпълнено. Следствие: **публичната атрибуция е ЗАДЪЛЖИТЕЛНА** за всеки показан ред с уикимапийски квартал — (1) „Wikimapia.org“ с връзка към http://wikimapia.org и (2) връзка към оригиналния URL на обекта (напр. `wikimapia.org/1851926`). Механично: нов български UI низ + `licence_quarter_boundary` в `META_KEYS`, в пиновете на D13 и в двата преписа, в СЪЩИЯ комит; текстът на низа е отделно одобрение на Петър → **решение §7 т. 8**. G27 се пренастройва да сверява този публичен низ, не само частния файл.
52: 
53: **3.4 Sui generis право върху база данни (К15).** §3 в ревизия 1 поднасяше защитата като даденост. Записва се пълно:
54: - **(а) Носителят и юрисдикцията.** Правото е на „производителя“ с съществена инвестиция (чл. 7(1), Дир. 96/9/ЕО); чл. 11 дава защита само на граждани/резиденти на ЕИП и дружества по правото на ЕИП. **Ако производителят на Уикимапия е извън ЕИП, базата не се ползва от sui generis защита в ЕС** и въпросът отпада по същество. **Мярка (06.09, ~03:50):** самите условия на Уикимапия, §3, казват: „The SERVICE is controlled and offered by WikiMapia from its facilities in the United States of America.“ Това е собственото твърдение на оператора, не независима проверка на правната форма и седалището — влиза в `source_terms` като цитат; присъдата дали чл. 11 изключва защитата е на Кими.
55: - **(б) Пълният тест на чл. 7(5).** ~180 полигона от милиони обекта не са съществена част нито количествено, нито качествено. Забраната на чл. 7(5) е за **повтарящо се и систематично** извличане на несъществени части, **което противоречи на нормалното използване на базата ИЛИ наранява неоснователно законните интереси на производителя** — двете кумулативни условия липсваха в ревизия 1. Обходът е систематичен; „противоречие с нормалното използване“ на безплатна публична база за некомерсиална карта е твърдение, което носещият тежестта трудно доказва. **Присъда: дори при съществуваща защита нарушението е оспоримо, не очевидно.**

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 876 -and $n -le 928) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
876: 
877: | Раздел | Присъда | Необходима поправка |
878: |---|---|---|
879: | §2 | НЕГОДНО | Source-kind проверка, еднозначен crosswalk, честен precision floor и работещи фикстури. |
880: | §4 | НЕГОДНО | Затворена decisions схема; конкретни write-set/изпълнител/съобщение; потвърждаване → decisions commit → assembly. |
881: | §5 | НЕГОДНО | Правилна биекция, проверена approval chain; G18 да проверява и разрешените подложки; G28 да допуска само разрешаващ verdict. |
882: | §6 | НЕГОДНО | Предварителен coordinate-only ход с G9, после М2-3 и борд. |
883: 
884: §4 само обещава write-set-овете. §6 има цикъл: мярката **преди борда** чака P8-а, който V2 поставя **след Г2**. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [A2:85](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:85), [V2:149](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:149)
885: 
886: Преди Петър да подпише, договорът трябва да има изпълним ред без цикли, проверима SHA/approval chain, поименни отрицателни фикстури и изрично приет обхват на непокритите квартали.
887: tokens used
888: 65,925
889: **НЕГОДНО за изпълнение в сегашния вид.** Прегледът е read-only; файлове не са променяни. Аритметиката е проверена; геометрични тела и browser export не са изпитвани.
890: 
891: Прочетеният документен обхват е следният; `V2`, `A1`, `A2` по-долу означават съответните планове. Извън него няма инспектирани JSON/GeoJSON/PDF или изпълним код.
892: 
893: ```text
894: docs/activeContext.md | 15557 bytes | 132 lines
895: docs/decisions/010_signed_quarter_boundaries.md | 53242 bytes | 142 lines
896: docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md | 61905 bytes | 264 lines
897: docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | 26249 bytes | 75 lines
898: docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md | 30160 bytes | 107 lines
899: scratch/places_search/granitsi_am2_brief_astra.md | 4915 bytes | 10 lines
900: ```
901: 
902: Декларираният статус на A2 е „за Gate 1“. Всички шест документа преминаха UTF-8 round-trip и проверката за mojibake.
903: 
904: **S14. Мрежата не доказва пълнота.** При зададеното в brief-а подреждане по центрове, 500 m квадратна мрежа гарантира най-близка проба на най-много `500/√2 = 353,55 m` **в покритите клетки**. Дискът е `0,3927 km²`; 100 по-близки центъра могат да изместят квартала — еквивалентна гъстота около `255/km²`. Това е контрапример, не измерена гъстота във Варна. Допълнителните 163 точки не осигуряват горна граница на конкуриращите центрове.
905: 
906: Пропускат се голям полигон с център между пробите, квартал сред плътни сгради, курорт с център извън bbox, компонент на `MultiPolygon`, чийто общ център е далеч, и валиден малък полигон под филтъра `0,04 km²`. API centre, centroid и регистрова точка не са непременно една координата. D7 изрично допуска `MultiPolygon`. [ADR:50](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:50)
907: 
908: Една ограничена проверка: за всеки код без еднозначен кандидат — `count=100` при регистровата точка и четири метрични отмествания ±300 m, включително извън bbox; запазени заявки, отговори и SHA. При 14 кода: максимум 70 заявки, приблизително 32,7 минути. Ненамереното остава „неустановено“. G26 доказва решение за код, а не изчерпателност на Wikimapia. [A2:74](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:74), [V2:142](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:142)
909: 
910: **S15. Решенията нямат достатъчно определен договор.** Минимумът е:
911: 
912: - `_meta`: `schema_version`, `board_sha256`, подписан `registry_sha256`, manifest с SHA на всички входове, версия на канонизацията;
913: - ред: `code`, `choice ∈ {official,reconstructed,wikimapia,none,deferred}`, квалифициран source Feature ID, geometry SHA, подписан crosswalk, `reason`, `decided_by`, неизменен `decided_at`;
914: - само за Wikimapia: `wm_id`, пълният `wm_polygon_sha256`; при останалите — `null`.
915: 
916: Общ `data_sha256` е достатъчен само ако обвързва целия manifest. Повтарянето на page/data SHA във всеки ред е излишно. `fetched_at` и `decided_at` означават различни събития. Raw snapshot SHA, canonical geometry SHA и delivery SHA трябва да имат отделни определения; за `MultiPolygon` липсват правила за подредбата на компонентите и вътрешните пръстени. [ADR:38](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:38), [A2:59](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:59)
917: 
918: **Пряко противоречие:** „всеки Feature има ред … и обратно“ отхвърля валиден `deferred`, който няма Feature. Правилната биекция е решения ↔ трите множества: `official/reconstructed/wikimapia→polygon`, `none→no_boundary` с null geometry, `deferred→_meta.deferred`. G26 изпуска `reconstructed`. [A2:63](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:63), [ADR:44](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:44)
919: 
920: Два записани `decisions_sha256` не доказват одобрение. Нужни са прочит на точния Petar-committed blob, сверка към подписан въпрос с видимо `тяло`, и проверка `code→source ID→frozen geometry`. G25 трябва да отхвърля подменен `wm_id`, дори геометричният SHA да съвпада. [ADR:42](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:42)
921: 
922: На Windows преименуване или `(1)` само не променя SHA; опасностите са избран стар download, редакторна BOM/CRLF конверсия и Git EOL преобразуване. При предложена канонизация UTF-8 без BOM, sorted keys, compact JSON и финален LF, след staging изпълнителят пуска следното с трите реални аргумента:
923: 
924: ```powershell
925: python -c "import sys,json,hashlib,subprocess,pathlib; b=pathlib.Path(sys.argv[2]).read_bytes(); j=json.loads(b.decode('utf-8')); assert b==(json.dumps(j,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8'); assert b==subprocess.check_output(['git','cat-file','blob',':'+sys.argv[1]]); assert hashlib.sha256(b).hexdigest()==sys.argv[3]; print('OK')" "<repo-relative-path>" "<exact-download-path>" "<SHA-shown-by-board>"
926: ```
927: 
928: Това проверява байтовете; schema/approval проверката остава отделна. Две сглобявания от едни входове трябва да дадат байт-еднакъв резултат.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format='%h %s' -- 'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md'" in C:\git\Fire_Varna
 succeeded in 0ms:
2007f30 docs(plan): amendment 2 revision 2a — Kimi К21 verdict embedded: source_terms verdict allowed_with_conditions (7 conditions), public attribution mandatory by Wikimapia ToS §1.G → G27 gets a public half (licence_quarter_boundary META key + Bulgarian UI string with two links), G28 opens only after conditions 1–3, new Petar decision 8 (text and place of the attribution row); still unsigned

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 109 -and $n -le 156) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
109: 
110: ## 6 · Мерките ПРЕДИ борда
111: 
112: - **М2-1 · покритие върху ЗАМРАЗЕНОТО тяло.** Твърдението „20+ от 25 квартала имат полигон“ е на Кими и е опровергано от собствена мярка към 00:36 (по нормализирано име: 15 съвпадения с дефекти — двата „Район Младост“, с.о. „Изгрев“, само „Бриз - юг“ 0,19 km², двусмислената „Комплекс Чайка“; 14 кода без полигон, сред тях `tsentar`, `maksuda`, `kolhozen_pazar`, `kv_levski`, `troshevo`, `hristo_botev`, `rozova_dolina`, `trakia`, `sv_ivan_rilski`, `mladost1`, `mladost2`). Тогава обходът беше на ~30 от 163 семена; повтаря се върху замразения файл и се цитира с неговия sha.
113: - **М2-1б · проверка за пълнота (нова, S14).** Мрежата 500 m гарантира най-близка проба до 353,55 m само в покритите клетки и не дава горна граница на конкуриращите центрове; пропускат се голям полигон с център между пробите, компонент на `MultiPolygon`, курорт извън bbox, полигон под филтъра 0,04 km². Затова: **за всеки регистров код без еднозначен кандидат — `count=100` при регистровата точка и четири метрични отмествания ±300 m (включително извън bbox); запазени заявки, отговори и SHA; ненамереното остава „неустановено“.** При 14 кода ≤ 70 заявки ≈ 33 минути. Тича **след** обхода и **преди** замразяването да се обяви за окончателно. **G26 доказва решение за код, не изчерпателност на Уикимапия.**
114: - **М2-2 · припокриване** (IoU, разлика в площ, симетрична разлика) срещу АГКК. Честно: сравними двойки днес са само Аспарухово/Галата/Чайка; с Одесос МР — нула, докато crosswalk-ът не е подписан. `shapely` 2.1.2 + `pyproj` 3.6.1 — нула нови зависимости.
115: - **М2-3 · местата вътре — днес НЕИЗПЪЛНИМА, и с цикъл (S19).** Популацията е 159, не 174. Координатите трябва да дойдат от пиннатия вход по D10 (`lat`/`lon` в `place_identity.json` — мерено: 375 обекта, **0** с координата); `places_375_hybrid.geojson` е негоден. **Цикълът:** мярката иска P8-а, а план v2 го поставя СЛЕД Г2. Двата изхода са в §7 т. 7: (а) отделен **coordinate-only ход** преди борда, чийто единствен write-set е `lat`/`lon` в `place_identity.json`, покрит от **G9**; или (б) **М2-3 се обявява изрично за след борда** и бордът тръгва без нея.
116: 
117: **Обхватът 38 задължава** преизмерване на уникалността по D12 върху ИЗНЕСЕНИЯ речник + фикстура за сблъсък с немаркирана улица (S7 е).
118: 
119: **Задължителни регресионни фикстури (S17), всяка падаща върху нарочно счупен кандидат:** `street_collision` · `district_retention` · `mladost_kind_collision` · `parent_child` · `order_identity` · `client_cache_matrix`. Положителната „училище св св константин и елена“ трябва да стигне до подписаната идентичност на Френското училище. **Числото „около 150“ отпада като цел** — 159 е допустима популация, не обещана печалба.
120: 
121: ## 7 · Решенията за Петър (седем отворени + едно взето)
122: 
123: 1. **Тръгваме ли по уикимапийския път?** — **ВЗЕТО от Петър** („прегледах районите от уикимапиа… нека ползваме тях“, 06.09 ~00:50). Остава процедурата: бордът започва с **5–6 полигона** с измерени дефекти (двата „Район Младост“, „Комплекс Чайка“, Кайсиева, Аспарухово, Бриз).
124: 2. **Стълбата v3 и D1** (§2, §4) — чужда геометрия с провенанс вместо ръка; `drawn_*` и `screenshot_sha256` стават `null` при внос. Препоръка: **да**.
125: 3. **G18** — статична проверка „борд без чертожен код **и с разрешена подложка**“ вместо да отпадне. Препоръка: **да**.
126: 4. **Лицензът на файла** — на ниво Feature (`_meta.licences[]`) вместо „най-строгият участник“; променя D2 и §6а т. 3. Препоръка: **да** — иначе АГКК полигонът е нерелицензируем. Уикимапийският клон остава **блокиран от G28** до попълнен `verdict`.
127: 5. **Обхватът 32 или 38, заглавното обещание и непокритите квартали.** По мярката към 00:36 **Център, Максуда, Колхозен пазар, Левски, Цветен квартал** нямаха нито официален, нито човешки полигон → `no_boundary`/`deferred`, а проверката „училище цветен квартал“ след пуша става **НЕПРИЛОЖИМА**. Списъкът се преизмерва върху замразеното тяло (М2-1/М2-1б). Препоръка: **38**, с **изрично приет списък на непокритите** в §7 на плана — или **32** и лотът се преформулира.
128: 6. **Реален безплатен ключ на Уикимапия** (К17). Регистрацията иска акаунт — **това е акт на Петър**, не на агент, и не е писмо до институция. Препоръка: **да, преди М2-1б**; при „не“ обходът остава с демо ключ и рискът се записва в `source_terms`.
129: 7. **Редът на М2-3** (S19). Препоръка: **coordinate-only ход с G9 преди борда**; алтернативата е М2-3 да се обяви изрично за след борда.
130: 8. **Публичната атрибуция на Уикимапия в приложението** (К21, ToS §1.G — задължителна, не по избор). Решението на Петър е за **текста и мястото** на българския UI низ в картата на мястото (напр. „Квартал по Wikimapia.org · обектът в Уикимапия“, двете като връзки), не за това дали да има такъв. Без него уикимапийски квартал не може да се публикува (G27 (б), G28). Препоръка: **кратък ред под името на квартала в картата на мястото, само когда изворът е Уикимапия.**
131: 
132: **(Отложено, не решение сега.)** DWG-инструмент: **не сега**; отваря се само ако след борда останат комплекси без приемлива граница, тогава по реда QGIS → LibreDWG → ODA.
133: 
134: ## 8 · Оборване — ЗАПИСАНИ ПРИСЪДИ
135: 
136: **Кими, лицензна леща (К15–К20):** *„§3 е НЕГОДНО за подпис в сегашния вид“*; блокира точно до цитиран ToS в `source_terms`, записана позиция „не е адаптация“ с довод по §1(b) и доказано игнориране на файла от обхода. (Трите входа са попълнени в ревизия 2 — §3.5, §3.2, §3.9; присъдата върху тях е следваща стъпка на Кими.)
137: **Кими К21 (присъдата за G28, 06.09 ~04:20):** `allowed_with_conditions`, седем условия (§3.5); публичната атрибуция по ToS §1.G е задължителна (§3.3, G27 (б), решение §7 т. 8); sui generis отпада по същество; „unreasonable load“ — не; версия 3.0 приета като допускане с „по-строгото печели“.
138: **Astra, механична леща (S14–S19):** *„НЕГОДНО за изпълнение в сегашния вид“* — §2, §4, §5, §6 поименно; преди подпис договорът иска изпълним ред без цикли, проверима SHA/approval верига, поименни отрицателни фикстури и изрично приет обхват на непокритите квартали.
139: 
140: **Приложено (по-строгото печели):** К15 → §3.4 (носител/юрисдикция, пълен чл. 7(5), извличане ≠ повторно използване, пост-фактум оценка) · К16 → §3.2 (позиция с довод, ODbL-аналогията невалидна) · К17 → §3.5 (цитати + URL + `checked_on` от ToS и API страницата; ключът = акт на Петър, §7 т. 6) · К18 → §3.3 (G27 явно зависим, включително от ToS §1.G) · К19 → §3.9, G26-фикстура, **G29**, обявеното допущение · К20 → статусът „годен за четене, не за подпис“ · S14 → **М2-1б** · S15 → §4 договорът на решенията, поправената биекция в **G26**, `reconstructed`, `wm_id` в **G25**, веригата на одобрението, **G30** · S16 → `edge = max(50, precision_m)` по D7, source-kind crosswalk, един изворен Feature на код, забрана за двойно присвояване, родство само подписано · S17 → „около 150“ махнато, шестте фикстури поименно · S18 → подът `max(50, 3×rms, max_residual + raster_error)`, **поправената фикстура rms 20/50**, независимата проверка по 20 точки с `dmax`/`p95` · S19 → §7 т. 7 (цикълът), таблицата с write-set-ове в §4, §7 т. 5 (изричното приемане).
141: 
142: **Отхвърлено / прието с отклонение:**
143: - **Кими К15(а) като освобождаване.** Разклонението „производител извън ЕИП → няма защита“ се записва с цитата от ToS §3, но **не отваря клона**: G28 остава fail-closed до попълнен `verdict`; собственото твърдение на оператора не е независима проверка.
144: - **Кими К17 „масов обход с демо ключ е извън предназначението“** — не се записва като установено нарушение: ToS §1.C.g говори за „unreasonable load“, а скоростта е наложена от самия API; остава **риск-хипотеза** за присъдата.
145: - **Кими К19 т. 1 като „най-силната находка“** — понижена до **поддържане на състояние**: измерено 06.09, `.gitignore:64` вече покрива пътя, `check-ignore` потвърждава, `ls-files` = 0. Гейтът остава, формулировката „пряко нарушение“ — не.
146: - **Astra S14 като искане за изчерпателност на Уикимапия** — отхвърлено: `place.getbyarea`/`place.search` връщат `found=0`, площен обход е невъзможен. Приема се неговата собствена ограничена проверка (М2-1б).
147: - **Astra S15 еднократният ред в конзолата** — приема се по същество, но **като скрипт с отрицателна фикстура** (G30), не като копи-пейст команда: доказателство е проверка, която е тичала и е падала.
148: - **Спирането на обхода** (от ревизия 1) — остава отхвърлено; поръчано е от Петър, а мярката и без това важи само върху замразено тяло.
149: 
150: Само Astra и Кими; никакъв Sol.
151: 
152: ## 9 · Какво НЕ се променя и кога тръгва
153: 
154: Нищо от §4 не тръгва преди Gate 1 **и** Г0-б **и** пуша. Измерено 06.09 ~04:00: Fire_Varna `main` е **ahead 17, behind 2** спрямо origin (комитите на този лот са документи и мерки); varna_3d `rezhimi` — ahead 41. §0.1 казва „нищо ново не се отваря, докато текущият не е пушнат“. Никаква геометрия публично. Никакви кадастрални идентификатори. Един лот в движение. Агентите не пушат.
155: 
156: **Докосванията на Петър** остават **тринайсет** (единайсетте по план v2 + комитът на решенията + комитът на сглобената геометрия); ако §7 т. 7 избере coordinate-only хода, броят се преизчислява в Г0-б. Списъкът се преброява наново в Г0-б.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 56 -and $n -le 108) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
56: - **(в) Извличане ≠ повторно използване.** „Геометрията никога не се публикува“ е щит срещу **reutilization**, не срещу **extraction**. Извличането вече се е случило — обходът тече (§0). **Присъдата по G28 е пост-фактум оценка на извършено действие, не разрешение.**
57: 
58: **3.5 ToS/API (К17) — входът на G28 е попълнен с цитати; присъдата остава на Кими.** `_meta.source_terms["wikimapia"]` носи `{url, checked_on, quote, terms, verdict, position}`, където `quote` е дословен цитат ≤ 2 реда. Записаното към 06.09.2026 (пълната мярка: `scratch/places_search/wikimapia_terms_2026-09-06.md`):
59: - **Условията** — `http://wikimapia.org/terms_reference.html` (достигат се от долния колонтитул „Wikimapia CC-BY-SA“; адресът без `.html` дава 404): **§1.F** „All User Submissions of all users and all Wikimapia Data are freely available for commercial and non-commercial use under Creative Commons license Attribution-ShareAlike through WikiMapia website, WikiMapia API and other current or future WikiMapia services.“ · **§1.G** „Public use of Wikimapia Data and it's derivatives requires special conditions: a. Link to Wikimapia data original url … b. Mention of "Wikimapia.org" (with a link to http://wikimapia.org …)“ · **§1.C.g** „you will not impose an unreasonable load on WikiMapia's infrastructure“ · **§3** услугата се предлага от САЩ. Версията на лиценза в условията **не е посочена** (само „Attribution-ShareAlike“) — дотук приеманото „3.0 Unported“ е допускане, което Кими сверява.
60: - **API документацията** — `https://wikimapia.org/api/`: „We open Wikimapia data free for non-commercial use (as you mention the original data source, according to Wikimapia TOS).“ — разминаване с §1.F („commercial and non-commercial“); нашата употреба е нетърговска и е покрита от двата текста.
61: - **Присъдата К21 за `_meta.source_terms["wikimapia"].verdict` = `allowed_with_conditions`.** Условията дословно по смисъл: (1) геометрията никога публично + G29; (2) публична атрибуция по §1.G (виж 3.3) — задължителна; (3) лиценз на ниво Feature с етикета по 3.8; (4) `licence: "CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)"` — изводът е еднакъв при 3.0 и 4.0; (5) дроселът на API-то (~1/28 s) не се заобикаля — без паралелни сесии, без вдигане на скоростта; всяко отклонение = нова присъда; (6) реален ключ преди М2-1б, или записан риск при отказ; (7) по-квартално „да“ от Петър върху замразен полигон с `wm_id`. G28 отваря клона само след условия 1–3. Присъдата е пост-фактум оценка на извършеното извличане, не разрешение за бъдещо; sui generis въпросът **отпада по същество** (оператор в САЩ, чл. 11 на Дир. 96/9) с нисковероятна резерва за ЕС дружество-носител; „unreasonable load“ по §1.C.g — **не**, скоростта е наложена от самия API.
62: - **Ключът:** „My keys / Create key“ иска акаунт — **регистрацията на реален безплатен ключ е акт на Петър** (самообслужване с ясни условия, не писмо до институция) → решение §7 т. 6. Обходът с демо ключ при скорост, наложена от самия API (~1 заявка/28 s), не е установено нарушение на §1.C.g; дали е „unreasonable load“ — въпрос към Кими, записан като риск.
63: 
64: **3.6 Лиценз на ниво Feature.** Отхвърля се „файлът става CC BY-SA в мига на първия уикимапийски Feature“: противоречи на приетия К3 и е неизпълнимо — същият файл носи АГКК полигони с **неустановени** условия (G22), които не могат да бъдат релицензирани. Значи: **лиценз на ниво Feature** (`license` вече е в D1) + `_meta.licences[]`. Променя §6а т. 3 на план v2 и реда „лицензът на ФАЙЛА е най-строгият участник“ в D2 `:40` → решение §7 т. 4.
65: 
66: **3.7 Резервният път „декларирано местно знание“ ОТПАДА.** Копирана геометрия със `source: "declared_local_knowledge"` не гаси нито BY, нито SA — сменя се етикетът, не произходът; D2 сверява съгласие между две самообявени полета, тоест гейтът ще светне зелено върху лъжа. Петър потвърди линия, но изрично отказа да чертае.
67: 
68: **3.8 Етикетът** (в частния файл): „граница по Уикимапия (обект <id>, свалена <дата>), очертана от доброволци — неофициален извор; CC BY-SA (wikimapia.org/terms_reference.html §1.F; creativecommons.org/licenses/by-sa/); потвърдена от Петър на <дата>; официален полигон няма (проверено 06.09.2026: АГКК, община — заключена, район, ПУП)“. Потвърждението е **отделно поле**, никога авторство. **D2 се допълва:** `official_polygon` → лицензът на извора; `human_polygon` → CC BY-SA с URI и обектен URL; `georef_reconstruction` → лицензът на изходния план; падаща фикстура за всяка нова двойка.
69: 
70: **3.9 Гейтовете като лицензна защита (К19) — измерено днес.** `.gitignore:64` = `/scratch/boundary_gallery/`; `git check-ignore -v` потвърждава, че и `wikimapia_quarters.geojson`, и `index.html` са игнорирани; `git ls-files scratch/boundary_gallery` = **0 проследени файла**. Тоест точката на Кими е **удовлетворена днес** — затова гейтът **G29** не поправя нарушение, а **пази състояние**: `check-ignore` за точните пътища преди всеки пуш на Fire_Varna, с отрицателна фикстура. Второ: **файлът с решения носи САМО `wm_id` + хешове, нула координати** — фикстура в G26. Трето, **обявено допущение:** защитата живее в затворените ключови набори (9-ключовия `_meta` и 13/17-ключовия ред); **всеки нов публичен артефакт-носител (плочки, дебъг-страница) = нов лицензен гейт**, защото G28 гледа само `source` при износа на редове.
71: 
72: **Присъдата на Кими, записана дословно по смисъл:** Петър **не може** да подпише §3, докато ToS не е цитиран в `source_terms` (сега е — 3.5), позицията по 3.2 не е записана с довода си (сега е) и игнорирането не е доказано (измерено — 3.9). Остава **самата присъда на Кими** върху попълнените входове: `verdict` е празен до нея и G28 държи клона затворен. §3 днес е **годен за четене, не за подпис**.
73: 
74: ## 4 · Какво се променя в ходовете
75: 
76: **Р (регистърът) е ПРЕДИ борда.** Измерено: `quarter_registry.json` носи 84 записа, жилищни = **32**, без `tsveten_kvartal` и без Вл. Варненчик I–V. G26 чете обхвата от **подписания** регистър; при обхват 38 Р-1 минава пръв.
77: 
78: **Редът се поправя (S19/S15):** Г1-а борд → **Г2-а сесия по потвърждаване** → **Г2-б комит на решенията (Петър)** → **Г2-в сглобяване**. В ревизия 1 сглобяването стоеше преди потвърждаването.
79: 
80: | Ход | Репо | Изпълнител | Изчерпателен write-set | Дословно съобщение |
81: |---|---|---|---|---|
82: | Г1-а борд | Fire_Varna | Claude Executor | `scratch/boundary_gallery/granitsi_board_06.09/{index.html,board.js,board.css}` — игнорирани | **без комит** |
83: | Г1-б гейтове | varna_3d | Claude Executor | `.gitignore` (`!data/quarters_signed.geojson` след ред 23), `src/qa_quarters_signed.py`, `web/quarters.guard.test.mjs` | `gates: unignore quarters_signed.geojson and add G1/G18 fixtures` |
84: | Г2-а сесия | — | Петър пред борда | — (износ Blob + `<a download>`) | — |
85: | Г2-б решения | Fire_Varna | **Petar1984** | `docs/granitsi/granitsi_decisions_<ISO дата>.json` (проследен, нула координати) | `data: signed quarter decisions <дата>` |
86: | Г2-в сглобяване | varna_3d | Claude Executor → комитът на geojson-а е на **Petar1984** | `src/build_quarters_signed.py`; после `data/quarters_signed.geojson` | `build: assemble quarters_signed.geojson from signed decisions` · `data: signed quarter boundaries v1` |
87: 
88: **Г1-б отменя §6а т. 20 на план v2 (`:230`) и амандамент №12 към №4 т. 6**, който връзваше реда с инструмента.
89: 
90: **Договорът на файла с решения (S15) — затворена схема.** `_meta`: `schema_version`, `board_sha256`, **подписан** `registry_sha256`, манифест със SHA на **всеки** вход, версия на канонизацията, `attribution` (низът от §3.8). Ред: `code`, `choice ∈ {official, reconstructed, wikimapia, none, deferred}`, **квалифициран идентификатор на изворния Feature**, `geometry_sha`, препратка към подписания crosswalk, `reason`, `decided_by`, неизменен `decided_at`. Само при Уикимапия: `wm_id` + пълен `wm_polygon_sha256`; при останалите — `null`. **`fetched_at` ≠ `decided_at`.** Три отделни определения: SHA на суровия снапшот, SHA на каноничната геометрия, SHA на доставката. За `MultiPolygon` се записва правило за подредбата на компонентите и на вътрешните пръстени. **Одобрението не се доказва с два записани `decisions_sha256`:** изпълнителят чете **точния комитнат от Петър блоб**, сверява го с подписания въпрос с видимо `тяло: <sha256>` и проверява веригата `code → изворен идентификатор → замразена геометрия`.
91: 
92: **Г2-в · провенансът.** `geometry_origin` · `imported_from` · `fetched_at` · `chosen_source` · `chosen_reason` · `confirmed_by` · `confirmed_at`; **`drawn_by` / `drawn_at` / `viewport` / `screenshot_sha256` са `null` при внесена геометрия** (гейт за взаимна изключителност). Промяна в D1 → §7 т. 2.
93: 
94: **Бордът.** Показва по код официалните и човешките полигони, написаните места, **блоковете на КАИС с номера като слой-проверка** (амандамент №1 §5 т. 3 — те НЕ отпадат), площ, IoU, извор, дата. Бутони „да“ / „не“ / „отложи“. **Няма код за чертане, няма `POST`. Подложката е локална** (PMTiles/КАИС) — днешната проба тегли `tile.openstreetmap.org` на живо (`index.html:68`), което D2 не допуска. Бордът **не е** инструментът по D11.
95: 
96: **Предгейтовете остават дословно:** **G19** (частно репо — М0.15 и до днес НЕ Е ИЗМЕРЕНО) и **G21** (ФАЗА_0). **DWG** — отложено (§7).
97: 
98: ## 5 · Гейтове
99: 
100: - **G25-а · пинът.** `wm_polygon_sha256` се преизчислява от проследената геометрия; фикстура: подменен връх при непроменен sha. **Ново (S15): G25 отхвърля подменен `wm_id`, дори геометричният SHA да съвпада** — фикстура. **G25-б** е ръчна датирана МЯРКА, не гейт.
101: - **G26 · пълнота и биекция (поправено по S15).** Ревизия 1 казваше „всеки Feature има ред и обратно“ — **това е грешно**: валиден `deferred` няма Feature. Правилната биекция е решения ↔ **трите множества на D4**: `official/reconstructed/wikimapia → polygon`; `none → no_boundary` с `geometry: null`; `deferred → _meta.deferred`. **`reconstructed` беше изпуснат — добавя се.** Всеки жилищен код от подписания регистър има решение; липсващо = ЧЕРВЕНО, поименно. Фикстури: `deferred` код с Feature; Feature без ред; **координата във файла с решения**.
102: - **G27 · атрибуцията (пренастроен по К21).** Две половини, двете червени при липса: (а) билд-гейт във varna_3d върху `quarters_signed.geojson` + `_meta.attribution` на файла с решения — точният низ от §3.8; (б) **публичната половина**: `licence_quarter_boundary` в `META_KEYS` на доставката (в пиновете на D13 и в двата преписа) и българският UI низ с двете връзки по ToS §1.G („Wikimapia.org“ + оригиналният URL на обекта) в картата на мястото, когато `quarter.src` идва от уикимапийски полигон. Фикстура: ред с уикимапийски квартал без публичния низ → ✗.
103: - **G28 · fail-closed.** Отваря се само при **разрешаващ** `verdict ∈ {"allowed", "allowed_with_conditions"}` **И** изпълнени условия 1–3 на К21 (машинно проверими: G29 зелен, G27 (а)+(б) зелени, `license` на всеки уикимапийски Feature попълнен); празен, `blocked` или непознат `verdict` = ЧЕРВЕНО и износът на редове с уикимапийски квартал е блокиран. Днес `verdict` е записан (К21), условия 2–3 още нямат код → клонът е **все още затворен**.
104: - **G22** се разширява по механизъм на `_meta.source_terms[<source>]`, но **изброяването на К8 се запазва дословно**.
105: - **G18** става статична проверка: в борда няма код, който пише връх, **и подложката е от разрешен списък** (фикстура: борд с `tile.openstreetmap.org` или Esri URL → ✗) → решение §7 т. 3.
106: - **G29 · игнорирането (нов).** `git check-ignore -v` за точните пътища + `git ls-files scratch/boundary_gallery` = 0, преди всеки пуш на Fire_Varna; отрицателна фикстура: нарочно проследен файл с геометрия.
107: - **G30 · байтовете (нов, S15).** Каноничен JSON (UTF-8 без BOM, sorted keys, compact, финален LF), байт-равен на `git cat-file blob :<път>`, `sha256` равен на показания от борда; **две сглобявания от едни входове дават байт-еднакъв резултат.** Проверката е **скрипт с фикстура** (BOM, CRLF, стар download), не еднократен ред в конзолата.
108: - **Непроменени:** G1, G17, G19, G21, G23, G24.

codex
Поправките за непълнотата на обхода, source-kind конфликтите и precision floor са изрично записани. Остава да проверя дали договорът за решенията е достатъчно определен и дали новата публична атрибуция се побира в затворените схеми и реда на гейтовете.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p = @('"'docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md'); "'$p | Sort-Object | ForEach-Object { $f = Get-Item -LiteralPath $_; '"'{0} | {1} bytes | {2} lines' -f "'$_,$f.Length,(Get-Content -LiteralPath $_ -Encoding UTF8).Count }' in C:\git\Fire_Varna
 succeeded in 16ms:
docs/decisions/010_signed_quarter_boundaries.md | 53242 bytes | 142 lines
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md | 26249 bytes | 75 lines

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/decisions/010_signed_quarter_boundaries.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 34 -and $n -le 65) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$n=0; Get-Content -LiteralPath '"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md' -Encoding UTF8 | ForEach-Object { "'$n++; if ($n -ge 16 -and $n -le 40) { '"'{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 0ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$files=@('"'docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md','scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md','scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md'); "'$enc = New-Object System.Text.UTF8Encoding($false,$true); foreach ($p in $files) { $bytes=[IO.File]::ReadAllBytes((Join-Path (Get-Location) $p)); $txt=$enc.GetString($bytes); $same=[Convert]::ToBase64String($bytes) -ceq [Convert]::ToBase64String($enc.GetBytes($txt)); $mojibake=[regex]::Matches($txt,'"'[\\u00D0\\u00D1\\u00C2][\\u0080-\\u00FF]').Count; '{0}: UTF8_roundtrip={1}; mojibake_matches={2}' -f "'$p,$same,$mojibake }' in C:\git\Fire_Varna
 succeeded in 27ms:
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md: UTF8_roundtrip=True; mojibake_matches=0
scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md: UTF8_roundtrip=True; mojibake_matches=648
scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md: UTF8_roundtrip=True; mojibake_matches=0

codex
S14, S16, S17 и S18 са затворени на ниво план. S15 остава частично: биекцията и approval chain са поправени, но правилото за `MultiPolygon` още е обещано, без да е определено. При G27 има конкретна празнина: публичният ред не дава на UI достатъчно данни да различи Wikimapia и да построи връзката към избрания обект.
codex
G28 вече задава машинно проверима конюнкция; липсата на бъдещия код сама по себе си не е нов дефект. За S19 остава разминаване: препоръчаният `coordinate-only` ход разрешава само промяна на JSON, а наследеният G9 проверява прегенериран файл; промяната на генератора остава в по-късния P8-а.
codex
**S20: четири RESOLVED, две PARTIALLY. Revision 2a още не е еднозначен изпълним договор.** Проверка само на поправките; без редакции. По-долу **A2** означава проверявания амандамент, **V2** — основния план, **ADR** — ADR 010.

- **S14 — RESOLVED.** М2-1б въвежда ограничената проверка за всеки код без еднозначен кандидат, запазва заявки/отговори/SHA и оставя ненамереното „неустановено“. Изрично: G26 доказва решение за код, не изчерпателност на Wikimapia. [A2:113](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:113)

- **S15 — PARTIALLY.** Поправени са approval chain, проверката срещу подменен `wm_id`, биекцията с `reconstructed`/`deferred` и byte-integrity. [A2:90](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:90), [A2:100](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:100), [A2:101](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:101), [A2:107](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:107) Остават неопределени точните ключове/типове/nullability на част от „затворената схема“, реалните определения на трите SHA обхвата и подреждането на `MultiPolygon`: „се записва правило“ още не е правило. Наследеният D1 определя външния пръстен, но не компонентите и вътрешните пръстени. [A2:90](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:90), [ADR:38](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:38)

- **S16 — RESOLVED.** Добавени са подписан source-kind crosswalk, еднозначен избор, забрана за двойно присвояване към несравними кодове и проверено родство; `edge=max(50,precision_m)` има правилната отрицателна фикстура. [A2:41](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:41), [A2:43](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:43)

- **S17 — RESOLVED на ниво план.** Шестте фикстури са поименни, трябва да падат върху счупен кандидат; положителният French-school случай е запазен; „около 150“ отпада. Поведението на фикстурите остава определено в непроменения амандамент №1. [A2:119](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:119), [A1:25](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25), [A1:38](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:38)

- **S18 — RESOLVED.** Подът е наречен предпазен минимум; грешната фикстура е поправена на rms 20/precision 50; независимите 20 точки изискват доказано същата граница и `dmax/p95`. Без проверката реконструкцията остава свидетел. [A2:37](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:37)

- **S19 — PARTIALLY.** Потвърждаване → Petar decisions commit → assembly е поправено и има конкретни write-set-ове. G18 вече проверява подложката. Но общият ред и предварителният coordinate-only ход остават непълно определени, както е описано по-долу. [A2:78](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:78), [A2:82](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:82), [A2:105](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:105)

**Нови механични дефекти и противоречия:**

1. **G27(b) няма определен път до конкретния Wikimapia URL.** Изисква разпознаване на извора и обектна връзка, но публичният `quarter` остава `{name,code,src}`; D0 запазва общия `SIGNED_POLYGON` канал и изрично не публикува `Feature.source`. Липсва договорен metadata mapping `code→source/URL` или друга изрична схема, която UI да прочете. [A2:47](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:47), [A2:102](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:102), [ADR:36](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:36)

2. **Metadata промяната е възможна, но договорът си противоречи.** Десети `_meta` ключ не нарушава сам по себе си 13/17-ключовите редове; нарушава непроменения деветключов allowlist. A2 изисква добавката, но продължава да разчита на „9-ключовия `_meta`“. Освен това „в СЪЩИЯ комит“ обединява upstream `META_KEYS`/преписите и downstream UI/D13 пиновете през различни репа — противно на подредената доставка по D13. [A2:51](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:51), [A2:70](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:70), [ADR:42](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:42), [ADR:62](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:62)

3. **Новият ред не разпределя всички наследени предпоставки.** Стрелката пропуска Г1-б; неговият нов „изчерпателен“ write-set не обяснява къде остават останалите проверки, Г1-в и независимият одит преди Г2. Това е нееднозначно заместване, не доказана отмяна на старите гейтове. [A2:78](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:78), [A2:83](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:83), [V2:114](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:114), [V2:119](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:119)

4. **Решение 7 не специфицира възпроизводим coordinate-only ход.** Единственият разрешен write-set е `lat/lon` в JSON, докато G9 проверява **прегенериран** файл, а промяната на генератора остава в по-късния P8-а. Нужен е отделен конкретен ход за генератора и данните. Това не доказва неизбежно падане на G9. [A2:115](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:115), [A2:129](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:129), [V2:150](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:150), [ADR:123](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:123)

**G28:** условия 1–3 вече са машинно проверима конюнкция. Остатъчният проблем е недоопределеният G27(b), не самата липса на бъдещ код. [A2:103](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:103)

За външния `qa_fire_varna_places_export.py` използвах локално декларирания договор в ADR:42; самият скрипт не е препрочитан.
tokens used
69,616
**S20: четири RESOLVED, две PARTIALLY. Revision 2a още не е еднозначен изпълним договор.** Проверка само на поправките; без редакции. По-долу **A2** означава проверявания амандамент, **V2** — основния план, **ADR** — ADR 010.

- **S14 — RESOLVED.** М2-1б въвежда ограничената проверка за всеки код без еднозначен кандидат, запазва заявки/отговори/SHA и оставя ненамереното „неустановено“. Изрично: G26 доказва решение за код, не изчерпателност на Wikimapia. [A2:113](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:113)

- **S15 — PARTIALLY.** Поправени са approval chain, проверката срещу подменен `wm_id`, биекцията с `reconstructed`/`deferred` и byte-integrity. [A2:90](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:90), [A2:100](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:100), [A2:101](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:101), [A2:107](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:107) Остават неопределени точните ключове/типове/nullability на част от „затворената схема“, реалните определения на трите SHA обхвата и подреждането на `MultiPolygon`: „се записва правило“ още не е правило. Наследеният D1 определя външния пръстен, но не компонентите и вътрешните пръстени. [A2:90](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:90), [ADR:38](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:38)

- **S16 — RESOLVED.** Добавени са подписан source-kind crosswalk, еднозначен избор, забрана за двойно присвояване към несравними кодове и проверено родство; `edge=max(50,precision_m)` има правилната отрицателна фикстура. [A2:41](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:41), [A2:43](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:43)

- **S17 — RESOLVED на ниво план.** Шестте фикстури са поименни, трябва да падат върху счупен кандидат; положителният French-school случай е запазен; „около 150“ отпада. Поведението на фикстурите остава определено в непроменения амандамент №1. [A2:119](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:119), [A1:25](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25), [A1:38](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:38)

- **S18 — RESOLVED.** Подът е наречен предпазен минимум; грешната фикстура е поправена на rms 20/precision 50; независимите 20 точки изискват доказано същата граница и `dmax/p95`. Без проверката реконструкцията остава свидетел. [A2:37](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:37)

- **S19 — PARTIALLY.** Потвърждаване → Petar decisions commit → assembly е поправено и има конкретни write-set-ове. G18 вече проверява подложката. Но общият ред и предварителният coordinate-only ход остават непълно определени, както е описано по-долу. [A2:78](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:78), [A2:82](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:82), [A2:105](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:105)

**Нови механични дефекти и противоречия:**

1. **G27(b) няма определен път до конкретния Wikimapia URL.** Изисква разпознаване на извора и обектна връзка, но публичният `quarter` остава `{name,code,src}`; D0 запазва общия `SIGNED_POLYGON` канал и изрично не публикува `Feature.source`. Липсва договорен metadata mapping `code→source/URL` или друга изрична схема, която UI да прочете. [A2:47](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:47), [A2:102](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:102), [ADR:36](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:36)

2. **Metadata промяната е възможна, но договорът си противоречи.** Десети `_meta` ключ не нарушава сам по себе си 13/17-ключовите редове; нарушава непроменения деветключов allowlist. A2 изисква добавката, но продължава да разчита на „9-ключовия `_meta`“. Освен това „в СЪЩИЯ комит“ обединява upstream `META_KEYS`/преписите и downstream UI/D13 пиновете през различни репа — противно на подредената доставка по D13. [A2:51](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:51), [A2:70](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:70), [ADR:42](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:42), [ADR:62](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:62)

3. **Новият ред не разпределя всички наследени предпоставки.** Стрелката пропуска Г1-б; неговият нов „изчерпателен“ write-set не обяснява къде остават останалите проверки, Г1-в и независимият одит преди Г2. Това е нееднозначно заместване, не доказана отмяна на старите гейтове. [A2:78](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:78), [A2:83](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:83), [V2:114](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:114), [V2:119](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:119)

4. **Решение 7 не специфицира възпроизводим coordinate-only ход.** Единственият разрешен write-set е `lat/lon` в JSON, докато G9 проверява **прегенериран** файл, а промяната на генератора остава в по-късния P8-а. Нужен е отделен конкретен ход за генератора и данните. Това не доказва неизбежно падане на G9. [A2:115](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:115), [A2:129](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:129), [V2:150](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_05.09.md:150), [ADR:123](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:123)

**G28:** условия 1–3 вече са машинно проверима конюнкция. Остатъчният проблем е недоопределеният G27(b), не самата липса на бъдещ код. [A2:103](C:/git/Fire_Varna/docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:103)

За външния `qa_fire_varna_places_export.py` използвах локално декларирания договор в ADR:42; самият скрипт не е препрочитан.
