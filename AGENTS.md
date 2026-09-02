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

**Live numbers live in the entry point, not here.** No state number enters this file: record counts, per-origin counts, file counts, byte sizes and commit hashes belong in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state). What stays here are numbers that are rules — hard caps, intervals, thresholds (§ Hard Constraints) — and pointers into configuration, such as the Worker deploy version in § Report Flow. A figure that carries a `непроверено` marker has no measurable source in this repo; never quote it as state.

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
| Canonical IDs (every id is `coord_<lon>_<lat>` today; `NAT-`, `VIK-`, `GZ-` survive in `legacy_ids`) | update `coords` in `data/hydrants.json` |
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
│                                     test_apply_approved_reports_parity.py, golden fixtures)
├── worker/                        <- Cloudflare Worker source + README (deploy version 5accc88e)
├── extract_hydrants.py            <- extracts embedded hydrant JSON from older index builds
├── verify_apply.py                <- one-off checker for an apply run (hydrants + provenance)
├── verify_h4.py                   <- one-off checker for the H4 ЕТР KMZ apply (reads the flag queue)
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
- **A service worker exists (`sw.js`) but is off by default.** `index.html` registers it only when the PMTiles basemap capability is active, and the committed flag `BASEMAP_PMTILES_ENABLED` is `false` — so by default (no `?basemap_pmtiles=1` opt-in stored on the device) tiles on the live site are still fetched live from OSM.
- `index.html` now depends on `data/hydrants.json`; serve over HTTP locally so fetch works.

---

## Known Tech Debt

1. **HTML has accumulated patches.** `updateCard()` rebuilds full HTML on every refresh and rewires buttons after `innerHTML`.
2. **No build system.** Diffs are hard to read. Refactoring is post-launch.
3. **Data is static JSON.** Updating hydrants requires regenerating/reviewing `data/hydrants.json`.
4. **Worker source lives in `worker/`** (extracted in `914dc2a`); Cloudflare deploy is manual, deploy version repo-declared `5accc88e`.
5. **The offline tile cache exists but is off by default.** `sw.js` and the PMTiles basemap release under `data/basemaps/` are both in the repo; the committed flag `BASEMAP_PMTILES_ENABLED` is `false`, and only a per-device opt-in (`?basemap_pmtiles=1`, `index.html` line 4504) registers them — without it the app still fails where live OSM tiles cannot load.
6. **No PWA manifest.**
7. **Tests exist (`tests/`, Python unittest); there is no CI — confirmed absent (no `.github/`, no other CI configuration in the repo).**
8. **Bulgarian-only UI.** No localization layer.

---

## Windows Dev Environment

Defender exclusions applied (2026-05-06):

- ExclusionPath: `C:\git\Fire_Varna`
- ExclusionProcess: `git.exe`, `git-remote-https.exe`, `node.exe`

Primary workflow: agents edit + commit locally in the canonical working directory `C:\git\Fire_Varna`; **Petar alone pushes** after reviewing the diff (Gate 2). The deploy clone `Fire_Varna_deploy2` no longer exists on disk; `C:\git\Fire_Varna` is the only working copy.

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
