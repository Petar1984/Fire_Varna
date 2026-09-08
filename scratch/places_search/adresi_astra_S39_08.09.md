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
session id: 01a07eff-86c9-75e2-a93f-df379ee35a1e
--------
user
S39 · Външно око (леща архитектура/ГИС): ЗАМЯНА НА ОСНОВАТА — imot.bg вместо Wikimapia за ЦЕЛИЯ град? Петър (08.09 ~16:00): „не говорих само за центъра, а за целия град. Иначе тези на центъра са супер — ползваме тях. Искам да прегледаме и за целия град — може би ще използваме тях вместо тези на Wikimapia“. Мярка (C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/raioni_swap_08.09.json, скрипт raioni_swap_08.09.py; СЪСТОЯНИЕ_Границите_06.09.md §18): 60-те подписани (ръчно потвърдени Wikimapia полигони; 61,7 km²; покриват 68 314 от 80 510 адресни точки = 84,9 %; 11 родства в _meta) срещу 95-те imot.bg полигона (плочка, 0 застъпвания, 93,1 km², 78 236 = 97,2 %; провенанс: обява, SHA-256, речник от 98 id). За всеки подписан: 38 имат imot двойник с IoU ≥ 0,6 (замяна без загуба); 13 се различават (борд): Св. Иван Рилски — imot НЯМА такъв район, неговата „Максуда“ покрива 67 % от нашия Рилски + Автогара 19 %; Евксиноград 0,44; Център 0,37 (Петър: нашият е сбъркан); Манастирски рид 0,47 (imot 4,09 km² срещу 2,10); Акчелар 0,54; Сотира 0,59; кв. Тракия — imot няма „Тракия“, само Зимно/Лятно кино Тракия + Централна поща; Възраждане = Възраждане 1–4 (родител без собствен imot); Победа = Победа 46 % + Конфуто 39 %; Младост = Младост 1+2; Морска градина — imot няма парк, само Салтанат 46 %; Фичоза 0,57; Салтанат 0,51; 7 „изчезват при замяна“ (3 983 сгради): Максуда (нашата 0,23 km²/1 242 сгради; imot-„Максуда“ е другаде), Средна Трака 958 и Горна Трака 616 (imot има една „Горна Трака“ 2,9 km², поглъщаща Евксиноград 30 %/Фатрико дере 26 %/Средна 19 %/Горна 15 %), Розова долина 741 и Дружба 56 (при imot вътре в Аспарухово), Абатко 272 (вътре в К&Е), Горчивата чешма 98 (в Салтанат); 2 родители = сбор от imot подрайони: Левски = Левски 1+2+Цветен квартал+Базар Левски (93 %), Владиславово = ВВ 1+2+Кайсиева+Боклук Тарла+Планова ПЗ (94 %); 46 imot полигона без наш двойник (нови). Остатък извън imot: 2 274 точки (срещу 12 196 извън подписаните). Контекст: ADR 010 (подписаните граници = Петър потвърждава Wikimapia полигони по борд; D6/D8), регистърът на кодовете във Varna_buildings, Б3 (стейджнат) с фикстури по 28 кода, 3D картата чете същите полигони; вчерашният ти S38 препоръча отделен слой area. Въпроси: (1) КОЯ ОСНОВА: (а) imot като единствена основа (замяна на Wikimapia; подписаните = imot след борд), (б) два слоя (quarter от Wikimapia/подпис + area от imot), (в) хибрид: imot като основа навсякъде, където IoU ≥ 0,6 или Петър го приема, а нашите остават като ДЕЦА/изключения там, където imot няма понятие (Св. Иван Рилски, Средна Трака, Розова долина, Дружба, Абатко, Горчивата чешма, Максуда) — с числа кое струва по-малко и е по-вярно за пожарникар; (2) как се пази D8 (детето ⊆ родител) и 11-те родства при плочка от imot, където родителите (Левски, Владиславово, Възраждане, Младост) нямат собствен полигон — родител = обединение на децата?; (3) какво означава „подписан“ при външна плочка: ред на борда (imot полигон → Петър потвърждава/отхвърля/поправя), версия, снапшот, замразяване; (4) какво чупи в кода/данните: QUARTER_CODES (28), фикстурите на Б3, quarter_registry.json (кодове), search_bridge; миграция по D13; (5) остатъкът 2 274 точки: маска и класификация. Не пипай нищо. До 900 думи: препоръка (а/б/в) + условия, с числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще сверя мярката, ADR 010 и зависимостите в наличните файлове, после ще дам препоръка с цена на миграцията и условия за подписване. Прегледът е само за четене.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status -sb' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -TotalCount 130' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-ChildItem -LiteralPath scratch/boundary_gallery/granitsi_preview_05.09 -File | Sort-Object Name | Select-Object -ExpandProperty Name' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg --files -g '*010*' -g '*S38*' -g '*СЪСТОЯНИЕ*' -g '*quarter*' -g '*bridge*' -g 'AGENTS.md' -g '*B3*' -g '*Б3*' docs scripts tests scratch" in C:\git\Fire_Varna
 succeeded in 518ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 129]
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
?? scratch/places_search/adresi_astra_S39_08.09.md
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

 succeeded in 486ms:
scratch\varna_quarters_osm_copy.geojson
scratch\quarters_saga_view.html
scratch\quarters_saga_points.js
scratch\quarters_review_20260812.html
scratch\quarters_points.js
scratch\quarters_partition_view.html
scratch\quarters_partition.js
scratch\quarters_list_20260812.md
scratch\quarters_cleanup_spec_20260812.md
docs\sessions\СЪСТОЯНИЕ_Границите_06.09.md
docs\sessions\СУТРИН_08.09_Б3.md
docs\decisions\010_signed_quarter_boundaries.md
docs\plans\ПЛАН_Б3_07.09_амандамент_2.md
docs\plans\ПЛАН_Б3_07.09_амандамент_1.md
docs\plans\ПЛАН_Б3_07.09.md
scratch\places_search\osm_quarters_brief_astra.md
scratch\places_search\COMMIT_MSG_B3.txt
scratch\places_search\adresi_bridge_depth_08.09.json
scratch\places_search\adresi_astra_S38_08.09.md
scratch\places_search\osm_quarters_measure_05.09.md
scratch\places_search\osm_quarters_brief_kimi.md
scratch\kais_func_2026-09-03\парцели\quarters.py

 succeeded in 639ms:
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

 succeeded in 709ms:
address_rows_08.09.json
adresi_proposal_08.09.html
adresi_proposal_08.09.json
agkk_au5_varna.geojson
agkk_gn_surfaces_varna.geojson
akchelar_kais_footprint.geojson
areas_preview_08.09.html
board.html
boundary_streets.geojson
decisions_5_draft_08.09.json
derived_quarters_cap150.geojson
derived_quarters_cap250.geojson
evksinograd_kais_footprint.geojson
gaps_buildings_08.09.json
gaps_candidates_08.09.geojson
gaps_candidates_wm_details_08.09.json
gaps_mask_08.09.geojson
gaps_preview_08.09.html
gaps_proposal_08.09.geojson
gaps_proposal_08.09.html
gaps_proposal_08.09.json
granitsi_decisions_3_2026-09-06_proba.json
hotels_08.09.json
hybrid_quarters.geojson
imot_api_points_08.09.json
imot_area_points_08.09.json
imot_areas_08.09.geojson
imot_areas_report_08.09.json
imot_bg_varna_areas_08.09.json
imot_bg_varna_dictionary_08.09.json
imot_bg_varna_polygons_08.09.geojson
index.html
kaisieva_pup_buildings.geojson
kaisieva_pup_official.geojson
labelled_buildings.json
landmarks_overpass_08.09.json
landmarks_wm_search_08.09.json
landmarks_wm_search2_08.09.json
m2_1_candidates_v2.json
mirela_preview_08.09.html
mirela_varna_areas_08.09.geojson
mladost2_streets_proposal.geojson
mock_kartonche.html
odesos_cadreg_from_map.geojson
odesos_mr_official.geojson
old_quarters_july.geojson
osm_place_areas.geojson
osm_quarters.geojson
osm_seeds.geojson
partition_build_08.09.py
partition_draft_08.09.geojson
partition_preview_08.09.html
partition_report_08.09.json
partition_v2_08.09.geojson
partition_v2_centre_fragments_08.09.geojson
partition_v2_report_08.09.json
places_08.09.json
places_375_cap150.geojson
places_375_cap250.geojson
places_375_hybrid.geojson
places_375_old.geojson
places_375_osm.geojson
places_375_streets.geojson
places_result_proba.geojson
quarters_overlay_08.09.html
quarters_result_proba.geojson
quarters_signed_08.09.geojson
raioni_compare_08.09.json
raioni_compare_08.09.py
raioni_imot_overlaps_08.09.json
raioni_preview_08.09.html
raioni_swap_08.09.json
raioni_swap_08.09.py
raioni_table_08.09.json
raioni_table_08.09.py
reclass_08.09.json
reclass_map_08.09.html
result.html
streets_quarters.geojson
tsentar_extended_08.09.geojson
tsveten_candidate_08.09.geojson
tsveten_preview_08.09.html
tsveten_preview_08.09.json
unions_2026-09-07.geojson
wikimapia.html
wikimapia_extra_2026-09-06.geojson
wikimapia_quarters.geojson
wikimapia_quarters_frozen_2026-09-06.geojson
wikimapia_quarters_frozen_2026-09-06_v2.geojson
zone_to_quarter_draft_08.09.json

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath scratch/boundary_gallery/granitsi_preview_05.09/raioni_swap_08.09.json -Encoding UTF8 -TotalCount 105' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -Encoding UTF8 -TotalCount 32' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath scratch/boundary_gallery/granitsi_preview_05.09/raioni_swap_08.09.py -Encoding UTF8 -TotalCount 150' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Item -LiteralPath docs/decisions/010_signed_quarter_boundaries.md,docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md,scratch/boundary_gallery/granitsi_preview_05.09/quarters_signed_08.09.geojson,scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson,scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_dictionary_08.09.json,scratch/boundary_gallery/granitsi_preview_05.09/address_rows_08.09.json | Sort-Object FullName | Select-Object FullName,Length' in C:\git\Fire_Varna
 succeeded in 672ms:
{
 "summary": {
  "n_signed": 60,
  "n_imot": 95,
  "buildings_total": 80510,
  "covered_by_signed": 68314,
  "covered_by_imot": 78236,
  "signed_area_km2": 61.67,
  "imot_area_km2": 93.14,
  "verdicts": {
   "imot слабо": 7,
   "imot ≠ наш": 13,
   "imot ≈ наш": 38,
   "нашият = сбор от 4 imot подрайона": 1,
   "нашият = сбор от 5 imot подрайона": 1
  },
  "lost_if_swap": [
   [
    "м-т Абатко",
    272
   ],
   [
    "ж.к. Дружба",
    56
   ],
   [
    "м-т Горчивата чешма",
    98
   ],
   [
    "с.о. Горна Трака",
    616
   ],
   [
    "Максуда",
    1242
   ],
   [
    "кв. Розова долина",
    741
   ],
   [
    "Средна Трака",
    958
   ]
  ],
  "buildings_in_lost": 3983,
  "imot_new_not_matched": [
   "Автогара",
   "Базар Левски",
   "Бизнес парк Варна",
   "Бизнес хотел",
   "Владислав Варненчик 1",
   "Владислав Варненчик 2",
   "Гранд Мол",
   "ЖП Гара",
   "Завод Дружба",
   "Конфуто",
   "Левски 1",
   "Левски 2",
   "Лятно кино Тракия",
   "Метро",
   "Окръжна болница-Генерали",
   "Операта",
   "Островна промишлена зона",
   "Погреби",
   "Пристанище Варна",
   "Промишлена зона Тополи",
   "Спортна зала",
   "Стадион Спартак",
   "Фестивален комплекс",
   "ХЕИ",
   "Цветен квартал",
   "Централна поща",
   "Чаталджа",
   "в.з.Виница - север",
   "в.з.Звездица",
   "м-т Атанас Тарла",
   "м-т Кантара",
   "м-т Крушките",
   "м-т Орехчето",
   "м-т Планова",
   "м-т Припек",
   "м-т Сълзица",
   "с. Звездица",
   "с. Казашко",
   "с. Каменар",
   "с. Константиново",
   "с. Тополи",
   "ВИНС-Червен площад",
   "Летище",
   "к.к. Слънчев ден",
   "м-т Боклук Тарла",
   "м-т Лазур"
  ],
  "residual_gap_points": 2274,
  "residual_gap_cells_ge10": 48,
  "residual_gap_top": [
   35,
   33,
   29,
   23,
   22,
   21,
   21,

 succeeded in 674ms:
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


 succeeded in 678ms:
# -*- coding: utf-8 -*-
"""Whole-city scenario: imot.bg's 95 polygons as the BASE layer instead of the Wikimapia-based signed 60.
For each signed polygon: best imot counterpart (name alias, else max IoU), IoU, areas, buildings, mirela agreement,
children/parents in both, verdict. Then the scenario numbers: coverage per district, signed polygons with no
counterpart (and the buildings they hold), imot polygons that are new, residual gaps by cluster.
Aggregates only leave this folder."""
import json, io, sys, math, re, collections
from shapely.geometry import shape, Point
from shapely.ops import unary_union
from shapely.strtree import STRtree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KM2 = 111.32 * 111.32 * math.cos(math.radians(43.21))
def nz(s):
    s = (s or "").lower(); s = re.sub(r"[„“\"”().,\-–]", " ", s); s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^(кв|ж к|жк|зк|р н|м т|к к|в з|с о|с|местност|район|квартал|селищно образувание)\s+", "", s); return s.strip()
# signed name -> imot slug (К37 aliases + obvious ones); anything else by max IoU
ALIAS = {"pogrebite": "pogrebi", "generalite": "okrazhna-bolnitsa-generali", "vladislavovo": None, "kaisieva": "kaysieva-gradina", "pz_planova": "planova-promishlena-zona",
         "kv_levski": None, "chaika_kk": "k-k-chayka", "chaika_kv": "chayka", "dobreva": "m-t-dobreva-cheshma", "balam_dere": "m-t-balam-dere", "mentesheto": "m-t-menteshe",
         "tsentar": "tsentar", "operata": "operata", "stadion_spartak": "stadion-spartak", "sportna_zala": "sportna-zala", "zavod_druzhba": "zavod-druzhba"}
signed = json.load(open("quarters_signed_08.09.geojson", encoding="utf-8"))
imot = json.load(open("imot_bg_varna_polygons_08.09.geojson", encoding="utf-8"))
mir = json.load(open("mirela_varna_areas_08.09.geojson", encoding="utf-8"))
part = json.load(open("partition_v2_08.09.geojson", encoding="utf-8"))
rows = json.load(open("address_rows_08.09.json", encoding="utf-8")); fo = rows["field_order"]
pts = [Point(r[fo.index("lng")], r[fo.index("lat")]) for r in rows["rows"]]
ptree = STRtree(pts)
def n_in(g): return sum(1 for i in ptree.query(g) if g.contains(pts[i]))
S = [(f["properties"], shape(f["geometry"]).buffer(0)) for f in signed["features"]]
I = [(f["properties"], shape(f["geometry"]).buffer(0)) for f in imot["features"]]
Ibyslug = {p["slug"]: (p, g) for p, g in I}
M = {nz(f["properties"]["h1"]): shape(f["geometry"]).buffer(0) for f in mir["features"]}
itree = STRtree([g for _, g in I])
edges = {e["child"]: e["parent"] for e in signed.get("_meta", {}).get("parent_child", [])}
for p, _ in S:
    if p.get("parent"): edges.setdefault(p["code"], p["parent"])
def iou(a, b): return a.intersection(b).area / a.union(b).area if not a.union(b).is_empty else 0
out = []; used = set()
for p, g in S:
    code = p["code"]; best = None
    slug = ALIAS.get(code, "?")
    if slug and slug in Ibyslug:
        ip, ig = Ibyslug[slug]; best = (ip, ig, iou(g, ig), "по име")
    elif slug is None:
        best = None  # handled below (sub-areas)
    else:
        k = nz(p["name"])
        cands = [(ip, ig) for ip, ig in I if nz(ip["name"]) == k]
        if not cands:
            cands = [I[i] for i in itree.query(g)]
            cands = [(ip, ig) for ip, ig in cands if g.intersects(ig)]
            if cands:
                ip, ig = max(cands, key=lambda c: iou(g, c[1])); best = (ip, ig, iou(g, ig), "по геометрия")
        else:
            ip, ig = cands[0]; best = (ip, ig, iou(g, ig), "по име")
    # sub-area splits: signed parent covered by several imot polygons (Левски = Левски 1+2+Базар+Дружба+Цветен; Владиславово = ВВ 1+2+Кайсиева+…)
    parts = []
    for i in itree.query(g):
        ip, ig = I[i]; x = g.intersection(ig).area
        if x / ig.area >= 0.5 and x / g.area >= 0.03: parts.append((round(100 * x / g.area, 1), round(100 * x / ig.area, 1), ip["name"]))
    parts.sort(reverse=True)
    covered_by_parts = round(sum(a for a, _, _ in parts), 1)
    mir_iou = None
    if best:
        m = M.get(nz(best[0]["name"]))
        if m is not None: mir_iou = round(iou(best[1], m), 2)
    nb_ours = n_in(g); nb_imot = n_in(best[1]) if best else None
    if best and best[2] >= 0.6: verdict = "imot ≈ наш (IoU %.2f) — замяна без загуба" % best[2]
    elif best and best[2] >= 0.3: verdict = "imot ≠ наш (IoU %.2f) — борд" % best[2]
    elif covered_by_parts >= 70: verdict = "нашият = сбор от %d imot подрайона (%s %%)" % (len(parts), covered_by_parts)
    elif best: verdict = "imot слабо (IoU %.2f) — при замяна нашият изчезва/променя се силно" % best[2]
    else: verdict = "НЯМА imot съответствие — при замяна изчезва"
    if best: used.add(best[0]["slug"])
    out.append(dict(code=code, name=p["name"], kind=p.get("kind"), district=p.get("district"), parent=edges.get(code), area_km2=round(g.area * KM2, 3), buildings=nb_ours,
                    imot=best[0]["name"] if best else None, imot_slug=best[0]["slug"] if best else None, match_by=best[3] if best else None, iou=round(best[2], 2) if best else None,
                    imot_area_km2=round(best[1].area * KM2, 3) if best else None, imot_buildings=nb_imot, imot_mirela_iou=mir_iou,
                    imot_parts=[dict(pct_of_ours=a, pct_of_imot=b, name=n) for a, b, n in parts[:8]], covered_by_parts_pct=covered_by_parts, verdict=verdict))
# scenario numbers
allI = unary_union([g for _, g in I]); allS = unary_union([g for _, g in S])
cov_I = sum(1 for p in pts if allI.contains(p)); cov_S = sum(1 for p in pts if allS.contains(p))
by_d = collections.defaultdict(lambda: [0, 0, 0])
dist = json.load(open("C:/git/Varna_buildings/data/osm/varna_districts_2026-06-13.geojson", encoding="utf-8")) if False else None
new_imot = [p["name"] for p, _ in I if p["slug"] not in used]
lost = [r for r in out if r["verdict"].startswith("НЯМА") or r["verdict"].startswith("imot слабо")]
gap_I = [p for p in pts if not allI.contains(p)]
G = 0.0009; GX = G / math.cos(math.radians(43.21))
grid = collections.Counter((int(p.y / G), int(p.x / GX)) for p in gap_I)
blobs = sorted(grid.values(), reverse=True)
summary = dict(n_signed=len(S), n_imot=len(I), buildings_total=len(pts), covered_by_signed=cov_S, covered_by_imot=cov_I,
               signed_area_km2=round(allS.area * KM2, 2), imot_area_km2=round(allI.area * KM2, 2),
               verdicts=collections.Counter(r["verdict"].split(" (")[0].split(" —")[0] for r in out),
               lost_if_swap=[(r["name"], r["buildings"]) for r in lost], buildings_in_lost=sum(r["buildings"] for r in lost),
               imot_new_not_matched=new_imot, residual_gap_points=len(gap_I), residual_gap_cells_ge10=sum(1 for v in blobs if v >= 10), residual_gap_top=blobs[:10])
json.dump(dict(summary=summary, rows=out), open("raioni_swap_08.09.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in summary.items() if k not in ("imot_new_not_matched",)}, ensure_ascii=False))
print("imot new (not matched to any signed):", len(new_imot))
for r in sorted(out, key=lambda r: (r["verdict"][:4], -(r["buildings"]))):
    print("%-34s %6.3f km² %5d сгр | imot: %-28s IoU %-5s (%s) mir %-5s | %s" % (r["name"], r["area_km2"], r["buildings"], r["imot"] or "—", r["iou"], r["match_by"] or "", r["imot_mirela_iou"], r["verdict"] if not r["imot_parts"] or r["iou"] and r["iou"] >= 0.6 else r["verdict"] + " · части: " + ", ".join("%s %.0f%%" % (x["name"], x["pct_of_ours"]) for x in r["imot_parts"][:5])))

 succeeded in 754ms:

FullName                                                                                                Length
--------                                                                                                ------
C:\git\Fire_Varna\docs\decisions\010_signed_quarter_boundaries.md                                        53242
C:\git\Fire_Varna\docs\sessions\СЪСТОЯНИЕ_Границите_06.09.md                                             89955
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\address_rows_08.09.json              5073137
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\imot_bg_varna_dictionary_08.09.json     6274
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\imot_bg_varna_polygons_08.09.geojson  175736
C:\git\Fire_Varna\scratch\boundary_gallery\granitsi_preview_05.09\quarters_signed_08.09.geojson         301917



codex
Скриптът нарича IoU ≥ 0,6 „замяна без загуба“, но мери площ, а не запазени адреси и имена. Ще проверя отделно какво се печели и губи при замяната; това е важно за 38-те уж лесни случая и за остатъка от 2 274 точки.

web search: 
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json
from pathlib import Path
p=Path('scratch/boundary_gallery/granitsi_preview_05.09')
for name in ['quarters_signed_08.09.geojson','imot_bg_varna_polygons_08.09.geojson','imot_bg_varna_dictionary_08.09.json','address_rows_08.09.json']:
 d=json.loads((p/name).read_text(encoding='utf-8'))
 print(name, 'top_keys=',list(d) if isinstance(d,dict) else 'list')
 if isinstance(d,dict):
  for k in ['_meta','meta','field_order']:
   if k in d: print(k,json.dumps(d[k],ensure_ascii=False)[:9500])
  if 'features' in d: print('first_properties',json.dumps(d['features'][0]['properties'],ensure_ascii=False))
'@ | python -B -X utf8 -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'D6|D8|D13|§18|## 18|S38|98|лиценз' docs/decisions/010_signed_quarter_boundaries.md docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md" in C:\git\Fire_Varna
 succeeded in 616ms:
docs/decisions/010_signed_quarter_boundaries.md
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md

 succeeded in 894ms:
quarters_signed_08.09.geojson top_keys= ['_meta', 'features', 'type']
_meta {"artifact_class": "signed_by_plan_signature", "attribution": "Кварталните граници в този файл са по Wikimapia.org (© Wikimapia contributors, CC BY-SA, ToS §1.G: връзка към обекта + „Wikimapia.org“ с връзка към http://wikimapia.org); карето „Младост 2“ е по улични оси от OpenStreetMap (© OpenStreetMap contributors, ODbL, https://www.openstreetmap.org/copyright). Геометрия НИКОГА не пътува публично.", "canonicalization": {"bytes": "UTF-8 без BOM, sorted keys, compact, финален LF (G30); две сглобявания са байт-еднакви", "raw_geometry_sha256": "sha256 на компактния {\"type\",\"coordinates\"} — правилото, което вече е в решенията (пренесено по Б0 т. 2)", "wm_polygon_sha256": "канонизацията на D1 по Б0 т. 2: 6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; вътрешните по часовника; MultiPolygon по амандамент №2 §4"}, "counts": {"choice_alias_of": 1, "choice_declared_streets": 1, "choice_deferred": 6, "choice_excluded": 1, "choice_wikimapia": 58, "choice_wikimapia_union": 1, "decisions_rows": 68, "features": 60, "features_with_our_district": 58, "features_with_resolved_district": 2, "registry_entries": 84, "registry_pending": 16}, "d1_schema": {"fields": ["code", "name", "kind", "parent", "source", "signed_by", "drawn_by", "approved_by", "drawn_at", "approved_at", "method", "basemap", "precision_m", "version", "license", "viewport", "visible_layers", "screenshot_sha256", "approval_digest", "witnesses", "note"], "nulled_on_import": ["drawn_by", "drawn_at", "basemap", "viewport", "visible_layers", "screenshot_sha256", "approval_digest"], "why": "Б0 т. 1 (подписан): за Feature със source ∈ {wikimapia, declared_streets} седемте полета на ръката са null по договор — взаимна изключителност „или ръка, или внос“. Дайджестът на D1 се замества от sha-веригата на Б0 т. 8: решения по sha → Feature с wm_polygon_sha256 → _meta.decisions_sha256."}, "decisions_author": "Claude Architect (тялото на решенията, 895e0d2) → Claude Executor (полето attribution по Б0.8, 3d747d3)", "decisions_based_on": {"file": "granitsi_decisions_3_2026-09-06_proba.json", "rev": "b6e627d0fb19e039a062aba955d030301ae45b2e", "sha256": "ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6"}, "decisions_blob_before_attribution": {"rev": "895e0d2651aac73516659f2a10ea5193b2be5d53", "sha256": "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89", "why": "тялото без полето attribution (Б0.8 го изисква); прегледано от Astra S23. Подписът на Петър е върху окончателния блоб, не върху този."}, "decisions_commit": "3d747d3308bf31fe17add9a510ad97423adc672a", "decisions_path": "scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json", "decisions_sha256": "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b", "decisions_sha256_rule": "sha256 на БЛОБА (git show <rev>:<път>), не на работното копие — Б0 т. 8", "decisions_sha256_worktree": {"bytes": 32983, "note": "работното копие е CRLF; подписан е БЛОБЪТ (Б0 т. 8), не този файл", "path": "C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json", "sha256": "fdb748bcb76cf6458be3ad0e8decf495ca954fdd4f62f4aea7ea1aee3d608f4f"}, "declared_deviations": [{"what": "choice: „wikimapia_union“ за кода dobreva (решения 4, Петър 07.09)", "why": "Площта, която Уикимапия нарича „Виница - север“ (5729421), е част от Добрева чешма — границата е обединението на двата човешки полигона. Обединението се смята в UTM 35N (EPSG:32635) и се връща в WGS84: така се възпроизвежда БАЙТ ПО БАЙТ пинът в решенията (d6f367bd…), който Петър видя. Обединение направо в градуси дава ДРУГА геометрия — различават се и двата хеша (bc92a76c… / fc1f7297…), а най-голямата разлика по връх е 4,177e-07° (≈ 4,6 cm), НЕ 1e-14°, както твърдеше по-ранният текст тук (поправено по Astra S23 F2). A9 отказва всеки друг резултат; рецептата и точните версии на shapely/GEOS/pyproj/PROJ са в _meta.union_recipe."}, {"what": "полето url на обединения Feature", "why": "Обединението има два изворни обекта. `url` носи ПЪРВИЯ от реда (този, чието име носи кодът), а всички обекти с техните url-и и собствени сурови хешове са в `witnesses` — ToS §1.G се изпълнява от реда за атрибуция плюс свидетелите."}, {"what": "choice: „excluded“ за кода vinitsa_sever", "why": "Петър (07.09): кодът отпада като квартал — няма Feature, редът е поименно в `_meta.excluded`. Деактивирането в quarter_registry.json е негов сутрешен ход: регистърът НЕ се пипа тук (червена черта 3 на плана), затова кодът остава в registry_entries и НЕ е в registry_pending (той ИМА решение)."}, {"what": "полето district в Feature-ите", "why": "Б0 т. 4 иска районът да е изведен по представителна точка срещу НАШИТЕ пет района, не от АГКК INSPIRE (G22 остава заключен). Затова слоят с петте административни граници влиза като назован вход, а АГКК остава само свидетел в _meta.district_witness_agkk."}, {"what": "районът на кодовете в _meta.district_resolutions.applied (district_src = agkk_au5_confirmed_by_petar)", "why": "Решение 9 (Петър, 07.09: „Кочмар и Възраждане 4 не са във Владиславово“). Само за поименно решените кодове районът НЕ идва от нашия слой, а от официалната граница на АГКК AU5, потвърдена от Петър; входът е подписан файл без геометрия, закотвен по sha256 в _meta.inputs. Спорът остава записан в _meta.district_witness_disputes с resolution petar_agkk — решението не трие разминаването, а го затваря. Всяко НЕрешено разминаване остава pending_petar."}, {"what": "входният етикет source: declared_local_knowledge на карето „Младост 2“", "why": "Отменен от амандамент №2 §3.7; НЕ пътува в изхода. Изходният Feature носи source: declared_streets и лиценз ODbL по подписания ключ на Б0 т. 3."}, {"what": "затвореният набор properties е 21 полета на D1 + 19 назовани провенанс-полета", "why": "Г2-в на амандамент №2 §4 изисква geometry_origin/imported_from/fetched_at/chosen_source/chosen_reason/confirmed_by/confirmed_at; Б0 т. 2 изисква двата хеша поотделно; G27(а) изисква реда за атрибуция. Наборът е затворен — непознат ключ спира сглобяването."}], "district_resolutions": {"applied": [{"agkk": "10135-03", "basis": "agkk_au5 10135-03", "code": "kochmar", "district": "mladost", "was": "vladislav_varnenchik"}, {"agkk": "10135-03", "basis": "agkk_au5 10135-03", "code": "vazrazhdane4", "district": "mladost", "was": "vladislav_varnenchik"}], "district_src": "agkk_au5_confirmed_by_petar", "path": "C:/git/Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json", "rule": "подписаният файл може да реши САМО спор, който съществува, и САМО в посоката на свидетеля АГКК AU5; всичко друго спира сглобяването (A22) и пада на гейта (C18/C20). Нерешените разминавания остават pending_petar.", "sha256": "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc", "signed_at": "2026-09-07T00:10:58+03:00", "signed_by": "Petar via Claude Architect (words 07.09: Кочмар и Възраждане 4 не са във Владиславово)"}, "district_witness_agkk": {"by_code": {"abatko": "10135-02", "akchelar": "10135-02", "alen_mak": "10135-02", "asparuhovo": "10135-05", "balam_dere": "10135-04", "borovets_sever": "10135-05", "borovets_yug": "10135-05", "briz": "10135-02", "chaika_kk": "10135-02", "chaika_kv": "10135-02", "dobreva": "10135-02", "dolna_traka": "10135-02", "druzhba": "10135-05", "evksinograd": "10135-02", "fichoza": "10135-05", "galata": "10135-05", "gorchivata_cheshma": "10135-02", "gorna_traka": "10135-02", "grackata_mahala": "10135-01", "hristo_botev": "10135-01", "izgrev_kv": "10135-02", "kaisieva": "10135-04", "kk_konstantin_elena": "10135-02", "kochmar": "10135-03", "kokardzha_generic": "10135-02", "kolhozen_pazar": "10135-01", "kv_levski": "10135-02", "maksuda": "10135-03", "manastirski_rid": "10135-02", "menteshe": "10135-04", "mladost": "10135-03", "mladost1": "10135-03", "mladost2": "10135-03", "morska_gradina": "10135-02", "pchelina": "10135-03", "perchemliyata": "10135-02", "pobeda": "10135-03", "priboy": "10135-05", "pz_planova": "10135-04", "rakitnika": "10135-05", "rozova_dolina": "10135-05", "saltanat": "10135-02", "sotira": "10135-02", "sredna_traka": "10135-02", "sv_ivan_rilski": "10135-03", "sveti_nikola": "10135-02", "trakia": "10135-01", "troshevo": "10135-03", "tsentar": "10135-01", "tv_kula": "10135-02", "vazrazhdane": "10135-03", "vazrazhdane1": "10135-03", "vazrazhdane2": "10135-03", "vazrazhdane3": "10135-03", "vazrazhdane4": "10135-03", "vinitsa": "10135-02", "vladislavovo": "10135-04", "zelenika": "10135-05", "zlatni_pyasatsi": "10135-02", "zpz": "10135-03"}, "crosswalk": {"10135-01": "odesos", "10135-02": "primorski", "10135-03": "mladost", "10135-04": "vladislav_varnenchik", "10135-05": "asparuhovo"}, "crosswalk_why": "подписаният превод национален код → нашите пет; АГКК НИКОГА не пише район (G22 заключен) — служи само за независимо свидетелство", "disputes": 2, "inside_one_district": 60, "outside_all": 0, "state": "свидетел: представителна точка на Feature-а срещу АГКК AU5"}, "district_witness_disputes": [{"agkk": "10135-03", "code": "kochmar", "ours": "vladislav_varnenchik", "resolution": "petar_agkk"}, {"agkk": "10135-03", "code": "vazrazhdane4", "ours": "vladislav_varnenchik", "resolution": "petar_agkk"}], "excluded": [{"code": "vinitsa_sever", "display": "с.о. Виница-север", "kind": "с.о.", "registry_action": "сутрешен ход на Петър: деактивиране на кода в quarter_registry.json — регистърът НЕ се пипа от изпълнителя", "why": "Петър (07.09): „Виница-север го изключваме“ — кодът отпада от регистъра като квартал/с.о. (ход
first_properties {"approval_digest": null, "approved_at": "2026-09-06T04:30:54.528Z", "approved_by": "Petar", "attribution": "Граница по Wikimapia.org (© Wikimapia contributors) — връзка към обекта в полето url; CC BY-SA; ToS §1.G изисква и „Wikimapia.org“ с връзка към http://wikimapia.org", "basemap": null, "chosen_reason": "", "chosen_source": "wikimapia", "code": "abatko", "confirmed_at": "2026-09-06T04:30:54.528Z", "confirmed_by": "Petar (board, unsigned proba)", "district": "primorski", "district_src": "fire_varna_district", "drawn_at": null, "drawn_by": null, "fetched_at": "2026-09-06", "geometry_origin": "wikimapia_object", "imported_from": "frozen_v2#wm_id=21794778", "kind": "м-т", "license": "CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)", "license_label": "граница по Уикимапия (обект 21794778, свалена 2026-09-06), очертана от доброволци — неофициален извор; CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели); потвърдена от Петър на 2026-09-06; официален полигон няма (проверено 06.09.2026: АГКК, община — заключена, район, ПУП)", "license_terms": "http://wikimapia.org/terms_reference.html §1.F (условията не посочват версия); creativecommons.org/licenses/by-sa/", "method": "human_polygon", "name": "м-т Абатко", "note": "", "parent": null, "parent_display": null, "parent_geometry_check": "няма родител в регистъра", "precision_m": 100, "raw_geometry_sha256": "c2e0662df8b93876edceb8349c918e32775ccba09945daaf1e1f430990f77bc4", "screenshot_sha256": null, "signed_by": "Petar", "source": "wikimapia", "url": "http://wikimapia.org/21794778/bg/Местност_Абатко", "version": 1, "viewport": null, "visible_layers": null, "witnesses": [{"fetched_at": "2026-09-06", "kind": "wikimapia_object", "raw_response_sha256": "1c0561cb7e612e72f291ca33d603cc6ef7713b88ab5af7cbd6d942fbc18a7fbe", "url": "http://wikimapia.org/21794778/bg/Местност_Абатко"}], "wm_id": 21794778, "wm_ids": null, "wm_polygon_sha256": "c67f2cfcf1542459a74c67181f72633a95a19bc254d2a87d739b71496c80ee1b", "wm_title": "Местност Абатко"}
imot_bg_varna_polygons_08.09.geojson top_keys= ['type', '_meta', 'features']
_meta {"source": "imot.bg — полигоните на районите, както ги чертае самият сайт (mob_api details → points)", "fetched": "2026-09-08", "n": 95, "missing": [], "dictionary_endpoint": "https://api.imot.bg/mob_api/dictionary/search/1?town=5", "dictionary_n": 98, "dictionary_sha256": "6fa3b07007203c5a5787d0af3e0d63c03d3a625dd741ab34c8dabe1965cbf38f", "dictionary_missing_polygons": [{"id": "5848", "name": "Електроразпределение Варна"}, {"id": "6294", "name": "Малка Чайка"}, {"id": "5866", "name": "Северна промишлена зона"}], "list_endpoint": "https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)", "crs": "WGS84 (EPSG:4326), lat/lng from the API swapped to GeoJSON lon/lat", "tools": "python 3.10, shapely 2.x; no geometry edits; validity checked before any buffer(0)", "raw_kept": "scratchpad (private), not in the repo; public delivery = names/codes/memberships only"}
first_properties {"slug": "avtogara", "name": "Автогара", "raion": "Автогара", "raion_num": "5490", "n_pts": 18, "n_adverts": 53, "center": [(коорд.), (коорд.)], "src": "imot.bg mob_api details (points of the район)", "fetched": "2026-09-08", "provenance": {"endpoint": "https://api.imot.bg/mob_api/details?id=<advert_id>", "advert_id": "1c178643538536817", "raw_sha256": "776f019378cc754b1f3977b9d42cc43f4d61dcfd14b749ca8322af95b0177068", "raw_bytes": 21307, "fetched_local": "2026-09-08 05:42:39", "field": "data.adverts[0].points (lat,lng~…), coordinates flag 0 = квартален полигон"}}
imot_bg_varna_dictionary_08.09.json top_keys= list
address_rows_08.09.json top_keys= ['schema_version', 'kind', 'coordinate_order', 'field_order', 'rows']
field_order ["normalized_address", "lat", "lng"]

web search: https://shapely.readthedocs.io/en/stable/reference/shapely.covers.html
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json, collections, math
from pathlib import Path
import shapely
from shapely.geometry import shape
from shapely.ops import unary_union
p=Path('scratch/boundary_gallery/granitsi_preview_05.09')
s=json.loads((p/'quarters_signed_08.09.geojson').read_text(encoding='utf-8')); i=json.loads((p/'imot_bg_varna_polygons_08.09.geojson').read_text(encoding='utf-8')); r=json.loads((p/'address_rows_08.09.json').read_text(encoding='utf-8')); report=json.loads((p/'raioni_swap_08.09.json').read_text(encoding='utf-8'))
fo=r['field_order']; pts=shapely.points([(x[fo.index('lng')],x[fo.index('lat')]) for x in r['rows']]); S=[shape(f['geometry']) for f in s['features']]; I=[shape(f['geometry']) for f in i['features']]
print('versions',shapely.__version__,shapely.geos_version_string)
print('coordinate_order',r['coordinate_order'],'kind',r['kind'],'invalid_raw_signed_imot',sum(not g.is_valid for g in S),sum(not g.is_valid for g in I))
S=[g.buffer(0) for g in S]; I=[g.buffer(0) for g in I]; us=unary_union(S); ui=unary_union(I); cs=shapely.contains(us,pts); ci=shapely.contains(ui,pts); cov=shapely.covers(ui,pts)
print('coverage',json.dumps({'signed':int(cs.sum()),'imot':int(ci.sum()),'both':int((cs&ci).sum()),'gain':int((~cs&ci).sum()),'lost':int((cs&~ci).sum()),'outside_both':int((~cs&~ci).sum()),'boundary_not_contains':int((cov&~ci).sum()),'imot_overlap_pairs_positive_area':sum(I[a].intersection(I[b]).area>0 for a in range(len(I)) for b in range(a+1,len(I)))}))
print('relations',json.dumps(s['_meta'].get('parent_child'),ensure_ascii=False))
print('meta_sourcekeys',sorted(s['_meta'].keys()))
bys={f['properties']['code']:g for f,g in zip(s['features'],S)}; byi={f['properties']['slug']:g for f,g in zip(i['features'],I)}
rr=[]
for row in report['rows']:
 if row['verdict'].startswith('imot ≈'):
  a=shapely.contains(bys[row['code']],pts); b=shapely.contains(byi[row['imot_slug']],pts)
  rr.append((row['name'],int((a&~b).sum()),int((~a&b).sum()),row['iou']))
print('easy38_point_membership_changes',json.dumps({'sum_departures_not_unique':sum(x[1] for x in rr),'sum_arrivals_not_unique':sum(x[2] for x in rr),'rows_with_departures':sum(x[1]>0 for x in rr),'top_departures':sorted(rr,key=lambda x:-x[1])[:8]},ensure_ascii=False))
print('dict_len',len(json.loads((p/'imot_bg_varna_dictionary_08.09.json').read_text(encoding='utf-8'))))
print('summary_ratios',{'net_gain':int(ci.sum()-cs.sum()),'pp_gain':100*(ci.sum()-cs.sum())/len(pts),'gap_reduction_pct':100*(ci.sum()-cs.sum())/(len(pts)-cs.sum())})
'@ | python -B -X utf8 -" in C:\git\Fire_Varna
 succeeded in 1763ms:
versions 2.1.2 3.13.1
coordinate_order [lat,lng] kind fire_varna_address_rows invalid_raw_signed_imot 0 0
coverage {"signed": 68314, "imot": 78236, "both": 67629, "gain": 10607, "lost": 685, "outside_both": 1589, "boundary_not_contains": 0, "imot_overlap_pairs_positive_area": 0}
relations [{"child": "abatko", "parent": "kk_konstantin_elena"}, {"child": "druzhba", "parent": "asparuhovo"}, {"child": "kaisieva", "parent": "vladislavovo"}, {"child": "kokardzha_generic", "parent": "izgrev_kv"}, {"child": "mladost1", "parent": "mladost"}, {"child": "mladost2", "parent": "mladost"}, {"child": "rozova_dolina", "parent": "asparuhovo"}, {"child": "saltanat", "parent": "morska_gradina"}, {"child": "vazrazhdane1", "parent": "vazrazhdane"}, {"child": "vazrazhdane2", "parent": "vazrazhdane"}, {"child": "vazrazhdane3", "parent": "vazrazhdane"}]
meta_sourcekeys ['artifact_class', 'attribution', 'canonicalization', 'counts', 'd1_schema', 'decisions_author', 'decisions_based_on', 'decisions_blob_before_attribution', 'decisions_commit', 'decisions_path', 'decisions_sha256', 'decisions_sha256_rule', 'decisions_sha256_worktree', 'declared_deviations', 'district_resolutions', 'district_witness_agkk', 'district_witness_disputes', 'excluded', 'generated_by', 'inputs', 'licences', 'lot', 'method_licence', 'parent_child', 'parent_child_without_polygon', 'plan', 'precision_floor_m', 'precision_m_by_method', 'publication', 'registry_pending', 'rows_without_feature', 'signature', 'source_terms', 'union_crs', 'union_recipe', 'union_witness']
easy38_point_membership_changes {"sum_departures_not_unique": 0, "sum_arrivals_not_unique": 0, "rows_with_departures": 0, "top_departures": []}
dict_len 98
summary_ratios {'net_gain': 9922, 'pp_gain': np.float64(12.323934914917402), 'gap_reduction_pct': np.float64(81.35454247294194)}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json
from pathlib import Path
import shapely
from shapely.geometry import shape
from shapely.ops import unary_union
p=Path('scratch/boundary_gallery/granitsi_preview_05.09')
s=json.loads((p/'quarters_signed_08.09.geojson').read_text(encoding='utf-8')); i=json.loads((p/'imot_bg_varna_polygons_08.09.geojson').read_text(encoding='utf-8')); r=json.loads((p/'address_rows_08.09.json').read_text(encoding='utf-8')); report=json.loads((p/'raioni_swap_08.09.json').read_text(encoding='utf-8'))
fo=r['field_order']; pts=shapely.points([(x[fo.index('lng')],x[fo.index('lat')]) for x in r['rows']]); S={f['properties']['code']:shape(f['geometry']) for f in s['features']}; I={f['properties']['slug']:shape(f['geometry']) for f in i['features']}; rr=[]
for row in report['rows']:
 if row['iou'] is not None and row['iou']>=0.6:
  a=shapely.contains(S[row['code']],pts); b=shapely.contains(I[row['imot_slug']],pts); rr.append((row['code'],row['name'],int((a&~b).sum()),int((~a&b).sum()),row['iou']))
print('easy38',json.dumps({'n':len(rr),'departure_sum':sum(x[2] for x in rr),'arrival_sum':sum(x[3] for x in rr),'rows_with_departures':sum(x[2]>0 for x in rr),'top':sorted(rr,key=lambda x:-x[2])[:6]},ensure_ascii=False))
ui=unary_union(list(I.values())); us=unary_union(list(S.values())); gap=~shapely.contains(ui,pts)
lost_codes=[row['code'] for row in report['rows'] if row['iou'] is not None and row['iou']<0.3 and row['covered_by_parts_pct']<70]
print('lost7_codes',lost_codes,'unique_address_count',int(shapely.contains(unary_union([S[c] for c in lost_codes]),pts).sum()))
print('old_covered_but_new_uncovered_by_code',json.dumps(sorted([(c,int((shapely.contains(g,pts)&gap).sum())) for c,g in S.items() if (shapely.contains(g,pts)&gap).sum()],key=lambda x:-x[1]),ensure_ascii=False))
print('hybrid95plus7_coverage',int(shapely.contains(unary_union([ui]+[S[c] for c in lost_codes]),pts).sum()))
print('top_exception_intersections',json.dumps([{ 'code':c,'pct_of_old_in_imot':round(100*g.intersection(ui).area/g.area,1),'parts':sorted([(slug,round(100*g.intersection(h).area/g.area,1)) for slug,h in I.items() if g.intersection(h).area/g.area>=.01],key=lambda x:-x[1])} for c,g in S.items() if c in lost_codes or c in ['sv_ivan_rilski','morska_gradina']],ensure_ascii=False))
print('loss_as_pct',round(100*685/68314,2),'hybrid_all_old_pct',round(100*(78236+685)/80510,2))
'@ | python -B -X utf8 -" in C:\git\Fire_Varna
 succeeded in 2755ms:
easy38 {"n": 38, "departure_sum": 3932, "arrival_sum": 2510, "rows_with_departures": 31, "top": [["hristo_botev", "кв. Христо Ботев", 884, 273, 0.69], ["briz", "ж.к. Бриз", 680, 22, 0.63], ["izgrev_kv", "кв. Изгрев", 545, 0, 0.76], ["troshevo", "кв. Трошево", 287, 94, 0.62], ["grackata_mahala", "Гръцката махала", 282, 1, 0.71], ["asparuhovo", "кв. Аспарухово", 167, 5, 0.63]]}
lost7_codes ['abatko', 'druzhba', 'gorchivata_cheshma', 'gorna_traka', 'maksuda', 'rozova_dolina', 'sredna_traka'] unique_address_count 3983
old_covered_but_new_uncovered_by_code [["asparuhovo", 167], ["morska_gradina", 114], ["zlatni_pyasatsi", 98], ["saltanat", 60], ["borovets_yug", 44], ["pobeda", 37], ["alen_mak", 35], ["chaika_kv", 34], ["mladost", 28], ["manastirski_rid", 18], ["mladost1", 18], ["fichoza", 16], ["menteshe", 15], ["chaika_kk", 11], ["vazrazhdane", 11], ["vazrazhdane1", 11], ["priboy", 10], ["zelenika", 8], ["zpz", 7], ["sotira", 6], ["tsentar", 5], ["borovets_sever", 4], ["dobreva", 4], ["dolna_traka", 4], ["vladislavovo", 4], ["izgrev_kv", 2], ["rakitnika", 2], ["balam_dere", 1]]
hybrid95plus7_coverage 78236
top_exception_intersections [{"code": "abatko", "pct_of_old_in_imot": 100.0, "parts": [["k-k-sv-sv-konstantin-i-elena", 100.0]]}, {"code": "druzhba", "pct_of_old_in_imot": 100.0, "parts": [["asparuhovo", 100.0]]}, {"code": "gorchivata_cheshma", "pct_of_old_in_imot": 99.3, "parts": [["m-t-saltanat", 97.6], ["sveti-nikola", 1.7]]}, {"code": "gorna_traka", "pct_of_old_in_imot": 100.0, "parts": [["m-t-gorna-traka", 85.1], ["m-t-akchelar", 10.8], ["vinitsa", 4.0]]}, {"code": "maksuda", "pct_of_old_in_imot": 100.0, "parts": [["maksuda", 85.2], ["hristo-botev", 14.7]]}, {"code": "morska_gradina", "pct_of_old_in_imot": 46.1, "parts": [["m-t-saltanat", 45.8]]}, {"code": "rozova_dolina", "pct_of_old_in_imot": 99.4, "parts": [["asparuhovo", 99.4]]}, {"code": "sredna_traka", "pct_of_old_in_imot": 100.0, "parts": [["m-t-gorna-traka", 98.6], ["m-t-dolna-traka", 1.4]]}, {"code": "sv_ivan_rilski", "pct_of_old_in_imot": 100.0, "parts": [["maksuda", 66.9], ["avtogara", 19.0], ["troshevo", 10.8], ["zapadna-promishlena-zona", 3.3]]}]
loss_as_pct 1.0 hybrid_all_old_pct 98.03

codex
Преизчислението показва +10 607 новопокрити точки, но и 685 точки, които губят покритие — нетно +9 922. В 31 от 38-те „лесни“ двойки има адреси, които напускат досегашния квартал. Седемте запазени местни понятия пазят имена за 3 983 адресни точки, но не намаляват остатъка от 2 274.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/decisions/010_signed_quarter_boundaries.md -Encoding UTF8 -TotalCount 77' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md -Encoding UTF8 | Select-Object -Skip 119 -First 31' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath index.html -Encoding UTF8 | Select-Object -Skip 6615 -First 41' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_dictionary_08.09.json -Encoding UTF8 -TotalCount 22' in C:\git\Fire_Varna
 succeeded in 1019ms:
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


 succeeded in 1088ms:

Думите на Петър (08.09 ~08:00): „центъра и завод дружба се застъпват — ще имаме конфликти там… искам да сложим общината, стадион спартак и лятно тракия. също обособи и операта… не искам да имаме полигони, които се застъпват. ползвай кими и астра.“

- **Пробата:** `granitsi_preview_05.09/partition_preview_08.09.html` (порт 8792) от `partition_build_08.09.py` (рецептата е в скрипта; всеки полигон носи списък „произход“ — какво е изрязано и защо). Вход: 60-те подписани + разширеният Център + 18-те предложени за дупките + Цветен квартал + ориентирите. Правила по ред: (1) детето изрязва родителя (11 родства от `_meta.parent_child` + `properties.parent` + родителите на предложените); (2) застъпване без родство → по-малкият печели; двойката е „ивица“ при < 10 000 m² И < 5 % от по-малкия (Astra S36: „И“, не „ИЛИ“), иначе „борд“; (3) ориентирите се изрязват от квартала, но адресът в тях **пази квартала** („Операта, Център“ — Astra S36 §2, отделна идентичност, не преименуване).
- **Резултат:** 82 полигона (154 части), **0 остатъчни застъпвания**; 62 двойки: **13 за борда** + 49 ивици автоматично. Загуби: Възраждане 97,5 % и Младост 90,6 % (→ ГРУПА за търсене без собствена територия, К35-3), Морска градина 53,6 % (Салтанат), Левски 29,5 %, Владиславово 25,8 %, Изгрев 17,7 %, К&Е 14,8 %, Св. Иван Рилски 12,3 %. Центърът: обединението е 3,272 km², ползвана е само свързаната част 1,946 km² (Astra S36 хвана, че старият отчет казваше „−2,8 %“ — вярно е 42 % спрямо обединението; откъснатите 0,764 + 0,431 + 0,13 km² са показани пунктирано и НЕ влизат → улици от Петър). Площ от входовете, която не е в никой полигон: 1,209 km² (= откъснатите части). Висящ родител: Боровец-север/юг → „borovets“ (няма такъв код).
- **13-те за борда** (печели по-малкият, алтернативата е показана): ПЗ Планова × Владиславово 405 927 m² (61 %) · Възраждане × Възраждане 4 118 278 m² (72 %) · ЗПЗ × Капелова градина 109 468 m² (23 %) · Максуда × Св. Иван Рилски 90 623 m² (39 %) · Манастирски рид × Виница 54 339 m² (3,2 %) · Победа × СПЗ 52 110 m² (8,4 %) · Трошево × СПЗ 40 804 m² (5,5 %) · Център × Погребите 36 320 m² (23 %) · к.к. Чайка × Златни пясъци 29 273 m² (1,7 %) · Балъм дере × Владиславово 25 990 m² (4,9 %) · Изгрев × Левски 18 857 m² (0,9 %) · **Център × Завод Дружба 18 587 m² (8,8 %) — печели Завод Дружба, застъпването изчезва** · Виница × Сава 12 542 m² (1 %). Кими К35: над 25 % от по-малкия отговорът е ЙЕРАРХИЯ, не арбитраж → предложени (неприложени) родства Възраждане 4 ⊂ Възраждане и ПЗ Планова ⊂ Владиславово; Капелова градина (кандидат) не бива да изяжда подписана ЗПЗ; Максуда/Победа/Трошево са за пречертаване. Изгрев × Кокарджа и Морска градина × Салтанат НЕ са спорове — родства.
- **Ориентирите (геометрията остава в игнорираната папка):** Операта = OSM сграда 176509102 (2 105 m², пл. Независимост 1; вътре са OSM възлите „Държавна опера – Варна“ и „Драматичен театър“; Overpass 08.09) → кварталът остава Център; **капан:** Wikimapia 5559999 / OSM „Сцена Филиал“ на 150 m западно е ДРУГА сграда. Общината = OSM 983640688 (кулата, townhall) ∪ 47704367 (3-етажната част), 2 725 m², бул. 8-ми Приморски полк 43 → Център (Wikimapia „Община Варна“ 19519675 е територия с 667 точки, не сграда). Стадион Спартак = Wikimapia 5548944 (41 точки, = OSM way 1305399349, Wikidata Q5245085), 21 744 m² — **лежи в дупка** (Левски на 151 m, Победа на 203 m) → без квартал, само район. **Лятно кино Тракия: няма контур в никой източник** (OSM: два възела-спирка 6154520520/6644351215 при (коорд.)/(коорд.); Wikimapia: спирка 19756032 и „Паркинг Лятно кино Тракия“ 7011115, 1 089 m²; place.search → 0) → точка-ориентир + паркингът като пунктиран кандидат; Петър казва кой контур е киното.
- **Прегледите:** Astra S36 (`scratch/places_search/adresi_astra_S36_08.09.md`): строго разделяне за адресната принадлежност, йерархия за търсенето, ориентирите като отделна идентичност без да сменят квартала; праг „И“; никоя двойка не е оправдана само от площта — автоматизацията след обща граница + подписан приоритет + проверка на засегнатите адреси; провенанс по W3C PROV (входове, операции, ред, точност, подпис) — 59-те резултата със `src="подписан"` не удостоверяват изменена геометрия; план v3 §2/§3 иска гейтове за покритие/гранични точки/родства/еднакви резултати; D8 допуска precision буфер (v3 го представя като строго съдържание); D6 остава отделно решение. Кими К35 (`adresi_kimi_K35_08.09.md`): **НЕГОДНО за подпис** (здраво на 87 %): 8 реални спора (по „ИЛИ“), 2 нови родства, `borovets` висящ, `parent` в полигоните ≠ `_meta` (Салтанат/Кокарджа/Розова долина имат parent null в properties) = двоен източник на истина; Цветен квартал n=0 (по конструкция — броят е само на сградите ИЗВЪН подписаните) срещу 713 в бележката; Завод Дружба е дете на Левски, но е 34 % в Левски, 8,8 % в Центъра, 57 % в дупка — родителят е под въпрос; 20-те предложени нямат `precision_m`; гейт за всеки билд: пресичане = 0 (толеранс 0,001 km²), дете ≥ 99 % в родителя, без висящи кодове, всяка сграда в точно един листов полигон, спорове над прага блокират билда, ориентирите като фиксирани точки с очакван код.
- **Чака Петър:** (1) проверка на картата; (2) 13-те двойки (или правилото „по-малкият печели“ за всички под 10 %); (3) двете родства + Боровец; (4) Завод Дружба: дете на Левски или зона без родител; (5) контурът на Лятно кино Тракия; (6) Стадион Спартак без квартал — така ли остава; (7) улиците за откъснатите части на Центъра (1,33 km²). Нищо не е подписано, нищо не е комитнато; Б3 стои стейджнат.

## 17 · Петър отхвърля сградите-ориентири: РАЙОНИТЕ по imot.bg + останалите дупки (08.09 ~10:00–12:00), в ход

Думите му: „не съм доволен — общината е по-голям район… за стадион спартак имах предвид района на юг от бул. Васил Левски в близост до стадиона, същото за общината и операта — това са райони. не виждам ВИНС и Червения площад — това са райони в центъра. Генералите не е идентифициран правилно… искам дупките да ги запълним с информация от imot.bg… също и другите останали дупки“.

- **imot.bg е източникът на всекидневните имена:** за град Варна има **95 района с брой обяви** (`granitsi_preview_05.09/imot_bg_varna_areas_08.09.json`): в центъра Автогара 53, Базар Левски 72, ВИНС-Червен площад 85, Гранд Мол 174, Гръцка махала 220, ЖП Гара 33, Завод Дружба 22, Зимно кино Тракия 86, Колхозен пазар 401, Конфуто 34, Лятно кино Тракия 277, Окръжна болница-Генерали 171 (= Генералите), Операта 84, Погреби 357, Спортна зала 59, Стадион Спартак 4, Фестивален комплекс 42, ХЕИ 57, Христо Ботев 83, Цветен квартал 329, Централна поща 115, Център 823, Чаталджа 108… „Общината“ НЯМА собствен ред (Astra) → само от споменавания „до Общината“. Механика: cp1251; списък `…/grad-varna/<slug>` + `/p-N` (40 на страница); списъчната страница няма описание; обявата има „Местоположение: град Варна, <район>“ + описание с улица/номер („ул. Цар Петър I 1, до Археологическия музей“); **координати няма без вход** (картата = login; картата на района = POST-форма) → не влизаме, не пращаме форми. Затова: улица от текста → нашата OSM улична геометрия (1 270 имена; най-дълъг префикс) / OSM адресни точки с номер (4 536) → точка (адрес/ъгъл/кръстовище) или улица → KDE. Суровите HTML са само в скрачпада; публично пътуват имена и бройки.
- **Прегледи:** Astra S37 (`adresi_astra_S37_08.09.md`): първо локализация с РОЛЯ на споменаването (адрес на имота / близост / транспорт / офис на агенцията — офисът изкривява облака), улица+номер → точка, само улица → отсечки без измислена среда, две улици → кръстовище само при „на ъгъла“, „до Операта“ → отношение, не точка; пилот ≤ 120 обяви/район, дедупликация; прагове (предложени): ≥ 30 надеждни локализации, ≥ 5 улици, ≥ 3 издатели, ≥ 20 контролни адреса; KDE 75/150/250 m с ядро 80 % / периферия 95 % (не е вероятност за принадлежност); всекидневната зона има собствена идентичност — етикет „Операта (Център)“ само при потвърдено родство, едно разделяне на листови клетки с квартал + зона; „няма обяви ≠ няма район“; Спартак с 4 обяви не се чертае автоматично → условието „южно от Васил Левски“ е контролно; гейтове (≥ 95 % верни роли на ръчна извадка ≥ 30; ≥ 90 % от ≥ 20 задържани адреса вътре; IoU ≥ 0,80 при нова извадка; 0 застъпвания; провенанс без описания/контакти). Кими К36 (`adresi_kimi_K36_08.09.md`): ~52 от 95-те покрити от наши кодове, ~30 нови (obshtinata/operata/tsentralna_poshta/festivalen_kompleks ⊂ tsentar; zimno/lyatno_kino_trakia ⊂ trakia; vins_cherven_ploshtad, chataldzha; stadion_spartak; avtogara; zhp_gara; slanchev_den (дупка К&Е–Златни); селата), 5 обекта (Гранд Мол, Бизнес хотел, Летище, Пристанище, Бизнес парк → alias, не клетки); конфликти: Левски 1/2 и ВВ 1/2 като деца (схемата Възраждане/Младост), Цветен квартал ⊂ levski2?, vazrazhdane4 → parent; праг 10/50 обяви; въпроси към Петър: ХЕИ, Конфуто, vv2↔Кайсиева, Спартак pri/mla, Каменар.
- **Маската на останалите дупки** (`gaps_mask_08.09.geojson`; частни адресни точки извън всяка клетка на partition_v2; решетка 100 m): 4 328 от 80 510 точки извън всичко; 42 петна с ≥ 10 сгради (3 235 сгради). Най-големите: **1 124 сгради / 0,65 km² при (коорд.)/(коорд.) — южно от бул. Васил Левски при Стадион Спартак** (точно районът на Петър); 422 при Генералите/Спортна зала ((коорд.)/(коорд.)); 251 при Общината/Център ((коорд.)/(коорд.)); 188 при Погребите/Операта/Колхозен пазар ((коорд.)/(коорд.)); 108 при Възраждане 4; 115 при Кокодива/Манастирски рид; 97 при Ракитника; 74+37+35 при Златни пясъци/Перчемлията; 73 при к.к. Чайка/Ален мак… Показани на `areas_preview_08.09.html` (сиви петна).
- **В ход (скрачпад, частно):** теглене на списъчните страници за 95-те района (продажби + наеми, GET през 3 s), после обявите (приоритет: централните + дупките, ≤ 220/район; после ≤ 60/район; през 2,5 s — часове); парсер `imot_parse_geocode.py` (улица/номер/ориентир + роля по Astra) и строител `imot_areas_build.py` (KDE 150 m, ядро/периферия, псевдо-райони „около: Общината/Операта/Спартак/ВИНС/Червения площад/Генералите/Спортна зала“ от споменаванията); страницата чете резултата, когато се появи. Workflow „varna-area-sources“ (6 разузнавача Opus + проверка) търси и други източници с полигони (homes.bg, address.bg, общински ГИС, OSM/Wikimapia/Wikidata, спирки).
- **Поправки на предишната проба:** ориентирите-сгради (§16) остават само като факти за сградите; районите се чертаят наново по обявите. Генералите = „Окръжна болница-Генерали“ (171 обяви), а не 4-точковият правоъгълник от Wikimapia.

## 18 · ПОЛИГОНИТЕ НА imot.bg — плочка на всекидневните райони; Петър: „супер са, сравни и другите“ (08.09 ~13:00–15:00)

- **Откритието (разузнавачи Opus, workflow „varna-area-sources“, 11 агента, + моя проверка):** imot.bg чертае собствени полигони за **98 района на Варна** (речник `api.imot.bg/mob_api/dictionary/search/1?town=5`) и ги дава без вход през мобилния JSON API: `mob_api/details?id=<обява>` → поле `points` (lat,lng~…), когато `coordinates` завършва на флаг 0 (обявата не е закачена на точен адрес → сайтът чертае целия район). 95 взети (трите без обяви: Електроразпределение Варна, Малка Чайка, Северна промишлена зона). **0 застъпвания помежду им, съседите споделят върхове точно, 93,03 km², всичките валидни преди поправка**, средно 40 върха. Файл `granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson` (частна папка; провенанс по полигон: обява, SHA-256 на суровия отговор, време; речникът и хешът му в `_meta`). Втора агенция mirela.bg: 73 начертани района (`mirela_varna_areas_08.09.geojson`; 49 застъпващи се двойки, 2 невалидни преди поправка — Владиславово, Фичоза; покрива 71,8 % от сградите срещу 97,2 % при imot).
- **Сравнението с нашите** (`raioni_table_08.09.py` → `raioni_table_08.09.json`; страница `raioni_preview_08.09.html`): 42 съвпадат с нашите (IoU ≥ 0,6); 20 със същото име, но друго чертане — **Център IoU 0,37** (техният е 0,84 km², по-малък от нашия разширен; Петър: нашият е сбъркан), **Стадион Спартак 0,09** (нашият е сградата, техният — районът южно от бул. Васил Левски, 0,235 km², mirela IoU 0,80), Генералите 0,55 (imot „Окръжна болница-Генерали“ 0,272 km²), Погреби 0,47, Максуда 0,29, Победа 0,41, Евксиноград 0,44, Манастирски рид 0,47, Салтанат 0,51, Горна Трака 0,15, Левски 1/2 срещу кв. Левски 0,24/0,33, ВВ 1/2 срещу Владиславово/Кайсиева 0,24/0,00, к.к. Чайка срещу кв. Чайка 0,00 (грешна съпоставка на имена → Кими); 20 нови, запълващи дупки (ВИНС-Червен площад 219 сгради, Чаталджа 211, Гранд Мол 190, Пристанище 353, м-т Планова 126, ЖП Гара 66, Метро 39, Атанас Тарла 45, Бизнес парк 17, Летище 16 + 9 села/м-та без сгради в дупка); 7 нови вътре в наш (Базар Левски ⊂ Левски, Конфуто ⊂ Победа, Фестивален ⊂ Гръцката махала, Зимно кино ⊂ Тракия, Слънчев ден ⊂ К&Е, Боклук Тарла ⊂ Владиславово, Франга дере ⊂ Кокарджа); 6 нови, пресичащи няколко наши (Лятно кино Тракия — 641 сгради в дупка + 30 % Тракия + 24 % Център; ХЕИ; Автогара; Бизнес хотел; Централна поща 67 % Център + 32 % Тракия; ПЗ Тополи). Покритие на дупките: **3 217 от 4 328** адресни точки (спрямо 82-те клетки на partition_v2; спрямо само 60-те подписани непокритите биха били 12 196 — Astra). Ориентири: Операта → „Операта“, Стадионът → „Стадион Спартак“, ИУ → „ВИНС-Червен площад“, Общината и Окръжна болница → „Център“ (imot няма район „Общината“; има го в address.bg/homes.bg без полигони), Битоля 13 → „ХЕИ“, Студентска бл. 11 → „Левски 1“.
- **Петър:** „супер са, сравни и другите“; „мисля че е добра идея да използваме полигоните на мирела?“ → отговор с числа: основа imot.bg, mirela = втори свидетел (съгласие IoU ≥ 0,7 при 26/95; 37 без съпоставка).
- **Astra S38** (`adresi_astra_S38_08.09.md`): ОТДЕЛЕН слой „район“ (`area`) със собствено одобрение и версия, редом с `quarter` (подписан) и `district` (административен); замяна на подписан квартал = отделна обоснована корекция: същата идентичност → доказана грешка → измерен ефект върху адресите → нов подпис; етикет „Левски 1 (кв. Левски)“, „Операта (Център)“ само при проверена принадлежност; търсенето индексира двете принадлежности отделно; клетките `Qᵢ ∩ Aⱼ` са производен индекс, не доказват родителство; IoU ≥ 0,7 между сайтовете е основание за преглед, не автоматична победа; провенанс-пакет (URL/параметри, id, време, суров отговор, SHA-256, условия, преобразувания, версии) — метаданните бяха непълни → допълнени днес; гейтове: всички 98 id отчетени, валидност преди поправка, 0 застъпвания, съвпадащи ръбове, отделен отчет за дупките, метрични площи, възпроизводимо присвояване; промяна на сайта → нов кандидат + пространствен диф; остатъчните 1 111 точки → маска и класификация (порт/промзона/село/остаряла точка), гейт „всяка точка отчетена“; ADR 010: D6 пази `quarter`, новият канал записва `area` отделно; D8 е вътре в слоя; план v3: версия на схемата, два резултата, отделни правила за търсене, подписани примери, гейтове. Кими К37 — в ход (съпоставка на имената, кой е верният контур при разлика, кодове за 34-те нови, гейт за плочков слой).
- **Кими К37** (`adresi_kimi_K37_08.09.md`): imot-слоят **ГОДНО** (95 полигона, 0 застъпвания, площите = сумата), таблицата **НЕГОДНО без регенерация** → поправено: 2 грешни алиаса (imot „к.к. Чайка“ = курортът `chaika_kk`, не кв. Чайка — потвърждава coord_rule; „Владислав Варненчик 2“ ⊂ Владиславово, не Кайсиева), „в.з. Виница-север“ = нов подрайон на Добрева чешма, и изрична бележка, че IoU е срещу подписаната геометрия преди изрязване, а overlaps/дупки — срещу клетките след изрязване. Правило R1–R5 за 20-те с друго чертане: **преначертай нашите** — Акчелар (mirela 0,75), Сотира (0,75), Стадион Спартак (0,80), Операта (0,84; микрорайон ⊂ Център), Окръжна болница-Генерали (нашият е 100 % в imot, Петър: „сбъркан“), Център (imot-ядро + потвърдените микрорайони ЖП Гара/ХЕИ/Поща/Операта/Бизнес хотел с mirela 0,78–0,85); **нашите стоят** — Максуда (mirela 0,14; 62 % от imot е в Св. Ив. Рилски), Фичоза, Евксиноград, Победа, Горна Трака (imot поглъща 4 подписани), Манастирски рид (imot 4,09 срещу наш 1,93 km²), Салтанат; **нерешено** — Погреби (0,51, леко към imot); **подрайони** — Левски 1/2, ВВ 1/2 (сумите на децата ≈ родителите). 34-те нови: 24 приеми (кодове/вид/район/родител в таблицата на К37: chataldzha, vins_cherven_ploshtad, zhp_gara, lyatno_kino_trakiya, hei, avtogara, tsentralna_poshta, konfuto, bazar_levski, festivalen_kompleks, zimno_kino_trakiya, slanchev_den, bokluk_tarla, franga_dere, pz_topoli, pz_metro, mt_planova, atanas_tarla…), 5 обекта (Гранд Мол, Бизнес хотел, Летище, Пристанище, Бизнес парк → alias/точка, не клетки), 10 извън адресния обхват (селата, Крушките/Орехчето/Припек/Лазур — 0 сгради → отложи).
- **Междинно (отпада):** методът „улици от текста на обявите → KDE“ (S37) даде само 127/370 локализирани обяви и ядра по 1–2 km² — недостатъчен; заменен от полигоните на самия сайт. HTML-тегленето е спряно (428 обяви, скрачпад).

 succeeded in 1096ms:
    // inclusion. `src` is a CLOSED set and each source has its own URL rule: the
    // single openstreetmap entry (`mladost2`) points at the ODbL copyright page and
    // matches no wikimapia pattern. Not one byte of any of it reaches a card.
    const ATTRIB_KEYS = ['src', 'url', 'label', 'licence'];
    const ATTRIB_SRC = ['wikimapia', 'openstreetmap'];
    // О17: pinned to the DELIVERED shape (http, id, path), not to the literal of
    // амандамент №2 („https://wikimapia.org/<wm_id>/“) — measured 07.09.
    const WM_URL = /^https?:\/\/wikimapia\.org\/\d+\//;
    const OSM_URL = 'https://www.openstreetmap.org/copyright';
    function validQuarterAttribution(meta, rows) {
      const map = meta && meta.quarter_attribution;
      if (!map || typeof map !== 'object' || Array.isArray(map)) return false;
      for (const k of Object.keys(map)) {
        const e = map[k];
        if (!e || typeof e !== 'object' || Array.isArray(e)) return false;
        if (Object.keys(e).length !== ATTRIB_KEYS.length) return false;
        for (const f of ATTRIB_KEYS) if (typeof e[f] !== 'string' || !e[f]) return false;
        if (ATTRIB_SRC.indexOf(e.src) < 0) return false;
        if (e.src === 'wikimapia' && !WM_URL.test(e.url)) return false;
        if (e.src === 'openstreetmap' && e.url !== OSM_URL) return false;
      }
      // equality with the SIGNED_POLYGON codes of THIS bundle (both directions)
      const need = new Set();
      for (const r of rows)
        if (r.quarter && r.quarter.src === 'SIGNED_POLYGON') need.add(r.quarter.code);
      if (Object.keys(map).length !== need.size) return false;
      for (const c of need) if (!map[c]) return false;
      return true;
    }
    const META_KEYS_HOTELS = ['generated', 'count', 'by_zone_src', 'licence',
      'licence_osm', 'licence_address', 'quarter_attribution', 'excluded'];
    const META_KEYS_PLACES = ['generated', 'count', 'by_kind', 'by_zone_src',
      'licence_osm', 'licence_registry', 'licence_wikidata', 'licence_address',
      'quarter_attribution', 'excluded'];
    function metaKeysAre(meta, want) {
      const got = Object.keys(meta || {});
      if (got.length !== want.length) return false;
      for (const k of want) if (got.indexOf(k) < 0) return false;
      return true;
    }
    const validateCats = (d) => !!(d && d._meta && d._meta.schema === 1 && d.forms &&

 succeeded in 891ms:
[
 {
  "id": "5490",
  "name": "Автогара"
 },
 {
  "id": "5491",
  "name": "Аспарухово"
 },
 {
  "id": "5840",
  "name": "Базар Левски"
 },
 {
  "id": "5841",
  "name": "Бизнес парк Варна"
 },
 {
  "id": "6183",
  "name": "Бизнес хотел"
 },
 {

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/decisions/010_signed_quarter_boundaries.md -Encoding UTF8 | Select-Object -Skip 45 -First 10' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/decisions/010_signed_quarter_boundaries.md -Encoding UTF8 | Select-Object -Skip 59 -First 6' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json
from pathlib import Path
from shapely.geometry import shape
from shapely.ops import transform, unary_union
from pyproj import Transformer
p=Path('scratch/boundary_gallery/granitsi_preview_05.09'); t=Transformer.from_crs('EPSG:4326','EPSG:32635',always_xy=True).transform
for f in ['quarters_signed_08.09.geojson','imot_bg_varna_polygons_08.09.geojson']:
 d=json.loads((p/f).read_text(encoding='utf-8')); u=unary_union([transform(t,shape(x['geometry'])) for x in d['features']]); print(f,round(u.area/1e6,4))
'@ | python -B -X utf8 -" in C:\git\Fire_Varna
 succeeded in 1071ms:
**D5 · Ново име само с ≥ 2 свидетеля (К3) и обратим път.** „Цветен квартал“: свидетел 1 = подписът на Петър; свидетел 2 = `node/9664925200` с 15 места на ≤ 900 m. Втори свидетел може да е и АГКК именувана точка (Левски и Максуда имат; М0.21), ред от пощенския указател или общинска публикация с адрес (М0.22) — по-силни от OSM възел, защото са официални. При ЕДИН свидетел името е `alias`, не код. **Отмяна:** ред клас „въпрос“ + обратен диф с двоен запис + махане на кода от петте затворени списъка в един комит на Fire_Varna; фикстура: код в доставка, който вече не е в регистъра → червено. Записът влиза през конвейера на Varna_buildings (D14).

**D6 · `SIGNED_POLYGON` — свидетел ранг 3 (S1/К2).** Нов канал под `REG-*` (0), `KAIS-quar` (1), `KAIS-addr` (2). ОТДЕЛЕН блок в `varna_3d/src/fire_varna_locations.py` **между ред 873 и 875** — след записа на `picked` в `out` (867–873), преди `if signed:` (875) — и **никога в цикъла `offered/ranked/conflict` (785–853)**, където `conflict` бланкира вече написано поле (`:834`, `:852`) и вкарва реда в `pending_signature`. **Шест състояния:** `confirmed` · `compatible` (деклариран родител/дете, БЕЗ замяна и без уточняване) · `disputed` · `edge_pending` (D7) · `override_noted` · `written`. Пише САМО в ред без нито един свидетел, без `pending`, извън ръба, в точно един полигон (или в декларираното дете), с `witness=[CH_SIGNED_POLYGON]` и кода в `channels[CH_SIGNED_POLYGON].ids` (`qa_fire_varna_m6.py:304-308`). Полигон-местност никога не пълни `quarter` — `classify(code) == field` (`KIND_CLASS:118`), с падаща фикстура. `_narrow` (`:907-917`) уточнява САМО вътре в полигонния канал. **`SIGNED_OVERRIDE` се пази безусловно (S1):** при 12-те подписани хотела блокът само сравнява и пише `override_noted` в леджера; никога не мени полето, никога не влиза в `signed_vs_witness`, а `CHANNEL_RANK` не получава ключ `SIGNED_OVERRIDE`. **`disputed` е ЛЕДЖЕР-САМО:** редът остава дословно както е, отива в `polygon_review`, нищо публично не се мени. Това е **обявено ОТКЛОНЕНИЕ от К2** (решение §6.4): `LOC_KEYS` са точно 3 (`index.html:6311`, `:6531-6533`), няма ключ за `winner`/`reason`, а „падане до район“ би изтрило написан от по-силен канал квартал. Таблицата на К2 е входна карта за реда в опашката; спорът се версионира (`polygon_review[i].polygon_version`). **159 е ДОПУСТИМАТА популация, не write-set.** 8-те сблъсъка не се решават от полигона.

**D7 · Ръбът: `max(50, precision_m)` в EPSG:32635 върху пиннати ИЗВОРНИ координати (S2 + К5).** `_meta.precision_floor_m = 50`; гейтът отказва `precision_m < 50`. Забранено е да се четат изнесените координати (`fire_varna_locations.py:968-982` прави точно това и се маха от полигонния път). Мери се И точката, И закотвеното тяло (`evidence.kais_i`); разминаване → `edge_pending`. Формулата е `shapely.geometry.shape(f["geometry"]).boundary.distance(point)` — през `shape`, защото подписан квартал реалистично е MultiPolygon. Проекция: `place_identity.make_projection()` (`:219-236`); `pyproj` 3.6.1, `shapely` 2.1.2 — нула нови зависимости. **Никакво местене, никакъв snap.** `SIGNED_POLYGON_BORDER` НЕ става публикуван `src` — **обявено ОТКЛОНЕНИЕ от К5** (решение §6.16).

**D8 · Йерархията — само подписана и геометрично доказана.** Родство се чете единствено от `parents` (днес 6 записа), ациклично И доказано: **дете ⊆ родител в рамките на `precision_m` буфер**; фалшив `parent` = червено. **Числовата опашка в `is_child` (`:488-503`) не е родство при полигони.** „≤ 1 полигон на място“ важи между НЕСРАВНИМИ квартали. **В ПРАЗЕН ред пише детето; в ред с написан квартал полигонът НИКОГА не уточнява.** Възраждане 1–4 нямат `parents` — поправка в регистъра, ПРЕДИ кода (D14).

**D9 · Версии, диф и откат (К5, S1).** **ВСЯКА нова версия иска подпис на Петър.** Прагове: > 2 места сменят квартал ИЛИ > 10 % площ → двоен запис преди/след и пълно преизмерване; под тях — обикновен отчет. `--diff <предишна>` е ГЕЙТ с изход ≠ 0 над праговете (G15). **Версия 1: диф-гейтът е НЕПРИЛОЖИМ, не червен.** **Откат на лоша версия:** предишната подписана версия се връща като НОВА версия (`version` расте, `previous_version` сочи отхвърлената, `note` носи довода), минава пълния G1+G15 и се комитва от Петър; никакво `git revert` върху геометрия и никакво тихо редактиране. Всеки диф се предава като ред клас „въпрос“ (по D3 не може да е „артефакт“).


 succeeded in 1070ms:
**D12 · Търсенето (клас B) — К6 + S4.** Идемпотентен `location_key(toks) -> (type, phrase)`, приложен ИДЕНТИЧНО върху индекса и остатъка, дефиниран върху **СПИСЪК ОТ ТОКЕНИ**. Типовият префикс е поредица с двете си арности. Хвърля съюза „и“ и префикса, **пази числата** и затворен списък посоки. Правило: остатъкът == пълната фраза на ТОЧНО ЕДИН запис, иначе уникална СЪСЕДНА подфраза; пазач: число / посока / „sveti“ никога не квалифицира. **Областта е ИЗНЕСЕНИЯТ речник**, премерен наново преди подпис. **Типът СТЕСНЯВА само когато е изричен И съвпада с поне един кандидат.** **Двусмислието не ражда нов видим текст** (`AGENTS.md:138`) — **обявено ОТКЛОНЕНИЕ от К6**: уточнителят при двусмислие е отложен, защото иска дословен български текст от Петър (решение §6.20); днешното поведение при двусмислие се запазва и се пази от замразена заявка. **Родител ⊃ дете живее в ИЗНОСА** (per-code `type` и `parents` по КОДОВЕ); затворените списъци → `_meta` до `zone_generic_words` (`build_place_categories.py:566`), fail-closed. **Паритет:** `window.__places.locationKey(q)` влиза в корпуса `probe_out/token_parity.json` (**759 низа**, М0.18). **11 подписани вектора** + проби съюз, точкувана форма, число, посока, двусмислие, йерархия. Манифест по `bundle:ordinal` („РОЯЛ“ ×2; `release.compare()` сравнява по име, `gates/release.py:780-823`). **Смяна на КЛОН при непроменени редове = делта от първи ред.**

**D13 · Атомност през ТРИ репа (S5/S6).** Един комит през две репа не съществува. **Подредената тройка важи за ДАННИТЕ, не за инструмента:** инструментът (Г1) и гейтовете му са предпоставка и стоят извън тройката. Тройката е: **(1) Varna_buildings** — записът, `parents`, преподписаната константа (D14); **(2) varna_3d** — резолверът, двата износни гейта (`qa_fire_varna_export.py:191`, `qa_fire_varna_places_export.py:323`), вторият препис (`qa_fire_varna_m6.py:58-64`), износът; **(3) Fire_Varna** — **блобовете влизат в СЪЩИЯ комит със затворените списъци**: `QUARTER_SRC` (`index.html:6313`), `QUARTER_CODES` (`:6317`), `LOCALITY_CODES` (`:6322`), трите SHA пина (`:6288-6290`), `LEGACY_BUNDLE_SHA` (`:6301`), `PLACES_CACHE` v6 → **v7** (`:6265`), и поименно пиновете на двата теста: `PLACES_SHA256`/`BYTES` 122089/`GZIP9` 13728, `HOTELS_*` 148685/13084, `CATEGORIES_*` 75818/9104, `QUARTER_BY_SRC` (точно равенство), `QUARTER_CODES`, `LOCALITY_CODES`, `LOCATION_COUNTS` {quarter 20, district 5, locality 5}, `LEGACY_ROWS` 18, `LOCALITY_COUNT`; плюс baseline → `fd13907` (`signed_by: "pending — Петър"`) и подмяната на allow-файла. Числата се ПРЕМЕРВАТ след чертането. Тихата смърт, доказана: непознат `src` → `validLocation` false (`:6528-6534`) → `validTypedLocation` (`:6535-6541`) → `validatePlaces2` (`:6569-6576`) → `null` → `places2 = []`, хотелите остават (`:6627-6640`) — **150 места изчезват мълчаливо**; `accept` сверява SHA само при `crypto.subtle` (`:6605`) → кешът задължително на v7. **Манифестите са ТРИ** (`gates/release.py:157-159`): `lot1v_v_manifest_BASE_P7.json` = дифът на ДАННИТЕ (P7→P8 по `place_id`), `lot1v_v_manifest_P7_F12.json` = дифът на ПОВЕДЕНИЕТО, `lot1v_v_reference_manifest.json` = манифестът на референцията; и трите се преизползват в съществуващите слотове с `_meta.what` и изричен ред „името е остаряло“. Имената живеят на **ПЕТ ръчни места**: `gates/release.py:157-159`, `:175-183`, `manifest_anchor_gate.py:42-44`, `recall_sweep.py:3070-3071`, `recall_sweep.py:2661`. **Замразените тела са ТРИ** (амандамент №11 т. 4): референцията `recall_sweep_rows.json` (вързана през `expectations._meta.reference`), `expectations.json`, и паритетният корпус `probe_out/token_parity.json`, който **днес не е вързан от нищо** и влиза в `expectations._meta.inputs`.

**D14 · Регистърът е подписано тяло (S5).** `Varna_buildings/js/lib_quarter_registry.mjs:35` заключва `schema_version`, `id`, `display`, `kind`, `aliases`, `parents`; `:45` държи `REGISTRY_SIGNED_SHA256`; `:121-127` хвърля „never patch the constant to make a build pass“. Затова: (1) промяната е **СОБСТВЕН датиран план в Varna_buildings със собствен §7 (дефиниция за готово)**, минаващ през неговите Approval gates (`AGENTS.md:273-275`) **и през Кими и Astra** (§0.3), чиято присъда влиза в **собствен амандамент — нов датиран файл** в същата папка; (2) константата се преизчислява и **подписва от Петър, в негов комит**, заедно с данните; (3) `node js/test_quarter_registry.mjs` тича в кръга (G5); (4) **агент никога не пипа константата**. Преди комита: нула съвпадения на новото име в 449 `quar` + 19 813 `addr` и нула сблъсък на `match_key` (М0.14); след комита `qa_fire_varna_location_isolation.py` зелено (G6/G10) — `place_zones._registry:252-255` индексира БЕЗ вид.


 succeeded in 1359ms:
quarters_signed_08.09.geojson 61.5967
imot_bg_varna_polygons_08.09.geojson 93.028

codex
Има още една съществена зависимост: геометричното обединение на децата няма да осигури търсене по родител. Б3 днес запазва случай, в който „Аспарухово“ не намира обекта в Дружба; валидаторът отхвърля и нов източник `imot`. Затова хибридът изисква миграция на родствата, търсенето и атрибуцията заедно с геометрията.

codex
**Препоръчвам (в) за целия град: imot като кандидат за основната геометрия, с подписани местни изключения и една обща йерархия.** Условието е запазване на разпознаваемите за пожарникаря понятия и проверка на адресните промени. **IoU ≥ 0,6 не разрешава автоматична замяна.** Двуслойният вариант (б) остава резервен там, където двете деления имат несъвместимо значение.

Прегледът е само за четене; нищо не е променено. Инвентарът и прочетените входове обхващат `raioni_swap_08.09.json`, `raioni_swap_08.09.py`, двата изворни GeoJSON файла, речника, адресните редове, §18, ADR 010 и съответните Б3 код/фикстури. Геометричните числа са проверени независимо от втори агент. Външните реализации на регистъра и `search_bridge` не са инспектирани; труд в часове не е измерен.

1. **Основа и цена**

| Вариант | Измерима цена/полза | Оценка |
|---|---|---|
| **(а)** | 95 геометрии; 97,2% покритие; седем местни понятия с 3 983 адресни точки губят досегашната си идентичност | Най-прост набор, недостатъчно доказана семантика |
| **(б)** | 60 + 95 = **155 изворни геометрии**, две принадлежности и правила за търсене | Пази различията, увеличава постоянната поддръжка |
| **(в)** | 95 кандидата + избрани изключения + производни родители; окончателният брой предстои | Предпочитан, ако се получи последователна йерархия |

Не мога обосновано да нарека (в) най-евтин **за реализация**; очаквам по-малко постоянна двойна поддръжка от (б).

Повторното пресичане установи **10 607 новопокрити, но 685 отпадащи точки**: нетно **+9 922**, или **+12,32 процентни пункта**. В **31/38** „лесни“ двойки адреси напускат стария квартал: общо **3 932 различни точки**, от които **475** остават извън всякакъв imot полигон. Следователно „замяна без загуба“ в [скрипта](/C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/raioni_swap_08.09.py:72) е недоказана присъда.

Тези числа измерват **адресни точки, не уникални сгради**, и покритие на наличните 80 510 точки, не независимо доказана пълнота за града. Площите в EPSG:32635 са **61,60 → 93,03 km²**; 61,67/93,14 са приближението на скрипта.

Бордът обхваща всичките 60 съпоставки: **38 за ускорен преглед, 22 за подробно решение**. „46 без двойник“ означава неизбрани от алгоритъма imot полигони; това не доказва 46 нови квартални кода.

2. **D8 и родителите**

Да: Левски, Владиславово, Възраждане и Младост могат да бъдат **обединение на поименно подписани деца**, с възпроизводима рецепта и собствена версия. Родителят остава цял агрегат; листовите територии дават конкретната принадлежност.

Проверяват се повторно **всичките 11 родства**, чрез една канонична таблица, без цикли. Отделно се подписва включването на Възраждане 4. При Левски/Владиславово **93%/94%** съответствие оставя разлика за адресен отчет и решение.

Старите изключения не стават деца по удобство. Св. Иван Рилски пресича **четири** imot клетки; Горна Трака — три; Максуда — поне две. Там са нужни подписана поправка на основата или изрично запазено различно деление. **Морска градина не може да се свие до Салтанат**, който покрива около 46%.

[D8](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52) допуска съдържание в рамките на `precision_m`; това се проверява метрично. За строго съдържание, включително общия ръб, подходящият предикат е [`covers`](https://shapely.readthedocs.io/en/stable/reference/shapely.covers.html). Геометричното съдържание само по себе си не доказва вярно родство.

3. **Какво се подписва**

Един бордов ред трябва да показва **старо → предложено**: код, име, вид, родител, контур, добавени/напускащи адреси, спорни ориентири. Решението е „приемам / отхвърлям / поправям / запазвам като изключение“.

Подписът обвързва точно: изворен id/URL/момент, суров SHA-256, версия и хеш на речника, преобразувания, резултатна геометрия, родства и снимка на борда. Декларираното `"WGS84 (EPSG:4326)"` и провенансът удостоверяват произхода; **не удостоверяват оперативна вярност**.

След одобрението снапшотът се замразява. Следващо теглене е нов кандидат с пространствен и адресен диф. [D9](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:54) изисква нов подпис; над две променени места или 10% площ — пълно преизмерване.

4. **Какво се чупи**

**28 `QUARTER_CODES` са доставеният речник**, не броят на всички понятия. Нов код може да отхвърли целия пакет. Допълнително [валидаторът](/C:/git/Fire_Varna/index.html:6620) допуска атрибуция само `wikimapia`/`openstreetmap`; imot изисква нов подписан договор за източника.

**Union не поправя търсенето.** Б3 фикстурата за „Аспарухово“ изключва обекта в Дружба; родителското търсене трябва да използва подписани кодови родства. Нужни са нови очаквания върху сегашните **11 фикстури/20 заявки**, плюс спорните граници.

[D13–D14](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:62): регистър/родства/подпис → 3D резолвер и износ → Fire данни, списъци, атрибуция, SHA, кеш и фикстури заедно. `search_bridge` трябва да бъде измерен в собствения checkout. D6 продължава да пази написаните REG/KAIS принадлежности.

Архитектурната промяна изисква подписан амандамeнт. Самият ADR още декларира **„Proposed … неподписана“** — документното несъответствие трябва да се изясни преди изпълнение.

5. **Остатъкът**

**2 274 = 685 загубени спрямо старото покритие + 1 589 извън двете основи.** Запазването на седемте местни полигона добавя **нула** покрити адресни точки.

Маската трябва да е `подписан обхват − обединение(imot)`, с всяка остатъчна точка отчетена веднъж: регресия, липсващ изворен полигон, парк/порт/промзона, периферия/село, съмнителна координата или нерешено. Отделна проверка за трите липсващи речникови id. **48-те клетки с ≥10 точки не са 48 доказани района**; автоматично присвояване по най-близък полигон би скрило проблема.
tokens used
80,343
**Препоръчвам (в) за целия град: imot като кандидат за основната геометрия, с подписани местни изключения и една обща йерархия.** Условието е запазване на разпознаваемите за пожарникаря понятия и проверка на адресните промени. **IoU ≥ 0,6 не разрешава автоматична замяна.** Двуслойният вариант (б) остава резервен там, където двете деления имат несъвместимо значение.

Прегледът е само за четене; нищо не е променено. Инвентарът и прочетените входове обхващат `raioni_swap_08.09.json`, `raioni_swap_08.09.py`, двата изворни GeoJSON файла, речника, адресните редове, §18, ADR 010 и съответните Б3 код/фикстури. Геометричните числа са проверени независимо от втори агент. Външните реализации на регистъра и `search_bridge` не са инспектирани; труд в часове не е измерен.

1. **Основа и цена**

| Вариант | Измерима цена/полза | Оценка |
|---|---|---|
| **(а)** | 95 геометрии; 97,2% покритие; седем местни понятия с 3 983 адресни точки губят досегашната си идентичност | Най-прост набор, недостатъчно доказана семантика |
| **(б)** | 60 + 95 = **155 изворни геометрии**, две принадлежности и правила за търсене | Пази различията, увеличава постоянната поддръжка |
| **(в)** | 95 кандидата + избрани изключения + производни родители; окончателният брой предстои | Предпочитан, ако се получи последователна йерархия |

Не мога обосновано да нарека (в) най-евтин **за реализация**; очаквам по-малко постоянна двойна поддръжка от (б).

Повторното пресичане установи **10 607 новопокрити, но 685 отпадащи точки**: нетно **+9 922**, или **+12,32 процентни пункта**. В **31/38** „лесни“ двойки адреси напускат стария квартал: общо **3 932 различни точки**, от които **475** остават извън всякакъв imot полигон. Следователно „замяна без загуба“ в [скрипта](/C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/raioni_swap_08.09.py:72) е недоказана присъда.

Тези числа измерват **адресни точки, не уникални сгради**, и покритие на наличните 80 510 точки, не независимо доказана пълнота за града. Площите в EPSG:32635 са **61,60 → 93,03 km²**; 61,67/93,14 са приближението на скрипта.

Бордът обхваща всичките 60 съпоставки: **38 за ускорен преглед, 22 за подробно решение**. „46 без двойник“ означава неизбрани от алгоритъма imot полигони; това не доказва 46 нови квартални кода.

2. **D8 и родителите**

Да: Левски, Владиславово, Възраждане и Младост могат да бъдат **обединение на поименно подписани деца**, с възпроизводима рецепта и собствена версия. Родителят остава цял агрегат; листовите територии дават конкретната принадлежност.

Проверяват се повторно **всичките 11 родства**, чрез една канонична таблица, без цикли. Отделно се подписва включването на Възраждане 4. При Левски/Владиславово **93%/94%** съответствие оставя разлика за адресен отчет и решение.

Старите изключения не стават деца по удобство. Св. Иван Рилски пресича **четири** imot клетки; Горна Трака — три; Максуда — поне две. Там са нужни подписана поправка на основата или изрично запазено различно деление. **Морска градина не може да се свие до Салтанат**, който покрива около 46%.

[D8](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:52) допуска съдържание в рамките на `precision_m`; това се проверява метрично. За строго съдържание, включително общия ръб, подходящият предикат е [`covers`](https://shapely.readthedocs.io/en/stable/reference/shapely.covers.html). Геометричното съдържание само по себе си не доказва вярно родство.

3. **Какво се подписва**

Един бордов ред трябва да показва **старо → предложено**: код, име, вид, родител, контур, добавени/напускащи адреси, спорни ориентири. Решението е „приемам / отхвърлям / поправям / запазвам като изключение“.

Подписът обвързва точно: изворен id/URL/момент, суров SHA-256, версия и хеш на речника, преобразувания, резултатна геометрия, родства и снимка на борда. Декларираното `"WGS84 (EPSG:4326)"` и провенансът удостоверяват произхода; **не удостоверяват оперативна вярност**.

След одобрението снапшотът се замразява. Следващо теглене е нов кандидат с пространствен и адресен диф. [D9](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:54) изисква нов подпис; над две променени места или 10% площ — пълно преизмерване.

4. **Какво се чупи**

**28 `QUARTER_CODES` са доставеният речник**, не броят на всички понятия. Нов код може да отхвърли целия пакет. Допълнително [валидаторът](/C:/git/Fire_Varna/index.html:6620) допуска атрибуция само `wikimapia`/`openstreetmap`; imot изисква нов подписан договор за източника.

**Union не поправя търсенето.** Б3 фикстурата за „Аспарухово“ изключва обекта в Дружба; родителското търсене трябва да използва подписани кодови родства. Нужни са нови очаквания върху сегашните **11 фикстури/20 заявки**, плюс спорните граници.

[D13–D14](/C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:62): регистър/родства/подпис → 3D резолвер и износ → Fire данни, списъци, атрибуция, SHA, кеш и фикстури заедно. `search_bridge` трябва да бъде измерен в собствения checkout. D6 продължава да пази написаните REG/KAIS принадлежности.

Архитектурната промяна изисква подписан амандамeнт. Самият ADR още декларира **„Proposed … неподписана“** — документното несъответствие трябва да се изясни преди изпълнение.

5. **Остатъкът**

**2 274 = 685 загубени спрямо старото покритие + 1 589 извън двете основи.** Запазването на седемте местни полигона добавя **нула** покрити адресни точки.

Маската трябва да е `подписан обхват − обединение(imot)`, с всяка остатъчна точка отчетена веднъж: регресия, липсващ изворен полигон, парк/порт/промзона, периферия/село, съмнителна координата или нерешено. Отделна проверка за трите липсващи речникови id. **48-те клетки с ≥10 точки не са 48 доказани района**; автоматично присвояване по най-близък полигон би скрило проблема.
