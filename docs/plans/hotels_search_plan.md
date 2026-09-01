# Plan — Hotels as a new result class in the address search

**File:** `docs/plans/hotels_search_plan.md` · **Date:** 2026-08-22 · **Status:** DRAFT — AWAITING PETAR SIGNATURE (Gate 1)
**Author:** Planner (read-only recon: 5 Opus readers + Fable synthesis, cross-checked against 4 independent earlier reports; zero contradictions).
**Origin:** Petar's brief of 22.08.2026 — the varna_3d hotels delivery (`ПЛАН_хотели.md` step Х5, dublet investigation З1 closed 22.08) enters the live-map search. **Requirement №1: no regression — the live map only gains, nothing existing changes.** Universities/landmarks are checked separately (annex, not in this cycle's commits).

---

## 1. Risk classification — 🔴 Architectural (escalation-dominant; rounded up)

| Trigger | Fired? | Evidence |
|---|---|---|
| ADR / architecture / schema / new external source | **YES** | New search result class (precedent: ADR 001 required an ADR for `kind:"approx"`); new non-cadastral data source in the repo → **ADR 006** ships with this plan |
| Committed data / data transform | **YES** | New file `data/hotels.json` under `data/**` |
| Multi-file in one subsystem | **YES** | `index.html` + `data/` + `tests/` + `README.md` |
| Non-trivial logic that would not fail loudly | YES | A matcher bug degrades silently → dedicated fail-loud probes (G3/G4) |
| UI wording change | **YES** | New Bulgarian strings — Petar picks exact wordings at Gate 1 (§11) |

**Topology: Variant A.** Planner (this doc) → **GATE 1 (Petar signs)** → Executor (Opus, separate agent, local commits) → Auditor (Opus, adversarial) → **GATE 2 (Petar reviews diff)** → Petar pushes. Agents never push.

## 2. Request scope

Add the 144 hotel places to the live-map search: findable by current name **and old name** („синчец" → ДАНА ПАЛАС), former hotels visibly marked „бивш", result click behaves like an address hit (anchor + marker + popup + nav), the `_meta.licence` line reproduced **verbatim** in README/attribution. Everything else on the map is untouchable. The input file is a **one-shot delivery**: future changes are regenerated in varna_3d (`src/export_fire_varna_hotels.py`) and re-copied; it is never hand-edited here.

## 3. Deterministic inventory + files read

**In scope (writes):** `data/hotels.json` (new), `index.html`, `tests/test_hotels_public_bundle.py` (new), `README.md`, `docs/decisions/006_hotels_in_search.md` (new), this plan.
**Read this cycle (recon, all cited in the reports under the session scratchpad `opus_recon/`):** `AGENTS.md`; `CLAUDE.md`; `index.html` (search IIFE 4780–6181: norm/skel 4786-4788, matchKindSet 4792, runGeocoderSearch 5100-5261, hitChip 5327-5332, appendExactHeader 5336-5352, renderResults 5368-5384, searchPinIcon 5413-5415, openSearchPopup 5416-5430, selectResult 5796-5822, approx block 5859-6070, renderCombined 6090-6102, resolveAndRender 6110-6128, listeners 6144-6180; attribution 1837-1862, 4507-4513; accommodation styles 4140/4148); `sw.js` (44-76, 190-202); `data/search_index.json` + `data/generation_manifest.json` (parsed, incl. the uncommitted ADR-063 republish diff); `docs/activeContext.md`; `docs/plans/*` (8), `docs/decisions/*` (5), `tests/*` (8), `scratch/BOARD.md`, `scratch/additive_features_frame.md`; varna_3d (read-only): `data/fire_varna_hotels.json` (full), `src/export_fire_varna_hotels.py`, `src/qa_fire_varna_export.py`, `ПЛАН_хотели.md`, `ФАЗА_0_лицензи.md`, `AGENTS.md`.

**Pre-existing dirty worktree (NOT ours, untouched):** ` M data/search_index.json`, ` M data/generation_manifest.json` (ADR-063 entrance-reattribution republish from Varna_buildings, awaiting Petar's own Gate 2), ` M AGENTS.md` (Output-budget section), scratch files. The Executor stages **explicit paths only**; `git status --short` must show these exactly as found.

## 4. Measured baseline (Planner, 22.08.2026) + negative findings

**The delivery** `C:\git\varna_3d\data\fire_varna_hotels.json`, generated 2026-08-22 10:05:52:

| Measure | Value |
|---|---|
| bytes / sha256 | **48,052** / `d9312d272a2afb701e162f8073050fc2160d0b52eedfe0320da7bb5b3941aad6` |
| gzip -9 (mtime=0) | 5,500 |
| entries / `_meta.count` | **144 / 144** (consistent) |
| kinds | `Хотел` 122 · `Семеен хотел` 19 · `комплекс` 3 |
| zones (10, named) | к.к. Златни пясъци 68 · к.к. Чайка 24 · район Одесос 18 · Манастирски рид 12 · к.к. Св. Константин 8 · Аспарухово/Галата 5 · Виница/север 4 · район Приморски 3 · Морска градина 1 · район Младост 1 |
| `old_names` | 7 entries, 1 synonym each (Акация→ГЛАДИОЛА, Морско око→НОА, Морска звезда→ВИСТАМАР, Синчец→ДАНА ПАЛАС, Копривщица→ВИВА КЛУБ, LTI Берлин ГБ→БЕРЛИН ГОЛДЪН БИЙЧ, Арабела блок С→АРАБЕЛА) |
| `status` | exactly 1 non-empty: `Русалка` (к.к. Св. Константин) = `"бивш"` |
| `src` | `НТР УИН` 122 · `КАИС адресно поле` 22 (the 22 carry name+coords only) |
| coordinates | named scalars `lat`/`lon` (no order ambiguity); 144/144 inside 43.00–43.45 / 27.60–28.15; measured lat 43.134567–43.300517, lon 27.877311–28.049085 |
| cadastral identifiers | **0** (regex `\b\d{4,5}\.\d+\.\d+`, `10135`, `кадаст` in data — all 0; the one `кадастрални` hit is prose inside `_meta.licence`) |
| mojibake | 0; strict UTF-8, no `\u` escapes; the only >U+2000 chars are „ “ in the name `„Виктория“` |

**Fire_Varna search today (relevant to non-regression):** the search consumes `data/search_index.json` (11,242,756 B worktree, 86,232 entries, kinds `address`/`mf`/`parcel` only) + `data/address_rows.json`, both built **cross-repo in Varna_buildings**, lazy-loaded on first focus. Result classes (chips): `адрес`, `сграда`, `вход`, `парцел`, synthetic `GPS`, dark `прибл. адрес` (`APPROX_ADDRESS_SEARCH_ENABLED = false`). Click = `anchorHydrantsAt` (re-ranks hydrants around the point, moves the blue dot) + one `searchMarker` + `setView(…, max(zoom,17))` + popup/detail sheet. `index.html` = 475,446 B; first load = `index.html` + `data/hydrants.json` only (lazy payloads exempt by definition, AGENTS.md:34).

**Negative findings matrix:**

| Searched for | Scope | Result |
|---|---|---|
| `хотел` / POI / places concept | `index.html`, docs/, tests/ | **absent** — only the building-layer `accommodation`/'Настаняване' style (index.html:4140/4148); hotels would be the first non-cadastral result class |
| hotels in `search_index.json` | payload parse | absent (kinds: address/mf/parcel) |
| address field / „Хан Омуртаг" | delivery file | **absent** — no address key exists; the two `РОЯЛ` entries are distinguished by zone (район Одесос 28 beds vs к.к. Златни пясъци 442 beds), not by street |
| zone values „курорт/град/квартал" | delivery file | absent — 10 named zones instead (brief's vocabulary corrected) |
| generator of search payloads | Fire_Varna scripts/ | absent — lives in Varna_buildings ⇒ hotels **cannot** enter `search_index.json` without a cross-repo change (forbidden here) |
| per-source attribution surface | `index.html` | absent — attribution is basemap-only today |
| test reading `index.html` behavior | tests/ | absent — unittest suite is non-regression only; behavioral proof needs a live probe (G3/G4) |

## 5. Chosen design

**Hotels = a new, self-contained result class, modeled on the ADR-001 (approx) pattern — additive and isolated; the address pipeline stays byte-identical in behavior.**

- **D1 — Payload.** `data/hotels.json` = **byte-identical copy** of the delivery (sha256 pinned above). Committed once; never edited here; future deliveries = regenerate in varna_3d → re-copy → new plan/commit. Lazy fetch on first search focus via its own `fetchHotelsJson` into its **own Cache API namespace `fire-varna-hotels-v1`** (approx precedent), independent of the address payloads and **fail-soft**: if it fails to load or validate, address search works exactly as today.
- **D2 — Runtime validation, fail-closed to absence.** On load: top-level keys `{_meta, hotels}`; `_meta.count === hotels.length === 144`; every entry has the 11 known keys; every coordinate inside bbox 43.00–43.45 / 27.60–28.15; forbidden-token scan (cadnum regex) over the raw text. Any violation ⇒ hotels disabled for the session (approx `approxDisabled` precedent), console error, addresses unaffected.
- **D3 — Matching.** Client-side over 144 entries (no inverted index needed). Tokens built at load from `name` + `old_names` + `zone` + `kind`, folded through the **existing** `norm()`+`skel()` (untouched) with a hotel-only pre-step: strip `„ “ ” "` and collapse double spaces (handles `„Виктория“`, `ХОТЕЛ  ХЕЛИОС СПА`). Match per query token: exact > prefix > capped-Levenshtein fuzzy (reusing `matchKindSet`'s constants); **all query tokens must match one entry** (approx precedent). Ranking: current-name match > old-name match; active > `бивш`; more exact > prefix > fuzzy; fewer tokens; file order. Zone tokens make „адмирал златни" vs „адмирал манастирски" unambiguous; kind tokens make „семеен" find the 19 family hotels.
- **D4 — Rendering.** Hotel rows appended **below** the exact address rows (ADR 001 D7 precedent) as one contiguous block, introduced by their own **group header** (reuses the existing `asr-group-header` class — the visible grouping Petar asked for on 22.08: hotels are never interleaved with address rows); shared `RESULT_LIMIT = 10`, new chip class `хотел`. Row shows the zone (necessary: two `РОЯЛ`, two `Адмирал`, two `ПЕРЛА`, two `Русалка` differ only by zone — distinct hotels km apart, not dublets) and the old name / „бивш" marker per the signed wording (§11). One hotel = one row = one pin: the delivery is 1:1 post-З1 (merged registrations, e.g. ДАНА ПАЛАС = one entry with two УИН); we never emit per-registration or per-building rows. Implementation: a **new** render function; `renderResults`/`renderCombined` stay byte-identical; `resolveAndRender` gets a minimal branch — **when zero hotel hits, the code path is exactly today's**.
- **D5 — Selection.** Reuses the address behavior verbatim: `anchorHydrantsAt(lat, lon)` (hydrants re-rank around the hotel — the operational payoff), the **same `searchMarker` slot** (so every existing cleanup path — Escape, empty query, next selection — works with zero new wiring) with a distinct hotel icon (orange `#f97316`, matching the building layer's 'Настаняване'), `setView(…, max(zoom,17))`, popup = name (+бивш) / kind ★cat · beds · zone / **per-record source line** (D7) / `buildNavActions` (Кола·Пеша·Карта·Street View). No building-detail sheet (hotels carry no `g`).
- **D6 — Flag.** `HOTELS_SEARCH_ENABLED` in the core next to the other two flags; **committed `true`** (recommendation — the gates run before Petar pushes; the flag remains the kill-switch). Petar may flip the recommendation at Gate 1.
- **D7 — Attribution (Условие 2 + the licence line).** (a) README (BG + EN mirrors): new source row + a „Хотели" subsection carrying the `_meta.licence` line **verbatim, byte-identical, in Bulgarian in both mirrors**; (b) popup per-record source line per the varna_3d `SRC_LABEL` precedent: `НТР УИН` → „Национален туристически регистър", `КАИС адресно поле` → „КАИС адресно поле (АГКК)", plus the coordinates credit „координати: КАИС Отворени данни (АГКК)". **No named licence is claimed** (ФАЗА_0: АГКК has not named one — we must not either).
- **D8 — Bundle test.** `tests/test_hotels_public_bundle.py` modeled on `test_approx_addresses_public_bundle.py`: sha256/bytes/gzip9 pins, count 144, schema allow-list (11 keys exactly), kind/src/status enums, bbox, forbidden tokens, **licence line byte-equal**, mojibake 0.
- **D9 — Untouched, by name:** `data/search_index.json`, `data/address_rows.json`, `data/hydrants.json`, `data/approx_addresses_v1.json`, `sw.js` (SW is unregistered in production; adding `fire-varna-hotels-v1` to `PROTECTED_CACHES` is logged as an obligation of the separate SW-lifecycle cycle — ADR 005/`sw_cache_lifecycle_fixes.md`), `worker/`, both existing flags, all hydrant modes/report flows, the camera outside the existing selection behavior.

**Decision ledger**

| Decision | Source | Evidence | Reversibility | Approval |
|---|---|---|---|---|
| Hotels as a new result class, NOT tokens in `search_index.json` | Planner | index is built in Varna_buildings (README:47-52, index.html:4760-66); cross-repo edits forbidden (CLAUDE.md guardrail 5); hotels carry non-address metadata (beds/cat/status/synonyms) that tokens cannot render | full: revert C2–C5 | **Pending Gate 1** |
| ADR-001 pattern (own file, own cache ns, own matcher, flag, fail-soft) | Repo precedent | ADR 001 D1–D9; approx block index.html:5859-6070 | same | Pending Gate 1 |
| Hotels always append below exact rows (not gated on `exactComplete` like approx) | Planner | approx rows are alternative *addresses* (redundant when exact exists); hotels are a different entity class — hiding БЕРЛИН behind an exact street hit would defeat the feature | same | Pending Gate 1 |
| One-shot delivery, byte-identical copy, regenerate upstream | Petar 22.08 + varna_3d | export script docstring: „нищо във Fire_Varna не се пипа от това репо"; brief: „не го редактирай на ръка" | n/a | Given |
| Licence line verbatim in README + per-record source in popup | Petar 22.08 + ФАЗА_0 Условие 2 | `qa_fire_varna_export.py` check 8 („ДОСЛОВНО"); `SRC_LABEL` precedent varna_3d web/index.html:3095-3103 | revert C5 | Given (wording via §11) |

**Rejected alternatives:** (1) *hotel names as `alias_tk` tokens on building rows* (quarters precedent) — requires the Varna_buildings builder, loses chip/beds/status/synonym display, and hotels aren't existing rows; (2) *merging into `search_index.json` locally* — hand-editing a generated cross-repo artifact, breaks its determinism/manifest; (3) *hotels as map markers/layer* — Petar's standing decision „Картата НЕ се пипа — всичко е само в търсачните данни" (BOARD.md:40); (4) *eager load* — 48 KB is small but first-load discipline and the lazy precedent cost nothing.

## 6. Commits (exact messages; staged with explicit paths; one logical change each)

- **C1** — `docs/plans/hotels_search_plan.md` (this, signed) + `docs/decisions/006_hotels_in_search.md` (ADR: D1–D9 above in ADR house format)
  `plan: hotels-in-search cycle — signed plan + ADR 006`
- **C2** — `data/hotels.json`
  `data(search): publish the hotels bundle from varna_3d (144 places, one-shot delivery)` — body names: generator `varna_3d/src/export_fire_varna_hotels.py`, generated 2026-08-22 10:05:52, З1 dublet investigation closed 22.08, sha256 `d9312d2…`, byte-identical copy, 0 cadastral identifiers, licence line inside `_meta`.
- **C3** — `tests/test_hotels_public_bundle.py`
  `test: SHA-pinned public-bundle gate for data/hotels.json` — body records the deliberately-broken-once proof (G2).
- **C4** — `index.html`
  `feat(search): hotels as a new result class in the address search` — body: additive/isolated claim, flag state, capability list (name/old-name/zone/kind matching, бивш marker, per-record source line, nav actions, hydrant re-anchor), G3 probe verdict, byte growth, „first load unchanged".
- **C5** — `README.md`
  `docs: hotels source + verbatim licence line in README (BG+EN)`

## 7. Gates — all machine-checkable; a failed gate STOPS and asks Petar (never „fix forward")

| # | Gate | Command / check | Pass |
|---|---|---|---|
| G0 | Baseline before any edit | `git rev-parse HEAD`; `(Get-Item index.html).Length`; `(Get-Item README.md).Length`; mojibake scan (G7 form) on `index.html`+`README.md`; `python -m unittest discover -s tests` (record test count); `git status --short -uall` snapshot | all recorded; suite green; scan 0; pre-existing dirt catalogued — else STOP |
| G1 | Payload identity | `Get-FileHash data\hotels.json -Algorithm SHA256` | `= d9312d272a2afb701e162f8073050fc2160d0b52eedfe0320da7bb5b3941aad6`; 48,052 bytes |
| G2 | Bundle gate runs AND falls | `python -m unittest tests.test_hotels_public_bundle` green; then once against a deliberately corrupted copy (flip one byte in a coordinate) → must go RED; restore, green again | both outcomes observed and recorded (проверка, която е ТИЧАЛА и е ПАДАЛА) |
| G3 | Address-search non-regression probe | `scratch/probe_hotels_fv.mjs` (playwright, precedent `probe_geo_fv.mjs`): fixed query set — „бл. 402 вх. 3", „макгахан 15", a quarter query, a GPS paste, „Няма съвпадения" nonsense query — serialized dropdown rows (labels+chips+order) **byte-identical before/after C4**; address click still: anchor + teal pin + zoom≥17 + popup/sheet | 0 diffs on every address case; console 0 errors |
| G4 | Hotel probes (the signed sample + synonyms) | same probe: (a) „берлин голдън бийч" → БЕРЛИН ГОЛДЪН БИЙЧ (not ГРИЙН ПАРК); (b) „парк хотел голдън бийч"; (c) „адмирал" → **two** rows distinguished by zone, „адмирал златни" → one; (d) „роял" → two rows (Одесос / Златни); (e) „вива клуб"; (f) „бел епок" (Семеен хотел, Одесос); synonyms: „синчец"→ДАНА ПАЛАС, „копривщица"→ВИВА КЛУБ, „морско око"→НОА, „морска звезда"→ВИСТАМАР, „лти"→БЕРЛИН ГОЛДЪН БИЙЧ; „русалка"→ two rows, Св. Константин one marked „бивш"; „виктория" finds `„Виктория“`; click on a hotel: orange pin, zoom≥17, popup shows name/kind/★/beds/zone/source line/nav actions, hydrants re-ranked around it, Escape clears everything | every case exact; console 0 errors |
| G5 | Confined, bounded diff | `git diff --numstat -- index.html` | insertions ≤ 300, deletions ≤ 6; all hunks inside the search IIFE + search CSS block; byte growth `(Get-Item index.html).Length − G0` ≤ **12,000 B** |
| G6 | First load unchanged | statement + `data/hotels.json` fetched only on focus (probe asserts no hotels request before focus) | first load = `index.html` + `data/hydrants.json`, byte-equal to G0 |
| G7 | Encoding | `Select-String -Path index.html,README.md,data\hotels.json -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8` | 0 matches |
| G8 | Suite non-regression | `python -m unittest discover -s tests` | green; count = G0 count + new tests |
| G9 | Licence line verbatim | `Select-String -Path README.md -Pattern 'отделни факти от Националния туристически регистър' -Encoding UTF8`; byte-compare the full line against `data/hotels.json` `_meta.licence` | present in BG and EN sections, byte-identical to `_meta.licence` |
| G10 | Clean staging | `git status --short -uall` after each commit | only the commit's named files changed vs G0 snapshot; pre-existing dirt untouched |
| G11 | 375px manual (CLAUDE.md § Verification) | `python -m http.server 8000`, 375px | full checklist incl. all 3 hydrant modes, report flow, follow mode — unchanged; hotel rows readable; touch targets ≥ 44px |

## 8. Rollback

Every commit is independently revertable; the feature entire = `git revert C4` (flag+code additive), data = `git revert C2`. No flag flip, no schema change, no push, no deploy anywhere in the cycle.

## 9. Approval-gate check

Architecture change → ADR 006 (C1). Data source change → this fresh Planner analysis. UI wording → §11 signatures. New dependency → **none** (no library, no build step). Push/deploy → none (Petar alone).

## 10. STOP conditions (Executor)

G0 red baseline; any G-gate red; the delivery file at `C:\git\varna_3d\data\fire_varna_hotels.json` no longer hashes `d9312d2…` at copy time (a newer regeneration exists → back to Petar); any temptation to edit hotels data, touch D9's untouchables, alter address ranking, or invent a Bulgarian string not signed in §11; unexpected worktree state beyond the G0 catalogue.

## 11. Open questions for Gate 1 (Petar picks / signs)

1. **Flag:** committed `true` from C4 (recommended — gates run before your push; flag stays as kill-switch), or `false` + separate signed flip?
2. **Chip wording:** W1 `хотел` (recommended — one chip for all three kinds; exact kind shows in the popup) / W2 per-kind chips (`хотел`/`семеен`/`комплекс`). **Group header wording:** W1 `Хотели` (recommended) / W2 `Места за настаняване` / your wording: ____
3. **Old-name display (always shown when present):** W1 `ДАНА ПАЛАС · старо: Синчец` (recommended) / W2 `ДАНА ПАЛАС (бивш „Синчец")` / your wording: ____
4. **Former marker:** W1 suffix `· бивш` in the row + `(бивш)` in the popup title (recommended) / W2 dedicated chip style.
5. **Popup source line:** W1 `име: Национален туристически регистър · координати: КАИС Отворени данни (АГКК)` (recommended; for the 22 КАИС-name rows: `име: КАИС адресно поле (АГКК) · …`) / your wording: ____
6. **README subsection text** — Executor drafts from D7, you approve at Gate 2 with the diff (licence line itself is fixed verbatim, not draftable).
7. **Data notes back to varna_3d (Т2/дублети, not this repo):** ГОЛДЪН ЛАЙН/`Явор` share byte-identical coordinates (likely one building, candidate 8th synonym); `Арабела блок С` is a block designator, not a true former name; `ХОТЕЛ  ХЕЛИОС СПА` double space. Forward?
8. **ФАЗА_0_лицензи.md** still shows „⏳ чака подпис" with unchecked boxes, while the licence line cites its conditions. Confirm it's considered signed (or sign it there) before this cycle publishes the citation.
9. **АГКК retroactive attribution** for the *existing* cadastre-derived surfaces (search payloads, building tiles) — separate future cycle? (This cycle credits АГКК on the hotel surfaces only.)

## 12. Planner notes to the Executor

Reuse the `searchMarker` variable slot for the hotel pin — every cleanup path then works untouched. Do not modify `norm`/`skel`/`matchKindSet`/`runGeocoderSearch`/`renderResults`/`renderCombined`/`selectResult` — new functions only, plus the minimal `resolveAndRender` branch. Build the probe before C4 and run it against G0 first (baseline capture). `data/hotels.json` goes in **no** `sw.js` list this cycle (D9). The dropdown builds with `textContent` only — keep it that way for hotel rows. Bulgarian UI strings byte-exact from §11; commit messages English.

---

## 13. Annex — universities & landmarks readiness (checked 22.08.2026, read-only recon in varna_3d; facts only, no commits here)

Measured against the hotels-delivery standard (dublet investigation · licence line · export gate):

- **Забележителности — PARTIAL.** 145 places live in the varna_3d canon (`data/places.json`, WGS84, per-record `name_src`, 0 cadastral ids), but: the dublet verdict doc is explicitly „спецификация, чака реда си" with two unresolved dublets standing in the canon („Св. Архангел Михаил" ×2, „Летен театър" ×2 — invisible to `qa_places.py`, which only judges dublets within one building); the licence is **ODbL (OSM)**, and ФАЗА_0 §В3 + `ПОДГОТОВКА_адреси.md:524-537` record the share-alike question for external publication as a known, consciously open hole; `data/places.json` `_meta` carries **no licence line** to copy; the export script excludes them by name (`vn-man-*`, `vn-osm-*`); 13 „без сграда" entries await Petar's decision.
- **Университети — ABSENT as places.** 0 entries in `places.json`; only 20 raw rows in `web/varna_poi_names.json` (chip `университет`) with live defects: ВУМ/ВУМ-double on one building, „Институт по океанология при БАН" and „Морска гимназия" mislabeled as университет, duplicated building rows; no board file, no dublet investigation at all; and the single live cadastral identifier in tracked varna_3d code sits precisely in the university rule У6 (`build_poi_names.py:122`, allow-listed, „чака решение на Петър").
- **No export path exists for either** — `export_fire_varna_hotels.py` is hotels-only by construction (prefix filter + `len(rows) < 140` threshold) and by its own docstring.

**Consequence:** this cycle ships hotels only. The D1–D9 mechanism is deliberately category-agnostic — a future clean delivery (e.g. `data/landmarks.json`) plugs into the same pattern with its own plan/signature. Universities/landmarks first need their own varna_3d cycles: dublet verdicts applied, an ODbL-for-external-publication decision, a university board. Those are varna_3d work, out of scope here.

---

**Signature line (to be filled by Petar):** `SIGNED: ______________  date: __________  Q1: __  Q2: W__  Q3: W__  Q4: W__  Q5: W__  Q7: __  Q8: __`
