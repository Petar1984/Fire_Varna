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
session id: 01a07dfb-c62e-70d0-9659-cab68edaa7e8
--------
user
S32 · Оборване на ПЛАН „Адресите по полигон“ v2 (леща МЕХАНИКА и гейтове), read-only. Файл: C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md (v2, чернова f745349). Контекст: твоята S31 (scratch/places_search/adresi_astra_S31_08.09.md); мярката scratch/places_search/adresi_po_poligon_measure_08.09.md; генераторите в C:/git/Varna_buildings/js/ (build_fire_varna_search_index.mjs, build_fire_varna_address_rows.mjs, lib_fire_varna_block_labels.mjs, lib_quarter_registry.mjs, test_fire_varna_publish_gate.mjs); клиентът C:/git/Fire_Varna/index.html (адресната търсачка ~4816-4900, ~5130-5260, approx ~5926-6070); гейтовете gates/*.py, tests/test_places_search_gate.py; полигоните: git -C C:/git/varna_3d show 05f485e:data/quarters_signed.geojson; данните data/search_index.json, data/address_rows.json. Атакувай САМО механиката: (1) §4 write-set и §1.В точките на вмъкване — верни ли са редовете/функциите, минимален ли е дифът, резолверът наистина ли обслужва ДВАТА display пътя (label / display_id) и структурните полета q/o/quarter_names (Р12/Р15) — измери какво чупят в клиента (entryTokenSet, _areaVocab, resolveC2BlockLabel, scoreEntry, компаратора); (2) §6 гейтове — всеки: може ли да мине без да докаже твърдението, пада ли отрицателната половина по СЪЩОТО твърдение (структурна проверка за геометрия/dist_to_edge_m, два билда байт-еднакви, generation coupling, address replay с --freeze и селектор, гардът на свидетеля wtk ∩ qtk = ∅, G-A6б срещу подписан остатък); (3) §5 редът — PowerShell без &&, без UTF-16 капани (> редирект), пин по OID, редът подпис→freeze→run_gates, Б3 комитван пръв и index.html в двата write-set-а; (4) М0 преизмерванията — изпълними ли са и пълни ли са. Измервай сам където можеш (нищо не пипай, нищо към отдалечено хранилище). Присъда: ГОДНО за подпис / НЕГОДНО с S32-1… (доказателство path:line или изход + точна поправка); до 800 думи.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя механиката спрямо кода и измерванията, без промени по файловете. Ще разделя проверката на генератори, гейтове и клиент, после ще събера само доказуемите дефекти в присъдата S32.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git status -sb; git rev-parse HEAD; Get-Content -LiteralPath 'docs/activeContext.md' -Encoding UTF8 -TotalCount 110" in C:\git\Fire_Varna
 succeeded in 543ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 106]
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
?? scratch/places_search/adresi_astra_S32_08.09.md
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
f745349a40ea14a6961d78da11e16744507f2a40
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$targets = @('"'AGENTS.md','docs/plans/ПЛАН_Адресите_по_полигон_08.09.md','scratch/places_search/adresi_astra_S31_08.09.md','scratch/places_search/adresi_po_poligon_measure_08.09.md','index.html','tests/test_places_search_gate.py','data/search_index.json','data/address_rows.json'); "'$targets | ForEach-Object { if (Test-Path -LiteralPath $_) { Get-Item -LiteralPath $_ | Select-Object FullName,Length } }; rg --files gates -g '"'*.py' --max-count 20 --max-columns 200 | Sort-Object; Get-ChildItem -LiteralPath 'C:/git/Varna_buildings/js' -File | Where-Object { "'$_.Name -in @('"'build_fire_varna_search_index.mjs','build_fire_varna_address_rows.mjs','lib_fire_varna_block_labels.mjs','lib_quarter_registry.mjs','test_fire_varna_publish_gate.mjs') } | Sort-Object Name | Select-Object FullName,Length" in C:\git\Fire_Varna
 succeeded in 722ms:

FullName                                                                     Length
--------                                                                     ------
C:\git\Fire_Varna\AGENTS.md                                                   27909
C:\git\Fire_Varna\docs\plans\ПЛАН_Адресите_по_полигон_08.09.md                97454
C:\git\Fire_Varna\scratch\places_search\adresi_astra_S31_08.09.md            235364
C:\git\Fire_Varna\scratch\places_search\adresi_po_poligon_measure_08.09.md     7900
C:\git\Fire_Varna\index.html                                                 566532
C:\git\Fire_Varna\tests\test_places_search_gate.py                           155787
C:\git\Fire_Varna\data\search_index.json                                   11242756
C:\git\Fire_Varna\data\address_rows.json                                    5073137
gates\__init__.py
gates\coverage.py
gates\probe\b3_g11.py
gates\release.py
gates\run_gates.py
gates\sign.py
C:\git\Varna_buildings\js\build_fire_varna_address_rows.mjs                    7626
C:\git\Varna_buildings\js\build_fire_varna_search_index.mjs                   67575
C:\git\Varna_buildings\js\lib_fire_varna_block_labels.mjs                     11844
C:\git\Varna_buildings\js\lib_quarter_registry.mjs                            19376
C:\git\Varna_buildings\js\test_fire_varna_publish_gate.mjs                    28780



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$n=0; Get-Content -LiteralPath $p -Encoding UTF8 | ForEach-Object { $n++; if ($_ -match '"'"'^#{1,4} |''^'"\\|.*(М0|G-A|Б3|Р12|Р15)|write-set|freeze|wtk|qtk') { '{0}: {1}' -f "'$n,$_ } }' in C:\git\Fire_Varna
 succeeded in 579ms:
1: # ПЛАН · Адресите по полигон (v2)
16: ## 0 · Червени редове (важат за всеки ход)
28: 11. **Един логически комит = един ход**, точното съобщение от §5, стейджване с явни пътища, никога `git add -A`. **`index.html` е в ДВАТА write-set-а** — преди F1 `git diff --cached -- index.html` трябва да е празен (§7 т. 14).
33: ## 1 · Мярка
35: ### А. Базата (всяко число с извор)
43: | полета | `label` 43 133 · `display_id` 43 295 · и двете 196 · `qtk` 19 494 · `alias_tk` 574 · `stk` 362 · `btk` 5 567 · `d` 85 935 |
53: Проверимост на днешните думи: от 19 494 с `qtk` само **8 968 (46,0 %)** стоят там, където полигон може да ги потвърди или обори.
66: **Флагманът (двамата опровергатели съвпадат, третият го потвърждава по друг път):** записът `{"kind":"mf","pin":[43.22212,27.9378],"tk":["studentska","bl","11"],"qtk":["chaika"],"label":"кв. Чайка, бл. 11","g":"b6797e83ec13fe798"}` е **вътре в кв. Левски на 67,4 m от ръба** при `precision_m = 100`; най-близкият чужд полигон **ж.к. Бриз е на 82,8 m** — тоест конкурент В лентата. Под Р5(а) и Р5(в) на v1 този запис **остава без квартал** → v1 не решаваше жалбата на Петър (§12).
69: **Днешното поведение на клиента** (СКАУТ 2 §1, реален матчер): „чайка студентска бл 11“ → ред 1 = `кв. Чайка, бл. 11`, `all=true`, съвпадението през **`qtk`**; „левски студентска бл 11“ → сградата **не излиза изобщо**; „левски битоля 13“ → `all=true` за улица извън всички полигони.
91: **Размерът на промяната (две независими оценки, и двете >> „~+0,3 MB“ от v1):** semantics ≈ **+1,26 MB** само за каноничния `qtk` + `q`; delivery ≈ **+1,54 MB** (q 0,308 + wtk 0,420 + нето qtk 0,812). Реалната стойност зависи от правилото за `wtk` (§4.1 т. 2) → М0.10.
95: ### Б. М0 — задължително преизмерване преди първия ред код
101: | М0.1 | **OID на полигоните** | `git -C C:/git/varna_3d rev-parse 05f485e:data/quarters_signed.geojson` | пинът е СЪДЪРЖАНИЕ, не комит; двамата опровергатели измериха един и същ блоб `82706fb5fef494175f912db82a871a6c38b4e472`, 301 917 B, sha256 `c1551d24…871b3` за 05f485e И 6486b48 → „противоречието“ на v1 отпада (§11.1) |
102: | М0.2 | байтовете + sha256 | Python: `subprocess.run(["git","-C","C:/git/varna_3d","cat-file","blob",OID],capture_output=True).stdout` → sha256 върху буфера → `open(...,"wb")` | константата `SIGNED_QUARTERS_OID/SHA256` не бива да пинова артефакт на обвивката |
103: | М0.3 | квартални маркери в `address_rows` | явен списък дефиниции | не е противоречие, а 4 дефиниции: буквално „кв./ж.к.“ **0**; водещ гол маркер **4 965**; „местност“ някъде **4 139**; подписано име като дума **23 888** (semantics) |
104: | М0.4 | сплит на припокриванията | скрипт по метода на СКАУТ 3 | 1 446/4 174 срещу 4 202/1 418 |
105: | М0.5 | **лентата: пълната таблица** | нов скрипт: за всеки пин — съдържащи полигони, `d_edge` до собствения ръб, най-близък чужд ръб | дава числата за Р5 (а)/(б)/(в)/(г) и за Р5-д; днешните оценки: 25 613 в лентата, 11 641/11 625 с конкурент, 2 156 извън лентата с конкурент, 4 042 извън-но-в-лентата |
106: | М0.5-б | **флагманите поименно** | същият скрипт, за пиновете `[43.22212,27.9378]`, `[43.21976,27.91949]`, „Цветен квартал бл. 11“, 3 записа на ул. Битоля | тези числа влизат ДОСЛОВНО в Р4/Р5 и в фикстурата на G-A3-г |
107: | М0.6 | **ориентирът** | за всички mf с `btk`: собствена улица (двете дефиниции на Р10), най-близка улична точка ≤ R, разстояние, отхвърлени низове, колизионни двойки и НЕразличими групи | сверява 385↔91↔95, 24↔16, 1 324↔213; **разминаване = СПИРАЙ** |
108: | М0.7 | блокови колизии ПРЕДИ | `npm run build:fire-varna:staging`, запис на `blockGroups/collisionPairs/collisionGroups/disambiguated/collisionNoStreet` (`build_fire_varna_search_index.mjs:1113-1116`) + `c2ResByReason` | смяната на квартала и махането на уличния суфикс пренареждат ключа `(quarter, block#)` |
109: | М0.8 | S9 базата | същият билд, `tokenInconsistentTotal` срещу `S9_BASELINE = 5828` (`:452-454`, `:1042-1051`) | дрифт гейтът ще реагира |
110: | М0.9 | червената база на Fire_Varna | `python -m gates.run_gates` · `python -m unittest discover -s tests` | днес: exit 1 (✗4, ✗6) и 24/342 паднали (СКАУТ 4) — адресният лот декларира СВОЙ назован интервал по G20 |
111: | М0.10 | **размерът** | пробен билд с новите полета → байтове на двата payload-а | Р12-в подписва таван; днес 15,57 MiB lazy |
112: | М0.11 | **състоянието на индекса** | `git -C C:/git/Fire_Varna status --porcelain` + `git diff --cached --stat -- index.html` | delivery измери `M  index.html` СТЕЙДЖНАТ (106+/24−) — F1 не тръгва, докато Б3 не е комитнат |
113: | М0.12 | районът на флагманите | `d` на записите с `bitolia`, `studentska bl 11` | v1 писа „район Одесос“; semantics измери 42/42 = **Приморски** (`d=4`), а `district_names` е проверен от Planner-а |
115: ### В. Точки на вмъкване (всички проверени лично от Planner-а сега)
117: **`C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs`:** `:452-454` S9 база · **`:457-458` `TYPEWORDS` (няма „do“)** · `:459-471` `canon` · `:481-487` `entryTokenSet(e)` — чете **геокодерния** запис, не публичния `o` · `:502-509` `s9Inconsistency` (правило (1): всички улични токени липсват → inconsistent) · **`:609-619` `resolveC2BlockLabel` — fail-closed, `reason:"token_inconsistent"`** · `:698` `o = {kind,pin}` · **`:701` `qtk` — единственото място, където кварталните токени влизат в индекса** · `:722-724` dtk/stk/btk · `:731` `evaluateRow` · **`:743-754` C2** · `:757-779` S9 · `:806` `display_id` само при липсващ label · `:826-842` F3 (не прилага повторно токеновия гард) · `:847-850` tidy · **`:857-871` регистърът** · **`:873-922` Р38** · `:923` push.
123: **`C:/git/Fire_Varna/index.html`:** `4881-4892` `baseAddressLabel` (label → `addressRows[display_id].normalized_address` → район) · `4893-4897` `formatAddressHit` · `5088-5100` `dedupeDisplayRows` · **`5134` резервен vocab · `5140-5145` postings · `5151` `_areaVocab = dtk∪qtk∪stk`** · `5164-5171` `qBlk`/`areaPresent`/`blockTyped` · `5197-5221` `scoreEntry`: tk `:5204` → alias `:5205` → **`matchedCore += 1` `:5206`** → **qtk `:5207`** → dtk `:5208` → stk `:5209` · **`:5216-5219` `dem`/`ddem`/`odem`/`sdem` — всичките с условие `matchedCore === 0`** · `5230-5256` компаратор, **`5252-5253` `tk.length + qtk.length`** · `5265` `trueTie` · **`5278-5288` груповият блоков клон** · `5291-5299` bare-block · `5303`/`5313` двете проекции · `5327` `SEARCH_CACHE` · **`5351-5372` `ensureSearchData` — тук е единственият слой, който може да е fail-closed** · `5411-5423` `buildExactItem` (`5417` заглавие, `5420` „район X“) · `5430` `'Няма съвпадения'` · `5926` approx = false.
125: ### Г. Гейтове днес — какво покрива адресната доставка
127: Нула от седемте на `run_gates`: `SHA_PINS` (`gates/run_gates.py:68-72`) и `PUBLIC_BLOBS` (`:82-87`) са затворени около hotels/places/categories/signed_facts; **`check_no_cad_ids` чете РАБОТНОТО ДЪРВО и мълчаливо пропуска липсващ файл** (`:188-191`); `coverage.py:75` = `("places","hotels")`. Пипат адресите само `tests/test_data_ascii_mojibake.py:35-36` и `tests/test_basemap_manifest.py:164-165`. `data/generation_manifest.json` не се чете от никого. `recall_sweep.py:73-76` работи само върху hotels/places/categories → **замразеният корпус не покрива адреси и няма адресна `--freeze` команда** (`:90`). Единственият истински пазач е публикационният гейт в `Varna_buildings`.
132: ## 2 · Целта и НЕ-целта
138: | в точно един полигон, **извън лентата** | името на полигона | `wtk` (търсим, демотиран) | „кв. Левски, …“ |
156: ## 3 · Решения за Петър преди билда
161: *Препоръка:* **подпиши ADR 007 И подпиши разширението му** (нов ADR 064, §4.1), което: (а) вдига 006 D12 за изброения адресен write-set; (б) **разпинова `scoreEntry` и компаратора** за назованите редове; (в) обявява, че G3 престава да е байтова равнопоставеност и се заменя с диференциален address replay; (г) **не** вдига `sw.js` и **не** вдига съдържанието на `address_rows.json`.
235: *Препоръка:* (а) `wtk` = написаните токени **МИНУС** каноничните на същия запис (иначе инвариантът `wtk ∩ qtk = ∅` пада на първия билд — ~4 588 записа имат съгласна дума); (б) речникът за „изричен квартален филтър“ се строи от **`quarter_names` (всичките 60 канонични имена)**, не от наблюдаваните `qtk` — иначе кварталите, които не са раздали нито едно име, нямат гард и „ж.к. Дружба, бл. 11“ остава пълно съвпадение през свидетеля.
243: *Препоръка:* числов или ≤ 2-знаков суфикс НЕ влиза самостоятелно в `qtk` (само биграмата „mladost 1“); токени с дължина ≤ 2 и чисти числа се изхвърлят. Делтата в подредбата (`:5252-5253`) се мери.
252: ## 4 · Write-set по репа
254: ### 4.1 `C:/git/Varna_buildings` (Executor комитва)
277: 2. Pass 2, **`:701`**: `o.qtk` вече не се преписва от геокодера. Ново:
279:  - `o.qtk = sq.tokens` и `o.q = quarterNameIndex(sq.display)` **само** при присъда с канон;
280:  - **`o.wtk = написаните токени МИНУС `o.qtk`** (Р14-а); празен масив не се пише;
283: 4. **`:873-922` Р38** се обвива в `if (!sq.hasCanon)`; добавеният токен отива в `wtk`.
287: 8. `vocab` (`:956-965`) се разширява с `wtk` и `otk`.
295: - `ALLOWED_ENTRY_KEYS` (`:56-59`) += `"q"`, `"wtk"`, `"otk"`, `"o"`; `TOKEN_FIELDS` (`:110`) += `"wtk"`, `"otk"`.
297: - `quarter_names` / `orientations`: масиви от низове, без mojibake/каднум/цифрова серия ≥ 5; `q` и `o` — цели числа в обхват; **всеки `qtk` токен ∈ речника от `quarter_names`**; `wtk ∩ qtk = ∅`.
298: - **НОВ вход: `output/signed_quarters_baked.json`** — гейтът сам преизчислява присъдата за **всеки** запис с `q` и пада при разминаване (това е G-A4; без този вход фикстурата „`qtk:["chaika"]` при пин в Левски“ е зелена, защото „chaika“ Е валидно канонично име).
299: - Отровени фикстури, всяка задължително падаща: (ф1) `coordinates` в НОВ топ-ключ; (ф2) `q` извън обхвата; (ф3) `qtk` с неканоничен токен; (ф4) `wtk ∩ qtk ≠ ∅`; (ф5) `quarter_names` с не-низ; (ф6) **запис с `q` = Чайка при пин вътре в кв. Левски**; (ф7) `o` без съответен ред в `orientations`.
305: ### 4.2 `C:/git/varna_3d`
308: ### 4.3 `C:/git/Fire_Varna` (Executor комитва кода; данните — Петър)
311: 1. `:5134` и `:5140-5145` — `wtk` и `otk` влизат в резервния vocab и в postings.
312: 2. `:5151` `_areaVocab` остава `['dtk','qtk','stk']` — **`wtk` и `otk` НЕ влизат** (иначе „студентска бл 11“ сменя клона на рендера, `:5168-5171` → `:5278-5288`).
313: 3. След `:5152`: `index._signedQuarterVocab` = множеството токени, произведени от **`quarter_names`** (Р14-б), не от наблюдаваните `qtk`.
315: 5. `scoreEntry` **след `:5209`**: клон за `wtk` — при `qFilterTok[qi] === true` **И** `e.q != null` свидетелят се пропуска изцяло (`best` остава 0 → `all=false`); иначе важи с `matchedViaWitness += 1`. Отделен клон за `otk` с `matchedViaOtkOnly`.
317: 7. `:5252-5253` подредбата остава `tk.length + qtk.length` — `wtk`/`otk` не се броят; делтата от смяната на `qtk` се обяснява в replay-а.
329: **НОВ · `scratch/places_search/address_corpus_build.py`** — **детерминистичен селектор** на корпуса (сортиран обход на класовете, фиксирано правило „първите N по нарастващ `_ord`“, без произволност, без seed) → пише кандидата в temp и, само с `--freeze`, проследената референция.
331: **НОВ · `tests/test_address_replay.py`** — обвивката; чете очакванията от нова секция `address_replay` в `expectations.json` („No number below is typed by an agent“ — числата идват от `--freeze`).
336: **ПРОМЯНА · `docs/decisions/007_address_path_v2.md`** — амандамент (write-set + разпиноване на scorer/comparator + новите гейтове; `address_rows.json` и `sw.js` остават недосегаеми) + `docs/activeContext.md`.
342: ## 5 · Ред на изпълнение
344: ### 0. Предусловие (ръката на Петър)
347: ### А. Varna_buildings (Executor, локални комити)
355: 7. **V5** генераторът: `q` + `wtk` + `otk`/`o` + `quarter_names`/`orientations` + schema 3.0 + Р38 подчинение + излизане на квартала от `label` → `feat(fire-varna): canonical quarter q, witness wtk and structural block orientation`
364: ### Б. Fire_Varna (Executor, локални комити — само код)
370: ### В. Доставка на данните
374: ### Г. Една публикация
375: Ред: **Б3 (ръката на Петър) → Varna_buildings → varna_3d (нула) → Fire_Varna код → адресните данни (ръката на Петър)**. Подпис и замразяване САМО когато и двете доставки са в HEAD. Една опашка (`ЗА_ПОДПИС_Б3_07.09.md` — адресните редове се ДОБАВЯТ в нея; преименуването на старата опашка е ход на Б3, не на този лот). Един allow-файл (адресният лот не иска нови allow редове). Едно `--freeze` за местата и едно за адресите, и двете СЛЕД подписа, всяко със свой комит. Един назован червен интервал по G20, различим от Б3-евия.
377: ### Д. Командите на Петър (по една на ред, без `&&`; **без `git push`**)
398: python scratch/places_search/address_corpus_build.py --freeze
400: git commit -m "freeze: address replay reference"
405: **ПУБЛИКУВАНЕ — след Gate 2, с отделна твоя дума.** (v1 слагаше `git push` редом с 13 неподписани решения; `python -m gates.sign` без аргументи пада с usage, `gates/sign.py:419-427`; `--freeze` преди комит прави проверка 6 BLOCKED, `gates/release.py:313`.)
409: ## 6 · Гейтове
415: | G-A1 | Пинът на полигоните (OID + sha, четени в Python) | `python tools/build_signed_quarter_index.py` | 0 | подменен байт в опечения вход; подаден commit-ish вместо OID |
416: | G-A2 | Публикационен гейт (разширен) | `npm run test:fire-varna-publish-gate:staging` | 0 | ф1 `coordinates` в нов топ-ключ; ф2 `q` извън обхват; ф3 неканоничен `qtk`; ф4 `wtk∩qtk≠∅`; ф5 не-низ в `quarter_names`; ф7 `o` без ред |
417: | G-A3 | **Истинност на резолвера** | `node js/test_signed_quarter_resolver.mjs` | 0 | (а) резолвер с „най-близък полигон“; (б) пин в зоната Виница вътре в Манастирски рид, обявен за Виница; (в) недоказан parent, обявен за дете |
418: | **G-A3-г** | **Флагманът, поименно** | част от G-A3 | 0 | **пинът `[43.22212, 27.9378]` ТРЯБВА да върне присъда, която дава „кв. Левски“** (при подписания Р5); пинът `[43.21976, 27.91949]` ТРЯБВА да върне класа по Р5-д |
419: | G-A4 | **Свидетелят не е авторитет — върху ДОСТАВЕНИТЕ байтове** | част от G-A2 (с полигонния вход) | 0 | ф6: запис с `q`/`qtk` = Чайка при пин вътре в кв. Левски |
420: | G-A5 | Пълнота на леджера (вкл. `source`/`mode`/`confidence` на свидетеля) | `node js/test_quarter_ledger.mjs` | 0 | изтрит ред за запис с различен свидетел |
421: | G-A6а | **Ориентир — подписан ПОД, не дизюнкция** | `node js/test_block_orientation.mjs` | 0 | брой блокови редове с `own`/`nearest` под пода от М0.6 (при валидни причини) → червено; причина извън затворения списък → червено |
422: | G-A6б | Различимост при колизия | същият | 0 | две групи в една двойка (квартал, блок №) с еднакъв ориентир и **извън** подписания списък изключения |
423: | G-A6в | Качество на ориентира | същият | 0 | ориентир с отхвърлен низ („ул кк зл пясъци…“); ориентир над подписания праг без бележка за разстояние |
424: | G-A7 | Р38 подчинение | част от G-A3 | 0 | ред в зоната с подписан фин квартал, префиксиран „кв. Виница“ |
425: | G-A8 | Два билда байт-идентични | `npm run test:fire-varna-determinism` | 0 | подменен байт в едното копие |
426: | G-A9 | Дрифт: S9 + C2 | вграден в билда (`:1042-1051`) + брояч | 0 | `tokenInconsistentTotal` > 20 % от 5 828; **`c2ResByReason.token_inconsistent` над подписания таван от М0.7** |
427: | G-A10 | Бюджет на диффа по етикетите | част от билда | 0 | брой сменени `label` извън подписания интервал (квартален сегмент + махнатия уличен суфикс) |
430: | G-B3 | Поколение ↔ размер ↔ броеве ↔ таван | `python -m unittest tests.test_address_generation` | 0 | чужд `bytes` в манифеста; `address_row_count ≠ rows.length`; сбор над подписания таван (Р12-в) |
433: | G-B6 | `FORBIDDEN` остава зелен | `python -m unittest tests.test_b3_gates` | без нови червени спрямо М0.9 | забранен низ, вкаран в адресен етикет |
439: ## 7 · STOP — спри и питай Петър
450: 10. Резолверът иска ново публично поле извън `q`, `wtk`, `otk`, `o`.
459: ## 8 · Локален преглед (проби с очакван резултат)
475: | 11 | **ред по display_id пътя** (напр. `константин и фружин бл 302`) | заглавието носи квартала И ориентира; при материализация (Р12-б) няма „ж.к. Бриз, акчелар“ |
483: ## 9 · Рискове и дългове
502: ## 10 · Какво НЕ се пипа
508: - Стейджнатият Б3 write-set (14 пътя, вкл. `gates/probe/b3_g11.py` и `tests/test_b3_gates.py`) — освен ако Петър не подпише Р18 вариант „разширяване на `ALLOWED_NEW`“.
517: ## 11 · Отхвърлени находки (с измерената причина)
521: 3. **semantics, „бонус“ към Битоля: „§1.А твърди, че Битоля носи `qtk = tsveten kvartal`“ — ОТХВЪРЛЕНО.** v1 §1.А цитира СКАУТ 3 §9, който дава ЕДИН пример („ул. Битоля 11, `qtk=tsveten kvartal`“), а не разпределение; същият СКАУТ в §3 брои `tsveten kvartal → кв. Левски` 318. Планът никога не е твърдял „всички Битоля са tsveten kvartal“. **Приета е обаче основната част:** районът в Р13.3/§8-5 е **Приморски**, не Одесос — `district_names` е проверен от Planner-а сега.
528: ## 12 · Оборване (какво казаха трите опровержения и какво е приложено)
531: Приложени блокери: флагманът пада под собствената политика → **нов Р5 с вариантите (в)/(г) + G-A3-г с поименна фикстура**; М0.5 е измеримо днес и оборва Р5в → **фалшивият праг 15 % махнат, вариантите носят измерените си цени**; `wtk ∩ qtk = ∅` срещу „свидетелят винаги“ → **Р14-а (изваждане)**; G-A6а без зъби → **подписан ПОД + затворен списък причини**; G-A6б червен върху данните → **Р9-б (втора степен + подписан списък изключения)**; ориентирът не стига до 205-те реда → **Р15 (структурно поле `o`)**; G-B5 извън среза → **`validateSearchPayload` вътре в среза + собствен гейт-ред**; корпусът без селектор и без freeze → **`address_corpus_build.py --freeze` + команда в §5.Д**.
532: Приложени мажори: противоречието §2 ↔ §4.1 за `inside_clear` → **една дефиниция в §2 + Р5**; класът „извън, но в лентата на един“ → **Р5-д + Р14-б**; фикстурите на G-B2/G-A2 ф1 → **блоб-четене, липсващ файл = червено, затворено топ-ниво, фикстура на топ ниво**; `stk` пренарежда груповия режим → **`otk`, извън `_areaVocab`**; гардът от наблюдавани `qtk` → **речник от `quarter_names`**; §0.10 ↔ §5.Г → **изравнени (Б3 се комитва пръв)**; G-B1 → **Р18 (собствен пробен файл) + истински родител**. Минорите за качеството на ориентира (Р11-б), фантомния М0.1, `git push` и регистрите по display_id пътя — също приложени.
539: Приложени блокери: **лотът е забранен от ПРИЕТ ADR 006 D12 и разрешен само от НЕПОДПИСАН ADR 007, а v1 не искаше този подпис → нов Р0 + Р0-б (kill switch)** — това е най-тежката управленска пробойна на v1; PowerShell разваля байтовете (`>` → UTF-16LE) → **пин по OID, четене в Python**; `python -m gates.sign` без аргументи пада, а редът подпис→freeze→run_gates дава червена проверка 6 → **пренаписан §5.Д**; ориентирът убива C2 етикета (`TYPEWORDS:457-458` няма „do“; `resolveC2BlockLabel:617` е fail-closed; `entryTokenSet:481-487` чете `e`, не `o`) → **Р15: ориентирът напуска `label` изцяло**.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'scratch/places_search/adresi_astra_S31_08.09.md'; "'$n=0; Get-Content -LiteralPath $p -Encoding UTF8 | ForEach-Object { $n++; if ($_ -match '"'"'^#{1,4} |S31-[0-9]|НЕГОДНО|ГОДНО'"') { '{0}: {1}' -f "'$n,$_ } } | Select-Object -First 100; $p='"'scratch/places_search/adresi_po_poligon_measure_08.09.md'; "'$n=0; Get-Content -LiteralPath $p -Encoding UTF8 -TotalCount 150 | ForEach-Object { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\Fire_Varna
 succeeded in 657ms:
176: # Active context â€” Fire_Varna
185: ## What this repo is
189: ## Where the work stands (05.09)
206: ## Current state
237: ### The red tests: 21 before A.2-4, 6 after (Ð°Ð¼Ð°Ð½Ð´Ð°Ð¼ÐµÐ½Ñ‚ â„–4 Ñ‚. 1 Ð¸ Ñ‚. 7)
289: ## Waiting for a signature
299: ## Forbidden here
303: ## Where things are
320: ## main...origin/main [ahead 100]
372: # Active context — Fire_Varna
381: ## What this repo is
385: ## Where the work stands (05.09)
402: ## Current state
433: ### The red tests: 21 before A.2-4, 6 after (амандамент №4 т. 1 и т. 7)
843: 3: **Дата:** 07.09.2026 · **Планер:** Claude Planner (read-only) · **Статус:** **ПОДПИСАН от Петър (07.09.2026): „подписвам плана Б3 v3 по препоръките“** — подписаното тяло е блобът в комит acddcd1, sha256 `51fde25f1be25a639c6f4f0a5a2b5c6dafe09f697498e8248b80c6cbdd7c343b`; §9 се чете по препоръките (виж §14) · **Заменя:** v2 (`e6ba50e`, чернова, неподписана), след две външни оборвания — **Astra S28** (механика, 10 условия) и **Кими К28** (данни/семантика, 7 условия), и двете **НЕГОДНО** (§12).
1151: 32: Стъпки 0–7 са изпълнени (изпълнители A, B, C; Opus) и одитирани (**ГОДНО**, 8 минора, нула блокери/майори): 13 пътя стейджнати, нищо комитнато; червеният набор D19/G20 е точно обявеният — 25 теста (21 замразена референция → стъпка 13; 3 `MapAttributionTest` → 12б; 1 `PlacesCacheNameTest` → А2-1), `run_gates` две червени (покритие exit 2 → стъпка 11; release BLOCKED 2 → стъпки 11/13/14 + А2-3), G11 `--cached` само `stray_new tests/test_b3_gates.py` → А2-2. Кими К30 / Astra S30 върху стейджнатия диф — виж записите.
1154: 35: - **Astra S30 (механика): НЕГОДНО с три блокера в ГЕЙТ-СКРИПТОВЕТЕ** (не в доставката): G11 четеше работното дърво вместо индекса при `--cached` и приемаше грешка на git за зелено; G1 не сверяваше трите клиентски пина в `index.html`. **Затворени** (изпълнител + одитор ГОДНО): `gates/probe/b3_g11.py` чете съдържание и инвентар от ЕДИН моментен срез (`git show :<path>` / `HEAD:<path>`, `:(top)` pathspec, chdir към върха, `check=True`, нечетимо → exit 1, счупен git или празен инвентар → exit 2); нов клас `ClientPinsTest` в `tests/test_places_public_bundle.py` сверява `PLACES2_SHA256`/`HOTELS_SHA256`/`CATS_SHA256`/`LEGACY_BUNDLE_SHA` от `index.html` с LF-телата (G1: 68 теста; една сменена цифра → червено). Това е коректно изпълнение на подписаните G1/G11, не нов обхват.
1166: 4: **Основание:** повторната проверка **Astra S29** върху v3 върна **НЕГОДНО** с осем МЕХАНИЧНИ условия (Кими К29: ГОДНО, без условия). §14 на плана предвижда точно това: „условие от тях влиза като амандамент (нов датиран файл) и се подписва отделно, само за делтата“.
1: # МЯРКА · адресите на Fire_Varna срещу подписаните квартални полигони (08.09.2026, read-only)
2: 
3: Изтор: `data/search_index.json` (86 232 записа с координата: 70 575 адреса, 14 687 сгради, 970 парцела) срещу `varna_3d data/quarters_signed.geojson` (60 подписани полигона, 05f485e), „най-малкият съдържащ полигон“. Кварталната дума на адреса (`qtk`) идва от кадастралния адрес; полигонът — от подписа на Петър. Съгласие = дума на адреса ∈ токените на името/кода на полигона.
4: 
5: ## 1 · Обща таблица
6: 
7: | клас | вътре в полигон, съгласни | вътре, несъгласни | вътре, без квартална дума | извън всички полигони |
8: |---|---|---|---|---|
9: | address | 2419 | 4977 | 53191 | 9988 |
10: | mf | 4206 | 3392 | 4024 | 3065 |
11: | parcel | 30 | 15 | 713 | 212 |
12: | **всички** | **6655** | **8384** | **57928** | **13265** |
13: 
14: ## 2 · Несъгласия (кадастрална дума → подписан полигон под точката), топ 25
15: 
16: | брой | дума на адреса | полигон |
17: |---|---|---|
18: | 1951 | vinitsa | с.о. Манастирски рид |
19: | 1380 | vinitsa | м-т Акчелар |
20: | 563 | kolhozen pazar | кв. Тракия |
21: | 487 | vinitsa | м-т Ален Мак |
22: | 452 | tsveten kvartal | кв. Левски |
23: | 437 | mikroraion | Гръцката махала |
24: | 326 | vinitsa | ж.к. Бриз |
25: | 277 | gratskata mahala | Център |
26: | 269 | mikroraion | Център |
27: | 234 | chaika | кв. Левски |
28: | 214 | rozova dolina | кв. Аспарухово |
29: | 208 | vinitsa | м-т Свети Никола |
30: | 188 | vinitsa | с.о. Перчемлията |
31: | 186 | vinitsa | Евксиноград |
32: | 161 | vinitsa | м-т Сотира |
33: | 111 | druzhba | кв. Аспарухово |
34: | 100 | vinitsa | к.к. Св. Св. Константин и Елена |
35: | 78 | hristo botev | кв. Св. Иван Рилски |
36: | 54 | sveti nikola | ж.к. Бриз |
37: | 51 | ti mikroraion | Център |
38: | 50 | vinitsa | с.о. Горна Трака |
39: | 36 | hristo botev | Колхозен пазар |
40: | 31 | vazrazhdane | с.о. Пчелина |
41: | 30 | tsentar | Колхозен пазар |
42: | 29 | ribarsko selishte karantinata | кв. Аспарухово |
43: 
44: ## 3 · Извън всички полигони, по кадастрална дума (центроид на групата)
45: 
46: | брой | дума | центроид |
47: |---|---|---|
48: | 8810 | (без дума) | 43.2021,27.9040 |
49: | 1461 | vinitsa | 43.2542,28.0062 |
50: | 753 | tsentar | 43.2066,27.9105 |
51: | 490 | kolhozen pazar | 43.2138,27.9059 |
52: | 478 | levski | 43.2165,27.9208 |
53: | 410 | gratskata mahala | 43.2109,27.9229 |
54: | 219 | chaika | 43.2127,27.9281 |
55: | 197 | tsveten kvartal | 43.2174,27.9133 |
56: | 143 | ti mikroraion | 43.2090,27.9114 |
57: | 89 | hristo botev | 43.2077,27.8979 |
58: | 54 | pobeda | 43.2197,27.9024 |
59: | 52 | evksinograd | 43.2373,27.9925 |
60: | 35 | sotira | 43.2274,27.9325 |
61: | 23 | alen mak priblizitelno | 43.2717,28.0301 |
62: | 22 | troshevo | 43.2193,27.8778 |
63: | 6 | mladost | 43.2306,27.8656 |
64: | 5 | galata | 43.1627,27.9363 |
65: | 3 | kochmar | 43.2416,27.8801 |
66: | 3 | dalbokoto dere | 43.2387,27.9854 |
67: | 3 | zelenika | 43.1606,27.9255 |
68: 
69: ## 4 · Колко записа би получил всеки подписан квартал по полигон (топ 25)
70: 
71: | записи | полигон |
72: |---|---|
73: | 4545 | кв. Аспарухово |
74: | 3571 | кв. Христо Ботев |
75: | 3351 | кв. Виница |
76: | 3302 | кв. Св. Иван Рилски |
77: | 3282 | кв. Левски |
78: | 2890 | кв. Изгрев |
79: | 2821 | Евксиноград |
80: | 2680 | с.о. Боровец-юг |
81: | 2321 | кв. Трошево |
82: | 2305 | м-т Ален Мак |
83: | 2282 | кв. Владиславово |
84: | 1994 | с.о. Манастирски рид |
85: | 1961 | с.о. Боровец-север |
86: | 1776 | кв. Галата |
87: | 1668 | Център |
88: | 1642 | Западна промишлена зона |
89: | 1626 | м-т Свети Никола |
90: | 1537 | ж.к. Бриз |
91: | 1516 | к.к. Чайка |
92: | 1441 | м-т Акчелар |
93: | 1342 | Колхозен пазар |
94: | 1302 | кв. Тракия |
95: | 1263 | Максуда |
96: | 1208 | м-т Сотира |
97: | 1195 | Гръцката махала |
98: 
99: ## 5 · Прочит
100: - Несъгласията са предимно СИСТЕМНИ: кадастралната „зона Виница“ е землищна дума върху много подписани квартали; „Колхозен пазар“ покрива Тракия; „микрорайон N“ е адресна форма без квартал; „Цветен квартал“ и „Център“ нямат подписан полигон.
101: - Поправката „координатата решава, кадастралната дума е свидетел“ е приложима на генератора на индекса (`js/build_fire_varna_search_index.mjs`), не в клиента: полигоните остават частни, публично пътува само думата. Дупките (Център, Цветен квартал, Колхозен пазар, Кайсиева/Възраждане 3 ръбове) искат решения преди това.
102: - Нищо от това не е в обхвата на Б3 (§10) — отделен лот.
103: 
104: ## 6 · Повтарящи се номера на блокове (мярка 08.09 ~01:00, по искане на Петър)
105: - Записи с блоков номер („бл. N“) в индекса: **5 274**, което е около **1 407 физически блока** (входовете, събрани на 60 m).
106: - **(А)** Един и същ номер за повече от един физически блок в СЪЩАТА кадастрална квартална дума: **263 двойки (дума, номер), 939 блока**. Най-тежко: без квартална дума бл. 2 → 22 блока, бл. 1 → 18; кв. Левски бл. 2 → 17, бл. 1 → 12, бл. 3 → 11, бл. 4 → 11 (Левски номерира блоковете по улица, затова номерата се повтарят).
107: - **(Б)** Номер, който съществува в повече от един квартал: **108 от 332** номера (бл. 2 в 28 квартала, бл. 1 в 25, бл. 3 в 22…).
108: - **(В)** По подписан полигон: **250 двойки, 824 блока** с повторен номер в същия полигон; извън полигоните: бл. 1 → 27, бл. 2 → 23.
109: - **Ориентирът:** от 4 403 етикета в блоков стил („кв. X, бл. N…“) само **244** носят улица след номера; **4 159 са без улица** — и за **всичките 4 159** има улична адресна точка до 80 m (4 143 до 50 m). Тоест „кв. Левски, бл. 11, до ул. Студентска“ е изводимо за 100 % от блоковете без нови източници.
110: - **Заявка на Петър (08.09):** „искам да сложим и близка улица, за да се различават блоковете… искам да го изчистим този проблем веднъж завинаги“ — влиза като изискване 2 на лота „Адресите по полигон“ (планът се пише); по тази тема сега не се действа.
111: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 1..150 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 151..300 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'scratch/places_search/adresi_astra_S31_08.09.md' -Encoding UTF8 -Tail 100" in C:\git\Fire_Varna
 succeeded in 630ms:

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

 succeeded in 686ms:
151: 
152: **НЕ-целта (изрично забранено):** най-близък полигон / буфер / разширяване на полигон; промяна на координата, номер, вход или идентичност; геометрия или разстояние до ръб в публичен файл; движение в регистъра; палене на approx (`index.html:5926`); преименуване на `.asr-item`; промяна на низа `'Няма съвпадения'` (`:5430`); промяна на СЪДЪРЖАНИЕТО на `data/address_rows.json` (ADR 007 D2); промяна на `sw.js`.
153: 
154: ---
155: 
156: ## 3 · Решения за Петър преди билда
157: 
158: > Всяко решение = един ред за подпис. Без подпис по Р0–Р18 билдът не тръгва.
159: 
160: **Р0 · Управленското разрешение (НОВО, блокиращо).** ADR 006 D12 (**Accepted**) изброява поименно `data/search_index.json`, `data/address_rows.json`, `sw.js` и **„every function of `initAddressSearch`“** като недосегаеми, а гейтът му е „адресният корпус е байт-идентичен“ (`006:157-163`). ADR 007, който вдига това, е **Proposed — awaiting Petar** (`007:3`) и при това пинова изрично **„the scorer and comparator“** (`007:15`) — точно каквото този лот пипа.
161: *Препоръка:* **подпиши ADR 007 И подпиши разширението му** (нов ADR 064, §4.1), което: (а) вдига 006 D12 за изброения адресен write-set; (б) **разпинова `scoreEntry` и компаратора** за назованите редове; (в) обявява, че G3 престава да е байтова равнопоставеност и се заменя с диференциален address replay; (г) **не** вдига `sw.js` и **не** вдига съдържанието на `address_rows.json`.
162: 
163: **Р0-б · Kill switch `ADDRESS_PATH_V2`.** ADR 007 D4 иска селектор на всеки use site, никога ранен `return`.
164: *Препоръка:* **да** — селектор около четирите нови места в клиента (`quarterPrefix`, `orientationSuffix`, гарда на свидетеля, `otk` клона). Цена: ~20 реда и двойна фикстура в replay-а (флаг вкл./изкл.).
165: 
166: **Р1 · Дупката „Център“** (753 mf извън всички + част от 8 810-те без дума).
167: *Препоръка:* неопределено; „район Одесос/Приморски“ по измерения `d`; свидетелят остава търсим; ред в борда „Център иска подписан полигон“. **Не разширяваме полигон.**
168: 
169: **Р2 · „Цветен квартал“** (няма полигон, няма запис в регистъра; 197 извън + 318 несъгласия към кв. Левски + 9 към Изгрев).
170: *Препоръка:* координатата решава — 318-те стават „кв. Левски“ (при Р5 (в)/(г); при (а)/(б) част от тях падат в лентата и остават неопределени — числото идва от М0.5); „цветен квартал“ остава свидетел; 197-те извън — по Р5-д.
171: 
172: **Р3 · „Колхозен пазар“** (490 извън + 245 несъгласия към кв. Тракия).
173: *Препоръка:* същото правило като Р2.
174: 
175: **Р4 · Флагманът Левски–Чайка при Студентска.** Измерено: пинът е ВЪТРЕ в кв. Левски на 67,4 m при `precision_m = 100`, конкурентът Бриз е на 82,8 m.
176: *Препоръка:* **„кв. Левски“ канон, „Чайка“ свидетел** — изпълнимо САМО при Р5 (в) или (г). При (а) и (б) този запис остава без квартал и **лотът не решава жалбата ти** — това е записано тук, на първа страница, не на осма.
177: 
178: **Р5 · Лентата — четири варианта с измерените цени** (числата се финализират от М0.5; днешните оценки в скоби):
179: 
180: | вариант | правило | губят име | флагманът |
181: |---|---|---:|---|
182: | (а) строга | всичко в собствената лента → неопределено | ~25 613 | ✗ |
183: | (б) конкурентна (v1 Р5в) | неопределено само при конкурент в лентата | ~11 6xx | ✗ |
184: | **(в) съдържанието решава (препоръка)** | пинът е в точно един полигон → името се дава; лентата се записва само в леджера | 0 | ✓ |
185: | (г) по-близкият конкурент | неопределено само ако чужд ръб е ПО-БЛИЗО от собствения | подмножество на (б) | ✓ (Бриз 82,8 > 67,4) |
186: 
187: *Довод за (в):* неопределеността не може да стане чуждо име; чужд полигон, който НЕ съдържа точката, не може да я спечели. *Честната цена:* при (в) грешка е възможна за записите на ≤ band от ръба (~25 613) — тя се лови от леджера и от извадката на Петър, не от гейт. Ако искаш нула такъв риск → (а), но тогава подпиши изрично, че флагманът остава без квартал.
188: **Прагът „15 %“ от v1 отпада** — той не е решение, а тавтология (§12).
189: 
190: **Р5-д · Класът „извън всички, но в лентата на ТОЧНО ЕДИН полигон“ (~4 042; пример: „кв. Левски, бл. 11, бул. Царевец“ на 51,2 m извън).**
191: *Препоръка:* **остава неопределен (без канон), НО свидетелят му НЕ се гаси** (виж Р14-б) — така „бл 11 левски“ продължава да го връща, само че под редовете с канон, с назована причина в леджера. Алтернативи за подпис: (i) получава името; (ii) пълно мълчание (не се препоръчва — истински Левски бл. 11 изчезва от собствената заявка на Петър).
192: 
193: **Р6 · Р38 (зоната „Виница“) срещу подписаните полигони.** Зоната хваща 9 771 реда (8 996 „без свидетелство“), а Манастирски рид (1 264), Акчелар (651), Ален Мак (205), Св. Никола (64), Бриз, Перчемлията, Евксиноград, Сотира имат СВОИ полигони.
194: *Препоръка:* подписаният полигон има предимство; Р38 работи само там, където резолверът връща неопределено; правилото „добавя, никога не реже“ се запазва, но добавеният токен отива в свидетелското поле. Отменя част от подписан на 12.08 прецедент → иска изричен нов подпис.
195: 
196: **Р6-б · Отношението към ADR 010 (D6/D7/D8).** ADR 010 D6 (`010:48`) урежда канала `SIGNED_POLYGON` в `varna_3d/src/fire_varna_locations.py` за **375-те МЕСТА** („пише само в ред без свидетел, извън ръба, в точно един полигон“); този лот е ДРУГА повърхност (адресният индекс, генериран в `Varna_buildings`) — затова тук няма автоматична отмяна (§11.2). Но политиките се разминават в три точки и това трябва да е ПОДПИСАНО, не мълчаливо: (1) тук полигонът пише и в ред с написан свидетел (~4 399 замени); (2) при Р5(в) пише и в лентата (~25 613); (3) D8 иска геометрично доказано `дете ⊆ родител` — приемаме го дословно (недоказаният parent → неопределено + червен ред в леджера).
197: *Препоръка:* ADR 064 изброява трите разминавания и казва „ADR 010 остава непроменен за местата“.
198: 
199: **Р7 · Несравними припокривания (4 174; топ: Аспарухово+Розова долина 746, Гръцката махала+Център 621, Възраждане+Възраждане 1 545 …).**
200: *Препоръка:* неопределено + леджер. Липсващите йерархии (1 179 + 746 + 525 + 296 + 239 записа) са ход в регистъра → **сутрешен списък**. Признатата цена: ~2 985 записа остават неопределени само заради липсващ `parent`.
201: 
202: **Р8 · Approx пакетът** (8 361, `index.html:5926 = false`). *Препоръка:* остава изключен; при палене минава през същия резолвер.
203: 
204: **Р9 · Ориентир: винаги или само при колизия?** Днес улица се лепи само при сблъсък в СЪЩИЯ написан квартал (`lib_fire_varna_block_labels.mjs:191-199`); само 26 етикета носят улица.
205: *Препоръка:* **винаги за блокови редове** („много блокове 11 в кв левски не е добре“). Колизионният детектор остава само за да маркира `must_disambiguate` и да храни G-A6б.
206: 
207: **Р9-б · Какво става, когато ориентирите СЪВПАДАТ** (измерено: 24 (gates) / 16 (semantics) неразличими групи; примери: ж.к. Бриз бл. В — 13 групи, „ул. Д-р Петър Скорчев“ 4 пъти; кв. Трошево бл. 5 — две групи „ул. Радост“; кв. Чайка бл. 37 — две групи БЕЗ улица).
208: *Препоръка:* втора степен на ориентира — **втората по близост различаваща улица**; ако и тя не различава — **разстоянието в метри** („до ул. Радост, 40 m“ / „…, 90 m“); остатъкът след двете степени е **подписан списък изключения** от М0.6, срещу който G-A6б сверява (гейт срещу измерен остатък, не срещу нула).
209: 
210: **Р9-в · Един източник на уличния текст.** С Р9 ориентирът става структурен → Pass C (`:191-199`) **спира** да лепи улица в `label` (иначе „бл. 11, ул. Мир, до ул. Мир“). Цена: ~26 етикета губят суфикса си, който се връща като структурен ориентир; диффът се мери (G-A10). *Алтернатива:* Pass C остава и структурният ориентир се пропуска там — по-малък диф, две правила.
211: 
212: **Р10 · Какво е „собствена улица“ и как се изписва.** Днешният `extractStreet` иска типов опенер (`:39`) → за „Студентска бл. 11“ връща **null** (17,5 % от блоковите `address_line` дават улица), но `tk` на записа НОСИ `studentska`.
213: *Препоръка (Р10-а):* собствена улица = `extractStreet(addrLine)` **ИЛИ** улично име от речника (1 625 имена), чиито токени са в `tk` на записа. Изписване: собствена → „, ул. Х“; чужда (най-близка) → „, **до** ул. Х“.
214: *Следствие за подписа:* при Р10-а флагманът се изписва **„кв. Левски, бл. 11, ул. Студентска“** (собствена улица), не „до ул. Студентска“. Ако предпочиташ „до“ — тогава Р10-б: собствена улица САМО по `extractStreet`, и флагманът минава по клона „най-близка“ (52 m). **Един низ, не два** — Р13 се подравнява по избора тук.
215: 
216: **Р11 · Радиус за „най-близка улица“.** Измерено: медиана 36,7 m, p90 93,9 m; 4 243 от 5 567 имат улица ≤ 120 m.
217: *Препоръка:* **120 m**, детерминистично разкъсване на равенства (по-малко разстояние → по-малък `skel` низ → по-малък `_ord`).
218: 
219: **Р11-б · Качество на ориентира.** 339 от 4 243 са на ≥ 100 m; парсването ражда низове като „ул кк зл пясъци х л вихрен“, „ул жк изгрев“, „ул д р индржишка кръстева“.
220: *Препоръка:* (1) ≤ 60 m → „до ул. Х“; 60–120 m → „до ул. Х, ~N m“; > 120 m → без ориентир, причина `no_street_within_radius`; (2) **филтър за нелегитимни низове** (токени `жк/кк/зпз/х л`, числови опашки, повече от 4 инициала) → причина `street_string_rejected`; (3) затворен списък допустими причини: `own_street`, `nearest_street`, `no_street_within_radius`, `street_string_rejected`, `no_block_number`.
221: 
222: **Р12 · Къде живее кварталната дума в дисплея.**
223: - (а) вътре в `label` — тогава display_id пътят (43 099 реда) остава без квартал завинаги;
224: - **(б) препоръка — структурно поле `q` + топ-ключ `quarter_names[]`** по образеца на `d`/`district_names`; кварталният сегмент напуска `label`; клиентът композира заглавието.
225: - **Р12-б (НОВО, задължително допълнение):** при (б) заглавието по display_id пътя е `префикс + ', ' + normalized_address`, а самият текст носи квартална дума → **2 775 записа биха се изписали „ж.к. Бриз, акчелар“**. Варианти: (i) **материализира се `label` само за тези 2 775** (байтовете се мерят в М0.10) — препоръка; (ii) амандамент на ADR 007 D2 и нормализация в `build_fire_varna_address_rows.mjs:98` — по-скъпо управленски; (iii) приема се и се обявява. Отделно 11 627 реда с НЕОПРЕДЕЛЕН канон запазват квартална дума в текста си → §2 цел 4 важи с това ограничение, освен ако не изберем (i) и за тях (цената пак е в М0.10).
226: - **Р12-в · Подписан таван за размера.** Оценките: +1,26 MB (semantics) / +1,54 MB (delivery) само за квартала, преди ориентира и материализацията. *Препоръка:* подписваш число `N` байта за СБОРА на двата lazy payload-а (днес 15,57 MiB); гейт G-B3 го чете от `expectations.json`; надвишаване = СПИРАЙ.
227: 
228: **Р13 · Точните низове (за дословен подпис, след избора по Р10 и М0.12):**
229: 1. заглавие с квартал и собствена улица: `кв. Левски, бл. 11, ул. Студентска` *(при Р10-а)* **или** `кв. Левски, бл. 11, до ул. Студентска` *(при Р10-б)*;
230: 2. заглавие без квартал: `бл. 11, до ул. Студентска` + втори ред `район Приморски`;
231: 3. адресен ред извън всички полигони: `ул. Битоля 13` + `район Приморски` (**не Одесос** — v1 сгреши; `d=4` = Приморски, `district_names` проверен);
232: 4. префиксът се взима **дословно** от `name` на полигона, с типовата представка, без превод.
233: 
234: **Р14 · Гардът на свидетеля.**
235: *Препоръка:* (а) `wtk` = написаните токени **МИНУС** каноничните на същия запис (иначе инвариантът `wtk ∩ qtk = ∅` пада на първия билд — ~4 588 записа имат съгласна дума); (б) речникът за „изричен квартален филтър“ се строи от **`quarter_names` (всичките 60 канонични имена)**, не от наблюдаваните `qtk` — иначе кварталите, които не са раздали нито едно име, нямат гард и „ж.к. Дружба, бл. 11“ остава пълно съвпадение през свидетеля.
236: **Р14-б · Обхват на гарда:** гардът гаси свидетеля САМО за записи с **`q != null`** (има канон, който му противоречи). Записите с неопределен канон (в т.ч. Р5-д) запазват силата на свидетеля, но с демотиране `wdem`. Така „чайка студентска бл 11“ не е пълно съвпадение, а „бл 11 левски“ все пак връща блока на бул. Царевец.
237: 
238: **Р15 · Ориентирът е СТРУКТУРЕН, не в `label` и не в `stk`.**
239: *Довод 1:* `resolveC2BlockLabel` (`:609-619`) е fail-closed по `s9Inconsistency`, а „до“ **не е в `TYPEWORDS` (`:457-458`)** → етикет „бл. 11, до ул. Мир“ с чужда улица дава `streetMissing === streetTotal` → `token_inconsistent` → етикетът се ИЗХВЪРЛЯ. *Довод 2:* `entryTokenSet` (`:481-487`) чете геокодерния `e`, а `o.stk` се пише на `:723` върху публичния обект — спасяването „през stk“ на v1 не работи без мутиране на `e`. *Довод 3:* `_areaVocab` (`:5151`) се храни от `stk` → ~306 нови улични имена биха превключили цяло семейство заявки в груповия блоков клон (`:5278-5288`).
240: *Препоръка:* ново поле `o` (индекс в топ-ключ `orientations[]`) + нови токени в **`otk`** (в postings и vocab, **НЕ в `_areaVocab`**), с демотер `otdem = 1`, ако поне един токен на заявката е съвпаднал **само** през `otk` (per-token, не `matchedCore === 0` — иначе демотерът е мъртъв, както е `sdem` при блокови заявки). Така: (1) `label` не се пипа → C2/S9 остават непокътнати; (2) ориентирът стига и до двата дисплей пътя (включително 205-те блокови реда без `label`); (3) „студентска бл 11“ не сменя клона на рендера.
241: 
242: **Р16 · Каноничните токени.** Правилото „skel(name без представка), разделено на думи“ дава голи цифри `1`,`2`,`3`,`4` (Младост 1/2, Възраждане 1–4 — проверено в имената) и къси `sv`, `rid`, `mak`.
243: *Препоръка:* числов или ≤ 2-знаков суфикс НЕ влиза самостоятелно в `qtk` (само биграмата „mladost 1“); токени с дължина ≤ 2 и чисти числа се изхвърлят. Делтата в подредбата (`:5252-5253`) се мери.
244: 269: - `tokens` по Р16.
270: 
271: **НОВ · `js/lib_block_orientation.mjs`** — ориентирът (B): собствена улица по Р10, най-близка ≤ R по Р11 с филтъра на Р11-б, втора степен и разстояние по Р9-б, затворен списък причини.
272: 
273: **НОВ · `js/test_signed_quarter_resolver.mjs`** (G-A3) · **НОВ · `js/test_block_orientation.mjs`** (G-A6) · **НОВ · `js/test_quarter_ledger.mjs`** (G-A5) · **НОВ · `js/test_fire_varna_determinism.mjs`** (G-A8).
274: 
275: **ПРОМЯНА · `js/build_fire_varna_search_index.mjs`**
276: 1. `main()`: зарежда `SIGNED_QUARTERS` + `ORIENTATION_MODEL` до `loadVinitsaZone`.
277: 2. Pass 2, **`:701`**: `o.qtk` вече не се преписва от геокодера. Ново:
278:  - `const sq = resolveQuarter(SIGNED_QUARTERS, o.pin);`
279:  - `o.qtk = sq.tokens` и `o.q = quarterNameIndex(sq.display)` **само** при присъда с канон;
280:  - **`o.wtk = написаните токени МИНУС `o.qtk`** (Р14-а); празен масив не се пише;
281:  - `o.otk` = токените на ориентира (собствена улица НЕ дублира `tk`; чуждата влиза само тук), `o.o` = индекс в `orientations[]`.
282: 3. **`:743` C2 и `:826-842` F3 не се пипат**; `label` вече не носи квартален сегмент (т. 5) и не носи улица (Р9-в) → рискът `token_inconsistent` не расте; броячът `c2ResByReason` се сравнява преди/след (G-A9).
283: 4. **`:873-922` Р38** се обвива в `if (!sq.hasCanon)`; добавеният токен отива в `wtk`.
284: 5. `stripQuarterSegment(label)` — само първият сегмент, само при `looksLikeQuarterSegment` (образец `lib_quarter_registry.mjs:220-229`); прилага се СЛЕД регистъра (`:857-871`), преди push.
285: 6. **Материализация на `label`** за подписаното подмножество по Р12-б (2 775 + евентуално 11 627) — само там, само с изчистения текст, с ледгер ред за всеки.
286: 7. Нови топ-ключове `quarter_names` (≤ 60) и `orientations` (сортиран, дедупликиран); `index_schema_version` `"2.0"` → **`"3.0"`**.
287: 8. `vocab` (`:956-965`) се разширява с `wtk` и `otk`.
288: 9. Нов частен изход `output/quarter_polygon_ledger.json`: старо име + **`source` (kais/osm) + `mode` + `confidence` + `distance_m` на написания свидетел**, ново име, присъда, `d_edge_own`, `nearest_other`, ориентир + причина, `complex_id`.
289: 10. Отчетът (`:1071-1159`) получава броячи по присъда, по клас на несъгласие, по причина за ориентира, `blockGroups/collisionPairs/disambiguated` и `c2ResByReason` **преди и след**.
290: 11. Забрана: `d_edge_own`, `nearest_other`, `competitors` не влизат в `o` при никакви обстоятелства.
291: 
292: **ПРОМЯНА · `js/lib_fire_varna_block_labels.mjs`** — Pass A `:168` остава свидетел; Pass B `:183` базата става `бл. ${rec.n}`; **Pass C `:191-199` спира да лепи улица** (Р9-в), само маркира `must_disambiguate`; нови stats `orientationOwn/Nearest/None/Rejected/collisionUnresolved`.
293: 
294: **ПРОМЯНА · `js/test_fire_varna_publish_gate.mjs`**
295: - `ALLOWED_ENTRY_KEYS` (`:56-59`) += `"q"`, `"wtk"`, `"otk"`, `"o"`; `TOKEN_FIELDS` (`:110`) += `"wtk"`, `"otk"`.
296: - **Затворен набор ТОП-ключове** (днес топ-нивото е отворено, `:128-147`) + забранени имена `dist_edge_m`, `edge_m`, `poly`, `ring`, `geometry`, `coordinates`, `geometries` навсякъде в документа.
297: - `quarter_names` / `orientations`: масиви от низове, без mojibake/каднум/цифрова серия ≥ 5; `q` и `o` — цели числа в обхват; **всеки `qtk` токен ∈ речника от `quarter_names`**; `wtk ∩ qtk = ∅`.
298: - **НОВ вход: `output/signed_quarters_baked.json`** — гейтът сам преизчислява присъдата за **всеки** запис с `q` и пада при разминаване (това е G-A4; без този вход фикстурата „`qtk:["chaika"]` при пин в Левски“ е зелена, защото „chaika“ Е валидно канонично име).
299: - Отровени фикстури, всяка задължително падаща: (ф1) `coordinates` в НОВ топ-ключ; (ф2) `q` извън обхвата; (ф3) `qtk` с неканоничен токен; (ф4) `wtk ∩ qtk ≠ ∅`; (ф5) `quarter_names` с не-низ; (ф6) **запис с `q` = Чайка при пин вътре в кв. Левски**; (ф7) `o` без съответен ред в `orientations`.
300: 

 succeeded in 701ms:
1: # ПЛАН · Адресите по полигон (v2)
2: 
3: **Файл:** `C:/git/Fire_Varna/scratch/places_search/ПЛАН_Адресите_по_полигон_v2_08.09.md`
4: **Дата:** 08.09.2026 · **Автор:** Planner (read-only, Opus) · **Статус:** ЧЕРНОВА — чака Gate 1 (подпис на Петър)
5: **Заменя:** v1 от 08.09 (същия ден). **Основание за v2:** три състезателни опровержения (gates / semantics / delivery), всичките с присъда **НЕГОДНО**. Всяка находка е сверена срещу файловете; приетите са вградени тук, отхвърлените са в §11, присъдите — в §12.
6: **Изпълнител:** Opus Executor · **Одитор:** Opus, състезателен · **Публикува:** Петър.
7: 
8: **Клас на риска: 🔴 АРХИТЕКТУРЕН.** Задействани спусъци: (1) нов канон за квартала в доставяни данни; (2) промяна на схемата на публичния payload (`index_schema_version`, `ALLOWED_ENTRY_KEYS`); (3) нов външен източник на имена в публична повърхност (подписаните полигони); (4) междурепова радиация `Varna_buildings → varna_3d → Fire_Varna`; (5) отмяна/уточняване на подписани прецеденти (Р38; отношението към ADR 010); **(6) НОВ — лотът е забранен от ПРИЕТ ADR 006 D12 и е разрешен само от НЕПОДПИСАН ADR 007** (`C:/git/Fire_Varna/docs/decisions/006_places_in_search.md:157-163`, `007_address_path_v2.md:3`), при това пипа изрично пиннатите „scorer and comparator“ (`007:15`); (7) доставка към публикуване, комбинирана с висящата Б3. Топология: **Вариант А**.
9: 
10: **Две доставки в един лот:**
11: - **(A) Каноничен квартал** — думата идва от подписания полигон под точката; написаният свидетел остава търсим, никога авторитетен.
12: - **(B) Ориентир за блоковете** — всеки блоков ред носи ориентир („кв. Левски, бл. 11, до ул. Студентска“), за да са различими едноименните блокове.
13: 
14: ---
15: 
16: ## 0 · Червени редове (важат за всеки ход)
17: 
18: 1. **Агентите не публикуват.** Никакъв `git push`, никакъв remote, никакъв `--no-verify`. Агентът казва „публикуване“ и спира. `git push` **не стои** в нито един команден списък на този план (§5.Д).
19: 2. **Нула геометрия и нула реконструкция на границата в публичен файл.** По ADR 010 D3 (`010:42`) публично излизат само `name`/`code`/`src`. **Не се изнася `dist_to_edge_m`** — нито поле, нито кофа, нито закръглено; забраната става структурна проверка в публикационния гейт (§4.1, G-A2).
20: 3. **`config/quarter_registry.json` не се пипа** (подписът `REGISTRY_SIGNED_SHA256`, `js/lib_quarter_registry.mjs:45-46`). Всяко движение в регистъра (родителите на Възраждане 1–4, Розова долина, Кокарджа, Абатко, Салтанат, висящият `borovets`) отива в **сутрешния списък**.
21: 4. **Данните комитва Петър** (D16/G4). Изпълнителят комитва само код, тестове, гейтове и документи.
22: 5. **Всеки гейт е команда с изход ≠ 0 и назована отрицателна фикстура, която ТРЯБВА да падне** — и фикстурата трябва да пада по НОВОТО твърдение, не по стара проверка (§6; прецедент `checkFixture`, `js/test_fire_varna_publish_gate.mjs`).
23: 6. **Само Opus.** Всеки `Agent`/`agent()` с `model: "opus"`.
24: 7. **Мярка преди промяна, с произход на всяко число.** Числата в §1.А носят етикет за извор (СКАУТ / опровергател / задание). Всяко число, което влиза в подпис, гейт или фикстура, се преизмерва в М0 (§1.Б); **разминаване с базата тук = СПИРАЙ** (§7).
25: 8. **Нула кадастрални идентификатори, нула ГРАО, нула PII** в двата адресни payload-а.
26: 9. **Атрибуцията не се пипа от този лот.** Измерено: низът „Кварталните граници“ днес **не съществува** в `index.html` (СКАУТ 5; потвърдено косвено — той стои само като ЗАБРАНЕН литерал в `tests/test_b3_gates.py:43-44`). Този лот не добавя и не преформулира нито един атрибуционен ред; `FORBIDDEN` остава зелен (G-B6). Ако Б3 достави ред за атрибуция, обхватът му за адресните редове е решение на Петър — **отделен ред в сутрешния списък**, не тук.
27: 10. **Б3 (местата) не се ПРОМЕНЯ от този лот**, но **се КОМИТВА пръв, от ръката на Петър** (§5.0). Двата текста на v1 (§0.10 „не се пипа“ ↔ §5.Г „влиза в HEAD пръв“) са изравнени тук.
28: 11. **Един логически комит = един ход**, точното съобщение от §5, стейджване с явни пътища, никога `git add -A`. **`index.html` е в ДВАТА write-set-а** — преди F1 `git diff --cached -- index.html` трябва да е празен (§7 т. 14).
29: 12. **`sw.js` не се пипа** (недосегаем и по `006:158`, и по `007:13`; освен това промяната е безполезна — `sw.js:104-106` трие само кешове с префикси `B2_CACHE_PREFIXES`, а `fire-varna-search-*` не е сред тях).
30: 
31: ---
32: 
33: ## 1 · Мярка
34: 
35: ### А. Базата (всяко число с извор)
36: 
37: **Публичните payload-и днес** (`C:/git/Fire_Varna/data/`, СКАУТ 1 §0/§2, СКАУТ 5 §A):
38: 
39: | факт | стойност |
40: |---|---|
41: | `search_index.json` | 11 242 756 B · 86 232 записа · `index_schema_version "2.0"` · `address_row_count 80510` · `vocab` 2 889 · `district_names` 5 |
42: | по вид | address 70 575 · mf 14 687 · parcel 970 |
43: | полета | `label` 43 133 · `display_id` 43 295 · и двете 196 · `qtk` 19 494 · `alias_tk` 574 · `stk` 362 · `btk` 5 567 · `d` 85 935 |
44: | `address_rows.json` | 5 073 137 B · 80 510 реда · `field_order ["normalized_address","lat","lng"]` |
45: | first load | HEAD 560 855 + 1 317 355 = 1 878 210 B (кап 5 MB); адресните са lazy — 15,57 MiB на първи фокус |
46: | `district_names` | **проверено от Planner-а сега:** `["Аспарухово","Владислав Варненчик","Младост","Одесос","Приморски"]` (`data/search_index.json`, top-level) — `d=3` е Одесос, `d=4` е Приморски |
47: 
48: **Подписаните полигони** (`C:/git/varna_3d/data/quarters_signed.geojson`): **проверено от Planner-а сега — 60 имена**, сред които `ж.к. Възраждане` + `Възраждане 1..4`, `ж.к. Младост` + `Младост 1/2`, `кв. Чайка` И `к.к. Чайка`, `кв. Левски`, `кв. Виница`, `Център`, `Колхозен пазар`; **няма „Цветен квартал“, няма „Боровец“ (само север/юг)**.
49: 
50: **Класове спрямо полигоните** (СКАУТ 3 §1–§5): inside-undisputed 42 566 · inside-edge 26 227 · overlap-incomparable 4 174 · outside-all 13 265. Върху inside-undisputed: съвпада 4 569 · противоречи 4 399 · без дума 33 598. Класове на несъгласие (n≥5, 53 реда): `vinitsa`→Манастирски рид 1 264 / Акчелар 651 / Ален Мак 205 / Св. Никола 64 / Сотира 63 / Перчемлията 88 / Евксиноград 68; `tsveten kvartal`→кв. Левски 318, →Изгрев 9; `mikroraion`→Център 269, →Гръцката махала 154; `kolhozen pazar`→кв. Тракия 245; **`chaika`→кв. Левски 150**; `rozova dolina`→Аспарухово 177.
51: Дупки (outside-all, само `mf` носят дума): Център 753 · Колхозен пазар 490 · Левски 478 · Гръцката махала 410 · Чайка 219 · Цветен квартал 197 · Виница 1 461 · без дума 8 810.
52: Припокривания: 5 620 → **подписан parent/child 1 446 · несравними 4 174** (СКАУТ 3 §5; обръща сплита 4 202/1 418 от мярката 08.09 → М0.4).
53: Проверимост на днешните думи: от 19 494 с `qtk` само **8 968 (46,0 %)** стоят там, където полигон може да ги потвърди или обори.
54: 
55: **Лентата и конкурентите (числа на опровергателите — задължителни за преизмерване в М0.5):**
56: 
57: | факт | gates | semantics |
58: |---|---:|---:|
59: | в точно един полигон | 67 347 | — |
60: | от тях в собствената лента | 25 613 | 25 613 |
61: | от тях с конкурент в лентата | **11 641 (45,4 %)** | **11 625 (44,3 %)** |
62: | извън лентата, но с конкурент | 2 156 | — |
63: | извън всички, но в лентата на ТОЧНО ЕДИН | **4 042** | — |
64: | извън всички, в лентата на няколко / далече | 620 / 8 603 | — |
65: 
66: **Флагманът (двамата опровергатели съвпадат, третият го потвърждава по друг път):** записът `{"kind":"mf","pin":[43.22212,27.9378],"tk":["studentska","bl","11"],"qtk":["chaika"],"label":"кв. Чайка, бл. 11","g":"b6797e83ec13fe798"}` е **вътре в кв. Левски на 67,4 m от ръба** при `precision_m = 100`; най-близкият чужд полигон **ж.к. Бриз е на 82,8 m** — тоест конкурент В лентата. Под Р5(а) и Р5(в) на v1 този запис **остава без квартал** → v1 не решаваше жалбата на Петър (§12).
67: Съседни случаи: „Цветен квартал, бл. 11“ вътре в кв. Левски на 56,3 m с конкуренти Изгрев 49,5 m и Кокарджа 49,0 m; запис `pin [43.21976, 27.91949]`, днес „кв. Левски, бл. 11, бул. Царевец“, е **51,2 m ИЗВЪН** кв. Левски.
68: 
69: **Днешното поведение на клиента** (СКАУТ 2 §1, реален матчер): „чайка студентска бл 11“ → ред 1 = `кв. Чайка, бл. 11`, `all=true`, съвпадението през **`qtk`**; „левски студентска бл 11“ → сградата **не излиза изобщо**; „левски битоля 13“ → `all=true` за улица извън всички полигони.
70: 
71: **Ориентирът (B) — база с ПРОТИВОРЕЧИЯ, които М0.6 решава:**
72: 
73: | факт | извор | стойност |
74: |---|---|---|
75: | mf записи с „бл 11“ в града | задание (Петър) | 385 |
76: | mf с `btk`, съдържащ „11“ | delivery | **91** |
77: | mf етикети `бл\.\s*11(?!\d)` | delivery | **95** |
78: | етикети с улица след блоковия номер | задание | 26 |
79: | mf с блоков номер (`btk`) общо | gates | 5 567 |
80: | от тях с улична точка ≤ 120 m | gates | 4 243 |
81: | от тях БЕЗ улица ≤ 120 m | gates | **1 324 (23,8 %)** |
82: | блокови групи по `g` / без улица в 120 m | semantics | 1 353 / **213 (15,7 %)** |
83: | колизионни двойки (каноничен квартал, блок №) | gates 186 · semantics 550 | — |
84: | от тях НЕразличими по ориентир | **gates 24 · semantics 16** | — |
85: | разстояние: медиана / p90 / ≥100 m | gates | 36,7 m / 93,9 m / **339 от 4 243** |
86: | `address_line` с уличен опенер | gates 21 717/60 614 (35,8 %) · semantics 185/1 056 блокови (17,5 %) | — |
87: | **клъстерът на флагмана** | delivery/semantics | `cluster_5eb05fc2c606f820`, `address_line = "Студентска бл. 11"` → `extractStreet` дава **null** (няма „ул.“), а `tk` на записа НОСИ `studentska` |
88: 
89: **Свидетелят НЕ е „кадастралната дума“** (semantics, върху `app/modules/search/data/search_bridge.json`): от 60 604 клъстера с `quarter.name` — `source`: **osm 35 054 / kais 25 550**; `mode`: nearest_point 33 188 / polygon_cover 1 866 / null 25 550; флагманът носи `{name:"кв. Чайка", source:"osm", confidence:"low", mode:"nearest_point", distance_m: 707.5}`. Затова в целия план думата е **„написан свидетел“** с колона `source` в леджера.
90: 
91: **Размерът на промяната (две независими оценки, и двете >> „~+0,3 MB“ от v1):** semantics ≈ **+1,26 MB** само за каноничния `qtk` + `q`; delivery ≈ **+1,54 MB** (q 0,308 + wtk 0,420 + нето qtk 0,812). Реалната стойност зависи от правилото за `wtk` (§4.1 т. 2) → М0.10.
92: 
93: **Двата дисплей пътя:** 42 937 само `label` · 43 099 само `display_id` · 196 и двете. **205 mf записа носят `btk` и НЯМАТ `label`** (gates и delivery съвпадат); общо 581 записа без `label` носят „бл“ в текста си от `address_rows` (delivery). За display_id пътя: **2 775 записа без `label`** биха се изписали „<каноничен квартал>, <ПРОТИВОРЕЧАЩА написана дума>“, а **11 627** с неопределен канон запазват квартална дума в свободния текст (semantics).
94: 
95: ### Б. М0 — задължително преизмерване преди първия ред код
96: 
97: Изпълнителят пуска и записва в `C:/git/Varna_buildings/output/addr_quarter_M0.json` (частно, `output/*` е gitignored). **Нула shell-пренасочвания и нула пайпове за байтове** (PowerShell 5.1 превръща `>` в UTF-16LE; delivery измери 603 838 B вместо 301 917 B и трети sha при пайп).
98: 
99: | № | какво | как | защо |
100: |---|---|---|---|
101: | М0.1 | **OID на полигоните** | `git -C C:/git/varna_3d rev-parse 05f485e:data/quarters_signed.geojson` | пинът е СЪДЪРЖАНИЕ, не комит; двамата опровергатели измериха един и същ блоб `82706fb5fef494175f912db82a871a6c38b4e472`, 301 917 B, sha256 `c1551d24…871b3` за 05f485e И 6486b48 → „противоречието“ на v1 отпада (§11.1) |
102: | М0.2 | байтовете + sha256 | Python: `subprocess.run(["git","-C","C:/git/varna_3d","cat-file","blob",OID],capture_output=True).stdout` → sha256 върху буфера → `open(...,"wb")` | константата `SIGNED_QUARTERS_OID/SHA256` не бива да пинова артефакт на обвивката |
103: | М0.3 | квартални маркери в `address_rows` | явен списък дефиниции | не е противоречие, а 4 дефиниции: буквално „кв./ж.к.“ **0**; водещ гол маркер **4 965**; „местност“ някъде **4 139**; подписано име като дума **23 888** (semantics) |
104: | М0.4 | сплит на припокриванията | скрипт по метода на СКАУТ 3 | 1 446/4 174 срещу 4 202/1 418 |
105: | М0.5 | **лентата: пълната таблица** | нов скрипт: за всеки пин — съдържащи полигони, `d_edge` до собствения ръб, най-близък чужд ръб | дава числата за Р5 (а)/(б)/(в)/(г) и за Р5-д; днешните оценки: 25 613 в лентата, 11 641/11 625 с конкурент, 2 156 извън лентата с конкурент, 4 042 извън-но-в-лентата |
106: | М0.5-б | **флагманите поименно** | същият скрипт, за пиновете `[43.22212,27.9378]`, `[43.21976,27.91949]`, „Цветен квартал бл. 11“, 3 записа на ул. Битоля | тези числа влизат ДОСЛОВНО в Р4/Р5 и в фикстурата на G-A3-г |
107: | М0.6 | **ориентирът** | за всички mf с `btk`: собствена улица (двете дефиниции на Р10), най-близка улична точка ≤ R, разстояние, отхвърлени низове, колизионни двойки и НЕразличими групи | сверява 385↔91↔95, 24↔16, 1 324↔213; **разминаване = СПИРАЙ** |
108: | М0.7 | блокови колизии ПРЕДИ | `npm run build:fire-varna:staging`, запис на `blockGroups/collisionPairs/collisionGroups/disambiguated/collisionNoStreet` (`build_fire_varna_search_index.mjs:1113-1116`) + `c2ResByReason` | смяната на квартала и махането на уличния суфикс пренареждат ключа `(quarter, block#)` |
109: | М0.8 | S9 базата | същият билд, `tokenInconsistentTotal` срещу `S9_BASELINE = 5828` (`:452-454`, `:1042-1051`) | дрифт гейтът ще реагира |
110: | М0.9 | червената база на Fire_Varna | `python -m gates.run_gates` · `python -m unittest discover -s tests` | днес: exit 1 (✗4, ✗6) и 24/342 паднали (СКАУТ 4) — адресният лот декларира СВОЙ назован интервал по G20 |
111: | М0.10 | **размерът** | пробен билд с новите полета → байтове на двата payload-а | Р12-в подписва таван; днес 15,57 MiB lazy |
112: | М0.11 | **състоянието на индекса** | `git -C C:/git/Fire_Varna status --porcelain` + `git diff --cached --stat -- index.html` | delivery измери `M  index.html` СТЕЙДЖНАТ (106+/24−) — F1 не тръгва, докато Б3 не е комитнат |
113: | М0.12 | районът на флагманите | `d` на записите с `bitolia`, `studentska bl 11` | v1 писа „район Одесос“; semantics измери 42/42 = **Приморски** (`d=4`), а `district_names` е проверен от Planner-а |
114: 
115: ### В. Точки на вмъкване (всички проверени лично от Planner-а сега)
116: 
117: **`C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs`:** `:452-454` S9 база · **`:457-458` `TYPEWORDS` (няма „do“)** · `:459-471` `canon` · `:481-487` `entryTokenSet(e)` — чете **геокодерния** запис, не публичния `o` · `:502-509` `s9Inconsistency` (правило (1): всички улични токени липсват → inconsistent) · **`:609-619` `resolveC2BlockLabel` — fail-closed, `reason:"token_inconsistent"`** · `:698` `o = {kind,pin}` · **`:701` `qtk` — единственото място, където кварталните токени влизат в индекса** · `:722-724` dtk/stk/btk · `:731` `evaluateRow` · **`:743-754` C2** · `:757-779` S9 · `:806` `display_id` само при липсващ label · `:826-842` F3 (не прилага повторно токеновия гард) · `:847-850` tidy · **`:857-871` регистърът** · **`:873-922` Р38** · `:923` push.
118: 
119: **`js/lib_fire_varna_block_labels.mjs`:** `:39` `STREET_TYPE_RE = /^(ул|бул|бл\.вход|пл)\.?$/i` · `:106-126` `extractStreet` (без типов опенер → `null`) · `:155` `buildBlockLabelIndex` · `:168` `cleanQuarterDisplay(info.quarter)` · `:170` `extractStreet(info.addrLine)` · `:183` база `` `${quarter}, бл. ${rec.n}` `` · **`:191-199` Pass C — улица САМО при колизия, лепи се като `${base}, ${street}` (без „до“)** · `:203-215` stats.
120: 
121: **`js/test_fire_varna_publish_gate.mjs`:** `:40-47` входовете (полигони НЕ се четат) · **`:56-59` `ALLOWED_ENTRY_KEYS` (13 ключа, затворен набор — всеки непознат ключ вече е нарушение)** · `:62-68` `PRIVATE_KEYS` · `:71` каднум · `:78-80` регион · `:101-104` `FORBIDDEN_SUBSTRINGS` · `:108` bbox · `:110` `TOKEN_FIELDS` · `:128-147` топ-ниво (НЕ е затворено множество).
122: 
123: **`C:/git/Fire_Varna/index.html`:** `4881-4892` `baseAddressLabel` (label → `addressRows[display_id].normalized_address` → район) · `4893-4897` `formatAddressHit` · `5088-5100` `dedupeDisplayRows` · **`5134` резервен vocab · `5140-5145` postings · `5151` `_areaVocab = dtk∪qtk∪stk`** · `5164-5171` `qBlk`/`areaPresent`/`blockTyped` · `5197-5221` `scoreEntry`: tk `:5204` → alias `:5205` → **`matchedCore += 1` `:5206`** → **qtk `:5207`** → dtk `:5208` → stk `:5209` · **`:5216-5219` `dem`/`ddem`/`odem`/`sdem` — всичките с условие `matchedCore === 0`** · `5230-5256` компаратор, **`5252-5253` `tk.length + qtk.length`** · `5265` `trueTie` · **`5278-5288` груповият блоков клон** · `5291-5299` bare-block · `5303`/`5313` двете проекции · `5327` `SEARCH_CACHE` · **`5351-5372` `ensureSearchData` — тук е единственият слой, който може да е fail-closed** · `5411-5423` `buildExactItem` (`5417` заглавие, `5420` „район X“) · `5430` `'Няма съвпадения'` · `5926` approx = false.
124: 
125: ### Г. Гейтове днес — какво покрива адресната доставка
126: 
127: Нула от седемте на `run_gates`: `SHA_PINS` (`gates/run_gates.py:68-72`) и `PUBLIC_BLOBS` (`:82-87`) са затворени около hotels/places/categories/signed_facts; **`check_no_cad_ids` чете РАБОТНОТО ДЪРВО и мълчаливо пропуска липсващ файл** (`:188-191`); `coverage.py:75` = `("places","hotels")`. Пипат адресите само `tests/test_data_ascii_mojibake.py:35-36` и `tests/test_basemap_manifest.py:164-165`. `data/generation_manifest.json` не се чете от никого. `recall_sweep.py:73-76` работи само върху hotels/places/categories → **замразеният корпус не покрива адреси и няма адресна `--freeze` команда** (`:90`). Единственият истински пазач е публикационният гейт в `Varna_buildings`.
128: `gates/probe/b3_g11.py` (стейджнат): инвентар + съдържание от ЕДНА снимка (`:91-93`, `:55-62`), но **`ALLOWED_NEW` е затворена седморка (`:40-46`) и `stray_new` дава exit 1 (`:116-119`)**; при `HEAD --cached` след комита дифът е празен и това рамо е инертно.
129: 
130: ---
131: 
132: ## 2 · Целта и НЕ-целта
133: 
134: **Вярно = координатата решава квартала; името е свидетел.**
135: 
136: | Класификация на пина | Каноничен квартал | Написан свидетел | Дисплей |
137: |---|---|---|---|
138: | в точно един полигон, **извън лентата** | името на полигона | `wtk` (търсим, демотиран) | „кв. Левски, …“ |
139: | в точно един полигон, **в лентата** | по Р5 (а/б/в/г) | същото | по Р5 |
140: | подписан parent/child + геометрично доказан | **само детето** | същото | детето |
141: | parent обявен, но недоказан геометрично | няма | същото | само „район X“ + леджер |
142: | несравнимо припокриване | няма | същото | само „район X“ |
143: | извън всички (вкл. „в лентата на един“, Р5-д) | по Р5-д | същото, **без гард** | по Р5-д |
144: 
145: **Целта:**
146: 1. Публичната квартална дума за еднозначните редове е името от подписания полигон, на **двата** дисплей пътя (label и display_id).
147: 2. Написаният свидетел остава **търсим** (правилото на Р38 „добавя, никога не реже“, комит `bfb5f86`), но **не удовлетворява изричен квартален филтър, когато записът има канон, който му противоречи**.
148: 3. Всеки блоков ред носи **ориентир**, доставен **структурно** (стига и до двата дисплей пътя, без да пипа `address_rows.json` и без да минава през токеновия гард на C2).
149: 4. Неопределеното се показва като неопределено — доколкото текстът позволява (§3 Р12: 2 775 реда днес биха си противоречили сами).
150: 5. Дупките, ръбовете и споровете отиват в **частен леджер** и в борда, не в данните.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 190..251 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 563ms:
190: **Р5-д · Класът „извън всички, но в лентата на ТОЧНО ЕДИН полигон“ (~4 042; пример: „кв. Левски, бл. 11, бул. Царевец“ на 51,2 m извън).**
191: *Препоръка:* **остава неопределен (без канон), НО свидетелят му НЕ се гаси** (виж Р14-б) — така „бл 11 левски“ продължава да го връща, само че под редовете с канон, с назована причина в леджера. Алтернативи за подпис: (i) получава името; (ii) пълно мълчание (не се препоръчва — истински Левски бл. 11 изчезва от собствената заявка на Петър).
192: 
193: **Р6 · Р38 (зоната „Виница“) срещу подписаните полигони.** Зоната хваща 9 771 реда (8 996 „без свидетелство“), а Манастирски рид (1 264), Акчелар (651), Ален Мак (205), Св. Никола (64), Бриз, Перчемлията, Евксиноград, Сотира имат СВОИ полигони.
194: *Препоръка:* подписаният полигон има предимство; Р38 работи само там, където резолверът връща неопределено; правилото „добавя, никога не реже“ се запазва, но добавеният токен отива в свидетелското поле. Отменя част от подписан на 12.08 прецедент → иска изричен нов подпис.
195: 
196: **Р6-б · Отношението към ADR 010 (D6/D7/D8).** ADR 010 D6 (`010:48`) урежда канала `SIGNED_POLYGON` в `varna_3d/src/fire_varna_locations.py` за **375-те МЕСТА** („пише само в ред без свидетел, извън ръба, в точно един полигон“); този лот е ДРУГА повърхност (адресният индекс, генериран в `Varna_buildings`) — затова тук няма автоматична отмяна (§11.2). Но политиките се разминават в три точки и това трябва да е ПОДПИСАНО, не мълчаливо: (1) тук полигонът пише и в ред с написан свидетел (~4 399 замени); (2) при Р5(в) пише и в лентата (~25 613); (3) D8 иска геометрично доказано `дете ⊆ родител` — приемаме го дословно (недоказаният parent → неопределено + червен ред в леджера).
197: *Препоръка:* ADR 064 изброява трите разминавания и казва „ADR 010 остава непроменен за местата“.
198: 
199: **Р7 · Несравними припокривания (4 174; топ: Аспарухово+Розова долина 746, Гръцката махала+Център 621, Възраждане+Възраждане 1 545 …).**
200: *Препоръка:* неопределено + леджер. Липсващите йерархии (1 179 + 746 + 525 + 296 + 239 записа) са ход в регистъра → **сутрешен списък**. Признатата цена: ~2 985 записа остават неопределени само заради липсващ `parent`.
201: 
202: **Р8 · Approx пакетът** (8 361, `index.html:5926 = false`). *Препоръка:* остава изключен; при палене минава през същия резолвер.
203: 
204: **Р9 · Ориентир: винаги или само при колизия?** Днес улица се лепи само при сблъсък в СЪЩИЯ написан квартал (`lib_fire_varna_block_labels.mjs:191-199`); само 26 етикета носят улица.
205: *Препоръка:* **винаги за блокови редове** („много блокове 11 в кв левски не е добре“). Колизионният детектор остава само за да маркира `must_disambiguate` и да храни G-A6б.
206: 
207: **Р9-б · Какво става, когато ориентирите СЪВПАДАТ** (измерено: 24 (gates) / 16 (semantics) неразличими групи; примери: ж.к. Бриз бл. В — 13 групи, „ул. Д-р Петър Скорчев“ 4 пъти; кв. Трошево бл. 5 — две групи „ул. Радост“; кв. Чайка бл. 37 — две групи БЕЗ улица).
208: *Препоръка:* втора степен на ориентира — **втората по близост различаваща улица**; ако и тя не различава — **разстоянието в метри** („до ул. Радост, 40 m“ / „…, 90 m“); остатъкът след двете степени е **подписан списък изключения** от М0.6, срещу който G-A6б сверява (гейт срещу измерен остатък, не срещу нула).
209: 
210: **Р9-в · Един източник на уличния текст.** С Р9 ориентирът става структурен → Pass C (`:191-199`) **спира** да лепи улица в `label` (иначе „бл. 11, ул. Мир, до ул. Мир“). Цена: ~26 етикета губят суфикса си, който се връща като структурен ориентир; диффът се мери (G-A10). *Алтернатива:* Pass C остава и структурният ориентир се пропуска там — по-малък диф, две правила.
211: 
212: **Р10 · Какво е „собствена улица“ и как се изписва.** Днешният `extractStreet` иска типов опенер (`:39`) → за „Студентска бл. 11“ връща **null** (17,5 % от блоковите `address_line` дават улица), но `tk` на записа НОСИ `studentska`.
213: *Препоръка (Р10-а):* собствена улица = `extractStreet(addrLine)` **ИЛИ** улично име от речника (1 625 имена), чиито токени са в `tk` на записа. Изписване: собствена → „, ул. Х“; чужда (най-близка) → „, **до** ул. Х“.
214: *Следствие за подписа:* при Р10-а флагманът се изписва **„кв. Левски, бл. 11, ул. Студентска“** (собствена улица), не „до ул. Студентска“. Ако предпочиташ „до“ — тогава Р10-б: собствена улица САМО по `extractStreet`, и флагманът минава по клона „най-близка“ (52 m). **Един низ, не два** — Р13 се подравнява по избора тук.
215: 
216: **Р11 · Радиус за „най-близка улица“.** Измерено: медиана 36,7 m, p90 93,9 m; 4 243 от 5 567 имат улица ≤ 120 m.
217: *Препоръка:* **120 m**, детерминистично разкъсване на равенства (по-малко разстояние → по-малък `skel` низ → по-малък `_ord`).
218: 
219: **Р11-б · Качество на ориентира.** 339 от 4 243 са на ≥ 100 m; парсването ражда низове като „ул кк зл пясъци х л вихрен“, „ул жк изгрев“, „ул д р индржишка кръстева“.
220: *Препоръка:* (1) ≤ 60 m → „до ул. Х“; 60–120 m → „до ул. Х, ~N m“; > 120 m → без ориентир, причина `no_street_within_radius`; (2) **филтър за нелегитимни низове** (токени `жк/кк/зпз/х л`, числови опашки, повече от 4 инициала) → причина `street_string_rejected`; (3) затворен списък допустими причини: `own_street`, `nearest_street`, `no_street_within_radius`, `street_string_rejected`, `no_block_number`.
221: 
222: **Р12 · Къде живее кварталната дума в дисплея.**
223: - (а) вътре в `label` — тогава display_id пътят (43 099 реда) остава без квартал завинаги;
224: - **(б) препоръка — структурно поле `q` + топ-ключ `quarter_names[]`** по образеца на `d`/`district_names`; кварталният сегмент напуска `label`; клиентът композира заглавието.
225: - **Р12-б (НОВО, задължително допълнение):** при (б) заглавието по display_id пътя е `префикс + ', ' + normalized_address`, а самият текст носи квартална дума → **2 775 записа биха се изписали „ж.к. Бриз, акчелар“**. Варианти: (i) **материализира се `label` само за тези 2 775** (байтовете се мерят в М0.10) — препоръка; (ii) амандамент на ADR 007 D2 и нормализация в `build_fire_varna_address_rows.mjs:98` — по-скъпо управленски; (iii) приема се и се обявява. Отделно 11 627 реда с НЕОПРЕДЕЛЕН канон запазват квартална дума в текста си → §2 цел 4 важи с това ограничение, освен ако не изберем (i) и за тях (цената пак е в М0.10).
226: - **Р12-в · Подписан таван за размера.** Оценките: +1,26 MB (semantics) / +1,54 MB (delivery) само за квартала, преди ориентира и материализацията. *Препоръка:* подписваш число `N` байта за СБОРА на двата lazy payload-а (днес 15,57 MiB); гейт G-B3 го чете от `expectations.json`; надвишаване = СПИРАЙ.
227: 
228: **Р13 · Точните низове (за дословен подпис, след избора по Р10 и М0.12):**
229: 1. заглавие с квартал и собствена улица: `кв. Левски, бл. 11, ул. Студентска` *(при Р10-а)* **или** `кв. Левски, бл. 11, до ул. Студентска` *(при Р10-б)*;
230: 2. заглавие без квартал: `бл. 11, до ул. Студентска` + втори ред `район Приморски`;
231: 3. адресен ред извън всички полигони: `ул. Битоля 13` + `район Приморски` (**не Одесос** — v1 сгреши; `d=4` = Приморски, `district_names` проверен);
232: 4. префиксът се взима **дословно** от `name` на полигона, с типовата представка, без превод.
233: 
234: **Р14 · Гардът на свидетеля.**
235: *Препоръка:* (а) `wtk` = написаните токени **МИНУС** каноничните на същия запис (иначе инвариантът `wtk ∩ qtk = ∅` пада на първия билд — ~4 588 записа имат съгласна дума); (б) речникът за „изричен квартален филтър“ се строи от **`quarter_names` (всичките 60 канонични имена)**, не от наблюдаваните `qtk` — иначе кварталите, които не са раздали нито едно име, нямат гард и „ж.к. Дружба, бл. 11“ остава пълно съвпадение през свидетеля.
236: **Р14-б · Обхват на гарда:** гардът гаси свидетеля САМО за записи с **`q != null`** (има канон, който му противоречи). Записите с неопределен канон (в т.ч. Р5-д) запазват силата на свидетеля, но с демотиране `wdem`. Така „чайка студентска бл 11“ не е пълно съвпадение, а „бл 11 левски“ все пак връща блока на бул. Царевец.
237: 
238: **Р15 · Ориентирът е СТРУКТУРЕН, не в `label` и не в `stk`.**
239: *Довод 1:* `resolveC2BlockLabel` (`:609-619`) е fail-closed по `s9Inconsistency`, а „до“ **не е в `TYPEWORDS` (`:457-458`)** → етикет „бл. 11, до ул. Мир“ с чужда улица дава `streetMissing === streetTotal` → `token_inconsistent` → етикетът се ИЗХВЪРЛЯ. *Довод 2:* `entryTokenSet` (`:481-487`) чете геокодерния `e`, а `o.stk` се пише на `:723` върху публичния обект — спасяването „през stk“ на v1 не работи без мутиране на `e`. *Довод 3:* `_areaVocab` (`:5151`) се храни от `stk` → ~306 нови улични имена биха превключили цяло семейство заявки в груповия блоков клон (`:5278-5288`).
240: *Препоръка:* ново поле `o` (индекс в топ-ключ `orientations[]`) + нови токени в **`otk`** (в postings и vocab, **НЕ в `_areaVocab`**), с демотер `otdem = 1`, ако поне един токен на заявката е съвпаднал **само** през `otk` (per-token, не `matchedCore === 0` — иначе демотерът е мъртъв, както е `sdem` при блокови заявки). Така: (1) `label` не се пипа → C2/S9 остават непокътнати; (2) ориентирът стига и до двата дисплей пътя (включително 205-те блокови реда без `label`); (3) „студентска бл 11“ не сменя клона на рендера.
241: 
242: **Р16 · Каноничните токени.** Правилото „skel(name без представка), разделено на думи“ дава голи цифри `1`,`2`,`3`,`4` (Младост 1/2, Възраждане 1–4 — проверено в имената) и къси `sv`, `rid`, `mak`.
243: *Препоръка:* числов или ≤ 2-знаков суфикс НЕ влиза самостоятелно в `qtk` (само биграмата „mladost 1“); токени с дължина ≤ 2 и чисти числа се изхвърлят. Делтата в подредбата (`:5252-5253`) се мери.
244: 
245: **Р17 · Как двете доставки стават ЕДНА публикация.** *Препоръка:* Б3 се комитва ПРЪВ, от твоята ръка (данните са твои), после върви адресният лот; подпис и замразяване **само когато и двете са в HEAD** (проверка 1 чете работното дърво, проверка 6 — блоба на HEAD).
246: 
247: **Р18 · G-B1 и `ALLOWED_NEW`.** Адресният лот добавя ≥ 4 нови проследени файла; `gates/probe/b3_g11.py:40-46` е затворена седморка и е част от стейджнатия Б3.
248: *Препоръка:* лотът получава **свой** пробен файл `gates/probe/addr_g11.py` (копие на механиката със свой `ALLOWED_NEW`), за да не пипаме Б3-евия артефакт. Алтернатива: разширяваш `ALLOWED_NEW` с четирите пътя — тогава §0.10 се амандира за този един ред.
249: 
250: ---
251: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 301..438 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 600ms:
301: **ПРОМЯНА · `package.json`** — `build:signed-quarters`, `test:signed-quarters`, `test:block-orientation`, `test:fire-varna-determinism`; **`build:fire-varna` (подразбиращият се път, който пише в `../Fire_Varna/data` и НЕ строи манифеста) се обявява за забранен** — доставя се само през `:staging` + ръчно копиране на трите файла заедно.
302: 
303: **НОВ · `docs/decisions/064_signed_quarter_polygons_decide_the_public_quarter.md`** — ADR (кондензиран шаблон) + ред в `docs/decisions/README.md`; изрично: кои клаузи на ADR 006/007 се вдигат, кои разминавания с ADR 010 се обявяват (Р6-б), че `sw.js` и съдържанието на `address_rows.json` остават недосегаеми; `docs/activeContext.md` + `docs/unknowns.md` в същия ред.
304: 
305: ### 4.2 `C:/git/varna_3d`
306: **Нула промени, нула комита.** Само четене на блоба по OID (М0.1).
307: 
308: ### 4.3 `C:/git/Fire_Varna` (Executor комитва кода; данните — Петър)
309: 
310: **ПРОМЯНА · `index.html`:**
311: 1. `:5134` и `:5140-5145` — `wtk` и `otk` влизат в резервния vocab и в postings.
312: 2. `:5151` `_areaVocab` остава `['dtk','qtk','stk']` — **`wtk` и `otk` НЕ влизат** (иначе „студентска бл 11“ сменя клона на рендера, `:5168-5171` → `:5278-5288`).
313: 3. След `:5152`: `index._signedQuarterVocab` = множеството токени, произведени от **`quarter_names`** (Р14-б), не от наблюдаваните `qtk`.
314: 4. След `:5185`: `qFilterTok[qi] = _signedQuarterVocab.has(toks[qi])`.
315: 5. `scoreEntry` **след `:5209`**: клон за `wtk` — при `qFilterTok[qi] === true` **И** `e.q != null` свидетелят се пропуска изцяло (`best` остава 0 → `all=false`); иначе важи с `matchedViaWitness += 1`. Отделен клон за `otk` с `matchedViaOtkOnly`.
316: 6. `:5216-5221`: `wdem = matchedViaWitness > 0 && matchedCore === 0 ? 1 : 0`; **`otdem = matchedViaOtkOnly > 0 ? 1 : 0`** (per-token, съзнателно различно от `sdem`, който е мъртъв при блокови заявки, защото `bl`/номерът винаги удрят `tk`); нови редове в компаратора между `:5239` и `:5240` и в `trueTie` (`:5265`).
317: 7. `:5252-5253` подредбата остава `tk.length + qtk.length` — `wtk`/`otk` не се броят; делтата от смяната на `qtk` се обяснява в replay-а.
318: 8. `baseAddressLabel` (`:4881-4892`) остава само адрес; нови `quarterPrefix(hit)` от `quarter_names[hit.q]` и `orientationSuffix(hit)` от `orientations[hit.o]`; `formatAddressHit` (`:4893-4897`) композира `prefix + ', ' + base + suffix` (липсващ `q`/`o` → съответната част отпада).
319: 9. `dedupeDisplayRows` (`:5088-5100`): ключът става `norm(label) + '||' + (g ?? '') + '||' + (q ?? '') + '||' + (o ?? '')`.
320: 10. Двете проекции (`:5303`, `:5313`) получават `q` и `o`.
321: 11. `buildExactItem` (`:5411-5423`): заглавието минава през `formatAddressHit`; редът „район X“ (`:5420`) остава непроменен; класът `.asr-item` не се пипа.
322: 12. `ctx` при избор (`≈:5858-5866`) и заглавието на панела (`≈:5648`) взимат същия композиран низ.
323: 13. **`validateSearchPayload(idx, rowsPayload)` — нова функция ВЪТРЕ в среза** (Р0-б флагът я не изключва), викана от `ensureSearchData` преди `searchIndex = idx` (`:5364`): `index_schema_version === '3.0'`; всяко `q`/`o` резолвира; `idx.address_row_count === rowsPayload.rows.length`. Отказ = цялата доставка се отхвърля.
324: 14. `:5327` `SEARCH_CACHE` → `'fire-varna-search-v3'` в СЪЩИЯ комит с payload-а. **`sw.js` не се пипа** (§0.12); старият кеш `fire-varna-search-v2` остава да лежи — записва се като дълг (§9).
325: 15. Маркери за среза: `// ---- ADDR slice start` … `// ---- ADDR slice end` около `norm/skel/matchKindSet/prepareIndex/runGeocoderSearch/scoreEntry/formatAddressHit/dedupeDisplayRows` **и около `validateSearchPayload`** (иначе G-B5 е неизпълним). Липсващ маркер = `AssertionError`.
326: 16. Не се пипат: `'Няма съвпадения'` (`:5430`), `APPROX_ADDRESS_SEARCH_ENABLED` (`:5926`), PLACES клонът.
327: 
328: **НОВ · `tests/address_replay.mjs`** — изрязва среза по маркерите и го изпълнява в Node със стъбове (модел `tests/granitsi_client_probe.mjs`), с флага `ADDRESS_PATH_V2` в двете положения.
329: **НОВ · `scratch/places_search/address_corpus_build.py`** — **детерминистичен селектор** на корпуса (сортиран обход на класовете, фиксирано правило „първите N по нарастващ `_ord`“, без произволност, без seed) → пише кандидата в temp и, само с `--freeze`, проследената референция.
330: **НОВ · `scratch/places_search/address_replay_rows.json`** — замразеният корпус, сверяван като **блоб** (`git show HEAD:`; готовата проверка е `worktree_differs`, `gates/release.py:313`). Стратификация ≥ 8 заявки на клас: съгласни · несъгласни (Виница-зона, Колхозен пазар, Цветен квартал, Чайка/Студентска, микрорайон) · вътре без дума · извън всички · **извън, но в лентата на един** · parent/child · несравними · в лентата · блокови колизии · вход · координатен клон · **display_id път**. Всеки ред носи кой дисплей път е дал текста.
331: **НОВ · `tests/test_address_replay.py`** — обвивката; чете очакванията от нова секция `address_replay` в `expectations.json` („No number below is typed by an agent“ — числата идват от `--freeze`).
332: **НОВ · `tests/test_address_generation.py`** — сверява `data/generation_manifest.json` (`sha256/bytes/entry_count/address_row_count/max_display_id`) срещу блобовете в СЪЩАТА снимка (`git show :<path>` / `HEAD:<path>`) + подписания таван от Р12-в.
333: **НОВ · `gates/probe/addr_g11.py`** — по Р18 (или разширяване на `ALLOWED_NEW`, ако Петър избере другия вариант).
334: **ПРОМЯНА · `gates/run_gates.py`** — `PUBLIC_BLOBS` (`:82-87`) += двата адресни блоба; **проверка 3 се пренаписва:** чете блоба (`git show :<path>`), а **липсващ файл от списъка става ЧЕРВЕН, не тих пропуск** (`:188-190`). `SHA_PINS` не се пипа.
335: **ПРОМЯНА · `tests/test_data_ascii_mojibake.py`** — обхватът включва `quarter_names`, `orientations` и `label`; сигнатури `U+FFFD` и `[Ð Ñ Â][\u0080-\u00FF]`.
336: **ПРОМЯНА · `docs/decisions/007_address_path_v2.md`** — амандамент (write-set + разпиноване на scorer/comparator + новите гейтове; `address_rows.json` и `sw.js` остават недосегаеми) + `docs/activeContext.md`.
337: 
338: **ДАННИ (комитва Петър):** `data/search_index.json`, `data/address_rows.json`, `data/generation_manifest.json` — трите заедно, в един комит.
339: 
340: ---
341: 
342: ## 5 · Ред на изпълнение
343: 
344: ### 0. Предусловие (ръката на Петър)
345: Б3 се комитва пръв (данните са негови). След това `git status --porcelain` няма стейджнати `data/` и `index.html` пътища — проверява се от Изпълнителя (М0.11); ако не е така — **СТОП**.
346: 
347: ### А. Varna_buildings (Executor, локални комити)
348: 1. **М0** (§1.Б) → `output/addr_quarter_M0.json`. Без него нищо не тръгва.
349: 2. Копира полигоните през Python по OID (никакви `>` и `|`); проверява `git check-ignore -v output/quarters_signed.geojson`.
350: 3. **V1** `tools/build_signed_quarter_index.py` + схемата → `feat(quarters): bake signed quarter polygons into a private resolver input`
351: 4. **V2** `js/lib_signed_quarters.mjs` → `feat(quarters): add lib_signed_quarters resolver with a pinned polygon digest`
352: 5. **V3** `js/test_signed_quarter_resolver.mjs` → `test(quarters): resolver truth gate with poisoned fixtures`
353:  *Доказателство:* вариант с „най-близък полигон“ трябва да **падне**; изходът се записва.
354: 6. **V4** `js/lib_block_orientation.mjs` → `feat(fire-varna): block orientation model with own and nearest street`
355: 7. **V5** генераторът: `q` + `wtk` + `otk`/`o` + `quarter_names`/`orientations` + schema 3.0 + Р38 подчинение + излизане на квартала от `label` → `feat(fire-varna): canonical quarter q, witness wtk and structural block orientation`
356: 8. **V6** материализацията по Р12-б → `feat(fire-varna): materialise labels where the address text contradicts the signed quarter`
357: 9. **V7** частният леджер + брояците → `feat(fire-varna): private quarter ledger and build-report counters`
358: 10. **V8** публикационният гейт (нови ключове, затворено топ-ниво, полигонният вход, 7 фикстури) → `test(fire-varna): publish gate verifies the quarter against the signed polygons`
359: 11. **V9** ориентирният гейт → `test(fire-varna): block orientation gate with a signed floor and collision fixtures`
360: 12. **V10** детерминизъм → `test(fire-varna): byte-identical rebuild gate`
361: 13. **V11** ADR 064 + индекс + activeContext + unknowns → `docs(adr): ADR 064 signed quarter polygons decide the public quarter word`
362: 14. Билд през staging + гейтовете G-A* (никакъв билд по подразбиращия се път).
363: 
364: ### Б. Fire_Varna (Executor, локални комити — само код)
365: 15. **F1** клиентът (16-те точки) + маркерите + `ADDRESS_PATH_V2` → `feat(search): render the canonical quarter and the block orientation from structured fields`
366: 16. **F2** replay двигателят + селекторът на корпуса + `expectations.address_replay` + `tests/test_address_replay.py` → `test(search): address replay gate with a frozen stratified corpus`
367: 17. **F3** `gates/run_gates.py` (блоб-четене + липсващ файл = червено) + `tests/test_address_generation.py` + mojibake обхватът + `gates/probe/addr_g11.py` → `feat(gates): address blobs join the cadastral-id, geometry and manifest checks`
368: 18. **F4** амандаментът на ADR 007 + `docs/activeContext.md` → `docs: ADR 007 amendment for the signed-quarter address delivery`
369: 
370: ### В. Доставка на данните
371: 19. Изпълнителят копира трите файла от `output/fire_varna_staging/` в `Fire_Varna/data/` **заедно** и пуска целия набор гейтове. Не комитва.
372: 20. Петър комитва данните (D16/G4).
373: 
374: ### Г. Една публикация
375: Ред: **Б3 (ръката на Петър) → Varna_buildings → varna_3d (нула) → Fire_Varna код → адресните данни (ръката на Петър)**. Подпис и замразяване САМО когато и двете доставки са в HEAD. Една опашка (`ЗА_ПОДПИС_Б3_07.09.md` — адресните редове се ДОБАВЯТ в нея; преименуването на старата опашка е ход на Б3, не на този лот). Един allow-файл (адресният лот не иска нови allow редове). Едно `--freeze` за местата и едно за адресите, и двете СЛЕД подписа, всяко със свой комит. Един назован червен интервал по G20, различим от Б3-евия.
376: 
377: ### Д. Командите на Петър (по една на ред, без `&&`; **без `git push`**)
378: 
379: ```powershell
380: cd C:\git\Varna_buildings
381: npm run build:signed-quarters
382: npm run test:signed-quarters
383: npm run test:block-orientation
384: npm run build:fire-varna:staging
385: npm run test:fire-varna-publish-gate:staging
386: npm run test:fire-varna-determinism
387: cd C:\git\Fire_Varna
388: git status --porcelain
389: git add data/search_index.json data/address_rows.json data/generation_manifest.json
390: git commit -m "data(search): quarter from signed polygons + block orientation"
391: $env:PYTHONIOENCODING="utf-8"
392: python -m unittest discover -s tests
393: python -m gates.run_gates
394: python gates/probe/addr_g11.py <комитът преди първия ход на лота>
395: python -m gates.sign R<n> да --queue scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md
396: git add scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md
397: git commit -m "sign: address delivery rows"
398: python scratch/places_search/address_corpus_build.py --freeze
399: git add scratch/places_search/address_replay_rows.json scratch/places_search/expectations.json
400: git commit -m "freeze: address replay reference"
401: python -m unittest discover -s tests
402: python -m gates.run_gates
403: ```
404: 
405: **ПУБЛИКУВАНЕ — след Gate 2, с отделна твоя дума.** (v1 слагаше `git push` редом с 13 неподписани решения; `python -m gates.sign` без аргументи пада с usage, `gates/sign.py:419-427`; `--freeze` преди комит прави проверка 6 BLOCKED, `gates/release.py:313`.)
406: 
407: ---
408: 
409: ## 6 · Гейтове
410: 
411: Всеки ред: команда · очакван изход · отрицателна фикстура, която ТРЯБВА да падне.
412: 
413: | # | Гейт | Команда | Изход | Отрицателното (задължително пада) |
414: |---|---|---|---|---|
415: | G-A1 | Пинът на полигоните (OID + sha, четени в Python) | `python tools/build_signed_quarter_index.py` | 0 | подменен байт в опечения вход; подаден commit-ish вместо OID |
416: | G-A2 | Публикационен гейт (разширен) | `npm run test:fire-varna-publish-gate:staging` | 0 | ф1 `coordinates` в нов топ-ключ; ф2 `q` извън обхват; ф3 неканоничен `qtk`; ф4 `wtk∩qtk≠∅`; ф5 не-низ в `quarter_names`; ф7 `o` без ред |
417: | G-A3 | **Истинност на резолвера** | `node js/test_signed_quarter_resolver.mjs` | 0 | (а) резолвер с „най-близък полигон“; (б) пин в зоната Виница вътре в Манастирски рид, обявен за Виница; (в) недоказан parent, обявен за дете |
418: | **G-A3-г** | **Флагманът, поименно** | част от G-A3 | 0 | **пинът `[43.22212, 27.9378]` ТРЯБВА да върне присъда, която дава „кв. Левски“** (при подписания Р5); пинът `[43.21976, 27.91949]` ТРЯБВА да върне класа по Р5-д |
419: | G-A4 | **Свидетелят не е авторитет — върху ДОСТАВЕНИТЕ байтове** | част от G-A2 (с полигонния вход) | 0 | ф6: запис с `q`/`qtk` = Чайка при пин вътре в кв. Левски |
420: | G-A5 | Пълнота на леджера (вкл. `source`/`mode`/`confidence` на свидетеля) | `node js/test_quarter_ledger.mjs` | 0 | изтрит ред за запис с различен свидетел |
421: | G-A6а | **Ориентир — подписан ПОД, не дизюнкция** | `node js/test_block_orientation.mjs` | 0 | брой блокови редове с `own`/`nearest` под пода от М0.6 (при валидни причини) → червено; причина извън затворения списък → червено |
422: | G-A6б | Различимост при колизия | същият | 0 | две групи в една двойка (квартал, блок №) с еднакъв ориентир и **извън** подписания списък изключения |
423: | G-A6в | Качество на ориентира | същият | 0 | ориентир с отхвърлен низ („ул кк зл пясъци…“); ориентир над подписания праг без бележка за разстояние |
424: | G-A7 | Р38 подчинение | част от G-A3 | 0 | ред в зоната с подписан фин квартал, префиксиран „кв. Виница“ |
425: | G-A8 | Два билда байт-идентични | `npm run test:fire-varna-determinism` | 0 | подменен байт в едното копие |
426: | G-A9 | Дрифт: S9 + C2 | вграден в билда (`:1042-1051`) + брояч | 0 | `tokenInconsistentTotal` > 20 % от 5 828; **`c2ResByReason.token_inconsistent` над подписания таван от М0.7** |
427: | G-A10 | Бюджет на диффа по етикетите | част от билда | 0 | брой сменени `label` извън подписания интервал (квартален сегмент + махнатия уличен суфикс) |
428: | G-B1 | Нула геометрия, структурно | `python gates/probe/addr_g11.py <родител>` | 0 | копие с ключ `coordinates`; **нов непосочен проследен файл → изход 1** (истински родител, не `HEAD`, иначе рамото е инертно) |
429: | G-B2 | Нула кадастрални id в адресните блобове | `python -m gates.run_gates` (проверка 3, вече по блоб) | 0 | посят `10135.1.1005.1` в **блоба**; **преименуван/липсващ файл от `PUBLIC_BLOBS` → червено** |
430: | G-B3 | Поколение ↔ размер ↔ броеве ↔ таван | `python -m unittest tests.test_address_generation` | 0 | чужд `bytes` в манифеста; `address_row_count ≠ rows.length`; сбор над подписания таван (Р12-в) |
431: | G-B4 | **Address replay** | `python -m unittest tests.test_address_replay` | 0 | (i) „чайка студентска бл 11“ като ПЪЛНО съвпадение; (ii) ред, назначен по най-близък полигон; (iii) два неразличими „бл 11 левски“; (iv) **заявка, която днес не е `blockTyped`, а утре става**; (v) `ADDRESS_PATH_V2=false`, който не връща базовото поведение |
432: | G-B5 | **Клиентска fail-closed валидация (собствен ред)** | `python -m unittest tests.test_address_replay -k validate` | 0 | (а) `index_schema_version "2.0"`; (б) `q` извън `quarter_names`; (в) несъвпадащи поколения на двата файла |
433: | G-B6 | `FORBIDDEN` остава зелен | `python -m unittest tests.test_b3_gates` | без нови червени спрямо М0.9 | забранен низ, вкаран в адресен етикет |
434: | G-B7 | Mojibake / UTF-8 | `python -m unittest tests.test_data_ascii_mojibake` | 0 | посято `Ð` и `U+FFFD` в `quarter_names`/`orientations` |
435: | G-B8 | Пълният набор | `python -m unittest discover -s tests` · `python -m gates.run_gates` | 0 червени извън назования интервал; 7/7 след подписа | — |
436: 
437: ---
438: 

codex
Базата е `f745349`; Б3 още е стейджнат, включително `index.html`. V2 изрично покрива двата display пътя, но виждам възможни пролуки в демотирането на свидетеля и проверката за смесени поколения. Проверявам ги срещу реалния клиентски код.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; 4816..4900 | ForEach-Object { '{0}: {1}' -f "'$_,$a[$_-1] }; 5088..5221 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 609ms:
4816:   //   * data/search_index.json (the GEOCODER matcher projection — streets,
4817:   //     addresses, kvartali AND MF block/entrance, with район/квартал area-gating),
4818:   //     by js/build_fire_varna_search_index.mjs;
4819:   //   * data/address_rows.json (display fallback: normalized_address by row id),
4820:   //     by js/build_fire_varna_address_rows.mjs.
4821:   // Neither carries cadnum / complex_id / section / ГРАО / owner data — enforced by
4822:   // that repo's publish gate (js/test_fire_varna_publish_gate.mjs) over BOTH files.
4823:   // Selecting a result flies the map to its pin, drops ONE teal result marker, and
4824:   // opens a standalone popup with the address + nav link-outs (NO "Докладвай" — it
4825:   // is an address, not a hydrant). Nothing here touches the hydrant layer, the
4826:   // building layer, modes, report, offline, or compass.
4827:   //
4828:   // The matcher is PORTED from Varna_buildings app/modules/search (skeleton.js
4829:   // norm/skel/lev/matchKindSet + searchLogic.js runGeocoderSearch) — NO MiniSearch,
4830:   // NO new engine. The ONLY adaptations: the group key bg||complex_id -> the opaque
4831:   // `g`; cadnum tie-breaks -> a stable runtime `_ord`; the inverted index + area-
4832:   // vocab are rebuilt client-side (the payload omits them). Folding queries through
4833:   // the SAME skeleton the index builder used means index tokens and queries can
4834:   // never drift. Reuses the IIFE-scoped `map`, `buildNavActions`, `POPUP_AUTOPAN_TL/BR`.
4835:   // =========================================================================
4836:   (function initAddressSearch() {
4837:     const inputEl = document.getElementById('addrSearchInput');
4838:     const resultsEl = document.getElementById('addrSearchResults');
4839:     if (!inputEl || !resultsEl) return; // header markup missing -> no-op
4840: 
4841:     // ---- skeleton primitives (verbatim from app/modules/search/skeleton.js) ----
4842:     function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
4843:     function skel(w){w=w.toLowerCase();var C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'};var o='';for(var i=0;i<w.length;i++){o+=(C[w[i]]!==undefined?C[w[i]]:w[i]);}return o.replace(/[yj]/g,'i').replace(/(\D)\1+/g,'$1');}
4844:     function lev(a,b,cap){var la=a.length,lb=b.length;if(Math.abs(la-lb)>cap)return cap+1;var prev=[];for(var j=0;j<=lb;j++)prev[j]=j;for(var i=1;i<=la;i++){var cur=[i],best=i;for(var j=1;j<=lb;j++){var v=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));cur[j]=v;if(v<best)best=v;}if(best>cap)return cap+1;prev=cur;}return prev[lb];}
4845:     // ADR 032 A2 per-(query token) match-KIND classifier (verbatim from
4846:     // searchLogic.js): 3 exact / 2 prefix / 1 within-cap fuzzy. The geocoder route
4847:     // ranks on match KIND, so a binary matchSet is insufficient.
4848:     function matchKindSet(qt, VOCAB){var s={},cap=qt.length>=7?2:1;for(var i=0;i<VOCAB.length;i++){var v=VOCAB[i],k=0;if(v===qt)k=3;else if(qt.length<=1)k=0;else if(v.indexOf(qt)===0)k=2;else if(qt.length<=3)k=0;else if(lev(qt,v,cap)<=cap)k=1;if(k)s[v]=k;}return s;}
4849: 
4850:     // ---- display payload (address_rows.json) + label resolution ----------------
4851:     // The matcher index carries NO display string for the 48k entries with no
4852:     // addr_key; their text is the source row's normalized_address, looked up by the
4853:     // hit's display_id in the SEPARATE address_rows.json. These closure vars are set
4854:     // by ensureSearchData() after both payloads load.
4855:     let addressRows = null;   // array of [normalized_address, lat, lng] by row id
4856:     let addrFieldIdx = null;  // { normalized_address, lat, lng } column indices
4857:     let districtNames = [];   // район display-enum table (search_index.district_names)
4858: 
4859:     // Schema-driven address-row layout (M1 plan: never hardcode a column). Derive
4860:     // each needed field position from the payload's field_order.
4861:     function buildAddressFieldIndex(payload){
4862:       const order = payload && Array.isArray(payload.field_order) ? payload.field_order : null;
4863:       if (!order) throw new Error('address_rows.json missing field_order');
4864:       const idx = {};
4865:       ['normalized_address', 'lat', 'lng'].forEach(function (name) {
4866:         const i = order.indexOf(name);
4867:         if (i === -1) throw new Error('address_rows.json field_order missing "' + name + '"');
4868:         idx[name] = i;
4869:       });
4870:       return idx;
4871:     }
4872: 
4873:     // formatAddressHit — label resolution chain (privacy-safe):
4874:     //   (1) the public geocoder `label` (= cleaned addr_key) when present;
4875:     //   (2) else addressRows[display_id].normalized_address (the separate display
4876:     //       payload, indexed by the source row id);
4877:     //   (3) else the район name; NEVER a cadnum / section / complex id (the index
4878:     //       carries none). An entrance (kind:"mf" + en) appends " · вх. <en>" to its
4879:     //       parent building's resolved address.
4880:     function prettyKey(s){ return String(s).replace(/\|/g, ' ').replace(/\s+/g, ' ').trim(); }
4881:     function baseAddressLabel(hit){
4882:       if (hit.label) return prettyKey(hit.label);
4883:       if (hit.display_id != null && addressRows && addrFieldIdx) {
4884:         const row = addressRows[hit.display_id];
4885:         if (Array.isArray(row)) {
4886:           const na = row[addrFieldIdx.normalized_address];
4887:           if (na) return na;
4888:         }
4889:       }
4890:       if (hit.d != null && districtNames[hit.d]) return districtNames[hit.d];
4891:       return '(адрес)';
4892:     }
4893:     function formatAddressHit(hit){
4894:       const base = baseAddressLabel(hit);
4895:       const isEntrance = hit.kind === 'mf' && hit.en != null && hit.en !== undefined;
4896:       return isEntrance ? base + ' · вх. ' + hit.en : base;
4897:     }
4898: 
4899:     // =====================================================================
4900:     // GPS coordinate input (kind:"coord"). ADDITIVE, isolated, no payload.
5088:     function dedupeDisplayRows(rows) {
5089:       if (!Array.isArray(rows) || rows.length === 0) return rows;
5090:       const labels = rows.map(function (r) { return String(formatAddressHit(r)); });
5091:       const sgradaBlocks = new Set();
5092:       for (let i = 0; i < rows.length; i++) {
5093:         const r = rows[i];
5094:         if (r && r.kind === 'mf' && (r.en == null || r.en === undefined)) {
5095:           const bn = labelBlockNumber(labels[i]);
5096:           if (bn != null) sgradaBlocks.add(bn);
5097:         }
5098:       }
5099:       const seen = new Set();
5100:       const out = [];
5101:       for (let i = 0; i < rows.length; i++) {
5102:         const r = rows[i];
5103:         if (r && r.kind === 'address') {
5104:           const bn = labelBlockNumber(labels[i]);
5105:           if (bn != null && sgradaBlocks.has(bn)) continue; // same-block сграда present
5106:         }
5107:         const key = norm(labels[i]) + '||' + (r && r.g != null ? String(r.g) : '');
5108:         if (seen.has(key)) continue;                        // identical rendered row
5109:         seen.add(key);
5110:         out.push(r);
5111:       }
5112:       if (rows.blockHeader) out.blockHeader = rows.blockHeader;
5113:       if (rows.bareBlockHeader) out.bareBlockHeader = rows.bareBlockHeader;
5114:       return out;
5115:     }
5116: 
5117:     // ---- ported runGeocoderSearch (public-safe geocoder route) ------------------
5118:     // Transplanted from Varna_buildings app/modules/search/searchLogic.js. The ONLY
5119:     // adaptations: the group key `bg||complex_id` -> the opaque `g`; the cadnum /
5120:     // section_cadnum determinism tie-breaks -> a stable runtime `_ord`; the inverted
5121:     // index + area-vocab are rebuilt CLIENT-SIDE (payload omits inverted); dropped
5122:     // fields (life_safety_rank / physical_building_id / quarter_assignment_trust /
5123:     // odem) are absent, leaving their comparator/dedup slots inert (null-safe).
5124:     // Result rows carry ONLY safe fields + label/display_id for resolution.
5125:     const SEARCH_LIMIT = 8;
5126: 
5127:     // Build vocab (if absent), the inverted index, the area-vocab, and stamp a stable
5128:     // `_ord` on every entry. Called ONCE after the payload loads.
5129:     function prepareIndex(index){
5130:       if (!index || !Array.isArray(index.entries)) return index;
5131:       for (let i = 0; i < index.entries.length; i++) index.entries[i]._ord = i;
5132:       if (!Array.isArray(index.vocab)) {
5133:         const set = new Set();
5134:         for (const e of index.entries) for (const f of ['tk','qtk','alias_tk','dtk','stk']) { const a = e[f]; if (a) for (const t of a) if (t) set.add(t); }
5135:         index.vocab = Array.from(set).sort();
5136:       }
5137:       const postings = new Map();
5138:       for (let i = 0; i < index.entries.length; i++) {
5139:         const e = index.entries[i];
5140:         let toks = e.tk || [];
5141:         if (e.qtk) toks = toks.concat(e.qtk);
5142:         if (e.alias_tk) toks = toks.concat(e.alias_tk);
5143:         if (e.dtk) toks = toks.concat(e.dtk);
5144:         if (e.stk) toks = toks.concat(e.stk);
5145:         for (const t of toks) { let ids = postings.get(t); if (!ids) postings.set(t, (ids = [])); if (ids[ids.length-1] !== i) ids.push(i); }
5146:       }
5147:       const inverted = {};
5148:       for (const t of index.vocab) inverted[t] = postings.get(t) || [];
5149:       index.inverted = inverted;
5150:       const av = new Set();
5151:       for (const e of index.entries) for (const f of ['dtk','qtk','stk']) { const a = e[f]; if (a) for (const t of a) if (t) av.add(t); }
5152:       index._areaVocab = av;
5153:       return index;
5154:     }
5155: 
5156:     function runGeocoderSearch(query, index){
5157:       if (!index || !Array.isArray(index.entries)) return [];
5158:       const qn = norm(query);
5159:       if (qn.length < 1) return [];
5160:       const rawToks = qn.split(/\s+/).filter(Boolean);
5161:       const toks = rawToks.map(skel);
5162:       if (toks.length === 0) return [];
5163: 
5164:       const blIdx = toks.indexOf('bl');
5165:       const qBlk = blIdx >= 0 && blIdx+1 < toks.length ? toks[blIdx+1] : null;
5166:       const qBlkDisplay = blIdx >= 0 && blIdx+1 < rawToks.length ? rawToks[blIdx+1] : null;
5167:       const av = index._areaVocab || new Set();
5168:       const areaPresent = qBlk != null && toks.some(function (t) { return t !== 'bl' && t !== 'vh' && t !== qBlk && av.has(t); });
5169:       const areaBlockTyped = qBlk != null && areaPresent;
5170:       const bareBlockTyped = qBlk != null && !areaPresent && !toks.includes('vh') && toks.every(function (t) { return t === 'bl' || t === qBlk; });
5171:       const blockTyped = areaBlockTyped;
5172: 
5173:       // F1 (search-quality cycle, frame §6 2026-07-02; ported from searchLogic.js) —
5174:       // entrance-TYPED query detection: an EXPLICIT вх/vh token FOLLOWED by an
5175:       // entrance designator (a number "9"/"11", number+letter "1а", or a single
5176:       // letter "а"/"b"). A dangling "вх" or "вх <word>" is NOT entrance-typed.
5177:       // Consumed ONLY by comparator slot (4) below: an entrance-typed query ranks
5178:       // the matched entrance child ABOVE an equal-relevance non-entrance row, so
5179:       // Enter on "бл 307 вх 9" selects the вход child, not the "вх 9-11" адрес row.
5180:       // Every other query keeps slot (4) byte-identical.
5181:       const vhIdx = toks.indexOf('vh'); // skel('вх') === skel('vh') === 'vh'
5182:       const entranceTyped =
5183:         vhIdx >= 0 && vhIdx + 1 < rawToks.length &&
5184:         /^(?:[0-9]+[a-zа-я]?|[a-zа-я])$/.test(rawToks[vhIdx + 1]);
5185: 
5186:       let vocab = index.vocab;
5187:       if (!Array.isArray(vocab)) { const set = new Set(); for (const e of index.entries) for (const t of (e.tk||[])) if (t) set.add(t); vocab = Array.from(set); }
5188:       const inverted = index.inverted && typeof index.inverted === 'object' ? index.inverted : null;
5189: 
5190:       const ms = toks.map(function (t) { return matchKindSet(t, vocab); });
5191:       const numericTok = toks.map(function (t) { return /^[0-9]+$/.test(t); });
5192: 
5193:       let candidateIds = null;
5194:       if (inverted) { candidateIds = new Set(); for (const m of ms) { for (const vt in m) { const ids = inverted[vt]; if (ids) for (let i = 0; i < ids.length; i++) candidateIds.add(ids[i]); } } }
5195: 
5196:       const scored = [];
5197:       const scoreEntry = function (e) {
5198:         if (!e) return;
5199:         let matched = 0, exactName = 0, exactNum = 0, prefix = 0, fuzzy = 0, matchedCore = 0, matchedViaDtk = 0, matchedViaStk = 0;
5200:         let qBlkMatched = false, all = true;
5201:         const tk = e.tk || [], qtk = e.qtk || null, atk = e.alias_tk || null, dtk = e.dtk || null, stk = e.stk || null;
5202:         for (let qi = 0; qi < toks.length; qi++) {
5203:           const m = ms[qi]; let best = 0;
5204:           for (let ti = 0; ti < tk.length; ti++) { const k = m[tk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } }
5205:           if (atk && best < 3) { for (let ti = 0; ti < atk.length; ti++) { const k = m[atk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } } }
5206:           if (best > 0) matchedCore += 1;
5207:           if (qtk && best < 3) { for (let ti = 0; ti < qtk.length; ti++) { const k = m[qtk[ti]]||0; if (k > best) { best = k; if (best === 3) break; } } }
5208:           if (dtk && best < 3) { for (let ti = 0; ti < dtk.length; ti++) { const k = m[dtk[ti]]||0; if (k > best) { best = k; matchedViaDtk += 1; if (best === 3) break; } } }
5209:           if (stk && best < 3) { for (let ti = 0; ti < stk.length; ti++) { const k = m[stk[ti]]||0; if (k > best) { best = k; matchedViaStk += 1; if (best === 3) break; } } }
5210:           if (best === 0) { all = false; continue; }
5211:           matched += 1;
5212:           if (blockTyped && toks[qi] === qBlk) qBlkMatched = true;
5213:           if (best === 3) { if (numericTok[qi]) exactNum += 1; else exactName += 1; } else if (best === 2) prefix += 1; else fuzzy += 1;
5214:         }
5215:         if (matched > 0) {
5216:           const dem = e.quarter_assignment_trust === 'conflicted' && matchedCore === 0 ? 1 : 0;
5217:           const ddem = matchedCore === 0 && matchedViaDtk > 0 ? 1 : 0;
5218:           const odem = e.odem ? 1 : 0;
5219:           const sdem = matchedCore === 0 && matchedViaStk > 0 ? 1 : 0;
5220:           const bmatch = blockTyped && (e.btk || []).includes(qBlk) ? 1 : 0;
5221:           scored.push({ e: e, matched: matched, exactName: exactName, exactNum: exactNum, prefix: prefix, fuzzy: fuzzy, all: all, dem: dem, ddem: ddem, sdem: sdem, odem: odem, bmatch: bmatch, qBlkMatched: qBlkMatched ? 1 : 0, bdem: 0 });

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; 5223..5372 | ForEach-Object { '{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 610ms:
5223:       };
5224:       if (candidateIds) { for (const id of candidateIds) scoreEntry(index.entries[id]); }
5225:       else { for (const e of index.entries) scoreEntry(e); }
5226: 
5227:       const existsBtkHolder = blockTyped && scored.some(function (s) { return s.bmatch === 1; });
5228:       if (existsBtkHolder) { for (const s of scored) s.bdem = (s.qBlkMatched === 1 && s.bmatch === 0) ? 1 : 0; }
5229: 
5230:       scored.sort(function (a, b) {
5231:         if (a.all !== b.all) return a.all ? -1 : 1;
5232:         if (b.matched !== a.matched) return b.matched - a.matched;
5233:         if (b.exactName !== a.exactName) return b.exactName - a.exactName;
5234:         if (b.exactNum !== a.exactNum) return b.exactNum - a.exactNum;
5235:         if (b.prefix !== a.prefix) return b.prefix - a.prefix;
5236:         if (a.bdem !== b.bdem) return a.bdem - b.bdem;
5237:         if (a.dem !== b.dem) return a.dem - b.dem;
5238:         if (a.ddem !== b.ddem) return a.ddem - b.ddem;
5239:         if (a.sdem !== b.sdem) return a.sdem - b.sdem;
5240:         if (a.odem !== b.odem) return a.odem - b.odem;
5241:         const aRank = a.e.life_safety_rank == null ? 2 : a.e.life_safety_rank;
5242:         const bRank = b.e.life_safety_rank == null ? 2 : b.e.life_safety_rank;
5243:         if (aRank !== bRank) return aRank - bRank;
5244:         const aEnt = a.e.en !== undefined, bEnt = b.e.en !== undefined;
5245:         // F1 — direction-gated slot (4): typed-entrance queries rank the entrance
5246:         // child first at equal relevance; all other queries keep the pre-existing
5247:         // "precise before entrance" demotion byte-identical.
5248:         if (aEnt !== bEnt) {
5249:           if (entranceTyped) return aEnt ? -1 : 1;
5250:           return aEnt ? 1 : -1;
5251:         }
5252:         const al = (a.e.tk||[]).length + (a.e.qtk ? a.e.qtk.length : 0);
5253:         const bl = (b.e.tk||[]).length + (b.e.qtk ? b.e.qtk.length : 0);
5254:         if (al !== bl) return al - bl;
5255:         return (a.e._ord||0) - (b.e._ord||0); // determinism (cadnum dropped)
5256:       });
5257: 
5258:       // physical_building dedup: physical_building_id is DROPPED -> pbid always null
5259:       // -> every row passes through (the block is inert but preserved verbatim).
5260:       const isEntranceQuery = toks.includes('vh');
5261:       let ranked = scored;
5262:       if (!isEntranceQuery) {
5263:         const reps = index.physical_building_reps && typeof index.physical_building_reps === 'object' ? index.physical_building_reps : {};
5264:         const rankOf = function (s) { return s.e.life_safety_rank == null ? 2 : s.e.life_safety_rank; };
5265:         const trueTie = function (a, b) { return a.all === b.all && a.matched === b.matched && a.exactName === b.exactName && a.exactNum === b.exactNum && a.prefix === b.prefix && a.bdem === b.bdem && a.dem === b.dem && a.ddem === b.ddem && a.sdem === b.sdem && a.odem === b.odem && rankOf(a) === rankOf(b); };
5266:         const keptPos = new Map(); ranked = [];
5267:         for (const s of scored) {
5268:           const pbid = s.e.physical_building_id;
5269:           if (pbid == null || s.e.en !== undefined) { ranked.push(s); continue; }
5270:           if (!keptPos.has(pbid)) { keptPos.set(pbid, ranked.length); ranked.push(s); continue; }
5271:           const pos = keptPos.get(pbid), kept = ranked[pos];
5272:           if (String(s.e._ord) === String(reps[pbid]) && String(kept.e._ord) !== String(reps[pbid]) && trueTie(kept, s)) ranked[pos] = s;
5273:         }
5274:       }
5275: 
5276:       // area-gated block GROUPING (opaque g instead of bg||complex_id).
5277:       let blockHeader = null;
5278:       if (blockTyped && !isEntranceQuery) {
5279:         const seen = new Set(); const grouped = []; let blockGroups = 0; const districtCount = new Map();
5280:         for (const s of ranked) {
5281:           const key = s.e.g;
5282:           if (key != null) { if (seen.has(key)) continue; seen.add(key); }
5283:           grouped.push(s);
5284:           if (s.all && s.bmatch === 1) { blockGroups += 1; const d = s.e.d; if (d != null) districtCount.set(d, (districtCount.get(d)||0)+1); }
5285:         }
5286:         ranked = grouped;
5287:         if (blockGroups > 0) { let bestD = null, bestN = -1; for (const pair of districtCount) if (pair[1] > bestN) { bestN = pair[1]; bestD = pair[0]; } blockHeader = { block: qBlkDisplay, count: blockGroups, district_enum: bestD }; }
5288:       }
5289: 
5290:       // bare-block surface (parent/child), grouped by opaque g.
5291:       if (bareBlockTyped) {
5292:         const parentCandidates = [];
5293:         for (const s of ranked) if (s.all && s.e.en === undefined && (s.e.btk || []).includes(qBlk)) parentCandidates.push(s);
5294:         if (parentCandidates.length > 0) {
5295:           const repByGroup = new Map();
5296:           for (const s of parentCandidates) { const key = s.e.g; if (key == null) continue; if (!repByGroup.has(key)) repByGroup.set(key, s); }
5297:           const childrenByGroup = new Map();
5298:           for (const s of ranked) { if (s.e.en === undefined) continue; const key = s.e.g; if (key == null || !repByGroup.has(key)) continue; if (!childrenByGroup.has(key)) childrenByGroup.set(key, []); childrenByGroup.get(key).push(s); }
5299:           const childSort = function (a, b) { const na = /^[0-9]+$/.test(a.e.en) ? parseInt(a.e.en,10) : NaN, nb = /^[0-9]+$/.test(b.e.en) ? parseInt(b.e.en,10) : NaN; const an = !Number.isNaN(na), bn = !Number.isNaN(nb); if (an && bn && na !== nb) return na - nb; if (an !== bn) return an ? -1 : 1; if (a.e.en !== b.e.en) return String(a.e.en).localeCompare(String(b.e.en)); return (a.e._ord||0) - (b.e._ord||0); };
5300:           const bareDistrictCount = new Map(); const groupList = [];
5301:           for (const pair of repByGroup) { const key = pair[0], rep = pair[1]; const children = (childrenByGroup.get(key) || []).slice().sort(childSort); groupList.push({ key: key, rep: rep, children: children }); const d = rep.e.d; if (d != null) bareDistrictCount.set(d, (bareDistrictCount.get(d)||0)+1); }
5302:           groupList.sort(function (a, b) { const da = a.rep.e.d == null ? Infinity : a.rep.e.d, db = b.rep.e.d == null ? Infinity : b.rep.e.d; if (da !== db) return da - db; return (a.rep.e._ord||0) - (b.rep.e._ord||0); });
5303:           const projectRow = function (s, role) { const e = s.e; return { kind: e.kind, en: e.en, pin: e.pin, d: e.d, label: e.label, display_id: e.display_id, g: e.g, allTokens: s.all, matched: s.matched, exact: s.exactName + s.exactNum, prefix: s.prefix, fuzzy: s.fuzzy, bareRole: role, block: qBlkDisplay }; };
5304:           const bareOut = [];
5305:           for (const g of groupList) { bareOut.push(projectRow(g.rep, 'parent')); for (const c of g.children) bareOut.push(projectRow(c, 'child')); }
5306:           bareOut.bareBlockHeader = { block: qBlkDisplay, groups: groupList.length, districts: Array.from(bareDistrictCount, function (p) { return { district_enum: p[0], count: p[1] }; }).sort(function (a, b) { return a.district_enum - b.district_enum; }) };
5307:           return bareOut;
5308:         }
5309:       }
5310: 
5311:       const out = ranked.slice(0, SEARCH_LIMIT).map(function (s) {
5312:         const e = s.e;
5313:         return { kind: e.kind, en: e.en, pin: e.pin, d: e.d, label: e.label, display_id: e.display_id, g: e.g, allTokens: s.all, matched: s.matched, exact: s.exactName + s.exactNum, prefix: s.prefix, fuzzy: s.fuzzy };
5314:       });
5315:       if (blockHeader) out.blockHeader = blockHeader;
5316:       return out;
5317:     }
5318: 
5319:     // ---- lazy load + cache (memory for the session + Cache API offline) ----------
5320:     // TWO payloads: the matcher index (search_index.json) + the display rows
5321:     // (address_rows.json). Both lazy-load on first focus, are parsed once, and are
5322:     // persisted to the Cache API so a return visit works offline. The index is only
5323:     // published to `searchIndex` AFTER prepareIndex() finishes (so a racing query
5324:     // never sees a half-built inverted index).
5325:     const SEARCH_INDEX_URL = 'data/search_index.json';
5326:     const ADDRESS_ROWS_URL = 'data/address_rows.json';
5327:     const SEARCH_CACHE = 'fire-varna-search-v2'; // v2 = geocoder payload (v1 was section_units)
5328:     const RESULT_LIMIT = 10;
5329:     const DEBOUNCE_MS = 120;
5330:     let searchIndex = null;       // prepared matcher index (memory cache)
5331:     let searchDataPromise = null; // in-flight load (dedupes concurrent focus/input)
5332: 
5333:     async function fetchCachedJson(url) {
5334:       try {
5335:         const resp = await fetch(url, { cache: 'no-cache' });
5336:         if (!resp.ok) throw new Error('HTTP ' + resp.status);
5337:         // Persist a clone for offline use (best-effort; never blocks the parse).
5338:         if (typeof caches !== 'undefined') {
5339:           try { const c = await caches.open(SEARCH_CACHE); await c.put(url, resp.clone()); } catch (e) {}
5340:         }
5341:         return await resp.json();
5342:       } catch (netErr) {
5343:         // Offline fallback: serve the previously cached copy if we have one.
5344:         if (typeof caches !== 'undefined') {
5345:           try { const c = await caches.open(SEARCH_CACHE); const hit = await c.match(url); if (hit) return await hit.json(); } catch (e) {}
5346:         }
5347:         throw netErr;
5348:       }
5349:     }
5350: 
5351:     async function ensureSearchData() {
5352:       if (searchIndex) return searchIndex;
5353:       if (searchDataPromise) return searchDataPromise;
5354:       searchDataPromise = (async function () {
5355:         try {
5356:           const [idx, rowsPayload] = await Promise.all([
5357:             fetchCachedJson(SEARCH_INDEX_URL),
5358:             fetchCachedJson(ADDRESS_ROWS_URL),
5359:           ]);
5360:           addressRows = (rowsPayload && Array.isArray(rowsPayload.rows)) ? rowsPayload.rows : [];
5361:           addrFieldIdx = buildAddressFieldIndex(rowsPayload);
5362:           districtNames = (idx && Array.isArray(idx.district_names)) ? idx.district_names : [];
5363:           prepareIndex(idx);        // build vocab/inverted/area-vocab + _ord (once)
5364:           searchIndex = idx;        // publish only AFTER fully prepared
5365:           return searchIndex;
5366:         } catch (err) {
5367:           searchDataPromise = null; // allow a later retry
5368:           throw err;
5369:         }
5370:       })();
5371:       return searchDataPromise;
5372:     }

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$a=Get-Content -LiteralPath '"'index.html' -Encoding UTF8; 5926..6070 | ForEach-Object { '{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 647ms:
5926:     const APPROX_ADDRESS_SEARCH_ENABLED = false;                // D5 flag OFF — feature dark pending B3 (clustered approx positions not yet distributed); Petar 2026-07-04. Code + v1.0.3 bundle stay; search falls back to exact-only ("Няма съвпадения")
5927:     const APPROX_ADDRESS_URL = 'data/approx_addresses_v1.json'; // D6 lazy bundle
5928:     const APPROX_CACHE = 'fire-varna-approx-addresses-v1';      // D6 own cache ns
5929:     const APPROX_FIELD_ORDER = ['street_name_bg', 'number', 'quarter', 'lat', 'lng', 'confidence', 'source'];
5930:     const APPROX_CONF_RANK = { high: 0, medium: 1, low: 2 };
5931:     const APPROX_SRC_RANK = { alias: 0, interp: 1, nearest: 2 };
5932:     const APPROX_STREET_TYPE_TOKENS = { ul: 1, bul: 1, pl: 1 };
5933:     // Varna WGS84 bbox — a coordinate outside it fails the on-load coords gate
5934:     // (matches the B1 emitter's validate_wgs bounds).
5935:     const APPROX_BBOX = { minLat: 43.00, maxLat: 43.45, minLng: 27.60, maxLng: 28.15 };
5936: 
5937:     let approxIndex = null;      // prepared approx index (memory cache)
5938:     let approxPromise = null;    // in-flight load (dedupes concurrent zero-exact)
5939:     let approxDisabled = false;  // a FATAL failure (bad schema/leak/coords) -> never retry
5940: 
5941:     // Fetch + Cache-API persist for the approx bundle (own namespace, offline fallback).
5942:     async function fetchApproxJson(url) {
5943:       try {
5944:         const resp = await fetch(url, { cache: 'no-cache' });
5945:         if (!resp.ok) throw new Error('HTTP ' + resp.status);
5946:         if (typeof caches !== 'undefined') {
5947:           try { const c = await caches.open(APPROX_CACHE); await c.put(url, resp.clone()); } catch (e) {}
5948:         }
5949:         return await resp.json();
5950:       } catch (netErr) {
5951:         if (typeof caches !== 'undefined') {
5952:           try { const c = await caches.open(APPROX_CACHE); const hit = await c.match(url); if (hit) return await hit.json(); } catch (e) {}
5953:         }
5954:         throw netErr;
5955:       }
5956:     }
5957:     function approxFatal(msg) { const e = new Error(msg); e.approxFatal = true; return e; }
5958: 
5959:     // Public street name -> match tokens: norm+skel, drop the leading УЛ./БУЛ./ПЛ.
5960:     // type token (mirrors the B0 search_entry projection), then append the number.
5961:     function approxStreetTokens(street) {
5962:       const toks = norm(street).split(/\s+/).filter(Boolean).map(skel).filter(Boolean);
5963:       while (toks.length && APPROX_STREET_TYPE_TOKENS[toks[0]]) toks.shift();
5964:       return toks;
5965:     }
5966:     function approxQuarterTokens(quarter) {
5967:       if (!quarter || quarter === 'unassigned') return [];
5968:       return norm(quarter).split(/\s+/).filter(Boolean).map(skel).filter(Boolean);
5969:     }
5970: 
5971:     // Validate the public bundle (schema + leaked-id + coords) and project each row
5972:     // to {kind:'approx', pin:[lat,lng], tk, qtk, street, number, quarter, conf, src,
5973:     // _ord}. Column positions come from field_order (never hardcoded). Throws
5974:     // approxFatal on a bad schema / leaked identifier -> the whole feature disables
5975:     // for the session (fallback to today). A single out-of-bbox / pin-less row is dropped.
5976:     function buildApproxIndex(payload) {
5977:       if (!payload || payload.kind !== 'fire_varna_approx_addresses_v1' ||
5978:           !Array.isArray(payload.field_order) || !Array.isArray(payload.rows)) {
5979:         throw approxFatal('approx bundle: bad schema');
5980:       }
5981:       const order = payload.field_order;
5982:       const col = {};
5983:       for (const name of APPROX_FIELD_ORDER) {
5984:         const i = order.indexOf(name);
5985:         if (i === -1) throw approxFatal('approx bundle: field_order missing ' + name);
5986:         col[name] = i;
5987:       }
5988:       const CAD = /\b10135\.\d+\.\d+(?:\.\d+)?\b/;   // a leaked cadnum -> disable
5989:       const entries = [];
5990:       for (let r = 0; r < payload.rows.length; r++) {
5991:         const row = payload.rows[r];
5992:         if (!Array.isArray(row)) throw approxFatal('approx bundle: row not an array');
5993:         const street = String(row[col.street_name_bg] == null ? '' : row[col.street_name_bg]);
5994:         const number = String(row[col.number] == null ? '' : row[col.number]);
5995:         const quarter = String(row[col.quarter] == null ? '' : row[col.quarter]);
5996:         const lat = Number(row[col.lat]);
5997:         const lng = Number(row[col.lng]);
5998:         if (CAD.test(street) || CAD.test(quarter)) throw approxFatal('approx bundle: leaked identifier');
5999:         if (!isFinite(lat) || !isFinite(lng)) continue;                      // no pin -> skip
6000:         if (lat < APPROX_BBOX.minLat || lat > APPROX_BBOX.maxLat ||
6001:             lng < APPROX_BBOX.minLng || lng > APPROX_BBOX.maxLng) continue;  // outside Varna -> skip
6002:         const tk = approxStreetTokens(street);
6003:         const nk = skel(number.toLowerCase());
6004:         if (nk) tk.push(nk);
6005:         entries.push({
6006:           kind: 'approx', pin: [lat, lng], tk: tk, qtk: approxQuarterTokens(quarter),
6007:           street: street, number: number, quarter: quarter,
6008:           conf: row[col.confidence], src: row[col.source], _ord: r,
6009:         });
6010:       }
6011:       // vocab + inverted index over tk+qtk (fast candidate lookup, like prepareIndex).
6012:       const vocabSet = new Set();
6013:       for (const e of entries) { for (const t of e.tk) vocabSet.add(t); for (const t of e.qtk) vocabSet.add(t); }
6014:       const vocab = Array.from(vocabSet).sort();
6015:       const inverted = {};
6016:       for (let i = 0; i < entries.length; i++) {
6017:         const e = entries[i];
6018:         const toks = e.qtk.length ? e.tk.concat(e.qtk) : e.tk;
6019:         for (const t of toks) { let ids = inverted[t]; if (!ids) inverted[t] = ids = []; if (ids[ids.length - 1] !== i) ids.push(i); }
6020:       }
6021:       return { entries: entries, vocab: vocab, inverted: inverted };
6022:     }
6023: 
6024:     async function ensureApproxData() {
6025:       if (!APPROX_ADDRESS_SEARCH_ENABLED || approxDisabled) return null;
6026:       if (approxIndex) return approxIndex;
6027:       if (approxPromise) return approxPromise;
6028:       approxPromise = (async function () {
6029:         try {
6030:           const payload = await fetchApproxJson(APPROX_ADDRESS_URL);
6031:           const idx = buildApproxIndex(payload);   // throws approxFatal on a bad file
6032:           approxIndex = idx;
6033:           return idx;
6034:         } catch (err) {
6035:           approxPromise = null;
6036:           if (err && err.approxFatal) approxDisabled = true; // bad file -> today's behaviour, no retry
6037:           return null;                                       // transient (network) -> retry next zero-exact
6038:         }
6039:       })();
6040:       return approxPromise;
6041:     }
6042: 
6043:     // Match an approx query: require EVERY query token to hit some tk/qtk token
6044:     // (approx is a fallback — keep it tight). Rank by match quality, then confidence,
6045:     // then source, then stable _ord (plan §Commit 3 ranking).
6046:     function runApproxSearch(query, aidx) {
6047:       if (!aidx || !Array.isArray(aidx.entries)) return [];
6048:       const qn = norm(query);
6049:       if (qn.length < 1) return [];
6050:       const toks = qn.split(/\s+/).filter(Boolean).map(skel).filter(Boolean);
6051:       if (!toks.length) return [];
6052:       const ms = toks.map(function (t) { return matchKindSet(t, aidx.vocab); });
6053:       const cand = new Set();
6054:       for (const m of ms) for (const vt in m) { const ids = aidx.inverted[vt]; if (ids) for (let i = 0; i < ids.length; i++) cand.add(ids[i]); }
6055:       const scored = [];
6056:       for (const id of cand) {
6057:         const e = aidx.entries[id];
6058:         let matched = 0, exact = 0, prefix = 0, fuzzy = 0, all = true;
6059:         for (let qi = 0; qi < toks.length; qi++) {
6060:           const m = ms[qi]; let best = 0;
6061:           for (let ti = 0; ti < e.tk.length; ti++) { const k = m[e.tk[ti]] || 0; if (k > best) { best = k; if (best === 3) break; } }
6062:           if (best < 3 && e.qtk.length) { for (let ti = 0; ti < e.qtk.length; ti++) { const k = m[e.qtk[ti]] || 0; if (k > best) { best = k; if (best === 3) break; } } }
6063:           if (best === 0) { all = false; break; }
6064:           matched += 1;
6065:           if (best === 3) exact += 1; else if (best === 2) prefix += 1; else fuzzy += 1;
6066:         }
6067:         if (all && matched > 0) scored.push({ e: e, matched: matched, exact: exact, prefix: prefix, fuzzy: fuzzy });
6068:       }
6069:       scored.sort(function (a, b) {
6070:         if (b.matched !== a.matched) return b.matched - a.matched;

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'),vm=require('vm');
const h=fs.readFileSync('index.html','utf8');
const slice=(a,b)=>h.slice(h.indexOf(a),h.indexOf(b));
let s=slice('    function norm(s)','    // ---- display payload')+slice('    const SEARCH_LIMIT = 8;','    // ---- lazy load + cache');
s=s.replace(\"['tk','qtk','alias_tk','dtk','stk']\",\"['tk','qtk','alias_tk','dtk','stk','wtk','otk']\");
s=s.replace('if (e.stk) toks = toks.concat(e.stk);','if (e.stk) toks = toks.concat(e.stk); if(e.wtk)toks=toks.concat(e.wtk); if(e.otk)toks=toks.concat(e.otk);');
s=s.replace('index._areaVocab = av;',\"index._areaVocab = av; index._signedQuarterVocab = new Set((index.quarter_names||[]).flatMap(n=>norm(n).split(/\\\\s+/).map(skel).filter(t=>t.length>2&&"'!/''^'"\\\\d+"'$/.test(t))));");
s=s.replace('"'let matched = 0, exactName', 'let matchedViaWitness=0, matchedViaOtkOnly=0; let matched = 0, exactName');
s=s.replace('if (best === 0) { all = false; continue; }',"'`if(e.wtk && best<3 && !(index._signedQuarterVocab.has(toks[qi]) && e.q!=null)){ let prior=best; for(const t of e.wtk)best=Math.max(best,m[t]||0); if(best>prior)matchedViaWitness++; } if(e.otk && best<3){let prior=best; for(const t of e.otk)best=Math.max(best,m[t]||0); if(best>prior)matchedViaOtkOnly++;} if (best === 0) { all = false; continue; }`);
s=s.replace('"'const dem = e.quarter_assignment_trust', 'const wdem=matchedViaWitness>0&&matchedCore===0?1:0, otdem=matchedViaOtkOnly>0?1:0; const dem = e.quarter_assignment_trust');
s=s.replace('scored.push({ e: e,','scored.push({ wdem, otdem, matchedCore, matchedViaWitness, e: e,');
s=s.replace('if (a.odem "'!== b.odem) return a.odem - b.odem;'"', 'if(a.wdem"'!==b.wdem)return a.wdem-b.wdem; if(a.otdem!==b.otdem)return a.otdem-b.otdem; if (a.odem !== b.odem) return a.odem - b.odem;'"');
s=s.replace('const existsBtkHolder =', 'globalThis.probeScored=scored; const existsBtkHolder =');
const ctx={};vm.createContext(ctx);vm.runInContext(s,ctx);
const idx=JSON.parse(fs.readFileSync('data/search_index.json','utf8'));
const flag=idx.entries.find(e=>e.kind==='mf'&&e.pin[0]===43.22212&&e.pin[1]===27.9378);
const canon={...flag,q:0,qtk:['levski'],wtk:['chaika']};
for(const query of ['chaika studentska bl 11','chai studentska bl 11','levski bl 11']){
 const rows=query.startsWith('levski')?[{...flag,qtk:[],wtk:['levski'],g:'witness'}, {...flag,q:0,qtk:['levski'],g:'canon'}]:[canon];
 const test={entries:rows,quarter_names:['levski','chaika']};ctx.prepareIndex(test);const out=ctx.runGeocoderSearch(query,test);
 console.log(JSON.stringify({query,out:out.map(r=>({g:r.g,all:r.allTokens})),scored:ctx.probeScored.map(r=>({g:r.e.g,all:r.all,matchedCore:r.matchedCore,witness:r.matchedViaWitness,wdem:r.wdem}))}));
}
const p=JSON.parse(fs.readFileSync('data/address_rows.json','utf8')); const mutated=structuredClone(p);mutated.rows.reverse();
console.log(JSON.stringify({sameCountGenerationPoison:{original:p.rows.length,reversed:mutated.rows.length,sameFirst:JSON.stringify(p.rows[0])===JSON.stringify(mutated.rows[0]),declaredClientCountCheck:idx.address_row_count===mutated.rows.length}}));
'@ | node" in C:\git\Fire_Varna
 succeeded in 676ms:
{"query":"chaika studentska bl 11","out":[{"g":"b6797e83ec13fe798","all":false}],"scored":[{"g":"b6797e83ec13fe798","all":false,"matchedCore":3,"witness":0,"wdem":0}]}
{"query":"chai studentska bl 11","out":[{"g":"b6797e83ec13fe798","all":true}],"scored":[{"g":"b6797e83ec13fe798","all":true,"matchedCore":3,"witness":1,"wdem":0}]}
{"query":"levski bl 11","out":[{"g":"witness","all":true},{"g":"canon","all":true}],"scored":[{"g":"witness","all":true,"matchedCore":2,"witness":1,"wdem":0},{"g":"canon","all":true,"matchedCore":2,"witness":0,"wdem":0}]}
{"sameCountGenerationPoison":{"original":80510,"reversed":80510,"sameFirst":false,"declaredClientCountCheck":true}}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'docs/plans/ПЛАН_Адресите_по_полигон_08.09.md'; "'$a=Get-Content -LiteralPath $p -Encoding UTF8; 252..300 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }; 156..189 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }; 439..482 | ForEach-Object { '"'{0}: {1}' -f "'$_,$a[$_-1] }' in C:\git\Fire_Varna
 succeeded in 597ms:
252: ## 4 · Write-set по репа
253: 
254: ### 4.1 `C:/git/Varna_buildings` (Executor комитва)
255: 
256: **НОВ · `tools/build_signed_quarter_index.py`** — Python пре-стъпка (прецедент `tools/build_quarname_enclosures.py`).
257: - Вход: блобът на полигоните, прочетен **в Python** (`git cat-file blob <OID>`, никакви пренасочвания) + `config/quarter_registry.json` само за четене.
258: - Проверява `OID` и sha256 срещу пиновете от М0.1/М0.2 → несъответствие = throw, нищо не се пише.
259: - EPSG:4326 → 32635; за всеки полигон: външен пръстен, `band_m = max(50, precision_m)`, bbox; **изчислява и таблица „кой полигон е конкурент на кого“ само за ЛЕДЖЕРА** (никога за публичния изход).
260: - Изход: `output/signed_quarters_baked.json` (частен) + `output/signed_quarters_baked_schema.json` (tracked по изключението `!output/*_schema.json`).
261: - Забрана: нищо извън `output/` (образец `_assert_private_out`, `tools/build_number_pins.py:883-896`).
262: 
263: **НОВ · `js/lib_signed_quarters.mjs`** — резолверът (НЕ в `lib_quarter_registry.mjs` — Д10, `js/test_quarter_registry.mjs:189-200`).
264: - `loadSignedQuarters(path)` — сверява `source_oid`/`source_sha256` с пинатите константи, проверява 60 полигона и `band_policy`, иначе throw с инструкция (образец `loadVinitsaZone`, `:158-186`).
265: - `resolveQuarter(model, pin)` → `{code, display, tokens, verdict, band_m, d_edge_own, nearest_other}`; `verdict ∈ inside_clear | inside_band | overlap_child | overlap_unproven | overlap_incomparable | outside_near_one | outside`.
266: - Правилата по подписания Р5/Р5-д; **`d_edge_own` и `nearest_other` се връщат САМО за леджера и никога не влизат в `o`.**
267: - `overlap_child` изисква геометрично доказано `дете ⊆ родител` в буфера (ADR 010 D8); недоказан parent → `overlap_unproven`.
268: - **Никакъв fallback по най-близък полигон — забранено на ниво код и на ниво тест.**
269: - `tokens` по Р16.
270: 
271: **НОВ · `js/lib_block_orientation.mjs`** — ориентирът (B): собствена улица по Р10, най-близка ≤ R по Р11 с филтъра на Р11-б, втора степен и разстояние по Р9-б, затворен списък причини.
272: 
273: **НОВ · `js/test_signed_quarter_resolver.mjs`** (G-A3) · **НОВ · `js/test_block_orientation.mjs`** (G-A6) · **НОВ · `js/test_quarter_ledger.mjs`** (G-A5) · **НОВ · `js/test_fire_varna_determinism.mjs`** (G-A8).
274: 
275: **ПРОМЯНА · `js/build_fire_varna_search_index.mjs`**
276: 1. `main()`: зарежда `SIGNED_QUARTERS` + `ORIENTATION_MODEL` до `loadVinitsaZone`.
277: 2. Pass 2, **`:701`**: `o.qtk` вече не се преписва от геокодера. Ново:
278:  - `const sq = resolveQuarter(SIGNED_QUARTERS, o.pin);`
279:  - `o.qtk = sq.tokens` и `o.q = quarterNameIndex(sq.display)` **само** при присъда с канон;
280:  - **`o.wtk = написаните токени МИНУС `o.qtk`** (Р14-а); празен масив не се пише;
281:  - `o.otk` = токените на ориентира (собствена улица НЕ дублира `tk`; чуждата влиза само тук), `o.o` = индекс в `orientations[]`.
282: 3. **`:743` C2 и `:826-842` F3 не се пипат**; `label` вече не носи квартален сегмент (т. 5) и не носи улица (Р9-в) → рискът `token_inconsistent` не расте; броячът `c2ResByReason` се сравнява преди/след (G-A9).
283: 4. **`:873-922` Р38** се обвива в `if (!sq.hasCanon)`; добавеният токен отива в `wtk`.
284: 5. `stripQuarterSegment(label)` — само първият сегмент, само при `looksLikeQuarterSegment` (образец `lib_quarter_registry.mjs:220-229`); прилага се СЛЕД регистъра (`:857-871`), преди push.
285: 6. **Материализация на `label`** за подписаното подмножество по Р12-б (2 775 + евентуално 11 627) — само там, само с изчистения текст, с ледгер ред за всеки.
286: 7. Нови топ-ключове `quarter_names` (≤ 60) и `orientations` (сортиран, дедупликиран); `index_schema_version` `"2.0"` → **`"3.0"`**.
287: 8. `vocab` (`:956-965`) се разширява с `wtk` и `otk`.
288: 9. Нов частен изход `output/quarter_polygon_ledger.json`: старо име + **`source` (kais/osm) + `mode` + `confidence` + `distance_m` на написания свидетел**, ново име, присъда, `d_edge_own`, `nearest_other`, ориентир + причина, `complex_id`.
289: 10. Отчетът (`:1071-1159`) получава броячи по присъда, по клас на несъгласие, по причина за ориентира, `blockGroups/collisionPairs/disambiguated` и `c2ResByReason` **преди и след**.
290: 11. Забрана: `d_edge_own`, `nearest_other`, `competitors` не влизат в `o` при никакви обстоятелства.
291: 
292: **ПРОМЯНА · `js/lib_fire_varna_block_labels.mjs`** — Pass A `:168` остава свидетел; Pass B `:183` базата става `бл. ${rec.n}`; **Pass C `:191-199` спира да лепи улица** (Р9-в), само маркира `must_disambiguate`; нови stats `orientationOwn/Nearest/None/Rejected/collisionUnresolved`.
293: 
294: **ПРОМЯНА · `js/test_fire_varna_publish_gate.mjs`**
295: - `ALLOWED_ENTRY_KEYS` (`:56-59`) += `"q"`, `"wtk"`, `"otk"`, `"o"`; `TOKEN_FIELDS` (`:110`) += `"wtk"`, `"otk"`.
296: - **Затворен набор ТОП-ключове** (днес топ-нивото е отворено, `:128-147`) + забранени имена `dist_edge_m`, `edge_m`, `poly`, `ring`, `geometry`, `coordinates`, `geometries` навсякъде в документа.
297: - `quarter_names` / `orientations`: масиви от низове, без mojibake/каднум/цифрова серия ≥ 5; `q` и `o` — цели числа в обхват; **всеки `qtk` токен ∈ речника от `quarter_names`**; `wtk ∩ qtk = ∅`.
298: - **НОВ вход: `output/signed_quarters_baked.json`** — гейтът сам преизчислява присъдата за **всеки** запис с `q` и пада при разминаване (това е G-A4; без този вход фикстурата „`qtk:["chaika"]` при пин в Левски“ е зелена, защото „chaika“ Е валидно канонично име).
299: - Отровени фикстури, всяка задължително падаща: (ф1) `coordinates` в НОВ топ-ключ; (ф2) `q` извън обхвата; (ф3) `qtk` с неканоничен токен; (ф4) `wtk ∩ qtk ≠ ∅`; (ф5) `quarter_names` с не-низ; (ф6) **запис с `q` = Чайка при пин вътре в кв. Левски**; (ф7) `o` без съответен ред в `orientations`.
300: 
156: ## 3 · Решения за Петър преди билда
157: 
158: > Всяко решение = един ред за подпис. Без подпис по Р0–Р18 билдът не тръгва.
159: 
160: **Р0 · Управленското разрешение (НОВО, блокиращо).** ADR 006 D12 (**Accepted**) изброява поименно `data/search_index.json`, `data/address_rows.json`, `sw.js` и **„every function of `initAddressSearch`“** като недосегаеми, а гейтът му е „адресният корпус е байт-идентичен“ (`006:157-163`). ADR 007, който вдига това, е **Proposed — awaiting Petar** (`007:3`) и при това пинова изрично **„the scorer and comparator“** (`007:15`) — точно каквото този лот пипа.
161: *Препоръка:* **подпиши ADR 007 И подпиши разширението му** (нов ADR 064, §4.1), което: (а) вдига 006 D12 за изброения адресен write-set; (б) **разпинова `scoreEntry` и компаратора** за назованите редове; (в) обявява, че G3 престава да е байтова равнопоставеност и се заменя с диференциален address replay; (г) **не** вдига `sw.js` и **не** вдига съдържанието на `address_rows.json`.
162: 
163: **Р0-б · Kill switch `ADDRESS_PATH_V2`.** ADR 007 D4 иска селектор на всеки use site, никога ранен `return`.
164: *Препоръка:* **да** — селектор около четирите нови места в клиента (`quarterPrefix`, `orientationSuffix`, гарда на свидетеля, `otk` клона). Цена: ~20 реда и двойна фикстура в replay-а (флаг вкл./изкл.).
165: 
166: **Р1 · Дупката „Център“** (753 mf извън всички + част от 8 810-те без дума).
167: *Препоръка:* неопределено; „район Одесос/Приморски“ по измерения `d`; свидетелят остава търсим; ред в борда „Център иска подписан полигон“. **Не разширяваме полигон.**
168: 
169: **Р2 · „Цветен квартал“** (няма полигон, няма запис в регистъра; 197 извън + 318 несъгласия към кв. Левски + 9 към Изгрев).
170: *Препоръка:* координатата решава — 318-те стават „кв. Левски“ (при Р5 (в)/(г); при (а)/(б) част от тях падат в лентата и остават неопределени — числото идва от М0.5); „цветен квартал“ остава свидетел; 197-те извън — по Р5-д.
171: 
172: **Р3 · „Колхозен пазар“** (490 извън + 245 несъгласия към кв. Тракия).
173: *Препоръка:* същото правило като Р2.
174: 
175: **Р4 · Флагманът Левски–Чайка при Студентска.** Измерено: пинът е ВЪТРЕ в кв. Левски на 67,4 m при `precision_m = 100`, конкурентът Бриз е на 82,8 m.
176: *Препоръка:* **„кв. Левски“ канон, „Чайка“ свидетел** — изпълнимо САМО при Р5 (в) или (г). При (а) и (б) този запис остава без квартал и **лотът не решава жалбата ти** — това е записано тук, на първа страница, не на осма.
177: 
178: **Р5 · Лентата — четири варианта с измерените цени** (числата се финализират от М0.5; днешните оценки в скоби):
179: 
180: | вариант | правило | губят име | флагманът |
181: |---|---|---:|---|
182: | (а) строга | всичко в собствената лента → неопределено | ~25 613 | ✗ |
183: | (б) конкурентна (v1 Р5в) | неопределено само при конкурент в лентата | ~11 6xx | ✗ |
184: | **(в) съдържанието решава (препоръка)** | пинът е в точно един полигон → името се дава; лентата се записва само в леджера | 0 | ✓ |
185: | (г) по-близкият конкурент | неопределено само ако чужд ръб е ПО-БЛИЗО от собствения | подмножество на (б) | ✓ (Бриз 82,8 > 67,4) |
186: 
187: *Довод за (в):* неопределеността не може да стане чуждо име; чужд полигон, който НЕ съдържа точката, не може да я спечели. *Честната цена:* при (в) грешка е възможна за записите на ≤ band от ръба (~25 613) — тя се лови от леджера и от извадката на Петър, не от гейт. Ако искаш нула такъв риск → (а), но тогава подпиши изрично, че флагманът остава без квартал.
188: **Прагът „15 %“ от v1 отпада** — той не е решение, а тавтология (§12).
189: 
439: ## 7 · STOP — спри и питай Петър
440: 
441: 1. М0.1/М0.3/М0.4/М0.5 дават числа, различни от §1.А.
442: 2. **М0.5-б показва за флагмана присъда, различна от подписаната по Р4/Р5** (тогава лотът не решава жалбата и това се казва веднага).
443: 3. **М0.6 се разминава с §1.А** (385 ↔ 91 ↔ 95; 24 ↔ 16; 1 324 ↔ 213).
444: 4. Който и да е гейт е червен и поправката не е очевидно безопасна.
445: 5. Билдът иска промяна в `config/quarter_registry.json`.
446: 6. Блоковите колизии след смяната се променят с > 20 % спрямо М0.7.
447: 7. `c2ResByReason.token_inconsistent` расте над подписания таван (ориентирът яде етикети).
448: 8. S9 `tokenInconsistentTotal` мърда с > 20 % спрямо 5 828.
449: 9. Сборът на двата lazy payload-а мине подписания таван (Р12-в).
450: 10. Резолверът иска ново публично поле извън `q`, `wtk`, `otk`, `o`.
451: 11. Появи се нужда да се пипне `data/address_rows.json`, `sw.js` или approx пакетът.
452: 12. Втора опашка `ЗА_ПОДПИС_*` в HEAD или втори json в `gates/allow/`.
453: 13. Някой ход изисква публикуване, remote достъп или `--no-verify`.
454: 14. **`git diff --cached` не е празен преди F1 или преди `gates.sign`** (смесени поколения / чужди хънкове в адресния комит).
455: 15. Пожелано е име за точка, която резолверът е обявил за неопределена („нека все пак сложим нещо“).
456: 
457: ---
458: 
459: ## 8 · Локален преглед (проби с очакван резултат)
460: 
461: `python -m http.server 8000`, 375 px, ръчно, преди Gate 2:
462: 
463: | # | Заявка | Очаквано |
464: |---|---|---|
465: | 1 | `бл 11 левски` | само блокове с пин в полигона кв. Левски **плюс** блокът на бул. Царевец (Р5-д, без квартална дума, демотиран); **всеки ред носи различен ориентир**; групата „N блока № 11“ брои каноничните |
466: | 2 | `студентска бл 11` | ред 1 = **кв. Левски, бл. 11, ул. Студентска** (Р10-а) или **…, до ул. Студентска** (Р10-б) — точно подписаният низ; „Чайка“ не се появява в заглавието; **рендерът остава в обикновения списък, не в груповия блоков клон** |
467: | 3 | `чайка студентска бл 11` | блокът **НЕ е пълно съвпадение** (`all=false`); ако излезе, е под редовете с истинска Чайка |
468: | 4 | `бл 11 чайка` | само блокове в полигоните к.к./кв. Чайка; Студентска бл. 11 не е сред тях |
469: | 5 | `левски битоля 13` | без квартална дума, вторият ред е **„район Приморски“**; „левски“ не дава пълно съвпадение |
470: | 6 | `цветен квартал битоля` | намира (свидетелят работи), нито един ред не показва „Цветен квартал“ като квартал |
471: | 7 | `бреза 6` | заглавие **кв. Левски**, свидетелят остава търсим |
472: | 8 | `манастирски рид` / `акчелар` / `ален мак` / `бриз` | фините подписани квартали, не „кв. Виница“ |
473: | 9 | `дълбокото дере` | продължава да намира (Р38 „добавя, никога не реже“) |
474: | 10 | `27 юли 22` · `алеко константинов 10` | Център (ако вътре) · кв. Тракия |
475: | 11 | **ред по display_id пътя** (напр. `константин и фружин бл 302`) | заглавието носи квартала И ориентира; при материализация (Р12-б) няма „ж.к. Бриз, акчелар“ |
476: | 12 | `дружба бл 11` / ТВ кула | по подписания Р5; редът не изчезва |
477: | 13 | `ADDRESS_PATH_V2 = false` | поведението е базовото; нито един нов низ не се показва |
478: | 14 | празна проверка | конзолата без грешки; `data/search_index.json` 200; картата под 3 s; трите режима; PLACES взима Enter само при `'Няма съвпадения'` |
479: | 15 | смяна на поколението | при подменен `address_rows` клиентът **отказва** доставката (fail-closed); стар кеш v2 не се сервира на страницата |
480: 
481: ---
482: 

codex
Пробата в паметта потвърди два дефекта: свидетелският ред за „левски бл 11“ получава `wdem=0` и може да изпревари каноничния; „чай студентска бл 11“ заобикаля гарда за „Чайка“. Разместване на 80 510 адресни реда също запазва броя им и минава описаната клиентска проверка, въпреки счупените `display_id` връзки.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json,hashlib,collections,pathlib
for name in ('search_index.json','address_rows.json'):
 p=pathlib.Path('data')/name;b=p.read_bytes();x=json.loads(b)
 print(name, 'bytes',len(b),'sha256',hashlib.sha256(b).hexdigest(),'keys',list(x))
 if 'entries' in x:
  e=x['entries'];print('entries',len(e),'kinds',dict(collections.Counter(r['kind'] for r in e)))
  print('label_only',sum('label'in r and 'display_id'not in r for r in e),'display_only',sum('display_id'in r and 'label'not in r for r in e),'both',sum('label'in r and 'display_id'in r for r in e),'btk_no_label',sum('btk'in r and 'label'not in r for r in e),'qtk_entries',sum('qtk'in r for r in e),'district_names',x.get('district_names'))
 else: print('rows',len(x['rows']),'field_order',x.get('field_order'))
'@ | python -B -" in C:\git\Fire_Varna
 exited 1 in 789ms:
search_index.json bytes 11242756 sha256 c12f94259bd986dd8b874f4866a0e9e311ada713e49ff4d67afcd58d48467b0d keys ['index_schema_version', 'kind', 'coordinate_order', 'district_names', 'address_row_count', 'entries', 'vocab']
entries 86232 kinds {'address': 70575, 'mf': 14687, 'parcel': 970}
label_only 42937 display_only 43099 both 196 btk_no_label 205 qtk_entries 19494 district_names Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "C:\Program Files\Python310\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode characters in position 2-11: character maps to <undefined>

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
const fs=require('fs'),vm=require('vm');const h=fs.readFileSync('index.html','utf8'); const p=JSON.parse(fs.readFileSync('data/address_rows.json','utf8')); console.log(JSON.stringify({addressRows:p.rows.length,bytes:fs.statSync('data/address_rows.json').size,fields:p.field_order}));let s=h.slice(h.indexOf('    function norm(s)'),h.indexOf('    // ---- display payload'))+h.slice(h.indexOf('    const SEARCH_LIMIT = 8;'),h.indexOf('    // ---- lazy load + cache'));const c={};vm.createContext(c);vm.runInContext(s,c);let i={entries:[{kind:'mf',pin:[43.2,27.9],tk:['bl','11'],qtk:['mladost','mladost 1'],btk:['11'],g:'m1'}]};c.prepareIndex(i);console.log(JSON.stringify({r16:c.runGeocoderSearch('mladost 1 bl 11',i),areaVocab:Array.from(i._areaVocab)}));
'@ | node" in C:\git\Fire_Varna
 succeeded in 563ms:
{"addressRows":80510,"bytes":5073137,"fields":["normalized_address","lat","lng"]}
{"r16":[{"kind":"mf","pin":[43.2,27.9],"g":"m1","allTokens":false,"matched":3,"exact":3,"prefix":0,"fuzzy":0}],"areaVocab":["mladost","mladost 1"]}

codex
Има и доказана пролука в структурния гейт: `coordinate_order: {dist_to_edge_m: 67.4}` минава описаните проверки. Редът за подписване също пропуска JSON артефактите, които `gates.sign` променя, а наличният freeze за местата би изтрил новата секция `address_replay`. Присъдата е НЕГОДНО; оформям точните поправки.
codex
**НЕГОДНО за подпис.**

База: `f745349`, Б3 още е стейджнат. Потвърдени: 86 232 записа; 43 099 само по `display_id`; 205 блокови записа без `label`. Пробите използват реалния matcher с описаните изменения **в паметта**. Нищо не е променено.

По-долу **П** означава [плана](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md).

- **S32-1 — Неизпълним scope/API.** [П:276](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:276) поставя моделите в `main()` „до loadVinitsaZone“, но той е в `buildPublicIndex()` — [генератор:671](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:671). Договорът `:265` няма използвания в `:283` `hasCanon`; `!undefined` допуска Р38 навсякъде. **Поправка:** зареждане в правилния scope или явни аргументи; единен булев `hasCanon`.

- **S32-2 — Свидетелят не се демотира.** Формулата [П:316](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:316) изисква `matchedCore===0`. При „левски бл 11“ измерих `matchedCore=2, wdem=0`; свидетелят изпреварва каноничния през по-късия `tk+qtk`. **Поправка:** демотиране при съвпадение само през свидетеля, независимо от останалите core токени; отрицателна фикстура за реда и груповия брояч.

- **S32-3 — Несъвместима токенизация.** Гардът [П:314](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:314) проверява точно `.has()`, matcher-ът допуска префикси: „чай студентска бл 11“ дава `all=true`, докато „чайка…“ е `false`. Р16 също се чупи: `qtk=["mladost","mladost 1"]`, заявка „младост 1 бл 11“ → `all=false`. **Поправка:** общ договор за квартални фрази, префикси и числови суфикси; отделни фикстури.

- **S32-4 — Kill switch не възстановява базата.** [П:164](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:164) изключва четири клиентски места, но генераторът вече е премахнал стария квартален текст и заменил `qtk`. **Поправка:** запазена базова проекция/доставка за изключения флаг или отпадане на обещанието за базово поведение в G-B4.

- **S32-5 — G-A6б използва старите колизии.** [П:292](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:292) оставя ключовете по свидетелския `c.quarter` — [блоков генератор:188](C:/git/Varna_buildings/js/lib_fire_varna_block_labels.mjs:188). **Поправка:** колизии по крайни `(q, block_number)` и различни `g`; същите идентичности за ориентира, гейта и подписания остатък.

- **S32-6 — Геометричният гейт пропуска забраненото разстояние.** Отровата `coordinate_order:{dist_to_edge_m:67.4}` даде **нула нарушения** при описаните проверки. [П:296](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:296) забранява друго име — `dist_edge_m`; съществуващият ключ е нетипизиран. **Поправка:** затворена типизирана схема навсякъде, точните забранени ключове; отрицателната фикстура да пада по изтичането, не само по непознат топ-ключ.

- **S32-7 — G-A4 допуска празно доказателство.** [П:297–298](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:297) проверява само наличните `q`, а `qtk` — срещу общия речник. Премахнати `q/qtk` или правилно `q=Левски` с `qtk=["chaika"]` не са изключени. **Поправка:** за всеки запис точно сравнение на наличието, стойността и токените с очаквания канон.

- **S32-8 — G-B5 не доказва поколение.** [П:323](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:323) проверява само схема, индекси и брой. Обърнати 80 510 адресни реда запазват броя и минават, но повреждат `display_id`. **Поправка:** клиентска проверка на digest на адресния payload, пиннат в индекса; фикстура със същия брой.

- **S32-9 — Replay/freeze не е свързан с release.** [recall_sweep.py:3774](C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:3774) създава нов `expectations` без `address_replay`; следващ places freeze го изтрива. Release няма адресни candidate/reference котви. **Поправка:** добавяне на двата файла към write-set, запазване на секцията, подписани digest връзки и cross-freeze отрицателен тест. Селекторът трябва да фиксира конкретните N и идентичности.

- **S32-10 — Командният ред остава противоречив.** [П:396](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:396) стейджва само опашката, въпреки че `gates.sign` променя и артефакти. Липсва places freeze. F1 комитва cache-v3 отделно от изисквания общ payload комит. **Поправка:** комит на всички изведени подписани пътища; двата freeze-а с отделни комити; cache превключването в човешкия комит с данните.

- **S32-11 — G-A1 атакува грешния етап.** [П:415](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:415) може просто да презапише отровения baked файл; loader-ът проверява декларирания произход. **Поправка:** проверка на самото baked съдържание спрямо пиннатия извор и отрова срещу loader-а. За G-A8 уточни два независими процеса/директории и сравнение на трите артефакта.

- **S32-12 — Непадащи отрицателни половини.** G-B6 чете само hotels/places — [тест:94](C:/git/Fire_Varna/tests/test_b3_gates.py:94); адресната отрова остава невидима. Самотно `Ð` в G-B7 не съвпада с заявения regex. **Поправка:** адресен renderer тест за двата дисплея; отделни отрови `\u00D0\u0090` и U+FFFD.

- **S32-13 — М0 е кръгов и непълен.** [П:111](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:111) иска билд с новите полета „преди първия код“. **Поправка:** отделни baseline и разрешена прототипна мярка; изпълними команди, дефиниции запис/група и окончателни подове/тавани/остатъци преди подпис.

OID/байтовият пин, PowerShell ограниченията и Б3-пръв са поправени. За останалите G-A проверки не установих допълнителен конкретен дефект.
tokens used
89,130
**НЕГОДНО за подпис.**

База: `f745349`, Б3 още е стейджнат. Потвърдени: 86 232 записа; 43 099 само по `display_id`; 205 блокови записа без `label`. Пробите използват реалния matcher с описаните изменения **в паметта**. Нищо не е променено.

По-долу **П** означава [плана](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md).

- **S32-1 — Неизпълним scope/API.** [П:276](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:276) поставя моделите в `main()` „до loadVinitsaZone“, но той е в `buildPublicIndex()` — [генератор:671](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:671). Договорът `:265` няма използвания в `:283` `hasCanon`; `!undefined` допуска Р38 навсякъде. **Поправка:** зареждане в правилния scope или явни аргументи; единен булев `hasCanon`.

- **S32-2 — Свидетелят не се демотира.** Формулата [П:316](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:316) изисква `matchedCore===0`. При „левски бл 11“ измерих `matchedCore=2, wdem=0`; свидетелят изпреварва каноничния през по-късия `tk+qtk`. **Поправка:** демотиране при съвпадение само през свидетеля, независимо от останалите core токени; отрицателна фикстура за реда и груповия брояч.

- **S32-3 — Несъвместима токенизация.** Гардът [П:314](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:314) проверява точно `.has()`, matcher-ът допуска префикси: „чай студентска бл 11“ дава `all=true`, докато „чайка…“ е `false`. Р16 също се чупи: `qtk=["mladost","mladost 1"]`, заявка „младост 1 бл 11“ → `all=false`. **Поправка:** общ договор за квартални фрази, префикси и числови суфикси; отделни фикстури.

- **S32-4 — Kill switch не възстановява базата.** [П:164](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:164) изключва четири клиентски места, но генераторът вече е премахнал стария квартален текст и заменил `qtk`. **Поправка:** запазена базова проекция/доставка за изключения флаг или отпадане на обещанието за базово поведение в G-B4.

- **S32-5 — G-A6б използва старите колизии.** [П:292](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:292) оставя ключовете по свидетелския `c.quarter` — [блоков генератор:188](C:/git/Varna_buildings/js/lib_fire_varna_block_labels.mjs:188). **Поправка:** колизии по крайни `(q, block_number)` и различни `g`; същите идентичности за ориентира, гейта и подписания остатък.

- **S32-6 — Геометричният гейт пропуска забраненото разстояние.** Отровата `coordinate_order:{dist_to_edge_m:67.4}` даде **нула нарушения** при описаните проверки. [П:296](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:296) забранява друго име — `dist_edge_m`; съществуващият ключ е нетипизиран. **Поправка:** затворена типизирана схема навсякъде, точните забранени ключове; отрицателната фикстура да пада по изтичането, не само по непознат топ-ключ.

- **S32-7 — G-A4 допуска празно доказателство.** [П:297–298](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:297) проверява само наличните `q`, а `qtk` — срещу общия речник. Премахнати `q/qtk` или правилно `q=Левски` с `qtk=["chaika"]` не са изключени. **Поправка:** за всеки запис точно сравнение на наличието, стойността и токените с очаквания канон.

- **S32-8 — G-B5 не доказва поколение.** [П:323](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:323) проверява само схема, индекси и брой. Обърнати 80 510 адресни реда запазват броя и минават, но повреждат `display_id`. **Поправка:** клиентска проверка на digest на адресния payload, пиннат в индекса; фикстура със същия брой.

- **S32-9 — Replay/freeze не е свързан с release.** [recall_sweep.py:3774](C:/git/Fire_Varna/scratch/places_search/recall_sweep.py:3774) създава нов `expectations` без `address_replay`; следващ places freeze го изтрива. Release няма адресни candidate/reference котви. **Поправка:** добавяне на двата файла към write-set, запазване на секцията, подписани digest връзки и cross-freeze отрицателен тест. Селекторът трябва да фиксира конкретните N и идентичности.

- **S32-10 — Командният ред остава противоречив.** [П:396](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:396) стейджва само опашката, въпреки че `gates.sign` променя и артефакти. Липсва places freeze. F1 комитва cache-v3 отделно от изисквания общ payload комит. **Поправка:** комит на всички изведени подписани пътища; двата freeze-а с отделни комити; cache превключването в човешкия комит с данните.

- **S32-11 — G-A1 атакува грешния етап.** [П:415](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:415) може просто да презапише отровения baked файл; loader-ът проверява декларирания произход. **Поправка:** проверка на самото baked съдържание спрямо пиннатия извор и отрова срещу loader-а. За G-A8 уточни два независими процеса/директории и сравнение на трите артефакта.

- **S32-12 — Непадащи отрицателни половини.** G-B6 чете само hotels/places — [тест:94](C:/git/Fire_Varna/tests/test_b3_gates.py:94); адресната отрова остава невидима. Самотно `Ð` в G-B7 не съвпада с заявения regex. **Поправка:** адресен renderer тест за двата дисплея; отделни отрови `\u00D0\u0090` и U+FFFD.

- **S32-13 — М0 е кръгов и непълен.** [П:111](C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md:111) иска билд с новите полета „преди първия код“. **Поправка:** отделни baseline и разрешена прототипна мярка; изпълними команди, дефиниции запис/група и окончателни подове/тавани/остатъци преди подпис.

OID/байтовият пин, PowerShell ограниченията и Б3-пръв са поправени. За останалите G-A проверки не установих допълнителен конкретен дефект.
