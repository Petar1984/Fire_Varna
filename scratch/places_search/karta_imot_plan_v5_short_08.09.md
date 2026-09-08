# Планировчик v5 — къс отговор (не план), 08.09

`signable()`** | `found = sorted((REPO_ROOT/ALLOW_DIR).glob("*.json")); if len(found) == 1: table["allow"] = …` — **глоб върху РАБОТНОТО ДЪРВО; при брой ≠ 1 ключът `allow` изчезва БЕЗ грешка и БЕЗ изход ≠ 0** | мълчалив fail-open в момента на подписа | **= (не се пипа); затваря се процедурно — О16 + Б-G6б** |
| `gates/release.py:437-458 queues_in_head` | `git ls-tree -r` + глоб по **basename** | подпапка НЕ спасява | **= ; Б-G6** |
| `gates/coverage.py:87`, `:96-104` | `SIGNER = "Петър"`; `signed_by.strip() == SIGNER`; изходи 2/3/5 | **изход 5 при `"pending — Петър"`** | **= (не се пипа); Б-G7; червен ред 20** |
| `tests/test_b3_gates.py:34`, `:90-91`, `:172`, `:174`, `:194`, `:197` | `DECISIONS_REL`; `doc["attribution"]`; `len(want) == 338`; `sha c6d29d4e…`; `body_digest(blob_at("HEAD", DECISIONS_REL))`; `yes_row_authorship(...) == []` | 3 пина + 2 assert-а | **АД (И-Б6)** |
| `index.html:6316` / `:6320` / `:6322` | `QUARTER_SRC` / `LOCALITY_SRC` / `DISTRICT_CODES` | 0 | **НЕ се пипат (О7)** |
| `index.html:6324-6331` / `:6332` | `QUARTER_CODES` (28) / `LOCALITY_CODES` (5) | пребазират се (~47 / ~32) | **АД (И-Б2, Р6)** |
| `index.html:6619`, `:6620`, `:6625`, `:6631-6633` | `ATTRIB_KEYS` / `ATTRIB_SRC` / `validQuarterAttribution` | **`:6633` → мълчалив отказ на цялата карта** | **АД (И-Б2); Б-G5** |
| `index.html:1901`, `:1918` | `OSM_ATTRIB`; `attribCtrl.addAttribution(OSM_ATTRIB)`; `QUARTERS_ATTRIB` = 0 попадения (М) | И11 никога не е бил приложен | **АД (И-Б3); цената = нула изтрити подписани байта (О8)** |
| `index.html:6268`, `:6291-6293`, `:6304-6307` | кеш `v7-225`; трите sha пина; `LEGACY_BUNDLE_SHA` | пребазират се | **АД (И-Б2)** |
| `scratch/places_search/qa_night_pins.py:206`, `:222`, `:227-241`, `:243`, `:401-446` | C3 `check-ignore` · C4 G29 нула проследена геометрия · C5 `ls-files scratch/boundary_gallery` = 0 · `worktree_negative` | **трите са ЗЕЛЕНИ днес (М), но цялата команда е ЧЕРВЕНА: изход 1, 12 паднали** | **= (не се пипа); механиката се пренася в `gates/probe/g29_ignore.py` (А-G9); Р14** |
| `tests/test_approx_addresses_public_bundle.py:25-28` | sha `97ebe841…`, gzip9 89 061, raw 846 649, 8 361 реда | 0 | **= ; Б-G11 + sha-изключението** |

### Б.4 · Приватностното правило — измерената таблица (защо E, а не A/B/D)

| файл (обхватът на `b3_g11.py`, 19 файла) | правило A (≥ 4 числови листа) | правило B (≥ 4 елемента, всички числа) | правило D (≥ 2 числа в кутията) | **правило E (приетото)** |
|---|---|---|---|---|
| `data/address_rows.json` | 1 (`/rows`) | 0 | 80 510 | **1 (`/rows`) — sha-изключение** |
| `data/approx_addresses_v1.json` | 1 (`/rows`) | 0 | 8 361 | **1 (`/rows`) — sha-изключение** |
| `data/basemaps/…/style.json` | **1 (`/layers[2]/paint/line-width`)** | 0 | 0 | **0** |
| `data/basemaps/…/varna_basemap_manifest.json` | 0 | 0 | 1 | 0 |
| `data/hydrants.json` | 0 | 0 | 6 875 | 0 |
| `data/hydrants.json.pre_address_backfill.json` | 0 | 0 | 5 389 | 0 |
| `data/hydrants.json.pre_cleanup_snapshot.json` | 0 | 0 | 5 795 | 0 |
| `data/hydrants_provenance.json` | 0 | 0 | 10 895 | 0 |
| `data/hydrants_provenance.json.pre_address_backfill.json` | 0 | 0 | 5 803 | 0 |
| `data/removed_hydrants.json` | 0 | 0 | 37 | 0 |
| `data/search_index.json` | 0 | 0 | 86 232 | 0 |
| `scratch/places_search/granitsi_fixtures_07.09.json` | 0 | 0 | 0 | 0 |
| останалите 7 | 0 | 0 | 0 | 0 |
| **ОБЩО** | **3 — чупи гейта** | **0 — маха защитата** | **209 898 — безсмислено** | **2 — точно двете пиннати** |

**Забранените ИМЕНА** (`advert_id`, `raw_sha256`, `raw_response_sha256`, `points`, `raion_points`, `localid`, `cadnum`) дават **0** попадения над същите 19 файла (М) — добавянето им не прави гейта червен, а затваря дупката, която `GEO = {"coordinates","geometry","geometries"}` (`b3_g11.py:37`) оставя отворена.