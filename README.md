# Fire_Varna — карта на пожарните хидранти във Варна

> Сверка 02.09.2026 (комит bc18d54): числата в този документ носят собствената си дата на измерване; каквото е остаряло към 02.09.2026 е отбелязано с ⚠ под реда.

**[Български](#български)** · **[English](#english)**

🔗 **<https://petar1984.github.io/Fire_Varna/>**

---

## Български

> Mobile-first PWA, което показва на пожарникаря най-близкия работещ
> пожарен хидрант във Варненска област — в браузъра, без инсталация,
> без акаунт.

### Какво прави

- Показва позицията ти и най-близките хидранти, в три режима:
  **до 100 м**, **топ 5 най-близки** (по подразбиране), **всички**.
- 🧭 един tap води до избрания хидрант — Google Maps при по-голямо
  разстояние, вграден компас в последните 100 м.
> ⚠ остаряло към 02.09.2026: buildNavActions дава 4 външни линка: Waze, Google Maps walking, Google карта, Street View. NEAR_THRESHOLD_M се ползва само на ред 2169 за режим „Близо" (измерено 01.09.2026, приложение Е) — `sed -n '4205,4210p' index.html; grep -n 'NEAR_THRESHOLD_M' index.html`
- 🚨 **сигнали от терена направо от картата**: повреден/блокиран хидрант,
  грешна локация, нов хидрант, потвърдено състояние. Сигналите се пазят
  и офлайн и се изпращат при връзка; всеки минава през човешка модерация,
  преди да промени данните.
> ⚠ остаряло към 02.09.2026: data-type="damaged" · data-type="exists_confirmed" · data-type="missing" · data-type="new_hydrant" · data-type="wrong_location" — `grep -o 'data-type="[a-z_]*"' index.html | sort -u`
- **Търсачка на адреси** — улици, номера, квартали, блок + вход
  (напр. „бл. 402 вх. 3"), и сурови GPS координати.
- **Хотели в търсачката** — 225 места за настаняване от Националния
  туристически регистър (име, вид, категория, легла, зона);
  „хотел адмирал“ намира и трите.
> ✓ вярно към 04.09.2026: 225 · 3 — `PYTHONIOENCODING=utf-8 python -c "import json;d=json.load(open('data/hotels.json',encoding='utf-8'));print(d['_meta']['count'], sum(1 for h in d['hotels'] if 'мирал' in h['name'].lower()))"`
- Сателитен изглед (Esri World Imagery) и сграден слой (векторни тайлове).

### Данните

Над **7 000 записа за хидранти** (точните текущи бройки:
[docs/activeContext.md](docs/activeContext.md#current-state)), обединени
и дедуплицирани от:
> ✓ вярно към 02.09.2026 (след ЛОТ 5 на плана от 01.09): [docs/activeContext.md § Current State](docs/activeContext.md#current-state) носи броя записи с командата до него — 7403 — `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"`; до 02.09.2026 същият път сочеше хрониката от 2026-07-04 (7,238 записа), сега замразена в [docs/archive/activeContext_2026-07-04.md](docs/archive/activeContext_2026-07-04.md).

> ⚠ остаряло към 02.09.2026: [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 147), ('pozarna_gz', 99), ('etr_devnya', 78)] — `python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"`

| източник | какво е |
|---|---|
| **ВиК Варна** | регистърът на водното дружество, по райони |
| **Национален регистър** | държавният набор за цялата страна |
| **ЕТР** | KMZ файлове на районните служби: Варна, Провадия, Долни чифлик, Девня (внесени 06.2026+) |
| **Полеви сигнали** | хидранти, докладвани, потвърдени или поправени на място през 🚨 |
| **Национален туристически регистър** | местата за настаняване (хотели) — отделни факти, атрибуция в попъпа |
| **OpenStreetMap** | имената на училищата, университетите, болниците и детските градини — © OpenStreetMap contributors, ODbL 1.0 |
| **Регистри (МОН/НЕИСПУО, ИАМН, Община Варна)** | регистровите имена на училищата, детските заведения и лечебните заведения — отделни факти, източникът на всеки ред стои в `src` |
| **Wikidata** | разгърнатите имена на три училища/висши училища като ПСЕВДОНИМИ ЗА ТЪРСЕНЕ (Q7035695, Q12291800, Q12299161) — CC0 1.0 Universal, снапшот с дата на достъп 03.09.2026 |

Координатите са WGS84. Рядката метаданна (тип, адрес, състояние) остава
точно толкова рядка, колкото е в източниците — нищо не се измисля. Всяка
приложена промяна е в [docs/moderation_log.md](docs/moderation_log.md),
провенансът на всеки запис се архивира — наборът е одитируем докрай.

Търсачните файлове (`data/search_index.json`, `data/address_rows.json`)
се строят в **отделен конвейер**
([Varna_buildings](https://github.com/Petar1984/Varna_buildings)) от
отворените данни на кадастъра и минават гейтове за поверителност и
цялост преди публикуване — без кадастрални идентификатори, без лични
данни.

#### Хотели

Местата за настаняване в търсачката идват от **Националния туристически
регистър** — отделни факти, без масово копиране на регистъра.
Координатите: собствена геолокация върху отворените данни на КАИС.
Имената от публична идентификация (OSM, официални сайтове, общински
регистри) също са отделни факти; източникът на всеки ред стои в `src` и
се показва в попъпа му.

Лицензният ред на доставката (`data/hotels.json`, `_meta.licence`),
дословно:

> Имената и регистровите данни: отделни факти от Националния туристически регистър (чл. 4 ЗАПСП; без масово копиране на регистъра). Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md). Старите имена: кадастрални адресни полета + публични източници, всяко с ред в присъдния документ на З1 (22.08.2026). Имената от публична идентификация (OSM, официални сайтове, общински регистри): отделни факти, а не извадка от база — източникът на всеки ред стои в `src` (цикълът „дупката“, 23.08.2026).

Вторият лицензен ред на същата доставка (`_meta.licence_osm`) покрива един
разгърнат псевдоним за търсене от OpenStreetMap, дословно:

> Разгърнати имена (псевдоними за търсене) от OpenStreetMap: „© OpenStreetMap contributors, ODbL“ — лиценз ODbL 1.0, снапшот 2026-08-10. Днес е един такъв псевдоним (way 199237000); изворът на всеки псевдоним стои в `old_names_src`.

В търсачката са и училищата, университетите, болниците, ДКЦ, хосписите и детските градини (броят и sha — в docs/activeContext.md): имената идват от OpenStreetMap (© OpenStreetMap contributors, ODbL 1.0) и от регистрите, посочени в реда-източник на всеки попъп.

Двата лицензни реда на доставката (`data/places.json`, `_meta.licence_osm` и
`_meta.licence_registry`), дословно:

> Имената от OpenStreetMap: „имена на обекти © OpenStreetMap contributors, ODbL“ — дословната атрибуция на web/varna_poi_names.json; лиценз ODbL 1.0. Самият пакет е производна база (систематична извадка) и се публикува под ODbL 1.0 — share-alike. Показването на един ред в попъп е Produced Work и за него атрибуцията стига (К8).

> Имената и регистровите данни: отделни факти от регистрите (чл. 4 ЗАПСП; без масово копиране на регистър) — Регистър на лечебните заведения (ИАМН), Регистър на училищата и детските заведения (Община Варна), Регистър на училищата (МОН/НЕИСПУО, одобрено 21.08); източникът на всеки ред стои в `src`. Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md).

Третият лицензен ред (`_meta.licence_wikidata`) е за новия извор на ЛОТ 1в:
разгърнатите имена, които влизат САМО като псевдоними за търсене — не като
показвано име. Дословно:

> Разгърнати имена (псевдоними за търсене) на 3 места: Wikidata Q7035695, Q12291800, Q12299161, CC0 1.0 Universal, достъп 03.09.2026. Низовете са зафиксирани с датата на достъп (снапшотът), не се теглят живо; изворът на всеки псевдоним стои в `old_names_src`.

Хотелите не са част от офлайн пакета (sw.js): без връзка търсачката на
места не работи.

Същото важи за `data/places.json` и за речника `data/place_categories.json`
— и те не са част от офлайн пакета (sw.js).

Кварталните псевдоними в `data/place_categories.json` (`zones`) са дословни
низове от собствения регистър на кварталите
(`Varna_buildings/config/quarter_registry.json`) — ред за проследимост, не
лиценз.

### Как се ползва

1. Отвори линка на телефона и разреши достъп до локацията.
2. Меню (⋮ / ⬆️) → **„Добавяне към началния екран"** — ползва се като
   приложение.
3. ⚠️ GPS-ът е несигурен в мазета и тунели — там ползвай 📌 за ръчна
   позиция.

### Архитектура

Статична страница + един малък worker. Без build система, без runtime
зависимости, без акаунти, без следене.
> ⚠ остаряло към 02.09.2026: 4132:  const VECTORGRID_CDN = 'https://unpkg.com/leaflet.vectorgrid@1.3.0/dist/Leaflet.VectorGrid.bundled.min.js'; · 4397:      s.src = VECTORGRID_CDN; — `grep -n 'VECTORGRID_CDN' index.html; grep -noiE 'gtag|google-analytics|plausible|matomo|sentry' index.html; ls -1 | grep -iE 'package|webpack|vite|rollup'`

- **Frontend** — един `index.html` (Leaflet 1.9.4 + MarkerCluster,
  ванилен JS/CSS) на GitHub Pages; `data/hydrants.json` се тегли при
  старт.
- **Cloudflare Worker** — приема сигналите (стават GitHub issues за
  модерация), връща одобрените към картата, и сервира сградните тайлове
  от R2 с токен.
- **Основа** — OpenStreetMap; Esri World Imagery при превключване.

Локално: `python -m http.server 8000` → <http://localhost:8000>
(`file://` не работи — данните се теглят с `fetch`; GPS иска HTTPS).

### Управление

Проектът се разработва с AI агенти под строг човешки контрол:
**Planner** (само чете) мери и планира; **Executor** изпълнява подписан
план с локални коммити; **никой от тях никога не пушва**. **Петър**
подписва всеки план, преглежда всеки диф и единствен пушва и разгръща.
Виж [docs/decisions/003_dual_claude_code_governance.md](docs/decisions/003_dual_claude_code_governance.md),
[AGENTS.md](./AGENTS.md) и [CLAUDE.md](./CLAUDE.md).

### Лиценз

Лицензът на кода **още не е избран** — дотогава: всички права запазени.
Наборът с хидрантите смесва публични източници с полева верификация —
питай, преди да го преизползваш.

### Благодарности

- **Пожарна служба Варна** — обратна връзка от терена
- **Доброволният отряд на гр. Варна** — тестване и верификация на място

За технически въпроси — [отвори issue](../../issues).

---

## English

> A mobile-first PWA that shows firefighters the nearest working fire
> hydrant in the Varna region, Bulgaria — in the browser, no
> installation, no account.

> ⚠ остаряло към 02.09.2026: 0 · 4507:  const BASEMAP_PMTILES_ENABLED = false; — `grep -c 'rel="manifest"' index.html; git ls-files | grep -i webmanifest; grep -n 'BASEMAP_PMTILES_ENABLED = ' index.html`

### What it does

- Shows your position and the nearest fire hydrants, with three view
  modes: **within 100 m**, **top 5 nearest** (default), **all**.
- 🧭 one tap navigates to the chosen hydrant — Google Maps for longer
  distances, a built-in compass within the last 100 m.
> ⚠ остаряло към 02.09.2026: четири линка (Waze / Google Maps walking / Google map / Street View); NEAR_THRESHOLD_M се ползва само за филтъра на режим „Близо" (измерено 01.09.2026, приложение Е) — `sed -n '4205,4210p' index.html; grep -n 'NEAR_THRESHOLD_M' index.html`
- 🚨 **field reports straight from the map**: broken/blocked hydrant,
  wrong location, new hydrant, condition confirmed. Reports queue
  offline and send when the connection returns; every report passes
  human moderation before it changes the dataset.
> ⚠ остаряло към 02.09.2026: data-type="damaged" · data-type="exists_confirmed" · data-type="missing" · data-type="new_hydrant" · data-type="wrong_location" — `grep -o 'data-type="[a-z_]*"' index.html | sort -u`
- **Address search** — streets, house numbers, quarters, block +
  entrance (e.g. „бл. 402 вх. 3"), plus raw GPS coordinates.
- **Hotels in the search** — 225 accommodation places from the National
  Tourist Register (name, kind, category, beds, zone); „хотел адмирал“
  finds all three.
> ✓ вярно към 04.09.2026: 225 · 3 — `PYTHONIOENCODING=utf-8 python -c "import json;d=json.load(open('data/hotels.json',encoding='utf-8'));print(d['_meta']['count'], sum(1 for h in d['hotels'] if 'мирал' in h['name'].lower()))"`
- Satellite imagery toggle (Esri World Imagery) and a building layer
  served as vector tiles.

### The data

Over **7,000 hydrant records** (exact live counts:
[docs/activeContext.md](docs/activeContext.md#current-state)), merged
and deduplicated from:
> ✓ вярно към 02.09.2026 (след ЛОТ 5 на плана от 01.09): същото като по-горе — новата входна точка носи 7403 с командата `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/hydrants.json',encoding='utf-8'))))"`; хрониката от 2026-07-04 (7,238 записа) е в [docs/archive/activeContext_2026-07-04.md](docs/archive/activeContext_2026-07-04.md).

> ⚠ остаряло към 02.09.2026: [('vik', 3524), ('national', 2329), ('etr_varna', 763), ('etr_provadia', 244), ('etr_dolni_chiflik', 219), ('field_report', 147), ('pozarna_gz', 99), ('etr_devnya', 78)] — `python -c "import json,collections;print(collections.Counter(x.get('origin') for x in json.load(open('data/hydrants.json',encoding='utf-8'))).most_common())"`

| source | what it is |
|---|---|
| **ВиК Варна** | the water utility's hydrant registry, by district |
| **National registry** | the country-wide hydrant dataset |
| **ЕТР imports** | district fire-service KMZ files: Varna, Provadia, Dolni Chiflik, Devnya (imported 2026-06+) |
| **Field reports** | hydrants reported, confirmed, or corrected on site via 🚨 |
| **National Tourist Register** | accommodation places (hotels) — separate facts, attribution in the popup |
| **OpenStreetMap** | the names of the schools, universities, hospitals and kindergartens — © OpenStreetMap contributors, ODbL 1.0 |
| **Registers (МОН/НЕИСПУО, ИАМН, Община Варна)** | the registry names of the schools, childcare and health establishments — separate facts, the source of every row sits in `src` |
| **Wikidata** | the expanded names of three schools/higher schools as SEARCH ALIASES (Q7035695, Q12291800, Q12299161) — CC0 1.0 Universal, snapshot accessed 2026-09-03 |

Coordinates are WGS84. Sparse metadata (type, address, operational
status) stays exactly as sparse as the sources are — nothing is
invented. Every applied change is tracked in
[docs/moderation_log.md](docs/moderation_log.md) and per-record
provenance is archived, so the dataset is fully auditable.

The address-search payloads (`data/search_index.json`,
`data/address_rows.json`) are **built in a separate pipeline**
([Varna_buildings](https://github.com/Petar1984/Varna_buildings)) from
the national cadastre's open data, and pass privacy and integrity gates
before publishing — no cadastral identifiers, no personal data.

#### Hotels

The accommodation places in the search come from the **National Tourist
Register** — separate facts, no bulk copying of the register. The
coordinates are our own geolocation over the КАИС open data. The names
taken from public identification (OSM, official websites, municipal
registers) are separate facts too; the source of every row sits in `src`
and is shown in its popup.

The delivery's licence line (`data/hotels.json`, `_meta.licence`),
verbatim (in Bulgarian, as published):

> Имената и регистровите данни: отделни факти от Националния туристически регистър (чл. 4 ЗАПСП; без масово копиране на регистъра). Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md). Старите имена: кадастрални адресни полета + публични източници, всяко с ред в присъдния документ на З1 (22.08.2026). Имената от публична идентификация (OSM, официални сайтове, общински регистри): отделни факти, а не извадка от база — източникът на всеки ред стои в `src` (цикълът „дупката“, 23.08.2026).

The same delivery's second licence line (`_meta.licence_osm`) covers one
expanded search alias taken from OpenStreetMap, verbatim (in Bulgarian, as
published):

> Разгърнати имена (псевдоними за търсене) от OpenStreetMap: „© OpenStreetMap contributors, ODbL“ — лиценз ODbL 1.0, снапшот 2026-08-10. Днес е един такъв псевдоним (way 199237000); изворът на всеки псевдоним стои в `old_names_src`.

The search also carries the schools, universities, hospitals, ДКЦ (diagnostic and consultation centres), hospices and kindergartens (the count and the sha — in docs/activeContext.md): the names come from OpenStreetMap (© OpenStreetMap contributors, ODbL 1.0) and from the registers named in the source row of every popup.

The delivery's two licence lines (`data/places.json`, `_meta.licence_osm` and
`_meta.licence_registry`), verbatim (in Bulgarian, as published):

> Имената от OpenStreetMap: „имена на обекти © OpenStreetMap contributors, ODbL“ — дословната атрибуция на web/varna_poi_names.json; лиценз ODbL 1.0. Самият пакет е производна база (систематична извадка) и се публикува под ODbL 1.0 — share-alike. Показването на един ред в попъп е Produced Work и за него атрибуцията стига (К8).

> Имената и регистровите данни: отделни факти от регистрите (чл. 4 ЗАПСП; без масово копиране на регистър) — Регистър на лечебните заведения (ИАМН), Регистър на училищата и детските заведения (Община Варна), Регистър на училищата (МОН/НЕИСПУО, одобрено 21.08); източникът на всеки ред стои в `src`. Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md).

The third licence line (`_meta.licence_wikidata`) is ЛОТ 1в's new source: the
expanded names enter as SEARCH ALIASES only — never as a displayed name.
Verbatim (in Bulgarian, as published):

> Разгърнати имена (псевдоними за търсене) на 3 места: Wikidata Q7035695, Q12291800, Q12299161, CC0 1.0 Universal, достъп 03.09.2026. Низовете са зафиксирани с датата на достъп (снапшотът), не се теглят живо; изворът на всеки псевдоним стои в `old_names_src`.

The hotels bundle is not part of the offline pack (sw.js): without a
connection the places search does not work.

The same holds for `data/places.json` and for the `data/place_categories.json`
dictionary — neither is part of the offline pack (sw.js) either.

The quarter aliases in `data/place_categories.json` (`zones`) are verbatim
strings from our own quarter registry
(`Varna_buildings/config/quarter_registry.json`) — a traceability line, not a
licence.

### Usage

1. Open the link on your phone and allow location access.
2. Menu (⋮ / ⬆️) → **"Add to Home Screen"** — works like an app.
3. ⚠️ GPS is unreliable in basements and tunnels — use 📌 to place your
   position manually there.

### Architecture

Static single-page app + one small serverless worker. No build system,
no runtime npm dependencies, no accounts, no tracking.
> ⚠ остаряло към 02.09.2026: 4132:  const VECTORGRID_CDN = 'https://unpkg.com/leaflet.vectorgrid@1.3.0/dist/Leaflet.VectorGrid.bundled.min.js'; · 4397:      s.src = VECTORGRID_CDN; — `grep -n 'VECTORGRID_CDN' index.html; grep -noiE 'gtag|google-analytics|plausible|matomo|sentry' index.html`

- **Frontend** — one `index.html` (Leaflet 1.9.4 + MarkerCluster,
  vanilla JS/CSS) on GitHub Pages; `data/hydrants.json` fetched at
  startup.
- **Cloudflare Worker** — receives field reports (turned into GitHub
  issues for moderation), polls applied issues back to the map, and
  serves token-gated building vector tiles from R2.
- **Basemap** — OpenStreetMap tiles; Esri World Imagery on toggle.

Local dev: `python -m http.server 8000` → <http://localhost:8000>
(`file://` won't work — data is fetched; geolocation needs HTTPS).

### Governance

Developed with AI agents under strict human control: a **Planner**
(read-only) measures and drafts plans; an **Executor** implements a
signed plan with local commits; **neither ever pushes**. **Petar** signs
every plan, reviews every diff, and is the only one who pushes or
deploys. See
[docs/decisions/003_dual_claude_code_governance.md](docs/decisions/003_dual_claude_code_governance.md),
[AGENTS.md](./AGENTS.md) and [CLAUDE.md](./CLAUDE.md).

### License

Code license is **not chosen yet** — until then: all rights reserved.
The hydrant dataset combines public-sector sources with field
verification; ask before reusing it.

### Acknowledgements

- **Varna Fire Service** — field feedback
- **Varna volunteer rescue team** — testing and on-site verification

For technical questions — [open an issue](../../issues).
