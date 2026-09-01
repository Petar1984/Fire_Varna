# STOP отчет — банер "в процес на разработка" (Fire_Varna, публично)

**Статус:** изпълнено LOKално, комитнато, **НЕ е пушнато**. Чака преглед на Petar + push.
**Комит:** `44321c6` на `main` (parent `299f1ee`), `ahead 1` от `origin/main`.
**Само 1 файл:** `index.html` (+99 / −8). `git show --stat HEAD` = само index.html.

---

## 1. Какво е направено

Дискретен, dismissible банер като **най-горен ред на header-стека** (`<div class="dev-notice">`
преди `.topbar`). Точният текст на Petar:

> ⚠ Системата е в процес на разработка — данните се проверяват и допълват. Не разчитайте единствено на нея.

- **Само UI.** Нула промени по data файлове, флагове, search/geocoder логика. (grep по добавените
  редове: няма `fetch`/`search_index`/`hydrants`/`flag`/`geocoder`/`localStorage` в кода — единствените
  срещания на "localStorage/sessionStorage" са в коментари.)
- **sessionStorage** (ключ `devNoticeDismissed`), НЕ localStorage → пак се показва при нова сесия.
- **Не закрива търсачката/картата.** Банерът бута надолу целия стек; търсачката остава изцяло видима.
- **Калибровка на overlay-ите:** банерът увеличава header-стека, затова всеки top-anchored overlay
  (`.pill`, `.controls`, `.status`, `.placement-banner`, `.prepick-banner`, desktop `.detail-sheet`
  страничен панел + `max-height`) вече чисти стека през `calc(150px + var(--dev-banner-h))` вместо голо
  `150px`. `--dev-banner-h` се **мери от JS** (реалната височина зависи от пренасянето на текста по
  ширина) и става **0 при dismiss** → подредбата след затваряне е идентична на преди банера.
- **Refinements от ревюто** (виж §4): 44px tap-таргет на ✕ (чрез layout-неутрален `::before`, без да
  расте банерът), `role="note"`, pre-paint guard срещу проблясък при reload в същата сесия.

Скрийншоти (untracked, до този отчет):
`scratch/dev_notice_375px.png` (показан, 375px) · `scratch/dev_notice_dismissed_375px.png`
(след затваряне = оригиналната подредба) · `scratch/dev_notice_desktop.png` (1280px, 1 ред).

---

## 2. Dirty tree — какво е паркирано (докладвано, НЕ пипано)

**ВАЖНО разминаване с промпта:** промптът очакваше `index.html` да носи непушнати работни промени
(basemap/E0), които да изолирам чрез `git stash`. **Проверих — `index.html` беше ЧИСТ** (0 staged/unstaged
преди моята работа). Паркираната E0/basemap работа е изцяло в `scratch/`, НЕ в `index.html`. Затова:

- **НЕ направих `git stash`.** Беше излишно (няма чужди hunk-ове в index.html за изолиране) и рисково
  (позната нестабилност на FV диска). Вместо това комитнах с **explicit path** `git add index.html` →
  `git commit -- index.html`, което по конструкция не може да прибере паркираното.
- Ако предпочиташ да бях минал през stash — кажи и ще преработя, но резултатът е същият по-безопасно.

**Паркирано и оставено непокътнато** (проверено `git status` след комита — идентично на преди):

| Файл | Състояние |
|---|---|
| `scratch/basemap_e0/e0_range.json` | modified (5+/31−) — E0 basemap |
| `scratch/basemap_e0/e0_range_report.md` | modified (1+/4−) — E0 basemap |
| `docs/plans/h2_kmz_adapter_plan.md`, `docs/plans/h4_kmz_apply_plan.md` | untracked |
| `verify_apply.py`, `verify_h4.py`, `"python verify_h4.py"` | untracked |
| `scratch/basemap_e0/local_render_probe.html`, `scratch/marker_redesign_frame.md`, `scratch/dev_notice_cc_prompt.md` | untracked |

Нищо от горните не е в комита `44321c6`.

---

## 3. Верификация (реален браузър, Playwright)

Пуснат локален сървър + Chromium на 320 / 375 / 1280px + dismiss flow. **12/12 PASS:**

- 375px: банер = 0–64px; търсачка = 159–197px (не се закрива); контроли @214px (чистят банера);
  `--dev-banner-h` (64px) == реалната височина на банера.
- 320px: същото; без закриване.
- Desktop 1280px: банерът се мери на 41px (текстът се събира на по-малко редове) — JS адаптира.
- Dismiss: банер скрит, `--dev-banner-h`→`0px`, контролите→`150px` (оригинал), `sessionStorage=1`.
- Reload (същата сесия): остава затворен. Нова сесия (нов контекст): банерът се връща.

---

## 4. Adversarial ревю (5 обектива × find→verify, 10 агента)

| Находка | Verify | Действие |
|---|---|---|
| ✕ бутон 26px < 44px comfort target | confirmed→nit | **Поправено** (44px hit-area през `::before`, без ръст на банера) |
| `role="status"` за статичен банер | nit | **Поправено** → `role="note"` |
| FOUC: затворен банер може да проблесне при reload | confirmed→nit | **Поправено** (pre-paint guard след `</header>`) |
| Broad `git add`/`-a` би прибрал паркираното | confirmed low | **Процедура**: explicit `git add index.html` (спазено) |
| Focus пада към `<body>` при dismiss | nit | **Пропуснато** — предложеният fix (focus търсачката) би тригнал lazy-load на search index → риск за търсенето. Оставено, за да е нула-риск. |
| `headerH=150` / `POPUP_AUTOPAN_TL` coupling | partial/nit | **Оставено — виж §5** |

---

## 5. Известен follow-up — РЕШЕНИЕ ЗА PETAR (не е в комита)

Докато **банерът е показан**, две JS константи още приемат header height = `150`:

- `positionPinInBand()` → `const headerH = 150;` (index.html:~4791) — центрира search-pin-а и служи
  като popup-clip guard (`minY = headerH + reserveTop`).
- `const POPUP_AUTOPAN_TL = [16, 150];` (index.html:~3772) — Leaflet popup auto-pan top padding.

И двете под-чистят по-високия header с ~височината на банера (**~64px на мобилно**), затова след
търсене пинът/попъпът може да седне леко нависоко, а попъп близо до горния ръб — частично зад банера.

- **Само козметично.** НУЛА ефект върху резултати/ранкинг/данни/dropdown/storage. (потвърдено от verify)
- **Само в първата сесия**, докато банерът се вижда; при dismiss `--dev-banner-h`→0 и константите пак
  стават точни (150) → без остатъчен ефект.
- Оставено съзнателно **непокътнато**, за да е това banner-only, zero-search-risk комит (спазвам
  "само банер hunk-а" + "нула риск за търсенето" от промпта).

**Готов one-line fix, ако искаш идеалната калибровка** (чете същия var в JS):
```js
// вместо: const headerH = 150;
const headerH = 150 + (parseFloat(getComputedStyle(document.documentElement)
                       .getPropertyValue('--dev-banner-h')) || 0);
// и POPUP_AUTOPAN_TL[1] да се смята при отваряне на попъп: 150 + (същото)
```
Ако одобриш — казвай и ще го добавя като отделен hunk (пак без push).

---

## 6. Следваща стъпка (Petar)

1. Преглед локално: `http://127.0.0.1:8000/Fire_Varna/index.html` (или моите скрийншоти в `scratch/`).
2. Реши §5 (приемаш козметиката / искаш one-line калибровката).
3. Ако е ОК → **ти пушваш** `44321c6` (agent НЕ пуши). Препоръка: pre-push `git fsck` (флаки FV диск).
