# AGENTS.md

> Read this **before** making any changes to this repo.
> Project owner: **Petar** — solo developer in Bulgaria, AI-assisted workflow, no formal CS background.
> If anything here conflicts with a user request in chat, raise the conflict — do not silently override.

---

## What this project is

Mobile-first **PWA for Varna fire department and a volunteer rescue squad** — locates the nearest fire hydrant via GPS.

- **Primary users:** Varna firefighters (~30–50). Emergency use, on phones, often with gloves.
- **Secondary users:** Volunteer rescue squad (Viber group). Verification and feedback only — **NOT for emergency use.**
- **Distribution:** GitHub Pages (free static hosting, HTTPS required for Geolocation API).
- **Language:** Bulgarian only. No localization layer. UI labels are precise and reviewed by Petar.

The app loads a static hydrant dataset, shows the user's GPS position, and guides them to the nearest hydrant.

---

## Stack

Single self-contained HTML file. Everything inlined.

| Component | Library | Size |
|---|---|---:|
| Map | Leaflet 1.9.4 | ~147 KB |
| Clustering | MarkerCluster 1.5.3 | ~34 KB |
| Hydrant data | Inline JSON | ~430 KB |
| App logic + CSS | Vanilla JS / CSS | ~60 KB |
| **Total** | | **~672 KB** |

No build system at runtime. No backend. No npm packages at runtime. No external CDN dependencies (everything inlined).

---

## Canonical dataset (decided)

**Source: regional KMZ files from ВиК Варна (the local water utility).**
Parsed file: `hydrants_varna.json` — **3,934 records, 433 KB**.

### Why this and not the national GeoJSON

Codex compared `hydrants_varna.json` against `geo_fire_hydrants.json` (national, ~17,962 records). Findings:

| Metric | Result |
|---|---|
| KMZ → local JSON parse loss | 0 (per-region counts match exactly) |
| National points inside Varna bbox | 2,366 (vs 3,934 local — **40% fewer**) |
| Local records matching any national within 25m | **10.7%** |
| Local records with no national counterpart within 25m | **89.3%** |
| National records with mixed/invalid EPSG:3857 coordinates | 428 |

The national dataset is **less complete and less reliable** for the Varna scope. It is owned by a fire-safety aggregator, not the maintainer of the hydrants.

### Compact JSON schema

```
{ i, s, a, r, z, t, st, c }
  │  │  │  │  │  │  │  └── [lon, lat]   (WGS84, always present)
  │  │  │  │  │  │  └───── status        (mostly empty)
  │  │  │  │  │  └──────── type          (mostly empty)
  │  │  │  │  └─────────── notes         (mostly empty)
  │  │  │  └────────────── district      (mostly empty)
  │  │  └───────────────── address       (~16% populated)
  │  └──────────────────── region        (one of 5 KMZ regions)
  └─────────────────────── id
```

Coordinates are 100% present. Other metadata fields are sparse — do not rely on them.

### Optional `status` field (added Sprint 1)

Records may carry an additional optional field `status` representing app-level visual state:

| Value | Meaning | Render |
|---|---|---|
| `verified` | Hydrant physically confirmed on-site by a volunteer/firefighter | SVG hydrant icon |
| `reported` | Reported as damaged / missing / needs attention | Yellow numbered pin |
| _absent_ | Canonical record from KMZ, not yet field-verified | Red numbered pin (default) |

**Forward-compatible.** Additional values may be added later. Older app builds and unknown values fall back to canonical (default) render — absence of the field is the canonical state.

**`status` is unrelated to `st`.** The compact `st` field above is the **source raw status string** from the original KMZ (mostly empty, e.g. operational/decommissioned tags from ВиК). `status` is **app-level visual state** added at field-verification time. They are not renamed, merged, or interchangeable.

`status` lives in `field_reports.json` and the embedded `hydrantData` JSON inside `index.html`. It is **not** added to `hydrants_varna.json` (canonical dataset stays clean — see § Canonical dataset rule).

### National dataset role

Kept in repo as **archive / reference only**. Not loaded at runtime.

Future option (not implemented): build-time enrichment of `hydrants_varna.json` with national `notes`/`name`/`status` fields **only** where spatial match is ≤5m. Defer until there is concrete user demand.

---

## Hard constraints (do not violate)

| Constraint | Reason |
|---|---|
| Static hosting only (GitHub Pages free tier) | Budget = 0 лв |
| Single deployable artifact at repo root (currently `index.html`) | GitHub Pages serves it |
| First load ≤ 1 MB ideal, **2 MB hard cap** | Mobile data, emergency use |
| Bulgarian UI labels preserved verbatim | Users speak Bulgarian only; wording is reviewed |
| Mobile-first: touch targets ≥ 44px, no hover-dependent UX | Field use, gloves, sweat |
| HTTPS-required APIs must work: Geolocation, DeviceOrientation, Web Share | Core features depend on these |
| **Scope: Varna oblast only** | National scope explicitly out of v1 |
| No new runtime dependencies without Petar approval | Single-file architecture |

---

## Tri-agent workflow

| Agent | Role | What it can do | What it cannot do |
|---|---|---|---|
| **Claude (chat)** | Architect / planner / auditor | Discuss, plan, draft, audit | Touch the repo |
| **Codex** | Repo-aware planner | Read files, produce concrete plans, run read-only analyses | Modify code without an explicit, separate execution handoff |
| **Claude Code** | Executor | Implement approved plans, edit files | Make architectural decisions independently |

**Petar = orchestrator.** All architectural and data decisions go through him. He reviews Codex plans before approving execution and reviews Claude Code output before commit.

### Approval gates

- **Architecture changes** (file layout, module split, new patterns) → Claude (chat) discussion first.
- **Data source changes** → fresh Codex analysis required.
- **UI label / wording changes** → Petar approval (Bulgarian wording is sensitive).
- **New runtime or build-time dependencies** → Petar approval.
- **Refactoring scope** → Codex plan + Petar approval before Claude Code edits files.

---

## Current repo state

**Loose files, no organized structure yet.** Refactoring is planned but not started.

```
C:\Projects\Varna_hydrants\
├── hydrants_varna (7).html        ← current app, ~672 KB, all features inlined
├── hydrants_varna.json            ← canonical dataset (3,934 records)
├── VARNA_IZTOK.kmz                ← source data
├── VARNA_ZAPAD.kmz
├── DEVNIa.kmz
├── DOLNI_ChIFLIK.kmz
├── PROVADIIa.kmz
├── geo_fire_hydrants.json         ← national archive (reference only)
├── geo_fire_hydrants.kml          ← same data, KML format
├── geo_fire_hydrants.zip          ← same data, shapefile
└── wfsrequest.txt                 ← record of the WFS endpoint the national export came from
```

**No** `src/`, `dist/`, `scripts/`, `data/`, `package.json`, `.gitignore` yet.

A future refactoring task will introduce a proper structure. Until then, do not assume any of those paths exist.

---

## Implemented features

All working, tested on mobile.

1. **Auto-start GPS** on page load (no splash screen, no button press).
2. **Loading pill** during GPS acquisition; switches to error pill with retry / manual buttons on failure.
3. **Three view modes** (chips at bottom of sheet):
   - "Близо <100м" — only hydrants within 100m radius
   - "Топ 5" (default) — 5 nearest by Haversine
   - "Всички" — full clustered overlay of all 3,934
4. **Bottom sheet** — compact card always visible (active target arrow, distance, name, nav/report buttons); list expands on tap of the handle.
5. **Compass arrow + heading cone** on user marker. User dot has translucent cone showing phone heading; bottom card has small directional arrow pointing at active target.
6. **Hybrid navigation** (🧭 button): distance > 100m opens Google Maps (driving); ≤ 100m switches in-app compass target and zooms.
7. **Follow mode** (📍 button): centers on user, auto-recenters on GPS updates. User pan exits follow mode.
8. **Manual position mode** (📌 button): next map click sets user position manually. For indoor / no-GPS use.
9. **Report modal** (🚨 button): physical-state categories (`ВИДИМ_ОК`, `ИЗКРИВЕН`, `ПОВРЕДЕН`, `БЛОКИРАН`, `ЗАРАСЪЛ`, `ЛИПСВАЩ`, `ГРЕШЕН_АДРЕС`) + free text → `navigator.share()` → user picks channel (Viber/Telegram/SMS).

---

## Implementation gotchas (learned the hard way)

- **`deviceorientation` fires at 100–200Hz on Android.** Don't EMA on every event — it over-converges and provides no smoothing. Solution: store latest raw heading, run EMA once per `requestAnimationFrame` (60Hz cap). `HEADING_SMOOTHING = 0.10`.
- **Use `L.divIcon` for all markers**, never `L.icon`. `L.icon` requires external marker images that fail in self-contained builds.
- **MarkerCluster is only used in "Всички" mode.** "Близо" and "Топ" render plain numbered pins — clustering adds no value for small sets.
- **Auto-fit only twice:** on first GPS lock and on mode change. Never on routine GPS updates (jarring).
- **No service worker yet.** Tiles are fetched live from OSM. Offline tile cache is the highest-priority gap for actual emergency use.

---

## Known tech debt

1. **HTML has accumulated patches.** Rewritten cleanly twice, then patched 4–5 more times. Duplicated CSS, `updateCard()` rebuilds full HTML on every refresh, button wiring after `innerHTML` assignment.
2. **No build system.** Diffs are hard to read. Refactoring is the next major task.
3. **Data hardcoded inline.** Updating hydrants requires regenerating the entire HTML.
4. **Reports go to user-picked channel.** No central collection. Volunteer reports scatter across Viber/Telegram/SMS.
5. **No offline tile cache.** App fails in basements, tunnels, large concrete buildings — exactly where firefighters need it.
6. **No PWA manifest.** "Add to Home Screen" works but it's not a real PWA install.
7. **No tests, no CI.** Acceptable at current size.
8. **Bulgarian-only UI.** No localization layer (acceptable for v1).

---

## Glossary (Bulgarian terms in code/UI)

| Bulgarian | English |
|---|---|
| Хидрант | Hydrant |
| Близо | Near |
| Всички | All |
| Точки | Points (markers) |
| Сигнал | Signal / report |
| ВиК | Water utility (Водоснабдяване и Канализация) |
| Район | District |
| Подрайон | Sub-district |
| Подател | Sender |
| ГДПБЗН | Fire safety / civil protection directorate (national) |
| Спешност | Urgency (removed from form, term kept here for reference) |

---

## When you (the agent) should stop and ask

- The user requests a change that contradicts a hard constraint above.
- The user requests a change to the canonical dataset.
- A planned change would push the build past the 2 MB hard cap.
- You are about to introduce a runtime or build-time dependency.
- You are about to change Bulgarian UI text.
- You don't have an approved Codex plan and the task is non-trivial.

When in doubt, ask. Petar would rather review a question than revert a commit.
