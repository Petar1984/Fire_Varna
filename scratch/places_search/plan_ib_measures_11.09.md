# МЯРКА 3 — varna_3d и данните (read-only, 11.09.2026)

Бази: `C:/git/varna_3d` HEAD `1a0595d`; `C:/git/Fire_Varna` HEAD `74c165f` (Б3 в стейджа, непипнат); `C:/git/Varna_buildings` HEAD `4c6b482`.

## 1 · Доставката D13 и кой какво произвежда

**`C:/git/varna_3d/src/fire_varna_locations.py`** (2091 реда) — стълбата quarter/district/locality за 375-те доставени записа. Пише ТРИ файла и само по флаг:
- `:83-84` LEDGER → `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` (965 388 B), `:85` CONFLICTS → `scratch/granitsi/conflict_ledger_07.09.json`, `:86` INPUTS → `data/fire_varna_location_inputs.json`; записът е в `:2057-2085` (`--ledger` / `--inputs`), без флаг прогонът само мери (docstring `:53-54`).
- `TYPE_NORM :247-262` (низовите представки), `KIND_CLASS :159-163`; „написан квартал не се променя“ — `:444-456` + `_meta.rule_p8a` на леджера.

**Пинът е на v1, не на v2** — `src/fire_varna_locations.py:96-98`: `QUARTERS_SIGNED = docs/archive/quarters_signed_v1_2026-09-06.geojson`, sha `c1551d24…`; сверява се в `:976-979` и **спира билда при разлика**. Същият пин стои и в `data/fire_varna_location_inputs.json:66,86-93` (path/sha/`features: 60`/commit `6486b48`). Коментарът `src/fire_varna_locations.py:93-95` го казва дословно: тази стълба съди по v1, пребазирането върху v2 е работа на И-Б.

Последствие, измерено в стейджа на Б3 (`git show :data/places.json` / `:data/hotels.json`): **57 квартала със `src = SIGNED_POLYGON`** (places 42 от 150, hotels 15 от 225) са изведени от v1-полигоните, а публичната атрибуция в двата блоба е `wikimapia` 13+7 кода и `openstreetmap` 1 (`_meta.quarter_attribution`). Останалите: places REG 39 / KAIS 10 / без квартал 59; hotels REG 115 / KAIS 25 / SIGNED_OVERRIDE 12 / без 58.

**Износителите не пишат във Fire_Varna**: `src/export_fire_varna_places.py:91` → `varna_3d/data/fire_varna_places.json`, `src/export_fire_varna_hotels.py:67` → `varna_3d/data/fire_varna_hotels.json`. Преносът е ръчен: `git -C ../varna_3d show HEAD:data/fire_varna_places.json > data/places.json` (`C:/git/Fire_Varna/tests/test_places_public_bundle.py:49`, хотелите `tests/test_hotels_public_bundle.py:51`). `src/place_addresses.py` (672) дава `address` на доставените записи, не адресната база.

**НИТО ЕДИН скрипт във varna_3d не произвежда `address_rows.json` или `search_index.json`.** Grep за `address_rows`/`search_index` в `varna_3d/src` връща само ЧЕТЕЦИ (`build_quarters_signed_imot.py:370,1244`, `apply_ntr_zhr.py:47`, `qa_quarters_signed_imot.py`). Производителите са в трето репо:
- `C:/git/Varna_buildings/js/build_fire_varna_address_rows.mjs` (158 реда) — чете частния `output/address_index.json`, пише `../Fire_Varna/data/address_rows.json` (`:58-65`), проекция `[normalized_address, lat, lng]` (`:103,:108-111`).
- `C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs` (1177 реда); последният комит и по двата е `bfb5f86` (12.08).
- Гейт при писане: `js/build_fire_varna_address_rows.mjs:121-126` (ABORT) през `js/test_fire_varna_publish_gate.mjs:245-256,262` — **`field_order` трябва да е точно `["normalized_address","lat","lng"]` и всеки ред точно 3-торка**; четвърта колона = билдът пада и не пише нищо.
- `C:/git/Fire_Varna/docs/decisions/007_address_path_v2.md:13` (D2): `data/address_rows.json` е в списъка **Untouchable**.
- `C:/git/Fire_Varna/AGENTS.md:381` — задача, която пипа checkout-а `Varna_buildings`, е в § When To Stop And Ask.

Клиентът чете по схема, не по позиция: `index.html:4861-4870` (`buildAddressFieldIndex`, хвърля при липсващо поле), `:5325-5326` + `:5351-5362` — двата payload-а се зареждат мързеливо при първи фокус, т.е. извън твърдия таван 5 MB за първо зареждане (`AGENTS.md:137`). В `search_index.json`: 86 232 записа, `qtk` носят само **19 494** (22,6 %), `display_id` 43 295, `label` 43 133, `address_row_count = 80510`; кварталната дума в търсенето днес живее в `qtk`/`label` (+ подписаната зона Р38, `build_fire_varna_search_index.mjs:147-154,873-905`), не в `address_rows.json`.

**Гейтът P8-а**: `src/qa_p8a.py` (620 реда, docstring `:1-37`) — G17 срещу блоб на `8d60aeb`, затворената таблица на изходите, правилата на районната резерва, D7 през AST. Леджерът `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` — 375 реда; `_meta.outcomes` = written 201, assigned_polygon 65, edge_pending 63, pin_outside_all 41, disputed_overlap 5, no_coord/deferred_zone/assigned_district 0; `_meta.counts.quarter_by_signed_polygon = 57`, `assigned_polygon_not_written = 8`, `pending_signature = 8`, `changed_zone = 153`. Пинът вътре е `quarters_signed … features: 60` — v1.

## 2 · Артефактът v2 и може ли същият код да даде леджер за 80 510

`data/quarters_signed.geojson` — 321 285 B, sha `64c65f2b…`, 95 Feature-а, **всичките с `Polygon` геометрия** (нула Feature-и без геометрия — виртуалните родители също са полигони, ADR 011 `:21`). Затворен набор от 41 properties, проверен при билда в `src/build_quarters_signed_imot.py:1253-1259`. Полета, годни за живата карта: `code, name, kind, parent, parent_display, district, district_src, precision_m, attribution, license/license_label/license_terms`. `kind` по доставката: кв 38, с.о. 15, жк 14, м-т 13, кк 4, местност 4, пз 4, зона 2, вз 1 — забележка: **23 от 95 кода имат kind, който `KIND_CLASS` (`fire_varna_locations.py:159-163`) класифицира като `locality`, не `quarter`** (м-т/местност/пз/зона).

`_meta.mask` (реален, в артефакта): `in_one_cell 78235 · tie_break 1 · outside_all_95 2274 · excluded_cell 0 · deferred_cell 0`, `tie_break_rule "най-малък raion_num"`, `address_rows_sha256 2a4766bd47…` — **същият sha като днешния `C:/git/Fire_Varna/data/address_rows.json`** (5 073 137 B, 80 510 реда), т.е. маската важи за живия payload без преизчисление.

Механизмът: `src/build_quarters_signed_imot.py:682-688` (`address_points`, ред `[lat,lng]`), `:691-702` (`_tree_hits`, STRtree, точка на общ ръб влиза и в двата), `:704-748` (`build_mask`). Функцията **вече връща `words` — код на клетка за всяка от 80 510-те точки в реда на `address_rows`** (`:718-731`), но `words` **не се записва никъде**: използва се само за броячите и за `build_diff` (`:784-800`, `:1245-1247`); единственият изход на билдъра е `--out` (`:1287`). Леджер „адрес → код на клетка“ като файл днес не съществува.

Независимо възпроизвеждане (мое, извън репата, shapely 2.1.2): **78 235 / 1 / 2 274 = 80 510 — байт в байт същите числа**. Условие: тай-брейкът трябва да ползва САМО 90-те клетки; с всичките 95 (с родителите) двусмислените стават 6 991. 84 от 90 клетки имат ≥1 адрес; шест са с нула: `krushkite, lazur, orehcheto, pripek, pz_topoli, vz_zvezditsa`. Средна дължина на код 10,18 знака.

## 3 · Правилата, които важат

- `docs/decisions/010_signed_quarter_boundaries.md:48` D6 (SIGNED_POLYGON = свидетел ранг 3, пише само в празен квартал; `KIND_CLASS` не позволява полигон-местност да пълни `quarter`), `:50` D7 (ръбът `max(50, precision_m)`; забранено е да се четат ИЗНЕСЕНИТЕ координати), `:60` D12 (търсенето), `:62` D13 (атомност през три репа; тихата смърт при непознат `src` → 150 места изчезват мълчаливо), `:68` D16 (подписаната геометрия и регистърът се комитват от `Petar1984`), `:72` D18 + `:131` G17 (201-те написани квартала байт-стабилни срещу `git show 8d60aeb:scratch/refactor/_addr/lot1v_locations_375.json`).
- `docs/decisions/011_kartata_imot.md:15` И-D1, `:21` И-D4, `:30` (D12, D13, D16, D18, G29 остават непроменени), `:42` (v1 архивиран, деветте четеца сочат архива — комит `79266d5`), `:51` И-D7 (D6 и D12 не се пипат; едно обявено изключение Р22 — 24 кода с голо име → дълг ИБ-22), `:55` (покритие 97,18 % за 90-те клетки; 2 274 точки за маска), `:40` (планът „Адресите по полигон“ остава като **лот И5**, референцията към полигоните → v2).
- Съществуващ неподписан план за точно тази работа: `C:/git/Fire_Varna/docs/plans/ПЛАН_Адресите_по_полигон_08.09.md` (728 реда), §Р12 `:318-326` — кварталната дума е планирана като структурно поле `q` + `quarter_names[]` в **search_index**, с изричното „`data/address_rows.json` не се пипа (ADR 007 D2)“.

## 4 · Размерът (измерено с `json.dumps(..., ensure_ascii=False, separators=(",",":"))`, изход само в `%TEMP%/claude/mjarka3/`)

База: `address_rows.json` = 5 073 137 B (gzip-9 517 454); `search_index.json` = 11 242 756 B (gzip-9 1 056 124); сборът на двата lazy payload-а = **16 315 893 B** — точно числото в `ПЛАН_Адресите_по_полигон_08.09.md:55,326`.

| Вариант | Файл (B) | Δ (B) | gzip-9 (B) | Δ gzip |
|---|---|---|---|---|
| (а) код като низ, 4-та колона на ред | 6 115 924 | **+1 042 787** | 557 133 | +39 679 |
| (б) цял индекс 0..89 (−1 за вън), 4-та колона | 5 305 473 | **+232 336** | 530 996 | +13 542 |
| (в) отделен файл `{schema, kind, codes[90], quarter_index[80510]}` | 233 626 | +233 626 нов файл | 13 336 | +13 336 |

Само масивът от индекси, без обвивка: 232 323 B. За сравнение — `q` като цяло число на всеки от 86 232 записа в `search_index.json` (най-лошият случай, всички записи): +594 412 B суров, gzip +154 446 B.

Оценките в `ПЛАН_Адресите_по_полигон_08.09.md:326` („+1,26 / +1,54 MB“, обявени за непотвърдени) са с 21–48 % над измереното за (а).

Варианти (а) и (б) са неизпълними без промяна в `Varna_buildings`: `js/test_fire_varna_publish_gate.mjs:253-262` изисква `field_order` с дължина 3 и редове-3-торки, а `docs/decisions/007_address_path_v2.md:13` държи `data/address_rows.json` в „Untouchable“.

---

# МЯРКА 2 — Б3 и замразените референции (одит, само четене)

**Базата.** `C:/git/Fire_Varna` main `74c165f`, `git rev-list --count origin/main..main` = **2**. Чист клонинг на `74c165f`: `python -m unittest discover -s tests` → **Ran 315 · OK, изход 0**. Работно дърво: **Ran 342 · FAILED (failures=24)**. Стейджът не е пипан; двата мръсни проследени файла (`scratch/places_search/lot1v_v_reference_manifest.json` 174 717 B, `scratch/places_search/probe_out/token_parity.json` 197 432 B) са с mtime **11.09 06:42**, преди този одит — прогоните ми не ги пренаписаха. `python -m gates.release` **не можах да пусна** (блокиран от класификатора) — заместих го с преки мерки през `gates.release.body_digest`/`blob_at`.

**Приписване на 24-те червени — измерено, не прието.** Клонинг на `74c165f` + САМО трите стейджнати блоба `data/places.json`/`hotels.json`/`place_categories.json` → `tests.test_places_search_gate`: **120 теста, 23 паднали**. Добавянето на стейджнатия `index.html` маха точно два (`Lot1vVGateTest.test_the_client_closed_lists_are_the_delivered_codes`, `.test_the_client_pins_the_dictionary_bundle_sha`) → **21**. Плюс 3 в `test_b3_gates` = **24/24 са на Б3; наследено червено = 0**. Съвпада дума по дума с ИБ-1 (`docs/plans/ПЛАН_Картата_imot_И-А_08.09.md:636`).

## 1 · Какво доставя Б3 и кое оцелява при квартал по полигон от v2

Подписът: `docs/plans/ПЛАН_Б3_07.09.md:892-895` (§14, „по препоръките", 17 решения от §9 `:814-836`); §13 т. 5 `:884` (цифрите `1`/`2` НЕ влизат в `M7_PREFIXES`, иначе детската заявка получава родителския отговор).

Доставката (мерена върху стейджа): places **150**, hotels **225**, добавени 0, изтрити 0, **57 реда със сменени `(quarter.name, zone)`** = 42 places + 15 hotels — точно `SIGNED_POLYGON` редовете. `quarter_attribution`: places **14** кода (13 wikimapia + 1 openstreetmap), hotels **7** (всичките wikimapia); `_meta` 10/8 ключа. Обединение на кварталните кодове в доставката = **28**.

**Умира при v2** (всичко е вързано за v1/Wikimapia):
- трите блоба — 57-те `SIGNED_POLYGON` реда са изведени от v1-полигоните;
- пиновете `index.html:6291-6293` (`eb8fa85c…`/`3dffc264…`/`9064705a…`) и `LEGACY_BUNDLE_SHA` `:6304`;
- `QUARTER_CODES` (28 кода в стейджа) — v2 носи 95 кода, от които 23 клас `locality` (ИБ-11, `:656`); всеки v2-код пада на `validLocation` → `accept` → `null` → `ensurePlaces` **хвърля** (механизмът е измерен в §1.6 `:134-145`);
- `validQuarterAttribution` + `ATTRIB_SRC = ['wikimapia','openstreetmap']` + `WM_URL` (стейджнат `index.html`) — извор, който v2 няма;
- низът за атрибуция (338 знака, sha `c6d29d4e…`) е дословно за Wikimapia + „каре Младост 2 по OSM"; `tests/test_b3_gates.py:34` сочи **отменения** `granitsi_decisions_4_2026-09-07_proba.json` (ИБ-7, `:648`);
- пинатите числа в `scratch/places_search/granitsi_fixtures_07.09.json` и всяка замразена референция — всяко `n` минава през кварталната дума.

**Оцелява** (типово, без списък от кодове): `isFallbackQuarter`/`ownQuarter` на шестте места (стейджнат `index.html`; огледалото `scratch/places_search/recall_sweep.py:601-632`); `LOCALITY_SRC` (О18); `metaKeysAre` като затворено МНОЖЕСТВО имена; буквената поправка `M7_PREFIXES` в двата двигателя (`index.html:6512` / `recall_sweep.py:3139`) — ИБ-22 (а) `:674` разширява СЪЩИЯ списък с `kvartal`/`zhk`; скелето на гейтовете `gates/probe/b3_g11.py`, `tests/granitsi_client_probe.mjs` и G8.

## 2 · Стейджът — 14 пътя

`git diff --cached --stat`: 3 843 вмъквания / 1 256 изтривания. Данни (3 блоба, байтов препис); `gates/probe/b3_g11.py` (+121, G11); `index.html` (+106/−24 — кешът v6→**v7**, трите sha, `QUARTER_SRC` +`SIGNED_POLYGON`+`DISTRICT_FALLBACK`, нов `LOCALITY_SRC`, `QUARTER_CODES` 16→**28**, `M7_PREFIXES`+`MR`, `validQuarterAttribution`, `META_KEYS_*`, маркерите „Б3 slice"); фикстурите `granitsi_fixtures_06.09 → _07.09` (855 D / 1 572 A); `probe_places_fv.mjs` (2 реда); `recall_sweep.py` (+66/−66 — огледалото); `tests/granitsi_client_probe.mjs` (+278); `tests/test_b3_gates.py` (+202); `test_granitsi_fixtures.py`/`test_hotels_public_bundle.py`/`test_places_public_bundle.py` (типовите правила на шестте места).

**Червено днес в `tests/test_b3_gates.py` — 3 от 5, по конструкция (`:11-14`, план §4 стъпка 12б):**
- `MapAttributionTest.test_add_attribution_receives_the_quarters_string` (`:167`) — сондата връща `added = ['© OpenStreetMap']`; **И11 го няма** — стейджнатият диф на `index.html` не докосва нищо над `:6253`, срезът на атрибуцията `:1900-1918` е непипнат;
- `.test_the_string_occurs_exactly_once_and_matches_the_decisions_file` (`:175`) — `index_text().count(want)` = **0**;
- `.test_the_queue_row_is_signed_and_both_digests_match` (`:189`) — **0 реда** с тяло `c6d29d4e…` в `scratch/places_search/ЗА_ПОДПИС_A.md` (27 реда, всички „да", последно пипната от `c060f43`).
- `CardHasNoAttributionTest` (и положителната, и посадената отрицателна половина) е **ЗЕЛЕНА** — 375 картончета, нула забранени низа.

**Опашката и allow-ът на Б3 НЕ са изпълнени.** `gates/probe/b3_g11.py:40-46` (`ALLOWED_NEW`) назовава три пътя, които не съществуват: `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`, `gates/allow/2026-09-07_b3.json`, `scratch/places_search/архив/АРХИВ_A_05.09.md` — тоест §4 стъпки 10-14 и решения §9 т. 8/9/14 стоят неизпълнени.

Червената линия държи: `python gates/probe/b3_g11.py HEAD --cached` → `{"scope": 19, "geo_hits": [], "unreadable": [], "stray_new": []}`, **изход 0**. Първо зареждане върху стейджа: `index.html` 566 532 B + `data/hydrants.json` 1 321 623 B = **1 888 155 B ≈ 1,80 MB** при таван 5 MB (планът §1.8.13 `:198` пише 1 878 210 — **числото е остаряло**, HEAD се е преместил); отложената доставка = 357 662 B.

## 3 · Замразените референции и механизмът на презамразяване

**Зависят от кварталната дума (21-те червени):** `tests/test_places_search_gate.py` — `P7RuleTest:197` (3 метода), `P7GateTest:277` (2), `FrozenDiffTest:294`, `Lot1GateTest:407` (3), `Lot1vAGateTest:533` (2), `Lot1vAdditiveFreezeTest:690`, `Lot1vABucketTest:772`, `Lot1vBGateTest:885` (2), `Lot1vBAdditiveFreezeTest:1019` (2), `Lot1vBBucketTest:1131`, `Lot1vVGateTest:1245` (2), `M7GateTest:1446`. **Зелени при същите данни:** `ImportGuardTest`, `RefBucketsTest`, `AnchorsReachableTest`, `ReleaseGateSignatureTest`, `RefusalSurvivesTheFreezeTest`, `FreezeAndAnchorTest`, `PlacesCacheNameTest` (приема v7), `Lot1FormTableTest`.

P7 поименно: `expectations.json.p7` = **tokens 2 / zones 2**; доставката дава **7 в 5** (`gratska, gratski, konstanin, varnenchik, vladislav, zhkizgrev, vasil`), `vasil` е и **име**-токен (`:220`), а `vladislav` е изрично в `foreign_guard` (`:256`) — три отделни пропадания + „no gate query exercises the added token gratska" (`:289`).

**Пиновете.** `scratch/places_search/expectations.json` `_meta`: `frozen: true`, `signed_by: "Петър"`, `reference`/`candidate` sha `61967588780f…`, `inputs["data/places.json"].sha256 = 329310f5…` (блобът на HEAD). Б3 сменя И данните, И двигателя (`recall_sweep.py`) → **и двата пина падат**. `gates/allow/` = точно един файл `2026-09-05_lot1v_v.json` (`signed_by "Петър"`, `date 2026-09-05`, **150 реда**); `gates/baseline/MANIFEST.json` = `signed_by "Петър"`, `rev f06ac06…`, трите блоба. По §9 т. 9 baseline остава `f06ac06`, но новият allow (138 реда) не съществува, а `run_gates` пада при >1 allow-файл (§1.9 `:215`).

**Механизмът.** `scratch/places_search/recall_sweep.py:90-97` — само `--freeze` пише проследени файлове, `--manifest` е report-only (но `:4249-4253` пренаписва проследения паритетен файл при всеки не-freeze прогон — оттам двата мръсни файла). `freeze_blockers` (`:3690-3706`) взема **присъдата на release дословно**: при изход ≠ 0 `freeze_writes` (`:3709-3726`) не вика нито един писател → „ЗАМРАЗЯВАНЕТО НЕ Е ИЗВЪРШЕНО", нула байта. `gates/release.py:644-694` `yes_row_authorship`: за всеки ред „да" **и най-новият, и най-старият** комит на дословния блок (`git log -S`) трябва да са с автор `HUMAN_AUTHOR = "Petar1984"` (`:214`); `run_gates` проверка 7 чете същата функция (`:84`). `gates/sign.py:139-147` `refuse_if_agent()` + `AGENT_IDENTITIES` (`:98`) и `:216-222` искат git-авторът да е Петър. **Извод: агент не може да презамрази — подписът е ръката на Петър.**

**ПОТВЪРДЕН БЛОКЕР, наследен, НЕ от Б3.** `gates.release.body_digest` на `scratch/places_search/expectations.json` **в HEAD** = `55cbf2c7f8f2…`, а подписаният ред **R8** в `scratch/places_search/ЗА_ПОДПИС_A.md` носи `тяло: f8c4e43f5e85…`. Разминават се при **нула** промени от работното дърво. Сценарий на провала: release никога не е зелен → `--freeze` се отказва → **21-те червени референции не могат да бъдат презамразени от никого**, докато Петър не преподпише R8. Това е ИБ-2 (`:638`), но мярката ми го закотвя в **HEAD**, не в работното дърво.

## 4 · ИБ-1…ИБ-23 — предпоставка или чакане

**Предпоставка за квартал-по-полигон на живата карта:** ИБ-11 (`:656`, преизносът 60→95, `quarter.parent`/`parent_display`, четирите `KIND_NORM` с **два тихи** отказа — `qa_fire_varna_places_export.py:355`→`:401` мълчалив DROP и `qa_fire_varna_export.py:201`→`:247` тих `None`); ИБ-6 (`:646`, котвите в `index.html` — без пребазиране клиентът отказва целия пакет); ИБ-12 (`:658`, деветте изчезващи имена, 685-те адреса, `data/approx_addresses_v1.json` — това Е адресната страна на целта); ИБ-2 + ИБ-3 (`:638`, `:640` — гейтът е червен ПРЕДИ лота: R8 + coverage изход 2 с 30 непокрити); ИБ-1 (`:636`, обявеният интервал и точният набор); ИБ-8 + ИБ-9 (`:650`, `:652` — опашка/allow механика; `ALLOWED_NEW` е затворена седморка); ИБ-22 (`:674`) — (а) е изпълнимо днес, (б) е **заключено от ИБ-11** и само обявява, че презамразяването на `granitsi_fixtures_07.09.json:521-570` иска подписа на Петър (пинатото `n: 0` за „възраждане 2"/„ж.к. възраждане 2" е подписано 07.09 §14 т. 1); ИБ-7 (`:648`) — иначе трите червени теста остават червени завинаги; ИБ-19 (`:672`) — самият план го слага преди първата публична доставка Б4.

**Може да чака:** ИБ-5 (`:644`), ИБ-10 (`:654`), ИБ-13 (`:660`), ИБ-14 (`:662`), ИБ-16 (`:666`), ИБ-17 (`:668` — байтовият пин държи днес), ИБ-20 (`:680`), ИБ-21 (`:678`), и Ф2/Д4 половината на ИБ-23 (`:676`).

**Отделно от функционалния път, но по-лошо от записаното:** ИБ-4 (`:642`) казва „приватностно нарушение вече в HEAD". Измерено: `scratch/places_search/adresi_astra_S39_08.09.md` е **в `origin/main`**, тоест **вече публикувано** — `advert_id` 1, `raw_sha256` 1, `mob_api` 3 попадения, еднакви в HEAD и в `origin/main`. `gates/probe/b3_g11.py:105-106` е структурно сляп за `.md` (обхват: проследени `data/*.json` ∪ променени `*.json/*.geojson`) — гейт, който би хванал това, няма. Същият клас са ИБ-15 (`:664`) и ИБ-18 (`:670`); Д5-половината на ИБ-23 (`docs/decisions/011_kartata_imot.md:11` срещу `:55`) е в документа, който Петър чете на Gate 2.

---

# МЯРКА 1 — живата карта днес (11.09.2026)

Мерено в `C:\git\Fire_Varna` върху **работното дърво** (със стейджната Б3). HEAD = `74c165f`; стейджът има 14 пътя, `index.html` +130/−24 (`git diff --cached --stat`). Номерата на редовете са от работното дърво; където Б3 ги измества, отбелязвам.

---

## 1) Как index.html зарежда и ползва двата товара

| Въпрос | Мярка | Път:ред |
|---|---|---|
| URL-и | `data/search_index.json`, `data/address_rows.json` | `C:/git/Fire_Varna/index.html:5325-5326` |
| Кога | **НЕ на първо зареждане** — лениво, при `focus` на полето за адрес; и при заявка (cold-load прозорец) | `index.html:6200` (`focus` → `ensureSearchData()`), `:6193`, `:6220`, `:5065` (coord клон) |
| Как | `Promise.all` на двата товара, после `prepareIndex(idx)`, и чак тогава `searchIndex = idx` | `index.html:5351-5372` |
| Кеш | Cache API `fire-varna-search-v2`, мрежа първо (`cache:'no-cache'`), офлайн fallback от кеша | `index.html:5327`, `:5331-5349`; `sw.js:46,53-54,76` |
| Лимит резултати | `RESULT_LIMIT = 10` | `index.html:5328` |

**Формат на `data/search_index.json`** (11 242 756 B, sha `c12f9425…`):

| Ключ | Стойност |
|---|---|
| `index_schema_version` / `kind` | `2.0` / `fire_varna_search_index` |
| `district_names` | 5 имена (Аспарухово, Владислав Варненчик, Младост, Одесос, Приморски) |
| `address_row_count` | 80 510 |
| `entries` | **86 232** — `address` 70 575, `mf` 14 687, `parcel` 970 |
| `vocab` | 2 889 токена |
| Полета по записи | `kind` 86 232, `pin` 86 232, `tk` 86 232, `d` 85 935 (297 без), `display_id` 43 295 (42 229 уникални), `label` 43 133, **`qtk` 19 494**, `g` 14 687, `dtk` 11 237, `btk` 5 567, `en` 4 764, `alias_tk` 574, `stk` 362 |

`data/address_rows.json` (5 073 137 B, sha `2a4766bd…`): `schema_version 2.0`, `field_order = ["normalized_address","lat","lng"]`, `rows` = **80 510**.

**Откъде идва кварталната дума на адрес:** от **текста**, зашит в `entry.label` при билда (Varna_buildings), и от `qtk` за area-gating. Няма поле „код на квартал“ никъде в индекса. Разпределение на префикса на 43 133-те `label`-а: латиница (без квартал) 30 284, `кв.` 7 105, друго 3 855, `ж.к.` 1 557, `м-т` 149, `к.к.` 108, `с.о.` 65, `ул.` 9, `бул.` 1. Верига на извеждане: `label` → иначе `addressRows[display_id].normalized_address` → иначе името на **района** → иначе `(адрес)` (`index.html:4881-4892`, `baseAddressLabel`); вход `· вх. <en>` (`:4893-4897`).

**Мярка „студентска бл 11“:**

| Какво | Стойност |
|---|---|
| Ред в `address_rows.json` | id 45949, `normalized_address = "студентска бл 11"` (без квартална дума) |
| Записи в индекса за id 45949 | **0** (редът не е сочен от нито един запис) |
| Записът, който отговаря на заявката | `kind:"mf"`, `tk:["studentska","bl","11"]`, **`qtk:["chaika"]`**, `dtk:["primorski"]`, `btk:["11"]`, `d:4`, **`label:"кв. Чайка, бл. 11"`** |
| Какво ще покаже картата | заглавие „кв. Чайка, бл. 11“ + мета ред „район Приморски“ |
| Какво казва v2 (измерено с point-in-polygon върху `varna_3d/data/quarters_signed.geojson`) | клетки `kv_levski` (родител) + **`levski1`** (лист) |
| Непоследователност на същата улица днес | бл. 11/12/13/14 → „кв. Чайка“; Студентска 1 / бл. 3 / бл. 4 / бл. 7 → „кв. Левски“; всичките са в `levski1` по v2 |

**Показване на резултат** (`index.html:5411-5423`, `buildExactItem`): чип по вид (`адрес` / `сграда` / `вход` / `парцел`, `:5383-5388`), заглавие `formatAddressHit(r)`, и втори ред `'район ' + districtNames[r.d]` — **само район, никога квартал като отделно поле**. Групова шапка „N блока № X в район Y“ — `:5393-5399`.

**Сверка на текстовата дума срещу v2** (9 002 `label`-а с типов префикс на квартал): **съвпадат 4 842 · разминават се 4 121 · 39 падат извън всички клетки**. Топ разминавания (днес → v2): владиславово→владислав варненчик 2 (535), владиславово→владислав варненчик 1 (426), левски→левски 2 (316), св. иван рилски→максуда (302), виница→манастирски рид (222), розова долина→аспарухово (184), владиславово→кайсиева градина (154), дружба→аспарухово (151), чайка→левски 1 (79), чайка→базар левски (72).

**Независима сверка на маската на билдъра** (95 полигона × 80 510 точки, shapely): 0 клетки → **2 274**; 1 клетка → 78 235; 2 клетки → 1 (тай-брейкът). Тоест **78 236 в точно една листова клетка** — числото от брифа се потвърждава. Забележка: и петте виртуални родителя НОСЯТ геометрия (`geometry_origin = imot_bg_points_union`), затова по всичките 95 разпределението е 0→2 274, 1→71 245, **2→6 991** (дете+родител).

---

## 2) Първо зареждане и таванът

| Какво се тегли преди картата да е годна | Байтове (работно дърво) | Байтове (HEAD) |
|---|---|---|
| `index.html` (вграден Leaflet + MarkerCluster + CSS + логика) | 566 532 | 560 855 |
| `data/hydrants.json` (`fetch` при init, `index.html:1774`) | 1 321 623 | 1 321 623 |
| **Общо първо зареждане** | **1 888 155 B = 1,80 MiB** | 1 882 478 B |

Всичко останало е лениво и НЕ влиза: `data/search_index.json` + `data/address_rows.json` (`:6200`, focus), `data/hotels.json`+`data/places.json`+`data/place_categories.json` (`:7475`, focus), `data/basemaps/basemap_manifest.json` (`:4565`, `:4586`), `data/approx_addresses_v1.json` (`:5927`).

**Точният текст на тавана**, `C:/git/Fire_Varna/AGENTS.md:137`:

> `| First load <= 3 MB ideal, **5 MB hard cap** | Mobile data, emergency use |`

Байтовата дефиниция **не е записана никъде**. Единствената улика е `docs/activeContext.md:43` — „first load (`index.html` + `data/hydrants.json`), hard cap 5 MB | **1876131 B = 1,79 MB**“: 1 876 131 / 1 048 576 = 1,789, тоест конвенцията е **MB = MiB → 5 MB = 5 242 880 B** (при 10⁶ щеше да пише 1,88). Grep за `5242880 | 5000000 | 5 * 1024 * 1024` в `AGENTS.md`, `tests/`, `gates/`, `scripts/` дава **0 попадения** — **няма машинен гейт за тавана**, само ред в документ. Самият ред е остарял: числото 1 876 131 предполага `hydrants.json` = 1 315 276 B, а файлът е 1 321 623 B (+6 347).

Запас до тавана: 5 242 880 − 1 888 155 = **3 354 725 B**. Двата товара на търсачката са 16 315 893 B — 3,1× тавана — затова стоят лениви.

---

## 3) Затворените списъци и кои клонове ги четат

| Константа | Брой днес | Път:ред (работно дърво / HEAD) |
|---|---|---|
| `DISTRICT_CODES` | **5** | `index.html:6322-6323` / HEAD `:6315` |
| `QUARTER_CODES` | **28** (Б3 ги вдигна от 20) | `index.html:6324-6331` / HEAD `:6317-6321` |
| `LOCALITY_CODES` | **5** | `index.html:6332` |
| `QUARTER_SRC` | 5 (`REG, KAIS, SIGNED_OVERRIDE, SIGNED_POLYGON, DISTRICT_FALLBACK`) | `index.html:6316` |
| `LOCALITY_SRC` | 4 (нов в Б3) | `index.html:6321` |
| `DISTRICT_SRC` | 2 | `index.html:6322` |
| `DISTRICT_MARK` | `'район'` | `index.html:6333` |
| `KIND_GROUP` | 12 вида → 9 групи | `index.html:6373-6382` |
| `KIND_CHIP` | 10 вида | `index.html:6383-6388` |
| `GROUP_COLOUR` | 9 групи → 3 цвята (`hotel/edu/health`) | `index.html:6391-6397` |
| `M7_PREFIXES` | 8 букви (`k,kv,zh,m,s,o,t,i`) | `index.html:6512` |
| `STREET_MARK` | 3 (`ул,бул,пл`) | `index.html:7076` |

**Кой ги чете:** единствените читатели на `QUARTER_CODES`/`LOCALITY_CODES`/`DISTRICT_CODES` са `validTypedLocation` (`index.html:6557-6573`), викан от `validateHotels` (`:6575`) и `validatePlaces2` (`:6591`) — валидатори на **bundle-ите `data/hotels.json` / `data/places.json`**, fail-closed (непознат код → целият bundle се отхвърля). **Нито един от тези списъци не се чете от адресната търсачка** (`initAddressSearch`, `:4835-5470`) — адресният квартал минава изцяло през `label`/`qtk` от `search_index.json`. `KIND_GROUP`/`GROUP_COLOUR` са за ВИДА на обекта (хотел/училище/болница), нямат връзка с квартали.

**Клонове на търсачката на места:**

| Клон | Ред | Чете |
|---|---|---|
| М7 „гола локационна дума“ | `index.html:7117-7150` | `r.qtk` / `r.ltk`, `dHit` през `!ownQuarter(r.e)`; `MR` = заявката без `M7_PREFIXES` |
| А3-street (`ул./бул./пл.`) | `:7076-7104` (`streetRows`), викан на `:7177-7180` | `STREET` фраза, стои ПРЕД кварталния клон |
| Явно „район X“ | `:7158-7163` (без ключ) и `:7184-7189` (с ключ) | `DISTRICT_MARK` + `r.dph` |
| Гола локационна фраза | `:7196-7205` | `r.qph` / `r.lph` / `r.gph` / `r.dph` |

**Покритие спрямо 95-те кода на v2** (`varna_3d/data/quarters_signed.geojson`, HEAD `1a0595d`, 95 Feature-а, 41 свойства, kind: кв 38 / с.о. 15 / жк 14 / м-т 13 / местност 4 / кк 4 / пз 4 / зона 2 / вз 1; 17 деца под 5 родителя, от които **10 номерирани**: levski1/2, mladost1/2, vazrazhdane1-4, vladislav_varnenchik1/2):

| Мярка | Число |
|---|---|
| `QUARTER_CODES ∪ LOCALITY_CODES` днес | 33 |
| Пресичане с 95-те | **28** |
| В index.html, но **няма** ги в v2 | **5**: `druzhba`, `morska_gradina`, `sv_ivan_rilski`, `trakia`, `vilite` |
| В v2, но **няма** ги в index.html | **67** |

Реално доставени кодове в стейджнатите bundle-и: `hotels.json` — 13 различни кода (`by_zone_src`: REG 115, district 58, KAIS 25, SIGNED_POLYGON 15, SIGNED_OVERRIDE 12); `places.json` — 25 кода (SIGNED_POLYGON 42, REG 39, KAIS 10, district 59). **`DISTRICT_FALLBACK` не се среща в нито един ред** — `isFallbackQuarter`/`ownQuarter` (`:6551-6556`) днес са мъртъв код по данните.

---

## 4) Кой строи двата товара и с какво са замразени

| Роля | Път |
|---|---|
| Строи `search_index.json` | `C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs` (изход по подразбиране `../Fire_Varna/data`, `:131-133`) |
| Строи `address_rows.json` | `C:/git/Varna_buildings/js/build_fire_varna_address_rows.mjs:58-60`, `field_order` на `:110` |
| Строи `generation_manifest.json` | `C:/git/Varna_buildings/js/build_fire_varna_manifest.mjs` |
| Publish-гейт (privacy) | `C:/git/Varna_buildings/js/test_fire_varna_publish_gate.mjs` |
| Кварталната дума в билда | `build_fire_varna_search_index.mjs:147-170` (зона „кв. Виница“, Р38, подпис 12.08), `:876-905` (добавя `VINITSA_TOKEN` към `qtk`, **само допълва, никога не реже**), `:393-500` (S9 override на token-INCONSISTENT `label`-и) |

**Пинове в Fire_Varna — измерено:**

| Гейт/пин | Какво покрива двата товара |
|---|---|
| `tests/test_basemap_manifest.py:164-165` | Само че низовете `data/search_index.json` / `data/address_rows.json` присъстват в `sw.js` и стратегията е `networkFirst` — **без sha, без брой** |
| `tests/test_data_ascii_mojibake.py:35-36,43` | Сканира двата файла за `\?{3,}`; `KNOWN_BROKEN_LABELS = frozenset()` (празна база от 13.08) — **без sha, без брой**; 4 теста |
| `data/generation_manifest.json` | **Единственият sha-пин**: `search_index.json` sha `c12f9425…` / 11 242 756 B / 86 232 записа / vocab 2 889; `address_rows.json` sha `2a4766bd…` / 5 073 137 B / 80 510 реда; `generation_id a8fc1ca4`. Сверих: **и двата sha съвпадат** с HEAD-blob И с работното дърво. **Никой тест, гейт или `index.html` не го чете** — единственото попадение при grep е `scratch/audit_2026-09-03/сгради/make_summary.py:27` |
| `gates/baseline/MANIFEST.json` | Пинова само **3 файла** — `hotels.json`, `places.json`, `place_categories.json` (подпис „Петър“, 05.09, rev `f06ac06`). Двата адресни товара **липсват** |
| `scratch/places_search/expectations.json` | 0 споменавания на двата товара |

Контраст: bundle-ите на местата имат sha-пин **в клиента** — `HOTELS_SHA256` / `PLACES2_SHA256` / `CATS_SHA256` (`index.html:6290-6292`) + `LEGACY_BUNDLE_SHA` (`:6304-6306`). Адресните товари нямат такъв пин в клиента.

---

## 5) Какво прави Б3 в стейджа (по функции)

`git diff --cached -- index.html` = 20 хънка, +130/−24. Всичко е в `initPlacesSearch` (места/хотели) — **нито един ред не пипа `initAddressSearch`, адресния индекс или първото зареждане**.

| Ред (нов) | Функция / константа | Промяна |
|---|---|---|
| `:6256`, `:7235` | маркери | „Б3 slice start/end“ коментари, DOM-free срез |
| `:6269` | `PLACES_CACHE` | `fire-varna-hotels-v6-225` → **`v7-225`** (инвалидира кеша на устройството) |
| `:6290-6292` | `HOTELS_SHA256`, `PLACES2_SHA256`, `CATS_SHA256` | нови стойности; **сверих: съвпадат байт-по-байт със стейджнатите blob-ове** (`eb8fa85c…`, `3dffc264…`, `9064705a…`) |
| `:6304-6306` | `LEGACY_BUNDLE_SHA` | същите два нови sha |
| `:6316` | `QUARTER_SRC` | +`SIGNED_POLYGON`, +`DISTRICT_FALLBACK` (3→5) |
| `:6321` | `LOCALITY_SRC` | **нова** константа — отделя локалността от разширения `QUARTER_SRC` (О18) |
| `:6324-6331` | `QUARTER_CODES` | 20 → **28** (+`dolna_traka`, `grackata_mahala`, `hristo_botev`, `kolhozen_pazar`, `kv_levski`, `sv_ivan_rilski`, `trakia`, `tsentar`) |
| `:6507-6512` | `M7_PREFIXES` | **нова** — 8 буквени префикса, 1:1 с `recall_sweep.py` |
| `:6551-6556` | `isFallbackQuarter`, `ownQuarter` | **нови** — `DISTRICT_FALLBACK` квартал не се чете като квартал |
| `:6557-6573` | `validTypedLocation` | клон за fallback (код от `DISTRICT_CODES`, име+код = районът на реда); локалността минава на `LOCALITY_SRC`; `zone` приема и двете форми |
| `:6575`, `:6591` | `validateHotels`, `validatePlaces2` | +`metaKeysAre(...)` и +`validQuarterAttribution(...)` |
| `:6613-6641` | `validQuarterAttribution`, `ATTRIB_KEYS/SRC`, `WM_URL`, `OSM_URL`, `META_KEYS_HOTELS/PLACES`, `metaKeysAre` | **нови** — картата `_meta.quarter_attribution` трябва да е **точно равна** на множеството `SIGNED_POLYGON` кодове в bundle-а. Измерено в стейджа: hotels 7 = 7 ✔, places 14 = 14 ✔ |
| `:6824`, `:6857` | `locTokens`, `locPhrases` | `h.quarter` → `ownQuarter(h)` |
| `:7133-7150` | клон М7 | `R` → `MR` (заявката без буквените префикси) на 5 места; `!r.e.quarter` → `!ownQuarter(r.e)` |
| `:7198` | клон „гола локационна фраза“ | `!r.e.quarter` → `!ownQuarter(r.e)` |
| `:7347` | картата на място | `h.quarter ? h.quarter.name` → `ownQuarter(h) ? …` |

Данни в стейджа: `hotels.json` +169/−? реда (225 записа, 8 `_meta` ключа), `places.json` (150 записа, 10 `_meta` ключа), `place_categories.json`. Нови файлове: `gates/probe/b3_g11.py` (121), `tests/test_b3_gates.py` (202), `tests/granitsi_client_probe.mjs` (278), `scratch/places_search/granitsi_fixtures_07.09.json` (1572, замества версията от 06.09).

**Разминаване, което мярката хваща:** `gates/baseline/MANIFEST.json` държи sha от `f06ac06` (`hotels 434d15d5…`, `places c31a866e…`, `cats 7fb4ddb6…`) — те **не съвпадат нито със стейджа, нито с HEAD** (HEAD: `46a44ce8…`, `329310f5…`, `874e33cd…`). `gates/run_gates.py:60` и `gates/release.py:183` четат точно този базов манифест.
