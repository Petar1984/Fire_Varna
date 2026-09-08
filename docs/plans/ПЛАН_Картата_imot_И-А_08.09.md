# ПЛАН · Картата imot — под-лот **И-А** (varna_3d + документи)

`Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` · 08.09.2026 · **редакция 4** (след шест одиторски кръга: два общи + „И-А кръг 1“, „И-А кръг 2“ и двата кръга върху редакция 3) · Планировчик (Opus, само четене) → **подпис на Петър (Gate 1)** → Изпълнител → Одитор → локален преглед → **Gate 2 и пуш от Петър**

**Какво прави този лот.** Прави плочката на imot.bg **канонична геометрия** в частното репо `varna_3d` — замразеният вход, подписаното тяло с решенията, нов билдър, негов собствен гейт, архив на v1 — и допълва три документа във Fire_Varna. **Нищо във Fire_Varna освен тези три проследени документа и един поименно обявен ИГНОРИРАН файл за преглед не се пипа.** Живата карта, доставката Б3, `index.html`, `data/`, `tests/`, `gates/` на Fire_Varna остават непроменени и си остават работа на **И-Б**.

**Предшественик.** `docs/plans/ПЛАН_Картата_imot_08.09.md` (редакция 4, **156 024 B, 735 реда, непроследен** — М: `wc -c -l` → `735 156024`; `git ls-files --error-unmatch` → `did not match any file`). Този под-лот **изпълнява** неговите §3 И-А, §5.А и Приложение Б; всяко място, където се разминава с него, е ред в §2. Планът v4 остава на диска като предшественик и **не се изтрива**.

Всяко число долу носи котва: **(Ч)** = `файл:ред`, **(М)** = командата, която пуснах, и изходът ѝ. Числа без котва в този план няма. Всяко число на редакция 3, което този кръг обори, е поправено ТУК с нова мярка и е назовано поименно на мястото си.

---

## 0 · Червени редове

1. **Нищо не се редактира преди подписа.** Първата команда на Изпълнителя е `git status --porcelain`, не `Write`. **Единственото изключение, обявено поименно:** файлът `Д1` — самият този план — се записва на диска СЛЕД подписа и ПРЕДИ `К1`, защото файлът, който лежи там днес, е **друга редакция** (М: 109 670 B, 536 реда, заглавен ред „редакция 2 (след два одиторски кръга)“, непроследен). Записът на подписания текст **не е редакция на подписано тяло** — той Е тялото (стъпка 2, ИА-О22).
2. **Никакъв `git push`.** Пушът е само на Петър (универсален инвариант №1).
3. **Данните и геометрията ги комитва Петър** (ADR 010 D16, Ч `010_signed_quarter_boundaries.md:68`). Агентът ги оставя стейджнати с изричен pathspec.
4. **Fire_Varna: САМО три ПРОСЛЕДЕНИ документа (Д1, Д2, Д3) + един поименно обявен ИГНОРИРАН файл за преглед (Д4).** Никакъв ред в `index.html`, `data/`, `tests/`, `gates/`, `scratch/places_search/*.py|*.json`. Докосване на пети път във Fire_Varna = STOP.
5. **Нула квартална геометрия и нула суров провенанс в проследен файл на Fire_Varna.** Геометрията, `advert_id`, `raw_sha256`, `points` и **всяка координата** живеят само в **частното** репо `varna_3d` и в игнорираната папка на Fire_Varna (М: `git check-ignore -v scratch/boundary_gallery/granitsi_preview_05.09/imot_bg_varna_polygons_08.09.geojson` → `.gitignore:64:/scratch/boundary_gallery/`). **Този план е проследен файл на Fire_Varna — затова в текста му няма нито една двойка `lat/lon`; навсякъде, където предишна редакция цитираше координата, стои „(координата в частния файл)“. Спазването се съди механично от ИА-19.** Обобщени производни (площи, брой върхове, хистограма на ръба, хешове) **не са координати** и остават позволени — обявено в ИА-О24, дългът за правило и гейт е ИБ-18.
6. **Гейт, чиято команда не може да върне ≠ 0, не е гейт.** Всяка обявена отрицателна половина ТРЯБВА да е тичала и да е паднала с записан изход; „ще падне“ не е доказателство (поука `gates-lie-more-than-code`). **Ред, за който предварително се знае, че няма да падне, НЕ стои в колоната „отрицателна половина“** — той е мярка и се записва в отчета.
7. **Нула регресии.** Всеки от деветте измерени изхода на **§1.2** се запазва — **със заявената в §5 команда за съответната фаза** (преди и след преместването на v1 командата е РАЗЛИЧНА; изходът е същият). Различен изход = STOP.
8. **Подписано тяло не се редактира на място.** Нова версия — нов файл, стар в архива, никога `git rm`.
9. **Кодът е на латиница.** Имена на модули и коментари на английски; на български остават документите и текстовете за човек (поука `code-in-english`).
10. **Собствени пространства на номерата — затворени и без сблъсък по азбука.** Гейтове **ИА-1 … ИА-19**, отклонения **ИА-О1 … ИА-О24**, спирачки **ИА-STOP 1 … 17**, файлове **Ф1 … Ф10**, точкови редакции **Т1 … Т15**, разлики в подписаното тяло **Х1 … Х10**, пинове **П1 … П18**, база **Н1 … Н9**, решения **Р1 … Р21**, комити **К1 … К9**, дългове към И-Б **ИБ-1 … ИБ-18**. (М: `grep -rIl "ИА-[0-9]" C:/git/Fire_Varna/docs C:/git/varna_3d/src C:/git/varna_3d/docs` → **0 файла извън самия този план**.)
   **Пространството `Б` НЕ се използва от този план в нито един вид.** Кръг 3 намери, че `Б1…Б15` (точкови редакции) и `Б-1…Б-16` (дългове) се различаваха само по тире, а „Б1“ и „Б3“ вече значат живи лотове в кода (М: `build_quarters_signed.py:1408` `"lot": "Б1"`, `:1563` `fail("червена черта", …лот Б1…)`, `qa_quarters_signed.py:1197` „Gate Б1“) и живата доставка Б3. Затова редакциите станаха **Т**, дълговете — **ИБ**. Никакъв `G4`, `G11`, `G15`, `G17`, `G21`, `G22`, `G23`, `G29`; никакъв гол `О7`/`О8`/`О16` — те са заети в `ПЛАН_Б3_07.09.md:240`, `:241`, `:249` (Ч), а пространството `О` там стига до **О30** (Ч `:263`). **Латинско `A` не се използва никъде.**
11. **Лицензът не е тема.** Дословният низ за атрибуция се **попълва** по решение Р10; не се обсъжда, не се проучва.
12. **Sha на доставка = блобът.** Във Fire_Varna работното копие ≠ блоб. Във **varna_3d разлика няма**: `.gitattributes:4` е `* text=auto eol=lf` (Ч), М: `git check-attr -a data/quarters_signed.geojson` → `eol: lf`, и работното копие, и блобът дават `c1551d24…`, 301 917 B. Правилото пак е „чети блоба“; varna_3d просто няма как да те излъже.
13. **Блоб се адресира стабилно, не през HEAD.** Навсякъде, където се чете блоб, ревизията се взема с `git -C <репо> log -1 --format=%H -- <път>` (М днес за черновата с решенията → `7556227…`; за `district_resolutions_2026-09-07.json` → `e6c706d…`; HEAD на Fire_Varna е `7556227` — съвпадението с първия е случайно и **не се ползва**). **Вход, който НЕ живее в никое git-репо, не може да се адресира по това правило и се пинва по sha256 на прочетените байтове** — това е точно случаят на слоя с петте района (Р21, ИА-О23).

---

## 1 · Мярка (всичко мерено 08.09; нула редакции)

### 1.1 · Състояние на репата

| | стойност | котва |
|---|---|---|
| `varna_3d` HEAD | `05f485e` · `Petar1984` · 2026-09-07 · „data: p8a quarter assignment ledger 07.09“ | (М) `git -C C:/git/varna_3d log -1 --pretty='%h %an %ad %s' --date=short` |
| `varna_3d` клон | `rezhimi` | (М) `git branch --show-current` |
| `varna_3d` ahead от `origin/main` | **74** | (М) `git rev-list --count origin/main..HEAD` |
| `varna_3d` мръсни проследени | **1** — `scratch/place_bodies/qa_place_bodies.md` | (М) `git status --porcelain \| grep -v '^??'` |
| `varna_3d` непроследени | **41** | (М) `git status --porcelain \| grep -c '^??'` |
| `varna_3d` `core.autocrlf` / `.gitattributes` | `true` / `* text=auto eol=lf` (Ч `:4`) → **работно копие = блоб** | (М) `git config core.autocrlf`, `git check-attr -a` |
| `Fire_Varna` HEAD | **`7556227`** · `Claude Architect` · „docs: decisions draft — kind_registry mapping onto the closed KIND_NORM table …“ | (М) `git log -1 --pretty='%h %an %s'` |
| `Fire_Varna` ahead | **138** | (М) `git rev-list --count origin/main..HEAD` |
| `Fire_Varna` стейджнати пътища (Б3) | **14** (`M` places/hotels/place_categories/index.html/probe_places_fv.mjs/recall_sweep.py/test_granitsi_fixtures/test_hotels_public_bundle/test_places_public_bundle · `A` b3_g11.py/granitsi_fixtures_07.09.json/granitsi_client_probe.mjs/test_b3_gates.py · `D` granitsi_fixtures_06.09.json) | (М) `git diff --cached --name-status` |
| `Fire_Varna` мръсни НЕстейджнати | **3** — `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md`, `scratch/places_search/lot1v_v_reference_manifest.json`, `scratch/places_search/probe_out/token_parity.json` | (М) `git status --porcelain` |
| `Fire_Varna` приватностен гейт | `{"scope": 19, "geo_hits": [], "unreadable": [], "stray_new": []}` · **изход 0** | (М) `python gates/probe/b3_g11.py HEAD --cached` |
| **`Д1` на диска ДНЕС** | **109 670 B, 536 реда, непроследен, заглавен ред „редакция 2“**; носи **три двойки координати** (М: `grep -nE '4[23]\.[0-9]{4,}\|2[78]\.[0-9]{4,}'` → редове `:104`, `:474`, `:510`) | (М) — затова червен ред 1 има своето единствено изключение и затова съществува ИА-19 |

> Заб.: HEAD-ът на Fire_Varna мърда сам (Петър приема доклади за хидранти). **Нито един гейт и нито един STOP тук не пинва HEAD на Fire_Varna** — само блобове, адресирани по правилото на червен ред 13.

### 1.2 · Базата на `varna_3d` е ЗЕЛЕНА (за разлика от Fire_Varna) — **девет реда**

| # | команда (М, тичана днес) | изход | какво печата |
|---|---|---|---|
| **Н1** | `python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json` | **0** | 20 проверки C1–C20; печата и „решени по подписан файл (`d494d4d256ae…`, решение 9): `kochmar→mladost`, `vazrazhdane4→mladost`“ |
| **Н2** | `python src/qa_p8a.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` | **0** | „присвояването по подписани граници е годно за комита на Петър“ |
| **Н3** | `python src/qa_fire_varna_places_export.py` | **0** | „артефактът може да тръгне към Fire_Varna“ |
| **Н4** | `python src/qa_place_zone_aliases.py` | **0** | „passes — every quarter alias is a verbatim string of the registry“ |
| **Н5** | `python src/qa_fire_varna_export.py` | **0** | „артефактът може да тръгне към Fire_Varna“ |
| **Н6** | `python src/qa_fire_varna_location_isolation.py` | **0** | „глобалната стълба, майсторът и чуждата тема са непокътнати“ |
| **Н7** | `python -m unittest discover -s tests` | **0** | „Ran **16** tests … OK“ |
| **Н8** | `python src/qa_fire_varna_m6.py` | **3** | „ЧАКА ПОДПИС: **8** реда с `pending_signature` — билдът е здрав, но ПУБЛИКАЦИЯ и `--freeze` са забранени“ (М: `qa_fire_varna_m6.py:12` „блокът `pending_signature` брои същото · 8 срещу 8“) |
| **Н9** | `python scratch/granitsi/zone_alias_negatives.py` | **0** | харнесът на отрицателните проби на `qa_place_zone_aliases` (П13) |

**Изход 3 на Н8 е НАСЛЕДЕН и НЕ Е ЧЕРВЕН** (Ч `qa_fire_varna_m6.py:526` `sys.exit(3)`). Записва се като база; смяна на числото 8 = STOP.

**Н7 се сверява по ИМЕНА, не по брой.** Комит К4 добавя `tests/test_quarters_signed_imot_fixtures.py` — след него броят расте. Пинът е: **изход 0 И шестнайсетте днешни идентификатора са сред пуснатите, всичките зелени.** Снемат се със **стабилна** команда (не с `grep " ... ok"` — `-v` печата докстринга вместо името при 6 от 16-те, мерено):

```
python -c "import unittest;s=unittest.defaultTestLoader.discover('tests');
ids=lambda t:[y for x in t for y in (ids(x) if isinstance(x,unittest.TestSuite) else [x.id()])];
print(chr(10).join(sorted(ids(s))))"
```

М днес → **16 идентификатора**, всичките в `test_quarters_signed_fixtures.SignedQuartersFixtures`: `test_artifact_carries_the_signed_shape`, `test_build_refuses_a_moved_vertex_in_a_union_part`, `test_build_refuses_a_moved_vertex_in_the_frozen_set`, `test_build_refuses_a_moved_vertex_in_the_mladost2_face`, `test_build_refuses_a_resolution_against_the_au5_witness`, `test_build_refuses_a_resolution_for_a_code_without_a_dispute`, `test_build_refuses_any_other_output_name`, `test_district_disputes_are_named_and_resolved_by_the_signed_file`, `test_every_negative_fixture_actually_fails`, `test_gate_is_green_on_the_signed_artifact`, `test_gate_refuses_a_resolution_for_a_code_without_a_dispute`, `test_gate_refuses_a_resolutions_file_against_the_au5_witness`, `test_rebuild_is_byte_identical`, `test_the_resolutions_input_is_the_signed_file`, `test_the_union_is_the_geometry_petar_signed`, `test_union_recipe_is_declared_honestly`.

### 1.3 · Схемата на v1 (какво трябва да възпроизведе v2, ключ по ключ)

Блобът: **301 917 B**, `sha256 = c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3` (М).

- **Върхови ключове (3):** `_meta`, `features`, `type`.
- **`_meta` — 36 ключа** (М, поименно): `artifact_class, attribution, canonicalization, counts, d1_schema, decisions_author, decisions_based_on, decisions_blob_before_attribution, decisions_commit, decisions_path, decisions_sha256, decisions_sha256_rule, decisions_sha256_worktree, declared_deviations, district_resolutions, district_witness_agkk, district_witness_disputes, excluded, generated_by, inputs, licences, lot, method_licence, parent_child, parent_child_without_polygon, plan, precision_floor_m, precision_m_by_method, publication, registry_pending, rows_without_feature, signature, source_terms, union_crs, union_recipe, union_witness`.
- **Feature — 3 ключа:** `geometry`, `properties`, `type`. **`properties` — 41 ключа** (М): `approval_digest, approved_at, approved_by, attribution, basemap, chosen_reason, chosen_source, code, confirmed_at, confirmed_by, district, district_src, drawn_at, drawn_by, fetched_at, geometry_origin, imported_from, kind, license, license_label, license_terms, method, name, note, parent, parent_display, parent_geometry_check, precision_m, raw_geometry_sha256, screenshot_sha256, signed_by, source, url, version, viewport, visible_layers, witnesses, wm_id, wm_ids, wm_polygon_sha256, wm_title`.
- **Нулираните полета.** М поименно: **седемте** на `_meta.d1_schema.nulled_on_import` (`drawn_by, drawn_at, basemap, viewport, visible_layers, screenshot_sha256, approval_digest`) са `null` по **всичките 60**; `wm_ids` е непразно по **1**; `wm_id` — по **58**; `wm_title` — по **60**.
- `_meta.precision_floor_m = 50`; `_meta.artifact_class = "signed_by_plan_signature"`; `_meta.counts` = **12** полета; `_meta.licences` = **2**; **`_meta.parent_child` = 11 двойки** `{child,parent}` (М, поименно: `abatko→kk_konstantin_elena`, `druzhba→asparuhovo`, `kaisieva→vladislavovo`, `kokardzha_generic→izgrev_kv`, `mladost1→mladost`, `mladost2→mladost`, `rozova_dolina→asparuhovo`, `saltanat→morska_gradina`, `vazrazhdane1/2/3→vazrazhdane`); `properties.parent` е непразно само по **6** Feature-а (М) — **двата източника на родство НЕ съвпадат и авторитетът за родство е `_meta.parent_child`** (виж следващата точка); `_meta.parent_child_without_polygon = []`; `_meta.registry_pending` = **16**.
- **`_meta.rows_without_feature` на v1 има ДВЕ кофи — `alias_of` (1 ред: `vayalar → sredna_traka`) и `deferred` (6 реда)** (М, дословно). v2 ще носи същия ключ с **друг набор кофи** — това е обявено отклонение ИА-О21.
- **`_meta.excluded` носи ЕДИН ред** (М, дословно): `vinitsa_sever` · `display "с.о. Виница-север"` · `kind "с.о."` · `registry_action` „сутрешен ход на Петър: деактивиране на кода в `quarter_registry.json` — регистърът НЕ се пипа от изпълнителя“ · `why` „Петър (07.09): «Виница-север го изключваме» …“. **В черновата с решенията същият код е ред 6295 с `include = "да"` и `kind_registry = "вз"`, 294 сгради, 0,303 km² (М) — тоест v2 го връща. Обратът е решение Р17 и се записва, не се премълчава** (ИА-О15).
- **Геометрия:** 60 × `Polygon`. **Площ (М, EPSG:32635):** сбор **66,886 km²**, обединение **61,597 km²**, **51 застъпващи се двойки > 1 m²**.
  **ПОПРАВЕНО ЧИСЛО (кръг 3 обори „47“):** от 51-те двойки **11 са двойка от `_meta.parent_child`** (М, поименно: `abatko–kk_konstantin_elena`, `asparuhovo–druzhba`, `asparuhovo–rozova_dolina`, `izgrev_kv–kokardzha_generic`, `kaisieva–vladislavovo`, `mladost–mladost1`, `mladost–mladost2`, `morska_gradina–saltanat`, `vazrazhdane–vazrazhdane1/2/3`) → **40 застъпвания извън родство**. Числото „47“ се получава само ако родството се чете от `properties.parent` (само 6 непразни, 4 от които в застъпване) — **изворът на родството в целия този план е `_meta.parent_child`, изрично и навсякъде.**
- **Покритие (М):** v1 покрива **68 314 / 80 510 = 84,85 %** от адресните точки (при обявеното в §1.5 правило за развръзка).

### 1.4 · Замразеният снапшот на imot.bg (входът)

| | стойност | котва |
|---|---|---|
| `imot_bg_varna_polygons_08.09.geojson` | 175 736 B · sha256 `77b405640000a304ec5dca94f4865cc1b5a4d552c0edfc4847fa4663e6662a1f` | (М) |
| `imot_bg_varna_dictionary_08.09.json` | 6 274 B · sha256 **`feba76e3c816a3e313d8ace0dcb373b4a1ee4ecb9b6356a122254d4846d22fdf`** · списък от **98** `{id, name}` | (М) |
| `_meta` на снапшота | 12 ключа: `crs, dictionary_endpoint, dictionary_missing_polygons, dictionary_n, dictionary_sha256, fetched, list_endpoint, missing, n, raw_kept, source, tools`; `fetched = "2026-09-08"`, `n = 95`, `missing = []`, `dictionary_n = 98` | (М) |
| **`_meta.list_endpoint` — ДОСЛОВНО** | **`https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)`** — **с опашката**. **`url` в артефакта = точно този низ** (Р10) | (М) |
| **`_meta.dictionary_sha256` ВЪТРЕ в снапшота** | **`6fa3b07007203c5a5787d0af3e0d63c03d3a625dd741ab34c8dabe1965cbf38f`** — **НЕ е** sha на файла-речник. Това е хешът на **суровия отговор** на `dictionary_endpoint` (`https://api.imot.bg/mob_api/dictionary/search/1?town=5`), а суровият отговор е „scratchpad (private), not in the repo“ (Ч `_meta.raw_kept`). **Авторитетът за гейта е sha-то на ФАЙЛА (`feba76e3…`); вграденото число се записва като свидетел, който никой не сверява.** | (М) |
| Feature-и | **95**, всички `Polygon`, по 1 пръстен | (М) |
| свойства на Feature | `center, fetched, n_adverts, n_pts, name, provenance, raion, raion_num, slug, src`; `provenance = {endpoint, advert_id, raw_sha256, raw_bytes, fetched_local, field}` — **низът `raw_response_sha256` се среща 0 пъти**; `properties.fetched` има **една** стойност `"2026-09-08"` | (М) |
| **знаци след точката — ПОПРАВЕНО** | **7 640 числа** в `coordinates`, хистограма **{5: 7, 6: 53, 7: 642, 8: 6938}** — **кофа с 2 знака НЯМА**. (Контрола: 7 640 / 2 = **3 820** = сборът на `n_pts` в тялото с решенията.) *(Редакция 3 казваше „2, 5, 6, 7, 8 · 1/19/195/653/6963“ — нито едно от петте числа не съвпада; оборено и заменено.)* | (М) |
| и двата файла | **игнорирани** — `.gitignore:64:/scratch/boundary_gallery/` | (М) `git check-ignore -v` |

**Върху 79-те доставяни клетки (не върху 95-те), след канонизацията по D1:** **0 невалидни преди поправка** · **0 невалидни след канонизация** · **0 застъпващи се двойки с площ > 0** · **2 849 върха** · **2 137 различни отсечки** · **712 споделени отсечки** · дължина на ръба (EPSG:32635): медиана **96,5 m**, средна **130,4**, p10 **37,0**, p90 **257,5**, max **1 484,3**, min **8,92** · площ **74,615 km²** (М; редакция 3 даваше p10 37,1 / p90 257,4 / min 8,97 — премерено наново върху канонизираните клетки).

### 1.5 · Адресните точки — маската, затворена и сверена

`Fire_Varna/data/address_rows.json`: **80 510** реда, `coordinate_order = "[lat,lng]"`, 5 073 137 B, sha256 **`2a4766bd474f34817081e2d4e49b0ab2abbe54080c809b0402e079e1b9a0904a`** (М, върху **блоба** на HEAD).

| клас (затворен набор от 3, плюс двата отчетни) | брой | котва |
|---|---|---|
| **`in_one_cell`** — в точно една клетка „да“ (канонизирани) | **77 210** | (М) |
| **`tie_break`** — на общия ръб на две клетки „да“ | **1** — една точка в район Приморски **(координата в частния файл)**, между **5055 `chaika_kk`** и **5053 `alen_mak`** | (М) |
| **М1 · `outside_all_95`** — извън всичките 95 полигона | **2 274** | (М) |
| **М2 · `excluded_cell`** — вътре в клетка, **която v2 изключва: десетте реда с `kind_registry = null` (петте „обекта“ И петте села)** | **1 025** = `pristanishte_varna` 355 · `biznes_hotel` 354 · `grand_mol` 274 · `biznes_park_varna` 26 · `letishte` 16 · петте села **0** | (М) |
| **М3 · `deferred_cell`** — вътре в **отложена клетка С ВИД** (шестте: `pz_topoli`, `vz_zvezditsa`, `krushkite`, `lazur`, `orehcheto`, `pripek`) | **0** | (М) |
| **сбор** | 77 210 + 1 + **3 299** = **80 510** | (М) |

> **Дефиницията, поправена след кръг 3:** `excluded_cell` покрива **десет** клетки, не пет — точно клетките, чиито редове отиват в `_meta.excluded` по §3.Г.1; `deferred_cell` покрива **шест** — точно клетките в `rows_without_feature.deferred`. Числово нищо не се мени (селата и отложените хващат 0 точки), но **дефиницията в §1.5 и дефиницията в §3.Г.1 вече са една и съща**, иначе ИА-11 не може да бъде написан еднозначно. Полето `mask.in_cell` от отрицателната половина на стар ИА-11 **не съществува** и е махнато; закотвените имена са `in_one_cell`, `tie_break`, `outside_all_95`, `excluded_cell`, `deferred_cell`, `address_rows_sha256`, `outside_note`, `tie_break_rule`.

- **Покритие на доставката: 77 211 / 80 510 = 95,90 %.** Ако петте „обекта“ влязат: 78 236 = **97,18 %** — това и е числото „97,2 %“ в ADR 011 (Ч `011_kartata_imot.md:47`). Двете се поправят в комит К8.
- **Дифът v1 → v2 по адресна точка — ПОПРАВЕН и възпроизводим.** Кръг 3 обори двойката „49 926 / 17 453“: тя не следва от никое обявено правило, защото **4 517 от 80 510-те точки попадат в ≥ 2 полигона на v1** (М), а правило за развръзка на страната v1 нямаше. **Обявено правило (Р20): за v1 печели азбучно най-малкият код; за v2 — най-малкият `raion_num` (Р6).** При него (М): същата дума **49 397** · сменена **17 982** · изгубена **935** · спечелена **9 832** · без дума и преди, и сега **2 364**. Сборът е 80 510; 49 397 + 17 982 + 935 = **68 314** (v1) ✔; 49 397 + 17 982 + 9 832 = **77 211** (v2) ✔. Правилото се записва дословно в `_meta.diff_v1_v2.tie_break_v1` и се преизмерва от ИА-13.
- Речникът на ADR 011 за М1 („порт, промзона, село, грешна координата“, Ч `011:47`) се записва в `_meta.mask.outside_note` **дословно**; той е бележка, не клас, и никой гейт не го съди.

### 1.6 · Тялото с решенията (черновата днес, **след комит 7556227**)

`Fire_Varna/scratch/places_search/imot_decisions_1_2026-09-08_draft.json` — **проследен и чист**. Стабилна ревизия: `git log -1 --format=%H -- <път>` → **`755622726bac3e8b977f9fd484b2e2d164661267`** (`Claude Architect`). **Блоб `sha256 = 8626ad43aea7a02d132f1e16ccc3b755ab782a87773d55f83eab51fc348fcaf8`, 51 275 B** (М).

- Върхови ключове: `_meta`, `rows`, `virtual_parents`. **`_meta` — 9 ключа** (М): `what, snapshot, dictionary_n, polygons, rule, signed_by, privacy, kind_registry_rule, decisions_open`.
- **98 реда, 16 ключа** (М): `area_km2, buildings, cls, code, code_src, district_agkk, imot_name, include, kind, kind_note, kind_registry, n_adverts, n_pts, parent, raion_num, slug`. **Няма ключ `display`.**
- `include` (М): **79 „да“ · 11 „отложено (0 сгради)“ · 5 „решение“ · 3 „решение (няма полигон…)“**.
- **`_meta.kind_registry_rule` — дословно** (Ч): „imot вид → вид от затворената таблица `KIND_NORM` (`varna_3d/src/fire_varna_locations.py:150-154`): `кв.→кв` · `ж.к./подрайон→жк` · `район→кв` (**ДА СЕ ПОДПИШЕ**; алтернатива `мр`) · `м-т→м-т` (клас locality) · `к.к.→кк` · `в.з.→вз` · промишлена зона→`пз` · Метро/Завод Дружба→`зона` · с./обект → без вид (не влизат в v2)“. **Котвата `:150-154` е ГРЕШНА** (М: `git grep -n KIND_NORM` → `src/fire_varna_locations.py:152`; таблицата е `:152-155`) — поправя се в самото тяло с разлика **Х9**, не само в плана.
- **`_meta.decisions_open` — 7 отворени решения** (Ч, дословно): „район→кв или мр“ · „5 обекта: точка/alias, не клетка“ · „3 района без полигон: чакане/ръчно/no_boundary“ · „11 отложени (0 сгради)“ · „**13** без район по АГКК → район по решение“ · „precision_m за плочката“ · „низът за атрибуция“. **Числото 13 е ГРЕШНО** (М: редовете без `district_agkk` са **16** = 98 − 82) — поправя се в тялото с разлика **Х10**. **Всичките седем са покрити от §9** (Р15/Р16 · Р3 · Р4 · Р7 · Р14 · Р8 · Р10).
- **`kind_registry` по 98-те реда** (М): `кв 34 · м-т 31 · жк 10 · пз 5 · кк 4 · зона 2 · вз 2 · **null 10**`.
- **`kind_registry` по 79-те „да“** (М): `кв 32 · м-т 27 · жк 10 · кк 4 · пз 3 · зона 2 · вз 1` = 79. **Нула стойности извън `KIND_NORM`.** (Суровият imot-вид по същите 79 е `м-т 27 · район 19 · кв. 13 · ж.к./подрайон 10 · зона 5 · к.к. 4 · в.з. 1` — 46 от тях са извън `KIND_NORM`; **точно това преобразуване е решено в самия файл, не се измисля от Изпълнителя**.)
- **Десетте реда с `kind_registry = null`** (М, поименно, с довода от `kind_note`): пет **обекта** — 5841 `biznes_park_varna`, 6183 `biznes_hotel`, 5847 `grand_mol`, 6134 `letishte`, 5864 `pristanishte_varna` („обект: не е клетка → без вид“); пет **села** — 740 `zvezditsa`, 751 `kazashko`, 755 `kamenar`, 764 `konstantinovo`, 821 `topoli` („село: няма вид в `KIND_NORM` → отложено“). **Null вид ⇔ ред в `_meta.excluded` с `delivered: false`: не влиза в v2 и се изброява поименно с довода си.**
- **Деветте НЕдоставяни реда С ВИД** (М): шест отложени — 6293 `pz_topoli`(пз), 6296 `vz_zvezditsa`(вз), 6299 `krushkite`, 6300 `lazur`, 6301 `orehcheto`, 6302 `pripek` (м-т); три без полигон — 5848 (кв), 6294 `malka_chaika` (кв), 5866 (пз). 79 + 10 + 9 = **98** ✔
- **`virtual_parents` е ОТДЕЛЕН списък от 5**, всеки `{code, name, kind, children}`; **нито един от петте не е ред в `rows`** (М). Децата са **17**, всичките `include = "да"` (М): `kv_levski` 4 (`bazar_levski, levski1, levski2, tsveten_kvartal`) · `vladislavovo` 5 (`vladislav_varnenchik1, vladislav_varnenchik2, kaisieva, pz_planova, bokluk_tarla`) · `vazrazhdane` 4 · `mladost` 2 · `pobeda_group` 2 (`konfuto, pobeda`).
- **Петте `virtual_parents` НЯМАТ `kind_registry`**; полето им `kind` е прозата „виртуален родител = обединение на децата“ (М). Дупката се запълва **без измисляне**: четирите вече съществуват в **подписания регистър** — `kv_levski → кв`, `vladislavovo → кв`, `vazrazhdane → жк`, `mladost → жк` (М: и регистърът, и v1 дават същото); само `pobeda_group` няма ред никъде и е **решение Р16** (предложение `кв` — двете му деца са `кв`).
- **97 различни кода за 98 реда** — `"TBD"` два пъти: 5848 „Електроразпределение Варна“ и 5866 „Северна промишлена зона“ (М). **След Х4: 98 различни в `rows`; с петте виртуални родителя — 103 различни в цялото тяло; доставяни — 84.**
- **Приватност (М, върху БЛОБА `8626ad43…`, по имена на ключове):** `advert_id, raw_sha256, raw_response_sha256, points, raion_points, localid, cadnum, center, coordinates, geometry, centroid, polygon, bbox` → **по 0 попадения**; float-ове в кутията на Варна → **0**. Подниз `advert` → **98**, всичките от `n_adverts` — затова сканът е **закотвен по име на ключ**.
- **Остава производно на частната геометрия:** `n_pts` (98 реда, сбор **3 820**) и `area_km2` (**95** реда) — вж. ИА-О9 и ИБ-15.

### 1.7 · Кодовете, регистърът и районът (върху ДОСТАВЯНИТЕ 84)

**v2 = 79 клетки „да“ + 5 виртуални родителя = 84 кода** (обосновката е в §3.Г.1).

| мярка (М) | стойност |
|---|---|
| v1 ∩ v2 | **51** |
| **v1, които изчезват** | **9** — `abatko, druzhba, gorchivata_cheshma, kokardzha_generic, morska_gradina, rozova_dolina, sredna_traka, sv_ivan_rilski, trakia` |
| нови в v2 | **33** (51 + 33 = 84; 51 + 9 = 60 — двете сметки затварят) |
| виртуални родители, които вече са в v1 | **4** — `kv_levski, mladost, vazrazhdane, vladislavovo` (`pobeda_group` е нов) |
| регистър | **84 записа**, `schema_version 1.1`; записите носят **15 различни ключа** (М): `aliases, aliases_note, aliases_pending_p3, children_note, display, id, kind, label_at, map_drop, map_label, osm_confirmed, osm_refused, parents, type_conflict_p3, why`; **6 записа носят `parents`** |
| **v2 − регистър** | **28** — `atanas_tarla, avtogara, bazar_levski, chataldzha, festivalen_kompleks, franga_dere, generalite, hei, kantara, konfuto, levski1, levski2, lyatno_kino_trakiya, operata, ostrovna_pz, pobeda_group, pogrebite, slanchev_den, sportna_zala, stadion_spartak, tsentralna_poshta, tsveten_kvartal, vins_cherven_ploshtad, vladislav_varnenchik1, vladislav_varnenchik2, zavod_druzhba, zhp_gara, zimno_kino_trakiya` |
| **регистър − v2** | **28** — `abatko, akchelar_vinitsa_seam, borovets, botanicheska, byalata_cheshma, deli_sava, druzhba, franga_kokardzha_seam, gabena, golyama_kokardzha, gorchivata_cheshma, kokardzha_generic, malka_chaika, malka_kokardzha, mikro4, mikro8, morska_gradina, rozova_dolina, shashkana, sredna_traka, starite_lozya, sv_ivan_rilski, trakata_so, trakata_vz, trakia, vayalar, vilite, yuzhna_pz` |
| от тях **жилищни** по `RESIDENTIAL_KINDS = {"кв","жк","кк"}` (Ч `src/build_quarters_candidate.py:56`) | **4** — `druzhba` (жк), `rozova_dolina` (кв), `sv_ivan_rilski` (кв), `trakia` (кв) |
| **клетки „да“ без район от НАШИЯ слой** | **0** (М — всичките 79 получават точно един район по представителна точка) |
| **редове с непразен `district_agkk`** | **82 от 98** (М) |
| **знаменателят на свидетеля — обявен точно** | **82** = редовете, които имат **И** район от нашия слой, **И** район по АГКК (М: върху 95-те полигонни реда; 12 нямат наш район, 13 нямат АГКК) |
| съгласие наш слой ↔ свидетел АГКК | **77 от 82** |
| разминавания | **5** — `vazrazhdane4`, `kochmar`, `so_planova` (5857), `salzitsa` (5860) — и четирите `include = "да"`, наш слой `vladislav_varnenchik`, АГКК `mladost` — плюс `pristanishte_varna` (наш `odesos`, АГКК `asparuhovo`; **изключен ред, НЕ Feature**). 77 + 5 = 82 ✔ |
| съгласие само по **доставяните** клетки | **74 от 78** (79 „да“ минус `perchemliyata`, който няма АГКК) |
| вече подписани спорове | **2** — `district_resolutions_2026-09-07.json`: `kochmar → mladost`, `vazrazhdane4 → mladost` (М) |
| **нови спорове** | **2** — `so_planova` и `salzitsa` |
| редове без `district_agkk` | **16** (М, поименно): `letishte`, `perchemliyata`, шестте отложени с вид, петте села, трите без полигон. От тях единственият „да“ е **`perchemliyata`** — поименната подписана резерва вече съществува (Ч `qa_place_zone_aliases.py:74` `SIGNED_DISTRICT_RESERVE = {"perchemliyata": "primorski"}`) |
| **район на петте виртуални родителя** | по представителна точка в нашия слой: `kv_levski → primorski`, `vladislavovo → vladislav_varnenchik`, `vazrazhdane → mladost`, `mladost → mladost`, `pobeda_group → mladost` (М) |

**Подписаният вход за споровете, пиннат по БЛОБ:** `Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json` — проследен; **ревизия `e6c706dffa8eb20897e66a16510297a54465ae50`** (`Claude Executor`, 2026-09-07), **блоб `sha256 = d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc`, 513 B** (М). Закотвен в `varna_3d/src/qa_quarters_signed.py:124-125` (`RESOLUTIONS_PATH`) и `:126` (`RESOLUTIONS_SIGNED_SHA256`).

**Шестият решаващ вход — слоят с петте района, който НЕ живее в git.** `district` на всичките 84 Feature-а идва от `C:/git/m6000_private/number_viewer/quarters_layer.geojson` (Ч `varna_3d/src/fire_varna_locations.py:135` `QUARTERS_LAYER`; Ч `src/build_quarters_signed.py:84` `DEFAULT_DISTRICTS`; филтърът е `authority == "osm"` и `display ∈ DISTRICTS`, Ч `:396-398`, а `DISTRICTS` е затворената петорка на `fire_varna_locations.py:141-147`). **М: `git -C C:/git/m6000_private log` → `fatal: not a git repository` — папката НЕ е репо, файлът няма блоб и не може да се адресира по червен ред 13.** Мярка на файла: **201 130 B, sha256 `26e39b001ce151203058d70bc53367a5b40c77c4b0dd7113cf2a7085c376cc22`**; в него `authority == "osm"` има 48 Feature-а, от които **точно 5** са с `display` от петорката (М). Затова: **пинва се по sha256 на прочетените байтове** (Р21, ИА-О23), влиза в `_meta.inputs` като шести вход и ражда дълг ИБ-17.

**Закритата таблица на видовете** (Ч `src/fire_varna_locations.py:152-155` `KIND_NORM`, 14 ключа; коментарният ѝ надслов е `:149-151`; проверката за вид извън нея е `:646`, `die()` — `:647-648`): `жк, кв, кк, со, с.о., вз, в.з., м-т, местност, махала, зона, пз, парк, мр`.

**Класът на вида** (Ч `src/fire_varna_locations.py:156-160` `KIND_CLASS`): `{жк, кв, кк, со, вз} → quarter`; `{местност, зона, пз, парк, мр} → locality`; `махала → DROP`. **Разпределението на 84-те доставяни (М):** видове `кв 35 · м-т 27 · жк 12 · кк 4 · пз 3 · зона 2 · вз 1` = 84; класове **52 quarter** и **32 locality**. **По D6 locality НИКОГА не пълни `quarter`** — измерена последица за публикуването, работа на **И-Б** (ИБ-11), не на И-А: И-А не публикува нищо.

### 1.8 · Пиновете, които сочат v1 — изчерпателно, мерено с `git grep`

(М) `git grep -l "quarters_signed.geojson" -- .` → **13 проследени файла**; `git grep -c` → **41 реда общо** (1+2+1+1+3+3+6+2+1+2+2+2+15). Долу е таблицата по ПИН — **18 реда**.

| # | пин | котва | какво пинва |
|---|---|---|---|
| П1 | `QUARTERS_SIGNED = ROOT/"data"/"quarters_signed.geojson"` | Ч `src/fire_varna_locations.py:93` | пътят |
| П2 | `QUARTERS_SIGNED_SHA256 = "c1551d24…"`, `die()` на `:974-976` | Ч `src/fire_varna_locations.py:94` | блобът |
| П3 | `RECORDED_INPUTS` — последният елемент е `"data/quarters_signed.geojson"` | Ч `src/fire_varna_locations.py:116` | **генераторът на картата `inputs`** — `:1960-1961` пише `{p: sha256_of(ROOT/p) for p in RECORDED_INPUTS if (ROOT/p).exists()}`, а `:2079` презаписва файла |
| П4 | провенансни низове `"path": "data/quarters_signed.geojson"` | Ч `src/fire_varna_locations.py:1689`, `:1968` | пътят |
| **П5** | **докстринг** „`data/quarters_signed.geojson` — подписаните граници като съдия“ | **Ч `src/fire_varna_locations.py:467`** | текст, който след И-А ще лъже, ако не се пипне |
| **П6** | **`die(f"пинът на quarters_signed.geojson в {INPUTS.name} е {pinned}…")`** | **Ч `src/fire_varna_locations.py:975`** | съобщение на гейт, което назовава файл, различен от прочетения |
| П7 | `by_source = {wikimapia, wikimapia_union, declared_streets}` + `die(...)` | Ч `src/fire_varna_locations.py:601-618` | **`imot_bg_tiling` няма ред → `die`** |
| П8 | `SIGNED_SHA`, `EXPECT_ROWS 375`, `EXPECT_WRITTEN 201`, `EXPECT_EMPTY`, `EXPECT_FEATURES 60`, `EDGE_FLOOR_M 50`; `--signed` по подразбиране | Ч `src/qa_p8a.py:60-66`, `:296`; сверката е `sha256_of(signed_path)` на `:318-321` | v1 |
| П9 | `SIGNED`, `EXPECT_SIGNED_CODES = 60`, докстрингът „one of the 60 SIGNED codes“ | Ч `src/qa_place_zone_aliases.py:66`, `:75`, `:26` | v1 |
| П10 | `QUARTERS_SIGNED`, `LOCATION_INPUTS`; `ATTR_SRC = {"wikimapia","openstreetmap"}` и трите ѝ спътници | Ч `src/qa_fire_varna_places_export.py:84`, `:85`, `:76`, `:79`, `:81`, `:82` | v1 |
| **П11** | **`check(False, "data/quarters_signed.geojson съществува", "липсва")`** | **Ч `src/qa_fire_varna_places_export.py:547`** | текст на изхода, който след Т11 ще назовава друг файл |
| П12 | `ARTIFACT`, `features == 60`, `human_polygon == 58`, докстрингът `:12` | Ч `tests/test_quarters_signed_fixtures.py:37`, `:172`, `:175`, `:12` | v1 |
| **П13** | **`SIGNED = ROOT/"data"/"quarters_signed.geojson"`, четен на `:67`** | **Ч `scratch/granitsi/zone_alias_negatives.py:28`** — **проследен харнес за отрицателните проби на `qa_place_zone_aliases`** | v1 |
| **П14** | `"data/quarters_signed.geojson": {sha256, bytes}` **вътре в картата `inputs`** — **ВТОРО място, различно от `quarters_signed.path`** | **Ч `data/fire_varna_location_inputs.json:66`** (сверявано на Ч `fire_varna_locations.py:974-976`) | блобът + пътят |
| П15 | `"path": "data/quarters_signed.geojson"` в `quarters_signed` блока | Ч `data/fire_varna_location_inputs.json:87` | пътят |
| **П16** | **червени черти по БАЗОВО ИМЕ:** `fail("червена черта", "този лот НЕ произвежда quarters_signed.geojson")` и „този гейт не съди файл с име `quarters_signed.geojson`“ | **Ч `src/build_quarters_candidate.py:664-665`** и **`src/qa_quarters_candidate.py:432-433`** | **безвредни за И-А** — v2 запазва името в `data/`, архивът има друго име. **Нула байта в тях** |
| П17 | `"path": "data/quarters_signed.geojson"` в `_meta.inputs` на леджера p8a | Ч `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:19` | **исторически запис**; `qa_p8a` НЕ го чете (М: сверява се само `--signed` по `SIGNED_SHA`) |
| П18 | `!data/quarters_signed.geojson` | Ч `.gitignore:34`, с описателен блок `:24-33`, който описва **v1** | пътят + документацията над него |

**Клоновете на стария билдър/гейт, които плочката би ударила** (защо не се адаптира — §2 ИА-О7): `build_quarters_signed.py:1542` `--raw-snapshot required=True` · `:1086-1096` `sources` по `wm_id` · `:1128-1149` три пътя за Feature, четвърти няма · `:1118-1119` `declared_streets != 1 → fail` · **`:1106-1107` A14 иска `row["display"]` и **регистров** `row["kind"]` — черновата няма `display` и носи imot-вид под името `kind`, значи A14 би паднал 98 пъти** · `:1563` червената черта, а `"lot": "Б1"` е на **`:1408`** · `:115-120` `PLAN` пинва плана на Б1.
**Гейтът:** `qa_quarters_signed.py:83` `LICENCE_BY_SOURCE = {wikimapia, declared_streets, wikimapia_union}` · `:359-368` блокът C9, в който **`:360` е буквално `for source in ("wikimapia","openstreetmap")`**, `:362` са шестте ключа на `source_terms`, `:367` иска `len(_meta.licences) >= 2` · `:170-171` C1 пинва `plan.file` и `decisions_sha256` към литерали · `:325-340` C8 няма врата за код извън регистъра и **`:338-340` е ТВЪРДО червено за жилищен код без ред в решенията** · `:1198-1199` **задължителен позиционен път** + `--registry required` · `:1214-1216` `if not path.exists(): return 1` · **`:1230-1231` чете `decisions_doc["decisions"]` и слива редове по код** (всичко Ч).
**Две поправени твърдения:** (1) `qa_quarters_signed.py:920` `make_fixtures(...)` **НЕ мутира документа** — `clone()` на `:929-930` е дълбоко копие (М). (2) **Старият гейт СТРУКТУРНО не може да прочете Ф7**: `:1230` иска ключ `decisions`, а тялото носи редовете под `rows` (М) — затова доводът „двата `TBD` биха се слели мълчаливо в стария гейт“ е **невалиден** и обосновката на Х4 е пренаписана към новия гейт.

### 1.9 · Механиката на `.gitignore` във `varna_3d` (М)

- `:4` = `data/*`; `:10-11` = обяснението защо изключение вътре в игнорирана ПАПКА не работи; `:12` = `!data/known_doors.json`; `:17` = `!data/street_aliases.json`; `:23` = `*.geojson`; `:24-33` = коментарният блок „ТРЕТОТО ИЗКЛЮЧЕНИЕ“, който описва **v1**; `:34` = `!data/quarters_signed.geojson`. Общо **238 реда**.
- **Проверено:** `git check-ignore -v data/archive/x.json` → `.gitignore:4:data/*` — **папка под `data/` не може да се върне.** `docs/archive/x.md` → нищо. `docs/archive/x.geojson` → `.gitignore:23:*.geojson` — иска поименно изключение след ред 23.
- **`tests/fixtures/**/*.geojson` е ИГНОРИРАН** (М: `git check-ignore -v tests/fixtures/qa_quarters_signed_imot/x.geojson` → `.gitignore:23:*.geojson`, изход 0). **Мярка, която затваря въпроса:** `git ls-files tests/fixtures` → **само 2 файла** (`identity_rekey_base_2026-09-07.json`, `readonly_ast_negative.py`); цялата съществуваща папка `tests/fixtures/qa_quarters_signed/` (20+ `.geojson`) **не е проследена**, а репото го казва дословно: `tests/test_quarters_signed_fixtures.py:21-22` — „The fixtures are regenerated here from the tracked code, never committed (`.gitignore:23` — `*.geojson`), so the write-set of the lot stays exhaustive.“ **Следствие: фикстурите на И-А НЕ са път от write-set-а и не се комитват** (ИА-О20).
- `docs/archive/` **вече съществува и е проследен** (М: `git ls-files docs` → `docs/archive/ПЛАН_блокове_поправка_v2_2026-08-20.md`); `docs/decisions/` също (М).

---

## 2 · Обявени отклонения

| № | Отклонение | Защо |
|---|---|---|
| **ИА-О1** | **Планът v4 СЪЩЕСТВУВА** (156 024 B, 735 реда, непроследен) и е суровината на този под-лот. | STOP по „измерено число се разминава“ важи първо за §2. |
| **ИА-О2** | **v2 носи 84 Feature-а — 79 клетки + 5 виртуални родителя.** | Мерено: обединенията на 17-те деца дават **5 единични `Polygon` без вътрешни пръстени, всичките валидни**. Друго решение би оставило 17 деца със `parent`, сочещ код без геометричен носител, и четирите оцелели родителски кода щяха да изчезнат от артефакта (изчезващите щяха да станат 13, не 9). |
| **ИА-О3** | **Тялото с решенията се МЕСТИ в `varna_3d`** (`data/quarters_decisions_imot_2026-09-08.json`). Черновата във Fire_Varna **остава на място непокътната**. Решение Р1. | ADR 011 И-D3 (Ч `011:17`) днес назовава път във Fire_Varna — **това решение се обръща с ред в комит К8, не мълчаливо** (инвариант 7). |
| **ИА-О4** | **Замразеният вход СЕ КОПИРА в `varna_3d/data/`** и става проследен там (Р13). | Иначе каноничният артефакт стъпва на файл, който **никое репо не носи**. `varna_3d` е частно, а червен ред 5 изрично разрешава суровия провенанс там. |
| **ИА-О5** | **v1 се архивира в `docs/archive/`, не в `data/archive/`.** | `data/*` е ПАПКОВО изключване; връщане назад е механично невъзможно (§1.9). |
| **ИА-О6** | **Осемнайсетте пина към v1 се пренасочват към архивния път** вместо да бъдат пребазирани към v2. Пиновете по sha (`c1551d24…`, 60, 301 917 B) **не се пипат**; П16 и П17 остават с нула байта. | Така целият стълб на `varna_3d` остава ЗЕЛЕН, а v2 се съди само от собствения си гейт. |
| **ИА-О7** | **`build_quarters_signed.py` и `qa_quarters_signed.py` не се пипат нито с един байт.** Пише се НОВ билдър и НОВ гейт. | §1.8, последният блок: това не е смяна на константи, а друг конвейер — старият гейт дори не може да ПРОЧЕТЕ новото тяло (`:1230` иска ключ `decisions`). |
| **ИА-О8** | **`--diff` СЕ ДОБАВЯ — но в НОВИЯ гейт.** ADR 010 D9 (Ч `010:54`) и G15 (Ч `010:129`) са регистрирани и **важат**: v2 е точно случаят над праговете (**17 982** сменени места при праг > 2; обединената площ 61,597 → 74,615 km² = **+21,1 %** при праг > 10 %). Затова **ИА-13 има две половини**: без `--diff-signed` → **изход 2**, с `--diff-signed "Р18"` → 0 плюс двоен запис и пълно преизмерване. | Нищо не се отменя: G15 се **изпълнява** в новия конвейер, а ADR 010 не се пипа. |
| **ИА-О9** | **`n_pts` (сбор 3 820) и `area_km2` (95 реда) остават в проследената чернова на Fire_Varna за целия интервал И-А → И-Б.** | Днес: `advert_id`, `raw_sha256`, координати → **0 попадения** (М). Изчистването/архивирането на черновата е И-Б (ИБ-15); тук се записва като **датиран дълг**, не се премълчава. |
| **ИА-О10** | **`_meta` на v2 е ЗАТВОРЕН набор от 41 имена** = 36-те на v1 **∪** двете, които ADR 011 И-D2 изисква и които v1 няма (`dictionary_sha256`, `snapshot_date`) **∪** трите обявени нови (`diff_v1_v2`, `mask`, `registry_pending_new`). `decisions_sha256` и `source_terms` **вече са сред 36-те** (М, поименно) и не се броят два пъти. Пълният списък е в §3.Г.8. ИА-6 съди срещу **тези 41**. | Срещу 36 гейтът е червен по конструкция (ИА-13 иска `diff_v1_v2`); срещу 39 два ADR-задължителни ключа стават червени. |
| **ИА-О11** | **`_meta.lot = "И-А"`, `_meta.plan.file = "Fire_Varna/docs/plans/ПЛАН_Картата_imot_И-А_08.09.md"`.** | ИА-6 сверява ИМЕНАТА на ключовете; съдържанието е на новия лот. |
| **ИА-О12** | **ИА-11 чете `Fire_Varna/data/address_rows.json` по sha на ПРОЧЕТЕНИЯ файл, не по литерал.** | HEAD-ът на Fire_Varna мърда сам. Човешката котва (80 510 / 77 210 / 1 / 3 299) стои в §1.5 и в отчета за Gate 2. |
| **ИА-О13** | **Изход 3 на Н8 се приема като база**, а не се „поправя“. | Ч `qa_fire_varna_m6.py:526`. |
| **ИА-О14** | **`scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:19` НЕ се пипа.** | Подписано тяло от 07.09 и **исторически запис**; `qa_p8a` не го чете (М). Червен ред 8 забранява редакция на място. |
| **ИА-О15** | **`vinitsa_sever`: подписаното изключване на v1 се ОБРЪЩА.** v2 го доставя. Обратът стои като **ред в `_meta.excluded` със `status: "reinstated"` и `delivered: true`**, носещ дословно стария довод, номера на решението (Р17) и датата — **и в `declared_deviations[]`**. | Изпразването на `excluded[]` изтрива записа на подписано решение; червен ред 8 и §10 т. 5 забраняват точно това. |
| **ИА-О16** | **`d1_schema.nulled_on_import` расте от 7 на 10** — при извор без уикимапийски обект нулирани са и `wm_id`, `wm_ids`, `wm_title`. v1 не се пипа; v2 носи собствения си, честен списък. | „Копирай `d1_schema` дословно от v1“ прави ключа описание, което не описва артефакта. |
| **ИА-О17** | **Твърдото правило на C8 („жилищен код без ред в решенията = червено“, Ч `qa_quarters_signed.py:338-340`) в НОВИЯ гейт става „изброени поименно с довод“** за четирите (`druzhba, rozova_dolina, sv_ivan_rilski, trakia`). | Намаляване на строгостта върху подписан регистър е ОТКЛОНЕНИЕ и мястото му е тук. Старият C8 остава непокътнат и продължава да съди v1 (ИА-12). |
| **ИА-О18** | **ВСИЧКИ ефемерни пътища на лота живеят ИЗВЪН двете репа, под `%TEMP%`, и не са пътища от write-set-а.** Изчерпателно: `…/ia_build_a` и `…/ia_build_b` (двата билда за ИА-10) · `…/ia_broken/*` (счупените копия на входове и на артефакта — механики 1 и 4) · `…/ia_fixtures` (отрицателните фикстури) · `…/ia_builder_nd.py` (нарочно недетерминираният вариант на билдъра, половината на ИА-10) · `…/ia_docs/*` (счупените копия за ИА-19) · `…/ia_neg_fv` и `…/ia_neg_v3` (двете временни git-дървета). М: `%TEMP%` = `C:\Users\Petar\AppData\Local\Temp`. Всичко се маха на стъпка 18 и се сверява с `git worktree list` в **двете** репа + `git status --short`. | Кръг 3: ИА-STOP 1 и 13 спираха Изпълнителя върху собствената му машинария, защото ИА-О18 покриваше само дървото. Сега покрива **всяка** ефемерна пътека. |
| **ИА-О19** | **`docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` пристига МРЪСЕН** (дневникът на §20 от днес, писан от Архитекта). **К9 носи и този хънк, и новия §21**, и Изпълнителят го показва дословно на стъпка 0. | Иначе `git status --short` след К9 „изчиства“ чужд ред, който никой не е обявил. |
| **ИА-О20** | **Отрицателните фикстури НЕ са път от write-set-а и НЕ се комитват.** „Ф4“ отпада като файл; номерацията Ф1…Ф10 остава непроменена, за да не се разчита таблицата наново. Фикстурите се раждат в `%TEMP%/ia_fixtures` от Ф2 и се съдят от Ф3. | М: `.geojson` под `tests/fixtures/` е игниран (`.gitignore:23`), нито един съществуващ фикстурен `.geojson` не е проследен, и `tests/test_quarters_signed_fixtures.py:21-22` казва точно това. Комит на `.geojson` фикстури би искал ПЕТИ ред в `.gitignore` — файл, който Т1 обявява за пипнат ВЕДНЪЖ и вече е в К2 — и би бил геометрия с ръката на Изпълнителя срещу D16. |
| **ИА-О21** | **`_meta.rows_without_feature` на v2 носи ДРУГ набор кофи от v1** — v1 има `alias_of` + `deferred` (М, дословно), v2 има `deferred` + `no_boundary`. | Един и същ ключ с различна структура е скрита схемна смяна; влиза поименно в `declared_deviations[]` и в §3.Г.1. |
| **ИА-О22** | **Ф2 приема позиционния път като НЕЗАДЪЛЖИТЕЛЕН (`nargs="?"`)** и в режим `--decisions-diff` (ИА-16) работи без артефакт. Освен това самият **Д1 се записва на диска след подписа и преди К1**. | Образецът `qa_quarters_signed.py:1198` прави пътя задължителен; при пренасяне ИА-16 щеше да пада с argparse-грешка (изход 2), която ИА-STOP 3 чете като червено. А файлът Д1 на диска днес е **редакция 2 с три координатни двойки** — да го комитнеш „дословно“ означава да внесеш координати в проследен файл на публичното репо (М, §1.1). |
| **ИА-О23** | **Слоят с петте района се пинва по sha256 на прочетените байтове (`26e39b00…`, 201 130 B), не по блоб.** | М: `C:/git/m6000_private` не е git репо. Решаващ вход извън `_meta.inputs` противоречи на D10 — затова той Е шестият вход, а невъзможността да се версионира е записана като дълг ИБ-17, не като мълчание. Решение Р21. |
| **ИА-О24** | **Обобщените производни (площи, брой върхове/отсечки, хистограма на ръба, Hausdorff, хешове на частни файлове) СТОЯТ в трите проследени документа на Fire_Varna.** Обхватът на ИА-7 (данни) и на ИА-19 (проза) е обявен така: **ИА-7 гледа само файлове с данни, ИА-19 гледа само координати в проза.** | Червен ред 5 забранява геометрия, суров провенанс и **координати**; агрегатът не е нито едно от трите. Че дупката „производни в проза“ е реална, а не теоретична, е измерено (ИБ-4/ИБ-18) — но затварянето ѝ иска правило И гейт, а те са И-Б. Тук се обявява, не се премълчава. |

---

## 3 · Write-set с котви (изчерпателен — път извън тази таблица = ИА-STOP 1)

### 3.А · `varna_3d` — нови файлове

| # | път | какво | комит |
|---|---|---|---|
| **Ф1** | `src/build_quarters_signed_imot.py` | **НОВ билдър** — правилата в §3.Г | **К4** |
| **Ф2** | `src/qa_quarters_signed_imot.py` | **НОВИЯТ ГЕЙТ** — реализира **ИА-1 … ИА-11, ИА-13 … ИА-17**, всяка проверка написана ТУК наново, нищо внесено от `qa_quarters_signed.py`. **CLI-договорът е обявен изчерпателно долу.** | **К4** |
| **Ф3** | `tests/test_quarters_signed_imot_fixtures.py` | **реализира ИА-18**: ражда фикстурите в `%TEMP%/ia_fixtures`, прогонва всяка с нейния `--only`, настоява за изход ≠ 0 **по своя номер**; проверява, че гейтът е зелен върху истинския v2 и че двата билда са байт-еднакви | **К4** |
| ~~Ф4~~ | — | **ОТПАДА** (ИА-О20): фикстурите са `.geojson`, игнорирани от `.gitignore:23`, и по установената практика на репото **никога не се комитват**. Номерът се оставя празен, за да не мърда останалата номерация. | — |
| **Ф5** | `data/imot_bg_varna_polygons_08.09.geojson` | **байтово копие** на снапшота (175 736 B, `77b40564…`) | **К2 · Петър** |
| **Ф6** | `data/imot_bg_varna_dictionary_08.09.json` | **байтово копие** на речника (6 274 B, `feba76e3…`) | **К2 · Петър** |
| **Ф7** | `data/quarters_decisions_imot_2026-09-08.json` | **каноничното подписано тяло** (Р1) — блобът `8626ad43…` плюс изброените в §3.В **десет** разлики и нищо друго | **К3 · Петър** |
| **Ф8** | `docs/archive/quarters_signed_v1_2026-09-06.geojson` | v1, **`git mv`**, байт за байт (301 917 B, `c1551d24…`) | **К6 · Петър** |
| **Ф9** | `docs/archive/РЕГИСТЪР_архив.md` | регистърът на архива: `стар път → нов път → комит → защо → кой го чете сега`; първи ред v1, втори ред „черновата с решенията — архивиране в И-Б“, трети ред „`granitsi_decisions_2/3/4` — отменени, физически архивирани в И-Б“ | **К5** |
| **Ф10** | `docs/decisions/ПРЕДЛОЖЕНИЕ_регистър_imot_08.09.md` | **само предложение** за `Varna_buildings/config/quarter_registry.json`. Схемата на записа е **измерената**: `id, display, kind, aliases, why` **плюс `parents`** — точно **17** от 28-те нови кода са деца на петте виртуални родителя (М), а йерархията в регистъра се носи от `parents` (М: 6 записа днес го носят). Съдържа: **28**-те нови кода, **28**-те регистрови кода без Feature, отделно четирите жилищни, деветте изчезващи, и **бележка за `malka_chaika`** (регистърът го дава като `м-т`, тялото му дава `kind_registry = "кв"`; редът е `no_boundary`, затова разминаването днес не удря гейт). **Нищо не се прилага.** | **К7** |

**CLI-договорът на Ф2 (обявен, защото три отрицателни половини зависят от него):**
`path` — **позиционен, `nargs="?"`** (ИА-О22) · `--registry` · `--tiling <снапшот>` · `--dictionary <речник>` · `--address-rows <път>` · `--districts <слой>` · `--decisions-repo/--decisions-rev/--decisions-path` (**Ф7 във varna_3d**) · `--resolutions-repo/--resolutions-rev/--resolutions-path` (**`district_resolutions_2026-09-07.json` във Fire_Varna**) · `--draft-repo/--draft-rev/--draft-path` (**черновата във Fire_Varna, само за `--decisions-diff`**) · `--diff <път до v1>` · `--diff-signed <низ>` · `--only <ИА-номер>` · `--make-fixtures --fixtures-dir <път>` · `--decisions-diff` · `--out <път>`.
**Без `--resolutions-*` отрицателната половина на ИА-9 не може да се напише: гейтът би прочел истинския файл и би върнал 0** (кръг 3, БЛОКЕР).

### 3.Б · `varna_3d` — точкови редакции (**архивният път е един и същ навсякъде**: `docs/archive/quarters_signed_v1_2026-09-06.geojson`)

| # | файл:ред | днес (Ч) | става |
|---|---|---|---|
| **Т1** | `.gitignore` — **ЕДНА редакция, един блок**: коментарният блок `:24-33` се пренаписва (той описва v1), и **непосредствено след `:34` се добавят четирите реда** | — | `!data/imot_bg_varna_polygons_08.09.geojson` · `!data/imot_bg_varna_dictionary_08.09.json` · `!data/quarters_decisions_imot_2026-09-08.json` · `!docs/archive/quarters_signed_v1_2026-09-06.geojson`. **Четирите стоят СЛЕД `:23` и СЛЕД `:4`, значи бият и двете правила** (§1.9). **ПЕТИ ред за `tests/fixtures/` НЕ се добавя** (ИА-О20). **Файлът се пипа ВЕДНЪЖ и се комитва ВЕДНЪЖ — в К2, ръката на Петър.** |
| **Т2** | `src/fire_varna_locations.py:93` | `QUARTERS_SIGNED` | архивният път + коментар, който назовава интервала И-А→И-Б |
| **Т3** | `src/fire_varna_locations.py:94` | `QUARTERS_SIGNED_SHA256` | **НЕ СЕ ПИПА** |
| **Т4** | `src/fire_varna_locations.py:116` (`RECORDED_INPUTS`) | `"data/quarters_signed.geojson"` | архивният път — **иначе `:1960-1961` ще пренапише картата `inputs` и ще разсинхронизира П14** |
| **Т5** | `src/fire_varna_locations.py:1689`, `:1968`, **`:467` (докстринг), `:975` (текстът на `die`)** | низът на пътя | архивният път **на четирите места** |
| **Т6** | `src/fire_varna_locations.py:601-618` | `by_source` | **НЕ СЕ ПИПА** → И-Б |
| **Т7** | `src/qa_p8a.py:296` | `--signed` по подразбиране | архивният път |
| **Т8** | `src/qa_p8a.py:60-66` | шестте константи | **НЕ СЕ ПИПАТ** → И-Б |
| **Т9** | `src/qa_place_zone_aliases.py:66` и докстрингът `:26` | `SIGNED` | архивният път (текстът „the 60 SIGNED codes“ получава „(v1, архивиран — И-Б го пребазира)“) |
| **Т10** | `src/qa_place_zone_aliases.py:75` | `EXPECT_SIGNED_CODES = 60` | **НЕ СЕ ПИПА** → И-Б |
| **Т11** | `src/qa_fire_varna_places_export.py:84` **и текстът на `:547`** | `QUARTERS_SIGNED`; `check(False, …)` | архивният път на двете места |
| **Т12** | `src/qa_fire_varna_places_export.py:76`, `:79`, `:81`, `:82` | `ATTR_*` | **НЕ СЕ ПИПАТ** → И-Б |
| **Т13** | `tests/test_quarters_signed_fixtures.py:37` и докстрингът `:12` | `ARTIFACT` | архивният път (`:172` = 60 и `:175` = 58 **остават** — те съдят v1) |
| **Т14** | **`scratch/granitsi/zone_alias_negatives.py:28`** (четен на `:67`) | `SIGNED` | архивният път — **без този ред отрицателните проби на `qa_place_zone_aliases` тихо започват да четат v2 и спират да падат** |
| **Т15** | `data/fire_varna_location_inputs.json` — **ДВЕТЕ места**: ключът `:66` в картата `inputs` и `:87` `quarters_signed.path` | `"data/quarters_signed.geojson"` | архивният път на двете места; **`sha256`, `bytes`, `features`, `commit`, `artifact_class`, `decisions_sha256` НЕ се пипат.** Файлът е под `data/` → **комитва го Петър (К6)** |

**`src/build_quarters_signed.py`, `src/qa_quarters_signed.py`, `src/qa_fire_varna_m6.py`, `src/qa_fire_varna_export.py`, `src/build_quarters_candidate.py`, `src/qa_quarters_candidate.py`, `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` — нула байта.**

**Как се пенсионира старият билдър: не се пенсионира — пенсионира се ВХОДЪТ му.** `build_quarters_signed.py` продължава да строи v1 байт за байт; `qa_quarters_signed.py` продължава да го съди по позиционен път; `tests/test_quarters_signed_fixtures.py` продължава да е зелен, само сочи архивния път. **Това е гейтът за нерегрес ИА-12.** За доставка старият билдър не се вика никога повече.

### 3.В · `Ф7` (подписаното тяло) срещу черновия блоб `8626ad43…` — **точно ДЕСЕТ разлики, нула други**

Гейтът ИА-16 чете черновия блоб (`--draft-repo C:/git/Fire_Varna --draft-path scratch/places_search/imot_decisions_1_2026-09-08_draft.json`; ревизията се намира с `git log -1 --format=%H -- <път>`), сверява sha == `8626ad43aea7a02d132f1e16ccc3b755ab782a87773d55f83eab51fc348fcaf8`, 51 275 B, и настоява дифът да е **точно този списък**:

| # | ключ | днес | става | защо |
|---|---|---|---|---|
| **Х1** | `_meta.signed_by` | `"pending — Петър"` | `"Petar"` | подписът |
| **Х2** | `_meta.rule` | „…`district` = свидетел АГКК AU5 по центроид **(G23)**“ | „`district` = НАШИЯТ слой от пет района по представителна точка (`district_src = fire_varna_district`); АГКК AU5 е **независим свидетел** по амандамента в ADR 011 И-D5 (Р19); замяна само с ред в подписан `district_resolutions`; всяко разминаване се записва поименно“ | `src/qa_district_official.py` **не съществува** (М) — G23 сочи скрипт-фантом; правилото се амандира в ADR, не се пренаписва мълчаливо в JSON (ИА-О25 → §2 ИА-О20-редът за ADR 010 е Р19) |
| **Х3** | `_meta.privacy` | „…в игнорираната папка **(G29)**“ | „…суровият провенанс живее в частното репо `varna_3d` (`data/imot_bg_varna_polygons_08.09.geojson`) и в игнорираната папка `scratch/boundary_gallery/` на Fire_Varna, доказано с `git check-ignore -v`“ | **G29 не е регистриран гейт** — М: `grep -c G29 010_signed_quarter_boundaries.md` → **0**; живее само в `ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:71` (описанието), с препратки на `:62` и `:104`, и в `qa_night_pins.py` |
| **Х4** | `rows[5848].code`, `rows[5866].code` | `"TBD"` × 2 | `"elektrorazpredelenie_varna"`, `"severna_promishlena_zona"` | **`"TBD"` не е код и чупи биекцията ред ↔ код, която ИА-3 съди** (98 реда → 97 различни кода, М). *(Доводът „старият гейт би ги слял мълчаливо на `:1231`“ е ОТТЕГЛЕН: `:1230` чете ключ `decisions`, а тялото носи `rows` — старият гейт не може да го прочете изобщо. Съдникът е ИА-14.)* |
| **Х5** | нов `_meta.counts` | — | **15 полета, всяко сверено от ИА-3**: `{dictionary: 98, polygons: 95, cells: 79, virtual_parents: 5, features: 84, excluded_rows: 10, excluded_entries: 11, deferred: 6, no_boundary: 3, distinct_codes_rows: 98, distinct_codes_body: 103, distinct_codes_delivered: 84, registry_entries: 84, registry_pending: 28, registry_pending_new: 28}`. **98 = 79 + 10 + 6 + 3 ✔** | брояч без сверка не е брояч. **`excluded_rows` брои ДОМА на редовете (10), `excluded_entries` — дължината на списъка (11, с върнатия `vinitsa_sever`)** — кръг 3 показа, че едно име за двете числа прави ИА-3 червен по конструкция. **Двата 28-ици носят имената на `_meta`-ключовете, които броят**, за да не са верни по случайност. |
| **Х6** | **`kind_registry` на петте `virtual_parents`** | липсва (полето `kind` е проза) | `kv_levski → "кв"`, `vladislavovo → "кв"`, `vazrazhdane → "жк"`, `mladost → "жк"` — **преписани от подписания регистър** (М: и регистърът, и v1 дават същото) — и `pobeda_group → "кв"` по **решение Р16** | 79-те клетки вече носят `kind_registry` от комит `7556227`; **петте родителя са единствената дупка и тя се затваря с извор, не с измисляне** |
| **Х7** | **нов `_meta.kind_registry_decisions`** | — | `{"район→кв": "Р15 (алтернатива мр = клас locality, не пълни quarter)", "pobeda_group→кв": "Р16"}` | двете места, където правилото на самата чернова казва „ДА СЕ ПОДПИШЕ“, стават следа в тялото |
| **Х8** | нов `_meta.signature` | — | `{signed_by: "Petar", signed_at, basis: "ПЛАН_Картата_imot_И-А_08.09.md §9", plan_body_sha256}` | по образеца на v1 `_meta.signature` (Ч) |
| **Х9** | **`_meta.kind_registry_rule` — котвата** | `…fire_varna_locations.py:150-154…` | `…fire_varna_locations.py:152-155…` | М: `git grep -n KIND_NORM` → `:152`; таблицата е `:152-155`. **Поправя се в ТЯЛОТО, не само в плана** — Ф7 е каноничният файл, който следващите лотове ще четат, а червен ред 8 после забранява да се пипа на място |
| **Х10** | **`_meta.decisions_open`, петият ред** | „**13** без район по АГКК → район по решение“ | „**16** без район по АГКК → район по решение“ | М: 98 − 82 = **16**, изброени поименно в §1.7 и в Р14. Същият довод като Х9 |

**`mask`, `diff_v1_v2`, `registry_pending_new` и `excluded` НЕ влизат в `Ф7`** — те са в `_meta` на артефакта (ИА-О10). **Човешката котва за Gate 2 не е предварителен sha (той е неизвестим преди Х1–Х10), а изходът на ИА-16: „десет наименувани разлики, нула други“, плюс sha-то, което Изпълнителят отпечатва след записа.**

### 3.Г · Правилата на новия билдър (`Ф1`) — дословно, без празни места

**Г.1 · Кой ражда Feature и къде отива всеки от 98-те реда.**
`include = "да"` → Feature (**79**). Всеки ред от `virtual_parents` → Feature с геометрия = обединението на децата му (**5**). **Общо 84.** Останалите **19** реда се разпределят в **два обявени дома, затворено**:

1. **Домът `_meta.excluded`, **10 РЕДА** (и **11 ЗАПИСА**):** десетте реда с **`kind_registry = null`** (пет обекта, пет села — поименно в §1.6), всеки с `code`, `raion_num`, `imot_name`, `kind` (суровият imot-вид), **`delivered: false`** и **`reason` = дословният `kind_note` от тялото**; плюс **един ЕДИНАДЕСЕТИ запис `vinitsa_sever` със `status: "reinstated"`, `delivered: true`** (ИА-О15, Р17), който **не е дом на ред** — редът му е Feature — а е запис на обърнато подписано решение. **Биекцията, която ИА-17 съди: `kind_registry = null` ⇔ запис в `excluded` с `delivered: false`. Записите с `delivered: true` са точно тези, за които §2 носи отклонение — днес един.** За `pristanishte_varna` записът носи и `district_witness_note` (разминаването наш слой ↔ АГКК, §1.7).
2. **`_meta.rows_without_feature` — затворена ДВОЙКА кофи, 9 реда:** `deferred[]` (**6**: `pz_topoli`, `vz_zvezditsa`, `krushkite`, `lazur`, `orehcheto`, `pripek` — всичките с вид, 0 сгради; **сборната площ на всичките 11 отложени реда с петте села е 10,691 km²**, М) и `no_boundary[]` (**3**: `elektrorazpredelenie_varna`, `malka_chaika`, `severna_promishlena_zona`). Трета кофа няма; `virtual_parent` **не е кофа**. **Наборът кофи се различава от v1 (`alias_of` + `deferred`) — обявено в ИА-О21 и в `declared_deviations[]`.**

**Инвариантът, който ИА-3 съди: 98 = 79 (Feature) + 10 (excluded_rows) + 6 (deferred) + 3 (no_boundary); `len(_meta.excluded) == counts.excluded_entries == 11`.**

**Г.2 · Всичките 41 полета на `properties` — правило за всяко:**

| поле | правило за v2 |
|---|---|
| `code` | кодът от решенията (79) / от `virtual_parents` (5) |
| `name` | `imot_name` с префикса на вида / `virtual_parents[].name` |
| `kind` | **`kind_registry` от Ф7** — от закритата таблица `KIND_NORM` (Ч `fire_varna_locations.py:152-155`). **Нула измислени стойности** (М: 84/84 покрити) |
| `parent` / `parent_display` | кодът/името на виртуалния родител при 17-те деца, иначе `null` |
| `parent_geometry_check` | `"дете ⊆ родител по конструкция (обединение)"` за 17-те; `"няма родител"` за останалите 67 |
| `source` | `"imot_bg_tiling"` (84 ×) |
| `method` | `"external_tiling"` (79) / `"imot_tiling_union"` (5) |
| `geometry_origin` | `"imot_bg_points"` / `"imot_bg_points_union"` |
| `imported_from` | `"imot_08.09#raion=<raion_num>"` / `"imot_08.09#union=<code>"` |
| `version` | `2` (84 ×) |
| `precision_m` | по Р8 (**100**) |
| `district` / `district_src` | §3.Г.5 |
| `signed_by` · `approved_by` | `"Petar"` |
| `approved_at` · `confirmed_at` | `"2026-09-08"` — **датата на подписа, не часовник** (детерминизъм) |
| `confirmed_by` | `"Petar (Gate 1, ПЛАН_Картата_imot_И-А_08.09)"` |
| `fetched_at` | `properties.fetched` на снапшота (М: една стойност, `"2026-09-08"`) |
| `chosen_source` | `"imot_bg_tiling"` / `"imot_bg_tiling_union"` |
| `chosen_reason` | `""` за клетките; за родителите — `"обединение на поименно подписаните деца (ADR 011 И-D4)"` |
| `license` · `license_terms` · `license_label` · `attribution` | дословно по Р10 |
| `url` | **дословно `_meta.list_endpoint` на снапшота**, с опашката: `https://www.imot.bg/obiavi/prodazhbi/grad-varna (95 with adverts, counts)` — **непразен по всичките 84** |
| `note` | `""`, освен за петте родителя, където носи изброените деца |
| `raw_geometry_sha256` | sha256 на компактния `{"type","coordinates"}` на **суровия** полигон (клетки) / на **проектираното обединение, върнато в WGS84 преди канонизация** (родители) |
| `wm_polygon_sha256` | **sha256 по канонизацията на D1** върху крайната геометрия — полето запазва смисъла си „хеш по D1“; `_meta.canonicalization` го казва изрично |
| `witnesses[]` | §3.Г.4 |
| **десетте нулирани** — `drawn_by, drawn_at, basemap, viewport, visible_layers, screenshot_sha256, approval_digest, wm_id, wm_ids, wm_title` | **`null` по всичките 84**. Седемте са договорът `D1_NULL_ON_IMPORT` (Ч `_meta.d1_schema.nulled_on_import`; М: null × 60 във v1); трите уикимапийски се добавят, защото извор няма (ИА-О16). **ADR 011 И-D2 иска низ в `drawn_by` — това е разминаване и се поправя в К8, не в артефакта.** |

**Г.3 · Канонизация по D1:** 6 знака, дедупликация на съседни върхове, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх, UTF-8 без BOM, `sort_keys`, компактно, финален LF. **Доказано безопасна** (М: 0 невалидни преди и след канонизация; 712 споделени отсечки остават споделени).

**Г.4 · Провенанс и преименувания, обявени поименно.** `witnesses[]` носи `{kind: "imot_bg_details", advert_id, raw_response_sha256, fetched_at, raion_num}` + `{kind: "imot_bg_dictionary", sha256, fetched_at, n: 98}`. **Съответствието с входа е обявено, защото имената НЕ съвпадат** (М): `witnesses.raw_response_sha256` ← `properties.provenance.raw_sha256` (низът `raw_response_sha256` се среща **0 пъти** в снапшота); `witnesses.fetched_at` ← `properties.fetched`; `witnesses[dictionary].sha256` ← **sha256 на файла-речник `feba76e3…`**, а НЕ вграденото `_meta.dictionary_sha256 = 6fa3b070…`, което е хешът на суровия HTTP-отговор и се записва отделно в `_meta.inputs[dictionary].raw_response_sha256` **като свидетел, който никой не сверява**. Родителите носят `witnesses` = обединението на витнесите на децата си. **Тези полета живеят САМО в частното репо** (червен ред 5).

**Г.5 · Районът.** `district` = кодът от НАШИЯ слой (`C:/git/m6000_private/number_viewer/quarters_layer.geojson`, филтър `authority == "osm"` и `display ∈ DISTRICTS`, Ч `build_quarters_signed.py:396-398`, `fire_varna_locations.py:141-147`) по **представителна точка**; `district_src = "fire_varna_district"`, или `"agkk_au5_confirmed_by_petar"` за код с ред в подписания `district_resolutions`. Виртуалните родители минават през **същото** правило (М: и петте получават еднозначен район). Разминаванията със свидетеля АГКК се изброяват поименно в `_meta.district_witness_disputes`, всяко с `delivered` и `resolution` (`"petar_agkk"` за подписаните, `"pending_petar"` за новите), по амандамента Р19.

**Г.6 · Виртуалните родители.** Обединение в **EPSG:32635**, връщане в WGS84, същата канонизация; `_meta.union_crs = "EPSG:32635"`, `_meta.union_recipe.authority = "projected"`, `_meta.union_witness.by_code` носи хеша на всяко обединение. **D8 е изпълнен по построяване.** Мерено: и петте дават единичен `Polygon` без вътрешни пръстени; площите **1,981 (kv_levski) / 3,453 (vladislavovo) / 1,205 (vazrazhdane) / 1,041 (mladost) / 0,612 (pobeda_group) km²**.

**Г.7 · Входовете по sha — ШЕСТ, и ВСИЧКИТЕ ШЕСТ живеят в `_meta.inputs[]`** (така D10 е изпълнен буквално; другите `_meta` ключове само **препращат** към записа в `inputs`, не го заместват):

1. полигоните (`77b40564…`, 175 736 B) — файл в `varna_3d/data/`;
2. речникът (`feba76e3…`, 6 274 B) + вграденото `6fa3b070…` като несверяван свидетел;
3. тялото с решенията Ф7 — **прочетено като блоб на varna_3d** (`{path, rev, sha256, bytes}`); `_meta.decisions_sha256` / `decisions_commit` / `decisions_path` са същите стойности, изнесени поименно по образеца на v1;
4. `Fire_Varna/data/address_rows.json` (`2a4766bd…`, 5 073 137 B) — **блоб на Fire_Varna**; `_meta.mask.address_rows_sha256` препраща към него;
5. **`Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json` — БЛОБ** (`rev e6c706d…`, sha `d494d4d256ae…`, 513 B); `_meta.district_resolutions.input` препраща към записа в `inputs`;
6. **`C:/git/m6000_private/number_viewer/quarters_layer.geojson` — ФАЙЛ извън git** (`26e39b00…`, 201 130 B), с `note: "извън git репо — пинва се по прочетени байтове (Р21, ИА-О23); версионирането е дълг ИБ-17"`.

**Разлика между пина и прочетените байтове = `sys.exit(1)`** за всичките шест.

**Г.8 · `_meta` — ЗАТВОРЕНИЯТ НАБОР ОТ 41 ИМЕНА, изброен изчерпателно:**

`artifact_class · attribution · canonicalization · counts · d1_schema · decisions_author · decisions_based_on · decisions_blob_before_attribution · decisions_commit · decisions_path · decisions_sha256 · decisions_sha256_rule · decisions_sha256_worktree · declared_deviations · dictionary_sha256 · diff_v1_v2 · district_resolutions · district_witness_agkk · district_witness_disputes · excluded · generated_by · inputs · licences · lot · mask · method_licence · parent_child · parent_child_without_polygon · plan · precision_floor_m · precision_m_by_method · publication · registry_pending · registry_pending_new · rows_without_feature · signature · snapshot_date · source_terms · union_crs · union_recipe · union_witness`

(= 36-те на v1 **+** `dictionary_sha256`, `snapshot_date` по ADR 011 И-D2 **+** `diff_v1_v2`, `mask`, `registry_pending_new`; `decisions_sha256` и `source_terms` вече са сред 36-те.)

Съдържанието: `artifact_class = "signed_by_plan_signature"` · `lot = "И-А"` · `plan` = този файл + sha на тялото му · `generated_by = "Claude Executor"` · `decisions_author = "Claude Architect (черновата, 7556227) → Петър (подпис)"` · `decisions_based_on` = черновият блоб `8626ad43…` + ревизията му · `decisions_blob_before_attribution` = същият · `decisions_sha256_rule` = дословно правилото на червен ред 12 · `decisions_sha256_worktree` = `{path, bytes, note: "varna_3d е eol=lf — работното копие Е блобът (git check-attr)"}` · `d1_schema` = полетата + **десетте** нулирани (ИА-О16) · `canonicalization` = трите правила + изричното изречение за `wm_polygon_sha256` при извор без уикимапийски обект · `dictionary_sha256` = **sha на ФАЙЛА** `feba76e3…` · `snapshot_date = "2026-09-08"` · `method_licence = {external_tiling: …, imot_tiling_union: …}` · `licences[]` = **един** запис (imot.bg) · `source_terms.imot_bg` = шестте ключа на Р10 · `attribution` = редът на Р10 · `publication` = „Геометрия НИКОГА не пътува публично; публично излизат само име, код и `src`“ · `precision_floor_m = 50` · `precision_m_by_method = {"external_tiling": 100, "imot_tiling_union": 100}` · `parent_child` = **17** двойки (**и това е ЕДИНСТВЕНИЯТ извор на родство, който гейтовете четат**) · `parent_child_without_polygon = []` · **`excluded` = 11 записа / 10 реда (Г.1)** · `rows_without_feature` = двете кофи (Г.1) · `registry_pending` = **28**-те регистрови кода без Feature · `registry_pending_new` = **28**-те доставяни кода без ред в регистъра · `district_resolutions` = приложените + препратка към вход 5 · `district_witness_agkk` = картата код → АГКК (**82** реда с двете стойности) · `district_witness_disputes` = **5** (4 `delivered: true`, 1 `delivered: false`) · `union_crs` / `union_recipe` / `union_witness` = Г.6 · `signature` = Gate 1 · `counts` = 15-те полета на Х5 · `mask` = §1.5, включително `tie_break_rule` · `diff_v1_v2` = ИА-13, включително `tie_break_v1` (Р20) · `declared_deviations[]` = **дословният списък ИА-О2, ИА-О4, ИА-О10, ИА-О12, ИА-О15, ИА-О16, ИА-О17, ИА-О21, ИА-О23, ИА-О24 + Г.2 (`drawn_by`) + Г.4 (двете преименувания)** — **всяко отклонение живее и в артефакта, не само в плана.**

**Г.9 · Детерминизъм.** Никаква дата „сега“, никакъв `set` в изхода, никаква подредба, зависеща от речник; два прогона → еднакви байтове (ИА-10).

### 3.Д · `Fire_Varna` — три проследени документа и един игниран файл

| # | път | какво |
|---|---|---|
| **Д1** | `docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` | **този текст, редакция 4, както го подписва Петър** — записва се на диска на стъпка 2 върху лежащата там редакция 2 (ИА-О22). **Нула координати в текста** (червен ред 5, съди се от ИА-19). |
| **Д2** | `docs/decisions/011_kartata_imot.md` | **ред-статус** („И-А изпълнен; тялото и геометрията са в varna_3d; И-Б отворен“) + поправките: **И-D3 (`:17`) — каноничният път става `varna_3d/data/quarters_decisions_imot_2026-09-08.json`** · **И-D2 (`:15`)** `drawn_by` → `null`, `raw_response_sha256` → обявеното съответствие с `provenance.raw_sha256`, `source_terms` от два на **шест** ключа, и изричното потвърждение, че `dictionary_sha256` + `snapshot_date` СА в `_meta` · **И-D4 (`:19`)**: виртуалните родители СА Feature-и (84 = 79 + 5) · **И-D5**: нови редове за архива на v1, за преместеното тяло, за копирания снапшот, **за обръщането на `vinitsa_sever` (Р17)**, **за амандамента на ADR 010 D0/G23 (Р19)** и **за пина по байтове на слоя с районите (Р21)** · **„Последствия“ (`:47`)**: `97,2 %` → **95,90 % за доставката (79 клетки) / 97,18 % при включени обекти**; `:48` „около 18 280 сменят думата“ → измереното **17 982 сменени · 935 изгубени · 9 832 спечелени** (при обявеното правило Р20); площите `61,7 km²` → **61,597 обединение / 66,886 сбор** за v1 и **74,615 / 82,908** за v2. **Статусът остава `Proposed`** (Ч `011:3`). |
| **Д3** | `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` | **§21** — „Под-лот И-А затворен“: какво е построено, къде живее, кои гейтове са зелени, какво чака И-Б, входна точка за следващата сесия. **Файлът пристига мръсен; К9 носи и този хънк** (ИА-О19). |
| **Д4** | `scratch/boundary_gallery/granitsi_preview_05.09/imot_v2_review_08.09.html` | **пробата за окото на Петър** (§8 т. 3). **ИГНОРИРАН** (М: `.gitignore:64:/scratch/boundary_gallery/`), никога проследен, никога комитван. Изброен ТУК поименно, защото червен ред 4 забранява ДОКОСВАНЕ, не проследеност — без този ред §8 искаше нарушение (кръг 3, ГОЛЯМ). |

**Механичната червена черта:** след всеки от трите комита се пуска `python gates/probe/b3_g11.py HEAD --cached`. Мерено защо това е безопасно: `changed()` (Ч `:70-83`) събира `new` от `git diff --cached --diff-filter=AMR HEAD`, тоест **от ИНДЕКСА срещу новия HEAD** — комитнатият файл вече е в HEAD и не е в дифа, значи `stray_new` остава `[]`, а **`ALLOWED_NEW` (Ч `:40-46`, седем записа; `LEGACY` е `:39`, `GEO` е `:37`) не се пипа**. `inventory()` (Ч `:84-93`) гледа само `data/*.json`, а **обхватът е Ч `:105-106`** (`scope = sorted(set(tracked) | set(f for f in touched if f.lower().endswith((".json", ".geojson"))))`; `tracked` идва от `:98`, `touched` — от `:104`) — **трите документа са `.md` и не влизат в него.** *(Редакции 2 и 3 цитираха `:104-108` и `:109-111`; и двете са грешни — `:109-111` е тялото на цикъла по `scope`. Поправено на двете места, където се ползва: тук и в ИБ-4.)*

---

## 4 · Ред на изпълнение

| стъпка | кой | какво | спирачка |
|---|---|---|---|
| 0 | Изп | Пълната мярка на §1 **без нито една редакция**. Записва OID-ите на 14-те стейджнати пътя (`git ls-files -s -- <14-те>`), деветте изхода Н1–Н9, **16-те идентификатора на тестовете** и **дословно мръсния хънк на Д3**. | разлика = **ИА-STOP 2** |
| 1 | **Петър** | **Gate 1** — подписва този план и **двайсет и едното** решения на §9. | без подпис нищо не тръгва |
| 2 | Изп | **Записва подписания текст като `Д1`** (върху редакция 2, ИА-О22) → пуска **ИА-19** върху Д1 → `git add -- docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` → комит **К1** → `b3_g11.py HEAD --cached` = 0 | ИА-19 ≠ 0 = **ИА-STOP 17**; b3_g11 ≠ 0 = **ИА-STOP 9** |
| 3 | Изп | Копира Ф5, Ф6 в `varna_3d/data/`; прави **единствената** редакция Т1; `git check-ignore -v` за Ф5, Ф6 → **нищо**; `git add -- data/imot_bg_varna_polygons_08.09.geojson data/imot_bg_varna_dictionary_08.09.json .gitignore`. **Не комитва.** | игниран вход = **ИА-STOP 11** |
| 4 | **Петър** | Комит **К2** (замразеният вход + `.gitignore` — **и четирите unignore реда, включително този за архива, са в ТОЗИ комит**). | — |
| 5 | Изп | Пише Ф1, Ф2, Ф3. Още нищо не се стартира срещу истински данни. | — |
| 6 | Изп | Подготвя **Ф7** в `varna_3d/data/`; пуска **ИА-16** (десетте разлики срещу черновия блоб) **без позиционен път** (ИА-О22) и отпечатва sha-то на записаното. `git add -- data/quarters_decisions_imot_2026-09-08.json`. **Не комитва.** | разлика извън списъка = **ИА-STOP 3** |
| 7 | **Петър** | Комит **К3** — подписаното тяло. | — |
| 8 | Изп | Строи в `%TEMP%/ia_build_a` и `%TEMP%/ia_build_b` → `cmp` (ИА-10). | различни байтове = **ИА-STOP 6** |
| 9 | Изп | Пуска Ф2 върху `<tmp>` артефакта: **ИА-1 … ИА-11, ИА-14 … ИА-17**. После **ИА-13 в двете си половини, с `--diff data/quarters_signed.geojson`** — v1 още стои там. **ИА-12 НЕ се пуска тук: командата му сочи архивния път, който още не съществува** (М: `qa_quarters_signed.py:1214-1216` `if not path.exists(): return 1`). | ≠ очакваното = **ИА-STOP 3** |
| 10 | Изп | `--make-fixtures --fixtures-dir %TEMP%/ia_fixtures` **върху построения артефакт**. **Причината стъпката да е ТУК е една: преди билда артефакт няма.** *(Не е вярно, че `make_fixtures` мутира документа — `clone()` на `:929-930` е дълбоко копие, М.)* Прогонва всяка фикстура с нейния `--only` и записва **истинския ѝ изходен код** и първия ред от изхода. Двете временни дървета се вдигат и се махат по ИА-О18. | фикстура с изход 0 = **ИА-STOP 5** |
| 11 | Изп | Комит **К4** (билдър, гейт, тест). **Фикстури НЕ се комитват** (ИА-О20). | — |
| 12 | Изп | Редакции Т2, Т4, Т5, Т7, Т9, Т11, Т13, **Т14**; подготвя **Т15 (двете места)**. `git mv data/quarters_signed.geojson docs/archive/quarters_signed_v1_2026-09-06.geojson`. Копира артефакта от `%TEMP%/ia_build_a` в `data/quarters_signed.geojson`. `git add --` изричните пътища. | — |
| 13 | Изп | **Пълният §5 върху новите пътища**: ИА-1 … ИА-19 (сега ИА-12 и ИА-13 сочат `docs/archive/…`) и **Н1′–Н9′**. Произвежда **Д4**. | всяко отклонение = **ИА-STOP 4** |
| 14 | Изп | Комит **К5** (кодът + Ф9). **`.gitignore` НЕ е тук** — вече е в К2. | — |
| 15 | **Петър** | Комит **К6** — v2 + `git mv` на v1 + `fire_varna_location_inputs.json`. | — |
| 16 | Изп | Комит **К7** (предложението за регистъра). | — |
| 17 | Изп | Комити **К8** и **К9** във Fire_Varna → **ИА-19 върху Д2 и Д3 преди всеки** → `b3_g11.py HEAD --cached` = 0 след всеки. | ИА-19 ≠ 0 = **ИА-STOP 17**; b3_g11 ≠ 0 = **ИА-STOP 9** |
| 18 | Изп | Пуска §5 наново, **отгоре докрай, върху комитнатото състояние**, и записва всеки изход дословно. Проверява `git worktree list` в **двете** репа и `git status --short` — **нула остатъци от `%TEMP%`, нула временни дървета**. | остатък = **ИА-STOP 1** |
| 19 | **Одитор** | Независим преглед на дифа срещу този план, ред по ред. | НЕГОДНО = **ИА-STOP 8** |
| 20 | **Петър** | §8 локален преглед → **Gate 2** → пуш (varna_3d `rezhimi`, Fire_Varna `main`). | — |

---

## 5 · Гейтове

**Кой гейт от кого се изпълнява (обявено, защото кръг 3 намери, че Ф2 „покрива ИА-1…ИА-18“, а две от тях не са в него):**
**Ф2** → ИА-1 … ИА-11, ИА-13 … ИА-17. **Старият гейт `src/qa_quarters_signed.py`** → ИА-12. **Ф3 (unittest)** → ИА-18. **Обявена команда с grep** → ИА-19.

**Как се чупи вход.** Четири механики, защото входовете са четири вида:

1. **Файл на диска** (снапшот, речник, `address_rows`, слоят с районите): счупено копие в `%TEMP%/ia_broken/`, гейтът се вика с път към него.
2. **Блоб на Fire_Varna** (`district_resolutions`, черновата за ИА-16): `git -C C:/git/Fire_Varna worktree add --detach C:/Users/Petar/AppData/Local/Temp/ia_neg_fv HEAD` → счупва се копието ТАМ → `git -C <wt> add -f -- <път>` → **`git -C <wt> -c user.name=… commit`** (детачнат HEAD, дангълинг комит, реалните клонове не мърдат) → гейтът се вика с `--resolutions-repo <wt> --resolutions-rev HEAD` (или `--draft-repo <wt>`) → **задължително** `git -C C:/git/Fire_Varna worktree remove --force <wt> && git -C C:/git/Fire_Varna worktree prune`.
3. **Блоб на varna_3d** (Ф7): **ВТОРО, отделно дърво** `git -C C:/git/varna_3d worktree add --detach C:/Users/Petar/AppData/Local/Temp/ia_neg_v3 HEAD`, същата процедура, `--decisions-repo <wt> --decisions-rev HEAD`, махане с `git -C C:/git/varna_3d worktree remove --force`. **Едно дърво не стига: Ф7 живее във varna_3d и този път просто НЕ СЪЩЕСТВУВА в дърво на Fire_Varna** (кръг 3, БЛОКЕР).
4. **Артефакт** (v2) и **проза** (за ИА-19): счупено копие в `%TEMP%`, гейтът се вика с него.

**Само `git add -f` НЕ стига** — мерено на цитирания образец (Ч `scratch/places_search/qa_night_pins.py:15-20`, `:111`, `:118`, `:171-175`): той доказва проследеност и сверява `worktree_sha256`, **но не подменя съдържание на блоб**. **Никой от тези пътища не е път от write-set-а** (ИА-О18).

**Всяка отрицателна половина се вика така, че да пада по СВОЯТА проверка.** Гейтът приема `--only <ИА-номер>`, който изключва останалите. Всяка се записва с: командата, счупения вход, `--only`, **истинския изходен код** и първия ред от изхода.

| # | гейт | команда · кога | очаквано | отрицателна половина (ТРЯБВА да даде ≠ 0) |
|---|---|---|---|---|
| **ИА-1** | валидност ПРЕДИ поправка | Ф2, `<артефакт> --tiling …` · стъпки 9, 13, 18 | 0; „95 входни полигона · **0 невалидни преди поправка** · 79 доставяни клетки · **0 невалидни след канонизация**“ (М) | копие на снапшота с пръстен „папийонка“ (самопресичане) → 1 |
| **ИА-2** | 0 застъпвания сред клетките · споделени ръбове | Ф2 · 9, 13, 18 | 0; **0 застъпващи се двойки > 0 m² сред 79-те клетки** · **712 споделени отсечки** · **2 849 върха** · **2 137 различни отсечки** (М) | копие на снапшота, в което една клетка е **буферирана с +0,0002°** → застъпване с всеки съсед → 1. (**Не „изместен връх“** — изместване навън прави процеп и гейтът остава 0.) |
| **ИА-3** | всеки от 98-те реда има точно един дом | Ф2 · 9, 13, 18 | 0; **98 = 79 Feature + 10 excluded_rows + 6 deferred + 3 no_boundary**; `len(_meta.excluded) == 11`; всяко id от речника точно веднъж; **`_meta.counts` (15 полета) съвпада дума по дума с преброеното**; **84 Feature-а = 79 + 5** | (блоб varna_3d) копие на Ф7 с махнат ред → „id без дом“ → 1; копие на артефакта с ръчно пипнат `counts.cells` → 1; копие с `counts.excluded_rows = 11` → 1 |
| **ИА-4** | застъпванията в артефакта са САМО родител–дете | Ф2 · 9, 13, 18 | 0; **17 двойки > 1 m², всичките в `_meta.parent_child`, всяка равна на пълната площ на детето; нула други** (М). Сбор на площите **82,908 km²**, обединение **74,615 km²** | копие на артефакта, в което геометрията на един родител е свита → двойката вече не е „дете ⊆ родител“ → 1 |
| **ИА-5** | D8 по конструкция | Ф2 · 9, 13, 18 | 0; всеки от **5**-те родителя е точно обединението на изброените си деца (17 общо), дете ⊆ родител, DAG без цикъл, `parent_child` = **17** двойки | (блоб varna_3d) копие на Ф7 с махнато дете от `children` → „родителят не е обединението“ → 1 |
| **ИА-6** | схемата | Ф2 · 9, 13, 18 | 0; **3 върхови ключа · 3 Feature ключа · 41 `properties` ключа** дословно по §1.3; **`_meta` = ЗАТВОРЕНИТЕ 41 имена на §3.Г.8**; **десетте нулирани полета са `null` по всичките 84**; **`rows_without_feature` носи точно кофите `deferred` и `no_boundary`** (ИА-О21) | копие с махнат `wm_polygon_sha256` → 1; копие с добавен `n_pts` в `properties` → 1; копие с добавен 42-ри `_meta` ключ → 1; копие без `snapshot_date` → 1; копие с кофа `alias_of` → 1 |
| **ИА-7** | **приватност — САМО файлове с ДАННИ** | Ф2, `--privacy-scope` · 9, 13, 18 | 0. **Обхватът е ЕДИН път: `Ф7`** — единственият файл с данни, който този лот създава или мени и който е тяло, а не геометрия. **Ф10, Д1, Д2, Д3 са ПРОЗА и са извън обхвата по конструкция — тях ги съди ИА-19** (ИА-О24); `data/quarters_signed.geojson` и `data/imot_bg_varna_polygons_08.09.geojson` са извън обхвата по конструкция — те СА геометрията в частното репо. По имена на ключове: `advert_id, raw_sha256, raw_response_sha256, points, raion_points, localid, cadnum, center, coordinates, geometry, centroid, polygon, bbox` → **0** и **0 float-а в кутията на Варна** (М днес върху блоба `8626ad43…`: 0 и 0; подниз `advert` = 98 от `n_adverts` и НЕ се брои) | копие на `Ф7` с добавен ключ `"advert_id"` → 1; копие на `Ф7` с ключ `"center"` и двойка числа в кутията на Варна → 1 |
| **ИА-8** | `source_terms` + атрибуция | Ф2 · 9, 13, 18 | 0; `_meta.source_terms.imot_bg` носи **шестте** ключа `url, checked_on, quote, terms, verdict, position` (по образеца C9, Ч `qa_quarters_signed.py:362`); `verdict ∈ {allowed, allowed_with_conditions}`; `len(_meta.licences) == 1`; всеки от 84-те носи непразни `license`, `license_terms`, `license_label`, `attribution` и **`url`, равен ДОСЛОВНО на `_meta.list_endpoint` на снапшота** | копие с празен `position` → 1; копие с Feature, чийто `license` е голо „CC BY-SA“ → 1; копие, в което `url` е низът без опашката „(95 with adverts, counts)“ → 1 |
| **ИА-9** | **шестте входа са пиннати и сверени по прочетени байтове** | Ф2 · 9, 13, 18 | 0; `_meta.inputs` носи **точно шест** записа (§3.Г.7); блобовите три се четат по `git log -1 --format=%H -- <път>` в СВОЕТО репо; файловите три се хешват от диска; **шестият носи `note` за живота си извън git**. Записва се и мярката „varna_3d е `eol=lf`: работно копие = блоб“ (М) — **доказан капан, не отрицателна половина** | копие на артефакта с подменен `decisions_sha256` → 1; копие на снапшота с един променен байт при непроменен пин → 1; **(блоб Fire_Varna, дърво `ia_neg_fv`) копие на `district_resolutions` с трета резолюция, подадено с `--resolutions-repo/--resolutions-rev` → 1**; копие на слоя с районите с изтрит район → 1 |
| **ИА-10** | **два билда → едни байтове** | `Ф1 --out %TEMP%/ia_build_a/q.geojson && Ф1 --out %TEMP%/ia_build_b/q.geojson && cmp` · 8, 13, 18 | `cmp` мълчи, изход 0 | **`%TEMP%/ia_builder_nd.py`** — копие на Ф1 с една стойност от `datetime.now()` — пуснато два пъти → `cmp` → 1. *(„Билд с подменен снапшот“ НЕ е половината на този гейт: по Г.7 подмененият вход спира билда на пина, файл не се пише и `cmp` пада с „No such file“ — доказва пина, не детерминизма.)* |
| **ИА-11** | всяка адресна точка отчетена | Ф2, `--address-rows C:/git/Fire_Varna/data/address_rows.json` · 9, 13, 18 | 0; гейтът **преизчислява** и сравнява със записаното в `_meta.mask`: **80 510 = 77 210 (`in_one_cell`) + 1 (`tie_break`, развързан по Р6) + 3 299**; маската е **затворена тройка**: `outside_all_95` **2 274** · `excluded_cell` **1 025** (вътре в някоя от **десетте** изключени клетки; поименно 355/354/274/26/16 и 0 за петте села) · `deferred_cell` **0** (вътре в някоя от **шестте** отложени с вид); `address_rows_sha256` == sha на прочетения блоб (`2a4766bd…`) | копие на артефакта с `mask.in_one_cell` = 77 211 → преизчисленото не съвпада → 1; копие с четвърти клас в маската → „клас извън затворената тройка“ → 1. (**Не „махни клетка“** — точките само се местят и сборът остава 80 510.) |
| **ИА-12** | **нерегрес: v1 още се съди от своя гейт** | `python src/qa_quarters_signed.py docs/archive/quarters_signed_v1_2026-09-06.geojson --registry …` · **само 13 и 18** (преди стъпка 12 архивният път не съществува, Ч `qa_quarters_signed.py:1214-1216`) | **0**, същите 20 проверки, същите числа като Н1 | копие на архива с махнат Feature → 1 |
| **ИА-13** | **D9 / G15 — дифът, в ДВЕ половини** | (а) `Ф2 <артефакт> --diff <v1>` · (б) същата + `--diff-signed "Р18"`. **`<v1>` = `data/quarters_signed.geojson` на стъпка 9, `docs/archive/quarters_signed_v1_2026-09-06.geojson` на 13 и 18** | (а) **изход 2** и ред „над праговете на D9: **17 982** места > 2 · площ **+21,1 %** > 10 % — иска подпис“ — **това е G15, изпълнен, не отменен, и се записва в ОТЧЕТА като мярка**; (б) **0**, при което `_meta.diff_v1_v2` носи и гейтът **преизмерва**: 60 → **84** Feature · сбор 66,886 → **82,908 km²** · обединение 61,597 → **74,615 km²** · застъпвания **извън `_meta.parent_child`** **40 → 0** · **51 → 17** двойки · **51 общи кода** · **9 изчезващи, поименно** · **33 нови** · покритие **84,85 % → 95,90 %** · по адресна точка **49 397 / 17 982 / 935 / 9 832 / 2 364** при `tie_break_v1 = "азбучно най-малък код"` (Р20) | **половина (а) НЕ е отрицателната половина** — тя е гейт върху истински вход и мястото ѝ е в отчета (червен ред 6). Отрицателната половина е: копие на артефакта, в което едно от деветте изчезващи имена липсва от списъка → 1 при (б); и копие с `tie_break_v1` = друг низ при непроменени числа → 1 |
| **ИА-14** | регистърът и видовете | Ф2 · 9, 13, 18 | 0; **всеки от 84-те кода е или в регистъра (84 записа), или поименно в `_meta.registry_pending_new` (28)**; `_meta.registry_pending` == `set(registry) − 84-те` (**28**); **четирите жилищни кода без Feature (`druzhba, rozova_dolina, sv_ivan_rilski, trakia`) са изброени поименно с довод** (ИА-О17); **`kind` на всеки от 84-те е ключ на `KIND_NORM`** (М: 84/84); **`"TBD"` като код = червено; нула повтарящи се кодове** | копие с върнат `"code": "TBD"` → 1; копие с два реда на един код → 1; копие с код нито в регистъра, нито в `registry_pending_new` → 1; копие с `kind: "обект"` → 1; копие с `kind: "район"` (суровият imot-вид) → 1 |
| **ИА-15** | районът | Ф2 · 9, 13, 18 | 0; всичките 84 имат `district` от затворената петорка; **0 клетки „да“ без район** (М); `_meta.district_witness_disputes` носи **точно 5** реда (`vazrazhdane4, kochmar, so_planova, salzitsa` с `delivered: true`; `pristanishte_varna` с `delivered: false`), първите два със `resolution: "petar_agkk"` от блоба `d494d4d256ae…`, следващите два с `"pending_petar"`; `perchemliyata` носи `fire_varna_district` и бележка към подписаната резерва (Ч `qa_place_zone_aliases.py:74`); **знаменателят на свидетеля е 82 = 77 + 5**, а по доставяните клетки — **74 съгласия от 78** | копие с изтрит ред от `district_witness_disputes` → 1; копие с `district` извън петорката → 1; копие с `delivered: true` за `pristanishte_varna` → 1 |
| **ИА-16** | **`Ф7` срещу черновия блоб** | `Ф2 --decisions-diff --draft-repo C:/git/Fire_Varna --draft-path scratch/places_search/imot_decisions_1_2026-09-08_draft.json` — **без позиционен път** (ИА-О22) · 6, 13, 18 | 0; ревизията се намира с `git log -1 --format=%H -- <път>` (**`7556227…`**), sha-то на блоба е **`8626ad43…`**, 51 275 B; дифът е **точно десетте разлики Х1–Х10, нула други**; отпечатва sha на `Ф7` за Gate 2 | (блоб Fire_Varna, дърво `ia_neg_fv`) копие на черновата с единайсета разлика → 1; копие, в което Х4 е върнато на `"TBD"` → 1 |
| **ИА-17** | **изключените редове** | Ф2 · 9, 13, 18 | 0; `_meta.excluded` носи **11** записа: **десетте с `kind_registry = null`, всеки с `delivered: false` и `reason` = дословният `kind_note`**, плюс **един със `status: "reinstated"`, `delivered: true`** (`vinitsa_sever`, стария довод дословно, „Р17“). **Биекция: `kind_registry = null` ⇔ запис с `delivered: false`.** Запис с `delivered: true` иска ред в `_meta.declared_deviations` | копие на артефакта с махнат ред от `excluded` → „ред с null вид без запис“ → 1; копие без реда `vinitsa_sever` → „подписано изключване обърнато без запис“ → 1; копие с `delivered: true` без ред в `declared_deviations` → 1 |
| **ИА-18** | **мета-гейт: половините са тичали** | `python -m unittest discover -s tests` (частта `test_quarters_signed_imot_fixtures.py`) · 13, 18 | 0; тестът **ражда фикстурите в `%TEMP%/ia_fixtures`** и **прогонва всяка** с нейния `--only`, настоявайки за изход ≠ 0 **по своя номер** | фикстура, нарочно направена валидна → тестът пада → 1 |
| **ИА-19** | **прозата не носи координати** | `grep -nE '(4[23]\|2[78])\.[0-9]{4,}' docs/plans/ПЛАН_Картата_imot_И-А_08.09.md docs/decisions/011_kartata_imot.md docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` · **преди К1, преди К8, преди К9, и на 18** | **0 попадения** (`grep` изход 1 = няма съвпадение = ЗЕЛЕНО; изход 0 = ЧЕРВЕНО). Обхватът е **само трите проследени `.md` на този лот**; Д4 е игниран и не се съди | копие на Д1 в `%TEMP%/ia_docs/` с една добавена двойка координати → `grep` намира → **ИА-19 червен**. **Тази половина е задължителна: тя доказва, че регулярният израз наистина хваща** — днешният файл на диска носи три такива двойки (М, §1.1) |

**Н1′–Н9′ · нерегрес на базата** — командите **се менят на стъпка 12**, изходите **не**:

| # | команда ПРЕДИ стъпка 12 | команда СЛЕД стъпка 12 | изход |
|---|---|---|---|
| Н1′ | `qa_quarters_signed.py data/quarters_signed.geojson --registry …` | **`qa_quarters_signed.py docs/archive/quarters_signed_v1_2026-09-06.geojson --registry …`** (= ИА-12) | **0** |
| Н2′ | `qa_p8a.py --ledger …` | същата (пътят е по подразбиране, пренасочен от Т7) | **0** |
| Н3′–Н6′ | четирите гейта | същите (константите пренасочени от Т9, Т11) | **0** ×4 |
| Н7′ | `unittest discover -s tests` | същата; сверява се по **16-те идентификатора**, не по броя | **0** |
| Н8′ | `qa_fire_varna_m6.py` | същата | **3**, същите **8** реда |
| Н9′ | `scratch/granitsi/zone_alias_negatives.py` | същата (харнесът П13, пренасочен от Т14) | **0** |

---

## 6 · Комити

**Идентичности** (ADR 010 D16, Ч `010:68`): `Claude Executor <executor@local>` за код и документи; `Petar1984 <petar.dikov2019@gmail.com>` за данни, геометрия и подписи.

**Задължителната двойка команди** (мерено: `git commit -m "…" -- b.txt` върху непроследен файл дава `error: pathspec … did not match any file(s) known to git`, **изход 1**; след `git add -- b.txt` същият комит минава с изход 0):

```
git add -- <изричните пътища>
git -c user.name="Claude Executor" -c user.email="executor@local" \
    commit -m "<точното съобщение>" -- <изричните пътища>
```

Никакъв `git add -A`, никакъв `git add .`, никакъв `--no-verify`. Всяко съобщение завършва с реда `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`. Тема **≤ 72 знака** (Ч `varna_3d/AGENTS.md:160`), **на английски, без кирилица** — дължините са премерени поименно (М).

| # | стъпка | репо / ръка | съобщение (дословно) | зн. (М) | пътища |
|---|---|---|---|---|---|
| **К1** | 2 | Fire_Varna · Изп | `docs(plan): sub-lot I-A plan for the imot.bg tiling` | **51** | `docs/plans/ПЛАН_Картата_imot_И-А_08.09.md` |
| **К2** | 4 | varna_3d · **Петър** | `data: frozen imot.bg tiling snapshot 08.09, 95 polygons` | **55** | `data/imot_bg_varna_polygons_08.09.geojson`, `data/imot_bg_varna_dictionary_08.09.json`, `.gitignore` (**и четирите unignore реда**) |
| **К3** | 7 | varna_3d · **Петър** | `data: signed decisions for the imot.bg tiling` | **45** | `data/quarters_decisions_imot_2026-09-08.json` |
| **К4** | 11 | varna_3d · Изп | `feat(quarters): imot.bg tiling builder and its own gate` | **55** | `src/build_quarters_signed_imot.py`, `src/qa_quarters_signed_imot.py`, `tests/test_quarters_signed_imot_fixtures.py` — **без фикстури** (ИА-О20) |
| **К5** | 14 | varna_3d · Изп | `chore(quarters): v1 readers follow it to docs/archive` | **53** | `src/fire_varna_locations.py`, `src/qa_fire_varna_places_export.py`, `src/qa_p8a.py`, `src/qa_place_zone_aliases.py`, `tests/test_quarters_signed_fixtures.py`, `scratch/granitsi/zone_alias_negatives.py`, `docs/archive/РЕГИСТЪР_архив.md` |
| **К6** | 15 | varna_3d · **Петър** | `data: quarters_signed v2; v1 archived, never deleted` | **52** | `data/quarters_signed.geojson`, `docs/archive/quarters_signed_v1_2026-09-06.geojson` (`git mv`), `data/fire_varna_location_inputs.json` |
| **К7** | 16 | varna_3d · Изп | `docs: registry proposal for 28 codes outside the registry` | **57** | `docs/decisions/ПРЕДЛОЖЕНИЕ_регистър_imot_08.09.md` |
| **К8** | 17 | Fire_Varna · Изп | `docs(adr): ADR 011 status line and the 08.09 corrections` | **56** | `docs/decisions/011_kartata_imot.md` |
| **К9** | 17 | Fire_Varna · Изп | `docs(state): section 21 - sub-lot I-A closed, I-B open` | **54** | `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` (**носи и мръсния хънк на §20 — ИА-О19**) |

**Няма капан на реда.** В И-А **нито един sha на v2 не се пинва в код** — всичките осемнайсет пина гледат v1 по непроменените си стойности. Затова К5 може да предхожда К6, а К6 не иска препинване след себе си. Пинът на решенията живее в `_meta.decisions_sha256` и се сверява **по време на прогона** срещу блоба, не като литерал в код (Р9).

**Следпроверка след всеки комит:** `git status --short` (само планираните пътища), `git log -1 --pretty='%h %an %s'` (правилната ръка), `git log -1 --pretty=%s | awk '{print length}'` ≤ 72; за Fire_Varna — `python gates/probe/b3_g11.py HEAD --cached` = 0.

**Котвата за стейджнатия Б3.** OID-ите на 14-те пътя се записват на стъпка 0 и се сверяват след К1, К8 и К9. **В И-А те не мърдат нито веднъж.** Разлика = **ИА-STOP 7**.

---

## 7 · STOP

| # | условие | действие |
|---|---|---|
| **ИА-STOP 1** | пипнат е път извън §3, **или е останал ефемерен път/временно дърво след стъпка 18** (пътищата под `%TEMP%` по ИА-О18 НЕ са пътища от write-set-а, докато лотът тече) | спри, покажи `git status --short` и `git worktree list` за двете репа, питай |
| **ИА-STOP 2** | някой от Н1–Н9, 16-те идентификатора или мръсният хънк на Д3 се различават на стъпка 0 | спри — базата не е тази, за която е писан планът |
| **ИА-STOP 3** | Ф2 или ИА-16 дават изход, различен от очаквания в §5 (за ИА-13 очакваното е **2** без подпис и **0** с него), и находката НЕ е в §9 | спри, покажи находките дословно |
| **ИА-STOP 4** | някой от Н1′–Н9′ сменя изхода си (вкл. броя 8 на Н8′) | спри — регресия |
| **ИА-STOP 5** | обявена отрицателна половина **не падна** (изход 0), или падна с чужд номер въпреки `--only` | спри — по червен ред 6 това е по-лошо от липсващ гейт |
| **ИА-STOP 6** | двата билда не са байт-еднакви | спри — билдът не е детерминиран |
| **ИА-STOP 7** | OID на някой от 14-те стейджнати пътя на Fire_Varna се е сменил | спри — доставката Б3 е пипната |
| **ИА-STOP 8** | одиторът връща НЕГОДНО | спри, върни се при Петър |
| **ИА-STOP 9** | `b3_g11.py HEAD --cached` ≠ 0 след Fire_Varna комит | спри — приватностният гейт е червен |
| **ИА-STOP 10** | измерено число се разминава с §1 | спри и питай — **не** „поправяй“ числото в плана |
| **ИА-STOP 11** | `git check-ignore` показва, че някой от Ф5, Ф6, Ф7, Ф8 е игниран след Т1 | спри — архив и вход, които git не вижда, не са архив и вход |
| **ИА-STOP 12** | иска се `git rm`, `git checkout`, `git stash`, `git reset` или изтриване на подписано тяло | спри — никога |
| **ИА-STOP 13** | появи се нужда от ред в `Fire_Varna/index.html`, `data/`, `tests/`, `gates/`, или в **пети** път на Fire_Varna извън Д1–Д4 | спри — това е И-Б |
| **ИА-STOP 14** | появи се нужда от ред в `Varna_buildings` | спри — това е ръката на Петър по D14 |
| **ИА-STOP 15** | Петър не е подписал някое от **двайсет и едното** решения на §9 | спри — не се подразбира |
| **ИА-STOP 16** | блобът на черновата вече не е `8626ad43…`, **или** блобът на `district_resolutions_2026-09-07.json` вече не е `d494d4d256ae…`, **или** sha на слоя с районите вече не е `26e39b00…` | спри — основата на Ф7 или решаващ вход се е сменил |
| **ИА-STOP 17** | ИА-19 намери координатна двойка в Д1, Д2 или Д3 | спри — червен ред 5 е нарушен в проследен файл на публично репо |

---

## 8 · Локален преглед (кои проби гледа Петър)

Всички проби са **в игнорираната папка** на Fire_Varna и не пътуват никъде:

1. `scratch/boundary_gallery/granitsi_preview_05.09/imot_city_08.09.html` — **95-те полигона**. На око: Чайка, Левски, Владиславово, Аспарухово, Галата седят там, където Петър ги очаква.
2. `…/imot_decisions_sign_08.09.html` — **страницата за подпис**: 98-те реда с `include`, кода, вида, **`kind_registry`** и района. Тук се вземат Р2–Р5, Р7, Р15, Р16, Р17.
3. **Д4** — `…/imot_v2_review_08.09.html`, произведен от Изпълнителя на стъпка 13 (**обявен поименно в §3.Д, игниран, никога проследен**): **84-те Feature-а** върху подложката, оцветени клетка/родител, **плюс 3 299-те точки на маската** в два цвята (2 274 `outside_all_95` и 1 025 `excluded_cell`), **плюс деветте изчезващи имена** върху старите им места и **935-те адреса, които губят дума**.
4. Извадка от **6 конкретни места** за сверка на око (правилото „примери за поправка“): `avtogara` (район→кв, Р15) · двойката на общия ръб `chaika_kk` / `alen_mak` (Р6) · `perchemliyata` (единственият „да“ без свидетел АГКК) · `so_planova` и `salzitsa` (двата нови спора) · **`vinitsa_sever`** (изключеният от 07.09, който v2 връща — Р17) · **`pobeda_group`** (единственият виртуален родител, който v1 не познава, и единственият вид без извор — Р16).
5. **Живата карта НЕ се пипа и НЕ се гледа** — тя е на старите данни; това е И-Б.

---

## 9 · Решения за Петър (Gate 1) — **двайсет и едно**

Всяко решение има **предложение по подразбиране**. „Да“ на плана без възражение = приемане на предложенията. **Седемте отворени точки, които самото тяло изброява в `_meta.decisions_open` (Ч), са покрити от Р15/Р16, Р3, Р4, Р7, Р14, Р8, Р10.**

| # | Въпрос | Измереното | **Предложение по подразбиране** |
|---|---|---|---|
| **Р1** | **Къде живее подписаното тяло?** | Днес е `Fire_Varna/scratch/places_search/imot_decisions_1_2026-09-08_draft.json` (проследен, публично репо, блоб `8626ad43…`, 51 275 B). Носи `n_pts` (3 820) и `area_km2` (95 реда). Машинарията за подпис във Fire_Varna е ЧЕРВЕНА (ИБ-1); varna_3d е ЗЕЛЕНА (§1.2). | **МЕСТИ се в `varna_3d/data/quarters_decisions_imot_2026-09-08.json`.** Черновата остава непокътната; архивирането ѝ е И-Б. **ADR 011 И-D3 се поправя с изричен ред в К8.** |
| **Р2** | **Виртуалните родители Feature-и ли са?** | И-D4 (Ч `011:19`) ги иска като обединения; v1 носи 4 от 5 като Feature-и; М: и петте обединения дават **единичен валиден `Polygon` без вътрешни пръстени**. | **ДА — 84 Feature-а (79 + 5).** Иначе 17 деца сочат родител без геометричен носител, а списъкът „изчезващи“ скача от 9 на 13. |
| **Р3** | **Петте „обекта“** | Тялото им дава **`kind_registry = null`** с довод „обект: не е клетка → без вид“ (Ч). И петте имат полигон и сгради; и петте **липсват от регистъра**. **Държат 1 025 адресни точки** (355/354/274/26/16, М). С тях покритието е 97,18 %, без тях — 95,90 %. | **ИЗКЛЮЧЕНИ.** Стоят поименно в **`_meta.excluded[]`** с `delivered: false` и довода си дословно; точките им са клас `excluded_cell`. **Цената е назована: 1 025 адреса (1,27 %) остават без квартална дума.** |
| **Р4** | **Трите без полигон** — 5848, 5866, 6294 | Речникът ги знае, imot няма полигон; `buildings = null`, `area_km2 = null` (М). `malka_chaika` е в регистъра като `м-т`, а тялото му дава `kind_registry = "кв"` (М) — разминаване, което днес не удря гейт, защото редът е `no_boundary`. | **`no_boundary` — БЕЗ Feature.** Изброяват се в `_meta.rows_without_feature.no_boundary[]` с довод. **Не** се прави Feature с `geometry: null`. Разминаването по `malka_chaika` влиза в Ф10. |
| **Р5** | **Двата кода `"TBD"`** | М: 98 реда → 97 различни кода. | **`elektrorazpredelenie_varna` и `severna_promishlena_zona`.** Реални, уникални, по правилото К37 (slug). ИА-14 прави `"TBD"` и повтарящ се код червено. |
| **Р6** | **Точката на общия ръб** (една) | Върху **суровите** полигони — **0** двойни попадения; след канонизацията по D1 — **1**, между **5055 к.к. Чайка** и **5053 м-т Ален мак** (М). **(Координатата ѝ живее в частния файл и не се преписва тук.)** | **Развръзка по най-малък `raion_num`.** Записва се в `_meta.mask.tie_break` и `tie_break_rule`, проверява се от ИА-11. Тук печели **5053 „м-т Ален мак“**. |
| **Р7** | **Единайсетте отложени** | Шест носят вид; **пет са села с `kind_registry = null`**. И единайсетте имат **0 сгради**, нито един няма район, и **не хващат нито една адресна точка** (М). Сумарно 10,691 km². | **Разделят се по вида.** Шестте с вид → `rows_without_feature.deferred[]`. **Петте села → `_meta.excluded[]`** (null вид = изключен ред). И двете поименно, с довод. |
| **Р8** | **`precision_m` за плочката** | Медианата на ръба на **79-те канонизирани клетки** е **96,5 m** (М). v1 дава 100 за `human_polygon`, 50 за `street_bounded_face`; подът по D7 е **50** (Ч `010:50`). | **`precision_m = 100` за всичките 84.** Измерената рисувателна стъпка е под 100 и над пода 50. |
| **Р9** | **Как се пинва тялото?** | Литерал `DECISIONS_BLOB_SHA256` в гейта трябва да е написан **преди** комита К3, който ражда блоба — капанът, който събори кръгове v2–v5. | **Без литерал.** Гейтът чете `_meta.decisions_sha256` и настоява да е равно на `sha256(git show <rev>:<път>)` на файла, който наистина е прочел. **Човешката котва за Gate 2 е изходът на ИА-16** („десет наименувани разлики, нула други“) плюс отпечатаното sha. |
| **Р10** | **Атрибуцията и `source_terms`** (попълва се, не се обсъжда) | C9 иска на извор **шест** ключа (Ч `qa_quarters_signed.py:362`); ADR 011 И-D2 дава два — поправя се в К8. **`_meta.list_endpoint` е с опашката** (М). | **`_meta.attribution` и `properties.attribution`:** „Кварталните граници в този файл са районите на imot.bg (© imot.bg), снапшот 08.09.2026. Геометрия НИКОГА не пътува публично.“ · **`license_label`:** „граница по районите на imot.bg (район `<raion_num>`, свалена 2026-09-08) — извор на всекидневната употреба, не официален кадастър“ · **`url` = ДОСЛОВНО `_meta.list_endpoint`** · **`_meta.source_terms.imot_bg`** = `{url: "https://www.imot.bg/obshti-uslovia", checked_on: "2026-09-08", quote: <дословният цитат, преписан от Изпълнителя>, terms: "https://www.imot.bg/obshti-uslovia", verdict: "allowed_with_conditions", position: "Публично пътуват само име, код и src на квартала; геометрията остава в частното репо."}`. |
| **Р11** | **Архивните пътища** | `data/archive/` е **механично невъзможен** (М, §1.9); `docs/archive/` вече съществува и е проследен (М). | **`docs/archive/quarters_signed_v1_2026-09-06.geojson`** (+ ред `!…` в блока на Т1) и **`docs/archive/РЕГИСТЪР_архив.md`**. Старите `granitsi_decisions_2/3/4_*.json` **не се местят в И-А** — те са пиннати от `build_quarters_signed.py:89` и от `Fire_Varna/tests/test_b3_gates.py:34`; преместването им е И-Б. |
| **Р12** | **Двата нови спора за район** — `so_planova`, `salzitsa` | `kochmar` и `vazrazhdane4` вече имат подписано решение (блоб `d494d4d256ae…`, ревизия `e6c706d…`, М). Знаменателят на свидетеля е **82** (77 + 5). | **Нашият слой печели; спорът се ЗАПИСВА, не се решава.** `district_src = "fire_varna_district"`, двата влизат в `_meta.district_witness_disputes` с `resolution: "pending_petar"`. |
| **Р13** | **Къде живее замразеният вход?** | Днес и двата файла са само в **игнорираната** папка на **публичното** репо (М). Никое репо не ги носи. | **Копират се в `varna_3d/data/` и стават проследени там** (Ф5, Ф6; комит на Петър). Иначе v2 не е възпроизводим от нито едно репо. |
| **Р14** | **Шестнайсетте кода без район от АГКК** | 11 отпадат по Р7, `letishte` по Р3, трите без полигон по Р4, `perchemliyata` е покрит от вече подписаната поименна резерва (Ч `qa_place_zone_aliases.py:74`) и получава `primorski` от нашия слой (М). Всичките **79 клетки „да“ имат район** (М). **Черновата казва „13“; вярното е 16** — поправя се с Х10. | **Не искат отделно решение** — този ред е за да го видиш и да кажеш „да“ веднъж. |
| **Р15** | **`район` → `кв` или `мр`?** (19 клетки) | Тялото само го маркира „**ДА СЕ ПОДПИШЕ**“ (Ч). `мр` е в `KIND_NORM`, но `KIND_CLASS` го праща в **locality** (Ч `fire_varna_locations.py:156-160`), а по D6 locality **никога не пълни `quarter`** — 19-те най-всекидневни имена (Автогара, ЖП гара, Операта, Гръцката махала…) биха останали без квартална дума. | **`район` → `кв`.** Записва се в `_meta.kind_registry_decisions` (Х7). Алтернатива `мр` — само с изрична твоя дума, и тогава И-Б трябва да отвори `LOCALITY_CODES`. |
| **Р16** | **Видът на петте виртуални родителя** | Полето им `kind` е проза (М). Четирите съществуват в **подписания регистър** и във v1 с един и същ вид (М). `pobeda_group` няма ред никъде; двете му деца са `кв` (М). | **Четирите се преписват от регистъра; `pobeda_group → "кв"`.** Три от четирите стойности имат два независими извора. |
| **Р17** | **`vinitsa_sever` — обръщане на подписано изключване** | v1 `_meta.excluded` носи един ред за него (Ч дословно); черновата го дава като клетка 6295, `include = "да"`, `kind_registry = "вз"`, 294 сгради, 0,303 km² (М). | **Обръща се съзнателно: v2 го доставя.** Записва се като **единайсети** запис в `_meta.excluded` със `status: "reinstated"`, `delivered: true`, стария довод дословно и „Р17“, плюс ред в `declared_deviations` и в И-D5. **Ако кажеш „не“ — редът излиза от 79-те и v2 става 78 + 5 = 83; всяко число в §1.5, §1.7 и §5 се преизмерва преди изпълнението.** |
| **Р18** | **D9 / G15 — дифът е над праговете** | Ч `010:54` и `:129`. Мерено: **17 982** места сменят думата, обединената площ расте с **21,1 %**. | **Подписваш дифа.** ИА-13 (а) тича без подпис и връща **2**; ИА-13 (б) тича с `--diff-signed "Р18"`, преизмерва всичко и връща 0. **G15 не се отменя — изпълнява се.** |
| **Р19** | **Амандамент на ADR 010 D0/G23** | Ч `010:36`: „всяко бъдещо разминаване АГКК ↔ `district.code` = STOP“; Ч `:137` регистрира G23. М: `varna_3d/src/qa_district_official.py` **не съществува**. Плочката ражда два нови спора (Р12). | **Ред в ADR 011 И-D5** (не в ADR 010, който е извън write-set-а): за плочката АГКК AU5 е **независим свидетел**; разминаване, **записано поименно** с `resolution` (подписан) или `"pending_petar"`, не е STOP; разминаване **без запис** е STOP. ИА-15 го изпълнява; дългът е ИБ-16. |
| **Р20** | **Правилото за развръзка на страната v1 в дифа** | М: **4 517** от 80 510-те точки попадат в ≥ 2 полигона на v1 — без обявено правило числата „същата/сменена дума“ не са възпроизводими (кръг 3 обори двойката 49 926/17 453). Четири правила дават четири различни резултата (М: по реда на файла 49 925/17 454; азбучно 49 397/17 982; най-малка площ 50 100/17 279; най-голяма площ 48 662/18 717). | **Азбучно най-малкият код печели.** Довод: детерминизъм, независим от реда на файла — същият клас правило като Р6. Записва се в `_meta.diff_v1_v2.tie_break_v1` и се преизмерва от ИА-13. Числата: **49 397 / 17 982 / 935 / 9 832 / 2 364**. |
| **Р21** | **Слоят с петте района — вход, който git не вижда** | М: `C:/git/m6000_private` **не е git репо**; файлът е 201 130 B, sha256 `26e39b00…`, дава точно 5 района с `authority == "osm"`. Той решава `district` на всичките 84 Feature-а. | **Влиза като ШЕСТИ вход в `_meta.inputs`, пиннат по sha256 на прочетените байтове**, с `note` защо не е блоб. Алтернатива: да се копира и във `varna_3d/data/` — **не се предлага в И-А**, защото е чужд слой и иска отделно решение за собственост; дългът е **ИБ-17**. |

---

## 10 · Какво НЕ се пипа

1. **`Fire_Varna/index.html`** — нито един байт. `QUARTER_SRC`, `LOCALITY_SRC`, `DISTRICT_CODES`, `QUARTER_CODES`, `LOCALITY_CODES`, `ATTRIB_KEYS`, `ATTRIB_SRC`, `validQuarterAttribution`, кешът, трите sha пина, `LEGACY_BUNDLE_SHA` — всичките са И-Б.
2. **`Fire_Varna/data/`** — `places.json`, `hotels.json`, `place_categories.json`, `address_rows.json`, `approx_addresses_v1.json`, хидрантите. Само за четене.
3. **`Fire_Varna/tests/` и `Fire_Varna/gates/`** — включително `gates/probe/b3_g11.py` (`GEO` `:37`, `LEGACY` `:39`, `ALLOWED_NEW` `:40-46`), `gates/release.py`, `gates/coverage.py`, `gates/allow/`, опашката `ЗА_ПОДПИС_*`, `tests/test_b3_gates.py`.
4. **Стейджнатата доставка Б3** — 14-те пътя, с непроменени OID. **Двата мръсни нестейджнати JSON-а** също не се пипат.
5. **`Varna_buildings`** — регистърът (84 записа, `schema_version 1.1`, 15 ключа) е подписано тяло по D14. И-А произвежда **само предложение**.
6. **`varna_3d/src/build_quarters_signed.py` и `src/qa_quarters_signed.py`** — нула байта (ИА-О7).
7. **Пиновете по sha на v1** — `fire_varna_locations.py:94`, `qa_p8a.py:60-66`, `qa_place_zone_aliases.py:75`, двата блока в `fire_varna_location_inputs.json`, `test_quarters_signed_fixtures.py:172`/`:175`. v1 не мърда байт.
8. **`scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json`** — подписан леджер и исторически запис (ИА-О14). **`src/build_quarters_candidate.py` и `src/qa_quarters_candidate.py`** — червените им черти по базово име (П16) остават непокътнати.
9. **`docs/decisions/010_signed_quarter_boundaries.md`** — нула байта. Амандаментът по Р19 живее в ADR 011.
10. **`C:/git/m6000_private`** — само за четене; И-А не копира и не мести слоя (Р21).
11. **Адресният резолвер** и планът „Адресите по полигон“ — отделен лот. **Живата карта, Worker-ът, R2, публикуването.** Нищо не се публикува; пушът е на Петър.
12. **Лицензът като тема.** Полето се попълва по Р10 и толкова.

---

## 11 · Пренесено към И-Б (измерени дефекти, които И-А не докосва)

**ИБ-1 · Базата на Fire_Varna е ЧЕРВЕНА и не е поправена от този лот.** М днес: `python -m unittest discover -s tests` → **342 теста, 24 паднали** (**21 в `test_places_search_gate`, 3 в `test_b3_gates`** — М по модул); `python -m gates.run_gates` → **изход 1**; `python -m gates.release` → **изход 6**; `python -m gates.coverage` → **изход 4**. И-Б трябва да обяви интервала по D19 (Ч `010:74`), да изброи точния набор падащи тестове и да не позволи нищо извън него.

**ИБ-2 · `scratch/places_search/expectations.json` е пренаписан след подписа** — М (`gates.release`): „тялото **55cbf2c7f8f2** ≠ дайджеста на ред R8 (**f8c4e43f5e85**) — пренаписано след подписа“; плюс „✗ двигателят не е кандидатът, който е подписан: **a73fa006ab0b** ≠ **61967588780f**“ и мръсния `lot1v_v_reference_manifest.json`.

**ИБ-3 · Покритието е пробито ПРЕДИ лота.** Гейт 4 на `run_gates` (М, дословно): `places zone_named: before=127 after=91 lost=44 changed=44 gained=8`; `hotels zone_named: before=199 after=167 lost=39 changed=11 gained=7`; „coverage изход 2 — 30 непокрити загубени/сменени реда“. `gates/allow/2026-09-05_lot1v_v.json` не ги покрива.

**ИБ-4 · Приватностно нарушение вече в HEAD:** `scratch/places_search/adresi_astra_S39_08.09.md` (проследен, М) носи дословно `"advert_id"`, `"raw_sha256"`, ендпойнта на `mob_api/details` и **координатна двойка в кутията на Варна** (числата не се преписват тук — червен ред 5). `b3_g11.py` е **структурно сляп** за `.md` (обхватът му е проследени `data/*.json` ∪ променени `*.json/*.geojson`, **Ч `:105-106`**). Иска се изчистване или подписано изключение + разширяване на обхвата.

**ИБ-5 · Приватностното правило „списък от ≥ 4 числа“ е fail-open за именувани координати.** Пръстен `[{"lat":…,"lon":…}, …]` минава и през него, и през черния списък по имена.

**ИБ-6 · `index.html` — котвите за пребазиране (М, проверени поименно):** `:1901`/`:1918` `OSM_ATTRIB`; `:6268` `PLACES_CACHE`; `:6291-6293` трите sha пина (`HOTELS_SHA256`, `PLACES2_SHA256`, `CATS_SHA256`); `:6304` `LEGACY_BUNDLE_SHA`; `:6316` `QUARTER_SRC`; `:6320` `LOCALITY_SRC`; `:6322` `DISTRICT_CODES`; `:6324` `QUARTER_CODES` (**28** кода, М); `:6332` `LOCALITY_CODES` (**5**, М); `:6619` `ATTRIB_KEYS`, `:6620` `ATTRIB_SRC`, `:6625` `validQuarterAttribution` (викан на `:6579` и `:6600`).

**ИБ-7 · `tests/test_b3_gates.py`:** `:34` `DECISIONS_REL` сочи отменения `granitsi_decisions_4_2026-09-07_proba.json`; `:90-91` чете `doc["attribution"]` от **работното дърво**; `:172` `len(want) == 338`; `:174` sha `c6d29d4e…`; `:194` блоб; `:197` `yes_row_authorship(...) == []`. **Три от тестовете падат днес** (М).

**ИБ-8 · Опашката и allow-ът:** `queues_in_head` глобва по basename (Ч `gates/release.py:437`); `signable()` (`:189`) глобва **работното дърво** и при брой ≠ 1 ключът `allow` изчезва без грешка; `gates/coverage.py:87` `SIGNER = "Петър"`, `:96` `is_signed_by_petar`.

**ИБ-9 · `ALLOWED_NEW`** (Ч `gates/probe/b3_g11.py:40-46`, седем записа) е затворена седморка; всеки нов проследен път на доставката иска ред там. `LEGACY` е `:39`, `GEO` е `:37`.

**ИБ-10 · `scratch/places_search/qa_night_pins.py` е ЧЕРВЕН по конструкция** (пинове от 06.09). Механиката иска отделен, чист скрипт; `--worktree-negative` доказва проследеност и сверява `worktree_sha256` (Ч `:15-20`, `:111`, `:118`, `:171-175`), **не подменено съдържание на блоб** (§5).

**ИБ-11 · Преизносът на местата и хотелите + леджерите.** Регистърът първи (D13), после `EXPECT_SIGNED_CODES` (60 → **84**), `ATTR_SRC`/`ATTR_LABEL`/`ATTR_LICENCE`/`ATTR_URL_HOST`, `by_source` в резолвера (`fire_varna_locations.py:601-618`), **ЧЕТИРИТЕ екземпляра** на `KIND_NORM`/`KIND_CLASS` с **четирите различни отказа** (М, `git grep`): `src/fire_varna_locations.py:152`/`:156` → `die` на `:647-648`; `src/qa_fire_varna_m6.py:113`/`:117` → **гол `KeyError`** на `:210`; `src/qa_fire_varna_places_export.py:355` → **мълчалив `DROP`** на `:401`; **`src/qa_fire_varna_export.py:201` → тих `None` на `:247`** (`KIND_NORM.get(e["kind"])`). Плюс `qa_p8a.py:60-66`, двата блока в `fire_varna_location_inputs.json`, `polygon_version`/`polygon_sha256` по D3, и **П17**. **И измереното последствие на И-А:** от 84-те доставяни кода **32 са клас `locality`** (м-т 27 · пз 3 · зона 2) и по D6 **никога не пълнят `quarter`** — И-Б трябва да реши какво вижда потребителят на тези места.

**ИБ-12 · Деветте изчезващи имена** (`abatko, druzhba, gorchivata_cheshma, kokardzha_generic, morska_gradina, rozova_dolina, sredna_traka, sv_ivan_rilski, trakia`), **935-те адреса, които губят дума**, **1 025-те в изключените клетки** и публичните редове на `data/approx_addresses_v1.json` — таван на загубите и поименен allow.

**ИБ-13 · Номерацията на гейтовете** — `G4`, `G15`, `G17`, `G21`, `G22`, `G23` значат по две неща в ADR 010 и в живия план Б3; **`О1`–`О30` са заети** в `ПЛАН_Б3_07.09.md:234-263` (М). И-Б трябва да пребазира номерацията, преди да пише таблица.

**ИБ-14 · `G29` не съществува като регистриран гейт** (М: `grep -c G29 010_signed_quarter_boundaries.md` → **0**; таблицата върви G0–G24). Живее само в `ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md:71` (с препратки `:62`, `:104`) и в `qa_night_pins.py`. Не му се дава име на файл.

**ИБ-15 · `n_pts` и `area_km2` в черновата на Fire_Varna** (ИА-О9) — производни на частната геометрия в проследен файл на публичното репо; изчистване или подписано изключение, плюс архивиране на самата чернова, след като Ф7 е в HEAD.

**ИБ-16 · `qa_district_official.py` (ADR 010 G23) не е построен** (М). Амандаментът по Р19 го превръща в дълг с обявена котва; И-Б или го строи, или го пенсионира с ред в ADR 010.

**ИБ-17 · Слоят с петте района няма версия.** `C:/git/m6000_private/number_viewer/quarters_layer.geojson` (201 130 B, sha `26e39b00…`) решава `district` на всеки Feature на v1 И на v2, а **папката не е git репо** (М). И-Б трябва да реши: собствен проследен екземпляр, submodule, или подписан пин по байтове с процедура за смяна. Днес И-А го пинва по байтове (Р21, ИА-О23).

**ИБ-18 · Производните на частната геометрия в ПРОЗА нямат нито правило, нито гейт.** И-А добавя три проследени `.md` в публичното репо с площи по обект, статистика на ръба, брой върхове/отсечки, Hausdorff и sha-та на частни файлове; ИА-19 съди само **координати**, ИА-7 съди само **данни**. Че дупката е реална, а не теоретична, показва ИБ-4. И-Б трябва да напише правилото (какъв агрегат е позволен) и гейта, който го съди — за `.md` също, не само за `.json`.