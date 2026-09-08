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
session id: 01a07ef2-2016-7e82-b2d8-d745af25a8d4
--------
user
S38 · Външно око (леща механика/ГИС): ПОЛИГОНИТЕ НА imot.bg КАТО СЛОЙ „РАЙОНИ“. Ново (08.09 ~13:00): imot.bg чертае собствени полигони за 98 района на Варна и ги дава през мобилния си JSON API без вход (GET; details → поле points; съседните райони споделят върхове точно, 0 застъпвания помежду им, общо 93,1 km²); взети са 95 (тези с обяви) в C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson; втора независима агенция mirela.bg има 73 начертани района (mirela_varna_areas_08.09.geojson). Петър ги видя: „супер са, сравни и другите“. Сравнението с нашите 60 подписани + предложените (raioni_table_08.09.json, raioni_compare_08.09.json; мярка: IoU с нашия със същото име, % на imot в нашия, дупки = частни адресни точки извън всяка наша клетка): 41 съвпадат (IoU ≥ 0,6), 20 със същото име, но друго чертане (Център IoU 0,37 — Петър вече каза, че нашият Център е сбъркан; Стадион Спартак 0,09 — нашият е сградата, техният е районът южно от бул. Васил Левски; Генералите 0,55; Погреби 0,47; Максуда 0,29; Победа 0,41; Евксиноград 0,44; Манастирски рид 0,47; Салтанат 0,51; Горна Трака 0,15; Левски 1/2 срещу нашия Левски 0,24/0,33; Владислав Варненчик 1/2 срещу Владиславово/Кайсиева 0,24/0,0; к.к. Чайка срещу кв. Чайка 0,0; Виница-север срещу Добрева чешма 0,0), 20 нови, които запълват дупки (ВИНС-Червен площад 219 сгради, Чаталджа 211, Гранд Мол 190, ЖП Гара 66, Пристанище 353, Метро 39, м-т Планова 126…), 6 нови, пресичащи няколко наши (Лятно кино Тракия 641 сгради в дупка + 30 % в Тракия + 24 % в Център; ХЕИ; Автогара; Бизнес хотел; Централна поща 67 % Център + 32 % Тракия), 7 нови вътре в наш (Базар Левски ⊂ Левски, Конфуто ⊂ Победа, Фестивален ⊂ Гръцка махала…). Покритие на дупките: 3 217 от 4 328 сгради. „Общината“ не е район в imot.bg (има го в address.bg/homes.bg без полигони). Въпроси: (1) МОДЕЛЪТ: imot.bg-плочката като ОТДЕЛЕН слой „район“ (всекидневно име) над нашия слой „квартал“ (подписан) — или замяна на подписаните полигони там, където imot е по-добър/по-подробен? Кой слой дава думата в адреса на пожарникаря и в търсенето („Операта (Център)“? „Левски 1“ срещу „кв. Левски“?); как се държат двата слоя без застъпване (клетки = пресичане на двата разделяния?); (2) ПРИОРИТЕТ при разлика със същото име: кога печели подписаният (Петър го е подписал) и кога чужденецът (две агенции съгласни — IoU imot/mirela ≥ 0,7); правило, не списък; (3) ПРОВЕНАНС и гейтове за външен полигон-слой: запис на източник/дата/id, проверка на топологията (споделени върхове, 0 застъпвания, покритие на сградите), какво става при промяна на сайта (замразен снапшот, хеш), какво пътува публично (само имена?); (4) ДУПКИТЕ, които остават (1 111 сгради извън и imot): как се доказва, че са реални (порт, промзони, села) — маска; (5) какво се променя в плана „Адресите по полигон“ v3 и в ADR 010 (D6/D8) при два слоя. Не пипай нищо. До 800 думи: препоръка + условия, с числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя измерванията, плана v3 и ADR 010 само за четене. Ще дам правило за двата слоя, приоритета и гейтовете, с ясно разграничение между измерено и предложено.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -TotalCount 150' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
 succeeded in 318ms:
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
`--freeze` Petar's signature unlocks, and with nothing else:

- `FrozenDiffTest::test_the_live_engine_replays_the_artefact` Â· `::test_rows_carry_the_p7_measure`
- `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket` Â· `::test_the_bucket_is_the_signed_answers`
- `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket` Â· `::test_the_bucket_is_the_signed_answers`

Every one of them reads `expectations.json` (grep: `require_expectations`, `EXP[`,
`gate_answers(`, `anchor_block(`, `claim(`). Proved in an isolated clone of this
commit: sign `expectations.json` and the two manifests, run `--freeze` once, run
the suite â†’ **0 red**; the clone is thrown away. `ReleaseGateSignatureTest` is the
one test that reads `signed_by`, and it is the fixture the plan asked for:
an unsigned artefact â†’ `gates.release` BLOCKED.

## Waiting for a signature

- **Ð¤Ð°Ð·Ð° A of the cleanup plan** â€” the four artefacts listed above; then `--freeze` once, tests green, `run_gates` green, audit, and Petar's push. `docs/plans/ÐŸÐ›ÐÐ_Ð˜Ð—Ð§Ð˜Ð¡Ð¢Ð’ÐÐÐ•_v2_05.09.md` Â§A.4.
- `decisions/007_address_path_v2.md` â€” `Proposed â€” awaiting Petar (Gate 1)`.
- `decisions/005_sw_cache_lifecycle.md` â€” `Proposed â€” awaiting Petar (Gate 1)`.
- `plans/hotels_search_plan.md`, `plans/sw_cache_lifecycle_fixes.md` â€” `DRAFT â€” AWAITING PETAR SIGNATURE (Gate 1)`.
- ADR 009 â€žÐ˜Ð´ÐµÐ½Ñ‚Ð¸Ñ‡Ð½Ð¾ÑÑ‚, Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ¸, Ð³ÐµÐ¹Ñ‚Ð¾Ð²Ðµâ€œ â€” Ð¤Ð°Ð·Ð° B of the cleanup plan, not written yet.

Parked scope (nothing opens until Ð¤Ð°Ð·Ð° A is pushed): `plans/PARKED.md`.

## Forbidden here

`git push`, Worker deploy, any publish â€” Petar only. Personal data in `data/`, in issues or in docs. New runtime or build-time dependencies, Bulgarian UI wording changes, a first load over 5 MB â€” not without Petar. Cross-repo edits from this checkout. `--freeze` on the search reference without a signed manifest. Writing `signed_by: "ÐŸÐµÑ‚ÑŠÑ€"` â€” an agent writes `pending â€” ÐŸÐµÑ‚ÑŠÑ€` and nothing else.

## Where things are

`index.html` (the whole app shell) Â· `data/hydrants.json` (runtime dataset) Â· `data/{places,hotels,place_categories}.json` (the places search, delivered from varna_3d) Â· `data/search_index.json` + `data/address_rows.json` (built in Varna_buildings) Â· `gates/` (the release gates: sha pins, key sets, cadastral scan, coverage, signed facts) Â· `worker/` (Cloudflare Worker source) Â· `sw.js` (ADR 002/005) Â· `scratch/places_search/` (the reference engine, the manifests, the boards) Â· `docs/decisions/` (ADRs) Â· `docs/plans/` (the task contracts) Â· `docs/archive/` (frozen chronicles).

Doctrine shared with Varna_buildings: ADR 004 â†’ Varna_buildings ADR 058. varna_3d generates the places delivery and consumes the hydrants for its 3D map.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --files --hidden -g '"'!'"\\.git/**' -g '"'!node_modules/**'"' -g '*010*' -g '*S38*' -g '*v3*' -g '*raioni*' -g '*imot*' -g '*mirela*' -g '*plan*' -g 'AGENTS.md' -g '*004*' -g '*003*' docs scratch AGENTS.md" in C:\git\Fire_Varna
 succeeded in 420ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 128]
M  data/hotels.json
M  data/place_categories.json
M  data/places.json
A  gates/probe/b3_g11.py
M  index.html
D  scratch/places_search/granitsi_fixtures_06.09.json
A  scratch/places_search/granitsi_fixtures_07.09.json
 M scratch/places_search/lot1v_v_reference_manifest.json
 M scratch/places_search/probe_out/token_parity.json
M  scratch/places_search/probe_places_fv.mjs
M  scratch/places_search/recall_sweep.py
A  tests/granitsi_client_probe.mjs
A  tests/test_b3_gates.py
M  tests/test_granitsi_fixtures.py
M  tests/test_hotels_public_bundle.py
M  tests/test_places_public_bundle.py
?? scratch/places_search/COMMIT_MSG_B3.txt
?? scratch/places_search/adresi_astra_S38_08.09.md
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
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

 succeeded in 373ms:
AGENTS.md
docs\plans\places_search_plan_2026-09-02.md
docs\plans\places_phase2_plan.md
docs\plans\hotels_search_plan.md
docs\plans\h4_kmz_apply_plan.md
docs\plans\h2_kmz_adapter_plan.md
docs\decisions\010_signed_quarter_boundaries.md
docs\decisions\004_measurement_doctrine.md
docs\decisions\003_dual_claude_code_governance.md
docs\audits\submission_status_and_moderation_plan_20260508.md
docs\audits\issue_ingest_plan_20260508.md
docs\audits\cleanup_execution_plan_20260508.md
docs\audits\bug_fixes_plan_20260508.md
docs\audits\backfill_and_submission_extension_plan_20260509.md
docs\audits\address_backfill_plan_20260511.md
scratch\places_search\adresi_astra_S38_08.09.md
scratch\governance_migration_plan.md
scratch\audit_2026-09-03\verify\verify_2\v3_fix.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --files --hidden --no-ignore --max-count 20 --max-columns 200 -g 'AGENTS.md' -g '*010*' -g '*004*' -g '*Адрес*' -g '*адрес*' -g '*v3*' -g '*raioni*' -g '*imot*' -g '*mirela*' -g '*S38*' docs scratch/boundary_gallery scratch/places_search | Sort-Object" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -Encoding UTF8 -TotalCount 28' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath scratch/places_search/adresi_astra_S38_08.09.md -Encoding UTF8 -TotalCount 150' in C:\git\Fire_Varna
 succeeded in 536ms:
docs\decisions\004_measurement_doctrine.md
docs\decisions\010_signed_quarter_boundaries.md
docs\plans\ПЛАН_Адресите_по_полигон_08.09.md
docs\plans\ПЛАН_ЛОТ1в_имена_и_адреси.md
scratch/boundary_gallery\granitsi_preview_05.09\imot_api_points_08.09.json
scratch/boundary_gallery\granitsi_preview_05.09\imot_area_points_08.09.json
scratch/boundary_gallery\granitsi_preview_05.09\imot_areas_08.09.geojson
scratch/boundary_gallery\granitsi_preview_05.09\imot_areas_report_08.09.json
scratch/boundary_gallery\granitsi_preview_05.09\imot_bg_varna_areas_08.09.json
scratch/boundary_gallery\granitsi_preview_05.09\imot_bg_varna_polygons_08.09.geojson
scratch/boundary_gallery\granitsi_preview_05.09\mirela_preview_08.09.html
scratch/boundary_gallery\granitsi_preview_05.09\mirela_varna_areas_08.09.geojson
scratch/boundary_gallery\granitsi_preview_05.09\raioni_compare_08.09.json
scratch/boundary_gallery\granitsi_preview_05.09\raioni_compare_08.09.py
scratch/boundary_gallery\granitsi_preview_05.09\raioni_imot_overlaps_08.09.json
scratch/boundary_gallery\granitsi_preview_05.09\raioni_preview_08.09.html
scratch/boundary_gallery\granitsi_preview_05.09\raioni_table_08.09.json
scratch/boundary_gallery\v3_neigh_0513.geojson
scratch/places_search\adresi_astra_S38_08.09.md

 succeeded in 627ms:
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


 succeeded in 631ms:
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
session id: 01a07ef2-2016-7e82-b2d8-d745af25a8d4
--------
user
S38 · Външно око (леща механика/ГИС): ПОЛИГОНИТЕ НА imot.bg КАТО СЛОЙ „РАЙОНИ“. Ново (08.09 ~13:00): imot.bg чертае собствени полигони за 98 района на Варна и ги дава през мобилния си JSON API без вход (GET; details → поле points; съседните райони споделят върхове точно, 0 застъпвания помежду им, общо 93,1 km²); взети са 95 (тези с обяви) в C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson; втора независима агенция mirela.bg има 73 начертани района (mirela_varna_areas_08.09.geojson). Петър ги видя: „супер са, сравни и другите“. Сравнението с нашите 60 подписани + предложените (raioni_table_08.09.json, raioni_compare_08.09.json; мярка: IoU с нашия със същото име, % на imot в нашия, дупки = частни адресни точки извън всяка наша клетка): 41 съвпадат (IoU ≥ 0,6), 20 със същото име, но друго чертане (Център IoU 0,37 — Петър вече каза, че нашият Център е сбъркан; Стадион Спартак 0,09 — нашият е сградата, техният е районът южно от бул. Васил Левски; Генералите 0,55; Погреби 0,47; Максуда 0,29; Победа 0,41; Евксиноград 0,44; Манастирски рид 0,47; Салтанат 0,51; Горна Трака 0,15; Левски 1/2 срещу нашия Левски 0,24/0,33; Владислав Варненчик 1/2 срещу Владиславово/Кайсиева 0,24/0,0; к.к. Чайка срещу кв. Чайка 0,0; Виница-север срещу Добрева чешма 0,0), 20 нови, които запълват дупки (ВИНС-Червен площад 219 сгради, Чаталджа 211, Гранд Мол 190, ЖП Гара 66, Пристанище 353, Метро 39, м-т Планова 126…), 6 нови, пресичащи няколко наши (Лятно кино Тракия 641 сгради в дупка + 30 % в Тракия + 24 % в Център; ХЕИ; Автогара; Бизнес хотел; Централна поща 67 % Център + 32 % Тракия), 7 нови вътре в наш (Базар Левски ⊂ Левски, Конфуто ⊂ Победа, Фестивален ⊂ Гръцка махала…). Покритие на дупките: 3 217 от 4 328 сгради. „Общината“ не е район в imot.bg (има го в address.bg/homes.bg без полигони). Въпроси: (1) МОДЕЛЪТ: imot.bg-плочката като ОТДЕЛЕН слой „район“ (всекидневно име) над нашия слой „квартал“ (подписан) — или замяна на подписаните полигони там, където imot е по-добър/по-подробен? Кой слой дава думата в адреса на пожарникаря и в търсенето („Операта (Център)“? „Левски 1“ срещу „кв. Левски“?); как се държат двата слоя без застъпване (клетки = пресичане на двата разделяния?); (2) ПРИОРИТЕТ при разлика със същото име: кога печели подписаният (Петър го е подписал) и кога чужденецът (две агенции съгласни — IoU imot/mirela ≥ 0,7); правило, не списък; (3) ПРОВЕНАНС и гейтове за външен полигон-слой: запис на източник/дата/id, проверка на топологията (споделени върхове, 0 застъпвания, покритие на сградите), какво става при промяна на сайта (замразен снапшот, хеш), какво пътува публично (само имена?); (4) ДУПКИТЕ, които остават (1 111 сгради извън и imot): как се доказва, че са реални (порт, промзони, села) — маска; (5) какво се променя в плана „Адресите по полигон“ v3 и в ADR 010 (D6/D8) при два слоя. Не пипай нищо. До 800 думи: препоръка + условия, с числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя измерванията, плана v3 и ADR 010 само за четене. Ще дам правило за двата слоя, приоритета и гейтовете, с ясно разграничение между измерено и предложено.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -TotalCount 150' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
 succeeded in 318ms:
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
`--freeze` Petar's signature unlocks, and with nothing else:

- `FrozenDiffTest::test_the_live_engine_replays_the_artefact` Â· `::test_rows_carry_the_p7_measure`
- `Lot1vABucketTest::test_the_live_engine_replays_the_new_bucket` Â· `::test_the_bucket_is_the_signed_answers`
- `Lot1vBBucketTest::test_the_live_engine_replays_the_new_bucket` Â· `::test_the_bucket_is_the_signed_answers`

Every one of them reads `expectations.json` (grep: `require_expectations`, `EXP[`,
`gate_answers(`, `anchor_block(`, `claim(`). Proved in an isolated clone of this
commit: sign `expectations.json` and the two manifests, run `--freeze` once, run
the suite â†’ **0 red**; the clone is thrown away. `ReleaseGateSignatureTest` is the
one test that reads `signed_by`, and it is the fixture the plan asked for:
an unsigned artefact â†’ `gates.release` BLOCKED.

## Waiting for a signature

- **Ð¤Ð°Ð·Ð° A of the cleanup plan** â€” the four artefacts listed above; then `--freeze` once, tests green, `run_gates` green, audit, and Petar's push. `docs/plans/ÐŸÐ›ÐÐ_Ð˜Ð—Ð§Ð˜Ð¡Ð¢Ð’ÐÐÐ•_v2_05.09.md` Â§A.4.
- `decisions/007_address_path_v2.md` â€” `Proposed â€” awaiting Petar (Gate 1)`.
- `decisions/005_sw_cache_lifecycle.md` â€” `Proposed â€” awaiting Petar (Gate 1)`.
- `plans/hotels_search_plan.md`, `plans/sw_cache_lifecycle_fixes.md` â€” `DRAFT â€” AWAITING PETAR SIGNATURE (Gate 1)`.
- ADR 009 â€žÐ˜Ð´ÐµÐ½Ñ‚Ð¸Ñ‡Ð½Ð¾ÑÑ‚, Ð¿Ð¾Ð´Ð¿Ð¸ÑÐ¸, Ð³ÐµÐ¹Ñ‚Ð¾Ð²Ðµâ€œ â€” Ð¤Ð°Ð·Ð° B of the cleanup plan, not written yet.

Parked scope (nothing opens until Ð¤Ð°Ð·Ð° A is pushed): `plans/PARKED.md`.

## Forbidden here

`git push`, Worker deploy, any publish â€” Petar only. Personal data in `data/`, in issues or in docs. New runtime or build-time dependencies, Bulgarian UI wording changes, a first load over 5 MB â€” not without Petar. Cross-repo edits from this checkout. `--freeze` on the search reference without a signed manifest. Writing `signed_by: "ÐŸÐµÑ‚ÑŠÑ€"` â€” an agent writes `pending â€” ÐŸÐµÑ‚ÑŠÑ€` and nothing else.


web search: 
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.py -Encoding UTF8 -TotalCount 150' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/decisions/010_signed_quarter_boundaries.md -Encoding UTF8 -TotalCount 145' in C:\git\Fire_Varna
 succeeded in 790ms:
# -*- coding: utf-8 -*-
"""Compare the everyday-area polygons of imot.bg (primary) and mirela.bg (control) with OUR partition (signed +
proposed) and with the gap mask. Outputs raioni_compare_08.09.json (aggregates only) for the report and the board.
For every imot.bg area: area, IoU with the same-named mirela polygon, which of our cells it overlaps (share of the
imot polygon), how many gap buildings (private pins outside every cell) it would cover, and a verdict class."""
import json, io, sys, math, re, collections
from shapely.geometry import shape, Point
from shapely.ops import unary_union
from shapely.strtree import STRtree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KM2 = 111.32 * 111.32 * math.cos(math.radians(43.21))
def nz(s):
    s = (s or "").lower()
    s = re.sub(r"[„“\"”().,\-–]", " ", s); s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^(кв|ж к|жк|зк|р н|м т|к к|в з|с о|с|местност|район|квартал)\s+", "", s)
    return s.strip()
imot = json.load(open("imot_bg_varna_polygons_08.09.geojson", encoding="utf-8"))
mir = json.load(open("mirela_varna_areas_08.09.geojson", encoding="utf-8"))
part = json.load(open("partition_v2_08.09.geojson", encoding="utf-8"))
signed = json.load(open("quarters_signed_08.09.geojson", encoding="utf-8"))
rows = json.load(open("address_rows_08.09.json", encoding="utf-8"))
fo = rows["field_order"]; pins = [(r[fo.index("lat")], r[fo.index("lng")]) for r in rows["rows"]]
cells = [(shape(f["geometry"]).buffer(0), f["properties"]) for f in part["features"]]
tree = STRtree([c[0] for c in cells])
allcells = unary_union([c[0] for c in cells])
gap_pts = [Point(lo, la) for la, lo in pins if not any(cells[i][0].contains(Point(lo, la)) for i in tree.query(Point(lo, la)))]
gap_tree = STRtree(gap_pts)
pin_tree = STRtree([Point(lo, la) for la, lo in pins])
M = {nz(f["properties"]["h1"]): shape(f["geometry"]).buffer(0) for f in mir["features"]}
SIGNED = {nz(f["properties"]["name"]): f["properties"]["code"] for f in signed["features"]}
out = []
for f in imot["features"]:
    p = f["properties"]; g = shape(f["geometry"]).buffer(0)
    if g.is_empty: continue
    k = nz(p["name"]); m = M.get(k)
    iou = None
    if m is not None and not m.is_empty:
        iou = round(g.intersection(m).area / g.union(m).area, 2)
    over = []
    for i in tree.query(g):
        c, cp = cells[i]
        x = g.intersection(c).area
        if x > 0: over.append((round(100 * x / g.area, 1), round(100 * x / c.area, 1), cp["name"], cp["src"]))
    over.sort(reverse=True)
    n_gap = sum(1 for i in gap_tree.query(g) if g.contains(gap_pts[i]))
    n_all = sum(1 for i in pin_tree.query(g) if g.contains(pin_tree.geometries[i]))
    uncovered = round(100 * g.difference(allcells).area / g.area, 1)
    same = [o for o in over if nz(o[2]) == k or nz(o[2]).replace("кв ", "") == k]
    if same and same[0][0] >= 60: cls = "същият квартал, друго чертане"
    elif uncovered >= 50: cls = "запълва дупка"
    elif over and over[0][0] >= 70: cls = "подрайон на " + over[0][2]
    else: cls = "пресича няколко наши"
    out.append(dict(name=p["name"], slug=p["slug"], n_adverts=p["n_adverts"], n_pts=p["n_pts"], area_km2=round(g.area * KM2, 3), iou_mirela=iou,
                    overlaps=[dict(pct_of_imot=a, pct_of_ours=b, ours=c, src=d) for a, b, c, d in over[:6]], pct_not_in_ours=uncovered,
                    buildings_inside=n_all, gap_buildings_inside=n_gap, cls=cls, has_ours=(k in SIGNED)))
out.sort(key=lambda r: -r["gap_buildings_inside"])
summary = dict(n_imot=len(out), n_mirela=len(mir["features"]), gap_buildings_total=len(gap_pts),
               gap_covered_by_imot=sum(1 for pt in gap_pts if any(shape(f["geometry"]).buffer(0).contains(pt) for f in imot["features"])),
               classes=collections.Counter(r["cls"] for r in out))
json.dump(dict(summary=summary, rows=out), open("raioni_compare_08.09.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(summary)
for r in out[:40]:
    print("%-28s %4d обяви %6.3f km²  IoU mirela %-5s  дупка: %4d сгради (всички %5d)  извън нашите %4.0f %%  %s  %s" % (r["name"], r["n_adverts"], r["area_km2"], r["iou_mirela"], r["gap_buildings_inside"], r["buildings_inside"], r["pct_not_in_ours"], r["cls"], "; ".join("%s %.0f%%" % (o["ours"], o["pct_of_imot"]) for o in r["overlaps"][:3])))

 succeeded in 809ms:
# ADR 010 · Граници, подписани от човек

**Статус:** Proposed (05.09.2026) — **чернова: необорена, неподписана.** Става `Accepted` в комита Г0-б на плана, СЛЕД оборването от Кими и Astra и СЛЕД Gate 1; до него този файл не пипа `docs/plans/PARKED.md` и `docs/activeContext.md`. Лотът се открива само по изричната дума на Петър, цитирана дословно в комита Г0-б.

**Предусловия — всяко проверимо, нито едно обещано:**

1. Доставка A е пушната (`fd13907`, 05.09 16:55) **и четирите публикувани хеша са сверени с локалните** — `docs/activeContext.md:3`: hotels `46a44ce82f15`, places `329310f577e8`, categories `874e33cd00e2`, **index.html `3d3bf79b58bf`**. Това е условието на S5, не само пушът.
2. **A.2-11 е изпълнен и одитиран като ЗАТВАРЯЩА стъпка на Фаза A**, под собствения си подписан план (`ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` + амандаменти №10/№11), преди този лот да се обяви. A.2-11 не се комитва по този ADR и не чака него.
3. **P1 е отпушен от Петър** (`PARKED.md:9`). Този ADR + ПЛАН v2 СА датираният план по `PARKED.md` „Как се вади ред оттук“ т. 3; §8 на плана е неговото оборване; редът се маха в Г0-б.
4. **ФАЗА_0 е подписана или условие 4 е потвърдено изрично.** `varna_3d/docs/decisions/ФАЗА_0_лицензи.md:4` = „⏳ чака подпис · нищо не се строи преди подпис“ (мерено). Докато този ред стои така, `_meta.faza0_signed` **не може** да е `true` — това е гейт G21, не самообявено поле — и G1 отказва И „по сгради“, И „по улици“.
5. **Видимостта на `github.com/Petar1984/varna_3d` — НЕ Е ИЗМЕРЕНО** (М0.15, иска мрежа). Гейт **G19** я мери преди Г2; публично репо събаря D3 и отваря решение §6.3.
6. **Редът на Фаза B–E спрямо „Границите“ е обявен от Петър** (решение §6.2).
7. **Непушнатото е преброено:** varna_3d 41 ahead, Varna_buildings **1 ahead**, Fire_Varna 1 ahead (М0.16) — лотът ги изпраща заедно (§3 т. 7–9).
8. **Официалните извори са проверени преди чертането** (05.09, 16:40–17:50; по думите на Петър „намери административните граници на кварталите… не съм сигурен, че тези квартали, които имаме, отговарят точно“): Astra, трети опит (`scratch/places_search/granitsi_astra_official_boundaries_05.09.md`) и пряка проверка на АГКК INSPIRE оттук (`scratch/places_search/agkk_inspire_measure_05.09.md`). Резултатът е **D0** (стълбата на изворите), **Ф0-б** в плана (пощенският указател като кандидат-свидетел), гейтове **G22–G24** и по-малка вечер за Петър.

Допълва ADR 008 D9 и ADR 006; не пипа ADR 007; не изпреварва ADR 009 (Фаза B). D3, D6–D11, D14 и D19 важат за `varna_3d` и `Varna_buildings`: канонът е този файл, а `varna_3d/docs/decisions/README.md` получава указателен ред в комита на **своя** изпълнител (правило 6).

## Контекст

**Думите на Петър (05.09):** „не виждам училища в Цветния квартал, а знам, че там има… училището в Св. Св. Константин и Елена не излиза, като напиша «училище св св константин и елена»… искам да имаме ясните граници на кварталите и всичко, което е в тези квартали, да излиза в търсачката… искам да изследваме целия клас такива грешки и да ги изчистваме по траен и фундаментален начин.“

**Всяко число тук има команда в §0 на плана.**

**Клас A · няма граници.** 174 от 375 реда без квартал; **159 без нито един канален id**, 8 `pending_signature`, 7 само с `locality` (М0.2). 14 от 32-та жилищни кода носят нула реда (М0.3). „Цветен квартал“ не е в регистъра; около `node/9664925200` стоят **15** места на ≤ 900 m (не 14, както казва v1 §1), най-близкото 3 ОУ „Ангел Кънчев“ на **132,6 m**, всички с `quarter = null` (М0.11).

**Клас B · търсенето не намира и това, което ИМА квартал.** Индексът гради фразите през `significant_tokens` (`scratch/places_search/recall_sweep.py:424-442`, `:515-533`), заявката слепва суровия остатък (`:1120`). `училище св св константин и елена` → M2, 12 чужди реда; същата **без** „и“ → A3-location, 1 ред = Френското училище (М0.8). Две поправки на v1: **сблъсъчните токени са 11, не 7** (+`1`,`2`,`i`,`s`, защото `Rec._loc_tokens:664-679` чете суровите токени) и **типовият префикс е поредица токени с две арности** (`к.к.`→`[k,k]` срещу `кк`→`[k]`; `ж.к.`→`[zh,k]` срещу `жк`→`[zhk]`; `с.о.`→`[s,o]`; `м-т`→`[m,t]`; `кв.`→`[kv]`) (М0.6).

**Клас C · живата карта** беше стара; затворен с публикацията на A.

**Никой отворен извор не носи жилищните граници.** OSM: **13 полигона `place=suburb|neighbourhood|quarter`, всички вилни зони и местности, нито един жилищен квартал**; източник `scratch/places_search/osm_quarters_measure_05.09.md:7`, Overpass снапшот `2026-09-04T21:46Z`, bbox 43.13–43.33 / 27.80–28.10 — **днес НЕПРОСЛЕДЕН, влиза в git с Г0-а (М0.17)**; до този комит присъдата няма проследим извор и не се цитира извън него. Само 27 от 32-та кода имат дори възел; трите курорта нямат — 131 от 201 типизирани реда без OSM свидетел (М0.11). Машинният път е пенсиониран: `m6000_private/number_viewer/quarters_drawn_v1.geojson` — **126 обвивки** (М0.18), **IoU 0,13** срещу праг 0,70 (`docs/plans/ПЛАН_ЛОТ_Границите.md:25`). За центъра остава един извор — назован човек. **За петте района и за шест квартала обаче има официален полигон** (по-долу).

**Официалните извори, проверени 05.09 (Astra трети опит + АГКК INSPIRE пряко; М0.19–М0.23).** Присъдата на Astra по 10 извора: *„Не установих проверен публичен набор с пълни официални граници на именуваните жилищни квартали във Варна.“* Граници носят ДРУГИ единици: петте района (ЗТДСОГГ 1995, чл. 4, по улици), полицейските микрорайони на МВР, устройствените зони на ОУП, проектното каре „17-ти микрорайон“ в Левски, ПУП-ПРЗ на ж.к. Чайка (публикуван, контурът неинспектиран). Само присвояване адрес → квартал дават: пощенският указател на „Български пощи“ (копие при КРС, PDF 17.05.2018, 11 344 012 B: жилищен район · улица · номера от/до; напр. ул. „Нарцис“ → ж.к. „Васил Левски“), изборният класификатор 29.10.2023, блоковете на МВР, общински публикации, адресната номенклатура на ГРАО (набор с означение CC0; улица/ж.к./квартал са АЛТЕРНАТИВНИ единици). **АГКК INSPIRE (`inspire.cadastre.bg/arcgis/rest/services`, снимка `10-2019-v0`), проверено оттук:** `Administrative_Unit` 5-ти ред = петте района (кодове `10135-01…05`) — **375 от 375 места в правилния район, 0 разминавания** с нашия `district.code`; `Geo_Names` Surface = официални полигони за **Владиславово, Виница, Галата, Аспарухово, Златни пясъци, Чайка** (последният носи и второ име „Св. Св. Константин И Елена“ върху СЪЩАТА геометрия, 3,07 km², и лежи между курортите: нашите 34 от 35 хотела с `kk_konstantin_elena` са извън всяка градска повърхнина на АГКК) — където и ние, и АГКК имаме квартал, съгласие **109 от 110**; единственият спор е ПАРК ХОТЕЛ БЕЛВЮ (REG Златни пясъци, вътре в „Чайка“); чисти печалби, ако полигонът е свидетел: **12 места** (Аспарухово 8, Владиславово 1, Виница 1, Златни 2), спорни 8 в „Чайка“ (4 от тях са висящите сблъсъци); центърът е ЕДИН полигон „Варна“ 19,53 km² със 134 от 174-те празни реда и без подквартали; `Geo_Names` Point = 722 официални ИМЕНА без граница, 53 от 84-те кода на регистъра имат такава точка (вкл. **Левски** и **Максуда**), 14 жилищни нямат, „Цветен квартал“ го няма и като точка. Условията за повторна употреба на INSPIRE услугата **не са установени** (Astra: „специален лиценз не установих“; страниците на КАИС и геопортала не носят лицензен ред — проверено 05.09 17:45) → G22.

## Решения

**D0 · Стълбата на изворите за квартал (добавено 05.09, 17:50, след проверката на официалните извори).** Четири степени, от най-силната: **(1) официален полигон на АГКК** (INSPIRE `Geo_Names` Surface; днес 6 кода) — влиза като Feature в СЪЩИЯ файл `quarters_signed.geojson` със `source: "agkk_inspire_gn"`, `method: "official_polygon"`, `drawn_by: "АГКК INSPIRE GN 10-2019-v0"`, `localid` на АГКК в `witnesses[]`, `approved_by: Петър` (той одобрява включването, не рисува); **ЗАКЛЮЧЕН, докато `_meta.agkk_terms` не носи URL + дата на проверени условия за повторна употреба (G22)**; **(2) написан извор** REG / KAIS / НТР — както днес, рангове 0–2, непроменени; **(3) официално адресно присвояване** (пощенският указател 2018; номенклатурата на ГРАО) — КАНДИДАТ-канал `POST-2018` в ранг 2 до `KAIS-addr`, който влиза САМО след мярката Ф0-б на плана и с подписан от Петър crosswalk „жилищен район“ ↔ регистров код; преди отчета никакъв код за него; **(4) деклариран полигон** (`source: "declared_local_knowledge"`) — ранг 3, D6. Полигоните (1) и (4) минават през ЕДИН канал `SIGNED_POLYGON` с еднакви гейтове (G1) и еднакво правило „пише само в празен, безспорен, неръбов ред“; **`source` на Feature-а е колона в леджера и ред в картончето** („по официален полигон на АГКК“ / „по местно знание, Петър, дата“), не нов публикуван `src`. За ЕДИН код не може да има едновременно официален и деклариран полигон — кодът е в точно едно множество на D4 със своя `source`; Петър може да ЗАМЕНИ официалния с деклариран само с довод в `note` (напр. АГКК „Чайка“ с две имена). Спор официален полигон ↔ написан извор (днес 1: ПАРК ХОТЕЛ БЕЛВЮ) е `disputed` по D6 — никога автоматичен победител. **Районът получава контролен гейт (G23):** АГКК AU5 ↔ `district.code` = 375/375 днес; всяко бъдещо разминаване = STOP. Суровите отговори на АГКК (`scratch/places_search/agkk_inspire_2026-09-05/`) остават **непроследени** до G22 и никога не влизат в публичен файл.

**D1 · Класът на извора и ЗАДЪЛЖИТЕЛНИТЕ полета (К1 + S3).** Всеки Feature носи затворен подреден набор `properties`, чието ПРИСЪСТВИЕ се проверява преди коя да е стойност: `code` · `name` · `kind` · `parent` (или `null`) · `source: "declared_local_knowledge"` · `signed_by` · `drawn_by` · `approved_by` · `drawn_at` · `approved_at` (ISO `2026-09-05`, никога точкувани) · `method` · `basemap` · `precision_m` · `version` · `license` · `viewport {center, zoom, bearing, pitch, width, height}` · `visible_layers {id: stamp}` · `screenshot_sha256` · `approval_digest` · `witnesses[]` · `note`. Липсващо поле = STOP. Дайджестът: фиксиран подреден списък в `_meta.digest_fields`, координати като низ с 6 знака, външен пръстен обратно на часовника, ротиран към лексикографски най-малкия връх, каноничен JSON, `sha256("v1\n" + геометрия + "\n" + json)`.

**D2 · Лицензът се решава ТУК (К4).** Таблица `method` → лиценз, проверявана за СЪГЛАСИЕ: „по памет“ / „по огради“ → **CC0-1.0**; „по сгради“ → **КАИС „Отворени данни“, атрибуция АГКК, CC0 не се твърди — ЗАКЛЮЧЕН, докато `_meta.faza0_signed` не е `true`, а той не може да е `true`, докато `ФАЗА_0_лицензи.md:4` носи „чака подпис“ (G21)**; „по улици“ → **ЗАКЛЮЧЕН винаги** (нарушава условие 4, `ФАЗА_0_лицензи.md:25-26`), отключва се само с изричен подписан ключ. **Лицензът на ФАЙЛА е най-строгият участник.** Подложка: нашата PMTiles основа (ADR 002 D8) или КАИС; **никога Esri** — инструментът отказва връх, докато `map.getLayoutProperty("sat","visibility") === "visible"` (`varna_3d/web/index.html:880`), проверено от G18.

**D3 · Къде живее геометрията и как е вързана.** Каноничен файл: **`varna_3d/data/quarters_signed.geojson`**, версиониран в git. `m6000_private` НЕ е git репо; `Fire_Varna/data/` е публичната папка и отпада по S5; **това решение стои върху предусловие 5 и не е валидно, докато G19 не покаже частно репо.** Файлът се хваща от `varna_3d/.gitignore:4` и `:23` → иска `!data/quarters_signed.geojson` **след ред 23** (М0.9). **Публикува се само `quarter: {name, code, src}` и изведеният `zone`; геометрия никога.** К5 ↔ S5: следвам S5 за РЕДА и К5 за ВЕРСИЯТА — `polygon_version` и `polygon_sha256` са ЗАДЪЛЖИТЕЛНИ в `expectations.json._meta` и в `data/place_categories.json._meta`, **никога на ред** (редът е 13/17 ключа, `index.html:6275`, `:6281`; `_meta` на доставката е затворен 9-ключов набор, `qa_fire_varna_places_export.py:62`, налаган на `:550`). **Ограничение, мерено:** `SIGNABLE` (`gates/release.py:175-183`) е затворена шесторка с пътища спрямо Fire_Varna, а `blob_at` (`:223`) чете блоб от ТОВА репо — **чужд път е недостъпен, значи геометрията НЕ може да получи ред клас „артефакт“.** Дайджестът ѝ пътува през `expectations._meta.polygon_sha256` + ред клас „въпрос“ с видимо `тяло: <sha256>` + G4 и G7. Разширяването на `SIGNABLE`/`blob_at` към чуждо репо е **съзнателно отложено за Фаза C**.

**D4 · Регистър ↔ полигон: три декларирани множества.** Всеки жилищен код (kind ∈ {кв, жк, кк}, ЧЕТЕН ОТ РЕГИСТЪРА, никога от литерал) попада в точно едно от `polygon` · `no_boundary` (Feature с `geometry: null`, RFC 7946, с довод и подпис) · `deferred` (`_meta.deferred`, с довод и дата, броен дълг). Липса и в трите = ЧЕРВЕНО. К7 т. 1: празен квартал носи `_meta.no_places: [{code, why, signed_by, signed_at}]`; гейтът сравнява МНОЖЕСТВА: „жилищни кодове с нула доставени реда ⊆ `no_places` ∪ `deferred`“, падайки поименно. **Ако `tsveten_kvartal` попадне в `no_boundary`/`deferred`, проверката след пуша №2 става НЕПРИЛОЖИМА и това се записва в отчета** (решение §6.28).

**D5 · Ново име само с ≥ 2 свидетеля (К3) и обратим път.** „Цветен квартал“: свидетел 1 = подписът на Петър; свидетел 2 = `node/9664925200` с 15 места на ≤ 900 m. Втори свидетел може да е и АГКК именувана точка (Левски и Максуда имат; М0.21), ред от пощенския указател или общинска публикация с адрес (М0.22) — по-силни от OSM възел, защото са официални. При ЕДИН свидетел името е `alias`, не код. **Отмяна:** ред клас „въпрос“ + обратен диф с двоен запис + махане на кода от петте затворени списъка в един комит на Fire_Varna; фикстура: код в доставка, който вече не е в регистъра → червено. Записът влиза през конвейера на Varna_buildings (D14).

**D6 · `SIGNED_POLYGON` — свидетел ранг 3 (S1/К2).** Нов канал под `REG-*` (0), `KAIS-quar` (1), `KAIS-addr` (2). ОТДЕЛЕН блок в `varna_3d/src/fire_varna_locations.py` **между ред 873 и 875** — след записа на `picked` в `out` (867–873), преди `if signed:` (875) — и **никога в цикъла `offered/ranked/conflict` (785–853)**, където `conflict` бланкира вече написано поле (`:834`, `:852`) и вкарва реда в `pending_signature`. **Шест състояния:** `confirmed` · `compatible` (деклариран родител/дете, БЕЗ замяна и без уточняване) · `disputed` · `edge_pending` (D7) · `override_noted` · `written`. Пише САМО в ред без нито един свидетел, без `pending`, извън ръба, в точно един полигон (или в декларираното дете), с `witness=[CH_SIGNED_POLYGON]` и кода в `channels[CH_SIGNED_POLYGON].ids` (`qa_fire_varna_m6.py:304-308`). Полигон-местност никога не пълни `quarter` — `classify(code) == field` (`KIND_CLASS:118`), с падаща фикстура. `_narrow` (`:907-917`) уточнява САМО вътре в полигонния канал. **`SIGNED_OVERRIDE` се пази безусловно (S1):** при 12-те подписани хотела блокът само сравнява и пише `override_noted` в леджера; никога не мени полето, никога не влиза в `signed_vs_witness`, а `CHANNEL_RANK` не получава ключ `SIGNED_OVERRIDE`. **`disputed` е ЛЕДЖЕР-САМО:** редът остава дословно както е, отива в `polygon_review`, нищо публично не се мени. Това е **обявено ОТКЛОНЕНИЕ от К2** (решение §6.4): `LOC_KEYS` са точно 3 (`index.html:6311`, `:6531-6533`), няма ключ за `winner`/`reason`, а „падане до район“ би изтрило написан от по-силен канал квартал. Таблицата на К2 е входна карта за реда в опашката; спорът се версионира (`polygon_review[i].polygon_version`). **159 е ДОПУСТИМАТА популация, не write-set.** 8-те сблъсъка не се решават от полигона.

**D7 · Ръбът: `max(50, precision_m)` в EPSG:32635 върху пиннати ИЗВОРНИ координати (S2 + К5).** `_meta.precision_floor_m = 50`; гейтът отказва `precision_m < 50`. Забранено е да се четат изнесените координати (`fire_varna_locations.py:968-982` прави точно това и се маха от полигонния път). Мери се И точката, И закотвеното тяло (`evidence.kais_i`); разминаване → `edge_pending`. Формулата е `shapely.geometry.shape(f["geometry"]).boundary.distance(point)` — през `shape`, защото подписан квартал реалистично е MultiPolygon. Проекция: `place_identity.make_projection()` (`:219-236`); `pyproj` 3.6.1, `shapely` 2.1.2 — нула нови зависимости. **Никакво местене, никакъв snap.** `SIGNED_POLYGON_BORDER` НЕ става публикуван `src` — **обявено ОТКЛОНЕНИЕ от К5** (решение §6.16).

**D8 · Йерархията — само подписана и геометрично доказана.** Родство се чете единствено от `parents` (днес 6 записа), ациклично И доказано: **дете ⊆ родител в рамките на `precision_m` буфер**; фалшив `parent` = червено. **Числовата опашка в `is_child` (`:488-503`) не е родство при полигони.** „≤ 1 полигон на място“ важи между НЕСРАВНИМИ квартали. **В ПРАЗЕН ред пише детето; в ред с написан квартал полигонът НИКОГА не уточнява.** Възраждане 1–4 нямат `parents` — поправка в регистъра, ПРЕДИ кода (D14).

**D9 · Версии, диф и откат (К5, S1).** **ВСЯКА нова версия иска подпис на Петър.** Прагове: > 2 места сменят квартал ИЛИ > 10 % площ → двоен запис преди/след и пълно преизмерване; под тях — обикновен отчет. `--diff <предишна>` е ГЕЙТ с изход ≠ 0 над праговете (G15). **Версия 1: диф-гейтът е НЕПРИЛОЖИМ, не червен.** **Откат на лоша версия:** предишната подписана версия се връща като НОВА версия (`version` расте, `previous_version` сочи отхвърлената, `note` носи довода), минава пълния G1+G15 и се комитва от Петър; никакво `git revert` върху геометрия и никакво тихо редактиране. Всеки диф се предава като ред клас „въпрос“ (по D3 не може да е „артефакт“).

**D10 · Леджерът и пиновете (S1, S2).** Към **23-те колони** (М0.4): точка/тяло + CRS, кандидат-полигони, канал, `dist_to_edge_m`, състояние по D6, старо/ново по КОД, хешове на геометрия/регистър/алгоритъм, `approval_digest`. В `_meta`: `pins_polygons` до `pins_m6` (`:1111`), `polygon_review` до `pending_signature` (`:1140`), и **`base_rev` — ревизията P7, срещу която се мерят D18 и манифестът-данни**. **Координатата идва от `lat`/`lon`, добавени в `data/place_identity.json`** (мерено: 375 обекта, 0 с координата) като НОВ ПИНАТ вход в `RECORDED_INPUTS` (`:91-92`), с гейт G9. **Пиновете на `quarters_signed.geojson`, `place_identity.json` и `web/varna_buildings_3d.geojson` влизат в `build_inputs` (`:1247-1253`) И СЕ СВЕРЯВАТ в `_check_pins` (`:623-639`) и в G-M6.** `--inputs` (`:1305-1310`) е ПИСАТЕЛ, пуска се веднъж.

**D11 · Инструментът и provenance (S3).** Свой „режим граница“ във `varna_3d/web`, **нула нови runtime зависимости** (`web/vendor` държи само maplibre-gl **5.7.2** — `web/vendor/maplibre-gl.js:3` — и pmtiles 4.3.0; М0.18). `pitch = 0` + `map.setTerrain(null)` (`web/index.html:1962-1963`), `#pitch` disabled, кликът отговаря ПРЕДИ хидранта (`:4571`). Лентата на неточността: `line-width` по `156543.03392·cos(43,2°)/2^z` → z13 3,6 · z16 28,7 · z18 114,9 px за 50 m (М0.13). Слоеве-свидетели: КАИС телата, 375-те пина, OSM етикет-точките, **предишната версия като отделен слой**. Записва целия набор на D1. `preserveDrawingBuffer` — **един условен ред** зад `?granitsa` (`:828-841`). **STOP:** безусловен `preserveDrawingBuffer`; какъвто и да е `POST` в `serve.py`. Износ = Blob + `<a download>`.

**D12 · Търсенето (клас B) — К6 + S4.** Идемпотентен `location_key(toks) -> (type, phrase)`, приложен ИДЕНТИЧНО върху индекса и остатъка, дефиниран върху **СПИСЪК ОТ ТОКЕНИ**. Типовият префикс е поредица с двете си арности. Хвърля съюза „и“ и префикса, **пази числата** и затворен списък посоки. Правило: остатъкът == пълната фраза на ТОЧНО ЕДИН запис, иначе уникална СЪСЕДНА подфраза; пазач: число / посока / „sveti“ никога не квалифицира. **Областта е ИЗНЕСЕНИЯТ речник**, премерен наново преди подпис. **Типът СТЕСНЯВА само когато е изричен И съвпада с поне един кандидат.** **Двусмислието не ражда нов видим текст** (`AGENTS.md:138`) — **обявено ОТКЛОНЕНИЕ от К6**: уточнителят при двусмислие е отложен, защото иска дословен български текст от Петър (решение §6.20); днешното поведение при двусмислие се запазва и се пази от замразена заявка. **Родител ⊃ дете живее в ИЗНОСА** (per-code `type` и `parents` по КОДОВЕ); затворените списъци → `_meta` до `zone_generic_words` (`build_place_categories.py:566`), fail-closed. **Паритет:** `window.__places.locationKey(q)` влиза в корпуса `probe_out/token_parity.json` (**759 низа**, М0.18). **11 подписани вектора** + проби съюз, точкувана форма, число, посока, двусмислие, йерархия. Манифест по `bundle:ordinal` („РОЯЛ“ ×2; `release.compare()` сравнява по име, `gates/release.py:780-823`). **Смяна на КЛОН при непроменени редове = делта от първи ред.**

**D13 · Атомност през ТРИ репа (S5/S6).** Един комит през две репа не съществува. **Подредената тройка важи за ДАННИТЕ, не за инструмента:** инструментът (Г1) и гейтовете му са предпоставка и стоят извън тройката. Тройката е: **(1) Varna_buildings** — записът, `parents`, преподписаната константа (D14); **(2) varna_3d** — резолверът, двата износни гейта (`qa_fire_varna_export.py:191`, `qa_fire_varna_places_export.py:323`), вторият препис (`qa_fire_varna_m6.py:58-64`), износът; **(3) Fire_Varna** — **блобовете влизат в СЪЩИЯ комит със затворените списъци**: `QUARTER_SRC` (`index.html:6313`), `QUARTER_CODES` (`:6317`), `LOCALITY_CODES` (`:6322`), трите SHA пина (`:6288-6290`), `LEGACY_BUNDLE_SHA` (`:6301`), `PLACES_CACHE` v6 → **v7** (`:6265`), и поименно пиновете на двата теста: `PLACES_SHA256`/`BYTES` 122089/`GZIP9` 13728, `HOTELS_*` 148685/13084, `CATEGORIES_*` 75818/9104, `QUARTER_BY_SRC` (точно равенство), `QUARTER_CODES`, `LOCALITY_CODES`, `LOCATION_COUNTS` {quarter 20, district 5, locality 5}, `LEGACY_ROWS` 18, `LOCALITY_COUNT`; плюс baseline → `fd13907` (`signed_by: "pending — Петър"`) и подмяната на allow-файла. Числата се ПРЕМЕРВАТ след чертането. Тихата смърт, доказана: непознат `src` → `validLocation` false (`:6528-6534`) → `validTypedLocation` (`:6535-6541`) → `validatePlaces2` (`:6569-6576`) → `null` → `places2 = []`, хотелите остават (`:6627-6640`) — **150 места изчезват мълчаливо**; `accept` сверява SHA само при `crypto.subtle` (`:6605`) → кешът задължително на v7. **Манифестите са ТРИ** (`gates/release.py:157-159`): `lot1v_v_manifest_BASE_P7.json` = дифът на ДАННИТЕ (P7→P8 по `place_id`), `lot1v_v_manifest_P7_F12.json` = дифът на ПОВЕДЕНИЕТО, `lot1v_v_reference_manifest.json` = манифестът на референцията; и трите се преизползват в съществуващите слотове с `_meta.what` и изричен ред „името е остаряло“. Имената живеят на **ПЕТ ръчни места**: `gates/release.py:157-159`, `:175-183`, `manifest_anchor_gate.py:42-44`, `recall_sweep.py:3070-3071`, `recall_sweep.py:2661`. **Замразените тела са ТРИ** (амандамент №11 т. 4): референцията `recall_sweep_rows.json` (вързана през `expectations._meta.reference`), `expectations.json`, и паритетният корпус `probe_out/token_parity.json`, който **днес не е вързан от нищо** и влиза в `expectations._meta.inputs`.

**D14 · Регистърът е подписано тяло (S5).** `Varna_buildings/js/lib_quarter_registry.mjs:35` заключва `schema_version`, `id`, `display`, `kind`, `aliases`, `parents`; `:45` държи `REGISTRY_SIGNED_SHA256`; `:121-127` хвърля „never patch the constant to make a build pass“. Затова: (1) промяната е **СОБСТВЕН датиран план в Varna_buildings със собствен §7 (дефиниция за готово)**, минаващ през неговите Approval gates (`AGENTS.md:273-275`) **и през Кими и Astra** (§0.3), чиято присъда влиза в **собствен амандамент — нов датиран файл** в същата папка; (2) константата се преизчислява и **подписва от Петър, в негов комит**, заедно с данните; (3) `node js/test_quarter_registry.mjs` тича в кръга (G5); (4) **агент никога не пипа константата**. Преди комита: нула съвпадения на новото име в 449 `quar` + 19 813 `addr` и нула сблъсък на `match_key` (М0.14); след комита `qa_fire_varna_location_isolation.py` зелено (G6/G10) — `place_zones._registry:252-255` индексира БЕЗ вид.

**D15 · Гейт 0 преди опашката.** `ЗА_ПОДПИС_Г.md` не се ПИШЕ, преди да е зелено: `release.find_queue` е рекурсивната версия; в HEAD има точно една опашка; в `gates/allow/` има точно един json (`run_gates.py:199-217`). Архивът на опашките е **извън** `scratch/places_search`. G0 е гейт-ред на всяка стъпка, чийто write-set пипа опашка или allow-файл.

**D16 · Идентичности и write-set-ове.** Всеки комит носи изчерпателен write-set и дословно съобщение (таблицата е в плана §2). `Claude Architect` за планове и решения, `Claude Executor` за изпълнение, `Petar1984` само за `gates.sign`, подписаната геометрия и регистъра. Ръчният комит на Петър във varna_3d/Varna_buildings е **втори, назован клас** до амандамент №4 т. 6 и влиза като **амандамент — нов датиран файл**.

**D17 · Дайджестът на тялото за доставка Г.** Амандамент №11 приема вариант (а) изрично „за доставка A“. За доставка Г вариантът се **преобявява** (решение §6.5): важи (а) — несъвпадение се прощава само когато последният комит по артефакта е на `Petar1984` — и G12 проверява точно това.

**D18 · Написаният квартал не се променя.** След P8 всеки от **201-те** реда с написан квартал (М0.4) ЗАПАЗВА кода си. Базата „преди“ е назована: `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`, където `<base_rev>` е `_meta.base_rev` на леджера (D10) — същата ревизия, която храни манифеста-данни. Проверката е команда с изход ≠ 0 (G17).

**D19 · Интервалът на замразяването е обявен, изброен и ограден.** `location_phrases` е подписана претенция в `expectations.json` (`tests/test_places_search_gate.py:464-478` я сверява с `REF.LOC_PHRASES`), а `--freeze` пренаписва очакванията едва СЛЕД подписа (амандамент №11 т. 3). Значи между F13-а и единственото `--freeze` `python -m unittest discover -s tests` е червен по конструкция. Това не е „червено по замисъл“, а **обявен интервал с гейт**: изпълнителят записва при отварянето му ТОЧНИЯ набор падащи тестове (G20), той трябва да е подмножество на назования в плана §2, всеки тест извън набора = STOP, и след `--freeze` наборът е ПРАЗЕН. Интервалът не пресича нито един гейт-ред, който твърди зелено.

**D20 · Затварящият документен комит.** Новите четири хеша се вписват в `docs/activeContext.md` СЛЕД пуша, в отделен комит на `Claude Architect` (Г3), който Петър пуска втори път. Локалното ≠ пушнатото за времето между двата пуша е очаквано и е назовано в §3 на плана.

## Как е изпълнена всяка приета атака

| Атака | Къде | Отклонение |
|---|---|---|
| К1 задължителни свойства | D1 | — |
| К2 спорът | D6 | **ДА** — леджер-само; без `winner`/`reason`; редът не пада до район → §6.4 |
| К3 два свидетеля | D5 | — |
| К4 лицензът в лота | D2, G21 | — |
| К5 версия, диф, откат | D3, D7, D9, G15 | **ДА** — `SIGNED_POLYGON_BORDER` не се публикува → §6.16 |
| К6 нормализатор + вектори | D12 | **ДА** — уточнителят при двусмислие отложен → §6.20 |
| К7 празен квартал / припокриване | D4, D8 | — |
| S1 ранг 3 + `SIGNED_OVERRIDE` се пази | D6, D8, D10 | — |
| S2 ръбът | D7 | — |
| S3 provenance | D1, D11 | — |
| S4 идентичности | D12 | — |
| S5 атомност и „varna_3d не се приема за частно“ | D3, D13, D14 | **ДА (условно)** — канонът е varna_3d при доказано частно репо; **G19 мери преди Г2** → §6.3 |
| S6 четирите счупвания | D6, D8, D12, D13 | — |

Таблицата се сверява от одитора на Г0 (read-only) и от Кими/Astra при оборването: всеки ред има **или** непразна клетка „къде“, **или** маркер „ДА“ с номер на решение в §6; ред без едно от двете е находка. Скрипт за това не се пише — архитектът не пише код, а стойност за картата няма (решение на архитекта, §6а т. 22 на плана).

## Последствия

**+** Петте района са доказано верни спрямо официалната граница (375/375); шест квартала получават официален полигон без нито един нарисуван връх; 12 места получават квартал с извор АГКК още преди вечерта; 159 реда без нито един написан свидетел могат да получат квартал по проследим път; 201-те написани получават второ око, чието несъгласие остава ВИДИМО и чийто код е защитен от гейт (D18); „училище цветен квартал“ и „училище св св константин и елена“ стават възможни.

**−** Честните цени: една вечер на Петър — по-къса след D0 (остатъкът: 26 жилищни кода без официален полигон, от които центърът няма НИКАКЪВ официален извор), но с непроверима дължина (144,80 km² изпъкнала обвивка); **единайсет негови докосвания**; 8-те сблъсъка остават `pending` и G-M6 остава изход 3 (G8); всяка нова версия е нов подпис; шест затворени списъка, три манифеста и три репа мърдат в подредена тройка; регистърът иска собствен план, собствено оборване и преподписана константа; геометрията не може да е подписан артефакт по днешния `SIGNABLE`; лицензът на „по улици“ може да отнеме CC0; обявен червен интервал (D19).

## Какво НЕ е

Не е връщане към машинните обвивки (126 обвивки, IoU 0,13). Не е OSM като съдия. **Не е замяна на регистъра с АГКК:** официалният полигон пише само в празни редове, спорът с написан извор е видим, а суровите отговори на АГКК не се публикуват и не се проследяват преди G22. Не е сваляне на пощенския указател „за всеки случай“ — Ф0-б тръгва само с думата на Петър (11,3 MB през сателита). Не е нова зависимост — `terra-draw`/`mapbox-gl-draw` отпадат, **geojson.io също отпада** (празната подложка е входът, който роди обвивките). Не е поправка на едно училище: поправят се съюзът, префиксът, числата, посоките и 11-те сблъсъчни думи. **Не решава 8-те `pending_signature`.** Не публикува геометрия, `place_id`, `SIGNED_POLYGON_BORDER` или нов ключ в реда. Не е промяна на ADR 007 и не е ADR 009. **Съзнателно отложено, с име и дата:** разширяването на `SIGNABLE`/`blob_at` към чуждо репо и преименуването на манифестните слотове (Фаза C); `POST` в `serve.py`; `place_id` в блобовете (ADR 009, Фаза B); уточнителят при двусмислие (иска дословен текст от Петър); изнасянето на фрази за всичките 32 кода; кодовете в `_meta.deferred` — **броен дълг**, не мълчание.

## Гейтове

Всеки ред е команда с изход ≠ 0, с назован файл и с отрицателна фикстура, която ТРЯБВА да падне преди да се пипнат данни. Планът §7 изброява всичките.

| # | Команда (файл) | Отрицателна фикстура |
|---|---|---|
| G0 | `python -m gates.release` (Fire_Varna) | втора опашка, **комитната** в scratch-клонинг → блок; два json в `gates/allow/` → ✗. Таблицата „Как е изпълнена всяка приета атака“ се сверява от одитора на Г0 и от Кими/Astra (ред без „къде“ и без „ДА“ + §6 номер = находка), не от скрипт |
| G1 | `python src/qa_quarters_signed.py` (нов, varna_3d) | 17 фикстури в `--break-me`: самопресичане · дублиран код · код извън регистъра · жилищен код извън трите множества · припокриване > `max(50, precision_m)` · деклариран родител без съдържание · дете без деклариран родител · полигон-местност за `quarter` · `method:"по улици"` без ключ · `method:"по сгради"` при `faza0_signed:false` · `basemap`/`visible_layers` = `sat` · лиценз, несъгласен с метода · липсващо задължително property · `precision_m` = 25 · разминат `approval_digest` · липсващ/празен файл = ЧЕРВЕНО · `--diff`: версия, мърдаща 3 места, и версия, мърдаща 11 % площ |
| G2 | `python src/qa_quarters_license.py` | `.geojson` с кадастрален низ ВЪТРЕ в координатен масив (+ доказателство, че СТАРИЯТ гейт е зелен) · `cadnum` в `properties` · `2026.09.05` червено / `2026-09-05` зелено. Поправят се `data_files()` (`:85-86`) и `walk_coords` (`:106-118`) |
| G3 | `python src/qa_no_cad_ids.py` | новият проследен файл е ВЪТРЕ в обхвата, не в `ALLOW` |
| G4 | `python src/qa_quarters_author.py` (нов): `git ls-files --error-unmatch data/quarters_signed.geojson` **и** `git log --format='%an' -1 -- …` == `Petar1984` | празен изход или непроследен път = ЧЕРВЕНО (fail-closed) |
| G5 | `node js/test_quarter_registry.mjs` (Varna_buildings) | регистър без преподписан `REGISTRY_SIGNED_SHA256` → червено |
| G6 | `python src/qa_registry_name_clash.py` (нов): 0 съвпадения в 449 `quar` + 19 813 `addr`, 0 сблъсъка на `match_key` | псевдоним, който прави стар запис двусмислен → G-ISO ✗ |
| G7 | четящ прогон `python src/fire_varna_locations.py` през `_check_pins` | подменен байт в `quarters_signed.geojson` / `place_identity.json` → `die` |
| G8 | `python src/qa_fire_varna_m6.py` → **изход 3, `fails` = 0, точно 8 `pending` (същите осем имена)** | девети `pending` или ≥ 1 `fail` = STOP. Публикацията остава забранена от Фаза A (`ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` §A.4) и се отпушва само от Фаза D — решение §6.29. Петте нови избора се ДОБАВЯТ към `choices` (`:173-176`): `channel`, `polycode`, `edge`, `dispute`, `child`; `CHANNEL_RANK` се чете с `.get` (`:310`, `:314` днес хвърлят `KeyError`) |
| G9 | сверка на прегенерирания `place_identity.json` | ≥ 1 разминат `place_id`/`kais_i`/`kais_d_m` → STOP |
| G10 | `python src/qa_fire_varna_location_isolation.py` → 4/4 | мръднат чужд артефакт → ✗ |
| G11 | `python scratch/places_search/recall_sweep.py` (report-only) срещу назован изход: 140 замразени в 6 кофи + `tokens` 45 / `trigger_today` 33 (`m7_trigger_tokens.json._meta.measured`) + 0 непокрити делти; `node scratch/places_search/probe_places_fv.mjs` над 759 низа + `locationKey`; **контролните заявки се мерят ТУК, преди пуша** | нарочно разминат JS клон → паритетът пада |
| G12 | `python -m gates.release` | делта без подписан ред; ред „да“ без видимо поле `тяло`; блок „да“ с най-нов комит на агент; дайджест по D17; мутиран `probe_out/token_parity.json` → `_meta.inputs` ✗ |
| G13 | `python -m gates.run_gates` | **G13-а (преди подписа):** допустими жълти са ТОЧНО „4 · покритие спрямо подписания baseline“ и „6 · release“, докато артефактите носят `pending — Петър`; всяко друго жълто и всяко червено = STOP. **G13-б (след подписа):** 7/7 зелени, 0 жълти |
| G14 | `python -m unittest discover -s tests` → 0 червени | извън интервала на D19; `QUARTER_BY_SRC` е точно равенство |
| G15 | `python src/qa_quarters_signed.py --diff <предишна>` | над праговете на D9 изход ≠ 0; версия 1 = неприложим; откат = нова версия по D9 |
| G16 | куката `.git/hooks/pre-push` + пушът | само Петър; без `--no-verify` |
| G17 | `python src/qa_written_quarters_stable.py` (нов) — 201 написани реда срещу `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json` | нарочно сменен код на един написан ред → изход ≠ 0 |
| G18 | `node web/quarters.guard.test.mjs` (нов) | пазачът при `visibility === "visible"` на `sat` не отказва връх → ✗ |
| G19 | `gh repo view Petar1984/varna_3d --json visibility,url` → `PRIVATE` | празен изход / `PUBLIC` = STOP преди Г2; D3 пада и §6.3 се преотваря |
| G20 | `python -m unittest discover -s tests 2>&1` при отваряне и при затваряне на интервала D19 | набор падащи тестове ⊄ назования в плана §2 → STOP; след `--freeze` наборът не е празен → STOP |
| G21 | `python src/qa_faza0_signed.py` (нов): `_meta.faza0_signed` може да е `true` само ако `docs/decisions/ФАЗА_0_лицензи.md:4` вече не носи „чака подпис“ | `faza0_signed: true` при днешния ред 4 → ✗ |
| G22 | вътре в `qa_quarters_signed.py`: Feature със `source: "agkk_inspire_gn"` се приема само ако `_meta.agkk_terms = {url, checked_on, terms}` е попълнено и `witnesses[]` носи `localid` на АГКК | официален полигон без `_meta.agkk_terms` → ✗; `localid`, който го няма в суровия отговор → ✗ |
| G23 | `python src/qa_district_official.py` (нов, varna_3d): всяко доставено място в АГКК AU5 полигона на своя `district.code` (днес 375/375, М0.19) | нарочно разменен код на район на един ред → изход ≠ 0 |
| G24 | отчетът на Ф0-б съществува ПРЕДИ Г2 и носи възпроизводими числа (SHA на PDF-а, брой редове за Варна, покритие на 174-те, съгласие с 201-те, черновата на crosswalk-а) | липсващ отчет или PDF с друг SHA → Г2 не тръгва |

## Оборване

Кими (К8+) и Astra (S7+) атакуват ТОЗИ документ и плана преди изпълнение (§0.3); същото важи и за собствения план на Varna_buildings (D14). Присъдите влизат като **амандамент — нов датиран файл** (`docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md`), а този раздел получава редакция в комита Г0-б, който сменя статуса на `Accepted`. Решенията за Петър са номерирани в §6 на плана и се отговарят на Gate 1.

web search: site.imot.bg общи условия авторски права информация ...
codex
Сравнението е спрямо подписани плюс предложени клетки, затова 3 217 покрити „дупки“ още не е резултат спрямо само подписания слой. Скриптът използва и `contains`, което изключва точките точно върху граница. Проверявам тези две уговорки, преди да оценя остатъка от 1 111.

web search: 
web search: https://www.imot.bg/obshti-uslovia
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
paths=['docs/activeContext.md','docs/decisions/004_measurement_doctrine.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_Адресите_по_полигон_08.09.md','scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_areas_08.09.json','scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson','scratch/boundary_gallery/granitsi_preview_05.09/mirela_varna_areas_08.09.geojson','scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.json','scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.py','scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json']
for s in sorted(paths):
 p=Path(s)
 print(s if p.is_file() else 'MISSING '+s)
'@ | python -X utf8 -B -" in C:\git\Fire_Varna
 succeeded in 665ms:
docs/activeContext.md
docs/decisions/004_measurement_doctrine.md
docs/decisions/010_signed_quarter_boundaries.md
MISSING docs/plans/????_????????_??_???????_08.09.md
scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_areas_08.09.json
scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson
scratch/boundary_gallery/granitsi_preview_05.09/mirela_varna_areas_08.09.geojson
scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.json
scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.py
scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@('docs/activeContext.md','docs/decisions/004_measurement_doctrine.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_Адресите_по_полигон_08.09.md','scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_areas_08.09.json','scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson','scratch/boundary_gallery/granitsi_preview_05.09/mirela_varna_areas_08.09.geojson','scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.json','scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.py','scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json') | Sort-Object | ForEach-Object { if (Test-Path -LiteralPath "'$_ -PathType Leaf) { $_ } else { '"'MISSING ' + "'$_ } }' in C:\git\Fire_Varna
 succeeded in 701ms:
docs/activeContext.md
docs/decisions/004_measurement_doctrine.md
docs/decisions/010_signed_quarter_boundaries.md
docs/plans/ПЛАН_Адресите_по_полигон_08.09.md
scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_areas_08.09.json
scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson
scratch/boundary_gallery/granitsi_preview_05.09/mirela_varna_areas_08.09.geojson
scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.json
scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.py
scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json

codex
Има поправка в броенето: таблицата съдържа **8 вътрешни подрайона**, така сборът е 95. Базата за „дупките“ е 82 клетки: 59 подписани, 20 предложени и 3 от ориентири. Планът v3 е „ЧЕРНОВА“, а ADR 010 е „Proposed“ — оценявам ги като предложения.

Обхватът е проверка само за четене. Основният инвентар е:

```text
docs/activeContext.md
docs/decisions/004_measurement_doctrine.md
docs/decisions/010_signed_quarter_boundaries.md
docs/plans/ПЛАН_Адресите_по_полигон_08.09.md
scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_areas_08.09.json
scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson
scratch/boundary_gallery/granitsi_preview_05.09/mirela_varna_areas_08.09.geojson
scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.json
scratch/boundary_gallery/granitsi_preview_05.09/raioni_compare_08.09.py
scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json
```

В метаданните на двата външни GeoJSON файла няма записан лиценз или хеш на суровия отговор; наличният списък не доказва кои са трите липсващи района.

web search: 
web search: https://www.imot.bg/obshti-uslovia
codex
Препоръчвам **отделен слой за всекидневните райони**, със собствено одобрение и версия. Замяната на подписан квартал трябва да остане отделна, обоснована корекция. Нищо не съм променял.

Проверката потвърди **95 валидни imot полигона, 0 площни застъпвания, 0 невалидни общи ръбове**. Площта е **93,028 km²** в метрична проекция; 93,1 идва от приблизителната формула. При Mirela **2 от 73** полигона са невалидни — Владиславово и Фичоза; сравнението ги поправя мълчаливо чрез `buffer(0)`.

Има съществена уговорка за покритието: **4 328 → 1 111**, намаление **74,3%**, е спрямо **82 клетки: 59 подписани + 20 предложени + 3 от ориентири**. Само спрямо оригиналните 60 подписани непокритите са **12 196**. Измерени са **адресни точки**, не доказано отделни сгради. Категориите в [таблицата](/C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json) са **41+20+20+6+8=95**; осмият „нов вътрешен“ е „Гръцка махала“ срещу „Гръцката махала“ — вероятен проблем при уеднаквяването на имената.

1. **Модел и адрес.** Поддържайте отделно `quarter`, `area` и административния `district`. Последният вече означава „район Приморски“ и не бива да получава брокерската семантика.

   За пожарникаря водят улицата/номерът или провереният ориентир; подписаният квартал остава основният териториален контекст. Одобреният всекидневен район добавя полезна точност: „Левски 1 (кв. Левски)“. „Операта (Център)“ е допустимо за конкретен обект с проверена принадлежност. При еднакви имена няма повторение; при спор уточнението отпада.

   Търсенето индексира двете принадлежности отделно: „Левски 1“ намира района, „кв. Левски“ — квартала. „к.к. Чайка“ и „кв. Чайка“ остават различни идентичности.

   Междуслойното пресичане е нормално. Ако са нужни клетки, те са **`Qᵢ ∩ Aⱼ` плюс остатъците с празна принадлежност**. Това е производен индекс; изходните геометрии се пазят. Пресичането не доказва родителство. Точка върху ръб получава гранична присъда, без произволен победител.

2. **Правило за приоритет.** Подписът определя действащата версия, но не доказва географска безпогрешност. Външен полигон заменя квартален само след: **същата териториална идентичност → доказана грешка → измерен ефект върху адресите → нов подпис на Петър**. При различна семантика се запазват две принадлежности.

   **IoU ≥0,7 между сайтовете е основание за преглед**, не автоматична победа: отделни сайтове не доказват независим произход. В таблицата този праг покриват **26/95**, а **37** нямат съпоставка с Mirela. По-дребното чертане също не е доказателство за точност. Признато грешният Център изисква корекция; дотогава спорният квартален етикет не трябва да внушава сигурност.

3. **Произход, топология и публикация.** Замразеният пакет трябва да съдържа точен URL/параметри, източников ID, време, суров отговор, SHA-256, условия за употреба, преобразувания и версия на инструментите. Днешните метаданни са непълни; наличните файлове не доказват **98**, нито кои три липсват.

   Гейтове: всички очаквани ID отчетени независимо от обявите; валидност **преди поправка**; 0 площни застъпвания; съвпадащи ръбове; отделен отчет за празнините; метрични площи; възпроизводимо присвояване на точките. Валидната топология допуска дупки — потвърдено и в [документацията на Shapely](https://shapely.readthedocs.io/en/2.1.2/reference/shapely.coverage_is_valid.html). Промяна на сайта създава нов кандидат, пространствен диф и списък променени принадлежности; приложението използва последния одобрен снапшот.

   Публично бих доставял само необходимите одобрени имена/кодове и принадлежности, без геометрията и частния доказателствен пакет. Но **„само имена“ не решава автоматично правата върху извлечените принадлежности**. В [условията на imot.bg](https://www.imot.bg/obshti-uslovia) не открих изрично разрешение за такова повторно използване; това остава условие преди доставка.

4. **Остатъчните 1 111.** Нужна е независимо обоснована маска на обхвата, после класификация: пристанище, промишлена територия, населено място, грешна/остаряла точка, непроучено. Съпоставянето със сграден отпечатък доказва сграда; териториален източник доказва категорията. Портът и промзоните остават в аварийния обхват. Маската не бива да прикрива непокритите точки. Гейтът е **всяка точка отчетена**, а не всяка насилствено получила квартал.

5. **v3 и ADR 010.** И двата документа още са чернови. В [ADR 010](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md) D6 запазва приоритета на писмените свидетели и подписаните изключения за `quarter`; новият канал записва отделно `area`. D8 ограничава конфликтите вътре във всеки слой; между слоевете няма автоматична йерархия.

   [Планът v3](/C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md) изисква версия на схемата, два отделни резултата от пространственото определяне, отделни правила за търсене, подписани примери за показване и гейтове за ръбове, едноименни места, променени адреси и размер. Същата семантика трябва изрично да обхване и адресите, и местата.
tokens used
69,741
Препоръчвам **отделен слой за всекидневните райони**, със собствено одобрение и версия. Замяната на подписан квартал трябва да остане отделна, обоснована корекция. Нищо не съм променял.

Проверката потвърди **95 валидни imot полигона, 0 площни застъпвания, 0 невалидни общи ръбове**. Площта е **93,028 km²** в метрична проекция; 93,1 идва от приблизителната формула. При Mirela **2 от 73** полигона са невалидни — Владиславово и Фичоза; сравнението ги поправя мълчаливо чрез `buffer(0)`.

Има съществена уговорка за покритието: **4 328 → 1 111**, намаление **74,3%**, е спрямо **82 клетки: 59 подписани + 20 предложени + 3 от ориентири**. Само спрямо оригиналните 60 подписани непокритите са **12 196**. Измерени са **адресни точки**, не доказано отделни сгради. Категориите в [таблицата](/C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/raioni_table_08.09.json) са **41+20+20+6+8=95**; осмият „нов вътрешен“ е „Гръцка махала“ срещу „Гръцката махала“ — вероятен проблем при уеднаквяването на имената.

1. **Модел и адрес.** Поддържайте отделно `quarter`, `area` и административния `district`. Последният вече означава „район Приморски“ и не бива да получава брокерската семантика.

   За пожарникаря водят улицата/номерът или провереният ориентир; подписаният квартал остава основният териториален контекст. Одобреният всекидневен район добавя полезна точност: „Левски 1 (кв. Левски)“. „Операта (Център)“ е допустимо за конкретен обект с проверена принадлежност. При еднакви имена няма повторение; при спор уточнението отпада.

   Търсенето индексира двете принадлежности отделно: „Левски 1“ намира района, „кв. Левски“ — квартала. „к.к. Чайка“ и „кв. Чайка“ остават различни идентичности.

   Междуслойното пресичане е нормално. Ако са нужни клетки, те са **`Qᵢ ∩ Aⱼ` плюс остатъците с празна принадлежност**. Това е производен индекс; изходните геометрии се пазят. Пресичането не доказва родителство. Точка върху ръб получава гранична присъда, без произволен победител.

2. **Правило за приоритет.** Подписът определя действащата версия, но не доказва географска безпогрешност. Външен полигон заменя квартален само след: **същата териториална идентичност → доказана грешка → измерен ефект върху адресите → нов подпис на Петър**. При различна семантика се запазват две принадлежности.

   **IoU ≥0,7 между сайтовете е основание за преглед**, не автоматична победа: отделни сайтове не доказват независим произход. В таблицата този праг покриват **26/95**, а **37** нямат съпоставка с Mirela. По-дребното чертане също не е доказателство за точност. Признато грешният Център изисква корекция; дотогава спорният квартален етикет не трябва да внушава сигурност.

3. **Произход, топология и публикация.** Замразеният пакет трябва да съдържа точен URL/параметри, източников ID, време, суров отговор, SHA-256, условия за употреба, преобразувания и версия на инструментите. Днешните метаданни са непълни; наличните файлове не доказват **98**, нито кои три липсват.

   Гейтове: всички очаквани ID отчетени независимо от обявите; валидност **преди поправка**; 0 площни застъпвания; съвпадащи ръбове; отделен отчет за празнините; метрични площи; възпроизводимо присвояване на точките. Валидната топология допуска дупки — потвърдено и в [документацията на Shapely](https://shapely.readthedocs.io/en/2.1.2/reference/shapely.coverage_is_valid.html). Промяна на сайта създава нов кандидат, пространствен диф и списък променени принадлежности; приложението използва последния одобрен снапшот.

   Публично бих доставял само необходимите одобрени имена/кодове и принадлежности, без геометрията и частния доказателствен пакет. Но **„само имена“ не решава автоматично правата върху извлечените принадлежности**. В [условията на imot.bg](https://www.imot.bg/obshti-uslovia) не открих изрично разрешение за такова повторно използване; това остава условие преди доставка.

4. **Остатъчните 1 111.** Нужна е независимо обоснована маска на обхвата, после класификация: пристанище, промишлена територия, населено място, грешна/остаряла точка, непроучено. Съпоставянето със сграден отпечатък доказва сграда; териториален източник доказва категорията. Портът и промзоните остават в аварийния обхват. Маската не бива да прикрива непокритите точки. Гейтът е **всяка точка отчетена**, а не всяка насилствено получила квартал.

5. **v3 и ADR 010.** И двата документа още са чернови. В [ADR 010](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md) D6 запазва приоритета на писмените свидетели и подписаните изключения за `quarter`; новият канал записва отделно `area`. D8 ограничава конфликтите вътре във всеки слой; между слоевете няма автоматична йерархия.

   [Планът v3](/C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md) изисква версия на схемата, два отделни резултата от пространственото определяне, отделни правила за търсене, подписани примери за показване и гейтове за ръбове, едноименни места, променени адреси и размер. Същата семантика трябва изрично да обхване и адресите, и местата.
