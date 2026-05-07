# AGENTS.md

> **Canonical current state:** see `docs/activeContext.md` (last updated commit hash and sprint status). If this file conflicts with `activeContext.md`, the latter wins.
>
> Read this **before** making any changes to this repo.
> Project owner: **Petar** - solo developer in Bulgaria, AI-assisted workflow, no formal CS background.
> If anything here conflicts with a user request in chat, raise the conflict; do not silently override.

---

## What This Project Is

Mobile-first **PWA for Varna fire department and a volunteer rescue squad** - locates the nearest fire hydrant via GPS.

- **Primary users:** Varna firefighters (~30-50). Emergency use, on phones, often with gloves.
- **Secondary users:** volunteer rescue squad. Verification and feedback only; **NOT for emergency use.**
- **Distribution:** GitHub Pages from `main`, HTTPS required.
- **Language:** Bulgarian only. No localization layer. UI labels are precise and reviewed by Petar.

The app loads a static hydrant dataset, shows the user's GPS position, and guides them to the nearest hydrant.

---

## Runtime Architecture

Static GitHub Pages frontend. No backend in the repo and no runtime build step.

| Component | Current State | Size |
|---|---|---:|
| App shell | `index.html` with inlined Leaflet, MarkerCluster, CSS, and app logic | 298,207 bytes |
| Hydrant data | `data/hydrants.json`, loaded by `fetch` on app init | 967,530 bytes |
| Report submission | Cloudflare Worker proxy | external |
| Report polling | Cloudflare Worker `GET /issues`, every 15 s | external |
| **Frontend first load** | `index.html` + `data/hydrants.json` | **1,265,737 bytes** |

Hydrant data lives in `data/hydrants.json` (**6,079 records (verified at runtime)**, `vik` + `national` + `field_report` origins). Loaded via fetch on app init. `index.html` contains UI shell, Leaflet, MarkerCluster, app logic, and an empty `<script id="hydrantData">` placeholder populated at runtime.

Local testing requires HTTP, not `file://`:

```powershell
python -m http.server 8000
```

---

## Data Model

`data/hydrants.json` is the runtime dataset. The original KMZ-derived `hydrants_varna.json` remains as a reference/source artifact, not the full runtime dataset.

Runtime compact schema:

```text
{ i, s, a, r, z, t, st, c, o, status? }
```

- `c` is `[lon, lat]` in WGS84 and is always present.
- `o` is the origin: `vik`, `national`, or `field_report`.
- `st` is the source raw status string from source data.
- `status` is app-level visual state and is unrelated to `st`.

App-level `status` values:

| Value | Meaning | Render |
|---|---|---|
| `verified` | Hydrant physically confirmed on-site | Red pin |
| `reported` | Reported damaged / missing / needs attention | Yellow pin |
| absent/unknown | Canonical unverified record | Gray pin |

Older app builds and unknown status values must fall back to canonical/unverified behavior.

### Wrong-Location Ingest Rule

For `wrong_location` reports, **always update the existing record's coordinate field (`c`) in place. Never create a new `field_*` record for `wrong_location`.**

| Target ID type | Action |
|---|---|
| Canonical IDs (`NAT-`, `VIK-`, `877-ZP`, etc.) | update `c` in `data/hydrants.json` only |
| `field_*` IDs | update `c` in **both** `field_reports.json` and `data/hydrants.json` |

After the coord update, set `status` to `"verified"`. Old coords go in the commit message for audit trail. New `field_*` records are created **only** for `new_hydrant` reports.

### National Dataset Role

The national source files are kept as archive/reference only. They are not loaded directly at runtime.

Future option, not implemented: build-time enrichment of runtime data with national metadata only where spatial match is <=5m. Defer until there is concrete user demand.

---

## Report Flow

Reports are submitted via `fetch` POST to Cloudflare Worker `varna-hydrants-proxy.petar-dikov2019.workers.dev`. Worker creates a labeled GitHub issue in this repo. Reports queue locally if offline.

Worker source currently lives only in Cloudflare dashboard. TODO commit 17: extract it to a `worker/` directory in this repo with deploy notes. Until then, treat the live Worker as the canonical source.

---

## Hard Constraints

| Constraint | Reason |
|---|---|
| Static hosting only (GitHub Pages free tier) | Budget = 0 BGN |
| App shell at repo root (`index.html`) plus static `data/hydrants.json` | GitHub Pages serves it |
| First load <= 1 MB ideal, **2 MB hard cap** | Mobile data, emergency use |
| Bulgarian UI labels preserved verbatim | Users speak Bulgarian only; wording is reviewed |
| Mobile-first: touch targets >= 44px, no hover-dependent UX | Field use, gloves, sweat |
| HTTPS-required APIs must work: Geolocation, DeviceOrientation, Worker `fetch` | Core features depend on these |
| **Scope: Varna oblast only** | National scope explicitly out of v1 |
| No new runtime or build-time dependencies without Petar approval | Keep static architecture simple |

---

## Tri-Agent Workflow

| Agent | Role | What it can do | What it cannot do |
|---|---|---|---|
| **Claude (chat)** | Architect / planner / auditor | Discuss, plan, draft, audit | Touch the repo |
| **Codex** | Repo-aware planner | Read files, produce concrete plans, run analyses, execute after explicit handoff | Make architectural decisions silently |
| **Claude Code** | Executor | Implement approved plans, edit files | Make architectural decisions independently |

**Petar = orchestrator.** All architectural and data decisions go through him.

Approval gates:

- **Architecture changes** (file layout, module split, new patterns) -> Claude (chat) discussion first.
- **Data source changes** -> fresh Codex analysis required.
- **UI label / wording changes** -> Petar approval.
- **New runtime or build-time dependencies** -> Petar approval.
- **Refactoring scope** -> Codex plan + Petar approval before edits.

---

## Current Repo State

Loose files, no organized source structure yet.

```text
C:\Projects\Varna_hydrants\
├── index.html                     <- current app shell, 292,281 bytes
├── data/hydrants.json             <- runtime hydrant data, 6,079 records
├── extract_hydrants.py            <- extracts embedded hydrant JSON from older index builds
├── field_reports.json             <- canonical field report state
├── hydrants_varna.json            <- original KMZ-derived reference dataset
├── VARNA_IZTOK.kmz                <- source data
├── VARNA_ZAPAD.kmz
├── DEVNIa.kmz
├── DOLNI_ChIFLIK.kmz
├── PROVADIIa.kmz
├── geo_fire_hydrants.json         <- national archive/reference
├── geo_fire_hydrants.kml          <- same data, KML format
└── wfsrequest.txt                 <- WFS endpoint record
```

No `src/`, `dist/`, `scripts/`, `package.json`, or CI yet.

---

## Implemented Features

All working, tested on mobile.

1. **Auto-start GPS** on page load.
2. **Loading pill** during GPS acquisition; retry/manual controls on failure.
3. **Three view modes**:
   - "Близо <100м" - hydrants within 100m radius
   - "Топ 5" - default, 5 nearest by Haversine
   - "Всички" - full clustered overlay of all 6,079 records (verified at runtime)
4. **Bottom sheet** - compact card always visible; list expands from handle.
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
- **Auto-fit only twice:** on first GPS lock and on mode change.
- **No service worker yet.** Tiles are fetched live from OSM.
- `index.html` now depends on `data/hydrants.json`; serve over HTTP locally so fetch works.

---

## Known Tech Debt

1. **HTML has accumulated patches.** `updateCard()` rebuilds full HTML on every refresh and rewires buttons after `innerHTML`.
2. **No build system.** Diffs are hard to read. Refactoring is post-launch.
3. **Data is static JSON.** Updating hydrants requires regenerating/reviewing `data/hydrants.json`.
4. **Worker source not yet in repo.** Live Worker is canonical until commit 17 extracts it.
5. **No offline tile cache.** App fails where live OSM tiles cannot load.
6. **No PWA manifest.**
7. **No tests, no CI.**
8. **Bulgarian-only UI.** No localization layer.

---

## Windows Dev Environment

Defender exclusions applied (2026-05-06):

- ExclusionPath: `C:\Projects\Varna_hydrants`, `C:\Users\Petar\Desktop\Fire_Varna_deploy2`
- ExclusionProcess: `git.exe`, `git-remote-https.exe`, `node.exe`

Primary workflow: edit + commit + push from `C:\Projects\Varna_hydrants` directly. Deploy clone `Fire_Varna_deploy2` is deprecated post-fix.

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
- A planned change would push the build past the 2 MB hard cap.
- You are about to introduce a runtime or build-time dependency.
- You are about to change Bulgarian UI text.
- You do not have an approved plan and the task is non-trivial.

When in doubt, ask. Petar would rather review a question than revert a commit.
