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

| Component | Current State |
|---|---|
| App shell | `index.html` with inlined Leaflet, MarkerCluster, CSS, and app logic |
| Hydrant data | `data/hydrants.json`, loaded by `fetch` on app init |
| Report submission | Cloudflare Worker proxy |
| Report polling | Cloudflare Worker `GET /issues`, every 15 s |
| **Frontend first load** | `index.html` + `data/hydrants.json` |

Hydrant data lives in `data/hydrants.json` (**5,911 records**, `vik` + `national` + `field_report` origins). Loaded via fetch on app init. `index.html` contains UI shell, Leaflet, MarkerCluster, app logic, and an empty `<script id="hydrantData">` placeholder populated at runtime.

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
  report_id?, reported_at? }
```

- `coords` is `[lon, lat]` in WGS84 and is always present.
- `origin` is `vik`, `national`, or `field_report` and is always present.
- `legacy_ids` is the array of a record's prior IDs (used for polling dedupe); always present.
- `type`, `region`, `address` are sparse descriptive fields.
- Visual / moderation state is split across three sparse fields, not one app-level `status`:

| Field | Observed values | Meaning / render |
|---|---|---|
| `existence_status` | `verified` | Hydrant physically confirmed on-site (red pin) |
| `review_status` | `reported` | Reported damaged / missing / needs attention (yellow pin) |
| `operational_status` | `works`, `not_working`, `not_tested` | Operational state, independent of existence |
| (all three absent) | — | Canonical unverified record (gray pin) |

Older app builds and unknown values must fall back to canonical/unverified behavior. `report_id` / `reported_at` carry field-report provenance.

### Wrong-Location Ingest Rule

For `wrong_location` reports, **always update the existing record's coordinate field (`coords`) in place. Never create a new `field_*` record for `wrong_location`.**

| Target ID type | Action |
|---|---|
| Canonical IDs (`NAT-`, `VIK-`, `877-ZP`, etc.) | update `coords` in `data/hydrants.json` |
| `field_*` IDs | update `coords` in `data/hydrants.json` |

`field_reports.json` is no longer a current file; all records (including `field_*`) live in `data/hydrants.json` only. After the coord update, set `existence_status` to `"verified"`. Old coords go in the commit message for audit trail. New `field_*` records are created **only** for `new_hydrant` reports.

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

### Codex Plan Preamble Checklist

Every Codex plan/proposal must include: request scope, deterministic inventory, files read, negative-findings matrix, quoted declared metadata, decision ledger, approval-gate check, and open questions.

Decision ledger schema:

| Decision | Source | Evidence | Reversibility | Approval status |
|---|---|---|---|---|
| Worker source extracted to `worker/` (`914dc2a`) | Repo evidence | `worker/` holds the Worker source + README; deploy version repo-declared `5accc88e` | Reversible by reverting the extraction commit | Existing approved project state |

---

## Codex Operating Protocol

### Scope Declaration

Codex may use a task-scoped inventory when the user request is narrow. The preamble must declare the inventory scope and cite the user request or brief that defines it. Files outside the declared scope may not be referenced unless Codex explicitly expands the scope, explains why, and updates the inventory.
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

Working directory: `C:\git\Fire_Varna`. Organized source structure (tracked top-level):

```text
C:\git\Fire_Varna\
├── index.html                     <- current app shell
├── data/                          <- runtime hydrant data (hydrants.json, 5,911 records;
│                                     hydrants_provenance.json)
├── scripts/                       <- ingest / migration / backfill tooling
│   ├── apply_approved_reports.py
│   ├── migrate_to_verbose_schema.py
│   ├── backfill_addresses_20260511.py / backfill_verified_type_20260509.py
│   ├── replay_historical_new_hydrant.py
│   └── lib/hydrant_core.py        <- H1 shared core (spatial dedup)
├── tests/                         <- unittest suite (test_hydrant_core.py,
│                                     test_apply_approved_reports_parity.py, golden fixtures)
├── worker/                        <- Cloudflare Worker source + README (deploy version 5accc88e)
├── extract_hydrants.py            <- extracts embedded hydrant JSON from older index builds
├── hydrants_varna.json            <- original KMZ-derived reference dataset
├── audit/                         <- historical audit snapshots / plans
└── docs/                          <- activeContext, plans, audits, architecture roadmap
```

`field_reports.json` is no longer present (records merged into `data/hydrants.json`). `scripts/`, `tests/`, and `worker/` now exist; CI is still absent/unconfirmed.

---

## Implemented Features

All working, tested on mobile.

1. **Auto-start GPS** on page load.
2. **Loading pill** during GPS acquisition; retry/manual controls on failure.
3. **Three view modes**:
   - "Близо <100м" - hydrants within 100m radius
   - "Топ 5" - default, 5 nearest by Haversine
   - "Всички" - full clustered overlay of all 5,911 records
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
4. **Worker source lives in `worker/`** (extracted in `914dc2a`); Cloudflare deploy is manual, deploy version repo-declared `5accc88e`.
5. **No offline tile cache.** App fails where live OSM tiles cannot load.
6. **No PWA manifest.**
7. **Tests exist (`tests/`, Python unittest); CI is absent/unconfirmed.**
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
