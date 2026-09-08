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
session id: 01a081b9-dbfd-78c0-991f-5f085ceeaac7
--------
user
S41 · Външно око (леща МЕХАНИКА), последна преди изпълнение. Петър одобри плочката на imot.bg като квартална карта и каза: „дай ги на Astra и на Кими за проверка и да ги вкарваме“; попита и дали зависим от сайта им. ОБОРИ следните твърдения на Архитекта, всяко с М (команда + изход) или Ч (файл:ред), без нищо да пишеш: (1) Конвейерът и живата карта НЕ зависят от imot.bg по време на работа: снимката от 08.09 е файл (Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson, 175 736 B, и varna_dictionary_08.09.json, 6 274 B — игнорирана папка), планът И-А я копира във varna_3d/data (К2 на Петър) и я пинва по sha; нито index.html, нито data/*.json на Fire_Varna, нито varna_3d/src викат imot.bg (единствената поява е стар скрипт verify_web_rows.py извън лота). Ако сайтът спре, спира само възможността за НОВА снимка. (2) Преименуването ИА-О40 (префиксът imot_bg_ падна от двата файла по думата на Петър) е пълно и непротиворечиво в плана docs/plans/ПЛАН_Картата_imot_И-А_08.09.md — Ф5/Ф6 (§3.А), Т1 (двата !-реда в §3.Б), К2 (§6), ИА-1 (§5), §1.4, Г.7 т. 1–2, червен ред 5, стъпка 3 — и в docs/decisions/011_kartata_imot.md и docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md §20; grep за старите имена дава 0 в трите проследени документа и в игнорираната папка; байтовете и sha са същите. (3) Провенансът не зависи от името на файла: _meta.source = imot_bg_tiling, _meta.list_endpoint и провенансът по Feature стоят вътре в снимката. (4) Планът е изпълним от стъпка 0 ДНЕС: финални проверки 8–10 (scratch/places_search/karta_imot_plan_reviews_08.09.md, последните три раздела) дадоха ГОДНО по двете лещи; базовата линия на §1.1 (две чужди worktree-та във Fire_Varna, Б3 стейджнат 14 пътя, varna_3d 05f485e/rezhimi) се възпроизвежда. (5) Нищо от геометрията не излиза публично (ADR 011, ИА-7/ИА-19, b3_g11). Правила: САМО четене; не преписвай координати (нито с точка, нито със запетая) и 64-знакови хешове в отговора — той влиза в проследен файл на публично репо; блобови sha по първите 8 знака. Формат: S41-1 … S41-5, всяко ОБОРВАМ / ПРИЕМАМ / С УГОВОРКА + довод 2–5 изречения + М/Ч; накрая S41-6: присъда ГОДНО/НЕГОДНО за старт на Изпълнителя и до 3 неща, които Изпълнителят трябва да знае. Таван 900 думи, без увод и обобщение.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя петте твърдения само с четене и ще върна М/Ч доказателства, без координати и пълни хешове. Ще разделя проверката на имената и провенанса от тази на работната база и забраната за публикуване.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'docs/activeContext.md' -TotalCount 120" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --short --branch' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$auditPaths = @('"'AGENTS.md','docs/plans/ПЛАН_Картата_imot_И-А_08.09.md','docs/decisions/011_kartata_imot.md','docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md','scratch/places_search/karta_imot_plan_reviews_08.09.md','scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson','scratch/boundary_gallery/granitsi_preview_05.09/varna_dictionary_08.09.json','index.html','.gitignore'); "'$auditPaths | Sort-Object | ForEach-Object { if (Test-Path -LiteralPath $_) { $auditItem=Get-Item -LiteralPath $_; '"'{0}"'`t{1} B'"' -f "'$_,$auditItem.Length } else { '"'MISSING: '+"'$_ } }; git rev-parse --show-toplevel' in C:\git\Fire_Varna
 succeeded in 380ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 153, behind 3]
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
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_brief_astra.md
?? scratch/places_search/granitsi_brief_kimi.md
?? scratch/places_search/karta_imot_plan_IA_r5_raw_08.09.md
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
?? scratch/places_search/tiles_astra_S41_08.09.md
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

 succeeded in 521ms:
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

 succeeded in 575ms:
.gitignore`t3287 B
AGENTS.md`t27909 B
docs/decisions/011_kartata_imot.md`t16540 B
docs/plans/ПЛАН_Картата_imot_И-А_08.09.md`t227700 B
docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md`t129713 B
index.html`t566532 B
scratch/boundary_gallery/granitsi_preview_05.09/varna_dictionary_08.09.json`t6274 B
scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson`t175736 B
scratch/places_search/karta_imot_plan_reviews_08.09.md`t597630 B
C:/git/Fire_Varna

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'imot[._]bg|imot-bg' index.html data -g '*.json'; rg -l --max-count 20 --max-columns 200 'imot[._]bg|imot-bg' 'C:/git/varna_3d/src'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'AGENTS.md' -Encoding UTF8 -TotalCount 65; Get-Item -LiteralPath 'C:/git/varna_3d' | Select-Object -ExpandProperty FullName; rg --files --max-count 20 --max-columns 200 -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!.git'"' 'C:/git/varna_3d'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re
p=Path('docs/plans/ПЛАН_Картата_imot_И-А_08.09.md')
lines=p.read_text(encoding='utf-8').splitlines()
for i,s in enumerate(lines,1):
 if s.startswith('#') or ('verify_web_rows' in s):
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'…',s)
  s=re.sub(r'(?<"'!'"\\w)\\d{2}[.,]\\d{3,}', '[coord]',s)
  print(f'{i}: {s}')
'@ | python -" in C:\git\Fire_Varna
 succeeded in 408ms:
C:/git/varna_3d/src\verify_web_rows.py

 succeeded in 575ms:
# AGENTS.md

> **Canonical current state:** [`docs/activeContext.md`](docs/activeContext.md) — the last-updated commit, the sprint status, and every live number this repo declares. If this file conflicts with `activeContext.md`, the latter wins.
>
> Read this **before** making any changes to this repo.
> Project owner: **Petar** - solo developer in Bulgaria, AI-assisted workflow, no formal CS background.
> If anything here conflicts with a user request in chat, raise the conflict; do not silently override.

---

## What This Project Is

Mobile-first **PWA for Varna fire department and a volunteer rescue squad** - locates the nearest fire hydrant via GPS.

<!-- сверка 01.09.2026: спорно, виж C:\git\plan.md приложение Е ред 13 -->

- **Primary users:** Varna firefighters (~30-50). Emergency use, on phones, often with gloves.

  <!-- непроверено (01.09.2026): няма измерим източник в репото -->

- **Secondary users:** volunteer rescue squad. Verification and feedback only; **NOT for emergency use.**
- **Distribution:** GitHub Pages from `main`, HTTPS required.
- **Language:** Bulgarian only. No localization layer. UI labels are precise and reviewed by Petar.

The app loads a static hydrant dataset, shows the user's GPS position, and guides them to the nearest hydrant.

---

## Entry Point

**Start here:** [`docs/activeContext.md`](docs/activeContext.md). It is the canonical current state of this repo — branch and HEAD, dataset counts, byte sizes, what shipped last, what is in flight. Read it before this file; on any conflict about current state it wins.

**Trunk:** `main`. It is the GitHub default (`git symbolic-ref refs/remotes/origin/HEAD` → `refs/remotes/origin/main`) and the branch the published site is served from. The other branches listed by `git branch -a` are frozen traces of past cycles; work happens on `main` only. Agents commit to `main` locally; Petar alone pushes, so `main` can sit ahead of `origin/main` between Gate 2 and the push — read `git status -sb` instead of assuming.

**What is forbidden here** is written in § Hard Constraints, § System Invariants and § When To Stop And Ask. Read those three before the first edit; they are not restated in this section.

**Live numbers live in the entry point, not here.** No state number enters this file: record counts, per-origin counts, file counts, byte sizes and commit hashes quoted as state belong in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state); a commit named as provenance (the commit of an import, of a fix) is a pointer, not state. What stays here are numbers that are rules — hard caps, intervals, thresholds (§ Hard Constraints) — and pointers into configuration, such as the Worker deploy version in § Report Flow. A figure that carries a `непроверено` marker has no measurable source in this repo; never quote it as state.

---

## Runtime Architecture

Static GitHub Pages frontend. No backend in the repo and no runtime build step.

<!-- сверка 01.09.2026: спорно, виж C:\git\plan.md приложение Е ред 26 -->

| Component | Current State |
|---|---|
| App shell | `index.html` with inlined Leaflet, MarkerCluster, CSS, and app logic |
| Hydrant data | `data/hydrants.json`, loaded by `fetch` on app init |
| Report submission | Cloudflare Worker proxy |
| Report polling | Cloudflare Worker `GET /issues`, every 15 s |
| **Frontend first load** | `index.html` + `data/hydrants.json` |

Hydrant data lives in `data/hydrants.json` (record count and per-origin counts: see [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state); the live origins are `vik`, `national`, `field_report`, `etr_varna`, `etr_provadia`, `etr_dolni_chiflik`, `etr_devnya`, `pozarna_gz`). Loaded via fetch on app init. `index.html` contains UI shell, Leaflet, MarkerCluster, app logic, and an empty `<script id="hydrantData">` placeholder populated at runtime.

Current byte sizes for `index.html`, `data/hydrants.json`, and first load are canonical in [docs/activeContext.md § Current State](docs/activeContext.md#current-state).

Local testing requires HTTP, not `file://`:

```powershell
python -m http.server 8000
```

---
C:\git\varna_3d
C:/git/varna_3d\AGENTS.md

 exited 1 in 507ms:
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "C:\Program Files\Python310\lib\pathlib.py", line 1134, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
  File "C:\Program Files\Python310\lib\pathlib.py", line 1119, in open
    return self._accessor.open(self, mode, buffering, encoding, errors,
OSError: [Errno 22] Invalid argument: 'docs\\plans\\????_???????_imot_?-?_08.09.md'

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p=next(Path('docs/plans').glob('*imot*08.09.md'))
for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
 if s.startswith('#') or 'verify_web_rows' in s:
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',s)
  s=re.sub(r'(?<"'!'"\\w)\\d{2}[.,]\\d{3,}', '[coord]',s)
  print(f'{i}: {s}')
'@ | python -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/varna_3d/AGENTS.md' -Encoding UTF8 -TotalCount 110; Get-Content -LiteralPath 'C:/git/varna_3d/src/verify_web_rows.py' -Encoding UTF8 -TotalCount 100" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
scope=[Path('index.html')]+sorted(Path('data').glob('*.json'))+sorted(Path('C:/git/varna_3d/src').rglob('*.py'))
print('INVENTORY')
for p in scope: print(p.as_posix())
print('MATCH SUMMARY')
for group,paths in [('Fire runtime',[Path('index.html')]+sorted(Path('data').glob('*.json'))),('3d src',[p for p in Path('C:/git/varna_3d/src').rglob('*') if p.is_file() and '__pycache__' not in p.parts])]:
 matched=[]
 for p in paths:
  if re.search(r'imot[._-]bg',p.read_text(encoding='utf-8',errors='ignore'),re.I): matched.append(p.as_posix())
 print(group, 'files_scanned=',len(paths), 'matching_files=',matched)
'@ | python -" in C:\git\Fire_Varna
 succeeded in 493ms:
3: # ПЛАН · Картата imot — плочката на imot.bg става кварталната карта (редакция 4)
25: ## 0 · Червени редове (без изключение)
53: ## 1 · Мярка (базата, преди един ред промяна)
55: ### 1.1 Трите репа СЕГА — `git log -1` и индексът
89: ### 1.2 Плочката (входът)
102: ### 1.3 Черновата с решенията — измерена СЕГА срещу HEAD блоба (всичко М)
120: ### 1.4 Приватностното правило върху ТОЧНИЯ обхват на гейта (М, тичано днес)
132: ### 1.5 Числата, които изпълнителят мери ПРЕДИ Gate 1 (мярката е ВХОД за подписа)
152: ## 2 · Обявени отклонения и разминавания (искат подписа на Петър)
154: ### 2.а · План ↔ ADR 011
171: ### 2.б · Отклонения от по-стари подписани/приети решения
193: ## 3 · Write-set (точните файлове, точните котви, поименно)
195: ### И-А · varna_3d + документите + данните на Петър
197: #### И-А1 · Документите (Fire_Varna)
209: #### И-А2 · Регистърът (Varna_buildings) — предложение + СОБСТВЕН лот на Петър
215: #### И-А3 · varna_3d — новият производител и новият гейт
268: #### И-А4 · `gates/probe/b3_g11.py` — трите декларирани промени (Fire_Varna, комит А-C1)
288: #### И-А5 · Каноничният файл с решенията (Fire_Varna, подписва Петър)
320: ### И-Б · Fire_Varna — доставката Б4 върху стейджнатия Б3
343: ## 4 · Ред на изпълнение
347: ### 4.0 · Общо начало
352: ### 4.А · Под-лот И-А (varna_3d + документите + данните на Петър)
371: ### 4.Б · Под-лот И-Б (Fire_Varna, доставката Б4)
387: ## 5 · Гейтове
405: ### 5.А · Гейтовете на И-А
425: ### 5.Б · Гейтовете на И-Б
445: ## 6 · Комити
478: ## 7 · STOP — лотът спира и пита
511: ## 8 · Локален преглед (ръката на Петър)
545: ## 9 · Решения за Петър (Gate 1) — 12 реда
565: ## 10 · Какво този лот НЕ пипа
587: ## Приложение А · дефект → къде е поправен (за одитора)
646: ## Приложение Б · измерената таблица на падащите клонове (какво точно би ударила плочката)
650: ### Б.1 · `varna_3d/src/build_quarters_signed.py` — клоновете, които входът imot би ударил
685: ### Б.2 · `varna_3d/src/qa_quarters_signed.py` — проверките и съдбата им в новия гейт
711: ### Б.3 · Останалите файлове (мерено)

 succeeded in 498ms:
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
# -*- coding: utf-8 -*-
"""A5 step 3 (ПЛАН_търговско-обществени.md §3 Р7, §7 А5) — the machine that
does not believe Sol.

Reads the markdown table out of `scratch/refactor/_pubbldg/plan/sol_batch1/sol_reply.md`,
OPENS every URL it carries, and writes into `data/raw_web_places.json` only the
rows where the page itself says the name. Everything else goes to `_board` with
the reason written out.

THE RULES, each a line of the plan:

  * Р1/Р7: the name enters only from an OFFICIAL site, with URL + date in
    `name_src`. Nothing from memory, nothing from an aggregator.
  * K1.4: `OFFICIAL_HOSTS` is NOT re-typed here — it is read out of
    `web/index.html` (the 3D card already owns that list). A host outside the
    list is allowed only because Sol presents it as the official page of the
    organisation; such a row is flagged `host_unlisted` and loses confidence.
  * K4.1: "ЕТ", "д-р", "адв.", "нотариус" and personal names never enter
    automatically — the row goes to the board for Petar's word.
  * §6 PII: no phone, no e-mail, anywhere — not in the file, not in the cache.
    The cache therefore keeps a SCRUBBED text fingerprint of the page plus the
    sha256 of the raw bytes and the date, never the raw HTML.
  * The name that is written is the one ON THE PAGE (verbatim span), not the
    one Sol typed; Sol only points.
  * Satellite link: at most one request per second, every page cached on disk,
    User-Agent carries the name of the project.

  Amendment No. 1: the output is a FILE. `build_places.py` is not run, nothing
  is exported.

    PYTHONIOENCODING=utf-8 python src/verify_web_rows.py
    PYTHONIOENCODING=utf-8 python src/verify_web_rows.py --offline  (cache only)
"""
from __future__ import annotations

import hashlib
import html as htmlmod
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from datetime import date, datetime
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCHDIR = os.path.join(ROOT, "scratch", "refactor", "_pubbldg", "plan", "sol_batch1")
BATCH = os.path.join(BATCHDIR, "batch.json")
REPLY = os.path.join(BATCHDIR, "sol_reply.md")
CACHE = os.path.join(BATCHDIR, "cache")
INDEX_HTML = os.path.join(ROOT, "web", "index.html")
KIND_MAP = os.path.join(ROOT, "data", "osm_kind_map.json")
PLACES = os.path.join(ROOT, "data", "places.json")
OSM_PLACES = os.path.join(ROOT, "data", "raw_public_osm_places.json")
WD_PLACES = os.path.join(ROOT, "data", "raw_wikidata_places.json")
OUT = os.path.join(ROOT, "data", "raw_web_places.json")

UA = "varna_3d-place-verifier/1.0 (fire map of Varna; one request per second)"
RATE_S = 1.1          # satellite link: at most one request per second
TIMEOUT_S = 30
N_BODIES = 80497
BBOX = (27.65, 43.13, 28.10, 43.35)   # lon_min, lat_min, lon_max, lat_max

CAD_RE = re.compile(r"\b[0-9]{4,5}\.[0-9]+\.[0-9]+")
# MEASURED, not assumed: the pages of the state tourist register carry cadastral
# identifiers in their address column (5 of them came down with batch 1). So the
# cache scrubber masks them by the rule of README §3 BEFORE anything is written
# to disk. The first version of the scrubber ate them only by accident, because
# its telephone rule was so loose that it swallowed the identifier as a phone
# number — an accident is not a gate. (No digits in this comment: a cadastral
# example written out would fail the gate this file exists to keep.)
CAD_MASK_RE = re.compile(r"\b(\d{4,5})\.\d+\.\d+(?:\.\d+)*")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# A telephone — not a date and not a float. Measured on the 5.7 MB transcript of
# Sol: the first draft (a dot allowed as a separator, no lookbehind) called 264
# strings a telephone and every one of them was "0.6999999880" or "01.09.2026".
# So: the run must START a token, the national form does not take a dot as a
# separator, and at least 8 digits must stand in it. Written down here so the
# next reader does not put the dot back.
PHONE_RE = re.compile(r"(?<![\d\w])(?:\+359|00359)[ \t\-().]*(?:\d[ \t\-().]*){6,}\d"
                      r"|(?<![\d\w.])0(?:[ \t\-()]*\d){7,}")
DIGIT_RUN_RE = re.compile(r"\d{7,}")
# The broad rule, used ONLY by the scrubber that writes the cache (see scrub_pii).
SCRUB_PHONE_RE = re.compile(r"(?<![\d\w])(?:\+359|00359|0)(?:[ \t\-().]*\d){6,}")
# K4.1 — never automatic; the board asks Petar row by row.
PERSON_RE = re.compile(r"(?:^|[^\wа-яА-Я])(ЕТ|Е\.Т\.|д-р|Д-р|ДР\.|адв\.|Адв\.|нотариус|Нотариус)(?:[^\wа-яА-Я]|$)")

# Domains the plan forbids as a source of a name (§1 of the plan). Matched on
# whole labels (host == d or host endswith "." + d), never as a substring —
# "x.com" must not condemn "lux.com".
DENY_DOMAINS = ("google.com", "google.bg", "goo.gl", "facebook.com", "fb.com",
                "instagram.com", "tiktok.com", "yandex.ru", "yandex.com",
                "foursquare.com", "tripadvisor.com", "tripadvisor.co.uk",
                "booking.com", "expedia.com", "openstreetmap.org", "osm.org",
                "wikipedia.org", "wikidata.org", "wikimedia.org", "yelp.com",

 succeeded in 751ms:
INVENTORY
index.html
data/address_rows.json
data/approx_addresses_v1.json
data/generation_manifest.json
data/hotels.json
data/hydrants.json
data/hydrants.json.pre_address_backfill.json
data/hydrants.json.pre_cleanup_snapshot.json
data/hydrants_provenance.json
data/hydrants_provenance.json.pre_address_backfill.json
data/place_categories.json
data/places.json
data/removed_hydrants.json
data/search_index.json
data/signed_facts.json
C:/git/varna_3d/src/apply_health_edu.py
C:/git/varna_3d/src/apply_hotels.py
C:/git/varna_3d/src/apply_hotels_kais.py
C:/git/varna_3d/src/apply_landmarks.py
C:/git/varna_3d/src/apply_ntr_zhr.py
C:/git/varna_3d/src/apply_official.py
C:/git/varna_3d/src/apply_public_osm.py
C:/git/varna_3d/src/apply_shops.py
C:/git/varna_3d/src/apply_wikidata.py
C:/git/varna_3d/src/apply_zones.py
C:/git/varna_3d/src/bridge_mesh.py
C:/git/varna_3d/src/build_bridge.py
C:/git/varna_3d/src/build_bridge_system.py
C:/git/varna_3d/src/build_carriageways.py
C:/git/varna_3d/src/build_d1_volumes.py
C:/git/varna_3d/src/build_landcover.py
C:/git/varna_3d/src/build_lod1.py
C:/git/varna_3d/src/build_place_aliases.py
C:/git/varna_3d/src/build_place_categories.py
C:/git/varna_3d/src/build_places.py
C:/git/varna_3d/src/build_places_board.py
C:/git/varna_3d/src/build_poi_names.py
C:/git/varna_3d/src/build_public_buildings_board.py
C:/git/varna_3d/src/build_public_buildings_geojson.py
C:/git/varna_3d/src/build_quarters_candidate.py
C:/git/varna_3d/src/build_quarters_signed.py
C:/git/varna_3d/src/build_section_bodies.py
C:/git/varna_3d/src/build_sections.py
C:/git/varna_3d/src/build_street_labels.py
C:/git/varna_3d/src/build_tail_sections.py
C:/git/varna_3d/src/build_terrain.py
C:/git/varna_3d/src/building_spec.py
C:/git/varna_3d/src/dwelling_units.py
C:/git/varna_3d/src/export_entrances_web.py
C:/git/varna_3d/src/export_fire_varna_hotels.py
C:/git/varna_3d/src/export_fire_varna_places.py
C:/git/varna_3d/src/export_relief_tiles.py
C:/git/varna_3d/src/export_terrain_tiles.py
C:/git/varna_3d/src/export_units_web.py
C:/git/varna_3d/src/export_web.py
C:/git/varna_3d/src/fetch_kais_opendata.py
C:/git/varna_3d/src/fetch_ntr_zhr.py
C:/git/varna_3d/src/fetch_wikidata_varna.py
C:/git/varna_3d/src/fire_varna_locations.py
C:/git/varna_3d/src/func_classes.py
C:/git/varna_3d/src/gen_archive.py
C:/git/varna_3d/src/gen_bridge.py
C:/git/varna_3d/src/gen_promote.py
C:/git/varna_3d/src/gen_rekey.py
C:/git/varna_3d/src/generation.py
C:/git/varna_3d/src/kais_adjpart.py
C:/git/varna_3d/src/kais_rules.py
C:/git/varna_3d/src/lot1v_v_manifest.py
C:/git/varna_3d/src/make_door_check.py
C:/git/varna_3d/src/make_door_review.py
C:/git/varna_3d/src/make_sol_batch.py
C:/git/varna_3d/src/measure_kais_quar_vs_polygons.py
C:/git/varna_3d/src/measure_place_coords.py
C:/git/varna_3d/src/measure_polygon_assign.py
C:/git/varna_3d/src/osm_footways.py
C:/git/varna_3d/src/osm_public_features.py
C:/git/varna_3d/src/osm_witness.py
C:/git/varna_3d/src/place_addresses.py
C:/git/varna_3d/src/place_identity.py
C:/git/varna_3d/src/place_zones.py
C:/git/varna_3d/src/places_registry_rows.py
C:/git/varna_3d/src/qa_apartments_coverage.py
C:/git/varna_3d/src/qa_audit_extraction.py
C:/git/varna_3d/src/qa_blocks.py
C:/git/varna_3d/src/qa_bodies.py
C:/git/varna_3d/src/qa_bridge_vs_terrain.py
C:/git/varna_3d/src/qa_building_info.py
C:/git/varna_3d/src/qa_compare_kais_versions.py
C:/git/varna_3d/src/qa_core_template.py
C:/git/varna_3d/src/qa_d1.py
C:/git/varna_3d/src/qa_door_check.py
C:/git/varna_3d/src/qa_door_review.py
C:/git/varna_3d/src/qa_entrance_gable.py
C:/git/varna_3d/src/qa_entrance_holes.py
C:/git/varna_3d/src/qa_entrance_known.py
C:/git/varna_3d/src/qa_entrance_nav.py
C:/git/varna_3d/src/qa_entrance_north.py
C:/git/varna_3d/src/qa_entrance_order.py
C:/git/varna_3d/src/qa_entrance_position.py
C:/git/varna_3d/src/qa_entrance_shape.py
C:/git/varna_3d/src/qa_entrance_siblings.py
C:/git/varna_3d/src/qa_entrance_underground.py
C:/git/varna_3d/src/qa_fire_varna_export.py
C:/git/varna_3d/src/qa_fire_varna_location_isolation.py
C:/git/varna_3d/src/qa_fire_varna_m6.py
C:/git/varna_3d/src/qa_fire_varna_places_export.py
C:/git/varna_3d/src/qa_fixed_point.py
C:/git/varna_3d/src/qa_floorfix_gain.py
C:/git/varna_3d/src/qa_floors_vs_units.py
C:/git/varna_3d/src/qa_footway_witness.py
C:/git/varna_3d/src/qa_generation.py
C:/git/varna_3d/src/qa_generation_parity.py
C:/git/varna_3d/src/qa_google_endpoints.py
C:/git/varna_3d/src/qa_ground_units.py
C:/git/varna_3d/src/qa_height_vs_dsm.py
C:/git/varna_3d/src/qa_heights_calibration.py
C:/git/varna_3d/src/qa_heights_published.py
C:/git/varna_3d/src/qa_identity_refresh.py
C:/git/varna_3d/src/qa_identity_rekey.py
C:/git/varna_3d/src/qa_insolation.py
C:/git/varna_3d/src/qa_no_cad_ids.py
C:/git/varna_3d/src/qa_no_extrude.py
C:/git/varna_3d/src/qa_opposite_terrace.py
C:/git/varna_3d/src/qa_osm_heights.py
C:/git/varna_3d/src/qa_p8a.py
C:/git/varna_3d/src/qa_place_aliases.py
C:/git/varna_3d/src/qa_place_bodies.py
C:/git/varna_3d/src/qa_place_identity_coords.py
C:/git/varna_3d/src/qa_place_sites.py
C:/git/varna_3d/src/qa_place_zone_aliases.py
C:/git/varna_3d/src/qa_places.py
C:/git/varna_3d/src/qa_podium_cores.py
C:/git/varna_3d/src/qa_poi_names.py
C:/git/varna_3d/src/qa_protrusion.py
C:/git/varna_3d/src/qa_quarters_candidate.py
C:/git/varna_3d/src/qa_quarters_license.py
C:/git/varna_3d/src/qa_quarters_signed.py
C:/git/varna_3d/src/qa_readonly_ast.py
C:/git/varna_3d/src/qa_road_modes.py
C:/git/varna_3d/src/qa_section_depth.py
C:/git/varna_3d/src/qa_sections.py
C:/git/varna_3d/src/qa_side_vs_point.py
C:/git/varna_3d/src/qa_slope_entrance.py
C:/git/varna_3d/src/qa_spec_vs_osm.py
C:/git/varna_3d/src/qa_stairwell_from_flats.py
C:/git/varna_3d/src/qa_storey_height_test.py
C:/git/varna_3d/src/qa_street_labels.py
C:/git/varna_3d/src/qa_terrain_ground.py
C:/git/varna_3d/src/qa_unit_area.py
C:/git/varna_3d/src/qa_units_by_entrance.py
C:/git/varna_3d/src/qa_vb_join.py
C:/git/varna_3d/src/qa_who_is_wrong_floors.py
C:/git/varna_3d/src/qa_why_placeholder.py
C:/git/varna_3d/src/registry_names.py
C:/git/varna_3d/src/scrub_cad_ids.py
C:/git/varna_3d/src/section_zones.py
C:/git/varna_3d/src/source_stamp.py
C:/git/varna_3d/src/storey_heights.py
C:/git/varna_3d/src/tail_rules.py
C:/git/varna_3d/src/terrain.py
C:/git/varna_3d/src/vb_attributes.py
C:/git/varna_3d/src/verify_web_rows.py
MATCH SUMMARY
Fire runtime files_scanned= 15 matching_files= []
3d src files_scanned= 147 matching_files= ['C:/git/varna_3d/src/verify_web_rows.py']

codex
Първата проверка намира 0 споменавания на imot.bg в посочените runtime файлове на Fire_Varna и само стария `verify_web_rows.py` във `varna_3d/src`. Има обаче разминаване с описанието на плана: локалният файл е „редакция 4“ и още съдържа старо име на снимката; проверявам дали това блокира началните стъпки.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p=next(Path('docs/plans').glob('*imot*08.09.md'))
print('FILE',p)
for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
 if 1<=i<=150:
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',s)
  s=re.sub(r'(?<"'!'"\\w)\\d{2}[.,]\\d{2,}', '[coord]',s)
  print(f'{i}: {s}')
'@ | python -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p=Path('C:/git/varna_3d/src/verify_web_rows.py')
a=p.read_text(encoding='utf-8').splitlines()
for i,s in enumerate(a,1):
 if 'imot' in s.lower():
  for j in range(max(0,i-7),min(len(a),i+3)):
   print(f'{j+1}: {a[j]}')
p=Path('C:/git/varna_3d/docs/activeContext.md')
print('ENTRY_EXISTS',p.exists())
if p.exists():
 for i,s in enumerate(p.read_text(encoding='utf-8').splitlines()[:70],1):
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',s)
  s=re.sub(r'(?<"'!'"\\w)\\d{2}[.,]\\d{2,}', '[coord]',s)
  print(f'{i}: {s}')
'@ | python -" in C:\git\Fire_Varna
 succeeded in 493ms:
FILE docs\plans\ПЛАН_Картата_imot_08.09.md
1: > **СТАТУС ([coord] нощ, Claude Architect):** ЧЕРНОВА v4 на ОБЩИЯ план — оборена НЕГОДНО от опровергателите (виж `scratch/places_search/karta_imot_plan_reviews_08.09.md`). ЗАМЕНЕНА от подлотовете: **И-А** = `docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` (varna_3d + документи), **И-Б** = Fire_Varna Б4 (следва). Пази се като предшественик (Приложение Б: измерените падащи клонове на стария строител). Не се подписва и не се изпълнява.
2: 
3: # ПЛАН · Картата imot — плочката на imot.bg става кварталната карта (редакция 4)
4: 
5: **Дата:** [coord].2026 · **Планер:** Claude Planner (read-only, без запис) · **Статус:** ЧЕРНОВА v4 — чака Gate 1 (подпис на Петър)
6: **Файл:** `C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_08.09.md`
7: **Заменя:** v1, v2 и **v3 — и трите оборени НЕГОДНО** (общо 6 рецензентски кръга; всички измерени дефекти са в `scratch/places_search/karta_imot_plan_reviews_08.09.md`). Картата „дефект → къде е поправен“ е **Приложение А**; измерената таблица на падащите клонове на билдъра/гейта е **Приложение Б**.
8: **Канон на решенията:** `docs/decisions/011_kartata_imot.md` (ADR 011, чернова, комитната `ab7219a`). Планът ИЗПЪЛНЯВА ADR 011; всяко разминаване е ред Р-А в §2 и го решава Петър.
9: **Основание (дословно, Петър, [coord], `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:164`):** „страхотна е !!!!! ТОВА Е НАШАТА КАРТА — ДАВАЙ ДА ИМПЛЕМЕНТИРАМЕ“ · „СТАРИТЕ ПОПРАВКИ НЕ ВАЖАТ … ИСКАМ ДА ВКАРАМЕ И РЕД ЗА ДА НЕ СЕ БЪРКАМЕ“.
10: 
11: **Клас на риска: 🔴 АРХИТЕКТУРЕН.** Спусъци: нов извор на геометрия в производствената верига · необратима канонична мутация (`quarters_signed.geojson` v1 → v2) · отмяна на подписан набор Б1 · кръстосан blast radius по D13 през трите репа · веригата към публикуване.
12: **Топология: Вариант А** — планер → **подпис на Петър (Gate 1)** → изпълнител → одитор (друг агент, read-only) → преглед на диф (Gate 2) → пуш от Петър.
13: 
14: > **Какво е различното в v4 (същината на трите оборвания).**
15: > 1. **Write-set-ът на varna_3d вече е ИЗЧЕРПАТЕЛЕН, защото е ИЗМЕРЕН, не обещан.** Всеки падащ клон, който плочката би ударила, е изброен поименно с файл:ред в **Приложение Б** — 17 клона в билдъра и 21 групи в гейта, плюс два `die()` в резолвера, които нито един предишен план не назова (`fire_varna_locations.py:94` пинът на sha, `:601-618` затворената таблица за атрибуция).
16: > 2. **Билдърът на Б1 не се адаптира — той е нерентабилен за адаптация и това е доказано с редове.** Ражда се НОВ `src/build_quarters_signed_imot.py` със СЪЩАТА изходна схема, и нов гейт `src/qa_quarters_signed_imot.py`. Доводът е в §3 И-А3 и в Приложение Б, колона „защо не се адаптира“.
17: > 3. **Лотът е разцепен на ДВА независимо изпълними и независимо подписвани под-лота: И-А и И-Б.** И-Б не тръгва, преди Петър да е комитнал И-А.
18: > 4. **Нито един гейт вече не вика несъществуващ скрипт или несъществуващ флаг.** Всеки гейт в §5 сочи или файл, който днес съществува (мерено), или файл, който конкретен комит в §6 създава.
19: > 5. **Отрицателните половини на гейтовете, които четат git блобове, се строят в еднократно `git worktree`** — точно както вече е построено в `scratch/places_search/qa_night_pins.py:400-446`. Никакъв `git stash`, никаква редакция на реалното дърво.
20: >
21: > **Произход на числата.** **(Ч)** = прочетено от назован файл:ред. **(М)** = измерено с показаната команда в тази сесия, [coord]. Няма трета категория. Всяко (М) долу е тичало.
22: 
23: ---
24: 
25: ## 0 · Червени редове (без изключение)
26: 
27: Наследени от `docs/plans/ПЛАН_Б3_07.09.md:13-33` и ADR 010:
28: 
29: 1. **Агентите не пушат** — с никакъв флаг, без `--no-verify`, без remote операция.
30: 2. **Нула КВАРТАЛНА ГЕОМЕТРИЯ в проследен файл на Fire_Varna.** Забранени са пръстени и координати на полигон. Котвата е **ADR 010 D3** (`010_signed_quarter_boundaries.md:42`, Ч): „публикува се само `quarter: {name, code, src}` и изведеният `zone`; геометрия никога“.
31: 3. **G29 СЪЩЕСТВУВА и остава в сила.** Мерено: дефиниран е в `docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:107` (Ч, дословно: „**G29 · игнорирането (нов).** `git check-ignore -v` за точните пътища + `git ls-files scratch/boundary_gallery` = 0, преди всеки пуш на Fire_Varna; отрицателна фикстура: нарочно проследен файл с геометрия“) и е **ПОСТРОЕН** в проследения `scratch/places_search/qa_night_pins.py` (`check_ignore` `:206`, `G29` `:229-242`, `--worktree-negative` `:400-446`), а `varna_3d/src/build_quarters_signed.py:1423` го цитира в `_meta.publication` (Ч). **v3 щеше да го изтрие от ADR 011 — това се отменя (Р-А1).** G29 е единственият построен гейт, който пази `scratch/boundary_gallery/` непроследена, а точно там живее целият частен вход на този лот.
32: 4. **`Varna_buildings/config/quarter_registry.json` не се пипа от агент** (ADR 010 D14; `Varna_buildings/js/lib_quarter_registry.mjs:45`).
33: 5. **Написан квартал не се променя** (ADR 010 D18, `010:72`, Ч). Гейтът му (ADR 010 G17) **не е построен** — този лот го строи (§3 И-А3.6).
34: 6. **Малки, обратими комити, изчерпателен write-set, дословно съобщение;** `git commit -- <изрични пътища>` винаги. **Забранени в целия лот:** `git add -A`, `git add .`, `git stash`, `git checkout -- .`, `git reset`, `git mv` върху път, който е само в индекса.
35: 7. **Данните, подписите, геометрията и регистърът чакат комит на `Petar1984`** (ADR 010 D16, `010:68`, Ч). Отклонението за кода в атомния комит е Р12.
36: 8. **Всеки гейт е команда с изход ≠ 0, чиято отрицателна половина е СЧУПЕН ВХОД.** Никога сменен праг. **Гейт, чиято команда не може да върне ≠ 0, не е гейт.**
37: 9. **Гейт, който чете git блоб, се чупи в еднократно `git worktree`, не в „копие във временна папка“.** Мерено защо: `gates/probe/b3_g11.py:34` (докстринг, Ч) „nothing reads the working tree any more“, а `blob()` `:55-63` прави `git show :<път>` / `git show HEAD:<път>`; `gates/release.py:437-458` (`queues_in_head`) чете `git ls-tree` на РЕАЛНОТО репо през `REPO_ROOT`. Копие във временна папка е невидимо и за двата. Точната механика е в §5 „Как се чупи вход“.
38: 10. **Само Opus; одиторът е друг агент** (read-only).
39: 11. **Кръстосаната изолация е еднопосочна:** от Fire_Varna се ЧЕТЕ блоб на varna_3d (`git -C ../varna_3d show <rev>:<път>`). Нищо не се пише в чуждо репо от сесия на друго репо.
40: 12. **Точно ЕДНА опашка `ЗА_ПОДПИС_*.md` в HEAD и точно ЕДИН json в `gates/allow/`.** Мерено: `queues_in_head` чете `git ls-tree -r` и глобва по **basename** (`gates/release.py:449-458`, Ч) → подпапка НЕ спасява; спасява само изнасяне извън `QUEUE_DIR = "scratch/places_search"` (`:171`).
41: 13. **`recall_sweep.py --manifest` ПРЕЗАПИСВА `expectations.json`.** Доказателство се снема САМО от ПЪРВИЯ прогон.
42: 14. **Отменено ≠ изтрито.** Всеки отменен артефакт се архивира с проследима следа и ред в регистъра (ADR 011 И-D5). Подписано тяло НИКОГА не се редактира на място — единствената разрешена редакция е един ред статус отгоре.
43: 15. **Частният провенанс НЕ влиза в проследен файл на Fire_Varna:** `advert_id`, `raw_response_sha256`, `points`, суровите отговори, всяка координата. Мерено на днешния HEAD блоб: черновата носи **0** координатоподобни float-а (граници `[coord]–[coord]` / `[coord]–[coord]`, `build_quarters_candidate.py:62-63`, Ч), **0** кадастрални идентификатора (`CAD_ID = re.compile(r"\b\d{4,5}\.\d+\.\d+")`, `qa_quarters_signed.py:81`, Ч), **0** `wm_polygon_sha256` (М). Числото на v3 „0 попадения на `provenance|raw_sha|advert`“ **е невярно**: `n_adverts` стои на всичките 98 реда → `grep -c 'provenance\|raw_sha\|advert'` = **98** (М). Правилото се формулира по СТРУКТУРА и по забранени КЛЮЧОВЕ, никога по субниз (§3 И-А4).
44: 16. **Всяка команда на агент е локална.** Никакъв `gh`, `curl`, никакво ново теглене от imot.bg — снапшотът [coord] е замразен вход.
45: 17. **„Картата“ = плочката, която РЕШАВА думата.** Този лот не слага нов слой в `index.html`; геометрията не се публикува.
46: 18. **Лицензът е техническо поле, не тема** (Петър, `~/.claude` памет „no licence talk“). Стойностите се ПОПЪЛВАТ от изпълнителя по публикуваните общи условия и се проверяват от гейт; в опашката влиза един ред клас „въпрос“ с `тяло: <sha на блока>`. Не се води лицензен разговор с Петър.
47: 19. **Загубите имат подписан ТАВАН, измерен ПРЕДИ подписа.**
48: 20. **Никой агент не пише allow-файл с подписа на Петър.** Изпълнителят пише реда с `signed_by: "pending — Петър"`. Мерено защо това е ЧЕСТНО, а не заобикаляне: `gates/coverage.py:104` (Ч) `return isinstance(signed_by, str) and signed_by.strip() == SIGNER`, `SIGNER = "Петър"` (`:87`, Ч); докстрингът `:41-43` изрично помни, че „Петър — pending, НЕ подписвам“ **вече е било прието за подпис** и това е поправено. Значи allow с `"pending — Петър"` дава **изход 5** („жълто — блокира като червено“, `:64`, Ч) — фейл-клоузд по конструкция, докато ръката на Петър не смени полето в СВОЙ комит.
49: 21. **Редът D13 се спазва: регистърът е ПЪРВИ.** Мерено: `qa_quarters_signed.py:341-343` и `:338-340` (Ч) нямат врата за код извън регистъра и за жилищен код без ред.
50: 
51: ---
52: 
53: ## 1 · Мярка (базата, преди един ред промяна)
54: 
55: ### 1.1 Трите репа СЕГА — `git log -1` и индексът
56: 
57: | факт | стойност | произход |
58: |---|---|---|
59: | **Fire_Varna HEAD** | `5537ce4` = `5537ce401b01554cdd33b01ad2d33a1cf899fd91`, `Claude Architect <architect@local>`, „docs: decisions draft — strip the private provenance prefixes…“ | **М** `git log -1 --pretty='%h %H %an <%ae> %s'` |
60: | ahead от `origin/main` | **134** | **М** `git rev-list --count origin/main..HEAD` |
61: | предходните два | `ab7219a` = ADR 011 + банер + §20; `3e55139` = черновата с решенията | Ч (`.git/logs/refs/heads/main`) |
62: | **стейджнати пътища** | **14**, статусите долу | **М** `git diff --cached --name-status` |
63: | опашки в HEAD | **една**: `scratch/places_search/ЗА_ПОДПИС_A.md` | **М** `git ls-tree -r --name-only HEAD \| grep ЗА_ПОДПИС` |
64: | allow-файлове | **един**: `gates/allow/2026-09-05_lot1v_v.json` | **М** `ls gates/allow/` |
65: | нови непроследени | `docs/plans/ПЛАН_Картата_imot_08.09.md`, `scratch/places_search/karta_imot_plan_reviews_08.09.md` и др. (`??`) | **М** `git status --porcelain` |
66: | `gates/probe/b3_g11.py` днес | `{"scope": 19, "geo_hits": [], "unreadable": [], "stray_new": []}` · **изход 0** | **М** `python gates/probe/b3_g11.py HEAD --cached` |
67: | **varna_3d HEAD** | `05f485e` `Petar1984` „data: p8a quarter assignment ledger [coord]“, клон **`rezhimi`** | **М** `git -C ../varna_3d log -1`, `symbolic-ref --short HEAD` |
68: | **регистърът** | `Varna_buildings/config/quarter_registry.json` — **84** записа, `schema_version 1.1`, **13** вида: `с.о. 20 · кв 18 · жк 11 · местност 12 · м-т 10 · кк 3 · зона 2 · пз 2 · мр 2 · со 1 · махала 1 · парк 1 · вз 1` — **няма „село“, няма „обект“** | **М** (python над `entries`) |
69: 
70: **14-те стейджнати пътя и комитът, който има право да смени OID-а им** (това е ЕДИНСТВЕНАТА котва; вж. §6 и STOP 7):
71: 
72: | # | път | статус | сменя се в |
73: |---|---|---|---|
74: | 1 | `data/hotels.json` | M | **Б-C4** |
75: | 2 | `data/place_categories.json` | M | **Б-C4** |
76: | 3 | `data/places.json` | M | **Б-C4** |
77: | 4 | **`gates/probe/b3_g11.py`** | A | **А-C1** ← единственото ранно изключение, §2 О12 |
78: | 5 | `index.html` | M | **Б-C4** |
79: | 6 | `scratch/places_search/granitsi_fixtures_06.09.json` | **D** | **Б-C4** |
80: | 7 | `scratch/places_search/granitsi_fixtures_07.09.json` | A | **Б-C4** |
81: | 8 | `scratch/places_search/probe_places_fv.mjs` | M | **Б-C4** |
82: | 9 | `scratch/places_search/recall_sweep.py` | M | **Б-C4** |
83: | 10 | `tests/granitsi_client_probe.mjs` | A | **Б-C4** |
84: | 11 | `tests/test_b3_gates.py` | A | **Б-C4** |
85: | 12 | `tests/test_granitsi_fixtures.py` | M | **Б-C4** |
86: | 13 | `tests/test_hotels_public_bundle.py` | M | **Б-C4** |
87: | 14 | `tests/test_places_public_bundle.py` | M | **Б-C4** |
88: 
89: ### 1.2 Плочката (входът)
90: 
91: | факт | стойност | произход |
92: |---|---|---|
93: | файл с полигоните | `scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson` (**игнорирана папка, пазена от G29**) | Ч (`СЪСТОЯНИЕ:144`) |
94: | полигони / речник | **95** от **98** речникови района | Ч (`СЪСТОЯНИЕ:144`; ADR 011 `:9`) |
95: | без полигон | Електроразпределение Варна 5848 · Малка Чайка 6294 · Северна промишлена зона 5866 | Ч (черновата) |
96: | качество | 0 застъпвания, споделени върхове, всички валидни преди поправка, [coord] km², ~40 върха средно | Ч (`СЪСТОЯНИЕ:144`) — **преизмерва се от А-G1/А-G2** |
97: | покритие на ПЛОЧКАТА | 78 236 от 80 510 (97,2 %); вън 2 274 | Ч (`СЪСТОЯНИЕ:155`), възпроизведено от рецензент (М-о) |
98: | **покритие на ДОСТАВКАТА** | **различно** — ~**77 211 / 3 299 = 95,9 %** при подразбирането на Р2 | М-о (рецензент); **преизмерва се задължително**, §1.5 т. 5 |
99: | подписаните 60 днес (v1) | 68 314 / 80 510 (84,9 %), 61,7 km² | Ч (`СЪСТОЯНИЕ:155`) |
100: | ефект от замяната | 18 280 от 68 314 точки (27 %) сменят думата | Ч (`СЪСТОЯНИЕ:156`) |
101: 
102: ### 1.3 Черновата с решенията — измерена СЕГА срещу HEAD блоба (всичко М)
103: 
104: Команда: `git show HEAD:scratch/places_search/imot_decisions_1_2026-09-08_draft.json` → python.
105: 
106: 1. **Върхови ключове:** `['_meta', 'virtual_parents', 'rows']`. **`rows` — не `decisions`.** А билдърът чете `decisions_doc.get("decisions")` (`build_quarters_signed.py:1063`, Ч) и гейтът `decisions_doc.get("decisions", [])` (`qa_quarters_signed.py:429`, Ч).
107: 2. **98 реда, 14 ключа на ред:** `raion_num · imot_name · slug · code · code_src · kind · cls · district_agkk · parent · include · n_adverts · buildings · area_km2 · n_pts`.
108: 3. **`include`:** `да` **79** · `решение` **5** · `отложено (0 сгради)` **11** · `решение (няма полигон…)` **3** = 98.
109: 4. **`kind` (това е imot-видът):** `м-т 31 · район 21 · кв. 13 · ж.к./подрайон 10 · зона 7 · обект 5 · с. 5 · к.к. 4 · в.з. 2` = 9 стойности. **Нито една не е регистров вид** (регистърът има `кв, жк, кк, со, с.о., вз, м-т, местност, махала, зона, пз, парк, мр`).
110: 5. **`cls`:** `клетка 88 · обект 5 · село 5`.
111: 6. **Кръстосано `kind × include` за 79-те „да“:** `район 19 · кв. 13 · ж.к./подрайон 10 · м-т 27 · зона 5 · к.к. 4 · в.з. 1`. **Сред 79-те „да“ НЯМА нито един „обект“ и нито едно „с.“** — петте обекта са всички под `include: решение`, петте села — всички под `отложено (0 сгради)`. Това е числото, което прави препоръката на Р2/Р3 евтина.
112: 7. **Класът quarter ↔ locality на 79-те „да“ при предложеното картографиране (Р5):** `район/кв./ж.к./к.к./в.з.` → жилищен вид → **quarter: 47**; `м-т/зона` → `KIND_CLASS = locality` (`fire_varna_locations.py:156-160`, Ч) → **locality: 32**. Днес `LOCALITY_CODES` в `index.html:6332` са **5** (М). **Това е най-голямата немерена досега последица на лота** и е решение Р6.
113: 8. **`code`:** **2 × `"TBD"`** (5848 Електроразпределение Варна, 5866 Северна промишлена зона), нула други дубликати.
114: 9. **Срещу регистъра:** **44** кода от решенията НЕ съществуват в регистъра; **31** регистрови кода нямат ред; от тях **8 жилищни** (`кв/жк/кк`): `druzhba, kv_levski, mladost, rozova_dolina, sv_ivan_rilski, trakia, vazrazhdane, vladislavovo`. (v3 писа „~45“ — точното число е **44**.)
115: 10. **Няма ключ `display`.** Билдърът иска `row["display"] == entry["display"]` **И** `row["kind"] == entry["kind"]` (`:1105-1106`, Ч) → **98 × A14** при днешния файл.
116: 11. **`virtual_parents`: 5** — `kv_levski, vladislavovo, vazrazhdane, mladost, pobeda_group`. `pobeda_group` не е регистров код, а `pobeda` е imot клетка (Р8).
117: 12. **`_meta` ключове:** `what · snapshot · dictionary_n · polygons · rule · signed_by · privacy`. `rule` носи „(G23)“, `privacy` носи „(G29)“. **G29 е верен и остава** (червен ред 3); **G23 е гейт без скрипт** — `src/qa_district_official.py` не съществува (М, Glob над `varna_3d/src/qa_*.py`).
118: 13. **Приватност:** 0 координатоподобни float-а, 0 кадастрални id, 0 `wm_polygon_sha256`, 0 забранени ключове от `FORBIDDEN_DECISION_KEYS` (`build_quarters_candidate.py:67-70`, Ч: `coordinates, geometry, geom, lat, lon, latitude, longitude, bbox, center, centroid, polygon, points, ring, rings`). **`n_adverts` × 98** — безобиден брой, но `grep 'advert'` го намира.
119: 
120: ### 1.4 Приватностното правило върху ТОЧНИЯ обхват на гейта (М, тичано днес)
121: 
122: Правилото на v3 („списък от ≥ 4 числа, ИЛИ списък от списъци“), приложено върху обхвата, който `b3_g11.py` наистина строи (`inventory()` `:83-93` + `changed()` `:70-83`, обхват `:104-106`), над **19** файла:
123: 
124: | файл | указател | попадения |
125: |---|---|---|
126: | `data/address_rows.json` | `/rows` | **1** (80 510 списъка `["1", (координата в частния файл)]`) |
127: | `data/approx_addresses_v1.json` | `/rows` | **1** (8 361 списъка) |
128: | **`scratch/places_search/granitsi_fixtures_07.09.json`** | `/fixtures[i]/queries[j]/identities` | **12** (списъци от НИЗОВЕ, нула география) |
129: 
130: **Общо 3 файла, 14 попадения — не 2, както твърдеше v3.** Затова правилото в §3 И-А4 е преформулирано: **списък от ≥ 4 ЧИСЛА** (не „списък от списъци“) + рекурсия в списъци от списъци до числата. Проверено: под това правило `identities` (низове) дава **0**, а `/rows` на двата адресни пакета дава по 1 — точно двете пиннати по sha изключения.
131: 
132: ### 1.5 Числата, които изпълнителят мери ПРЕДИ Gate 1 (мярката е ВХОД за подписа)
133: 
134: Отчет: `scratch/places_search/imot_baseline_08.09.md` (нов проследен файл, комит **А-C1**).
135: 
136: 1. Повторение на §1.1 във всичките три репа + `git ls-files -s -- <14-те пътя>` (OID-ите) + `git config core.autocrlf`.
137: 2. Валидност преди поправка, застъпвания > 1 m², обща площ, брой върхове — `gates/probe/imot_tiling_check.py` (създава се, §3 И-А4).
138: 3. `sha256` (LF блоб) на файла с полигоните и на речника; каноничният и суровият дайджест **на всеки полигон** (входът за И-C4/И-C5).
139: 4. Уникалност и реалност на кодовете: 0 дубликати, 0 `"TBD"`, 0 празни.
140: 5. **Присвояване на 80 510-те точки ДВА ПЪТИ:** (а) срещу всичките 95 полигона (очаквано 78 236 / 2 274 — сверка с §1.2); (б) **срещу доставените клетки** (79 „да“ минус изключеното по Р2/Р3) → истинският сплит. **Числото (б) влиза в ADR 011 и в А-G4.**
141: 6. Регистърът: `decided − registry` (очаквано **44**), `registry − decided` (очаквано **31**), от тях жилищните (очаквано **8**, поименно).
142: 7. **ТАВАНЪТ на загубите, поименно, преди подписа.** База (М днес): `data/places.json` = **150** реда, **91** с `quarter`, **25** различни кода; `data/hotels.json` = **225** реда, **167** с `quarter`, **13** различни кода. Мери се: (1) колко реда сменят `quarter`; (2) колко губят `quarter`; (3) кои от 28-те `QUARTER_CODES` и 5-те `LOCALITY_CODES` изчезват. **Измерено предварително от планера (М):** 7 от 28 `QUARTER_CODES` и 2 от 5 `LOCALITY_CODES` нямат ред = **9 живи кода**; 4 от тях (`kv_levski, mladost, vazrazhdane, vladislavovo`) оцеляват като виртуални родители; **5 изчезват: `druzhba, sv_ivan_rilski, trakia, morska_gradina, vilite`** — от тях само `druzhba` е в седмицата на Р7, останалите **4 искат отделно „да“**.
143: 8. **D18 предварително:** колко от 201-те реда с написан квартал биха сменили кода си, срещу `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`, `<base_rev>` от `_meta.base_rev` на леджера (ADR 010 D18, `010:72`, Ч). Очаквано 0; ненулево → ред за подпис ПРЕДИ лота.
144: 9. `precision_m`: медиана и 95-и персентил на разстоянието imot-ръб ↔ АГКК ръб за официалните кодове, EPSG:32635 → нагоре до кръгло ≥ 50 (`PRECISION_FLOOR_M = 50`, `build_quarters_signed.py:127`; `EDGE_FLOOR_M = 50`, `fire_varna_locations.py:388`).
145: 10. **`quarter_attribution` — с ВЯРНАТА команда и ВЯРНИЯ обхват.** Полето е **речник по код**, не списък. Мерено днес: **в ИНДЕКСА** (стейджнатия Б3) `data/places.json._meta.quarter_attribution` = **14** реда (**13 `wikimapia` + 1 `openstreetmap`**), `data/hotels.json` = **7** (7 `wikimapia`); **в HEAD ключът изобщо ГО НЯМА** и в двата файла (М). v3 представи индекса като „днес в репото“ — поправено.
146: 11. Приватност върху днешния HEAD/индекс: прогон на новото структурно правило → **очаквани точно ДВЕ** попадения (`/rows` на двата адресни пакета) под правилото „≥ 4 числа“; различно число = СПИРАЙ.
147: 12. Трите блоба: `bytes`, `sha256`, `gzip9` от `git show`, не от диска (CRLF).
148: 13. **Новият низ за атрибуция:** `len()` и `sha256`. Мерено защо: `tests/test_b3_gates.py:171-173` (Ч) пинва `len(want) == 338` и `sha256 == c6d29d4e...` за уикимапийския низ, а низът на Р11 е ~93 знака. И двата пина се преизмерват.
149: 
150: ---

 succeeded in 480ms:
96: DENY_DOMAINS = ("google.com", "google.bg", "goo.gl", "facebook.com", "fb.com",
97:                 "instagram.com", "tiktok.com", "yandex.ru", "yandex.com",
98:                 "foursquare.com", "tripadvisor.com", "tripadvisor.co.uk",
99:                 "booking.com", "expedia.com", "openstreetmap.org", "osm.org",
100:                 "wikipedia.org", "wikidata.org", "wikimedia.org", "yelp.com",
101:                 "2gis.ru", "waze.com", "bgmaps.com", "zoom.bg", "olx.bg",
102:                 "bazar.bg", "imot.bg", "bg-mamma.com", "pinterest.com",
103:                 "linkedin.com", "youtube.com", "twitter.com", "x.com",
104:                 "mapy.cz", "here.com", "apple.com", "alle.bg", "grabo.bg",
105:                 "zapatoo.bg", "restaurantguru.com", "menu.bg", "bgmenu.com")
ENTRY_EXISTS True
1: # Varna 3D — входна точка
2: 
3: **Дата:** [coord].2026 · **последно сверено срещу комит** 9f55c08 (`rezhimi`; напред спрямо `origin/rezhimi` с комитите на плана от [coord] до пуша на Петър — таблицата) · сверил: Opus (executor), одитирал: <одитор> · подпис: __
4: > Всяко число тук е изходът на командата до него, пусната на датата горе (`verify_numbers.py` го проверява). Число без команда не влиза.
5: > Хрониката по дати е замразена в [СЪСТОЯНИЕ.md](СЪСТОЯНИЕ.md) (до [coord].2026). Изворите са описани в [../DATA.md](../DATA.md) (мерени [coord].2026).
6: 
7: ## Какво е това
8: Триизмерен модел на Варна от КАИС „Отворени данни" — стои НАД `Varna_buildings` (данните за сградите) и `Fire_Varna` (хидрантите), чете техните изходи, не ги пипа. Публикуваното е `web/` (карта: `Varna 3D.bat` → http://127.0.0.1:8791).
9: 
10: ## Стволът
11: - Работен клон: `rezhimi`. Клонът по подразбиране в GitHub: `main` (изравнен с `origin/rezhimi` в ЛОТ 3 на плана от [coord]; проследява `origin/main`; занапред — В-1/Р-12).
12: 
13: ## Тема „търговско-обществените сгради" ([coord].2026, сесия git-65 / Fable) — сурови данни във файл, нищо в картата
14: - **Състояние:** Ф0 мярка (`b8141ec`) → план v1.1 подписан по думите на Петър (`docs/plans/ПЛАН_търговско-обществени.md`, §11 амандаменти) → лотове А0/А1 (`c74bad0`, `a7f1a68`), А4 (`0ccc525`), А3 (`12b082f`), А5 + бордът (`7a4bed5`). По амандамент №1 („за сега инфото на файл") `build_places.py` НЕ е пускан, износ към Fire_Varna няма; А2/А6/Б/В чакат преценката на Петър. Докладът: [audits/ДОКЛАД_03.09_търговско-обществени.md](audits/ДОКЛАД_03.09_търговско-обществени.md); бордът: [audits/БОРД_търговско-обществени_2026-09-03.md](audits/БОРД_търговско-обществени_2026-09-03.md).
15: - **Живи числа на темата** ([coord].2026):
16: 
17: | Какво | Стойност | Команда |
18: |---|---|---|
19: | OSM места (сурови) | 1848 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_public_osm_places.json',encoding='utf-8'))['places']))"` |
20: | НТР ЗХР места (сурови) | 373 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_ntr_zhr_places.json',encoding='utf-8'))['places']))"` |
21: | Wikidata места (сурови) | 44 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_wikidata_places.json',encoding='utf-8'))['places']))"` |
22: | официални сайтове (Сол, сурови) | 5 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_web_places.json',encoding='utf-8'))['places']))"` |
23: | тела в геофайла / с име | 10367 / 1538 | `PYTHONIOENCODING=utf-8 python src/build_public_buildings_geojson.py \| grep '^bodies'` (изходът е в `output/`, извън git) |
24: | мастерът `places.json` недокоснат от темата | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |
25: 
26: ## Тема „ЛОТ 1в за Fire_Varna" ([coord].2026, сесия git-08) — имената, адресите, кварталите
27: - **Състояние:** лот А (псевдонимите с извор, `1d5ec9a`, `859dbe5`) → лот Б (адресът с извор на всеки запис, `25a6d79`) → **лот В (P6): кварталът, районът и допълнителното с извор.** Планът и подписът са на Fire_Varna: `Fire_Varna/docs/plans/ПЛАН_ЛОТ1в-В_кварталите.md` (Gate 1-В подписан, §3з); ADR `Fire_Varna/docs/decisions/008_places_aliases_and_addresses.md`. Във Fire_Varna не е пипано нищо оттук — прави се САМО артефактът.
28: - **Правилото (§3г, подписано):** кварталът е САМО жилищно ниво по регистъра на кварталите и САМО с човешки написан извор — регистровият адресен сегмент (`REG`) или кадастралният квартал на закотвеното тяло (`KAIS`); без извор → честно „район X". Районът идва САМО от КАИС `reg` (петте градски района, затворен списък). Допълнителното (`locality`) носи промишлените зони, парковете и местностите. **Нищо нарисувано и нищо OSM-производно не решава** — обвивките, етикет-точките и районният полигон са само сравнителни колони в маскирания ledger `../scratch/refactor/_addr/lot1v_locations_375.json`.
29: - **Изолация:** новата стълба (`src/fire_varna_locations.py`) е Fire-export-only. Глобалната `src/place_zones.py`, майсторът и артефактите на паралелната тема не мърдат — доказва го `src/qa_fire_varna_location_isolation.py` (G-ISO) срещу закованите входове `data/fire_varna_location_inputs.json`.
30: - **Чака подпис:** манифестът old → new (209 реда) преди замразяването на референцията във Fire_Varna; фикс-извадката за окото на Петър е в ledger-а.
31: - **Хигиена след одита на лот В (P6-б):** SHA-то на доставка се смята върху LF-нормализирани байтове — тоест е SHA-то на блоба (`git show HEAD:<път>`), не на байтовете на този диск (прясно записаният износ е CRLF, прясно изтегленият — LF); затова гейтът (g) на `qa_place_zone_aliases.py` и G-ISO отговарят еднакво в работното дърво и в чист worktree. `data/registry_manifest.json` е комитнат (22 стойности `zone` в `grandfathered`/`board_queue`; секцията `rows` е идентична с P6), затова пинът му вече сочи блоб от историята. Ledger-ът носи `_meta.fix_sample_why` (доводите се ИЗВЕЖДАТ от полетата на реда) и `_meta.open_question_map_label`: 6 реда губят квартала си по `map_label:false`, 5 от тях с човешки написан регистров сегмент (ДГ 32, ДГ 36) — за решение на Петър.
32: - **Живи числа на темата** ([coord].2026):
33: 
34: | Какво | Стойност | Команда |
35: |---|---|---|
36: | доставени записа (места + хотели) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
37: | с квартал (REG 34 · KAIS 94 · подписан override 12) | 140 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
38: | с допълнително местоположение | 8 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
39: | с район (100 % покритие, нула карантина) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
40: | сменят зона спрямо доставеното (манифестът) | 209 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| tail -1` |
41: | G-ISO: глобалната стълба и чуждата тема непокътнати | минава | `PYTHONIOENCODING=utf-8 python src/qa_fire_varna_location_isolation.py \| tail -1` |
42: | самоличности с непроменен `place_id` | 375 (0 нови) | `PYTHONIOENCODING=utf-8 python src/place_identity.py \| grep 'обекта'` |
43: 
44: ## Отворена тема (към [coord].2026, по СЪСТОЯНИЕ.md § [coord])
45: - **Секции от апартаменти v1.3** — одит ГОДНО, **чака Gate 2** върху [извадката](../scratch/refactor/_addr/ПРЕГЛЕД_извадка_секции_01.09.md) (броят места е по документа; непроверено [coord].2026); след „давай" — Ф4-сливане. Дали Gate 2 е даден след [coord]: непроверено ([coord].2026), В-2.
46: - **Входове без регистър v2.1** — подписан; [бордът](../scratch/refactor/_addr/БОРД_изведени_входове_66.md) (сгради/входове по заглавието на документа; непроверено [coord].2026) чака визуалната проверка на Петър. Непроверено след [coord] (В-2).
47: - **Римски цифри в имената** — [ПЛАН_римски_цифри.md](plans/ПЛАН_римски_цифри.md) v1.1: мярката (11/370 poi, 3/576 места, 8 в регистъра на МОН; правилото НЕ в `skel` — 1 872 адресни „и“), Сол събори v1 (4 блокера) — чака поправен план + подпис; не е изпълнявано.
48: - **Фаза 2 на местата за Fire_Varna** (училища/университети/болници/ДКЦ/хосписи/детски градини) — ИЗПЪЛНЕНА: износът `data/fire_varna_places.json` (135 места, 74 изключени поименно; ff760e3) и кварталът/районът по стълбата за местата и хотелите (ba78a25); планът v1.5 е копие на `Fire_Varna/docs/plans/places_phase2_plan.md` ([ПЛАН_фаза2_места.md](plans/ПЛАН_фаза2_места.md)); мярката на фунията в [../scratch/refactor/_addr/ФУНИЯ_фаза2_02.09.md](../scratch/refactor/_addr/ФУНИЯ_фаза2_02.09.md). Отворено за подпис (§10): П7 — кварталните псевдоними от регистъра в `data/place_categories.json` (`build_place_categories.py`, ключ `zones`); лот Д5 — 53-те общински детски градини от извадката [coord] върху КАИС-парцелите (Владиславово: 2 от поне 5 в доставката). Решенията на Петър (лицензът на регистрите, ODbL върху bundle-а, МЦ вън/вътре) — в доклада на Fire_Varna.
49: 
50: ## Чака подпис / преглед
51: - Gate 2 на секциите (горе) · визуалната проверка на входовете (горе) · непушнатите комити (числата долу) — пушът е на Петър.
52: 
53: ## Последният доклад
54: - [audits/ДОКЛАД_01.09_секции_и_входове.md](audits/ДОКЛАД_01.09_секции_и_входове.md)
55: 
56: ## Живи числа
57: | Какво | Стойност | Команда |
58: |---|---|---|
59: | комити на `rezhimi` | 469 | `git rev-list --count rezhimi` |
60: | последен пушнат комит | 1a8e170 2026-08-31 | `git log -1 --format='%h %cs' origin/rezhimi` |
61: | непушнати към `origin/rezhimi` | 15 | `git rev-list --count origin/rezhimi..rezhimi` |
62: | публикувано поколение на кадастъра | [coord].2026 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('web/varna_buildings_3d.manifest.json',encoding='utf-8'))['generation']['buildings'])"` |
63: | сгради в публикувания слой | 80497 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('web/varna_buildings_3d.manifest.json',encoding='utf-8'))['buildings'])"` |
64: | секции (3D) | 2101 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('web/varna_sections_3d.geojson',encoding='utf-8'))['features']))"` |
65: | изведени входове | 11748 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('web/varna_entrances_derived.geojson',encoding='utf-8'))['features']))"` |
66: | места (`places.json`) | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |
67: | гейт „нула кадастрални идентификатори" | минава | `PYTHONIOENCODING=utf-8 python src/qa_no_cad_ids.py \| tail -1 \| cut -d' ' -f1` |
68: 
69: > Двата реда за брой комити („комити на `rezhimi`“ и „непушнати към `origin/rezhimi`“) мърдат с +1 при всеки комит — включително този, който добавя файла; сверката е спрямо комита в ред 3 (= `git rev-parse --short HEAD~1` веднага след комита на ЛОТ 5). Затова `verify_numbers.py` върху комитнатия файл показва точно тези два реда с +1.
70: 

codex
Уточнение: „редакция 4“ е архивният предшественик, попаднал в търсенето по шаблон. Точно посоченият план И-А съществува и съдържа преименуването; предишната ми забележка за старото име не се отнася до него.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
ps=list(Path('docs/plans').glob('*imot_*-*_08.09.md'));assert len(ps)==1
p=ps[0]; print('FILE',p,'BYTES',p.stat().st_size)
for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
 if i<=130:
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',s)
  s=re.sub(r'(?<"'!'"\\w)(?:27|28|43|44)[.,]\\d{2,}', '[coord]',s)
  print(f'{i}: {s}')
'@ | python -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p=next(Path('docs/plans').glob('*imot_*-*_08.09.md'))
a=p.read_text(encoding='utf-8').splitlines()
for i,s in enumerate(a,1):
 if s.startswith('#') or 'imot.bg' in s or 'varna_polygons_08.09' in s or 'varna_dictionary_08.09' in s:
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',s)
  s=re.sub(r'(?<"'!'"\\w)(?:27|28|43|44)[.,]\\d{2,}', '[coord]',s)
  print(f'{i}: {s}')
'@ | python -" in C:\git\Fire_Varna
 succeeded in 477ms:
FILE docs\plans\ПЛАН_Картата_imot_И-А_08.09.md BYTES 227700
1: # ПЛАН · Картата imot — под-лот **И-А** (varna_3d + документи)
2: 
3: `Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` · 08.09.2026 · **редакция 4** (след шест одиторски кръга: два общи + „И-А кръг 1“, „И-А кръг 2“ и двата кръга върху редакция 3; плюс Astra S40/Кими К39 и финалните проверки, свити от Архитекта като редове ИА-О30 нататък в §2 — броят им расте и се чете там и в червен ред 10, не тук — ИА-О38) · Планировчик (Opus, само четене) → **подпис на Петър (Gate 1)** → Изпълнител → Одитор → локален преглед → **Gate 2 и пуш от Петър**
4: 
5: **Какво прави този лот.** Прави плочката на imot.bg **канонична геометрия** в частното репо `varna_3d` — замразеният вход, подписаното тяло с решенията, нов билдър, негов собствен гейт, архив на v1 — и допълва три документа във Fire_Varna. **Нищо във Fire_Varna освен тези три проследени документа и един поименно обявен ИГНОРИРАН файл за преглед не се пипа.** Живата карта, доставката Б3, `index.html`, `data/`, `tests/`, `gates/` на Fire_Varna остават непроменени и си остават работа на **И-Б**.
6: 
7: **Предшественик.** `docs/plans/ПЛАН_Картата_imot_08.09.md` (редакция 4, **проследен** — М: `git ls-files --error-unmatch` → 0, последен комит по пътя `146beac`, ред-статус „заменен от И-А/И-Б“ отгоре; байтове и редове **не се пинват** — ИА-О32/ИА-О33). Този под-лот **изпълнява** неговите §3 И-А, §5.А и Приложение Б; всяко място, където се разминава с него, е ред в §2. Планът v4 остава на диска като предшественик и **не се изтрива**.
8: 
9: Всяко число долу носи котва: **(Ч)** = `файл:ред`, **(М)** = командата, която пуснах, и изходът ѝ. Числа без котва в този план няма. Всяко число на редакция 3, което този кръг обори, е поправено ТУК с нова мярка и е назовано поименно на мястото си.
10: 
11: ---
12: 
13: ## 0 · Червени редове
14: 
15: 1. **Нищо не се редактира преди подписа.** Първата команда на Изпълнителя е `git status --porcelain`, не `Write`. **Няма изключение за `Д1` (ИА-О32):** самият този план е ВЕЧЕ проследен и комитнат от Архитекта (М: `git ls-files --error-unmatch docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` → 0; последен комит по пътя — Архитект). Подписът на Петър е думата му в чата; Архитектът (не Изпълнителят) вписва един ред-статус „подписан от Петър, <дата>, ревизия <sha>“ отгоре и го комитва като **К1**; ако Петър поиска редакции, Архитектът ги внася ПРЕДИ подписа. Изпълнителят никога не пише в `Д1`.
16: 2. **Никакъв `git push`.** Пушът е само на Петър (универсален инвариант №1).
17: 3. **Данните и геометрията ги комитва Петър** (ADR 010 D16, Ч `010_signed_quarter_boundaries.md:68`). Агентът ги оставя стейджнати с изричен pathspec.
18: 4. **Fire_Varna: САМО три ПРОСЛЕДЕНИ документа (Д1, Д2, Д3) + един поименно обявен ИГНОРИРАН файл за преглед (Д4).** Никакъв ред в `index.html`, `data/`, `tests/`, `gates/`, `scratch/places_search/*.py|*.json`. Докосване на пети път във Fire_Varna = STOP.
19: 5. **Нула квартална геометрия и нула суров провенанс в проследен файл на Fire_Varna.** Геометрията, `advert_id`, `raw_sha256`, `points` и **всяка координата** живеят само в **частното** репо `varna_3d` и в игнорираната папка на Fire_Varna (М: `git check-ignore -v scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson` → `.gitignore:64:/scratch/boundary_gallery/`). **Този план е проследен файл на Fire_Varna — затова в текста му няма нито една двойка `lat/lon`; навсякъде, където предишна редакция цитираше координата, стои „(координата в частния файл)“. Спазването се съди механично от ИА-19.** Обобщени производни (площи, брой върхове, хистограма на ръба, хешове) **не са координати** и остават позволени — обявено в ИА-О24, дългът за правило и гейт е ИБ-18.
20: 6. **Гейт, чиято команда не може да върне ≠ 0, не е гейт.** Всяка обявена отрицателна половина ТРЯБВА да е тичала и да е паднала с записан изход; „ще падне“ не е доказателство (поука `gates-lie-more-than-code`). **Ред, за който предварително се знае, че няма да падне, НЕ стои в колоната „отрицателна половина“** — той е мярка и се записва в отчета.
21: 7. **Нула регресии.** Всеки от деветте измерени изхода на **§1.2** се запазва — **със заявената в §5 команда за съответната фаза** (преди и след преместването на v1 командата е РАЗЛИЧНА; изходът е същият). Различен изход = STOP.
22: 8. **Подписано тяло не се редактира на място.** Нова версия — нов файл, стар в архива, никога `git rm`.
23: 9. **Кодът е на латиница.** Имена на модули и коментари на английски; на български остават документите и текстовете за човек (поука `code-in-english`).
24: 10. **Собствени пространства на номерата — затворени и без сблъсък по азбука.** Гейтове **ИА-1 … ИА-19**, отклонения **ИА-О1 … ИА-О40** (ИА-О25 … ИА-О29 не съществуват — номерата са прескочени, за да не се преномерират препратки; ИА-О30 … ИА-О40 са сверките на Архитекта), спирачки **ИА-STOP 1 … 18**, файлове **Ф1 … Ф10**, точкови редакции **Т1 … Т15**, разлики в подписаното тяло **Х1 … Х11**, пинове **П1 … П18**, база **Н1 … Н9**, решения **Р1 … Р21**, комити **К1 … К9**, дългове към И-Б **ИБ-1 … ИБ-20**. (М, ИА-О33: `grep -rIl "ИА-[0-9]" C:/git/Fire_Varna/docs C:/git/varna_3d/src C:/git/varna_3d/docs` → **точно два файла: този план и Д3** — `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` §20 води дневника на сверките от ИА-О30 нататък; нищо в varna_3d.) **Кръговете на опровергателите се цитират винаги с името на лещата — „Кими К37“, „Astra S40“; голо „К37“ не е комит (ИА-О33).**
25:    **Пространството `Б` НЕ се използва от този план в нито един вид.** Кръг 3 намери, че `Б1…Б15` (точкови редакции) и `Б-1…Б-16` (дългове) се различаваха само по тире, а „Б1“ и „Б3“ вече значат живи лотове в кода (М: `build_quarters_signed.py:1408` `"lot": "Б1"`, `:1563` `fail("червена черта", …лот Б1…)`, `qa_quarters_signed.py:1197` „Gate Б1“) и живата доставка Б3. Затова редакциите станаха **Т**, дълговете — **ИБ**. Никакъв `G4`, `G11`, `G15`, `G17`, `G21`, `G22`, `G23`, `G29`; никакъв гол `О7`/`О8`/`О16` — те са заети в `ПЛАН_Б3_07.09.md:240`, `:241`, `:249` (Ч), а пространството `О` там стига до **О30** (Ч `:263`). **Латинско `A` не се използва като СОБСТВЕНО пространство (`A<n>`) никъде** — цитатите на `A13`/`A14` на стария билдър и „I-A“ в съобщенията на комитите са цитати и имена, не пространство (ИА-О35).
26: 11. **Лицензът не е тема.** Дословният низ за атрибуция се **попълва** по решение Р10; не се обсъжда, не се проучва.
27: 12. **Sha на доставка = блобът.** Във Fire_Varna работното копие МОЖЕ да е ≠ блоб (CRLF); за файловете, които този лот чете, днес са равни (М, ИА-О39: `data/address_rows.json` — `eol: lf`, 0 CRLF, един и същ sha), но правилото пак е „чети блоба“. Във **varna_3d разлика няма**: `.gitattributes:4` е `* text=auto eol=lf` (Ч), М: `git check-attr -a data/quarters_signed.geojson` → `eol: lf`, и работното копие, и блобът дават `c1551d24…`, 301 917 B. Правилото пак е „чети блоба“; varna_3d просто няма как да те излъже.
28: 13. **Блоб се адресира стабилно, не през HEAD.** Навсякъде, където се чете блоб, ревизията се взема с `git -C <репо> log -1 --format=%H -- <път>` (М днес за черновата с решенията → `7556227…`; за `district_resolutions_2026-09-07.json` → `e6c706d…`; HEAD на Fire_Varna в деня на мярката беше същият `7556227` — съвпадение, което **не се ползва**; HEAD е променлив, ИА-О32). **Вход, който НЕ живее в никое git-репо, не може да се адресира по това правило и се пинва по sha256 на прочетените байтове** — това е точно случаят на слоя с петте района (Р21, ИА-О23). **ИА-О35: същото важи за всеки вход, за който Ф2 няма `--*-repo/--*-rev` флагове (`address_rows`, регистърът) — байтовете са пинът, `rev` е свидетел; блобово се сверяват само Ф7, резолюциите и диф-базата (§3.Г.7).**
29: 
30: ---
31: 
32: ## 1 · Мярка (всичко мерено 08.09; нула редакции)
33: 
34: ### 1.1 · Състояние на репата
35: 
36: | | стойност | котва |
37: |---|---|---|
38: | `varna_3d` HEAD | `05f485e` · `Petar1984` · 2026-09-07 · „data: p8a quarter assignment ledger 07.09“ | (М) `git -C C:/git/varna_3d log -1 --pretty='%h %an %ad %s' --date=short` |
39: | `varna_3d` клон | `rezhimi` | (М) `git branch --show-current` |
40: | `varna_3d` ahead от `origin/main` | **74** | (М) `git rev-list --count origin/main..HEAD` |
41: | `varna_3d` мръсни проследени | **1** — `scratch/place_bodies/qa_place_bodies.md` | (М) `git status --porcelain`, преброени редовете без `??` (без тръба в клетката — ИА-О35) |
42: | `varna_3d` непроследени | **41** | (М) `git status --porcelain`, преброени редовете с `??` (ИА-О35) |
43: | `varna_3d` `core.autocrlf` / `.gitattributes` | `true` / `* text=auto eol=lf` (Ч `:4`) → **работно копие = блоб** | (М) `git config core.autocrlf`, `git check-attr -a` |
44: | `Fire_Varna` HEAD | **ПРОМЕНЛИВА — не се пинва** (Петър приема доклади за хидранти; Архитектът комитва документи). Записва се на стъпка 0 като факт, не като очакване (ИА-О32). | (М на стъпка 0) `git log -1 --pretty='%h %an %s'` |
45: | `Fire_Varna` ahead | **ПРОМЕНЛИВА — записва се, не се пинва** (ИА-О32) | (М на стъпка 0) `git rev-list --count origin/main..HEAD` |
46: | `Fire_Varna` стейджнати пътища (Б3) | **14** (`M` places/hotels/place_categories/index.html/probe_places_fv.mjs/recall_sweep.py/test_granitsi_fixtures/test_hotels_public_bundle/test_places_public_bundle · `A` b3_g11.py/granitsi_fixtures_07.09.json/granitsi_client_probe.mjs/test_b3_gates.py · `D` granitsi_fixtures_06.09.json) | (М) `git diff --cached --name-status` |
47: | `Fire_Varna` мръсни НЕстейджнати | **записват се на стъпка 0** (ИА-О32); очаквани и допустими: `scratch/places_search/lot1v_v_reference_manifest.json`, `scratch/places_search/probe_out/token_parity.json` (мръсни нарочно от Б3), евентуално `scratch/places_search/karta_imot_plan_reviews_08.09.md`; **`docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` е ЧИСТ** (§20 е комитнат) | (М на стъпка 0) `git status --porcelain` |
48: | `Fire_Varna` приватностен гейт | `{"scope": 19, "geo_hits": [], "unreadable": [], "stray_new": []}` · **изход 0** | (М) `python gates/probe/b3_g11.py HEAD --cached` |
49: | **временни дървета (базова линия — ИА-О36)** | `Fire_Varna`: **2 чужди, допустими, не се пипат** — `C:/git/_wt/fv_lot1_client` (клон `lot1-client`) и `C:/Users/Petar/AppData/Local/Temp/claude/wt_fv` (detached, от 07.09; чужд път, не е на този лот); `varna_3d`: **0**. Записват се на стъпка 0 като БАЗОВА ЛИНИЯ; критерият на стъпка 18 е „нула НОВИ дървета спрямо нея“, не „нула дървета“ | (М) `git worktree list` в двете репа |
50: | **`Д1` на диска ДНЕС** | **ПРОСЛЕДЕН и чист** (последен комит по пътя — Архитект), заглавен ред „редакция 4“ + сверките от ИА-О30 нататък (растат с всяка проверка; последната е в червен ред 10); **0 двойки координати** (М, ИА-О33, с командата на ИА-19 в поправения ѝ вид: `grep -nE -e '\b4[23][.,][0-9]{3,}\b' -e '\b2[78][.,][0-9]{3,}\b'` → изход 1). Байтовете и броят редове **не се пинват** — Д1 расте с всяка сверка (ИА-О32) | (М на стъпка 0: `git ls-files --error-unmatch`, `git status --porcelain -- <Д1>` = празно, ИА-19 = изход 1) |
51: 
52: > Заб.: HEAD-ът на Fire_Varna мърда сам (Петър приема доклади за хидранти). **Нито един гейт и нито един STOP тук не пинва HEAD на Fire_Varna** — само блобове, адресирани по правилото на червен ред 13.
53: 
54: ### 1.2 · Базата на `varna_3d` е ЗЕЛЕНА (за разлика от Fire_Varna) — **девет реда**
55: 
56: | # | команда (М, тичана днес) | изход | какво печата |
57: |---|---|---|---|
58: | **Н1** | `python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json` | **0** | 20 проверки C1–C20; печата и „решени по подписан файл (`d494d4d256ae…`, решение 9): `kochmar→mladost`, `vazrazhdane4→mladost`“ |
59: | **Н2** | `python src/qa_p8a.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` | **0** | „присвояването по подписани граници е годно за комита на Петър“ |
60: | **Н3** | `python src/qa_fire_varna_places_export.py` | **0** | „артефактът може да тръгне към Fire_Varna“ |
61: | **Н4** | `python src/qa_place_zone_aliases.py` | **0** | „passes — every quarter alias is a verbatim string of the registry“ |
62: | **Н5** | `python src/qa_fire_varna_export.py` | **0** | „артефактът може да тръгне към Fire_Varna“ |
63: | **Н6** | `python src/qa_fire_varna_location_isolation.py` | **0** | „глобалната стълба, майсторът и чуждата тема са непокътнати“ |
64: | **Н7** | `python -m unittest discover -s tests` | **0** | „Ran **16** tests … OK“ |
65: | **Н8** | `python src/qa_fire_varna_m6.py` | **3** | „ЧАКА ПОДПИС: **8** реда с `pending_signature` — билдът е здрав, но ПУБЛИКАЦИЯ и `--freeze` са забранени“ (М: `qa_fire_varna_m6.py:41` (докстрингът) и `:489` (проверката) „блокът `pending_signature` брои същото · 8 срещу 8“) |
66: | **Н9** | `python scratch/granitsi/zone_alias_negatives.py` | **0** | харнесът на отрицателните проби на `qa_place_zone_aliases` (П13) |
67: 
68: **Изход 3 на Н8 е НАСЛЕДЕН и НЕ Е ЧЕРВЕН** (Ч `qa_fire_varna_m6.py:526` `sys.exit(3)`). Записва се като база; смяна на числото 8 = STOP.
69: 
70: **Н7 се сверява по ИМЕНА, не по брой.** Комит К4 добавя `tests/test_quarters_signed_imot_fixtures.py` — след него броят расте. Пинът е: **изход 0 И шестнайсетте днешни идентификатора са сред пуснатите, всичките зелени.** Снемат се със **стабилна** команда (не с `grep " ... ok"` — `-v` печата докстринга вместо името при 6 от 16-те, мерено):
71: 
72: ```
73: python -c "import unittest;s=unittest.defaultTestLoader.discover('tests');
74: ids=lambda t:[y for x in t for y in (ids(x) if isinstance(x,unittest.TestSuite) else [x.id()])];
75: print(chr(10).join(sorted(ids(s))))"
76: ```
77: 
78: М днес → **16 идентификатора**, всичките в `test_quarters_signed_fixtures.SignedQuartersFixtures`: `test_artifact_carries_the_signed_shape`, `test_build_refuses_a_moved_vertex_in_a_union_part`, `test_build_refuses_a_moved_vertex_in_the_frozen_set`, `test_build_refuses_a_moved_vertex_in_the_mladost2_face`, `test_build_refuses_a_resolution_against_the_au5_witness`, `test_build_refuses_a_resolution_for_a_code_without_a_dispute`, `test_build_refuses_any_other_output_name`, `test_district_disputes_are_named_and_resolved_by_the_signed_file`, `test_every_negative_fixture_actually_fails`, `test_gate_is_green_on_the_signed_artifact`, `test_gate_refuses_a_resolution_for_a_code_without_a_dispute`, `test_gate_refuses_a_resolutions_file_against_the_au5_witness`, `test_rebuild_is_byte_identical`, `test_the_resolutions_input_is_the_signed_file`, `test_the_union_is_the_geometry_petar_signed`, `test_union_recipe_is_declared_honestly`.
79: 
80: ### 1.3 · Схемата на v1 (какво трябва да възпроизведе v2, ключ по ключ)
81: 
82: Блобът: **301 917 B**, `sha256 = c1551d24...` (М).
83: 
84: - **Върхови ключове (3):** `_meta`, `features`, `type`.
85: - **`_meta` — 36 ключа** (М, поименно): `artifact_class, attribution, canonicalization, counts, d1_schema, decisions_author, decisions_based_on, decisions_blob_before_attribution, decisions_commit, decisions_path, decisions_sha256, decisions_sha256_rule, decisions_sha256_worktree, declared_deviations, district_resolutions, district_witness_agkk, district_witness_disputes, excluded, generated_by, inputs, licences, lot, method_licence, parent_child, parent_child_without_polygon, plan, precision_floor_m, precision_m_by_method, publication, registry_pending, rows_without_feature, signature, source_terms, union_crs, union_recipe, union_witness`.
86: - **Feature — 3 ключа:** `geometry`, `properties`, `type`. **`properties` — 41 ключа** (М): `approval_digest, approved_at, approved_by, attribution, basemap, chosen_reason, chosen_source, code, confirmed_at, confirmed_by, district, district_src, drawn_at, drawn_by, fetched_at, geometry_origin, imported_from, kind, license, license_label, license_terms, method, name, note, parent, parent_display, parent_geometry_check, precision_m, raw_geometry_sha256, screenshot_sha256, signed_by, source, url, version, viewport, visible_layers, witnesses, wm_id, wm_ids, wm_polygon_sha256, wm_title`.
87: - **Нулираните полета.** М поименно: **седемте** на `_meta.d1_schema.nulled_on_import` (`drawn_by, drawn_at, basemap, viewport, visible_layers, screenshot_sha256, approval_digest`) са `null` по **всичките 60**; `wm_ids` е непразно по **1**; `wm_id` — по **58**; `wm_title` — по **60**.
88: - `_meta.precision_floor_m = 50`; `_meta.artifact_class = "signed_by_plan_signature"`; `_meta.counts` = **12** полета; `_meta.licences` = **2**; **`_meta.parent_child` = 11 двойки** `{child,parent}` (М, поименно: `abatko→kk_konstantin_elena`, `druzhba→asparuhovo`, `kaisieva→vladislavovo`, `kokardzha_generic→izgrev_kv`, `mladost1→mladost`, `mladost2→mladost`, `rozova_dolina→asparuhovo`, `saltanat→morska_gradina`, `vazrazhdane1/2/3→vazrazhdane`); `properties.parent` е непразно само по **6** Feature-а (М) — **двата източника на родство НЕ съвпадат и авторитетът за родство е `_meta.parent_child`** (виж следващата точка); `_meta.parent_child_without_polygon = []`; `_meta.registry_pending` = **16**.
89: - **`_meta.rows_without_feature` на v1 има ДВЕ кофи — `alias_of` (1 ред: `vayalar → sredna_traka`) и `deferred` (6 реда)** (М, дословно). v2 ще носи същия ключ с **друг набор кофи** — това е обявено отклонение ИА-О21.
90: - **`_meta.excluded` носи ЕДИН ред** (М, дословно): `vinitsa_sever` · `display "с.о. Виница-север"` · `kind "с.о."` · `registry_action` „сутрешен ход на Петър: деактивиране на кода в `quarter_registry.json` — регистърът НЕ се пипа от изпълнителя“ · `why` „Петър (07.09): «Виница-север го изключваме» …“. **В черновата с решенията същият код е ред 6295 с `include = "да"` и `kind_registry = "вз"`, 294 сгради, 0,303 km² (М) — тоест v2 го връща. Обратът е решение Р17 и се записва, не се премълчава** (ИА-О15).
91: - **Геометрия:** 60 × `Polygon`. **Площ (М, EPSG:32635):** сбор **66,886 km²**, обединение **61,597 km²**, **51 застъпващи се двойки > 1 m²**.
92:   **ПОПРАВЕНО ЧИСЛО (кръг 3 обори „47“):** от 51-те двойки **11 са двойка от `_meta.parent_child`** (М, поименно: `abatko–kk_konstantin_elena`, `asparuhovo–druzhba`, `asparuhovo–rozova_dolina`, `izgrev_kv–kokardzha_generic`, `kaisieva–vladislavovo`, `mladost–mladost1`, `mladost–mladost2`, `morska_gradina–saltanat`, `vazrazhdane–vazrazhdane1/2/3`) → **40 застъпвания извън родство**. Числото „47“ се получава само ако родството се чете от `properties.parent` (само 6 непразни, 4 от които в застъпване) — **изворът на родството в целия този план е `_meta.parent_child`, изрично и навсякъде.**
93: - **Покритие (М):** v1 покрива **68 314 / 80 510 = 84,85 %** от адресните точки (при обявеното в §1.5 правило за развръзка).
94: 
95: ### 1.4 · Замразеният снапшот на imot.bg (входът)
96: 
97: | | стойност | котва |
98: |---|---|---|
99: | `varna_polygons_08.09.geojson` | 175 736 B · sha256 `77b40564...` | (М) |
100: | `varna_dictionary_08.09.json` | 6 274 B · sha256 **`feba76e3...`** · списък от **98** `{id, name}` | (М) |
101: | `_meta` на снапшота | 12 ключа: `crs, dictionary_endpoint, dictionary_missing_polygons, dictionary_n, dictionary_sha256, fetched, list_endpoint, missing, n, raw_kept, source, tools`; `fetched = "2026-09-08"`, `n = 95`, `missing = []`, `dictionary_n = 98` | (М) |
102: | **`_meta.list_endpoint` — ДОСЛОВНО** | **`https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)`** — **с опашката**. **`url` на всеки от 84-те Feature-а = ЧИСТИЯТ адрес без опашката** (`source_terms.imot_bg.url` е друго поле — страницата с условията, Р10) (`https://www.imot.bg/obiavi/prodazhbi/grad-varna` — §3.Г.2 ред `url`, ИА-8, ИА-О30 т. 2; ИА-О38 поправя този ред, който ИА-О30 беше пропуснал) | (М) |
103: | **`_meta.dictionary_sha256` ВЪТРЕ в снапшота** | **(хешът на суровия отговор е частен провенанс и стои само в снапшота, не в този проследен план — ИА-О31)** — **НЕ е** sha на файла-речник. Това е хешът на **суровия отговор** на `dictionary_endpoint` (`https://api.imot.bg/mob_api/dictionary/search/1?town=5`), а суровият отговор е „scratchpad (private), not in the repo“ (Ч `_meta.raw_kept`). **Авторитетът за гейта е sha-то на ФАЙЛА (`feba76e3…`); вграденото число се записва като свидетел, който никой не сверява.** | (М) |
104: | Feature-и | **95**, всички `Polygon`, по 1 пръстен | (М) |
105: | свойства на Feature | `center, fetched, n_adverts, n_pts, name, provenance, raion, raion_num, slug, src`; `provenance = {endpoint, advert_id, raw_sha256, raw_bytes, fetched_local, field}` — **низът `raw_response_sha256` се среща 0 пъти**; `properties.fetched` има **една** стойност `"2026-09-08"` | (М) |
106: | **знаци след точката — ПОПРАВЕНО** | **7 640 числа** в `coordinates`, хистограма **{5: 7, 6: 53, 7: 642, 8: 6938}** — **кофа с 2 знака НЯМА**. (Контрола: 7 640 / 2 = **3 820** = сборът на `n_pts` в тялото с решенията.) *(Редакция 3 казваше „2, 5, 6, 7, 8 · 1/19/195/653/6963“ — нито едно от петте числа не съвпада; оборено и заменено.)* | (М) |
107: | и двата файла | **игнорирани** — `.gitignore:64:/scratch/boundary_gallery/` | (М) `git check-ignore -v` |
108: 
109: **Върху 79-те доставяни клетки (не върху 95-те), след канонизацията по D1:** **0 невалидни преди поправка** · **0 невалидни след канонизация** · **0 застъпващи се двойки с площ > 0** · **2 849 отсечки с кратност** (= 2 137 различни + 712 споделени; различни върхове **2 061** — ИА-О37) · **2 137 различни отсечки** · **712 споделени отсечки** · дължина на ръба (EPSG:32635, **върху съвкупността от 2 849 отсечки — споделените броени два пъти; върху 2 137-те различни статистиката е друга: 96,1 / 127,8 / 37,6 / 248,7 — ИА-О36**): медиана **96,5 m**, средна **130,4**, p10 **37,0**, p90 **257,5**, max **1 484,3**, min **8,92** · площ **74,615 km²** (М; редакция 3 даваше p10 37,1 / p90 257,4 / min 8,97 — премерено наново върху канонизираните клетки).
110: 
111: ### 1.5 · Адресните точки — маската, затворена и сверена
112: 
113: `Fire_Varna/data/address_rows.json`: **80 510** реда, `coordinate_order = "[lat,lng]"`, 5 073 137 B, sha256 **`2a4766bd...`** (М, върху **блоба** на HEAD).
114: 
115: | клас (затворен набор от 3: `outside_all_95`, `excluded_cell`, `deferred_cell`; плюс двата отчетни `in_one_cell`, `tie_break` — ИА-О35) | брой | котва |
116: |---|---|---|
117: | **`in_one_cell`** — в точно една клетка „да“ (канонизирани) | **77 210** | (М) |
118: | **`tie_break`** — на общия ръб на две клетки „да“ | **1** — една точка в район Приморски **(координата в частния файл)**, между **5055 `chaika_kk`** и **5053 `alen_mak`** | (М) |
119: | **М1 · `outside_all_95`** — извън всичките 95 полигона | **2 274** | (М) |
120: | **М2 · `excluded_cell`** — вътре в клетка, **която v2 изключва: десетте реда с `kind_registry = null` (петте „обекта“ И петте села)** | **1 025** = `pristanishte_varna` 355 · `biznes_hotel` 354 · `grand_mol` 274 · `biznes_park_varna` 26 · `letishte` 16 · петте села **0** | (М) |
121: | **М3 · `deferred_cell`** — вътре в **отложена клетка С ВИД** (шестте: `pz_topoli`, `vz_zvezditsa`, `krushkite`, `lazur`, `orehcheto`, `pripek`) | **0** | (М) |
122: | **сбор** | 77 210 + 1 + **3 299** = **80 510** | (М) |
123: 
124: > **Дефиницията, поправена след кръг 3:** `excluded_cell` покрива **десет** клетки, не пет — точно клетките, чиито редове отиват в `_meta.excluded` по §3.Г.1; `deferred_cell` покрива **шест** — точно клетките в `rows_without_feature.deferred`. Числово нищо не се мени (селата и отложените хващат 0 точки), но **дефиницията в §1.5 и дефиницията в §3.Г.1 вече са една и съща**, иначе ИА-11 не може да бъде написан еднозначно. Полето `mask.in_cell` от отрицателната половина на стар ИА-11 **не съществува** и е махнато; закотвените имена са `in_one_cell`, `tie_break`, `outside_all_95`, `excluded_cell`, `deferred_cell`, `address_rows_sha256`, `outside_note`, `tie_break_rule`.
125: 
126: - **Покритие на доставката: 77 211 / 80 510 = 95,90 %.** Ако петте „обекта“ влязат: 78 236 = **97,18 %** — това и е числото „97,2 %“ в ADR 011 (Ч `011_kartata_imot.md:47`). Двете се поправят в комит К8.
127: - **Дифът v1 → v2 по адресна точка — ПОПРАВЕН и възпроизводим.** Кръг 3 обори двойката „49 926 / 17 453“: тя не следва от никое обявено правило, защото **4 517 от 80 510-те точки попадат в ≥ 2 полигона на v1** (М), а правило за развръзка на страната v1 нямаше. **Обявено правило (Р20): за v1 печели азбучно най-малкият код; за v2 — най-малкият `raion_num` (Р6).** При него (М): същата дума **49 397** · сменена **17 982** · изгубена **935** · спечелена **9 832** · без дума и преди, и сега **2 364**. Сборът е 80 510; 49 397 + 17 982 + 935 = **68 314** (v1) ✔; 49 397 + 17 982 + 9 832 = **77 211** (v2) ✔. Правилото се записва дословно в `_meta.diff_v1_v2.tie_break_v1` и се преизмерва от ИА-13.
128: - Речникът на ADR 011 за М1 („порт, промзона, село, грешна координата“, Ч `011:47`) се записва в `_meta.mask.outside_note` **дословно**; той е бележка, не клас, и никой гейт не го съди.
129: 
130: ### 1.6 · Тялото с решенията (черновата днес, **след комит 7556227**)

 succeeded in 485ms:
1: # ПЛАН · Картата imot — под-лот **И-А** (varna_3d + документи)
5: **Какво прави този лот.** Прави плочката на imot.bg **канонична геометрия** в частното репо `varna_3d` — замразеният вход, подписаното тяло с решенията, нов билдър, негов собствен гейт, архив на v1 — и допълва три документа във Fire_Varna. **Нищо във Fire_Varna освен тези три проследени документа и един поименно обявен ИГНОРИРАН файл за преглед не се пипа.** Живата карта, доставката Б3, `index.html`, `data/`, `tests/`, `gates/` на Fire_Varna остават непроменени и си остават работа на **И-Б**.
13: ## 0 · Червени редове
19: 5. **Нула квартална геометрия и нула суров провенанс в проследен файл на Fire_Varna.** Геометрията, `advert_id`, `raw_sha256`, `points` и **всяка координата** живеят само в **частното** репо `varna_3d` и в игнорираната папка на Fire_Varna (М: `git check-ignore -v scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson` → `.gitignore:64:/scratch/boundary_gallery/`). **Този план е проследен файл на Fire_Varna — затова в текста му няма нито една двойка `lat/lon`; навсякъде, където предишна редакция цитираше координата, стои „(координата в частния файл)“. Спазването се съди механично от ИА-19.** Обобщени производни (площи, брой върхове, хистограма на ръба, хешове) **не са координати** и остават позволени — обявено в ИА-О24, дългът за правило и гейт е ИБ-18.
32: ## 1 · Мярка (всичко мерено 08.09; нула редакции)
34: ### 1.1 · Състояние на репата
54: ### 1.2 · Базата на `varna_3d` е ЗЕЛЕНА (за разлика от Fire_Varna) — **девет реда**
80: ### 1.3 · Схемата на v1 (какво трябва да възпроизведе v2, ключ по ключ)
95: ### 1.4 · Замразеният снапшот на imot.bg (входът)
99: | `varna_polygons_08.09.geojson` | 175 736 B · sha256 `77b40564...` | (М) |
100: | `varna_dictionary_08.09.json` | 6 274 B · sha256 **`feba76e3...`** · списък от **98** `{id, name}` | (М) |
102: | **`_meta.list_endpoint` — ДОСЛОВНО** | **`https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)`** — **с опашката**. **`url` на всеки от 84-те Feature-а = ЧИСТИЯТ адрес без опашката** (`source_terms.imot_bg.url` е друго поле — страницата с условията, Р10) (`https://www.imot.bg/obiavi/prodazhbi/grad-varna` — §3.Г.2 ред `url`, ИА-8, ИА-О30 т. 2; ИА-О38 поправя този ред, който ИА-О30 беше пропуснал) | (М) |
103: | **`_meta.dictionary_sha256` ВЪТРЕ в снапшота** | **(хешът на суровия отговор е частен провенанс и стои само в снапшота, не в този проследен план — ИА-О31)** — **НЕ е** sha на файла-речник. Това е хешът на **суровия отговор** на `dictionary_endpoint` (`https://api.imot.bg/mob_api/dictionary/search/1?town=5`), а суровият отговор е „scratchpad (private), not in the repo“ (Ч `_meta.raw_kept`). **Авторитетът за гейта е sha-то на ФАЙЛА (`feba76e3…`); вграденото число се записва като свидетел, който никой не сверява.** | (М) |
111: ### 1.5 · Адресните точки — маската, затворена и сверена
130: ### 1.6 · Тялото с решенията (черновата днес, **след комит 7556227**)
149: ### 1.7 · Кодовете, регистърът и районът (върху ДОСТАВЯНИТЕ 84)
182: ### 1.8 · Пиновете, които сочат v1 — изчерпателно, мерено с `git grep`
211: ### 1.9 · Механиката на `.gitignore` във `varna_3d` (М)
220: ## 2 · Обявени отклонения
248: | **ИА-О30** | **Сверка на Архитекта след кръг 5 (08.09 нощ).** Шест поправки, всяка отбелязана на мястото си с „ИА-О30“: (1) `--privacy-scope <път>` влиза в CLI-договора на Ф2 (§3.А), защото ИА-7 го ползва; (2) `url` в артефакта = **чистият** адрес `https://www.imot.bg/obiavi/prodazhbi/grad-varna` — описателната опашка на `_meta.list_endpoint` не е URL (§3 ред `url`, ИА-8, Р10); (3) `_meta.source_terms.imot_bg` = **три** ключа `{url, recorded_on, position}` — отклонение от шесткльчовия образец C9 на v1, защото за imot.bg не е правена работа по условията и никой не е отварял страницата; ИА-8 съди трите (Р10 дава алтернативата с шест само по изрична дума на Петър); (4) записите в `_meta.excluded` носят петорката на v1 `{code, display, kind, registry_action, why}` + `delivered`/`status`, без ключ `reason` (ИА-17) **[наборът е разширен с `district_witness_note` от ИА-О31 т. 2 / ИА-О32 т. 10 — ИА-17 носи окончателния]**; (5) ИА-19 хваща и българската десетична запетая и има две отрицателни половини (точка и запетая); (6) ИА-19 → ИА-STOP 17 при изход 0 на `grep` (полярността е записана изрично). Числата в §1.4, §1.5, §1.7, Х5 и §5 остават тези на редакция 4; Р15/Р17 казват какво се преизмерва при „мр“ / „не“. | Петър подписва редакцията с тези шест; кръгове 1–5 на опровергателите са в `scratch/places_search/karta_imot_plan_reviews_08.09.md`. |
258: | **ИА-О40** | **Преименуване по думата на Петър (08.09 обед): префиксът `imot_bg_` пада от имената на двата замразени файла.** Ф5 = `data/varna_polygons_08.09.geojson`, Ф6 = `data/varna_dictionary_08.09.json`; същите имена в игнорираната изворна папка, в Т1 (двата `!`-реда), К2, ИА-1, §1.4, Г.7 т. 1–2, червен ред 5 и стъпка 3. **Съдържанието не е пипано: байтовете и sha (175 736 B / `77b40564…`; 6 274 B / `feba76e3…`) остават пиновете.** Изворът остава записан вътре: `_meta.source = "imot_bg_tiling"`, `_meta.list_endpoint`, провенансът по Feature — името на файла не е носител на провенанс. Промяна на текст, не на мярка; проверява се с `grep` (0 стари имена в трите проследени документа и в игнорираната папка) и от Astra (механика) преди изпълнението. | Думата на Петър: „искам да махнеш imot_bg от името на файла“; „одобрявам плочките — дай ги на Astra и на Кими за проверка и да ги вкарваме“. |
260: ## 3 · Write-set с котви (изчерпателен — път извън тази таблица = ИА-STOP 1)
262: ### 3.А · `varna_3d` — нови файлове
270: | **Ф5** | `data/varna_polygons_08.09.geojson` | **байтово копие** на снапшота (175 736 B, `77b40564…`) | **К2 · Петър** |
271: | **Ф6** | `data/varna_dictionary_08.09.json` | **байтово копие** на речника (6 274 B, `feba76e3…`) | **К2 · Петър** |
281: ### 3.Б · `varna_3d` — точкови редакции (**архивният път е един и същ навсякъде**: `docs/archive/quarters_signed_v1_2026-09-06.geojson`)
285: | **Т1** | `.gitignore` — **ЕДНА редакция, един блок**: коментарният блок `:24-33` се пренаписва (той описва v1), и **непосредствено след `:34` се добавят четирите реда** | — | `!data/varna_polygons_08.09.geojson` · `!data/varna_dictionary_08.09.json` · `!data/quarters_decisions_imot_2026-09-08.json` · `!docs/archive/quarters_signed_v1_2026-09-06.geojson`. **Четирите стоят СЛЕД `:23` и СЛЕД `:4`, значи бият и двете правила** (§1.9). **ПЕТИ ред за `tests/fixtures/` НЕ се добавя** (ИА-О20). **Файлът се пипа ВЕДНЪЖ и се комитва ВЕДНЪЖ — в К2, ръката на Петър.** |
305: ### 3.В · `Ф7` (подписаното тяло) срещу черновия блоб `8626ad43…` — **точно ЕДИНАЙСЕТ разлики, нула други** (Х11 от ИА-О34; заглавието поправено от ИА-О35)
313: | **Х3** | `_meta.privacy` | „…в игнорираната папка **(G29)**“ | „…суровият провенанс живее в частното репо `varna_3d` (`data/varna_polygons_08.09.geojson`) и в игнорираната папка `scratch/boundary_gallery/` на Fire_Varna, доказано с `git check-ignore -v`“ | **G29 не е регистриран в ADR 010** (М: `grep -c G29 010_signed_quarter_boundaries.md` → **0**), но **СЪЩЕСТВУВА и остава в сила** (предшественикът `:31`): дефиниран в `ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:107` (препратки `:62`, `:104`, `:141`; `:71` е мярката на игнорирането), ПОСТРОЕН в `scratch/places_search/qa_night_pins.py` (`check_ignore` `:206`, докстрингът G29 `:229`, отчетът `:242`, отрицателната половина `:402-444`) — ИА-О34 поправя старата котва `:71`; `_meta.privacy` спира да се позовава на номер, който ADR 010 не познава, и казва какво е доказано |
325: ### 3.Г · Правилата на новия билдър (`Ф1`) — дословно, без празни места
357: | `license` · `license_terms` · `license_label` · `attribution` | **дословно (ИА-О31, Р10):** `license` = `"условия на imot.bg — присъда няма; геометрията не пътува публично (виж _meta.source_terms.imot_bg)"` · `license_terms` = `"https://www.imot.bg/obshti-uslovia"` · `license_label` = `"граница по районите на imot.bg (район <raion_num>, свалена 2026-09-08) — извор на всекидневната употреба, не официален кадастър"` · `attribution` = `"Кварталните граници в този файл са районите на imot.bg (© imot.bg), снапшот 08.09.2026. Геометрия НИКОГА не пътува публично."` — и четирите непразни по всичките 84 (ИА-8) |
358: | `url` | **чистият адрес на списъка на imot.bg за град Варна: `https://www.imot.bg/obiavi/prodazhbi/grad-varna`** — това е `_meta.list_endpoint` на снапшота БЕЗ описателната опашка „(95 with adverts, counts)“, която е бележка, не URL (ИА-О30; Ф1 отрязва всичко от първия интервал нататък) — **непразен и еднакъв по всичките 84** (ИА-О31: смисълът на `url` се сменя от „обектът-извор“ (v1, 60 различни) към „списъкът-извор“ (v2, един) — и това отклонение стои и в `_meta.declared_deviations[]`) |
392: Съдържанието: `artifact_class = "signed_by_plan_signature"` · `lot = "И-А"` · `plan` = `{file, rev: plan_rev, blob_sha256: plan_body_sha256}` (`file` както във v1 и ИА-О11; същите стойности като Х8 — ИА-О33/ИА-О34) · `generated_by = "Claude Executor"` · `decisions_author = "Claude Architect (черновата, 7556227) → Петър (подпис)"` · `decisions_based_on` = черновият блоб `8626ad43…` + ревизията му · `decisions_blob_before_attribution` = същият · `decisions_sha256_rule` = дословно правилото на червен ред 12 · `decisions_sha256_worktree` = `{path, bytes, note: "varna_3d е eol=lf — работното копие Е блобът (git check-attr)"}` · `d1_schema` = полетата + **десетте** нулирани (ИА-О16) · `canonicalization` = трите правила + изричното изречение за `wm_polygon_sha256` при извор без уикимапийски обект · `dictionary_sha256` = **sha на ФАЙЛА** `feba76e3…` · `snapshot_date = "2026-09-08"` · `method_licence = {external_tiling: …, imot_tiling_union: …}` · `licences[]` = **един** запис (imot.bg) · `source_terms.imot_bg` = **трите** ключа на Р10 (`url, recorded_on, position` — ИА-О30/ИА-О31) · `attribution` = редът на Р10 · `publication` = „Геометрия НИКОГА не пътува публично; публично излизат само име, код и `src`“ · `precision_floor_m = 50` · `precision_m_by_method = {"external_tiling": 100, "imot_tiling_union": 100}` · `parent_child` = **17** двойки (**и това е ЕДИНСТВЕНИЯТ извор на родство, който гейтовете четат**) · `parent_child_without_polygon = []` · **`excluded` = 11 записа / 10 реда (Г.1)** · `rows_without_feature` = двете кофи (Г.1) · `registry_pending` = **28**-те регистрови кода без Feature · `registry_pending_new` = **28**-те доставяни кода без ред в регистъра · `district_resolutions` = приложените + препратка към вход 5 · `district_witness_agkk` = картата код → АГКК (**82** реда с двете стойности) · `district_witness_disputes` = **5** (4 `delivered: true`, 1 `delivered: false`) · `union_crs` / `union_recipe` / `union_witness` = Г.6 · `signature` = Gate 1 · `counts` = 15-те полета на Х5 · `mask` = §1.5, включително `tie_break_rule` · `diff_v1_v2` = **изчислен от Ф1 срещу `--diff-base` (осмият вход, §3.Г.7) и преизмерен от ИА-13 (б)**, включително `tie_break_v1` (Р20) — ИА-О35 · `declared_deviations[]` = **дословният списък от 16 записа (ИА-О33), по един запис на ред, всеки `{id, text}` с точно тези `id`:** `ИА-О2` · `ИА-О4` · `ИА-О10` · `ИА-О12` · `ИА-О15` · `ИА-О16` · `ИА-О17` · `ИА-О21` · `ИА-О23` · `ИА-О24` · `Г.2-drawn_by` (`drawn_by = null`) · `Г.4` (един запис с двете преименувания) · **`Р4` (отклонение от ADR 010 D4: `no_boundary` без Feature)** · **`Г.2-url` (смисълът на `url` = списъкът-извор, един за всичките 84, не обектът-извор)** · **`Р17` (`vinitsa_sever` — обърнато подписано изключване, `delivered: true`)** · **`Р10` (`source_terms.imot_bg` с три ключа вместо шестте на C9 — ИА-О30 т. 3)** — **всяко отклонение живее и в артефакта, не само в плана; ИА-6 съди списъка по `id`.**
396: ### 3.Д · `Fire_Varna` — три проследени документа и един игниран файл
401: | **Д2** | `docs/decisions/011_kartata_imot.md` | **ред-статус** („И-А изпълнен; тялото и геометрията са в varna_3d; И-Б отворен“) + поправките: **И-D3 (`:17`) — каноничният път става `varna_3d/data/quarters_decisions_imot_2026-09-08.json`** · **И-D2 (`:15`)** `drawn_by` → `null`, `raw_response_sha256` → обявеното съответствие с `provenance.raw_sha256`, `source_terms.imot_bg` от два на **три** ключа (`url, recorded_on, position` — ИА-О30/ИА-О31; не шест: за imot.bg не е правена работа по условията), **амандамент на ADR 010 D4** (`no_boundary` без Feature — Р4; и че `deferred` не живее в `_meta.deferred`, а в `rows_without_feature.deferred[]` за imot-редовете и в `_meta.registry_pending` за регистровите кодове — наследено от v1, което също няма `_meta.deferred`; ИА-О36), и изричното потвърждение, че `dictionary_sha256` + `snapshot_date` СА в `_meta` · **И-D4 (`:19`)**: виртуалните родители СА Feature-и (84 = 79 + 5) · **И-D5**: нови редове за архива на v1, за преместеното тяло, за копирания снапшот, **за обръщането на `vinitsa_sever` (Р17)**, **за амандамента на ADR 010 D0/G23 (Р19)** и **за пина по байтове на слоя с районите (Р21)** · **„Последствия“ (`:47`)**: `97,2 %` → **95,90 % за доставката (79 клетки) / 97,18 % при включени обекти**; `:48` „около 18 280 сменят думата“ → измереното **17 982 сменени · 935 изгубени · 9 832 спечелени** (при обявеното правило Р20); площите `61,7 km²` → **61,597 обединение / 66,886 сбор** за v1 и **74,615 / 82,908** за v2. **Статусът остава `Proposed`** (Ч `011:3`). |
409: ## 4 · Ред на изпълнение
416: | 3 | Изп | Копира Ф5, Ф6 от игнорираната папка `Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/` (червен ред 5; М: `git check-ignore -v` → `.gitignore:64`) в `varna_3d/data/`; прави **единствената** редакция Т1; `git check-ignore -v --no-index` за Ф5, Ф6 → **печата разрешаващото `!`-правило на Т1** (ИА-О34: БЕЗ `--no-index` командата мълчи с изход 1 за всеки път, който вече е в индекса — М в еднократно репо и в живото varna_3d върху `data/quarters_signed.geojson`; редът се ЗАПИСВА като мярка, не спира) → `git add -- data/varna_polygons_08.09.geojson data/varna_dictionary_08.09.json .gitignore` → **`git ls-files --error-unmatch -- <двата>` = 0** (това е критерият). **Не комитва.** | `ls-files --error-unmatch` ≠ 0 = **ИА-STOP 11** (единственият критерий — ИА-О34) |
437: ## 5 · Гейтове
461: | **ИА-7** | **приватност — САМО файлове с ДАННИ** | Ф2, `--privacy-scope <път>` (в CLI-договора на Ф2, §3.А) · 9, 13, 18 | 0. **Обхватът е ЕДИН път: `Ф7`** — единственият файл с данни, който този лот създава или мени и който е тяло, а не геометрия. **Ф10, Д1, Д2, Д3 са ПРОЗА и са извън обхвата по конструкция — тях ги съди ИА-19** (ИА-О24); `data/quarters_signed.geojson` и `data/varna_polygons_08.09.geojson` са извън обхвата по конструкция — те СА геометрията в частното репо. По имена на ключове: `advert_id, raw_sha256, raw_response_sha256, points, raion_points, localid, cadnum, center, coordinates, geometry, centroid, polygon, bbox` → **0** и **0 float-а в кутията на Варна** (М днес върху блоба `8626ad43…`: 0 и 0; подниз `advert` = 98 от `n_adverts` и НЕ се брои) | копие на `Ф7` с добавен ключ `"advert_id"` → 1; копие на `Ф7` с ключ `"center"` и двойка числа в кутията на Варна → 1 |
462: | **ИА-8** | `source_terms` + атрибуция | Ф2 · 9, 13, 18 | 0; `_meta.source_terms.imot_bg` носи **ТОЧНО трите** ключа `url, recorded_on, position` (Р10; **ИА-О30: отклонение от шесткльчовия образец C9 на v1** — `quote/terms/verdict/checked_on` НЕ се пишат, защото никой не е отварял страницата и датата на „проверка“ би била атестация за нещо, което не се е случило); `len(_meta.licences) == 1`; всеки от 84-те носи непразни `license`, `license_terms`, `license_label`, `attribution` и **`url` == `https://www.imot.bg/obiavi/prodazhbi/grad-varna`** (чистият адрес, §3 ред `url`) | копие с празен `position` → 1; копие с четвърти ключ `checked_on` в `source_terms.imot_bg` → 1; копие с Feature, чийто `license` е голо „CC BY-SA“ → 1; копие, в което `url` носи опашката „(95 with adverts, counts)“ → 1 |
488: ## 6 · Комити
505: | **К2** | 4 | varna_3d · **Петър** | `data: frozen imot.bg tiling snapshot 08.09, 95 polygons` | **55** | `data/varna_polygons_08.09.geojson`, `data/varna_dictionary_08.09.json`, `.gitignore` (**и четирите unignore реда**) |
506: | **К3** | 7 | varna_3d · **Петър** | `data: signed decisions for the imot.bg tiling` | **45** | `data/quarters_decisions_imot_2026-09-08.json` |
507: | **К4** | 11 | varna_3d · Изп | `feat(quarters): imot.bg tiling builder and its own gate` | **55** | `src/build_quarters_signed_imot.py`, `src/qa_quarters_signed_imot.py`, `tests/test_quarters_signed_imot_fixtures.py` — **без фикстури** (ИА-О20) |
522: ## 7 · STOP
547: ## 8 · Локален преглед (кои проби гледа Петър)
559: ## 9 · Решения за Петър (Gate 1) — **двайсет и едно**
574: | **Р10** | **Атрибуцията и `source_terms`** (попълва се, не се обсъжда) | C9 на v1 иска на извор **шест** ключа (Ч `qa_quarters_signed.py:362`) — **за v2 важи ИА-8 с ТРИ** (ИА-О30/ИА-О31); ADR 011 И-D2 дава два — поправя се в К8. **`_meta.list_endpoint` е с опашката** (М). | **`_meta.attribution` и `properties.attribution`:** „Кварталните граници в този файл са районите на imot.bg (© imot.bg), снапшот 08.09.2026. Геометрия НИКОГА не пътува публично.“ · **`license_label`:** „граница по районите на imot.bg (район `<raion_num>`, свалена 2026-09-08) — извор на всекидневната употреба, не официален кадастър“ · **`url` = чистият адрес `https://www.imot.bg/obiavi/prodazhbi/grad-varna`** (без описателната опашка на `_meta.list_endpoint`) · **`_meta.source_terms.imot_bg` = ТОЧНО ТРИ ключа:** `{url: "https://www.imot.bg/obshti-uslovia", recorded_on: "2026-09-08", position: "Публично пътуват само име, код и src на квартала; геометрията остава в частното репо."}` — **без `quote`, `terms`, `verdict`, `checked_on`**: никой не е отварял страницата, а дата на „проверка“ в подписан артефакт би била атестация за нещо, което не се е случило (ИА-О30). Докато присъда няма, **нищо от този артефакт не пътува публично** — записва се в `_meta.publication`; дългът е **ИБ-19** (§11). **Алтернатива само с изрична твоя дума:** Изпълнителят отваря страницата, преписва абзаца дословно в `quote`, вписва `checked_on` и `terms`, ти подписваш присъдата с ред в опашката — тогава ключовете стават шест и ИА-8 се пренаписва за тях. |
589: ## 10 · Какво НЕ се пипа
606: ## 11 · Пренесено към И-Б (измерени дефекти, които И-А не докосва)
644: **ИБ-19 · Условията на извора imot.bg нямат присъда.** И-А записва само `{url, recorded_on, position}` в `_meta.source_terms.imot_bg` (Р10, ИА-О30) и заключва публикацията в `_meta.publication`. Присъдата (кой отваря страницата, кой преписва абзаца, кой подписва реда в опашката) е дълг на И-Б преди първата публична доставка Б4; никакъв лицензен разговор с Петър — само ред клас „въпрос“ с `тяло: <sha>` (червен ред 11).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p=next(Path('docs/plans').glob('*imot_*-*_08.09.md'));a=p.read_text(encoding='utf-8').splitlines()
for start,end in [(100,119),(377,390),(411,419),(451,455)]:
 for i in range(start-1,end):
  s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',a[i])
  s=re.sub(r'(?<"'!'"\\w)(?:27|28|43|44)[.,]\\d{2,}', '[coord]',s)
  print(f'{i+1}: {s}')
'@ | python -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'fetch\\(|loadHotels|loadPlaces|hotels.json|places.json' index.html; rg -n --max-count 20 --max-columns 200 'hotels.json|places.json|fetch\\(' index.html" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git check-ignore -v -- scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson scratch/boundary_gallery/granitsi_preview_05.09/varna_dictionary_08.09.json; git -c core.quotePath=false ls-files -- scratch/boundary_gallery; git -c safe.directory=C:/git/varna_3d status --short -- data/varna_polygons_08.09.geojson data/varna_dictionary_08.09.json src/build_quarters_signed_imot.py src/qa_quarters_signed_imot.py' in C:\git\Fire_Varna
 succeeded in 331ms:
100: | `varna_dictionary_08.09.json` | 6 274 B · sha256 **`feba76e3...`** · списък от **98** `{id, name}` | (М) |
101: | `_meta` на снапшота | 12 ключа: `crs, dictionary_endpoint, dictionary_missing_polygons, dictionary_n, dictionary_sha256, fetched, list_endpoint, missing, n, raw_kept, source, tools`; `fetched = "2026-09-08"`, `n = 95`, `missing = []`, `dictionary_n = 98` | (М) |
102: | **`_meta.list_endpoint` — ДОСЛОВНО** | **`https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)`** — **с опашката**. **`url` на всеки от 84-те Feature-а = ЧИСТИЯТ адрес без опашката** (`source_terms.imot_bg.url` е друго поле — страницата с условията, Р10) (`https://www.imot.bg/obiavi/prodazhbi/grad-varna` — §3.Г.2 ред `url`, ИА-8, ИА-О30 т. 2; ИА-О38 поправя този ред, който ИА-О30 беше пропуснал) | (М) |
103: | **`_meta.dictionary_sha256` ВЪТРЕ в снапшота** | **(хешът на суровия отговор е частен провенанс и стои само в снапшота, не в този проследен план — ИА-О31)** — **НЕ е** sha на файла-речник. Това е хешът на **суровия отговор** на `dictionary_endpoint` (`https://api.imot.bg/mob_api/dictionary/search/1?town=5`), а суровият отговор е „scratchpad (private), not in the repo“ (Ч `_meta.raw_kept`). **Авторитетът за гейта е sha-то на ФАЙЛА (`feba76e3…`); вграденото число се записва като свидетел, който никой не сверява.** | (М) |
104: | Feature-и | **95**, всички `Polygon`, по 1 пръстен | (М) |
105: | свойства на Feature | `center, fetched, n_adverts, n_pts, name, provenance, raion, raion_num, slug, src`; `provenance = {endpoint, advert_id, raw_sha256, raw_bytes, fetched_local, field}` — **низът `raw_response_sha256` се среща 0 пъти**; `properties.fetched` има **една** стойност `"2026-09-08"` | (М) |
106: | **знаци след точката — ПОПРАВЕНО** | **7 640 числа** в `coordinates`, хистограма **{5: 7, 6: 53, 7: 642, 8: 6938}** — **кофа с 2 знака НЯМА**. (Контрола: 7 640 / 2 = **3 820** = сборът на `n_pts` в тялото с решенията.) *(Редакция 3 казваше „2, 5, 6, 7, 8 · 1/19/195/653/6963“ — нито едно от петте числа не съвпада; оборено и заменено.)* | (М) |
107: | и двата файла | **игнорирани** — `.gitignore:64:/scratch/boundary_gallery/` | (М) `git check-ignore -v` |
108: 
109: **Върху 79-те доставяни клетки (не върху 95-те), след канонизацията по D1:** **0 невалидни преди поправка** · **0 невалидни след канонизация** · **0 застъпващи се двойки с площ > 0** · **2 849 отсечки с кратност** (= 2 137 различни + 712 споделени; различни върхове **2 061** — ИА-О37) · **2 137 различни отсечки** · **712 споделени отсечки** · дължина на ръба (EPSG:32635, **върху съвкупността от 2 849 отсечки — споделените броени два пъти; върху 2 137-те различни статистиката е друга: 96,1 / 127,8 / 37,6 / 248,7 — ИА-О36**): медиана **96,5 m**, средна **130,4**, p10 **37,0**, p90 **257,5**, max **1 484,3**, min **8,92** · площ **74,615 km²** (М; редакция 3 даваше p10 37,1 / p90 257,4 / min 8,97 — премерено наново върху канонизираните клетки).
110: 
111: ### 1.5 · Адресните точки — маската, затворена и сверена
112: 
113: `Fire_Varna/data/address_rows.json`: **80 510** реда, `coordinate_order = "[lat,lng]"`, 5 073 137 B, sha256 **`2a4766bd...`** (М, върху **блоба** на HEAD).
114: 
115: | клас (затворен набор от 3: `outside_all_95`, `excluded_cell`, `deferred_cell`; плюс двата отчетни `in_one_cell`, `tie_break` — ИА-О35) | брой | котва |
116: |---|---|---|
117: | **`in_one_cell`** — в точно една клетка „да“ (канонизирани) | **77 210** | (М) |
118: | **`tie_break`** — на общия ръб на две клетки „да“ | **1** — една точка в район Приморски **(координата в частния файл)**, между **5055 `chaika_kk`** и **5053 `alen_mak`** | (М) |
119: | **М1 · `outside_all_95`** — извън всичките 95 полигона | **2 274** | (М) |
377: 3. тялото с решенията Ф7 — **прочетено като блоб на varna_3d** (`{path, rev, sha256, bytes}`); `_meta.decisions_sha256` / `decisions_commit` / `decisions_path` са същите стойности, изнесени поименно по образеца на v1;
378: 4. `Fire_Varna/data/address_rows.json` (`2a4766bd…`, 5 073 137 B) — **файл, пиннат по прочетените байтове; блобът на Fire_Varna е свидетел (`{repo, rev, path}`), ИА-О35/ИА-О38**; `_meta.mask.address_rows_sha256` препраща към него;
379: 5. **`Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json` — БЛОБ** (`rev e6c706d…`, sha `d494d4d256ae…`, 513 B); `_meta.district_resolutions.input` препраща към записа в `inputs`;
380: 6. **`C:/git/m6000_private/number_viewer/quarters_layer.geojson` — ФАЙЛ извън git** (`26e39b00…`, 201 130 B), с `note: "извън git репо — пинва се по прочетени байтове (Р21, ИА-О23); версионирането е дълг ИБ-17"`;
381: 7. **`C:/git/Varna_buildings/config/quarter_registry.json` — БЛОБ на Varna_buildings** (М, ИА-О34: `git -C C:/git/Varna_buildings log -1 --format=%H -- config/quarter_registry.json` → `627b240…`, 52 299 B, sha `7d217401…`; 84 записа) — регистърът ражда `counts.registry_entries`, `registry_pending`, `registry_pending_new` и вида на 56 кода (Х11); четен е само (D14, изолация на репата); **пинът е sha256 на прочетените байтове, `{repo, rev, path}` са свидетел** (ИА-О35: Ф2 няма `--registry-repo/-rev`, а трето временно дърво във Varna_buildings е забранено от ИА-STOP 14 — счупва се по механика 1);
382: 8. **v1 като диф-база — БЛОБ на varna_3d** (ИА-О35): `role: "diff_base"`, `{repo: varna_3d, rev: 6486b48…, path: data/quarters_signed.geojson, sha256: c1551d24…, bytes: 301 917, note: "след К6 живее в docs/archive/quarters_signed_v1_2026-09-06.geojson (Ф8); блобът е същият"}` — ревизията е `git -C C:/git/varna_3d log -1 --format=%H -- <пътя, подаден на --diff-base>` (М днес: `6486b48…`); той ражда САМО `_meta.diff_v1_v2`, не геометрия; ИА-9 го сверява с `git show <rev>:<path>`, който е стабилен и след `git mv` (червен ред 13). **Празна ревизия (ИА-О36):** на стъпка 13 `--diff-base` сочи архивния път, чийто `git mv` е само стейджнат (К6 е стъпка 14) → `git log -1 -- <път>` е празен; Ф1 записва `rev: null` + `note: "път без история — пресен билд за ИА-10"` и хешира байтовете; това е допустимо САМО за пресните билдове на ИА-10 (сравняват се помежду си), доставеният файл от стъпка 8 носи истинската ревизия.
383: 
384: **Разлика между пина и прочетените байтове = `sys.exit(1)`** за всичките осем. **Кой как се сверява (ИА-О35):** по БЛОБ (`git show <rev>:<path>` в своето репо) — Ф7 (`--decisions-repo/-rev/-path`), резолюциите (`--resolutions-repo/-rev/-path`) и диф-базата (записаните `rev`/`path` в артефакта); по БАЙТОВЕ от диска (sha256; `rev` е свидетел, където файлът е в git) — снапшотът, речникът, `address_rows`, слоят с районите, регистърът. Правилото: блобово адресиране само където Ф2 има тройка флагове или артефактът носи ревизията; иначе байтовете са пинът.
385: 
386: **Г.8 · `_meta` — ЗАТВОРЕНИЯТ НАБОР ОТ 41 ИМЕНА, изброен изчерпателно:**
387: 
388: `artifact_class · attribution · canonicalization · counts · d1_schema · decisions_author · decisions_based_on · decisions_blob_before_attribution · decisions_commit · decisions_path · decisions_sha256 · decisions_sha256_rule · decisions_sha256_worktree · declared_deviations · dictionary_sha256 · diff_v1_v2 · district_resolutions · district_witness_agkk · district_witness_disputes · excluded · generated_by · inputs · licences · lot · mask · method_licence · parent_child · parent_child_without_polygon · plan · precision_floor_m · precision_m_by_method · publication · registry_pending · registry_pending_new · rows_without_feature · signature · snapshot_date · source_terms · union_crs · union_recipe · union_witness`
389: 
390: (= 36-те на v1 **+** `dictionary_sha256`, `snapshot_date` по ADR 011 И-D2 **+** `diff_v1_v2`, `mask`, `registry_pending_new`; `decisions_sha256` и `source_terms` вече са сред 36-те.)
411: | стъпка | кой | какво | спирачка |
412: |---|---|---|---|
413: | 0 | Изп | Пълната мярка на §1 **без нито една редакция**. Записва OID-ите на 14-те стейджнати пътя (`git ls-files -s -- <14-те>`), **`git worktree list` на двете репа като базова линия (ИА-О36: Fire_Varna днес носи две чужди дървета — §1.1)**, изходите **Н1–Н6, Н8, Н9**, **16-те идентификатора на тестовете** (по списък, без прогон) и **състоянието на Д3** по `git status --porcelain -- docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` (чист или мръсен — записва се фактът; **ИА-О31:** старият хънк на §20 е комитнат в `0304a3c`, не се изисква). **Н7 (`python -m unittest discover -s tests`) НЕ се пуска на стъпка 0** — `tests/test_quarters_signed_fixtures.py:156-157` (пазачът и `shutil.rmtree`) изтрива и регенерира фикстури в репото (Ч); мери се на стъпка 13 в еднократното `git worktree`. | разлика в Н1–Н6, Н8, Н9 или в 16-те идентификатора = **ИА-STOP 2** |
414: | 1 | **Петър** | **Gate 1** — подписва този план и **двайсет и едното** решения на §9. | без подпис нищо не тръгва |
415: | 2 | **Архитект** (не Изп) | **К1 = ред-статус „подписан от Петър, <дата>, ревизия <sha>“ отгоре на Д1**, само ако Петър подпише без редакции (при редакции Архитектът ги внася преди подписа); Изпълнителят на стъпка 2 само пуска **ИА-19** върху БЛОБА на Д1 в HEAD (`git show HEAD:<Д1> > %TEMP%/ia_docs/d1_head.md`, после изразът на ИА-19 — двата `-e` образеца — върху ТОЗИ файл като единствен операнд; ИА-О34: `grep` с файлови операнди пренебрегва stdin, затова тръба към командата на §5 съди работното дърво, не блоба — М) и `b3_g11.py HEAD --cached` = 0 (ИА-О32) | ИА-19 с изход **0** (`grep` намери координата) = **ИА-STOP 17**; изход **2** (грешка на командата) = **ИА-STOP 5**; изход 1 = чисто; b3_g11 ≠ 0 = **ИА-STOP 9** |
416: | 3 | Изп | Копира Ф5, Ф6 от игнорираната папка `Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/` (червен ред 5; М: `git check-ignore -v` → `.gitignore:64`) в `varna_3d/data/`; прави **единствената** редакция Т1; `git check-ignore -v --no-index` за Ф5, Ф6 → **печата разрешаващото `!`-правило на Т1** (ИА-О34: БЕЗ `--no-index` командата мълчи с изход 1 за всеки път, който вече е в индекса — М в еднократно репо и в живото varna_3d върху `data/quarters_signed.geojson`; редът се ЗАПИСВА като мярка, не спира) → `git add -- data/varna_polygons_08.09.geojson data/varna_dictionary_08.09.json .gitignore` → **`git ls-files --error-unmatch -- <двата>` = 0** (това е критерият). **Не комитва.** | `ls-files --error-unmatch` ≠ 0 = **ИА-STOP 11** (единственият критерий — ИА-О34) |
417: | 4 | **Петър** | Комит **К2** (замразеният вход + `.gitignore` — **и четирите unignore реда, включително този за архива, са в ТОЗИ комит**). | — |
418: | 5 | Изп | Пише Ф1, Ф2, Ф3. Още нищо не се стартира срещу истински данни. | — |
419: | 6 | Изп | Подготвя **Ф7** в `varna_3d/data/`; пуска **ИА-16** (единайсетте разлики срещу черновия блоб) **без позиционен път** (ИА-О22) — **Ф7 се чете от диска по `--decisions-path` (блоб още няма; работно копие = блоб във varna_3d, червен ред 12 — ИА-О34)** — и отпечатва sha-то на записаното. `git add -- data/quarters_decisions_imot_2026-09-08.json`. **Не комитва.** | разлика извън списъка = **ИА-STOP 3** |
451: **Всяка отрицателна половина се вика така, че да пада по СВОЯТА проверка.** Гейтът приема `--only <ИА-номер>`, който изключва останалите. Всяка се записва с: командата, счупения вход, `--only`, **истинския изходен код** и първия ред от изхода.
452: 
453: | # | гейт | команда · кога | очаквано | отрицателна половина (ТРЯБВА да даде ≠ 0) |
454: |---|---|---|---|---|
455: | **ИА-1** | валидност ПРЕДИ поправка | Ф2, `<артефакт> --tiling …` · стъпки 9, 13, 18 | 0; „95 входни полигона · **0 невалидни преди поправка** · 79 доставяни клетки · **0 невалидни след канонизация**“ (М) | копие на снапшота с пръстен „папийонка“ (самопресичане) → 1 |

 succeeded in 367ms:
index.html
1774:    const response = await fetch('data/hydrants.json', { cache: 'no-cache' });
3277:    return fetch(url, { method: 'POST', headers: headers, body: JSON.stringify(body) })
4039:      const res = await fetch(url, { cache: 'no-store' });
4423:    const resp = await fetch(BUILDING_TOKEN_URL, { method: 'GET', mode: 'cors', credentials: 'omit' });
4586:    basemapManifestPromise = fetch(BASEMAP_MANIFEST_URL, { cache: 'no-store' })
5335:        const resp = await fetch(url, { cache: 'no-cache' });
5839:        const res = await fetch(detailUrlFor(g), ac ? { signal: ac.signal } : undefined);
5944:        const resp = await fetch(url, { cache: 'no-cache' });
6257:    const PLACES_URL = 'data/hotels.json', CATS_URL = 'data/place_categories.json';
6258:    const PLACES2_URL = 'data/places.json';            // фаза 2: училища/университети/болници/градини
6363:      // Фаза 2 Д3/К8 - the four src values of data/places.json, each naming its own
6693:        const resp = await fetch(url, ac ? { cache: 'no-cache', signal: ac.signal } : { cache: 'no-cache' });

 succeeded in 365ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
.gitignore:64:/scratch/boundary_gallery/	scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson
.gitignore:64:/scratch/boundary_gallery/	scratch/boundary_gallery/granitsi_preview_05.09/varna_dictionary_08.09.json
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p=Path('index.html');a=p.read_text(encoding='utf-8').splitlines()
for start,end in [(6253,6265),(6682,6703)]:
 for i in range(start-1,end): print(f'{i+1}: {a[i]}')
p=next(Path('docs/plans').glob('*imot_*-*_08.09.md'));a=p.read_text(encoding='utf-8').splitlines()
for i in range(371,377):
 s=re.sub(r'\\b[0-9a-fA-F]{64}\\b',lambda m:m[0][:8]+'...',a[i]);print(f'PLAN {i+1}: {s}')
'@ | python -" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
import json,hashlib,re,sys
sys.stdout.reconfigure(encoding='utf-8')
root=Path('scratch/boundary_gallery/granitsi_preview_05.09')
p=root/'varna_polygons_08.09.geojson';a=json.loads(p.read_bytes());f=a['features']
print('snapshot_meta_source=',json.dumps(a['_meta']['source'],ensure_ascii=False))
print('properties_src_values=',sorted({x['properties']['src'] for x in f}))
print('list_endpoint_present=',bool(a['_meta'].get('list_endpoint')))
print('feature_provenance_count=',sum(bool(x['properties'].get('provenance')) for x in f),'of',len(f))
for name in ('varna_polygons_08.09.geojson','varna_dictionary_08.09.json'):
 b=(root/name).read_bytes(); h=hashlib.sha256(b).hexdigest();print(name,'bytes=',len(b),'sha256_prefix=',h[:8])
 print('3d_copied_file_exists=',(Path('C:/git/varna_3d/data')/name).exists())
'@ | python -" in C:\git\Fire_Varna
 succeeded in 567ms:
6253:     const box = document.getElementById('placesSearchResults');
6254:     if (!inputEl || !theirsEl || !box) return;   // header markup missing -> no-op
6255: 
6256:     // ---- Б3 slice start (pure, DOM-free: constants → validators → cache → index → search) ----
6257:     const PLACES_URL = 'data/hotels.json', CATS_URL = 'data/place_categories.json';
6258:     const PLACES2_URL = 'data/places.json';            // фаза 2: училища/университети/болници/градини
6259:     // ADR 008 D8: the NAME is not a contract, the VERSION is — it changes with every
6260:     // change of the blobs. ЛОТ 1в-А rewrote all three (v2 → v3); ЛОТ 1в-Б added the
6261:     // `address` key to two of them (v3 → v4); ЛОТ 1в-В replaced the single `zone`
6262:     // with the three typed fields in all three, so v4 → v5 (the count stays 225).
6263:     // F12 (P7: М2+М3+М6) rewrites the VALUES of those fields — hotels with a named
6264:     // quarter 96 → 152, places 44 → 49 — so a device holding v5 must not answer
6265:     // from it: v5 → v6 (the count still stays 225).
6682:           if (Array.from(new Uint8Array(digest)).map((b) => b.toString(16).padStart(2, '0')).join('') !== sha) return null;
6683:         }
6684:         const data = JSON.parse(text);
6685:         return validate(data, text) ? data : null;
6686:       } catch (e) { return null; }
6687:     }
6688:     async function fetchValidatedJson(url, sha, validate) {
6689:       const ac = ('AbortController' in window) ? new AbortController() : null;
6690:       const timer = setTimeout(function () { if (ac) ac.abort(); }, FETCH_TIMEOUT_MS);   // covers text() too
6691:       let text = null;
6692:       try {
6693:         const resp = await fetch(url, ac ? { cache: 'no-cache', signal: ac.signal } : { cache: 'no-cache' });
6694:         if (resp.ok) text = await resp.text();
6695:       } catch (e) { text = null; }
6696:       clearTimeout(timer);
6697:       const fresh = await accept(text, sha, validate);
6698:       if (fresh) { cachePut(url, text); return fresh; }
6699:       return await accept(await cacheText(url), sha, validate);   // В7: a bad cache is ignored, not deleted
6700:     }
6701:     function ensurePlaces() {
6702:       if (placesPromise) return placesPromise;
6703:       placesPromise = (async function () {
PLAN 372: 
PLAN 373: **Г.7 · Входовете по sha — ОСЕМ (ИА-О34: регистърът е седмият; ИА-О35: v1 като диф-база е осмият), и ВСИЧКИТЕ ОСЕМ живеят в `_meta.inputs[]`** (така D10 е изпълнен буквално; другите `_meta` ключове само **препращат** към записа в `inputs`, не го заместват):
PLAN 374: 
PLAN 375: 1. полигоните (`77b40564…`, 175 736 B) — файл в `varna_3d/data/`;
PLAN 376: 2. речникът (`feba76e3…`, 6 274 B) + вграденото `(хешът на суровия отговор — само в снапшота, ИА-О32)` като несверяван свидетел;
PLAN 377: 3. тялото с решенията Ф7 — **прочетено като блоб на varna_3d** (`{path, rev, sha256, bytes}`); `_meta.decisions_sha256` / `decisions_commit` / `decisions_path` са същите стойности, изнесени поименно по образеца на v1;

 succeeded in 546ms:
snapshot_meta_source= "imot.bg — полигоните на районите, както ги чертае самият сайт (mob_api details → points)"
properties_src_values= ['imot.bg mob_api details (points of the район)']
list_endpoint_present= True
feature_provenance_count= 95 of 95
varna_polygons_08.09.geojson bytes= 175736 sha256_prefix= 77b40564
3d_copied_file_exists= False
varna_dictionary_08.09.json bytes= 6274 sha256_prefix= feba76e3
3d_copied_file_exists= False

codex
Намерих конкретна неточност: ИА-О40 посочва грешна стойност за входното `_meta.source`. Провенансът е запазен във файла, а грешният цитат не участва в гейт или инструкция за четене на входа. Базата с 14 стейджнати пътя и двете чужди работни дървета се възпроизвежда; остава да формулирам точно ограниченията на присъдата за старт.

codex
**S41-1 — ПРИЕМАМ.** Снимката е локален вход; планът предписва байтово копиране и проверка на пиновете, без заявка към imot.bg. Единственото съвпадение във `varna_3d/src` е дори в **списъка със забранени домейни**, а не извикване на сайта. Спирането му не прекъсва използването на запазената снимка; прекъсва придобиването на следваща.

**М:** сканиране за `imot[._-]bg` → Fire_Varna: **15 файла, 0 съвпадения**; `varna_3d/src`: **147 файла, само `verify_web_rows.py`**. **Ч:** [забраненият домейн:102](C:/git/varna_3d/src/verify_web_rows.py:102), [локалните URL:6257](C:/git/Fire_Varna/index.html:6257), [пиновете:375](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:375), [копирането:416](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:416).

**S41-2 — ПРИЕМАМ за преименуването.** Двете нови имена са съгласувани във всички посочени места; ИА-1 използва аргумента `--tiling` и не съдържа старо име. Търсенето в трите документа и игнорираната папка намира **0 стари имена**, включително сред имената на файловете. Измерените байтове и пълните дайджести съвпадат с пиновете; независимо историческо сравнение „преди/след“ не е правено.

**М:** `len(p.read_bytes()), hashlib.sha256(p.read_bytes()).hexdigest()[:8]` → полигони **175736 / `77b40564`**, речник **6274 / `feba76e3`**; `full_digest in plan_text` → **True / True**. **Ч:** [Ф5/Ф6:270](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:270), [Т1:285](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:285), [К2:505](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:505), [ADR:9](C:/git/Fire_Varna/docs/decisions/011_kartata_imot.md:9), [състояние:183](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:183).

**S41-3 — ОБОРВАМ точната стойност.** Входното `_meta.source` **не е** `imot_bg_tiling`; ИА-О40 смесва входния провенанс с предписаното **изходно** `Feature.properties.source`. Независимостта от файловото име обаче е вярна: `_meta.list_endpoint` присъства и **95/95 Feature-а** имат провенанс. Неточността е описателна — не намерих входен гейт, зависещ от грешния литерал.

**М:** `python -X utf8 -B -c "import json;print(json.load(open('scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson',encoding='utf-8'))['_meta']['source'])"` → `imot.bg — полигоните на районите, както ги чертае самият сайт (mob_api details → points)`. **Ч:** [грешният цитат:258](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:258), [изходното поле:344](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:344).

**S41-4 — С УГОВОРКА.** Посочената работна база се възпроизвежда. Последните три раздела са ГОДНО: **9 „мерки“ и двете лещи на 10**; формулировката за всички проверки 8–10 заличава по-ранните НЕГОДНО на 8 „мерки“ и 9 „изпълнимост“. Стъпка 0 предхожда Gate 1/К1, затова липсващият подписан банер не блокира началната мярка.

**М:** `git diff --cached --name-status` → **14: 9 M / 4 A / 1 D**; `git worktree list` → основното + **две чужди дървета**; `git -C C:/git/varna_3d log -1 --format=%h` → **`05f485e`**, `branch --show-current` → **`rezhimi`**. **Ч:** [старите присъди:759](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:759), [:811](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:811), [последните раздели:826](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:826), [:849](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:849), [:877](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:877).

**S41-5 — С УГОВОРКА.** Забраната за публична геометрия е ясна и провереният Б3 индекс е чист. Това доказва ограничения проверен обхват: `b3_g11` проверява JSON/GeoJSON, ИА-7 — Ф7, ИА-19 — координатни числа в трите документа. Зелените резултати не са всеобхватно доказателство за целия публичен репозиторий.

**М:** `python -B gates/probe/b3_g11.py HEAD --cached` → `{"scope":19,"geo_hits":[],"unreadable":[],"stray_new":[]}`, **изход 0**. **Ч:** [обхватът:105](C:/git/Fire_Varna/gates/probe/b3_g11.py:105), [ИА-7:461](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:461), [ИА-19:473](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:473).

**S41-6 — ГОДНО за старт на Изпълнителя от стъпка 0.**

1. Архитектът да поправи описанието на `_meta.source` преди К1; **снимката не се „поправя“** — това би нарушило пина.
2. Запазват се Б3 индексът и чуждите дървета. Н7 не се изпълнява в живото дърво; Н9 записва в игнорирана папка, затова не е пускан при този одит само с четене ([план:241](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:241), [:413](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:413)).
3. Преди първата редакция се следват Gate 1 и К1; И-А не разрешава публична доставка ([план:414](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:414), [:5](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:5)).
tokens used
75,993
**S41-1 — ПРИЕМАМ.** Снимката е локален вход; планът предписва байтово копиране и проверка на пиновете, без заявка към imot.bg. Единственото съвпадение във `varna_3d/src` е дори в **списъка със забранени домейни**, а не извикване на сайта. Спирането му не прекъсва използването на запазената снимка; прекъсва придобиването на следваща.

**М:** сканиране за `imot[._-]bg` → Fire_Varna: **15 файла, 0 съвпадения**; `varna_3d/src`: **147 файла, само `verify_web_rows.py`**. **Ч:** [забраненият домейн:102](C:/git/varna_3d/src/verify_web_rows.py:102), [локалните URL:6257](C:/git/Fire_Varna/index.html:6257), [пиновете:375](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:375), [копирането:416](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:416).

**S41-2 — ПРИЕМАМ за преименуването.** Двете нови имена са съгласувани във всички посочени места; ИА-1 използва аргумента `--tiling` и не съдържа старо име. Търсенето в трите документа и игнорираната папка намира **0 стари имена**, включително сред имената на файловете. Измерените байтове и пълните дайджести съвпадат с пиновете; независимо историческо сравнение „преди/след“ не е правено.

**М:** `len(p.read_bytes()), hashlib.sha256(p.read_bytes()).hexdigest()[:8]` → полигони **175736 / `77b40564`**, речник **6274 / `feba76e3`**; `full_digest in plan_text` → **True / True**. **Ч:** [Ф5/Ф6:270](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:270), [Т1:285](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:285), [К2:505](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:505), [ADR:9](C:/git/Fire_Varna/docs/decisions/011_kartata_imot.md:9), [състояние:183](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:183).

**S41-3 — ОБОРВАМ точната стойност.** Входното `_meta.source` **не е** `imot_bg_tiling`; ИА-О40 смесва входния провенанс с предписаното **изходно** `Feature.properties.source`. Независимостта от файловото име обаче е вярна: `_meta.list_endpoint` присъства и **95/95 Feature-а** имат провенанс. Неточността е описателна — не намерих входен гейт, зависещ от грешния литерал.

**М:** `python -X utf8 -B -c "import json;print(json.load(open('scratch/boundary_gallery/granitsi_preview_05.09/varna_polygons_08.09.geojson',encoding='utf-8'))['_meta']['source'])"` → `imot.bg — полигоните на районите, както ги чертае самият сайт (mob_api details → points)`. **Ч:** [грешният цитат:258](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:258), [изходното поле:344](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:344).

**S41-4 — С УГОВОРКА.** Посочената работна база се възпроизвежда. Последните три раздела са ГОДНО: **9 „мерки“ и двете лещи на 10**; формулировката за всички проверки 8–10 заличава по-ранните НЕГОДНО на 8 „мерки“ и 9 „изпълнимост“. Стъпка 0 предхожда Gate 1/К1, затова липсващият подписан банер не блокира началната мярка.

**М:** `git diff --cached --name-status` → **14: 9 M / 4 A / 1 D**; `git worktree list` → основното + **две чужди дървета**; `git -C C:/git/varna_3d log -1 --format=%h` → **`05f485e`**, `branch --show-current` → **`rezhimi`**. **Ч:** [старите присъди:759](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:759), [:811](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:811), [последните раздели:826](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:826), [:849](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:849), [:877](C:/git/Fire_Varna/scratch/places_search/karta_imot_plan_reviews_08.09.md:877).

**S41-5 — С УГОВОРКА.** Забраната за публична геометрия е ясна и провереният Б3 индекс е чист. Това доказва ограничения проверен обхват: `b3_g11` проверява JSON/GeoJSON, ИА-7 — Ф7, ИА-19 — координатни числа в трите документа. Зелените резултати не са всеобхватно доказателство за целия публичен репозиторий.

**М:** `python -B gates/probe/b3_g11.py HEAD --cached` → `{"scope":19,"geo_hits":[],"unreadable":[],"stray_new":[]}`, **изход 0**. **Ч:** [обхватът:105](C:/git/Fire_Varna/gates/probe/b3_g11.py:105), [ИА-7:461](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:461), [ИА-19:473](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:473).

**S41-6 — ГОДНО за старт на Изпълнителя от стъпка 0.**

1. Архитектът да поправи описанието на `_meta.source` преди К1; **снимката не се „поправя“** — това би нарушило пина.
2. Запазват се Б3 индексът и чуждите дървета. Н7 не се изпълнява в живото дърво; Н9 записва в игнорирана папка, затова не е пускан при този одит само с четене ([план:241](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:241), [:413](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:413)).
3. Преди първата редакция се следват Gate 1 и К1; И-А не разрешава публична доставка ([план:414](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:414), [:5](C:/git/Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:5)).
