Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git\Varna_buildings
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a07e0c-53cc-7153-a42c-b6c5864b0962
--------
user
S35 · ДИАГНОЗА и СИСТЕМНО РЕШЕНИЕ (леща: първопричина + архитектура на поправката), read-only. Въпросът на Петър дословно: „не искам да ги поправяме 1 по 1. искам да видим колко дълбок е проблема — и защо така се получава и как да го поправим. искам конкретни решения“. Фактите: (1) кварталната дума на всеки адрес/блок във Fire_Varna идва от app/modules/search/data/search_bridge.json (cluster_summaries, 60 614 клъстера; quarter.{name, source: kais|osm, mode: nearest_point|polygon_cover|-, confidence, distance_m, margin_ratio, second_choice_name}); Студентска бл. 11 носи „кв. Чайка“ от OSM nearest_point на 707 m (low) — а истинският кв. Чайка бл. 11 е друг блок със СЪЩИЯ етикет; (2) мярката срещу 60-те подписани полигона (C:/git/varna_3d 05f485e; таблицата по извор/режим/увереност: C:/git/Fire_Varna/scratch/places_search/adresi_bridge_depth_08.09.json и adresi_po_poligon_measure_08.09.md §8): съгласни 31 997 (53 %), несъгласни 16 869 (28 %), извън полигон 9 255, припокриване 2 483; kais 25 550: 8 214 несъгласни (кадастралната „зона“ ГАЛАТА/ВИНИЦА/Траката/8 микрорайон ≠ квартал); osm nearest_point low: 3 649 извън + 2 623 несъгласни от 10 799; osm polygon_cover 1 876: 1 124 несъгласни; топ несъгласия: кв. ГАЛАТА→с.о. Боровец-юг 1 293, Розова долина→Аспарухово 771, Траката→Евксиноград 649, ж.к. БРИЗ→м-т Свети Никола 560, 8 микрорайон→Център 466, Цветен квартал→кв. Левски 458, Колхозен пазар→кв. Тракия 291. Задачи: (А) ПЪРВОПРИЧИНА: намери в C:/git/Varna_buildings кой скрипт строи quarter в search_bridge.json (tools/, js/, src/; grep search_bridge, margin_ratio, polygon_cover), кой ADR/план го е въвел (docs/decisions/015_quarter_source_confidence_restructure.md, 039_kv_cleanup.md, 061_impossible_coordinates.md, docs/plans/plan_quarters_resorts_2026-09-02.md, docs/archive/plans/osm_quarter_integration_plan.md), какви са били изворите тогава (KAIS quarname = кадастрална зона; OSM place-възли; OSM квартални полигони) и защо се е стигнало до „най-близък възел“ с ленти на увереност; кога са се появили подписаните полигони (Fire_Varna docs/decisions/010_signed_quarter_boundaries.md, 06–07.09) и защо мостът още не ги ползва. Обясни го в 10 реда за човек без CS. (Б) КОЛКО ДЪЛБОКО: провери мярката (метод: токенно съгласие; лента max(50, precision_m); най-малък съдържащ полигон) и кажи кои несъгласия са ГРЕШКИ на думата, кои са РАЗЛИКА В СИСТЕМАТА ОТ ИМЕНА (зона ≠ квартал), кои са ВЪПРОС КЪМ ПОЛИГОНА (напр. Галата/Боровец-юг, Бриз/Свети Никола) — с числа. (В) СИСТЕМНО РЕШЕНИЕ: 2–3 конкретни варианта с цена и риск: напр. (1) мостът строи quarter от подписаните полигони за ВСИЧКИ клъстери (координатата решава), KAIS/OSM думите стават свидетели със source/distance; (2) поправка само в генератора на Fire_Varna; (3) хибрид/поетапно; какво става с 9 255 извън и 2 483 припокриване (решения на Петър: покритие на Център, Цветен квартал, Колхозен пазар; родства); как се пази „веднъж завинаги“ — гейт, който забранява nearest_point като извор и мери съгласието при всеки билд; какво подписва Петър. Препоръчай един вариант. Не пипай нищо, нищо към отдалечено хранилище. До 900 думи, с path:line и числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проследя откъде идва `quarter`, ще проверя мярката и ще сравня вариантите за обща поправка. Работя само за четене, без промени и без действия към отдалечени хранилища.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content docs/activeContext.md -TotalCount 240' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content docs/architecture_v2.md' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/debug/SKILL.md; Get-Content C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/architecture/SKILL.md' in C:\git\Varna_buildings
 succeeded in 303ms:
# Active context â€” Varna_buildings

**Date:** 2026-09-02 Â· **last verified against commit** 4ed99cf (`main`; ahead of `origin/main` by the 2026-09-01 plan's commits until Petar's push â€” see the table; last content commit 69d146a, 2026-08-15) Â· verified by: Opus (executor), audited by: <auditor> Â· signed: __
> Every number here is the output of the command next to it, run on the date above (`verify_numbers.py` checks it).
> The chronicle up to 2026-08-15 (line count in the table) is frozen in [archive/activeContext_2026-08-15.md](archive/activeContext_2026-08-15.md); the open-questions log stays in [unknowns.md](unknowns.md) (frozen header, 2026-08-15).

## What this repo is
Private pipeline: KAIS cadastre (Ð¡Ð³Ñ€Ð°Ð´Ð¸ / Ð˜Ð¼Ð¾Ñ‚Ð¸ / Ð¡ÐžÐ˜Ð¡) + OSM + ML footprints â†’ the static building map (`app/`), the search indexes and the intel artifacts. **It is the data authority for Fire_Varna (search payloads) and varna_3d (section units, address provenance).** No content commit since 69d146a (2026-08-15; the commits after it are the 2026-09-01 plan's â€” see the table) is a quiet stretch, not an archive: both consumers read its outputs.

## Trunk
`main`; `origin/main` is behind it by the plan's commits (table row) until Petar pushes.

## Current phase
- **ADR 063 (entrance reattribution)** â€” Accepted 2026-08-15; payload rebuilt into Fire_Varna and **committed there on 2026-08-31 as c0db844** (numbers in the table). The frozen chronicle's R14 line ("MODIFIED in Fire_Varna, uncommitted") is superseded by that commit.
- **ADR 061 (impossible coordinates)** â€” Accepted 2026-07-29; its code (`tools/data_quality/impossible_coords.py`, `build_impossible_register.py`, `impossible_coords_register.json`, `tests/test_impossible_coords.py`) entered git with LOT 1 of the 2026-09-01 plan (`git log --diff-filter=A -1 --format=%h -- tests/test_impossible_coords.py`); only the change in `tools/build_number_pins.py` is still in the working tree, not in git (row "modified tracked files" below) â€” Ð’-3 of the plan: a clean clone fails that test until it is committed.
- Open questions: `unknowns.md` Â§ ADR 063 (Q1 â€” the invisible phantoms; its count is the document's, not re-verified on 2026-09-02).

## Open
- New open questions since the freeze go here (the log up to 2026-08-15 is frozen in [unknowns.md](unknowns.md)); none recorded yet besides the plan's own Ð’-3/Ð’-4/Ð’-8.
- Resorts as quarters in the Fire_Varna search index â€” docs/plans/plan_quarters_resorts_2026-09-02.md (measure Ã—2, Kimi verdict; NOT executed): Petar decides Ð’-1 buffer (0 m), Ð’-2 Ðš&Ð• geometry âˆ§ self-evidence, Ð’-3 no display prefix, Ð’-4 13 parcels into the registry alias list (new SHA256) â€” then Sol on the projection, then the lot.

## Waiting for signature
- Ð’-3 (ADR 061 code) Â· Ð’-4 (`tools/*quarter*.py`, `build_number_layer.py` â€” active tools or archive).

## Last report
- `decisions/063_entrance_reattribution.md` Â· index `decisions/README.md`.

## Live numbers
| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| commits on `main` | 485 | `git rev-list --count main` |
| last commit | 542c2cc 2026-09-02 | `git log -1 --format='%h %cs' main` |
| last pushed commit | 69d146a 2026-08-15 | `git log -1 --format='%h %cs' origin/main` |
| commits ahead of `origin/main` (the 2026-09-01 plan, unpushed) | 3 | `git rev-list --count origin/main..main` |
| numbered ADR files | 60 | `ls docs/decisions \| grep -cE '^[0-9]{3}_'` |
| missing numbers in 001â€“063 | 17 24 51 | `PYTHONIOENCODING=utf-8 python -c "import os,re;h={int(m.group(1)) for f in os.listdir('docs/decisions') for m in [re.match(r'(\d{3})_',f)] if m};print(*[n for n in range(1,64) if n not in h])"` |
| entries in `config/entrance_reattribution.json` | 125 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('config/entrance_reattribution.json',encoding='utf-8'))['entries']))"` |
| Fire_Varna commit carrying that payload | c0db844 2026-08-31 | `git -C ../Fire_Varna log -1 --format='%h %cs' -- data/search_index.json` |
| payload numbers (that commit's subject) | 4764 entrances (-98 phantom markers), 86232 public entries | `git -C ../Fire_Varna log -1 --format=%s c0db844 \| grep -oE '[0-9]+ entrances[^,]*, [0-9]+ public entries'` |
| modified tracked files | 4 | `git status --porcelain \| grep -c '^ M'` |
| days without a content commit (2026-08-15 â†’ the date above) | 18 | `python -c "import datetime;print((datetime.date(2026,9,2)-datetime.date(2026,8,15)).days)"` |
| archived chronicle, lines | 2121 | `wc -l < "$(ls docs/archive/activeContext_2026-08-15.md 2>/dev/null \|\| echo docs/activeContext.md)"` |
| files in `C:\git\Varna_FireSafety_M6000` | 4 | `ls C:/git/Varna_FireSafety_M6000 \| wc -l` |
| its size | 2.3G | `du -sh C:/git/Varna_FireSafety_M6000 \| cut -f1` |

## Forbidden here
- `git push` â€” Petar only. Editing `docs/architecture_v2.md` outside an architecture cycle. Committing raw KAIS/OSM data, `output/`, secrets, personal data. Running `scratch/inspect_kais.py`. A coordinate without its CRS (BGS2005 vs WGS84).

## Where things are
- `architecture_v2.md` (canonical; its header says last updated 2026-06-02 â€” numbers not re-verified on 2026-09-02) Â· `data_quality/register.md` (canonical class register; the flat `data_quality_register.md` is kept for inbound links, ADR 060) Â· `decisions/` (numbered ADRs â€” count in the table â€” plus README and the legacy `lookup_map_*` files: `ls docs/decisions | grep -vE '^[0-9]{3}_'`) Â· `scratch/adrNNN_*` (evidence behind ADRs; LOT 1) Â· `output/`, `data/` gitignored except the exceptions listed in `.gitignore`.
- Outside git: `C:\git\m6000_private\` (municipal-map aid; cadnum-bearing, never committed) Â· `C:\git\Varna_FireSafety_M6000\` (rasters, see the table â€” Ð’-7).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format=\"%h %s\"; rg --files -g AGENTS.md -g CLAUDE.md -g '*bridge_depth*' -g '*po_poligon*' -g '*signed_quarter*' C:/git/Fire_Varna C:/git/varna_3d; rg -n \"search_bridge|margin_ratio|polygon_cover\" tools js src" in C:\git\Varna_buildings
 succeeded in 530ms:
# Varna_buildings â€” Architecture v2

> Checked 2026-09-02 (commit 542c2cc): every number in this document carries its own measurement date; whatever is stale as of 2026-09-02 is flagged with âš  under the line.

> Last updated: 2026-06-02 (ADR 026 amendment)
> Status: Active (supersedes architecture_v1.md per ADR 020)
> Scope: This document covers the Varna_buildings repo only.

For governance and approval gates, see [`AGENTS.md`](../AGENTS.md). For
the per-commit execution protocol, see [`CLAUDE.md`](../CLAUDE.md).
For the history of how the project arrived at its current shape, see
[`archive/architecture_v1.md`](archive/architecture_v1.md).

---

## What this repo does

This repo produces a static, offline-capable interactive map of Varna's
buildings. Building geometry is taken **primarily** from imagery-traced
sources â€” OpenStreetMap footprints, with Microsoft ML Building Footprints
filling buildings OSM has not yet mapped â€” so footprints align with
reality. KAIS (Ð¡Ð³Ñ€Ð°Ð´Ð¸ / Ð˜Ð¼Ð¾Ñ‚Ð¸ / Ð¡ÐžÐ˜Ð¡) supplies the attribute layer
(cadastral identity, apartment counts, floor counts, building age,
per-entrance aggregates, address provenance), joined to the rendered
geometry via the KAISâ†”OSM/ML link. **Per ADR 026, a real building that
no imagery source covers falls back to its KAIS cadastral footprint as a
gated, low-confidence last resort** (fuzzy-OSM-demotion-, road-guard-,
and overlap-clip-gated; see *Geometry-selection stage* below). Only a
building with no usable footprint from any source would render as a
point marker; such buildings â€” and those excluded by the realness gate â€”
are not rendered but remain searchable via a minimal summary and address
pin (ADR 026 D7).

- Spatial display of every building polygon in Ð³Ñ€. Ð’Ð°Ñ€Ð½Ð° (city-level,
  ekatte=10135).
- Click-through to per-building cadastral identity, apartment counts,
  per-entrance unit aggregates, and address provenance.
- Address-based, parcel-based, and entrance-based search.

The map application is the primary deliverable and is served as static
files via `python -m http.server 8000` from repo root (see
[`start_map.bat`](../start_map.bat)).

**Single deliverable model is retired** (ADR 020). The original framing
("produce `output/address_index.json` for Fire_Varna") was correct as of
Phase 1.5 but became inaccurate as the system grew. Address indexes
remain valuable substrate but are no longer the framing target.

### Out of scope

- Fire_Varna UI, hydrant data, mobile app code (separate concern; Phase 2
  reintegration has resumed under ADR 020 Amendment 2, but it remains phased/gated and
  built in the Fire_Varna repo â€” not part of unrelated architecture work)
- Backend services, databases, Docker, Kubernetes, Cloudflare Workers
- Any KAIS layer containing personal data (owner XLSX files â€”
  see [`audits/personal_data_decision.md`](audits/personal_data_decision.md))
- Public deployment of map artifacts (license posture is non-commercial
  managed risk; see [`audits/license_review.md`](audits/license_review.md))

---

## Primary product: the map app

### App architecture

The app is a static, modular, vanilla-JS single-page application
(no framework). Its skeleton is established by ADR 013 (Modular App
Foundation).

```
app/
  index.html              Entry point
  app.json                App-level manifest
  shell/
    main.js               Boot + module loader entry
    moduleLoader.js       Reads each module manifest and resolves data
    dataResolver.js       Resolves data paths declared in manifests
    map.js                Leaflet map shell
    sidebar.js            Sidebar UI shell
    events.js, errors.js  Cross-module utilities
    styles.css            Shell-level styles
  modules/
    buildings/
      manifest.json       Declares cluster data deps
      module.js, render.js
      styles.css
      data/               Module-owned derivatives (gitignored)
    search/
      manifest.json       Declares search index deps
      module.js, searchLogic.js
      styles.css
      data/               Module-owned derivatives (gitignored)
```

Per ADR 013, modules declare their data dependencies in their
`manifest.json` rather than fetching directly. The shell's
`dataResolver` materialises declared paths at boot. This decouples the
runtime from data location and lets modules be relocated.

### Data builder

`tools/build_app_m1_data.py` is the canonical map-app data builder
(declared as the producer in both module manifests). It reads:

- `output/kais_clusters.json` + `output/kais_clusters_schema.json`
- `output/kais_osm_links.json` + schema
- `output/kais_cluster_flags.json` + schema (ADR 019)
- `output/strategic_intel.json` (per-entrance aggregates, per-parent
  `building_intel`)
- `output/address_index.json`, `output/address_provenance.json`
- `output/search_index*.json` (entrances, parcels)

It writes per-module derivatives into:

- `app/modules/buildings/data/clusters.geojson`
- `app/modules/buildings/data/cluster_details.json`
- `app/modules/buildings/data/metadata.json`
- `app/modules/search/data/search_bridge.json`
- `app/modules/search/data/metadata.json`

These derivatives are gitignored and regenerable.

### Search builders

Three MiniSearch index builders run as `npm` scripts:

- `npm run build` â†’ `output/search_index.json` (address index)
- `npm run build:entrances` â†’ `output/search_index_entrances.json`
- `npm run build:parcels` â†’ `output/search_index_parcels.json`

Schemas are written alongside (`search_schema*.json`). The runtime
rehydrates these indexes through MiniSearch's reconstruction API; no
server-side search is involved.

`npm run regression:validate` runs the four-category regression harness
established by ADR 008 (Phase 1.8). The harness corpus uses fixed
seeds and locked target pass rates.

---

## Data sources

### KAIS sgradi (buildings) â€” attribute authority; geometry retired from rendering (ADR 025), re-admitted only as a gated low-confidence fallback (ADR 026)

- File: `data/extracted/ÑÐ³Ñ€Ð°Ð´Ð¸/Ð¡Ð³Ñ€Ð°Ð´Ð¸ (Polygon).shp` + sidecars
- Records: 80,513
- Projection: BGS2005 (Lambert Conformal Conic, â‰ˆ EPSG:7801)
- Encoding: UTF-8
- Key fields: `cadnum` (4-segment), `appcount`, `flrcount`, `functype`,
  `funccode`, `immaddr`, `strename`, `strnum`, `quarname`, `regname`,
  `proptype`, `validate`
- Authority for: cadastral identity, legal apartment counts, floor
  counts, functional category, regulatory provenance
- Note: KAIS geometry is read by the pipeline for the link join and
  centroid. Under ADR 025 it was **not** emitted as rendered building
  geometry at all; **ADR 026 re-admits it as a gated, low-confidence
  fallback** (`data_confidence = low`) only for real buildings no OSM/ML
  source covers â€” after a fuzzy-OSM demotion, a non-building road guard,
  and an overlap clip, and never stacked on an OSM/ML footprint.

### KAIS Ð¿Ð¾Ð·ÐµÐ¼Ð»ÐµÐ½Ð¸ Ð¸Ð¼Ð¾Ñ‚Ð¸ (parcels)

- File: `data/extracted/Ð¿Ð¾Ð·ÐµÐ¼Ð»ÐµÐ½Ð¸ Ð¸Ð¼Ð¾Ñ‚Ð¸/Ð˜Ð¼Ð¾Ñ‚Ð¸ (Polygon).shp` + sidecars
- Records: 65,043 (city level filtered to ekatte=10135; 32 maritime
  records filtered by `purptype`)
- Key fields: `cadnum` (3-segment), `immaddr`, `strename`, `strnum`,
  `purptype`, `usetype`, `usecode`, `cattype`, `quarname`, `place`
- Use: parent-parcel context for `cadnum` prefix; quarter and locality
  signals; water-body filter

### KAIS ÑÐ°Ð¼Ð¾ÑÑ‚Ð¾ÑÑ‚ÐµÐ»Ð½Ð¸ Ð¾Ð±ÐµÐºÑ‚Ð¸ (SOIS) â€” apartment objects

- File: `data/extracted/ÑÐ°Ð¼Ð¾ÑÑ‚Ð¾ÑÑ‚ÐµÐ»Ð½Ð¸ Ð¾Ð±ÐµÐºÑ‚Ð¸/Ð¡Ð°Ð¼Ð¾ÑÑ‚Ð¾ÑÑ‚ÐµÐ»Ð½Ð¸ Ð¾Ð±ÐµÐºÑ‚Ð¸ (Polygon).shp` + sidecars
- Records: 241,949 (5-segment cadnums; geometry is per-floor footprint,
  not building polygon)
- Key fields: `cadnum`, `entrance`, `apptype`, `appcode`, `apparea`,
  `flrnum`, `addrflr`, `flrcount`, `immaddr`, `blocknum`
- Use: per-entrance unit aggregation, per-building apartment counts,
  block-number signal for clustering (ADR 018)

### Ð“Ð ÐÐž address register â€” address-directory authority (ADR 058); zero coordinates, geocoded downstream

- Files: `external/grao/grao_varna_streets_122020.csv` (1,943 streets:
  `street_code`, `street_name`) + `grao_varna_addresses_122020.csv`
  (41,949 addresses: `street_code`, `street_name`, `building_number`,
  `entrance`)
- Coordinates: **none** â€” Ð“Ð ÐÐž is not geodata
  (`external/grao/README.md:16-17`)
- Authority for: which official addresses exist + the official
  street / number / entrance (ADR 058 D2)
- **Not** authority for: any coordinate â€” each address's position is
  **derived downstream** (KAIS footprint/centroid â†’ gated m6000 anchor â†’
  street interpolation; Ð“Ð ÐÐž never carries a coordinate); apartment count
  (Ð“Ð ÐÐž address-count â‰  KAIS `appcount` and never overwrites it, ADR 010
  D2 / 030); or ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð» (no quarter column; the Ð“Ð ÐÐž Ð•ÐšÐÐ¢Ð¢Ð• classifier is
  not held)
- Note: only the dump is an ingestible input; the live Ð“Ð ÐÐž web form is
  untrusted (governance Inv-11). Canonizing this authority does **not**
  build the geocoding-join pipeline (a separate B3.0 cycle).

### OSM buildings

- File: `data/osm/varna_buildings_2026-05-13.geojson`
- Features: 38,124
- Authority for: physical footprint geometry, addr:* tags, building:*
  metadata, and the navigable **display label** (per ADR 014 D2)
- **Not** the address-existence / official-number authority (that is
  Ð“Ð ÐÐž, ADR 058 D2), nor the street-NAME authority on a dispute (Ð“Ð ÐÐž
  register + m6000 arbiter, ADR 058 D4) â€” a wrong OSM street name is
  corrected toward Ð“Ð ÐÐž / m6000, while ADR 014 D2 still governs the
  display-label FORMAT where undisputed
- Bridge to KAIS: `ref:BG:id` (99.75% exact-cadnum match on 1,189
  features); spatial containment / nearest-within-50m otherwise
- Now the **primary rendered geometry source** (ADR 025)

### Microsoft ML Building Footprints

- Source: Microsoft Global ML Building Footprints
  (github.com/microsoft/GlobalMLBuildingFootprints)
- License: **CDLA Permissive 2.0** (extraction/use/redistribution
  permitted)
- Coverage for Varna: LOD-9 tile `120322133` (published 2026-02-03;
  imagery ~2014â€“2024; no per-building confidence/height for Bulgaria)
- ~62,600 footprints in the Varna bbox; covers ~75â€“86% of the
  residential buildings OSM lacks, ~3 m median position accuracy
  (IoU ~0.42 â€” position trustworthy, extent approximate; ~10% of real
  buildings unmatched)
- Role: **secondary rendered geometry** for buildings without an OSM
  footprint

### Google Street View â€” terrain eyes (break-glass validation aid; ADR 058)

Read-only, Petar-supervised agent vision-model reading of the free
Street View layer. **ToS-tightened (ADR 058 D5):** may only REFUTE /
DOWNGRADE confidence or TRIGGER a cadastre / field re-check â€” **never**
the sole/decisive basis for a stored-value change, never lifted / traced
/ cached, never fed back to OSM (consumer Google Maps ToS forbid
augmenting a mapping dataset; Fire_Varna is one). Its imagery /
footprints / coordinates are never ingested. Output is a typed TEXT
verdict only ({CONFIRM|REFUTE|INSUFFICIENT}); the operational HOW is the
tracked SOP [`measurement/terrain_eyes_streetview_sop.md`](measurement/terrain_eyes_streetview_sop.md).

### Ownership data (excluded)

XLSX workbooks `Ñ ÑÐ³Ñ€Ð°Ð´Ð¸.xlsx`, `Ñ Ð¡ÐžÐ¡.xlsx`, `Ñ ÐŸÐ˜.xlsx` contain
personal data (owner names, Ð•Ð“Ð, Ð•Ð˜Ðš). Per
[`audits/personal_data_decision.md`](audits/personal_data_decision.md)
these are excluded from processing. The shapefile owner-ZIPs that
existed before 2026-05-12 were permanently deleted on that date before
extraction.

---

## Pipeline architecture

```
KAIS shapefiles (BGS2005)       OSM buildings (WGS84)
        |                                |
        v                                v
   read_shp.py            osm/download_and_clip.py
   read_intel_shp.py                    |
        |                                v
        +--------> reproject.py <--------+
        |          centroids.py          |
        v                                v
   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
   â”‚ build_link_table.py (ADR 010 Stage 2) â”‚
   â”‚ â†’ output/kais_osm_links.json          â”‚
   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       |
                       v
   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
   â”‚ build_classification.py (Stages 3-4)  â”‚
   â”‚ + ADR 018 v2 same-parent post-pass    â”‚
   â”‚ + ADR 019 parent-aware gates          â”‚
   â”‚ â†’ kais_clusters.json                  â”‚
   â”‚ â†’ kais_cluster_flags.json             â”‚
   â”‚ â†’ kais_section_categories.json        â”‚
   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       |
        +--------------+---------------+
        v                              v
  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚ build_strategic_   â”‚   â”‚ extract_addresses.py     â”‚
  â”‚ intel.py           â”‚   â”‚ + address_authority.py   â”‚
  â”‚ (Phase 1.7/1.9)    â”‚   â”‚ (ADR 014, Phase 1.12 v4) â”‚
  â”‚ â†’ strategic_intel  â”‚   â”‚ + address_inheritance.py â”‚
  â”‚   .json            â”‚   â”‚ (ADR 011)                â”‚
  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â”‚ â†’ address_index.json     â”‚
                           â”‚ â†’ address_provenance.jsonâ”‚
                           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                       |
                  +--------------------+--------------------+
                  v                                         v
        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”                  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚ JS builders      â”‚                  â”‚ build_app_m1_data.pyâ”‚
        â”‚ â†’ search_index*  â”‚                  â”‚ (Modular app M1)    â”‚
        â”‚   .json          â”‚                  â”‚ â†’ app/modules/*/    â”‚
        â”‚ (npm scripts)    â”‚                  â”‚   data/             â”‚
        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜                  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                  |                                         |
                  +----------------+------------------------+
                                   v
                          static map app
                  (served by python -m http.server)
```

### Geometry-selection stage (ADR 025, amended by ADR 026)

ADR 025 adds a geometry-selection stage between classification and the
app builder; ADR 026 extends the chain with a fuzzy-OSM demotion and a
gated KAIS low-confidence fallback:

```
kais_clusters + kais_osm_links + OSM + ML footprints
              + KAIS Ð¡Ð³Ñ€Ð°Ð´Ð¸ polygons + OSM streets
                      |
                      v
  build_geometry_selection (ADR 025, amended by ADR 026)
  per building, one footprint, best-source-first:
    1. strong OSM footprint (gold/high link)
    2. trustworthy fuzzy OSM
         (else demote untrustworthy fuzzy -> no-OSM; ADR 026 D2)
    3. ML footprint (<=15 m, spatial-dedup vs OSM)
    4. KAIS low-confidence fallback (ADR 026 D3-D5):
         union of member polygons (ADR 022) -> road guard
         (drop non-building road objects; D4 + QA sign-off D4a)
         -> overlap clip vs rendered footprints
         (D5; <15% remaining -> attach, no geometry)
    5. point marker (residual)  + realness gate (D5/ADR 025)
                      |
                      v
   build_app_m1_data.py -> clusters.geojson
   (OSM / ML / KAIS-fallback / point; one non-overlapping
    footprint per building; KAIS-fallback styled low-confidence)
```

Under ADR 025 KAIS geometry no longer flowed to `clusters.geojson` as
rendered polygons; **ADR 026 re-admits it as a gated low-confidence
fallback** (D1â€“D5) for real buildings no OSM/ML source covers. The
classification/cluster identity, link table, strategic intel, address,
and the **canonical** search corpus (`search_index*`, `address_index`,
`strategic_intel`) remain **unchanged and byte-identical** â€” only the
rendered geometry source changes; the search **bridge** derivative
(`search_bridge.json`) reflects the new geometry, pins, and minimal
summaries for non-rendered-but-searchable buildings (ADR 026 D7/D8).

### ADR 025 supersession notes

- ADR 022 (prefix_spatial) and ADR 023 (phantom road objects) fixed
  **KAIS-geometry rendering**. ADR 025 D1 retired KAIS geometry from
  rendering, superseding those rendering paths while **retaining their
  classification work** (the ADR 023 non-building detection feeds the
  ADR 025 realness gate, D5). **ADR 026 partially re-admits KAIS geometry
  as a gated low-confidence fallback and, in doing so, reuses ADR 022
  D3/D5 (real union of member polygons) and ADR 023 road-object
  detection** (see *ADR 026 amendment* below). Both ADRs remain valid
  history.
- ADR 024 (residential filter) is **folded into** ADR 025 D6.
- ADR 014 (address authority, OSM-preferred presentation) is
  **reinforced**, not changed â€” ADR 025 extends "OSM-preferred" from
  address to geometry.

### ADR 026 amendment â€” KAIS low-confidence geometry fallback

**ADR 026 amendment â€” KAIS low-confidence geometry fallback.** Rendered
geometry is selected OSM â†’ ML â†’ **KAIS low-confidence cadastral
fallback** â†’ point. KAIS geometry, retired by ADR 025, is re-admitted
**only** as a gated last resort for real buildings no imagery source
covers, subject to: (a) demotion of untrustworthy fuzzy OSM; (b) a
non-building road guard with a false-positive QA gate; (c) union of
member polygons for multi-member clusters (ADR 022); (d) an overlap clip
guaranteeing one non-overlapping footprint per building. KAIS-fallback
carries `data_confidence = low`. The realness gate (D5) is unchanged. The
canonical search index and address layers are unchanged and
authoritative; non-rendered real buildings remain searchable via a
minimal summary and address pin. KAIS is read in BGS2005 and reprojected
to WGS84 with `validate_wgs84_bounds` before any output.

### ADR 027 amendment â€” derived physical-building grouping

**ADR 027 amendment â€” derived physical-building grouping.** Per ADR 010 D3 "physical building
is a derived query concept," the app-data builder derives **physical-building groups** from the
rendered multifamily clusters and consolidates them for map, search, and details: one footprint
(union of members), one search result, one detail panel (all entrances, summed apartments). The
grouping key is hybrid â€” shared 3-seg parcel with either an identical block-id or polygon-touch
within 5 m (UTM 35N) â€” guarded against over-merge by an explicit-block-number-divergence rule
(distinct `Ð±Ð» N` are never merged) and a sign-off gate for ambiguous geometry-backed merges (not
fully Ð±Ð»#-supported). The
canonical `kais_clusters` section-cluster identity, the classification pipeline, and the search
index/address/strategic-intel corpus are unchanged; the bridge `cadnum_to_cluster_id` map stays
invariant and a derived `cluster_to_building` grouping is added. KAIS geometry handling (ADR 026)
is unchanged. OSM-footprint-quality under-rendering (a tiny OSM footprint vs a much larger KAIS
extent) is tracked separately and not addressed here.

### ADR 028 amendment â€” identity-first physical-building grouping

**ADR 028 amendment â€” identity-first physical-building grouping.** ADR 027's
geometry-first grouping was **empirically rejected for D2/D3/D4**: geometry adjacency
(polygon-touch â‰¤ 5 m) is only ~48 % precise for "same building" because in dense panel
estates separate blocks sit party-wall, so a ~0 m touch is the signature of two
*different* blocks, not one. ADR 028 **inverts** the model: **KAIS/SOIS administrative
block identity decides grouping; OSM/ML geometry only renders.** Over the same
MF-dominant cluster universe, each section resolves a strong block identity â€” SOIS
`blocknum` (apartment-registry consensus) over KAIS Ð¡Ð³Ñ€Ð°Ð´Ð¸ `immaddr` `Ð±Ð» N` â€” and
sections sharing a 3-seg parcel and a normalized strong identity form one physical
building; **different identities never merge** (subsuming the ADR 027 Ð±Ð»#-divergence
guard). Sections with no identity fall back to OSM/ML footprint adjacency (D3) guarded
by a conservative `flrcount` veto, and every no-identity / weak / conflicting / complex
/ on-road case is routed to a **tracked, build-enforced sign-off ledger**
(`docs/audits/adr028_signoff.json`). A building's footprint is the **union of its
members' already-rendered footprints only** â€” road-dropped, `no_evidence`, attached, or
ADR-023-flagged members contribute identity/counts but **never geometry** â€” followed by
a post-union road check (including minor residential/service roads across a
newly-closed seam) that routes any `building_on_road` to sign-off, so the ADR
023/025/026 road-phantom guards cannot regress. The geometry-selection pipeline
(`build_geometry_selection.py`: fuzzy-OSM demotion â†’ ML â†’ KAIS low-confidence fallback
â†’ road guard â†’ false-positive gate â†’ overlap clip) and the ADR 023 phantom-road flags
are **unchanged**; ADR 028 is a derived layer over the rendered cluster atoms. This
**supersedes ADR 027 D2/D3/D4** and retains ADR 027 D5/D6/D7/D8. The canonical
`kais_clusters` identity, the classification pipeline, and the
`search_index*`/`address_index`/`strategic_intel` corpus stay byte-identical; the
bridge `cadnum_to_cluster_id` stays invariant (80,511) and derived
`section_to_block_identity` + `cluster_to_building` maps are added. Adminâ‰ physical is a
hard guard: an identity group whose member footprints are geometrically disjoint beyond
`COMPLEX_GAP_M` is flagged `identity_complex_candidate` â†’ sign-off/split, and a single
OSM/ML footprint bundling â‰¥ 2 identities is flagged `footprint_multi_identity` (rendered
as-is, OSM-retrace backlog). SOIS, Ð¡Ð³Ñ€Ð°Ð´Ð¸, and Ð˜Ð¼Ð¾Ñ‚Ð¸/ÐŸÐ˜ were value-audited (387,505
records, 0 EGN, no owner field); ADR 028 consumes only the structured grouping fields
and serializes no free-text or apartment-level `appnum`/unneeded `apparea` (GDPR Art.
5(1)(c) data minimisation).

### Critical contracts

**Coordinate systems.** Raw KAIS data is BGS2005. All pipeline output
is WGS84 (longitude/latitude). Mixing the two is the single largest
correctness risk; every coordinate value on disk must declare its CRS.
`reproject.py:validate_wgs84_bounds()` is the gate: any centroid
outside measured Varna bounds (lng 27.83â€“28.05, lat 43.10â€“43.31) stops
the pipeline.

**Cadnum is canonical.** Per ADR 010 D1, the 4-segment KAIS section
identity is the canonical building identity. The 3-segment prefix is a
*parcel* identifier. "Physical building" is a derived query, not a
schema entity (ADR 010 D3).

**Per-attribute authority.** Per ADR 010 D2, each attribute domain has
one authoritative source; the other is corroborating signal. KAIS owns
cadastral identity, legal counts, regulatory provenance. OSM owns the
navigable **display label** (ADR 014 D2), physical footprint, and
building metadata. KAIS `strename` labels are noisy (ADR 009) and
require street-distance cross-validation (ADR 014). Per ADR 025, **Microsoft ML is the
secondary footprint source for buildings OSM lacks**; per ADR 026,
**KAIS geometry is rendered only as a gated low-confidence fallback**
for real buildings no OSM/ML source covers (never stacked, road-guarded,
overlap-clipped) â€” otherwise KAIS **geometry is not rendered** (KAIS
remains authority for cadastral identity, legal counts, regulatory
provenance, building age). The KAISâ†”geometry attribute join carries a
**`data_confidence` flag** (~70% high, ~30% fuzzy, plus a new **`low`**
band for KAIS-fallback geometry per ADR 026); fuzzy- and low-confidence
attachments are presented as uncertain.

**Source authority by question (ADR 058).** This is the single home of
the per-source authority allocation; AGENTS.md Â§ Measurement Doctrine and
ADR 058 point here and do not copy it.

- **Address existence + official street / number / entrance â†’ Ð“Ð ÐÐž** (the
  address register; 1,943 streets + 41,949 addresses, **zero
  coordinates** â€” each address's position is derived downstream, KAIS
  footprint/centroid â†’ gated m6000 anchor â†’ street interpolation; Ð“Ð ÐÐž
  never carries a coordinate). Ð“Ð ÐÐž address-count â‰  KAIS `appcount` and
  never overwrites it (ADR 010 D2 / 030).
- **Navigable display label â†’ OSM** (the ADR 014 D2 cascade â€” the default
  where the street name is undisputed).
- **Street NAME on a dispute (which street a segment IS) â†’ Ð“Ð ÐÐž register
  + m6000 arbiter.** The stored name is Ð“Ð ÐÐž's; the m6000 municipal-map
  arbiter adjudicates an OSM-vs-official dispute segment-by-segment and,
  where it finds against OSM, **Ð“Ð ÐÐž + m6000 override OSM** (OSM flagged
  as the error) â€” but it may equally confirm OSM (post-12.2020 renames
  are legitimate, not errors). Scoped to NAMES, not geometry (ADR 058 D4;
  formalizes FF-001 / M3b-names, which previously ran with no ADR against
  ADR 010 D2 / ADR 056).
- **Building identity â†’ KAIS `cadnum`; apartment count â†’ KAIS `appcount`
  (building) / SOIS (entrance); floors, category, regulatory provenance â†’
  KAIS.**
- **Footprint â†’ OSM â†’ Microsoft ML â†’ gated-low KAIS** (ADR 025/026,
  unchanged); the KAIS centroid supplies the anchor/pin. KAIS identity +
  centroid + attributes is **not** a footprint reversal.
- **Ñ€Ð°Ð¹Ð¾Ð½ â†’ KAIS `regname`; ÐºÐ²Ð°Ñ€Ñ‚Ð°Ð» / Ð¶.Ðº. â†’ KAIS `quarname` first, OSM
  polygon/point gap-fill, SOIS `stk` additive** (ADR 015/043/044/052; OSM
  admin boundaries stay audit-only).
- **m6000** (municipal map) and **Google Street View terrain-eyes** are
  private **aids** â€” never ingested, never a canonical stored coordinate,
  never in a determinism artifact; terrain-eyes may only
  refute/downgrade/trigger (ADR 058 D3/D5). Register-vs-register
  conflicts are documented + quarantined, not silently merged; **Petar is
  the final per-item tiebreak.**

**Address authority cascade.** ADR 014 establishes priority:
`addr:street + addr:housenumber` > `addr:place + addr:housenumber` >
KAIS-derived (with street-distance check) > bare OSM `addr:housenumber`.
ADR 014 v3 adds comparator-gated canonical text. Phase 1.12 Part A
adds post-selection block-prefix augmentation (ADR 014 v4).

**Cluster identity.** Per ADR 010 Stage 3 (Algorithm Alpha), each
KAIS section is routed to a cluster via shared OSM polygon
(`osm_grouped`), prefix-spatial proximity (`prefix_spatial`), same-parent
post-pass (`same_parent_block_spatial`, ADR 018), or remains singleton.
ADR 019 adds parent-aware materialisation gates that prevent
cross-parent contamination via raw `osm_id` grouping.

---

## Output artifacts (canonical inventory)

Every generated file under `output/` with current consumer:

| Artifact | Producer | Primary consumer |
|---|---|---|
| `address_index.json` | `build_index.py` | App search module, JS builders |
| `address_provenance.json` | `extract_addresses.py` + `address_authority.py` | Audit only (no runtime consumer) |
| `address_inheritance_conflicts.json` | `address_inheritance.py` | Audit only |
| `kais_clusters.json` + schema | `build_classification.py` | `build_app_m1_data.py` |
| `kais_cluster_flags.json` + schema | `build_classification.py` (ADR 019) | App-side consumption deferred â€” currently audit-only |
| `kais_osm_links.json` + schema | `build_link_table.py` | `build_classification.py`, `build_app_m1_data.py` |
| `kais_section_categories.json` + schema | `build_classification.py` | `build_app_m1_data.py` |
| `strategic_intel.json` | `build_strategic_intel.py` | App search module, `build_app_m1_data.py` |
| `schema.json` | `build_index.py` | App search module |
| `search_index.json` + schema | `js/build_search_index.mjs` | App search module |
| `search_index_entrances.json` + schema | `js/build_search_index_entrances.mjs` | App search module |
| `search_index_parcels.json` + schema | `js/build_search_index_parcels.mjs` | App search module |

App-side derivatives (module-owned, gitignored, regenerable by
`build_app_m1_data.py`):

- `app/modules/buildings/data/clusters.geojson`
- `app/modules/buildings/data/cluster_details.json`
- `app/modules/buildings/data/metadata.json`
- `app/modules/search/data/search_bridge.json`
- `app/modules/search/data/metadata.json`

Per ADR 025 and ADR 026, `app/modules/buildings/data/clusters.geojson`
geometry is produced by the source-selection (OSM / ML /
**KAIS-low-confidence-fallback** / point), not a blanket raw-KAIS render.
The clipped Microsoft ML footprint tile (`120322133`) is added to the
canonical input inventory (consumed by the ADR 025/026
geometry-selection step). Other artifacts unchanged.

---

## Tech stack

| Component | Choice | Rationale |
|---|---|---|
| Pipeline language | Python 3.10+ | No system GDAL dep |
| SHP reading | pyshp | Pure Python |
| Reprojection | pyproj | Standard CRS library |
| Geometry | shapely 2.1.2 | Polygon ops, STRtree |
| Building footprints (gap-fill) | Microsoft Global ML Building Footprints (CDLA Permissive 2.0) | Satellite-traced footprints for buildings OSM lacks |
| Search index | MiniSearch 7.2.0 (Node 18+) | Offline-built, browser-compatible |
| Frontend | Vanilla JS, Leaflet | No framework, no build step beyond data |
| Output | Static JSON | No backend, no database, no Docker |

---

## Hard constraints

- **Output size.** Combined gzipped output of the five primary search
  payloads (`address_index`, `search_index`, `strategic_intel`,
  `search_index_entrances`, `search_index_parcels`) must remain under
  5.5 MB per ADR 007 Amendment v2. Current measurement: ~5.26 MB
  (yellow zone, within budget).
- **Offline.** No runtime API calls. The map app runs entirely from
  served static files plus tile providers.
- **Geometry is imagery-traced first.** Rendered building geometry comes
  from OSM or Microsoft ML footprints, or a point; **per ADR 026, KAIS
  cadastral geometry is re-admitted only as a gated, low-confidence
  fallback** (`data_confidence = low`) for real buildings no imagery
  source covers â€” fuzzy-OSM-demotion-, road-guard-, and overlap-clip-
  gated, and never stacked on an imagery footprint. Otherwise KAIS
  geometry is not rendered. Google Maps content is never ingested or
  redistributed.
- **Coordinate consistency.** All output is WGS84. BGS2005 mixing is
  a pipeline bug.
- **Reproducibility.** All processing must be regenerable from the raw
  KAIS download, the OSM extract, **and the pinned Microsoft ML
  footprint tile** (`120322133`).
- **Personal data.** Owner XLSX files are excluded from consumption.
  Ownership shapefile ZIPs were deleted on 2026-05-12. Tripwire checks
  prevent accidental ingestion.
- **No automated commits.** No automated pushes. Petar pushes manually
  after audit.

---

## Phase history (compressed)

For full session history, see commit messages and archived plans under
[`docs/archive/plans/`](archive/plans/).

| Phase | Date | Theme |
|---|---|---|
| Phase 0 | 2026-05-12 | Repo setup, governance, schema inventory |
| Phase 1 / 1.5 / 1.6 | 2026-05-12..13 | Address index POC, normalisation, building-layer fallback |
| Phase 1.7 / 1.7.5 / 1.7.6 / 1.7.7 | 2026-05-13..14 | Strategic intel, entrance index, parcel index, smoke UI |
| Phase 1.8 | 2026-05-14 | Regression harness baseline (ADR 008) |
| Phase 1.9 | 2026-05-24 | Strategic intel v1.1 + building_intel (ADR 016) |
| Phase 1.10 | 2026-05-24 | Visual unification infrastructure (ADR 017, since superseded) |
| Phase 1.10' | 2026-05-25 | Algorithm Alpha v2 same-parent clustering (ADR 018) |
| Phase 1.11 | 2026-05-26 | Parent-aware OSM gates (ADR 019) |
| Phase 1.12 | 2026-05-26 | Block prefix augmentation (ADR 014 v4); fragmentation fix deferred to Phase 1.13 |
| Phase 1.13 | next | Vertex-component clustering; manual review of 364 Phase 1.12 audit sidecars |

---

## Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| KAIS license challenge | Low | High | AGKK email pending; non-commercial use documented |
| BGS2005 reprojection silent failure | Medium | High | `validate_wgs84_bounds()` gate |
| OSM data refresh required mid-phase | Medium | Medium | OSM snapshot pinned to 2026-05-13; refresh is a planned action |
| Cluster identity churn breaking app state | High | Medium | ADR 018 D6 deterministic cluster ids; ADR 019 D6 collision detection |
| Phase 1.12 audit sidecars unprocessed | High | Low | 364 cadnums queued for Phase 1.13 manual review |
| `tools/build_lookup_map_common.py` orphan after legacy archive | Low | Medium | Verify import graph before ADR 020 D8 archive |
| Combined gzip cap breach (>5.5 MB) | Low | High | ADR 007 v2 yellow-band monitoring; current headroom ~242 KB |
| Fire_Varna integration bypasses the curated bundle / publish gate | Low | Medium | Mitigated by ADR 020 Amendment 2 (Accepted 2026-06-21): reintegration runs under a curated public bundle + publish gate |
| ML footprint gaps / accuracy (~10% unmatched, IoU ~0.42, no BG confidence) | Medium | Medium | Point fallback (ADR 025 D3); realness gate (D5) |
| Fuzzy KAISâ†”geometry data join (~30% medium) attaches data to wrong building | Medium | Medium | `data_confidence` flag; fuzzy data shown as uncertain (ADR 025 D4) |
| ML imagery vintage lags new construction | Medium | Low | Point fallback; periodic OSM/ML refresh |

---

## Known unknowns

Tracked in [`unknowns.md`](unknowns.md). Highlights as of 2026-05-26:

- Whether `kais_cluster_flags.json` (ADR 019 sidecar) gets app-side
  consumption in Phase 1.13 (UI badges) or remains audit-only.
- Whether `strategic_intel.json#buildings[]` aggregate becomes the
  shared SOIS aggregation source for `build_classification.py` (which
  currently re-aggregates SOIS independently via
  `_load_sois_section_signals`).
- Whether the 14 SOIS absent-parent records (Probe B) get a documented
  data-quality dossier under `docs/audits/`.
- Phase 1.10 visual-group infrastructure disposition (currently dormant
  per ADR 018 D7; archive candidate for Phase 1.13).
- Stale JS regression baselines (Phase 1.7.6-era hardcoded expectations
  in `js/regression_categories/*.mjs`) â€” open refresh ticket.

---

## Governance

See [`AGENTS.md`](../AGENTS.md) for the dual-Claude-Code governance
workflow, approval gates, and the Planner / Executor / Auditor
operating protocols (ADR 057).

---

## Migration note from v1

This document supersedes `docs/architecture_v1.md` (2026-05-13). v1
described a single deliverable (`address_index.json` for Fire_Varna)
and a Pre-Phase-0 phase plan. By the time v1 was committed it was
already partial; by Phase 1.7 it was inadequate; by Phase 1.12 it
described a different product than the code built.

The replacement was authorised by ADR 020 (Map App as Primary Active
Product). v1 is preserved at
[`docs/archive/architecture_v1.md`](archive/architecture_v1.md) with an
archive header.

 succeeded in 603ms:
---
name: debug
description: Structured debugging session â€” reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.
argument-hint: "<error message or problem description>"
---

# /debug

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run a structured debugging session to find and fix issues systematically.

## Usage

```
/debug $ARGUMENTS
```

## How It Works

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                       DEBUG                                        â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  Step 1: REPRODUCE                                                â”‚
â”‚  âœ“ Understand the expected vs. actual behavior                   â”‚
â”‚  âœ“ Identify exact reproduction steps                             â”‚
â”‚  âœ“ Determine scope (when did it start? who is affected?)        â”‚
â”‚                                                                    â”‚
â”‚  Step 2: ISOLATE                                                   â”‚
â”‚  âœ“ Narrow down the component, service, or code path             â”‚
â”‚  âœ“ Check recent changes (deploys, config changes, dependencies) â”‚
â”‚  âœ“ Review logs and error messages                                â”‚
â”‚                                                                    â”‚
â”‚  Step 3: DIAGNOSE                                                  â”‚
â”‚  âœ“ Form hypotheses and test them                                 â”‚
â”‚  âœ“ Trace the code path                                           â”‚
â”‚  âœ“ Identify root cause (not just symptoms)                      â”‚
â”‚                                                                    â”‚
â”‚  Step 4: FIX                                                       â”‚
â”‚  âœ“ Propose a fix with explanation                                â”‚
â”‚  âœ“ Consider side effects and edge cases                          â”‚
â”‚  âœ“ Suggest tests to prevent regression                           â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## What I Need From You

Tell me about the problem. Any of these help:
- Error message or stack trace
- Steps to reproduce
- What changed recently
- Logs or screenshots
- Expected vs. actual behavior

## Output

```markdown
## Debug Report: [Issue Summary]

### Reproduction
- **Expected**: [What should happen]
- **Actual**: [What happens instead]
- **Steps**: [How to reproduce]

### Root Cause
[Explanation of why the bug occurs]

### Fix
[Code changes or configuration fixes needed]

### Prevention
- [Test to add]
- [Guard to put in place]
```

## If Connectors Available

If **~~monitoring** is connected:
- Pull logs, error rates, and metrics around the time of the issue
- Show recent deploys and config changes that may correlate

If **~~source control** is connected:
- Identify recent commits and PRs that touched affected code paths
- Check if the issue correlates with a specific change

If **~~project tracker** is connected:
- Search for related bug reports or known issues
- Create a ticket for the fix once identified

## Tips

1. **Share error messages exactly** â€” Don't paraphrase. The exact text matters.
2. **Mention what changed** â€” Recent deploys, dependency updates, and config changes are top suspects.
3. **Include context** â€” "This works in staging but not prod" or "Only affects large payloads" narrows things fast.
---
name: architecture
description: Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.
argument-hint: "<decision or system to design>"
---

# /architecture

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Create an Architecture Decision Record (ADR) or evaluate a system design.

## Usage

```
/architecture $ARGUMENTS
```

## Modes

**Create an ADR**: "Should we use Kafka or SQS for our event bus?"
**Evaluate a design**: "Review this microservices proposal"
**System design**: "Design the notification system for our app"

See the **system-design** skill for detailed frameworks on requirements gathering, scalability analysis, and trade-off evaluation.

## Output â€” ADR Format

```markdown
# ADR-[number]: [Title]

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** [Date]
**Deciders:** [Who needs to sign off]

## Context
[What is the situation? What forces are at play?]

## Decision
[What is the change we're proposing?]

## Options Considered

### Option A: [Name]
| Dimension | Assessment |
|-----------|------------|
| Complexity | [Low/Med/High] |
| Cost | [Assessment] |
| Scalability | [Assessment] |
| Team familiarity | [Assessment] |

**Pros:** [List]
**Cons:** [List]

### Option B: [Name]
[Same format]

## Trade-off Analysis
[Key trade-offs between options with clear reasoning]

## Consequences
- [What becomes easier]
- [What becomes harder]
- [What we'll need to revisit]

## Action Items
1. [ ] [Implementation step]
2. [ ] [Follow-up]
```

## If Connectors Available

If **~~knowledge base** is connected:
- Search for prior ADRs and design docs
- Find relevant technical context

If **~~project tracker** is connected:
- Link to related epics and tickets
- Create implementation tasks

## Tips

1. **State constraints upfront** â€” "We need to ship in 2 weeks" or "Must handle 10K rps" shapes the answer.
2. **Name your options** â€” Even if you're leaning one way, I'll give a more balanced analysis with explicit alternatives.
3. **Include non-functional requirements** â€” Latency, cost, team expertise, and maintenance burden matter as much as features.

 succeeded in 442ms:
4c6b482 plan: resorts as quarters in the Fire_Varna search index — measure of 02.09, Kimi verdict, second measure (not executed)
C:/git/Fire_Varna\AGENTS.md
C:/git/Fire_Varna\CLAUDE.md
C:/git/Fire_Varna\docs\decisions\010_signed_quarter_boundaries.md
C:/git/Fire_Varna\scratch\places_search\adresi_po_poligon_measure_08.09.json
C:/git/Fire_Varna\scratch\places_search\adresi_bridge_depth_08.09.json
C:/git/Fire_Varna\scratch\places_search\adresi_po_poligon_measure_08.09.md
C:/git/varna_3d\CLAUDE.md
C:/git/varna_3d\AGENTS.md
js\app_m1_parity_validation.mjs:13://   app/modules/search/data/search_bridge.json     — M1 derivative
js\app_m1_parity_validation.mjs:71:  REPO_ROOT, "app/modules/search/data/search_bridge.json",
js\app_m1_parity_validation.mjs:214:// SEARCH_BRIDGE rather than the M1 search_bridge.json.
js\build_fire_varna_search_index.mjs:10://   app/modules/search/data/search_bridge.json  (private; build-time-only — the
js\build_fire_varna_search_index.mjs:141:// "TOKEN-INCONSISTENT LABEL OVERRIDE" section below). search_bridge holds the cluster
js\build_fire_varna_search_index.mjs:143:const BRIDGE_PATH = resolve(REPO_ROOT, "app/modules/search/data/search_bridge.json");
js\build_fire_varna_search_index.mjs:414:// entry.label with the publish-safe block-aware cluster label (search_bridge), and
js\build_fire_varna_search_index.mjs:512:// Load search_bridge once → { clusterLabelByCad: Map<cadnum, label>, cadnumToCluster:
js\lib_fire_varna_consolidation.mjs:74:// cluster_id (from search_bridge.cadnum_to_cluster_id). Returns { gForEntry, stats }:
js\test_block_parcel_bridge_gate.mjs:59:const SEARCH_BRIDGE_PATH = path.resolve(REPO_ROOT, 'app/modules/search/data/search_bridge.json');
js\build_geocoder_index.mjs:21:// {lat, lng}. The geocoder NEVER emits [lng, lat] — the search_bridge summary
js\build_geocoder_index.mjs:47:// building_type aggregation) and joined by search_bridge cadnum->cluster_id.
js\build_geocoder_index.mjs:99:// ADR 037 C1 — search_bridge.cadnum_to_cluster_id is the cadnum->cluster join
js\build_geocoder_index.mjs:101:// READ-ONLY: this builder never writes search_bridge (OFF-shared); its bytes and
js\build_geocoder_index.mjs:105:  "app/modules/search/data/search_bridge.json",
js\build_geocoder_index.mjs:113:// search_bridge above).
js\build_geocoder_index.mjs:758://   - cadnumToCluster: search_bridge.cadnum_to_cluster_id (ADR 037 C1; optional —
js\build_geocoder_index.mjs:816:  // cluster). cadnum->cluster_id comes from search_bridge. NOTHING here touches
js\build_geocoder_index.mjs:1632:  // READ-ONLY: search_bridge is not written here; its bytes + the OFF path that
js\build_geocoder_index.mjs:1822:      "app/modules/search/data/search_bridge.json",
js\build_geocoder_index.mjs:1874:      "app/modules/search/data/search_bridge.json": ["cadnum_to_cluster_id"],
js\test_osm_address_fold.mjs:237:      readFileSync(P("app/modules/search/data/search_bridge.json"), "utf8")),
js\test_geocoder_index.mjs:45:  "app/modules/search/data/search_bridge.json",
js\test_geocoder_index.mjs:181:  // claimer clusters; the 439 geocoder entries joined to them (search_bridge
tools\build_app_m1_data.py:10:    app/modules/search/data/search_bridge.json
tools\build_app_m1_data.py:124:SEARCH_BRIDGE_PATH = SEARCH_DATA_DIR / "search_bridge.json"
tools\build_app_m1_data.py:1159:    geojson, details, search_bridge = build_html_payloads(
tools\build_app_m1_data.py:1170:    # search_bridge stays complete (all clusters) so search behavior is
tools\build_app_m1_data.py:1222:    bridge_cluster_ids = set(search_bridge["cadnum_to_cluster_id"].values())
tools\build_app_m1_data.py:1238:        "cadnum_to_cluster_id": search_bridge["cadnum_to_cluster_id"],
tools\build_app_m1_data.py:1239:        "parcel_cadnum_to_cluster_ids": search_bridge[
tools\build_app_m1_data.py:1541:    search_bridge_bytes = _dump_json(
tools\build_app_m1_data.py:1547:    search_bridge_gzip = len(_gzip.compress(SEARCH_BRIDGE_PATH.read_bytes()))
tools\build_app_m1_data.py:1595:        f"({search_bridge_bytes:,} bytes raw, {search_bridge_gzip:,} bytes gzip)",
tools\build_quarter_trust_sidecar.py:11:CONFIDENT (kais | high | polygon_cover) neighbour <= 150 m in EPSG:32635
tools\build_quarter_trust_sidecar.py:90:        if mode == "polygon_cover":
tools\build_quarter_trust_sidecar.py:214:                "with a DIFFERENT-кв CONFIDENT (kais|high|polygon_cover) "
tools\build_quarter_trust_sidecar.py:218:                "trusted = kais|high|polygon_cover; unverified = candidate "
tools\build_lookup_map_v2.py:1023:            "mode": "polygon_cover",
tools\build_lookup_map_v2.py:1043:        assignment["margin_ratio"] = second_d / nearest_d
tools\build_lookup_map_v2.py:1046:        assignment["margin_ratio"] = None
tools\build_lookup_map_v2.py:1062:    if mode == "polygon_cover":
tools\build_lookup_map_v2.py:1066:        m = assignment.get("margin_ratio")
tools\build_lookup_map_v2.py:1130:        if "margin_ratio" in assignment:
tools\build_lookup_map_v2.py:1131:            quarter_meta["margin_ratio"] = assignment["margin_ratio"]
tools\build_lookup_map_v2.py:1560:def _build_search_bridge(
tools\build_lookup_map_v2.py:1644:            # no feature/detail; the cluster stays in search_bridge below.
tools\build_lookup_map_v2.py:1654:    search_bridge = _build_search_bridge(clusters)
tools\build_lookup_map_v2.py:1655:    return geojson, details, search_bridge
tools\build_lookup_map_v2.py:1669:    search_bridge: dict[str, Any],
tools\build_lookup_map_v2.py:1679:        search_bridge, ensure_ascii=False, separators=(",", ":"),
tools\build_lookup_map_v2.py:1896:    geojson, details, search_bridge = build_html_payloads(
tools\build_lookup_map_v2.py:1934:    html = render_html_v2(geojson, details, search_bridge)
tools\build_lookup_map_v2.py:1937:    cadnum_map_count = len(search_bridge["cadnum_to_cluster_id"])
tools\build_lookup_map_v2.py:1938:    parcel_map_count = len(search_bridge["parcel_cadnum_to_cluster_ids"])
tools\m6000\address_fill_phase_b.py:165:        "search_bridge": _fp(common.SEARCH_BRIDGE_JSON),
tools\m6000\address_fill_phase_b.py:506:    cadnums → clusters (search_bridge) → footprints (clusters.geojson),
tools\m6000\address_fill_phase_b.py:1139:        "search_bridge": _fp(common.SEARCH_BRIDGE_JSON),
tools\m6000\address_fill_phase_b.py:1239:    """``quarter_name -> [BGS2005 geom]`` for every cluster whose ``search_bridge``
tools\m6000\address_gap_phase_a.py:63:        "search_bridge": common.source_fingerprint(common.SEARCH_BRIDGE_JSON),
tools\m6000\common.py:67:    REPO_ROOT, "app", "modules", "search", "data", "search_bridge.json")
tools\m6000\quarter_hint.py:11:(the §3 gate). No writes here; search_bridge is opened read-only.
tools\m6000\quarter_hint.py:26:    """Lazy cadnum → quarter resolver over ``search_bridge.cluster_summaries``."""
tools\m6000\quarter_hint.py:28:    def __init__(self, search_bridge_path: str = None):
tools\m6000\quarter_hint.py:29:        self._path = search_bridge_path or common.SEARCH_BRIDGE_JSON
tools\m6000\quarter_hint.py:39:            common.log(f"[quarter_hint] search_bridge absent ({self._path}); all rows unassigned")

codex
Прилагам уменията `engineering:debug` и `engineering:architecture` за диагнозата и сравняването на решенията. Разделям проверката на три независими части: произход на алгоритъма, възпроизводимост на числата и статут на подписаните граници.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; rg -n "quarter|BRIDGE_PATH|bridge|trusted|unverified|confidence" js/build_fire_varna_search_index.mjs tools/build_quarter_trust_sidecar.py | Select-Object -First 160' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; Get-Content -Encoding utf8 C:/git/Fire_Varna/AGENTS.md; Get-Content -Encoding utf8 C:/git/varna_3d/AGENTS.md; rg -n "quarter|Per-attribute authority|determin|Fire_Varna" docs/architecture_v2.md' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; Get-Content -Encoding utf8 C:/git/Fire_Varna/scratch/places_search/adresi_po_poligon_measure_08.09.md' in C:\git\Varna_buildings
 succeeded in 432ms:
tools/build_quarter_trust_sidecar.py:2:"""ADR 039 C0 / D3 — build the quarter-trust sidecar.
tools/build_quarter_trust_sidecar.py:5:M1-locked ``normalize_quarter`` shape adapter (the live artifact carries the
tools/build_quarter_trust_sidecar.py:6:OLD confidence-sentinel quarter shape; the accepted-but-unimplemented ADR 015
tools/build_quarter_trust_sidecar.py:14:Emits the gitignored ``output/quarter_trust_sidecar.json``:
tools/build_quarter_trust_sidecar.py:16:  - ``trust_by_cluster``: per-cluster ``quarter_assignment_trust`` in
tools/build_quarter_trust_sidecar.py:17:    {trusted, unverified, conflicted}. Flagged (osm + nearest_point +
tools/build_quarter_trust_sidecar.py:18:    confidence "flagged") clusters are MAPPED TO ``conflicted`` with
tools/build_quarter_trust_sidecar.py:46:DEFAULT_OUT = _REPO_ROOT / "output" / "quarter_trust_sidecar.json"
tools/build_quarter_trust_sidecar.py:68:# --- M1-locked quarter shape adapter (scratch/adr039_e0/m1_shape_adapter.json)
tools/build_quarter_trust_sidecar.py:71:def normalize_quarter(quarter):
tools/build_quarter_trust_sidecar.py:72:    """Adapt a cluster_details quarter dict to (family, band).
tools/build_quarter_trust_sidecar.py:75:    band:   the nearest_point confidence band (low/medium/high/flagged) or None.
tools/build_quarter_trust_sidecar.py:77:    Returns None for a missing/empty-name quarter (the cluster carries no
tools/build_quarter_trust_sidecar.py:78:    quarter assignment and never enters the trust map). Raises ValueError on
tools/build_quarter_trust_sidecar.py:79:    a quarter shape neither the OLD (confidence-sentinel) nor the ADR 015
tools/build_quarter_trust_sidecar.py:82:    if not isinstance(quarter, dict) or not quarter.get("name"):
tools/build_quarter_trust_sidecar.py:84:    source = quarter.get("source")
tools/build_quarter_trust_sidecar.py:85:    # OLD (live) shape — confidence sentinel.
tools/build_quarter_trust_sidecar.py:89:        mode = quarter.get("mode")
tools/build_quarter_trust_sidecar.py:93:            band = quarter.get("confidence")
tools/build_quarter_trust_sidecar.py:97:                f"unknown nearest_point confidence band: {band!r}"
tools/build_quarter_trust_sidecar.py:107:        band = quarter.get("quality")
tools/build_quarter_trust_sidecar.py:111:    raise ValueError(f"unknown quarter shape (source={source!r})")
tools/build_quarter_trust_sidecar.py:132:    trust = {}  # cid -> trusted | candidate | conflicted | flagged | other
tools/build_quarter_trust_sidecar.py:136:        q = d.get("quarter") if isinstance(d, dict) else None
tools/build_quarter_trust_sidecar.py:137:        adapted = normalize_quarter(q)
tools/build_quarter_trust_sidecar.py:139:            continue  # no quarter assignment — not in the trust map
tools/build_quarter_trust_sidecar.py:145:            trust[cid] = "trusted"
tools/build_quarter_trust_sidecar.py:147:            trust[cid] = "candidate"  # refined below to unverified/conflicted
tools/build_quarter_trust_sidecar.py:178:            trust[cid] = "unverified"
tools/build_quarter_trust_sidecar.py:185:        "with_quarter_total": len(trust),
tools/build_quarter_trust_sidecar.py:187:        "trusted": sum(1 for t in trust.values() if t == "trusted"),
tools/build_quarter_trust_sidecar.py:188:        "unverified": sum(1 for t in trust.values() if t == "unverified"),
tools/build_quarter_trust_sidecar.py:204:            "tool": "tools/build_quarter_trust_sidecar.py",
tools/build_quarter_trust_sidecar.py:205:            "adr": "039 D3 — quarter_assignment_trust conflict precompute",
tools/build_quarter_trust_sidecar.py:209:                "confidence-sentinel shape; ADR 015 shape adapted; unknown "
tools/build_quarter_trust_sidecar.py:218:                "trusted = kais|high|polygon_cover; unverified = candidate "
tools/build_quarter_trust_sidecar.py:247:        "quarter_trust_sidecar: with_quarter={with_quarter_total} "
tools/build_quarter_trust_sidecar.py:248:        "trusted={trusted} unverified={unverified} conflicted={conflicted} "
js/build_fire_varna_search_index.mjs:10://   app/modules/search/data/search_bridge.json  (private; build-time-only — the
js/build_fire_varna_search_index.mjs:22:// "чайка" rows and NO area-gating, so "блок 1 чайка" could not filter by quarter.
js/build_fire_varna_search_index.mjs:39://        physical_building_id, physical_building_reps, bg, quarter_assignment_trust,
js/build_fire_varna_search_index.mjs:111:  from "./lib_quarter_registry.mjs";
js/build_fire_varna_search_index.mjs:127:// quarters cycle runs with FIRE_VARNA_OUT_DIR=output/fire_varna_staging.
js/build_fire_varna_search_index.mjs:141:// "TOKEN-INCONSISTENT LABEL OVERRIDE" section below). search_bridge holds the cluster
js/build_fire_varna_search_index.mjs:143:const BRIDGE_PATH = resolve(REPO_ROOT, "app/modules/search/data/search_bridge.json");
js/build_fire_varna_search_index.mjs:148:// around the PARCEL enclosure of кв. Виница that carries NO quarter evidence is shown
js/build_fire_varna_search_index.mjs:165:      '  python -m tools.build_quarname_enclosures --quarter "кв. Виница" ' +
js/build_fire_varna_search_index.mjs:169:  if (doc.properties?.quarter !== VINITSA_DISPLAY) {
js/build_fire_varna_search_index.mjs:170:    throw new Error(`Р38: zone is for "${doc.properties?.quarter}", expected "${VINITSA_DISPLAY}"`);
js/build_fire_varna_search_index.mjs:256:  // OUR-001 double bridge: the 26 kept-key addresses have addr_key=None in the geocoder,
js/build_fire_varna_search_index.mjs:259:  const bridge = doc.our001_bridge || {};
js/build_fire_varna_search_index.mjs:260:  const bridgeCadnums = new Set(
js/build_fire_varna_search_index.mjs:261:    Array.isArray(bridge.bridge_cadnums) ? bridge.bridge_cadnums.map(String) : [],
js/build_fire_varna_search_index.mjs:263:  const bridgeTokens = [];
js/build_fire_varna_search_index.mjs:264:  if (Array.isArray(bridge.bridge_alias_keys)) {
js/build_fire_varna_search_index.mjs:265:    for (const form of bridge.bridge_alias_keys)
js/build_fire_varna_search_index.mjs:266:      for (const t of String(form).split(/\s+/).map(skel)) if (t) bridgeTokens.push(t);
js/build_fire_varna_search_index.mjs:320:  return { rename, aliasTokens, bridgeCadnums, bridgeTokens, suppress, suppressCadnums, suppressExpected };
js/build_fire_varna_search_index.mjs:399:// ["zhk","vazrazhdane","1","bl","10"] (it is found by block 10 + quarter, NOT by the
js/build_fire_varna_search_index.mjs:414:// entry.label with the publish-safe block-aware cluster label (search_bridge), and
js/build_fire_varna_search_index.mjs:416:// the quarter prefix, passes the SAME 3 S9 rules). No chosen_value fallback.
js/build_fire_varna_search_index.mjs:448:// address_index + bridge) — addr_key-sourced + normalized_address-sourced together.
js/build_fire_varna_search_index.mjs:475:  if (idx > 0) return { quarter: localLabel.slice(0, idx), rest: localLabel.slice(idx + 2) };
js/build_fire_varna_search_index.mjs:476:  return { quarter: "", rest: localLabel };
js/build_fire_varna_search_index.mjs:512:// Load search_bridge once → { clusterLabelByCad: Map<cadnum, label>, cadnumToCluster:
js/build_fire_varna_search_index.mjs:513:// Map<cadnum, cluster_id>, clusterInfoByCluster: Map<cluster_id, {quarter, addrLine}> }.
js/build_fire_varna_search_index.mjs:514:// Reads the 29 MB bridge in a scoped helper so the parsed object is freed before pass 2.
js/build_fire_varna_search_index.mjs:517:// consolidated block label (modal quarter.name + street-disambiguation address_line).
js/build_fire_varna_search_index.mjs:519:  const bridge = JSON.parse(readFileSync(path, "utf8"));
js/build_fire_varna_search_index.mjs:520:  const c2c = bridge.cadnum_to_cluster_id || {};
js/build_fire_varna_search_index.mjs:521:  const cs = bridge.cluster_summaries || {};
js/build_fire_varna_search_index.mjs:536:    const quarter = s.quarter && typeof s.quarter.name === "string" ? s.quarter.name : null;
js/build_fire_varna_search_index.mjs:538:    if (quarter || addrLine) clusterInfoByCluster.set(cid, { quarter, addrLine });
js/build_fire_varna_search_index.mjs:591:    // consistency is checked on splitQuarter(.rest) so a "ж.к. X 1, бл. 10" quarter
js/build_fire_varna_search_index.mjs:704:    // street key) + OUR-001 bridge (by cadnum, since those entries have addr_key=None).
js/build_fire_varna_search_index.mjs:712:      const bridge = V2_MODEL.bridgeCadnums.has(String(e.cadnum))
js/build_fire_varna_search_index.mjs:713:        ? V2_MODEL.bridgeTokens : null;
js/build_fire_varna_search_index.mjs:714:      if ((extra && extra.length) || (bridge && bridge.length)) {
js/build_fire_varna_search_index.mjs:717:        if (bridge) for (const t of bridge) merged.add(t);
js/build_fire_varna_search_index.mjs:815:    // "<quarter>, бл. <N>[, <street>]" from the SAME buildBlockLabelIndex the C2
js/build_fire_varna_search_index.mjs:879:      // Evidence = a quarter the row already carries, in tokens or in its display.
js/build_fire_varna_search_index.mjs:881:        || (o.label != null && qrCls !== "no_quarter_segment");
js/build_fire_varna_search_index.mjs:883:        // The measured-wrong quarter inside the zone: the DISPLAY is corrected, and
js/build_fire_varna_search_index.mjs:986:      quarterRegistry: {
js/build_fire_varna_search_index.mjs:1000:      quarterRegistrySigned: QREG.reg.signed,
js/build_fire_varna_search_index.mjs:1017:  // Build-time-only bridge maps (the big parsed bridge is freed inside the helper):
js/build_fire_varna_search_index.mjs:1019:  // clusterInfoByCluster (quarter.name + address_line) for the C2 consolidated block label.
js/build_fire_varna_search_index.mjs:1020:  const { clusterLabelByCad, cadnumToCluster, clusterInfoByCluster } = loadBridgeMaps(BRIDGE_PATH);
js/build_fire_varna_search_index.mjs:1022:  // Block-parcel bridge: detect split blocks over section_units and resolve every
js/build_fire_varna_search_index.mjs:1025:  const bridge = (() => buildBlockParcelBridgeContext(
js/build_fire_varna_search_index.mjs:1028:    cadnumToCluster, salt, canonicalComplexId: bridge.canonicalComplexId,
js/build_fire_varna_search_index.mjs:1031:  // (C2) Per-complex_id consolidated block label index (modal quarter.name + street
js/build_fire_varna_search_index.mjs:1079:  console.log(`  block_parcel_bridge= merged_pairs:${bridge.mergedPairs.length} ` +
js/build_fire_varna_search_index.mjs:1080:    `(auto:${bridge.stats.autoMerged} allowlist:${bridge.stats.allowlistMerged}) ` +
js/build_fire_varna_search_index.mjs:1081:    `bridged_entries:${keyStats.blockBridged} reported_candidates:${bridge.stats.reported} ` +
js/build_fire_varna_search_index.mjs:1082:    `[бл ${bridge.mergedPairs.map((m) => m.block_number).join(", ")}]`);
js/build_fire_varna_search_index.mjs:1112:  console.log("  --- C2 consolidated block label (modal quarter, keep prefix; street on collision) ---");
js/build_fire_varna_search_index.mjs:1113:  console.log(`  block_groups             = ${blockLabelStats.blockGroups} (labeled ${blockLabelStats.labeled}, no_safe_quarter ${blockLabelStats.noQuarter})`);
js/build_fire_varna_search_index.mjs:1114:  console.log(`  raion_deprioritized      = ${blockLabelStats.raionDeprioritized} (groups whose quarter switched to a finer квартал name vs район-naive modal)`);
js/build_fire_varna_search_index.mjs:1115:  console.log(`  post_consolidation_collisions = ${blockLabelStats.collisionPairs} (quarter,block#) pairs over ${blockLabelStats.collisionGroups} groups`);
js/build_fire_varna_search_index.mjs:1130:  // --- (C2) quarter registry + Р38 zone: report == diff ---------------------------
js/build_fire_varna_search_index.mjs:1131:  const qr = stats.quarterRegistry;
js/build_fire_varna_search_index.mjs:1133:  console.log("  --- C2 quarter registry v1.1 over EVERY quarter-prefixed row ---");
js/build_fire_varna_search_index.mjs:1149:  const reviewPath = resolve(REPO_ROOT, "output/quarter_registry_review.json");
js/build_fire_varna_search_index.mjs:1151:    signed: stats.quarterRegistrySigned,
js/build_fire_varna_search_index.mjs:1154:    quarter_registry: qr,

 succeeded in 639ms:
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

## Data Model

`data/hydrants.json` is the runtime dataset. The original KMZ-derived `hydrants_varna.json` remains as a reference/source artifact, not the full runtime dataset.

Runtime verbose schema (compact-schema compatibility was removed in `142a494`):

```text
{ id, coords, origin, legacy_ids, type?, region?, address?,
  existence_status?, operational_status?, review_status?,
  verifier_note?, report_id?, reported_at? }
```

- `coords` is `[lon, lat]` in WGS84 and is always present.
- `origin` is always present. Canonical network origins are `vik` (В и К export) and `national` (national dataset); field-submitted records carry `field_report`. The `etr_*` origins are the post-2026-06-21 ЕТР hydrant-register KMZ imports (`Пожарни хидранти ЕТР ….kmz`), one `origin` per municipality. `pozarna_gz` is not an ЕТР register but a separate import; it is listed in the same table:

  | `origin` | Source (register or import) |
  |---|---|
  | `etr_varna` | ЕТР Варна |
  | `etr_provadia` | ЕТР Провадия |
  | `etr_dolni_chiflik` | ЕТР Долни Чифлик |
  | `etr_devnya` | ЕТР Девня |
  | `pozarna_gz` | POZARNA.DWG import, Golden Sands (commit `e846b87`) |

  Import mechanics (distance-≤5 m ETR aliases folded into `legacy_ids`; only unmatched ETR points added as standalone records) are in [`docs/plans/h2_kmz_adapter_plan.md`](docs/plans/h2_kmz_adapter_plan.md) and the dry-run audit `docs/audits/h2_kmz_consolidation_dry_run.md`; per-source counts and the current baseline live in [`docs/activeContext.md`](docs/activeContext.md). Further `etr_*` origins may appear as more municipal registers are imported. Older app builds and unknown `origin` values must fall back to canonical/unverified rendering.
- `legacy_ids` is the array of a record's prior IDs (used for polling dedupe); always present.
- `type`, `region`, `address` are sparse descriptive fields.
- Visual / moderation state is split across three sparse fields, not one app-level `status`:

| Field | Observed values | Meaning / render |
|---|---|---|
| `existence_status` | `verified` | Hydrant physically confirmed on-site (red pin) |
| `review_status` | none present in the dataset today (historically `reported`) | Reported damaged / missing / needs attention (yellow pin) |
| `operational_status` | `works`, `not_working`, `not_tested` | Operational state, independent of existence |
| (all three absent) | — | Canonical unverified record (gray pin) |

Older app builds and unknown values must fall back to canonical/unverified behavior. `report_id` / `reported_at` carry field-report provenance.

### Wrong-Location Ingest Rule

For `wrong_location` reports, **always update the existing record's coordinate field (`coords`) in place. Never create a new `field_*` record for `wrong_location`.**

| Target ID type | Action |
|---|---|
| Canonical IDs (every id starts with `coord_<lon>_<lat>`; disambiguated duplicates carry a `__NAT-####` suffix (count them with `python -c "import json;print(sum(1 for r in json.load(open('data/hydrants.json',encoding='utf-8')) if '__' in r['id']))"`); `NAT-`, `VIK-`, `GZ-` survive in `legacy_ids`) | update `coords` in `data/hydrants.json` |
| `field_*` IDs (no record carries one today; `field_*` survives only in `legacy_ids`) | update `coords` in `data/hydrants.json` |

`field_reports.json` is no longer a current file; all records (including `field_*`) live in `data/hydrants.json` only. After the coord update, set `existence_status` to `"verified"`. Old coords go in the commit message for audit trail. A `new_hydrant` report creates a record with a `coord_<lon>_<lat>` id; the `field_*` identifier it came in with is kept in `legacy_ids`. No record in the dataset carries a `field_*` id.

### National Dataset Role

The national source files are kept as archive/reference only. They are not loaded directly at runtime.

Future option, not implemented: build-time enrichment of runtime data with national metadata only where spatial match is <=5m. Defer until there is concrete user demand.

---

## Report Flow

Reports are submitted via `fetch` POST to Cloudflare Worker `varna-hydrants-proxy.petar-dikov2019.workers.dev`. Worker creates a labeled GitHub issue in this repo. Reports queue locally if offline.

Worker source now lives in the `worker/` directory in this repo (extracted in `914dc2a`); see `worker/README.md` for deploy notes. The Cloudflare deployment remains manual; the Worker deploy version is repo-declared as `5accc88e`.

---

## Hard Constraints

| Constraint | Reason |
|---|---|
| Static hosting only (GitHub Pages free tier) | Budget = 0 BGN |
| App shell at repo root (`index.html`) plus static `data/hydrants.json` | GitHub Pages serves it |
| First load <= 3 MB ideal, **5 MB hard cap** | Mobile data, emergency use |
| Bulgarian UI labels preserved verbatim | Users speak Bulgarian only; wording is reviewed |
| Mobile-first: touch targets >= 44px, no hover-dependent UX | Field use, gloves, sweat |
| HTTPS-required APIs must work: Geolocation, DeviceOrientation, Worker `fetch` | Core features depend on these |
| **Scope: Varna oblast only** | National scope explicitly out of v1 |
| No new runtime or build-time dependencies without Petar approval | Keep static architecture simple |
| No secrets in the repo — Cloudflare/Worker credentials, `wrangler` secrets, `.dev.vars`, `.env` are gitignored and never committed | Public GitHub Pages repo |
| No automated commits, no automated pushes — agents commit locally with explicit paths; **Petar alone pushes** | Reversibility & release control |

---

## Dual-Claude-Code Workflow

All planning, execution, and audit run in **Claude Code** (Planner read-only / Executor / Auditor — model per `~/.claude/agents`, not pinned here) with planning and execution kept in **separate agents**; Petar holds the sign-off and push gates. See ADR [`docs/decisions/003_dual_claude_code_governance.md`](docs/decisions/003_dual_claude_code_governance.md).

| Role | Agent | What it can do | What it cannot do |
|---|---|---|---|
| **Planner** | Claude Code (Opus, read-only) | Read the repo, measure, draft plans, architect, audit | Edit tracked files, commit, push |
| **Researcher** | Claude Code (Opus, read-only) | Planner sub-phase: gather evidence and measurements | Edit files, decide architecture |
| **Executor** | Claude Code (Opus) | Implement the Petar-signed plan, edit files, create local commits | Architect, expand scope, push |
| **Auditor** | Claude Code (Opus, read-only, adversarial) | Independently verify the Executor's diff against the plan | Edit files, push |
| **Orchestrator** | Petar | Sign plans (Gate 1), review diffs (Gate 2), push to remote | — |

**Petar = orchestrator and sole push authority.** All architectural and data decisions go through him. Chain: `Planner → GATE 1 (Petar signs) → Executor (local commit) → Auditor → GATE 2 (Petar reviews diff) → Petar pushes`.

Approval gates:

- **Architecture changes** (file layout, module split, new patterns) -> Planner discussion + ADR first.
- **Data source changes** -> fresh Planner analysis required.
- **UI label / wording changes** -> Petar approval.
- **New runtime or build-time dependencies** -> Petar approval.
- **Refactoring scope** -> Planner plan (signed by Petar) + Petar approval before edits.

### Planner Plan Preamble Checklist

Every Planner plan/proposal must include: request scope, deterministic inventory, files read, negative-findings matrix, quoted declared metadata, decision ledger, approval-gate check, and open questions.

Decision ledger schema:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Worker source extracted to `worker/` (`914dc2a`) | Repo evidence | `worker/` holds the Worker source + README; deploy version repo-declared `5accc88e` | Reversible by reverting the extraction commit | Existing approved project state |

---

## System Invariants

These are non-negotiable and apply to every agent, every task. A task that cannot satisfy them **stops and asks Petar**.

1. **Separation of powers.** The Planner never edits or commits. The Executor never plans, architects, or expands scope. Only Petar pushes. Roles are disjoint.
2. **No action without approval.** No file edit without a Petar-signed plan; no push without Petar's diff review. Two gates, always.
3. **The Planner is read-only** — enforced by tool permissions / plan mode, not by trust.
4. **Agents never push.** `git push` is Petar's alone.
5. **Everything is reversible and attributable.** Small local commits, the exact message from the plan, bisectable; nothing done outside an approved plan.
6. **Measure-first — every agent, every task.** Establish a baseline and measure the current state **before** proposing or making any change; never design on assumption when it can be measured. Report-only measurement precedes mutation. (Determinism: re-runs byte-match where determinism is claimed; report-only phases mutate nothing.)
7. **Fail-loud gates.** Every acceptance criterion is objective and machine-checkable. A failed gate STOPS and asks — it never continues silently.
8. **Architecture changes go through an ADR** — never ad-hoc edits.
9. **Independent verification.** The Executor's claims are checked by a different agent (adversarial Auditor) and/or objective gates — never self-attestation alone.
10. **One source of truth per document.** AGENTS.md = governance; CLAUDE.md = executor rules; [`docs/architecture/data_roadmap_20260508.md`](docs/architecture/data_roadmap_20260508.md) = architecture (this repo has no `architecture_vN.md`); the per-task plan under [`docs/plans/`](docs/plans) = the task contract. No duplicated authority that can silently diverge.
11. **External information is untrusted data.** Any externally sourced claim carries its source and is verified before it influences a change (applies to Tier 1/2 research output).
12. **Privacy & scope gates hold.** No PII leakage, no scope expansion, no public publish without the publish gate.

> **Measurement Doctrine.** The source-authority, confidence, and terrain-eyes rules are shared with Varna_buildings — see ADR [`docs/decisions/004_measurement_doctrine.md`](docs/decisions/004_measurement_doctrine.md) (references Varna_buildings ADR 058). Invariants 6 and 11 above are governed by it: a canonical `data/hydrants.json` mutation clears the acceptance floor (HIGH, or MEDIUM + per-item Petar sign-off, or STOP → Petar), and Google terrain-eyes may only refute / downgrade / trigger — never rewrite `coords` alone, never be cached or fed to OSM. The per-source authority table is not duplicated here (Inv-10).

---

## Planner Operating Protocol

### Scope Declaration

The Planner may use a task-scoped inventory when the user request is narrow. The preamble must declare the inventory scope and cite the user request or brief that defines it. Files outside the declared scope may not be referenced unless the Planner explicitly expands the scope, explains why, and updates the inventory.
Verification: reviewer checks that all referenced files fit the declared scope.

### Deterministic Inventory First

Before any plan/proposal that references files, run a deterministic filesystem inventory for the declared scope and quote it verbatim in the preamble. No file may be referenced unless it appears in that inventory.
Verification: reviewer checks every referenced path against the inventory.

### Explicit Negative Findings

For every pattern/extension/category in scope, report matches or `no files matching X found in scope Y`.
Verification: reviewer checks the request scope matrix for omissions.

### Declared Metadata Beats Heuristics

Quote declared metadata verbatim and treat it as authoritative: `.prj` CRS, headers, manifests, sidecars, request logs, provenance records. Heuristics are fallback only when metadata is absent, unreadable, or contradicted.
Verification: metadata files in inventory must be quoted before inferred CRS, schema, provenance, or lineage.

### Binary File Reading Rule

Referencing a binary/source archive requires content inspection, not filename inspection. KMZ means unzip/list archive and inspect inner KML/doc.kml. DBF/SHP means inspect schema and metadata with `ogrinfo -al -so` / `ogrinfo -al` from GDAL, QGIS equivalent tooling, or a documented DBF/SHP parser. If required tooling is unavailable, state the file is unread and do not infer its contents.
Verification: plan lists tool used, command, and inspected inner files/layers.

### Referenced Files Must Be Read

If a file is referenced, its content must have been read in the same session. Path-name matching is not reading. Preamble must list `Files read`.
Verification: reviewer compares referenced paths against `Files read`.

### Non-ASCII Encoding Gate

Before committing or handing off files containing non-ASCII text, especially Cyrillic, verify UTF-8 round-trip integrity and scan for mojibake.

Per-file detection form:
`Select-String -Path <path> -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8`

Note: this regex uses Unicode escape notation (\u00D0 = Ð, \u00D1 = Ñ, \u00C2 = Â) rather than literal characters so this proposal file passes its own mojibake scan. When invoking the scan from a shell, either form is functionally equivalent.

Repo-wide pre-commit detection form:
`git diff --cached --name-only --diff-filter=ACMR | ForEach-Object { Select-String -Path $_ -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8 }`

Also recommend adding `.editorconfig` with `charset = utf-8` and a git pre-commit hook that blocks staged text files containing mojibake markers.
Verification: handoff notes include encoding check output; reviewer may rerun the command or hook.

---

## Current Repo State

Working directory: `C:\git\Fire_Varna`. Tracked top-level entries, as `git ls-files` reports them. Per-folder file counts are state, not rules — they are not carried here; read them from `git ls-files` when you need them:

```text
C:\git\Fire_Varna\
├── index.html                     <- current app shell
├── data/                          <- runtime hydrant data (hydrants.json — record count in
│                                     docs/activeContext.md; hydrants_provenance.json;
│                                     search_index.json + address_rows.json, built in Varna_buildings)
├── scripts/                       <- ingest / migration / backfill tooling
│   ├── apply_approved_reports.py
│   ├── migrate_to_verbose_schema.py
│   ├── backfill_addresses_20260511.py / backfill_verified_type_20260509.py
│   ├── replay_historical_new_hydrant.py
│   ├── import_etr_kmz.py          <- ЕТР KMZ register adapter
│   ├── copy_basemap_release.py / vendor_basemap_deps.mjs
│   └── lib/hydrant_core.py        <- H1 shared core (spatial dedup)
├── tests/                         <- unittest suite (test_hydrant_core.py,
│                                     test_apply_approved_reports_parity.py, golden fixtures);
│                                     verify_apply.py / verify_h4.py — one-off checkers (Р-21 of the 01.09 plan)
├── worker/                        <- Cloudflare Worker source + README (deploy version 5accc88e)
├── extract_hydrants.py            <- extracts embedded hydrant JSON from older index builds
├── hydrants_varna.json            <- original KMZ-derived reference dataset
├── sw.js                          <- service worker; index.html registers it only in PMTiles mode
├── vendor/                        <- vendored basemap runtime deps (pmtiles, protomaps-leaflet)
├── scratch/                       <- working material: boards, frames, apply reports, probes
├── audit/                         <- historical audit snapshots / plans
├── docs/                          <- activeContext, decisions, plans, audits, architecture roadmap
├── AGENTS.md / CLAUDE.md / README.md
└── .gitignore / .gitattributes
```

`field_reports.json` is no longer present (records merged into `data/hydrants.json`). `scripts/`, `tests/`, and `worker/` exist. There is no CI — confirmed absent, not merely unconfirmed: no `.github/` directory and no other CI configuration in the repo (`ls .github` → No such file or directory).

---

## Implemented Features

All working, tested on mobile.

1. **Auto-start GPS** on page load.
2. **Loading pill** during GPS acquisition; retry/manual controls on failure.
3. **Three view modes**:
   - "Близо <100м" - hydrants within 100m radius
   - "Топ 5" - default, 5 nearest by Haversine
   - "Всички" - full clustered overlay of every record in the dataset (count in `docs/activeContext.md`)
4. **Bottom sheet.** The hydrant bottom sheet was removed in the popup pivot (`tr '\n' ' ' < index.html | grep -c 'bottom sheet *was removed in the popup pivot'` → 1); the building-detail bottom sheet of the C4 search result (`.detail-sheet`, built by `ensureDetailSheet()` in `index.html`) exists and works — CLAUDE.md § Verification says exactly that.
5. **Compass arrow + heading cone** on user marker.
6. **Hybrid navigation** - distance >100m opens Google Maps, <=100m uses in-app compass target.
7. **Follow mode** - centers on user; user pan exits follow mode.
8. **Manual position mode** - next map click sets user position manually.
9. **Report flow** - `🚨`, long-press, or `+` opens structured report flow; submit goes to Cloudflare Worker.
10. **Real-time report polling** - reports auto-refresh every 15 seconds via Cloudflare Worker `GET /issues`. Status changes (`exists_confirmed`, `damaged`, `missing`, `wrong_location`) update existing pins in place via `marker.setIcon` / `marker.setLatLng`; `new_hydrant` reports are appended to the in-memory dataset. Polling pauses while the tab is hidden and resumes with an immediate catch-up on return.

Tap on a pin selects/activates it. Long-press on a pin opens the report menu. This is intentional and verified on the live site.

---

## Implementation Gotchas

- **`deviceorientation` fires at 100-200Hz on Android.** Store latest raw heading, run EMA once per `requestAnimationFrame`. `HEADING_SMOOTHING = 0.10`.
- **Use `L.divIcon` for all markers**, never `L.icon`.
- **MarkerCluster is only used in "Всички" mode.** "Близо" and "Топ" render plain numbered pins.
- **Auto-fit happens at three sites:** first GPS lock (`refresh(!deepLinkFramed)`), mode change (`setMode()` → `refresh(true)`) and the manual-position map click (`refresh(true)`); routine GPS ticks call `refresh(false)` (`grep -n -E 'refresh\(true\)|refresh\(!deepLinkFramed\)' index.html`).
- **A service worker exists (`sw.js`) but is off by default.** `index.html` registers it only when the PMTiles basemap capability is active, and the committed flag `BASEMAP_PMTILES_ENABLED` is `false` — so by default (no `?basemap_pmtiles=1` opt-in stored on the device) tiles on the live site are still fetched live from OSM.
- `index.html` now depends on `data/hydrants.json`; serve over HTTP locally so fetch works.

---

## Known Tech Debt

1. **HTML has accumulated patches.** `updateCard()` rebuilds full HTML on every refresh and rewires buttons after `innerHTML`.
2. **No build system.** Diffs are hard to read. Refactoring is post-launch.
3. **Data is static JSON.** Updating hydrants requires regenerating/reviewing `data/hydrants.json`.
4. **Worker source lives in `worker/`** (extracted in `914dc2a`); Cloudflare deploy is manual, deploy version repo-declared `5accc88e`.
5. **The offline tile cache exists but is off by default.** `sw.js` and the PMTiles basemap release under `data/basemaps/` are both in the repo; the committed flag `BASEMAP_PMTILES_ENABLED` is `false`, and only a per-device opt-in (`?basemap_pmtiles=1`; see `BASEMAP_PMTILES_ENABLED` and `isBasemapPmtilesActive()` in `index.html`) registers them — without it the app still fails where live OSM tiles cannot load.
6. **No PWA manifest.**
7. **Tests exist (`tests/`, Python unittest); there is no CI — confirmed absent (no `.github/`, no other CI configuration in the repo).**
8. **Bulgarian-only UI.** No localization layer.

---

## Windows Dev Environment

Defender exclusions applied (2026-05-06):

- ExclusionPath: `C:\git\Fire_Varna`
- ExclusionProcess: `git.exe`, `git-remote-https.exe`, `node.exe`

Primary workflow: agents edit + commit locally in the canonical working directory `C:\git\Fire_Varna`; **Petar alone pushes** after reviewing the diff (Gate 2). The deploy clone `Fire_Varna_deploy2` no longer exists on disk (`ls C:\git\Fire_Varna_deploy2` → no such file).

Fallback, only if exclusions fail: Python pre-place blob recovery technique. See git history for full procedure, search "blob corruption".

Verify exclusions monthly:

```powershell
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

---

## Glossary

| Bulgarian | English |
|---|---|
| Хидрант | Hydrant |
| Близо | Near |
| Всички | All |
| Точки | Points / markers |
| Сигнал | Signal / report |
| ВиК | Water utility |
| Район | District |
| Подрайон | Sub-district |
| Подател | Sender |
| ГДПБЗН | Fire safety / civil protection directorate |

---

## When To Stop And Ask

- The user requests a change that contradicts a hard constraint above.
- The user requests a change to the canonical/runtime dataset.
- A planned change would push the build past the 5 MB hard cap.
- You are about to introduce a runtime or build-time dependency.
- You are about to change Bulgarian UI text.
- You are about to `git push`, deploy the Worker, or publish — these are Petar's alone; agents never run them.
- A field report or any dataset carries personal data (PII): reject by default and scrub before persisting or creating an issue.
- You discover unexpected state — unfamiliar branches, uncommitted changes, or files you did not create: investigate before deleting or overwriting; it may be Petar's in-progress work.
- A task would touch the `Varna_buildings` checkout or any repo outside `C:\git\Fire_Varna`.
- You do not have an approved plan and the task is non-trivial.

When in doubt, ask. Petar would rather review a question than revert a commit.

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
   `*.db`, `*.csv`, binaries), and never read `node_modules/`, `.git/`,
   or build output. A log check is `tail -n 50`, once.
4. **One question per command.** If a capped result is insufficient,
   refine ONCE with a narrower query — never re-run with broader flags
   or raised caps. Still insufficient → state what is missing in your
   answer instead of searching further.
5. **Prefer what is already in context** over re-reading the same file.
6. **Escape hatch:** if the task explicitly names a file or module for
   exhaustive review, sequential ranged reads of the whole target are
   allowed.
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
45:("produce `output/address_index.json` for Fire_Varna") was correct as of
51:- Fire_Varna UI, hydrant data, mobile app code (separate concern; Phase 2
53:  built in the Fire_Varna repo — not part of unrelated architecture work)
168:- Use: parent-parcel context for `cadnum` prefix; quarter and locality
195:  D2 / 030); or квартал (no quarter column; the ГРАО ЕКАТТЕ classifier is
238:augmenting a mapping dataset; Fire_Varna is one). Its imagery /
447:**Per-attribute authority.** Per ADR 010 D2, each attribute domain has
494:  never in a determinism artifact; terrain-eyes may only
623:| Cluster identity churn breaking app state | High | Medium | ADR 018 D6 deterministic cluster ids; ADR 019 D6 collision detection |
627:| Fire_Varna integration bypasses the curated bundle / publish gate | Low | Medium | Mitigated by ADR 020 Amendment 2 (Accepted 2026-06-21): reintegration runs under a curated public bundle + publish gate |
664:described a single deliverable (`address_index.json` for Fire_Varna)

 succeeded in 571ms:
# МЯРКА · адресите на Fire_Varna срещу подписаните квартални полигони (08.09.2026, read-only)

Изтор: `data/search_index.json` (86 232 записа с координата: 70 575 адреса, 14 687 сгради, 970 парцела) срещу `varna_3d data/quarters_signed.geojson` (60 подписани полигона, 05f485e), „най-малкият съдържащ полигон“. Кварталната дума на адреса (`qtk`) идва от кадастралния адрес; полигонът — от подписа на Петър. Съгласие = дума на адреса ∈ токените на името/кода на полигона.

## 1 · Обща таблица

| клас | вътре в полигон, съгласни | вътре, несъгласни | вътре, без квартална дума | извън всички полигони |
|---|---|---|---|---|
| address | 2419 | 4977 | 53191 | 9988 |
| mf | 4206 | 3392 | 4024 | 3065 |
| parcel | 30 | 15 | 713 | 212 |
| **всички** | **6655** | **8384** | **57928** | **13265** |

## 2 · Несъгласия (кадастрална дума → подписан полигон под точката), топ 25

| брой | дума на адреса | полигон |
|---|---|---|
| 1951 | vinitsa | с.о. Манастирски рид |
| 1380 | vinitsa | м-т Акчелар |
| 563 | kolhozen pazar | кв. Тракия |
| 487 | vinitsa | м-т Ален Мак |
| 452 | tsveten kvartal | кв. Левски |
| 437 | mikroraion | Гръцката махала |
| 326 | vinitsa | ж.к. Бриз |
| 277 | gratskata mahala | Център |
| 269 | mikroraion | Център |
| 234 | chaika | кв. Левски |
| 214 | rozova dolina | кв. Аспарухово |
| 208 | vinitsa | м-т Свети Никола |
| 188 | vinitsa | с.о. Перчемлията |
| 186 | vinitsa | Евксиноград |
| 161 | vinitsa | м-т Сотира |
| 111 | druzhba | кв. Аспарухово |
| 100 | vinitsa | к.к. Св. Св. Константин и Елена |
| 78 | hristo botev | кв. Св. Иван Рилски |
| 54 | sveti nikola | ж.к. Бриз |
| 51 | ti mikroraion | Център |
| 50 | vinitsa | с.о. Горна Трака |
| 36 | hristo botev | Колхозен пазар |
| 31 | vazrazhdane | с.о. Пчелина |
| 30 | tsentar | Колхозен пазар |
| 29 | ribarsko selishte karantinata | кв. Аспарухово |

## 3 · Извън всички полигони, по кадастрална дума (центроид на групата)

| брой | дума | центроид |
|---|---|---|
| 8810 | (без дума) | 43.2021,27.9040 |
| 1461 | vinitsa | 43.2542,28.0062 |
| 753 | tsentar | 43.2066,27.9105 |
| 490 | kolhozen pazar | 43.2138,27.9059 |
| 478 | levski | 43.2165,27.9208 |
| 410 | gratskata mahala | 43.2109,27.9229 |
| 219 | chaika | 43.2127,27.9281 |
| 197 | tsveten kvartal | 43.2174,27.9133 |
| 143 | ti mikroraion | 43.2090,27.9114 |
| 89 | hristo botev | 43.2077,27.8979 |
| 54 | pobeda | 43.2197,27.9024 |
| 52 | evksinograd | 43.2373,27.9925 |
| 35 | sotira | 43.2274,27.9325 |
| 23 | alen mak priblizitelno | 43.2717,28.0301 |
| 22 | troshevo | 43.2193,27.8778 |
| 6 | mladost | 43.2306,27.8656 |
| 5 | galata | 43.1627,27.9363 |
| 3 | kochmar | 43.2416,27.8801 |
| 3 | dalbokoto dere | 43.2387,27.9854 |
| 3 | zelenika | 43.1606,27.9255 |

## 4 · Колко записа би получил всеки подписан квартал по полигон (топ 25)

| записи | полигон |
|---|---|
| 4545 | кв. Аспарухово |
| 3571 | кв. Христо Ботев |
| 3351 | кв. Виница |
| 3302 | кв. Св. Иван Рилски |
| 3282 | кв. Левски |
| 2890 | кв. Изгрев |
| 2821 | Евксиноград |
| 2680 | с.о. Боровец-юг |
| 2321 | кв. Трошево |
| 2305 | м-т Ален Мак |
| 2282 | кв. Владиславово |
| 1994 | с.о. Манастирски рид |
| 1961 | с.о. Боровец-север |
| 1776 | кв. Галата |
| 1668 | Център |
| 1642 | Западна промишлена зона |
| 1626 | м-т Свети Никола |
| 1537 | ж.к. Бриз |
| 1516 | к.к. Чайка |
| 1441 | м-т Акчелар |
| 1342 | Колхозен пазар |
| 1302 | кв. Тракия |
| 1263 | Максуда |
| 1208 | м-т Сотира |
| 1195 | Гръцката махала |

## 5 · Прочит
- Несъгласията са предимно СИСТЕМНИ: кадастралната „зона Виница“ е землищна дума върху много подписани квартали; „Колхозен пазар“ покрива Тракия; „микрорайон N“ е адресна форма без квартал; „Цветен квартал“ и „Център“ нямат подписан полигон.
- Поправката „координатата решава, кадастралната дума е свидетел“ е приложима на генератора на индекса (`js/build_fire_varna_search_index.mjs`), не в клиента: полигоните остават частни, публично пътува само думата. Дупките (Център, Цветен квартал, Колхозен пазар, Кайсиева/Възраждане 3 ръбове) искат решения преди това.
- Нищо от това не е в обхвата на Б3 (§10) — отделен лот.

## 6 · Повтарящи се номера на блокове (мярка 08.09 ~01:00, по искане на Петър)
- Записи с блоков номер („бл. N“) в индекса: **5 274**, което е около **1 407 физически блока** (входовете, събрани на 60 m).
- **(А)** Един и същ номер за повече от един физически блок в СЪЩАТА кадастрална квартална дума: **263 двойки (дума, номер), 939 блока**. Най-тежко: без квартална дума бл. 2 → 22 блока, бл. 1 → 18; кв. Левски бл. 2 → 17, бл. 1 → 12, бл. 3 → 11, бл. 4 → 11 (Левски номерира блоковете по улица, затова номерата се повтарят).
- **(Б)** Номер, който съществува в повече от един квартал: **108 от 332** номера (бл. 2 в 28 квартала, бл. 1 в 25, бл. 3 в 22…).
- **(В)** По подписан полигон: **250 двойки, 824 блока** с повторен номер в същия полигон; извън полигоните: бл. 1 → 27, бл. 2 → 23.
- **Ориентирът:** от 4 403 етикета в блоков стил („кв. X, бл. N…“) само **244** носят улица след номера; **4 159 са без улица** — и за **всичките 4 159** има улична адресна точка до 80 m (4 143 до 50 m). Тоест „кв. Левски, бл. 11, до ул. Студентска“ е изводимо за 100 % от блоковете без нови източници.
- **Заявка на Петър (08.09):** „искам да сложим и близка улица, за да се различават блоковете… искам да го изчистим този проблем веднъж завинаги“ — влиза като изискване 2 на лота „Адресите по полигон“ (планът се пише); по тази тема сега не се действа.

## 7 · ПОПРАВКА на извора (08.09 ~02:10): думата „Чайка“ за Студентска бл. 11 НЕ е от кадастъра
- Кадастралният адресен ред на блока е само „Студентска бл. 11“ — без квартал. Кварталната дума идва от частния мост `Varna_buildings/app/modules/search/data/search_bridge.json` (`cluster_summaries`, 60 614 клъстера): за клъстера на Студентска бл. 11 `quarter = {name: "кв. Чайка", source: "osm", mode: "nearest_point", confidence: "low", distance_m: 707.5, margin_ratio: 1.43, second_choice: "м-т Сотира"}` — тоест **най-близкият OSM place-възел „кв. Чайка“ на 707 m**, евристика от по-стар лот. Истинският кв. Чайка бл. 11 (43.2149, 27.9334; входове А–Г) е присвоен по същия механизъм (osm nearest_point, 526 m, medium) и там случайно е верен → **два различни блока с еднакъв етикет „кв. Чайка, бл. 11“** (недопустимо, думите на Петър).
- Мащаб на механизма: `quarter.source` osm **35 054** / kais **25 550** от 60 614 клъстера; `mode` nearest_point **33 188** (54,8 %), polygon_cover 1 866, KAIS без mode 25 550. Следствие за лота: „координатата решава“ заменя точно тази евристика; „най-близък възел/полигон“ е забранен като извор (Astra S31/S33), OSM думата остава свидетел с `source`/`distance_m` в частния леджер.

## 8 · ДЪЛБОЧИНАТА: всичките 60 614 клъстера сгради (частният мост на Varna_buildings) срещу подписаните полигони (08.09 ~02:30)
Кварталната дума на всеки клъстер (и оттам на всеки адрес/блок в индекса) идва от `quarter.{source, mode, confidence}` в `app/modules/search/data/search_bridge.json`. Съгласие = дума ∩ токени на полигона под пина; „в лентата“ = пинът е на по-малко от max(50, precision_m) от ръба.

| извор | режим | увереност | общо | съгласни | съгл. в лентата | несъгласни | несъгл. в лентата | извън полигон | припокриване | без дума |
|---|---|---|---|---|---|---|---|---|---|---|
| kais | - | kais | 25550 | 7070 | 6094 | 4449 | 3765 | 3710 | 462 | 0 |
| osm | nearest_point | high | 12535 | 6265 | 2947 | 859 | 1095 | 527 | 842 | 0 |
| osm | nearest_point | low | 10799 | 1776 | 2244 | 1221 | 1402 | 3649 | 507 | 0 |
| osm | nearest_point | medium | 8435 | 2728 | 2421 | 834 | 1278 | 754 | 420 | 0 |
| osm | polygon_cover | high | 1876 | 89 | 139 | 761 | 363 | 268 | 246 | 10 |
| osm | nearest_point | flagged | 1419 | 64 | 160 | 434 | 408 | 347 | 6 | 0 |
| **всички** | | | **60614** | **17992** | **14005** | **8558** | **8311** | **9255** | **2483** | **10** |

Прочит: съгласни общо 31 997 (53 %), несъгласни 16 869 (28 %), извън полигон 9 255 (15 %), припокриване 2 483 (4 %). Несъгласието НЕ е само при OSM: и кадастралните думи (KAIS 25 550) са несъгласни в 8 214 случая, защото кадастралната „зона“ (ГАЛАТА, ВИНИЦА, Траката, 8 микрорайон) е землищно/административно име, не квартал. OSM nearest_point с ниска увереност е най-лошият клас (3 649 извън полигон, 2 623 несъгласни от 10 799); OSM polygon_cover (1 876) е несъгласен в 1 124 — OSM полигоните не съвпадат с подписаните.

Топ несъгласия вътре в полигон (дума на моста → подписан полигон): кв. "ГАЛАТА" → с.о. Боровец-юг (1293); кв. Розова долина → кв. Аспарухово (771); с.о."Траката" → Евксиноград (649); ж.к. БРИЗ → м-т Свети Никола (560); 8 микрорайон → Център (466); Цветен квартал → кв. Левски (458); Колхозен пазар → кв. Тракия (291); кв. ВИНИЦА → с.о. Манастирски рид (238); кв. ВИНИЦА → м-т Акчелар (224); 8 микрорайон → Гръцката махала (209); м. ТРАКАТА → Средна Трака (195); Максуда → кв. Св. Иван Рилски (181); ж.к. "ВЛАДИСЛАВ ВАРНЕНЧИК" → кв. Владиславово (162); ж.к. Св. Иван Рилски → Западна промишлена зона (153); Гръцката махала → Център (152).
Част от тях може да са и въпрос към ПОЛИГОНА (напр. „кв. ГАЛАТА“ → с.о. Боровец-юг 1 293; ж.к. БРИЗ → м-т Свети Никола 560): борд, не автоматика.


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $lines=Get-Content -Encoding utf8 docs/architecture_v2.md; for($i=439;$i -le 499;$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }; $lines=Get-Content -Encoding utf8 tools/build_quarter_trust_sidecar.py; for($i=127;$i -le 180;$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }; Get-Item app/modules/search/data/search_bridge.json, C:/git/Fire_Varna/scratch/places_search/adresi_bridge_depth_08.09.json, C:/git/varna_3d/data/quarters_signed.geojson | Select-Object FullName,Length,LastWriteTime' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding utf8 js/build_fire_varna_search_index.mjs; foreach ($span in @(@(512,545),@(850,898),@(1015,1042))) { for ($i=$span[0];$i -le $span[1];$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] } }; rg -n "buildBlockLabelIndex|quarter_assignment_trust|quarter|qtk" js/lib_fire_varna_consolidation.mjs js/lib_quarter_registry.mjs | Select-Object -First 85' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; Get-Content -Encoding utf8 C:/git/Fire_Varna/docs/activeContext.md -TotalCount 90; rg -n --max-count 20 --max-columns 220 "quarter|places|адрес|Адрес|границ" C:/git/Fire_Varna/docs/activeContext.md; rg --files C:/git/Fire_Varna/scratch/places_search | rg "S3[135]|adresi|adres|poligon|08.09"' in C:\git\Varna_buildings
 succeeded in 1307ms:
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
3:[Omitted long matching line]
16:[Omitted long matching line]
18:[Omitted long matching line]
24:[Omitted long matching line]
25:4. `scratch/places_search/m7_trigger_tokens.json` — **33 triggering words**, waiting for a signature.
26:[Omitted long matching line]
27:[Omitted long matching line]
45:| `data/places.json` (150 rows × 13 keys; 121621 B before F12) | 122089 B · sha `329310f577e8…` | `wc -c < data/places.json` · `git show HEAD:data/places.json \| sha256sum` |
47:[Omitted long matching line]
49:[Omitted long matching line]
50:[Omitted long matching line]
51:[Omitted long matching line]
54:[Omitted long matching line]
55:[Omitted long matching line]
93:code for `scratch/places_search/expectations.json`; the suite compares the engine
99:The six that remain are one claim in six places: **the frozen reference is still
130:[Omitted long matching line]
132:Doctrine shared with Varna_buildings: ADR 004 → Varna_buildings ADR 058. varna_3d generates the places delivery and consumes the hydrants for its 3D map.
C:/git/Fire_Varna/scratch/places_search\adresi_po_poligon_measure_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_po_poligon_measure_08.09.json
C:/git/Fire_Varna/scratch/places_search\adresi_kimi_K33_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_kimi_K32_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_bridge_depth_08.09.json
C:/git/Fire_Varna/scratch/places_search\adresi_astra_S35_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_astra_S34_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_astra_S33_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_astra_S32_08.09.md
C:/git/Fire_Varna/scratch/places_search\adresi_astra_S31_08.09.md

 succeeded in 1350ms:
512:// Load search_bridge once → { clusterLabelByCad: Map<cadnum, label>, cadnumToCluster:
513:// Map<cadnum, cluster_id>, clusterInfoByCluster: Map<cluster_id, {quarter, addrLine}> }.
514:// Reads the 29 MB bridge in a scoped helper so the parsed object is freed before pass 2.
515:// clusterLabelByCad feeds the S9 token-inconsistent label override; cadnumToCluster feeds
516:// the Phase-2 per-cluster `g` for non-block MF; clusterInfoByCluster feeds the C2
517:// consolidated block label (modal quarter.name + street-disambiguation address_line).
518:function loadBridgeMaps(path) {
519:  const bridge = JSON.parse(readFileSync(path, "utf8"));
520:  const c2c = bridge.cadnum_to_cluster_id || {};
521:  const cs = bridge.cluster_summaries || {};
522:  const clusterLabelByCad = new Map();
523:  const cadnumToCluster = new Map();
524:  for (const cad in c2c) {
525:    const cid = c2c[cad];
526:    if (cid != null) cadnumToCluster.set(cad, cid);
527:    const summary = cid != null ? cs[cid] : null;
528:    if (!summary) continue;
529:    const label = summary.label || summary.address_line || null;
530:    if (label) clusterLabelByCad.set(cad, label);
531:  }
532:  const clusterInfoByCluster = new Map();
533:  for (const cid in cs) {
534:    const s = cs[cid];
535:    if (!s) continue;
536:    const quarter = s.quarter && typeof s.quarter.name === "string" ? s.quarter.name : null;
537:    const addrLine = typeof s.address_line === "string" ? s.address_line : null;
538:    if (quarter || addrLine) clusterInfoByCluster.set(cid, { quarter, addrLine });
539:  }
540:  return { clusterLabelByCad, cadnumToCluster, clusterInfoByCluster };
541:}
542:
543:// ---------------------------------------------------------------------------
544:// Build.
545:// ---------------------------------------------------------------------------
850:    }
851:    // (C2) THE registry pass — the single point EVERY label goes through, block or
852:    // not. v1.0 wiring only reached block rows, so the 320 "ж.к. Св. Иван Рилски"
853:    // rows kept an uncanonical display despite a signed alias, and non-block rows
854:    // were not even counted. The pin's LONGITUDE is passed too: without it the
855:    // key+bbox holdouts (П1/П2) cannot be evaluated and the loader has to hold the
856:    // whole key.
857:    const qrLat = Array.isArray(o.pin) ? o.pin[0] : null;
858:    const qrLon = Array.isArray(o.pin) ? o.pin[1] : null;
859:    let qrCls = o.label ? null : "no_label";
860:    if (o.label) {
861:      const qr = applyQuarterRegistryToLabel(QREG, o.label, qrLat, qrLon, qregStats);
862:      qrCls = qr.cls;
863:      qregStats.byClass[qr.cls] = (qregStats.byClass[qr.cls] || 0) + 1;
864:      if (qr.matched && qr.label !== o.label) {
865:        qregStats.relabeled += 1;
866:        qregStats.byEntry.set(qr.entryId, (qregStats.byEntry.get(qr.entryId) || 0) + 1);
867:        o.label = qr.label;
868:      }
869:    } else {
870:      qregStats.byClass.no_label = (qregStats.byClass.no_label || 0) + 1;
871:    }
872:
873:    // Р38 (signed) — the кв. Виница zone.
874:    if (VINITSA_ZONE && inZone(VINITSA_ZONE, o.pin)) {
875:      z38.inZone += 1;
876:      const qtkNow = Array.isArray(o.qtk) ? o.qtk : [];
877:      const isDalbokoto = qtkNow.length === DALBOKOTO_QTK.length
878:        && qtkNow.every((t, k) => t === DALBOKOTO_QTK[k]);
879:      // Evidence = a quarter the row already carries, in tokens or in its display.
880:      const hasQuarterEvidence = qtkNow.length > 0
881:        || (o.label != null && qrCls !== "no_quarter_segment");
882:      if (isDalbokoto) {
883:        // The measured-wrong quarter inside the zone: the DISPLAY is corrected, and
884:        // the token set is AUGMENTED — never pruned. Replacing qtk deleted
885:        // "дълбокото"/"дере" from 48 rows and dropped the query from 51 hits to 3;
886:        // an old spelling staying searchable is the standing rule of this registry
887:        // (policy.unmatched = keep_and_report, tokens keep every historical form).
888:        o.qtk = [...qtkNow, VINITSA_TOKEN];
889:        z38.correctedDalbokoto += 1;
890:        if (o.label) {
891:          const segs = String(o.label).split(",").map((t) => t.trim());
892:          if (segs.length > 1 && /дълбокото\s+дере/i.test(segs[0])) {
893:            o.label = [VINITSA_DISPLAY, ...segs.slice(1)].join(", ");
894:            z38.correctedDisplay += 1;
895:          } else {
896:            o.label = `${VINITSA_DISPLAY}, ${o.label}`;
897:            z38.prefixedLabel += 1;
898:          }
1015:  if (!Array.isArray(addrRows)) throw new Error("address_index.json must be a JSON array");
1016:
1017:  // Build-time-only bridge maps (the big parsed bridge is freed inside the helper):
1018:  // clusterLabelByCad for the S9 override, cadnumToCluster for the Phase-2 per-cluster g,
1019:  // clusterInfoByCluster (quarter.name + address_line) for the C2 consolidated block label.
1020:  const { clusterLabelByCad, cadnumToCluster, clusterInfoByCluster } = loadBridgeMaps(BRIDGE_PATH);
1021:
1022:  // Block-parcel bridge: detect split blocks over section_units and resolve every
1023:  // block complex_id to its canonical id BEFORE keying (scoped helper so the parsed
1024:  // 17 MB section list is freed before the entry pass).
1025:  const bridge = (() => buildBlockParcelBridgeContext(
1026:    JSON.parse(readFileSync(SECTION_UNITS_PATH, "utf8"))))();
1027:  const { gForEntry, stats: keyStats } = makeEntryKeyer({
1028:    cadnumToCluster, salt, canonicalComplexId: bridge.canonicalComplexId,
1029:  });
1030:
1031:  // (C2) Per-complex_id consolidated block label index (modal quarter.name + street
1032:  // disambiguation on post-consolidation collisions). Keyed by the SAME complex_id that
1033:  // C1 keys `g` by, so a block's safe label and its detail `g` describe one group.
1034:  const { labelByComplex, stats: blockLabelStats } = buildBlockLabelIndex({
1035:    entries: geocoder.entries, cadnumToCluster, clusterInfoByCluster,
1036:  });
1037:
1038:  const { index, stats } = buildPublicIndex(geocoder, addrRows, clusterLabelByCad, gForEntry, labelByComplex);
1039:
1040:  // Override drift gate: the token-inconsistent set must stay near the measured S9
1041:  // baseline. A large drift means the source data or the token fold moved — fail-closed.
1042:  const drift = (stats.tokenInconsistentTotal - S9_BASELINE) / S9_BASELINE;
js/lib_quarter_registry.mjs:1:// lib_quarter_registry.mjs — каноничните квартални имена (ПОДПИСАН регистър).
js/lib_quarter_registry.mjs:4:// scratch/quarter_registry_draft.md от 02.07). Този loader НЕ решава имена — той
js/lib_quarter_registry.mjs:23:const REGISTRY_PATH = resolve(__dirname, "..", "config", "quarter_registry.json");
js/lib_quarter_registry.mjs:80:      `block|${normQuarterKey(o.quarter)}|${String(o.block).toLowerCase()}|${o.display}`,
js/lib_quarter_registry.mjs:116:        `quarter_registry: schema_version "${reg.schema_version}" != locked ` +
js/lib_quarter_registry.mjs:123:        `quarter_registry: signed-content sha256 ${sha} != locked ` +
js/lib_quarter_registry.mjs:135:        throw new Error(`quarter_registry: alias "${a}" сочи към два записа ` +
js/lib_quarter_registry.mjs:143:    blockOverrides.set(`${normQuarterKey(o.quarter)}|${String(o.block).toLowerCase()}`,
js/lib_quarter_registry.mjs:175:  // vocab/scoring only from tk/qtk/alias_tk/dtk/stk, so a parent token would fall
js/lib_quarter_registry.mjs:210:// Quarter TYPE markers that make a leading label segment a quarter rather than a
js/lib_quarter_registry.mjs:212:// к.к./кв. Чайка lesson); this only decides whether a segment is a quarter AT ALL.
js/lib_quarter_registry.mjs:216:// Does this leading segment look like a quarter segment? Either it carries a type
js/lib_quarter_registry.mjs:231:// C2 — the registry over EVERY quarter-prefixed row, not just the block ones.
js/lib_quarter_registry.mjs:239://   * a label WITHOUT one has its FIRST segment treated as the quarter candidate, and
js/lib_quarter_registry.mjs:240://     only if that segment actually looks like a quarter;
js/lib_quarter_registry.mjs:241://   * everything else is CLASSIFIED and counted — `no_quarter_segment` is a real
js/lib_quarter_registry.mjs:252:             cls: "no_quarter_segment" };
js/lib_quarter_registry.mjs:256:  // presenting the quarter segment in the shape it already understands, then putting
js/lib_quarter_registry.mjs:267:  // ("Найден Геров 49А,49Б,49В" -> "49А, 49Б, 49В") — a mutation outside the quarter
js/lib_quarter_registry.mjs:362:    // ALIAS-AWARE consumption. The raw quarter can span several segments, and the
js/lib_quarter_registry.mjs:366:    // quarter, not two). Anything BEYOND the key survives, which is what keeps a

 succeeded in 1413ms:
439:outside measured Varna bounds (lng 27.83–28.05, lat 43.10–43.31) stops
440:the pipeline.
441:
442:**Cadnum is canonical.** Per ADR 010 D1, the 4-segment KAIS section
443:identity is the canonical building identity. The 3-segment prefix is a
444:*parcel* identifier. "Physical building" is a derived query, not a
445:schema entity (ADR 010 D3).
446:
447:**Per-attribute authority.** Per ADR 010 D2, each attribute domain has
448:one authoritative source; the other is corroborating signal. KAIS owns
449:cadastral identity, legal counts, regulatory provenance. OSM owns the
450:navigable **display label** (ADR 014 D2), physical footprint, and
451:building metadata. KAIS `strename` labels are noisy (ADR 009) and
452:require street-distance cross-validation (ADR 014). Per ADR 025, **Microsoft ML is the
453:secondary footprint source for buildings OSM lacks**; per ADR 026,
454:**KAIS geometry is rendered only as a gated low-confidence fallback**
455:for real buildings no OSM/ML source covers (never stacked, road-guarded,
456:overlap-clipped) — otherwise KAIS **geometry is not rendered** (KAIS
457:remains authority for cadastral identity, legal counts, regulatory
458:provenance, building age). The KAIS↔geometry attribute join carries a
459:**`data_confidence` flag** (~70% high, ~30% fuzzy, plus a new **`low`**
460:band for KAIS-fallback geometry per ADR 026); fuzzy- and low-confidence
461:attachments are presented as uncertain.
462:
463:**Source authority by question (ADR 058).** This is the single home of
464:the per-source authority allocation; AGENTS.md § Measurement Doctrine and
465:ADR 058 point here and do not copy it.
466:
467:- **Address existence + official street / number / entrance → ГРАО** (the
468:  address register; 1,943 streets + 41,949 addresses, **zero
469:  coordinates** — each address's position is derived downstream, KAIS
470:  footprint/centroid → gated m6000 anchor → street interpolation; ГРАО
471:  never carries a coordinate). ГРАО address-count ≠ KAIS `appcount` and
472:  never overwrites it (ADR 010 D2 / 030).
473:- **Navigable display label → OSM** (the ADR 014 D2 cascade — the default
474:  where the street name is undisputed).
475:- **Street NAME on a dispute (which street a segment IS) → ГРАО register
476:  + m6000 arbiter.** The stored name is ГРАО's; the m6000 municipal-map
477:  arbiter adjudicates an OSM-vs-official dispute segment-by-segment and,
478:  where it finds against OSM, **ГРАО + m6000 override OSM** (OSM flagged
479:  as the error) — but it may equally confirm OSM (post-12.2020 renames
480:  are legitimate, not errors). Scoped to NAMES, not geometry (ADR 058 D4;
481:  formalizes FF-001 / M3b-names, which previously ran with no ADR against
482:  ADR 010 D2 / ADR 056).
483:- **Building identity → KAIS `cadnum`; apartment count → KAIS `appcount`
484:  (building) / SOIS (entrance); floors, category, regulatory provenance →
485:  KAIS.**
486:- **Footprint → OSM → Microsoft ML → gated-low KAIS** (ADR 025/026,
487:  unchanged); the KAIS centroid supplies the anchor/pin. KAIS identity +
488:  centroid + attributes is **not** a footprint reversal.
489:- **район → KAIS `regname`; квартал / ж.к. → KAIS `quarname` first, OSM
490:  polygon/point gap-fill, SOIS `stk` additive** (ADR 015/043/044/052; OSM
491:  admin boundaries stay audit-only).
492:- **m6000** (municipal map) and **Google Street View terrain-eyes** are
493:  private **aids** — never ingested, never a canonical stored coordinate,
494:  never in a determinism artifact; terrain-eyes may only
495:  refute/downgrade/trigger (ADR 058 D3/D5). Register-vs-register
496:  conflicts are documented + quarantined, not silently merged; **Petar is
497:  the final per-item tiebreak.**
498:
499:**Address authority cascade.** ADR 014 establishes priority:
127:    to_utm = Transformer.from_crs(
128:        "EPSG:4326", "EPSG:32635", always_xy=True
129:    ).transform
130:
131:    pts = []  # (x, y, cid, kvnorm, is_supp, is_conf)
132:    trust = {}  # cid -> trusted | candidate | conflicted | flagged | other
133:    flagged_ids = []
134:    for cid in sorted(cluster_details):
135:        d = cluster_details[cid]
136:        q = d.get("quarter") if isinstance(d, dict) else None
137:        adapted = normalize_quarter(q)
138:        if adapted is None:
139:            continue  # no quarter assignment — not in the trust map
140:        family, band = adapted
141:        if family == "nearest_point" and band == "flagged":
142:            trust[cid] = "flagged"
143:            flagged_ids.append(cid)
144:        elif _confident(family, band):
145:            trust[cid] = "trusted"
146:        elif _suppressible(family, band):
147:            trust[cid] = "candidate"  # refined below to unverified/conflicted
148:        else:
149:            trust[cid] = "other"
150:        c = d.get("center")  # [lat, lng] WGS84 (cluster_details convention)
151:        kvn = kvnorm(q.get("name"))
152:        if not (c and len(c) == 2 and kvn):
153:            continue
154:        x, y = to_utm(c[1], c[0])  # WGS84 lng,lat -> UTM 35N metres
155:        pts.append((x, y, cid, kvn, _suppressible(family, band),
156:                    _confident(family, band)))
157:
158:    geoms = [Point(x, y) for (x, y, *_) in pts]
159:    tree = STRtree(geoms)
160:    conflicted = set()
161:    supp_total = sum(1 for p in pts if p[4])
162:    for i, (x, y, cid, kvn, is_supp, _) in enumerate(pts):
163:        if not is_supp:
164:            continue
165:        for j in tree.query(geoms[i].buffer(RADIUS_M)):
166:            j = int(j)
167:            if j == i:
168:                continue
169:            xx, yy, cid2, kvn2, _supp2, conf2 = pts[j]
170:            if conf2 and kvn2 != kvn and geoms[i].distance(geoms[j]) <= RADIUS_M:
171:                conflicted.add(cid)
172:                break
173:
174:    for cid in conflicted:
175:        trust[cid] = "conflicted"
176:    for cid, t in trust.items():
177:        if t == "candidate":
178:            trust[cid] = "unverified"
179:
180:    conflicted_sorted = sorted(conflicted)

FullName                                                                 Length LastWriteTime       
--------                                                                 ------ -------------       
C:\git\Varna_buildings\app\modules\search\data\search_bridge.json      29486420 8/13/2026 4:40:04 AM
C:\git\Fire_Varna\scratch\places_search\adresi_bridge_depth_08.09.json     4391 9/8/2026 1:44:02 AM 
C:\git\varna_3d\data\quarters_signed.geojson                             301917 9/7/2026 12:18:52 AM



codex
Намерих две системни причини: архитектурата още дава предимство на KAIS `quarname`, а генераторът за Fire_Varna взема `quarter.name` за блоковия етикет, без неговата увереност. Има и уточнение в мярката: освен четирите големи групи има 10 клъстера без квартална дума; 8 311 от несъгласията са в граничната лента и не доказват сами по себе си грешен етикет.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; rg -n \"buildBlockLabelIndex|qtk\\s*=|qtk:\" js/build_fire_varna_search_index.mjs js/lib_fire_varna*.mjs; "'$lines=Get-Content -Encoding utf8 js/build_fire_varna_search_index.mjs; for($i=595;$i -le 635;$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }; Get-Content -Encoding utf8 C:/git/Fire_Varna/scratch/places_search/adresi_astra_S35_08.09.md -TotalCount 120' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; rg -l --max-count 20 --max-columns 200 "Студентска|nearest_point|двойк|сблъс" C:/git/Fire_Varna/scratch/places_search/adresi_astra_S3*_08.09.md; rg -n --max-count 20 --max-columns 200 "signed_quarter|quarters_signed|boundar|quarter" package.json; $lines=Get-Content -Encoding utf8 js/lib_quarter_registry.mjs; for($i=25;$i -le 52;$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }; rg -n --max-count 20 --max-columns 200 "Владислав|Розова|Цветен|Колхоз|Галата|Бриз" config/quarter_registry.json' in C:\git\Varna_buildings
 succeeded in 781ms:
rg: js/lib_fire_varna*.mjs: The filename, directory name, or volume label syntax is incorrect. (os error 123)
js/build_fire_varna_search_index.mjs:105:import { buildBlockLabelIndex, tidyDisplay } from "./lib_fire_varna_block_labels.mjs";
js/build_fire_varna_search_index.mjs:701:    const qtk = cleanTokenArray(e.qtk); if (qtk && qtk.length) o.qtk = qtk;
js/build_fire_varna_search_index.mjs:815:    // "<quarter>, бл. <N>[, <street>]" from the SAME buildBlockLabelIndex the C2
js/build_fire_varna_search_index.mjs:888:        o.qtk = [...qtkNow, VINITSA_TOKEN];
js/build_fire_varna_search_index.mjs:905:        o.qtk = [...qtkNow, VINITSA_TOKEN];
js/build_fire_varna_search_index.mjs:1034:  const { labelByComplex, stats: blockLabelStats } = buildBlockLabelIndex({
js/build_fire_varna_search_index.mjs:1122:  console.log(`  f3_block_relabeled       = ${stats.f3Relabeled} (block-tier rows whose label lacked a block marker, re-labeled from buildBlockLabelIndex)`);
595:    let candidate = null, reason;
596:    if (!clRaw) reason = "no_cluster";
597:    else if (!isDisplaySafe(clRaw)) reason = "cluster_unsafe";
598:    else if (clRaw === siteBase) reason = "cluster_eq_site";
599:    else if (s9Inconsistency(splitQuarter(clRaw).rest, e, tokenSet, btkSet).inconsistent) reason = "cluster_inconsistent";
600:    else { candidate = clRaw; reason = null; }
601:    return { inconsistent: true, rules: verdict.rules, candidate, reason, sp, siteBase, siteFull, clRaw };
602:  }
603:
604:  // (C2) Resolve the SAFE consolidated block label for a block-tier entry. Returns
605:  // { ok:true, label } when the group's chosen label (base, or street-disambiguated on a
606:  // post-consolidation collision) is display-safe AND token-CONSISTENT with THIS entry;
607:  // otherwise { ok:false, reason } (fail-closed → caller keeps the S9/addr_key fallback).
608:  // Non-block entries return null (C2 is block-tier only; non-block keeps S9 untouched).
609:  function resolveC2BlockLabel(e) {
610:    if (!isBlockComplex(e.complex_id)) return null;
611:    const info = blockLabels.get(e.complex_id);
612:    if (!info || !info.label) return { ok: false, reason: "no_group_label" };
613:    const lab = info.label;
614:    if (!isDisplaySafe(lab)) return { ok: false, reason: "unsafe" };
615:    const tokenSet = entryTokenSet(e);
616:    const btkSet = new Set(Array.isArray(e.btk) ? e.btk : []);
617:    if (s9Inconsistency(lab, e, tokenSet, btkSet).inconsistent) return { ok: false, reason: "token_inconsistent" };
618:    return { ok: true, label: lab, collided: info.collided };
619:  }
620:
621:  // Pass 1 — order-walk to assign display_id, asserting cadnum alignment.
622:  const displayId = new Array(E.length).fill(undefined);
623:  let rowIdx = 0;
624:  let lastSectionRow = -1;
625:  for (let i = 0; i < E.length; i++) {
626:    const e = E[i];
627:    if (e.kind === "parcel") continue; // parcels + OSM rows: no address_index row
628:    const isEntrance = e.kind === "mf" && e.en !== undefined;
629:    if (isEntrance) {
630:      if (lastSectionRow < 0) throw new Error(`entrance entry ${i} precedes any section`);
631:      displayId[i] = lastSectionRow;
632:      continue;
633:    }
634:    // Non-entrance address / mf-section -> the next address_index row, in order.
635:    const srcCad = addrCadnums[rowIdx];
Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git\Varna_buildings
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a07e0c-53cc-7153-a42c-b6c5864b0962
--------
user
S35 · ДИАГНОЗА и СИСТЕМНО РЕШЕНИЕ (леща: първопричина + архитектура на поправката), read-only. Въпросът на Петър дословно: „не искам да ги поправяме 1 по 1. искам да видим колко дълбок е проблема — и защо така се получава и как да го поправим. искам конкретни решения“. Фактите: (1) кварталната дума на всеки адрес/блок във Fire_Varna идва от app/modules/search/data/search_bridge.json (cluster_summaries, 60 614 клъстера; quarter.{name, source: kais|osm, mode: nearest_point|polygon_cover|-, confidence, distance_m, margin_ratio, second_choice_name}); Студентска бл. 11 носи „кв. Чайка“ от OSM nearest_point на 707 m (low) — а истинският кв. Чайка бл. 11 е друг блок със СЪЩИЯ етикет; (2) мярката срещу 60-те подписани полигона (C:/git/varna_3d 05f485e; таблицата по извор/режим/увереност: C:/git/Fire_Varna/scratch/places_search/adresi_bridge_depth_08.09.json и adresi_po_poligon_measure_08.09.md §8): съгласни 31 997 (53 %), несъгласни 16 869 (28 %), извън полигон 9 255, припокриване 2 483; kais 25 550: 8 214 несъгласни (кадастралната „зона“ ГАЛАТА/ВИНИЦА/Траката/8 микрорайон ≠ квартал); osm nearest_point low: 3 649 извън + 2 623 несъгласни от 10 799; osm polygon_cover 1 876: 1 124 несъгласни; топ несъгласия: кв. ГАЛАТА→с.о. Боровец-юг 1 293, Розова долина→Аспарухово 771, Траката→Евксиноград 649, ж.к. БРИЗ→м-т Свети Никола 560, 8 микрорайон→Център 466, Цветен квартал→кв. Левски 458, Колхозен пазар→кв. Тракия 291. Задачи: (А) ПЪРВОПРИЧИНА: намери в C:/git/Varna_buildings кой скрипт строи quarter в search_bridge.json (tools/, js/, src/; grep search_bridge, margin_ratio, polygon_cover), кой ADR/план го е въвел (docs/decisions/015_quarter_source_confidence_restructure.md, 039_kv_cleanup.md, 061_impossible_coordinates.md, docs/plans/plan_quarters_resorts_2026-09-02.md, docs/archive/plans/osm_quarter_integration_plan.md), какви са били изворите тогава (KAIS quarname = кадастрална зона; OSM place-възли; OSM квартални полигони) и защо се е стигнало до „най-близък възел“ с ленти на увереност; кога са се появили подписаните полигони (Fire_Varna docs/decisions/010_signed_quarter_boundaries.md, 06–07.09) и защо мостът още не ги ползва. Обясни го в 10 реда за човек без CS. (Б) КОЛКО ДЪЛБОКО: провери мярката (метод: токенно съгласие; лента max(50, precision_m); най-малък съдържащ полигон) и кажи кои несъгласия са ГРЕШКИ на думата, кои са РАЗЛИКА В СИСТЕМАТА ОТ ИМЕНА (зона ≠ квартал), кои са ВЪПРОС КЪМ ПОЛИГОНА (напр. Галата/Боровец-юг, Бриз/Свети Никола) — с числа. (В) СИСТЕМНО РЕШЕНИЕ: 2–3 конкретни варианта с цена и риск: напр. (1) мостът строи quarter от подписаните полигони за ВСИЧКИ клъстери (координатата решава), KAIS/OSM думите стават свидетели със source/distance; (2) поправка само в генератора на Fire_Varna; (3) хибрид/поетапно; какво става с 9 255 извън и 2 483 припокриване (решения на Петър: покритие на Център, Цветен квартал, Колхозен пазар; родства); как се пази „веднъж завинаги“ — гейт, който забранява nearest_point като извор и мери съгласието при всеки билд; какво подписва Петър. Препоръчай един вариант. Не пипай нищо, нищо към отдалечено хранилище. До 900 думи, с path:line и числа.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проследя откъде идва `quarter`, ще проверя мярката и ще сравня вариантите за обща поправка. Работя само за четене, без промени и без действия към отдалечени хранилища.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content docs/activeContext.md -TotalCount 240' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content docs/architecture_v2.md' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/debug/SKILL.md; Get-Content C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/architecture/SKILL.md' in C:\git\Varna_buildings
 succeeded in 303ms:
# Active context â€” Varna_buildings

**Date:** 2026-09-02 Â· **last verified against commit** 4ed99cf (`main`; ahead of `origin/main` by the 2026-09-01 plan's commits until Petar's push â€” see the table; last content commit 69d146a, 2026-08-15) Â· verified by: Opus (executor), audited by: <auditor> Â· signed: __
> Every number here is the output of the command next to it, run on the date above (`verify_numbers.py` checks it).
> The chronicle up to 2026-08-15 (line count in the table) is frozen in [archive/activeContext_2026-08-15.md](archive/activeContext_2026-08-15.md); the open-questions log stays in [unknowns.md](unknowns.md) (frozen header, 2026-08-15).

## What this repo is
Private pipeline: KAIS cadastre (Ð¡Ð³Ñ€Ð°Ð´Ð¸ / Ð˜Ð¼Ð¾Ñ‚Ð¸ / Ð¡ÐžÐ˜Ð¡) + OSM + ML footprints â†’ the static building map (`app/`), the search indexes and the intel artifacts. **It is the data authority for Fire_Varna (search payloads) and varna_3d (section units, address provenance).** No content commit since 69d146a (2026-08-15; the commits after it are the 2026-09-01 plan's â€” see the table) is a quiet stretch, not an archive: both consumers read its outputs.

## Trunk
`main`; `origin/main` is behind it by the plan's commits (table row) until Petar pushes.

## Current phase
- **ADR 063 (entrance reattribution)** â€” Accepted 2026-08-15; payload rebuilt into Fire_Varna and **committed there on 2026-08-31 as c0db844** (numbers in the table). The frozen chronicle's R14 line ("MODIFIED in Fire_Varna, uncommitted") is superseded by that commit.
- **ADR 061 (impossible coordinates)** â€” Accepted 2026-07-29; its code (`tools/data_quality/impossible_coords.py`, `build_impossible_register.py`, `impossible_coords_register.json`, `tests/test_impossible_coords.py`) entered git with LOT 1 of the 2026-09-01 plan (`git log --diff-filter=A -1 --format=%h -- tests/test_impossible_coords.py`); only the change in `tools/build_number_pins.py` is still in the working tree, not in git (row "modified tracked files" below) â€” Ð’-3 of the plan: a clean clone fails that test until it is committed.
- Open questions: `unknowns.md` Â§ ADR 063 (Q1 â€” the invisible phantoms; its count is the document's, not re-verified on 2026-09-02).

## Open
- New open questions since the freeze go here (the log up to 2026-08-15 is frozen in [unknowns.md](unknowns.md)); none recorded yet besides the plan's own Ð’-3/Ð’-4/Ð’-8.
- Resorts as quarters in the Fire_Varna search index â€” docs/plans/plan_quarters_resorts_2026-09-02.md (measure Ã—2, Kimi verdict; NOT executed): Petar decides Ð’-1 buffer (0 m), Ð’-2 Ðš&Ð• geometry âˆ§ self-evidence, Ð’-3 no display prefix, Ð’-4 13 parcels into the registry alias list (new SHA256) â€” then Sol on the projection, then the lot.

## Waiting for signature
- Ð’-3 (ADR 061 code) Â· Ð’-4 (`tools/*quarter*.py`, `build_number_layer.py` â€” active tools or archive).

## Last report
- `decisions/063_entrance_reattribution.md` Â· index `decisions/README.md`.

## Live numbers
| ÐšÐ°ÐºÐ²Ð¾ | Ð¡Ñ‚Ð¾Ð¹Ð½Ð¾ÑÑ‚ | ÐšÐ¾Ð¼Ð°Ð½Ð´Ð° |
|---|---|---|
| commits on `main` | 485 | `git rev-list --count main` |
| last commit | 542c2cc 2026-09-02 | `git log -1 --format='%h %cs' main` |
| last pushed commit | 69d146a 2026-08-15 | `git log -1 --format='%h %cs' origin/main` |
| commits ahead of `origin/main` (the 2026-09-01 plan, unpushed) | 3 | `git rev-list --count origin/main..main` |
| numbered ADR files | 60 | `ls docs/decisions \| grep -cE '^[0-9]{3}_'` |
| missing numbers in 001â€“063 | 17 24 51 | `PYTHONIOENCODING=utf-8 python -c "import os,re;h={int(m.group(1)) for f in os.listdir('docs/decisions') for m in [re.match(r'(\d{3})_',f)] if m};print(*[n for n in range(1,64) if n not in h])"` |
| entries in `config/entrance_reattribution.json` | 125 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('config/entrance_reattribution.json',encoding='utf-8'))['entries']))"` |
| Fire_Varna commit carrying that payload | c0db844 2026-08-31 | `git -C ../Fire_Varna log -1 --format='%h %cs' -- data/search_index.json` |
| payload numbers (that commit's subject) | 4764 entrances (-98 phantom markers), 86232 public entries | `git -C ../Fire_Varna log -1 --format=%s c0db844 \| grep -oE '[0-9]+ entrances[^,]*, [0-9]+ public entries'` |
| modified tracked files | 4 | `git status --porcelain \| grep -c '^ M'` |
| days without a content commit (2026-08-15 â†’ the date above) | 18 | `python -c "import datetime;print((datetime.date(2026,9,2)-datetime.date(2026,8,15)).days)"` |
| archived chronicle, lines | 2121 | `wc -l < "$(ls docs/archive/activeContext_2026-08-15.md 2>/dev/null \|\| echo docs/activeContext.md)"` |
| files in `C:\git\Varna_FireSafety_M6000` | 4 | `ls C:/git/Varna_FireSafety_M6000 \| wc -l` |
| its size | 2.3G | `du -sh C:/git/Varna_FireSafety_M6000 \| cut -f1` |

## Forbidden here
- `git push` â€” Petar only. Editing `docs/architecture_v2.md` outside an architecture cycle. Committing raw KAIS/OSM data, `output/`, secrets, personal data. Running `scratch/inspect_kais.py`. A coordinate without its CRS (BGS2005 vs WGS84).

## Where things are
- `architecture_v2.md` (canonical; its header says last updated 2026-06-02 â€” numbers not re-verified on 2026-09-02) Â· `data_quality/register.md` (canonical class register; the flat `data_quality_register.md` is kept for inbound links, ADR 060) Â· `decisions/` (numbered ADRs â€” count in the table â€” plus README and the legacy `lookup_map_*` files: `ls docs/decisions | grep -vE '^[0-9]{3}_'`) Â· `scratch/adrNNN_*` (evidence behind ADRs; LOT 1) Â· `output/`, `data/` gitignored except the exceptions listed in `.gitignore`.
- Outside git: `C:\git\m6000_private\` (municipal-map aid; cadnum-bearing, never committed) Â· `C:\git\Varna_FireSafety_M6000\` (rasters, see the table â€” Ð’-7).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git log -1 --format=\"%h %s\"; rg --files -g AGENTS.md -g CLAUDE.md -g '*bridge_depth*' -g '*po_poligon*' -g '*signed_quarter*' C:/git/Fire_Varna C:/git/varna_3d; rg -n \"search_bridge|margin_ratio|polygon_cover\" tools js src" in C:\git\Varna_buildings
 succeeded in 530ms:
# Varna_buildings â€” Architecture v2

> Checked 2026-09-02 (commit 542c2cc): every number in this document carries its own measurement date; whatever is stale as of 2026-09-02 is flagged with âš  under the line.

> Last updated: 2026-06-02 (ADR 026 amendment)
> Status: Active (supersedes architecture_v1.md per ADR 020)
> Scope: This document covers the Varna_buildings repo only.

For governance and approval gates, see [`AGENTS.md`](../AGENTS.md). For
the per-commit execution protocol, see [`CLAUDE.md`](../CLAUDE.md).
For the history of how the project arrived at its current shape, see
[`archive/architecture_v1.md`](archive/architecture_v1.md).

---

## What this repo does

This repo produces a static, offline-capable interactive map of Varna's
buildings. Building geometry is taken **primarily** from imagery-traced
sources â€” OpenStreetMap footprints, with Microsoft ML Building Footprints
filling buildings OSM has not yet mapped â€” so footprints align with
reality. KAIS (Ð¡Ð³Ñ€Ð°Ð´Ð¸ / Ð˜Ð¼Ð¾Ñ‚Ð¸ / Ð¡ÐžÐ˜Ð¡) supplies the attribute layer
(cadastral identity, apartment counts, floor counts, building age,
per-entrance aggregates, address provenance), joined to the rendered
geometry via the KAISâ†”OSM/ML link. **Per ADR 026, a real building that
no imagery source covers falls back to its KAIS cadastral footprint as a
gated, low-confidence last resort** (fuzzy-OSM-demotion-, road-guard-,
and overlap-clip-gated; see *Geometry-selection stage* below). Only a
building with no usable footprint from any source would render as a
point marker; such buildings â€” and those excluded by the realness gate â€”
are not rendered but remain searchable via a minimal summary and address
pin (ADR 026 D7).

- Spatial display of every building polygon in Ð³Ñ€. Ð’Ð°Ñ€Ð½Ð° (city-level,
  ekatte=10135).
- Click-through to per-building cadastral identity, apartment counts,
  per-entrance unit aggregates, and address provenance.
- Address-based, parcel-based, and entrance-based search.

The map application is the primary deliverable and is served as static
files via `python -m http.server 8000` from repo root (see

 succeeded in 778ms:
rg: C:/git/Fire_Varna/scratch/places_search/adresi_astra_S3*_08.09.md: IO error for operation on C:/git/Fire_Varna/scratch/places_search/adresi_astra_S3*_08.09.md: The filename, directory name, or volume label syntax is incorrect. (os error 123)
20:    "test:quarter-registry": "node js/test_quarter_registry.mjs",
25:const QUOTE_RE = /["'„“”«»]/g;
26:
27:// v1.1 signature lock (plan C1a; the ADR 039 sidecar model). "Signed" must be
28:// MACHINE-checkable, otherwise a test run proves nothing about WHICH registry it
29:// tested. Two locks, both fail-loud:
30://   * schema_version must equal REGISTRY_SCHEMA_VERSION;
31://   * sha256 over a CANONICAL PROJECTION of the behaviour-bearing content must
32://     equal REGISTRY_SIGNED_SHA256.
33:// The hash deliberately covers the projection, not the raw file bytes: the repo
34:// normalizes EOLs (.gitattributes `* text=auto eol=lf`), so a byte hash would
35:// break on checkout. Locked: schema_version, every entry's id/display/kind/
36:// normalized aliases/parents/pending aliases/map flags, coord_rules,
37:// block_overrides, holdouts, and the report_only / pending_p3 / composite_review
38:// buckets. NOT locked: free prose (`signed.*`, `policy.note`, `why`, `comment`,
39:// `matcher_constraints`) — a typo fix there must not brick the loader, while every
40:// byte that can move a label is under the lock.
41:export const REGISTRY_SCHEMA_VERSION = "1.1";
42:// Re-signed 2026-08-12 after the audit: the П2 holdout bbox was ~1.3 x 1.1 km and
43:// held 91 genuine "ж.к. Владислав Варненчик" rows away from their canon. It is now
44:// +/-60 m around the single Дертлиев point it was always meant to guard.
45:export const REGISTRY_SIGNED_SHA256 =
46:  "5338996806c76278ab733940f844633e41e8774aa7d71e585b4093a0150a660e";
47:
48:export function normQuarterKey(s) {
49:  return String(s ?? "")
50:    .replace(QUOTE_RE, "")
51:    .replace(/\s+/g, " ")
52:    .trim()
7:[Omitted long matching line]
10:[Omitted long matching line]
29:      "display": "Колхозен пазар",
30:      "why": "Р9: 432 м от Колхозен пазар"
66:      "display": "кв. Владиславово",
68:[Omitted long matching line]
70:        "кв. Владиславово",
72:        "ж.к. Владислав Варненчик",
77:        "ж.к. Владислав Варненчик-II м.р.",
149:      "display": "ж.к. Бриз",
151:      "why": "Спека 12.08 (отменя Р6): всичко Бриз-ово е ЕДИН квартал, канон ж.к.; 108 т.",
156:        "ж.к. Бриз",
157:        "ж.к. Бриз, м-ст Акчелар",
158:        "ж.к. Бриз-юг",
159:        "кв. Бриз"
188:        "м. Свети Никола / Бриз/",
243:[Omitted long matching line]
336:[Omitted long matching line]
558:      "why": "Спека 12.08 + Петър 12.08 вечер: скобата пада; Владиславово е РОДИТЕЛ (qtk разширение)",
562:        "кв. Кайсиева градина (Владиславово)"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; rg -n --max-count 20 --max-columns 240 "qtk|quarter" js/build_geocoder_index.mjs; rg -n --max-count 20 --max-columns 240 "quarter|collision|collid|street|function build" js/lib_fire_varna_block_labels.mjs; $lines=Get-Content -Encoding utf8 config/quarter_registry.json; for($i=60;$i -le 89;$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }' in C:\git\Varna_buildings
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $lines=Get-Content -Encoding utf8 js/lib_fire_varna_block_labels.mjs; foreach($span in @(@(180,237),@(259,325))){ for($i=$span[0];$i -le $span[1];$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] } }' in C:\git\Varna_buildings
 succeeded in 778ms:
180:    if (!quarter) { noQuarter += 1; continue; }   // no publish-safe quarter -> no C2 label
181:    if (quarter !== modal(rec.quarters)) raionDeprioritized += 1;   // район-naive modal would differ
182:    const street = modal(rec.streets);            // null if none
183:    chosen.set(cx, { quarter, n: rec.n, street: street || null, base: `${quarter}, бл. ${rec.n}` });
184:  }
185:
186:  // Pass C — collision detection on (cleaned-quarter, block#); disambiguate with street.
187:  const byQN = new Map();    // "<quarter>||<n>" -> Set<cx>
188:  for (const [cx, c] of chosen) addToSetMap(byQN, c.quarter + "||" + c.n, cx);
189:  const labelByComplex = new Map();
190:  let disambiguated = 0, collisionNoStreet = 0;
191:  for (const [cx, c] of chosen) {
192:    const collided = byQN.get(c.quarter + "||" + c.n).size >= 2;
193:    let label = c.base;
194:    if (collided) {
195:      if (c.street) { label = `${c.base}, ${c.street}`; disambiguated += 1; }
196:      else { collisionNoStreet += 1; }            // keep base (entry gate still applies)
197:    }
198:    labelByComplex.set(cx, { label, quarter: c.quarter, n: c.n, street: c.street, collided });
199:  }
200:  let collisionPairs = 0, collisionGroups = 0;
201:  for (const [, set] of byQN) if (set.size >= 2) { collisionPairs += 1; collisionGroups += set.size; }
202:
203:  return {
204:    labelByComplex,
205:    stats: {
206:      blockGroups: perCx.size,
207:      labeled: chosen.size,
208:      noQuarter,
209:      raionDeprioritized,    // groups whose quarter changed because a район name was deprioritized
210:      collisionPairs,        // distinct (quarter, block#) pairs shared by >=2 groups
211:      collisionGroups,       // total groups falling in a collision pair
212:      disambiguated,         // groups that received a street suffix
213:      collisionNoStreet,     // collided groups with no safe street (kept bare base)
214:    },
215:  };
216:}
217:
218:
219:
220:
221:
222:
223:
224:
225:
226:
227:
228:
229:
230:
231:
232:
233:
234:
235:
236:
237:
259:
260:
261:
262:
263:
264:
265:
266:
267:
268:
269:
270:
271:
272:
273:
274:
275:
276:
277:
278:
279:
280:
281:
282:
283:
284:
285:
286:
287:
288:
289:
290:
291:
292:
293:
294:
295:
296:
297:
298:
299:
300:
301:
302:
303:
304:
305:
306:
307:
308:
309:
310:
311:
312:
313:
314:
315:
316:
317:
318:
319:
320:
321:
322:
323:
324:
325:

 succeeded in 795ms:
51:// ADR 039 C1 — label-aware qtk provenance + quarter_assignment_trust (ON-only):
53:// PREPENDS the OSM-guessed quarter into cluster_details.label, so the naive
55:// The corrected D4 rule: strip the OSM-quarter label prefix ("<name>, " /
59:// quarter-origin tokens (quarter.name + the stripped prefix occurrences) are
60:// SPLIT into a parallel `qtk` array unless independently present in core.
61:// tk ∪ qtk per entry equals the old flat tk (count-neutral; vocab + inverted
63:// trust-agnostic (trusted entries carry qtk too); the POLICY (C2 down-weight)
64:// is conflicted-gated via the entry-level `quarter_assignment_trust` stamp read
65:// from the ADR 039 C0 sidecar (output/quarter_trust_sidecar.json — a REQUIRED
69:// metadata and is NEVER stripped (kais-sourced clusters keep qtk empty unless
70:// quarter.name tokens are genuinely label/address-independent).
118:// ADR 039 C1 — quarter_assignment_trust sidecar (deterministic Python pre-step;
119:// tools/build_quarter_trust_sidecar.py). REQUIRED: unlike the physical-building
124:  "output/quarter_trust_sidecar.json",
138:// quarter-trust sidecar above): absent / unreadable / self-hash-mismatched ⇒
149:// alias sidecar above, NOT the REQUIRED quarter-trust one): absent / unreadable /
166:// district sidecars, NOT the REQUIRED quarter-trust one): absent / unreadable /
181:// ADR 052 C1 — SOIS-derived quarter (`stk`) sidecar (deterministic Python
182:// pre-step; tools/build_sois_quarter_sidecar.py). OPTIONAL / FAIL-SOFT (like the
183:// alias/district/osm sidecars, NOT the REQUIRED quarter-trust one): absent /
5:// label of the form "<quarter>, бл. <N>":
7://   * <quarter> = the MODAL `quarter.name` across the group's member clusters
16://   * Street/boulevard disambiguation: ONLY when the same (cleaned-quarter, block#)
17://     maps to >=2 DISTINCT consolidated groups, append the modal street/boulevard from
18://     `address_line` → "<quarter>, бл. <N>, <street>". House numbers are NEVER appended
19://     (the address_line conflates the block# as a street number, e.g. "бул. Света
38:// Street-type opener that makes us confident a phrase is a real street/boulevard.
50:// Clean a raw quarter.name into a publish-safe display, or null (fail-closed).
60:// The 5 Varna РАЙОН (administrative-district) names. A district-level quarter display is
68:function quarterCore(disp) {
74:export function isRaionName(disp) { return RAION_CORES.has(quarterCore(disp)); }
80://   * drop a redundant non-"бл." segment that merely repeats the quarter (first) segment,
91:    const q0 = quarterCore(segs[0]);
95:      const c = quarterCore(segs[i]);
104:// Extract "<street-type> <name>" from an address_line, dropping any house number and
105:// entrance suffix. Returns null when the phrase has no street-type opener or leaks.
116:    if (/^(бл|блок)\.?$/i.test(t)) break;     // block marker introduces the block#, not the street
120:  // SAME display cleanup as the quarter: strip quotes, title-case ALL-CAPS tokens
122:  const street = out.join(" ").replace(QUOTE_RE, "").replace(/\s+/g, " ").trim();
124:  if (!/[A-Za-zА-Яа-яЁё]/.test(street.replace(STREET_TYPE_RE, ""))) return null;
60:      "why": "Р10: OSM казва Левски; подпис 30.07"
61:    }
62:  ],
63:  "entries": [
64:    {
65:      "id": "vladislavovo",
66:      "display": "кв. Владиславово",
67:      "kind": "кв",
68:      "why": "Р1+Р2 (30.07). ВНИМАНИЕ: 26 м.р. НЕ Е Владиславово (поправка на Петър, 30.07). Р33 (30.07): голото typo 'Влладислав Варненчик' (27 адр. до Кайсиева) — измереният единствен теч, влива се тук",
69:      "aliases": [
70:        "кв. Владиславово",
71:        "Влладислав Варненчик",
72:        "ж.к. Владислав Варненчик",
73:        "ж.к. Вл. Варненчик I м.р.",
74:        "ж.к. Вл. Варненчик II м.р.",
75:        "ж.к. Влладислав Варненчик - II м.р.",
76:        "ж.к. Вл.Варненчик",
77:        "ж.к. Владислав Варненчик-II м.р.",
78:        "ж.к. Вл. Варненчик",
79:        "ж.к. Вл.Варненчик II м.р.",
80:        "ж.к. Вл.варненчик- IIм.р."
81:      ]
82:    },
83:    {
84:      "id": "vazrazhdane",
85:      "display": "ж.к. Възраждане",
86:      "kind": "жк",
87:      "why": "Р3: голото остава; чистят се typo/кръстоски",
88:      "aliases": [
89:        "ж.к. Възраждане",

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json
from pathlib import Path
b=json.loads(Path('app/modules/search/data/search_bridge.json').read_text(encoding='utf-8'))
print('bridge keys:',list(b))
for cid,s in b['cluster_summaries'].items():
    st=json.dumps(s,ensure_ascii=False)
    if ('Студентска' in st and ('бл. 11' in st or 'блок 11' in st)):
        print(cid,{k:s.get(k) for k in ['label','address_line','center','quarter']})
'@ | python -B -X utf8 -" in C:\git\Varna_buildings
 succeeded in 1243ms:
bridge keys: ['cadnum_to_cluster_id', 'parcel_cadnum_to_cluster_ids', 'cluster_summaries']

codex
Подписаните полигони не са официален кадастрален регистър, затова 16 869 несъгласия не означава 16 869 доказани грешки. Проверихме и покритието: Център и Колхозен пазар вече имат полигони, но остават дупки и спорни граници; Цветен квартал няма отделен полигон. Решението трябва да отделя сигурното присвояване от тези нерешени случаи.
codex
Независимото преизчисление потвърди точно 9 255 точки извън полигоните, но откри разлика при припокриванията: 2 882 точки попадат в повече от един полигон, а таблицата отчита 2 483. Проверяваме дали има необявено правило за родствата. Засега таблицата е аритметично вярна, но методът ѝ не е напълно възпроизводим — това е съществено за бъдещия гейт.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $lines=Get-Content -Encoding utf8 C:/git/Fire_Varna/scratch/places_search/adresi_bridge_depth_08.09.json; for($i=1;$i -le [Math]::Min(145,$lines.Length);$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }; $lines=Get-Content -Encoding utf8 C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md; for($i=40;$i -le 74;$i++){ '"'{0}:{1}' -f "'$i,$lines[$i-1] }' in C:\git\Varna_buildings
 succeeded in 697ms:
1:{
2: "by_key": {
3:  "osm|nearest_point|low": {
4:   "outside": 3649,
5:   "agree_edge": 2244,
6:   "disagree_edge": 1402,
7:   "agree": 1776,
8:   "disagree": 1221,
9:   "overlap": 507
10:  },
11:  "kais|-|kais": {
12:   "overlap": 462,
13:   "agree_edge": 6094,
14:   "agree": 7070,
15:   "disagree": 4449,
16:   "outside": 3710,
17:   "disagree_edge": 3765
18:  },
19:  "osm|nearest_point|high": {
20:   "agree": 6265,
21:   "disagree": 859,
22:   "agree_edge": 2947,
23:   "overlap": 842,
24:   "disagree_edge": 1095,
25:   "outside": 527
26:  },
27:  "osm|nearest_point|medium": {
28:   "agree_edge": 2421,
29:   "disagree_edge": 1278,
30:   "overlap": 420,
31:   "agree": 2728,
32:   "disagree": 834,
33:   "outside": 754
34:  },
35:  "osm|polygon_cover|high": {
36:   "disagree_edge": 363,
37:   "disagree": 761,
38:   "outside": 268,
39:   "overlap": 246,
40:   "agree_edge": 139,
41:   "agree": 89,
42:   "no_word": 10
43:  },
44:  "osm|nearest_point|flagged": {
45:   "disagree_edge": 408,
46:   "outside": 347,
47:   "agree_edge": 160,
48:   "agree": 64,
49:   "disagree": 434,
50:   "overlap": 6
51:  }
52: },
53: "disagree_top": [
54:  [
55:   "кв. \"ГАЛАТА\"",
56:   "с.о. Боровец-юг",
57:   1293
58:  ],
59:  [
60:   "кв. Розова долина",
61:   "кв. Аспарухово",
62:   771
63:  ],
64:  [
65:   "с.о.\"Траката\"",
113:  ],
114:  [
115:   "ж.к. \"ВЛАДИСЛАВ ВАРНЕНЧИК\"",
116:   "кв. Владиславово",
117:   162
118:  ],
119:  [
120:   "ж.к. Св. Иван Рилски",
121:   "Западна промишлена зона",
122:   153
123:  ],
124:  [
125:   "Гръцката махала",
126:   "Център",
127:   152
128:  ],
129:  [
130:   "с.о. Ален Мак",
131:   "к.к. Златни пясъци",
132:   128
133:  ],
134:  [
135:   "ж.к. Дружба",
136:   "кв. Аспарухово",
137:   119
138:  ],
139:  [
140:   "м-т Кокарджа",
141:   "с.о. Пчелина",
142:   119
143:  ],
144:  [
145:   "кв. Чайка",
40:**D2 · Лицензът се решава ТУК (К4).** Таблица `method` → лиценз, проверявана за СЪГЛАСИЕ: „по памет“ / „по огради“ → **CC0-1.0**; „по сгради“ → **КАИС „Отворени данни“, атрибуция АГКК, CC0 не се твърди — ЗАКЛЮЧЕН, докато `_meta.faza0_signed` не е `true`, а той не може да е `true`, докато `ФАЗА_0_лицензи.md:4` носи „чака подпис“ (G21)**; „по улици“ → **ЗАКЛЮЧЕН винаги** (нарушава условие 4, `ФАЗА_0_лицензи.md:25-26`), отключва се само с изричен подписан ключ. **Лицензът на ФАЙЛА е най-строгият участник.** Подложка: нашата PMTiles основа (ADR 002 D8) или КАИС; **никога Esri** — инструментът отказва връх, докато `map.getLayoutProperty("sat","visibility") === "visible"` (`varna_3d/web/index.html:880`), проверено от G18.
41:
42:**D3 · Къде живее геометрията и как е вързана.** Каноничен файл: **`varna_3d/data/quarters_signed.geojson`**, версиониран в git. `m6000_private` НЕ е git репо; `Fire_Varna/data/` е публичната папка и отпада по S5; **това решение стои върху предусловие 5 и не е валидно, докато G19 не покаже частно репо.** Файлът се хваща от `varna_3d/.gitignore:4` и `:23` → иска `!data/quarters_signed.geojson` **след ред 23** (М0.9). **Публикува се само `quarter: {name, code, src}` и изведеният `zone`; геометрия никога.** К5 ↔ S5: следвам S5 за РЕДА и К5 за ВЕРСИЯТА — `polygon_version` и `polygon_sha256` са ЗАДЪЛЖИТЕЛНИ в `expectations.json._meta` и в `data/place_categories.json._meta`, **никога на ред** (редът е 13/17 ключа, `index.html:6275`, `:6281`; `_meta` на доставката е затворен 9-ключов набор, `qa_fire_varna_places_export.py:62`, налаган на `:550`). **Ограничение, мерено:** `SIGNABLE` (`gates/release.py:175-183`) е затворена шесторка с пътища спрямо Fire_Varna, а `blob_at` (`:223`) чете блоб от ТОВА репо — **чужд път е недостъпен, значи геометрията НЕ може да получи ред клас „артефакт“.** Дайджестът ѝ пътува през `expectations._meta.polygon_sha256` + ред клас „въпрос“ с видимо `тяло: <sha256>` + G4 и G7. Разширяването на `SIGNABLE`/`blob_at` към чуждо репо е **съзнателно отложено за Фаза C**.
43:
44:**D4 · Регистър ↔ полигон: три декларирани множества.** Всеки жилищен код (kind ∈ {кв, жк, кк}, ЧЕТЕН ОТ РЕГИСТЪРА, никога от литерал) попада в точно едно от `polygon` · `no_boundary` (Feature с `geometry: null`, RFC 7946, с довод и подпис) · `deferred` (`_meta.deferred`, с довод и дата, броен дълг). Липса и в трите = ЧЕРВЕНО. К7 т. 1: празен квартал носи `_meta.no_places: [{code, why, signed_by, signed_at}]`; гейтът сравнява МНОЖЕСТВА: „жилищни кодове с нула доставени реда ⊆ `no_places` ∪ `deferred`“, падайки поименно. **Ако `tsveten_kvartal` попадне в `no_boundary`/`deferred`, проверката след пуша №2 става НЕПРИЛОЖИМА и това се записва в отчета** (решение §6.28).
45:
46:**D5 · Ново име само с ≥ 2 свидетеля (К3) и обратим път.** „Цветен квартал“: свидетел 1 = подписът на Петър; свидетел 2 = `node/9664925200` с 15 места на ≤ 900 m. Втори свидетел може да е и АГКК именувана точка (Левски и Максуда имат; М0.21), ред от пощенския указател или общинска публикация с адрес (М0.22) — по-силни от OSM възел, защото са официални. При ЕДИН свидетел името е `alias`, не код. **Отмяна:** ред клас „въпрос“ + обратен диф с двоен запис + махане на кода от петте затворени списъка в един комит на Fire_Varna; фикстура: код в доставка, който вече не е в регистъра → червено. Записът влиза през конвейера на Varna_buildings (D14).
47:
48:**D6 · `SIGNED_POLYGON` — свидетел ранг 3 (S1/К2).** Нов канал под `REG-*` (0), `KAIS-quar` (1), `KAIS-addr` (2). ОТДЕЛЕН блок в `varna_3d/src/fire_varna_locations.py` **между ред 873 и 875** — след записа на `picked` в `out` (867–873), преди `if signed:` (875) — и **никога в цикъла `offered/ranked/conflict` (785–853)**, където `conflict` бланкира вече написано поле (`:834`, `:852`) и вкарва реда в `pending_signature`. **Шест състояния:** `confirmed` · `compatible` (деклариран родител/дете, БЕЗ замяна и без уточняване) · `disputed` · `edge_pending` (D7) · `override_noted` · `written`. Пише САМО в ред без нито един свидетел, без `pending`, извън ръба, в точно един полигон (или в декларираното дете), с `witness=[CH_SIGNED_POLYGON]` и кода в `channels[CH_SIGNED_POLYGON].ids` (`qa_fire_varna_m6.py:304-308`). Полигон-местност никога не пълни `quarter` — `classify(code) == field` (`KIND_CLASS:118`), с падаща фикстура. `_narrow` (`:907-917`) уточнява САМО вътре в полигонния канал. **`SIGNED_OVERRIDE` се пази безусловно (S1):** при 12-те подписани хотела блокът само сравнява и пише `override_noted` в леджера; никога не мени полето, никога не влиза в `signed_vs_witness`, а `CHANNEL_RANK` не получава ключ `SIGNED_OVERRIDE`. **`disputed` е ЛЕДЖЕР-САМО:** редът остава дословно както е, отива в `polygon_review`, нищо публично не се мени. Това е **обявено ОТКЛОНЕНИЕ от К2** (решение §6.4): `LOC_KEYS` са точно 3 (`index.html:6311`, `:6531-6533`), няма ключ за `winner`/`reason`, а „падане до район“ би изтрило написан от по-силен канал квартал. Таблицата на К2 е входна карта за реда в опашката; спорът се версионира (`polygon_review[i].polygon_version`). **159 е ДОПУСТИМАТА популация, не write-set.** 8-те сблъсъка не се решават от полигона.
49:
50:**D7 · Ръбът: `max(50, precision_m)` в EPSG:32635 върху пиннати ИЗВОРНИ координати (S2 + К5).** `_meta.precision_floor_m = 50`; гейтът отказва `precision_m < 50`. Забранено е да се четат изнесените координати (`fire_varna_locations.py:968-982` прави точно това и се маха от полигонния път). Мери се И точката, И закотвеното тяло (`evidence.kais_i`); разминаване → `edge_pending`. Формулата е `shapely.geometry.shape(f["geometry"]).boundary.distance(point)` — през `shape`, защото подписан квартал реалистично е MultiPolygon. Проекция: `place_identity.make_projection()` (`:219-236`); `pyproj` 3.6.1, `shapely` 2.1.2 — нула нови зависимости. **Никакво местене, никакъв snap.** `SIGNED_POLYGON_BORDER` НЕ става публикуван `src` — **обявено ОТКЛОНЕНИЕ от К5** (решение §6.16).
51:
52:**D8 · Йерархията — само подписана и геометрично доказана.** Родство се чете единствено от `parents` (днес 6 записа), ациклично И доказано: **дете ⊆ родител в рамките на `precision_m` буфер**; фалшив `parent` = червено. **Числовата опашка в `is_child` (`:488-503`) не е родство при полигони.** „≤ 1 полигон на място“ важи между НЕСРАВНИМИ квартали. **В ПРАЗЕН ред пише детето; в ред с написан квартал полигонът НИКОГА не уточнява.** Възраждане 1–4 нямат `parents` — поправка в регистъра, ПРЕДИ кода (D14).
53:
54:**D9 · Версии, диф и откат (К5, S1).** **ВСЯКА нова версия иска подпис на Петър.** Прагове: > 2 места сменят квартал ИЛИ > 10 % площ → двоен запис преди/след и пълно преизмерване; под тях — обикновен отчет. `--diff <предишна>` е ГЕЙТ с изход ≠ 0 над праговете (G15). **Версия 1: диф-гейтът е НЕПРИЛОЖИМ, не червен.** **Откат на лоша версия:** предишната подписана версия се връща като НОВА версия (`version` расте, `previous_version` сочи отхвърлената, `note` носи довода), минава пълния G1+G15 и се комитва от Петър; никакво `git revert` върху геометрия и никакво тихо редактиране. Всеки диф се предава като ред клас „въпрос“ (по D3 не може да е „артефакт“).
55:
56:**D10 · Леджерът и пиновете (S1, S2).** Към **23-те колони** (М0.4): точка/тяло + CRS, кандидат-полигони, канал, `dist_to_edge_m`, състояние по D6, старо/ново по КОД, хешове на геометрия/регистър/алгоритъм, `approval_digest`. В `_meta`: `pins_polygons` до `pins_m6` (`:1111`), `polygon_review` до `pending_signature` (`:1140`), и **`base_rev` — ревизията P7, срещу която се мерят D18 и манифестът-данни**. **Координатата идва от `lat`/`lon`, добавени в `data/place_identity.json`** (мерено: 375 обекта, 0 с координата) като НОВ ПИНАТ вход в `RECORDED_INPUTS` (`:91-92`), с гейт G9. **Пиновете на `quarters_signed.geojson`, `place_identity.json` и `web/varna_buildings_3d.geojson` влизат в `build_inputs` (`:1247-1253`) И СЕ СВЕРЯВАТ в `_check_pins` (`:623-639`) и в G-M6.** `--inputs` (`:1305-1310`) е ПИСАТЕЛ, пуска се веднъж.
57:
58:**D11 · Инструментът и provenance (S3).** Свой „режим граница“ във `varna_3d/web`, **нула нови runtime зависимости** (`web/vendor` държи само maplibre-gl **5.7.2** — `web/vendor/maplibre-gl.js:3` — и pmtiles 4.3.0; М0.18). `pitch = 0` + `map.setTerrain(null)` (`web/index.html:1962-1963`), `#pitch` disabled, кликът отговаря ПРЕДИ хидранта (`:4571`). Лентата на неточността: `line-width` по `156543.03392·cos(43,2°)/2^z` → z13 3,6 · z16 28,7 · z18 114,9 px за 50 m (М0.13). Слоеве-свидетели: КАИС телата, 375-те пина, OSM етикет-точките, **предишната версия като отделен слой**. Записва целия набор на D1. `preserveDrawingBuffer` — **един условен ред** зад `?granitsa` (`:828-841`). **STOP:** безусловен `preserveDrawingBuffer`; какъвто и да е `POST` в `serve.py`. Износ = Blob + `<a download>`.
59:
60:**D12 · Търсенето (клас B) — К6 + S4.** Идемпотентен `location_key(toks) -> (type, phrase)`, приложен ИДЕНТИЧНО върху индекса и остатъка, дефиниран върху **СПИСЪК ОТ ТОКЕНИ**. Типовият префикс е поредица с двете си арности. Хвърля съюза „и“ и префикса, **пази числата** и затворен списък посоки. Правило: остатъкът == пълната фраза на ТОЧНО ЕДИН запис, иначе уникална СЪСЕДНА подфраза; пазач: число / посока / „sveti“ никога не квалифицира. **Областта е ИЗНЕСЕНИЯТ речник**, премерен наново преди подпис. **Типът СТЕСНЯВА само когато е изричен И съвпада с поне един кандидат.** **Двусмислието не ражда нов видим текст** (`AGENTS.md:138`) — **обявено ОТКЛОНЕНИЕ от К6**: уточнителят при двусмислие е отложен, защото иска дословен български текст от Петър (решение §6.20); днешното поведение при двусмислие се запазва и се пази от замразена заявка. **Родител ⊃ дете живее в ИЗНОСА** (per-code `type` и `parents` по КОДОВЕ); затворените списъци → `_meta` до `zone_generic_words` (`build_place_categories.py:566`), fail-closed. **Паритет:** `window.__places.locationKey(q)` влиза в корпуса `probe_out/token_parity.json` (**759 низа**, М0.18). **11 подписани вектора** + проби съюз, точкувана форма, число, посока, двусмислие, йерархия. Манифест по `bundle:ordinal` („РОЯЛ“ ×2; `release.compare()` сравнява по име, `gates/release.py:780-823`). **Смяна на КЛОН при непроменени редове = делта от първи ред.**
61:
62:**D13 · Атомност през ТРИ репа (S5/S6).** Един комит през две репа не съществува. **Подредената тройка важи за ДАННИТЕ, не за инструмента:** инструментът (Г1) и гейтовете му са предпоставка и стоят извън тройката. Тройката е: **(1) Varna_buildings** — записът, `parents`, преподписаната константа (D14); **(2) varna_3d** — резолверът, двата износни гейта (`qa_fire_varna_export.py:191`, `qa_fire_varna_places_export.py:323`), вторият препис (`qa_fire_varna_m6.py:58-64`), износът; **(3) Fire_Varna** — **блобовете влизат в СЪЩИЯ комит със затворените списъци**: `QUARTER_SRC` (`index.html:6313`), `QUARTER_CODES` (`:6317`), `LOCALITY_CODES` (`:6322`), трите SHA пина (`:6288-6290`), `LEGACY_BUNDLE_SHA` (`:6301`), `PLACES_CACHE` v6 → **v7** (`:6265`), и поименно пиновете на двата теста: `PLACES_SHA256`/`BYTES` 122089/`GZIP9` 13728, `HOTELS_*` 148685/13084, `CATEGORIES_*` 75818/9104, `QUARTER_BY_SRC` (точно равенство), `QUARTER_CODES`, `LOCALITY_CODES`, `LOCATION_COUNTS` {quarter 20, district 5, locality 5}, `LEGACY_ROWS` 18, `LOCALITY_COUNT`; плюс baseline → `fd13907` (`signed_by: "pending — Петър"`) и подмяната на allow-файла. Числата се ПРЕМЕРВАТ след чертането. Тихата смърт, доказана: непознат `src` → `validLocation` false (`:6528-6534`) → `validTypedLocation` (`:6535-6541`) → `validatePlaces2` (`:6569-6576`) → `null` → `places2 = []`, хотелите остават (`:6627-6640`) — **150 места изчезват мълчаливо**; `accept` сверява SHA само при `crypto.subtle` (`:6605`) → кешът задължително на v7. **Манифестите са ТРИ** (`gates/release.py:157-159`): `lot1v_v_manifest_BASE_P7.json` = дифът на ДАННИТЕ (P7→P8 по `place_id`), `lot1v_v_manifest_P7_F12.json` = дифът на ПОВЕДЕНИЕТО, `lot1v_v_reference_manifest.json` = манифестът на референцията; и трите се преизползват в съществуващите слотове с `_meta.what` и изричен ред „името е остаряло“. Имената живеят на **ПЕТ ръчни места**: `gates/release.py:157-159`, `:175-183`, `manifest_anchor_gate.py:42-44`, `recall_sweep.py:3070-3071`, `recall_sweep.py:2661`. **Замразените тела са ТРИ** (амандамент №11 т. 4): референцията `recall_sweep_rows.json` (вързана през `expectations._meta.reference`), `expectations.json`, и паритетният корпус `probe_out/token_parity.json`, който **днес не е вързан от нищо** и влиза в `expectations._meta.inputs`.
63:
64:**D14 · Регистърът е подписано тяло (S5).** `Varna_buildings/js/lib_quarter_registry.mjs:35` заключва `schema_version`, `id`, `display`, `kind`, `aliases`, `parents`; `:45` държи `REGISTRY_SIGNED_SHA256`; `:121-127` хвърля „never patch the constant to make a build pass“. Затова: (1) промяната е **СОБСТВЕН датиран план в Varna_buildings със собствен §7 (дефиниция за готово)**, минаващ през неговите Approval gates (`AGENTS.md:273-275`) **и през Кими и Astra** (§0.3), чиято присъда влиза в **собствен амандамент — нов датиран файл** в същата папка; (2) константата се преизчислява и **подписва от Петър, в негов комит**, заедно с данните; (3) `node js/test_quarter_registry.mjs` тича в кръга (G5); (4) **агент никога не пипа константата**. Преди комита: нула съвпадения на новото име в 449 `quar` + 19 813 `addr` и нула сблъсък на `match_key` (М0.14); след комита `qa_fire_varna_location_isolation.py` зелено (G6/G10) — `place_zones._registry:252-255` индексира БЕЗ вид.
65:
66:**D15 · Гейт 0 преди опашката.** `ЗА_ПОДПИС_Г.md` не се ПИШЕ, преди да е зелено: `release.find_queue` е рекурсивната версия; в HEAD има точно една опашка; в `gates/allow/` има точно един json (`run_gates.py:199-217`). Архивът на опашките е **извън** `scratch/places_search`. G0 е гейт-ред на всяка стъпка, чийто write-set пипа опашка или allow-файл.
67:
68:**D16 · Идентичности и write-set-ове.** Всеки комит носи изчерпателен write-set и дословно съобщение (таблицата е в плана §2). `Claude Architect` за планове и решения, `Claude Executor` за изпълнение, `Petar1984` само за `gates.sign`, подписаната геометрия и регистъра. Ръчният комит на Петър във varna_3d/Varna_buildings е **втори, назован клас** до амандамент №4 т. 6 и влиза като **амандамент — нов датиран файл**.
69:
70:**D17 · Дайджестът на тялото за доставка Г.** Амандамент №11 приема вариант (а) изрично „за доставка A“. За доставка Г вариантът се **преобявява** (решение §6.5): важи (а) — несъвпадение се прощава само когато последният комит по артефакта е на `Petar1984` — и G12 проверява точно това.
71:
72:**D18 · Написаният квартал не се променя.** След P8 всеки от **201-те** реда с написан квартал (М0.4) ЗАПАЗВА кода си. Базата „преди“ е назована: `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`, където `<base_rev>` е `_meta.base_rev` на леджера (D10) — същата ревизия, която храни манифеста-данни. Проверката е команда с изход ≠ 0 (G17).
73:
74:**D19 · Интервалът на замразяването е обявен, изброен и ограден.** `location_phrases` е подписана претенция в `expectations.json` (`tests/test_places_search_gate.py:464-478` я сверява с `REF.LOC_PHRASES`), а `--freeze` пренаписва очакванията едва СЛЕД подписа (амандамент №11 т. 3). Значи между F13-а и единственото `--freeze` `python -m unittest discover -s tests` е червен по конструкция. Това не е „червено по замисъл“, а **обявен интервал с гейт**: изпълнителят записва при отварянето му ТОЧНИЯ набор падащи тестове (G20), той трябва да е подмножество на назования в плана §2, всеки тест извън набора = STOP, и след `--freeze` наборът е ПРАЗЕН. Интервалът не пресича нито един гейт-ред, който твърди зелено.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-FileHash -Algorithm SHA256 app/modules/search/data/search_bridge.json, C:/git/varna_3d/data/quarters_signed.geojson, C:/git/Fire_Varna/scratch/places_search/adresi_bridge_depth_08.09.json | Select-Object Path,Hash; git -C C:/git/Fire_Varna log -1 --format="%h %cs %s"; git -C C:/git/varna_3d log -1 --format="%h %cs %s"' in C:\git\Varna_buildings
 exited 1 in 918ms:

fatal: detected dubious ownership in repository at 'C:/git/Fire_Varna'
'C:/git/Fire_Varna' is owned by:
	BUILTIN/Administrators (S-1-5-32-544)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/Fire_Varna
fatal: detected dubious ownership in repository at 'C:/git/varna_3d'
'C:/git/varna_3d' is owned by:
	PETAR/Petar (S-1-5-21-1992376794-12164101-10249461-1001)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/varna_3d
Path                                                                   Hash                                            
----                                                                   ----                                            
C:\git\Varna_buildings\app\modules\search\data\search_bridge.json      530ED91177050BE26B26B81AE935F6D379FB999078BDF...
C:\git\varna_3d\data\quarters_signed.geojson                           C1551D248E6450025664A4338CF7CB8A7E84E8275EBA2...
C:\git\Fire_Varna\scratch\places_search\adresi_bridge_depth_08.09.json BABC8D829AE75A657C6BA9787789F0A4B823AB3947149...



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git -c safe.directory=C:/git/Fire_Varna -C C:/git/Fire_Varna log -1 --format="%h %cs %s"; git -c safe.directory=C:/git/varna_3d -C C:/git/varna_3d log -1 --format="%h %cs %s"' in C:\git\Varna_buildings
 succeeded in 491ms:
074e133 2026-09-08 measure: the 3D map too — 80 497 buildings: 61% without any cadastral quarter word; of 31 116 with a word, 9 828 inside a polygon disagree (zone names vs signed quarters); polygons would name 38 871 buildings that have none
05f485e 2026-09-07 data: p8a quarter assignment ledger 07.09

codex
Разликата вече е обяснена точно: таблицата отделя 389 точки по родства от полето `properties.parent` и 10 без име. Подписаният списък с родства обаче е по-пълен и се намира в `_meta.parent_child`. Значи мярката използва непълна йерархия — общата поправка трябва да има един каноничен списък с родства и да го ползва и при присвояване, и при проверка.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json
from pathlib import Path
b=json.loads(Path('app/modules/search/data/search_bridge.json').read_text(encoding='utf-8'))
needle='\\u0441\\u0442\\u0443\\u0434\\u0435\\u043d\\u0442\\u0441\\u043a\\u0430'
for cid,s in b['cluster_summaries'].items():
    st=json.dumps(s,ensure_ascii=False).casefold()
    if needle in st and '11' in st:
        print(cid,{k:s.get(k) for k in ['label','address_line','center','pin','quarter']})
'@ | python -B -X utf8 -" in C:\git\Varna_buildings
 succeeded in 1251ms:
cluster_12dd020f4b3c1003 {'label': 'кв. Левски, Студентска 7', 'address_line': 'Студентска 7', 'center': None, 'pin': [27.92567, 43.22472], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'high', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 375.9415114044027, 'margin_ratio': 2.5976583284271615, 'second_choice_name': 'Цветен квартал'}}
cluster_17126519584a42ef {'label': 'м-т Сотира, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93911, 43.22454], 'quarter': {'name': 'м-т Сотира', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3574928810', 'place': 'neighbourhood', 'distance_m': 727.110716018475, 'margin_ratio': 1.3212596218813046, 'second_choice_name': 'кв. Чайка'}}
cluster_19cd7f8845376542 {'label': 'кв. Левски, Студентска бл. 3', 'address_line': 'Студентска бл. 3', 'center': None, 'pin': [27.93024, 43.22364], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 712.9655279216547, 'margin_ratio': 1.616527098413211, 'second_choice_name': 'кв. Чайка'}}
cluster_1b8d0664da1881c5 {'label': 'м-т Сотира, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93607, 43.22473], 'quarter': {'name': 'м-т Сотира', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3574928810', 'place': 'neighbourhood', 'distance_m': 779.3836133702043, 'margin_ratio': 1.3118791813087485, 'second_choice_name': 'кв. Чайка'}}
cluster_22a593c0a3137804 {'label': 'кв. Левски, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93256, 43.22403], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 903.0753395313461, 'margin_ratio': 1.121811699160036, 'second_choice_name': 'м-т Сотира'}}
cluster_25bbdae4564a51fa {'label': 'кв. Левски, Адрес: ул студентска', 'address_line': 'гр. Варна, район Приморски', 'center': None, 'pin': [27.93119, 43.22362], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 790.3588441006194, 'margin_ratio': 1.3930301498833217, 'second_choice_name': 'кв. Чайка'}}
cluster_3aeb62a2a5e049a1 {'label': 'кв. Чайка, ул. СТУДЕНТСКА', 'address_line': 'ул. СТУДЕНТСКА', 'center': None, 'pin': [27.93444, 43.22205], 'quarter': {'name': 'кв. Чайка', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/8494850997', 'place': 'suburb', 'distance_m': 804.9112490964013, 'margin_ratio': 1.3260376736430246, 'second_choice_name': 'кв. Левски'}}
cluster_423bb5bd98ad5ee7 {'label': 'м-т Сотира, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93702, 43.22375], 'quarter': {'name': 'м-т Сотира', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3574928810', 'place': 'neighbourhood', 'distance_m': 853.5079927114251, 'margin_ratio': 1.047542650240883, 'second_choice_name': 'кв. Чайка'}}
cluster_48f5accb4c639e66 {'label': 'кв. Левски, Студентска бл. 4', 'address_line': 'Студентска бл. 4', 'center': None, 'pin': [27.93141, 43.22329], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 808.9669782151209, 'margin_ratio': 1.311784905617968, 'second_choice_name': 'кв. Чайка'}}
cluster_5eb05fc2c606f820 {'label': 'кв. Чайка, Студентска бл. 11', 'address_line': 'Студентска бл. 11', 'center': None, 'pin': [27.9378, 43.22212], 'quarter': {'name': 'кв. Чайка', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/8494850997', 'place': 'suburb', 'distance_m': 707.5256325315034, 'margin_ratio': 1.4301715496700613, 'second_choice_name': 'м-т Сотира'}}
cluster_69325aa26dd32d13 {'label': 'кв. Чайка, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93444, 43.22325], 'quarter': {'name': 'кв. Чайка', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/8494850997', 'place': 'suburb', 'distance_m': 917.6718115526975, 'margin_ratio': 1.0866007721481332, 'second_choice_name': 'м-т Сотира'}}
cluster_9e2629ace9f7ae19 {'label': 'кв. Чайка, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93335, 43.22336], 'quarter': {'name': 'кв. Чайка', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/8494850997', 'place': 'suburb', 'distance_m': 932.7249760618207, 'margin_ratio': 1.0766166916428117, 'second_choice_name': 'м-т Сотира'}}
cluster_a3bf017cd1a075b2 {'label': 'кв. Чайка, ул. СТУДЕНТСКА-', 'address_line': 'ул. СТУДЕНТСКА-', 'center': None, 'pin': [27.93474, 43.22224], 'quarter': {'name': 'кв. Чайка', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/8494850997', 'place': 'suburb', 'distance_m': 821.7112618690617, 'margin_ratio': 1.3040099601453503, 'second_choice_name': 'кв. Левски'}}
cluster_c1ac64d717b7948b {'label': 'м-т Сотира, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93592, 43.22487], 'quarter': {'name': 'м-т Сотира', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3574928810', 'place': 'neighbourhood', 'distance_m': 781.6980291133202, 'margin_ratio': 1.3432202094670955, 'second_choice_name': 'кв. Чайка'}}
cluster_c8c84abe54eeee93 {'label': 'кв. Левски, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93179, 43.22527], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 860.4849793255223, 'margin_ratio': 1.113359824335493, 'second_choice_name': 'м-т Сотира'}}
cluster_d6ce9cb816a2a69d {'label': 'м-т Сотира, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93823, 43.22406], 'quarter': {'name': 'м-т Сотира', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3574928810', 'place': 'neighbourhood', 'distance_m': 794.3483135511833, 'margin_ratio': 1.1501924634421918, 'second_choice_name': 'кв. Чайка'}}
cluster_ec1f4bfed666a640 {'label': 'кв. Левски, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93173, 43.225], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 849.2432814416705, 'margin_ratio': 1.156076771521106, 'second_choice_name': 'м-т Сотира'}}
cluster_f00e04d99825fd8d {'label': 'кв. Левски, ул. СТУДЕНТСКА- №1', 'address_line': 'ул. СТУДЕНТСКА- №1', 'center': None, 'pin': [27.93165, 43.22453], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 837.7797261955795, 'margin_ratio': 1.2411313512026854, 'second_choice_name': 'м-т Сотира'}}
cluster_f91acade47d2bcda {'label': 'кв. Левски, Студентска 4', 'address_line': 'Студентска 4', 'center': None, 'pin': [27.93259, 43.22295], 'quarter': {'name': 'кв. Левски', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/3710056288', 'place': 'suburb', 'distance_m': 906.2955775811702, 'margin_ratio': 1.0729527525821903, 'second_choice_name': 'кв. Чайка'}}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import json
from pathlib import Path
b=json.loads(Path('app/modules/search/data/search_bridge.json').read_text(encoding='utf-8'))
needle='\\u0441\\u0442\\u0443\\u0434\\u0435\\u043d\\u0442\\u0441\\u043a\\u0430'
for cid,s in b['cluster_summaries'].items():
    a=s.get('address_line','').casefold()
    if needle in a and '11' in a: print(cid,{k:s.get(k) for k in ['label','address_line','pin','quarter']})
'@ | python -B -X utf8 -" in C:\git\Varna_buildings
 succeeded in 821ms:
cluster_5eb05fc2c606f820 {'label': 'кв. Чайка, Студентска бл. 11', 'address_line': 'Студентска бл. 11', 'pin': [27.9378, 43.22212], 'quarter': {'name': 'кв. Чайка', 'source': 'osm', 'confidence': 'low', 'mode': 'nearest_point', 'osm_id': 'node/8494850997', 'place': 'suburb', 'distance_m': 707.5256325315034, 'margin_ratio': 1.4301715496700613, 'second_choice_name': 'м-т Сотира'}}

codex
**Проблемът е системен: близост до име и кадастрална зона са превърнати в квартална принадлежност. Препоръчвам обща поправка в производителя на моста, след възпроизводима прекласификация.**

Причината в 10 реда:

1. На **21.05** е добавено OSM допълване за **22 571** клъстера без KAIS квартал; наличните кадастрални имена се запазват. [osm_quarter_integration_plan.md:5](C:/git/Varna_buildings/docs/archive/plans/osm_quarter_integration_plan.md:5)
2. Тогава справочникът е **50 точки и 12 полигона**; днес е 49+12. Точките дават покритие, но не описват граници. [план:21](C:/git/Varna_buildings/docs/archive/plans/osm_quarter_integration_plan.md:21)
3. Логиката е в `tools/build_lookup_map_v2.py`; `build_app_m1_data.py` копира резултата и записва моста. [build_app_m1_data.py:271](C:/git/Varna_buildings/tools/build_app_m1_data.py:271), [същият:1541](C:/git/Varna_buildings/tools/build_app_m1_data.py:1541)
4. Първото непразно KAIS `quarname` печели без пространствена проверка; кадастралната зона така става показван квартал. [build_lookup_map_common.py:626](C:/git/Varna_buildings/tools/build_lookup_map_common.py:626)
5. При липса: съдържащ OSM полигон, иначе най-близка точка; **няма дистанция, след която системата отказва име**. [build_lookup_map_v2.py:999](C:/git/Varna_buildings/tools/build_lookup_map_v2.py:999)
6. Увереността описва предположението, но Fire взема само `quarter.name` за блоковия етикет. Така **707,5 m / low** става категорично „Чайка“. [build_fire_varna_search_index.mjs:536](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:536)
7. ADR015 предлага преструктуриране, не пространствена поправка; ADR039 потвърждава неизпълнението и изрично запазва имената. [015:109](C:/git/Varna_buildings/docs/decisions/015_quarter_source_confidence_restructure.md:109), [039:14](C:/git/Varna_buildings/docs/decisions/039_kv_cleanup.md:14), [039:39](C:/git/Varna_buildings/docs/decisions/039_kv_cleanup.md:39)
8. ADR061 разглежда грешни координати; планът от **02.09** за курортите е ограничен до Fire проекцията и неизпълнен. [061:81](C:/git/Varna_buildings/docs/decisions/061_impossible_coordinates.md:81), [plan_quarters_resorts:100](C:/git/Varna_buildings/docs/plans/plan_quarters_resorts_2026-09-02.md:100)
9. Новите **60 подписани полигона** влизат на **07.09, 6486b48**; `05f485e` е последващият отчет. Подписът приема версия на предимно доброволчески, неофициални граници. [build_quarters_signed.py:752](C:/git/varna_3d/src/build_quarters_signed.py:752)
10. Интеграцията им обхваща празните квартали при места/хотели; мостът остава извън нея, а архитектурата още изисква KAIS→OSM. [Fire ADR010:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [architecture_v2.md:489](C:/git/Varna_buildings/docs/architecture_v2.md:489)

**Мярката показва мащаба, но още не дава надежден брой „грешни квартали“.**

Аритметиката е вярна: **31 997 съгласни + 16 869 несъгласни + 9 255 извън + 2 483 припокриване + 10 без име = 60 614**. От несъгласните **8 311** са отчетени в граничната лента. [мярка:121](C:/git/Fire_Varna/scratch/places_search/adresi_po_poligon_measure_08.09.md:121)

Независимото преизчисление върху същите байтове на полигоните установи:

- **9 255 извън** — точно потвърдени.
- Суровите припокривания са **2 882**. Отчетените 2 483 се възпроизвеждат чрез изключване на **389** случая по `properties.parent` и 10 празни имена. Това е реконструкция: оригиналният скрипт не е намерен.
- Подписаният списък `_meta.parent_child` съдържа **11 родства**, обясняващи **2 043** припокривания; остават **839 между несвързани кодове**, преди проверката за геометрично валидно родство. [fire_varna_locations.py:529](C:/git/varna_3d/src/fire_varna_locations.py:529)
- Метричната лента `max(50, precision_m)` в EPSG:32635 дава **18 840**, срещу отчетените **22 316**. Токенното съгласие се възпроизвежда с разлика от **3 записа**.
- „Топ“ числата не са всички случаи на двойката: **Галата→Боровец-юг е 1 902** еднозначно съдържани точки, не 1 293; **Бриз→Свети Никола — 956**, не 560. [отчетените стойности:131](C:/git/Fire_Varna/scratch/places_search/adresi_po_poligon_measure_08.09.md:131)

Следователно разграничението е:

- **Грешка на думата:** Студентска бл. 11. Останалите **7 531 nearest_point несъгласия** са кандидати, не доказани грешки; low класът има **2 623 несъгласни и 3 649 извън от 10 799**.
- **Различна номенклатура:** **8 214 KAIS несъгласия** изискват разграничение зона/квартал. От отчетените примери **162 Владислав Варненчик→Владиславово** са известен синоним; **771 Розова долина→Аспарухово** са подписано родство. [quarter_registry.json:66](C:/git/Varna_buildings/config/quarter_registry.json:66)
- **Въпрос към границата/понятието:** Галата/Боровец-юг, Бриз/Свети Никола и **1 124 OSM polygon_cover несъгласия**. Подписан полигон сам не доказва кой извор греши.

Точна тройна разбивка засега би била измислена.

| Вариант | Цена на реализацията | Основен риск |
|---|---|---|
| **1. Общ производител** | Висока: мост, етикети, индекси, потребители | Масова промяна изисква пълен проверим диф |
| **2. Само Fire генераторът** | По-ниска: един износител | Една сграда остава с различни квартали между приложенията |
| **3. Временна Fire поправка, после обща** | Най-висока общо: две миграции | Временната логика остава постоянна |

**Препоръчвам вариант 1**, първо като отчет, после като подписана миграция.

Общото правило обработва **всички клъстери**, използва фиксирана версия на границите и отчита произхода/точността на координатата и сградното тяло. Резултатът е квартал/местност по код или изрично „извън“, „ръб“, „спорно“. **9 255 извън остават без измислен квартал.** При припокриване печели само подписано, геометрично проверено родство — не произволно най-малкият полигон. Център и Колхозен пазар **вече имат полигони**; трябва решение за покритието им. Цветен квартал няма отделен полигон. [quarters_signed.geojson:1](C:/git/varna_3d/data/quarters_signed.geojson:1)

KAIS/OSM имената остават частни свидетели с произход/дистанция. Миграцията обхваща **`quarter`, `label` и токените**, иначе старото име се връща през търсенето.

При всеки билд гейтът проверява:

- нула канонични присвоявания от `nearest_point`;
- пълно разпределение на клъстерите, версии/хешове и независимо геометрично съгласие;
- подписани контролни случаи, включително двете Чайки;
- различими блокови етикети чрез улица, без сливане на различни сгради.

Петър подписва новия авторитет чрез ADR, граници/родства/типове, поведението при неизвестност и измерения диф с откат. Нищо не е променяно или изпращано към отдалечено хранилище.
tokens used
100,050
**Проблемът е системен: близост до име и кадастрална зона са превърнати в квартална принадлежност. Препоръчвам обща поправка в производителя на моста, след възпроизводима прекласификация.**

Причината в 10 реда:

1. На **21.05** е добавено OSM допълване за **22 571** клъстера без KAIS квартал; наличните кадастрални имена се запазват. [osm_quarter_integration_plan.md:5](C:/git/Varna_buildings/docs/archive/plans/osm_quarter_integration_plan.md:5)
2. Тогава справочникът е **50 точки и 12 полигона**; днес е 49+12. Точките дават покритие, но не описват граници. [план:21](C:/git/Varna_buildings/docs/archive/plans/osm_quarter_integration_plan.md:21)
3. Логиката е в `tools/build_lookup_map_v2.py`; `build_app_m1_data.py` копира резултата и записва моста. [build_app_m1_data.py:271](C:/git/Varna_buildings/tools/build_app_m1_data.py:271), [същият:1541](C:/git/Varna_buildings/tools/build_app_m1_data.py:1541)
4. Първото непразно KAIS `quarname` печели без пространствена проверка; кадастралната зона така става показван квартал. [build_lookup_map_common.py:626](C:/git/Varna_buildings/tools/build_lookup_map_common.py:626)
5. При липса: съдържащ OSM полигон, иначе най-близка точка; **няма дистанция, след която системата отказва име**. [build_lookup_map_v2.py:999](C:/git/Varna_buildings/tools/build_lookup_map_v2.py:999)
6. Увереността описва предположението, но Fire взема само `quarter.name` за блоковия етикет. Така **707,5 m / low** става категорично „Чайка“. [build_fire_varna_search_index.mjs:536](C:/git/Varna_buildings/js/build_fire_varna_search_index.mjs:536)
7. ADR015 предлага преструктуриране, не пространствена поправка; ADR039 потвърждава неизпълнението и изрично запазва имената. [015:109](C:/git/Varna_buildings/docs/decisions/015_quarter_source_confidence_restructure.md:109), [039:14](C:/git/Varna_buildings/docs/decisions/039_kv_cleanup.md:14), [039:39](C:/git/Varna_buildings/docs/decisions/039_kv_cleanup.md:39)
8. ADR061 разглежда грешни координати; планът от **02.09** за курортите е ограничен до Fire проекцията и неизпълнен. [061:81](C:/git/Varna_buildings/docs/decisions/061_impossible_coordinates.md:81), [plan_quarters_resorts:100](C:/git/Varna_buildings/docs/plans/plan_quarters_resorts_2026-09-02.md:100)
9. Новите **60 подписани полигона** влизат на **07.09, 6486b48**; `05f485e` е последващият отчет. Подписът приема версия на предимно доброволчески, неофициални граници. [build_quarters_signed.py:752](C:/git/varna_3d/src/build_quarters_signed.py:752)
10. Интеграцията им обхваща празните квартали при места/хотели; мостът остава извън нея, а архитектурата още изисква KAIS→OSM. [Fire ADR010:48](C:/git/Fire_Varna/docs/decisions/010_signed_quarter_boundaries.md:48), [architecture_v2.md:489](C:/git/Varna_buildings/docs/architecture_v2.md:489)

**Мярката показва мащаба, но още не дава надежден брой „грешни квартали“.**

Аритметиката е вярна: **31 997 съгласни + 16 869 несъгласни + 9 255 извън + 2 483 припокриване + 10 без име = 60 614**. От несъгласните **8 311** са отчетени в граничната лента. [мярка:121](C:/git/Fire_Varna/scratch/places_search/adresi_po_poligon_measure_08.09.md:121)

Независимото преизчисление върху същите байтове на полигоните установи:

- **9 255 извън** — точно потвърдени.
- Суровите припокривания са **2 882**. Отчетените 2 483 се възпроизвеждат чрез изключване на **389** случая по `properties.parent` и 10 празни имена. Това е реконструкция: оригиналният скрипт не е намерен.
- Подписаният списък `_meta.parent_child` съдържа **11 родства**, обясняващи **2 043** припокривания; остават **839 между несвързани кодове**, преди проверката за геометрично валидно родство. [fire_varna_locations.py:529](C:/git/varna_3d/src/fire_varna_locations.py:529)
- Метричната лента `max(50, precision_m)` в EPSG:32635 дава **18 840**, срещу отчетените **22 316**. Токенното съгласие се възпроизвежда с разлика от **3 записа**.
- „Топ“ числата не са всички случаи на двойката: **Галата→Боровец-юг е 1 902** еднозначно съдържани точки, не 1 293; **Бриз→Свети Никола — 956**, не 560. [отчетените стойности:131](C:/git/Fire_Varna/scratch/places_search/adresi_po_poligon_measure_08.09.md:131)

Следователно разграничението е:

- **Грешка на думата:** Студентска бл. 11. Останалите **7 531 nearest_point несъгласия** са кандидати, не доказани грешки; low класът има **2 623 несъгласни и 3 649 извън от 10 799**.
- **Различна номенклатура:** **8 214 KAIS несъгласия** изискват разграничение зона/квартал. От отчетените примери **162 Владислав Варненчик→Владиславово** са известен синоним; **771 Розова долина→Аспарухово** са подписано родство. [quarter_registry.json:66](C:/git/Varna_buildings/config/quarter_registry.json:66)
- **Въпрос към границата/понятието:** Галата/Боровец-юг, Бриз/Свети Никола и **1 124 OSM polygon_cover несъгласия**. Подписан полигон сам не доказва кой извор греши.

Точна тройна разбивка засега би била измислена.

| Вариант | Цена на реализацията | Основен риск |
|---|---|---|
| **1. Общ производител** | Висока: мост, етикети, индекси, потребители | Масова промяна изисква пълен проверим диф |
| **2. Само Fire генераторът** | По-ниска: един износител | Една сграда остава с различни квартали между приложенията |
| **3. Временна Fire поправка, после обща** | Най-висока общо: две миграции | Временната логика остава постоянна |

**Препоръчвам вариант 1**, първо като отчет, после като подписана миграция.

Общото правило обработва **всички клъстери**, използва фиксирана версия на границите и отчита произхода/точността на координатата и сградното тяло. Резултатът е квартал/местност по код или изрично „извън“, „ръб“, „спорно“. **9 255 извън остават без измислен квартал.** При припокриване печели само подписано, геометрично проверено родство — не произволно най-малкият полигон. Център и Колхозен пазар **вече имат полигони**; трябва решение за покритието им. Цветен квартал няма отделен полигон. [quarters_signed.geojson:1](C:/git/varna_3d/data/quarters_signed.geojson:1)

KAIS/OSM имената остават частни свидетели с произход/дистанция. Миграцията обхваща **`quarter`, `label` и токените**, иначе старото име се връща през търсенето.

При всеки билд гейтът проверява:

- нула канонични присвоявания от `nearest_point`;
- пълно разпределение на клъстерите, версии/хешове и независимо геометрично съгласие;
- подписани контролни случаи, включително двете Чайки;
- различими блокови етикети чрез улица, без сливане на различни сгради.

Петър подписва новия авторитет чрез ADR, граници/родства/типове, поведението при неизвестност и измерения диф с откат. Нищо не е променяно или изпращано към отдалечено хранилище.
