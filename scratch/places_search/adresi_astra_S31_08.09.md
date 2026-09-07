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
session id: 01a07d9d-b182-74d1-9412-b08da4c8bad5
--------
user
S31 · Външно око (леща механика), read-only: КАК да поправим кварталните думи на адресите във Fire_Varna. Находка на Петър при локалния преглед: адресната търсачка дава „кв. Чайка, Студентска бл. 11“ и „кв. Левски, ул. Битоля 13“, докато подписаните квартални полигони (varna_3d data/quarters_signed.geojson, 05f485e; 60 полигона, частни) казват друго (Студентска бл. 11 е ВЪТРЕ в кв. Левски, 59 m от ръба; цялата Битоля е ИЗВЪН всички полигони — дупката „Цветен квартал“). Мярката: scratch/places_search/adresi_po_poligon_measure_08.09.md (+ .json): от 86 232 записа с координата в data/search_index.json — 6 655 съгласни, 8 384 несъгласни (системни класове: кадастралната „зона Виница“ върху Манастирски рид/Акчелар/Ален мак/Бриз/…; Колхозен пазар→Тракия; Цветен квартал→Левски; Чайка→Левски при Студентска; „микрорайон“→Гръцката махала/Център), **57 928 вътре в полигон БЕЗ квартална дума**, 13 265 извън всички полигони (Център 753 без полигон, Левски 478, Колхозен пазар 490, Цветен квартал 197, Чайка 219…). Кварталната дума qtk идва от кадастралния адрес през генератора C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs (+ lib_quarter_registry.mjs; там вече има ЗОНОВ механизъм Р38 за кв. Виница: VINITSA_TOKEN се ДОБАВЯ към qtk, никога не се маха — вж. редове ~140-170 и ~870-910) и build_fire_varna_address_rows.mjs; клиентът index.html (адресната търсачка ~4816-4870, ~5130-5260, approx ~5972-6070) чете tk/qtk/dtk и НЕ прави point-in-polygon. Принципът на Петър: „координатата решава квартала, името е свидетел“ (docs/decisions/010_signed_quarter_boundaries.md; памет). Ограничения: нула геометрия в публичното репо (полигоните остават във varna_3d; публично пътува само думата); лот Б3 (docs/plans/ПЛАН_Б3_07.09.md §10) изрично НЕ пипа адресната търсачка — това е ОТДЕЛЕН лот след Б3; D13 подредена тройка при всяка доставка на data/; гейтът на търсенето (tests/test_places_search_gate.py, scratch/places_search/expectations.json, recall_sweep.py) замразява резултатите. Въпроси: (1) къде е правилното място на поправката — генераторът във Varna_buildings (point-in-polygon с частните полигони при билд, qtk ДОБАВЯ токените на подписания квартал, display label от полигона, кадастралната дума остава като свидетел/alias) или другаде; кой файл/функция; (2) какво става с 13 265 записа извън полигони и с 57 928 без дума — политика (район само? „без квартал“?), и кои дупки искат решение на Петър преди билда (Център, Цветен квартал, Колхозен пазар, ръбът 100 m); (3) какъв е удaрът върху search_index.json (размер 11,2 MB, 5 MB праг за първо зареждане не важи — lazy), върху approx адресите, върху замразения корпус и гейтовете — какъв кръг делти; (4) минималната форма на лота (write-set, гейтове с отрицателни половини, D13, какво подписва Петър) и рисковете; (5) провери мярката ми за грешки в метода (транслитерация на qtk срещу имената; „най-малкият съдържащ полигон“; съгласие по токен). Измервай сам където можеш (Varna_buildings е четимо: git -C C:/git/Varna_buildings; search_index.json е в Fire_Varna/data). Не пипай нищо, не комитвай, нищо към отдалечено хранилище. Отговор до 900 думи: препоръка + условия, с доказателства path:line или числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя мярката и пътя от генераторите до търсачката, само с четене. Ще отделя механичната поправка от решенията за квартални граници, които трябва да подпишеш.

2026-09-07T20:45:10.871182Z ERROR codex_core::tools::router: error=exec_command failed: CreateProcess { message: "Rejected(\"Failed to create unified exec process: CreateProcessWithLogonW failed: 1056\")" }
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git -C C:/git/Varna_buildings status -sb' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -TotalCount 150' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git ls-files -- AGENTS.md CLAUDE.md docs/activeContext.md docs/decisions/010_signed_quarter_boundaries.md 'docs/plans/ПЛАН_Б3_07.09.md' data/search_index.json data/address_rows.json index.html tests/test_places_search_gate.py scratch/places_search scripts" in C:\git\Fire_Varna
 exited 1 in 404ms:
fatal: detected dubious ownership in repository at 'C:/git/Varna_buildings'
'C:/git/Varna_buildings' is owned by:
	BUILTIN/Administrators (S-1-5-32-544)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/Varna_buildings

 succeeded in 397ms:
AGENTS.md
CLAUDE.md
data/address_rows.json
data/search_index.json
docs/activeContext.md
docs/decisions/010_signed_quarter_boundaries.md
docs/plans/ПЛАН_Б3_07.09.md
index.html
scratch/places_search/.gitignore
scratch/places_search/adresi_po_poligon_measure_08.09.json
scratch/places_search/adresi_po_poligon_measure_08.09.md
scratch/places_search/agkk_inspire_2026-09-05/varna_municipality_kvartali_hub_meta_2026-09-05.json
scratch/places_search/agkk_inspire_measure_05.09.md
scratch/places_search/baseline_02.09.md
scratch/places_search/check_municipal_kvartali.py
scratch/places_search/derived_boundaries_measure_05.09.md
scratch/places_search/district_resolutions_2026-09-07.json
scratch/places_search/expectations.json
scratch/places_search/gen_m7_tokens.py
scratch/places_search/golden_panel_synthesis.md
scratch/places_search/granitsi_am2_astra_S14-S19_06.09.md
scratch/places_search/granitsi_am2_astra_S20_verify_06.09.md
scratch/places_search/granitsi_am2_brief_astra.md
scratch/places_search/granitsi_am2_brief_kimi.md
scratch/places_search/granitsi_am2_kimi_K15-K20_06.09.md
scratch/places_search/granitsi_am2_kimi_K21_verdict_06.09.md
scratch/places_search/granitsi_am3_astra_S25_07.09.md
scratch/places_search/granitsi_am3_kimi_K26_07.09.md
scratch/places_search/granitsi_astra_official_boundaries_05.09.md
scratch/places_search/granitsi_b1v2_astra_S23_07.09.md
scratch/places_search/granitsi_b1v2_kimi_K24_07.09.md
scratch/places_search/granitsi_b1v4_astra_S24_07.09.md
scratch/places_search/granitsi_b1v4_kimi_K25_07.09.md
scratch/places_search/granitsi_b2_astra_S26_07.09.md
scratch/places_search/granitsi_b2_astra_S27_07.09.md
scratch/places_search/granitsi_b2_kimi_K27_07.09.md
scratch/places_search/granitsi_b3_astra_S28_07.09.md
scratch/places_search/granitsi_b3_astra_S29_07.09.md
scratch/places_search/granitsi_b3_astra_S30_07.09.md
scratch/places_search/granitsi_b3_kimi_K28_07.09.md
scratch/places_search/granitsi_b3_kimi_K29_07.09.md
scratch/places_search/granitsi_b3_kimi_K30_07.09.md
scratch/places_search/granitsi_b3_kimi_K31_07.09.md
scratch/places_search/granitsi_blocks_astra_B1-B6_05.09.md
scratch/places_search/granitsi_blocks_brief_astra.md
scratch/places_search/granitsi_blocks_brief_kimi.md
scratch/places_search/granitsi_blocks_kimi_B1-B6_05.09.md
scratch/places_search/granitsi_decisions_2026-09-06_proba.json
scratch/places_search/granitsi_decisions_2_2026-09-06_proba.json
scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json
scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json
scratch/places_search/granitsi_fixtures_07.09.json
scratch/places_search/granitsi_forumi_astra_T1-T4_06.09.md
scratch/places_search/granitsi_forumi_brief_astra.md
scratch/places_search/granitsi_forumi_brief_kimi.md
scratch/places_search/granitsi_forumi_kimi_F1-F5_06.09.md
scratch/places_search/granitsi_night_astra_S21_06.09.md
scratch/places_search/granitsi_night_astra_S22_review_07.09.md
scratch/places_search/granitsi_night_kimi_K22_06.09.md
scratch/places_search/granitsi_night_kimi_K23_review_07.09.md
scratch/places_search/granitsi_osm_astra_A1-A4_05.09.md
scratch/places_search/granitsi_osm_brief_astra.md
scratch/places_search/granitsi_osm_brief_kimi.md
scratch/places_search/granitsi_osm_kimi_T1-T5_05.09.md
scratch/places_search/granitsi_rayoni_astra_R0-R6_05.09.md
scratch/places_search/granitsi_rayoni_brief_astra.md
scratch/places_search/granitsi_rayoni_brief_kimi.md
scratch/places_search/granitsi_rayoni_kimi_P1-P5_05.09.md
scratch/places_search/granitsi_v2_astra_S7-S13_05.09.md
scratch/places_search/granitsi_v2_brief_astra.md
scratch/places_search/granitsi_v2_brief_kimi.md
scratch/places_search/granitsi_v2_kimi_K8-K14_05.09.md
scratch/places_search/granitsi_zoniraine_brief_kimi.md
scratch/places_search/granitsi_zonirane_kimi_Z1-Z5_05.09.md
scratch/places_search/lot1_reference_preview_v2.md
scratch/places_search/lot1v_addr_join.json
scratch/places_search/lot1v_addresses_for_signature.md
scratch/places_search/lot1v_brief_kimi.md
scratch/places_search/lot1v_brief_sol.md
scratch/places_search/lot1v_v_brief_kimi.md
scratch/places_search/lot1v_v_brief_sol.md
scratch/places_search/lot1v_v_manifest_BASE_P7.json
scratch/places_search/lot1v_v_manifest_P7_F12.json
scratch/places_search/lot1v_v_reference_manifest.json
scratch/places_search/lot1v_v_zones_for_signature.md
scratch/places_search/m7_significance_gate.py
scratch/places_search/m7_trigger_tokens.json
scratch/places_search/manifest_anchor_gate.py
scratch/places_search/manifest_before.json
scratch/places_search/municipal_kvartali_layer_05.09.md
scratch/places_search/noshtna_pins_06.09.json
scratch/places_search/osm_quarters_measure_05.09.md
scratch/places_search/p7_attack_brief.md
scratch/places_search/p7_zone_aliases.json
scratch/places_search/p7_zone_aliases_v2.json
scratch/places_search/probe_out/after.json
scratch/places_search/probe_out/after_requests.json
scratch/places_search/probe_out/before.json
scratch/places_search/probe_out/before_requests.json
scratch/places_search/probe_out/g4.json
scratch/places_search/probe_out/screens/hospital.png
scratch/places_search/probe_out/screens/hotel.png
scratch/places_search/probe_out/screens/school.png
scratch/places_search/probe_out/token_parity.json
scratch/places_search/probe_places_fv.mjs
scratch/places_search/qa_night_acceptance.py
scratch/places_search/qa_night_pins.py
scratch/places_search/recall_sweep.py
scratch/places_search/recall_sweep_rows.json
scratch/places_search/wikimapia_frozen_measure_06.09.md
scratch/places_search/wikimapia_petar_notes_06.09.md
scratch/places_search/wikimapia_terms_2026-09-06.md
scratch/places_search/БОРД_истинност_375.md
scratch/places_search/ЗА_ПОДПИС_A.md
scratch/places_search/КАРТА_на_състоянието_05.09.md
scratch/places_search/ОБОРВАНЕ_ПЛАН_Ред_05.09.md
scratch/places_search/ОДИТ_A210_05.09.md
scratch/places_search/ОДИТ_A211_05.09.md
scratch/places_search/ОДИТ_A29_05.09.md
scratch/places_search/ОДИТ_ЛОТ0_05.09.md
scratch/places_search/ОДИТ_ЛОТ0fix_05.09.md
scratch/places_search/ОТЧЕТ_A211_05.09.md
scratch/places_search/ОТЧЕТ_Ф0б_05.09.md
scratch/places_search/ПРЕГЛЕД_търговско-обществени_03.09.md
scratch/places_search/ЧЕРНОВА_ПЛАН_Ред_05.09.md
scripts/apply_approved_reports.py
scripts/backfill_addresses_20260511.py
scripts/backfill_verified_type_20260509.py
scripts/copy_basemap_release.py
scripts/hooks/pre-push
scripts/import_etr_kmz.py
scripts/lib/__init__.py
scripts/lib/hydrant_core.py
scripts/migrate_to_verbose_schema.py
scripts/replay_historical_new_hydrant.py
scripts/vendor_basemap_deps.mjs
tests/test_places_search_gate.py

 succeeded in 538ms:
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git -c safe.directory=C:/git/Fire_Varna status -sb' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath docs/activeContext.md -Encoding UTF8 -TotalCount 65' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$paths = @('"'AGENTS.md','CLAUDE.md','docs/activeContext.md','docs/decisions/010_signed_quarter_boundaries.md','docs/plans/ПЛАН_Б3_07.09.md'); "'$paths | Sort-Object | ForEach-Object { if (Test-Path -LiteralPath $_) { $_ } else { '"'MISSING ' + "'$_ } }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'D13|100 m|100м|100 м|подреден|адресн|подпис|Статус' -- docs/decisions/010_signed_quarter_boundaries.md docs/plans/ПЛАН_Б3_07.09.md AGENTS.md CLAUDE.md" in C:\git\Fire_Varna
 succeeded in 372ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 100]
M  data/hotels.json
M  data/place_categories.json
M  data/places.json
A  gates/probe/b3_g11.py
M  index.html
D  scratch/places_search/granitsi_fixtures_06.09.json
A  scratch/places_search/granitsi_fixtures_07.09.json
 M scratch/places_search/lot1v_v_reference_manifest.json
 M scratch/places_search/probe_out/token_parity.json
M  scratch/places_search/recall_sweep.py
A  tests/granitsi_client_probe.mjs
A  tests/test_b3_gates.py
M  tests/test_granitsi_fixtures.py
M  tests/test_hotels_public_bundle.py
M  tests/test_places_public_bundle.py
?? scratch/places_search/COMMIT_MSG_B3.txt
?? scratch/places_search/adresi_astra_S31_08.09.md
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

 succeeded in 535ms:
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

 succeeded in 414ms:
AGENTS.md
docs/decisions/010_signed_quarter_boundaries.md
docs/plans/ПЛАН_Б3_07.09.md

 succeeded in 656ms:
AGENTS.md
CLAUDE.md
docs/activeContext.md
docs/decisions/010_signed_quarter_boundaries.md
docs/plans/ПЛАН_Б3_07.09.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath docs/decisions/010_signed_quarter_boundaries.md -Encoding UTF8 -TotalCount 150 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'D13|100 m|100м|100 м|подреден|адресн|"'^##|Статус|подписан'"' -- docs/plans/ПЛАН_Б3_07.09.md" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git -c safe.directory=C:/git/Fire_Varna rev-parse HEAD' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -LiteralPath CLAUDE.md -Encoding UTF8 -TotalCount 150 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 411ms:
1:# ПЛАН Б3 · Търсене по квартал над подписаните граници (Fire_Varna) — v3
3:[Omitted long matching line]
4:[Omitted long matching line]
13:## 0 · Червени редове (наследени, без изключение)
21:[Omitted long matching line]
32:[Omitted long matching line]
36:## 1 · Мярка (базата, преди един ред промяна)
38:### 1.1 Състояние на репата — **преизмерено 07.09, котвата се движи**
53:### 1.2 Днешните котви в `C:/git/Fire_Varna/index.html`
78:[Omitted long matching line]
82:### 1.3 Липсващите кодове
89:### 1.4 Новите пинове (LF-блобове от git, не от диска)
110:### 1.5 Какво носи доставката — **преизмерено, с поправка на v2**
123:### 1.5б 🔴 `_meta` — точните множества ключове (единственият авторитет на G17)
134:### 1.6 Какво умира днес, ако блобовете влязат сами — **изпълнено, не изведено** 🔴
147:### 1.7 Референцията и фикстурите
181:### 1.8 🔴 Мерките, които оборванията добавиха (новите СТОП-числа)
185:[Omitted long matching line]
188:[Omitted long matching line]
206:[Omitted long matching line]

 succeeded in 476ms:
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
74: **D19 · Интервалът на замразяването е обявен, изброен и ограден.** `location_phrases` е подписана претенция в `expectations.json` (`tests/test_places_search_gate.py:464-478` я сверява с `REF.LOC_PHRASES`), а `--freeze` пренаписва очакванията едва СЛЕД подписа (амандамент №11 т. 3). Значи между F13-а и единственото `--freeze` `python -m unittest discover -s tests` е червен по конструкция. Това не е „червено по замисъл“, а **обявен интервал с гейт**: изпълнителят записва при отварянето му ТОЧНИЯ набор падащи тестове (G20), той трябва да е подмножество на назования в плана §2, всеки тест извън набора = STOP, и след `--freeze` наборът е ПРАЗЕН. Интервалът не пресича нито един гейт-ред, който твърди зелено.
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

 succeeded in 411ms:
321d209d30478e150327f7a5a1f69f33c68520aa

 succeeded in 546ms:
1: # CLAUDE.md
2: 
3: > **Canonical current state:** see `docs/activeContext.md` (last updated commit hash and sprint status). If this file conflicts with `activeContext.md`, the latter wins.
4: >
5: > Instructions for **Claude Code** working in this repo.
6: > Read `AGENTS.md` first for project context, dataset rules, and constraints.
7: 
8: ---
9: 
10: ## Orientation (repo · trunk · forbidden · entry point · live numbers)
11: 
12: - **What this repo is.** `Fire_Varna` — the mobile-first web app that shows a firefighter the nearest working fire hydrant in Varna oblast, in the browser, with no install and no account (`README.md` § Български). The app shell (`index.html`), the dataset (`data/`), the ingest and audit scripts (`scripts/`, `audit/`), the tests (`tests/`), the Cloudflare Worker source (`worker/`) and the governance documents (`docs/`) all live in this one repo.
13: - **Trunk.** `main` — GitHub's default branch (`git symbolic-ref refs/remotes/origin/HEAD` → `refs/remotes/origin/main`) and the branch the site is published from ([AGENTS.md § What This Project Is](AGENTS.md#what-this-project-is): "Distribution: GitHub Pages from `main`"). Work commits land here; every other branch is a frozen trace of a past cycle, listed by `git branch -avv` and dated by `git for-each-ref --sort=-committerdate --format='%(refname:short) %(committerdate:short)' refs/heads refs/remotes`. Petar alone pushes (Gate 2), so `main` can stand ahead of `origin/main` between his pushes — measure that with `git rev-list --count origin/main..main`, never resolve it with `git push`.
14: - **What is forbidden here.** § Hard Rules below — never push · never commit secrets · field-report PII gate · destructive-op gate · cross-repo isolation · no automated commits — plus [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). A rule you are about to bend is the signal to stop and ask, not to improvise.
15: - **Entry point.** [`docs/activeContext.md`](docs/activeContext.md#current-state) — read it before anything else when resuming work. On current state it wins over this file (see the header above).
16: - **Live numbers.** No state number enters this file. Record counts, byte sizes and commit hashes live in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state) — one truth per document. The numbers that do stay here are rules, not state: the 15 s poll interval (`POLL_INTERVAL_MS`), the 5 MB first-load hard cap ([AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints)), `HEADING_SMOOTHING = 0.10`. If you need a fresh count, run the command — do not write the result into this file.
17: 
18: ---
19: 
20: ## Your Role
21: 
22: You are the **Executor** in the dual-Claude-Code pipeline. See `AGENTS.md` § Dual-Claude-Code workflow, and ADR [`docs/decisions/003_dual_claude_code_governance.md`](docs/decisions/003_dual_claude_code_governance.md).
23: 
24: | Role | Agent | What it does |
25: |---|---|---|
26: | **Planner** | Claude Code — read-only (model per `~/.claude/agents`) | Plans, architects, measures, drafts the plan. Never edits or commits. |
27: | **Researcher** | Claude Code — read-only (model per `~/.claude/agents`) | Planner sub-phase: gathers evidence and measurements. Never edits. |
28: | **Executor (you)** | Claude Code (model per `~/.claude/agents`) | Implements the signed plan, edits files, commits locally. Never pushes, never architects. |
29: | **Auditor** | Claude Code — read-only, adversarial (model per `~/.claude/agents`) | Independently checks the Executor's diff against the plan. Never edits. |
30: | **Orchestrator** | Petar | Signs plans (Gate 1), reviews diffs (Gate 2), pushes. Sole push authority. |
31: 
32: If you receive a task without an approved plan from the **Planner** (read-only; model per `~/.claude/agents`), signed by Petar, stop and ask. Do not improvise architecture.
33: 
34: ---
35: 
36: ## Hard Rules
37: 
38: Project-wide constraints (size budget, static hosting, Bulgarian UI labels, dependencies, mobile-first, HTTPS-required APIs, Varna-only scope) are canonical in [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). Stop and ask if an approved plan would violate them.
39: 
40: ### Non-negotiable guardrails (harmonized with Varna_buildings)
41: 
42: 1. **Never run `git push`.** Petar pushes manually after reviewing commits locally, at Gate 2. This holds with any flag; never use `--no-verify` and never bypass the pre-push hook.
43: 2. **Never commit secrets.** No Cloudflare API tokens, Worker deploy credentials, `wrangler` secrets, `.dev.vars`, or `.env` files ever enter the repo. Verify `.gitignore` covers them before staging if in doubt.
44: 3. **Field-report / PII gate.** Treat field-report submissions as personal data: reject by default, and scrub any identifying content before persisting to `data/` or creating a GitHub issue. Stop and ask before persisting anything that could carry PII.
45: 4. **Destructive-op gate.** If you discover unexpected state — unfamiliar branches, uncommitted changes, files you did not create — investigate before deleting or overwriting. It may be Petar's in-progress work.
46: 5. **Cross-repo isolation.** Do not touch the `Varna_buildings` checkout, or any other repo, from here. Work stays inside `C:\git\Fire_Varna`.
47: 6. **No automated commits.** One logical change per commit, staged with explicit paths, using the exact commit message from the approved plan.
48: 
49: ### Per-commit execution protocol
50: 
51: For each commit in an approved plan:
52: 
53: 1. Read the commit specification in the plan.
54: 2. Verify dependencies on earlier commits are met.
55: 3. Create or modify only the files the spec names.
56: 4. Stage those files with **explicit paths** (never `git add -A` / `git add .`) and commit with the **exact** message from the plan.
57: 5. Run `git status --short` to confirm only the intended files were committed and pre-existing dirty/untracked files were left untouched.
58: 6. Report commit number, hash, files, and acceptance-check result.
59: 7. If an acceptance check fails, **stop and ask Petar.** Do not roll forward with a broken commit.
60: 
61: ---
62: 
63: ## Code Style
64: 
65: This codebase is read primarily by AI agents and a non-CS-trained owner.
66: 
67: - Clear names over short names.
68: - Comments explain **why**, not **what**.
69: - No clever one-liners. No premature abstraction.
70: - One concern per function.
71: - No dead code. If you replace something, delete the old version.
72: 
73: ---
74: 
75: ## Specific Gotchas
76: 
77: - **`deviceorientation` fires at 100-200Hz on Android.** EMA must run on `requestAnimationFrame`, reading the latest stored raw heading. Do not EMA inside the event handler. `HEADING_SMOOTHING = 0.10`.
78: - **All map markers use `L.divIcon`**, never `L.icon`.
79: - **`L.markerClusterGroup` is used only in "Всички" mode.** Other modes use plain numbered pins. Do not unify this.
80: - **Map auto-fit happens at three sites, never on routine GPS updates:** the first GPS lock (`refresh(!deepLinkFramed)` — skipped when a `?h=` deep link already framed the map on one hydrant), `setMode()`, and the manual-position map click. Routine GPS ticks call `refresh(false)`.
81: - **Tap and long-press differ intentionally.** Tap selects/activates a hydrant; long-press opens the report menu.
82: - **`targetCardHTML()` builds the card HTML into `modalBody.innerHTML` at two call sites.** In `showReportModal()` the listeners are re-attached right after by `wireReporterBar()` + `wireFormHandlers()`; in `showReportTypePicker()` by `wireReporterBar()` + the inline `.type-btn` handlers; preserve that unless a refactor explicitly changes it.
83: - **Polling interval is fixed at 15 s (`POLL_INTERVAL_MS`).** Do not lower without coordinating Worker KV cache TTL (currently 30 s) and reviewing the rate math in `docs/plans/commit_15_worker_get.md`.
84: - **Polling must never block the UI thread.** All work happens inside `async pollIssues()` with a `setTimeout` schedule. Do not call `refresh()` from polling and do not introduce synchronous JSON-walking over the full `HYDRANTS` array.
85: - **Polling pauses while the tab is hidden** (`document.hidden`) and fires one immediate catch-up poll on return. Preserve both halves — losing the catch-up means stale pins after long backgrounding.
86: - **Polling updates pins via `marker.setIcon` and `marker.setLatLng`, never by rebuilding** the cluster or calling `refresh()`. Marker tags `_hydrantId` / `_pinKind` / `_rank` / `_isActivePin` are set in `refresh()` and consumed by the polling code; mutating them outside `refresh()` will leak the active-pin flag across transitions.
87: - **`lastPollSince` only advances on a successful, parseable response.** Failures (network, non-2xx, invalid JSON) keep the cursor where it was so the next poll re-requests the same window.
88: 
89: ---
90: 
91: ## Field Report Ingest Rules
92: 
93: See [AGENTS.md § Wrong-Location Ingest Rule](AGENTS.md#wrong-location-ingest-rule) for the canonical table and rules. Stop and ask before any data edit unless the approved plan names the affected report IDs.
94: 
95: A canonical coordinate mutation follows the **Measurement Doctrine** — ADR [`docs/decisions/004_measurement_doctrine.md`](docs/decisions/004_measurement_doctrine.md) (references Varna_buildings ADR 058): clear the acceptance floor before mutating `coords`; Google terrain-eyes may only refute / downgrade / trigger a re-check, never rewrite a coordinate alone, never be cached or fed back to OSM.
96: 
97: ---
98: 
99: ## Report Flow
100: 
101: See [AGENTS.md § Report Flow](AGENTS.md#report-flow) and [docs/activeContext.md § Current State](docs/activeContext.md#current-state).
102: 
103: ---
104: 
105: ## Verification
106: 
107: No CI yet, but tests exist (`tests/`, Python `unittest`). When ingest or shared-core (`scripts/lib/hydrant_core.py`) behavior is relevant, run the suite:
108: 
109: ```powershell
110: python -m unittest discover -s tests
111: ```
112: 
113: For frontend / deployable changes, before reporting done:
114: 
115: 1. Serve locally over HTTP:
116: 
117:    ```powershell
118:    python -m http.server 8000
119:    ```
120: 
121: 2. Open at 375px viewport width and check:
122:    - Map renders within 3 seconds.
123:    - Browser console has no runtime errors.
124:    - `data/hydrants.json` loads with HTTP 200.
125:    - `JSON.parse(document.getElementById('hydrantData').textContent).length` equals the record count declared in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state) — the count is not written here; read it there, or measure `data/hydrants.json` yourself.
126:    - GPS lock works, or graceful error pill with retry/manual controls appears.
127:    - All 3 view modes render correctly: "Близо", "Топ 5", "Всички".
128:    - Cluster mode shows clusters when zoomed out.
129:    - Building detail sheet (`.detail-sheet`, the C4 search result) opens and closes; the hydrant bottom sheet no longer exists — it was removed in the popup pivot.
130:    - Compass cone rotates with simulated `deviceorientation` events.
131:    - FAB `+` opens the report-type menu.
132:    - Long-press on a verified pin opens the report menu.
133:    - Follow mode recenters; user pan exits follow mode.
134:    - Manual position mode accepts a map click.
135:    - Report submit uses Worker `fetch` POST and queues locally if offline.
136: 
137: 3. Report `index.html` and `data/hydrants.json` sizes after changes.
138: 
139: ---
140: 
141: ## Windows Dev Environment
142: 
143: See [AGENTS.md § Windows Dev Environment](AGENTS.md#windows-dev-environment).
144: 
145: ---
146: 
147: ## What Requires Going Back To Humans
148: 
149: See [AGENTS.md § Dual-Claude-Code Workflow](AGENTS.md#dual-claude-code-workflow) for the canonical approval gates. Asking is cheap. Reverting commits is not.
150: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/decisions/010_signed_quarter_boundaries.md -Encoding UTF8; 44..99 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$a[$_] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 '"'^## 10|D13|адресната|100 м|100m'"' -- docs/plans/ПЛАН_Б3_07.09.md" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_Б3_07.09.md -Encoding UTF8; 0..34 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$a[$_] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git ls-files -- gates' in C:\git\Fire_Varna
 succeeded in 419ms:
4:[Omitted long matching line]
78:[Omitted long matching line]
241:[Omitted long matching line]
742:feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)
744:data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
800:[Omitted long matching line]
840:## 10 · Какво НЕ се пипа

 succeeded in 501ms:
45: 69: 
70: **D17 · Дайджестът на тялото за доставка Г.** Амандамент №11 приема вариант (а) изрично „за доставка A“. За доставка Г вариантът се **преобявява** (решение §6.5): важи (а) — несъвпадение се прощава само когато последният комит по артефакта е на `Petar1984` — и G12 проверява точно това.
71: 
72: **D18 · Написаният квартал не се променя.** След P8 всеки от **201-те** реда с написан квартал (М0.4) ЗАПАЗВА кода си. Базата „преди“ е назована: `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`, където `<base_rev>` е `_meta.base_rev` на леджера (D10) — същата ревизия, която храни манифеста-данни. Проверката е команда с изход ≠ 0 (G17).
73: 
74: **D19 · Интервалът на замразяването е обявен, изброен и ограден.** `location_phrases` е подписана претенция в `expectations.json` (`tests/test_places_search_gate.py:464-478` я сверява с `REF.LOC_PHRASES`), а `--freeze` пренаписва очакванията едва СЛЕД подписа (амандамент №11 т. 3). Значи между F13-а и единственото `--freeze` `python -m unittest discover -s tests` е червен по конструкция. Това не е „червено по замисъл“, а **обявен интервал с гейт**: изпълнителят записва при отварянето му ТОЧНИЯ набор падащи тестове (G20), той трябва да е подмножество на назования в плана §2, всеки тест извън набора = STOP, и след `--freeze` наборът е ПРАЗЕН. Интервалът не пресича нито един гейт-ред, който твърди зелено.
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

 succeeded in 419ms:
gates/__init__.py
gates/allow/2026-09-05_lot1v_v.json
gates/baseline/MANIFEST.json
gates/coverage.py
gates/probe/b3_g11.py
gates/release.py
gates/run_gates.py
gates/sign.py

 succeeded in 589ms:
1: # ПЛАН Б3 · Търсене по квартал над подписаните граници (Fire_Varna) — v3
2: 
3: **Дата:** 07.09.2026 · **Планер:** Claude Planner (read-only) · **Статус:** **ПОДПИСАН от Петър (07.09.2026): „подписвам плана Б3 v3 по препоръките“** — подписаното тяло е блобът в комит acddcd1, sha256 `51fde25f1be25a639c6f4f0a5a2b5c6dafe09f697498e8248b80c6cbdd7c343b`; §9 се чете по препоръките (виж §14) · **Заменя:** v2 (`e6ba50e`, чернова, неподписана), след две външни оборвания — **Astra S28** (механика, 10 условия) и **Кими К28** (данни/семантика, 7 условия), и двете **НЕГОДНО** (§12).
4: **Клас на риска:** 🔴 **Архитектурен** (ескалационно-доминантен). Спуснали се спусъци: (1) промяна на схема/ADR — `_meta` 9→10 и 7→8 ключа, затворените списъци `QUARTER_SRC`/`QUARTER_CODES`/новият `LOCALITY_SRC` са договор, ADR 010 D3/D12/D13 носят остарял текст; (2) необратима канонична мутация — замразената референция, `expectations.json`, подписаният allow и **изваждане на подписана опашка от глоба на release**; (3) release/publish верига — този комит е това, което Петър пуска към живата карта; (4) кръстосан blast radius varna_3d → Fire_Varna по подредената тройка D13. Топология: **Вариант А** (планер → подпис на Петър → изпълнител → одитор → преглед на Петър → пуш от Петър).
5: **Записване:** планерът е read-only; файлът е записан от архитекта (чернова acddcd1, подпис в следващия комит). §4 стъпка 1 е изпълнена с това; изпълнителят я пропуска.
6: 
7: > **Произход на числата (честно).** v2 беше писан без Bash — всяко число там беше или **(Ч)** прочетено, или **(М)** от чужда мярка. **v3 е измерен от планера със собствени команди.** Всяко число долу носи командата, с която е получено. Числата, които не съм могъл да измеря без запис в репото, са измерени в **клонинг** (`git clone --shared C:/git/Fire_Varna <scratchpad>/shadow`) — това чете източника и не пише в него; такива числа са маркирани **(К)** и изпълнителят ги преизмерва на място.
8: >
9: > **Нищо не е писано, комитвано или пускано в `C:/git/Fire_Varna` и `C:/git/varna_3d` от тази сесия.**
10: 
11: ---
12: 
13: ## 0 · Червени редове (наследени, без изключение)
14: 
15: Дословно от `C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:11-23`:
16: 
17: 1. **Агентите не пушат.** Никога, с никакъв флаг, без `--no-verify` (`:13`).
18: 2. **Нула геометрия в проследен файл на Fire_Varna.** Публично пътуват само име, код и картата за атрибуция (`:14`).
19: 3. **`Varna_buildings/config/quarter_registry.json` не се пипа** (`:15`).
20: 4. **Написан квартал не се променя** (D18/G17) (`:16`).
21: 5. **Малки, обратими комити**, изчерпателен write-set, дословно съобщение, автор `Claude Executor <executor@local>`; **подписаната геометрия и решенията чакат комит на `Petar1984`** (D16, G4 fail-closed) (`:17`). → О4 и **О24**: авторството се НАЛАГА с флагове, не се предполага.
22: 6. **Всеки гейт е команда с изход ≠ 0 и с отрицателна фикстура, която ТРЯБВА да падне.** Паднал гейт СПИРА лота (`:18`).
23: 7. **Само Opus** — изпълнители и одитори (`:19`).
24: 8. **Одиторът е друг агент** (read-only) (`:20`).
25: 
26: Допълнителни за този лот:
27: 
28: 9. **Кръстосаната изолация е еднопосочна:** от Fire_Varna се ЧЕТЕ блоб на varna_3d (`git -C ../varna_3d show <rev>:<път>`, командата е записана в `tests/test_places_public_bundle.py:49`). Нищо не се пише, комитва или пуска във varna_3d от тази сесия.
29: 10. **Нищо не се публикува преди локалния преглед на Петър** (`python -m http.server 8000`, §8).
30: 11. **„pending — Петър“ не е подпис.** `gates/run_gates.py:775-790` връща 1 и при жълто.
31: 12. **Точно ЕДНА опашка в HEAD и точно ЕДИН allow-json.** (Ч) `gates/release.py:171-172` (`QUEUE_DIR = "scratch/places_search"`, `QUEUE_GLOB = "ЗА_ПОДПИС_*.md"`), `:437-458` (`queues_in_head` чете `git ls-tree -r -z HEAD` и сравнява **basename**-а), `:465-472` (>1 → `raise ValueError`), `:1259-1265` (изключението → BLOCKED). Allow: `gates/run_gates.py:199-217`.
32: 13. 🔴 **Нов (О30): `recall_sweep.py --manifest` ПРЕЗАПИСВА `expectations.json`.** Вторият прогон в същия ден е зелен по конструкция. Доказателство се снема САМО от ПЪРВИЯ прогон срещу подписаното тяло.
33: 
34: ---
35: 

codex
Работното дърво съдържа подготвени промени по Б3, затова ще посоча ясно коя версия проверявам. Има и важен риск в предложението „само добавяме qtk“: то може да запази грешния квартал като равноправен филтър, въпреки поправения надпис.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_Б3_07.09.md -Encoding UTF8; 787..855 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$a[$_] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_Б3_07.09.md -Encoding UTF8; 909..959 | ForEach-Object { if($_ -lt $a.Count){ '"'{0}: {1}' -f ("'$_+1),$a[$_] } }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'D13|100 m|100м|100 м|координатата|D18' -- docs/plans/*амандамент* docs/plans/*НОЩНА* docs/decisions" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'search_index|address_rows|inputs|SIGNABLE|DATA_' -- gates/release.py gates/run_gates.py" in C:\git\Fire_Varna
 succeeded in 550ms:
788: ---
789: 
790: ## 8 · Локален преглед (как Петър гледа)
791: 
792: ```powershell
793: cd C:\git\Fire_Varna
794: python -m http.server 8000
795: ```
796: `http://localhost:8000/index.html`, отворена конзола, ширина 375 px, Hard reload (кешът вече е v7). Първо: конзолата е чиста и **няма** реда `legacy_by_row: друг пакет…`.
797: 
798: | # | пишеш | очакваш (числата са измерени 07.09) |
799: |---|---|---|
800: | 1 | `Кайсиева градина` | в нашата секция — **3 реда `M2-failopen`**, нито един квартален; в адресната търсачка отгоре — 9 реда. |
801: | 2 | `училище Възраждане 3` | **2 реда по ИМЕТО**: `3 ОУ Ангел Кънчев` [**кв. Левски**] и `III ПМГ` [**кв. Тракия**] — **нито един не е във Възраждане 3**. Шум по името, не отговор по квартал. |
802: | 3 | `възраждане`, после `възраждане 2` | **5** реда (`ДГ 29 „Звънче“`, `ДГ 31 „Крилатко“`, `II ОУ „Никола Йонков Вапцаров“`, `ДГ 33 „Делфинче“`, `ДГ№34 „Лястовичка“`) и **0 реда** за детето. **Половината „дете → детето“ НЕ работи** (О16) — това подписваш. |
803: | 4 | `левски`, после `кв. Левски` | голото `левски` → **14 реда, 12 с код `kv_levski`**. `кв. Левски` → **4 ЧУЖДИ реда** (`НУ Васил Левски` [кв. Аспарухово], `ПГ „Васил Левски“`, `ДГ№40` [кв. Владиславово], болница). Същото за `кв. Тракия` (**1**, и той е `dolna_traka`), `кв. Христо Ботев` (**24**, от които **точно 1** е `hristo_botev` — `ЦДГ 8 - Христо Ботев`, и то по име), `ж.к. Св. Иван Рилски` (**22**, нула с кода). **Ако избереш вариант Б по §9 т. 1, тези четири стават 14 / 4 / 4 / 4 с 12 / 4 / 3 / 2 верни реда.** |
804: | 5 | `бриз` | 🔴 **4 реда** (не 2): `ПАРК ХОТЕЛ БРИЗ` [к.к. Златни пясъци — **по име**], `IV ЕГ Жолио Кюри` [ж.к. Бриз, нов], `ПГ „Д. И. Менделеев“` [ж.к. Бриз, нов], `Камелия` [ж.к. Бриз, заварен]. Двата нови са `SIGNED_POLYGON`. |
805: | 6 | `чайка` | **30 реда** — 19 `chaika_kk` + 10 `chaika_kv` + `„ДКЦ Чайка“ ЕООД` (без квартал). Фразата слива двата кода без подписано родство (О16). |
806: | 7 | `аспарухово`, после `дружба` | **16** реда (9 с `asparuhovo`, 7 „район Аспарухово“) **без** `ЦДГ 43 „Пинокио“`, и **2** реда. Подписаното родство `druzhba ⊂ asparuhovo` **не действа**. |
807: | 8 | `Никея` (хотел в Чайка) → картончето | ред **„вид · к.к. Чайка · район Приморски“**; **НЯМА ред за извор** (измерено: 375/375 картончета без нито един от забранените низове); долу вляво, до `© OpenStreetMap`, стои низът за границите. |
808: | 9 | `училище район Младост` / `младост` | **12** / **20**. Изричното районно търсене задържа и петте училища със собствен квартал. |
809: | 10 | **надписът при 375 px** | низът е **338 знака** и застава в същия долен ляв ъгъл, където са бутоните `+`/`−` (`:1900` и `:1917`). Проверява се **на екрана**: бутоните `+`/`−` и локацията остават **видими и натискаеми** при трите базови карти. Ако не са — §9 т. 7, вариант „къс низ“. |
810: | 11 🔴 | **отказът, който мълчи** (О27) | ако някога доставка донесе код извън списъка, в нашата секция ще има **225 реда вместо 375 и НУЛА съобщение**. Днес това не се вижда — подписваш го като известно поведение. |
811: 
812: ---
813: 
814: ## 9 · Решения за Петър
815: 
816: 1. 🔴 **Типовият префикс („кв. Левски“ и трите му близнака).** Измерено (1.8.4): `кв. Левски` 4 чужди, `кв. Тракия` 1, `кв. Христо Ботев` 24 (1 верен по име), `ж.к. Св. Иван Рилски` 22. Причина: `index.html:6495-6496` / `recall_sweep.py:424-431` — токен ≤ 2 знака не е значещ, а М7 иска `R.every(isSignificantToken)`. **Три варианта:**
817:    - **(А) Отлагане** (позицията на v2): D12 + `locationKey` в паритетния корпус са лот **Б5**. Цена: осемте нови квартала се търсят само с голото си име. Цена днес: 0.
818:    - **(Б) Евтината поправка (К28-5), ПРЕПОРЪЧАНА.** Двигателят вече назовава затворения списък `M7_PREFIXES` (`recall_sweep.py:3093` = `("k","kv","zh","m","s","o","t","i","1","2")`). Пропускат се **само буквените** префикси (`k, kv, zh, m, s, o, t, i`) преди теста за значимост в М7 клона, в **двата двигателя**: `recall_sweep.py:1257`+`:1263` (2 реда) и `index.html:7058-7069` (клиентът **няма** такъв списък — иска новата константа + филтриран `R`, ~5 реда). **Измерено върху копие в скрачпада:** `кв. Левски` **4 → 14** (12 с `kv_levski`), `кв. Тракия` **1 → 4** (4/4), `кв. Христо Ботев` **24 → 4** (3/4), `ж.к. Св. Иван Рилски` **22 → 4** (2/4). **Цена на презамразяване: НУЛА** — 156-заявъчният подписан корпус дава **0 промени**, а дъмпът на референцията е **байт-еднакъв** (1 273 012 B). Остава честната цена: **паритетът** (клиентът трябва да получи същите ~5 реда, иначе двата двигателя се разминават) и **един нов кръг на фикстурите/паритетната сонда**. Числата (`2`, `1`) остават извън списъка: **„възраждане 2“ и „младост 2“ пак дават 0** — детската заявка не оживява.
819:    - **(В) Пълният D12** (нормализатор + `locationKey` в паритета): измерено, че вариант **А′** (пропускане и на числата `1`/`2`) прави „възраждане 2“ и „младост 2“ да върнат **5** и **20** — тоест ДЕТСКАТА заявка получава РОДИТЕЛСКИЯ отговор. Това е по-лошо от 0 и планерът го **отхвърля** (§13 т. 5).
820:    **Препоръка: (Б).** Ако Петър каже (А), §8 проба 4 остава както е и О15 се подписва изрично.
821: 2. 🔴 **Правилото родител/дете.** Измерено: работи по фраза само за Младост/Възраждане, **не работи** за `druzhba ⊂ asparuhovo`, **не работи** за детската заявка, и **слива** `chaika_kk`+`chaika_kv`. **Препоръка: замразяваме измереното** (фикстури 5–8) и подписваш О16. Вариант Б: `locations.quarter[<code>].parents` в речника → днешната доставка отпада и цикълът се повтаря отначало.
822: 3. **`QUARTER_CODES` +8 (=28)** + машинен гейт „списъкът == речникът“ (измерено днес: равни). **Препоръка: да.**
823: 4. **Един атомен комит с твой автор** (О4) + наложено авторство на агентските комити (О24). **Препоръка: да.**
824: 5. **`DISTRICT_FALLBACK`: пълното типово правило на ШЕСТ места** (О19) + синтетична положителна фикстура с разделен `_broken`. **Препоръка: пълното правило.**
825: 6. **Етикетът на fallback ред се приема в ДВЕТЕ форми** (О20; измерено: износителят пише `zone === quarter.name` за 375/375). **Препоръка: да.**
826: 7. 🔴 **Низът в подножието не е твой подпис днес** (О21). **Препоръка:** подписваш го като **ред „въпрос“** с `тяло: c6d29d4e…` (sha на низа) и `тяло-на-файла: c57a79c2…`; **сверката е в G9, защото `release.py:1367-1371` пропуска ред без артефакт** — това е механика, не небрежност. Две бележки: низът казва „в този файл“ (писан е за файла с решенията), а на 375 px заема долния ляв ъгъл при бутоните — §8 проба 10 решава дали остава дословен.
827: 8. **`granitsi_fixtures_06.09.json` → `…_07.09.json`** (`git mv`). **Препоръка: да.**
828: 9. 🔴 **baseline и allow (О22).** **Препоръка: baseline ОСТАВА `f06ac06`**; новият allow бюджетира **138-те** реда. Семантиката, дословно: „lost“ = ред с назован квартал/зона в базата и без такъв в кандидата (places 44, hotels 39); „changed“ = друг назован (places 44, hotels 11). Обяснението защо не са 150: срещу `f00dd78` са **150**, значи доставката **връща 12**. Пренасочването на baseline е **отделен по-късен подписан лот**.
829: 10. 🔴 **Мълчаливият UI отказ (О27, ново).** Нощният план `:144` го забранява, а Б3 го запазва — при чужд код клиентът показва 225 вместо 375 и мълчи. **Препоръка:** подписваш го като **обявено отклонение** и фикстура 9в го пинва; видимият отказ е отделен малък лот.
830: 11. **Перчемлията / решение 10** (О6) — подпиши поименния резерв **преди** комита или сложи изричен „отложено“ ред в опашката.
831: 12. **Документният дълг** (О9 + О23) — **отделен комит след пуша**.
832: 13. **Node-паритетната фикстура е ПОСТРОЕНА** (фикстура 11). **Препоръка: да.**
833: 14. 🔴 **Старата опашка (О25) — поправено срещу v2.** Измерено: `архив/ЗА_ПОДПИС_A_05.09.md` **пак се брои** за опашка (`queues_in_head` е рекурсивен и гледа basename), тоест release остава BLOCKED. **Препоръка: `git mv` към `scratch/places_search/архив/АРХИВ_A_05.09.md`** — името губи префикса. Изтриване не е нужно: 27-те подписани реда остават четими и в историята, и в архива.
834: 15. **`LOCALITY_SRC` (О18)** — стеснението, което пази местността от `DISTRICT_FALLBACK`. **Препоръка: да.**
835: 16. **`_meta` става затворено МНОЖЕСТВО в клиента (О17)** — 10/8 ключа поименно, `src ∈ {wikimapia, openstreetmap}` с правило за всеки, и **равенство** карта ↔ `SIGNED_POLYGON` кодове (14 / 7). **Препоръка: да** — това е половината от G27(б), която иначе остава неналожена.
836: 17. 🔴 **`P7_ADDED` дрейфът (О28, ново).** Новият речник добавя **5 нови токена** (`gratska`, `gratski`, `varnenchik`, `vladislav`, `vasil`), а подписаният `foreign_guard` изрично казва, че `vladislav`/`varnenchik` са били отхвърлени като чужди. **Препоръка:** ред „въпрос“ в опашката с двата списъка дословно; ако Петър не иска новите псевдоними, това е промяна в **износа на varna_3d**, не в Fire_Varna, и доставката се връща.
837: 
838: ---
839: 
840: ## 10 · Какво НЕ се пипа
841: 
842: - `Varna_buildings/config/quarter_registry.json` и изобщо репото `Varna_buildings`.
843: - `varna_3d`: чете се **само** блоб; `data/quarters_signed.geojson` никога не влиза във Fire_Varna.
844: - **Написаните 201 квартала** (D18/G17) и леджерът.
845: - `DISTRICT_CODES` (`:6315`), `LOCALITY_CODES` (`:6322`), `EXPECT_KEYS`/`EXPECT2_KEYS`, `EXPECT_COUNT`/`EXPECT2_COUNT`, `TOP`/`MIN_Q`/`DEBOUNCE_MS`, `KINDS`/`KINDS2`/`STATUSES`.
846: - **`gates/baseline/MANIFEST.json`** (О22), **`INPUT_RELS`** (`recall_sweep.py:2815-2816`, О23) и **`CENTER`** (`:102-104`).
847: - Адресната търсачка (`index.html:5928-6070`, `data/approx_addresses_v1.json`), `data/search_index.json`, `data/address_rows.json`.
848: - Хидрантите, формата за докладване, Worker-ът, базовите карти и `BASEMAP_PMTILES_ENABLED` (`:4563`).
849: - Двигателите на гейта: `gates/run_gates.py`, `gates/release.py`, `gates/sign.py`, `gates/coverage.py`, `scripts/hooks/pre-push` — **нула редакции** (затова G9 сверява дайджеста сам).
850: - Числата на `granitsi_fixtures_06.09.json` като исторически запис.
851: - Публикуваните sha и `origin/main` — до ръката на Петър.
852: 
853: ---
854: 
855: ## 11 · Отхвърлени находки (от кръговете на v1/v2)
856: 

 exited 1 in 418ms:
rg: docs/plans/*амандамент*: The filename, directory name, or volume label syntax is incorrect. (os error 123)
rg: docs/plans/*НОЩНА*: The filename, directory name, or volume label syntax is incorrect. (os error 123)
docs/decisions\010_signed_quarter_boundaries.md

 succeeded in 583ms:
 succeeded in 422ms:
gates/run_gates.py
gates/release.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git ls-files -- 'docs/plans/*амандамент*' 'docs/plans/*НОЩНА*'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'search_index|address_rows|INPUT|sha256' -- gates/release.py" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath gates/run_gates.py -Encoding UTF8; 0..88 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$a[$_] }' in C:\git\Fire_Varna
 succeeded in 393ms:
docs/plans/ПЛАН_Б3_07.09_амандамент_1.md
docs/plans/ПЛАН_Б3_07.09_амандамент_2.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_10_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_11_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_1_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_2_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_3_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_4_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_5_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_6_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_7_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_8_05.09.md
docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_9_05.09.md
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md
docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md
docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md

 succeeded in 390ms:
111:<sha256>`, the values without the signature fields) and check 6 recompares it
342:    return hashlib.sha256(raw).hexdigest()
390:    """sha256 of an artefact BODY — its values, without the signature field.
901:    """(commit, path, sha256, complaint) — the reference THE QUEUE was written against.
919:    commit, rel, want = anchor.get("commit"), anchor.get("path"), anchor.get("sha256")
968:    return {"sha256": digest(raw), "bytes": len(raw), "path": REFERENCE_REL,
1218:        if want is not None and anchor.get("sha256") != want:
1223:                  % ((anchor.get("sha256") or u"—")[:12], want[:12]))
1245:        if want.get("sha256") != got:
1247:                  % (got[:12], (want.get("sha256") or u"—")[:12]))

 succeeded in 530ms:
1: #!/usr/bin/env python3
2: """The single executable the push waits on.
3: 
4:     python -m gates.run_gates [--base git:<rev>] [--allow <path>]
5: 
6: Seven checks, one table, one exit code:
7: 
8:   1. sha pins        the three SHA256 constants in `index.html` against the
9:                      LF-normalised bytes of the three delivered blobs — exactly
10:                      the bytes `fetchValidatedJson` digests in the browser
11:   2. key sets        every row carries exactly EXPECT_KEYS / EXPECT2_KEYS
12:                      (hotels 17, places 13) — the count and the names
13:   3. qa_no_cad_ids   no cadastral identifier ever rides a public blob
14:   4. coverage        gates/coverage.py against the last signed baseline
15:                      (gates/baseline/MANIFEST.json); no baseline = STOP
16:   5. signed_facts    data/signed_facts.json — the small judging file
17:   6. release         gates/release.py — the frozen reference, the engine
18:                      candidate, the pinned inputs and the manifests bound by
19:                      digest; every delta covered by a signed queue row
20:   7. authorship      every `signed_by: "Петър"` was introduced by a commit of
21:                      Petar1984, never by an agent (`git log -S`) — AND the body
22:                      it protects has not been rewritten since: the newest commit
23:                      on a signed artefact is Petar's too, or he recorded the
24:                      digest of the resulting body himself (амандамент №5 т. 3),
25:                      on a queue whose own authorship was settled first
26:                      (амандамент №6 т. 3) and with HIS commit as the one that
27:                      introduced the number (амандамент №8 т. 2) — and every
28:                      „да“ ROW of that queue was introduced by a commit of his
29:                      as well (амандамент №9 т. 2)
30: 
31: The gate never imports `unittest` and never reads `tests/`: a check that shares
32: code with the suite it guards cannot fail independently of it.
33: 
34: Every check runs, always: the table is written for the human, not stopped at
35: the first mark. Exit code: 0 only when every check is green; 1 when any check
36: is red OR yellow — "pending — Петър" is not a signature (Амандамент №1, т. 8),
37: and neither is "Петърчо Иванов": the signature is compared exactly, by
38: `coverage.is_signed_by_petar`, for the baseline manifest and the allow-file
39: alike. `--base` replaces the signed baseline with an ad-hoc revision and is
40: therefore ⚠ by construction: it measures, it does not absolve.
41: One number for the pre-push hook to read.
42: """
43: 
44: from __future__ import annotations
45: 
46: import argparse
47: import hashlib
48: import json
49: import re
50: import subprocess
51: import sys
52: from pathlib import Path
53: 
54: from gates import coverage
55: from gates import release
56: 
57: REPO_ROOT = Path(__file__).resolve().parent.parent
58: 
59: INDEX_HTML = "index.html"
60: BASELINE_PATH = "gates/baseline/MANIFEST.json"
61: ALLOW_DIR = "gates/allow"
62: SIGNED_FACTS_PATH = "data/signed_facts.json"
63: # The only author whose commit may INTRODUCE a signature (§0.5) — one string,
64: # kept in `gates.release` and read by every gate that asks whose hand it was.
65: HUMAN_AUTHOR = release.HUMAN_AUTHOR
66: 
67: # (constant in index.html, delivered blob)
68: SHA_PINS = (
69:     ("HOTELS_SHA256", "data/hotels.json"),
70:     ("PLACES2_SHA256", "data/places.json"),
71:     ("CATS_SHA256", "data/place_categories.json"),
72: )
73: 
74: ROW_FILES = (
75:     ("hotels", "data/hotels.json", "hotels", "EXPECT_KEYS", 17),
76:     ("places", "data/places.json", "places", "EXPECT2_KEYS", 13),
77: )
78: 
79: # A cadastral id never rides a public bundle (ADR 008 Д2) — the same regex the
80: # client applies to the fetched text, applied here to the tracked bytes.
81: CADASTRAL_RE = re.compile(r"\b\d{4,5}\.\d+\.\d+")
82: PUBLIC_BLOBS = (
83:     "data/hotels.json",
84:     "data/places.json",
85:     "data/place_categories.json",
86:     SIGNED_FACTS_PATH,
87: )
88: 
89: OK, WARN, BAD = "✓", "⚠", "✗"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 'D13|100 м|100m|координатата|D18|най-малк' -- docs/plans -g '*амандамент*' -g '*НОЩНА*'" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_Б3_07.09_амандамент_2.md -Encoding UTF8; 0..74 | ForEach-Object { if($_ -lt $a.Count){ '"'{0}: {1}' -f ("'$_+1),$a[$_] } }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_Б3_07.09_амандамент_1.md -Encoding UTF8; 0..65 | ForEach-Object { if($_ -lt $a.Count){ '"'{0}: {1}' -f ("'$_+1),$a[$_] } }' in C:\git\Fire_Varna
 exited 1 in 444ms:
rg: -g: The system cannot find the file specified. (os error 2)
rg: *амандамент*: The filename, directory name, or volume label syntax is incorrect. (os error 123)
rg: -g: The system cannot find the file specified. (os error 2)
rg: *НОЩНА*: The filename, directory name, or volume label syntax is incorrect. (os error 123)
docs/plans\h1_shared_core_spatial_dedup.md
docs/plans\h2_kmz_adapter_plan.md
docs/plans\places_search_plan_2026-09-02.md
docs/plans\recommendations_2026-09-03.md
docs/plans\ПЛАН_Б3_07.09.md
docs/plans\ПЛАН_ЛОТ1г_телата.md
docs/plans\ПЛАН_ЛОТ_Границите_v2_05.09.md
docs/plans\ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md
docs/plans\ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md
docs/plans\ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md

 succeeded in 600ms:
1: # АМАНДАМЕНТ №2 към ПЛАН Б3 · 07.09.2026 (нощта, чернова на архитекта)
2: 
3: **Какво изменя:** `docs/plans/ПЛАН_Б3_07.09.md` (v3, подписан 4db50c2) + амандамент №1 (подписан 4fdd303).
4: **Основание:** изпълнител B спря правилно на §7 т. 4 — червен тест ИЗВЪН обявения набор, който никоя следваща подписана стъпка не гаси. Изпълнител A остави две находки от същия механичен род. Нито едно от 17-те подписани решения не се променя; нито един нов избор за картата.
5: **Статут:** ⏳ **за подпис на Петър сутринта — само делтата; преди атомния комит 2.** Поправките НЕ са приложени през нощта (нито един ред извън write-set-а без подпис); червените остават обявени в набора D19/G20.
6: 
7: ## 1 · Трите механични поправки
8: 
9: ### А2-1 · Второто ръчно копие на името на кеша (ADR 008 D8)
10: **Мярка (B):** `tests/test_places_search_gate.PlacesCacheNameTest.test_the_probe_uses_the_name_index_html_owns` → exit 1: `'fire-varna-hotels-v7-225' != 'fire-varna-hotels-v6-225'`. Причина: `scratch/places_search/probe_places_fv.mjs:802` носи `const PLACES_CACHE = "fire-varna-hotels-v6-225";` (ползван на :1002, :1004, :1533); `git grep` показва точно двете живи копия (index.html и сондата). В контрафактуален клонинг с новите данни, но със стария index.html, тестът е зелен — червеното е следствие само от И1. ADR 008 D8 казва изрично: името се води на ръка от ДВЕ страни.
11: **Поправка:** нова редакция **И1б** в write-set-а: `scratch/places_search/probe_places_fv.mjs:802` → `const PLACES_CACHE = "fire-varna-hotels-v7-225";` (един ред; §10 не забранява файла). Влиза в атомния комит 2. Гейт: същият тест → 0; отрицателно: върни v6 → 1.
12: 
13: ### А2-2 · Гейтът на новите файлове не познава собствения си тестов файл
14: **Мярка (A):** `gates/probe/b3_g11.py` `ALLOWED_NEW` (амандамент 1, S29-4) не изброява `tests/test_b3_gates.py` (файлът е поискан от S29-8 в същия амандамент) → `stray_new: ["tests/test_b3_gates.py"]`, exit 1 при комита (STOP 22 по конструкция).
15: **Поправка:** `ALLOWED_NEW` получава реда `"tests/test_b3_gates.py"`. Гейт: `python gates/probe/b3_g11.py HEAD --cached` → 0; отрицателно: непознат нов файл в скрачпад-клонинг → 1.
16: 
17: ### А2-3 · О26 се разширява с втори проследен изход на двигателя
18: **Мярка (A/B):** обикновеният (не-freeze) прогон на `recall_sweep.py` пише и `scratch/places_search/lot1v_v_reference_manifest.json` (проследен), не само `probe_out/token_parity.json`. Дали байтовете се менят при днешните прогони: виж реда „git diff --stat“ в доклада на изпълнител C.
19: **Поправка:** О26 и §4 стъпка 7 назовават и двата файла; ако манифестът е променен, той пътува с комит 5 (замразяването), не с комит 2; ако е байт-еднакъв — записва се, че е бил пренаписан без промяна.
20: 
21: ### А2-4 · G11 приема `--cached` (обявено разширение на подписания скрипт)
22: **Мярка (A, одитор):** амандамент 1 S29-4 дава скрипта дословно с команда `python gates\probe3_g11.py <parent>` (диф родител→HEAD). Комит 2 е ръката на Петър (§6, О4) — гейтът трябва да е изпълним ВЪРХУ СТЕЙДЖА, преди комитът да съществува. Изпълнител A добави втори режим: `python gates/probe/b3_g11.py HEAD --cached` (диф родител→индекс), обявен в докстринга; без флага поведението е подписаното байт за байт.
23: **Поправка:** редът се подписва като част от S29-4. Гейт: `--cached` върху стейджа → 0 след А2-2; след комита на Петър — и без флага → 0.
24: 
25: ## 2 · Уточнения, които НЕ са поправки (записват се за подписа)
26: **Фикстура 9в:** пинът на плана за мутираното тяло (128 402 B / `6bfbcbf2…`) не се възпроизвежда; §3.5 казва, че числата се преизмерват. Мутацията се записва дословно: първият обект `"quarter"` със `"src": "SIGNED_POLYGON"` в `data/places.json` получава `"code": "tsentar_new"` (беше `kv_levski`) → тяло 128 403 B, sha256 `2064527328899246c32b0c83f8fc3dba9c01d1cbbb67791a6dcc18e88c997733`. Изпълнител C я пинна така (`was_code: kv_levski`); одиторът я премери независимо: същите байтове и sha.
27: **Фикстура 4 (`order_identity`):** „заварената“ мутация вече ДОБАВЯ ред (ОУ „Иван Вазов“ отиде в ж.к. Победа с доставката: 20 → 21), а фикстурата съществува, за да покаже, че сравнение по множество не лови пренареждане. Преизведена по същия клас като 6/7/8: `27 ДГ Успех` получава квартал {ж.к. Младост, mladost, SIGNED_POLYGON} при непипнат `zone` → 20 реда, СЪЩОТО множество, ред 12 → ред 2. Одиторът: „same SET=True, same ORDER=False“ — точно това, което фикстурата пази.
28: **`tests/granitsi_client_probe.mjs`:** изпълнител C поправи 4 реда в сондата на A (askът `search` чете `x.e.name`, защото клиентският ред е обвивката `{e: record, …}`); без поправката фикстура 11 щеше да сравнява `[null, null, …]` — вакуумно зелено. Файлът е в същия некомитнат write-set; подписаното не е пипано.
29: **Харнесът** брои `with_quarter`/`without_quarter` по `own_quarter(r)`, не по суровото поле (иначе DISTRICT_FALLBACK ред би се броил за квартален); върху днешната доставка (0 fallback реда) разликата е нула.
30: 
31: ## 3 · Изпълнение и одит (нощта на 07→08.09, за протокола)
32: Стъпки 0–7 са изпълнени (изпълнители A, B, C; Opus) и одитирани (**ГОДНО**, 8 минора, нула блокери/майори): 13 пътя стейджнати, нищо комитнато; червеният набор D19/G20 е точно обявеният — 25 теста (21 замразена референция → стъпка 13; 3 `MapAttributionTest` → 12б; 1 `PlacesCacheNameTest` → А2-1), `run_gates` две червени (покритие exit 2 → стъпка 11; release BLOCKED 2 → стъпки 11/13/14 + А2-3), G11 `--cached` само `stray_new tests/test_b3_gates.py` → А2-2. Кими К30 / Astra S30 върху стейджнатия диф — виж записите.
33: 
34: ## 3б · Външни прегледи на изпълнението и поправките (нощта, за протокола)
35: - **Astra S30 (механика): НЕГОДНО с три блокера в ГЕЙТ-СКРИПТОВЕТЕ** (не в доставката): G11 четеше работното дърво вместо индекса при `--cached` и приемаше грешка на git за зелено; G1 не сверяваше трите клиентски пина в `index.html`. **Затворени** (изпълнител + одитор ГОДНО): `gates/probe/b3_g11.py` чете съдържание и инвентар от ЕДИН моментен срез (`git show :<path>` / `HEAD:<path>`, `:(top)` pathspec, chdir към върха, `check=True`, нечетимо → exit 1, счупен git или празен инвентар → exit 2); нов клас `ClientPinsTest` в `tests/test_places_public_bundle.py` сверява `PLACES2_SHA256`/`HOTELS_SHA256`/`CATS_SHA256`/`LEGACY_BUNDLE_SHA` от `index.html` с LF-телата (G1: 68 теста; една сменена цифра → червено). Това е коректно изпълнение на подписаните G1/G11, не нов обхват.
36: - **Кими К30/К31 (данни + клиент): всичко измеримо зелено** — 11-те фикстури възпроизводими, вариант Б потвърден в двата двигателя, 16-те hunk-а на `index.html` приписани към И1–И13, И11 отсъства, сондата коректна. **Приет дълг (К30):** размяна на `url` между два wikimapia записа минава валидатора — механичен гейт без подписана таблица няма; sha-пиновете покриват реалната доставка.
37: - **Остатъчни минори (записани, без действие):** гейтът G11 се закотвя за хранилището на CWD (при абсолютен път от чужда директория гледа друго дърво); `ClientPinsTest` чете работното дърво (равно на индекса при комита, сверено с `git diff --exit-code`).
38: - **Крайно състояние:** 13 стейджнати пътя (3841+/1255−), родителят на комит 2 е последният комит на архитекта в `main`; `python -m unittest discover -s tests` → 342 теста, 25 червени = точно обявеният набор; данните 3dffc264/eb8fa85c/9064705a непокътнати.
39: 
40: ## 4 · Какво подписва Петър
41: Един подпис за четирите реда: А2-1 (v7 в сондата), А2-2 (`ALLOWED_NEW` + `tests/test_b3_gates.py`), А2-3 (манифестът пътува с комит 5, препоръка б), А2-4 (`--cached`), плюс уточненията в §2. Нищо от 17-те решения не се променя. **Редът сутринта:** подпис → изпълнител прилага А2-1/А2-2 (два реда) и ги стейджва → атомният комит 2 на Петър.

 succeeded in 572ms:
1: # АМАНДАМЕНТ №1 към ПЛАН Б3 · 07.09.2026
2: 
3: **Какво изменя:** `docs/plans/ПЛАН_Б3_07.09.md` (v3, ПОДПИСАН от Петър, комит `4db50c2`, §14).
4: **Основание:** повторната проверка **Astra S29** върху v3 върна **НЕГОДНО** с осем МЕХАНИЧНИ условия (Кими К29: ГОДНО, без условия). §14 на плана предвижда точно това: „условие от тях влиза като амандамент (нов датиран файл) и се подписва отделно, само за делтата“.
5: **Какво НЕ се променя:** нито едно от **седемнадесетте подписани решения** на §9 (прочитът в §14 остава дословен). Всички редакции тук са в **гейтове, команди, броени числа и реда на две стъпки** — нула нови решения, нула нов write-set, нула ново поведение на картата.
6: **Статут:** **ПОДПИСАН от Петър (07.09.2026): „подписвам“** — подписаното тяло е блобът в комит 1daefb6, sha256 `b769d83a38e098290a062dc3a7ad8366cf82412f939d61592e95ceb6880fa149`. Изпълнението на Б3 тръгва по ПЛАН v3 (4db50c2) + този амандамент.
7: **Всяко твърдение по-долу е измерено** в `git clone --shared` копие (скрачпад), с новите блобове на `varna_3d 05f485e`, чиито три пина съвпаднаха байт в байт с §1.4 (`3dffc264… / eb8fa85c… / 9064705a…`). Работното дърво на `C:/git/Fire_Varna` е непипнато (`git status --porcelain` без проследени редове).
8: 
9: ---
10: 
11: ## 1 · Приетите осем условия
12: 
13: ### S29-1 · G7 не е изпълним в PowerShell и редът му е обърнат
14: 
15: **Място:** §5, блокът „G7 — дословно“, **редове 661–675**; и §4, **редове 576–578**.
16: **СТАРО (663–664 и 668–669, дословно):**
17: ```powershell
18: python scratch\places_search\recall_sweep.py
19: copy /Y "%TEMP%\fv_measures\lot1v_v_candidate_rows.json" "<scratch>\g7_dump_A.json"
20: ```
21: **СТАРО (край на ред 675):** „Ревизиите на двигателя се пинват в отчета (`git rev-parse HEAD:scratch/places_search/recall_sweep.py` преди и след).“
22: 
23: **НОВО — дъмп A, в НОВАТА стъпка 5б (ПРЕДИ редакцията на двигателя):**
24: ```powershell
25: python scratch\places_search\recall_sweep.py
26: Copy-Item -LiteralPath "$env:TEMP\fv_measures\lot1v_v_candidate_rows.json" -Destination "<scratch>\g7_dump_A.json" -Force -ErrorAction Stop
27: python -c "import hashlib,pathlib; b=pathlib.Path('scratch/places_search/recall_sweep.py').read_bytes().replace(b'\r\n',b'\n'); print('engine_A', hashlib.sha256(b).hexdigest())"
28: ```
29: **НОВО — дъмп B, в стъпка 7 (СЛЕД §3.4–3.6):**
30: ```powershell
31: python scratch\places_search\recall_sweep.py
32: Copy-Item -LiteralPath "$env:TEMP\fv_measures\lot1v_v_candidate_rows.json" -Destination "<scratch>\g7_dump_B.json" -Force -ErrorAction Stop
33: python -c "import hashlib,pathlib; b=pathlib.Path('scratch/places_search/recall_sweep.py').read_bytes().replace(b'\r\n',b'\n'); print('engine_B', hashlib.sha256(b).hexdigest())"
34: ```
35: **НОВО — двата comparator-а (и двата задължителни, exit ≠ 0 спира лота):**
36: ```powershell
37: python -c "import pathlib,sys; a=pathlib.Path(r'<scratch>\g7_dump_A.json').read_bytes(); b=pathlib.Path(r'<scratch>\g7_dump_B.json').read_bytes(); print(len(a),len(b),a==b); sys.exit(0 if a==b else 1)"
38: python -c "import sys; A='<engine_A>'; B='<engine_B>'; print(A,B,A!=B); sys.exit(0 if A!=B else 1)"
39: ```
40: Вторият е новото: без него гейтът може да сравни **същия** двигател със себе си и да мине празен.
41: **Мярка:** `powershell -NoProfile -Command '…try { copy /Y "$env:TEMP\nope.json" "X.txt" } catch { exit 1 }'` → **exit 1, `ParameterBindingException`** (`copy` е псевдоним на `Copy-Item`; `%TEMP%` не се разгръща в PowerShell); същото с `Copy-Item -LiteralPath "$env:TEMP\…" -Force -ErrorAction Stop` → **exit 0, файлът е там**. · `git rev-parse HEAD:scratch/places_search/recall_sweep.py` преди и след редакция в работното дърво → **един и същ OID `bae0c1bf…`**, докато `sha256` на изпълнения файл се мени `0869f12c…` → `ec6fef0a…`: пинът по `HEAD:path` е сляп точно за това, което G7 мери. · Дъмпът след прогон → **1 324 215 B** (числото на плана се потвърждава).
42: 
43: ### S29-2 · Отрицателната фикстура 8 нарушава собствения си договор
44: 
45: **Място:** §3.5, **ред 454** (правилото на харнеса) и **ред 466** (фикстура 8).
46: **СТАРО (454):** „`_broken` носи `fails_on: "<заявка>"`; тестът твърди, че `assert_case` хвърля **и** че точно тази заявка е сменена, а останалите заявки на фикстурата са непроменени“.
47: **СТАРО (край на 466):** „`fails_on: "аспарухово"`, а вторият ред се пази като второ твърдение“.
48: 
49: **НОВО (454):** `_broken` носи **`fails_on: [<заявка>, …]` — МНОЖЕСТВО**, и тестът мери кои заявки наистина са мръднали:
50: ```python
51:     qs = [w["q"] for w in case["queries"]]
52:     clean  = dict((q, answer(self.reference, q)) for q in qs)          # без ops
53:     broken_m = dict((q, answer(self.reference, q, broken["ops"])) for q in qs)
54:     changed = sorted(q for q in qs if broken_m[q] != clean[q])
55:     self.assertEqual(changed, sorted(broken["fails_on"]), name)        # ТОЧНО множеството
56:     with self.assertRaises(AssertionError):                            # и то наистина чупи
57:         self.assert_case(case, broken_m)
58: ```
59: Едно-заявъчните фикстури носят списък от един елемент. Мутация, която мърда заявка ИЗВЪН `fails_on`, вече не минава за доказателство — и мутация, която НЕ мърда обявена заявка, също пада.
60: **НОВО (край на 466):** → **„аспарухово“ 16 → 17** (детето влиза при родителя) **И** **„дружба“ 2 → 1** (клонът пада от `M7-bare-location` на `M3`). **`fails_on: ["аспарухово", "дружба"]`** — двете са РАВНОПРАВНИ твърдения на една мутация, не главно и второстепенно.
61: 
62: **Мярка:** един `op` (`ЦДГ 43 "Пинокио"` → `quarter {name: "кв. Аспарухово", code: "druzhba", src: SIGNED_POLYGON}`, `zone: "кв. Аспарухово"`) над целия корпус (226 записа + шестте фикстурни заявки), сравнение чист ↔ мутиран:
63: **променени записи: 4; различни заявки: 4** — `аспарухово 16→17`, `дружба M7/2 → M3/1`, и латинските им близнаци `asparuhovo`, `druzhba` в кофата `gate_m7_bare`. **Нищо друго не мърда.** Другите поправени мутации на плана се потвърдиха непроменени (`чайка` 30, `възраждане` 5/0/0).
64: 
65: ### S29-3 · О29 и §13 т.4 броят заявките погрешно
66: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 '100|D13|координат|D18|малк|ръб' -- docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 '100|D13|координат|D18|малк|ръб' -- docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md" in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md -Encoding UTF8; 0..74 | ForEach-Object { if($_ -lt $a.Count){ '"'{0}: {1}' -f ("'$_+1),$a[$_] } }' in C:\git\Fire_Varna
 succeeded in 393ms:
10:[Omitted long matching line]
16:[Omitted long matching line]
38:[Omitted long matching line]
44:[Omitted long matching line]
52:[Omitted long matching line]
71:[Omitted long matching line]
86:[Omitted long matching line]
91:[Omitted long matching line]
102:[Omitted long matching line]
103:[Omitted long matching line]
114:[Omitted long matching line]
116:[Omitted long matching line]

 succeeded in 374ms:
5:[Omitted long matching line]
7:[Omitted long matching line]
16:4. **Написан квартал не се променя** (D18/G17). Спорът е ред в леджера, не редакция.
32:[Omitted long matching line]
45:[Omitted long matching line]
58:[Omitted long matching line]
60:[Omitted long matching line]
61:[Omitted long matching line]
63:[Omitted long matching line]
73:[Omitted long matching line]
80:[Omitted long matching line]
83:[Omitted long matching line]
86:[Omitted long matching line]
93:[Omitted long matching line]
96:[Omitted long matching line]
105:[Omitted long matching line]
125:[Omitted long matching line]
127:[Omitted long matching line]
129:6. **`precision_m`**: 100 за `wikimapia`, 50 за `street_bounded_face`; ръб = `max(50, precision_m)` по D7 → `edge_pending`. Препоръка: да.
132:[Omitted long matching line]

 succeeded in 540ms:
1: # Амандамент №3 към ЛОТ „Границите" (07.09.2026) — самоличността на местата срещу квартала
2: 
3: **§0 · Място в редицата.** Продължава редицата на ЛОТА: `ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md` → `_2_06.09.md` → този, №3. Изменя **Б2** от подписания `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md`; не редактира нито един подписан ред.
4: 
5: **Клас: 🔴 Архитектурен.** Спуснати спусъци: променя подписан договор за данните (ключът на самоличността) · мутира каноничното `data/place_identity.json` · пипа данни, които пътуват към Fire_Varna · сменя и добавя гейтове. **Топология: Вариант А.** **Статус: ЗА ПОДПИС (Gate 1). НЕПОДПИСАН.**
6: **Не отваря нищо ново:** Б3/търсенето, регистърът, `quarters_signed.geojson`, написаните 201 квартала и живата карта не се пипат. Нула пуш.
7: 
8: ## 1 · Мярката (read-only, 07.09)
9: 
10: 1. **Ключът и котвите.** `src/place_identity.py:207,222`: `base = "<файл>|skel(име)|zone"`. `anchors_of()` (`:569-583`) дава четири нива: `reg` · `ntr` · `kais` · и чак после `key`, в който седи зоната (`:582`). Стара самоличност, която нищо не намира, е „оттеглена БЕЗ решение" и СПИРА билда (`:813-816`). `site_id` НЕ е котва (`:623-659`).
11: 2. **Кой виси на крехкия ключ.** `scratch/granitsi/aud_regen.log:3`: ntr 192 · kais 144 · reg 35 · **key 4**. 371/375 не зависят от зоната. Четирите са две двойки върху едно кадастрално тяло: ДГ№52 + Диспансерът (`kais_i` 1523) и III ПМГ + ОУ „П. Р. Славейков" (`kais_i` 39992).
12: 3. **Кои два реда падат.** В спрения износ втората двойка минава `район Одесос → кв. Тракия` (`SIGNED_POLYGON`); ключовете се менят, `kais` е двусмислена, `reg`/`ntr` ги няма → два сирака, генераторът пада. 55 от 57-те смени на зона се спасяват от reg/ntr/kais.
13: 4. **Присвояването вече носи `place_id`.** `fire_varna_locations.py:967-979` свързва по УИН, после по `(файл, skel(име))` — „by evidence, never by zone". Леджерът е `{_meta, rows, quarantine}`, като **`rows` е СПИСЪК от 375 реда**, всеки с `place_id`/`old_zone`/`new_zone`; `old_zone` идва от ЗАМРАЗЕНИЯ блок `legacy_zones` (`:886-893`, покрива 375/375), не от зоната в самоличността. Речник по `place_id` е само `book.rows` в паметта (`:1937`).
14: 5. **Износът не може да носи id.** `place_identity.py:38-40`: публичните `data/fire_varna_*.json` не носят id — подписан договор.
15: 6. **Стълкновения без зоната.** Мерено: местата дават 150 различни скелета от 150 (нула стълкновения); хотелите — четири двойки (`admiral`, `perla`, `roial`, `rusalka`), и осемте реда `matched_by: "ntr"`, решавани по УИН.
16: 7. **Речникът на търсенето.** `qa_place_zone_aliases.py` пада на проверка (а) (`:213-217`). Числото в СЪСТОЯНИЕ §5 („три зони") е ОТРЯЗАН текст (`lost[:3]`): доставените непознати зони са **ОСЕМ** — Гръцката махала, Долна Трака, Колхозен пазар, Център, кв. Левски, кв. Св. Иван Рилски, кв. Тракия, кв. Христо Ботев. И осемте са ДОСЛОВНИ `display` низове в `quarter_registry.json`, а `build_place_categories.py:300-329` строи псевдонимите САМО от регистъра → лекът е прегенериране, нула ръчни низове.
17: 8. **М6 и формата на свидетеля (D6).** `CH_SIGNED_POLYGON` не е в `CHANNELS` (`:173-180`), затова редът носи `witness.quarter = ["SIGNED_POLYGON"]` без код в `channels` → проверка (б) (`qa_fire_varna_m6.py:304-308`) обявява 57 нарушители. Мерено днес: `qa_fire_varna_m6.py` връща **изход 3** („ЧАКА ПОДПИС: 8 реда", `:367`), не 0; спреният леджер носи същите 8 (`_meta.counts.pending_signature = 8`).
18: 9. **Пиновете.** `_check_pins` (`:922-949`) сверява НТР, двете таблици, `quarters_signed` и базата на леджера — но НЕ блока `inputs` (`RECORDED_INPUTS :108`). Затова `data/fire_varna_location_inputs.json:51` пинва `e8b4c836…`, а стейджнатата самоличност е `1141bbc2…`. Отделно `web/varna_buildings_3d.geojson` — ИЗВОРЪТ на координатите (`place_identity.py:90`) — изобщо не е в `RECORDED_INPUTS`, макар D10 (`010:56`) да го иска.
19: 
20: ## 2 · Двата пътя и присъдата
21: 
22: **Път Б** (ключът остава; `place_id` се носи през леджера) е механично възможен, но (i) износът не може да носи id, значи единственият носител е леджерът; (ii) зоната остава В КЛЮЧА, значи всяко чисто `python src/place_identity.py` (командата от собствения докстринг `:60`) връща същите два сирака. Ред на действията не е гейт.
23: 
24: **Път А** (`<файл>|skel(име)`): измерено — **375/375 `place_id` остават същите**; сменя се само полето `key` на 375-те живи обекта (оттеглените пазят записаните си ключове, уникалността `:668-672` остава); двата сирака изчезват по конструкция; появяват се 4 стълкновения при хотелите, за които ключът и без това не решава. `qa_place_sites.py:165-168` свързва по ключ, пресметнат от същия код от двете страни → прекодирането му е невидимо.
25: 
26: **Присъда: път А.** Ред в `RENAMES` не се съчинява от изпълнител: сирак → СТОП и имената при Петър.
27: 
28: ## 3 · Write-set и дословни съобщения (varna_3d, автор `Claude Executor <executor@local>`)
29: 
30: | # | Файлове | Съобщение |
31: |---|---|---|
32: | 1 | `src/place_identity.py` (`base` `:207,222`; `anchors_of:582`; `rule_key` в `_meta`; докстринг `:26,:176`) + `src/place_addresses.py:377` (второто копие на договора) | `fix(identity): drop the zone from the identity key, anchor on file and name skeleton` |
33: | 2 | `src/qa_identity_rekey.py` + `scratch/granitsi/rekey_negatives.py` и фикстурите | `gates: qa_identity_rekey with negative fixtures for the zone-free key` |
34: | 3 | **`src/qa_identity_refresh.py`** (G9-base: `KEY_PARTS` 3→2; C6 става „при освежаване ключът НЕ се мени"; C7 отпада — режимите „само key" и „само zone" са раздѐлни) + обновените `scratch/granitsi/identity_refresh_negatives.py` | `gates: qa_identity_refresh follows the zone-free key` |
35: | 4 | `src/fire_varna_locations.py` (`CH_DISTRICT_FALLBACK`; двата канала се пишат и в `channels` с `ids`/`raw` — изпълнение на D6) | `feat(m6): write the signed-polygon and district-fallback witnesses into the ledger channels` |
36: | 5 | `src/qa_fire_varna_m6.py` (**константата `LEDGER` НЕ се пипа**; нов `--ledger <път>`; ранг 3/4 за двата канала; полигонът пише само където петте низови канала мълчат; резервата иска районен код) | `gates: qa_fire_varna_m6 judges a ledger given as an explicit input` |
37: | 6 | `src/fire_varna_locations.py` (`_check_pins` сверява `inputs["data/place_identity.json"]`; нов `--accept-identity <sha>`, който пропуска ТАЗИ проверка ПРЕДИ строенето на книгата; `web/varna_buildings_3d.geojson` влиза в `RECORDED_INPUTS` като записан) | `fix(pins): verify the place identity pin on every run, refresh only with --accept-identity` |
38: 
39: Данните остават СТЕЙДЖНАТИ за комитите на Петър (D16/G4). Fire_Varna получава само този документ и реда в доклада.
40: **Записан дълг (датиран 07.09):** `lot1v_v_manifest.py:30` продължава да чете стария леджер по константа — изричен вход при следващия лот; `web/varna_buildings_3d.geojson` се записва, но още не се сверява в `_check_pins`; износителите продължават да пишат стенен часовник (`export_fire_varna_places.py:822`, `export_fire_varna_hotels.py:427`).
41: 
42: ## 4 · Ред на изпълнение
43: 
44: 1. **прекодиране:** генераторът върху ДНЕШНИТЕ износи → `data/place_identity.candidate.json`; `qa_identity_rekey` срещу база = стейджнатия блоб `1141bbc2…` (обектите: само `key`; `_meta`: само `rule_key`);
45: 2. **пиновете (веднага):** `python src/fire_varna_locations.py --inputs --accept-identity <sha от 1>` — без флага стъпка 2 умира в конструктора (`:903`), защото `--inputs` също минава през `load()` (`:1913-1916`);
46: 3. **присвояване:** `fire_varna_locations` → нови износи + датиран леджер;
47: 4. **освежаване на зоната:** генераторът върху НОВИТЕ износи → `qa_identity_refresh` (позволено поле: само `zone`; 0 нови, 0 оттеглени) → пиновете пак (`--inputs --accept-identity <нов sha>`);
48: 5. **речникът:** `build_place_categories.py`;
49: 6. **неподвижна точка:** присвояването се пуска втори път върху освежената самоличност → **леджерът излиза БАЙТ-ЕДНАКЪВ** (`_meta` му няма часовник — проверено), а двата износа са еднакви **след изключване на единствения назован ключ `_meta.generated`**. Сравнението прави гейтът, не окото.
50: 
51: ## 5 · Гейтове и отрицателни фикстури (всяка ТРЯБВА да падне)
52: 
53: - `qa_identity_rekey.py`: 375/375 `place_id` еднакви · 0 нови · 0 оттеглени · всеки нов ключ = `<файл>|skel(име)`(`#N`) · два прогона байт-еднакви. Отрицателни: подменен `place_id`; изтрит обект; ключ със зона; сменена и зона в режим „само ключ".
54: - `qa_identity_refresh.py` (обновен) зелен на стъпка 4; отрицателни: сменен ключ при освежаване; чуждо поле.
55: - `qa_place_sites.py` зелен (0 сираци в двете посоки); червено = СТОП с имената.
56: - `qa_place_zone_aliases.py` = 0 след прегенерирането. Отрицателни по **всичките осем** зони: изтрит ред за нова зона; ръчен псевдоним извън регистъра; застоял `legacy_bundle_sha`.
57: - `qa_fire_varna_m6.py --ledger <датирания>`: **`fails = 0` (изход 1 е забраненият) И изход 3 с ТОЧНО тези 8 поименни `pending_signature` реда** (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата), нито един повече. `--break-me witness` пада. Нови отрицателни: `SIGNED_POLYGON` в свидетеля без кода в `channels`; низов канал предлага код, а полигонът пише; резерва с код извън петте района.
58: - **Гейтовете на прегенерираните артефакти:** `qa_fire_varna_places_export.py`, `qa_fire_varna_export.py` (затвореният набор `_meta` ключове, вече 10 с `quarter_attribution`), `qa_fire_varna_location_isolation.py` — поименно, с командите.
59: - **Пинът:** обърнат hex знак в `inputs` → СТОП; освежаване без `--accept-identity` → СТОП.
60: - **Неподвижната точка:** отрицателна фикстура „подменен ред при еднакъв часовник → червено".
61: - `qa_p8a.py` (G17), `qa_no_cad_ids.py`, `python -m unittest` — зелени.
62: 
63: ## 6 · Комитите на Петър, в този ред
64: 
65: 1. `data/place_identity.json` + `data/fire_varna_location_inputs.json` — `data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned` (файлът носи ДВА товара: 1664/164 реда, от които 375-те координати на Б2-0)
66: 2. `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `data/place_categories.json` — `data: places and hotels with quarter by signed polygon, search dictionary regenerated`
67: 3. новият леджер — `data: p8a quarter assignment ledger 07.09`
68: 
69: ## 7 · STOP
70: 
71: Лотът спира и пита Петър при: сирак след прекодирането (поименно) · неподвижната точка различна извън `_meta.generated` · G17 показва променен написан квартал · зона без регистров запис след прегенерирането · опит да се впише ред в `RENAMES`/`MERGES` · комит на данни от агент · зелен гейт без доказано падаща отрицателна фикстура · `--inputs` без `--accept-identity`.
72: **Не е червен гейт, а грешка на оператора:** `qa_place_identity_coords.py` (G9) съди лот Б2-0 и по конструкция забранява смяна на `key`/`zone` — в този лот НЕ се пуска.
73: 
74: ## 8 · Решенията за Петър
75: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md -Encoding UTF8; 29..58 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$a[$_] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md -Encoding UTF8; 118..135 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$a[$_] }' in C:\git\Fire_Varna
 succeeded in 510ms:
119: 
120: 
121: ## 6 · ЧАСТ Б — нощ от резултати (тръгва само с подписан блок Б0)
122: 
123: ### Б0 · Блокът решения, който Петър подписва тази вечер (препоръките са на архитекта; всяко „да“ е негово)
124: 1. **Схема за ВНЕСЕНА геометрия (промяна на D1, обявена).** За Feature с `source ∈ {wikimapia, declared_streets}` полетата `drawn_by · drawn_at · basemap · viewport · visible_layers · screenshot_sha256 · approval_digest` са `null` по договор (гейт за взаимна изключителност: или ръка, или внос); `approved_by = "Petar"`, `approved_at = decided_at` от решенията; `signed_by = "Petar"` става валидно с подписа на този план по sha на решенията (т. 8); `witnesses[]` = [{kind: "wikimapia_object", url, fetched_at, raw_response_sha256}] (за Младост 2: {kind: "osm_carriageways", ways по име, fetched: 2026-09-06}); `version: 1`; `note = reason`. Останалите 14 полета на D1 остават задължителни. **Делта спрямо амандамент №2 §4 (К22 П1):** §4 null-ва четири полета (`drawn_by/drawn_at/viewport/screenshot_sha256`); тук се добавят още три — `basemap`, `visible_layers` и `approval_digest`; дайджестът на D1 (връзката одобрение ↔ байтове) се замества от sha-веригата на т. 8 (решения по sha → Feature с `wm_polygon_sha256` → `_meta.decisions_sha256`). Препоръка: да.
125: 2. **`wm_polygon_sha256` = канонизацията на D1** (6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; MultiPolygon по правилото на амандамент №2 §4). Суровият хеш от решенията се пренася като `raw_geometry_sha256` и гейтът сверява и двата. Препоръка: да.
126: 3. **Младост 2 — изричен подписан ключ по D2** за `code = mladost2`, `method = "street_bounded_face"`, лиценз `"ODbL © OpenStreetMap contributors"` (осите), `precision_m = 50`, четирите улици дословно в `witnesses`. Само този код; всеки друг Feature с този метод = червено. Препоръка: да.
127: 4. **Районът** се пише от НАШИЯ `district.code` на мястото (375/375 съгласие с АГКК, мерено 05.09), `district_src: "fire_varna_district"`; в Feature-ите на кварталите районът е изведен по представителна точка срещу същите наши 5 района, не от АГКК INSPIRE (G22 остава заключен). Резервата „място без квартал → районът“ пише `quarter = {name: <име на района>, code: <словесният код от DISTRICT_CODES>, src: "DISTRICT_FALLBACK"}` с три ограничения (К22 П3): (i) fallback-редовете **не са „написан квартал“** по D18/G17 — подписан полигон в бъдеща версия ги замества; (ii) място, което лежи в зона на код с `deferred`/`registry_pending` (16-те без решение, Ваялар, Младост 2 без ключа), **не получава fallback** — остава празно, поименно в леджера; (iii) място с `pin_outside_all` **или** чийто полигон противоречи на всеки наличен низов свидетел (кадастралният `quar` на тялото, адресният низ) отива в `disputed`, не се пише — координатата решава, но пин без нито един съгласен свидетел е подозрителен. Семантиката „quarter понякога е район“ е изрично „да“ тук, не само преизмерени пинове. Препоръка: да.
128: 5. **Десетият ключ на `_meta` се казва `quarter_attribution`** (името в §3.3 на амандамент №2 отпада); форма `{<code>: {src, url, label, licence}}` — независима от извора, носи Wikimapia, ODbL и бъдещи; UI редът се **рендерира от `label` и `url` на записа**, никога от фиксиран низ (К22 П2): за Wikimapia — „квартал по Wikimapia.org · обектът“ (двете като връзки по ToS §1.G); за `mladost2` — записът `{src: "openstreetmap", url: "https://www.openstreetmap.org/copyright", label: "© OpenStreetMap contributors", licence: "ODbL"}` (ODbL §4.3); без запис в картата — нищо. Отрицателна фикстура: код със `src: openstreetmap`, показан с Wikimapia-низ → ✗. Препоръка: да.
129: 6. **`precision_m`**: 100 за `wikimapia`, 50 за `street_bounded_face`; ръб = `max(50, precision_m)` по D7 → `edge_pending`. Препоръка: да.
130: 7. **`QUARTER_CODES` се разширява** с 41-те потвърдени кода, които днес липсват; `morska_gradina`, `sveti_nikola`, `zelenika` остават в `LOCALITY_CODES` (търсят се като местности); `QUARTER_SRC` получава `SIGNED_POLYGON` и `DISTRICT_FALLBACK`; `PLACES_CACHE` v6→v7; пиновете и `expectations.json` — в подредената доставка varna_3d → Fire_Varna. Препоръка: да.
131: 8. **Решенията**: Петър подписва `granitsi_decisions_3_2026-09-06_proba.json` **по sha256 на блоба в b6e627d** (`git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json | sha256sum`), с добавен от изпълнителя ред `attribution` (ToS §1.G) в СЪЩИЯ файл в нов комит, чийто sha той препотвърждава сутринта. Препоръка: да — това е Г2-б без нов блоб.
132: 9. **Родството — подписан DAG (измерен 06.09 вечерта, ≥ 98 % от детето вътре в родителя): 11 двойки** — abatko ⊂ kk_konstantin_elena · druzhba ⊂ asparuhovo · rozova_dolina ⊂ asparuhovo · kaisieva ⊂ vladislavovo · kokardzha_generic ⊂ izgrev_kv · mladost1 ⊂ mladost · mladost2 ⊂ mladost · saltanat ⊂ morska_gradina · vazrazhdane1 ⊂ vazrazhdane · vazrazhdane2 ⊂ vazrazhdane · vazrazhdane3 ⊂ vazrazhdane. **Частични припокривания (5–98 % от по-малкия), които НЕ са родство:** vazrazhdane4/vazrazhdane 72 % · pz_planova/vladislavovo 61 % · grackata_mahala/tsentar 52 % · vinitsa_sever/dobreva 51 % · maksuda/sv_ivan_rilski 39 % — място в такава двойна зона е `disputed`. Правилото е **транзитивно** по DAG-а (A ⊂ B ⊂ C → A печели пред B и C) и се подписва като геометричен факт за присвояването, без да се пипа регистърът (`parents` там е сутрешен дълг). Препоръка: да.
133: 10. **Ваялар** остава без граница тази нощ (`alias_of` → регистър сутринта); **Евксиноград** = 5729429 с бележката за конфликта на имена; **16-те без решение** → `deferred` в `_meta.registry_pending`. Препоръка: да.
134: 11. **Координатите на местата (промяна на D7/D10, обявена; Astra S21 т. 3).** D7 забранява изнесените координати за присвояване (кръгово), а `place_identity.json` има 0/375 lat/lon. Източникът става **представителната точка на кадастралното тяло, към което идентичността вече сочи** (`site_id`/`kais_i` → `web/varna_buildings_3d.geojson`), записана в `place_identity.json` от генератора (`coord_src: "kais_body_representative_point"`, `coord_precision_m: 20`); място без връзка към тяло → `no_coord`, остава празно и поименно в леджера. Ходът: резервно копие на `data/place_identity.json` в `C:/Users/Petar/AppData/Local/Temp/claude/C--git/26f42576-326e-4863-b700-f1e02c26a0c9/scratchpad/backup_place_identity_2026-09-06.json` (+ sha256 в пиновете; възстановяване: копиране обратно + проверка на sha), генериране в `data/place_identity.candidate.json`, G9 върху кандидата (байт-дифът спрямо основата е само в `lat`/`lon`/`coord_src`/`coord_precision_m`; `place_id` непроменени), подмяна САМО при зелено. Без това „да“ Б2 не тръгва и остава мярка Н2. Препоръка: да — това е „координатите не лъжат“, направено проверимо: координатата идва от кадастъра, не от нашия износ.
135: 12. **Изходите на присвояването — затворена, взаимно изключваща се таблица** (Astra S21 т. 6), в този ред: `written` (записан квартал, непроменен; ако полигонът е родител или дете на записания по DAG → `compatible`, иначе `disputed_written`) → `no_coord` → `pin_outside_all` → `edge_pending` (в ръба `max(50, precision_m)` на най-малкия съдържащ) → `disputed_overlap` (в ≥ 2 полигона без DAG връзка) → `deferred_zone` (полигон само на код от `registry_pending`/отложен) → `assigned_polygon` (най-малкият съдържащ по DAG) → `assigned_district` (само по т. 4 (i)–(iii)). Всяко място получава точно един изход; таблицата е гейт с фикстура за всяка клетка. Препоръка: да.
136: 

 succeeded in 523ms:
30: ## 2 · Стълбата на изворите v3 — за ГРАНИЦАТА
31: 
32: Номерацията на D0 (`010_signed_quarter_boundaries.md:36`) се пренарежда: степени (1) и (2) определят **линията**; написаният извор за **мястото** (REG/KAIS/НТР, рангове 0–2) и `POST-2018` остават непроменени.
33: 
34: **(1) Официален полигон.** (а) **АГКК INSPIRE `Geo_Names` Surface** — 6 кода, `source: "agkk_inspire_gn"`; заключен по G22/К8. (б) **Общинският слой „Квартали“** (52 полигона; `municipal_kvartali_layer_05.09.md:4-10`) — **днес заключен** (`SB_0005 Subscription is disabled`), проверката е скрипт, не писмо.
35: 
36: **(1-б) Реконструиран официален план — ОТДЕЛНО, ПО-НИСКО стъпало.** Одесоските 11 микрорайона са извадени от PDF по цвят и закачени с афинна трансформация (rms 11 m, max 21 m, 15 контролни точки) — **изведена от агент геометрия**. Полетата носят номера, не имена → **0 кода за G26 днес**; съответствието МР → регистров код е собствен подписан ред в опашката.
37: 
38: **Подът на неточността се поправя (S18).** Не „≥ 3×rms“, а `precision_m ≥ max(50, 3×rms, max_residual + raster_error)` — **предпазен минимум, не установена точност**. Фикстурата от ревизия 1 („rms 11 при `precision_m` 50“) е **невярна: тя МИНАВА**, защото `max(50, 33) = 50`. Отрицателната фикстура става **rms 20 при `precision_m` 50**. RMS върху използваните центроиди мери напасването, не линията: не включва грешното съответствие, растеризацията и поведението между контролните точки. **Независима проверка на линията:** 20 предварително избрани точки по периметъра срещу доказано СЪЩАТА граница, отчетени `dmax` и `p95`; най-близкият произволен КАИС ръб на парцел дава фалшив успех и не се брои. Без нея реконструкцията остава **свидетел**, не граница. Подписът МР → код решава идентичност, не точност.
39: 
40: **(2) Човешки полигон — Уикимапия** (CC BY-SA), `source: "wikimapia"`, `method: "human_polygon"`. Пиннат с **`wm_polygon_sha256`** (пълни 64 hex; `polygon_sha256` е зает от D3), плюс `wm_id`, `fetched_at`, `url`. Канонизацията е дословно тази на D1. **Валиден САМО след изричното „да“ на Петър за ТОЗИ квартал**, с подписан ред от crosswalk-а „заглавие ↔ регистров код“ — никакъв автоматичен матчер.
41: 
42: **Конфликтите (разширено D6, поправено по S16).** Три измерени класа: (а) **човешки ↔ човешки** — „Район Младост“ е два полигона (13,22 и 12,34 km²); (б) **един полигон ↔ два кода** — „Комплекс Чайка“ пасва и на `chaika_kv`, и на `chaika_kk`; (в) **грешен вид** — „Район Младост“ е РАЙОН, „Изгрев“ е с.о. **`classify(code) == field` НЕ доказва вида на изворния полигон** — районен полигон може да получи валиден квартален код и да мине проверката. Минималното правило, което влиза в D6: **подписан source-kind crosswalk; точно един избран изворен Feature на код; една геометрия никога към два несравними кода; неразрешено двусмислие → без писане.** Нормализаторът на заглавия (в данните стои `&amp;quot;`, най-големият обект е „Βарна“ с гръцка бета) **не решава** „Чайка“ и двата „Младост“. Родител/дете — само по подписано И геометрично проверено родство (D8).
43: 
44: **`precision_m` за чужда геометрия.** `district_map_georef` по формулата горе; `wikimapia` ≥ 100 m до доказано друго; Feature без явен `precision_m` = червено. **Ръбът е по D7: `edge = max(50, precision_m)`** (ревизия 1 пишеше „ръб 50 m“ — невярно при `precision_m` 100). Фикстура: празен безспорен ред, точка и тяло на 75 m навътре, `precision_m` 100 → `edge_pending`, без присвояване; на повече от 100 m и без други пречки → допустимо `written`.
45: 
46: ## 3 · Лицензът — присъдата на Кими е ЗАПИСАНА; клонът остава блокиран от G28
47: 
48: **3.1 Прието третиране.** Геометрията остава в `varna_3d/data` и **никога не се публикува** (D3 `:42`); публичният ред остава 13/17 ключа с `quarter: {name, code, src}`.
49: 
50: **3.2 „Публикуването на име не е адаптация“ е ПОЗИЦИЯ с довод, не консенсус (К16).** Довод: §1(b) на CC BY-SA 3.0 определя Adaptation като произведение, основано върху Произведението (превод, преработка, аранжировка). Point-in-polygon **не пренася израз** от полигона — резултатът е факт (пространствено отношение) плюс предсъществуващо кратко име; имената са факти. Значи §4(b) ShareAlike не захапва изнесените редове. **ODbL-аналогията „produced work“ е изрично невалидна:** „Produced Work“ е дефиниран термин на ODbL (§1.0, §4.3–4.4), създаден защото ODbL покрива правата върху бази; CC BY-SA няма такава категория — анализът при CC е само „Adaptation или не“. Позицията влиза дословно в `_meta.source_terms["wikimapia"].position`.
51: 
52: **3.3 Зависимостта на G27 (К18).** §4(c) на CC BY-SA 3.0 се задейства при разпространение. Частният geojson не се разпространява — атрибуцията там е provenance. Публичните редове, **АКО позицията по 3.2 издържи**, не са Adaptation → публична атрибуция не се изисква по лиценза. **Но ToS §1.G на Уикимапия** (по-долу, 3.5) иска при „public use of Wikimapia Data and it's derivatives“ връзка към оригиналния обект и „Wikimapia.org“ — дали присвоеното име е „derivative“ по смисъла на §1.G е част от присъдата на Кими (К18). **Присъда К21 (Кими, 06.09 ~01:40): тежкият клон се задейства.** Позицията по 3.2 издържа като лицензен анализ, но §1.G е **договорна клауза**, не лицензна: „Public use of Wikimapia Data and it's derivatives requires…“ — публикуваното име на квартал само по себе си е Wikimapia Data (заглавията са User Submissions по §1.B/§1.F), а полигонът определя кое име се присвоява; приложението се гледа в браузър, тоест „if viewed from any web browser“ е изпълнено. Следствие: **публичната атрибуция е ЗАДЪЛЖИТЕЛНА** за всеки показан ред с уикимапийски квартал — (1) „Wikimapia.org“ с връзка към http://wikimapia.org и (2) връзка към оригиналния URL на обекта (напр. `wikimapia.org/1851926`). Механично: нов български UI низ + `licence_quarter_boundary` в `META_KEYS`, в пиновете на D13 и в двата преписа, в СЪЩИЯ комит; текстът на низа е отделно одобрение на Петър → **решение §7 т. 8**. G27 се пренастройва да сверява този публичен низ, не само частния файл.
53: 
54: **3.4 Sui generis право върху база данни (К15).** §3 в ревизия 1 поднасяше защитата като даденост. Записва се пълно:
55: - **(а) Носителят и юрисдикцията.** Правото е на „производителя“ с съществена инвестиция (чл. 7(1), Дир. 96/9/ЕО); чл. 11 дава защита само на граждани/резиденти на ЕИП и дружества по правото на ЕИП. **Ако производителят на Уикимапия е извън ЕИП, базата не се ползва от sui generis защита в ЕС** и въпросът отпада по същество. **Мярка (06.09, ~01:15):** самите условия на Уикимапия, §3, казват: „The SERVICE is controlled and offered by WikiMapia from its facilities in the United States of America.“ Това е собственото твърдение на оператора, не независима проверка на правната форма и седалището — влиза в `source_terms` като цитат; присъдата дали чл. 11 изключва защитата е на Кими.
56: - **(б) Пълният тест на чл. 7(5).** ~180 полигона от милиони обекта не са съществена част нито количествено, нито качествено. Забраната на чл. 7(5) е за **повтарящо се и систематично** извличане на несъществени части, **което противоречи на нормалното използване на базата ИЛИ наранява неоснователно законните интереси на производителя** — двете кумулативни условия липсваха в ревизия 1. Обходът е систематичен; „противоречие с нормалното използване“ на безплатна публична база за некомерсиална карта е твърдение, което носещият тежестта трудно доказва. **Присъда: дори при съществуваща защита нарушението е оспоримо, не очевидно.**
57: - **(в) Извличане ≠ повторно използване.** „Геометрията никога не се публикува“ е щит срещу **reutilization**, не срещу **extraction**. Извличането вече се е случило — обходът тече (§0). **Присъдата по G28 е пост-фактум оценка на извършено действие, не разрешение.**
58: 
59: **3.5 ToS/API (К17) — входът на G28 е попълнен с цитати; присъдата остава на Кими.** `_meta.source_terms["wikimapia"]` носи `{url, checked_on, quote, terms, verdict, position}`, където `quote` е дословен цитат ≤ 2 реда. Записаното към 06.09.2026 (пълната мярка: `scratch/places_search/wikimapia_terms_2026-09-06.md`):

codex
Проверката откри две съществени ограничения. Замразеният корпус проверява места и хотели, но не тези адреси. А „най-малкият полигон“ избира победител и при неподписани припокривания: 5 620 адресни записа попадат в два полигона. Това трябва да се отдели от автоматично допустимите поправки.

codex
С точния нормализатор четирите ти броя се възпроизвеждат. Те обаче още не са списък за автоматична поправка: има 1 418 записа в несравними припокривания и 29 054 вътрешни записа в лентата на неточност. „Център“ има подписан полигон; проблемът там е непълно покритие, а не липсващ полигон.

codex
**Поправката принадлежи в генераторите на Varna_buildings, при билд с пиннатите частни полигони. Самото добавяне към `qtk` обаче поправя намирането, без да премахва грешната квартална принадлежност.** Препоръчвам отделен лот след Б3 с ясно разделени каноничен квартал и кадастрален alias.

Проверено read-only: Fire_Varna `321d209` с подготвен Б3 в стейджа; Varna_buildings `4c6b482`; varna_3d `05f485e`. Инвентаризирани и прочетени са посочените генератори, клиентски диапазони, payload-и, мярка, полигони и гейтове. Нищо не е променено или комитвано.

1. **Механика и място.** Общ build-time resolver трябва да обслужва [`buildPublicIndex()`](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:546) и [`buildAddressRows()`](C:/git/Varna_buildings/js/build_fire_varna_address_rows.mjs:91). Първият днес копира кадастралния `qtk` на ред 701; вторият почиства адресния низ, без пространствено присвояване. Частният GeoJSON се чете директно по проверен SHA; геометрия не се копира във Fire_Varna.

   Покрий **двата display пътя**: 43 133 записа с `label` и 43 295 с `display_id`. Клиентът избира между тях на [`index.html:4881`](C:/git/Fire_Varna/index.html:4881). Поправка само на кварталния префикс в индексния `label` пропуска половината резултати.

   Препоръчвам канонични квартални токени плюс отделен свидетелски alias, който **не удовлетворява изричен квартален филтър**. Днешният `alias_tk` също няма тази защита. Изпълних действителния matcher в паметта: добавяне на `levski` към двата записа за Студентска бл. 11 прави **и „Левски Студентска бл 11“, и „Чайка Студентска бл 11“ пълни точни съвпадения** ([клиент:5204](C:/git/Fire_Varna/index.html:5204)).

   Подписът трябва изрично да определи приоритета спрямо [Р38](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:873). Нужна е и повторна проверка на блоковите колизии: сегашният [`buildBlockLabelIndex()`](C:/git/Varna_buildings/js/lib_fire_varna_block_labels.mjs:155) разграничава по стария квартал.

2. **Политика за празните и външните.** За безспорна вътрешна точка извън лентата на неточност: подписаното име с правилния вид — квартал, местност и т.н. При припокриване печели само подписаното дете по йерархията. За останалите: кварталът остава неопределен; показва се провереният район, ако е наличен. „Без квартал“ твърди повече, отколкото знаем; нов такъв UI текст не е необходим.

   **13 265 извън полигони не означава 13 265 без квартал.** Не използвай най-близък полигон или буфер за автоматично присвояване. Преди билда Петър подписва как се третират непокритите части около Цветен квартал, Колхозен пазар и Център — допълнена граница или изрично отложени записи. Център **има** полигон; липсва пълно покритие.

   Студентска бл. 11 е специален стоп: собственото измерване на двата индексни пина дава **67,52/68,16 m**, при `precision_m=100`. Следователно и твоите 59 m, и възпроизведените разстояния попадат в `edge_pending`, а не в автоматично допустимите поправки.

3. **Размер и търсене.** Измерено:

   | Файл | Байтове | gzip9 |
   |---|---:|---:|
   | search_index | 11 242 756 | 1 056 136 |
   | address_rows | 5 073 137 | 517 466 |

   При първото активиране търсачката зарежда общо **16 315 893 B**; това е lazy товар. Илюстративно добавяне само на полигонни `qtk` към всички вътрешни записи увеличи компактния JSON с около **1,41 MB**, без етикети, речник и ограниченията за ръбове. Това не е допустим кандидат или окончателен бюджет.

   Добавките влияят и на заявки **без квартал**: сортирането използва `tk.length + qtk.length` ([5252](C:/git/Fire_Varna/index.html:5252)). Мерят се ред, групиране, надпис и пълнота на съвпадението.

   Approx е отделен пакет: **8 361 записа**, собствен `quarter`, флаг `false` ([5926](C:/git/Fire_Varna/index.html:5926)). Поправката на двата адресни файла не го поправя. Оставането му изключен е проверимо условие; бъдещото включване изисква същата пространствена политика.

4. **Минимален лот и гейтове.** Write-set: общ resolver и неговите тестове; двата генератора; двата публични адресни файла; клиентският квартален matcher/display/cache; отделен адресен корпус и подписван манифест. Частният одит пази входни SHA, старо/ново, кандидат-кодове, разстояние и причина. Геометрията и регистърът остават пиннати предпоставки.

   Доставката следва **D13: Varna_buildings → varna_3d → Fire_Varna**; планът трябва изрично да назове адресните артефакти и проверките във всяко звено. Във Fire_Varna данни, клиент и версия на кеша влизат съгласувано.

   Отрицателните половини трябва да събарят: грешен стар квартал като авторитетно съвпадение; неподписан/ръбов/двусмислен assignment; променени координати, номер, вход или идентичност; геометрия в публичния износ; смесени поколения кеш; необяснена делта. Два билда дават еднакви байтове; проверява се UTF-8.

   **Посоченият замразен корпус не проверява адресите**: [двигателят:73](C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:73) зарежда само хотели, места и категории. За него очакването е нулева делта; нужен е нов адресен replay. Петър подписва политиката, изключенията, точните UI низове, write-set-а и измерения манифест преди замразяване.

5. **Одит на мярката.** С точния [`norm/skel`](C:/git/Varna_buildings/app/modules/search/skeleton.js:31) възпроизведох **6 655 / 8 384 / 57 928 / 13 265**. Корекции в тълкуването:

   - **57 928 означава „без qtk“**; 3 936 от тях вече имат „кв./ж.к.“ в етикета.
   - 5 620 записа са в два полигона: 4 202 в подписано родство, **1 418 в несравними припокривания**.
   - **29 054** вътрешни записа са в лентата `max(50, precision_m)`.
   - Съгласие по един токен допуска поне **25 неверни „Средна/Долна Трака“ съгласия**.
   - Нула невалидни полигони, дупки или точки точно на ръб; 86 232 записа представляват 85 651 различни координати.

   Следователно мярката е добра диагностика, но още не е разрешен write-set.
tokens used
90,860
**Поправката принадлежи в генераторите на Varna_buildings, при билд с пиннатите частни полигони. Самото добавяне към `qtk` обаче поправя намирането, без да премахва грешната квартална принадлежност.** Препоръчвам отделен лот след Б3 с ясно разделени каноничен квартал и кадастрален alias.

Проверено read-only: Fire_Varna `321d209` с подготвен Б3 в стейджа; Varna_buildings `4c6b482`; varna_3d `05f485e`. Инвентаризирани и прочетени са посочените генератори, клиентски диапазони, payload-и, мярка, полигони и гейтове. Нищо не е променено или комитвано.

1. **Механика и място.** Общ build-time resolver трябва да обслужва [`buildPublicIndex()`](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:546) и [`buildAddressRows()`](C:/git/Varna_buildings/js/build_fire_varna_address_rows.mjs:91). Първият днес копира кадастралния `qtk` на ред 701; вторият почиства адресния низ, без пространствено присвояване. Частният GeoJSON се чете директно по проверен SHA; геометрия не се копира във Fire_Varna.

   Покрий **двата display пътя**: 43 133 записа с `label` и 43 295 с `display_id`. Клиентът избира между тях на [`index.html:4881`](C:/git/Fire_Varna/index.html:4881). Поправка само на кварталния префикс в индексния `label` пропуска половината резултати.

   Препоръчвам канонични квартални токени плюс отделен свидетелски alias, който **не удовлетворява изричен квартален филтър**. Днешният `alias_tk` също няма тази защита. Изпълних действителния matcher в паметта: добавяне на `levski` към двата записа за Студентска бл. 11 прави **и „Левски Студентска бл 11“, и „Чайка Студентска бл 11“ пълни точни съвпадения** ([клиент:5204](C:/git/Fire_Varna/index.html:5204)).

   Подписът трябва изрично да определи приоритета спрямо [Р38](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:873). Нужна е и повторна проверка на блоковите колизии: сегашният [`buildBlockLabelIndex()`](C:/git/Varna_buildings/js/lib_fire_varna_block_labels.mjs:155) разграничава по стария квартал.

2. **Политика за празните и външните.** За безспорна вътрешна точка извън лентата на неточност: подписаното име с правилния вид — квартал, местност и т.н. При припокриване печели само подписаното дете по йерархията. За останалите: кварталът остава неопределен; показва се провереният район, ако е наличен. „Без квартал“ твърди повече, отколкото знаем; нов такъв UI текст не е необходим.

   **13 265 извън полигони не означава 13 265 без квартал.** Не използвай най-близък полигон или буфер за автоматично присвояване. Преди билда Петър подписва как се третират непокритите части около Цветен квартал, Колхозен пазар и Център — допълнена граница или изрично отложени записи. Център **има** полигон; липсва пълно покритие.

   Студентска бл. 11 е специален стоп: собственото измерване на двата индексни пина дава **67,52/68,16 m**, при `precision_m=100`. Следователно и твоите 59 m, и възпроизведените разстояния попадат в `edge_pending`, а не в автоматично допустимите поправки.

3. **Размер и търсене.** Измерено:

   | Файл | Байтове | gzip9 |
   |---|---:|---:|
   | search_index | 11 242 756 | 1 056 136 |
   | address_rows | 5 073 137 | 517 466 |

   При първото активиране търсачката зарежда общо **16 315 893 B**; това е lazy товар. Илюстративно добавяне само на полигонни `qtk` към всички вътрешни записи увеличи компактния JSON с около **1,41 MB**, без етикети, речник и ограниченията за ръбове. Това не е допустим кандидат или окончателен бюджет.

   Добавките влияят и на заявки **без квартал**: сортирането използва `tk.length + qtk.length` ([5252](C:/git/Fire_Varna/index.html:5252)). Мерят се ред, групиране, надпис и пълнота на съвпадението.

   Approx е отделен пакет: **8 361 записа**, собствен `quarter`, флаг `false` ([5926](C:/git/Fire_Varna/index.html:5926)). Поправката на двата адресни файла не го поправя. Оставането му изключен е проверимо условие; бъдещото включване изисква същата пространствена политика.

4. **Минимален лот и гейтове.** Write-set: общ resolver и неговите тестове; двата генератора; двата публични адресни файла; клиентският квартален matcher/display/cache; отделен адресен корпус и подписван манифест. Частният одит пази входни SHA, старо/ново, кандидат-кодове, разстояние и причина. Геометрията и регистърът остават пиннати предпоставки.

   Доставката следва **D13: Varna_buildings → varna_3d → Fire_Varna**; планът трябва изрично да назове адресните артефакти и проверките във всяко звено. Във Fire_Varna данни, клиент и версия на кеша влизат съгласувано.

   Отрицателните половини трябва да събарят: грешен стар квартал като авторитетно съвпадение; неподписан/ръбов/двусмислен assignment; променени координати, номер, вход или идентичност; геометрия в публичния износ; смесени поколения кеш; необяснена делта. Два билда дават еднакви байтове; проверява се UTF-8.

   **Посоченият замразен корпус не проверява адресите**: [двигателят:73](C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:73) зарежда само хотели, места и категории. За него очакването е нулева делта; нужен е нов адресен replay. Петър подписва политиката, изключенията, точните UI низове, write-set-а и измерения манифест преди замразяване.

5. **Одит на мярката.** С точния [`norm/skel`](C:/git/Varna_buildings/app/modules/search/skeleton.js:31) възпроизведох **6 655 / 8 384 / 57 928 / 13 265**. Корекции в тълкуването:

   - **57 928 означава „без qtk“**; 3 936 от тях вече имат „кв./ж.к.“ в етикета.
   - 5 620 записа са в два полигона: 4 202 в подписано родство, **1 418 в несравними припокривания**.
   - **29 054** вътрешни записа са в лентата `max(50, precision_m)`.
   - Съгласие по един токен допуска поне **25 неверни „Средна/Долна Трака“ съгласия**.
   - Нула невалидни полигони, дупки или точки точно на ръб; 86 232 записа представляват 85 651 различни координати.

   Следователно мярката е добра диагностика, но още не е разрешен write-set.
