# Fire_Varna — карта на пожарните хидранти във Варна

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
- 🚨 **сигнали от терена направо от картата**: повреден/блокиран хидрант,
  грешна локация, нов хидрант, потвърдено състояние. Сигналите се пазят
  и офлайн и се изпращат при връзка; всеки минава през човешка модерация,
  преди да промени данните.
- **Търсачка на адреси** — улици, номера, квартали, блок + вход
  (напр. „бл. 402 вх. 3"), и сурови GPS координати.
- Сателитен изглед (Esri World Imagery) и сграден слой (векторни тайлове).

### Данните

Над **7 000 записа за хидранти** (точните текущи бройки:
[docs/activeContext.md](docs/activeContext.md#current-state)), обединени
и дедуплицирани от:

| източник | какво е |
|---|---|
| **ВиК Варна** | регистърът на водното дружество, по райони |
| **Национален регистър** | държавният набор за цялата страна |
| **ЕТР** | KMZ файлове на районните служби: Варна, Провадия, Долни чифлик, Девня (внесени 06.2026+) |
| **Полеви сигнали** | хидранти, докладвани, потвърдени или поправени на място през 🚨 |

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

### Как се ползва

1. Отвори линка на телефона и разреши достъп до локацията.
2. Меню (⋮ / ⬆️) → **„Добавяне към началния екран"** — ползва се като
   приложение.
3. ⚠️ GPS-ът е несигурен в мазета и тунели — там ползвай 📌 за ръчна
   позиция.

### Архитектура

Статична страница + един малък worker. Без build система, без runtime
зависимости, без акаунти, без следене.

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

### What it does

- Shows your position and the nearest fire hydrants, with three view
  modes: **within 100 m**, **top 5 nearest** (default), **all**.
- 🧭 one tap navigates to the chosen hydrant — Google Maps for longer
  distances, a built-in compass within the last 100 m.
- 🚨 **field reports straight from the map**: broken/blocked hydrant,
  wrong location, new hydrant, condition confirmed. Reports queue
  offline and send when the connection returns; every report passes
  human moderation before it changes the dataset.
- **Address search** — streets, house numbers, quarters, block +
  entrance (e.g. „бл. 402 вх. 3"), plus raw GPS coordinates.
- Satellite imagery toggle (Esri World Imagery) and a building layer
  served as vector tiles.

### The data

Over **7,000 hydrant records** (exact live counts:
[docs/activeContext.md](docs/activeContext.md#current-state)), merged
and deduplicated from:

| source | what it is |
|---|---|
| **ВиК Варна** | the water utility's hydrant registry, by district |
| **National registry** | the country-wide hydrant dataset |
| **ЕТР imports** | district fire-service KMZ files: Varna, Provadia, Dolni Chiflik, Devnya (imported 2026-06+) |
| **Field reports** | hydrants reported, confirmed, or corrected on site via 🚨 |

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

### Usage

1. Open the link on your phone and allow location access.
2. Menu (⋮ / ⬆️) → **"Add to Home Screen"** — works like an app.
3. ⚠️ GPS is unreliable in basements and tunnels — use 📌 to place your
   position manually there.

### Architecture

Static single-page app + one small serverless worker. No build system,
no runtime npm dependencies, no accounts, no tracking.

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
