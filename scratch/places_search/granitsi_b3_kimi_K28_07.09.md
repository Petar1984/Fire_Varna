kimi version 0.34.0
• This is a read-only analysis task in Bulgarian. I need to analyze the plan ПЛАН_Б3_07.09.md against measurements on new_data/. Let me read the files first.

  The working directory is C:\Users\Petar\AppData\Local\Temp\tmp.kxXpAqZNoi, but I should cite paths relative to the kimi_b3 root (the copy). So the files here correspond to that root.

  Let me read the key files: ПЛАН_Б3_07.09.md, the signed base files, ADR 010, and measure new_data/.

  Let me start reading.

• Ще започна с четене на плана v2 и подписаната основа.

• The plan file is large (632 lines, ~97KB). I need to read it fully. Let me page through the saved output. The preview showed lines 1-18 roughly. Let me read from the output_path.

  Also need: ПЛАН_НОЩНА_СМЯНА §0/§2а/§Б3 lines 143-145, амандамент 3, СЪСТОЯНИЕ §4 §6-§8. And measurements on new_data/.

  Let me read the full plan file via the output path.Now I have the plan v2. Next: read the signed base documents to check citations (ПЛАН_НОЩНА_СМЯНА §Б3 lines 143-145, амандамент 3, СЪСТОЯНИЕ §4 решения 8/9, §6-§8). And measure new_data/.

  Let me read the other docs first.

• Планът е прочетен. Сега чета подписаната основа и амандементите.

• Now read ПЛАН_НОЩНА_СМЯНА §0/§2а/§Б3 (lines ~143-145) to check citations. And the other plan file. Then do measurements on new_data/.

  Let me read the signed plan file (probably big). Let me check its size and read relevant sections.

• Сега чета подписания нощен план — ключовите редове §0/§2а/§Б3.    163 ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md
  11392 expectations.json
    855 granitsi_fixtures_06.09.json
    371 index_excerpts.txt
    461 test_places_public_bundle.py
   4334 recall_sweep.py
   7587 new_data/hotels.json
   2877 new_data/place_categories.json
   4651 new_data/places.json
   7482 old_data/hotels.json
   2763 old_data/place_categories.json
   4396 old_data/places.json
  47332 total
total 3372
drwxr-xr-x 1 Petar 197121      0 Sep  7 08:36 .
drwxr-xr-x 1 Petar 197121      0 Sep  7 08:36 ..
-rw-r--r-- 1 Petar 197121  53242 Sep  7 08:36 010_signed_quarter_boundaries.md
-rw-r--r-- 1 Petar 197121 330301 Sep  7 08:36 expectations.json
-rw-r--r-- 1 Petar 197121  32133 Sep  7 08:36 granitsi_fixtures_06.09.json
-rw-r--r-- 1 Petar 197121  25730 Sep  7 08:36 index_excerpts.txt
drwxr-xr-x 1 Petar 197121      0 Sep  7 08:36 new_data
drwxr-xr-x 1 Petar 197121      0 Sep  7 08:36 old_data
-rw-r--r-- 1 Petar 197121 229775 Sep  7 08:36 recall_sweep.py
-rw-r--r-- 1 Petar 197121  11279 Sep  7 08:36 test_granitsi_fixtures.py
-rw-r--r-- 1 Petar 197121  29194 Sep  7 08:36 test_places_public_bundle.py
-rw-r--r-- 1 Petar 197121  95033 Sep  7 08:36 ПЛАН_Б3_07.09.md
-rw-r--r-- 1 Petar 197121  62452 Sep  7 08:36 ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md
-rw-r--r-- 1 Petar 197121  29465 Sep  7 08:36 ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md
-rw-r--r-- 1 Petar 197121  29242 Sep  7 08:36 СЪСТОЯНИЕ_Границите_06.09.md


12. **Изходите на присвояването — затворена, взаимно изключваща се таблица** (Astra S21 т. 6), в този ред: `written` (записан квартал, непроменен; ако полигонът е родител или дете на записания по DAG → `compatible`, иначе `disputed_written`) → `no_coord` → `pin_outside_all` → `edge_pending` (в ръба `max(50, precision_m)` на най-малкия съдържащ) → `disputed_overlap` (в ≥ 2 полигона без DAG връзка) → `deferred_zone` (полигон само на код от `registry_pending`/отложен) → `assigned_polygon` (най-малкият съдържащ по DAG) → `assigned_district` (само по т. 4 (i)–(iii)). Всяко място получава точно един изход; таблицата е гейт с фикстура за всяка клетка. Препоръка: да.

### Б1 · Сглобяване (varna_3d, частно) — `data/quarters_signed.geojson`
Изпълнител: Claude Executor. Write-set: `src/build_quarters_signed.py`, `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`, `.gitignore` (`!data/quarters_signed.geojson`), `data/quarters_signed.geojson`. Съобщения: `build: assemble quarters_signed.geojson from decisions 3 (sha <…>) with D1 schema for imported geometry` · `gates: qa_quarters_signed with negative fixtures`. Съдържание: 61 Feature (60 Уикимапия + Младост 2 по ключа от Б0 т. 3), полетата по Б0 т. 1–4, 6; `_meta`: `artifact_class: "signed_by_plan_signature"`, `decisions_sha256`, `decisions_commit`, манифест на входовете (frozen v2, extra 5729429, mladost2 face, agkk_au5 само като свидетел), `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict: "allowed_with_conditions", position}`, `parent_child[]` (Б0 т. 9), `registry_pending[]`. Байтове по G30 (UTF-8 без BOM, sorted keys, compact, финален LF; две сглобявания = байт-еднакви). **Гейт (червен):** предгейтове G19 (`gh repo view varna_3d --json visibility` = PRIVATE) и G3 (`qa_no_cad_ids.py`); G25-а (двата хеша поотделно, подменен връх → ✗, подменен `wm_id` → ✗), G26 (биекция решения ↔ трите множества на D4 с `declared_streets`→polygon, `alias_of`/`deferred`→`_meta`; всеки код от регистъра има решение или е в `registry_pending`, поименно), G27(а) (низът по амандамент №2 §3.8 във всеки Feature), D1 (21 полета, `null` само където Б0 т. 1 позволява; `drawn_*` непразно при внос → ✗), лиценз (голо „CC BY-SA“ → ✗), една геометрия към два кода → ✗, `precision_m` липсва → ✗, метод „по улици“ без `mladost2` → ✗. Комитът на `data/quarters_signed.geojson` е **на Петър** по D16/G4: изпълнителят го оставя стейджнат с готово съобщение (`data: signed quarter boundaries v1 (decisions 3, sha <…>)`) и го записва в доклада; всичко след Б1 чете файла по sha, не по комит.

### Б2 · Присвояване P8-а (varna_3d) — тръгва само с подписано Б0 т. 11; изходите са КАНДИДАТИ за комита на Петър
Write-set: `src/fire_varna_locations.py` (каналът `SIGNED_POLYGON` + `DISTRICT_FALLBACK`, четене на `quarters_signed.geojson` по sha; `LEDGER` сочи НОВ датиран леджер `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` с `_meta.base_rev` = комитът на стария; старият не се пипа), `src/qa_p8a.py`, `data/fire_varna_places.json`, `data/fire_varna_hotels.json` (износът), `data/fire_varna_location_inputs.json` (пиновете, вкл. `quarters_signed.geojson` sha), новият леджер. Съобщения: `feat(p8a): SIGNED_POLYGON channel with district fallback, new dated ledger, written quarters untouched` · `data: places export with quarter_attribution (decisions 3)`. Правила: само ПРАЗЕН квартал се пише; най-малкият съдържащ полигон; двойка без подписано родство и място в двата → `disputed`, не се пише; ръб `max(50, precision_m)` → `edge_pending`; без полигон → районът само по Б0 т. 4 (i)–(iii): не в зони на отложени кодове, не при `pin_outside_all` без съгласен свидетел, и винаги заместим; записан ≠ полигон → леджер `disputed`, редът непроменен (G17). Гейт: fallback-ред в зона на отложен код → ✗; fallback-ред, защитен от G17 в следваща версия → ✗ (фикстура с втора версия, в която подписан полигон трябва да го замести). Координати: САМО от `place_identity.json` след хода по Б0 т. 11 (G9 зелен); изнесените координати са забранени за присвояване (D7) — гейт: скриптът не отваря `data/fire_varna_*.json` за четене на координати (AST-проверка като в Н4). Изходите на таблицата по Б0 т. 12 се броят и записват поименно. Десетият ключ по Б0 т. 5 във varna_3d: `META_KEYS` (places 9→10, hotels 7→8 — измерено от Astra), двата износителя (`export_fire_varna_places.py:816`, `export_fire_varna_hotels.py:420`), QA/M6 и `build_place_categories.py` (родители и полигонен провенанс) в един varna_3d комит на изпълнителя; **износените данни (`data/fire_varna_*.json`, новият леджер) остават стейджнати за комита на Петър** (D16/G4) с готово съобщение в доклада. **Гейт (червен):** G17 (всеки записан квартал в стария леджер-блоб `git show <base_rev>:…` е байт-равен в новия износ), G4 (fail-closed без подпис → тук подписът е този план + sha на решенията, записани в `_meta`), `qa_fire_varna_places_export.py` с 10 ключа, брой присвоени = броят „би получил“ от Н2 (мярката и резултатът трябва да съвпадат до място), `edge_pending` и `disputed` в леджера поименно, `python -m unittest` зелен.

### Б3 · Търсене по квартал F13 (Fire_Varna) — СУТРИНТА, не нощес (Astra S21 т. 4–5: доставката е един атомен комит с подписи, които само Петър дава)
Write-set: `index.html` (`QUARTER_SRC`, `QUARTER_CODES` +41, `PLACES_CACHE` v7, нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`), `data/places.json`, `data/hotels.json` (доставката от Б2 по подредената тройка на D13: пинове + `expectations.json` + двата преписа), `tests/test_granitsi_fixtures.py` (шестте S17 фикстури, вкл. `client_cache_matrix` в node — изпълнителят назовава изпълнителя), `release/sign` артефактите по гейта на доставката от 05.09. Съобщения: `feat(search): quarter search over signed boundaries, attribution row, QUARTER_CODES +41, cache v7` · `data: places delivery with quarter_attribution (D13 ordered)` · `tests: S17 fixtures fail on broken candidates`. Пълният write-set по Astra S21 т. 4: трите data файла (`places.json`, `hotels.json`, **`place_categories.json`**), `index.html` (`PLACES_CACHE` v7, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци `:6265`, зареждане/валидиране `:6528`, атрибуцията в паметта `:6657`, D12/индекс/търсене и картончето `:7253`; **типово правило за `DISTRICT_FALLBACK`** — районен код в `quarter` не бива да чупи `!quarter` условието на районното търсене `:7064`), двата bundle теста (`test_places_public_bundle.py:55`, `test_hotels_public_bundle.py:61`), `expectations.json`, трите манифеста, референтният/паритетният корпус и Python паритетът на търсенето (D13 `:62`). Нощес изпълнителят **подготвя** дифа като кръпка (`scratch/places_search/b3_patch_07.09.diff`, непроследена) и фикстурата `client_cache_matrix.foreign_code_while_other_bundle_valid` (Node: валидни хотели, кеш v6/v7, crypto on/off; приемане = двата булеви валидатора минават И 150+225 реда реално се индексират; чужд код → наблюдаем отказ, не `places2=[]` мълчаливо). **Гейт (сутрин, след комитите и подписите на Петър):** замразената референция (нула изгубени резултати), шестте фикстури падат на счупен кандидат и минават след, `python -m unittest discover -s tests` и `python -m gates.run_gates` зелени, размерът ≤ 5 MB, никаква геометрия в проследените `data/*.json` на Fire_Varna (grep за `coordinates` в тях → 0 извън `data/hydrants.json`).

### Б4 · Одит на Б1–Б3 и докладът
Одитор (Opus, read-only, друг агент) на всеки лот: гейтовете преизпълнени, дифът срещу write-set-а (всеки допълнителен файл = находка), авторите, съобщенията, sha веригата решения → граници → леджер → износ → доставка. Докладът `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna) носи числата на А и Б, всички sha, спрелите лотове с причината, и §„Какво прави Петър сутринта“: комит на `quarters_signed.geojson` (G4), препотвърждаване на решенията по sha, преглед на дифа в трите репа, регистърът (Ваялар, Евксиноград/Траката, Цветен квартал, `parents`, 16-те), Gate 2, пуш.

**Ред на изпълнение при подписан Б0 (Astra S21 т. 7):** договорите от §2а (скриптове + отрицателни фикстури, всяка доказано падаща) → Н0 (основа: HEAD-ове, мръсният диф, пинове, G19/G29) → Н1 → Н2-0 → Н2 → Н4 (мерки) → Н3-а (независим) → **Б1** (кандидат-подписан файл, стейджнат) → **Б2** само с Б0 т. 11 (G9 зелен), изходите стейджнати → **подготовка на Б3** (кръпка + фикстурата за шумно падане) → Б4 (одит) → Н5 (докладът, винаги). **STOP преди Б2**, ако Б0 т. 11 не е подписан или G9 е червен. **Сутринта:** комитите на Петър (геометрия, решения по sha с реда за атрибуция, износът) → Б3 като един атомен комит → подписи/freeze → пълен набор + 7/7 → одит → пуш. При червено в 03:00: чуждият проследен диф и последният зелен release остават непокътнати; откатът е по write-set (стейджнатото се маха с `git restore --staged`, изходите се трият по назован път) — общ `git revert` не е договор за стейджната геометрия.

## 7 · Конфликти и нормализация (мярка, влиза в Н2/Н4 и в доклада)
- **Леджер на конфликтите по поле** за всяко от 375-те места: какво твърди всеки извор за квартала — регистровият запис (REG/KAIS/НТР, ранг), адресният низ (парсиран: „бул. Владислав Варненчик“ ≠ „кв. Владиславово“ — булевард и квартал носят едно име), кадастралният `quar` на най-близкото тяло, потвърденият полигон (координата), районът; колона `resolution` по правилото „координатата решава квартала; името е свидетел“, и колона `conflict_kind` ∈ {none, name_vs_polygon, parent_vs_child, pin_outside_all, written_outside_polygon}. Изход: `scratch/granitsi/conflict_ledger_07.09.json` (varna_3d, непроследен) + числата по вид в доклада. Нищо не се презаписва от този леджер; той е списъкът за Петър.
- **Сградите (Н4)** носят същите колони: кадастрален `quar` срещу полигона по координатата на тялото; несъгласията по вид (адрес на булевард с име на квартал; Кайсиева/Владиславово; Акчелар/Виница; курорт/квартал Чайка).
- **Правилото за бъдещето** (в доклада, за амандамент): всеки нов извор влиза с ранг и с колона в леджера; никой извор не презаписва друг; координатата е арбитърът за полето „квартал“; имената се нормализират през регистъра (alias-и), не през редакции на данните.

## Какво подписва Петър

**ЧАСТ А (винаги):** подписваш **една нощ от мерки**: шест лота, които четат — пинове с доказана верига (Н0), кандидат-геометрия от 60-те уикимапийски кода в частното репо, която НЕ е подписан артефакт и умира с една команда (Н1), координати и присвояване, преброени срещу непокътнат леджер и три ленти на неточността (Н2-0, Н2), пет фикстури, които фиксират ДНЕШНОТО поведение на търсенето (Н3-а), мярката за ~10k сгради (Н4) и доклад, чиито числа идват от одитора (Н5) — плюс двете обявени отклонения от `ПЛАН_ИЗЧИСТВАНЕ_v2 §0.1` и `§0.3` и десетте решения в §5, които остават твои и на които нито един агент няма право да отговори през нощта.

**ЧАСТ Б (само с блок Б0):** подписваш и дванадесетте решения в §6 Б0 — тогава нощта произвежда `quarters_signed.geojson` (стейджнат за твоя комит), координатите на местата от кадастралните тела (т. 11, с резервно копие и G9), присвояването на квартал за празните места като кандидат-износ (стейджнат), кръпката и шумната фикстура за търсенето (Б3 се комитва сутринта с твоите подписи), и одитиран доклад; всичко локално, обратимо, без пуш. Без т. 11 нощта спира преди Б2 и присвояването остава мярка.

## Какво НЕ се пипа тази нощ (ЧАСТ А; при подписан Б0 изключенията са изброени в Б1–Б3)

• I have the §Б3 text (line 144 was truncated in output but I got most of it — the task says line 143-145; line 144 was truncated. Let me get line 144 fully. Also §0 and §2а. Let me get the full line 144 and §0/§2а.3106
Write-set: `index.html` (`QUARTER_SRC`, `QUARTER_CODES` +41, `PLACES_CACHE` v7, нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`), `data/places.json`, `data/hotels.json` (доставката от Б2 по подредената тройка на D13: пинове + `expectations.json` + двата преписа), `tests/test_granitsi_fixtures.py` (шестте S17 фикстури, вкл. `client_cache_matrix` в node — изпълнителят назовава изпълнителя), `release/sign` артефактите по гейта на доставката от 05.09. Съобщения: `feat(search): quarter search over signed boundaries, attribution row, QUARTER_CODES +41, cache v7` · `data: places delivery with quarter_attribution (D13 ordered)` · `tests: S17 fixtures fail on broken candidates`. Пълният write-set по Astra S21 т. 4: трите data файла (`places.json`, `hotels.json`, **`place_categories.json`**), `index.html` (`PLACES_CACHE` v7, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци `:6265`, зареждане/валидиране `:6528`, атрибуцията в паметта `:6657`, D12/индекс/търсене и картончето `:7253`; **типово правило за `DISTRICT_FALLBACK`** — районен код в `quarter` не бива да чупи `!quarter` условието на районното търсене `:7064`), двата bundle теста (`test_places_public_bundle.py:55`, `test_hotels_public_bundle.py:61`), `expectations.json`, трите манифеста, референтният/паритетният корпус и Python паритетът на търсенето (D13 `:62`). Нощес изпълнителят **подготвя** дифа като кръпка (`scratch/places_search/b3_patch_07.09.diff`, непроследена) и фикстурата `client_cache_matrix.foreign_code_while_other_bundle_valid` (Node: валидни хотели, кеш v6/v7, crypto on/off; приемане = двата булеви валидатора минават И 150+225 реда реално се индексират; чужд код → наблюдаем отказ, не `places2=[]` мълчаливо). **Гейт (сутрин, след комитите и подписите на Петър):** замразената референция (нула изгубени резултати), шестте фикстури падат на счупен кандидат и минават след, `python -m unittest discover -s tests` и `python -m gates.run_gates` зелени, размерът ≤ 5 MB, никаква геометрия в проследените `data/*.json` на Fire_Varna (grep за `coordinates` в тях → 0 извън `data/hydrants.json`).
Good, I have the §Б3 text now (the signed text): "нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`", "QUARTER_CODES +41", "шестте S17 фикстури", "типово правило за DISTRICT_FALLBACK" (only at :7064), "замразената референция (нула изгубени резултати)".

  Now, measurements on new_data/. Let me do the measurements with Python:

  1. §1.3: 8 missing codes; 28 delivered.
  2. §1.5: 57 rows change exactly quarter/zone; quarter_attribution 18 codes; url form.
  3. §1.8: counts of rows with specific quarter codes in new_data; "младост" 28→20; "училище младост" 11→6 (these are search results via recall_sweep — but recall_sweep.py in this copy presumably points to data/ paths... running it might be complex; the task says measure with commands on new_data/. I can run recall_sweep with appropriate flags? Let me check recall_sweep.py briefly for how it loads data and how search works. Actually task says: (1.8 table — count yourself by new_data: how many rows carry kv_levski, trakia, hristo_botev, sv_ivan_rilski, pobeda, vazrazhdane1/2, mladost2, chaika_kk/kv, druzhba; "младост" 28→20; "училище младост" 11→6).

  The "младост" 28→20 etc. come from running the search engine. The task allows me to count rows directly by new_data. Running recall_sweep may be doable — check its data path configuration. Let me first do the JSON measurements with Python (read-only, in-memory).

  Also: О22 — 138 moved rows: zone_named lost/changed old→new. I can compute that by comparing old_data vs new_data rows: rows with old quarter/zone vs new quarter/zone. Coverage semantics: "zone_named lost/changed". I can approximate: for each place/hotel matched by identity (name?), compare zone. Let's compute counts of rows where zone changed, where zone was non-null in old and null/different in new etc. Coverage "moved rows" = rows whose named zone was lost or changed. 138 = places 44+44 + hotels 39+11 = 138. Let me verify: places: zone_named lost 44, changed 44 = 88; hotels: lost 39, changed 11 = 50; total 138. I can attempt to compute with simple identity matching (by name?) — old and new both have same rows, no adds/deletes, so match by position or by name+type. Compute old zone vs new zone.

  4. О15: isSignificantToken — check index_excerpts.txt for :6495 and the M7 branch at :7059. "кв." token length ≤ 2 → not significant. Verify: token "кв" s.length=2 → excluded; "левски" length 7 → significant. Query "кв. Левски": significant tokens = [levski]; M7 requires R.every(isSignificantToken)? Actually the claim: "кв. Левски" → M3 with 4 rows, zero with code kv_levski; "левски" → M7-bare 14 rows, 12 with kv_levski. Cheaper fix the plan misses? Possibly: add "kv"/"zhk" type-prefix tokens to significant tokens only when followed by... Or simpler: the quarter dictionary phrases — e.g. adding alias "кв. Левски" as an alias in the dictionary so the M3 location phrase matches? Actually a cheap fix: the zone aliases in place_categories already map "васил левски" etc. The M3 branch matches phrases from the dictionary; "кв. левски" — the dictionary phrases for kv_levski include "ж.к. васил левски"? Let me check place_categories.json aliases. A cheaper fix might be: add prefix forms ("кв. левски") as aliases in the dictionary — no D12 normalizer needed, data-only change... but that changes dictionary = new export. Or in the client: expand isSignificantToken to accept known type prefixes. Let me examine excerpts.

  5. О16: DAG doesn't enter; "дете → детето" doesn't work — check: "възраждане 2" → 0 rows because number token dropped, so query becomes "възраждане" which matches parent phrase... wait plan says "възраждане 2" → 0 rows. Hmm, if number is dropped, the remainder is "възраждане" which should match 5 rows. Plan says 0 rows. Because M7 requires every token significant and...? Need to check the engine. Actually the plan's measure says 0. Let me verify by running recall_sweep if feasible.

  6. О19/О20: DISTRICT_FALLBACK rule at six places; two zone labels.

  7. §3.5 eleven fixtures — for each: does it test the real claim and does _broken fail by the same check. This requires reading test_granitsi_fixtures.py and granitsi_fixtures_06.09.json, plus thinking. That file exists in the copy (the current 5-fixture version). The plan proposes 11 fixtures — I need to evaluate plausibility against the current harness.

  8. §8 probes numbers vs new_data.

  9. О14: "младост" 28→20 — which 8 rows and why; acceptable by the design "everything INSIDE the quarter".

  Let me start the measurements with Python scripts (read-only). First the JSON-level counts.

• Основата е прочетена. Сега правим измерванията върху `new_data/`.== counts ==
places 150 hotels 225 old places 150 old hotels 225
== distinct quarter codes delivered (new) == 28
['asparuhovo', 'borovets_yug', 'briz', 'chaika_kk', 'chaika_kv', 'dolna_traka', 'druzhba', 'galata', 'grackata_mahala', 'hristo_botev', 'izgrev_kv', 'kk_konstantin_elena', 'kolhozen_pazar', 'kv_levski', 'mladost', 'mladost2', 'pobeda', 'priboy', 'sv_ivan_rilski', 'trakia', 'troshevo', 'tsentar', 'vazrazhdane', 'vazrazhdane1', 'vazrazhdane2', 'vinitsa', 'vladislavovo', 'zlatni_pyasatsi']
delivered == plan's 28: True | extra: set() | missing: set()
old distinct quarter codes: 20
missing = delivered - old: ['dolna_traka', 'grackata_mahala', 'hristo_botev', 'kolhozen_pazar', 'kv_levski', 'sv_ivan_rilski', 'trakia', 'tsentar']
plan claims missing 8: ['dolna_traka', 'grackata_mahala', 'hristo_botev', 'kolhozen_pazar', 'kv_levski', 'sv_ivan_rilski', 'trakia', 'tsentar']
match: True
kv_levski 12
trakia 4
hristo_botev 3
sv_ivan_rilski 2
pobeda 4
vazrazhdane1 1
vazrazhdane2 1
mladost2 3
chaika_kk 19
chaika_kv 10
druzhba 1
tsentar 9
dolna_traka 2
grackata_mahala 2
kolhozen_pazar 2
== src counts new ==
Counter({('hotels', 'REG'): 115, ('places', 'SIGNED_POLYGON'): 42, ('places', 'REG'): 39, ('hotels', 'KAIS'): 25, ('hotels', 'SIGNED_POLYGON'): 15, ('hotels', 'SIGNED_OVERRIDE'): 12, ('places', 'KAIS'): 10})
== 57 rows change exactly quarter/zone ==
57
Counter({('quarter', 'zone'): 57})
places changed: 42 hotels: 15
all null->SIGNED_POLYGON: True
== _meta ==
places _meta keys: ['by_kind', 'by_zone_src', 'count', 'excluded', 'generated', 'licence_address', 'licence_osm', 'licence_registry', 'licence_wikidata', 'quarter_attribution'] 10
hotels _meta keys: ['by_zone_src', 'count', 'excluded', 'generated', 'licence', 'licence_address', 'licence_osm', 'quarter_attribution'] 8
quarter_attribution places: 14 hotels: 7
union: 18
attribution srcs: Counter({'wikimapia': 17, 'openstreetmap': 1})
urls not matching ^https?://wikimapia.org/<id>/: {'mladost2': 'https://www.openstreetmap.org/copyright'}
kv_levski 
Traceback (most recent call last):
  File "<stdin>", line 76, in <module>
  File "C:\Program Files\Python310\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u0436' in position 109: character maps to <undefined>


• The last print failed due to cp1252 encoding — I'll set PYTHONIOENCODING=utf-8. Let me set up a todo list and continue measurements. Key results so far confirm §1.3, §1.5 (57 rows, attribution 18 codes, url form — note the mladost2 URL is openstreetmap, which doesn't match the WM_URL regex but its src is 'openstreetmap' so the regex only applies when src === 'wikimapia' — plan's validator checks `e.src === 'wikimapia' && !WM_URL.test(e.url)` so mladost2 passes. Good.)

  Next: 
  - zone counts, dictionary (place_categories): 20→28 zones, aliases 39→48, parents 0 of 28.
  - QUARTER_BY_SRC values claimed in §3.3: places {"REG":39,"KAIS":10,"SIGNED_POLYGON":42} ✓ matches; hotels {"REG":115,"KAIS":25,"SIGNED_OVERRIDE":12,"SIGNED_POLYGON":15} ✓. LOCATION_COUNTS {quarter 28, district 5, locality 5}, LEGACY_ROWS 18, LOCALITY_COUNT 5 places / 7 hotels.
  - О22: 138 moved rows — compute zone_named lost/changed old→new.
  - Search semantics: run recall_sweep? It likely needs data paths. Check how recall_sweep loads data and whether I can run search queries against new_data. Also index_excerpts for isSignificantToken and the branches.

  Let me continue.

• Първата серия потвърди §1.3/§1.5. Продължавам с речника, етикетите и брояча за О22.

== attribution url forms ==
kv_levski {"src": "wikimapia", "label": "Wikimapia.org", "licence": "CC BY-SA", "url": "http://wikimapia.org/900042/bg/ж.к._Васил_Левски"}
mladost2 {"src": "openstreetmap", "label": "© OpenStreetMap contributors", "licence": "ODbL", "url": "https://www.openstreetmap.org/copyright"}
attribution keys equal places/hotels: {'tsentar', 'kolhozen_pazar', 'kv_levski'}
== dictionary ==
zones new/old: 28 20
district new/old: 5 5 | locality: 5 5
zone entry shape: ["kv_levski", {"name": "кв. Левски", "aliases": ["Васил Левски", "кв. Васил Левски", "Левски"]}]
aliases new/old: 48 39
parents nonzero: []
zone_generic_words: 8
cats _meta keys: ['contains_cadastral_id', 'contains_personal_data', 'curated_forms', 'generated', 'generator', 'legacy_bundle_sha', 'legacy_dropped_by_m3', 'n_chips', 'n_forms', 'n_legacy_dropped_by_m3', 'n_legacy_rows', 'n_locations', 'rule', 'rule_curated', 'rule_legacy', 'rule_legacy_m3', 'rule_locations', 'rule_sha', 'rule_zone_overrides', 'rule_zones', 'schema', 'sources', 'what', 'zone_alias_overrides', 'zone_alias_skipped', 'zone_generic_words', 'zones_unmatched']
== LOCALITY_COUNT ==
places locality rows: 5 hotels: 7
places locality srcs: Counter({'KAIS': 4, 'REG': 1})
== LEGACY_ROWS / location counts in _meta ==
places _meta.by_zone_src: {"KAIS": 10, "REG": 39, "SIGNED_POLYGON": 42, "district": 59}
hotels _meta.by_zone_src: {"KAIS": 25, "REG": 115, "SIGNED_OVERRIDE": 12, "SIGNED_POLYGON": 15, "district": 58}
== QUARTER_BY_SRC recomputed ==
places: {'SIGNED_POLYGON': 42, 'REG': 39, 'KAIS': 10} | hotels: {'SIGNED_OVERRIDE': 12, 'REG': 115, 'KAIS': 25, 'SIGNED_POLYGON': 15}
DISTRICT_FALLBACK rows: 0
== zone labels: quarter rows, zone == quarter.name ? ==
rows with quarter: 258 zone!=quarter.name: 0
rows w/o quarter: 117 zone!='район '+district.name: 0
• All §1.5/§3.3 numbers confirmed. Note: plan says "201 написани квартала преписани дословно (REG 154, KAIS 35, SIGNED_OVERRIDE 12)" — 39+115=154 REG ✓, 10+25=35 KAIS ✓, 12 SIGNED_OVERRIDE ✓. 201 written total; rows without quarter 117 (59+58) ✓ ("117 без квартал" §1.5).

  LEGACY_ROWS 18: check nc['_meta']['n_legacy_rows']. Let me check. Also LOCATION_COUNTS {quarter 28, district 5, locality 5} — computed: 28 ✓, 5 ✓, 5 ✓.

  Now О22: 138 moved rows — zone_named lost/changed old→new. Let me understand the coverage semantics: presumably "zone_named" = zone string that names a quarter (not "район X"). lost = row had named zone before, now different... Let me compute: rows where old zone is a "named" (non-'район ') zone and new zone differs (lost = old named → new not named? changed = named→different named?). Plan: places zone_named lost 44 / changed 44; hotels 39 / 11. Total 138.

  Hmm wait — 57 rows changed quarter/zone null→SIGNED_POLYGON. How can there be 44+44=88 places rows "moved"? Maybe coverage counts differently: maybe "moved" includes rows whose zone changed at all... Let me compute simple diffs of zone by identity match, and zone categories. Old places: rows with zone not starting with 'район' — count them; new ditto.

  Actually old data: how many places have quarter? old places REG 39+KAIS 10 = 49 quarter rows... plus maybe more. Old zones: 20 quarter zones. Let me just compute: for each matched row, old_zone vs new_zone; classify lost = old had named zone, new doesn't have that zone... In coverage terms "lost" probably = row in baseline with a named zone whose name no longer appears in candidate zone; "changed" = zone name changed. Let me compute and see if numbers 44/44/39/11 emerge.

  Also "младост" 28→20 and "училище младост" 11→6: need the search engine. Check recall_sweep.py — how it loads data, and whether I can run queries against new_data/old_data. Let me look at relevant parts: REC._loc_tokens 664-679, search, phrase building 424-442, 515-533, 1120, and data loading. The file is 4334 lines. Let me grep for data path / OUTDIR / main.

• Данните потвърждават §1.3–§1.5 и §3.3. Сега О22 (138 реда) и двигателят на търсенето.n_legacy_rows: 18
places zone changed rows: 42 | named->named: 0 | named->unnamed: 0
Traceback (most recent call last):
  File "<stdin>", line 20, in <module>
AssertionError


• Hotels have duplicate names (the plan mentions "РОЯЛ" ×2; 225 rows, 224 unique name+type pairs). So identity by name alone fails for hotels. Use (name, ...) with ordinal or (name, type). Let me match by (name, kind/type) with fallback by index position. Old and new have same order presumably (0 added/removed). Simpler: match by index position since counts are equal and presumably same order. Let me check whether rows are in the same order — compare name sequences.hotel name order identical: True
place name order identical: True
places lost: 0 changed: 0
hotels lost: 0 changed: 0
Hmm — with zip by position and named-ness by quarter, no lost/changed? That contradicts 1.8.1's "places zone_named lost 44/changed 44". But wait: 57 rows changed zone from "район X" to quarter name — those are unnamed→named (gained). But plan says 44 lost + 44 changed for places. So coverage must count something else. Maybe coverage counts zone changes differently: maybe "zone_named" refers to rows matched by zone in the baseline expectations/allow — i.e., rows in the allow file whose zone label moved. Or maybe: baseline f06ac06 zone values vs candidate, where "lost" = baseline row's zone no longer equal, "changed"... 

  Alternatively the coverage tool may compare by zone string only: "lost" = zone string present in old but row changed, "changed" = ... Let me think: 57 rows changed quarter/zone. But coverage says 88 places rows moved. Hmm 88 ≠ 57. So coverage counts something beyond direct zone diff. Perhaps it counts rows whose zone *label* changed OR whose zone's meaning changed. Wait — 42 places + 15 hotels = 57 changed. But 1.8.1 says 138 moved rows total (44+44+39+11 = 138). 

  Alternative interpretation: coverage is a *result-set* coverage: it measures search results (zone_named bucket = queries by zone name?), i.e., "moved rows" might be recall rows: the recall_sweep reference rows that change bucket between baseline and candidate. The phrase "zone_named lost/changed" suggests: for the zone_named category (queries like "младост"), rows that were in results before and aren't now (lost) or changed. E.g. "младост" 28→20 loses 8; "училище младост" 11→6 loses 5; "училище район младост" 12 stays but 6 zone changed... Summed across 140 frozen queries, you could get 44/44/39/11.

  I can't easily replicate gates/coverage.py since it's not in this copy. The plan claims (M) 138 with a command referencing gates.coverage which isn't here. I can still sanity-check plausibility: the coverage gate's allow lists rows by identity+zone; "moved" = rows in baseline whose zone differs in candidate... but direct zone diff gives only 57. Unless coverage counts each affected *query row* in expectations? Hmm.

  Actually maybe coverage compares against baseline f06ac06 which may differ from old_data (today's data/ on Fire_Varna HEAD f00dd78). old_data = "днешните data/*.json на Fire_Varna" = HEAD f00dd78 presumably. Baseline f06ac06 is the signed baseline from 05.09 — possibly older than f00dd78? The §1.1 says HEAD is f00dd78, ahead 81. f06ac06 might be an earlier commit. If baseline data differ more from new_data than old_data does, the 138 could include other changes. We can't verify directly; we have only old_data and new_data. So for О22 I can compute old→new: 57 rows changed (zone+quarter), and state that "138 against f06ac06" is not reproducible from this copy; but the plan itself marks it (M) with STOP re-measure. I can note consistency: allow budgets 138 ≥ 57 direct zone changes; the rest (81) may stem from f06ac06 ≠ f00dd78.

  Hmm, wait. Let me reconsider: maybe coverage counts *expectations rows*: the frozen reference has 140 queries; coverage measures which reference rows change. "places zone_named lost 44/changed 44" — the sum per bucket. Without gates/coverage.py in the copy I can't recompute. I'll flag it as non-reproducible here and note the plan already requires re-measurement (STOP 1). Actually the task asks: "О22 (baseline остава f06ac06, allow бюджетира 138 преместени реда — преброй ги сам: zone_named lost/changed по old→new)". So they want me to count old→new. I got 57 rows with zone changed (42+15), all unnamed→named. So by old→new: lost 0 / changed 0 in the strict sense; 57 gained. If "changed" counts zone-label change including район→quarter name, then 42+15=57 ≠ 138. So the 138 cannot be reproduced from old→new — likely because baseline f06ac06 ≠ old_data (HEAD f00dd78). Let me check: is old_data really f00dd78's data or f06ac06's? The task says old_data/ = "днешните data/*.json на Fire_Varna". If there were data commits between f06ac06 and f00dd78, diffs would show. The plan §1.9 says the allow file has 150 rows budgeted against the 05.09 delivery... 

  Let me look at what coverage counts: without the code, approximate: maybe "zone_named" lost/changed refers to the *reference search results* (recall sweep): for each frozen query, the result rows; a row is "lost" if it was in the old result and not in the new; "changed" if it's in both but its zone label changed. To verify 138 I'd need to run recall_sweep against both datasets. That's the next big step: figure out if recall_sweep.py can run standalone with the copy's data. Let me inspect recall_sweep.py's entry, paths, and how to run a query.recall_sweep.py expects REPO_ROOT = parents[2] of the file, i.e. the file is at scratch/places_search/recall_sweep.py. In this copy it's at root. It loads data from REPO_ROOT/data/*.json. I can run it if I construct a layout — but the task says don't create/modify files... "не изпълнявай команди, които пишат по диска". Running recall_sweep writes to OUTDIR (%TEMP%/fv_measures) and overwrites probe_out/token_parity.json (REPO_PARITY_OUT) — writes to disk, forbidden. Also running requires creating directory structure — forbidden.

  Alternative: import the module pieces in-memory. I can load recall_sweep.py source, patch the data-loading part... That's executing code but read-only if I avoid module main. Simpler: replicate the search semantics in-memory using the engine classes? The engine is complex (4334 lines). 

  Better approach: load the module with monkeypatched paths in-memory without executing main. Module-level code at :258-260 loads cats/hotels/places2 at import — reading files. I can monkeypatch the module's constants after import... but the load happens at import time at module level. I could read the source, and exec it with modified constants via regex replacement in memory — replace the paths HOTELS/PLACES2/CATS to point at new_data, and set OUTDIR to... exec would still run main? Check the bottom of file for `if __name__ == "__main__"`. Also FREEZE reads sys.argv. And the module writes only when main runs? Let me check what runs at import: module-level data load at :258-260, plus maybe more heavy computation at module level. And does anything write at import? Line 4249-4253 writes REPO_PARITY_OUT — check if that's in a function or module level.

  Actually a cleaner approach: exec a modified source string where I replace path constants with new_data/old_data paths and stub the writing. That's read-only w.r.t. disk as long as I don't invoke writing functions. But risk: module-level code may do the whole sweep (it's a 4334-line script; data loads at :258, and much logic could be module-level). Let me check the structure: grep "^def \|^class \|^if __name__".68:REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
73:HOTELS = str(REPO_ROOT / "data" / "hotels.json")
75:CATS = str(REPO_ROOT / "data" / "place_categories.json")
76:REPO_ROWS_OUT = str(REPO_ROOT / "scratch" / "places_search" / "recall_sweep_rows.json")
79:REPO_PARITY_OUT = str(REPO_ROOT / "scratch" / "places_search" / "probe_out"
84:OUTDIR = (pathlib.Path(tempfile.gettempdir()) / "fv_measures").as_posix() + "/"
90:FREEZE = "--freeze" in sys.argv
91:REPORT_ONLY = not FREEZE
95:MANIFEST = "--manifest" in sys.argv
100:GENERATED_AT = datetime.date.today().isoformat()
104:CENTER = (43.2141, 27.9147)
105:TOP = 8
109:def norm(s):
118:_SKEL = {
127:def skel(w):
135:def lev(a, b, cap):
155:TYPO = re.compile(u"[\u201e\u201c\u201d\u201a\u2018\u2019\u00ab\u00bb\u2013\u2014/()]")
157:LET = u"\u0410-\u042f\u0430-\u044fA-Za-z"
158:NOL = u"(?<![" + LET + u"])"
159:NOR = u"(?![" + LET + u"])"
160:MARKERS = [
167:ORD_SUF = re.compile(
171:_ORD_STEM = {
180:_ORD_END = [u"\u0438", u"\u0430", u"\u043e", u"\u0438\u044f\u0442", u"\u0438\u044f",
182:ORD_WORDS = {}
188:COMPOUNDS = {u"апартхотел": [u"апарт", u"хотел"],
191:ROMAN_OK = re.compile(r"^(x{0,3})(ix|iv|v?i{0,3})$")
192:ROMAN_SHAPE = re.compile(r"^[ivx]{1,5}$")
193:_RV = {"i": 1, "v": 5, "x": 10}
195:def roman_to_arabic(t):
205:class Tok(object):
214:def place_tokens(s):
253:def key_of(s):
263:CHIP_HEAD = {}
268:FORM_IDX = {}
287:EXTRA_FORMS = {
298:MAXFORM = 3   # plan sec.3 T2: forms up to 3 tokens
301:ADDR = set([u"\u0431\u043b", u"\u0431\u043b\u043e\u043a", u"\u0432\u0445",
310:ALIAS_GENERIC = set([skel(u"\u0432\u0430\u0440\u043d\u0430"), skel(u"\u0433\u0440"), skel(u"\u0433\u0440\u0430\u0434")])
318:def name_quality(t, v):
334:def zone_alias_tokens(cats_doc, zones):
400:ZONES_IN = sorted(set([h["zone"] for h in hotels] + [p["zone"] for p in places2]))
416:LOC_CLASSES = (u"quarter", u"district", u"locality")
418:GENERIC_TOKENS = set()
424:def significant_token(t):
434:def significant_tokens(s):
443:def location_dicts(cats_doc):
469:def location_alias_tokens(entries):
515:def location_phrases(entries, added):
535:LOCATIONS = location_dicts(cats)
542:def bundle_digests(path):
560:LEGACY_BUNDLE_SHA = ((cats.get("_meta") or {}).get("legacy_bundle_sha") or {})
561:LEGACY_SHA_OK = all(LEGACY_BUNDLE_SHA.get(key) in bundle_digests(path)
563:LEGACY_BY_ROW = (cats.get("legacy_by_row") or {}) if LEGACY_SHA_OK else {}
573:LEGACY_LOOKUP = {}
581:def legacy_of(bundle, ordinal):
604:class Rec(object):
692:RECS = ([Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
698:EXACT_NAME = {}
707:EXACT_ALIAS = {}
722:STREET = {}
728:STREET_MARK = (u"ул", u"бул", u"пл")
731:def street_rows(R, cls):
764:def alias_significant(qt):
775:def exact_alias(qt):
782:def in_class(rec, fk):
803:CLASS_OF = {}
811:KIND_GROUP = {
827:GEN_CAP = 300                                    # M3/B2: the generosity ceiling
830:def group_of(rec):
834:GROUP_SIZE = {}
839:def gen_ok(rec):
851:CAPMODES = ("plan", "poi")
852:CAPMODE = "plan"                                           # "plan" | "poi"
855:def set_capmode(argv):
878:BASE = {"P1": False, "P2": True, "P3": True, "P4": True, "P5": True,
880:FIX = dict(BASE)
883:def set_fix(cfg):
888:def kind_gen(t, v):
909:def token_match(rec, t):
---
            _refused = _release["refused"]
            print(u"release: %s ; непокрити делти %d ; отказани %d"
                  % (_release["verdict"], len(_release["uncovered"]), len(_refused)))

    # ---------------------------------------------------------------- the writes
    # Амандамент №4 т. 2: the gates are computed ABOVE; the tracked bodies are
    # written HERE, last, and only when there is nothing red and the signature is
    # on the manifests. The old order wrote the reference first and measured
    # afterwards, so a red run left a frozen artefact behind.
    if not FREEZE:
        # A report-only run gates nothing and publishes nothing; its tracked
        # parity corpus is written here, at the end, with the other writes.
        pathlib.Path(REPO_PARITY_OUT).write_text(_parity_text, encoding="utf-8",
                                                 newline=chr(10))
    if MANIFEST and not FREEZE:
        _doc = build_expectations(blob_text(u"HEAD", ROWS_REL), ROWS,
                                  measure_sweep(M5, EXTRA), refused=_refused)
        _path, _signature = write_expectations(_doc, frozen=False)
        print(u"REPORT-ONLY: очаквания -> %s (signed_by: %s)" % (_path, _signature))

    if FREEZE:
---
            _fresh = build_expectations(_rows_text, ROWS, measure_sweep(M5, EXTRA),
                                        refused=_refused)
        except (ValueError, OSError, SystemExit) as _exc:
            # A body that cannot even be measured is a body nobody may freeze.
            # `SystemExit` is named on purpose: `blob_text` fails loud with it,
            # and a missing reference blob would otherwise kill the run before
            # the blockers above are ever printed — the exit code would be right
            # and the reason unreadable.
            blockers.append(u"очакванията не могат да се измерят: %s" % _exc)
            _fresh = None
        if _fresh is not None and engine_blocks(_fresh) != engine_blocks(expectations() or {}):
            blockers.append(u"измереното сега се различава от подписаното — "
                            u"замразяването не пренася подпис върху друг отговор")
        def _write_reference():
            # The reference the JS is gated against lives next to the probe that
            # replays it — one file, one generator. LF on purpose: the CRLF twin
            # on a Windows worktree is the same OID and different bytes (F12-ж).
            pathlib.Path(REPO_ROWS_OUT).write_text(_rows_text, encoding="utf-8",
                                                   newline="\n")
            return u"FREEZE: замразена референция -> %s" % REPO_ROWS_OUT

        def _write_expectations():
            _path, _signature = write_expectations(
                build_expectations(_rows_text, ROWS, measure_sweep(M5, EXTRA),
                                   refused=_refused), frozen=True)
            return u"FREEZE: очаквания -> %s (signed_by: %s)" % (_path, _signature)

        def _write_parity():
            # The third tracked body of this script, in the same block: a refused
            # freeze leaves it byte-untouched (амандамент №5 т. 4).
            pathlib.Path(REPO_PARITY_OUT).write_text(_parity_text, encoding="utf-8",
                                                     newline=chr(10))
            return u"FREEZE: паритет на токенизатора -> %s" % REPO_PARITY_OUT

        _code, _written = freeze_writes(blockers, [_write_reference,
                                                   _write_expectations,
                                                   _write_parity])
        if _code:
            return _code

    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
So `main()` is only called under `if __name__ == "__main__"`. The writes happen inside main(). Module-level: data loads, RECS built, LOCATIONS etc. So I can import recall_sweep as a module (with sys.argv clean) — but paths point to REPO_ROOT/data which is parents[2] of this file = two levels above the temp dir root — nonexistent. I can import with importlib after monkeypatching? The load happens at module level, so I need to intercept before import. Option: read the source, patch the path lines, and exec in a module namespace with `__name__` set to something != "__main__". The heavy sweep presumably runs in main() only — good. But there may be module-level `measure_sweep` etc.? The lines 692: RECS built at module level — that's fine (in-memory). Does anything else expensive run at module level? Let me check for module-level calls like `M5 =` etc. Probably in main(). I'll exec the patched source and then call its search function on queries.

  Need to find the search entry point: `def search(` probably exists. Grep for "def search".1228:def search(q):
3402:def measure_sweep(m5, extra):
3782:def main():
1228:def search(q):
732:    """ЛОТ 1в-Б (ADR 008 D6) — the A3-street branch; None = not a street query.
1133:M7_ENABLED = True
1185:    if not M7_ENABLED or not R:
1265:            return bare, "M7-bare-location"
1276:            return explicit_district, "A3-district"
1296:                return marked, "A3-street"
1300:            return explicit, "A3-district"
1307:                return rows, ("A3-record+zone-phrase" if head else "A3-location")
1320:        return street, "A3-street"
1329:            return rows, "M2-failopen"
1620:# on 03.09 with П7 off and on; for the GAINS `M2-failopen` is red by
1837:# A3-street branch, three are controls that must NOT move: the number without a
1902:    if br != "A3-street":
2257:    u"`M2-failopen`. В този прогон не се задейства нито веднъж.",
2354:M7_BUCKET = "gate_m7_bare"
2749:        ROWS[M7_BUCKET].append({
2755:            "ok": _b == "M7-bare-location",
2925:    global M7_ENABLED
2930:    M7_ENABLED = False
2934:        M7_ENABLED = True
3015:               for m in m7_moved if m["bucket"] != M7_BUCKET]
3018:        M7_ENABLED = False
3023:            M7_ENABLED = True
3044:            "m7_bucket": M7_BUCKET,
3047:                1 for e in rows_with_m7[M7_BUCKET] if e["branch"] == "M7-bare-location"),
3048:            "m7_rows": sum(len(e["rows"]) for e in rows_with_m7[M7_BUCKET]),
3055:            "extra": [e for e in m7_extra if e["bucket"] != M7_BUCKET],
3064:                         for e in rows_with_m7[M7_BUCKET]],
3093:M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")
3094:M7_PLACES = (u"zlatni", u"mladost", u"chaika", u"zpz", u"vilite",
Good — `search(q)` at :1228 returns (rows, branch). I can exec a patched copy of the module source with data paths pointed at new_data (or old_data), and `__name__ != "__main__"` so main() never runs (no disk writes; writes are inside main). Check: does module-level code write anything? Lines 4249-4253 are inside main (indentation suggests inside main). Data load at :258-260 module level. Also line 855+ `set_capmode(argv)` is a function. FREEZE = "--freeze" in sys.argv at module level — fine if argv clean. GENERATED_AT today — fine.

  Concern: patch paths via string replacement of the three constants. REPO_ROOT computed from __file__ — I'll set __file__ appropriately or just replace the path lines. Simplest: replace lines 68-76 with explicit paths.

  Let me write a runner that:
  1. reads recall_sweep.py source
  2. replaces REPO_ROOT assignment with `REPO_ROOT = pathlib.Path(r"<abs path to a dir>")`... but HOTELS etc. derive from REPO_ROOT/data/... Since data lives in new_data/, I can patch lines 73-75 directly to the three file paths, and REPO_ROWS_OUT/REPO_PARITY_OUT to dummy strings (unused outside main; but blob_text and expectations use them in functions only).
  3. exec with __name__='rs_mod', sys.argv=['x'].
  4. call search on the queries, print branch + count + names + quarters.

  One risk: module-level code may reference git (LEGACY_BUNDLE_SHA check at :560-563 uses bundle_digests of local files — reads files only). blob_text only in functions. Let me check line 542-563: LEGACY_SHA_OK computed at import reading files — fine.

  Also `expectations()` at :2011 reads EXPECTATIONS_OUT — inside function, lazy. OK.

  Let me check what search(q) returns exactly — rows list of Rec? For printing names, rows probably Rec objects with .name or dict. Let me read search around 1228-1340 to know the return shape, plus the M7 branch at 1185-1270 and the district branches ~1120-1130, and the phrase/token parts 424-442, 515-533, 664-679.Now I'll build the in-memory runner. Patch lines 68-84 area. Replace:
  - Line 68: REPO_ROOT = pathlib.Path(...) — keep but point somewhere safe. Actually simpler: replace the three path constants lines 73-75 with the actual paths, and line 76/79 to dummy (functions only). OUTDIR :84 points to %TEMP% — fine, only used in main.

  Also LEGACY_BUNDLE_SHA check at :560-563 uses bundle_digests(path) on local files at module level — reads, fine.

  But watch: `expectations()` function reads EXPECTATIONS_OUT — only called in main presumably, or in search? No.

  Also module-level code after line 692 might run sweeps? Line 2749 is inside function presumably. Let me be careful: after exec, call mod.search. The module-level builds RECS, EXACT_NAME, STREET, LOCATIONS — all in-memory. Good.

  Potential issue: place_tokens uses locale? No. Let's do it.

  Queries to run against both old and new data:
  - "кв. Левски", "кв. Тракия", "кв. Христо Ботев", "ж.к. Св. Иван Рилски", "левски", "възраждане 2", "ж.к. възраждане 2", "младост 2", "чайка", "аспарухово", "дружба", "кайсиева градина", "училище възраждане 3", "младост", "училище младост", "училище район младост", "възраждане", "училище възраждане", "детска градина дойран".

  Verify against plan's table §1.7/1.8 and §8.

• Сега пускам двигателя in-memory (read-only) върху old_data и new_data.========== OLD
кв. Левски                   | M3                     |   4 | {None: 4}
кв. Тракия                   | M3                     |   1 | {None: 1}
кв. Христо Ботев             | M3                     |  24 | {'asparuhovo': 1, None: 10, 'vladislavovo': 1, 'kk_konstantin_elena': 2, 'chaika_kk': 1, 'zlatni_pyasatsi': 9}
ж.к. Св. Иван Рилски         | M3                     |  22 | {None: 14, 'mladost2': 1, 'kk_konstantin_elena': 3, 'asparuhovo': 1, 'vladislavovo': 1, 'zlatni_pyasatsi': 2}
левски                       | M3                     |   4 | {None: 4}
възраждане 2                 | M3                     |   0 | {}
ж.к. възраждане 2            | M3                     |   0 | {}
младост 2                    | M3                     |   0 | {}
чайка                        | M7-bare-location       |  29 | {'chaika_kv': 10, None: 1, 'chaika_kk': 18}
аспарухово                   | M7-bare-location       |  16 | {'asparuhovo': 4, None: 12}
дружба                       | M7-bare-location       |   2 | {None: 1, 'druzhba': 1}
кайсиева градина             | M2-failopen            |   3 | {'zlatni_pyasatsi': 1, None: 1, 'chaika_kv': 1}
училище възраждане 3         | M2                     |   2 | {None: 2}
младост                      | M7-bare-location       |  28 | {None: 22, 'mladost': 5, 'mladost2': 1}
училище младост              | A3-location            |  11 | {'mladost': 1, 'mladost2': 1, None: 9}
училище район младост        | A3-district            |  12 | {None: 9, 'mladost': 1, 'vazrazhdane2': 1, 'mladost2': 1}
възраждане                   | M7-bare-location       |   5 | {'vazrazhdane': 3, 'vazrazhdane2': 1, 'vazrazhdane1': 1}
училище възраждане           | A3-location            |   1 | {'vazrazhdane2': 1}
детска градина дойран        | A3-street              |   1 | {None: 1}
бриз                         | M7-bare-location       |   2 | {'zlatni_pyasatsi': 1, 'briz': 1}
========== NEW
кв. Левски                   | M3                     |   4 | {'asparuhovo': 1, None: 2, 'vladislavovo': 1}
кв. Тракия                   | M3                     |   1 | {'dolna_traka': 1}
кв. Христо Ботев             | M3                     |  24 | {'asparuhovo': 1, 'hristo_botev': 1, None: 7, 'vladislavovo': 1, 'kolhozen_pazar': 1, 'tsentar': 1, 'kk_konstantin_elena': 2, 'chaika_kk': 1, 'zlatni_pyasatsi': 9}
ж.к. Св. Иван Рилски         | M3                     |  22 | {None: 9, 'asparuhovo': 3, 'pobeda': 1, 'mladost2': 1, 'kk_konstantin_elena': 3, 'tsentar': 1, 'vladislavovo': 1, 'hristo_botev': 1, 'zlatni_pyasatsi': 2}
левски                       | M7-bare-location       |  14 | {None: 1, 'asparuhovo': 1, 'kv_levski': 12}
възраждане 2                 | M3                     |   0 | {}
ж.к. възраждане 2            | M3                     |   0 | {}
младост 2                    | M3                     |   0 | {}
чайка                        | M7-bare-location       |  30 | {'chaika_kv': 10, None: 1, 'chaika_kk': 19}
аспарухово                   | M7-bare-location       |  16 | {'asparuhovo': 9, None: 7}
дружба                       | M7-bare-location       |   2 | {'kv_levski': 1, 'druzhba': 1}
кайсиева градина             | M2-failopen            |   3 | {'zlatni_pyasatsi': 1, None: 1, 'chaika_kv': 1}
училище възраждане 3         | M2                     |   2 | {'kv_levski': 1, 'trakia': 1}
младост                      | M7-bare-location       |  20 | {None: 12, 'mladost2': 3, 'mladost': 5}
училище младост              | A3-location            |   6 | {'mladost': 1, 'mladost2': 2, None: 3}
училище район младост        | A3-district            |  12 | {'pobeda': 3, None: 3, 'sv_ivan_rilski': 1, 'troshevo': 1, 'mladost': 1, 'mladost2': 2, 'vazrazhdane2': 1}
възраждане                   | M7-bare-location       |   5 | {'vazrazhdane': 3, 'vazrazhdane2': 1, 'vazrazhdane1': 1}
училище възраждане           | A3-location            |   1 | {'vazrazhdane2': 1}
детска градина дойран        | A3-street              |   1 | {None: 1}
бриз                         | M7-bare-location       |   4 | {'zlatni_pyasatsi': 1, 'briz': 3}


• Excellent. Results confirm the plan's measured numbers almost exactly:

  - §1.8.4: "кв. Левски" M3 4 rows, zero kv_levski ✓ (new: asparuhovo 1, None 2, vladislavovo 1 — 0 kv_levski ✓). "кв. Тракия" M3 1 row ✓ (dolna_traka — wait, plan says "нула с търсения код"; the 1 row has dolna_traka, not trakia ✓). "кв. Христо Ботев" M3 24 ✓ with hristo_botev: 1 — wait, plan 1.8.4 says "нула с търсения код" for all four! But new run shows hristo_botev: 1 in "кв. Христо Ботев". Hmm — let me check: plan says 1.8.4: „кв. Левски" / „кв. Тракия" / „кв. Христо Ботев" / „ж.к. Св. Иван Рилски" → M3, съответно 4 / 1 / 24 / 22 реда, нула с търсения код. My measurement shows one row with code hristo_botev among the 24. Let me identify that row — it might be named "Христо Ботев" matching by name rather than by quarter. The claim "нула с търсения код" (zero rows with the searched code) is FALSE for hristo_botev — 1 row carries hristo_botev. That's a discrepancy to check carefully. Which row is it? Possibly a school named after Христо Ботев located in кв. Христо Ботев — found by name tokens (M3 = name match, not location match). The plan's claim was "нула с търсения код" — my count shows 1 with the code. Need to print row names.

  - §1.8.5 "левски" → M7-bare 14 rows, 12 with kv_levski ✓.
  - §1.8.6: "възраждане 2" / "ж.к. възраждане 2" / "младост 2" → 0 rows ✓ (M3, 0).
  - §1.8.7: "чайка" → M7-bare 30 rows ✓ (29 old; plan says 30 new ✓), mixed chaika_kk 19 + chaika_kv 10 ✓.
  - §1.8.8: "аспарухово" → 16 ✓ (plan says "без ЦДГ 43 Пинокио" — need name check; the None: 7 rows — check if Пинокио among them), "дружба" → 2 ✓.
  - §1.8.9: "кайсиева градина" → M2-failopen 3 ✓; "училище възраждане 3" → M2 2 ✓ (kv_levski + trakia — plan §8 says 3 ОУ Ангел Кънчев [кв. Левски] and III ПМГ [кв. Тракия] ✓).
  - §1.7: "младост" 28→20 ✓ (M7-bare). Plan says new 20 (8/12) — mine: mladost 5 + mladost2 3 = 8 with quarter, 12 without ✓. Old 28 (6/22): mine old shows mladost 5, mladost2 1 = 6, None 22 ✓.
  - "училище младост" 11→6 ✓ (A3-location), new 3 with quarter ✓ (mladost 1 + mladost2 2 = 3 ✓).
  - "училище район младост" A3-district 12 ✓, new "9 с квартал" — mine: pobeda 3 + sv_ivan_rilski 1 + troshevo 1 + mladost 1 + mladost2 2 + vazrazhdane2 1 = 9 ✓. Plan §1.7 says "6 сменени zone" — new quarters among the 12 vs old 3: old had mladost 1, vazrazhdane2 1, mladost2 1 = 3; new 9 → 6 changed ✓.
  - "възраждане" 5 ✓, "училище възраждане" 1 ✓ (vazrazhdane2 — plan says II ОУ Вапцаров; row shows vazrazhdane2 code — plan §1.7 says "училище възраждане → 1 (II ОУ Никола Йонков Вапцаров)" — check name).
  - "детска градина дойран" A3-street 1 ✓.
  - "бриз" — plan §8 probe 5: "бриз" → IV ЕГ Жолио Кюри and ПГ Менделеев — two new SIGNED_POLYGON rows. My new run: 4 rows (zlatni_pyasatsi 1, briz 3). Old: 2 rows (zlatni 1, briz 1). Hmm plan says probe 5 expects 2 rows: IV ЕГ and ПГ Менделеев. But new data gives 4 rows for "бриз": 3 with briz + 1 zlatni. Discrepancy! Old had 2 rows. New has 4. Plan §8 probe 5 says "`бриз` → IV ЕГ Жолио Кюри и ПГ „Д. И. Менделеев" — двата нови SIGNED_POLYGON реда." That implies 2 rows total. My measurement: 4. Need names to verify.

  Also §8 probe 7: "аспарухово → 16 реда без ЦДГ 43 Пинокио" — my count 16 ✓; check names for Пинокио absence.

  §8 probe 4: "левски" → 14 rows, 12 kv_levski ✓ names: I ЕГ, Технически университет, ДГ№10 Карамфилче, хотел Сорбона. And "кв. Левски" → 4 чужди реда: НУ Васил Левски [Аспарухово], ПГ Васил Левски [район Младост], ДГ№40 [Владиславово], болница Лисичкова. My new run: asparuhovo 1, None 2, vladislavovo 1 ✓ 4 rows, 0 kv_levski ✓.

  §8 probe 1: "Кайсиева градина" → 3 rows M2-failopen, no quarter rows in our section... my run: zlatni_pyasatsi 1, None 1, chaika_kv 1 — all have quarters except one None. Plan says "няма квартални редове (3 реда M2-failopen)". Hmm — 2 of the 3 rows HAVE quarters (zlatni, chaika_kv). "в нашата секция — няма квартални редове" maybe means no rows found by quarter semantics (M2-failopen is name/noise). Fine.

  Now the key discrepancies to nail down:
  1. hristo_botev:1 in "кв. Христо Ботев" — plan 1.8.4 claims zero rows with searched code. 
  2. "бриз" → 4 rows vs plan §8 probe 5 implying 2.
  3. Fixture 5 "parent_child (Младост)": A3-location, 6, 3 with quarter ✓ matches "училище младост".
  4. Fixture 3 "mladost_kind_collision": M7-bare-location, 20, 8/12 ✓.
  5. Fixture 6: (а) "възраждане" → 5 ✓; (б) "възраждане 2" → 0 ✓; (в) "ж.к. възраждане 2" → 0 ✓.
  6. Fixture 7: "чайка" → 30 ✓.
  7. Fixture 8: "аспарухово" → 16, без Пинокио; "дружба" → 2 ✓.

  Print names for: "кв. Христо Ботев" (the hristo_botev row), "бриз" (4 rows), "аспарухово" (check Пинокио), "дружба" (2 rows), "младост" old vs new to identify the 8 lost rows, "училище младост" old vs new (11→6), "чайка" old 29 vs new 30 (which row added), "кв. Левски" names, "училище възраждане" name.### NEW кв. Христо Ботев
    ОУ Христо Ботев | кв. Аспарухово | asparuhovo
    ЦДГ 8 - Христо Ботев | кв. Христо Ботев | hristo_botev
    Национално училище по изкуствата "Добри Христов" | район Одесос | None
    Хотел-ресторант „Комитово ханче“ | кв. Владиславово | vladislavovo
    Hotel Color | Колхозен пазар | kolhozen_pazar
    Hugo Hotel | район Одесос | None
    БИЗАР ХОТЕЛ | район Одесос | None
    Family Hotel Astra | Център | tsentar
    ГРАНД ХОТЕЛ ЛОНДОН | район Одесос | None
    Мотел „Иванчов хан“ | к.к. Св. Св. Константин и Елена | kk_konstantin_elena
    Hotel Bona Vita | район Приморски | None
    Хотел „Журналист“ / МДЖ | к.к. Чайка | chaika_kk
    ПАРК ХОТЕЛ БЕЛВЮ | к.к. Златни пясъци | zlatni_pyasatsi
    ХОТЕЛ  ХЕЛИОС СПА | к.к. Златни пясъци | zlatni_pyasatsi
    ПАРК ХОТЕЛ ОДЕСОС | к.к. Златни пясъци | zlatni_pyasatsi
    ПАРК-ХОТЕЛ ТИНТЯВА | к.к. Златни пясъци | zlatni_pyasatsi
    КЛУБ ХОТЕЛ БОЛЕРО | к.к. Златни пясъци | zlatni_pyasatsi
    ПАРК ХОТЕЛ БРИЗ | к.к. Златни пясъци | zlatni_pyasatsi
    РОСЛИН ДИМЯТ ХОТЕЛ ВАРНА | район Приморски | None
    Art Green Boutique Hotel | район Одесос | None
    ПРЕСТИЖ ХОТЕЛ И АКВАПАРК | к.к. Златни пясъци | zlatni_pyasatsi
    ПАРК ХОТЕЛ ГОЛДЪН БИЙЧ | к.к. Златни пясъци | zlatni_pyasatsi
    ЕНСАНА АКВАХУС ХЕЛТ СПА ХОТЕЛ | к.к. Св. Св. Константин и Елена | kk_konstantin_elena
    ПРЕСТИЖ ГРАНД ХОТЕЛ И АКВАПАРК | к.к. Златни пясъци | zlatni_pyasatsi
### NEW бриз
    ПАРК ХОТЕЛ БРИЗ | к.к. Златни пясъци | zlatni_pyasatsi
    IV ЕГ Жолио Кюри | ж.к. Бриз | briz
    Професионална гимназия по химични и хранително-вкусови технологии "Д. И. Менделеев" | ж.к. Бриз | briz
    Камелия | ж.к. Бриз | briz
### NEW кв. Левски
    НУ Васил Левски | кв. Аспарухово | asparuhovo
    ПГ по строителство, архитектура и геодезия "Васил Левски" | район Младост | None
    ДГ№40 „Детски свят“ | кв. Владиславово | vladislavovo
    „Специализирана болница за активно лечение по детски болести – доктор Лисичкова“ ЕООД | район Младост | None
### NEW дружба
    ОДГ №14 "Дружба" | кв. Левски | kv_levski
    ЦДГ 43 "Пинокио" | ж.к. Дружба | druzhba
### аспарухово NEW — Пинокио present?
[]
### аспарухово OLD — Пинокио?
[] | old count 16
### младост: OLD vs NEW names
lost from old: ['ОУ „Иван Вазов“', 'Професионална гимназия по електротехника', 'Професионална Техническа Гимназия', 'ДГ№53 „Слънчево зайче“', 'ОУ Отец Паисий', 'ДГ№26 „Изворче"', 'ОУ Добри Чинтулов', 'ДГ 24 "Детско градче"']
gained in new: []
### училище младост: OLD vs NEW
lost: ['ОУ „Иван Вазов“', 'Професионална гимназия по електротехника', 'Професионална Техническа Гимназия', 'ОУ Отец Паисий', 'ОУ Добри Чинтулов']
### чайка OLD vs NEW
gained: ['Nikea / Nikeya Park'] lost: []
### училище възраждане NEW
[('II ОУ „Никола Йонков Вапцаров“', 'ж.к. Възраждане 2', 'vazrazhdane2')]
### училище район младост NEW zone changes vs OLD
    ОУ „Иван Вазов“ | район Младост -> ж.к. Победа | pobeda
    Професионална гимназия по електротехника | район Младост -> ж.к. Победа | pobeda
    Професионална Техническа Гимназия | район Младост -> ж.к. Победа | pobeda
    ПГГСД „Николай Хайтов“ | район Младост -> район Младост | None
    ОУ „Свети Иван Рилски“ | район Младост -> район Младост | None
    ОУ Отец Паисий | район Младост -> кв. Св. Иван Рилски | sv_ivan_rilski
    ОУ Добри Чинтулов | район Младост -> кв. Трошево | troshevo
    СУ „Неофит Бозвели“ | ж.к. Младост -> ж.к. Младост | mladost
    СУ „Гео Милев“ | район Младост -> ж.к. Младост 2 | mladost2
    II ОУ „Никола Йонков Вапцаров“ | ж.к. Възраждане 2 -> ж.к. Възраждане 2 | vazrazhdane2
    ПГИ „Д-р Иван Богоров“ | ж.к. Младост 2 -> ж.к. Младост 2 | mladost2
    ПГ по строителство, архитектура и геодезия "Васил Левски" | район Младост -> район Младост | None
Very productive. Key findings:

  1. **1.8.4 discrepancy**: "кв. Христо Ботев" → 24 rows, and one of them (ЦДГ 8 - Христо Ботев) carries code `hristo_botev`. Plan says "нула с търсения код" — FALSE: 1 row has the searched code. But note: it's found via M3 (name match), not via the quarter mechanism. The claim "нула с търсения код" as a count over the result set is measurably wrong (1 ≠ 0). Also "кв. Тракия" → 1 row with `dolna_traka` — the plan §8 probe 4 says "кв. Тракия (1 чужд ред)". Mine: 1 row — which is it? Let me note: the row has dolna_traka code. Fine.

  2. **§8 probe 5 "бриз"**: plan expects "IV ЕГ Жолио Кюри и ПГ Менделеев — двата нови SIGNED_POLYGON реда". Measured: 4 rows — plus ПАРК ХОТЕЛ БРИЗ (zlatni_pyasatsi, name match) and Камелия (briz). Old: 2 rows (ПАРК ХОТЕЛ БРИЗ + ?). Actually old "бриз" was 2 rows: zlatni_pyasatsi 1, briz 1 — briz 1 = Камелия presumably (it had briz before? Камелия's zone old — need check). Actually old count shows briz:1 — some row already had briz in old data (Камелия likely, REG/KAIS). So probe 5's phrasing "двата нови SIGNED_POLYGON реда" is fine as an expectation of *new* rows, but the probe table says "очакваш: IV ЕГ Жолио Кюри и ПГ Менделеев" — could mislead since result is 4 rows including Камелия and ПАРК ХОТЕЛ БРИЗ. Minor.

  3. **О14 / "младост" 28→20**: the 8 lost rows: ОУ Иван Вазов, ПГ по електротехника, ПТГ, ДГ№53 Слънчево зайче, ОУ Отец Паисий, ДГ№26 Изворче, ОУ Добри Чинтулов, ДГ 24 Детско градче. Plan §1.7 names only 5 schools (Вазов, ПГЕ, ПТГ → pobeda; Отец Паисий → sv_ivan_rilski; Чинтулов → troshevo). But there are 8 lost rows — three more are детски градини (ДГ№53 Слънчево зайче, ДГ№26 Изворче, ДГ 24 Детско градче). Where did they go? They now have quarters (probably pobeda/sv_ivan_rilski/troshevo or others). Why do they leave the "младост" result? Because M7-bare-location matches zone phrase: old zone "район Младост" contains token "младост"? Wait — bare_location_rows presumably matches rows whose zone words include the query. Old zone "район Младост" → matches "младост". New zone "ж.к. Победа" → no longer matches. So the 8 lost = 5 schools + 3 kindergartens that got real quarters. Plan §1.7 attributes the loss to "пет училища" only — misses the 3 kindergartens in the поименно explanation. The count 28→20 is right, but the explanation "пет училища напускат" is incomplete (8 rows: 5 училища + 3 детски градини). Check where the 3 ДГ went.

  Also verify the "всичко ВЪТРЕ в квартала" design question: those 8 rows are inside *some* quarter (Pobeda etc.), which is inside район Младост. Query "младост" is a *quarter* phrase (ж.к. Младост), not the district. The design "всичко ВЪТРЕ в квартала" concerns quarter queries; "младост" is ambiguous between ж.к. Младост and район Младост — M7-bare treats it as location phrase matching zones "ж.к. Младост"/"ж.к. Младост 2" and previously "район Младост". So the loss is: rows in *other* quarters of district Младост no longer appear under "младост". By the signed design ("училище район младост" is the district query — explicit), the bare "младост" arguably should be the quarter. The plan handles it via O14 (signed losses). Acceptable? The explicit district query still returns 12 ✓ (probe 9). So the loss is defensible but must be signed — the plan does that (О14, решение implicit via queue). But the plan's поименно explanation is wrong/incomplete: 5 schools named, 8 rows actually lost, and the three kindergartens are unnamed. Condition.

  4. **"училище младост" 11→6**: lost 5 (the 5 schools) ✓ plan's claim "пет училища" matches this query exactly. But §1.7 ties the explanation to this query while the "младост" query loses 8. Fine.

  5. Fixture checks §3.5:
  - Fixture 8 claims "аспарухово → 16 реда, без ЦДГ 43 Пинокио (druzhba)". Measured: 16 rows, no Пинокио ✓. But note "дружба" → 2 rows: ОДГ №14 Дружба (kv_levski! — by name match) + ЦДГ 43 Пинокио (druzhba). So ОДГ №14 "Дружба" is in кв. Левски and appears via its name. The claim "druzhba ⊂ asparuhovo не работи" — Пинокио has druzhba code and doesn't appear under "аспарухово" ✓ (16 rows, no Пинокио — and old also 16 without Пинокио: so this behavior is unchanged, freezing existing behavior ✓ consistent with "замразява измереното").
  - Fixture 6 broken: "кодът на ДГ№34 Лястовичка → vazrazhdane1_new → родителят връща 4". Hmm — if you mutate Лястовичка's code to an unknown code, "възраждане" should return 5-1=4 ✓ plausible if Лястовичка is one of the 5. Check: is ДГ№34 Лястовичка in the "възраждане" 5? Need name list. Also (б)/(в) claim 0 rows ✓ measured.
  - Fixture 7: "чайка → 30" ✓; broken: rename chaika_kv name to something without "Чайка" → merge disappears. Wait — the phrase map is built from zone *names* in the dictionary (place_categories locations), not from row names. chaika_kv's dictionary name is "кв. Чайка". Renaming the *zone name* in the dictionary would remove the phrase. The fixture says "смени името на chaika_kv" — ambiguous: dictionary entry name or row zone? The M7 branch matches zone phrase via row zone strings presumably. Row zones for chaika_kv = "кв. Чайка". So mutating row zone names works. Plausible.
  - Fixture 9 (Node): depends on the slice mechanics; verifiable only at build. The _broken (a): QUARTER_SRC without SIGNED_POLYGON in slice text → places2=[] and RECS.length===225 — matches 1.6 measurement (42 bad places rows → validatePlaces2 false → places2=[], hotels stay 225) ✓.
  - Fixture 10 _broken: "махни ownQuarter от :7118 → училище младост 6 → 5 (измерено)". Hmm. With a synthetic fallback row... the claim is about the synthetic row. Can't measure directly; but the claim "(б) остава в отговора на ГОЛАТА заявка училище младост (клон :7118)" — wait, :7118 is the district branch inside... need to check index_excerpts for :7064/:7118 semantics. The bare query "младост" M7 — how does ownQuarter affect it? For the synthetic fallback row (quarter = district), the M7 branch at :7064 `!r.e.quarter`... Let me read index_excerpts.

  6. О15 cheaper fix question: "кв. Левски" — the tokens: "кв." → token kv (length 2, not significant), "левски" significant. Query class: no key ("кв" is... wait M7 requires bare_location_query(R) where R = all tokens (no key). "кв. левски" → R = [kv, levski]; significant check: kv fails → M7 not taken → falls to M3. But wait, why does "кв. Христо Ботев" return 24 rows via M3? Because gen gate passes (hotel class ≤300?), then scored by name tokens: "левски"/"ботев" match names. So the fix... A cheaper fix than D12: add aliases with prefix forms to the dictionary? The dictionary aliases for kv_levski are ["Васил Левски", "кв. Васил Левски", "Левски"] — "кв. Левски" the exact typed query isn't an alias; adding alias "кв. Левски" would make... how do aliases enter search? location_phrases(entries, added) builds phrases from names+aliases. Phrase "кв васил левски" — tokens kv(v?), "кв."→"kv" length 2 not significant → phrase tokens significant = [vasil, levski]? If phrases are built from significant tokens only, then "кв. Васил Левски" phrase = "васил левски". Query "кв. Левски" remainder significant = [levski] — doesn't equal phrase "васил левски" (M3 location match needs exact phrase?). Actually M7 bare_location_rows — let me read lines 424-442 & 515-533 & bare_location_rows to understand. The plan's claim "по-евтина поправка която планът пропуска" — the task asks me to check whether a cheaper fix exists that the plan misses. Candidate: in isSignificantToken/bare_location_query, drop known type-prefix tokens (kv, zh, k, kk...) from R before the significance test — i.e., treat "кв. Левски" as bare location "левски". That's a ~3-line client change + reference change, much cheaper than full D12 normalizer (which does phrase identity, conjunctions, numbers, directions). The plan says D12 deferred to Б5 "with new parity corpus". A cheaper fix: filter the closed list of type prefixes in bare_location_query only. But that changes behavior of the frozen reference → still needs re-freeze and parity; but it does NOT need locationKey in the parity corpus or phrase canonicalization. The plan's О15 says "Ако Петър каже „сега" — това е друг лот с нов паритетен корпус и нов кръг делти". A cheaper option exists (prefix-skip in bare_location_query + significant_token exception for the closed prefix list) that would fix exactly the four failing typed queries, and could arguably ride in Б3. But it changes engine behavior — needs frozen expectations update. The plan chose to defer; is that "пропуска"? The task asks "има ли по-евтина поправка, която планът пропуска". I should verify by reading bare_location_query and significant_token and the excerpt of index.html.

  Also check: does "кв. левски" hit exact_alias? No (4 rows M3). 

  7. О16 minimal signed path: DAG doesn't enter (parents 0 of 28 in delivery ✓ — confirmed: parents nonzero: [] ). "дете → детето не работи" — confirmed ("възраждане 2" → 0). Minimal signed path: plan §3.7 says the honest carrier is `locations.quarter[<code>].parents: [<code>]` in place_categories — lot Б5. That's consistent.

  8. О19: six places — recall_sweep :621,:623,:1123,:1167,:2146,:2150 + two bundle tests. Verify these lines exist and do what the plan claims. :1123/:1167 in this copy? The copy's recall_sweep is 4334 lines; line numbers: check :621/:623 (Rec qtk/qph), :1123, :1167, :2146, :2150.

  9. О20: two labels — verify zone invariance measured: rows with quarter all have zone == quarter.name (258/258 ✓ measured). And the JS :6544 requires zone === quarter.name — so a fallback row (quarter.name = district name, zone = "район X") would fail today → И6 both labels. Consistent.

  10. О22: 138 — I could not reproduce (got 57 zone changes old→new; baseline f06ac06 unavailable in the copy). Report honestly: old→new = 57 zone changes (42+15), all unnamed→named, 0 lost/0 changed in the named→named/named→unnamed sense. The 138 must include baseline-vs-HEAD differences. Wait — actually, maybe coverage counts rows where the zone *label* changed including gains: 42 places + 15 hotels = 57 "changed"... 138 = 44+44+39+11. Hmm, 44+44 = 88 places, 39+11 = 50 hotels. If baseline f06ac06 differs from HEAD f00dd78 in more rows... §1.1 says HEAD f00dd78, ahead 81 commits; baseline f06ac06 signed 05.09. Between them there could be data changes (e.g., the "ИЗЧИСТВАНЕ" lot?). Actually the 05.09 delivery A was at fd13907 (published). f06ac06 is the baseline rev. Since old_data = today's data (f00dd78), and f06ac06 is older, extra diffs are plausible. So: cannot reproduce 138 in this copy; the plan itself treats it as STOP-number to re-measure (§4 стъпка 2). I'll state: not reproducible here; old→new gives 57, so the 138's correctness depends on f06ac06 content not present in the copy — condition: the allow must be generated mechanically from coverage output (the plan already requires that in §4 стъпка 9). Actually the task says "преброй ги сам: zone_named lost/changed по old→new" — answer: по old→new lost 0 / changed 57 (all gains from район→квартал); 138 is not old→new, it's f06ac06→new. Good enough.

  Let me now read index_excerpts.txt for the relevant anchors, and recall_sweep lines 424-442, 515-533, 621-623, 664-679, 1120-1170, 2140-2155.

• Сега проверявам котвите в `index_excerpts.txt` и съответните редове на `recall_sweep.py`.

• The excerpts confirm the client mechanics. Key: `isSignificantToken` at excerpt line 108 (= index.html:6495-6496 per plan): `!t.num && t.orig.length > 2 && t.s.length > 2 && ADDR.indexOf(t.orig) < 0 && !GENERIC_WORDS.has(t.s)`. "кв." → orig "кв." — hmm, orig includes the dot? placeTokens probably strips; t.orig "кв." length 3 > 2! Wait — "кв." with the dot is 3 chars, so orig.length > 2 passes? But t.s (skeleton) "kv" length 2 fails `t.s.length > 2`. So excluded by s.length. OK.

  M7 branch (excerpt 258-268): bare location query requires R.every(isSignificantToken). "кв. Левски" → R = [кв, левски], кв not significant → M7 skipped → falls into M3 name scoring → 4 rows by name. Confirmed by measurement.

  Cheaper fix for О15: The question — is there a cheaper fix the plan misses? Options:
  (a) In the M7 guard and phrase building, drop the closed list of type-prefix tokens (kv, zh, k, kk, m, s, o, zh.k...) from R — then "кв. Левски" = bare "левски" → 14 rows incl. 12 kv_levski. That's a small, local change in 2 engines (bare_location_query/significant filter), no new parity surface (no locationKey), no phrase canonicalization. But it changes M3-vs-M7 routing for any query with type prefix. Risk: "кв." + name of a *street*? Streets have own markers (ул/бул/пл) separate. The prefix list is closed (M7_PREFIXES in recall_sweep :3093 exists already! `(u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")` — interesting, there's already an M7_PREFIXES constant). So the engine already knows the prefix list. A minimal fix: in bare_location_query, allow R tokens that are in M7_PREFIXES to be ignored. That would fix exactly the measured failures ("кв. Левски" etc.) without D12's full normalizer. It still needs expectations re-freeze (the reference changes behavior), but it doesn't need a new parity corpus or `locationKey` on the client. So yes — the plan's framing "D12 or nothing" misses a cheaper middle path. But is it signed-safe? It changes answers for existing queries (e.g. "ж.к. Младост" today → ? let me test: "ж.к. младост" — probably M3 with name noise today; after fix → M7-bare 20 rows). It's a behavior change requiring the same signing machinery (queue rows, freeze). The plan's О15 offers "ако Петър каже сега — друг лот". The cheaper fix would still be a behavior change — arguably belongs in the same deferred lot Б5, but it's cheaper than full D12 (no locationKey parity, no phrase identity). So: the plan is not wrong to defer, but О15's claim that doing it now = "нов паритетен корпус и нов кръг делти" (i.e., full D12) overstates the cost; a prefix-skip fix is much smaller. That's a valid К28 finding (minor/major).

  Let me check M7_PREFIXES usage to confirm the list exists for exactly this.

  Also check "възраждане 2" mechanics: R = [възраждане, 2]; "2" is t.num → not significant → M7 skipped → M3 gate → cls gen_ok... 0 rows because M3 name scoring: no name contains "възраждане" + number 2? Actually returns [] M3. Meanwhile bare "възраждане" → M7-bare 5. So child query fails because the number kills M7. Cheaper fix same as above (numbers in M7: the plan's D12 "пази числата"). Actually for "възраждане 2", the phrase for vazrazhdane2 is "възраждане 2"? Phrases are built from significant tokens — numbers are dropped → phrase "възраждане", colliding with parent. That's why M7 on bare "възраждане" merges parent+children (shared phrase). And "възраждане 2" fails since the number token isn't significant. A fix keeping numbers as significant in M7 context would give child its own phrase. But qtk/qph are built from significant tokens (numbers excluded) so phrase of vazrazhdane2 = "възраждане" — even with number kept in query, no row's phrase contains "2" → the query wouldn't match. So child phrase needs numbers kept at phrase-build time — that's exactly D12's "пази числата" on the index side. So the "дете→детето" fix genuinely requires index-side change (phrase building keeps numbers), which is D12-ish. Minimal signed path = the plan's О16 freeze is honest.

  For "дружба ⊂ асарухово": phrase map has no relation; only parents[] in dictionary could carry it — delivery has parents 0 of 28 ✓. Plan §3.7 confirms.

  Now О19: verify recall_sweep.py:621,623,1123,1167,2146,2150 and test_places_public_bundle.py:291-293,:309. Let me read those.

  Also verify fixture-related: test_granitsi_fixtures.py current state (5 fixtures, 2 deferred) and granitsi_fixtures_06.09.json.

  Also §3.3 pinned numbers vs test file: read test_places_public_bundle.py lines 55-57, 80, 88-89 etc. Note: plan §3.3 references `tests/test_hotels_public_bundle.py` which is NOT in the copy (only test_places_public_bundle.py). Fine.

  Also check the "К27" citation in О18: "местност никога не пълни quarter" — from СЪСТОЯНИЕ §7 К27 ✓ (reads: "местност никога не пълни quarter" — yes, in К27 answer (2): "местност никога не пълни quarter"). ✓

  Check ADR 010 D12/D13 citations: D12 line 60 of ADR ✓ (we read it — it contains locationKey parity 759 strings). О15 cites ADR D12 correctly.

  Now read recall_sweep specific lines.        self.district = h.get("district") or None
        self.locality = h.get("locality") or None
        self.p7 = []
        self.qtk = self._loc_tokens(u"quarter", self.quarter)
        self.ltk = self._loc_tokens(u"locality", self.locality)
        self.qph = self._loc_phrases(u"quarter", self.quarter)
        self.lph = self._loc_phrases(u"locality", self.locality)
        self.dph = self._loc_phrases(u"district", self.district)
        self.bundle = bundle                              # „hotels“ | „places“
    if not R:
        return None
    phrase = u" ".join(t.s for t in R)
    q_rows = [r for r in cls if phrase in r.qph]
    l_rows = [r for r in cls if phrase in r.lph or phrase in r.gph]
    d_rows = [r for r in cls if r.quarter is None and phrase in r.dph]
    if not (q_rows or l_rows or d_rows):
        return None
    return order_category(q_rows), order_category(l_rows), order_category(d_rows)


    phrase = u" ".join(tokens)
    # The exact-name head of ЛОТ 1 decision 1 keeps a record whose own NAME is
    # the phrase above the location rows it happens to share the word with.
    head = order_category([r for r in cls if name_has_phrase(r, R)])
    district_hit = [r for r in cls if r.quarter is None and phrase in r.dph]
    return stable_unique(head + order_category(quarter_hit)
                         + order_category(locality_hit) + order_category(district_hit))


def bare_location_query(R):
                   u"старите зонови думи са изключени (fail-closed)")
    for r in RECS:
        if not r.district or r.district.get("code") not in DISTRICT_CODES:
            bad.append(u"%s: район извън затворения списък (%s)"
                       % (r.name, json.dumps(r.district, ensure_ascii=False)))
            continue
        want = (r.quarter or {}).get("name") or (u"район " + r.district["name"])
        if r.zone != want:
            bad.append(u"%s: `zone` = %s, а типовите полета дават %s"
                       % (r.name, r.zone, want))
        if r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]:
            bad.append(u"%s: квартал извън речника (%s)" % (r.name, r.quarter.get("code")))
        if r.locality and r.locality.get("code") not in LOCATIONS[u"locality"]:
            bad.append(u"%s: допълнително място извън речника (%s)"
                       % (r.name, r.locality.get("code")))
        if r.zone in r.legacy:
            bad.append(u"%s: старата зонова дума е и показваната зона (%s)"
#     ordinals of „Възраждане 1/2“ all reach `qtk`/`ltk` as tokens of their own,
#     and before F12-е „к“ answered with 163 rows and „кв“ with 36;
#   · a place a human really types must still answer through the branch.
M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")
M7_PLACES = (u"zlatni", u"mladost", u"chaika", u"zpz", u"vilite",
             u"златни пясъци", u"младост")
M7_BRANCH = u"M7-bare-location"


def failing_queries(bad):
    """The unique queries a gate complains about.
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
# G2 override: the corrupted copy is fed in through the environment, not by editing data/.
PLACES = pathlib.Path(os.environ.get("FIRE_VARNA_PLACES_PATH") or (REPO / "data" / "places.json"))

# The tracked LF blob, measured at C11 (varna_3d HEAD ba78a25, branch rezhimi):
#   git -C ../varna_3d show HEAD:data/fire_varna_places.json > data/places.json
# F12 (P7 = М2 + М3 + М6, commit adad6b0): the delivery was re-exported — М2 stopped
# dropping a typed location on `map_label: false`, so five more places carry a quarter
# — and the three numbers are re-measured on the NEW blob. The docstring rule holds:
# a drift is a re-delivery, and this IS the re-delivery.
# 121 621 B / 35aaf0cd5811… → the values below.
PLACES_SHA256 = "329310f577e8353673b9014af99624a78ab825fb0ad53e93fc572a28660d88c0"
PLACES_BYTES = 122089
PLACES_GZIP9 = 13728

EXPECTED_COUNT = 150
TOP_LEVEL_KEYS = {"_meta", "places"}
            self.assertIsInstance(rec["name"], str)
            self.assertTrue(rec["name"].strip(), rec)
            lat, lon = rec["lat"], rec["lon"]
            self.assertIsInstance(lat, (int, float))
            self.assertIsInstance(lon, (int, float))
            self.assertTrue(min_lat <= lat <= max_lat, rec)
            self.assertTrue(min_lon <= lon <= max_lon, rec)

    def test_every_typed_location_is_null_or_the_closed_three_key_object(self):
        """ЛОТ 1в-В (S1): {name, src, code}, all three non-empty, from closed lists."""
        for rec in self.records:
            for field, srcs, codes in (("quarter", QUARTER_SRC, QUARTER_CODES),
                                       ("locality", QUARTER_SRC, LOCALITY_CODES),
                                       ("district", DISTRICT_SRC, DISTRICT_CODES)):
                value = rec[field]
                if value is None:
                    self.assertNotEqual(field, "district", rec["name"])
                    continue
                self.assertIsInstance(value, dict, rec["name"])
                self.assertEqual(set(value), LOCATION_KEYS, rec["name"])
                for key in LOCATION_KEYS:
                    self.assertIsInstance(value[key], str, rec["name"])
                    self.assertTrue(value[key].strip(), rec["name"])
                self.assertIn(value["src"], srcs, rec["name"])
                self.assertIn(value["code"], codes, rec["name"])

    def test_the_compat_label_follows_from_the_typed_fields(self):
        """S1: `zone` === quarter?.name ?? „район “ + district.name — nothing else."""
        for rec in self.records:
            want = rec["quarter"]["name"] if rec["quarter"] else "район " + rec["district"]["name"]
            self.assertEqual(rec["zone"], want, rec["name"])

    def test_the_district_covers_every_record(self):
        """S4: 100 % and the five city districts, measured — not assumed."""
        self.assertEqual(sum(1 for r in self.records if r["district"]), len(self.records))
        self.assertEqual({r["district"]["code"] for r in self.records} - DISTRICT_CODES, set())
Confirmed:
  - recall_sweep.py:621/623 are qtk/qph (close to claimed :621/:623 — actual 621=`self.qtk`, 623=`self.qph` ✓).
  - :1123 is `d_rows = [r for r in cls if r.quarter is None ...]` ✓ (in location_rows).
  - :1167 `district_hit = [… if r.quarter is None …]` ✓ (bare_location_rows presumably).
  - :2146 `want = (r.quarter or {}).get("name") or (u"район " + …)` ✓ and :2150 `if r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]` ✓ — both in the qa function. These confirm О19's claim that the reference engine has the same `quarter is None` semantics reversed for fallback rows.
  - test_places_public_bundle.py:291-293 area — the locality validated with QUARTER_SRC ✓ (line ~292: `("locality", QUARTER_SRC, LOCALITY_CODES)`), and :309 `want = rec["quarter"]["name"] if rec["quarter"] else "район " + …` ✓. Confirms О18/О19/О20 readings.

  M7_PREFIXES exists at :3093 with (k, kv, zh, m, s, o, t, i, 1, 2) — the engine already enumerates the prefix tokens (used in failing-queries gate context). This supports the "cheaper fix exists" observation for О15: a prefix-skip in bare_location_query (both engines) using an already-named closed list.

  Now the fixtures: read test_granitsi_fixtures.py and granitsi_fixtures_06.09.json to assess §3.5's eleven fixtures against the harness (EXPECTED_NAMES 5, mutations keyed by name, branch optional for Node, etc.).

• О19/О20 котвите са верни. Сега фикстурният харнес и фикстурите.

• Now granitsi_fixtures_06.09.json — read the fixture file to see the five fixtures and their content. It's 855 lines/32KB. Let me read key parts._meta keys: ['attribution', 'deferred', 'delivery', 'engine', 'geometry', 'inputs', 'lot', 'measured_at', 'measured_by', 'plan', 'purpose', 'status']
_meta.status: measured_not_signed
deferred: 
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "C:\Program Files\Python310\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode characters in position 25-32: character maps to <undefined>
deferred: {"client_cache_matrix": "Отложена: браузърно поведение (кеш v6/v7, crypto on/off, двата булеви валидатора), а единственият node-изпълнител в tests/ днес е test_data_ascii_mojibake.py; Н3-а не назовава втори. Влиза в Б3 (план §6 Б3), не тази нощ.", "parent_child_vazrazhdane": "Отложена: vazrazhdane1..4 нямат `parents` в config/quarter_registry.json (сутрешен дълг, план §5 т. 9); затова родителската двойка тази нощ е mladost/mladost2."}
inputs: ['data/hotels.json', 'data/places.json', 'data/place_categories.json']
--- street_collision | query: детска градина дойран | today: A3-street 1 wq 0 woq 1
    broken: На ДГ 30 "Синчец" — ДРУГ запис от същия клас, не търсеният — се записва quarter {"name": "кв. Дойран", "code": "doyran", "src": "SIGNED_POLYGON"}: измислен квартал-съименник на улицата. Резултат: клонът A3-street умира, отговорът е чуждият запис, а редът на ул. Дойран се губи.
    observed: A3-category+zone/kind 1 | set_identical: False
--- district_retention | query: училище район младост | today: A3-district 12 wq 3 woq 9
    broken: На ОУ Отец Паисий се записва quarter {"name": "район Младост", "code": "mladost_district", "src": "DISTRICT_FALLBACK"} И `district` става null — както би направил износ, който пише резервния квартал върху районното поле. Резултат: редът изчезва от районното търсене, 12 → 11.
    observed: A3-district 11 | set_identical: False
--- mladost_kind_collision | query: младост | today: M7-bare-location 28 wq 6 woq 22
    broken: На ДГ№53 „Слънчево зайче“ (район Младост, днес без квартал) се записва quarter {"name": "район Младост", "code": "mladost_district", "src": "DISTRICT_FALLBACK"} — районът в квартално поле. Резултат: редът напуска районната страна и влиза в кварталната по ИМЕТО на полето (кодът е непознат на речника), сплитът се мени и редът се разбърква.
    observed: M7-bare-location 28 | set_identical: True
--- order_identity | query: младост | today: M7-bare-location 28 wq 6 woq 22
    broken: На ОУ „Иван Вазов“ (район Младост, днес без квартал) се записва quarter {"name": "ж.к. Младост", "code": "mladost", "src": "SIGNED_POLYGON"} — напълно ПРАВИЛЕН запис с познат код. Резултат: множеството идентичности е същото, но редът се мени (записът скача от 8-а на 2-ра позиция); сравнение по множество би минало зелено.
    observed: M7-bare-location 28 | set_identical: True
--- parent_child | query: училище младост | today: A3-location 11 wq 2 woq 9
    broken: Кодът на квартала на ПГИ „Д-р Иван Богоров“ се сменя на "mladost2_new" — нов код без подредената тройка на D13 в data/place_categories.json — а името остава „ж.к. Младост 2“. Резултат: `qph` е празно, детето изчезва от отговора на родителската дума, 11 → 10, мълчаливо.
    observed: A3-location 10 | set_identical: False
Now I can verify the fixtures against the new delivery by actually running the five queries with mutations over new_data. The plan §3.5 claims (numbers re-measured): fixture 1: A3-street, 1, ДГ№12 Ян Бибиян ✓ (measured above: детска градина дойран → A3-street, 1 — name? need to confirm it's Ян Бибиян). Fixture 2: A3-district 12, 9 with quarter ✓ (measured 12, 9 wq). Fixture 3: M7-bare 20, 8/12 ✓. Fixture 5: A3-location 6, 3 wq ✓.

  But do the _broken mutations still break under new data? Fixture 2's broken: ОУ Отец Паисий gets DISTRICT_FALLBACK quarter + district null → 11. Under new data, Отец Паисий HAS a quarter (sv_ivan_rilski). The mutation overwrites quarter to the fallback and nulls district. dph for district null... The district branch `district_rows` filters by r.dph.has(dphrase); with district None, dph presumably empty → row leaves → 12→11 ✓ still plausible. But fixture 2's "новите zone" claim — identities changed.

  Rather than reason, run the mutations with my patched modules over new_data. The mutations reference rows by name — all named rows exist in new_data (no adds/deletes). Let me run all five fixtures' broken ops over new_data and check whether the same assertions fail, plus verify fixture 6-8 claims. Also fixture 6 broken claim: mutating ДГ№34 Лястовичка's quarter code to vazrazhdane1_new → parent returns 4. Under the harness, reindex rebuilds qph from rec.quarter name — code change doesn't change name... wait qph is built from the quarter NAME phrases? Let me check Rec._loc_phrases: builds phrases from the location NAME via significant tokens. If we change only the code, the name stays "ж.к. Възраждане 1" and qph unchanged → parent still returns 5, and the fixture wouldn't fail! But the plan says broken: "родителят връща 4". Hmm — but in fixture 5 (existing parent_child), the mutation changes the code to "mladost2_new" and the observed result is 11→10. Why does changing code break qph? Let me read _loc_phrases/_loc_tokens (664-679) to understand: maybe phrases are looked up from the DICTIONARY by code — i.e., loc phrases come from location_dicts keyed by code. If code unknown → no phrases → row drops from phrase matching. That explains it. So the fixture mechanism works via code→dictionary lookup. Good.

  Fixture 6's broken claim "родителят връща 4": mutating Лястовичка's code → its qph empties → "възраждане" parent query returns 5-1=4 ✓ IF Лястовичка is one of the 5 rows of "възраждане". Need to check: is ДГ№34 Лястовичка among the 5? Let me print names of "възраждане" results.

  Also confirm "детска градина дойран" row name is ДГ№12 Ян Бибиян.

  And fixture 3's new broken: "+ SIGNED_POLYGON с код извън 28-те" — combined with заварената. OK.

  Fixture 10: synthetic fallback row — claims (б): stays in the answer of bare "училище младост" (клон :7118) and "младост" (:7064). Note: "училище младост" is A3-location (has key "училище"), not bare. :7118 in index.html is the district-rows-in-A3 branch (`dRows = cls.filter((r) => !r.e.quarter && r.dph.has(phrase))` at excerpt :318). With ownQuarter change, fallback row has r.e.quarter set but ownQuarter(r.e) null → remains in dRows ✓. And broken: removing ownQuarter from :7118 → fallback row excluded → 6→5 for the synthetic-delivery count. The claim "(измерено)" — with one synthetic fallback row added, "училище младост" would be 7 with the fix and 6 without... The plan says 6→5: presumably the fixture's synthetic row replaces an existing row's quarter with the fallback (mutating an existing row in the 6) rather than adding. E.g. take one of the 6 rows (say a None-quarter school in район Младост), set quarter = fallback(mladost district). With the fix, ownQuarter null → row stays in dRows → still 6; broken (without ownQuarter) → row has quarter → excluded → 5. ✓ plausible and measurable at build time. OK.

  Fixture 11 parity — six queries through the slice and recall_sweep — mechanics plausible.

  Fixture 9: claims RECS.length === 375 — wait, "RECS.length === 225 при среза с оригиналния QUARTER_SRC (places2 = [])" — buildIndex(hotels=225, places2=[]) → RECS = 225 ✓. And valid delivery → 375 ✓.

  Also verify the OLD-vs-NEW for fixture 4 order_identity: plan claims "същите 20, подредени". The mutation: ОУ Иван Вазов gets correct quarter mladost SIGNED_POLYGON. Under NEW data, ОУ Иван Вазов ALREADY has quarter pobeda with zone ж.к. Победа — the mutation sets it to mladost. Then "младост" query: row re-enters via qph "младост" → 21 rows, not "същите 20 подредени"! Wait — under new data, Вазов is NOT in the 20 (it's in pobeda, zone ж.к. Победа, no "младост" phrase). Mutating its quarter to mladost changes zone? The mutation sets quarter field only, not zone. qph derives from quarter name → phrase "младост" added → row joins qHit → result becomes 21 rows → n changes 20→21 → assert fails ✓ it DOES break (good — the fixture fails), but the plan's claim "същите 20, подредени" (same 20, reordered) is wrong: under new data the mutation ADDS the row back (it had left). Actually wait — would it? The row has district mladost; zone stays "ж.к. Победа"... M7 bare branch: qHit = rows whose qtk contains all query tokens; Вазов with quarter mladost gets qtk [mladost] → included. So measured n=21 ≠ 20 → assertion fails on n AND identities. So the fixture still fails ✓, but the broken observed values must be re-measured (n=21, not 28-set-identical reorder). Plan says numbers re-measured ("числата се ПРЕИЗМЕРВАТ") ✓ — the plan explicitly marks fixture numbers for re-measurement. But its claim "твърди: същите 20, подредени" for the passing half is fine; the _broken description in the table just says "заварената". The заварена mutation text says "Резултат: множеството идентичности е същото, но редът се мени (записът скача от 8-а на 2-ра позиция)" — under new data that mutation's effect differs (row was already written). The plan only requires the broken to fail; the observed block gets re-measured. Acceptable, but the *narrative* of the inherited mutation no longer describes reality — the fixture file is rewritten with re-measured observed values. OK.

  Better: let me actually run the five inherited mutations over new_data to see whether each still fails and what the observed numbers are. I can reuse the harness functions logic inline (apply_ops by name, reindex). Let me do that — it directly answers §3.5 "пада ли _broken по същата проверка".

  Fixture mutations from the 06.09 file — get ops arrays. Let me run.

• Сега проверявам дали петте заварени `_broken` мутации още падат върху новата доставка.### street_collision | детска градина дойран
  NEW today: A3-street 1 wq 0 woq 1 | 06.09 recorded: A3-street 1 0 1 | same: True
  NEW broken: A3-category+zone/kind 1 wq 1 woq 0 | 06.09 observed: A3-category+zone/kind 1
  broken still differs from NEW today: True
### district_retention | училище район младост
  NEW today: A3-district 12 wq 9 woq 3 | 06.09 recorded: A3-district 12 3 9 | same: False
  NEW broken: A3-district 11 wq 8 woq 3 | 06.09 observed: A3-district 11
  broken still differs from NEW today: True
### mladost_kind_collision | младост
  NEW today: M7-bare-location 20 wq 8 woq 12 | 06.09 recorded: M7-bare-location 28 6 22 | same: False
  NEW broken: M7-bare-location 21 wq 9 woq 12 | 06.09 observed: M7-bare-location 28
  broken still differs from NEW today: True
### order_identity | младост
  NEW today: M7-bare-location 20 wq 8 woq 12 | 06.09 recorded: M7-bare-location 28 6 22 | same: False
  NEW broken: M7-bare-location 21 wq 9 woq 12 | 06.09 observed: M7-bare-location 28
  broken still differs from NEW today: True
### parent_child | училище младост
  NEW today: A3-location 6 wq 3 woq 3 | 06.09 recorded: A3-location 11 2 9 | same: False
  NEW broken: A3-location 5 wq 2 woq 3 | 06.09 observed: A3-location 10
  broken still differs from NEW today: True
### възраждане NEW names: ['ДГ 29 "Звънче"', 'ДГ 31 "Крилатко"', 'II ОУ „Никола Йонков Вапцаров“', 'ДГ 33 „Делфинче“', 'ДГ№34 „Лястовичка“']
### детска градина дойран NEW: ['ДГ№12 „Ян Бибиян“']
Traceback (most recent call last):
  File "<stdin>", line 69, in <module>
  File "<stdin>", line 43, in answer
AssertionError: ('ДГ №34 „Лястовичка“', 0)


• Excellent results:

  1. All five inherited fixtures' mutations still break under new data ✓ (each `_broken` differs from the NEW today) — and the re-measured "today" values match the plan §3.5 table:
  - fixture 1: A3-street 1 ✓ (ДГ№12 Ян Бибиян ✓)
  - fixture 2: A3-district 12, wq 9 ✓ (plan says "12, 9 с квартал, новите zone" ✓); broken still → 11 ✓ (план: "заварената (DISTRICT_FALLBACK + district: null → 11)" ✓)
  - fixture 3: M7-bare-location 20, 8/12 ✓; broken → 21 (n differs → fails ✓)
  - fixture 4: broken → 21 (fails ✓)
  - fixture 5: A3-location 6, 3 wq ✓; broken → 5 ✓ (mutation on ПГИ Богоров code → drops from 6 to 5 — wait plan fixture 5 broken says "код mladost2_new без подредената тройка" ✓ same mechanism)

  2. Fixture 6 broken claim: mutating ДГ№34 Лястовичка's code → vazrazhdane1_new → parent returns 4. The "възраждане" 5 include ДГ№34 Лястовичка ✓. My attempt failed only because of the name string ("ДГ №34" vs "ДГ№34" — actual name is "ДГ№34 „Лястовичка“"). Let me rerun with the right name to verify → expect 4.

  Also verify §8 probe 2: "училище възраждане 3" → 2 rows: 3 ОУ Ангел Кънчев (kv_levski) and III ПМГ (trakia) — my earlier run: kv_levski 1 + trakia 1 ✓. Check names.

  Also probe 1: "Кайсиева градина" 3 rows M2-failopen "в нашата секция — няма квартални редове" — my run shows zlatni_pyasatsi 1 + chaika_kv 1 (rows WITH quarters). The claim "няма квартални редове" likely means "no rows from кв. Кайсиева градина" (no such quarter code). OK.

  Probe 4 details confirmed ("кв. Левски" → 4 rows: НУ Васил Левски asparuhovo, ПГ Васил Левски None, ДГ№40 vladislavovo, болница Лисичкова None ✓ matches §8's named four).

  Remaining checks:
  - fixture 6 broken with correct name.
  - О15: verify token behavior for "кв." — check place_tokens handles "кв." → orig? And confirm the cheaper-fix claim: M7_PREFIXES exists at :3093-3094 (it's used for failing_queries gate, not the branch). So a minimal fix: in bare_location_query, ignore tokens in a closed prefix set; in JS likewise. This is plausible — I'll cite that the engine already names the list (recall_sweep.py:3093).
  - §1.4 hashes: verify new_data files' sha256/bytes/gzip match §1.4 claims (LF normalization).
  - О13/§1.10: zero "coordinates" in new_data.
  - QUARTER_BY_SRC claimed in §3.3: places {"REG":39,"KAIS":10,"SIGNED_POLYGON":42} ✓ measured; hotels {"REG":115,"KAIS":25,"SIGNED_OVERRIDE":12,"SIGNED_POLYGON":15} ✓ measured. LOCATION_COUNTS 28/5/5 ✓. LEGACY_ROWS 18 ✓ (n_legacy_rows=18). LOCALITY_COUNT places 5 ✓ hotels 7 ✓.
  - О17: url regex — 17 wikimapia urls match `^https?://wikimapia\.org/\d+/` ✓; mladost2 src openstreetmap, regex only applies to wikimapia ✓. Plan И10's WM_URL regex ✓ fits delivered data.
  - Check new_data place_categories license strings vs old (§3.3 "Лицензните низове се сравняват дословно").
  - expectations.json: check frozen: true, signed_by Петър, _meta.inputs = three old blobs.

  Let me also check §1.4 hashes and coordinates grep.

• Почти всичко се потвърди. Довършвам оставащите мерки: хешове, fixture 6 с правилното име, expectations, лицензни низове.== §1.4 hashes (LF) ==
new_data/places.json True ('3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66', 128401, 14748)
new_data/hotels.json True ('eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51', 151263, 13642)
new_data/place_categories.json True ('9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231', 77998, 9690)
== coordinates in new_data ==
new_data/places.json 0 | cadastral: 0
new_data/hotels.json 0 | cadastral: 0
new_data/place_categories.json 0 | cadastral: 0
== licence strings old vs new ==
old cats _meta keys: ['contains_cadastral_id', 'contains_personal_data', 'curated_forms', 'generated', 'generator', 'legacy_bundle_sha', 'legacy_dropped_by_m3', 'n_chips', 'n_forms', 'n_legacy_dropped_by_m3', 'n_legacy_rows', 'n_locations', 'rule', 'rule_curated', 'rule_legacy', 'rule_legacy_m3', 'rule_locations', 'rule_sha', 'rule_zones', 'schema', 'sources', 'what', 'zone_alias_skipped', 'zone_generic_words', 'zones_unmatched']
changed _meta keys old->new: ['generated', 'legacy_bundle_sha', 'legacy_dropped_by_m3', 'n_legacy_dropped_by_m3', 'n_locations', 'zones_unmatched']
hotels _meta changed: ['by_zone_src', 'generated']
places _meta changed: ['by_zone_src', 'generated']
== expectations.json ==
frozen: None | signed_by: Петър
inputs: {"data/places.json": {"sha256": "329310f577e8353673b9014af99624a78ab825fb0ad53e93fc572a28660d88c0", "bytes": 122089, "path": "data/places.json", "commit": "HEAD", "what": "входът на доставката"}, "data/hotels.json": {"sha256": "46a44ce82f154ca6f77f5001c0393b4654a818ba6d5e8540fb1c6f337fe0418d", "byte


• Confirmed: hashes match §1.4 byte-for-byte; zero coordinates/cadastral ids; licence strings unchanged (changed keys are generated/legacy_bundle_sha/by_zone_src/n_locations/zones_unmatched — no licence_* changes); expectations signed_by Петър with old blobs.

  Note: `frozen` is None at top level — maybe nested elsewhere. Plan §1.9 says "expectations.json — frozen: true". Let me check where frozen lives. Also fixture 6 broken test with correct name, and "училище възраждане 3" names. Quick final run."frozen": true
възраждане baseline: ('M7-bare-location', 5)
fixture6 broken: ('M7-bare-location', 5) -> parent returns 5 (plan claims 4)
чайка after chaika_kv rename: M7-bare-location 21
училище възраждане 3 names: ['3 ОУ Ангел Кънчев', 'III ПМГ „Акад. Методий Попов“']
Two important negative findings:

  1. **Fixture 6 `_broken` does NOT fail as claimed.** Plan: "кодът на ДГ№34 Лястовичка → vazrazhdane1_new → родителят връща 4". Measured: parent still returns 5. Why? Because qph is built from the quarter NAME (significant tokens), not via code lookup in the dictionary. Wait — but the existing fixture 5 (parent_child) with code mladost2_new DID drop the row (11→10 on old, 6→5 on new). Why the difference? Let me think: fixture 5's query "училище младост" is A3-location with qRows = qph.has(phrase). ПГИ Богоров has quarter mladost2, name "ж.к. Младост 2" → phrase "младост" (numbers dropped) → matches. Changing code to mladost2_new → why would qph change if qph derives from name?...

  Let me check Rec._loc_phrases (664-679). Perhaps _loc_phrases looks up the LOCATION DICTIONARY by code: LOCATIONS["quarter"][code] gives the entry with name/aliases, and phrases are built from the dictionary entry. Unknown code → no phrases → empty qph. That's why fixture 5 works. But then my fixture-6 attempt should also have dropped Лястовичка... unless my mutation didn't take because the name uses „...“ quotes — assert passed (len==1), so mutation applied. But parent still returns 5.

  Hmm, wait — maybe Лястовичка in "възраждане" 5 comes via vazrazhdane (parent) not vazrazhdane1? Baseline names: ДГ 29 Звънче, ДГ 31 Крилатко, II ОУ Вапцаров, ДГ 33 Делфинче, ДГ№34 Лястовичка. Which codes? Earlier qc for "възраждане": vazrazhdane 3, vazrazhdane1 1, vazrazhdane2 1. Maybe Лястовичка's code is vazrazhdane (parent), not vazrazhdane1. Then changing its code to vazrazhdane1_new with name "ж.к. Възраждане 1"... qph would be built from the new name? Depends on implementation. The plan's broken says "кодът на ДГ№34 Лястовичка → vazrazhdane1_new → родителят връща 4" — presumably assuming Лястовичка is vazrazhdane1. Let me check its actual code in new_data. If it's `vazrazhdane` (parent), then the mutation keeps name... I set name to "ж.к. Възраждане 1" in the mutation's quarter.name. If qph derives from name: "възраждане" phrase still matches (number dropped) → row stays → 5. If qph derives from dictionary-by-code: unknown code → empty → row drops → 4. My measurement shows 5, so qph derives from the name (or from zone). But then why does fixture 5's existing mutation work? In fixture 5 the mutation sets code mladost2_new but the plan-file mutation — let me re-read: "Кодът на квартала на ПГИ „Д-р Иван Богоров“ се сменя на mladost2_new ... а името остава „ж.к. Младост 2“. Резултат: qph е празно". And measured it works (11→10 old; my rerun 6→5 new ✓). So qph IS code-dependent. So why didn't my fixture-6 attempt drop Лястовичка?

  Possibility: Лястовичка's code is vazrazhdane1 already, and I changed name+code; but wait, I need to check what qph is built from. Let me read _loc_phrases at 664-679.

  Actually maybe the M7 branch for "възраждане" uses qtk (tokens) not qph. bare_location_rows uses qtk/ltk tokens: qHit = R.every token in r.qtk. qtk = _loc_tokens("quarter", quarter) — tokens of the quarter name, possibly via dictionary. If qtk is built from the name directly, code change does nothing → row stays → 5. And in A3-location (fixture 5, has key), the branch uses qph — code-dependent. That would explain both: M7 (bare) unaffected by code mutation; A3-location affected. So the plan's fixture-6 _broken ("родителят връща 4") is WRONG as measured: the parent query "възраждане" is bare (M7) and returns 5 regardless. The broken doesn't fail ⇒ fixture 6 as specified has a green-by-accident negative half — a real blocker for §3.5's claim "всяка с падащ _broken".

  Wait — but maybe qtk is also code-dependent (dictionary lookup by code). My measurement says the row stayed. So either qtk derives from name, or the mutation didn't affect. I set quarter to a whole new object with name "ж.к. Възраждане 1", code vazrazhdane1_new. Row stayed → 5. So for the M7 branch, code-unknown mutation does not drop the row. Confirmed: plan's fixture 6 _broken as written does NOT fail by the same check. Need to double check by reading _loc_tokens to be sure, but the empirical result is decisive: 5, not 4.

  Actually hold on — maybe Лястовичка is in the 5 via *district* phrase (dph) or *name*? It could be matched through dRows (district fallback) — no, M7 uses qtk/ltk/dph: bare = nameHasPhrase + qHit + lHit + dHit where dHit requires !quarter. Лястовичка has a quarter. If its qtk became empty (code unknown), would it still match via... dHit requires no quarter; lHit via locality. It has no locality presumably. So if qtk were code-dependent, row would drop → 4. It didn't drop → qtk is name-derived. But then in fixture 5 (A3-location branch) qph... also name-derived? Then why did mladost2_new drop Богоров? Hmm, my rerun of fixture 5 showed 6→5, so the mutation DID drop Богоров. Let me look at _loc_tokens/_loc_phrases 664-679 to resolve the asymmetry. Maybe _loc_phrases looks up the dictionary (code→phrases) while _loc_tokens uses name directly. That matches: A3 branch (qph) drops, M7 branch (qtk) doesn't. Then the plan's fixture 6 _broken is measurably wrong (M7 branch is token-based). Unless they meant the assertion to fail via a different sub-claim: fixture 6's "today" includes (а) 5 rows. If the mutation returns 5 with same names... identical → no failure. So yes, the _broken of fixture 6 does not fail. That's a genuine finding: К28 blocker/major.

  2. **Fixture 7 _broken**: "смени името на chaika_kv на нещо без думата Чайка → сливането изчезва". My simulation renamed row quarter names/zones (not the dictionary): "чайка" went 30 → 21. Hmm, 21 not 20 (chaika_kk 19 + None 1 = 20 expected; got 21). Whatever — it does drop, so the negative half plausibly fails ✓ (30→21 ≠ 30). But note: where the name lives matters — if fixture mutates the dictionary entry name (place_categories locations), the harness's reindex doesn't rebuild LOCATIONS (module-level, built from cats at import) — mutations apply to rows only (apply_ops touches hotels/places bundles). So fixture 7's mutation must be on rows (zone/quarter name), which my sim shows works (30→21). OK but the harness reindex rebuilds only RECS-derived structures; qtk derives from row quarter name → works. ✓ But wait — if qtk were name-derived, fixture 5's code-only mutation wouldn't have dropped Богоров... contradiction. Let me read _loc_tokens/_loc_phrases to settle.

  3. §8 probe 2 names confirmed: 3 ОУ Ангел Кънчев + III ПМГ ✓.

  Let me read recall_sweep 604-700 (Rec class).

• Намерих две несъответствия във фикстури 6/7. Чета `Rec._loc_tokens/_loc_phrases`, за да установя механизма точно.

• Now it's clear:

  - `_loc_tokens` (qtk): built from the field's NAME directly (`place_tokens(field["name"])`) + accepted aliases of its code from `LOC_EXTRA`. So code-unknown mutation keeps name tokens → M7 (qtk) unaffected. My fixture-6 test: parent still 5. ✓ explains.
  - `_loc_phrases` (qph): `LOC_PHRASES[cls][code]` — dictionary lookup BY CODE. Unknown code → empty qph → A3-location branch drops the row. ✓ explains fixture 5 (mladost2_new drops Богоров from "училище младост" 6→5).

  So plan fixture 6 `_broken`: "кодът на ДГ№34 Лястовичка → vazrazhdane1_new → родителят връща 4" — the parent query "възраждане" is **M7-bare** (token-based, qtk from NAME). Changing only the code leaves qtk intact (name stays "ж.к. Възраждане 1"... wait, in my mutation I also set the name to "ж.к. Възраждане 1" — original name is probably "ж.к. Възраждане 1" already? Лястовичка's quarter — let me check its current quarter: code vazrazhdane1, name "ж.к. Възраждане 1". My mutation set the same name, new code → qtk unchanged → row stays → 5. Measured: 5. So the broken as described does NOT fail. **Fixture 6's `_broken` is measurably green** — a blocker for §3.5's "всяка с падащ _broken" claim, since G2 requires every _broken to produce AssertionError. The plan's claim "родителят връща 4" is false under the measured engine: +the harness test `test_every_broken_candidate_makes_the_same_assertion_fail` would go RED not because behavior broke but because the mutation changed nothing. Actually the fixture would FAIL the harness (broken must fail; if it doesn't fail, `assertRaises(AssertionError)` fails → test red). So building the plan as written → red test at step 6 → STOP. That's a real defect: fixture 6's negative half doesn't bite.

  Wait — but maybe they'd mutate differently: "кодът на ДГ№34 Лястовичка → vazrazhdane1_new" — maybe they also mean that the fixture asserts via sub-claims (а),(б),(в)? The harness `assert_case` compares branch/n/split/identities of the fixture's query. If fixture 6 has multiple queries (възраждане, възраждане 2, ж.к. възраждане 2), the harness needs extension (assert_case takes one query). Plan §3.5 harness changes mention assert_case stays for Python fixtures, branch optional for Node. Fixture 6 has three sub-queries — the current harness shape (one query per case) doesn't support that directly; they'd need three cases or extension. Minor.

  Also fixture 7's claim "смени името на chaika_kv": mutation on rows (zone + quarter.name) — my sim: 30→21 ✓ fails (good). But hold on: mutations can only touch bundle rows; the phrase map (LOC_PHRASES) is module-level from cats — the "сливане" happens through qtk/qph of rows with chaika_kv code. Renaming row quarter.name changes qtk (name tokens) but qph stays (code still chaika_kv → dictionary phrases "чайка" remain!). M7 uses qtk/ltk tokens (bare_location_rows: qHit via qtk). Let me verify bare_location_rows — line ~1150-1170. Earlier I saw bare_location_rows at ~1163-1170: uses quarter_hit... let me look. The excerpt at 1163-1170 showed `district_hit = [r for r in cls if r.quarter is None and phrase in r.dph]` and quarter_hit/locality_hit — via qph presumably (phrase in r.qph). If M7 uses qph (dictionary phrases by code), renaming row quarter.name does NOT remove the merge... but my sim showed 30→21. Hmm, my sim renamed both quarter.name AND zone. Let me check bare_location_rows exact code.

  Also which is it for M7: qtk or qph? Let me read 1140-1180.Confirmed: M7 (`bare_location_rows`) reads `qtk`/`ltk` — tokens built from the quarter NAME (`_loc_tokens`) plus code aliases from LOC_EXTRA. So:

  - **Fixture 6 `_broken` (code-only mutation) does NOT fail**: qtk unchanged → parent returns 5, not 4. Measured directly: 5. Plan's claim is measurably wrong. However — wait, would the harness's assertion then be red at build time and caught? Yes, at §4 step 6 the fixture test would be red because `assertRaises(AssertionError)` fails. So it's self- revealing, but as written the plan instructs the executor to build something that cannot pass G2 — a real defect worth a condition. Unless... hmm, let me double check: maybe with the mutation, the row gets matched differently — no, measurement is decisive: 5 = today.

  Actually wait — one subtlety: my mutation set `quarter` to a new dict. `_loc_tokens` uses `field.get("name")` — "ж.к. Възраждане 1" — tokens: zh,k dropped (length ≤2 / prefix), "vazrazhdane" + "1" → significant tokens: vazrazhdane (num 1 dropped). Same as before. qtk identical → row in result. ✓ 5.

  - **Fixture 7 `_broken`**: rename chaika_kv name. M7 qtk from name → my sim dropped to 21 ✓ fails. Good. (21 because one extra None row? bare had None:1 → after rename maybe a district row entered? whatever — it differs, fails ✓.)

  But note fixture 7's mutation via apply_ops on rows works only if it renames zone/quarter.name on MANY rows (all chaika_kv rows) — ops keyed by name hit exactly one row each. Renaming ONE row's quarter name leaves 9 other chaika_kv rows → merge persists → 29 vs 30... still differs → fails ✓ but for a weaker reason. The plan says "смени името на chaika_kv на нещо без думата Чайка → сливането изчезва" — with per-row mutation keyed by unique name, you can only rename one row, so the merge does NOT disappear; only n changes 30→29 (or the renamed row leaves). The _broken still fails (observed re-measured), but the *described mechanism* ("сливането изчезва") is inaccurate — the merge doesn't disappear by renaming one row. Alternatively they might mutate the dictionary... apply_ops only touches bundles. Minor wording issue; the negative half still fails. I'll note it as minor.

  Also О15 cheaper fix: engine already names the prefix list (M7_PREFIXES at :3093, though used in gate code). A minimal fix: in `bare_location_query`, filter R tokens that are known type prefixes before the significance check — one-line-ish in both engines. This fixes "кв. Левски" → 14 (12 kv_levski). It does NOT fix "възраждане 2" (needs numbers in phrases, index-side). So the cheaper fix covers О15's four typed queries but not О16's child queries. The plan's О15 text says "Ако Петър каже „сега“ — това е друг лот с нов паритетен корпус и нов кръг делти" — overstated: parity corpus isn't needed for this narrower change (no locationKey). Still needs re-freeze of expectations (rows change) — the plan's §1.7 numbers would change though: "кв. Левски" would stop returning 4 чужди. Anyway — finding: plan misses the cheap option; deferral itself is defensible but the stated cost is inflated.

  Hmm wait, actually there's an even cheaper angle: the four typed queries fail because M7's guard rejects R containing "кв". But even simpler: the *measured* effect of prefix-skip on other queries — e.g. "кв. Младост" today → M3 name-noise? Let me quickly test what "ж.к. младост" returns today and whether prefix-skip would change signed frozen queries. This matters for cost assessment: any behavior change on frozen queries requires new deltas in the queue. The plan's "нов кръг делти" is partially true (expectations re-freeze needed) but "нов паритетен корпус" is not. I'll phrase carefully.

  Also should check: does "кв. левски" hit exact_alias or A0? It returned M3 4 — fine.

  Now О14 acceptability: the 8 lost rows: 5 schools (named in plan) + 3 kindergartens (unnamed in plan §1.7 explanation). Where did the 3 ДГ go? They got quarters (pobeda/sv_ivan_rilski/troshevo?). Check their new zones. Quick check: ДГ№53 Слънчево зайче, ДГ№26 Изворче, ДГ 24 Детско градче — new quarter codes. Let me verify they're inside район Младост (all in district mladost presumably) — so under the *district* query "училище район младост" the schools stay (probe 9: 12 ✓, measured 12 with the 5 schools still there). The kindergartens aren't in that query because it's "училище". The bare "младост" query is the *quarter* Mladost by the engine's own signed semantics ("bare „младост“ is the quarter first" — comment at :1150). So by the design "всичко ВЪТРЕ в квартала", rows in *other* quarters shouldn't appear under "младост" — the old behavior (28) included район-Младост rows, i.e. district leakage. The new 20 = quarter Mladost + Mladost 2 + district rows without quarter. That's *more* correct by design. Acceptable, and the plan does route it through signature (О14). But §1.7's поименно explanation misses the 3 kindergartens — condition: name all 8.

  Let me get the 3 ДГ's new quarters. And confirm О16's claim "работи по фраза за mladost2/vazrazhdane1/2" — measured: "младост" includes mladost2 rows (3) ✓, "възраждане" includes vazrazhdane1/2 ✓ — because the number token is dropped from qtk (name "ж.к. Младост 2" → significant token "младост"). ✓ "случайно съвпадение" — accurate: the child answers the parent's word because its own number is invisible.

  "дете → детето не работи" ✓ measured (0 rows). Minimal signed path = Б5 parents in dictionary — plan §3.7 says it. Also note there IS a cheaper partial path for child query: keep numbers significant in qtk phrases — but that's D12 territory again.

  Let me run the last small check: the 3 ДГ new quarters + whether "младост" new-20 includes all mladost+mladost2 coded rows (5+3=8 wq ✓) — i.e., nothing with code mladost/mladost2 is missing from the 20 (design "всичко ВЪТРЕ в квартала излиза"). Count rows with code mladost/mladost2 in delivery: mladost 5? earlier newc: mladost wasn't printed. Let me check counts and that all appear in the 20.

• Последна серия мерки: къде отиват трите ДГ и пълнота на покритието „всичко в квартала“.ДГ№53 „Слънчево зайче“ -> sv_ivan_rilski | district: mladost | zone: кв. Св. Иван Рилски
ДГ№26 „Изворче" -> troshevo | district: mladost | zone: кв. Трошево
ДГ 24 "Детско градче" -> troshevo | district: mladost | zone: кв. Трошево
rows coded mladost/mladost2: 8 | missing from answer: []
kv_levski rows: 12 | missing from 'левски': []
Лястовичка quarter: {'name': 'ж.к. Възраждане 1', 'src': 'REG', 'code': 'vazrazhdane1'}
ж.к. младост -> M3 2
кв. младост -> M3 2
ж.к. възраждане -> M3 0


• All measurements done. Let me finalize:

  **Confirmed true:**
  - §1.3: exactly the 8 codes; 28 delivered ✓ (set equality)
  - §1.5: 57 rows change exactly quarter+zone (42+15), all null→SIGNED_POLYGON ✓; quarter_attribution 18 codes (17 wikimapia + 1 osm mladost2) ✓; url form http://wikimapia.org/900042/bg/… ✓ matches И10 regex; _meta 10/8 ✓; zones 20→28, aliases 39→48 ✓; parents 0 of 28 ✓; 201 written (154/35/12) ✓; 117 without quarter ✓; 0 DISTRICT_FALLBACK ✓; hashes/bytes/gzip ✓; zero coordinates/cadastral ✓; licence strings unchanged ✓.
  - §1.7/§1.8: every engine number reproduced: M3 4/1/24/22; левски 14/12 kv_levski; възраждане 2 etc. → 0; чайка 30 (29 old; gained Nikea hotel — now chaika_kk presumably); аспарухово 16 without Пинокио; дружба 2; кайсиева 3 M2-failopen; възраждане-3 M2 2 (Ангел Кънчев kv_levski + III ПМГ trakia); младост 28→20 (8/12); училище младост 11→6 (3 wq); училище район младост 12 (9 wq, 6 zone changes); възраждане 5; училище възраждане 1 Вапцаров.
  - О15 mechanism ✓ (isSignificantToken drops prefixes/numbers — excerpt :108; recall_sweep :424-431 + :1185-1198).
  - О16 ✓ (parents 0/28; child queries 0; chaika merge measured; druzhba not under asparuhovo).
  - О19 ✓ (recall_sweep :621/:623/:1123/:1167/:2146/:2150 verified; bundle test :291-293/:309 verified).
  - О20 ✓ (258/258 zone == quarter.name; 117/117 район-label; excerpt :133 single label today).
  - О17 ✓ (17/17 wikimapia urls match ^https?://wikimapia\.org/\d+/; mladost2 src=openstreetmap exempt from the regex since it applies only at src==='wikimapia'; _meta 10/8 closed).
  - §3.5 fixtures 1-5: re-measured values match the plan's claims; all five _broken still fail under new_data (street_collision A3-category+zone/kind 1; district_retention 11; mladost_kind_collision 21; order_identity 21; parent_child 5).
  - §8 probes: 1 ✓ (3 rows), 2 ✓ (2 rows named), 3 ✓ (5/0), 4 ✓ (14/12 + 4 чужди named exactly), 6 ✓ (30 mixed), 7 ✓ (16 без Пинокио / 2), 9 ✓ (12/20). Probe 5 wording ("двата нови SIGNED_POLYGON реда") is incomplete: measured answer is 4 rows — ПАРК ХОТЕЛ БРИЗ (name hit, zlatni) + Камелия (briz, pre-existing) + the 2 new rows. Minor.
  - §1.8.4 "нула с търсения код" — FALSE for hristo_botev: ЦДГ 8 - Христо Ботев carries hristo_botev among the 24 (1 row). The plan's own §8 probe 4 doesn't name it either. Condition: correct the count to "1 ред с търсения код (по име, не по квартален механизъм)" — the semantic claim (typed query doesn't find the quarter) still holds since it's an M3 name hit.
  - Fixture 6 _broken DOES NOT FAIL: measured parent "възраждане" returns 5 after the code-only mutation (plan claims 4), because M7 reads qtk from the quarter NAME (recall_sweep.py:664-680, :1159), while qph by code matters only for A3-location (:686, :1121). This is the one hard defect: G2 requires every _broken to fail; as specified, fixture 6's negative half is green → §4 стъпка 6 goes red → STOP. Fix: mutate so the parent answer actually moves — e.g. rename Лястовичка's quarter.name to a string without "възраждане" (then qtk loses the token → 4), or key the fixture on the child branch differently. Precise fix: `_broken`: set quarter = {"name": "ж.к. Възраждане 1" → any name w/o the word}, or keep code change but assert on "училище възраждане"-style A3 query... but (б)/(в) claim 0 rows for child queries already; the broken must attack (а). The correct minimal broken: rename the quarter name (drops qtk token) → 4. Measured equivalent: my chaika rename sim dropped rows the same way.
  - О22: 138 not reproducible from old→new in this copy: old(HEAD f00dd78)→new = 57 zone changes (42+15), all unnamed→named, 0 lost/0 changed named→named. The 138 is measured against baseline f06ac06 (not present in the copy) — so its correctness is unverifiable here; the plan already treats it as STOP-number re-measured in §4 стъпка 2 and mechanically generated allow (стъпка 9). Note risk: if 138 is wrong, allow generation stops the lot — safe. I'll note it as an observation, not a condition... Actually the task explicitly says "преброй ги сам: zone_named lost/changed по old→new" — answer: 0/0 lost/changed, 57 gained. Wait, but maybe coverage semantics count *named zone lost* = row whose baseline zone was a quarter name and now differs — 0 in old→new. So by old→new the count is 57 gains; 138 vs f06ac06 implies f06ac06 differs from f00dd78 by ~81 more moved rows... Actually careful: 138-57=81 — interesting, equals "ahead 81"? Coincidence probably. Can't verify. State it.
  - О14: the 8 lost rows named: 5 schools (Вазов, ПГЕ, ПТГ → pobeda; Отец Паисий → sv_ivan_rilski; Чинтулов → troshevo) + 3 kindergartens (ДГ№53 Слънчево зайче → sv_ivan_rilski; ДГ№26 Изворче → troshevo; ДГ 24 Детско градче → troshevo). All 8 remain in district Младост and stay in the explicit "училище район младост" (12, measured) — wait, kindergartens aren't in the "училище" query; but "детска градина район младост" would hold them. By the design "всичко ВЪТРЕ в квартала": all 8 mladost/mladost2-coded rows are in the 20 ✓ (measured: none missing). The loss = rows of OTHER quarters of the district — the engine's own signed comment (:1150) says bare "младост" is the quarter first. So acceptable-by-design ✓, but the plan's §1.7 поименно причина names only 5 — condition: name all 8 in the queue delta rows.
  - О15 cheaper fix: yes, exists and the plan overstates the cost. Minimal fix: in `bare_location_query` (recall_sweep.py:1185-1198) and the client M7 guard (index.html:7059/excerpt:258), ignore the closed prefix-token list before the significance test (the engine already names it: M7_PREFIXES :3093). Measured consequence: "кв. Левски" would become bare "левски" → 14/12. This fixes the four typed queries WITHOUT locationKey/parity corpus; it does change frozen answers (re-freeze + queue deltas still needed), so deferral remains defensible, but "нов паритетен корпус" is not required. The plan frames the only alternative as full D12 — incomplete option analysis. Minor/major condition.

  Also: fixture 6's (б)/(в) "0 rows" verified ✓. Fixture 6 harness shape: three sub-queries in one fixture — assert_case is single-query; plan says assert_case stays for Python fixtures; fixture 6 with three queries needs harness extension not fully specified. Fold into the fixture-6 condition.

  Fixture 7 mutation mechanism: ops are per-row by unique name; renaming "the name of chaika_kv" (dictionary entry) is NOT expressible via apply_ops (bundles only). Row-level rename of one row still breaks the count (30→29... measured 30→21 when renaming ALL rows' zone+quarter.name; single-row rename would give 29 or keep? qtk of that row loses "chaika"... it would leave → 29 ≠ 30 → fails ✓) but "сливането изчезва" is not what a single-row mutation shows. Condition: specify the mutation as multi-op over all 10 chaika_kv rows or re-word the claimed effect. Minor.

  Word budget: ≤900 words. Verdict: ГОДНО с условия? The fixture-6 _broken green-negative is a blocker-class defect against the plan's own red line 6 ("всеки _broken ТРЯБВА да падне") — but it's self-revealing at build (test goes red → STOP), and the fix is mechanical and small. The hristo_botev "нула с търсения код" is a false measured claim in a plan whose numbers are STOP-numbers — under §7 т.1 the executor would STOP when re-measuring. Both are exactly the class of thing the plan's own machinery catches; but the task asks for a verdict: ГОДНО за подпис / НЕГОДНО с номерирани условия. Given (а) a measurably false STOP-number claim (1.8.4 hristo_botev), (б) a fixture whose negative half cannot fail as written, (в) mislabeled §8 probe 5 count, (г) §1.7 explanation naming 5 of 8 rows — I'd say НЕГОДНО with numbered conditions (the tradition in this repo: Кими verdicts with conditions). Given the severity (fixture 6 breaks the plan's own gate G2; a false (М) number in §1.8), НЕГОДНО is the honest verdict.

  Conditions:
  - К28-1: 1.8.4 correction — hristo_botev count.
  - К28-2: fixture 6 _broken doesn't fail (measurement: 5 not 4); replace mutation with name-rename (measured mechanism qtk) → 4.
  - К28-3: §1.7 name all 8 lost rows.
  - К28-4: §8 probe 5: "бриз" returns 4 rows, not 2.
  - К28-5: О15: record the cheaper prefix-skip option (M7_PREFIXES already exists) — decide consciously.
  - К28-6: О22/138: not reproducible old→new (57 gains, 0 lost/0 changed); pin the coverage semantics + require the executor's re-measure to state f06ac06's data diff vs HEAD.
  - К28-7 (minor): fixture 7 mutation must touch all 10 chaika_kv rows (apply_ops is per-row).

  Also fixture 6 harness multi-query note — fold into К28-2.

  Write the verdict in ≤900 words, Bulgarian, citing paths relative to the kimi_b3 root. Commands+numbers for each condition.Write the final verdict. ≤900 words, Bulgarian, paths relative to kimi_b3 root. All measurements done read-only (Python in-memory; no disk writes — my patched exec never called main(), writes live inside main()).

• # К28 · Присъда: **НЕГОДНО** — 7 условия

  Метод: `recall_sweep.py` е пуснат in-memory (пачнати са само трите пътя `HOTELS`/`PLACES2`/`CATS` → `old_data/`/`new_data/`; `main()` не е викан — записите са вътре в него, нула писане по диска). Потвърдено: §1.3 (доставени точно 28 кода, липсващите са точно изброените 8 — set-равенство), §1.4 (трите sha/bytes/gzip съвпадат байт-по-байт), §1.5 (57 реда сменят точно `quarter`+`zone`, 42+15, всички `null→SIGNED_POLYGON`; `quarter_attribution` 18 кода = 17 wikimapia + 1 openstreetmap/`mladost2`; url `http://wikimapia.org/900042/bg/…` пасва на регекса в И10; `_meta` 10/8; зони 20→28, псевдоними 39→48, `parents` 0/28; 201 написани = REG 154 + KAIS 35 + SIGNED_OVERRIDE 12; 117 без квартал; 0 `DISTRICT_FALLBACK`; 258/258 `zone == quarter.name`; нула `coordinates`/кадастрални; лицензните низове непроменени). Цитатите от основата са верни: §Б3 ред 144 („+41“, D12, „дете → детето“, „attribution row“, шест фикстури), ADR 010 D12/D13, СЪСТОЯНИЕ решения 8/9, ам. 3. Котвите на О19 са точни (`recall_sweep.py:621,623,1123,1167,2146,2150`; `test_places_public_bundle.py:291-293,:309`); О18 (`index_excerpts.txt:126` — locality с QUARTER_SRC) и О20 (`:133` — един етикет днес) също. §8 проби 1,2,3,4,6,7,9 — числата верни по `new_data`.

  **К28-1 · §1.8.4 носи невярно (М)-число.** Твърди „нула с търсения код“ и за четирите заявки. Измерено: „кв. Христо Ботев“ → M3, 24 реда, от които **ЦДГ 8 - Христо Ботев носи `hristo_botev`** (1 ≠ 0; чрез име, не през кварталния механизъм). Команда: пачнат `search(u"кв. Христо Ботев")` + брояч по `r.quarter.code`. Поправка: „24 реда, **1 с търсения код** (M3 по име) — кварталният механизъм не участва“. Останалите три (4/1/22, нула кода) са верни.

  **К28-2 · Фикстура 6 `_broken` НЕ пада — нарушава червен ред 6.** Планът твърди: кодът на ДГ№34 „Лястовичка“ → `vazrazhdane1_new` ⇒ „възраждане“ връща 4. Измерено: връща **5** (мутация по име `ДГ№34 „Лястовичка“`, `quarter={name:"ж.к. Възраждане 1", code:"vazrazhdane1_new", src:"SIGNED_POLYGON"}`). Механизъм (прочетен): M7 чете `qtk`, строен от ИМЕТО на квартала (`recall_sweep.py:672`, `:1159`), не от кода; кодът важи само за `qph`/A3-location (`:686`, `:1121`) — затова заварената фикстура 5 работи, а тази не. Построена така, G2 е червен на §4 стъпка 6. Поправка: `_broken` да пипа името — `quarter.name`/`zone` без думата „Възраждане“ (измерено същото за `chaika_kv`: 30→21) ⇒ родителят връща 4. Бонус: фикстура 6 има три заявки, а `assert_case` (`test_granitsi_fixtures.py:197-204`) е еднозаявков — харнесът иска разширение, записано в §3.5.

  **К28-3 · §1.7 назовава 5 от 8-те загубени реда (О14).** Измерено поименно (old→new на „младост“): ОУ „Иван Вазов“, ПГ по електротехника, ПТГ (→`pobeda`), ОУ „Отец Паисий“, **ДГ№53 „Слънчево зайче“** (→`sv_ivan_rilski`), ОУ „Добри Чинтулов“, **ДГ№26 „Изворче“**, **ДГ 24 „Детско градче“** (→`troshevo`). Трите детски градини липсват от обяснението; делта-редовете в опашката трябва да са 8. По замисъла загубата е приемлива: и 8-те остават в район Младост и в изричното „училище район младост“ (12, измерено), а всички редове с код `mladost`/`mladost2` (8) са ВЪТРЕ в новите 20 — нула липсващи.

  **К28-4 · §8 проба 5 подброява.** „бриз“ връща **4** реда (ПАРК ХОТЕЛ БРИЗ/`zlatni_pyasatsi` по име, Камелия/`briz` заварен, + двата нови), не 2. Поправка: „4 реда, от които двата нови SIGNED_POLYGON“.

  **К28-5 · О15 пропуска по-евтината поправка.** Вярно е: „кв. Левски“ не намира квартала (`isSignificantToken`, `index_excerpts.txt:108`; `recall_sweep.py:1185-1198`), голото „левски“ го намира (14/12). Но планът казва „сега = пълен D12 + нов паритетен корпус“. Двигателят вече назовава затворения префиксен списък (`recall_sweep.py:3093` `M7_PREFIXES`); пропускане на префиксните токени преди теста за значимост в `bare_location_query` (и двата двигателя) е ~2 реда и не иска `locationKey`/паритет. Отлагането остава защитимо (делтите и презамразяването си остават), но решението на Петър трябва да вижда и този вариант.

  **К28-6 · 138-те на О22 са невъзпроизводими от old→new.** По `old_data`→`new_data`: zone_named lost **0** / changed **0**, 57 печалби (район→квартал). 138 е срещу baseline `f06ac06`, чиито данни липсват в копието → числото е непроверимо тук. Поправка: О22 да запише семантиката на coverage (кое е „lost/changed“) и §4 стъпка 2 да изисква освен 138 и дифа `f06ac06`↔`f00dd78`, който я обяснява. Механичният allow (стъпка 9) + STOP 1 правят риска саморазкриващ се.

  **К28-7 · Фикстура 7 `_broken` е неточно описана.** `apply_ops` (`test_granitsi_fixtures.py:67-84`) мутира ред по ред по уникално име; „смени името на `chaika_kv`“ като един запис не е изразимо — преименуване на **всичките 10** реда `chaika_kv` (по един op на ред) дава 30→20 (измерено: 21 при смяна и на `zone`; сливането наистина изчезва). Поправка: мутацията се изброява поименно.

  Всичко друго в плана издържа измерването — включително петте заварени `_broken`, които падат и върху новата доставка (1: A3-category+zone/kind 1; 2: 11; 3: 21; 4: 21; 5: 5).

To resume this session: kimi -r session_2175c539-41f5-4238-80a2-cf2488ac8780
