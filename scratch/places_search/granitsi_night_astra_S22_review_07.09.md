Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a077e9-fc74-76c1-82cc-3fc40972510c
--------
user
S22 — POST-EXECUTION REVIEW of the night shift for lot Границите (06→07.09), lens MECHANICS (Petar: the architect, Kimi and Astra review the execution from different angles). Repos on this machine, read-only: C:/git/Fire_Varna (main) and C:/git/varna_3d (private, branch rezhimi). Read: Fire_Varna/docs/audits/ДОКЛАД_07.09_нощна_смяна.md (the night report, commit c6c5d44), Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md (the signed plan), the night commits: Fire_Varna a454b60 (Н0 pins + qa_night_pins.py), 093b259 (Н3-а fixtures), 57ab8eb (architect .gitignore fix), c6c5d44 (report); varna_3d 0fed1e0 (Н1), fb59f8d (Н2-0), 524fe31 (Н2), 5e468a1 (Н4), 2800a7c + 791b0cb (Б1: build_quarters_signed.py, qa_quarters_signed.py, tests/test_quarters_signed_fixtures.py) and the STAGED uncommitted varna_3d/data/quarters_signed.geojson (sha256 3f423898…, 61 Features). Lot Б2-0 (coordinates into place_identity.json) went RED on G9: the candidate changed 154 fields outside the four coordinate keys (77 zone + 77 key) because the identity base is from 04.09 and the generator inputs moved; the executor stopped; the architect afterwards restored src/place_identity.py to HEAD and moved the candidate, the qa script and the diff to C:/Users/Petar/AppData/Local/Temp/claude/C--git/26f42576-326e-4863-b700-f1e02c26a0c9/scratchpad/b20_inflight_2026-09-07/ (place_identity.py.diff, qa_place_identity_coords.py, place_identity.candidate.json) — read them there. Questions: (1) Do the night commits match the plan write-sets and messages exactly? Any file outside a write-set? Any hard-limit breach (push, geometry in tracked Fire_Varna files, registry, written quarters, the pre-existing dirty file scratch/place_bodies/qa_place_bodies.md)? (2) Б1: is data/quarters_signed.geojson consistent with Б0 (D1 schema for imported geometry with the 7 null fields, D1 canonical wm_polygon_sha256 + raw hash, mladost2 by the signed key with ODbL label and precision 50, district from our district code, parent_child DAG of 11, registry_pending 16, _meta.artifact_class)? Run python src/qa_quarters_signed.py with the right arguments and the negative fixtures (python -m unittest tests.test_quarters_signed_fixtures) and report exit codes. (3) G9 root cause: is the zone/key drift a generator non-determinism, a moved input, or a real base mismatch — and what is the correct morning procedure so that the coordinate step can pass without laundering (options: regenerate the base first from today's inputs and commit that as a separate step; or compare candidate vs a freshly regenerated no-coord run instead of the 04.09 backup)? (4) Is the report c6c5d44 accurate about the state as it is NOW (after the architect cleanup), and what one paragraph must an addendum correct? (5) Anything unsafe for Petar's morning push (Fire_Varna is 2 behind origin — ingest commits by Petar; the merge order). Verdict ГОДНО/НЕГОДНО for the execution, with named fixes; at most 1400 words; Bulgarian with English identifiers; cite file:line and commit shas.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя плановете, commit-ите и текущия index, ще пусна Б1 проверките и ще проследя причината за G9. Разделям независимите проверки между агенти; работата остава read-only.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:\\git\\Varna_buildings\\scratch\\hydrant_map_integration_frame.md' -TotalCount 220; Get-Location" in C:\git
 succeeded in 155ms:
# Hydrant Map Integration â€” Framing / Handoff (Phase 2 Reintegration)

**Status:** Framing draft (chat-Claude). Input for a new architecture cycle.
**Date:** 2026-06-21

This document is the handoff for integrating the hydrant app with the
buildings pipeline. It is the gated "Phase 2 reintegration" that
`docs/architecture_v2.md` deferred (requires an ADR 020 amendment). Start
the new Cowork session by reading this + both repos, then run the cycle.

---

## 1. Purpose

A firefighter searches an address â†’ finds the nearest hydrants; sees all
hydrants for field verification; the owner adds/edits hydrants, building
annotations, and the verification design **without touching core code**.
Mobile-first is the primary purpose.

## 2. The two repos

- **Varna_buildings** (PRIVATE, Python) â€” KAIS address/building pipeline +
  map app. Holds raw KAIS, intel, personal-data-sensitive material.
- **Fire_Varna** (PUBLIC, HTML/PWA) â€” "Ð¥Ð¸Ð´Ñ€Ð°Ð½Ñ‚Ð¸ Ð’Ð°Ñ€Ð½Ð°", GitHub Pages at
  `https://petar1984.github.io/Fire_Varna/`. 6,000+ hydrants, Leaflet +
  MarkerCluster + `data/hydrants.json`, Cloudflare Worker â†’ GitHub issues.

## 3. Confirmed architecture decisions

1. **Private pipeline â†’ public app.** Varna_buildings stays PRIVATE and
   build-time; it emits **curated, safe** outputs that feed Fire_Varna.
   Raw KAIS, intel, and personal data never cross to the public side.
2. **Host = Fire_Varna Pages.** All user-facing functionality lives in the
   public app.
3. **Mobile-first, light payload.** Heavy layers (`strategic_intel` ~34MB,
   `section_units` ~17MB, raw geocoder ~19MB) NEVER go to mobile.
4. **Config/data-driven editing.** Hydrants, building annotations, and the
   verification flow are editable without touching core app logic.

## 4. The "one repo" reframe (important)

The private/public split means they **cannot** be one git repo (a public
GitHub Pages repo cannot contain the private KAIS pipeline). So:

- **Two repos, clean split.** Varna_buildings (private pipeline) +
  Fire_Varna (public app).
- **Your day-to-day "one repo to debug/edit" is Fire_Varna** â€” it holds
  everything user-facing (map, hydrants, building display, search,
  verification config, data). You rarely touch the pipeline; it just
  regenerates building data from KAIS.
- **"Merge" = integrate capabilities + a curated data handoff**, NOT a
  git-history merge.

## 5. Two constraints to design around

- **Mobile weight.** Core GPS â†’ nearest-hydrant needs **nothing** from
  buildings (just `hydrants.json`, already on device, offline). Address
  search needs a geocoder: either a **slim on-device index** (address-tier,
  `{text, lat, lng}` only â†’ under 1MB gzip, lazy-loaded + service-worker
  cached â†’ offline search) or a **Worker-side geocoder** (ultra-light, needs
  signal to search). Likely: slim on-device default, Worker as fallback.
- **Public/private boundary.** The pipeline publishes ONLY the safe subset
  (no raw KAIS, no personal data, KAIS-license-clean). A **publish gate**
  defines what is safe to cross to the public app.

## 6. Mobile-lightness strategy

- Core (offline): `hydrants.json` + GPS â†’ nearest, MarkerCluster for 6k
  points (already exists).
- Address search: slim geocoder (<1MB gzip, lazy, SW-cached) or Worker.
- Footprints: optional â€” simplified / viewport-only / lazy.
- Service worker: offline cache + fast repeat boot; hydrants-first boot.

## 7. Config / data-driven layers (edit without code)

- **Hydrants:** curated dataset + the existing ðŸš¨ â†’ Worker â†’ GitHub flow
  (extend for add/edit).
- **Buildings:** an **override/annotation layer** (name / status / note) on
  top of pipeline-derived data; editable file or UI â†’ Worker â†’ GitHub; the
  pipeline regenerates under it and overrides persist. (Buildings are
  derived from KAIS â€” you cannot edit them like hydrants; you annotate via
  overrides, a pattern the pipeline already uses with sidecars.)
- **Verification:** a `verification_config.json` defining form fields,
  statuses, labels, and colors/icons; the app renders verification FROM it.
  Edit the config â†’ change the verification flow and look, no app-logic
  touch. Theming via CSS variables for visual changes; a ground-up layout
  redesign still touches the HTML/CSS template (but not the core logic).

## 8. Verification (field)

- **All-hydrants view:** every hydrant status-coded (verified / reported /
  unverified / canonical), MarkerCluster, on the map. Extends the existing
  "Ð’ÑÐ¸Ñ‡ÐºÐ¸" mode. No extra payload â€” data is already on device.
- **Config-driven design** (section 7).
- **Preserve** the existing ðŸš¨ â†’ Worker â†’ GitHub-issue flow.

## 9. Phasing (non-breaking, incremental)

- **Phase 0 â€” Architecture cycle.** ADR (amend ADR 020 / new ADR);
  reconcile both repos' governance; define the curated-bundle contract +
  the publish gate.
- **Phase 1 â€” Pipeline emits the curated mobile bundle** (slim geocoder +
  footprint subset, safe). Varna_buildings user-facing unchanged.
- **Phase 2 â€” Fire_Varna consumes the bundle:** building display + address
  search in the app. Both apps still work.
- **Phase 3 â€” All-hydrants verification view + `verification_config`** (config-driven).
- **Phase 4 â€” Building override/annotation edit layer.**
- **Phase 5 â€” Mobile optimization pass** (SW cache, lazy-load, payload
  budget, field testing on a phone).

Each phase must not break the prior one; verify both apps after each.

## 10. Open decisions for the cycle

- Slim on-device geocoder vs Worker geocoder (offline search vs
  ultra-light) â€” likely both.
- The exact curated-bundle contract (fields, footprint detail level, and the
  publish-gate / safe-subset definition).
- Governance reconciliation (one combined AGENTS/CLAUDE across both repos,
  or per-repo with a shared integration ADR).

## 11. Governance

- Gated Phase 2 reintegration (`architecture_v2.md`: deferred, ADR 020
  amendment required).
- Both repos share the tri-agent workflow (chat-Claude architect / Codex
  planner / Claude Code executor / Petar signs + pushes).
- Don't break anything; never push (Petar pushes); no personal data on the
  public side; BGS2005 â†” WGS84 discipline (hydrants are already WGS84).

## 12. Setup for the new Cowork project

1. Clone the public app locally next to the pipeline:
   `git clone https://github.com/Petar1984/Fire_Varna.git C:\git\Fire_Varna`
2. New Cowork project â†’ **select the parent folder `C:\git\`** so both
   `Varna_buildings` and `Fire_Varna` are accessible as files.
3. Make sure this framing doc is reachable (it lives in
   `Varna_buildings/scratch/`, so it is under the selected parent).
4. First action in the new session: chat-Claude reads this + both repos â†’
   frames the integration ADR â†’ runs the tri-agent cycle, phased per
   section 9.

Path  
----  
C:\git



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; Get-Content -Encoding UTF8 -LiteralPath 'AGENTS.md'; Get-Content -Encoding UTF8 -LiteralPath 'CLAUDE.md'; git -c core.quotePath=false status --short --branch; git log -6 --oneline" in C:\git\Fire_Varna
 succeeded in 52ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## main...origin/main [ahead 48, behind 2]
?? scratch/places_search/cleanup_brief_astra.md
?? scratch/places_search/cleanup_brief_kimi.md
?? scratch/places_search/golden_brief_kimi.md
?? scratch/places_search/golden_brief_sol.md
?? scratch/places_search/granitsi_brief_astra.md
?? scratch/places_search/granitsi_brief_kimi.md
?? scratch/places_search/granitsi_night_astra_S22_review_07.09.md
?? scratch/places_search/granitsi_night_kimi_K23_review_07.09.md
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
c6c5d44 docs: night-shift report 07.09
a454b60 measure: pin night-shift inputs, base_rev and ignore proofs (06.09)
57ab8eb gitignore: protect raw АГКК responses and any GeoJSON under scratch/places_search from ever being tracked (root cause of the red Н0 gate; architect fix outside the lot write-set, recorded)
65a0c7a docs: night-shift report 07.09
093b259 tests: five S17 fixtures against today's frozen behaviour
d862834 docs(plan): night plan v2 SIGNED by Petar (A + Б0 1–12 per recommendations; post-execution review by architect, Kimi and Astra as lot Б5); signed body sha recorded

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; Get-Content -Encoding UTF8 -LiteralPath 'AGENTS.md'; Get-Content -Encoding UTF8 -LiteralPath 'CLAUDE.md'; git -c core.quotePath=false status --short --branch; git log -9 --oneline" in C:\git\varna_3d
 succeeded in 41ms:
## rezhimi...origin/rezhimi [ahead 47]
A  data/quarters_signed.geojson
 M scratch/place_bodies/qa_place_bodies.md
?? docs/sessions/ПРОМПТ_20.08.md
?? scratch/refactor/_addr/_measure_pal13.py
?? scratch/refactor/_addr/_measure_tu_campus.py
?? scratch/refactor/_addr/f0b_join_375.json
?? scratch/refactor/_addr/f0b_join_375_pass2.json
?? scratch/refactor/_addr/kimi_атака_имена_бунгала.txt
?? scratch/refactor/_addr/kimi_атака_планове.txt
?? scratch/refactor/_addr/kimi_атака_смяна2.txt
?? scratch/refactor/_addr/osm_poi_varna.md
?? scratch/refactor/_addr/post_codes_all_2018.pdf
?? scratch/refactor/_addr/post_codes_varna_2018.json
?? scratch/refactor/_addr/БОРД_противоречия.md
?? scratch/refactor/_addr/БОРД_част_от_сграда.md
?? scratch/refactor/_addr/МЯРКА_курорти_повторно.md
?? scratch/refactor/_addr/МЯРКА_хотели.md
?? scratch/refactor/_addr/ОТЧЕТ_A1_05.09.md
?? scratch/refactor/_addr/ОТЧЕТ_P7_05.09.md
?? scratch/refactor/_addr/ОТЧЕТ_P7e_05.09.md
?? scratch/refactor/_addr/ПОДГОТОВКА_адреси.md
?? scratch/refactor/_addr/РАЗСЛЕДВАНЕ_адрес.md
?? scratch/refactor/_addr/СВЕРКА_живата_карта.md
?? scratch/refactor/_addr/Т7_недовършено_19.08.patch
?? scratch/refactor/_pubbldg/func/extras_log.txt
?? scratch/refactor/_pubbldg/func/run_log.txt
?? scratch/refactor/_pubbldg/join/check_log.txt
?? scratch/refactor/_pubbldg/join/extras_log.txt
?? scratch/refactor/_pubbldg/join/run_log.txt
?? scratch/refactor/_pubbldg/join/sample.json
?? scratch/refactor/_pubbldg/plan/kimi_plan_stderr.log
?? scratch/refactor/_pubbldg/plan/sol_plan_stderr.log
?? scratch/refactor/_pubbldg/plots/plots_by_class.json
?? scratch/refactor/_pubbldg/plots/plots_pooled.json
?? scratch/refactor/_pubbldg/plots/run_log.txt
?? scratch/refactor/_pubbldg/sources/check_log.txt
?? scratch/refactor/_pubbldg/sources/measure_osm_log.txt
?? scratch/refactor/_pubbldg/sources/measure_outside_log.txt
?? scratch/refactor/_pubbldg/sources/measure_sources_log.txt
?? scratch/refactor/_pubbldg/sources/name_channels.json
?? scratch/refactor/_pubbldg/sources/osm_named_features.json
?? scratch/refactor/_pubbldg/verify/kimi_stderr.log
?? scratch/refactor/_pubbldg/verify/sol_stderr.log
791b0cb gates: qa_quarters_signed with negative fixtures
2800a7c build: assemble quarters_signed.geojson from decisions 3 (sha ec2813e1c074) with D1 schema for imported geometry
5e468a1 measure: KAIS quar vs candidate polygons, read-only
524fe31 measure: polygon-vs-written quarter, ledger untouched
fb59f8d measure: derive place coordinates read-only, no identity mutation
0fed1e0 measure: candidate quarter geometry from pinned decisions (no signed artifact)
8d60aeb места: qa_fire_varna_export (хотелите) научава М2 — map_label:false не е DROP (A.1)
e902004 места: qa_fire_varna_places_export научава М2 — map_label:false не е DROP (P7-е)
e613089 места: износ след М2+М3+М6 и манифест BASE→P7 с покритие, pending и allow-списък за подпис (P7-д)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -Encoding UTF8 -LiteralPath 'C:\\git\\Fire_Varna\\docs\\plans\\ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'; Get-Content -Encoding UTF8 -LiteralPath 'C:\\git\\Fire_Varna\\docs\\audits\\ДОКЛАД_07.09_нощна_смяна.md'" in C:\git
 succeeded in 0ms:
# ПЛАН НОЩНА СМЯНА · Границите (06→07.09.2026) — v2 за подпис (след Кими К22 и Astra S21)

**Клас: 🔴 Архитектурен. Статус: ПОДПИСАН от Петър (06.09.2026, вечерта; част А и част Б с блок Б0 т. 1–12 по препоръките).** Думите му: „подписвам и след изпълнението искам ти, кими и астра да прегледате изпълнението от различни ъгли“. Подписаното тяло: v2, sha256 на blob-а в комит 42b2635 = `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766`. Следизпълнителен преглед: архитект (Fable, дифът), Кими (данни/лиценз), Astra (механика) — записано като лот Б5. Топология: планировчик → три вътрешни оборвания (Opus) → Кими + Astra → подпис → изпълнител → независим одитор на всеки лот → Петър.

**Строеж на плана.** **ЧАСТ А** (лотове Н0–Н5) е нощ от **мерки** — тръгва при подпис на плана и не иска нито едно ново решение; така е след трите вътрешни оборвания (D1 е затворен набор от 21 полета; D2 заключва метода „по улици“; D13 затворени публични набори; G17). **ЧАСТ Б** (лотове Б1–Б4) е нощ от **резултати** — подписан файл с граници, присвояване на квартал, търсене по квартал — и тръгва САМО ако Петър подпише тази вечер и **блока решения Б0** (§6), защото всяко от тях е негово по ADR 010 и амандамент №2. Ако Б0 не е подписан, нощта е само А. Ако Б0 е подписан, А се изпълнява първа (числата ѝ де-рискуват Б), после Б.

**Принципът на Петър за данните (06.09, вечерта):** „дори имената на адресите да лъжат — геокоординатите не лъжат“. Кварталът на място се определя от координатата му спрямо потвърдените полигони; адресните низове са свидетели, не съдии; спор (записан ≠ полигон) е ред в леджер, никога презапис. Раздел §7 „Конфликти и нормализация“ прави от това мярка.

**Водещата промяна спрямо чернова 1:** тази нощ НЕ се ражда канонична подписана геометрия. Нощта произвежда **мерки и кандидати** — никой файл не се казва `quarters_signed.geojson` и никой не твърди „подписано“. Причината е измерена: D1 (`docs/decisions/010_signed_quarter_boundaries.md:38`) е ЗАТВОРЕН набор от 21 полета с „липсващо поле = STOP“, а внесен уикимапийски полигон няма `drawn_by/drawn_at/basemap/viewport/screenshot_sha256/approval_digest/witnesses`. Схемата за ВНЕСЕНА геометрия е амандамент за подпис, не решение на изпълнител.

## 0 · Червени редове (важат за всеки лот, без изключение)

1. **Агентите не пушат.** Никога, с никакъв флаг, без `--no-verify`.
2. **Нула геометрия в проследен файл на Fire_Varna.** Публично пътуват само име, код и картата за атрибуция.
3. **`Varna_buildings/config/quarter_registry.json` не се пипа.** Ваялар→alias, Евксиноград/Траката, Цветен квартал, 16-те без решение, липсващите `parents` — всичко отива в сутрешния списък (§5).
4. **Написан квартал не се променя** (D18/G17). Спорът е ред в леджера, не редакция.
5. **Малки, обратими комити**, изчерпателен write-set, дословно съобщение, автор `Claude Executor <executor@local>`; подписаната геометрия и решенията чакат комит на `Petar1984` (D16, G4 е fail-closed).
6. **Всеки гейт е команда с изход ≠ 0 и с отрицателна фикстура, която ТРЯБВА да падне.** Паднал гейт СПИРА лота; нощта продължава само с лотовете, които не зависят от него.
7. **Само Opus** — изпълнители и одитори; всеки `agent()` с `model: "opus"`.
8. **Одиторът е друг агент** (read-only) за всеки лот. Самопотвърждение не е доказателство.

**Две обявени отклонения (искат подпис заедно с плана):** (а) `ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md §0.1` иска един лот в движение до пуш — измерено: Fire_Varna 37 ahead, varna_3d 41, Varna_buildings 1; нощта отваря шест лота в три репа, всичките мерки. (б) `§0.3` иска Kimi и Astra преди изпълнение — този план минава през Astra преди първия ред код; при недостъпност нощта се свива до Н0 и Н4.

## 1 · Мярка преди плана (прочетено тази вечер, read-only)

- `granitsi_decisions_3_2026-09-06_proba.json`: 68 реда, `choice` = wikimapia 60 · deferred 6 · declared_streets 1 · alias_of 1. Ключове на реда: code, display, kind, choice, wm_id, wm_polygon_sha256, wm_title, reason, decided_by, decided_at. **`precision_m` — 0/68.** Договорът в амандамент №2 §4 не познава `declared_streets` и `alias_of` → G26 се разширява (обявено отклонение).
- Файлът е **ПРОСЛЕДЕН И КОМИТНАТ ОТ АГЕНТ**: `b6e627d`, автор `Claude Architect`. Значи състоянието не е „некомитнат“, а `agent_committed_proba` — амандамент №2 §4 иска блоб, комитнат от Петър.
- `wm_polygon_sha256` в решенията е **СУРОВ** хеш на компактния `{"type","coordinates"}`, не канонизацията по D1 (6 знака, CCW, ротация, подредба по площ). Мерено: `abatko` = `c2e0662d…`, `mladost2` = `80f40ee1…`.
- `agkk_au5_varna.geojson`: 5 Feature-а **без `properties`**; ключове `nationalcode` ("10135-01"…"10135-05"), `upper`, `area_km2`, `n_places`, `district_codes_inside`. **Словесен код на район в този файл НЯМА.** Словесните са `index.html:6315` (`DISTRICT_CODES`).
- `index.html:6313` `QUARTER_SRC`, `:6317-6321` `QUARTER_CODES` = **затворен списък от 20 кода**; **41 от 61-те потвърдени кода ги няма** в него, а `morska_gradina`, `sveti_nikola`, `zelenika` са в `LOCALITY_CODES` (`:6322`) — друг клас. Непознат код умира мълчаливо по същия път като непознат `src`.
- `varna_3d/src/fire_varna_locations.py:76`: `LEDGER = scratch/refactor/_addr/lot1v_locations_375.json` — **проследен**; той е базата на G17. Всеки прогон на канала го презаписва.
- `_meta.base_rev` **не съществува** в днешния леджер, а D18/G17 (`ADR:72,:131`) четат `git show <base_rev>:…`. Променливата е недефинирана.
- `varna_3d/.gitignore:4` `data/*`, `:23` `*.geojson` → `data/place_identity.json` е игнориран; `place_identity.py:602` чете предишния файл, `:1261` го презаписва — това е СЪСТОЯНИЕ, не производна.
- `web/varna_buildings_info.json` е таблица без геометрия; телата са `web/varna_buildings_3d.geojson` (29.9 MB).
- Вложеност между 60-те полигона: **10 вложени двойки, 7 НЕДЕКЛАРИРАНИ** (rozova_dolina⊂asparuhovo, kokardzha_generic⊂izgrev_kv, abatko⊂kk_konstantin_elena, saltanat⊂morska_gradina, vazrazhdane1/2/3⊂vazrazhdane). `parents` в регистъра са **дисплей-низове** и има само 6; `borovets` няма потвърден полигон.
- `varna_3d` = PRIVATE (`gh` не е в PATH; работи с `C:\Program Files\GitHub CLI\gh.exe`). `ФАЗА_0_лицензи.md:4` = „⏳ чака подпис“ → G21 държи заключено.
- Шестте фикстури S17 ги няма в `Fire_Varna/tests/`; днешният набор е 310 теста, зелен.

## 2 · Лотовете

| Лот | Репо | Изчерпателен write-set | Дословно съобщение | Откат |
|---|---|---|---|---|
| Н0 пинове | Fire_Varna | `scratch/places_search/noshtna_pins_06.09.json`, `scratch/places_search/qa_night_pins.py` | `measure: pin night-shift inputs, base_rev and ignore proofs (06.09)` | `git revert <sha>` |
| Н1 кандидат | varna_3d | `src/build_quarters_candidate.py`, `src/qa_quarters_candidate.py` (изходът `scratch/granitsi/quarters_candidate_07.09.geojson` е игнориран по `.gitignore:23` и НЕ се стейджва) | `measure: candidate quarter geometry from pinned decisions (no signed artifact)` | `git revert <sha>` + изтриване на изхода по назован път |
| Н2-0 координати | varna_3d | `src/measure_place_coords.py` (изход `scratch/granitsi/place_coords_07.09.json`, непроследен) | `measure: derive place coordinates read-only, no identity mutation` | същото |
| Н2 присвояване | varna_3d | `src/measure_polygon_assign.py` (изход `scratch/granitsi/assign_measure_07.09.json`) | `measure: polygon-vs-written quarter, ledger untouched` | същото |
| Н3-а фикстури | Fire_Varna | `tests/test_granitsi_fixtures.py`, `scratch/places_search/granitsi_fixtures_06.09.json` | `tests: five S17 fixtures against today's frozen behaviour` | `git revert <sha>` |
| Н4 сгради | varna_3d | `src/measure_kais_quar_vs_polygons.py` | `measure: KAIS quar vs candidate polygons, read-only` | `git revert <sha>` |
| Н5 доклад | Fire_Varna | `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` | `docs: night-shift report 07.09` | `git revert <sha>` |

Зависимости: Н0 → всичко. Н1 → Н2, Н4. Н2-0 → Н2. Н3-а е независим. Пада ли Н1 — Н2 и Н4 отпадат, Н3-а и Н5 продължават.


### 2а · Договори на скриптовете (Astra S21 т. 1: „липсващ бъдещ скрипт е допустим deliverable, но с подписан интерфейс, точна команда, exit code и фикстура“)
| скрипт (нов, в write-set-а на лота) | команда (от корена на репото) | exit 0 означава | отрицателна фикстура (трябва да даде exit ≠ 0) |
|---|---|---|---|
| `scratch/places_search/qa_night_pins.py` (Fire_Varna) | `python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json` | всеки sha256 в пиновете е преизчислен и равен; `git check-ignore` за всеки геометричен път = игнориран; `git ls-files scratch/boundary_gallery` = 0; `base_rev` = записаният HEAD | `--pins <копие с един обърнат hex знак>` → ≠ 0; `--worktree-negative` (еднократно worktree с `git add -f` на копие на geometry-файл) → гейтът за G29 там ≠ 0 |
| `src/build_quarters_candidate.py` (varna_3d) | `python src/build_quarters_candidate.py --decisions <път> --frozen <път> --extra <път> --out scratch/granitsi/quarters_candidate_07.09.geojson` | файлът е написан, `_meta.artifact_class == "candidate_not_signed"`, две последователни сглобявания са байт-еднакви | `--decisions <файл с координата в ред>` → ≠ 0; `--frozen <файл с подменен връх>` → ≠ 0 |
| `src/qa_quarters_candidate.py` (varna_3d) | `python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --registry <път> --decisions <път>` | всички проверки от Н1 минават; 16-те `registry_pending` са ИЗКЛЮЧЕНИЕТО, формализирано: код без решение е ✗ САМО ако не е в `_meta.registry_pending` (списъкът е затворен и се сверява срещу решенията) | `tests/fixtures/qa_quarters_candidate/*.geojson` — по една фикстура на проверка (подменен `wm_id`, `declared_local_knowledge`, голо „CC BY-SA“, две кода–една геометрия, `artifact_class` друг, код извън `registry_pending` без ред) → всяка ≠ 0 |
| `src/measure_place_coords.py` (varna_3d) | `python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json` | 375 реда; всяка координата в 43.13–43.35 / 27.65–28.10; `sha256(data/place_identity.json)` преди == след (проверява се в скрипта и се печата) | `--bodies <файл с тяло извън кутията>` → ≠ 0; `--identity <файл без place_id>` → ≠ 0 |
| `src/measure_polygon_assign.py` (varna_3d) | `python src/measure_polygon_assign.py --base-rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b --polygons <кандидат> --coords <place_coords> --parents <DAG от Б0 т. 12> --out scratch/granitsi/assign_measure_07.09.json` | чете леджера през `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`; sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` преди == след; `git status --porcelain` без нови проследени промени извън write-set-а | `--polygons <кандидат с една координата, преместена в чужд квартал>` → числата се променят и `--expect <предишен изход>` дава ≠ 0; `--base-rev <несъществуващ>` → ≠ 0 |
| `tests/test_granitsi_fixtures.py` (Fire_Varna) | `python -m unittest tests.test_granitsi_fixtures` | петте фикстури минават върху днешното поведение | всяка фикстура има `_broken` вариант в `scratch/places_search/granitsi_fixtures_06.09.json`, който тестът пуска и очаква да ПАДНЕ (assertRaises); липсващ `_broken` = тестът е червен |
| `src/measure_kais_quar_vs_polygons.py` (varna_3d) | `python src/measure_kais_quar_vs_polygons.py --info web/varna_buildings_info.json --bodies web/varna_buildings_3d.geojson --polygons <кандидат>` | таблица на stdout (съвпада / не / няма полигон / само район), нула кадастрални идентификатори и координати; sha256-манифест на `data/` и `web/` преди == след | `python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py` (нов, в write-set-а на Н4): AST-обход за `open(...,'w')`, `Path.open`, `json.dump`, `shutil.*`, `os.replace/remove`, `subprocess` → ≠ 0; фикстура `tests/fixtures/readonly_ast_negative.py` с `json.dump` → ≠ 0 |
| Н5 (одит) | `python scratch/places_search/qa_night_acceptance.py --report docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna, в write-set-а на Н5) | всеки лот в доклада има: sha-та на write-set-а, exit кодовете на гейта и на всяка отрицателна фикстура (≠ 0), авторът на комита, съобщението дословно | доклад без ред за някой лот или с гейт без падаща фикстура → ≠ 0 |

**Базова ревизия (Astra S21 т. 2):** `base_rev` = **пълният HEAD на varna_3d, замразен в Н0 преди всяка промяна** — измерено сега `8d60aebb365fb8e74ccc863d3b3db90b74180a3b` (клон `rezhimi`); Н0 го записва в пиновете и проверява, че леджер-блобът и двата износа съвпадат с приетата основа; **не** се взима последният леджер-комит (`31db7b9…` — леджерът там е същият, но износите се различават). QA и манифестът (`qa_fire_varna_m6.py:48`, `lot1v_v_manifest.py:30`) четат стария леджер по константа — при Б2 кандидатът и основата се подават като изрични входове, не чрез смяна на константата. Н0 записва и **мръсния проследен диф във varna_3d** (1 файл сега) като част от основата; „празен `git status`“ не е гейт — гейтът е „нищо ново извън write-set-а“.

**G19 команда (Windows):** `& "C:\Program Files\GitHub CLI\gh.exe" repo view Petar1984/varna_3d --json visibility` → `{"visibility":"PRIVATE"}`; друго или празно = СТОП за целия varna_3d фронт.

## 3 · Лот по лот

### Н0 · Предусловия и пинове
`noshtna_pins_06.09.json` (нула координати) пинва `sha256` на: решенията (**плюс комита `b6e627d` и автора `Claude Architect`**), `frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson` (`b53a3322…`) **и** `granitsi_preview_05.09/wikimapia_quarters_frozen_2026-09-06_v2.geojson` — двете копия са байт-еднакви, **веригата се доказва по sha, не по име**; суровия снапшот; `m2_1_candidates_v2.json` (`1331130e…`, обявен вход на решенията); `wikimapia_extra_2026-09-06.geojson` (Евксиноград 5729429, **извън обявения frozen манифест** — записва се изрично); `mladost2_streets_proposal.geojson`; `agkk_au5_varna.geojson`; `quarter_registry.json`; `lot1v_locations_375.json`; **`base_rev` = точният комит, от който се чете леджер-блобът**. Записва се и, че `based_on` предшественикът `granitsi_decisions_2_…` липсва на диска — веригата назад е скъсана (ред в доклада, не мълчание). Плюс `git rev-list --count origin/…` за трите репа и **G19**: `"C:\Program Files\GitHub CLI\gh.exe" repo view varna_3d --json visibility` → трябва `PRIVATE`; празен изход или `PUBLIC` = СТОП за целия varna_3d фронт.

**Гейт Н0 (червен).** `qa_night_pins.py` преизчислява всеки sha и повтаря git-проверките. Фикстури: обърнат hex знак → ≠ 0; **`git add -f` върху копие на geometry-файл в еднократно worktree → гейтът за G29 трябва да падне ТАМ и да е зелен в реалното дърво** (`git add -n` е dry-run и не доказва нищо); подменено ИМЕ при съвпадащ sha → зелено, подменен sha → червено.

### Н1 · Кандидат-геометрия (varna_3d, частно, НЕподписано)
Един Feature на **уикимапийски** потвърден код: **60 кода** (59 + Евксиноград). **Младост 2 НЕ влиза** — D2 (`ADR:40`) казва „по улици“ → ЗАКЛЮЧЕН ВИНАГИ, отключва се само с изричен подписан ключ, а G1 има точно тази отрицателна фикстура; излиза като `deferred` и поименно в §5. Полета: `code`, `name`, `kind`, `source: "wikimapia"`, `wm_id`, **`raw_geometry_sha256`** (пренесен от решенията) **и** `wm_polygon_sha256_d1` (пресметнат по канонизацията на D1) — двете правила се записват отделно, разликата е обявено отклонение за Петър; `url`, `fetched_at`, `confirmed_by/at`, `chosen_reason`; **`licence` дословно** по амандамент №2 §3.8 и К21 т. 3–4: `"CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)"` + етикета за доброволци/неофициален извор/URL на условията/дата; `attribution` низът; `parent` от регистъра след **явна стъпка дисплей→код с гейт** (непознат дисплей = червено), а за код с родител без полигон (`borovets_sever`, `borovets_yug`) — `parent_geometry_check: "няма родителски полигон"`. **`precision_m` НЕ се измисля** (0/68 в решенията) — Feature-ът носи `precision_m: null` и лотът не го замества с литерал. **`district` НЕ се пише** (виж §5 т. 4); вместо това мярка: за всеки кандидат кой `nationalcode` го съдържа. `_meta`: `artifact_class: "candidate_not_signed"`, `decisions_state: "agent_committed_proba (b6e627d, Claude Architect)"`, манифест на входовете, `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict, position}`, `registry_pending` с **16-те кода без решение поименно**.

**Гейт Н1 (червен).** Предгейтове: **G19** (частно репо), **G3** (`qa_no_cad_ids.py` — задължителен преди всеки комит по CLAUDE.md на varna_3d). Фикстури: подменен връх при непроменен sha (за ВСЕКИ от двата хеш-ключа поотделно, всеки срещу своя източник) · подменен `wm_id` · `deferred` код с Feature и Feature без ред · **жилищен код от регистъра без ред в решенията → ✗, поименно** · координата във файла с решения · липсващ ред за атрибуция · **не-уикимапийски ред с непразно `wm_*` → ✗** · **входен Feature със `source: "declared_local_knowledge"` → ✗** (етикетът е отменен от амандамент №2 §3.7) · голо „CC BY-SA“ или липсващ `terms` → ✗ · една геометрия към два несравними кода · BOM/CRLF/несортирани ключове · две сглобявания дават байт-еднакъв файл · **`_meta.artifact_class ≠ "candidate_not_signed"` → ✗**.

### Н2-0 · Координати — МЯРКА, без мутация
`place_identity.json` **не се докосва** (игнориран, състояние, генераторът чете сам себе си). Отделен скрипт извежда `place_id → lat/lon` от същите връзки, които идентичността вече носи (`site_id`/`kais_i` → представителна точка на тяло в `web/varna_buildings_3d.geojson`), и пише САМО в `scratch/granitsi/place_coords_07.09.json`. Място без връзка → `no_coord`, брои се, не се гади. **Гейт:** 375 реда; всяка координата в кутията 43.13–43.35 / 27.65–28.10; sha256 на `data/place_identity.json` идентичен преди и след. Фикстури: координата извън кутията → ✗; липсващ `place_id` → ✗.

### Н2 · Присвояване — САМО ЧИСЛА, нула запис
Скриптът чете **блоба** `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json` (не работния файл), кандидат-полигоните и координатите, и брои. `fire_varna_locations.py` **не се редактира**; леджерът **не се презаписва**. Правила на мярката: празен квартал + точно един полигон → „би получил“; **място в ≥ 2 полигона БЕЗ декларирано родство → `disputed`** (7-те недекларирани вложености); „най-малкият печели, детето преди родителя“ важи САМО за 6-те декларирани двойки; написан ≠ полигон → `disputed`; **няма полигон → редът си остава с вече написания район** (нищо не се извежда от АГКК); ръбът се брои в **три ленти 50/100/250 m** и трите числа влизат в доклада, докато Петър не подпише `precision_m`. **Гейт:** sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` **идентични преди и след**; `git status --porcelain` в varna_3d празен извън write-set-а.

**Десетият ключ на `_meta` НЕ се специфицира и НЕ се пуска.** Причина: подписваният източник го нарича с ДВЕ имена — амандамент №2 §3.3 (`licence_quarter_boundary`) и §5/G27 (`quarter_attribution`), а фикстурата на G27 отхвърля `_meta` с 11 ключа. Едното трябва да умре с думата на Петър (§5 т. 5).

### Н3-а · Фикстури (Fire_Varna) — днешното поведение, не приемане
Пет фикстури: `street_collision`, `district_retention`, `mladost_kind_collision`, `order_identity`, **`parent_child` върху двойка с ДНЕС регистрирано родство** (`mladost`/`mladost2`) — версията с Възраждане се отлага, защото vazrazhdane1..4 нямат `parents`. **`client_cache_matrix` се отлага** с назована причина: браузърно поведение, а единственият node-изпълнител в `tests/` е `test_data_ascii_mojibake.py`; лотът не назовава втори. Всяка фикстура пада върху нарочно счупен кандидат и мутацията влиза дословно в доклада. **Гейт:** `python -m unittest discover -s tests` (310+ зелени) И `python -m gates.run_gates` без червено — иначе сутрешният пуш на Петър е блокиран от собствената му кука. Записва се изрично: **това фиксира ДНЕШНОТО поведение; утре F13 ще ги направи кандидат-очаквания, не приемане.**

**Н3-б СПИРА (нарочно).** Търсенето по квартал и редът за атрибуция в картончето не тръгват: нов `src` или нов код без подредената тройка на D13 изхвърля 150 места мълчаливо, а измереното е по-лошо от очакваното — **41 кода липсват в `QUARTER_CODES`**, три от тях са днес местности.

### Н4 · Сградите — САМО мярка
Вход: `web/varna_buildings_info.json` (речниково кодирана колона `quar`, `build_places.py:78-96`) + **`web/varna_buildings_3d.geojson`** (телата, поименно) + кандидат-полигоните. За всяка сграда с непразен `quar`: съвпада / не съвпада / няма полигон / само район. Изход: **stdout**; нула кадастрални идентификатори, нула координати. **Гейт (червен):** AST-проверка за извикване на пишеща функция (не grep — `json.dump(obj, fp)`, `Path.open("w")`, `shutil.copy` минават през списък от низове), с фикстура-вариант, който пише през `json.dump` → ✗; плюс sha256-манифест на **всичко под `data/` и `web/`** преди и след и `git status --porcelain` празен.

### Н5 · Одит и доклад
Одитор (Opus, read-only, различен агент) на всеки лот: преизпълнява гейтовете, сверява дифа срещу write-set-а (**всеки допълнителен файл = находка**), проверява автора, съобщението и `git log --format=%an -1 --` върху пътя на решенията срещу `_meta`. **Разделение:** одиторът дава числата, изпълнителят ги записва без да ги тълкува. Докладът носи: числата на Н1, Н2 (по трите ленти), Н3-а (5/5 + доказаните падания + двете отложени), Н4, всички sha, поименния списък на спрелите лотове с причината, и §„Какво прави Петър сутринта“.

**Атрибуция в проследените артефакти:** всеки нощен проследен файл на Fire_Varna, който назовава уикимапийски обект, носи ред за атрибуция по §3.8 (ключ `attribution` в JSON, заглавен ред в MD) — ToS §1.G важи и когато github.com рендерира файла в браузър. Вече комитнатият `granitsi_decisions_3_…json` (60 `wm_id` + заглавия) няма такъв ред: **това е сутрешен дълг, не нощна поправка.**

## 4 · Нарушения, които спират нощта веднага

Опит за `git push` · геометрия в проследен файл на Fire_Varna · редакция на регистъра · промяна на написан квартал · запис в `lot1v_locations_375.json`, `place_identity.json` или `data/fire_varna_*.json` · файл на име `quarters_signed.geojson` · Feature по метод „по улици“ · нов публичен `src` **или нов квартален КОД** без разширен `QUARTER_CODES` и подредената тройка на D13 · низът `10135` в **публична** доставка (в частния провенанс и в мярката е позволен — иначе АГКК изворът е неназовим) · зелен гейт без падаща отрицателна фикстура.

## 5 · Сутринта (решенията за Петър, ако Б0 НЕ е подписан тази вечер)

1. **Схемата за ВНЕСЕНА геометрия** (кои от 21-те полета на D1 отпадат и с какво се заместват) — амандамент, без който няма подписан артефакт.
2. **Кое правило е `wm_polygon_sha256`** — суровият хеш (днешният в решенията) или канонизацията на D1.
3. **Младост 2**: подписан ключ по D2 + лиценз (ODbL, „© OpenStreetMap contributors“) + под на `precision_m` за уличен метод.
4. **Районът**: от нашия `district.code` (375/375 съгласие) с явен `district_src`, или от АГКК — тогава `_meta.source_terms["agkk_inspire_au5"]` се попълва и G22/G23 стават червени предгейтове.
5. **Едно име за десетия ключ** (`licence_quarter_boundary` или `quarter_attribution`) и низът за атрибуция; картата да е независима от извора `{code:{src,url,label,licence}}`, за да носи и ODbL, и АГКК.
6. **`precision_m`** — стойност и довод (от нея зависи кой е `edge_pending`).
7. **Разширяването на `QUARTER_CODES`** с 41-те кода и какво става с `morska_gradina`, `sveti_nikola`, `zelenika`, които днес са местности.
8. **Решенията**: `git mv` на днешния блоб под подписан път (не втори блоб с втора sha) или подпис на днешния път.
9. Регистърът: Ваялар→alias, Евксиноград/Траката, Цветен квартал, `parents` за Възраждане 1–4 и Розова долина, 16-те без решение.
10. Дългове: D10 твърди, че `_check_pins` (`:623-639`) сверява `inputs` — не ги сверява; `_meta.base_rev` липсва в леджера; `granitsi_decisions_3` няма ред за атрибуция.


## 6 · ЧАСТ Б — нощ от резултати (тръгва само с подписан блок Б0)

### Б0 · Блокът решения, който Петър подписва тази вечер (препоръките са на архитекта; всяко „да“ е негово)
1. **Схема за ВНЕСЕНА геометрия (промяна на D1, обявена).** За Feature с `source ∈ {wikimapia, declared_streets}` полетата `drawn_by · drawn_at · basemap · viewport · visible_layers · screenshot_sha256 · approval_digest` са `null` по договор (гейт за взаимна изключителност: или ръка, или внос); `approved_by = "Petar"`, `approved_at = decided_at` от решенията; `signed_by = "Petar"` става валидно с подписа на този план по sha на решенията (т. 8); `witnesses[]` = [{kind: "wikimapia_object", url, fetched_at, raw_response_sha256}] (за Младост 2: {kind: "osm_carriageways", ways по име, fetched: 2026-09-06}); `version: 1`; `note = reason`. Останалите 14 полета на D1 остават задължителни. **Делта спрямо амандамент №2 §4 (К22 П1):** §4 null-ва четири полета (`drawn_by/drawn_at/viewport/screenshot_sha256`); тук се добавят още три — `basemap`, `visible_layers` и `approval_digest`; дайджестът на D1 (връзката одобрение ↔ байтове) се замества от sha-веригата на т. 8 (решения по sha → Feature с `wm_polygon_sha256` → `_meta.decisions_sha256`). Препоръка: да.
2. **`wm_polygon_sha256` = канонизацията на D1** (6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; MultiPolygon по правилото на амандамент №2 §4). Суровият хеш от решенията се пренася като `raw_geometry_sha256` и гейтът сверява и двата. Препоръка: да.
3. **Младост 2 — изричен подписан ключ по D2** за `code = mladost2`, `method = "street_bounded_face"`, лиценз `"ODbL © OpenStreetMap contributors"` (осите), `precision_m = 50`, четирите улици дословно в `witnesses`. Само този код; всеки друг Feature с този метод = червено. Препоръка: да.
4. **Районът** се пише от НАШИЯ `district.code` на мястото (375/375 съгласие с АГКК, мерено 05.09), `district_src: "fire_varna_district"`; в Feature-ите на кварталите районът е изведен по представителна точка срещу същите наши 5 района, не от АГКК INSPIRE (G22 остава заключен). Резервата „място без квартал → районът“ пише `quarter = {name: <име на района>, code: <словесният код от DISTRICT_CODES>, src: "DISTRICT_FALLBACK"}` с три ограничения (К22 П3): (i) fallback-редовете **не са „написан квартал“** по D18/G17 — подписан полигон в бъдеща версия ги замества; (ii) място, което лежи в зона на код с `deferred`/`registry_pending` (16-те без решение, Ваялар, Младост 2 без ключа), **не получава fallback** — остава празно, поименно в леджера; (iii) място с `pin_outside_all` **или** чийто полигон противоречи на всеки наличен низов свидетел (кадастралният `quar` на тялото, адресният низ) отива в `disputed`, не се пише — координатата решава, но пин без нито един съгласен свидетел е подозрителен. Семантиката „quarter понякога е район“ е изрично „да“ тук, не само преизмерени пинове. Препоръка: да.
5. **Десетият ключ на `_meta` се казва `quarter_attribution`** (името в §3.3 на амандамент №2 отпада); форма `{<code>: {src, url, label, licence}}` — независима от извора, носи Wikimapia, ODbL и бъдещи; UI редът се **рендерира от `label` и `url` на записа**, никога от фиксиран низ (К22 П2): за Wikimapia — „квартал по Wikimapia.org · обектът“ (двете като връзки по ToS §1.G); за `mladost2` — записът `{src: "openstreetmap", url: "https://www.openstreetmap.org/copyright", label: "© OpenStreetMap contributors", licence: "ODbL"}` (ODbL §4.3); без запис в картата — нищо. Отрицателна фикстура: код със `src: openstreetmap`, показан с Wikimapia-низ → ✗. Препоръка: да.
6. **`precision_m`**: 100 за `wikimapia`, 50 за `street_bounded_face`; ръб = `max(50, precision_m)` по D7 → `edge_pending`. Препоръка: да.
7. **`QUARTER_CODES` се разширява** с 41-те потвърдени кода, които днес липсват; `morska_gradina`, `sveti_nikola`, `zelenika` остават в `LOCALITY_CODES` (търсят се като местности); `QUARTER_SRC` получава `SIGNED_POLYGON` и `DISTRICT_FALLBACK`; `PLACES_CACHE` v6→v7; пиновете и `expectations.json` — в подредената доставка varna_3d → Fire_Varna. Препоръка: да.
8. **Решенията**: Петър подписва `granitsi_decisions_3_2026-09-06_proba.json` **по sha256 на блоба в b6e627d** (`git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json | sha256sum`), с добавен от изпълнителя ред `attribution` (ToS §1.G) в СЪЩИЯ файл в нов комит, чийто sha той препотвърждава сутринта. Препоръка: да — това е Г2-б без нов блоб.
9. **Родството — подписан DAG (измерен 06.09 вечерта, ≥ 98 % от детето вътре в родителя): 11 двойки** — abatko ⊂ kk_konstantin_elena · druzhba ⊂ asparuhovo · rozova_dolina ⊂ asparuhovo · kaisieva ⊂ vladislavovo · kokardzha_generic ⊂ izgrev_kv · mladost1 ⊂ mladost · mladost2 ⊂ mladost · saltanat ⊂ morska_gradina · vazrazhdane1 ⊂ vazrazhdane · vazrazhdane2 ⊂ vazrazhdane · vazrazhdane3 ⊂ vazrazhdane. **Частични припокривания (5–98 % от по-малкия), които НЕ са родство:** vazrazhdane4/vazrazhdane 72 % · pz_planova/vladislavovo 61 % · grackata_mahala/tsentar 52 % · vinitsa_sever/dobreva 51 % · maksuda/sv_ivan_rilski 39 % — място в такава двойна зона е `disputed`. Правилото е **транзитивно** по DAG-а (A ⊂ B ⊂ C → A печели пред B и C) и се подписва като геометричен факт за присвояването, без да се пипа регистърът (`parents` там е сутрешен дълг). Препоръка: да.
10. **Ваялар** остава без граница тази нощ (`alias_of` → регистър сутринта); **Евксиноград** = 5729429 с бележката за конфликта на имена; **16-те без решение** → `deferred` в `_meta.registry_pending`. Препоръка: да.
11. **Координатите на местата (промяна на D7/D10, обявена; Astra S21 т. 3).** D7 забранява изнесените координати за присвояване (кръгово), а `place_identity.json` има 0/375 lat/lon. Източникът става **представителната точка на кадастралното тяло, към което идентичността вече сочи** (`site_id`/`kais_i` → `web/varna_buildings_3d.geojson`), записана в `place_identity.json` от генератора (`coord_src: "kais_body_representative_point"`, `coord_precision_m: 20`); място без връзка към тяло → `no_coord`, остава празно и поименно в леджера. Ходът: резервно копие на `data/place_identity.json` в `C:/Users/Petar/AppData/Local/Temp/claude/C--git/26f42576-326e-4863-b700-f1e02c26a0c9/scratchpad/backup_place_identity_2026-09-06.json` (+ sha256 в пиновете; възстановяване: копиране обратно + проверка на sha), генериране в `data/place_identity.candidate.json`, G9 върху кандидата (байт-дифът спрямо основата е само в `lat`/`lon`/`coord_src`/`coord_precision_m`; `place_id` непроменени), подмяна САМО при зелено. Без това „да“ Б2 не тръгва и остава мярка Н2. Препоръка: да — това е „координатите не лъжат“, направено проверимо: координатата идва от кадастъра, не от нашия износ.
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

`quarter_registry.json` · написаните 201 квартала · `lot1v_locations_375.json` · `place_identity.json` и `data/fire_varna_*.json` · `fire_varna_locations.py` и каналът `SIGNED_POLYGON` · `.gitignore` на varna_3d (разигнорирането чака комита на Петър по G4) · `index.html` (нито `QUARTER_SRC`, нито `QUARTER_CODES`, нито картончето, нито `PLACES_CACHE`) · `_meta` на износа и десетият ключ · Младост 2 като Feature · полето `district` в геометрията · `precision_m` като число · `origin` на което и да е от трите репа.
# ДОКЛАД · нощна смяна „Границите“ (06→07.09.2026)

**Атрибуция (Wikimapia ToS §1.G):** кварталните граници, за които става дума в този доклад, са изведени от данни на [Wikimapia.org](http://wikimapia.org); допълнителният обект, назован в мерките по-долу, е [wikimapia.org/5729429](http://wikimapia.org/5729429). Лиценз на извора: „CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)“. За `mladost2` изворът на осите е OpenStreetMap — „© OpenStreetMap contributors“, ODbL.

**План:** `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md`, ПОДПИСАН от Петър; sha256 на подписаното тяло = `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766` (блобът в `42b2635`).
**Лот на този доклад:** Н5. **Съобщение:** `docs: night-shift report 07.09`. Този доклад ЗАМЕСТВА версията от `65a0c7a`, която описваше по-ранно състояние (Н0 червен, 2 от 11 лота) и вече не е вярна.
**Разделение (план §3, Н5):** числата идват от ОДИТОРИТЕ; изпълнителят на Н5 ги записва, без да ги тълкува. Разминаване между изпълнител и одитор се печата с двете стойности и **[РАЗМИНАВАНЕ]**. Където до Н5 НЕ е стигнал одиторски запис, числото е измерено наново от изпълнителя на Н5 (read-only) и носи **[БЕЗ ОДИТОР]** — това е признание за липса на независима проверка, не оценка.

---

## 0 · Присъда

**Част А (Н0–Н5) е изпълнена: 7 от 7 лота ЗЕЛЕНИ, 6 комита.** Доставените одиторски присъди са **пет: Н0, Н1, Н2-0, Н2, Н3-а — всичките ГОДНО**, всяка с преизпълнени гейтове и собствени допълнителни отрицателни фикстури.

**Находка №1 на този доклад: ЦЯЛОСТНА одиторска присъда за нощта НЕ е доставена до Н5, както и одиторски запис за Н4 и за част Б.** Затова:
- числата на **Н4** тук са измерени наново от изпълнителя на Н5 с командите от договора §2а — **[БЕЗ ОДИТОР]**;
- **гейтът на Н5** е самопроверка на записа (машинна), не одит на нощта;
- преди Gate 2 Петър има основание да поиска одит на Н4 и на част Б (лот Б5 на плана: архитект, Кими, Astra).

**Твърдите ограничения ДЪРЖАТ — нула нарушения по шестте забрани на §4:** нула пуш (`origin` на трите репа е недокоснат) · нула геометрия в проследен файл на Fire_Varna от тази нощ · `quarter_registry.json` непокътнат (sha `7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6`, дифът празен) · нула променени написани квартала (леджерът е байт-равен на блоба при основата) · нула записи в леджера, `place_identity.json` и `data/fire_varna_*.json` · нула разминавания между изпълнителски и одиторски числа в доставените лотове.

**Броячи (измерени сега):** Fire_Varna 47 напред и 2 НАЗАД спрямо `origin/main` (сливането сутринта е на Петър; след комита на Н5 — 48 напред) · varna_3d 47 напред, 0 назад спрямо `origin/rezhimi` · Varna_buildings 1 напред, регистърът непроменен.

---

## 1 · Лотовете (машинно проверим запис)

Всеки блок се чете от `scratch/places_search/qa_night_acceptance.py`: гейтът преизчислява всяко sha256 от файла на диска, препрочита всеки комит, автор и съобщение от git, взима дословните съобщения и write-set-овете от подписания план и иска команда до всеки изходен код.

```лот
код: Н0
статус: ЗЕЛЕН
комит: a454b60e1f6ff4ca51f6aebd6a6c55e28a0cffb5
автор: Claude Executor <executor@local>
съобщение: measure: pin night-shift inputs, base_rev and ignore proofs (06.09)
файл: scratch/places_search/noshtna_pins_06.09.json = d187ecbe94dde3614215e84e6e9d06046e4c3154ff3594f7e24be2eb9d273376
файл: scratch/places_search/qa_night_pins.py = 3a813b0c74486e27c90bada7477e7a3e728f9c9fbc24f5ad7bd9ac151e51ab4e
гейт: 0 | договорен гейт §2а, 11 проверки, преизпълнен и СЛЕД комита | python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json
гейт: 0 | предгейт G19, varna_3d е PRIVATE | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
фикстура: 1 | обърнат един hex знак в пинатия sha на frozen v2 | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/pins_flipped_hex.json
фикстура: 3 | еднократно worktree с git add -f върху геометричен файл, реалното дърво остава чисто | python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json --worktree-negative
фикстура: 1 | одиторска, подменен base_rev | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_baserev.json
фикстура: 1 | одиторска, подменен HEAD на varna_3d | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_v3head.json
фикстура: 1 | одиторска, подменен sha на мръсния проследен файл | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_dirty.json
фикстура: 1 | одиторска, подменен блоб-sha на регистъра | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_blob.json
фикстура: 1 | одиторска, вкаран ключ с координати в пиновете | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_coords.json
фикстура: 1 | одиторска, пинат по-ранен HEAD, комит извън write-set-а | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_c7outside.json
фикстура: 1 | одиторска, сгрешен ahead на Varna_buildings | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_ahead.json
фикстура: 1 | одиторска, очаквана видимост PUBLIC | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_g19.json
проба: 0 | положителна, същият sha под ДРУГО име остава зелен | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/pins_name_swapped.json
проба: 0 | ОДИТОРСКИ ПРОПУСК, пинове с празен списък входове минават мълчаливо | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_empty_inputs.json
```

```лот
код: Н1
статус: ЗЕЛЕН
комит: 0fed1e0fafab387a33536414f94093f36af5e9db
автор: Claude Executor <executor@local>
съобщение: measure: candidate quarter geometry from pinned decisions (no signed artifact)
файл: src/build_quarters_candidate.py = 27fe228d9c56787b581994df07ba869e4ad7b9101ab399e6496262c7e8e36858
файл: src/qa_quarters_candidate.py = eaf8ec73f4151392118c36390df39471c357568f3162b8a333791ac77d3812ab
гейт: 0 | предгейт G19, частно репо | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
гейт: 0 | предгейт G3, нула кадастрални идентификатори | python src/qa_no_cad_ids.py
гейт: 0 | сглобяване на кандидата по договора §2а | python src/build_quarters_candidate.py --decisions <решения> --frozen <frozen v2> --extra <extra> --out scratch/granitsi/quarters_candidate_07.09.geojson
гейт: 0 | QA на кандидата, 15 проверки | python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --registry <регистър> --decisions <решения>
гейт: 0 | детерминизъм, две сглобявания в отделни процеси са байт-еднакви | cmp scratch/granitsi/_run1.geojson scratch/granitsi/quarters_candidate_07.09.geojson
гейт: 0 | изходът е игнориран | git check-ignore -v scratch/granitsi/quarters_candidate_07.09.geojson
гейт: 0 | нула проследени изходи и фикстури | git ls-files scratch/granitsi tests/fixtures/qa_quarters_candidate
фикстура: 1 | build, координата в ред на решенията | python src/build_quarters_candidate.py --decisions <fix>/decisions_with_coordinate.json
фикстура: 1 | build, подменен връх при непроменен sha | python src/build_quarters_candidate.py --frozen <fix>/frozen_vertex_moved.geojson
фикстура: 1 | build, не-уикимапийски ред с непразен wm_id | python src/build_quarters_candidate.py --decisions <fix>/decisions_nonwikimapia_wm_id.json
фикстура: 1 | build, жилищен код от регистъра без ред в решенията | python src/build_quarters_candidate.py --registry <fix>/registry_residential_without_decision.json
фикстура: 1 | build, червената черта за името на подписания файл | python src/build_quarters_candidate.py --out <scratchpad>/quarters_signed.geojson
фикстура: 1 | QA, друг клас на артефакта | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/artifact_class_other.geojson
фикстура: 1 | QA, BOM/CRLF/несортирани ключове | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/bom_crlf_unsorted.geojson
фикстура: 1 | QA, отмененият етикет declared_local_knowledge | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/declared_local_knowledge.geojson
фикстура: 1 | QA, преместен връх срещу двата хеша | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/vertex_moved.geojson
фикстура: 1 | QA, подменен само суровият хеш | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/hash_raw_substituted.geojson
фикстура: 1 | QA, подменен само хешът по D1 | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/hash_d1_substituted.geojson
фикстура: 1 | QA, подменен wm_id | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/wm_id_substituted.geojson
фикстура: 1 | QA, отложен код с Feature | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/deferred_code_with_feature.geojson
фикстура: 1 | QA, Feature без ред в решенията | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/feature_without_row.geojson
фикстура: 1 | QA, код извън registry_pending без решение | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/code_outside_registry_pending.geojson
фикстура: 1 | QA, голо CC BY-SA | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/bare_cc_by_sa.geojson
фикстура: 1 | QA, липсващи условия на извора | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/missing_terms.geojson
фикстура: 1 | QA, липсващ ред за атрибуция | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/missing_attribution.geojson
фикстура: 1 | QA, една геометрия към два кода | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/two_codes_one_geometry.geojson
фикстура: 1 | QA, измислен precision_m | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/precision_invented.geojson
фикстура: 1 | QA, родител извън регистъра | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/parent_not_in_registry.geojson
фикстура: 1 | одиторска, чужд не-уикимапийски ред с непразно wm поле | python src/build_quarters_candidate.py --decisions <SP>/aud_vilite_wm_polygon.json
фикстура: 1 | одиторска, записан район в свойствата | python src/qa_quarters_candidate.py <SP>/aud_district_written.geojson
фикстура: 1 | одиторска, метод по улици | python src/qa_quarters_candidate.py <SP>/aud_method_streets.geojson
фикстура: 1 | одиторска, кадастрален идентификатор в заглавие | python src/qa_quarters_candidate.py <SP>/aud_cad_id.geojson
фикстура: 1 | одиторска, QA срещу решения с координата | python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --decisions <fix>/decisions_with_coordinate.json
```

```лот
код: Н2-0
статус: ЗЕЛЕН
комит: fb59f8dba1a1d0b1c47875b7e97ff35c366bf7b6
автор: Claude Executor <executor@local>
съобщение: measure: derive place coordinates read-only, no identity mutation
файл: src/measure_place_coords.py = 2adebea6a41393e9138e0f6fd58a04ebdc1e8a79cdda58d5c990afb3cfa9c1e8
гейт: 0 | предгейт G19, частно репо | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
гейт: 0 | договорен гейт §2а, 375 реда, кутията, sha на самоличността преди == след | python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json
гейт: 0 | повторяемост, вторият прогон дава байт-еднакъв изход | python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json
гейт: 0 | изходът е игнориран и не може да влезе в git | git check-ignore -v scratch/granitsi/place_coords_07.09.json
гейт: 0 | предкомитен G3 | python src/qa_no_cad_ids.py
фикстура: 1 | тяло извън кутията на Варна | python src/measure_place_coords.py --bodies scratch/granitsi/fixtures/bodies_outside_box.geojson
фикстура: 1 | ред от самоличността без place_id | python src/measure_place_coords.py --identity scratch/granitsi/fixtures/identity_without_place_id.json
фикстура: 1 | пазач, изходът сочи към самата самоличност | python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out data/place_identity.json
```

```лот
код: Н2
статус: ЗЕЛЕН
комит: 524fe313fe7c57fdab58fbc112fc59c35abcade5
автор: Claude Executor <executor@local>
съобщение: measure: polygon-vs-written quarter, ledger untouched
файл: src/measure_polygon_assign.py = 5da8ba7767ce7ac602603af75c80b104d9329783b1cf8e23b817c288a6e28956
гейт: 0 | предгейт G19, частно репо | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
гейт: 0 | договорен гейт §2а, леджерът се чете като блоб при основата | python src/measure_polygon_assign.py --base-rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b --polygons scratch/granitsi/quarters_candidate_07.09.geojson --coords scratch/granitsi/place_coords_07.09.json --parents scratch/granitsi/parents_dag_b0_07.09.json --out scratch/granitsi/assign_measure_07.09.json
гейт: 0 | детерминизъм, два прогона дават еднакви sha на двата изхода | sha256sum -c <scratchpad>/h1.txt
гейт: 0 | положителен контрол, expect срещу собствения изход не пада | python src/measure_polygon_assign.py --expect scratch/granitsi/assign_measure_07.09.json --out scratch/granitsi/assign_measure_control.json
гейт: 0 | предкомитни G3 и qa_no_extrude | python src/qa_no_cad_ids.py
гейт: 0 | нула нови проследени промени извън write-set-а | git status --porcelain
фикстура: 1 | връх на кандидат-полигон, преместен върху чуждо място, срещу expect | python src/measure_polygon_assign.py --polygons scratch/granitsi/fixtures/candidate_vertex_into_foreign_quarter.geojson --expect scratch/granitsi/assign_measure_07.09.json
фикстура: 1 | несъществуваща базова ревизия | python src/measure_polygon_assign.py --base-rev 0000000000000000000000000000000000000000
```

```лот
код: Н3-а
статус: ЗЕЛЕН
комит: 093b259466e8cf951db385d25a4be757775d85e9
автор: Claude Executor <executor@local>
съобщение: tests: five S17 fixtures against today's frozen behaviour
файл: tests/test_granitsi_fixtures.py = 3bd4ab18c12dacd0e6679246217e68b9389519b0226e608ade1a05adc37d6c00
файл: scratch/places_search/granitsi_fixtures_06.09.json = 9f6ff150231efb3771635cf83894c9f28d68467a092fd3a377dcec5c9e4def98
гейт: 0 | договорен гейт §2а, модулът на лота, 5 фикстури | python -m unittest tests.test_granitsi_fixtures
гейт: 0 | пълният набор на репото, 315 теста | python -m unittest discover -s tests
гейт: 0 | гейтовете на репото, без които сутрешният пуш е блокиран | python -m gates.run_gates
гейт: 0 | write-set изчерпателен, точно два файла в комита | git show --name-only --format= 093b259
фикстура: 1 | счупен кандидат street_collision | python <scratchpad>/neg_broken_case.py street_collision
фикстура: 1 | счупен кандидат district_retention | python <scratchpad>/neg_broken_case.py district_retention
фикстура: 1 | счупен кандидат mladost_kind_collision | python <scratchpad>/neg_broken_case.py mladost_kind_collision
фикстура: 1 | счупен кандидат order_identity | python <scratchpad>/neg_broken_case.py order_identity
фикстура: 1 | счупен кандидат parent_child | python <scratchpad>/neg_broken_case.py parent_child
фикстура: 1 | липсващ счупен вариант прави теста червен | python <scratchpad>/neg_missing_broken.py
фикстура: 1 | одиторска, подправено днешно число в записа | python <scratchpad>/auditor_neg_tampered_today.py today_n
фикстура: 1 | одиторска, подправен sha на входа на доставката | python <scratchpad>/auditor_neg_tampered_today.py input_sha
проба: 1 | нула геометрия в двата проследени файла, grep без съвпадения дава изход 1 | grep -cE "lat|lon" tests/test_granitsi_fixtures.py scratch/places_search/granitsi_fixtures_06.09.json
```

```лот
код: Н4
статус: ЗЕЛЕН
комит: 5e468a11ec5bf5e79e54cf78ddd5257714b6c50d
автор: Claude Executor <executor@local>
съобщение: measure: KAIS quar vs candidate polygons, read-only
файл: src/measure_kais_quar_vs_polygons.py = 8354f5537b8c5d7f0ee79bdf80de7b7d4f1b16589a7cbb5aba4be73ab734ca67
файл: src/qa_readonly_ast.py = 77720c0a347d29d00d4f257fd32054936e56eb3d448932200eebd89861b62440
файл: tests/fixtures/readonly_ast_negative.py = 52592b78b97638a6abfcec739e8d3156f9c0845c1fbd70cb0f8ed9bd06bb9cd9
гейт: 0 | договорен гейт §2а, 7 проверки, таблицата на stdout, манифестът преди == след | python src/measure_kais_quar_vs_polygons.py --info web/varna_buildings_info.json --bodies web/varna_buildings_3d.geojson --polygons scratch/granitsi/quarters_candidate_07.09.geojson
гейт: 0 | AST обход на самия измерващ скрипт, нула пишещи извиквания | python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py
фикстура: 1 | фикстура, която пише през json.dump | python src/qa_readonly_ast.py tests/fixtures/readonly_ast_negative.py
```

```лот
код: Н5
статус: ЗЕЛЕН
комит: предстои (този комит)
автор: Claude Executor <executor@local>
съобщение: docs: night-shift report 07.09
файл: docs/audits/ДОКЛАД_07.09_нощна_смяна.md = самореферентен (този доклад)
файл: scratch/places_search/qa_night_acceptance.py = f07088030af4eb3a43671bf3e429da8a36bf1dfba4c8ea2663d276a7644e7344
гейт: 0 | договорен гейт §2а, приемане на доклада | python scratch/places_search/qa_night_acceptance.py --report docs/audits/ДОКЛАД_07.09_нощна_смяна.md
фикстура: 1 | доклад без блока на един лот | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_missing_lot.md
фикстура: 1 | изходите на отрицателните фикстури на един лот, изкарани нула | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_zero_fixtures.md
фикстура: 1 | обърнат hex знак в sha на write-set | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_flipped_sha.md
фикстура: 1 | подправен автор на комит | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_author.md
фикстура: 1 | изходен код без команда, новата проверка C9 | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_no_command.md
```

---

## 2 · Числата

### Н1 · кандидат-геометрия (varna_3d, частно, НЕподписано)
60 Feature-а от 60 уикимапийски решения; входните решения са 68 реда (wikimapia 60 · deferred 6 · declared_streets 1 · alias_of 1). Кандидатът: 239 889 B, sha256 `4f466b92abaa93cb725ff5d1b7255661bda7f4d6e73c510a5d8f0c637e706522`, два независими прогона байт-еднакви, класът `candidate_not_signed`, изходът игнориран и нула проследени изходи. Регистър: 84 записа, 16 отложени поименно; **нула жилищни кода (кв./жк/кк) без решение** — 16-те отложени са с.о., местност, махала, мр, пз, м-т, со, вз, зона. Всичките 60 са Polygon (нула MultiPolygon), всичките 60 идват от замразения набор (288 Feature-а), нула от extra-файла. Родство: 55 без родител, 3 с родител с полигон, 2 с родител без полигон. `precision_m` е null в 60/60 (не се измисля), полето за район не се пише в геометрията.
**Двете хеш-правила се разминават за 60 от 60 Feature-а** — суровият хеш от решенията срещу канонизацията по D1. Това е решение №2 за Петър, не козметика.
**Поправки на плана (от одитора):** обектът 5729429 е и в замразения набор, и в extra-файла, с байт-еднаква геометрия — планът греши, като го нарича „извън обявения frozen манифест“; изходът се игнорира от ред 66 на `.gitignore` (`scratch/*`), не от ред 23.
**Обявено отклонение (иска ратификация):** allow-списък от едно име (`mladost2`), който допуска остатъчните уикимапийски полета при не-уикимапийски ред; всеки друг такъв ред спира сглобяването (доказано с фикстура).

### Н2 · присвояване (само числа, нула запис)
Основа: `8d60aebb365fb8e74ccc863d3b3db90b74180a3b`; леджерът се чете като блоб (sha `d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075`, 375 реда, 201 написани квартала, блоб == работен файл).

Изходи при подписания ръб 100 m (затворената таблица на Б0 т. 12): **written 201** (от тях: същият 186 · спор написан срещу полигон 7 · без полигон 8 · съвместим 0) · **pin_outside_all 41** · **edge_pending 63** · **disputed_overlap 5** · **deferred_zone 0** · **assigned_polygon 65** („би получил“) · **assigned_district 0**.

Трите ленти на неточността: **50 m** → edge_pending 30 · би получил 94 · спор 9 · **100 m** → 63 · 65 · 5 · **250 m** → 113 · 20 · 0.

Леджер на конфликтите по вид: none 286 · name_vs_polygon 33 · pin_outside_all 49 · written_outside_polygon 7 · parent_vs_child 0.

Спор „написан ≠ полигон“ (7, поименно; редовете остават с написаното): Албиция (galata срещу fichoza) · Зеленика (galata срещу zelenika) · Кабакум (chaika_kk срещу alen_mak) · ПАРК ХОТЕЛ БЕЛВЮ (zlatni_pyasatsi срещу alen_mak) · ПГИ „Д-р Иван Богоров“ (mladost2 срещу mladost и mladost1) · „Хоспис Мишел Паре“ (kk_konstantin_elena срещу evksinograd) · „Хоспис Филаретова“ (borovets_yug срещу zelenika).
Двойна зона без родство (5, всичките grackata_mahala и tsentar): ДГ 7 „Ал. С. Пушкин“ · Еника · НУИ „Добри Христов“ · Плаза · Хай.
Написан квартал без кандидат-полигон (8): Империя · ЛОТОС · НИМФА · ОАЗИС · РИВИЕРА БИЙЧ (zlatni_pyasatsi) · Станкино ханче · Комитово ханче (vladislavovo) · УМБАЛ „Св. Марина“ (kk_konstantin_elena).

Подписаният DAG е преизмерен върху кандидат-полигоните: 10 от 11 двойки измерими, всичките ≥ 98,4 % от детето вътре в родителя (mladost2 няма полигон, двойката е инертна); петте частични припокривания дават 72,07 · 60,98 · 52,02 · 51,37 · 39,04 % — както в Б0 т. 9. **Открити 6 недекларирани припокривания, всичките под 5 %** (най-голямото balam_dere и vladislavovo, 4,94 %) — за сутрешния списък.

**Находки на изпълнителя и одитора:** `assigned_district` е недостижима клетка при тези входове (подписаният ред слага pin_outside_all преди нея), а `deferred_zone` също е недостижима, защото нито един отложен код няма Feature — три клетки на затворената таблица (тези две и `no_coord`) нямат нито срещане, нито фикстура. Числото 49 в леджера = 41 изхода pin_outside_all плюс 8-те „написан без полигон“.

### Н2-0 · координати (мярка, без мутация)
375/375 реда с координата, нула `no_coord`, нула координати извън кутията на Варна; 368 различни кадастрални тела, 7 места делят тяло. `data/place_identity.json` е недокоснат: sha256 `e8b4c836f6020d55589867e5de6d819c3e7f81a6194d0fa92f237af81b6533b6` преди == след, същият mtime. Изход 146 896 B, sha256 `60f9a9306ca1e9aec691266fd9be5408e9b3679a945ff262b9db46a7f4c2e76d`, два прогона байт-еднакви, преизчислен независимо от одитора с нула разлики. `precision_m` не се измисля.

### Н3-а · фикстури (Fire_Varna)
5 фикстури зелени срещу днешното поведение; пълният набор 315 теста зелен; гейтовете на репото зелени. Двете отложени са назовани: версията с Възраждане (няма родство в регистъра) и `client_cache_matrix` (браузърно поведение, няма назован изпълнител). Доказаните падания: street_collision клонът се мени (A3-street към A3-category и zone/kind) · district_retention 12 към 11 · mladost_kind_collision с квартал 6 към 7 · order_identity с квартал 6 към 7 · parent_child 11 към 10.
**Находка на одитора:** при `order_identity` и `mladost_kind_collision` падането идва от броя с квартал, не от подредбата; редът наистина се мени (сравнението по множество би минало зелено и това е записано в самата фикстура). `_meta.engine.sha256` се записва, но никой не го сверява — пинът е декоративен, докато смяната на двигателя се лови косвено през числата.

### Н4 · сградите (мярка) **[БЕЗ ОДИТОР]**
Входове (sha256 в изхода): таблица `f7ee3e07…`, тела `d0c83360…`, полигони `4f466b92…`, регистър `7d217401…`. Манифест на `data/` и `web/`: 467 файла, дайджест `a6cc9eb7dfcc0d98e705e43004a81b187e9f865f478a9f75dba5b7966e1bcaaa`, преди == след.
80 497 сгради в таблицата · 31 116 с непразен кадастрален квартал · 49 381 без · 60 кандидат-полигона · 1 545 тела в две и повече зони (от тях 226 с декларирано родство).
Затворената таблица: **съвпада 15 764 (50,7 %) · не съвпада 10 112 (32,5 %) · няма полигон 4 532 (14,6 %) · само район 708 (2,3 %)**.
Разбивка на „не съвпада“: 7 131 име срещу полигон · 2 828 написаният код няма кандидат-полигон · 153 полигонът е родител или дете по декларираното родство · 60 низът-свидетел повтаря написаното.
Поименните несъгласия на §7: Кайсиева/Владиславово 114 · Акчелар/Виница 933 · курорт/квартал Чайка 0 · многозначен низ, разрешен от полигона 988.
Най-големите несъгласия (написан код към кода на най-малкия съдържащ полигон): galata към borovets_yug 2 045 · trakata към evksinograd 1 197 · briz към sveti_nikola 1 022 · vinitsa към akchelar 933 · trakata към sredna_traka 703 · vinitsa към manastirski_rid 602 · dobreva към vinitsa_sever 524 · vazrazhdane към vazrazhdane1 219.
Низове „само район“: 157 различни, най-чести „в.з. Варна“ 141 и вариантите на „вилна зона“ 195 общо.
Нула кадастрални идентификатори и нула координати в изхода (проверка C6 на гейта); AST-обходът потвърждава, че скриптът няма нито едно пишещо извикване.

---

## 3 · Част Б — заварено състояние (НЕ е лот на този доклад)

Мандатът на Н5 е доклад за нощта; лотовете Б са изпълнявани от други агенти и **до Н5 не е стигнал нито техен запис, нито одит**. Затова тук стои само измереното сега, read-only — **[БЕЗ ОДИТОР]**:

- **Б1 · два комита във varna_3d:** `2800a7cf3f8aa4d301956b7879c54bc35b8bb25b` (`build: assemble quarters_signed.geojson from decisions 3 (sha ec2813e1c074) with D1 schema for imported geometry`; файлове `.gitignore`, `src/build_quarters_signed.py`) и `791b0cb2ccc509e5ff75bf195fe9806a1eaba0c6` (`gates: qa_quarters_signed with negative fixtures`; файлове `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`), и двата с автор `Claude Executor <executor@local>`.
- **Стейджнат за комита на Петър (D16/G4):** `data/quarters_signed.geojson` — 291 024 B, sha256 `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1` (индексът и работният файл са байт-еднакви). Проверен наново тази нощ от изпълнителя на Н5: `python src/qa_quarters_signed.py data/quarters_signed.geojson --registry <регистър>` → изход 0, 18 проверки, 61 Feature-а, 68 решения, 16 отложени, блоб на решенията `ec2813e1c074…`; `python -m unittest tests.test_quarters_signed_fixtures` → 7 теста, изход 0. **Отрицателни фикстури за Б1 не са преизпълнени от Н5** — гейтът без доказано падане не е приет за зелен по §0 т. 6; иска се одит преди Gate 2.
- **Б2-0 (Б0 т. 11) е НЕЗАВЪРШЕН:** `src/place_identity.py` е променен, но **не е комитнат**; съществува кандидат `data/place_identity.candidate.json` (240 134 B, sha256 `1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761`); резервното копие на самоличността е на подписания път в scratchpad-а и е байт-еднакво с живия файл (`e8b4c836…`). **Подмяна НЕ е извършена** — живият `data/place_identity.json` е с sha от началото на нощта.
- **Б2, Б3, Б4 не са тръгвали:** `data/fire_varna_places.json` (`329310f5…`), `data/fire_varna_hotels.json` (`46a44ce8…`) и леджерът (`d5050f1c…`) са с непроменени sha; кръпката `scratch/places_search/b3_patch_07.09.diff` не съществува.
- **Мръсното дърво на varna_3d:** три проследени промени — `scratch/place_bodies/qa_place_bodies.md` (заварена отпреди нощта, недокосната), `src/place_identity.py` (Б2-0, некомитнат) и стейджнатият `data/quarters_signed.geojson`.

---

## 4 · Спрели лотове, обявени отклонения и оставени дългове

- **Н3-б СПИРА нарочно** (план §3): нов код или нов източник без подредената тройка на D13 изхвърля 150 места мълчаливо, а 41 потвърдени кода липсват в затворения списък на картата.
- **Отложени фикстури:** версията на `parent_child` с Възраждане (няма родство в регистъра) и `client_cache_matrix` (браузърно поведение).
- **Обявено отклонение №1 (Н0, чуждо на лота):** червеното на първия прогон на Н0 е изчистено с промяна на `.gitignore` в комит `57ab8ebff32038028c98dfe8a8044c63dac2b3b8` от `Claude Architect` — извън write-set-а на който и да е лот. По същество е поправка на първопричината (седемте геометрични пътя вече наистина се игнорират, нула проследени файлове са скрити с това), но е промяна на политика в проследен файл в нощ от мерки — **иска изричната дума на Петър на Gate 2**.
- **Обявено отклонение №2 (Н1):** allow-списъкът от едно име при не-уикимапийски ред с остатъчни уикимапийски полета.
- **Обявено отклонение №3 (Н5, този лот):** гейтът на доклада е допълнен с две по-строги проверки — всеки записан изходен код носи име и команда, и докладът трябва да цитира sha256 на подписаното тяло на плана. Двете правят гейта по-строг, не по-мек.
- **Известни пропуски на гейтовете (за амандамент, не за нощта):** пинове с празен списък входове минават мълчаливо (Н0); `_meta.engine.sha256` не се сверява от никого (Н3-а); три клетки на затворената таблица са недостижими при днешните входове (Н2); проверката „нула проследена геометрия“ обхожда седем декларирани пътя, не цялото репо — във Fire_Varna има един по-стар проследен геометричен файл, комитнат от Петър на 02.09 и вече в `origin/main`.
- **Дългове от §5 на плана, непроменени:** решенията нямат ред за атрибуция; `_meta.base_rev` липсва в леджера; веригата назад към предходния файл с решения е скъсана (предшественикът липсва на диска).

---

## 5 · Какво прави Петър сутринта

1. **Комит на геометрията (G4/D16).** `C:/git/varna_3d` — `data/quarters_signed.geojson` е СТЕЙДЖНАТ и чака неговия комит; готово съобщение: `data: signed quarter boundaries v1 (decisions 3, sha ec2813e1c074)`. Преди комита да сравни sha на файла с `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1` и да реши дали приема Б1 без преизпълнени отрицателни фикстури (виж §3).
2. **Износите.** Няма стейджнат износ — Б2 не е тръгвал; `data/fire_varna_places.json`, `data/fire_varna_hotels.json` и леджерът са непроменени. Ако иска износ с квартали, първо трябва да реши какво става с незавършеното Б2-0 (кандидатът за самоличността и некомитнатият `src/place_identity.py`): да го довърши с G9 или да го отмени (копиране на резервното копие върху `data/place_identity.json` и сверка на sha `e8b4c836…`; днес двете са еднакви, така че отмяната е изтриване на кандидата и връщане на скрипта).
3. **Препотвърждаване на решенията по sha.** `git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json` дава `ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6` — **подписва се БЛОБЪТ**, не работният файл (работният е с други знаци за край на ред и друг sha). В същия файл влиза липсващият ред за атрибуция, в нов комит, чийто sha той препотвърждава.
4. **Преглед на дифа в трите репа.** Fire_Varna: 48 комита напред и **2 назад** — сливането с `origin/main` е негово решение. varna_3d: 47 напред, клон `rezhimi`. Varna_buildings: 1 напред, регистърът недокоснат. Да погледне поименно шестте нощни комита и стейджнатата геометрия.
5. **Б3 като ЕДИН атомен комит** с неговите подписи (търсене по квартал, разширеният списък кодове, редът за атрибуция в картончето, доставката по подредената тройка) — нощес нищо от него не е пипано и кръпка не е оставена.
6. **Регистърът** (`Varna_buildings/config/quarter_registry.json`, непокътнат): Ваялар като alias · Евксиноград и Траката (конфликтът на имена) · Цветен квартал · липсващите родители (Възраждане 1–4, Розова долина) · 16-те кода без решение. Плюс новото: 6 недекларирани припокривания под 5 % и решенията от §5 на плана (схема за внесена геометрия, кое хеш-правило, Младост 2, районът, името на десетия ключ, precision_m, разширяването на списъка кодове).
7. **Gate 2 и пуш.** Пълният набор (315 теста) и `python -m gates.run_gates` са зелени сега; пушът е само негов — нито един агент не е пипал `origin`.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('docs/audits/ДОКЛАД_07.09_нощна_смяна.md'); print('\\n'.join(f'{i}: {s}' for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1)))\"" in C:\git\Fire_Varna
 succeeded in 0ms:
1: # ДОКЛАД · нощна смяна „Границите“ (06→07.09.2026)
2: 
3: **Атрибуция (Wikimapia ToS §1.G):** кварталните граници, за които става дума в този доклад, са изведени от данни на [Wikimapia.org](http://wikimapia.org); допълнителният обект, назован в мерките по-долу, е [wikimapia.org/5729429](http://wikimapia.org/5729429). Лиценз на извора: „CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)“. За `mladost2` изворът на осите е OpenStreetMap — „© OpenStreetMap contributors“, ODbL.
4: 
5: **План:** `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md`, ПОДПИСАН от Петър; sha256 на подписаното тяло = `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766` (блобът в `42b2635`).
6: **Лот на този доклад:** Н5. **Съобщение:** `docs: night-shift report 07.09`. Този доклад ЗАМЕСТВА версията от `65a0c7a`, която описваше по-ранно състояние (Н0 червен, 2 от 11 лота) и вече не е вярна.
7: **Разделение (план §3, Н5):** числата идват от ОДИТОРИТЕ; изпълнителят на Н5 ги записва, без да ги тълкува. Разминаване между изпълнител и одитор се печата с двете стойности и **[РАЗМИНАВАНЕ]**. Където до Н5 НЕ е стигнал одиторски запис, числото е измерено наново от изпълнителя на Н5 (read-only) и носи **[БЕЗ ОДИТОР]** — това е признание за липса на независима проверка, не оценка.
8: 
9: ---
10: 
11: ## 0 · Присъда
12: 
13: **Част А (Н0–Н5) е изпълнена: 7 от 7 лота ЗЕЛЕНИ, 6 комита.** Доставените одиторски присъди са **пет: Н0, Н1, Н2-0, Н2, Н3-а — всичките ГОДНО**, всяка с преизпълнени гейтове и собствени допълнителни отрицателни фикстури.
14: 
15: **Находка №1 на този доклад: ЦЯЛОСТНА одиторска присъда за нощта НЕ е доставена до Н5, както и одиторски запис за Н4 и за част Б.** Затова:
16: - числата на **Н4** тук са измерени наново от изпълнителя на Н5 с командите от договора §2а — **[БЕЗ ОДИТОР]**;
17: - **гейтът на Н5** е самопроверка на записа (машинна), не одит на нощта;
18: - преди Gate 2 Петър има основание да поиска одит на Н4 и на част Б (лот Б5 на плана: архитект, Кими, Astra).
19: 
20: **Твърдите ограничения ДЪРЖАТ — нула нарушения по шестте забрани на §4:** нула пуш (`origin` на трите репа е недокоснат) · нула геометрия в проследен файл на Fire_Varna от тази нощ · `quarter_registry.json` непокътнат (sha `7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6`, дифът празен) · нула променени написани квартала (леджерът е байт-равен на блоба при основата) · нула записи в леджера, `place_identity.json` и `data/fire_varna_*.json` · нула разминавания между изпълнителски и одиторски числа в доставените лотове.
21: 
22: **Броячи (измерени сега):** Fire_Varna 47 напред и 2 НАЗАД спрямо `origin/main` (сливането сутринта е на Петър; след комита на Н5 — 48 напред) · varna_3d 47 напред, 0 назад спрямо `origin/rezhimi` · Varna_buildings 1 напред, регистърът непроменен.
23: 
24: ---
25: 
26: ## 1 · Лотовете (машинно проверим запис)
27: 
28: Всеки блок се чете от `scratch/places_search/qa_night_acceptance.py`: гейтът преизчислява всяко sha256 от файла на диска, препрочита всеки комит, автор и съобщение от git, взима дословните съобщения и write-set-овете от подписания план и иска команда до всеки изходен код.
29: 
30: ```лот
31: код: Н0
32: статус: ЗЕЛЕН
33: комит: a454b60e1f6ff4ca51f6aebd6a6c55e28a0cffb5
34: автор: Claude Executor <executor@local>
35: съобщение: measure: pin night-shift inputs, base_rev and ignore proofs (06.09)
36: файл: scratch/places_search/noshtna_pins_06.09.json = d187ecbe94dde3614215e84e6e9d06046e4c3154ff3594f7e24be2eb9d273376
37: файл: scratch/places_search/qa_night_pins.py = 3a813b0c74486e27c90bada7477e7a3e728f9c9fbc24f5ad7bd9ac151e51ab4e
38: гейт: 0 | договорен гейт §2а, 11 проверки, преизпълнен и СЛЕД комита | python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json
39: гейт: 0 | предгейт G19, varna_3d е PRIVATE | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
40: фикстура: 1 | обърнат един hex знак в пинатия sha на frozen v2 | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/pins_flipped_hex.json
41: фикстура: 3 | еднократно worktree с git add -f върху геометричен файл, реалното дърво остава чисто | python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json --worktree-negative
42: фикстура: 1 | одиторска, подменен base_rev | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_baserev.json
43: фикстура: 1 | одиторска, подменен HEAD на varna_3d | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_v3head.json
44: фикстура: 1 | одиторска, подменен sha на мръсния проследен файл | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_dirty.json
45: фикстура: 1 | одиторска, подменен блоб-sha на регистъра | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_blob.json
46: фикстура: 1 | одиторска, вкаран ключ с координати в пиновете | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_coords.json
47: фикстура: 1 | одиторска, пинат по-ранен HEAD, комит извън write-set-а | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_c7outside.json
48: фикстура: 1 | одиторска, сгрешен ahead на Varna_buildings | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_ahead.json
49: фикстура: 1 | одиторска, очаквана видимост PUBLIC | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_g19.json
50: проба: 0 | положителна, същият sha под ДРУГО име остава зелен | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/pins_name_swapped.json
51: проба: 0 | ОДИТОРСКИ ПРОПУСК, пинове с празен списък входове минават мълчаливо | python scratch/places_search/qa_night_pins.py --pins <scratchpad>/audit_neg_empty_inputs.json
52: ```
53: 
54: ```лот
55: код: Н1
56: статус: ЗЕЛЕН
57: комит: 0fed1e0fafab387a33536414f94093f36af5e9db
58: автор: Claude Executor <executor@local>
59: съобщение: measure: candidate quarter geometry from pinned decisions (no signed artifact)
60: файл: src/build_quarters_candidate.py = 27fe228d9c56787b581994df07ba869e4ad7b9101ab399e6496262c7e8e36858
61: файл: src/qa_quarters_candidate.py = eaf8ec73f4151392118c36390df39471c357568f3162b8a333791ac77d3812ab
62: гейт: 0 | предгейт G19, частно репо | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
63: гейт: 0 | предгейт G3, нула кадастрални идентификатори | python src/qa_no_cad_ids.py
64: гейт: 0 | сглобяване на кандидата по договора §2а | python src/build_quarters_candidate.py --decisions <решения> --frozen <frozen v2> --extra <extra> --out scratch/granitsi/quarters_candidate_07.09.geojson
65: гейт: 0 | QA на кандидата, 15 проверки | python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --registry <регистър> --decisions <решения>
66: гейт: 0 | детерминизъм, две сглобявания в отделни процеси са байт-еднакви | cmp scratch/granitsi/_run1.geojson scratch/granitsi/quarters_candidate_07.09.geojson
67: гейт: 0 | изходът е игнориран | git check-ignore -v scratch/granitsi/quarters_candidate_07.09.geojson
68: гейт: 0 | нула проследени изходи и фикстури | git ls-files scratch/granitsi tests/fixtures/qa_quarters_candidate
69: фикстура: 1 | build, координата в ред на решенията | python src/build_quarters_candidate.py --decisions <fix>/decisions_with_coordinate.json
70: фикстура: 1 | build, подменен връх при непроменен sha | python src/build_quarters_candidate.py --frozen <fix>/frozen_vertex_moved.geojson
71: фикстура: 1 | build, не-уикимапийски ред с непразен wm_id | python src/build_quarters_candidate.py --decisions <fix>/decisions_nonwikimapia_wm_id.json
72: фикстура: 1 | build, жилищен код от регистъра без ред в решенията | python src/build_quarters_candidate.py --registry <fix>/registry_residential_without_decision.json
73: фикстура: 1 | build, червената черта за името на подписания файл | python src/build_quarters_candidate.py --out <scratchpad>/quarters_signed.geojson
74: фикстура: 1 | QA, друг клас на артефакта | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/artifact_class_other.geojson
75: фикстура: 1 | QA, BOM/CRLF/несортирани ключове | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/bom_crlf_unsorted.geojson
76: фикстура: 1 | QA, отмененият етикет declared_local_knowledge | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/declared_local_knowledge.geojson
77: фикстура: 1 | QA, преместен връх срещу двата хеша | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/vertex_moved.geojson
78: фикстура: 1 | QA, подменен само суровият хеш | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/hash_raw_substituted.geojson
79: фикстура: 1 | QA, подменен само хешът по D1 | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/hash_d1_substituted.geojson
80: фикстура: 1 | QA, подменен wm_id | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/wm_id_substituted.geojson
81: фикстура: 1 | QA, отложен код с Feature | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/deferred_code_with_feature.geojson
82: фикстура: 1 | QA, Feature без ред в решенията | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/feature_without_row.geojson
83: фикстура: 1 | QA, код извън registry_pending без решение | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/code_outside_registry_pending.geojson
84: фикстура: 1 | QA, голо CC BY-SA | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/bare_cc_by_sa.geojson
85: фикстура: 1 | QA, липсващи условия на извора | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/missing_terms.geojson
86: фикстура: 1 | QA, липсващ ред за атрибуция | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/missing_attribution.geojson
87: фикстура: 1 | QA, една геометрия към два кода | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/two_codes_one_geometry.geojson
88: фикстура: 1 | QA, измислен precision_m | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/precision_invented.geojson
89: фикстура: 1 | QA, родител извън регистъра | python src/qa_quarters_candidate.py tests/fixtures/qa_quarters_candidate/parent_not_in_registry.geojson
90: фикстура: 1 | одиторска, чужд не-уикимапийски ред с непразно wm поле | python src/build_quarters_candidate.py --decisions <SP>/aud_vilite_wm_polygon.json
91: фикстура: 1 | одиторска, записан район в свойствата | python src/qa_quarters_candidate.py <SP>/aud_district_written.geojson
92: фикстура: 1 | одиторска, метод по улици | python src/qa_quarters_candidate.py <SP>/aud_method_streets.geojson
93: фикстура: 1 | одиторска, кадастрален идентификатор в заглавие | python src/qa_quarters_candidate.py <SP>/aud_cad_id.geojson
94: фикстура: 1 | одиторска, QA срещу решения с координата | python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --decisions <fix>/decisions_with_coordinate.json
95: ```
96: 
97: ```лот
98: код: Н2-0
99: статус: ЗЕЛЕН
100: комит: fb59f8dba1a1d0b1c47875b7e97ff35c366bf7b6
101: автор: Claude Executor <executor@local>
102: съобщение: measure: derive place coordinates read-only, no identity mutation
103: файл: src/measure_place_coords.py = 2adebea6a41393e9138e0f6fd58a04ebdc1e8a79cdda58d5c990afb3cfa9c1e8
104: гейт: 0 | предгейт G19, частно репо | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
105: гейт: 0 | договорен гейт §2а, 375 реда, кутията, sha на самоличността преди == след | python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json
106: гейт: 0 | повторяемост, вторият прогон дава байт-еднакъв изход | python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json
107: гейт: 0 | изходът е игнориран и не може да влезе в git | git check-ignore -v scratch/granitsi/place_coords_07.09.json
108: гейт: 0 | предкомитен G3 | python src/qa_no_cad_ids.py
109: фикстура: 1 | тяло извън кутията на Варна | python src/measure_place_coords.py --bodies scratch/granitsi/fixtures/bodies_outside_box.geojson
110: фикстура: 1 | ред от самоличността без place_id | python src/measure_place_coords.py --identity scratch/granitsi/fixtures/identity_without_place_id.json
111: фикстура: 1 | пазач, изходът сочи към самата самоличност | python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out data/place_identity.json
112: ```
113: 
114: ```лот
115: код: Н2
116: статус: ЗЕЛЕН
117: комит: 524fe313fe7c57fdab58fbc112fc59c35abcade5
118: автор: Claude Executor <executor@local>
119: съобщение: measure: polygon-vs-written quarter, ledger untouched
120: файл: src/measure_polygon_assign.py = 5da8ba7767ce7ac602603af75c80b104d9329783b1cf8e23b817c288a6e28956
121: гейт: 0 | предгейт G19, частно репо | "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility
122: гейт: 0 | договорен гейт §2а, леджерът се чете като блоб при основата | python src/measure_polygon_assign.py --base-rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b --polygons scratch/granitsi/quarters_candidate_07.09.geojson --coords scratch/granitsi/place_coords_07.09.json --parents scratch/granitsi/parents_dag_b0_07.09.json --out scratch/granitsi/assign_measure_07.09.json
123: гейт: 0 | детерминизъм, два прогона дават еднакви sha на двата изхода | sha256sum -c <scratchpad>/h1.txt
124: гейт: 0 | положителен контрол, expect срещу собствения изход не пада | python src/measure_polygon_assign.py --expect scratch/granitsi/assign_measure_07.09.json --out scratch/granitsi/assign_measure_control.json
125: гейт: 0 | предкомитни G3 и qa_no_extrude | python src/qa_no_cad_ids.py
126: гейт: 0 | нула нови проследени промени извън write-set-а | git status --porcelain
127: фикстура: 1 | връх на кандидат-полигон, преместен върху чуждо място, срещу expect | python src/measure_polygon_assign.py --polygons scratch/granitsi/fixtures/candidate_vertex_into_foreign_quarter.geojson --expect scratch/granitsi/assign_measure_07.09.json
128: фикстура: 1 | несъществуваща базова ревизия | python src/measure_polygon_assign.py --base-rev 0000000000000000000000000000000000000000
129: ```
130: 
131: ```лот
132: код: Н3-а
133: статус: ЗЕЛЕН
134: комит: 093b259466e8cf951db385d25a4be757775d85e9
135: автор: Claude Executor <executor@local>
136: съобщение: tests: five S17 fixtures against today's frozen behaviour
137: файл: tests/test_granitsi_fixtures.py = 3bd4ab18c12dacd0e6679246217e68b9389519b0226e608ade1a05adc37d6c00
138: файл: scratch/places_search/granitsi_fixtures_06.09.json = 9f6ff150231efb3771635cf83894c9f28d68467a092fd3a377dcec5c9e4def98
139: гейт: 0 | договорен гейт §2а, модулът на лота, 5 фикстури | python -m unittest tests.test_granitsi_fixtures
140: гейт: 0 | пълният набор на репото, 315 теста | python -m unittest discover -s tests
141: гейт: 0 | гейтовете на репото, без които сутрешният пуш е блокиран | python -m gates.run_gates
142: гейт: 0 | write-set изчерпателен, точно два файла в комита | git show --name-only --format= 093b259
143: фикстура: 1 | счупен кандидат street_collision | python <scratchpad>/neg_broken_case.py street_collision
144: фикстура: 1 | счупен кандидат district_retention | python <scratchpad>/neg_broken_case.py district_retention
145: фикстура: 1 | счупен кандидат mladost_kind_collision | python <scratchpad>/neg_broken_case.py mladost_kind_collision
146: фикстура: 1 | счупен кандидат order_identity | python <scratchpad>/neg_broken_case.py order_identity
147: фикстура: 1 | счупен кандидат parent_child | python <scratchpad>/neg_broken_case.py parent_child
148: фикстура: 1 | липсващ счупен вариант прави теста червен | python <scratchpad>/neg_missing_broken.py
149: фикстура: 1 | одиторска, подправено днешно число в записа | python <scratchpad>/auditor_neg_tampered_today.py today_n
150: фикстура: 1 | одиторска, подправен sha на входа на доставката | python <scratchpad>/auditor_neg_tampered_today.py input_sha
151: проба: 1 | нула геометрия в двата проследени файла, grep без съвпадения дава изход 1 | grep -cE "lat|lon" tests/test_granitsi_fixtures.py scratch/places_search/granitsi_fixtures_06.09.json
152: ```
153: 
154: ```лот
155: код: Н4
156: статус: ЗЕЛЕН
157: комит: 5e468a11ec5bf5e79e54cf78ddd5257714b6c50d
158: автор: Claude Executor <executor@local>
159: съобщение: measure: KAIS quar vs candidate polygons, read-only
160: файл: src/measure_kais_quar_vs_polygons.py = 8354f5537b8c5d7f0ee79bdf80de7b7d4f1b16589a7cbb5aba4be73ab734ca67
161: файл: src/qa_readonly_ast.py = 77720c0a347d29d00d4f257fd32054936e56eb3d448932200eebd89861b62440
162: файл: tests/fixtures/readonly_ast_negative.py = 52592b78b97638a6abfcec739e8d3156f9c0845c1fbd70cb0f8ed9bd06bb9cd9
163: гейт: 0 | договорен гейт §2а, 7 проверки, таблицата на stdout, манифестът преди == след | python src/measure_kais_quar_vs_polygons.py --info web/varna_buildings_info.json --bodies web/varna_buildings_3d.geojson --polygons scratch/granitsi/quarters_candidate_07.09.geojson
164: гейт: 0 | AST обход на самия измерващ скрипт, нула пишещи извиквания | python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py
165: фикстура: 1 | фикстура, която пише през json.dump | python src/qa_readonly_ast.py tests/fixtures/readonly_ast_negative.py
166: ```
167: 
168: ```лот
169: код: Н5
170: статус: ЗЕЛЕН
171: комит: предстои (този комит)
172: автор: Claude Executor <executor@local>
173: съобщение: docs: night-shift report 07.09
174: файл: docs/audits/ДОКЛАД_07.09_нощна_смяна.md = самореферентен (този доклад)
175: файл: scratch/places_search/qa_night_acceptance.py = f07088030af4eb3a43671bf3e429da8a36bf1dfba4c8ea2663d276a7644e7344
176: гейт: 0 | договорен гейт §2а, приемане на доклада | python scratch/places_search/qa_night_acceptance.py --report docs/audits/ДОКЛАД_07.09_нощна_смяна.md
177: фикстура: 1 | доклад без блока на един лот | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_missing_lot.md
178: фикстура: 1 | изходите на отрицателните фикстури на един лот, изкарани нула | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_zero_fixtures.md
179: фикстура: 1 | обърнат hex знак в sha на write-set | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_flipped_sha.md
180: фикстура: 1 | подправен автор на комит | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_author.md
181: фикстура: 1 | изходен код без команда, новата проверка C9 | python scratch/places_search/qa_night_acceptance.py --report <scratchpad>/n5_neg_no_command.md
182: ```
183: 
184: ---
185: 
186: ## 2 · Числата
187: 
188: ### Н1 · кандидат-геометрия (varna_3d, частно, НЕподписано)
189: 60 Feature-а от 60 уикимапийски решения; входните решения са 68 реда (wikimapia 60 · deferred 6 · declared_streets 1 · alias_of 1). Кандидатът: 239 889 B, sha256 `4f466b92abaa93cb725ff5d1b7255661bda7f4d6e73c510a5d8f0c637e706522`, два независими прогона байт-еднакви, класът `candidate_not_signed`, изходът игнориран и нула проследени изходи. Регистър: 84 записа, 16 отложени поименно; **нула жилищни кода (кв./жк/кк) без решение** — 16-те отложени са с.о., местност, махала, мр, пз, м-т, со, вз, зона. Всичките 60 са Polygon (нула MultiPolygon), всичките 60 идват от замразения набор (288 Feature-а), нула от extra-файла. Родство: 55 без родител, 3 с родител с полигон, 2 с родител без полигон. `precision_m` е null в 60/60 (не се измисля), полето за район не се пише в геометрията.
190: **Двете хеш-правила се разминават за 60 от 60 Feature-а** — суровият хеш от решенията срещу канонизацията по D1. Това е решение №2 за Петър, не козметика.
191: **Поправки на плана (от одитора):** обектът 5729429 е и в замразения набор, и в extra-файла, с байт-еднаква геометрия — планът греши, като го нарича „извън обявения frozen манифест“; изходът се игнорира от ред 66 на `.gitignore` (`scratch/*`), не от ред 23.
192: **Обявено отклонение (иска ратификация):** allow-списък от едно име (`mladost2`), който допуска остатъчните уикимапийски полета при не-уикимапийски ред; всеки друг такъв ред спира сглобяването (доказано с фикстура).
193: 
194: ### Н2 · присвояване (само числа, нула запис)
195: Основа: `8d60aebb365fb8e74ccc863d3b3db90b74180a3b`; леджерът се чете като блоб (sha `d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075`, 375 реда, 201 написани квартала, блоб == работен файл).
196: 
197: Изходи при подписания ръб 100 m (затворената таблица на Б0 т. 12): **written 201** (от тях: същият 186 · спор написан срещу полигон 7 · без полигон 8 · съвместим 0) · **pin_outside_all 41** · **edge_pending 63** · **disputed_overlap 5** · **deferred_zone 0** · **assigned_polygon 65** („би получил“) · **assigned_district 0**.
198: 
199: Трите ленти на неточността: **50 m** → edge_pending 30 · би получил 94 · спор 9 · **100 m** → 63 · 65 · 5 · **250 m** → 113 · 20 · 0.
200: 
201: Леджер на конфликтите по вид: none 286 · name_vs_polygon 33 · pin_outside_all 49 · written_outside_polygon 7 · parent_vs_child 0.
202: 
203: Спор „написан ≠ полигон“ (7, поименно; редовете остават с написаното): Албиция (galata срещу fichoza) · Зеленика (galata срещу zelenika) · Кабакум (chaika_kk срещу alen_mak) · ПАРК ХОТЕЛ БЕЛВЮ (zlatni_pyasatsi срещу alen_mak) · ПГИ „Д-р Иван Богоров“ (mladost2 срещу mladost и mladost1) · „Хоспис Мишел Паре“ (kk_konstantin_elena срещу evksinograd) · „Хоспис Филаретова“ (borovets_yug срещу zelenika).
204: Двойна зона без родство (5, всичките grackata_mahala и tsentar): ДГ 7 „Ал. С. Пушкин“ · Еника · НУИ „Добри Христов“ · Плаза · Хай.
205: Написан квартал без кандидат-полигон (8): Империя · ЛОТОС · НИМФА · ОАЗИС · РИВИЕРА БИЙЧ (zlatni_pyasatsi) · Станкино ханче · Комитово ханче (vladislavovo) · УМБАЛ „Св. Марина“ (kk_konstantin_elena).
206: 
207: Подписаният DAG е преизмерен върху кандидат-полигоните: 10 от 11 двойки измерими, всичките ≥ 98,4 % от детето вътре в родителя (mladost2 няма полигон, двойката е инертна); петте частични припокривания дават 72,07 · 60,98 · 52,02 · 51,37 · 39,04 % — както в Б0 т. 9. **Открити 6 недекларирани припокривания, всичките под 5 %** (най-голямото balam_dere и vladislavovo, 4,94 %) — за сутрешния списък.
208: 
209: **Находки на изпълнителя и одитора:** `assigned_district` е недостижима клетка при тези входове (подписаният ред слага pin_outside_all преди нея), а `deferred_zone` също е недостижима, защото нито един отложен код няма Feature — три клетки на затворената таблица (тези две и `no_coord`) нямат нито срещане, нито фикстура. Числото 49 в леджера = 41 изхода pin_outside_all плюс 8-те „написан без полигон“.
210: 
211: ### Н2-0 · координати (мярка, без мутация)
212: 375/375 реда с координата, нула `no_coord`, нула координати извън кутията на Варна; 368 различни кадастрални тела, 7 места делят тяло. `data/place_identity.json` е недокоснат: sha256 `e8b4c836f6020d55589867e5de6d819c3e7f81a6194d0fa92f237af81b6533b6` преди == след, същият mtime. Изход 146 896 B, sha256 `60f9a9306ca1e9aec691266fd9be5408e9b3679a945ff262b9db46a7f4c2e76d`, два прогона байт-еднакви, преизчислен независимо от одитора с нула разлики. `precision_m` не се измисля.
213: 
214: ### Н3-а · фикстури (Fire_Varna)
215: 5 фикстури зелени срещу днешното поведение; пълният набор 315 теста зелен; гейтовете на репото зелени. Двете отложени са назовани: версията с Възраждане (няма родство в регистъра) и `client_cache_matrix` (браузърно поведение, няма назован изпълнител). Доказаните падания: street_collision клонът се мени (A3-street към A3-category и zone/kind) · district_retention 12 към 11 · mladost_kind_collision с квартал 6 към 7 · order_identity с квартал 6 към 7 · parent_child 11 към 10.
216: **Находка на одитора:** при `order_identity` и `mladost_kind_collision` падането идва от броя с квартал, не от подредбата; редът наистина се мени (сравнението по множество би минало зелено и това е записано в самата фикстура). `_meta.engine.sha256` се записва, но никой не го сверява — пинът е декоративен, докато смяната на двигателя се лови косвено през числата.
217: 
218: ### Н4 · сградите (мярка) **[БЕЗ ОДИТОР]**
219: Входове (sha256 в изхода): таблица `f7ee3e07…`, тела `d0c83360…`, полигони `4f466b92…`, регистър `7d217401…`. Манифест на `data/` и `web/`: 467 файла, дайджест `a6cc9eb7dfcc0d98e705e43004a81b187e9f865f478a9f75dba5b7966e1bcaaa`, преди == след.
220: 80 497 сгради в таблицата · 31 116 с непразен кадастрален квартал · 49 381 без · 60 кандидат-полигона · 1 545 тела в две и повече зони (от тях 226 с декларирано родство).
221: Затворената таблица: **съвпада 15 764 (50,7 %) · не съвпада 10 112 (32,5 %) · няма полигон 4 532 (14,6 %) · само район 708 (2,3 %)**.
222: Разбивка на „не съвпада“: 7 131 име срещу полигон · 2 828 написаният код няма кандидат-полигон · 153 полигонът е родител или дете по декларираното родство · 60 низът-свидетел повтаря написаното.
223: Поименните несъгласия на §7: Кайсиева/Владиславово 114 · Акчелар/Виница 933 · курорт/квартал Чайка 0 · многозначен низ, разрешен от полигона 988.
224: Най-големите несъгласия (написан код към кода на най-малкия съдържащ полигон): galata към borovets_yug 2 045 · trakata към evksinograd 1 197 · briz към sveti_nikola 1 022 · vinitsa към akchelar 933 · trakata към sredna_traka 703 · vinitsa към manastirski_rid 602 · dobreva към vinitsa_sever 524 · vazrazhdane към vazrazhdane1 219.
225: Низове „само район“: 157 различни, най-чести „в.з. Варна“ 141 и вариантите на „вилна зона“ 195 общо.
226: Нула кадастрални идентификатори и нула координати в изхода (проверка C6 на гейта); AST-обходът потвърждава, че скриптът няма нито едно пишещо извикване.
227: 
228: ---
229: 
230: ## 3 · Част Б — заварено състояние (НЕ е лот на този доклад)
231: 
232: Мандатът на Н5 е доклад за нощта; лотовете Б са изпълнявани от други агенти и **до Н5 не е стигнал нито техен запис, нито одит**. Затова тук стои само измереното сега, read-only — **[БЕЗ ОДИТОР]**:
233: 
234: - **Б1 · два комита във varna_3d:** `2800a7cf3f8aa4d301956b7879c54bc35b8bb25b` (`build: assemble quarters_signed.geojson from decisions 3 (sha ec2813e1c074) with D1 schema for imported geometry`; файлове `.gitignore`, `src/build_quarters_signed.py`) и `791b0cb2ccc509e5ff75bf195fe9806a1eaba0c6` (`gates: qa_quarters_signed with negative fixtures`; файлове `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`), и двата с автор `Claude Executor <executor@local>`.
235: - **Стейджнат за комита на Петър (D16/G4):** `data/quarters_signed.geojson` — 291 024 B, sha256 `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1` (индексът и работният файл са байт-еднакви). Проверен наново тази нощ от изпълнителя на Н5: `python src/qa_quarters_signed.py data/quarters_signed.geojson --registry <регистър>` → изход 0, 18 проверки, 61 Feature-а, 68 решения, 16 отложени, блоб на решенията `ec2813e1c074…`; `python -m unittest tests.test_quarters_signed_fixtures` → 7 теста, изход 0. **Отрицателни фикстури за Б1 не са преизпълнени от Н5** — гейтът без доказано падане не е приет за зелен по §0 т. 6; иска се одит преди Gate 2.
236: - **Б2-0 (Б0 т. 11) е НЕЗАВЪРШЕН:** `src/place_identity.py` е променен, но **не е комитнат**; съществува кандидат `data/place_identity.candidate.json` (240 134 B, sha256 `1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761`); резервното копие на самоличността е на подписания път в scratchpad-а и е байт-еднакво с живия файл (`e8b4c836…`). **Подмяна НЕ е извършена** — живият `data/place_identity.json` е с sha от началото на нощта.
237: - **Б2, Б3, Б4 не са тръгвали:** `data/fire_varna_places.json` (`329310f5…`), `data/fire_varna_hotels.json` (`46a44ce8…`) и леджерът (`d5050f1c…`) са с непроменени sha; кръпката `scratch/places_search/b3_patch_07.09.diff` не съществува.
238: - **Мръсното дърво на varna_3d:** три проследени промени — `scratch/place_bodies/qa_place_bodies.md` (заварена отпреди нощта, недокосната), `src/place_identity.py` (Б2-0, некомитнат) и стейджнатият `data/quarters_signed.geojson`.
239: 
240: ---
241: 
242: ## 4 · Спрели лотове, обявени отклонения и оставени дългове
243: 
244: - **Н3-б СПИРА нарочно** (план §3): нов код или нов източник без подредената тройка на D13 изхвърля 150 места мълчаливо, а 41 потвърдени кода липсват в затворения списък на картата.
245: - **Отложени фикстури:** версията на `parent_child` с Възраждане (няма родство в регистъра) и `client_cache_matrix` (браузърно поведение).
246: - **Обявено отклонение №1 (Н0, чуждо на лота):** червеното на първия прогон на Н0 е изчистено с промяна на `.gitignore` в комит `57ab8ebff32038028c98dfe8a8044c63dac2b3b8` от `Claude Architect` — извън write-set-а на който и да е лот. По същество е поправка на първопричината (седемте геометрични пътя вече наистина се игнорират, нула проследени файлове са скрити с това), но е промяна на политика в проследен файл в нощ от мерки — **иска изричната дума на Петър на Gate 2**.
247: - **Обявено отклонение №2 (Н1):** allow-списъкът от едно име при не-уикимапийски ред с остатъчни уикимапийски полета.
248: - **Обявено отклонение №3 (Н5, този лот):** гейтът на доклада е допълнен с две по-строги проверки — всеки записан изходен код носи име и команда, и докладът трябва да цитира sha256 на подписаното тяло на плана. Двете правят гейта по-строг, не по-мек.
249: - **Известни пропуски на гейтовете (за амандамент, не за нощта):** пинове с празен списък входове минават мълчаливо (Н0); `_meta.engine.sha256` не се сверява от никого (Н3-а); три клетки на затворената таблица са недостижими при днешните входове (Н2); проверката „нула проследена геометрия“ обхожда седем декларирани пътя, не цялото репо — във Fire_Varna има един по-стар проследен геометричен файл, комитнат от Петър на 02.09 и вече в `origin/main`.
250: - **Дългове от §5 на плана, непроменени:** решенията нямат ред за атрибуция; `_meta.base_rev` липсва в леджера; веригата назад към предходния файл с решения е скъсана (предшественикът липсва на диска).
251: 
252: ---
253: 
254: ## 5 · Какво прави Петър сутринта
255: 
256: 1. **Комит на геометрията (G4/D16).** `C:/git/varna_3d` — `data/quarters_signed.geojson` е СТЕЙДЖНАТ и чака неговия комит; готово съобщение: `data: signed quarter boundaries v1 (decisions 3, sha ec2813e1c074)`. Преди комита да сравни sha на файла с `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1` и да реши дали приема Б1 без преизпълнени отрицателни фикстури (виж §3).
257: 2. **Износите.** Няма стейджнат износ — Б2 не е тръгвал; `data/fire_varna_places.json`, `data/fire_varna_hotels.json` и леджерът са непроменени. Ако иска износ с квартали, първо трябва да реши какво става с незавършеното Б2-0 (кандидатът за самоличността и некомитнатият `src/place_identity.py`): да го довърши с G9 или да го отмени (копиране на резервното копие върху `data/place_identity.json` и сверка на sha `e8b4c836…`; днес двете са еднакви, така че отмяната е изтриване на кандидата и връщане на скрипта).
258: 3. **Препотвърждаване на решенията по sha.** `git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json` дава `ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6` — **подписва се БЛОБЪТ**, не работният файл (работният е с други знаци за край на ред и друг sha). В същия файл влиза липсващият ред за атрибуция, в нов комит, чийто sha той препотвърждава.
259: 4. **Преглед на дифа в трите репа.** Fire_Varna: 48 комита напред и **2 назад** — сливането с `origin/main` е негово решение. varna_3d: 47 напред, клон `rezhimi`. Varna_buildings: 1 напред, регистърът недокоснат. Да погледне поименно шестте нощни комита и стейджнатата геометрия.
260: 5. **Б3 като ЕДИН атомен комит** с неговите подписи (търсене по квартал, разширеният списък кодове, редът за атрибуция в картончето, доставката по подредената тройка) — нощес нищо от него не е пипано и кръпка не е оставена.
261: 6. **Регистърът** (`Varna_buildings/config/quarter_registry.json`, непокътнат): Ваялар като alias · Евксиноград и Траката (конфликтът на имена) · Цветен квартал · липсващите родители (Възраждане 1–4, Розова долина) · 16-те кода без решение. Плюс новото: 6 недекларирани припокривания под 5 % и решенията от §5 на плана (схема за внесена геометрия, кое хеш-правило, Младост 2, районът, името на десетия ключ, precision_m, разширяването на списъка кодове).
262: 7. **Gate 2 и пуш.** Пълният набор (315 теста) и `python -m gates.run_gates` са зелени сега; пушът е само негов — нито един агент не е пипал `origin`.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; paths=['C:/git/Fire_Varna/docs/activeContext.md','C:/git/varna_3d/AGENTS.md','C:/git/varna_3d/CLAUDE.md']; [(print('\\nFILE '+s+'\\n'+Path(s).read_text(encoding='utf-8'))) for s in paths]\"" in C:\git
 succeeded in 0ms:

FILE C:/git/Fire_Varna/docs/activeContext.md
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
one test that reads `signed_by`, and it is the fixture the plan asked for:
an unsigned artefact → `gates.release` BLOCKED.

## Waiting for a signature

- **Фаза A of the cleanup plan** — the four artefacts listed above; then `--freeze` once, tests green, `run_gates` green, audit, and Petar's push. `docs/plans/ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md` §A.4.
- `decisions/007_address_path_v2.md` — `Proposed — awaiting Petar (Gate 1)`.
- `decisions/005_sw_cache_lifecycle.md` — `Proposed — awaiting Petar (Gate 1)`.
- `plans/hotels_search_plan.md`, `plans/sw_cache_lifecycle_fixes.md` — `DRAFT — AWAITING PETAR SIGNATURE (Gate 1)`.
- ADR 009 „Идентичност, подписи, гейтове“ — Фаза B of the cleanup plan, not written yet.

Parked scope (nothing opens until Фаза A is pushed): `plans/PARKED.md`.

## Forbidden here

`git push`, Worker deploy, any publish — Petar only. Personal data in `data/`, in issues or in docs. New runtime or build-time dependencies, Bulgarian UI wording changes, a first load over 5 MB — not without Petar. Cross-repo edits from this checkout. `--freeze` on the search reference without a signed manifest. Writing `signed_by: "Петър"` — an agent writes `pending — Петър` and nothing else.

## Where things are

`index.html` (the whole app shell) · `data/hydrants.json` (runtime dataset) · `data/{places,hotels,place_categories}.json` (the places search, delivered from varna_3d) · `data/search_index.json` + `data/address_rows.json` (built in Varna_buildings) · `gates/` (the release gates: sha pins, key sets, cadastral scan, coverage, signed facts) · `worker/` (Cloudflare Worker source) · `sw.js` (ADR 002/005) · `scratch/places_search/` (the reference engine, the manifests, the boards) · `docs/decisions/` (ADRs) · `docs/plans/` (the task contracts) · `docs/archive/` (frozen chronicles).

Doctrine shared with Varna_buildings: ADR 004 → Varna_buildings ADR 058. varna_3d generates the places delivery and consumes the hydrants for its 3D map.


FILE C:/git/varna_3d/AGENTS.md
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
`src/qa_no_extrude.py` and by the generation tools `src/gen_rekey.py`, `src/gen_promote.py`, `src/gen_archive.py`
(`git grep -n 'ПЛАН_П2в_терена.md' -- src`).

**A decision is a file, never an ad-hoc change.** An architecture or scope
decision becomes its own document under `docs/decisions/`, on the model of
`C:\git\Varna_buildings\CLAUDE.md` § "ADR & scratch hygiene": an accepted
decision is never rewritten (status stamps only), the status vocabulary is
closed, and the index row is updated in the same commit as the decision.

**Commit messages.** The subject line is ≤ 72 characters. The recorded exception is the
commits of the 01.09 plan, whose subjects start with `ЛОТ ` or `docs: 71` (`git log --format=%s | grep -cE '^(ЛОТ |docs: 71)'`) —
their texts were fixed in the plan before each commit. Older subjects average far above
72 characters (`git log -50 --format=%s | python -c "import sys;L=[len(x) for x in sys.stdin.read().splitlines()];print(sum(L)/len(L))"` — characters, not bytes). The narrative belongs
in the body of the commit or in the document, not in the subject.

## Output budget (token discipline)

Context cost here is dominated by tool output, not by files or prompts.
Hard rules:

1. **Search capped.** `rg` always with `--max-count 20 --max-columns 200`.
   Start with `rg -l` (file list only), then read matches selectively.
2. **Read ranges, never whole files.** Use `sed -n 'A,Bp'`, `head -n 100`,
   or `Get-Content -TotalCount 100`. Max 150 lines per read; for a large
   file, read only the range you need.
3. **Data and logs are size-gated.** `head`/`tail` samples of data files
   are fine; never output a whole file over 1 MB (`*.log`, `*.jsonl`,
   `*.db`, `*.csv`, binaries), and never read `.git/`, the generated meshes
   and tiles under `output/`, or the probe screenshots under
   `scratch/web_probes/` — the tracked reports under `output/` are documents,
   not build output, and are readable. There is no `node_modules/` in this
   repo: the vendored web libraries are in `web/vendor/`. A log check is
   `tail -n 50`, once.
4. **One question per command.** If a capped result is insufficient,
   refine ONCE with a narrower query — never re-run with broader flags
   or raised caps. Still insufficient → state what is missing in your
   answer instead of searching further.
5. **Prefer what is already in context** over re-reading the same file.
6. **Escape hatch:** if the task explicitly names a file or module for
   exhaustive review, sequential ranged reads of the whole target are
   allowed.


FILE C:/git/varna_3d/CLAUDE.md
# CLAUDE.md — Executor guide for Varna 3D

Read [AGENTS.md](AGENTS.md) first for roles and gates, [DATA.md](DATA.md) for
what the data actually contains, [README.md](README.md) for scope.

## Orientation — what · trunk · forbidden · entry point · live numbers

- **What this repo is** — `AGENTS.md`, section *What this repo is*.
- **Trunk** — `AGENTS.md`, section *The trunk*. Whichever branch it turns out to be, an
  agent never pushes it (`AGENTS.md`, hard rule 1).
- **Forbidden here** — the hard rules are in `AGENTS.md`; the executor-side list is
  *Before you build a mesh* and *When to stop and ask* below.
- **Entry point** — `AGENTS.md`, section *Entry point*. Today it is `СЪСТОЯНИЕ.md` in
  the repo root; LOT 4 of the plan of 2026-09-01 moves it to `docs/СЪСТОЯНИЕ.md`, and
  after LOT 5 the entry point becomes `docs/activeContext.md`.
- **Live numbers** — `AGENTS.md`, section *Live numbers*. The rule for this file: **no
  state number enters it** — no count of buildings, sections, entrances, commits, QA
  scripts or tracked files. A number the work needs is measured with its own command
  (`AGENTS.md`, hard rule 5); it is never copied out of a document.

## Where things are

| What | Path |
|---|---|
| KAIS shapefiles (BGS2005) | `C:\git\Varna_buildings\data\extracted\` |
| Derived outputs (age, OSM links, clusters) | `C:\git\Varna_buildings\output\` |
| Quarter/district layer | `C:\git\m6000_private\number_viewer\quarters_layer.geojson` |
| Sensitive (cadnum-bearing) | `C:\git\m6000_private\` — **stays there** |
| Bridge to Sol | `C:\git\bridge\` (`to_gpt/`, `from_gpt/`, `ЖУРНАЛ.md`) |
| State (entry point) | `СЪСТОЯНИЕ.md` in the repo root — see **Orientation** above (LOT 4 moves it to `docs/СЪСТОЯНИЕ.md`) |
| Repo gates | `src/qa_*.py`. Mandatory before every commit under a signed plan: `qa_no_cad_ids.py`, which judges every tracked file (`git ls-files`) for cadastral identifiers — the exceptions are enumerated with their reason in its `ALLOW` block — and `qa_no_extrude.py`, which judges `data/no_extrude_verdicts.json`. `scrub_cad_ids.py` masks identifiers and keeps the audit trail |
| Map, locally | `Varna 3D.bat` → `serve.py` on port 8791, serving `C:\git`, opens `web/index.html`. Not `python -m http.server`: PMTiles needs HTTP Range (byte serving) |

## Reading the shapefiles — the two traps

```python
# UTF-8, not cp1251. Wrong encoding renders Cyrillic as "Р–РёР»РёС‰РЅР°".
r = shapefile.Reader(path, encoding="utf-8", encodingErrors="replace")
```

Coordinates are **BGS2005**. Reproject with `pyproj` before anything else, and
validate the result against the Varna bounding box — stop the build if it fails.

## Style

- **Python 3.10+**, `pyshp` / `pyproj` / `shapely` / `trimesh` / `numpy` /
  `scipy` / `Pillow` / `mapbox_earcut` / `rasterio`. No system GDAL of its own; `rasterio` ships GDAL inside its wheel.
- **Code and comments in English.** Bulgarian only in docs and UI text.
- **One concern per script.** Pipeline scripts in `src/`, probes in `scratch/`.
- **Reproducible.** Everything regenerable from the KAIS extract + free sources.
- **No silent failure.** Validate, then write. Never write, then hope.

## Before you build a mesh

1. Is Phase 0 (licensing) signed? If not, stop and say so.
2. Does the step have a signed plan? If not, you are the Planner, not the
   Executor — write the plan, do not edit.
3. Does the output contain any `cadnum`? If yes, it stays in `m6000_private`.

## When to stop and ask

- An acceptance check fails and there is no obvious safe fix.
- A licence turns out to forbid the intended use.
- A step would touch `Varna_buildings`, `Fire_Varna`, or anything outside this
  folder.
- You find state you did not create — investigate before overwriting; it may be
  Petar's work in progress.


codex
Докладът вече е остарял за Б2-0: описва кандидат и променен `src/place_identity.py` в repo-то, а те са изнесени след cleanup-а. Проверявам точните hashes и ще отделя историческия резултат от нощта от състоянието за сутрешния Gate 2.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('docs/audits/ДОКЛАД_07.09_нощна_смяна.md'); a=p.read_text(encoding='utf-8').splitlines();print('\\n'.join(f'{i+1}: {a[i]}' for i in range(130, min(len(a),245))))\"" in C:\git\Fire_Varna
 succeeded in 6ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('docs/activeContext.md'); a=p.read_text(encoding='utf-8').splitlines();print('\\n'.join(f'{i+1}: {a[i]}' for i in range(min(len(a),110))))\"; git -c core.quotePath=false status --short --branch; git diff -- src/place_identity.py; git diff --cached --name-status" in C:\git\varna_3d
 succeeded in 56ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## rezhimi...origin/rezhimi [ahead 47]
A  data/quarters_signed.geojson
 M scratch/place_bodies/qa_place_bodies.md
?? docs/sessions/ПРОМПТ_20.08.md
?? scratch/refactor/_addr/_measure_pal13.py
?? scratch/refactor/_addr/_measure_tu_campus.py
?? scratch/refactor/_addr/f0b_join_375.json
?? scratch/refactor/_addr/f0b_join_375_pass2.json
?? scratch/refactor/_addr/kimi_атака_имена_бунгала.txt
?? scratch/refactor/_addr/kimi_атака_планове.txt
?? scratch/refactor/_addr/kimi_атака_смяна2.txt
?? scratch/refactor/_addr/osm_poi_varna.md
?? scratch/refactor/_addr/post_codes_all_2018.pdf
?? scratch/refactor/_addr/post_codes_varna_2018.json
?? scratch/refactor/_addr/БОРД_противоречия.md
?? scratch/refactor/_addr/БОРД_част_от_сграда.md
?? scratch/refactor/_addr/МЯРКА_курорти_повторно.md
?? scratch/refactor/_addr/МЯРКА_хотели.md
?? scratch/refactor/_addr/ОТЧЕТ_A1_05.09.md
?? scratch/refactor/_addr/ОТЧЕТ_P7_05.09.md
?? scratch/refactor/_addr/ОТЧЕТ_P7e_05.09.md
?? scratch/refactor/_addr/ПОДГОТОВКА_адреси.md
?? scratch/refactor/_addr/РАЗСЛЕДВАНЕ_адрес.md
?? scratch/refactor/_addr/СВЕРКА_живата_карта.md
?? scratch/refactor/_addr/Т7_недовършено_19.08.patch
?? scratch/refactor/_pubbldg/func/extras_log.txt
?? scratch/refactor/_pubbldg/func/run_log.txt
?? scratch/refactor/_pubbldg/join/check_log.txt
?? scratch/refactor/_pubbldg/join/extras_log.txt
?? scratch/refactor/_pubbldg/join/run_log.txt
?? scratch/refactor/_pubbldg/join/sample.json
?? scratch/refactor/_pubbldg/plan/kimi_plan_stderr.log
?? scratch/refactor/_pubbldg/plan/sol_plan_stderr.log
?? scratch/refactor/_pubbldg/plots/plots_by_class.json
?? scratch/refactor/_pubbldg/plots/plots_pooled.json
?? scratch/refactor/_pubbldg/plots/run_log.txt
?? scratch/refactor/_pubbldg/sources/check_log.txt
?? scratch/refactor/_pubbldg/sources/measure_osm_log.txt
?? scratch/refactor/_pubbldg/sources/measure_outside_log.txt
?? scratch/refactor/_pubbldg/sources/measure_sources_log.txt
?? scratch/refactor/_pubbldg/sources/name_channels.json
?? scratch/refactor/_pubbldg/sources/osm_named_features.json
?? scratch/refactor/_pubbldg/verify/kimi_stderr.log
?? scratch/refactor/_pubbldg/verify/sol_stderr.log
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
A	data/quarters_signed.geojson

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(f'{i+1}: {a[i]}' for i in range(0,min(len(a),145))))\"" in C:\git\Fire_Varna
 succeeded in 0ms:
1: # ПЛАН НОЩНА СМЯНА · Границите (06→07.09.2026) — v2 за подпис (след Кими К22 и Astra S21)
2: 
3: **Клас: 🔴 Архитектурен. Статус: ПОДПИСАН от Петър (06.09.2026, вечерта; част А и част Б с блок Б0 т. 1–12 по препоръките).** Думите му: „подписвам и след изпълнението искам ти, кими и астра да прегледате изпълнението от различни ъгли“. Подписаното тяло: v2, sha256 на blob-а в комит 42b2635 = `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766`. Следизпълнителен преглед: архитект (Fable, дифът), Кими (данни/лиценз), Astra (механика) — записано като лот Б5. Топология: планировчик → три вътрешни оборвания (Opus) → Кими + Astra → подпис → изпълнител → независим одитор на всеки лот → Петър.
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
53: 
54: ### 2а · Договори на скриптовете (Astra S21 т. 1: „липсващ бъдещ скрипт е допустим deliverable, но с подписан интерфейс, точна команда, exit code и фикстура“)
55: | скрипт (нов, в write-set-а на лота) | команда (от корена на репото) | exit 0 означава | отрицателна фикстура (трябва да даде exit ≠ 0) |
56: |---|---|---|---|
57: | `scratch/places_search/qa_night_pins.py` (Fire_Varna) | `python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json` | всеки sha256 в пиновете е преизчислен и равен; `git check-ignore` за всеки геометричен път = игнориран; `git ls-files scratch/boundary_gallery` = 0; `base_rev` = записаният HEAD | `--pins <копие с един обърнат hex знак>` → ≠ 0; `--worktree-negative` (еднократно worktree с `git add -f` на копие на geometry-файл) → гейтът за G29 там ≠ 0 |
58: | `src/build_quarters_candidate.py` (varna_3d) | `python src/build_quarters_candidate.py --decisions <път> --frozen <път> --extra <път> --out scratch/granitsi/quarters_candidate_07.09.geojson` | файлът е написан, `_meta.artifact_class == "candidate_not_signed"`, две последователни сглобявания са байт-еднакви | `--decisions <файл с координата в ред>` → ≠ 0; `--frozen <файл с подменен връх>` → ≠ 0 |
59: | `src/qa_quarters_candidate.py` (varna_3d) | `python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --registry <път> --decisions <път>` | всички проверки от Н1 минават; 16-те `registry_pending` са ИЗКЛЮЧЕНИЕТО, формализирано: код без решение е ✗ САМО ако не е в `_meta.registry_pending` (списъкът е затворен и се сверява срещу решенията) | `tests/fixtures/qa_quarters_candidate/*.geojson` — по една фикстура на проверка (подменен `wm_id`, `declared_local_knowledge`, голо „CC BY-SA“, две кода–една геометрия, `artifact_class` друг, код извън `registry_pending` без ред) → всяка ≠ 0 |
60: | `src/measure_place_coords.py` (varna_3d) | `python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json` | 375 реда; всяка координата в 43.13–43.35 / 27.65–28.10; `sha256(data/place_identity.json)` преди == след (проверява се в скрипта и се печата) | `--bodies <файл с тяло извън кутията>` → ≠ 0; `--identity <файл без place_id>` → ≠ 0 |
61: | `src/measure_polygon_assign.py` (varna_3d) | `python src/measure_polygon_assign.py --base-rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b --polygons <кандидат> --coords <place_coords> --parents <DAG от Б0 т. 12> --out scratch/granitsi/assign_measure_07.09.json` | чете леджера през `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`; sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` преди == след; `git status --porcelain` без нови проследени промени извън write-set-а | `--polygons <кандидат с една координата, преместена в чужд квартал>` → числата се променят и `--expect <предишен изход>` дава ≠ 0; `--base-rev <несъществуващ>` → ≠ 0 |
62: | `tests/test_granitsi_fixtures.py` (Fire_Varna) | `python -m unittest tests.test_granitsi_fixtures` | петте фикстури минават върху днешното поведение | всяка фикстура има `_broken` вариант в `scratch/places_search/granitsi_fixtures_06.09.json`, който тестът пуска и очаква да ПАДНЕ (assertRaises); липсващ `_broken` = тестът е червен |
63: | `src/measure_kais_quar_vs_polygons.py` (varna_3d) | `python src/measure_kais_quar_vs_polygons.py --info web/varna_buildings_info.json --bodies web/varna_buildings_3d.geojson --polygons <кандидат>` | таблица на stdout (съвпада / не / няма полигон / само район), нула кадастрални идентификатори и координати; sha256-манифест на `data/` и `web/` преди == след | `python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py` (нов, в write-set-а на Н4): AST-обход за `open(...,'w')`, `Path.open`, `json.dump`, `shutil.*`, `os.replace/remove`, `subprocess` → ≠ 0; фикстура `tests/fixtures/readonly_ast_negative.py` с `json.dump` → ≠ 0 |
64: | Н5 (одит) | `python scratch/places_search/qa_night_acceptance.py --report docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna, в write-set-а на Н5) | всеки лот в доклада има: sha-та на write-set-а, exit кодовете на гейта и на всяка отрицателна фикстура (≠ 0), авторът на комита, съобщението дословно | доклад без ред за някой лот или с гейт без падаща фикстура → ≠ 0 |
65: 
66: **Базова ревизия (Astra S21 т. 2):** `base_rev` = **пълният HEAD на varna_3d, замразен в Н0 преди всяка промяна** — измерено сега `8d60aebb365fb8e74ccc863d3b3db90b74180a3b` (клон `rezhimi`); Н0 го записва в пиновете и проверява, че леджер-блобът и двата износа съвпадат с приетата основа; **не** се взима последният леджер-комит (`31db7b9…` — леджерът там е същият, но износите се различават). QA и манифестът (`qa_fire_varna_m6.py:48`, `lot1v_v_manifest.py:30`) четат стария леджер по константа — при Б2 кандидатът и основата се подават като изрични входове, не чрез смяна на константата. Н0 записва и **мръсния проследен диф във varna_3d** (1 файл сега) като част от основата; „празен `git status`“ не е гейт — гейтът е „нищо ново извън write-set-а“.
67: 
68: **G19 команда (Windows):** `& "C:\Program Files\GitHub CLI\gh.exe" repo view Petar1984/varna_3d --json visibility` → `{"visibility":"PRIVATE"}`; друго или празно = СТОП за целия varna_3d фронт.
69: 
70: ## 3 · Лот по лот
71: 
72: ### Н0 · Предусловия и пинове
73: `noshtna_pins_06.09.json` (нула координати) пинва `sha256` на: решенията (**плюс комита `b6e627d` и автора `Claude Architect`**), `frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson` (`b53a3322…`) **и** `granitsi_preview_05.09/wikimapia_quarters_frozen_2026-09-06_v2.geojson` — двете копия са байт-еднакви, **веригата се доказва по sha, не по име**; суровия снапшот; `m2_1_candidates_v2.json` (`1331130e…`, обявен вход на решенията); `wikimapia_extra_2026-09-06.geojson` (Евксиноград 5729429, **извън обявения frozen манифест** — записва се изрично); `mladost2_streets_proposal.geojson`; `agkk_au5_varna.geojson`; `quarter_registry.json`; `lot1v_locations_375.json`; **`base_rev` = точният комит, от който се чете леджер-блобът**. Записва се и, че `based_on` предшественикът `granitsi_decisions_2_…` липсва на диска — веригата назад е скъсана (ред в доклада, не мълчание). Плюс `git rev-list --count origin/…` за трите репа и **G19**: `"C:\Program Files\GitHub CLI\gh.exe" repo view varna_3d --json visibility` → трябва `PRIVATE`; празен изход или `PUBLIC` = СТОП за целия varna_3d фронт.
74: 
75: **Гейт Н0 (червен).** `qa_night_pins.py` преизчислява всеки sha и повтаря git-проверките. Фикстури: обърнат hex знак → ≠ 0; **`git add -f` върху копие на geometry-файл в еднократно worktree → гейтът за G29 трябва да падне ТАМ и да е зелен в реалното дърво** (`git add -n` е dry-run и не доказва нищо); подменено ИМЕ при съвпадащ sha → зелено, подменен sha → червено.
76: 
77: ### Н1 · Кандидат-геометрия (varna_3d, частно, НЕподписано)
78: Един Feature на **уикимапийски** потвърден код: **60 кода** (59 + Евксиноград). **Младост 2 НЕ влиза** — D2 (`ADR:40`) казва „по улици“ → ЗАКЛЮЧЕН ВИНАГИ, отключва се само с изричен подписан ключ, а G1 има точно тази отрицателна фикстура; излиза като `deferred` и поименно в §5. Полета: `code`, `name`, `kind`, `source: "wikimapia"`, `wm_id`, **`raw_geometry_sha256`** (пренесен от решенията) **и** `wm_polygon_sha256_d1` (пресметнат по канонизацията на D1) — двете правила се записват отделно, разликата е обявено отклонение за Петър; `url`, `fetched_at`, `confirmed_by/at`, `chosen_reason`; **`licence` дословно** по амандамент №2 §3.8 и К21 т. 3–4: `"CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)"` + етикета за доброволци/неофициален извор/URL на условията/дата; `attribution` низът; `parent` от регистъра след **явна стъпка дисплей→код с гейт** (непознат дисплей = червено), а за код с родител без полигон (`borovets_sever`, `borovets_yug`) — `parent_geometry_check: "няма родителски полигон"`. **`precision_m` НЕ се измисля** (0/68 в решенията) — Feature-ът носи `precision_m: null` и лотът не го замества с литерал. **`district` НЕ се пише** (виж §5 т. 4); вместо това мярка: за всеки кандидат кой `nationalcode` го съдържа. `_meta`: `artifact_class: "candidate_not_signed"`, `decisions_state: "agent_committed_proba (b6e627d, Claude Architect)"`, манифест на входовете, `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict, position}`, `registry_pending` с **16-те кода без решение поименно**.
79: 
80: **Гейт Н1 (червен).** Предгейтове: **G19** (частно репо), **G3** (`qa_no_cad_ids.py` — задължителен преди всеки комит по CLAUDE.md на varna_3d). Фикстури: подменен връх при непроменен sha (за ВСЕКИ от двата хеш-ключа поотделно, всеки срещу своя източник) · подменен `wm_id` · `deferred` код с Feature и Feature без ред · **жилищен код от регистъра без ред в решенията → ✗, поименно** · координата във файла с решения · липсващ ред за атрибуция · **не-уикимапийски ред с непразно `wm_*` → ✗** · **входен Feature със `source: "declared_local_knowledge"` → ✗** (етикетът е отменен от амандамент №2 §3.7) · голо „CC BY-SA“ или липсващ `terms` → ✗ · една геометрия към два несравними кода · BOM/CRLF/несортирани ключове · две сглобявания дават байт-еднакъв файл · **`_meta.artifact_class ≠ "candidate_not_signed"` → ✗**.
81: 
82: ### Н2-0 · Координати — МЯРКА, без мутация
83: `place_identity.json` **не се докосва** (игнориран, състояние, генераторът чете сам себе си). Отделен скрипт извежда `place_id → lat/lon` от същите връзки, които идентичността вече носи (`site_id`/`kais_i` → представителна точка на тяло в `web/varna_buildings_3d.geojson`), и пише САМО в `scratch/granitsi/place_coords_07.09.json`. Място без връзка → `no_coord`, брои се, не се гади. **Гейт:** 375 реда; всяка координата в кутията 43.13–43.35 / 27.65–28.10; sha256 на `data/place_identity.json` идентичен преди и след. Фикстури: координата извън кутията → ✗; липсващ `place_id` → ✗.
84: 
85: ### Н2 · Присвояване — САМО ЧИСЛА, нула запис
86: Скриптът чете **блоба** `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json` (не работния файл), кандидат-полигоните и координатите, и брои. `fire_varna_locations.py` **не се редактира**; леджерът **не се презаписва**. Правила на мярката: празен квартал + точно един полигон → „би получил“; **място в ≥ 2 полигона БЕЗ декларирано родство → `disputed`** (7-те недекларирани вложености); „най-малкият печели, детето преди родителя“ важи САМО за 6-те декларирани двойки; написан ≠ полигон → `disputed`; **няма полигон → редът си остава с вече написания район** (нищо не се извежда от АГКК); ръбът се брои в **три ленти 50/100/250 m** и трите числа влизат в доклада, докато Петър не подпише `precision_m`. **Гейт:** sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` **идентични преди и след**; `git status --porcelain` в varna_3d празен извън write-set-а.
87: 
88: **Десетият ключ на `_meta` НЕ се специфицира и НЕ се пуска.** Причина: подписваният източник го нарича с ДВЕ имена — амандамент №2 §3.3 (`licence_quarter_boundary`) и §5/G27 (`quarter_attribution`), а фикстурата на G27 отхвърля `_meta` с 11 ключа. Едното трябва да умре с думата на Петър (§5 т. 5).
89: 
90: ### Н3-а · Фикстури (Fire_Varna) — днешното поведение, не приемане
91: Пет фикстури: `street_collision`, `district_retention`, `mladost_kind_collision`, `order_identity`, **`parent_child` върху двойка с ДНЕС регистрирано родство** (`mladost`/`mladost2`) — версията с Възраждане се отлага, защото vazrazhdane1..4 нямат `parents`. **`client_cache_matrix` се отлага** с назована причина: браузърно поведение, а единственият node-изпълнител в `tests/` е `test_data_ascii_mojibake.py`; лотът не назовава втори. Всяка фикстура пада върху нарочно счупен кандидат и мутацията влиза дословно в доклада. **Гейт:** `python -m unittest discover -s tests` (310+ зелени) И `python -m gates.run_gates` без червено — иначе сутрешният пуш на Петър е блокиран от собствената му кука. Записва се изрично: **това фиксира ДНЕШНОТО поведение; утре F13 ще ги направи кандидат-очаквания, не приемане.**
92: 
93: **Н3-б СПИРА (нарочно).** Търсенето по квартал и редът за атрибуция в картончето не тръгват: нов `src` или нов код без подредената тройка на D13 изхвърля 150 места мълчаливо, а измереното е по-лошо от очакваното — **41 кода липсват в `QUARTER_CODES`**, три от тях са днес местности.
94: 
95: ### Н4 · Сградите — САМО мярка
96: Вход: `web/varna_buildings_info.json` (речниково кодирана колона `quar`, `build_places.py:78-96`) + **`web/varna_buildings_3d.geojson`** (телата, поименно) + кандидат-полигоните. За всяка сграда с непразен `quar`: съвпада / не съвпада / няма полигон / само район. Изход: **stdout**; нула кадастрални идентификатори, нула координати. **Гейт (червен):** AST-проверка за извикване на пишеща функция (не grep — `json.dump(obj, fp)`, `Path.open("w")`, `shutil.copy` минават през списък от низове), с фикстура-вариант, който пише през `json.dump` → ✗; плюс sha256-манифест на **всичко под `data/` и `web/`** преди и след и `git status --porcelain` празен.
97: 
98: ### Н5 · Одит и доклад
99: Одитор (Opus, read-only, различен агент) на всеки лот: преизпълнява гейтовете, сверява дифа срещу write-set-а (**всеки допълнителен файл = находка**), проверява автора, съобщението и `git log --format=%an -1 --` върху пътя на решенията срещу `_meta`. **Разделение:** одиторът дава числата, изпълнителят ги записва без да ги тълкува. Докладът носи: числата на Н1, Н2 (по трите ленти), Н3-а (5/5 + доказаните падания + двете отложени), Н4, всички sha, поименния списък на спрелите лотове с причината, и §„Какво прави Петър сутринта“.
100: 
101: **Атрибуция в проследените артефакти:** всеки нощен проследен файл на Fire_Varna, който назовава уикимапийски обект, носи ред за атрибуция по §3.8 (ключ `attribution` в JSON, заглавен ред в MD) — ToS §1.G важи и когато github.com рендерира файла в браузър. Вече комитнатият `granitsi_decisions_3_…json` (60 `wm_id` + заглавия) няма такъв ред: **това е сутрешен дълг, не нощна поправка.**
102: 
103: ## 4 · Нарушения, които спират нощта веднага
104: 
105: Опит за `git push` · геометрия в проследен файл на Fire_Varna · редакция на регистъра · промяна на написан квартал · запис в `lot1v_locations_375.json`, `place_identity.json` или `data/fire_varna_*.json` · файл на име `quarters_signed.geojson` · Feature по метод „по улици“ · нов публичен `src` **или нов квартален КОД** без разширен `QUARTER_CODES` и подредената тройка на D13 · низът `10135` в **публична** доставка (в частния провенанс и в мярката е позволен — иначе АГКК изворът е неназовим) · зелен гейт без падаща отрицателна фикстура.
106: 
107: ## 5 · Сутринта (решенията за Петър, ако Б0 НЕ е подписан тази вечер)
108: 
109: 1. **Схемата за ВНЕСЕНА геометрия** (кои от 21-те полета на D1 отпадат и с какво се заместват) — амандамент, без който няма подписан артефакт.
110: 2. **Кое правило е `wm_polygon_sha256`** — суровият хеш (днешният в решенията) или канонизацията на D1.
111: 3. **Младост 2**: подписан ключ по D2 + лиценз (ODbL, „© OpenStreetMap contributors“) + под на `precision_m` за уличен метод.
112: 4. **Районът**: от нашия `district.code` (375/375 съгласие) с явен `district_src`, или от АГКК — тогава `_meta.source_terms["agkk_inspire_au5"]` се попълва и G22/G23 стават червени предгейтове.
113: 5. **Едно име за десетия ключ** (`licence_quarter_boundary` или `quarter_attribution`) и низът за атрибуция; картата да е независима от извора `{code:{src,url,label,licence}}`, за да носи и ODbL, и АГКК.
114: 6. **`precision_m`** — стойност и довод (от нея зависи кой е `edge_pending`).
115: 7. **Разширяването на `QUARTER_CODES`** с 41-те кода и какво става с `morska_gradina`, `sveti_nikola`, `zelenika`, които днес са местности.
116: 8. **Решенията**: `git mv` на днешния блоб под подписан път (не втори блоб с втора sha) или подпис на днешния път.
117: 9. Регистърът: Ваялар→alias, Евксиноград/Траката, Цветен квартал, `parents` за Възраждане 1–4 и Розова долина, 16-те без решение.
118: 10. Дългове: D10 твърди, че `_check_pins` (`:623-639`) сверява `inputs` — не ги сверява; `_meta.base_rev` липсва в леджера; `granitsi_decisions_3` няма ред за атрибуция.
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
137: ### Б1 · Сглобяване (varna_3d, частно) — `data/quarters_signed.geojson`
138: Изпълнител: Claude Executor. Write-set: `src/build_quarters_signed.py`, `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`, `.gitignore` (`!data/quarters_signed.geojson`), `data/quarters_signed.geojson`. Съобщения: `build: assemble quarters_signed.geojson from decisions 3 (sha <…>) with D1 schema for imported geometry` · `gates: qa_quarters_signed with negative fixtures`. Съдържание: 61 Feature (60 Уикимапия + Младост 2 по ключа от Б0 т. 3), полетата по Б0 т. 1–4, 6; `_meta`: `artifact_class: "signed_by_plan_signature"`, `decisions_sha256`, `decisions_commit`, манифест на входовете (frozen v2, extra 5729429, mladost2 face, agkk_au5 само като свидетел), `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict: "allowed_with_conditions", position}`, `parent_child[]` (Б0 т. 9), `registry_pending[]`. Байтове по G30 (UTF-8 без BOM, sorted keys, compact, финален LF; две сглобявания = байт-еднакви). **Гейт (червен):** предгейтове G19 (`gh repo view varna_3d --json visibility` = PRIVATE) и G3 (`qa_no_cad_ids.py`); G25-а (двата хеша поотделно, подменен връх → ✗, подменен `wm_id` → ✗), G26 (биекция решения ↔ трите множества на D4 с `declared_streets`→polygon, `alias_of`/`deferred`→`_meta`; всеки код от регистъра има решение или е в `registry_pending`, поименно), G27(а) (низът по амандамент №2 §3.8 във всеки Feature), D1 (21 полета, `null` само където Б0 т. 1 позволява; `drawn_*` непразно при внос → ✗), лиценз (голо „CC BY-SA“ → ✗), една геометрия към два кода → ✗, `precision_m` липсва → ✗, метод „по улици“ без `mladost2` → ✗. Комитът на `data/quarters_signed.geojson` е **на Петър** по D16/G4: изпълнителят го оставя стейджнат с готово съобщение (`data: signed quarter boundaries v1 (decisions 3, sha <…>)`) и го записва в доклада; всичко след Б1 чете файла по sha, не по комит.
139: 
140: ### Б2 · Присвояване P8-а (varna_3d) — тръгва само с подписано Б0 т. 11; изходите са КАНДИДАТИ за комита на Петър
141: Write-set: `src/fire_varna_locations.py` (каналът `SIGNED_POLYGON` + `DISTRICT_FALLBACK`, четене на `quarters_signed.geojson` по sha; `LEDGER` сочи НОВ датиран леджер `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` с `_meta.base_rev` = комитът на стария; старият не се пипа), `src/qa_p8a.py`, `data/fire_varna_places.json`, `data/fire_varna_hotels.json` (износът), `data/fire_varna_location_inputs.json` (пиновете, вкл. `quarters_signed.geojson` sha), новият леджер. Съобщения: `feat(p8a): SIGNED_POLYGON channel with district fallback, new dated ledger, written quarters untouched` · `data: places export with quarter_attribution (decisions 3)`. Правила: само ПРАЗЕН квартал се пише; най-малкият съдържащ полигон; двойка без подписано родство и място в двата → `disputed`, не се пише; ръб `max(50, precision_m)` → `edge_pending`; без полигон → районът само по Б0 т. 4 (i)–(iii): не в зони на отложени кодове, не при `pin_outside_all` без съгласен свидетел, и винаги заместим; записан ≠ полигон → леджер `disputed`, редът непроменен (G17). Гейт: fallback-ред в зона на отложен код → ✗; fallback-ред, защитен от G17 в следваща версия → ✗ (фикстура с втора версия, в която подписан полигон трябва да го замести). Координати: САМО от `place_identity.json` след хода по Б0 т. 11 (G9 зелен); изнесените координати са забранени за присвояване (D7) — гейт: скриптът не отваря `data/fire_varna_*.json` за четене на координати (AST-проверка като в Н4). Изходите на таблицата по Б0 т. 12 се броят и записват поименно. Десетият ключ по Б0 т. 5 във varna_3d: `META_KEYS` (places 9→10, hotels 7→8 — измерено от Astra), двата износителя (`export_fire_varna_places.py:816`, `export_fire_varna_hotels.py:420`), QA/M6 и `build_place_categories.py` (родители и полигонен провенанс) в един varna_3d комит на изпълнителя; **износените данни (`data/fire_varna_*.json`, новият леджер) остават стейджнати за комита на Петър** (D16/G4) с готово съобщение в доклада. **Гейт (червен):** G17 (всеки записан квартал в стария леджер-блоб `git show <base_rev>:…` е байт-равен в новия износ), G4 (fail-closed без подпис → тук подписът е този план + sha на решенията, записани в `_meta`), `qa_fire_varna_places_export.py` с 10 ключа, брой присвоени = броят „би получил“ от Н2 (мярката и резултатът трябва да съвпадат до място), `edge_pending` и `disputed` в леджера поименно, `python -m unittest` зелен.
142: 
143: ### Б3 · Търсене по квартал F13 (Fire_Varna) — СУТРИНТА, не нощес (Astra S21 т. 4–5: доставката е един атомен комит с подписи, които само Петър дава)
144: Write-set: `index.html` (`QUARTER_SRC`, `QUARTER_CODES` +41, `PLACES_CACHE` v7, нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`), `data/places.json`, `data/hotels.json` (доставката от Б2 по подредената тройка на D13: пинове + `expectations.json` + двата преписа), `tests/test_granitsi_fixtures.py` (шестте S17 фикстури, вкл. `client_cache_matrix` в node — изпълнителят назовава изпълнителя), `release/sign` артефактите по гейта на доставката от 05.09. Съобщения: `feat(search): quarter search over signed boundaries, attribution row, QUARTER_CODES +41, cache v7` · `data: places delivery with quarter_attribution (D13 ordered)` · `tests: S17 fixtures fail on broken candidates`. Пълният write-set по Astra S21 т. 4: трите data файла (`places.json`, `hotels.json`, **`place_categories.json`**), `index.html` (`PLACES_CACHE` v7, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци `:6265`, зареждане/валидиране `:6528`, атрибуцията в паметта `:6657`, D12/индекс/търсене и картончето `:7253`; **типово правило за `DISTRICT_FALLBACK`** — районен код в `quarter` не бива да чупи `!quarter` условието на районното търсене `:7064`), двата bundle теста (`test_places_public_bundle.py:55`, `test_hotels_public_bundle.py:61`), `expectations.json`, трите манифеста, референтният/паритетният корпус и Python паритетът на търсенето (D13 `:62`). Нощес изпълнителят **подготвя** дифа като кръпка (`scratch/places_search/b3_patch_07.09.diff`, непроследена) и фикстурата `client_cache_matrix.foreign_code_while_other_bundle_valid` (Node: валидни хотели, кеш v6/v7, crypto on/off; приемане = двата булеви валидатора минават И 150+225 реда реално се индексират; чужд код → наблюдаем отказ, не `places2=[]` мълчаливо). **Гейт (сутрин, след комитите и подписите на Петър):** замразената референция (нула изгубени резултати), шестте фикстури падат на счупен кандидат и минават след, `python -m unittest discover -s tests` и `python -m gates.run_gates` зелени, размерът ≤ 5 MB, никаква геометрия в проследените `data/*.json` на Fire_Varna (grep за `coordinates` в тях → 0 извън `data/hydrants.json`).
145: 

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('src/measure_kais_quar_vs_polygons.py'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(f'{i+1}: {s}' for i,s in enumerate(a) if s.startswith(('def ','class ','import ','from ')) or any(t in s for t in ['write','ArgumentParser','add_argument','manifest','json.dump'])))\"; Get-Content -Encoding UTF8 -LiteralPath 'src/qa_readonly_ast.py' -TotalCount 140" in C:\git\varna_3d
 succeeded in 15ms:
be an AST walk and NOT a grep: `json.dump(obj, fp)`, `Path.open("w")` and
`shutil.copy` all pass a list of forbidden strings — `json.dump` is spelled the
same as `json.dumps`, `open` appears in `.open(` and in comments, and a grep for
"write" hits every docstring in the house. The parser is the only reader that
knows a CALL from a word.

    python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py

Exit 0 = no write-capable call found in any given file. Exit 1 = the findings,
each with its line number and the name of the rule it broke. A file that does
not parse is a finding too — an unparsable file has proven nothing.

The negative fixture is tracked next to the code: `tests/fixtures/readonly_ast_negative.py`
is a copy of an honest measure with ONE `json.dump` in it, and the gate must
exit non-zero on it. A gate whose negative fixture has not actually run and
actually failed is not a gate.

What counts as write-capable (a closed, named list — an unknown mechanism is a
finding for the next amendment, not a silent pass):

  * `open(...)` with a mode that contains `w`, `a`, `x` or `+`, and `open(...)`
    whose mode is not a literal (a mode that cannot be read cannot be trusted);
  * any `.open(...)` method call — `Path.open` is named by the plan, and the
    receiver of a method call is not knowable from the syntax alone;
  * `json.dump` (the file writer; `json.dumps` builds a string and is allowed);
  * any call on `shutil` and on `subprocess`, plus `os.system`/`os.popen`;
  * the writing half of `os`: `replace`, `remove`, `rename`, `unlink`, `mkdir`,
    `makedirs`, `rmdir`, `removedirs`, `truncate`, `write`, `chmod`, `link`,
    `symlink`, `utime`;
  * `.write(...)`, `.writelines(...)`, `.write_text(...)`, `.write_bytes(...)`,
    `.unlink(...)`, `.rename(...)`, `.replace(...)`, `.mkdir(...)`,
    `.touch(...)`, `.rmdir(...)` — except when the receiver is written literally
    as `sys.stdout` or `sys.stderr` (printing is not writing to the repo).
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WRITE_MODE_CHARACTERS = set("wax+")

FORBIDDEN_MODULES = {"shutil", "subprocess"}

FORBIDDEN_OS_FUNCTIONS = {
    "system", "popen", "replace", "remove", "rename", "renames", "unlink",
    "mkdir", "makedirs", "rmdir", "removedirs", "truncate", "write", "chmod",
    "link", "symlink", "utime",
}

FORBIDDEN_METHODS = {
    "open", "write", "writelines", "write_text", "write_bytes", "unlink",
    "rename", "replace", "mkdir", "touch", "rmdir",
}

# `print` writes to stdout; so does an explicit `sys.stdout.write`. The report of
# a measure IS stdout, so these two receivers are the one allowance, and it is
# syntactic: only the literal `sys.stdout` / `sys.stderr` passes.
ALLOWED_WRITE_RECEIVERS = {"sys.stdout", "sys.stderr"}


def dotted_name(node: ast.AST) -> str:
    """`sys.stdout` → "sys.stdout"; anything else that is not a plain dotted path → ""."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = dotted_name(node.value)
        return f"{base}.{node.attr}" if base else ""
    return ""


def mode_argument(call: ast.Call) -> ast.AST | None:
    if len(call.args) >= 2:
        return call.args[1]
    for keyword in call.keywords:
        if keyword.arg == "mode":
            return keyword.value
    return None


def findings_in(source: str, path: Path) -> list[str]:
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as error:
        return [f"{path}:{error.lineno}: файлът не се разбира от парсера ({error.msg})"]

    found: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module = node.module if isinstance(node, ast.ImportFrom) else None
            names = [module] if module else [alias.name for alias in node.names]
            for name in names:
                head = (name or "").split(".")[0]
                if head in FORBIDDEN_MODULES:
                    found.append(f"{path}:{node.lineno}: внос на `{head}` — модул за писане/изпълнение")
            continue
        if not isinstance(node, ast.Call):
            continue

        target = dotted_name(node.func)

        if target == "open" or target.endswith(".open") and target.split(".")[0] == "io":
            mode = mode_argument(node)
            if mode is None:
                continue  # no mode = "r"
            if isinstance(mode, ast.Constant) and isinstance(mode.value, str):
                if WRITE_MODE_CHARACTERS & set(mode.value):
                    found.append(f"{path}:{node.lineno}: `open(..., {mode.value!r})` — режим за писане")
            else:
                found.append(f"{path}:{node.lineno}: `open(...)` с неизвестен режим — не се доказва четене")
            continue

        head = target.split(".")[0] if target else ""
        if head in FORBIDDEN_MODULES:
            found.append(f"{path}:{node.lineno}: `{target}(...)` — извикване на {head}")
            continue
        if head == "os" and target.split(".")[-1] in FORBIDDEN_OS_FUNCTIONS and target.count(".") == 1:
            found.append(f"{path}:{node.lineno}: `{target}(...)` — пишеща функция на os")
            continue
        if target in {"json.dump", "pickle.dump"}:
            found.append(f"{path}:{node.lineno}: `{target}(...)` — записва във файлов обект")
            continue

        if isinstance(node.func, ast.Attribute) and node.func.attr in FORBIDDEN_METHODS:
            receiver = dotted_name(node.func.value)
            if receiver in ALLOWED_WRITE_RECEIVERS:
                continue
            shown = receiver or "<израз>"
            found.append(f"{path}:{node.lineno}: `{shown}.{node.func.attr}(...)` — пишещ/отварящ метод")
    return found


def main() -> int:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; python src/qa_readonly_ast.py tests/fixtures/readonly_ast_negative.py" in C:\git\varna_3d
 succeeded in 0ms:
✓ ГЕЙТ READ-ONLY ЗЕЛЕН · 1 файла · нула пишещи извиквания (open с режим за писане · .open · json.dump/pickle.dump · shutil · subprocess · пишещите функции на os · .write/.write_text/.unlink/.rename/.mkdir и роднините им)

 exited 1 in 0ms:
✗ ГЕЙТ READ-ONLY ЧЕРВЕН — 1 находки:
  ✗ tests\fixtures\readonly_ast_negative.py:34: `json.dump(...)` — записва във файлов обект

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'write|rmtree|mkdir|subprocess|argparse|def main|check_' scratch/places_search/qa_night_acceptance.py" in C:\git\Fire_Varna
 succeeded in 0ms:
8:carries the sha256 values of its write-set, the exit code of its gate and of every negative
15:  * a copy with one flipped hex character in a write-set sha256,
24:write-set paths are parsed out of the SIGNED plan, so a report that renames a lot's message
27:The gate reads only; it never writes into any of the three repositories.
32:import argparse
36:import subprocess
92:    proc = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
118:    """Drop '(...)' spans: the plan uses them for outputs that are NOT in the write-set."""
228:def main():
229:    parser = argparse.ArgumentParser(description="Гейт Н5: приемане на нощния доклад.")
347:        # --- write-set: every plan path present, every sha recomputed ---
351:            "C7 %s·write-set пълен" % lot,
358:            "C7 %s·write-set без чужди пътища" % lot,
507:            "C10 %s·комитът е write-set-ът" % lot,

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('docs/audits/ДОКЛАД_07.09_нощна_смяна.md'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(f'{i+1}: {a[i]}' for i in range(245,len(a))))\"" in C:\git\Fire_Varna
 succeeded in 0ms:
246: - **Обявено отклонение №1 (Н0, чуждо на лота):** червеното на първия прогон на Н0 е изчистено с промяна на `.gitignore` в комит `57ab8ebff32038028c98dfe8a8044c63dac2b3b8` от `Claude Architect` — извън write-set-а на който и да е лот. По същество е поправка на първопричината (седемте геометрични пътя вече наистина се игнорират, нула проследени файлове са скрити с това), но е промяна на политика в проследен файл в нощ от мерки — **иска изричната дума на Петър на Gate 2**.
247: - **Обявено отклонение №2 (Н1):** allow-списъкът от едно име при не-уикимапийски ред с остатъчни уикимапийски полета.
248: - **Обявено отклонение №3 (Н5, този лот):** гейтът на доклада е допълнен с две по-строги проверки — всеки записан изходен код носи име и команда, и докладът трябва да цитира sha256 на подписаното тяло на плана. Двете правят гейта по-строг, не по-мек.
249: - **Известни пропуски на гейтовете (за амандамент, не за нощта):** пинове с празен списък входове минават мълчаливо (Н0); `_meta.engine.sha256` не се сверява от никого (Н3-а); три клетки на затворената таблица са недостижими при днешните входове (Н2); проверката „нула проследена геометрия“ обхожда седем декларирани пътя, не цялото репо — във Fire_Varna има един по-стар проследен геометричен файл, комитнат от Петър на 02.09 и вече в `origin/main`.
250: - **Дългове от §5 на плана, непроменени:** решенията нямат ред за атрибуция; `_meta.base_rev` липсва в леджера; веригата назад към предходния файл с решения е скъсана (предшественикът липсва на диска).
251: 
252: ---
253: 
254: ## 5 · Какво прави Петър сутринта
255: 
256: 1. **Комит на геометрията (G4/D16).** `C:/git/varna_3d` — `data/quarters_signed.geojson` е СТЕЙДЖНАТ и чака неговия комит; готово съобщение: `data: signed quarter boundaries v1 (decisions 3, sha ec2813e1c074)`. Преди комита да сравни sha на файла с `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1` и да реши дали приема Б1 без преизпълнени отрицателни фикстури (виж §3).
257: 2. **Износите.** Няма стейджнат износ — Б2 не е тръгвал; `data/fire_varna_places.json`, `data/fire_varna_hotels.json` и леджерът са непроменени. Ако иска износ с квартали, първо трябва да реши какво става с незавършеното Б2-0 (кандидатът за самоличността и некомитнатият `src/place_identity.py`): да го довърши с G9 или да го отмени (копиране на резервното копие върху `data/place_identity.json` и сверка на sha `e8b4c836…`; днес двете са еднакви, така че отмяната е изтриване на кандидата и връщане на скрипта).
258: 3. **Препотвърждаване на решенията по sha.** `git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json` дава `ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6` — **подписва се БЛОБЪТ**, не работният файл (работният е с други знаци за край на ред и друг sha). В същия файл влиза липсващият ред за атрибуция, в нов комит, чийто sha той препотвърждава.
259: 4. **Преглед на дифа в трите репа.** Fire_Varna: 48 комита напред и **2 назад** — сливането с `origin/main` е негово решение. varna_3d: 47 напред, клон `rezhimi`. Varna_buildings: 1 напред, регистърът недокоснат. Да погледне поименно шестте нощни комита и стейджнатата геометрия.
260: 5. **Б3 като ЕДИН атомен комит** с неговите подписи (търсене по квартал, разширеният списък кодове, редът за атрибуция в картончето, доставката по подредената тройка) — нощес нищо от него не е пипано и кръпка не е оставена.
261: 6. **Регистърът** (`Varna_buildings/config/quarter_registry.json`, непокътнат): Ваялар като alias · Евксиноград и Траката (конфликтът на имена) · Цветен квартал · липсващите родители (Възраждане 1–4, Розова долина) · 16-те кода без решение. Плюс новото: 6 недекларирани припокривания под 5 % и решенията от §5 на плана (схема за внесена геометрия, кое хеш-правило, Младост 2, районът, името на десетия ключ, precision_m, разширяването на списъка кодове).
262: 7. **Gate 2 и пуш.** Пълният набор (315 теста) и `python -m gates.run_gates` са зелени сега; пушът е само негов — нито един агент не е пипал `origin`.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; "'$env:PYTHONDONTWRITEBYTECODE='"'1'; @'
import sys, runpy, os
blocked = {'os.remove','os.rename','os.rmdir','os.mkdir','os.chmod','os.utime','os.link','os.symlink','shutil.rmtree','shutil.copyfile'}
def readonly(event,args):
    if event in blocked:
        raise PermissionError('S22 read-only audit: '+event)
    if event == 'open':
        mode=args[1]; flags=args[2]
        if (isinstance(mode,str) and any(c in mode for c in 'wax+')) or (isinstance(flags,int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND)):
            raise PermissionError('S22 read-only audit: file write')
sys.addaudithook(readonly)
sys.argv=['src/measure_kais_quar_vs_polygons.py','--info','web/varna_buildings_info.json','--bodies','web/varna_buildings_3d.geojson','--polygons','scratch/granitsi/quarters_candidate_07.09.geojson']
runpy.run_path(sys.argv[0],run_name='__main__')
'@ | python -B -" in C:\git\varna_3d
 succeeded in 8816ms:
МЯРКА Н4 · кадастралният `quar` срещу кандидат-полигоните (read-only)
  входове: info sha256 f7ee3e072ee1d51f831f7067058e962e558f1c9daa8660ed4dcac6f6df27df20
           тела sha256 d0c8336061601cdeba2d2905a19187bb052a4aae3f539797e7525bc1651ed1dc
           полигони sha256 4f466b92abaa93cb725ff5d1b7255661bda7f4d6e73c510a5d8f0c637e706522
           регистър sha256 7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6
  клас на кандидата: candidate_not_signed · основа: 8d60aebb365fb8e74ccc863d3b3db90b74180a3b
  манифест data/+web/: 466 файла · дайджест a35a7a7fec048319fe8ee1beb313ba27f0724ef04c07ba020e9288fa18a5bdd4 (преди == след)

сгради в таблицата: 80497 · с непразен quar: 31116 · без quar: 49381
кандидат-полигони: 60 кода · тела в ≥ 2 полигона: 1545 (от тях с декларирано родство: 226)

ТАБЛИЦА (затворена — всяка сграда с непразен quar получава точно един изход):
  съвпада         15764   50.7%
  не съвпада      10112   32.5%
  няма полигон     4532   14.6%
  само район        708    2.3%
  общо            31116

разбивка на „не съвпада“ по вид:
    7131  име срещу полигон
    2828  написаният код няма кандидат-полигон (отложен/registry_pending)
     153  полигонът е родител или дете по декларираното родство
      60  улицата се сверява до същия код като написания quar (низът-свидетел повтаря написаното)

поименните несъгласия на §7 (броят се само когато и написаното, и полигонът са в семейството):
     114  Кайсиева/Владиславово
     933  Акчелар/Виница
       0  курорт/квартал Чайка
     988  многозначен низ, разрешен от полигона (влиза в „съвпада“ — тук е Чайка и Траката)

топ 15 несъгласия (написан код → код на най-малкия съдържащ полигон):
    2045  galata → borovets_yug
    1197  trakata_so|trakata_vz → evksinograd
    1022  briz → sveti_nikola
     933  vinitsa → akchelar
     703  trakata_so|trakata_vz → sredna_traka
     602  vinitsa → manastirski_rid
     524  dobreva → vinitsa_sever
     219  vazrazhdane → vazrazhdane1
     207  trakata_so|trakata_vz → gorna_traka
     202  galata → fichoza
     196  vilite → asparuhovo
     183  sveti_nikola → briz
     136  vinitsa → perchemliyata
     128  priboy → fichoza
     125  vazrazhdane → vazrazhdane4

топ 10 низа „само район“ (не се сверяват до квартал в регистъра):
     141  в.з. Варна
     102  "Вилна зона"
      67  вилна зона
      43  м. БАБА АЛИНО
      26  кв. "Вилна зона"
      17  м. ФРАНГА ДЕРЕ
      10  к.к. СВ.СВ. КОНСТАНТИН И ЕЛЕНА, ГРАО 0
       8  "ЗАПАДНА ПРОМИШЛЕНА ЗОНА-ЮГ"
       8  к.к. "Св. Константин и Елена", ул. 56
       7  к.к. "ЗЛАТНИ ПЯСЪЦИ" Х-Л "ИНТЕРНАЦИОНАЛ"
  различни такива низа: 157

✓ ГЕЙТ Н4 ЗЕЛЕН · 7 проверки: C1 входове · C2 клас на кандидата · C3 таблица↔тела 1:1 · C4 кодове/геометрия · C5 затворена таблица · C6 нула кадастрални идентификатори и координати · C7 манифест data/+web/ преди == след

codex
Commit проверката потвърди дословните Executor messages. Допълнителните QA файлове за Н4/Н5 са разрешени в §2а; реалното отклонение е `.gitignore` в `57ab8eb`. Н4 даде същите числа при повторен read-only прогон, но текущият файлов манифест е 466 файла вместо 467 след изнасянето на кандидата.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('scratch/places_search/qa_night_acceptance.py'); a=p.read_text(encoding='utf-8').splitlines();print('\\n'.join(f'{i+1}: {a[i]}' for i in range(85,158))); print('\\n'.join(f'{i+1}: {a[i]}' for i in range(495,min(len(a),552))))\"" in C:\git\Fire_Varna
 succeeded in 0ms:
86:             h.update(block)
87:     return h.hexdigest()
88: 
89: 
90: def run(args, cwd=None):
91:     """Run a git command and return (exit_code, stdout, stderr) as text."""
92:     proc = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
93:     return (
94:         proc.returncode,
95:         proc.stdout.decode("utf-8", "replace"),
96:         proc.stderr.decode("utf-8", "replace"),
97:     )
98: 
99: 
100: class Report(object):
101:     """Collects the verdict lines; any red line makes the gate red."""
102: 
103:     def __init__(self):
104:         self.failed = 0
105:         self.checks = 0
106: 
107:     def check(self, name, ok, detail=""):
108:         self.checks += 1
109:         if ok:
110:             print("[ЗЕЛЕНО] %s%s" % (name, (" — " + detail) if detail else ""))
111:         else:
112:             self.failed += 1
113:             print("[ЧЕРВЕНО] %s%s" % (name, (" — " + detail) if detail else ""))
114:         return ok
115: 
116: 
117: def strip_parentheticals(text):
118:     """Drop '(...)' spans: the plan uses them for outputs that are NOT in the write-set."""
119:     out = []
120:     depth = 0
121:     for ch in text:
122:         if ch == "(":
123:             depth += 1
124:         elif ch == ")":
125:             if depth:
126:                 depth -= 1
127:         elif depth == 0:
128:             out.append(ch)
129:     return "".join(out)
130: 
131: 
132: def parse_plan(plan_text):
133:     """Parse the §2 lot table of the signed plan.
134: 
135:     Returns {code: {"repo": str, "paths": [str], "message": str}} in plan order.
136:     """
137:     lots = {}
138:     order = []
139:     in_table = False
140:     for line in plan_text.split("\n"):
141:         if line.startswith("| Лот |"):
142:             in_table = True
143:             continue
144:         if in_table:
145:             if not line.startswith("|"):
146:                 break
147:             cells = [c.strip() for c in line.strip().strip("|").split("|")]
148:             if len(cells) < 4:
149:                 continue
150:             if set(cells[0]) <= set("-: "):
151:                 continue
152:             code = cells[0].split()[0]
153:             repo = cells[1]
154:             paths = [
155:                 p
156:                 for p in re.findall(r"`([^`]+)`", strip_parentheticals(cells[2]))
157:                 if "/" in p and not p.endswith("/")
158:             ]
496:                 "-c",
497:                 "core.quotepath=false",
498:                 "show",
499:                 "--name-only",
500:                 "--format=",
501:                 commit,
502:             ],
503:             cwd=root,
504:         )
505:         touched = sorted(p for p in out.split("\n") if p.strip())
506:         rep.check(
507:             "C10 %s·комитът е write-set-ът" % lot,
508:             touched == sorted(p for p, _s in block["files"]),
509:             "комитнати: %s" % ", ".join(touched),
510:         )
511: 
512:     # --- C11: the report is tied to the SIGNED body of the plan ----------------
513:     # The plan records the sha256 of the body Petar signed; a report that does not
514:     # quote it cannot be attributed to a signed plan.
515:     signed_sha = None
516:     for line in plan_text.split("\n"):
517:         if "Подписаното тяло" in line:
518:             found = re.findall(r"[0-9a-f]{64}", line)
519:             if found:
520:                 signed_sha = found[0]
521:             break
522:     rep.check(
523:         "C11 подпис·тялото на плана",
524:         bool(signed_sha) and signed_sha in report_text,
525:         "подписано тяло: %s" % (signed_sha or "планът не обявява sha"),
526:     )
527: 
528:     print("")
529:     if rep.failed:
530:         print(
531:             "ГЕЙТ Н5: ЧЕРВЕН — паднали проверки: %d от %d" % (rep.failed, rep.checks)
532:         )
533:         return 1
534:     print("ГЕЙТ Н5: ЗЕЛЕН — %d проверки" % rep.checks)
535:     return 0
536: 
537: 
538: if __name__ == "__main__":
539:     sys.exit(main())

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; import hashlib,json; root=Path('C:/Users/Petar/AppData/Local/Temp/claude/C--git/26f42576-326e-4863-b700-f1e02c26a0c9/scratchpad'); p=root/'b20_inflight_2026-09-07';print(json.dumps([dict(path=str(x),bytes=x.stat().st_size,sha256=hashlib.sha256(x.read_bytes()).hexdigest()) for x in p.iterdir() if x.is_file()],ensure_ascii=False,indent=2)); print('repo_candidate_exists',Path('C:/git/varna_3d/data/place_identity.candidate.json').exists());print('repo_qa_exists',Path('C:/git/varna_3d/src/qa_place_identity_coords.py').exists())\"" in C:\git
 succeeded in 3ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; "'$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:GIT_OPTIONAL_LOCKS='"'0'; @'
import subprocess,sys
p=subprocess.run([sys.executable,'-B','scratch/places_search/qa_night_acceptance.py','--report','docs/audits/ДОКЛАД_07.09_нощна_смяна.md'],capture_output=True,text=True,encoding='utf-8')
lines=p.stdout.splitlines()
print('\\n'.join(s for s in lines if '[ЧЕРВЕНО]' in s or 'ГЕЙТ Н5:' in s))
if p.stderr: print(p.stderr[-1800:])
print('EXIT_CODE',p.returncode)
raise SystemExit(p.returncode)
'@ | python -B -" in C:\git\Fire_Varna
 exited 1 in 58ms:

EXIT_CODE 2

codex
G9 е възпроизведен: точно 77 `zone` + 77 `key`. Два прогона без координати дават еднакъв резултат, който съвпада с кандидата след махане на четирите coordinate keys — причината е стара identity база спрямо преместените входове. Б1 QA е зелен и 26 налични отрицателни fixtures падат; unittest setup-ът обаче опитва да изтрие и пресъздаде fixture директорията, затова read-only защитата го спря.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; "'$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:GIT_OPTIONAL_LOCKS='"'0'; @'
import subprocess,sys
p=subprocess.run([sys.executable,'-B','scratch/places_search/qa_night_acceptance.py','--report','docs/audits/ДОКЛАД_07.09_нощна_смяна.md'],capture_output=True,text=True,encoding='utf-8')
print(p.stdout[:1800]); print(p.stderr[:1800]); print('EXIT_CODE',p.returncode)
raise SystemExit(p.returncode)
'@ | python -B -" in C:\git\Fire_Varna
 exited 1 in 60ms:
[ЧЕРВЕНО] C1 доклад — липсва файл: docs/audits/??????_07.09_?????_?????.md


EXIT_CODE 2

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; "'$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:GIT_OPTIONAL_LOCKS='"'0'; "'$env:GIT_CONFIG_COUNT='"'1'; "'$env:GIT_CONFIG_KEY_0='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_0='"'*'; @'
from pathlib import Path
import subprocess,sys
report=next(Path('docs/audits').glob('*07.09*'))
p=subprocess.run([sys.executable,'-B','scratch/places_search/qa_night_acceptance.py','--report',str(report)],capture_output=True,text=True,encoding='utf-8')
print('\\n'.join(s for s in p.stdout.splitlines() if '\\u0427\\u0415\\u0420\\u0412\\u0415\\u041d\\u041e' in s or '\\u0413\\u0415\\u0419\\u0422 \\u041d5:' in s))
print(p.stderr[-600:]);print('EXIT_CODE',p.returncode)
raise SystemExit(p.returncode)
'@ | python -B -" in C:\git\Fire_Varna
 succeeded in 324ms:
ГЕЙТ Н5: ЗЕЛЕН — 107 проверки

EXIT_CODE 0

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('src/build_quarters_signed.py'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(f'{i+1}: {a[i]}' for i in range(440,511)))\"; git -c core.quotePath=false diff --name-only; git -c core.quotePath=false diff --cached --name-only" in C:\git\varna_3d
 succeeded in 27ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
data/quarters_signed.geojson

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONIOENCODING='"'utf-8'; python -B -c \"from pathlib import Path; p=Path('docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'); a=p.read_text(encoding='utf-8').splitlines(); print('\\n'.join(f'{i+1}: {a[i]}' for i in range(123,134)))\"; git status --short --untracked-files=no" in C:\git\Fire_Varna
 succeeded in 5ms:
codex
**Присъда: НЕГОДНО за окончателно приемане на цялото изпълнение.** Конкретният Б1 артефакт е годен, а спирането на G9 е правилно. Остават нератифицирано отклонение, две слабости в QA и неточен текущ отчет. Няма установена повреда на защитените данни.

1. **Commit-и, write-set-и и ограничения**

Всички посочени Executor commit-и имат дословните съобщения и автора `Claude Executor <executor@local>`:

- Fire_Varna: `a454b60`, `093b259`, `c6c5d44`.
- varna_3d: `0fed1e0`, `fb59f8d`, `524fe31`, `5e468a1`, `2800a7c`, `791b0cb`.

Write-set-ите съвпадат с **целия договор**. `qa_readonly_ast.py` и `readonly_ast_negative.py` са разрешени в §2а, както и `qa_night_acceptance.py`; отсъствието им от кратката таблица не ги прави чужди файлове. Б1 разрешава и `.gitignore`. [План:43](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:43), [План:63](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:63), [План:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138).

**Истинското отклонение е Fire_Varna `.gitignore`, `57ab8eb`, автор `Claude Architect`.** Поправката отстранява причината за червения Н0, но е извън подписаните write-set-и. **F1: изрична ратификация от Петър**, със запазена следа за отклонението. Докладът правилно го признава. [Доклад:246](C:/git/Fire_Varna/docs/audits/ДОКЛАД_07.09_нощна_смяна.md:246).

Има и първи Н5 commit `65a0c7a`, заменен съдържателно от `c6c5d44`. Следователно част А има **8 Executor commit-а плюс architect fix**, а Б1 добавя два. „Шестте нощни комита“ е грешна инвентаризация.

Защитените SHA съвпадат с Н0: registry `7d217401…`, ledger `d5050f1c…`, identity `e8b4c836…`, exports `329310f5…`/`46a44ce8…`, завареният dirty `qa_place_bodies.md` — `51b0f4d9…`. Няма промяна на написаните квартали. [Пинове:75](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:75), [Пинове:237](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:237), [Пинове:305](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:305).

Няма **нова** геометрия в нощните tracked Fire файлове. Буквалното repository-wide „нула геометрия“ обаче е нарушено още преди нощта: `scratch/pozarna_gz/pozarna_gz_wgs84.geojson`, 321 Point Features, внесен от Петър с `614fb34`, вече в `origin/main`. Не е установен push; локалната история сама не доказва отсъствие на всякакъв push attempt.

2. **Б1: артефактът съответства на Б0**

[Index и worktree](C:/git/varna_3d/data/quarters_signed.geojson:1) са байт-еднакви: **291024 B, 61 Features**, SHA256 `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1`. Две сглобявания в паметта възпроизвеждат същите байтове.

Потвърдени са:

- 21 D1 полета; седемте `null` са `drawn_by`, `drawn_at`, `basemap`, `viewport`, `visible_layers`, `screenshot_sha256`, `approval_digest`. `witnesses` е попълнен. [План:124](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:124).
- Каноничният `wm_polygon_sha256` и отделният `raw_geometry_sha256` са проверени независимо. [QA:145](C:/git/varna_3d/src/qa_quarters_signed.py:145).
- `mladost2`: подписаният `street_bounded_face`, четирите улици, `ODbL © OpenStreetMap contributors`, `precision_m:50`; останалите 60 имат precision 100. [Builder:457](C:/git/varna_3d/src/build_quarters_signed.py:457).
- Районът е изчислен срещу нашите пет района: **0/61 пространствени разминавания**. DAG — точно 11 двойки; `registry_pending` — точно 16; `artifact_class:"signed_by_plan_signature"`. [Builder:283](C:/git/varna_3d/src/build_quarters_signed.py:283), [QA:388](C:/git/varna_3d/src/qa_quarters_signed.py:388).

Изпълнената QA команда:

```text
python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna
```

**Exit 0**, 18 проверки. Всички **26 налични отрицателни fixtures дават exit 1** с очакваната проверка.

`python -m unittest tests.test_quarters_signed_fixtures`, изпълнен през wrapper със забрана на мутации: **exit 1, Ran 0 tests**. `setUpClass` опитва `shutil.rmtree(FIXTURES)` и пресъздаване на директорията — несъвместимо с този read-only преглед. [Tests:103](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:103). Еквивалентите на седемте сценария са проверени без записи; това **не е** оригинален unittest exit 0.

Две възпроизведени слабости в `791b0cb`: **C1 приема `signed_body_sha256` от 64 нули**, а **C18 приема допустим, но пространствено неверен район**. Текущият артефакт е правилен. **F2: exact plan pin и spatial district verification, с отрицателни fixtures; отделно успешно изпълнение на оригиналния suite в изолирана среда с разрешени тестови записи.** [QA:93](C:/git/varna_3d/src/qa_quarters_signed.py:93), [QA:398](C:/git/varna_3d/src/qa_quarters_signed.py:398).

3. **G9: преместен вход → реално разминаване със старата база**

Identity е tracked, последно променена в `756d166` от 04.09. `e613089` от 05.09 променя точно **5 places +72 hotels zones**. Генераторът чете тези `zone` и ги включва в `key`. [Generator:172](C:/git/varna_3d/src/place_identity.py:172), [Generator:187](C:/git/varna_3d/src/place_identity.py:187).

Паркираният G9 даде **exit 1: 77 `zone` +77 `key`, никакви други некоординатни промени**. Два no-coordinate прогона в паметта са еднакви и съвпадат с кандидата след премахване на четирите coordinate keys; **0 нови IDs**. Това отхвърля недетерминизма като причина.

Правилният сутрешен ход е **отделно подписано освежаване на identity базата**, review на 154-те промени, отделен commit, нов backup/SHA, после координатният кандидат и непроменен G9. Контролирайте и `registry_manifest.json`: обикновеното `main()` пише и него. [Generator:1259](C:/git/varna_3d/src/place_identity.py:1259).

Fresh no-coordinate comparison е полезен диагностичен контрол. Самостоятелната подмяна на comparator-а би прикрила реалния старо→ново delta; подписаният договор изисква сравнение с backup и допуска само четирите ключа. [План:134](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:134).

4. **F3: addendum към `c6c5d44`**

Н5 QA още дава **exit 0, 107 проверки**, въпреки остарелия разказ. Н4 е независимо преизпълнен: **exit 0**, същите числа; AST **0**, отрицателна fixture **1**. Следният един абзац трябва да замени текущото оперативно описание на Б2-0 и cleanup-а: [Доклад:236](C:/git/Fire_Varna/docs/audits/ДОКЛАД_07.09_нощна_смяна.md:236).

> След architect cleanup Б2-0 остава спрян на G9 заради 154 некоординатни промени от стара identity база спрямо обновените входове. `src/place_identity.py` е възстановен до HEAD; candidate, QA и diff са запазени в `scratchpad/b20_inflight_2026-09-07/`, кандидатът със SHA `1141bbc2…`. Живата identity остава `e8b4c836…`; подмяна няма. Tracked промените във varna_3d са само staged `quarters_signed.geojson` и завареният dirty `qa_place_bodies.md`. Н4 числата се възпроизвеждат; текущият data/web манифест е 466 файла, digest `a35a7a7f…`, след изнасянето на кандидата. Б1 QA и 26 отрицателни fixtures са независимо проверени; оригиналният unittest е блокиран от read-only защитата. Продължаването изисква одобрена нова identity база.

Коригирайте също броя commit-и и твърдението за липсващ predecessor: `decisions_2` съществува; прекъсването е неговото `based_on:null`. Б0 решенията вече са подписани и не трябва да се представят като нерешени.

5. **Сутрешният push и merge редът**

Fire е **48 ahead/2 behind**. Remote ingest `1af2140`/`18948de` са patch-идентични с локалните `b6866e5`/`fa7a6c0`. Петте ingest файла съвпадат между tips; read-only `merge-tree` даде **exit 0, празен резултат**.

Петър първо сверява remote и прави **обикновен merge на `origin/main`**, запазвайки pinned SHA; ingest не се повтаря. После поправките, актуалните gates и Gate 2. При нов attribution blob трябва да се обнови и провери производната SHA верига. Частният артефакт и евентуалният Б2 предхождат атомната публична доставка Б3; staged геометрията чака commit на Петър. [План:131](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:131), [План:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138).
tokens used
103,318
**Присъда: НЕГОДНО за окончателно приемане на цялото изпълнение.** Конкретният Б1 артефакт е годен, а спирането на G9 е правилно. Остават нератифицирано отклонение, две слабости в QA и неточен текущ отчет. Няма установена повреда на защитените данни.

1. **Commit-и, write-set-и и ограничения**

Всички посочени Executor commit-и имат дословните съобщения и автора `Claude Executor <executor@local>`:

- Fire_Varna: `a454b60`, `093b259`, `c6c5d44`.
- varna_3d: `0fed1e0`, `fb59f8d`, `524fe31`, `5e468a1`, `2800a7c`, `791b0cb`.

Write-set-ите съвпадат с **целия договор**. `qa_readonly_ast.py` и `readonly_ast_negative.py` са разрешени в §2а, както и `qa_night_acceptance.py`; отсъствието им от кратката таблица не ги прави чужди файлове. Б1 разрешава и `.gitignore`. [План:43](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:43), [План:63](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:63), [План:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138).

**Истинското отклонение е Fire_Varna `.gitignore`, `57ab8eb`, автор `Claude Architect`.** Поправката отстранява причината за червения Н0, но е извън подписаните write-set-и. **F1: изрична ратификация от Петър**, със запазена следа за отклонението. Докладът правилно го признава. [Доклад:246](C:/git/Fire_Varna/docs/audits/ДОКЛАД_07.09_нощна_смяна.md:246).

Има и първи Н5 commit `65a0c7a`, заменен съдържателно от `c6c5d44`. Следователно част А има **8 Executor commit-а плюс architect fix**, а Б1 добавя два. „Шестте нощни комита“ е грешна инвентаризация.

Защитените SHA съвпадат с Н0: registry `7d217401…`, ledger `d5050f1c…`, identity `e8b4c836…`, exports `329310f5…`/`46a44ce8…`, завареният dirty `qa_place_bodies.md` — `51b0f4d9…`. Няма промяна на написаните квартали. [Пинове:75](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:75), [Пинове:237](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:237), [Пинове:305](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:305).

Няма **нова** геометрия в нощните tracked Fire файлове. Буквалното repository-wide „нула геометрия“ обаче е нарушено още преди нощта: `scratch/pozarna_gz/pozarna_gz_wgs84.geojson`, 321 Point Features, внесен от Петър с `614fb34`, вече в `origin/main`. Не е установен push; локалната история сама не доказва отсъствие на всякакъв push attempt.

2. **Б1: артефактът съответства на Б0**

[Index и worktree](C:/git/varna_3d/data/quarters_signed.geojson:1) са байт-еднакви: **291024 B, 61 Features**, SHA256 `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1`. Две сглобявания в паметта възпроизвеждат същите байтове.

Потвърдени са:

- 21 D1 полета; седемте `null` са `drawn_by`, `drawn_at`, `basemap`, `viewport`, `visible_layers`, `screenshot_sha256`, `approval_digest`. `witnesses` е попълнен. [План:124](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:124).
- Каноничният `wm_polygon_sha256` и отделният `raw_geometry_sha256` са проверени независимо. [QA:145](C:/git/varna_3d/src/qa_quarters_signed.py:145).
- `mladost2`: подписаният `street_bounded_face`, четирите улици, `ODbL © OpenStreetMap contributors`, `precision_m:50`; останалите 60 имат precision 100. [Builder:457](C:/git/varna_3d/src/build_quarters_signed.py:457).
- Районът е изчислен срещу нашите пет района: **0/61 пространствени разминавания**. DAG — точно 11 двойки; `registry_pending` — точно 16; `artifact_class:"signed_by_plan_signature"`. [Builder:283](C:/git/varna_3d/src/build_quarters_signed.py:283), [QA:388](C:/git/varna_3d/src/qa_quarters_signed.py:388).

Изпълнената QA команда:

```text
python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna
```

**Exit 0**, 18 проверки. Всички **26 налични отрицателни fixtures дават exit 1** с очакваната проверка.

`python -m unittest tests.test_quarters_signed_fixtures`, изпълнен през wrapper със забрана на мутации: **exit 1, Ran 0 tests**. `setUpClass` опитва `shutil.rmtree(FIXTURES)` и пресъздаване на директорията — несъвместимо с този read-only преглед. [Tests:103](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:103). Еквивалентите на седемте сценария са проверени без записи; това **не е** оригинален unittest exit 0.

Две възпроизведени слабости в `791b0cb`: **C1 приема `signed_body_sha256` от 64 нули**, а **C18 приема допустим, но пространствено неверен район**. Текущият артефакт е правилен. **F2: exact plan pin и spatial district verification, с отрицателни fixtures; отделно успешно изпълнение на оригиналния suite в изолирана среда с разрешени тестови записи.** [QA:93](C:/git/varna_3d/src/qa_quarters_signed.py:93), [QA:398](C:/git/varna_3d/src/qa_quarters_signed.py:398).

3. **G9: преместен вход → реално разминаване със старата база**

Identity е tracked, последно променена в `756d166` от 04.09. `e613089` от 05.09 променя точно **5 places +72 hotels zones**. Генераторът чете тези `zone` и ги включва в `key`. [Generator:172](C:/git/varna_3d/src/place_identity.py:172), [Generator:187](C:/git/varna_3d/src/place_identity.py:187).

Паркираният G9 даде **exit 1: 77 `zone` +77 `key`, никакви други некоординатни промени**. Два no-coordinate прогона в паметта са еднакви и съвпадат с кандидата след премахване на четирите coordinate keys; **0 нови IDs**. Това отхвърля недетерминизма като причина.

Правилният сутрешен ход е **отделно подписано освежаване на identity базата**, review на 154-те промени, отделен commit, нов backup/SHA, после координатният кандидат и непроменен G9. Контролирайте и `registry_manifest.json`: обикновеното `main()` пише и него. [Generator:1259](C:/git/varna_3d/src/place_identity.py:1259).

Fresh no-coordinate comparison е полезен диагностичен контрол. Самостоятелната подмяна на comparator-а би прикрила реалния старо→ново delta; подписаният договор изисква сравнение с backup и допуска само четирите ключа. [План:134](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:134).

4. **F3: addendum към `c6c5d44`**

Н5 QA още дава **exit 0, 107 проверки**, въпреки остарелия разказ. Н4 е независимо преизпълнен: **exit 0**, същите числа; AST **0**, отрицателна fixture **1**. Следният един абзац трябва да замени текущото оперативно описание на Б2-0 и cleanup-а: [Доклад:236](C:/git/Fire_Varna/docs/audits/ДОКЛАД_07.09_нощна_смяна.md:236).

> След architect cleanup Б2-0 остава спрян на G9 заради 154 некоординатни промени от стара identity база спрямо обновените входове. `src/place_identity.py` е възстановен до HEAD; candidate, QA и diff са запазени в `scratchpad/b20_inflight_2026-09-07/`, кандидатът със SHA `1141bbc2…`. Живата identity остава `e8b4c836…`; подмяна няма. Tracked промените във varna_3d са само staged `quarters_signed.geojson` и завареният dirty `qa_place_bodies.md`. Н4 числата се възпроизвеждат; текущият data/web манифест е 466 файла, digest `a35a7a7f…`, след изнасянето на кандидата. Б1 QA и 26 отрицателни fixtures са независимо проверени; оригиналният unittest е блокиран от read-only защитата. Продължаването изисква одобрена нова identity база.

Коригирайте също броя commit-и и твърдението за липсващ predecessor: `decisions_2` съществува; прекъсването е неговото `based_on:null`. Б0 решенията вече са подписани и не трябва да се представят като нерешени.

5. **Сутрешният push и merge редът**

Fire е **48 ahead/2 behind**. Remote ingest `1af2140`/`18948de` са patch-идентични с локалните `b6866e5`/`fa7a6c0`. Петте ingest файла съвпадат между tips; read-only `merge-tree` даде **exit 0, празен резултат**.

Петър първо сверява remote и прави **обикновен merge на `origin/main`**, запазвайки pinned SHA; ingest не се повтаря. После поправките, актуалните gates и Gate 2. При нов attribution blob трябва да се обнови и провери производната SHA верига. Частният артефакт и евентуалният Б2 предхождат атомната публична доставка Б3; staged геометрията чака commit на Петър. [План:131](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:131), [План:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138).
