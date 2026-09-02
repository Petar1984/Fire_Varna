# Базова линия C0 — цикълът „местата в търсачката“ (02.09.2026)

**Лот:** C0 по `docs/plans/places_search_plan_2026-09-02.md` §4 · **гейт:** G0 (§5).
**HEAD преди лота:** `6ac2235eaadd8b31fce9b79096496a0c53ea3e69` · **клон:** `main`.
**Повторен пуск:** първият пуск на C0 спря по един червен тест; причината е измерена и описана в §4 — предсъществуващ дефект на ТЕСТА, не на кода.
Всяко число тук носи командата си. Мерено в `C:\git\Fire_Varna`, 02.09.2026.

## 1 · Мярката (какво · стойност · команда)

| какво | стойност | команда |
|---|---|---|
| HEAD | `6ac2235eaadd8b31fce9b79096496a0c53ea3e69` | `git rev-parse HEAD` |
| клон | `main` | `git rev-parse --abbrev-ref HEAD` |
| непушнати комита | 1 | `git rev-list --count origin/main..main` |
| `index.html` | 475 446 B · sha256 `0bccd106f842a35e2840d2f20734d249d1d160cbb854dac3915188b7afe1e0f0` | `wc -c index.html` · `manifest_before.json` |
| `README.md` | 14 137 B · sha256 `523ddd7ddcbae4c2abbd67dcd24b0da4ec0a6873005e3b09a66ed32de1ce1c8e` | `wc -c README.md` · `manifest_before.json` |
| `sw.js` | 11 839 B · sha256 `c83000233092d5a37625e8ce0b2806fd8f7d7cd72192072c08af4d5a9c10f430` | `wc -c sw.js` · `manifest_before.json` |
| `data/hydrants.json` | 1 313 848 B · sha256 `6191f08ecfb8c02a0aaf17191c223fbddc8b48fbfca4158555b9e90da83fced6` | `manifest_before.json` |
| `data/search_index.json` | 11 242 756 B · sha256 `c12f94259bd986dd…` | `manifest_before.json` |
| `data/address_rows.json` | 5 073 137 B · sha256 `2a4766bd474f3481…` | `manifest_before.json` |
| файлове в манифеста | **14** = `index.html`, `sw.js`, `README.md` + 10 файла на първо ниво в `data/` + `data/basemaps/basemap_manifest.json` | `manifest_before.json` (обход: `sorted(os.listdir('data'))`, само файлове) |
| първо зареждане по код | `index.html` + `data/hydrants.json` = 475 446 + 1 313 848 = **1 789 294 B** (1.71 MiB) при таван 5 MB | AGENTS.md § Runtime Architecture, ред „Frontend first load“; `index.html:1716–1718` (`loadHydrantData()` → `fetch('data/hydrants.json', { cache: 'no-cache' })`) |
| адресните payload-и в първото зареждане | **не** — `search_index.json` и `address_rows.json` се теглят lazy при първи фокус на полето | `index.html:5264–5270` (коментарът „Both lazy-load on first focus“), `index.html:1586` |
| тестове | `Ran 126 tests in 3.176s` · `OK` | `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests` |
| флаки-тестът изолирано | `Ran 1 test` · `OK` ×3 (3 последователни пуска) | `PYTHONIOENCODING=utf-8 python -m unittest tests.test_etr_kmz_adapter.DeterminismTest.test_two_runs_byte_identical` |
| mojibake `index.html` | 0 | `python -c "re.findall(r'[\u00d0\u00d1\u00c2][\u0080-\u00ff]', text)"` |
| mojibake `README.md` | 0 | същата команда |
| здраве на репото | `git fsck` — празен изход, код 0 | `git fsck --no-dangling --no-reflogs` |
| `gc.auto` | `0` | `git config gc.auto` |
| работно дърво | 3 променени + 1 неследен (§2) | `git status --short -uall` |

## 2 · Снимката на `git status --short -uall` (преди C0)

```
 M docs/plans/places_search_plan_2026-09-02.md
 M scratch/basemap_e0/e0_range.json
 M scratch/basemap_e0/e0_range_report.md
?? docs/plans/places_phase2_plan.md
```

- `docs/plans/places_search_plan_2026-09-02.md` — планът v2 (+ §10 v2.1, §11 v2.2); **write-set на C1**, не влиза в C0 и остава ` M` след него.
- `scratch/basemap_e0/e0_range.json`, `scratch/basemap_e0/e0_range_report.md` — работа на Петър; не се пипат.
- `docs/plans/places_phase2_plan.md` — планът за фаза 2 v0 (архитектът); не се пипа и не се комитва в C0.

Очакваната снимка СЛЕД C0 е същата: двата файла на C0 стават проследени и чисти, останалите четири реда не мърдат.

## 3 · Декларираните write-set-ове (план §4)

| # | write-set | съобщение | гейтове |
|---|---|---|---|
| C0 | `scratch/places_search/baseline_02.09.md`, `scratch/places_search/manifest_before.json` | `chore(search): baseline + byte manifest before the places-search cycle (02.09)` | G0 |
| C1 | `docs/plans/places_search_plan_2026-09-02.md` (v2), `docs/decisions/006_places_in_search.md` | `plan: places-in-search v2 — separate branch, own container/cache/selection; ADR 006` | — |
| C2 | `data/hotels.json`, `data/place_categories.json` | `data(search): publish the hotels bundle (226, sha 17800b5d) and the category dictionary from varna_3d` | G1 |
| C3 | `tests/test_hotels_public_bundle.py`, `tests/test_places_search_primitives.py` | `test: SHA-pinned public-bundle gate for data/hotels.json + verbatim-primitive gate for the places search` | G2, G12а |
| C4 | `index.html`, `scratch/places_search/probe_places_fv.mjs`, `scratch/places_search/probe_out/*` | `feat(search): places (hotels) as a separate result branch under the address search, behind HOTELS_SEARCH_ENABLED` | G3–G7, G12 |
| C4b (условен) | `index.html` | `feat(search): category listing, marker rule and typographic cleaning for the places branch` | G3–G5 наново |
| C5 | `README.md` | `docs: hotels source, verbatim licence line and the offline note in README (BG+EN)` | G8–G10 |
| C6 | — (одитор, само четене) | — | всички гейтове наново |

## 4 · Флаки-тестът (предсъществуващ дефект на ТЕСТА, не на кода)

`tests/test_etr_kmz_adapter.py::DeterminismTest::test_two_runs_byte_identical` пада периодично. Измерената причина:

- фикстурата `write_kmz` (`tests/test_etr_kmz_adapter.py:49`) пише ZIP-а на ред **72** — `with zipfile.ZipFile(path, "w") as z:` — без изричен `ZipInfo.date_time`, тоест `writestr` щампова **локалното време** в ZIP-хедъра; гранулацията на ZIP-времето е 2 секунди;
- адаптерът хешира самите KMZ-и и записва хеша в отчета — `scripts/import_etr_kmz.py:619` (`"sha256": f.sha256` в `kmz_files`);
- когато двата пуска на теста попаднат от двете страни на 2-секундната граница, ZIP-байтовете (значи и sha256) се различават и сравнението „байт-идентично“ пада.

**Поправката на фикстурата НЕ е в никой write-set на този цикъл** (C0–C5) — тя чака отделен подпис на Петър.

**Как се чете гейтът „тестовете OK“ до тогава:** пусни пакета; ако единственият червен е точно този тест — пусни го изолирано и запиши двата изхода; гейтът минава с бележка „125 зелени + 1 предсъществуващ флаки (документиран)“. **Всеки друг червен тест = STOP.**

Този пуск на C0: пакетът е **изцяло зелен** (`Ran 126 tests … OK`) и изолираният тест мина 3/3 — бележката за 125+1 не е потрябвала.

## 5 · Правилото за следващите лотове (G0)

Всеки следващ лот сверява `manifest_before.json` преди комита: **байт извън обявения write-set на лота = СТОП и питане**. Разрешените разлики в `git status --short -uall` са точно файловете на текущия лот, вече комитнатите файлове на предишните лотове и четирите реда от §2.
