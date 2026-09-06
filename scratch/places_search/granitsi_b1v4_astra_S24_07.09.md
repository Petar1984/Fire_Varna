Reading additional input from stdin...
OpenAI Codex v0.153.3
--------
workdir: C:\git
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: ultra
reasoning summaries: none
session id: 01a078a1-fb89-7383-acf0-6a9909444492
--------
user
S24 — FINAL REVIEW (lens MECHANICS) of lot Б1 artefact before Petar commits it. Repos read-only: C:/git/varna_3d (branch rezhimi; commits since your S23: e2da307 'build+gates: district resolutions input (decision 9) — Кочмар and Възраждане 4 → Младост, QA accepts only AU5-consistent resolutions'; earlier 6dde0a5, 7fb0e92 applied your S23 F2/F3) and C:/git/Fire_Varna (commits 3d747d3 decisions 4 + attribution → blob 74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b; e6c706d scratch/places_search/district_resolutions_2026-09-07.json = decision 9). STAGED uncommitted: varna_3d/data/quarters_signed.geojson sha256 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3, 301 917 B, 60 Features. Per-lot auditor: ГОДНО with minors (the 'ours' field of a resolved dispute is not re-verified against our layer; counts.features_with_our_district semantics changed silently; the resolutions signed sha is hardcoded in the QA). Verify: (1) your S23 F1–F3 are closed (chain: decisions 4 final blob pinned as _meta.decisions_sha256; union recipe text corrected with library versions and the two negatives; independent AU5 witness with signed crosswalk, the 2 disputes resolved by Petar with AU5-consistent resolutions only); run the QA gate (python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna) and python -m unittest tests.test_quarters_signed_fixtures (write access to the fixtures folder may be needed — if you cannot, say so) with exit codes; (2) the three auditor minors — which must be fixed BEFORE the commit and which can wait; (3) the exact commit for Petar: message text, and the byte/sha check he should run before committing (git cat-file blob :data/quarters_signed.geojson | sha256sum vs the staged sha); (4) any remaining hard-limit or provenance issue (no push; registry untouched; decisions 4 blob signed by Petar by sha — what exact sentence should he write to sign it). Verdict ГОДНО/НЕГОДНО for committing the artefact now; at most 900 words; Bulgarian with English identifiers; cite file:line and shas.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя staged blob-а, provenance веригата и затварянето на F1–F3, ще изпълня двата gate-а и ще дам присъда за commit. Работя read-only; ще отделя независим преглед на трите auditor minors.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -LiteralPath C:/git/Varna_buildings/scratch/hydrant_map_integration_frame.md' in C:\git
 succeeded in 0ms:
# Hydrant Map Integration â€” Framing / Handoff (Phase 2 Reintegration)

**Status:** Framing draft (chat-Claude). Input for a new architecture cycle.
**Date:** 2026-06-21

This document is the handoff for integrating the hydrant app with the
buildings pipeline. It is the gated "Phase 2 reintegration" that
`docs/architecture_v2.md` deferred (requires an ADR 020 amendment). Start
the new Cowork session by reading this + both repos, then run the cycle.

---

## 1. Purpose

A firefighter searches an address â†’ finds the nearest hydrants; sees all
hydrants for field verification; the owner adds/edits hydrants, building
annotations, and the verification design **without touching core code**.
Mobile-first is the primary purpose.

## 2. The two repos

- **Varna_buildings** (PRIVATE, Python) â€” KAIS address/building pipeline +
  map app. Holds raw KAIS, intel, personal-data-sensitive material.
- **Fire_Varna** (PUBLIC, HTML/PWA) â€” "Ð¥Ð¸Ð´Ñ€Ð°Ð½Ñ‚Ð¸ Ð’Ð°Ñ€Ð½Ð°", GitHub Pages at
  `https://petar1984.github.io/Fire_Varna/`. 6,000+ hydrants, Leaflet +
  MarkerCluster + `data/hydrants.json`, Cloudflare Worker â†’ GitHub issues.

## 3. Confirmed architecture decisions

1. **Private pipeline â†’ public app.** Varna_buildings stays PRIVATE and
   build-time; it emits **curated, safe** outputs that feed Fire_Varna.
   Raw KAIS, intel, and personal data never cross to the public side.
2. **Host = Fire_Varna Pages.** All user-facing functionality lives in the
   public app.
3. **Mobile-first, light payload.** Heavy layers (`strategic_intel` ~34MB,
   `section_units` ~17MB, raw geocoder ~19MB) NEVER go to mobile.
4. **Config/data-driven editing.** Hydrants, building annotations, and the
   verification flow are editable without touching core app logic.

## 4. The "one repo" reframe (important)

The private/public split means they **cannot** be one git repo (a public
GitHub Pages repo cannot contain the private KAIS pipeline). So:

- **Two repos, clean split.** Varna_buildings (private pipeline) +
  Fire_Varna (public app).
- **Your day-to-day "one repo to debug/edit" is Fire_Varna** â€” it holds
  everything user-facing (map, hydrants, building display, search,
  verification config, data). You rarely touch the pipeline; it just
  regenerates building data from KAIS.
- **"Merge" = integrate capabilities + a curated data handoff**, NOT a
  git-history merge.

## 5. Two constraints to design around

- **Mobile weight.** Core GPS â†’ nearest-hydrant needs **nothing** from
  buildings (just `hydrants.json`, already on device, offline). Address
  search needs a geocoder: either a **slim on-device index** (address-tier,
  `{text, lat, lng}` only â†’ under 1MB gzip, lazy-loaded + service-worker
  cached â†’ offline search) or a **Worker-side geocoder** (ultra-light, needs
  signal to search). Likely: slim on-device default, Worker as fallback.
- **Public/private boundary.** The pipeline publishes ONLY the safe subset
  (no raw KAIS, no personal data, KAIS-license-clean). A **publish gate**
  defines what is safe to cross to the public app.

## 6. Mobile-lightness strategy

- Core (offline): `hydrants.json` + GPS â†’ nearest, MarkerCluster for 6k
  points (already exists).
- Address search: slim geocoder (<1MB gzip, lazy, SW-cached) or Worker.
- Footprints: optional â€” simplified / viewport-only / lazy.
- Service worker: offline cache + fast repeat boot; hydrants-first boot.

## 7. Config / data-driven layers (edit without code)

- **Hydrants:** curated dataset + the existing ðŸš¨ â†’ Worker â†’ GitHub flow
  (extend for add/edit).
- **Buildings:** an **override/annotation layer** (name / status / note) on
  top of pipeline-derived data; editable file or UI â†’ Worker â†’ GitHub; the
  pipeline regenerates under it and overrides persist. (Buildings are
  derived from KAIS â€” you cannot edit them like hydrants; you annotate via
  overrides, a pattern the pipeline already uses with sidecars.)
- **Verification:** a `verification_config.json` defining form fields,
  statuses, labels, and colors/icons; the app renders verification FROM it.
  Edit the config â†’ change the verification flow and look, no app-logic
  touch. Theming via CSS variables for visual changes; a ground-up layout
  redesign still touches the HTML/CSS template (but not the core logic).

## 8. Verification (field)

- **All-hydrants view:** every hydrant status-coded (verified / reported /
  unverified / canonical), MarkerCluster, on the map. Extends the existing
  "Ð’ÑÐ¸Ñ‡ÐºÐ¸" mode. No extra payload â€” data is already on device.
- **Config-driven design** (section 7).
- **Preserve** the existing ðŸš¨ â†’ Worker â†’ GitHub-issue flow.

## 9. Phasing (non-breaking, incremental)

- **Phase 0 â€” Architecture cycle.** ADR (amend ADR 020 / new ADR);
  reconcile both repos' governance; define the curated-bundle contract +
  the publish gate.
- **Phase 1 â€” Pipeline emits the curated mobile bundle** (slim geocoder +
  footprint subset, safe). Varna_buildings user-facing unchanged.
- **Phase 2 â€” Fire_Varna consumes the bundle:** building display + address
  search in the app. Both apps still work.
- **Phase 3 â€” All-hydrants verification view + `verification_config`** (config-driven).
- **Phase 4 â€” Building override/annotation edit layer.**
- **Phase 5 â€” Mobile optimization pass** (SW cache, lazy-load, payload
  budget, field testing on a phone).

Each phase must not break the prior one; verify both apps after each.

## 10. Open decisions for the cycle

- Slim on-device geocoder vs Worker geocoder (offline search vs
  ultra-light) â€” likely both.
- The exact curated-bundle contract (fields, footprint detail level, and the
  publish-gate / safe-subset definition).
- Governance reconciliation (one combined AGENTS/CLAUDE across both repos,
  or per-repo with a shared integration ADR).

## 11. Governance

- Gated Phase 2 reintegration (`architecture_v2.md`: deferred, ADR 020
  amendment required).
- Both repos share the tri-agent workflow (chat-Claude architect / Codex
  planner / Claude Code executor / Petar signs + pushes).
- Don't break anything; never push (Petar pushes); no personal data on the
  public side; BGS2005 â†” WGS84 discipline (hydrants are already WGS84).

## 12. Setup for the new Cowork project

1. Clone the public app locally next to the pipeline:
   `git clone https://github.com/Petar1984/Fire_Varna.git C:\git\Fire_Varna`
2. New Cowork project â†’ **select the parent folder `C:\git\`** so both
   `Varna_buildings` and `Fire_Varna` are accessible as files.
3. Make sure this framing doc is reachable (it lives in
   `Varna_buildings/scratch/`, so it is under the selected parent).
4. First action in the new session: chat-Claude reads this + both repos â†’
   frames the integration ADR â†’ runs the tri-agent cycle, phased per
   section 9.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -Encoding UTF8 -LiteralPath C:/git/varna_3d/AGENTS.md,C:/git/varna_3d/CLAUDE.md,C:/git/Fire_Varna/AGENTS.md,C:/git/Fire_Varna/CLAUDE.md' in C:\git
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git --no-optional-locks status --short; git log -4 --oneline; rg --files -g AGENTS.md -g '*decisions*' -g '*district*' -g '*S23*' -g '*audit*'" in C:\git\Fire_Varna
 succeeded in 50ms:

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
# CLAUDE.md

> **Canonical current state:** see `docs/activeContext.md` (last updated commit hash and sprint status). If this file conflicts with `activeContext.md`, the latter wins.
>
> Instructions for **Claude Code** working in this repo.
> Read `AGENTS.md` first for project context, dataset rules, and constraints.

---

## Orientation (repo · trunk · forbidden · entry point · live numbers)

- **What this repo is.** `Fire_Varna` — the mobile-first web app that shows a firefighter the nearest working fire hydrant in Varna oblast, in the browser, with no install and no account (`README.md` § Български). The app shell (`index.html`), the dataset (`data/`), the ingest and audit scripts (`scripts/`, `audit/`), the tests (`tests/`), the Cloudflare Worker source (`worker/`) and the governance documents (`docs/`) all live in this one repo.
- **Trunk.** `main` — GitHub's default branch (`git symbolic-ref refs/remotes/origin/HEAD` → `refs/remotes/origin/main`) and the branch the site is published from ([AGENTS.md § What This Project Is](AGENTS.md#what-this-project-is): "Distribution: GitHub Pages from `main`"). Work commits land here; every other branch is a frozen trace of a past cycle, listed by `git branch -avv` and dated by `git for-each-ref --sort=-committerdate --format='%(refname:short) %(committerdate:short)' refs/heads refs/remotes`. Petar alone pushes (Gate 2), so `main` can stand ahead of `origin/main` between his pushes — measure that with `git rev-list --count origin/main..main`, never resolve it with `git push`.
- **What is forbidden here.** § Hard Rules below — never push · never commit secrets · field-report PII gate · destructive-op gate · cross-repo isolation · no automated commits — plus [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). A rule you are about to bend is the signal to stop and ask, not to improvise.
- **Entry point.** [`docs/activeContext.md`](docs/activeContext.md#current-state) — read it before anything else when resuming work. On current state it wins over this file (see the header above).
- **Live numbers.** No state number enters this file. Record counts, byte sizes and commit hashes live in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state) — one truth per document. The numbers that do stay here are rules, not state: the 15 s poll interval (`POLL_INTERVAL_MS`), the 5 MB first-load hard cap ([AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints)), `HEADING_SMOOTHING = 0.10`. If you need a fresh count, run the command — do not write the result into this file.

---

## Your Role

You are the **Executor** in the dual-Claude-Code pipeline. See `AGENTS.md` § Dual-Claude-Code workflow, and ADR [`docs/decisions/003_dual_claude_code_governance.md`](docs/decisions/003_dual_claude_code_governance.md).

| Role | Agent | What it does |
|---|---|---|
| **Planner** | Claude Code — read-only (model per `~/.claude/agents`) | Plans, architects, measures, drafts the plan. Never edits or commits. |
| **Researcher** | Claude Code — read-only (model per `~/.claude/agents`) | Planner sub-phase: gathers evidence and measurements. Never edits. |
| **Executor (you)** | Claude Code (model per `~/.claude/agents`) | Implements the signed plan, edits files, commits locally. Never pushes, never architects. |
| **Auditor** | Claude Code — read-only, adversarial (model per `~/.claude/agents`) | Independently checks the Executor's diff against the plan. Never edits. |
| **Orchestrator** | Petar | Signs plans (Gate 1), reviews diffs (Gate 2), pushes. Sole push authority. |

If you receive a task without an approved plan from the **Planner** (read-only; model per `~/.claude/agents`), signed by Petar, stop and ask. Do not improvise architecture.

---

## Hard Rules

Project-wide constraints (size budget, static hosting, Bulgarian UI labels, dependencies, mobile-first, HTTPS-required APIs, Varna-only scope) are canonical in [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints). Stop and ask if an approved plan would violate them.

### Non-negotiable guardrails (harmonized with Varna_buildings)

1. **Never run `git push`.** Petar pushes manually after reviewing commits locally, at Gate 2. This holds with any flag; never use `--no-verify` and never bypass the pre-push hook.
2. **Never commit secrets.** No Cloudflare API tokens, Worker deploy credentials, `wrangler` secrets, `.dev.vars`, or `.env` files ever enter the repo. Verify `.gitignore` covers them before staging if in doubt.
3. **Field-report / PII gate.** Treat field-report submissions as personal data: reject by default, and scrub any identifying content before persisting to `data/` or creating a GitHub issue. Stop and ask before persisting anything that could carry PII.
4. **Destructive-op gate.** If you discover unexpected state — unfamiliar branches, uncommitted changes, files you did not create — investigate before deleting or overwriting. It may be Petar's in-progress work.
5. **Cross-repo isolation.** Do not touch the `Varna_buildings` checkout, or any other repo, from here. Work stays inside `C:\git\Fire_Varna`.
6. **No automated commits.** One logical change per commit, staged with explicit paths, using the exact commit message from the approved plan.

### Per-commit execution protocol

For each commit in an approved plan:

1. Read the commit specification in the plan.
2. Verify dependencies on earlier commits are met.
3. Create or modify only the files the spec names.
4. Stage those files with **explicit paths** (never `git add -A` / `git add .`) and commit with the **exact** message from the plan.
5. Run `git status --short` to confirm only the intended files were committed and pre-existing dirty/untracked files were left untouched.
6. Report commit number, hash, files, and acceptance-check result.
7. If an acceptance check fails, **stop and ask Petar.** Do not roll forward with a broken commit.

---

## Code Style

This codebase is read primarily by AI agents and a non-CS-trained owner.

- Clear names over short names.
- Comments explain **why**, not **what**.
- No clever one-liners. No premature abstraction.
- One concern per function.
- No dead code. If you replace something, delete the old version.

---

## Specific Gotchas

- **`deviceorientation` fires at 100-200Hz on Android.** EMA must run on `requestAnimationFrame`, reading the latest stored raw heading. Do not EMA inside the event handler. `HEADING_SMOOTHING = 0.10`.
- **All map markers use `L.divIcon`**, never `L.icon`.
- **`L.markerClusterGroup` is used only in "Всички" mode.** Other modes use plain numbered pins. Do not unify this.
- **Map auto-fit happens at three sites, never on routine GPS updates:** the first GPS lock (`refresh(!deepLinkFramed)` — skipped when a `?h=` deep link already framed the map on one hydrant), `setMode()`, and the manual-position map click. Routine GPS ticks call `refresh(false)`.
- **Tap and long-press differ intentionally.** Tap selects/activates a hydrant; long-press opens the report menu.
- **`targetCardHTML()` builds the card HTML into `modalBody.innerHTML` at two call sites.** In `showReportModal()` the listeners are re-attached right after by `wireReporterBar()` + `wireFormHandlers()`; in `showReportTypePicker()` by `wireReporterBar()` + the inline `.type-btn` handlers; preserve that unless a refactor explicitly changes it.
- **Polling interval is fixed at 15 s (`POLL_INTERVAL_MS`).** Do not lower without coordinating Worker KV cache TTL (currently 30 s) and reviewing the rate math in `docs/plans/commit_15_worker_get.md`.
- **Polling must never block the UI thread.** All work happens inside `async pollIssues()` with a `setTimeout` schedule. Do not call `refresh()` from polling and do not introduce synchronous JSON-walking over the full `HYDRANTS` array.
- **Polling pauses while the tab is hidden** (`document.hidden`) and fires one immediate catch-up poll on return. Preserve both halves — losing the catch-up means stale pins after long backgrounding.
- **Polling updates pins via `marker.setIcon` and `marker.setLatLng`, never by rebuilding** the cluster or calling `refresh()`. Marker tags `_hydrantId` / `_pinKind` / `_rank` / `_isActivePin` are set in `refresh()` and consumed by the polling code; mutating them outside `refresh()` will leak the active-pin flag across transitions.
- **`lastPollSince` only advances on a successful, parseable response.** Failures (network, non-2xx, invalid JSON) keep the cursor where it was so the next poll re-requests the same window.

---

## Field Report Ingest Rules

See [AGENTS.md § Wrong-Location Ingest Rule](AGENTS.md#wrong-location-ingest-rule) for the canonical table and rules. Stop and ask before any data edit unless the approved plan names the affected report IDs.

A canonical coordinate mutation follows the **Measurement Doctrine** — ADR [`docs/decisions/004_measurement_doctrine.md`](docs/decisions/004_measurement_doctrine.md) (references Varna_buildings ADR 058): clear the acceptance floor before mutating `coords`; Google terrain-eyes may only refute / downgrade / trigger a re-check, never rewrite a coordinate alone, never be cached or fed back to OSM.

---

## Report Flow

See [AGENTS.md § Report Flow](AGENTS.md#report-flow) and [docs/activeContext.md § Current State](docs/activeContext.md#current-state).

---

## Verification

No CI yet, but tests exist (`tests/`, Python `unittest`). When ingest or shared-core (`scripts/lib/hydrant_core.py`) behavior is relevant, run the suite:

```powershell
python -m unittest discover -s tests
```

For frontend / deployable changes, before reporting done:

1. Serve locally over HTTP:

   ```powershell
   python -m http.server 8000
   ```

2. Open at 375px viewport width and check:
   - Map renders within 3 seconds.
   - Browser console has no runtime errors.
   - `data/hydrants.json` loads with HTTP 200.
   - `JSON.parse(document.getElementById('hydrantData').textContent).length` equals the record count declared in [`docs/activeContext.md` § Current State](docs/activeContext.md#current-state) — the count is not written here; read it there, or measure `data/hydrants.json` yourself.
   - GPS lock works, or graceful error pill with retry/manual controls appears.
   - All 3 view modes render correctly: "Близо", "Топ 5", "Всички".
   - Cluster mode shows clusters when zoomed out.
   - Building detail sheet (`.detail-sheet`, the C4 search result) opens and closes; the hydrant bottom sheet no longer exists — it was removed in the popup pivot.
   - Compass cone rotates with simulated `deviceorientation` events.
   - FAB `+` opens the report-type menu.
   - Long-press on a verified pin opens the report menu.
   - Follow mode recenters; user pan exits follow mode.
   - Manual position mode accepts a map click.
   - Report submit uses Worker `fetch` POST and queues locally if offline.

3. Report `index.html` and `data/hydrants.json` sizes after changes.

---

## Windows Dev Environment

See [AGENTS.md § Windows Dev Environment](AGENTS.md#windows-dev-environment).

---

## What Requires Going Back To Humans

See [AGENTS.md § Dual-Claude-Code Workflow](AGENTS.md#dual-claude-code-workflow) for the canonical approval gates. Asking is cheap. Reverting commits is not.

---

## Workflow Expectations

- **One logical change per commit.**
- **Commit messages in English.**
- Code comments in English. UI strings in Bulgarian.
- Before refactoring, confirm there is an approved Planner plan signed by Petar describing the target structure.
- After any change to the deployable, state files changed, file sizes, and any constraint that came close to being violated.
- After any governance section rename, run grep for old section names and update Markdown anchor links in the same pass.

 succeeded in 49ms:
e6c706d record: district resolutions (decision 9) — Кочмар and Възраждане 4 → Младост per АГКК AU5
fe56252 measure: our OSM-based district layer vs official АГКК AU5 — Владиславово IoU 0.79 (404 ha excess north of Трети март = Кочмар/Възраждане 4 zone, official Младост), Младост 0.69, Одесос 0.80, Аспарухово 0.96, Приморски 0.995; proposal: districts of quarter polygons from AU5
f2dba07 docs(sessions): decision 9 — Кочмар and Възраждане 4 belong to district Младост (АГКК AU5 confirmed by Petar); our district layer disagrees with the official boundary near бул. Трети март — morning measure
3d747d3 record: decisions 4 — attribution field added (night plan Б0.8); Petar signs the final blob sha
scratch\places_search\granitsi_decisions_4_2026-09-07_proba.json
scratch\places_search\granitsi_decisions_3_2026-09-06_proba.json
scratch\places_search\granitsi_decisions_2_2026-09-06_proba.json
scratch\places_search\granitsi_decisions_2026-09-06_proba.json
scratch\places_search\granitsi_b1v2_astra_S23_07.09.md
scratch\places_search\district_resolutions_2026-09-07.json
scratch\patch_live_osm_audit_20260811.md
AGENTS.md
scratch\kais_func_2026-09-03\парцели\v2_audit.txt
docs\audits\data_architecture_audit_20260508.md
docs\audits\data_audit_and_target_schema_20260508.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git --no-optional-locks status --short; git branch --show-current; git log -5 --oneline; rg --files -g AGENTS.md -g '*quarters*' -g '*S23*' -g '*decisions*' -g '*district*' -g '*lot*' -g '*audit*' -g '*crosswalk*'" in C:\git\varna_3d
 succeeded in 65ms:
rezhimi
e2da307 build+gates: district resolutions input (decision 9) — Кочмар and Възраждане 4 → Младост, QA accepts only AU5-consistent resolutions
7fb0e92 gates: qa_quarters_signed — independent AU5 district witness, union_crs and degree-union negatives (Astra S23)
6dde0a5 build: quarters_signed — union recipe and library versions pinned, district witness disputes recorded (Astra S23)
8c262e9 gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)
63d077d build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)
tests\test_quarters_signed_fixtures.py
tests\fixtures\qa_quarters_signed\resolved_district_contradicts_au5.geojson
tests\fixtures\qa_quarters_signed\district_spatially_wrong.geojson
tests\fixtures\qa_quarters_signed\district_from_agkk.geojson
tests\fixtures\qa_quarters_signed\district_dispute_delisted.geojson
tests\fixtures\qa_quarters_signed\decisions_sha_substituted.geojson
tests\fixtures\qa_quarters_signed\au5_crosswalk_swapped.geojson
src\qa_quarters_signed.py
src\qa_quarters_license.py
src\qa_quarters_candidate.py
src\qa_audit_extraction.py
src\lot1v_v_manifest.py
src\build_quarters_signed.py
src\build_quarters_candidate.py
data\quarters_signed.geojson
AGENTS.md
scratch\refactor\_pubbldg\plots\plots_pooled.json
scratch\refactor\_pubbldg\plots\plots_by_district.json
scratch\refactor\_pubbldg\plots\plots_by_class.json
scratch\refactor\_pubbldg\join\coverage_by_district.json
scratch\refactor\_pubbldg\func\func_by_district.json
scratch\refactor\_addr\lot1v_v_manifest_BASE_P7.md
scratch\refactor\_addr\lot1v_v_manifest_BASE_P7.json
scratch\refactor\_addr\lot1v_locations_375.json
scratch\refactor\_addr\_shops_quarters.json
scratch\refactor\_addr\_quarters_kimi_питане.md
scratch\refactor\_addr\_quarters_kimi_отговор.md
scratch\refactor\_addr\_quarters_kimi_err.log
scratch\refactor\_addr\_shops_quarters_detail.json
scratch\refactor\_addr\_shops_quarters2.json
scratch\refactor\_addr\_shops_quarters_probe.py
scratch\refactor\_addr\_shops_quarters_probe2.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -Encoding UTF8 -LiteralPath docs/activeContext.md -TotalCount 150' in C:\git\varna_3d
 succeeded in 27ms:
# Varna 3D — входна точка

**Дата:** 02.09.2026 · **последно сверено срещу комит** 9f55c08 (`rezhimi`; напред спрямо `origin/rezhimi` с комитите на плана от 01.09 до пуша на Петър — таблицата) · сверил: Opus (executor), одитирал: <одитор> · подпис: __
> Всяко число тук е изходът на командата до него, пусната на датата горе (`verify_numbers.py` го проверява). Число без команда не влиза.
> Хрониката по дати е замразена в [СЪСТОЯНИЕ.md](СЪСТОЯНИЕ.md) (до 01.09.2026). Изворите са описани в [../DATA.md](../DATA.md) (мерени 30.07.2026).

## Какво е това
Триизмерен модел на Варна от КАИС „Отворени данни" — стои НАД `Varna_buildings` (данните за сградите) и `Fire_Varna` (хидрантите), чете техните изходи, не ги пипа. Публикуваното е `web/` (карта: `Varna 3D.bat` → http://127.0.0.1:8791).

## Стволът
- Работен клон: `rezhimi`. Клонът по подразбиране в GitHub: `main` (изравнен с `origin/rezhimi` в ЛОТ 3 на плана от 01.09; проследява `origin/main`; занапред — В-1/Р-12).

## Тема „търговско-обществените сгради" (03.09.2026, сесия git-65 / Fable) — сурови данни във файл, нищо в картата
- **Състояние:** Ф0 мярка (`b8141ec`) → план v1.1 подписан по думите на Петър (`docs/plans/ПЛАН_търговско-обществени.md`, §11 амандаменти) → лотове А0/А1 (`c74bad0`, `a7f1a68`), А4 (`0ccc525`), А3 (`12b082f`), А5 + бордът (`7a4bed5`). По амандамент №1 („за сега инфото на файл") `build_places.py` НЕ е пускан, износ към Fire_Varna няма; А2/А6/Б/В чакат преценката на Петър. Докладът: [audits/ДОКЛАД_03.09_търговско-обществени.md](audits/ДОКЛАД_03.09_търговско-обществени.md); бордът: [audits/БОРД_търговско-обществени_2026-09-03.md](audits/БОРД_търговско-обществени_2026-09-03.md).
- **Живи числа на темата** (03.09.2026):

| Какво | Стойност | Команда |
|---|---|---|
| OSM места (сурови) | 1848 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_public_osm_places.json',encoding='utf-8'))['places']))"` |
| НТР ЗХР места (сурови) | 373 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_ntr_zhr_places.json',encoding='utf-8'))['places']))"` |
| Wikidata места (сурови) | 44 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_wikidata_places.json',encoding='utf-8'))['places']))"` |
| официални сайтове (Сол, сурови) | 5 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/raw_web_places.json',encoding='utf-8'))['places']))"` |
| тела в геофайла / с име | 10367 / 1538 | `PYTHONIOENCODING=utf-8 python src/build_public_buildings_geojson.py \| grep '^bodies'` (изходът е в `output/`, извън git) |
| мастерът `places.json` недокоснат от темата | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |

## Тема „ЛОТ 1в за Fire_Varna" (04.09.2026, сесия git-08) — имената, адресите, кварталите
- **Състояние:** лот А (псевдонимите с извор, `1d5ec9a`, `859dbe5`) → лот Б (адресът с извор на всеки запис, `25a6d79`) → **лот В (P6): кварталът, районът и допълнителното с извор.** Планът и подписът са на Fire_Varna: `Fire_Varna/docs/plans/ПЛАН_ЛОТ1в-В_кварталите.md` (Gate 1-В подписан, §3з); ADR `Fire_Varna/docs/decisions/008_places_aliases_and_addresses.md`. Във Fire_Varna не е пипано нищо оттук — прави се САМО артефактът.
- **Правилото (§3г, подписано):** кварталът е САМО жилищно ниво по регистъра на кварталите и САМО с човешки написан извор — регистровият адресен сегмент (`REG`) или кадастралният квартал на закотвеното тяло (`KAIS`); без извор → честно „район X". Районът идва САМО от КАИС `reg` (петте градски района, затворен списък). Допълнителното (`locality`) носи промишлените зони, парковете и местностите. **Нищо нарисувано и нищо OSM-производно не решава** — обвивките, етикет-точките и районният полигон са само сравнителни колони в маскирания ledger `../scratch/refactor/_addr/lot1v_locations_375.json`.
- **Изолация:** новата стълба (`src/fire_varna_locations.py`) е Fire-export-only. Глобалната `src/place_zones.py`, майсторът и артефактите на паралелната тема не мърдат — доказва го `src/qa_fire_varna_location_isolation.py` (G-ISO) срещу закованите входове `data/fire_varna_location_inputs.json`.
- **Чака подпис:** манифестът old → new (209 реда) преди замразяването на референцията във Fire_Varna; фикс-извадката за окото на Петър е в ledger-а.
- **Хигиена след одита на лот В (P6-б):** SHA-то на доставка се смята върху LF-нормализирани байтове — тоест е SHA-то на блоба (`git show HEAD:<път>`), не на байтовете на този диск (прясно записаният износ е CRLF, прясно изтегленият — LF); затова гейтът (g) на `qa_place_zone_aliases.py` и G-ISO отговарят еднакво в работното дърво и в чист worktree. `data/registry_manifest.json` е комитнат (22 стойности `zone` в `grandfathered`/`board_queue`; секцията `rows` е идентична с P6), затова пинът му вече сочи блоб от историята. Ledger-ът носи `_meta.fix_sample_why` (доводите се ИЗВЕЖДАТ от полетата на реда) и `_meta.open_question_map_label`: 6 реда губят квартала си по `map_label:false`, 5 от тях с човешки написан регистров сегмент (ДГ 32, ДГ 36) — за решение на Петър.
- **Живи числа на темата** (04.09.2026):

| Какво | Стойност | Команда |
|---|---|---|
| доставени записа (места + хотели) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| с квартал (REG 34 · KAIS 94 · подписан override 12) | 140 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| с допълнително местоположение | 8 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| с район (100 % покритие, нула карантина) | 375 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| head -1` |
| сменят зона спрямо доставеното (манифестът) | 209 | `PYTHONIOENCODING=utf-8 python src/fire_varna_locations.py \| tail -1` |
| G-ISO: глобалната стълба и чуждата тема непокътнати | минава | `PYTHONIOENCODING=utf-8 python src/qa_fire_varna_location_isolation.py \| tail -1` |
| самоличности с непроменен `place_id` | 375 (0 нови) | `PYTHONIOENCODING=utf-8 python src/place_identity.py \| grep 'обекта'` |

## Отворена тема (към 01.09.2026, по СЪСТОЯНИЕ.md § 01.09)
- **Секции от апартаменти v1.3** — одит ГОДНО, **чака Gate 2** върху [извадката](../scratch/refactor/_addr/ПРЕГЛЕД_извадка_секции_01.09.md) (броят места е по документа; непроверено 01.09.2026); след „давай" — Ф4-сливане. Дали Gate 2 е даден след 01.09: непроверено (01.09.2026), В-2.
- **Входове без регистър v2.1** — подписан; [бордът](../scratch/refactor/_addr/БОРД_изведени_входове_66.md) (сгради/входове по заглавието на документа; непроверено 01.09.2026) чака визуалната проверка на Петър. Непроверено след 01.09 (В-2).
- **Римски цифри в имената** — [ПЛАН_римски_цифри.md](plans/ПЛАН_римски_цифри.md) v1.1: мярката (11/370 poi, 3/576 места, 8 в регистъра на МОН; правилото НЕ в `skel` — 1 872 адресни „и“), Сол събори v1 (4 блокера) — чака поправен план + подпис; не е изпълнявано.
- **Фаза 2 на местата за Fire_Varna** (училища/университети/болници/ДКЦ/хосписи/детски градини) — ИЗПЪЛНЕНА: износът `data/fire_varna_places.json` (135 места, 74 изключени поименно; ff760e3) и кварталът/районът по стълбата за местата и хотелите (ba78a25); планът v1.5 е копие на `Fire_Varna/docs/plans/places_phase2_plan.md` ([ПЛАН_фаза2_места.md](plans/ПЛАН_фаза2_места.md)); мярката на фунията в [../scratch/refactor/_addr/ФУНИЯ_фаза2_02.09.md](../scratch/refactor/_addr/ФУНИЯ_фаза2_02.09.md). Отворено за подпис (§10): П7 — кварталните псевдоними от регистъра в `data/place_categories.json` (`build_place_categories.py`, ключ `zones`); лот Д5 — 53-те общински детски градини от извадката 19.08 върху КАИС-парцелите (Владиславово: 2 от поне 5 в доставката). Решенията на Петър (лицензът на регистрите, ODbL върху bundle-а, МЦ вън/вътре) — в доклада на Fire_Varna.

## Чака подпис / преглед
- Gate 2 на секциите (горе) · визуалната проверка на входовете (горе) · непушнатите комити (числата долу) — пушът е на Петър.

## Последният доклад
- [audits/ДОКЛАД_01.09_секции_и_входове.md](audits/ДОКЛАД_01.09_секции_и_входове.md)

## Живи числа
| Какво | Стойност | Команда |
|---|---|---|
| комити на `rezhimi` | 469 | `git rev-list --count rezhimi` |
| последен пушнат комит | 1a8e170 2026-08-31 | `git log -1 --format='%h %cs' origin/rezhimi` |
| непушнати към `origin/rezhimi` | 15 | `git rev-list --count origin/rezhimi..rezhimi` |
| публикувано поколение на кадастъра | 24.07.2026 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('web/varna_buildings_3d.manifest.json',encoding='utf-8'))['generation']['buildings'])"` |
| сгради в публикувания слой | 80497 | `PYTHONIOENCODING=utf-8 python -c "import json;print(json.load(open('web/varna_buildings_3d.manifest.json',encoding='utf-8'))['buildings'])"` |
| секции (3D) | 2101 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('web/varna_sections_3d.geojson',encoding='utf-8'))['features']))"` |
| изведени входове | 11748 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('web/varna_entrances_derived.geojson',encoding='utf-8'))['features']))"` |
| места (`places.json`) | 576 | `PYTHONIOENCODING=utf-8 python -c "import json;print(len(json.load(open('data/places.json',encoding='utf-8'))['places']))"` |
| гейт „нула кадастрални идентификатори" | минава | `PYTHONIOENCODING=utf-8 python src/qa_no_cad_ids.py \| tail -1 \| cut -d' ' -f1` |

> Двата реда за брой комити („комити на `rezhimi`“ и „непушнати към `origin/rezhimi`“) мърдат с +1 при всеки комит — включително този, който добавя файла; сверката е спрямо комита в ред 3 (= `git rev-parse --short HEAD~1` веднага след комита на ЛОТ 5). Затова `verify_numbers.py` върху комитнатия файл показва точно тези два реда с +1.

> Доставката `fire_varna_hotels.json` е потребена от Fire_Varna като проследения LF-blob на HEAD 9f55c08 (OID `4c5d72c4…`, 78 601 B) — командата: `git rev-parse HEAD:data/fire_varna_hotels.json`

## Забранено тук
- `git push` — само Петър. Кадастрален идентификатор извън `C:\git\m6000_private` — гейтът `src/qa_no_cad_ids.py`. OSM данни в модела — само сравняват (ФАЗА_0, условие 4). `git checkout main` / `clean -fd` / `reset --hard`, докато има неследени файлове. Данни в git — `.gitignore` ред 1 (изключенията са изброени там).

## Къде са нещата
- `docs/plans` · `docs/audits` · `docs/sessions` · `docs/research` · `docs/decisions` (+ индекс) · `docs/measurement` · `docs/СЪСТОЯНИЕ.md` — по плана от 01.09 (ЛОТ 4). `docs/sessions/ПРОМПТ_20.08.md` е извън git (Р-4: носи кадастрален идентификатор). `ПЛАН_П2в_терена.md` остава в корена: вход на конвейера (`src/qa_no_extrude.py`).
- `scratch/refactor/_addr/` — доказателствената база (мерки, бордове, разследвания, атаките на Kimi/Sol); `scratch/web_probes/` — проверката през истински Chrome (README вътре).
- Извън git: `C:\git\m6000_private\` (носи кадастрални идентификатори — по замисъл); `C:\git\bridge\` (каналът към Sol); `C:\git\Varna_buildings\output\` и `data\extracted\` (изворите, виж DATA.md).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -Encoding UTF8 -LiteralPath docs/activeContext.md -TotalCount 100' in C:\git\Fire_Varna
 succeeded in 29ms:
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

**AFTER A.2-4 — 6 red, one class.** Every delivery-dependent expectation left the
code for `scratch/places_search/expectations.json`; the suite compares the engine
with that tracked body (which can and does fail: move the engine, forget the
artefact, and it is red), and whether Petar has SIGNED it is the release gate's
question — план v2 §0.4 („очакване, което чака подпис, е ред в опашката, не
червен тест“) and §A.2 („готовността на доставката отива в release-гейта“).

The six that remain are one claim in six places: **the frozen reference is still
the one of лот Б and the engine has moved past it** — they go green with the ONE

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import subprocess,hashlib,json,pathlib
p='data/quarters_signed.geojson'
b=subprocess.check_output(['git','cat-file','blob',':'+p]); w=pathlib.Path(p).read_bytes()
d=json.loads(b)
print('STAGED',len(b),hashlib.sha256(b).hexdigest(),'features',len(d['features']))
print('WORKTREE_IDENTICAL',w==b)
print('STAGED_NAMES',subprocess.check_output(['git','diff','--cached','--name-status']).decode('utf-8'))
print(json.dumps(d.get('_meta'),ensure_ascii=False,indent=2))
'@ | python -" in C:\git\varna_3d
 succeeded in 106ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
STAGED 301917 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3 features 60
WORKTREE_IDENTICAL True
STAGED_NAMES A	data/quarters_signed.geojson

{
  "artifact_class": "signed_by_plan_signature",
  "attribution": "Кварталните граници в този файл са по Wikimapia.org (© Wikimapia contributors, CC BY-SA, ToS §1.G: връзка към обекта + „Wikimapia.org“ с връзка към http://wikimapia.org); карето „Младост 2“ е по улични оси от OpenStreetMap (© OpenStreetMap contributors, ODbL, https://www.openstreetmap.org/copyright). Геометрия НИКОГА не пътува публично.",
  "canonicalization": {
    "bytes": "UTF-8 без BOM, sorted keys, compact, финален LF (G30); две сглобявания са байт-еднакви",
    "raw_geometry_sha256": "sha256 на компактния {\"type\",\"coordinates\"} — правилото, което вече е в решенията (пренесено по Б0 т. 2)",
    "wm_polygon_sha256": "канонизацията на D1 по Б0 т. 2: 6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; вътрешните по часовника; MultiPolygon по амандамент №2 §4"
  },
  "counts": {
    "choice_alias_of": 1,
    "choice_declared_streets": 1,
    "choice_deferred": 6,
    "choice_excluded": 1,
    "choice_wikimapia": 58,
    "choice_wikimapia_union": 1,
    "decisions_rows": 68,
    "features": 60,
    "features_with_our_district": 58,
    "features_with_resolved_district": 2,
    "registry_entries": 84,
    "registry_pending": 16
  },
  "d1_schema": {
    "fields": [
      "code",
      "name",
      "kind",
      "parent",
      "source",
      "signed_by",
      "drawn_by",
      "approved_by",
      "drawn_at",
      "approved_at",
      "method",
      "basemap",
      "precision_m",
      "version",
      "license",
      "viewport",
      "visible_layers",
      "screenshot_sha256",
      "approval_digest",
      "witnesses",
      "note"
    ],
    "nulled_on_import": [
      "drawn_by",
      "drawn_at",
      "basemap",
      "viewport",
      "visible_layers",
      "screenshot_sha256",
      "approval_digest"
    ],
    "why": "Б0 т. 1 (подписан): за Feature със source ∈ {wikimapia, declared_streets} седемте полета на ръката са null по договор — взаимна изключителност „или ръка, или внос“. Дайджестът на D1 се замества от sha-веригата на Б0 т. 8: решения по sha → Feature с wm_polygon_sha256 → _meta.decisions_sha256."
  },
  "decisions_author": "Claude Architect (тялото на решенията, 895e0d2) → Claude Executor (полето attribution по Б0.8, 3d747d3)",
  "decisions_based_on": {
    "file": "granitsi_decisions_3_2026-09-06_proba.json",
    "rev": "b6e627d0fb19e039a062aba955d030301ae45b2e",
    "sha256": "ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6"
  },
  "decisions_blob_before_attribution": {
    "rev": "895e0d2651aac73516659f2a10ea5193b2be5d53",
    "sha256": "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89",
    "why": "тялото без полето attribution (Б0.8 го изисква); прегледано от Astra S23. Подписът на Петър е върху окончателния блоб, не върху този."
  },
  "decisions_commit": "3d747d3308bf31fe17add9a510ad97423adc672a",
  "decisions_path": "scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json",
  "decisions_sha256": "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b",
  "decisions_sha256_rule": "sha256 на БЛОБА (git show <rev>:<път>), не на работното копие — Б0 т. 8",
  "decisions_sha256_worktree": {
    "bytes": 32983,
    "note": "работното копие е CRLF; подписан е БЛОБЪТ (Б0 т. 8), не този файл",
    "path": "C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json",
    "sha256": "fdb748bcb76cf6458be3ad0e8decf495ca954fdd4f62f4aea7ea1aee3d608f4f"
  },
  "declared_deviations": [
    {
      "what": "choice: „wikimapia_union“ за кода dobreva (решения 4, Петър 07.09)",
      "why": "Площта, която Уикимапия нарича „Виница - север“ (5729421), е част от Добрева чешма — границата е обединението на двата човешки полигона. Обединението се смята в UTM 35N (EPSG:32635) и се връща в WGS84: така се възпроизвежда БАЙТ ПО БАЙТ пинът в решенията (d6f367bd…), който Петър видя. Обединение направо в градуси дава ДРУГА геометрия — различават се и двата хеша (bc92a76c… / fc1f7297…), а най-голямата разлика по връх е 4,177e-07° (≈ 4,6 cm), НЕ 1e-14°, както твърдеше по-ранният текст тук (поправено по Astra S23 F2). A9 отказва всеки друг резултат; рецептата и точните версии на shapely/GEOS/pyproj/PROJ са в _meta.union_recipe."
    },
    {
      "what": "полето url на обединения Feature",
      "why": "Обединението има два изворни обекта. `url` носи ПЪРВИЯ от реда (този, чието име носи кодът), а всички обекти с техните url-и и собствени сурови хешове са в `witnesses` — ToS §1.G се изпълнява от реда за атрибуция плюс свидетелите."
    },
    {
      "what": "choice: „excluded“ за кода vinitsa_sever",
      "why": "Петър (07.09): кодът отпада като квартал — няма Feature, редът е поименно в `_meta.excluded`. Деактивирането в quarter_registry.json е негов сутрешен ход: регистърът НЕ се пипа тук (червена черта 3 на плана), затова кодът остава в registry_entries и НЕ е в registry_pending (той ИМА решение)."
    },
    {
      "what": "полето district в Feature-ите",
      "why": "Б0 т. 4 иска районът да е изведен по представителна точка срещу НАШИТЕ пет района, не от АГКК INSPIRE (G22 остава заключен). Затова слоят с петте административни граници влиза като назован вход, а АГКК остава само свидетел в _meta.district_witness_agkk."
    },
    {
      "what": "районът на кодовете в _meta.district_resolutions.applied (district_src = agkk_au5_confirmed_by_petar)",
      "why": "Решение 9 (Петър, 07.09: „Кочмар и Възраждане 4 не са във Владиславово“). Само за поименно решените кодове районът НЕ идва от нашия слой, а от официалната граница на АГКК AU5, потвърдена от Петър; входът е подписан файл без геометрия, закотвен по sha256 в _meta.inputs. Спорът остава записан в _meta.district_witness_disputes с resolution petar_agkk — решението не трие разминаването, а го затваря. Всяко НЕрешено разминаване остава pending_petar."
    },
    {
      "what": "входният етикет source: declared_local_knowledge на карето „Младост 2“",
      "why": "Отменен от амандамент №2 §3.7; НЕ пътува в изхода. Изходният Feature носи source: declared_streets и лиценз ODbL по подписания ключ на Б0 т. 3."
    },
    {
      "what": "затвореният набор properties е 21 полета на D1 + 19 назовани провенанс-полета",
      "why": "Г2-в на амандамент №2 §4 изисква geometry_origin/imported_from/fetched_at/chosen_source/chosen_reason/confirmed_by/confirmed_at; Б0 т. 2 изисква двата хеша поотделно; G27(а) изисква реда за атрибуция. Наборът е затворен — непознат ключ спира сглобяването."
    }
  ],
  "district_resolutions": {
    "applied": [
      {
        "agkk": "10135-03",
        "basis": "agkk_au5 10135-03",
        "code": "kochmar",
        "district": "mladost",
        "was": "vladislav_varnenchik"
      },
      {
        "agkk": "10135-03",
        "basis": "agkk_au5 10135-03",
        "code": "vazrazhdane4",
        "district": "mladost",
        "was": "vladislav_varnenchik"
      }
    ],
    "district_src": "agkk_au5_confirmed_by_petar",
    "path": "C:/git/Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json",
    "rule": "подписаният файл може да реши САМО спор, който съществува, и САМО в посоката на свидетеля АГКК AU5; всичко друго спира сглобяването (A22) и пада на гейта (C18/C20). Нерешените разминавания остават pending_petar.",
    "sha256": "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc",
    "signed_at": "2026-09-07T00:10:58+03:00",
    "signed_by": "Petar via Claude Architect (words 07.09: Кочмар и Възраждане 4 не са във Владиславово)"
  },
  "district_witness_agkk": {
    "by_code": {
      "abatko": "10135-02",
      "akchelar": "10135-02",
      "alen_mak": "10135-02",
      "asparuhovo": "10135-05",
      "balam_dere": "10135-04",
      "borovets_sever": "10135-05",
      "borovets_yug": "10135-05",
      "briz": "10135-02",
      "chaika_kk": "10135-02",
      "chaika_kv": "10135-02",
      "dobreva": "10135-02",
      "dolna_traka": "10135-02",
      "druzhba": "10135-05",
      "evksinograd": "10135-02",
      "fichoza": "10135-05",
      "galata": "10135-05",
      "gorchivata_cheshma": "10135-02",
      "gorna_traka": "10135-02",
      "grackata_mahala": "10135-01",
      "hristo_botev": "10135-01",
      "izgrev_kv": "10135-02",
      "kaisieva": "10135-04",
      "kk_konstantin_elena": "10135-02",
      "kochmar": "10135-03",
      "kokardzha_generic": "10135-02",
      "kolhozen_pazar": "10135-01",
      "kv_levski": "10135-02",
      "maksuda": "10135-03",
      "manastirski_rid": "10135-02",
      "menteshe": "10135-04",
      "mladost": "10135-03",
      "mladost1": "10135-03",
      "mladost2": "10135-03",
      "morska_gradina": "10135-02",
      "pchelina": "10135-03",
      "perchemliyata": "10135-02",
      "pobeda": "10135-03",
      "priboy": "10135-05",
      "pz_planova": "10135-04",
      "rakitnika": "10135-05",
      "rozova_dolina": "10135-05",
      "saltanat": "10135-02",
      "sotira": "10135-02",
      "sredna_traka": "10135-02",
      "sv_ivan_rilski": "10135-03",
      "sveti_nikola": "10135-02",
      "trakia": "10135-01",
      "troshevo": "10135-03",
      "tsentar": "10135-01",
      "tv_kula": "10135-02",
      "vazrazhdane": "10135-03",
      "vazrazhdane1": "10135-03",
      "vazrazhdane2": "10135-03",
      "vazrazhdane3": "10135-03",
      "vazrazhdane4": "10135-03",
      "vinitsa": "10135-02",
      "vladislavovo": "10135-04",
      "zelenika": "10135-05",
      "zlatni_pyasatsi": "10135-02",
      "zpz": "10135-03"
    },
    "crosswalk": {
      "10135-01": "odesos",
      "10135-02": "primorski",
      "10135-03": "mladost",
      "10135-04": "vladislav_varnenchik",
      "10135-05": "asparuhovo"
    },
    "crosswalk_why": "подписаният превод национален код → нашите пет; АГКК НИКОГА не пише район (G22 заключен) — служи само за независимо свидетелство",
    "disputes": 2,
    "inside_one_district": 60,
    "outside_all": 0,
    "state": "свидетел: представителна точка на Feature-а срещу АГКК AU5"
  },
  "district_witness_disputes": [
    {
      "agkk": "10135-03",
      "code": "kochmar",
      "ours": "vladislav_varnenchik",
      "resolution": "petar_agkk"
    },
    {
      "agkk": "10135-03",
      "code": "vazrazhdane4",
      "ours": "vladislav_varnenchik",
      "resolution": "petar_agkk"
    }
  ],
  "excluded": [
    {
      "code": "vinitsa_sever",
      "display": "с.о. Виница-север",
      "kind": "с.о.",
      "registry_action": "сутрешен ход на Петър: деактивиране на кода в quarter_registry.json — регистърът НЕ се пипа от изпълнителя",
      "why": "Петър (07.09): „Виница-север го изключваме“ — кодът отпада от регистъра като квартал/с.о. (ход Р: деактивиране), не е второ име; площта е Добрева чешма"
    }
  ],
  "generated_by": "Claude Executor",
  "inputs": [
    {
      "bytes": 32129,
      "id": "decisions_4",
      "path": "Fire_Varna:3d747d3308bf31fe17add9a510ad97423adc672a:scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json",
      "role": "решенията — подписани по sha256 на блоба (Б0 т. 8); четени от git, не от работното копие",
      "sha256": "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b"
    },
    {
      "bytes": 589222,
      "id": "frozen_v2",
      "path": "C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson",
      "role": "замразеният уикимапийски набор — изворът на единичните геометрии и на двете части на обединението",
      "sha256": "b53a3322b1a6e5670ea17f7638ab77d198e120d108e623fa7bc78ae702daf976"
    },
    {
      "bytes": 3713,
      "id": "wikimapia_extra_5729429",
      "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/wikimapia_extra_2026-09-06.geojson",
      "role": "обектът 5729429 (Евксиноград/Траката), подаден от Петър след замразяването",
      "sha256": "b220423c6f954405fb0dbf94621fab30a8b6585e7156089c67e14dfa41382dd8"
    },
    {
      "bytes": 5071516,
      "id": "raw_snapshot",
      "path": "C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/wikimapia_varna_places_raw_2026-09-06.json",
      "role": "суровият отговор на обхода — raw_response_sha256 в witnesses на уикимапийските Feature-и",
      "sha256": "1c0561cb7e612e72f291ca33d603cc6ef7713b88ab5af7cbd6d942fbc18a7fbe"
    },
    {
      "bytes": 2971,
      "id": "mladost2_face",
      "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/mladost2_streets_proposal.geojson",
      "role": "карето „Младост 2“ по четирите улици (оси от OSM) — подписаният ключ на Б0 т. 3",
      "sha256": "66fd3f57f76d4f104911dc2f7576f33e678435b6e1156a19d61c0bf34030f5b8"
    },
    {
      "bytes": 52299,
      "id": "quarter_registry",
      "path": "C:/git/Varna_buildings/config/quarter_registry.json",
      "role": "регистърът — имена, вид и родство; ЧЕТЕН, никога пипан (червена черта 3)",
      "sha256": "7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6"
    },
    {
      "bytes": 201130,
      "id": "our_districts",
      "path": "C:/git/m6000_private/number_viewer/quarters_layer.geojson",
      "role": "нашите пет административни района (слоят за сравнение на fire_varna_locations) — изворът на полето district по Б0 т. 4",
      "sha256": "26e39b001ce151203058d70bc53367a5b40c77c4b0dd7113cf2a7085c376cc22"
    },
    {
      "bytes": 61469,
      "id": "agkk_au5",
      "path": "C:/git/Fire_Varna/scratch/places_search/agkk_inspire_2026-09-05/agkk_au5_varna.geojson",
      "role": "петте района на АГКК INSPIRE — САМО свидетел (G22 остава заключен, Б0 т. 4)",
      "sha256": "78a2de59600eb103719ca072b3963c6b7195598a65a66e4653c7cd53c966c669"
    },
    {
      "bytes": 513,
      "id": "district_resolutions",
      "path": "C:/git/Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json",
      "role": "подписаните решения по спорове за района (решение 9, Петър 07.09) — без геометрия; изворът на district_src=agkk_au5_confirmed_by_petar",
      "sha256": "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc",
      "signed_at": "2026-09-07T00:10:58+03:00",
      "signed_by": "Petar via Claude Architect (words 07.09: Кочмар и Възраждане 4 не са във Владиславово)"
    },
    {
      "bytes": 3921,
      "id": "unions_2026-09-07",
      "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/unions_2026-09-07.geojson",
      "role": "обединенията, както Петър ги видя — САМО свидетел; геометрията се преизчислява от замразения набор и сверява байт по байт срещу него",
      "sha256": "0fe781500725d78f46b9f931b66ad0267f782413f2c47f28a7669b68d1504080"
    }
  ],
  "licences": [
    {
      "applies_to": "58 Feature-а с method=human_polygon и 1 с method=human_polygons_union (обединение на човешки полигони — същият извор, същият лиценз)",
      "attribution": "Граница по Wikimapia.org (© Wikimapia contributors) — връзка към обекта в полето url; CC BY-SA; ToS §1.G изисква и „Wikimapia.org“ с връзка към http://wikimapia.org",
      "licence": "CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)",
      "source": "wikimapia",
      "terms": "http://wikimapia.org/terms_reference.html §1.F (условията не посочват версия); creativecommons.org/licenses/by-sa/"
    },
    {
      "applies_to": "1 Feature с method=street_bounded_face (mladost2) — осите на четирите улици",
      "attribution": "© OpenStreetMap contributors · https://www.openstreetmap.org/copyright (ODbL)",
      "licence": "ODbL © OpenStreetMap contributors",
      "source": "openstreetmap",
      "terms": "https://www.openstreetmap.org/copyright (Open Database License 1.0; https://opendatacommons.org/licenses/odbl/1-0/)"
    }
  ],
  "lot": "Б1",
  "method_licence": {
    "human_polygon": "CC BY-SA с URI и обектен URL (амандамент №2 §3.8, допълнение към D2)",
    "human_polygons_union": "CC BY-SA като при human_polygon — обединение на два уикимапийски човешки полигона по решение на Петър (решения 4); частите с техните url-и и сурови хешове са в witnesses; геометрията се смята в EPSG:32635",
    "street_bounded_face": "ODbL © OpenStreetMap contributors — изричен подписан ключ по D2 (Б0 т. 3), само за mladost2"
  },
  "parent_child": [
    {
      "child": "abatko",
      "parent": "kk_konstantin_elena"
    },
    {
      "child": "druzhba",
      "parent": "asparuhovo"
    },
    {
      "child": "kaisieva",
      "parent": "vladislavovo"
    },
    {
      "child": "kokardzha_generic",
      "parent": "izgrev_kv"
    },
    {
      "child": "mladost1",
      "parent": "mladost"
    },
    {
      "child": "mladost2",
      "parent": "mladost"
    },
    {
      "child": "rozova_dolina",
      "parent": "asparuhovo"
    },
    {
      "child": "saltanat",
      "parent": "morska_gradina"
    },
    {
      "child": "vazrazhdane1",
      "parent": "vazrazhdane"
    },
    {
      "child": "vazrazhdane2",
      "parent": "vazrazhdane"
    },
    {
      "child": "vazrazhdane3",
      "parent": "vazrazhdane"
    }
  ],
  "parent_child_without_polygon": [],
  "plan": {
    "file": "Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md",
    "signed_block": "§6 Б0 т. 1–12 (подписан от Петър, 06.09.2026 вечерта)",
    "signed_body_commit": "42b2635",
    "signed_body_sha256": "4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766"
  },
  "precision_floor_m": 50,
  "precision_m_by_method": {
    "human_polygon": 100,
    "human_polygons_union": 100,
    "street_bounded_face": 50
  },
  "publication": "Геометрия НИКОГА не пътува публично (G29). Публично излизат само име, код и src на квартала, плюс реда за атрибуция по ToS §1.G / ODbL §4.3.",
  "registry_pending": [
    {
      "code": "akchelar_vinitsa_seam",
      "display": "Акчелар-виница",
      "kind": "местност",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "borovets",
      "display": "Боровец",
      "kind": "с.о.",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "byalata_cheshma",
      "display": "с.о. Бялата чешма и Дъбравата",
      "kind": "с.о.",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "deli_sava",
      "display": "с.о. Дели Сава",
      "kind": "с.о.",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "franga_kokardzha_seam",
      "display": "местност Франга Дере И Кокарджа",
      "kind": "местност",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "gabena",
      "display": "Гъбена махала",
      "kind": "махала",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "golyama_kokardzha",
      "display": "м. Голяма Кокарджа",
      "kind": "местност",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "malka_kokardzha",
      "display": "м. Малка Кокарджа",
      "kind": "местност",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "mikro8",
      "display": "8 микрорайон",
      "kind": "мр",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "pz_metro",
      "display": "ПЗ Метро",
      "kind": "пз",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "salzitsa",
      "display": "с.о. Сълзица",
      "kind": "с.о.",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "shashkana",
      "display": "м-т Шашкъна",
      "kind": "м-т",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "so_planova",
      "display": "с.о. Планова",
      "kind": "с.о.",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "trakata_so",
      "display": "с.о. Траката",
      "kind": "со",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "trakata_vz",
      "display": "в.з. Траката",
      "kind": "вз",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    },
    {
      "code": "yuzhna_pz",
      "display": "Южна промишлена зона",
      "kind": "зона",
      "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"
    }
  ],
  "rows_without_feature": {
    "alias_of": [
      {
        "alias_of": "sredna_traka",
        "code": "vayalar",
        "why": "„пишем го Средна Трака“ — Ваялар става второ име на Средна Трака (промяна в регистъра, ход Р); полигон 5708971 остава на sredna_traka"
      }
    ],
    "deferred": [
      {
        "code": "bokluk_tarla",
        "why": "отложен на борда"
      },
      {
        "code": "botanicheska",
        "why": "отложен на борда"
      },
      {
        "code": "malka_chaika",
        "why": "отложен на борда"
      },
      {
        "code": "mikro4",
        "why": "отложен на борда"
      },
      {
        "code": "starite_lozya",
        "why": "отложен на борда"
      },
      {
        "code": "vilite",
        "why": "отложен на борда"
      }
    ]
  },
  "signature": {
    "basis": "подписът на плана (§6 Б0 т. 1–12) върху решенията по sha256 на блоба; signed_by в Feature-ите става валидно точно с този подпис (Б0 т. 1)",
    "commit_of_this_file_belongs_to": "Petar1984 (D16 / G4 — изпълнителят го оставя стейджнат)",
    "signed_at": "2026-09-06",
    "signed_by": "Petar"
  },
  "source_terms": {
    "openstreetmap": {
      "checked_on": "2026-09-06",
      "position": "Само осите на четирите улици са от OSM; карето е затворената лицева площ между тях. Публично пътува единствено името на квартала, никога геометрията; атрибуцията по §4.3 се носи от записа в quarter_attribution на доставката (Б0 т. 5).",
      "quote": "„OpenStreetMap® is open data, licensed under the Open Data Commons Open Database License (ODbL) by the OpenStreetMap Foundation (OSMF).“",
      "terms": "ODbL 1.0; §4.3 иска атрибуция „© OpenStreetMap contributors“ при всяко Produced Work",
      "url": "https://www.openstreetmap.org/copyright",
      "verdict": "allowed_with_conditions"
    },
    "wikimapia": {
      "checked_on": "2026-09-06",
      "position": "Присвояването на име по точка-в-полигон не е Adaptation по §1(b) на CC BY-SA — резултатът е факт (пространствено отношение) плюс предсъществуващо кратко име. Но ToS §1.G е ДОГОВОРНА клауза: публичната атрибуция е задължителна за всеки показан ред с уикимапийски квартал. Геометрия никога не пътува публично.",
      "quote": "§1.F „All User Submissions of all users and all Wikimapia Data are freely available for commercial and non-commercial use under Creative Commons license Attribution-ShareAlike…“ · §1.G „Public use of Wikimapia Data and it's derivatives requires special conditions: a. Link to Wikimapia data original url … b. Mention of \"Wikimapia.org\"…“",
      "terms": "CC BY-SA, версия непосочена в условията; §1.C.g забранява „unreasonable load“; §3 — услугата се предлага от САЩ",
      "url": "http://wikimapia.org/terms_reference.html",
      "verdict": "allowed_with_conditions"
    }
  },
  "union_crs": "EPSG:32635",
  "union_recipe": {
    "applies_to": [
      "dobreva"
    ],
    "authority": "projected",
    "crs": "EPSG:32635",
    "degree_space_diagnostic": {
      "max_vertex_delta_deg": 4.177e-07,
      "raw_geometry_sha256": "bc92a76c9c675e72fbb265c75d16fed8cf382401a5714716a483fe913fd0b8f3",
      "why": "unary_union направо в градуси дава ДРУГА геометрия: различават се И ДВАТА хеша, а най-голямата разлика по връх е 4,177e-07° (≈ 4,6 cm), не 1e-14°, както твърдеше по-ранният текст тук (Astra S23 F2). Освен това unary_union в градуси също минава през GEOS — не е „независимо от библиотеката“. Записано като диагностика; НЕ е втори допустим резултат.",
      "wm_polygon_sha256": "fc1f72976acece5386aa016f9baa495be976307d0f49c8c99ee1bb098fe733d3"
    },
    "determinism": "измерено 07.09: три повторения и обърнат ред на частите дават същия суров хеш; изходът няма поле с часовник, затова две сглобявания са байт-еднакви (G30/A18)",
    "libraries": {
      "GEOS": "3.13.1",
      "PROJ": "9.3.0",
      "pyproj": "3.6.1",
      "shapely": "2.1.2"
    },
    "projected_pin": {
      "raw_geometry_sha256": "d6f367bdf56671bf6ff2d59d587a6235d8f0cb34be4396ebe78ea8949f537014",
      "why": "това е пинът в решенията и геометрията във файла на борда — авторитетът; A9 спира сглобяването при всеки друг резултат",
      "wm_polygon_sha256": "b42a74d1177406d4f27182798d65356b337689a611e4c1fe07c6b07f8eaec7f8"
    },
    "steps": [
      "1. shapely.geometry.shape върху всяка част; невалиден пръстен → shapely.validation.make_valid",
      "2. pyproj Transformer EPSG:4326 → EPSG:32635 (always_xy=True) върху всяка част",
      "3. shapely.ops.unary_union върху проектираните части",
      "4. MultiPolygon → най-голямата по площ част (правилото на плана); друг тип → спиране",
      "5. Transformer EPSG:32635 → EPSG:4326 (always_xy=True) обратно",
      "6. mapping() → списъци (json round trip), после двата хеша на Б0 т. 2"
    ],
    "witness_file": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/unions_2026-09-07.geojson",
    "witness_file_sha256": "0fe781500725d78f46b9f931b66ad0267f782413f2c47f28a7669b68d1504080",
    "witness_state": "свидетел: преизчисленото обединение срещу файла на борда"
  },
  "union_witness": {
    "by_code": {
      "dobreva": "d6f367bdf56671bf6ff2d59d587a6235d8f0cb34be4396ebe78ea8949f537014"
    },
    "state": "свидетел: преизчисленото обединение срещу файла на борда"
  }
}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -Encoding UTF8 -LiteralPath tests/test_quarters_signed_fixtures.py | Select-Object -First 150 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }; rg -n --max-count 20 --max-columns 200 '"'"'^(def |SIGNED_|DEFAULT_|MAX_|PLAN_|DECISIONS_)|write|mkdir|open'"\\(' src/qa_quarters_signed.py" in C:\git\varna_3d
 succeeded in 76ms:
1: """Lot Б1 — the gate is only a gate if its negative fixtures have actually run and
2: actually failed.  This test runs every one of them, as a subprocess, and records
3: the exit code.
4: 
5:     python -m unittest discover -s tests -t tests
6: 
7: (`-t tests`, not `-t .`: `tests/` deliberately carries no `__init__.py`, so it is the
8: top level of its own discovery — the write-set of the lot stays exactly the five
9: files the plan names.)
10: 
11: Green means:
12:   * `src/qa_quarters_signed.py` exits 0 on the real `data/quarters_signed.geojson`;
13:   * every fixture in `tests/fixtures/qa_quarters_signed/` makes it exit != 0, and
14:     the failure names the check it was built to break;
15:   * the input-side fixtures — a moved vertex in each of the three geometry inputs and
16:     two schema-valid resolutions files (decision 9) that must not be honoured — make
17:     `src/build_quarters_signed.py` exit != 0;
18:   * a fresh assembly into a temporary directory is byte-identical to the file on
19:     disk (G30 determinism), so the artefact can be rebuilt from its inputs.
20: 
21: The fixtures are regenerated here from the tracked code, never committed
22: (`.gitignore:23` — `*.geojson`), so the write-set of the lot stays exhaustive.
23: """
24: from __future__ import annotations
25: 
26: import hashlib
27: import json
28: import shutil
29: import subprocess
30: import sys
31: import tempfile
32: import unittest
33: from pathlib import Path
34: 
35: ROOT = Path(__file__).resolve().parent.parent
36: FIXTURES = ROOT / "tests" / "fixtures" / "qa_quarters_signed"
37: ARTIFACT = ROOT / "data" / "quarters_signed.geojson"
38: REGISTRY = "C:/git/Varna_buildings/config/quarter_registry.json"
39: FIRE_VARNA = Path("C:/git/Fire_Varna")
40: 
41: BOUNDARY = FIRE_VARNA / "scratch" / "boundary_gallery"
42: FROZEN = BOUNDARY / "frozen_2026-09-06" / "wikimapia_quarters_2026-09-06_v2.geojson"
43: RAW_SNAPSHOT = BOUNDARY / "frozen_2026-09-06" / "wikimapia_varna_places_raw_2026-09-06.json"
44: EXTRA = BOUNDARY / "granitsi_preview_05.09" / "wikimapia_extra_2026-09-06.geojson"
45: MLADOST2 = BOUNDARY / "granitsi_preview_05.09" / "mladost2_streets_proposal.geojson"
46: UNIONS_FILE = BOUNDARY / "granitsi_preview_05.09" / "unions_2026-09-07.geojson"
47: 
48: # The three signatures this artefact hangs on, written out here on purpose: the test
49: # must fail if any of them drifts in the code, not quote the code back at itself.
50: # Astra S23 F1: the FINAL blob — the body plus the `attribution` field of Б0.8.  The
51: # earlier blob (`2c650160…`, 895e0d2) is the one S23 read; a signature on it would not
52: # be a signature on this file.
53: DECISIONS_BLOB_SHA256 = "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b"
54: PLAN_BODY_SHA256 = "4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766"
55: UNION_RAW_SHA256 = "d6f367bdf56671bf6ff2d59d587a6235d8f0cb34be4396ebe78ea8949f537014"
56: UNION_D1_SHA256 = "b42a74d1177406d4f27182798d65356b337689a611e4c1fe07c6b07f8eaec7f8"
57: DEGREE_UNION_RAW_SHA256 = "bc92a76c9c675e72fbb265c75d16fed8cf382401a5714716a483fe913fd0b8f3"
58: AU5_SHA256 = "78a2de59600eb103719ca072b3963c6b7195598a65a66e4653c7cd53c966c669"
59: # Decision 9 (Petar, 07.09): the signed file that closes the two disagreements.  Its
60: # sha256 is written out here as well — the artefact, the gate and this test must all
61: # be talking about the same signed bytes.
62: RESOLUTIONS_FILE = FIRE_VARNA / "scratch" / "places_search" / "district_resolutions_2026-09-07.json"
63: RESOLUTIONS_SHA256 = "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc"
64: RESOLVED_DISTRICT_SRC = "agkk_au5_confirmed_by_petar"
65: # S23 F3: the two disagreements between our district and the АГКК witness, by name —
66: # each now RESOLVED by that signed file (`ours` keeps naming what our layer says, so
67: # the disagreement stays visible; the district written is the АГКК one).
68: EXPECTED_DISPUTES = [
69:     {"agkk": "10135-03", "code": "kochmar", "ours": "vladislav_varnenchik",
70:      "resolution": "petar_agkk"},
71:     {"agkk": "10135-03", "code": "vazrazhdane4", "ours": "vladislav_varnenchik",
72:      "resolution": "petar_agkk"},
73: ]
74: 
75: # fixture name → the check whose name must appear in the gate's output.
76: EXPECTED_CHECK = {
77:     "artifact_class_other": "C1",
78:     "decisions_sha_substituted": "C1",
79:     "bom_crlf_unsorted": "C2",
80:     "d1_field_missing": "C3",
81:     "drawn_by_filled_on_import": "C3",
82:     "d1_null_not_allowed": "C3",
83:     "declared_local_knowledge": "C3",
84:     "vertex_moved": "C4",
85:     "hash_raw_substituted": "C4",
86:     "hash_d1_substituted": "C5",
87:     "wm_id_substituted": "C6",
88:     "deferred_code_with_feature": "C7",
89:     "feature_without_row": "C7",
90:     "mladost2_missing": "C7",
91:     "code_outside_registry_pending": "C8",
92:     "bare_cc_by_sa": "C9",
93:     "missing_terms": "C9",
94:     "missing_attribution": "C10",
95:     "osm_code_with_wikimapia_string": "C10",
96:     "two_codes_one_geometry": "C11",
97:     "precision_missing": "C13",
98:     "precision_below_floor": "C13",
99:     "street_method_other_code": "C16",
100:     "parent_not_in_registry": "C14",
101:     "dag_pair_removed": "C17",
102:     "district_from_agkk": "C18",
103:     # Astra S22 F2 — the two weaknesses the gate used to let through.
104:     "plan_sha_zeroed": "C1",
105:     "district_spatially_wrong": "C18",
106:     # Decisions 4 — the union and the excluded code.
107:     "excluded_code_with_feature": "C7",
108:     "union_wm_ids_substituted": "C6",
109:     # Astra S23 F2 — the union pin, honestly declared and bound to its CRS.
110:     "degree_union_self_rehashed": "C4",
111:     "union_crs_substituted": "C19",
112:     # Astra S23 F3 — the independent АГКК AU5 district witness.
113:     "au5_crosswalk_swapped": "C20",
114:     "district_dispute_delisted": "C20",
115:     "third_dispute_unlisted": "C20",
116:     "au5_sha_substituted": "C20",
117:     # Decision 9 — the signed resolutions input.
118:     "resolutions_sha_substituted": "C20",
119:     "resolved_district_contradicts_au5": "C20",
120:     "resolution_without_dispute": "C20",
121: }
122: 
123: 
124: def run(args: list[str]) -> subprocess.CompletedProcess:
125:     return subprocess.run(
126:         [sys.executable] + args, cwd=str(ROOT), capture_output=True,
127:     )
128: 
129: 
130: def text_of(result: subprocess.CompletedProcess) -> str:
131:     return (result.stdout + result.stderr).decode("utf-8", "replace")
132: 
133: 
134: def gate(path: Path, extra: list[str] | None = None) -> subprocess.CompletedProcess:
135:     return run(["src/qa_quarters_signed.py", str(path), "--registry", REGISTRY]
136:                + (extra or []))
137: 
138: 
139: def build_args(out: Path, frozen: Path = FROZEN, mladost2: Path = MLADOST2,
140:                resolutions: Path | None = None) -> list[str]:
141:     return [
142:         "src/build_quarters_signed.py",
143:         "--frozen", str(frozen),
144:         "--raw-snapshot", str(RAW_SNAPSHOT),
145:         "--extra", str(EXTRA),
146:         "--mladost2", str(mladost2),
147:         "--out", str(out),
148:     ] + (["--district-resolutions", str(resolutions)] if resolutions else [])
149: 
150: 
18:`.gitignore:23` (`*.geojson`) keeps them untracked, so the write-set of the lot stays
99:SIGNED_UNION_CRS = "EPSG:32635"
100:SIGNED_UNION_RAW_SHA256 = "d6f367bdf56671bf6ff2d59d587a6235d8f0cb34be4396ebe78ea8949f537014"
101:SIGNED_UNION_D1_SHA256 = "b42a74d1177406d4f27182798d65356b337689a611e4c1fe07c6b07f8eaec7f8"
137:DEFAULT_FROZEN = ("C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/"
143:def bad(check: str, message: str) -> None:
149:def check_artifact_class(meta: dict) -> None:
179:def check_bytes(path: Path, document: dict) -> None:
191:def check_d1_schema(features: list) -> None:
221:def check_hashes_raw(features: list, rows_by_code: dict) -> None:
240:def check_hashes_d1(features: list) -> None:
252:def check_wm_id(features: list, rows_by_code: dict) -> None:
290:def check_bijection(features: list, rows: list, meta: dict) -> None:
325:def check_registry(meta: dict, registry: dict, rows: list) -> None:
346:def check_licence(features: list, meta: dict) -> None:
371:def check_attribution(features: list, meta: dict) -> None:
393:def check_unique_geometry(features: list) -> None:
414:def check_decisions_clean(decisions_doc, where: str) -> None:
434:def check_precision(features: list) -> None:
452:def check_method(features: list) -> None:

codex
Staged е само `data/quarters_signed.geojson`; има и несвързани unstaged/untracked файлове, които оставям непокътнати. Тестовият код вече pin-ва final decisions blob-а и съдържа отрицателните случаи за union и AU5; сега проверявам изпълнението им и точните staged bytes.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import subprocess,hashlib,json,pathlib
p='data/quarters_signed.geojson'; b=subprocess.check_output(['git','cat-file','blob',':'+p]); d=json.loads(b); m=d['_meta']
print('STAGED',len(b),hashlib.sha256(b).hexdigest(),'features',len(d['features']),'worktree_equal',pathlib.Path(p).read_bytes()==b)
print('META_KEYS',list(m))
for k in m:
 if k not in ['deferred_registry_codes','registry_missing_codes','rows_without_feature','source_terms','dag','attribution','union_recipe','union_witness']:
  s=json.dumps(m[k],ensure_ascii=False)
  print(k,s if len(s)<5500 else s[:800]+' ...')
'@ | python -" in C:\git\varna_3d
 exited 1 in 127ms:
✗ A1 блоб на решенията: git show 3d747d3308bf31fe17add9a510ad97423adc672a:scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json падна (fatal: detected dubious ownership in repository at 'C:/git/Fire_Varna'
'C:/git/Fire_Varna' is owned by:
	BUILTIN/Administrators (S-1-5-32-544)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/Fire_Varna)

 succeeded in 154ms:
STAGED 301917 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3 features 60 worktree_equal True
META_KEYS ['artifact_class', 'attribution', 'canonicalization', 'counts', 'd1_schema', 'decisions_author', 'decisions_based_on', 'decisions_blob_before_attribution', 'decisions_commit', 'decisions_path', 'decisions_sha256', 'decisions_sha256_rule', 'decisions_sha256_worktree', 'declared_deviations', 'district_resolutions', 'district_witness_agkk', 'district_witness_disputes', 'excluded', 'generated_by', 'inputs', 'licences', 'lot', 'method_licence', 'parent_child', 'parent_child_without_polygon', 'plan', 'precision_floor_m', 'precision_m_by_method', 'publication', 'registry_pending', 'rows_without_feature', 'signature', 'source_terms', 'union_crs', 'union_recipe', 'union_witness']
artifact_class "signed_by_plan_signature"
canonicalization {"bytes": "UTF-8 без BOM, sorted keys, compact, финален LF (G30); две сглобявания са байт-еднакви", "raw_geometry_sha256": "sha256 на компактния {\"type\",\"coordinates\"} — правилото, което вече е в решенията (пренесено по Б0 т. 2)", "wm_polygon_sha256": "канонизацията на D1 по Б0 т. 2: 6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; вътрешните по часовника; MultiPolygon по амандамент №2 §4"}
counts {"choice_alias_of": 1, "choice_declared_streets": 1, "choice_deferred": 6, "choice_excluded": 1, "choice_wikimapia": 58, "choice_wikimapia_union": 1, "decisions_rows": 68, "features": 60, "features_with_our_district": 58, "features_with_resolved_district": 2, "registry_entries": 84, "registry_pending": 16}
d1_schema {"fields": ["code", "name", "kind", "parent", "source", "signed_by", "drawn_by", "approved_by", "drawn_at", "approved_at", "method", "basemap", "precision_m", "version", "license", "viewport", "visible_layers", "screenshot_sha256", "approval_digest", "witnesses", "note"], "nulled_on_import": ["drawn_by", "drawn_at", "basemap", "viewport", "visible_layers", "screenshot_sha256", "approval_digest"], "why": "Б0 т. 1 (подписан): за Feature със source ∈ {wikimapia, declared_streets} седемте полета на ръката са null по договор — взаимна изключителност „или ръка, или внос“. Дайджестът на D1 се замества от sha-веригата на Б0 т. 8: решения по sha → Feature с wm_polygon_sha256 → _meta.decisions_sha256."}
decisions_author "Claude Architect (тялото на решенията, 895e0d2) → Claude Executor (полето attribution по Б0.8, 3d747d3)"
decisions_based_on {"file": "granitsi_decisions_3_2026-09-06_proba.json", "rev": "b6e627d0fb19e039a062aba955d030301ae45b2e", "sha256": "ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6"}
decisions_blob_before_attribution {"rev": "895e0d2651aac73516659f2a10ea5193b2be5d53", "sha256": "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89", "why": "тялото без полето attribution (Б0.8 го изисква); прегледано от Astra S23. Подписът на Петър е върху окончателния блоб, не върху този."}
decisions_commit "3d747d3308bf31fe17add9a510ad97423adc672a"
decisions_path "scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json"
decisions_sha256 "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b"
decisions_sha256_rule "sha256 на БЛОБА (git show <rev>:<път>), не на работното копие — Б0 т. 8"
decisions_sha256_worktree {"bytes": 32983, "note": "работното копие е CRLF; подписан е БЛОБЪТ (Б0 т. 8), не този файл", "path": "C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json", "sha256": "fdb748bcb76cf6458be3ad0e8decf495ca954fdd4f62f4aea7ea1aee3d608f4f"}
declared_deviations [{"what": "choice: „wikimapia_union“ за кода dobreva (решения 4, Петър 07.09)", "why": "Площта, която Уикимапия нарича „Виница - север“ (5729421), е част от Добрева чешма — границата е обединението на двата човешки полигона. Обединението се смята в UTM 35N (EPSG:32635) и се връща в WGS84: така се възпроизвежда БАЙТ ПО БАЙТ пинът в решенията (d6f367bd…), който Петър видя. Обединение направо в градуси дава ДРУГА геометрия — различават се и двата хеша (bc92a76c… / fc1f7297…), а най-голямата разлика по връх е 4,177e-07° (≈ 4,6 cm), НЕ 1e-14°, както твърдеше по-ранният текст тук (поправено по Astra S23 F2). A9 отказва всеки друг резултат; рецептата и точните версии на shapely/GEOS/pyproj/PROJ са в _meta.union_recipe."}, {"what": "полето url на обединения Feature", "why": "Обединението има два изворни обекта. `url` носи ПЪРВИЯ от реда (този, чието име носи кодът), а всички обекти с техните url-и и собствени сурови хешове са в `witnesses` — ToS §1.G се изпълнява от реда за атрибуция плюс свидетелите."}, {"what": "choice: „excluded“ за кода vinitsa_sever", "why": "Петър (07.09): кодът отпада като квартал — няма Feature, редът е поименно в `_meta.excluded`. Деактивирането в quarter_registry.json е негов сутрешен ход: регистърът НЕ се пипа тук (червена черта 3 на плана), затова кодът остава в registry_entries и НЕ е в registry_pending (той ИМА решение)."}, {"what": "полето district в Feature-ите", "why": "Б0 т. 4 иска районът да е изведен по представителна точка срещу НАШИТЕ пет района, не от АГКК INSPIRE (G22 остава заключен). Затова слоят с петте административни граници влиза като назован вход, а АГКК остава само свидетел в _meta.district_witness_agkk."}, {"what": "районът на кодовете в _meta.district_resolutions.applied (district_src = agkk_au5_confirmed_by_petar)", "why": "Решение 9 (Петър, 07.09: „Кочмар и Възраждане 4 не са във Владиславово“). Само за поименно решените кодове районът НЕ идва от нашия слой, а от официалната граница на АГКК AU5, потвърдена от Петър; входът е подписан файл без геометрия, закотвен по sha256 в _meta.inputs. Спорът остава записан в _meta.district_witness_disputes с resolution petar_agkk — решението не трие разминаването, а го затваря. Всяко НЕрешено разминаване остава pending_petar."}, {"what": "входният етикет source: declared_local_knowledge на карето „Младост 2“", "why": "Отменен от амандамент №2 §3.7; НЕ пътува в изхода. Изходният Feature носи source: declared_streets и лиценз ODbL по подписания ключ на Б0 т. 3."}, {"what": "затвореният набор properties е 21 полета на D1 + 19 назовани провенанс-полета", "why": "Г2-в на амандамент №2 §4 изисква geometry_origin/imported_from/fetched_at/chosen_source/chosen_reason/confirmed_by/confirmed_at; Б0 т. 2 изисква двата хеша поотделно; G27(а) изисква реда за атрибуция. Наборът е затворен — непознат ключ спира сглобяването."}]
district_resolutions {"applied": [{"agkk": "10135-03", "basis": "agkk_au5 10135-03", "code": "kochmar", "district": "mladost", "was": "vladislav_varnenchik"}, {"agkk": "10135-03", "basis": "agkk_au5 10135-03", "code": "vazrazhdane4", "district": "mladost", "was": "vladislav_varnenchik"}], "district_src": "agkk_au5_confirmed_by_petar", "path": "C:/git/Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json", "rule": "подписаният файл може да реши САМО спор, който съществува, и САМО в посоката на свидетеля АГКК AU5; всичко друго спира сглобяването (A22) и пада на гейта (C18/C20). Нерешените разминавания остават pending_petar.", "sha256": "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc", "signed_at": "2026-09-07T00:10:58+03:00", "signed_by": "Petar via Claude Architect (words 07.09: Кочмар и Възраждане 4 не са във Владиславово)"}
district_witness_agkk {"by_code": {"abatko": "10135-02", "akchelar": "10135-02", "alen_mak": "10135-02", "asparuhovo": "10135-05", "balam_dere": "10135-04", "borovets_sever": "10135-05", "borovets_yug": "10135-05", "briz": "10135-02", "chaika_kk": "10135-02", "chaika_kv": "10135-02", "dobreva": "10135-02", "dolna_traka": "10135-02", "druzhba": "10135-05", "evksinograd": "10135-02", "fichoza": "10135-05", "galata": "10135-05", "gorchivata_cheshma": "10135-02", "gorna_traka": "10135-02", "grackata_mahala": "10135-01", "hristo_botev": "10135-01", "izgrev_kv": "10135-02", "kaisieva": "10135-04", "kk_konstantin_elena": "10135-02", "kochmar": "10135-03", "kokardzha_generic": "10135-02", "kolhozen_pazar": "10135-01", "kv_levski": "10135-02", "maksuda": "10135-03", "manastirski_rid": "10135-02", "menteshe": "10135-04", "mladost": "10135-03", "mladost1": "10135-03", "mladost2": "10135-03", "morska_gradina": "10135-02", "pchelina": "10135-03", "perchemliyata": "10135-02", "pobeda": "10135-03", "priboy": "10135-05", "pz_planova": "10135-04", "rakitnika": "10135-05", "rozova_dolina": "10135-05", "saltanat": "10135-02", "sotira": "10135-02", "sredna_traka": "10135-02", "sv_ivan_rilski": "10135-03", "sveti_nikola": "10135-02", "trakia": "10135-01", "troshevo": "10135-03", "tsentar": "10135-01", "tv_kula": "10135-02", "vazrazhdane": "10135-03", "vazrazhdane1": "10135-03", "vazrazhdane2": "10135-03", "vazrazhdane3": "10135-03", "vazrazhdane4": "10135-03", "vinitsa": "10135-02", "vladislavovo": "10135-04", "zelenika": "10135-05", "zlatni_pyasatsi": "10135-02", "zpz": "10135-03"}, "crosswalk": {"10135-01": "odesos", "10135-02": "primorski", "10135-03": "mladost", "10135-04": "vladislav_varnenchik", "10135-05": "asparuhovo"}, "crosswalk_why": "подписаният превод национален код → нашите пет; АГКК НИКОГА не пише район (G22 заключен) — служи само за независимо свидетелство", "disputes": 2, "inside_one_district": 60, "outside_all": 0, "state": "свидетел: представителна точка на Feature-а срещу АГКК AU5"}
district_witness_disputes [{"agkk": "10135-03", "code": "kochmar", "ours": "vladislav_varnenchik", "resolution": "petar_agkk"}, {"agkk": "10135-03", "code": "vazrazhdane4", "ours": "vladislav_varnenchik", "resolution": "petar_agkk"}]
excluded [{"code": "vinitsa_sever", "display": "с.о. Виница-север", "kind": "с.о.", "registry_action": "сутрешен ход на Петър: деактивиране на кода в quarter_registry.json — регистърът НЕ се пипа от изпълнителя", "why": "Петър (07.09): „Виница-север го изключваме“ — кодът отпада от регистъра като квартал/с.о. (ход Р: деактивиране), не е второ име; площта е Добрева чешма"}]
generated_by "Claude Executor"
inputs [{"bytes": 32129, "id": "decisions_4", "path": "Fire_Varna:3d747d3308bf31fe17add9a510ad97423adc672a:scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json", "role": "решенията — подписани по sha256 на блоба (Б0 т. 8); четени от git, не от работното копие", "sha256": "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b"}, {"bytes": 589222, "id": "frozen_v2", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson", "role": "замразеният уикимапийски набор — изворът на единичните геометрии и на двете части на обединението", "sha256": "b53a3322b1a6e5670ea17f7638ab77d198e120d108e623fa7bc78ae702daf976"}, {"bytes": 3713, "id": "wikimapia_extra_5729429", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/wikimapia_extra_2026-09-06.geojson", "role": "обектът 5729429 (Евксиноград/Траката), подаден от Петър след замразяването", "sha256": "b220423c6f954405fb0dbf94621fab30a8b6585e7156089c67e14dfa41382dd8"}, {"bytes": 5071516, "id": "raw_snapshot", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/wikimapia_varna_places_raw_2026-09-06.json", "role": "суровият отговор на обхода — raw_response_sha256 в witnesses на уикимапийските Feature-и", "sha256": "1c0561cb7e612e72f291ca33d603cc6ef7713b88ab5af7cbd6d942fbc18a7fbe"}, {"bytes": 2971, "id": "mladost2_face", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/mladost2_streets_proposal.geojson", "role": "карето „Младост 2“ по четирите улици (оси от OSM) — подписаният ключ на Б0 т. 3", "sha256": "66fd3f57f76d4f104911dc2f7576f33e678435b6e1156a19d61c0bf34030f5b8"}, {"bytes": 52299, "id": "quarter_registry", "path": "C:/git/Varna_buildings/config/quarter_registry.json", "role": "регистърът — имена, вид и родство; ЧЕТЕН, никога пипан (червена черта 3)", "sha256": "7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6"}, {"bytes": 201130, "id": "our_districts", "path": "C:/git/m6000_private/number_viewer/quarters_layer.geojson", "role": "нашите пет административни района (слоят за сравнение на fire_varna_locations) — изворът на полето district по Б0 т. 4", "sha256": "26e39b001ce151203058d70bc53367a5b40c77c4b0dd7113cf2a7085c376cc22"}, {"bytes": 61469, "id": "agkk_au5", "path": "C:/git/Fire_Varna/scratch/places_search/agkk_inspire_2026-09-05/agkk_au5_varna.geojson", "role": "петте района на АГКК INSPIRE — САМО свидетел (G22 остава заключен, Б0 т. 4)", "sha256": "78a2de59600eb103719ca072b3963c6b7195598a65a66e4653c7cd53c966c669"}, {"bytes": 513, "id": "district_resolutions", "path": "C:/git/Fire_Varna/scratch/places_search/district_resolutions_2026-09-07.json", "role": "подписаните решения по спорове за района (решение 9, Петър 07.09) — без геометрия; изворът на district_src=agkk_au5_confirmed_by_petar", "sha256": "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc", "signed_at": "2026-09-07T00:10:58+03:00", "signed_by": "Petar via Claude Architect (words 07.09: Кочмар и Възраждане 4 не са във Владиславово)"}, {"bytes": 3921, "id": "unions_2026-09-07", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/unions_2026-09-07.geojson", "role": "обединенията, както Петър ги видя — САМО свидетел; геометрията се преизчислява от замразения набор и сверява байт по байт срещу него", "sha256": "0fe781500725d78f46b9f931b66ad0267f782413f2c47f28a7669b68d1504080"}]
licences [{"applies_to": "58 Feature-а с method=human_polygon и 1 с method=human_polygons_union (обединение на човешки полигони — същият извор, същият лиценз)", "attribution": "Граница по Wikimapia.org (© Wikimapia contributors) — връзка към обекта в полето url; CC BY-SA; ToS §1.G изисква и „Wikimapia.org“ с връзка към http://wikimapia.org", "licence": "CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)", "source": "wikimapia", "terms": "http://wikimapia.org/terms_reference.html §1.F (условията не посочват версия); creativecommons.org/licenses/by-sa/"}, {"applies_to": "1 Feature с method=street_bounded_face (mladost2) — осите на четирите улици", "attribution": "© OpenStreetMap contributors · https://www.openstreetmap.org/copyright (ODbL)", "licence": "ODbL © OpenStreetMap contributors", "source": "openstreetmap", "terms": "https://www.openstreetmap.org/copyright (Open Database License 1.0; https://opendatacommons.org/licenses/odbl/1-0/)"}]
lot "Б1"
method_licence {"human_polygon": "CC BY-SA с URI и обектен URL (амандамент №2 §3.8, допълнение към D2)", "human_polygons_union": "CC BY-SA като при human_polygon — обединение на два уикимапийски човешки полигона по решение на Петър (решения 4); частите с техните url-и и сурови хешове са в witnesses; геометрията се смята в EPSG:32635", "street_bounded_face": "ODbL © OpenStreetMap contributors — изричен подписан ключ по D2 (Б0 т. 3), само за mladost2"}
parent_child [{"child": "abatko", "parent": "kk_konstantin_elena"}, {"child": "druzhba", "parent": "asparuhovo"}, {"child": "kaisieva", "parent": "vladislavovo"}, {"child": "kokardzha_generic", "parent": "izgrev_kv"}, {"child": "mladost1", "parent": "mladost"}, {"child": "mladost2", "parent": "mladost"}, {"child": "rozova_dolina", "parent": "asparuhovo"}, {"child": "saltanat", "parent": "morska_gradina"}, {"child": "vazrazhdane1", "parent": "vazrazhdane"}, {"child": "vazrazhdane2", "parent": "vazrazhdane"}, {"child": "vazrazhdane3", "parent": "vazrazhdane"}]
parent_child_without_polygon []
plan {"file": "Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md", "signed_block": "§6 Б0 т. 1–12 (подписан от Петър, 06.09.2026 вечерта)", "signed_body_commit": "42b2635", "signed_body_sha256": "4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766"}
precision_floor_m 50
precision_m_by_method {"human_polygon": 100, "human_polygons_union": 100, "street_bounded_face": 50}
publication "Геометрия НИКОГА не пътува публично (G29). Публично излизат само име, код и src на квартала, плюс реда за атрибуция по ToS §1.G / ODbL §4.3."
registry_pending [{"code": "akchelar_vinitsa_seam", "display": "Акчелар-виница", "kind": "местност", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "borovets", "display": "Боровец", "kind": "с.о.", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "byalata_cheshma", "display": "с.о. Бялата чешма и Дъбравата", "kind": "с.о.", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "deli_sava", "display": "с.о. Дели Сава", "kind": "с.о.", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "franga_kokardzha_seam", "display": "местност Франга Дере И Кокарджа", "kind": "местност", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "gabena", "display": "Гъбена махала", "kind": "махала", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "golyama_kokardzha", "display": "м. Голяма Кокарджа", "kind": "местност", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "malka_kokardzha", "display": "м. Малка Кокарджа", "kind": "местност", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "mikro8", "display": "8 микрорайон", "kind": "мр", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "pz_metro", "display": "ПЗ Метро", "kind": "пз", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "salzitsa", "display": "с.о. Сълзица", "kind": "с.о.", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "shashkana", "display": "м-т Шашкъна", "kind": "м-т", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "so_planova", "display": "с.о. Планова", "kind": "с.о.", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "trakata_so", "display": "с.о. Траката", "kind": "со", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "trakata_vz", "display": "в.з. Траката", "kind": "вз", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}, {"code": "yuzhna_pz", "display": "Южна промишлена зона", "kind": "зона", "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)"}]
signature {"basis": "подписът на плана (§6 Б0 т. 1–12) върху решенията по sha256 на блоба; signed_by в Feature-ите става валидно точно с този подпис (Б0 т. 1)", "commit_of_this_file_belongs_to": "Petar1984 (D16 / G4 — изпълнителят го оставя стейджнат)", "signed_at": "2026-09-06", "signed_by": "Petar"}
union_crs "EPSG:32635"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=150; Get-Content -Encoding UTF8 -LiteralPath tests/test_quarters_signed_fixtures.py | Select-Object -Skip 150 -First 145 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\varna_3d
 succeeded in 71ms:
151: class SignedQuartersFixtures(unittest.TestCase):
152:     @classmethod
153:     def setUpClass(cls) -> None:
154:         if not ARTIFACT.exists():
155:             raise unittest.SkipTest(f"липсва {ARTIFACT} — лот Б1 не е сглобен")
156:         if FIXTURES.exists():
157:             shutil.rmtree(FIXTURES)
158:         made = run(["src/qa_quarters_signed.py", str(ARTIFACT),
159:                     "--registry", REGISTRY, "--make-fixtures"])
160:         if made.returncode != 0:
161:             raise AssertionError(f"генерирането на фикстурите падна:\n{text_of(made)}")
162: 
163:     def test_gate_is_green_on_the_signed_artifact(self) -> None:
164:         result = gate(ARTIFACT)
165:         self.assertEqual(result.returncode, 0, text_of(result))
166: 
167:     def test_artifact_carries_the_signed_shape(self) -> None:
168:         document = json.loads(ARTIFACT.read_bytes().decode("utf-8"))
169:         meta = document["_meta"]
170:         self.assertEqual(meta["artifact_class"], "signed_by_plan_signature")
171:         # Decisions 4: 58 single Wikimapia polygons + 1 union + Младост 2.
172:         self.assertEqual(len(document["features"]), 60)
173:         methods = [f["properties"]["method"] for f in document["features"]]
174:         self.assertEqual(methods.count("street_bounded_face"), 1)
175:         self.assertEqual(methods.count("human_polygon"), 58)
176:         self.assertEqual(methods.count("human_polygons_union"), 1)
177:         self.assertEqual(meta["decisions_sha256"], DECISIONS_BLOB_SHA256)
178:         self.assertEqual(meta["plan"]["signed_body_sha256"], PLAN_BODY_SHA256)
179:         self.assertEqual([item["code"] for item in meta["excluded"]], ["vinitsa_sever"])
180:         self.assertNotIn("vinitsa_sever", {f["properties"]["code"] for f in document["features"]})
181: 
182:     def test_the_union_is_the_geometry_petar_signed(self) -> None:
183:         """The pin travels: decisions row → Feature → the union file of the board."""
184:         document = json.loads(ARTIFACT.read_bytes().decode("utf-8"))
185:         union = [f for f in document["features"]
186:                  if f["properties"]["method"] == "human_polygons_union"]
187:         self.assertEqual(len(union), 1)
188:         props = union[0]["properties"]
189:         self.assertEqual(props["code"], "dobreva")
190:         self.assertEqual(props["wm_ids"], [5729380, 5729421])
191:         self.assertIsNone(props["wm_id"])
192:         self.assertEqual(props["raw_geometry_sha256"], UNION_RAW_SHA256)
193:         self.assertEqual(props["precision_m"], 100)
194:         self.assertEqual(len(props["witnesses"]), 2)
195:         witness = json.loads(UNIONS_FILE.read_bytes().decode("utf-8"))["features"][0]
196:         self.assertEqual(witness["properties"]["wm_polygon_sha256"], UNION_RAW_SHA256)
197: 
198:     def test_union_recipe_is_declared_honestly(self) -> None:
199:         """Astra S23 F2: the projected union is the authority, the degree-space one is a
200:         DIFFERENT geometry (both hash keys differ), and the library versions are named."""
201:         meta = json.loads(ARTIFACT.read_bytes().decode("utf-8"))["_meta"]
202:         self.assertEqual(meta["union_crs"], "EPSG:32635")
203:         recipe = meta["union_recipe"]
204:         self.assertEqual(recipe["crs"], "EPSG:32635")
205:         self.assertEqual(recipe["authority"], "projected")
206:         self.assertEqual(recipe["projected_pin"]["raw_geometry_sha256"], UNION_RAW_SHA256)
207:         self.assertEqual(recipe["projected_pin"]["wm_polygon_sha256"], UNION_D1_SHA256)
208:         self.assertEqual(recipe["degree_space_diagnostic"]["raw_geometry_sha256"],
209:                          DEGREE_UNION_RAW_SHA256)
210:         self.assertNotEqual(recipe["degree_space_diagnostic"]["raw_geometry_sha256"],
211:                             recipe["projected_pin"]["raw_geometry_sha256"])
212:         self.assertNotEqual(recipe["degree_space_diagnostic"]["wm_polygon_sha256"],
213:                             recipe["projected_pin"]["wm_polygon_sha256"])
214:         for name in ("shapely", "GEOS", "pyproj", "PROJ"):
215:             self.assertTrue(recipe["libraries"].get(name), f"липсва версията на {name}")
216:         self.assertEqual(
217:             recipe["witness_file_sha256"],
218:             hashlib.sha256(UNIONS_FILE.read_bytes()).hexdigest(),
219:             "рецептата не сочи файла с обединенията, който Петър видя",
220:         )
221: 
222:     def test_district_disputes_are_named_and_resolved_by_the_signed_file(self) -> None:
223:         """Astra S23 F3 + decision 9: the two disagreements with the АГКК witness stay
224:         NAMED, and both are closed by Petar's signed file — Кочмар and Възраждане 4 are
225:         written as Младост, with the provenance that says who decided it."""
226:         document = json.loads(ARTIFACT.read_bytes().decode("utf-8"))
227:         meta = document["_meta"]
228:         self.assertEqual(meta["district_witness_disputes"], EXPECTED_DISPUTES)
229:         self.assertEqual(meta["district_witness_agkk"]["crosswalk"]["10135-03"], "mladost")
230:         self.assertEqual(meta["district_witness_agkk"]["crosswalk"]["10135-04"],
231:                          "vladislav_varnenchik")
232:         by_code = {f["properties"]["code"]: f["properties"] for f in document["features"]}
233:         for row in EXPECTED_DISPUTES:
234:             props = by_code[row["code"]]
235:             self.assertEqual(props["district"], "mladost")
236:             self.assertNotEqual(props["district"], row["ours"])
237:             self.assertEqual(props["district_src"], RESOLVED_DISTRICT_SRC)
238:         pin = next(i for i in meta["inputs"] if i["id"] == "agkk_au5")
239:         self.assertEqual(pin["sha256"], AU5_SHA256)
240: 
241:     def test_the_resolutions_input_is_the_signed_file(self) -> None:
242:         """Decision 9 travels as a signed FILE, pinned by sha256: the bytes on disk, the
243:         pin in the manifest and the sha written out in this test are one and the same."""
244:         meta = json.loads(ARTIFACT.read_bytes().decode("utf-8"))["_meta"]
245:         self.assertEqual(hashlib.sha256(RESOLUTIONS_FILE.read_bytes()).hexdigest(),
246:                          RESOLUTIONS_SHA256)
247:         pin = next(i for i in meta["inputs"] if i["id"] == "district_resolutions")
248:         self.assertEqual(pin["sha256"], RESOLUTIONS_SHA256)
249:         block = meta["district_resolutions"]
250:         self.assertEqual(block["sha256"], RESOLUTIONS_SHA256)
251:         self.assertEqual(block["district_src"], RESOLVED_DISTRICT_SRC)
252:         self.assertEqual(
253:             [(r["code"], r["was"], r["district"], r["agkk"]) for r in block["applied"]],
254:             [("kochmar", "vladislav_varnenchik", "mladost", "10135-03"),
255:              ("vazrazhdane4", "vladislav_varnenchik", "mladost", "10135-03")])
256:         self.assertEqual(json.loads(RESOLUTIONS_FILE.read_bytes().decode("utf-8"))["schema_version"],
257:                          "1")
258: 
259:     def test_build_refuses_a_resolution_against_the_au5_witness(self) -> None:
260:         """A signed-looking file that decides a dispute AGAINST the witness it cites is
261:         a different decision — the build stops instead of writing it."""
262:         with tempfile.TemporaryDirectory() as tmp:
263:             made = run(build_args(Path(tmp) / "quarters_signed.geojson")
264:                        + ["--make-negative-fixtures", tmp])
265:             self.assertEqual(made.returncode, 0, text_of(made))
266:             broken = Path(tmp) / "resolutions_against_au5.json"
267:             result = run(build_args(Path(tmp) / "quarters_signed.geojson", resolutions=broken))
268:             self.assertNotEqual(result.returncode, 0, text_of(result))
269:             self.assertIn("A22", text_of(result))
270: 
271:     def test_build_refuses_a_resolution_for_a_code_without_a_dispute(self) -> None:
272:         with tempfile.TemporaryDirectory() as tmp:
273:             made = run(build_args(Path(tmp) / "quarters_signed.geojson")
274:                        + ["--make-negative-fixtures", tmp])
275:             self.assertEqual(made.returncode, 0, text_of(made))
276:             broken = Path(tmp) / "resolutions_without_dispute.json"
277:             result = run(build_args(Path(tmp) / "quarters_signed.geojson", resolutions=broken))
278:             self.assertNotEqual(result.returncode, 0, text_of(result))
279:             self.assertIn("A22", text_of(result))
280: 
281:     def test_gate_refuses_a_resolutions_file_against_the_au5_witness(self) -> None:
282:         """The gate does its own AU5 point-in-polygon: a resolutions file pointing
283:         anywhere else is red, whatever the artefact says."""
284:         with tempfile.TemporaryDirectory() as tmp:
285:             made = run(build_args(Path(tmp) / "quarters_signed.geojson")
286:                        + ["--make-negative-fixtures", tmp])
287:             self.assertEqual(made.returncode, 0, text_of(made))
288:             broken = Path(tmp) / "resolutions_against_au5.json"
289:             result = gate(ARTIFACT, ["--district-resolutions", str(broken)])
290:             output = text_of(result)
291:             self.assertNotEqual(result.returncode, 0, output)
292:             self.assertIn("C20", output)
293:             self.assertIn("приемаме само решение, съгласно с AU5", output)
294: 
295:     def test_gate_refuses_a_resolution_for_a_code_without_a_dispute(self) -> None:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=0; Get-Content -Encoding UTF8 -LiteralPath src/qa_quarters_signed.py | Select-Object -First 145 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }; rg -n --max-count 20 --max-columns 200 '"'"'^def |write|mkdir|--fixtures'"' src/qa_quarters_signed.py | Select-Object -Last 20" in C:\git\varna_3d
 succeeded in 63ms:
1: """Gate Б1 — judges `data/quarters_signed.geojson`, the SIGNED quarter boundaries.
2: 
3:     python src/qa_quarters_signed.py data/quarters_signed.geojson \
4:         --registry  C:/git/Varna_buildings/config/quarter_registry.json \
5:         --decisions-repo C:/git/Fire_Varna
6: 
7: Exit 0 means every check below passed.  Exit 1 names every failing check.
8: 
9: Pre-gates, run separately and recorded by their own exit code (plan §6 Б1):
10:   G19  "C:/Program Files/GitHub CLI/gh.exe" repo view Petar1984/varna_3d --json visibility  → PRIVATE
11:   G3   python src/qa_no_cad_ids.py
12: 
13: The negative fixtures live in `tests/fixtures/qa_quarters_signed/*.geojson` and are
14: produced by this same script:
15: 
16:     python src/qa_quarters_signed.py <файл> --registry … --make-fixtures
17: 
18: `.gitignore:23` (`*.geojson`) keeps them untracked, so the write-set of the lot stays
19: exhaustive and they are regenerated from this tracked code on demand.  A gate whose
20: negative fixture has not actually run and actually failed is not a gate — that is what
21: `tests/test_quarters_signed_fixtures.py` proves, one fixture at a time.
22: """
23: from __future__ import annotations
24: 
25: import argparse
26: import hashlib
27: import json
28: import re
29: import sys
30: from pathlib import Path
31: 
32: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
33: sys.stderr.reconfigure(encoding="utf-8", errors="replace")
34: 
35: SRC = Path(__file__).resolve().parent
36: sys.path.insert(0, str(SRC))
37: 
38: from build_quarters_candidate import (  # noqa: E402
39:     FORBIDDEN_DECISION_KEYS,
40:     LAT_MAX,
41:     LAT_MIN,
42:     LICENCE,
43:     LON_MAX,
44:     LON_MIN,
45:     RESIDENTIAL_KINDS,
46:     canonical_bytes,
47:     canonical_geometry_sha256,
48:     raw_geometry_sha256,
49: )
50: from build_quarters_signed import (  # noqa: E402
51:     ABOLISHED_SOURCE,
52:     ALL_FIELDS,
53:     ARTIFACT_CLASS,
54:     CHOICES,
55:     D1_FIELDS,
56:     D1_NULL_ON_IMPORT,
57:     D1_REQUIRED_NON_NULL,
58:     DECISIONS_BLOB_SHA256,
59:     DECISIONS_PATH,
60:     DECISIONS_REV,
61:     DEFAULT_DISTRICTS,
62:     EXCLUDED_CHOICE,
63:     METHOD_SOURCE,
64:     ODBL_LICENSE,
65:     PARENT_CHILD,
66:     PLAN,
67:     POLYGON_CHOICES,
68:     PRECISION_BY_METHOD,
69:     PRECISION_FLOOR_M,
70:     STREET_METHOD,
71:     STREET_METHOD_ONLY_CODE,
72:     UNION_METHOD,
73:     UNION_SOURCE,
74:     WIKIMAPIA_SOURCES,
75:     district_of,
76:     load_our_districts,
77:     read_decisions_blob,
78: )
79: from fire_varna_locations import DISTRICTS  # noqa: E402
80: 
81: CAD_ID = re.compile(r"\b\d{4,5}\.\d+\.\d+")
82: DISTRICT_CODES = {code for code, _ in DISTRICTS.values()}
83: LICENCE_BY_SOURCE = {"wikimapia": LICENCE, "declared_streets": ODBL_LICENSE,
84:                      UNION_SOURCE: LICENCE}
85: 
86: # ---------------------------------------------------------------------------
87: # Astra S23 — what this gate pins ITSELF, on purpose.
88: #
89: # These four blocks are NOT imported from the builder.  A gate that asks the code
90: # under test for its own expected answer is not a gate: substituting `UNION_CRS` in
91: # the builder would then pass, which is exactly the hole S23 F2 found.  They are
92: # written out here, and a drift on either side is a red gate.
93: # ---------------------------------------------------------------------------
94: 
95: # S23 F2 — the union recipe.  The PROJECTED union is the authority (it is the pin in
96: # the decisions and the geometry Petar looked at); the degree-space union is a
97: # different geometry, recorded only as a diagnostic.  Measured 07.09: the largest
98: # per-vertex difference is 4.177e-07°, not 1e-14°, and BOTH hash keys differ.
99: SIGNED_UNION_CRS = "EPSG:32635"
100: SIGNED_UNION_RAW_SHA256 = "d6f367bdf56671bf6ff2d59d587a6235d8f0cb34be4396ebe78ea8949f537014"
101: SIGNED_UNION_D1_SHA256 = "b42a74d1177406d4f27182798d65356b337689a611e4c1fe07c6b07f8eaec7f8"
102: DEGREE_UNION_RAW_SHA256 = "bc92a76c9c675e72fbb265c75d16fed8cf382401a5714716a483fe913fd0b8f3"
103: DEGREE_UNION_D1_SHA256 = "fc1f72976acece5386aa016f9baa495be976307d0f49c8c99ee1bb098fe733d3"
104: REQUIRED_LIBRARIES = ("GEOS", "PROJ", "pyproj", "shapely")
105: 
106: # S23 F3 — the independent district witness.  The АГКК INSPIRE AU5 layer by its own
107: # sha256, and the SIGNED crosswalk from its national codes to our five district codes.
108: AU5_PATH = ("C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/"
109:             "agkk_au5_varna.geojson")
110: AU5_SHA256 = "78a2de59600eb103719ca072b3963c6b7195598a65a66e4653c7cd53c966c669"
111: AU5_CROSSWALK = {
112:     "10135-01": "odesos",
113:     "10135-02": "primorski",
114:     "10135-03": "mladost",
115:     "10135-04": "vladislav_varnenchik",
116:     "10135-05": "asparuhovo",
117: }
118: DISPUTE_RESOLUTION = "pending_petar"
119: DISPUTE_FIELDS = ("agkk", "code", "ours", "resolution")
120: 
121: # Decision 9 (Petar, 07.09) — the SIGNED resolutions input.  Pinned here too, and NOT
122: # imported from the builder: the gate must be able to say „the artefact was built from
123: # the file Petar signed“ without asking the builder what it thinks that file is.
124: RESOLUTIONS_PATH = ("C:/git/Fire_Varna/scratch/places_search/"
125:                     "district_resolutions_2026-09-07.json")
126: RESOLUTIONS_SIGNED_SHA256 = "d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc"
127: RESOLUTIONS_SCHEMA_VERSION = "1"
128: RESOLUTION_RESOLVED = "petar_agkk"
129: RESOLVED_DISTRICT_SRC = "agkk_au5_confirmed_by_petar"
130: OUR_DISTRICT_SRC = "fire_varna_district"
131: DISTRICT_SRC_ALLOWED = (OUR_DISTRICT_SRC, RESOLVED_DISTRICT_SRC)
132: RESOLUTION_FIELDS = ("basis", "code", "district", "resolution")
133: 
134: 
135: # The frozen Wikimapia body — read ONLY when the negative fixtures are generated, to
136: # build the degree-space union that must be rejected.  Never read by the checks.
137: DEFAULT_FROZEN = ("C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/"
138:                   "wikimapia_quarters_2026-09-06_v2.geojson")
139: 
140: FAILURES: list[str] = []
141: 
142: 
143: def bad(check: str, message: str) -> None:
144:     FAILURES.append(f"{check}: {message}")
145: 
18:`.gitignore:23` (`*.geojson`) keeps them untracked, so the write-set of the lot stays
143:def bad(check: str, message: str) -> None:
149:def check_artifact_class(meta: dict) -> None:
179:def check_bytes(path: Path, document: dict) -> None:
191:def check_d1_schema(features: list) -> None:
221:def check_hashes_raw(features: list, rows_by_code: dict) -> None:
240:def check_hashes_d1(features: list) -> None:
252:def check_wm_id(features: list, rows_by_code: dict) -> None:
290:def check_bijection(features: list, rows: list, meta: dict) -> None:
325:def check_registry(meta: dict, registry: dict, rows: list) -> None:
346:def check_licence(features: list, meta: dict) -> None:
371:def check_attribution(features: list, meta: dict) -> None:
393:def check_unique_geometry(features: list) -> None:
414:def check_decisions_clean(decisions_doc, where: str) -> None:
434:def check_precision(features: list) -> None:
452:def check_method(features: list) -> None:
468:def check_parents(features: list, registry: dict, feature_codes: set) -> None:
496:def check_dag(meta: dict, registry: dict) -> None:
506:def load_signed_resolutions(path: Path) -> tuple[dict, str | None]:
549:def check_district(features: list, districts_path: str, resolutions: dict) -> None:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; "'$env:GIT_CONFIG_COUNT='"'2'; "'$env:GIT_CONFIG_KEY_0='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_0='"'C:/git/Fire_Varna'; "'$env:GIT_CONFIG_KEY_1='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_1='"'C:/git/varna_3d'; "'$fixtureTarget=(Resolve-Path -LiteralPath '"'C:/git/varna_3d/tests/fixtures/qa_quarters_signed').Path; if ("'$fixtureTarget -ne '"'C:\\git\\varna_3d\\tests\\fixtures\\qa_quarters_signed') { throw 'Unexpected fixture path' }; python -m unittest tests.test_quarters_signed_fixtures" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; "'$env:GIT_CONFIG_COUNT='"'2'; "'$env:GIT_CONFIG_KEY_0='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_0='"'C:/git/Fire_Varna'; "'$env:GIT_CONFIG_KEY_1='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_1='"'C:/git/varna_3d'; python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna" in C:\git\varna_3d
 exited 1 in 131ms:
E
======================================================================
ERROR: setUpClass (tests.test_quarters_signed_fixtures.SignedQuartersFixtures)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\git\varna_3d\tests\test_quarters_signed_fixtures.py", line 157, in setUpClass
    shutil.rmtree(FIXTURES)
  File "C:\Program Files\Python310\lib\shutil.py", line 749, in rmtree
    return _rmtree_unsafe(path, onerror)
  File "C:\Program Files\Python310\lib\shutil.py", line 619, in _rmtree_unsafe
    onerror(os.unlink, fullname, sys.exc_info())
  File "C:\Program Files\Python310\lib\shutil.py", line 617, in _rmtree_unsafe
    os.unlink(fullname)
PermissionError: [WinError 5] Access is denied: 'C:\\git\\varna_3d\\tests\\fixtures\\qa_quarters_signed\\artifact_class_other.geojson'

----------------------------------------------------------------------
Ran 0 tests in 0.001s

FAILED (errors=1)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=550; Get-Content -Encoding UTF8 -LiteralPath src/qa_quarters_signed.py | Select-Object -Skip 550 -First 145 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\varna_3d
 succeeded in 86ms:
551:     позволен, но ПРОСТРАНСТВЕНО ГРЕШЕН район минаваше.  The gate re-derives the
552:     district itself, from the same named layer of Б0 т. 4 (our five, never АГКК — G22
553:     stays locked), by the representative point of the Feature, and compares.
554: 
555:     Decision 9 (Petar, 07.09) opens exactly ONE door in that rule: a code NAMED in the
556:     signed resolutions file may carry the district of the АГКК AU5 witness instead of
557:     ours, with `district_src = agkk_au5_confirmed_by_petar`.  Three conditions, all
558:     checked here: the code must be listed, the listed district must be the one written,
559:     and our layer must actually DISAGREE with it — a „resolution“ of a district our own
560:     layer already gives is a decision about nothing, and it fails.  Whether the written
561:     district is what AU5 says is C20's job: the two checks share no input.
562:     """
563:     districts = load_our_districts(Path(districts_path))
564:     for feature in features:
565:         props = feature.get("properties") or {}
566:         code = props.get("code")
567:         district = props.get("district")
568:         src = props.get("district_src")
569:         if district is not None and district not in DISTRICT_CODES:
570:             bad("C18 район", f"{code}: district {district!r} е извън затворената петорка")
571:         if src not in DISTRICT_SRC_ALLOWED:
572:             bad("C18 район", f"{code}: district_src {src!r} — Б0 т. 4 иска "
573:                              f"„{OUR_DISTRICT_SRC}“, а решение 9 позволява само "
574:                              f"„{RESOLVED_DISTRICT_SRC}“; никога чист АГКК (G22 остава заключен)")
575:         geometry = feature.get("geometry")
576:         if not geometry:
577:             bad("C18 район", f"{code}: липсва геометрия, районът не може да се провери")
578:             continue
579:         measured = district_of(geometry, districts)
580:         row = resolutions.get(code)
581:         if src == RESOLVED_DISTRICT_SRC:
582:             if row is None:
583:                 bad("C18 район",
584:                     f"{code}: district_src {RESOLVED_DISTRICT_SRC!r}, а кодът НЕ е в подписания "
585:                     "файл с решенията — район се заменя само с подписана дума")
586:             elif row.get("district") != district:
587:                 bad("C18 район",
588:                     f"{code}: районът {district!r} не е подписаният {row.get('district')!r}")
589:             if district == measured:
590:                 bad("C18 район",
591:                     f"{code}: решение за район без спор — нашият слой също дава {measured!r}")
592:             continue
593:         if row is not None:
594:             bad("C18 район",
595:                 f"{code}: има подписано решение за района, а Feature-ът още носи "
596:                 f"{OUR_DISTRICT_SRC!r} — решението не е приложено")
597:         if district != measured:
598:             bad("C18 район",
599:                 f"{code}: district {district!r} не е районът, в който лежи представителната точка "
600:                 f"на Feature-а ({measured!r}) — позволен код не е доказан район")
601: 
602: 
603: def check_union_recipe(features: list, meta: dict) -> None:
604:     """C19 — Astra S23 F2: the union pin, honestly declared and BOUND to the CRS.
605: 
606:     Before this check, substituting `_meta.union_crs` for `EPSG:4326` passed the whole
607:     gate: the pin was checked, but nothing tied the pin to the space it was computed
608:     in, so the file could claim a recipe that does not produce its own geometry.  The
609:     gate now pins the CRS, both hash keys of the authoritative (projected) union, both
610:     hash keys of the degree-space union it must NOT be, and the library versions —
611:     `unary_union` is GEOS code in either space, so „library independent“ is false.
612:     """
613:     if meta.get("union_crs") != SIGNED_UNION_CRS:
614:         bad("C19 рецепта на обединението",
615:             f"_meta.union_crs = {meta.get('union_crs')!r}, а подписаният е {SIGNED_UNION_CRS!r} "
616:             "(градусното пространство дава ДРУГА геометрия, не същата с шум)")
617:     recipe = meta.get("union_recipe")
618:     if not isinstance(recipe, dict) or not recipe:
619:         bad("C19 рецепта на обединението", "_meta.union_recipe липсва — рецептата не е записана")
620:         return
621:     if recipe.get("crs") != SIGNED_UNION_CRS:
622:         bad("C19 рецепта на обединението",
623:             f"union_recipe.crs = {recipe.get('crs')!r} вместо {SIGNED_UNION_CRS!r}")
624:     if recipe.get("crs") != meta.get("union_crs"):
625:         bad("C19 рецепта на обединението",
626:             f"union_recipe.crs {recipe.get('crs')!r} и _meta.union_crs {meta.get('union_crs')!r} се разминават")
627:     if recipe.get("authority") != "projected":
628:         bad("C19 рецепта на обединението",
629:             f"authority = {recipe.get('authority')!r}; авторитетът е проектираното обединение")
630:     if not isinstance(recipe.get("steps"), list) or len(recipe.get("steps") or []) < 3:
631:         bad("C19 рецепта на обединението", "steps не описва рецептата стъпка по стъпка")
632:     pin = recipe.get("projected_pin") or {}
633:     if pin.get("raw_geometry_sha256") != SIGNED_UNION_RAW_SHA256:
634:         bad("C19 рецепта на обединението",
635:             f"projected_pin.raw_geometry_sha256 {str(pin.get('raw_geometry_sha256'))[:12]}… "
636:             f"не е пинът {SIGNED_UNION_RAW_SHA256[:12]}…")
637:     if pin.get("wm_polygon_sha256") != SIGNED_UNION_D1_SHA256:
638:         bad("C19 рецепта на обединението",
639:             f"projected_pin.wm_polygon_sha256 {str(pin.get('wm_polygon_sha256'))[:12]}… "
640:             f"не е пинът по D1 {SIGNED_UNION_D1_SHA256[:12]}…")
641:     degree = recipe.get("degree_space_diagnostic") or {}
642:     if degree.get("raw_geometry_sha256") != DEGREE_UNION_RAW_SHA256:
643:         bad("C19 рецепта на обединението",
644:             "degree_space_diagnostic.raw_geometry_sha256 не е измереният "
645:             f"{DEGREE_UNION_RAW_SHA256[:12]}…")
646:     if degree.get("wm_polygon_sha256") != DEGREE_UNION_D1_SHA256:
647:         bad("C19 рецепта на обединението",
648:             "degree_space_diagnostic.wm_polygon_sha256 не е измереният "
649:             f"{DEGREE_UNION_D1_SHA256[:12]}…")
650:     if degree.get("raw_geometry_sha256") == pin.get("raw_geometry_sha256"):
651:         bad("C19 рецепта на обединението",
652:             "градусното и проектираното обединение са записани с ЕДИН хеш — те са различни геометрии")
653:     libraries = recipe.get("libraries") or {}
654:     for name in REQUIRED_LIBRARIES:
655:         if not libraries.get(name):
656:             bad("C19 рецепта на обединението",
657:                 f"libraries.{name} липсва — unary_union и проекцията са код на GEOS/PROJ, "
658:                 "версията е част от рецептата")
659:     if not recipe.get("witness_file_sha256"):
660:         bad("C19 рецепта на обединението", "witness_file_sha256 липсва — файлът, който Петър видя, не е закотвен")
661:     else:
662:         witness_pin = next((i for i in meta.get("inputs") or []
663:                             if str(i.get("id", "")).startswith("unions_")), None)
664:         if witness_pin and witness_pin.get("sha256") != recipe.get("witness_file_sha256"):
665:             bad("C19 рецепта на обединението",
666:                 "witness_file_sha256 не е sha-то на закотвения файл с обединенията в _meta.inputs")
667:     unions = [f for f in features if (f.get("properties") or {}).get("source") == UNION_SOURCE]
668:     if not unions:
669:         bad("C19 рецепта на обединението", "няма Feature с обединение, а рецептата е записана")
670:     for feature in unions:
671:         props = feature.get("properties") or {}
672:         code = props.get("code")
673:         if props.get("raw_geometry_sha256") != SIGNED_UNION_RAW_SHA256:
674:             bad("C19 рецепта на обединението",
675:                 f"{code}: суровият хеш не е проектираното обединение {SIGNED_UNION_RAW_SHA256[:12]}…")
676:         if props.get("wm_polygon_sha256") != SIGNED_UNION_D1_SHA256:
677:             bad("C19 рецепта на обединението",
678:                 f"{code}: хешът по D1 не е този на проектираното обединение {SIGNED_UNION_D1_SHA256[:12]}…")
679:         if props.get("raw_geometry_sha256") == DEGREE_UNION_RAW_SHA256:
680:             bad("C19 рецепта на обединението",
681:                 f"{code}: това е обединението В ГРАДУСИ — друга геометрия, не подписаната")
682: 
683: 
684: def check_district_witness_au5(features: list, meta: dict, au5_path: str,
685:                                resolutions: dict, resolutions_sha: str | None,
686:                                resolutions_path: str) -> None:
687:     """C20 — Astra S23 F3: an INDEPENDENT district witness.
688: 
689:     C18 re-derives the district from the same layer and the same helpers the builder
690:     uses, so a common defect in that layer stays invisible to both.  This check shares
691:     nothing with the builder: it reads the АГКК INSPIRE AU5 layer by its own pinned
692:     sha256, does its own point-in-polygon with its own crosswalk, and requires every
693:     disagreement to be NAMED in `_meta.district_witness_disputes`.
694: 
695:     It never replaces a district BY ITSELF: Б0 т. 4 keeps our source, and a disagreement

 succeeded in 306ms:
✓ ГЕЙТ Б1 ЗЕЛЕН · data\quarters_signed.geojson · 301917 B · sha256 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3
  Feature-и: 60 · решения: 68 · registry_pending: 16 · блоб на решенията 74f09d505e2b…
  обединения: 1 · изключени: ['vinitsa_sever'] · подписано тяло на плана 4ce6ea842a0a… (42b2635)
  рецепта на обединението: EPSG:32635 (авторитет projected) · {'GEOS': '3.13.1', 'PROJ': '9.3.0', 'pyproj': '3.6.1', 'shapely': '2.1.2'}
  независим свидетел АГКК AU5 (78a2de59600e…): 58 съгласни · чакат Петър [] → pending_petar
  решени по подписан файл (d494d4d256ae…, решение 9): [('kochmar', 'mladost'), ('vazrazhdane4', 'mladost')] → petar_agkk / agkk_au5_confirmed_by_petar
  20 проверки: C1 клас/подпис (дословен sha на плана) · C2 байтове (G30) · C3 D1 схема (21 полета) · C4 суров хеш (G25-а) · C5 хеш по D1 (G25-а) · C6 wm_id (G25-а) · C7 биекция (G26) · C8 регистър (G26) · C9 лиценз · C10 атрибуция (G27-а) · C11 еднозначност · C12 решения · C13 precision_m · C14 родител · C15 кадастрални идентификатори · C16 метод · C17 DAG (Б0 т. 9) · C18 район ПРОСТРАНСТВЕНО (Б0 т. 4 + решение 9) · C19 рецепта на обединението (S23 F2) · C20 независим свидетел АГКК AU5 (S23 F3) с подписаните решения по решение 9

codex
QA gate-ът мина: exit `0`, 60 Features, точният staged SHA и двата спора решени към `mladost`. `unittest` завърши с exit `1`, преди да изпълни тестове: read-only sandbox отказва изтриването/регенерирането на fixtures. Ще проверя наличните negative fixtures без запис и ще отбележа ясно тази граница на проверката.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=845; Get-Content -Encoding UTF8 -LiteralPath src/qa_quarters_signed.py | Select-Object -Skip 845 -First 110 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }; rg -n --max-count 20 --max-columns 200 '"'"'^def main|check_|def .*fixtures'"' src/qa_quarters_signed.py | Select-Object -Last 20" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=695; Get-Content -Encoding UTF8 -LiteralPath src/qa_quarters_signed.py | Select-Object -Skip 695 -First 150 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\varna_3d
 succeeded in 74ms:
846:                 f"{code}: нашият район е {ours!r}, АГКК го слага в {hits[0]} ({witness}), а "
847:                 "несъгласието не е в _meta.district_witness_disputes")
848:             continue
849:         if row.get("resolution") != DISPUTE_RESOLUTION:
850:             bad("C20 независим свидетел (АГКК AU5)",
851:                 f"{code}: спорът е обявен за решен ({row.get('resolution')!r}), а районът в "
852:                 f"Feature-а още е нашият ({ours!r}) — решение, което не е приложено")
853:         if row.get("ours") != ours or row.get("agkk") != hits[0]:
854:             bad("C20 независим свидетел (АГКК AU5)",
855:                 f"{code}: записаният спор {row.get('ours')!r}/{row.get('agkk')!r} не е измереният "
856:                 f"{ours!r}/{hits[0]!r}")
857:     for code in sorted(declared):
858:         bad("C20 независим свидетел (АГКК AU5)", f"{code}: спор в _meta без такъв Feature")
859: 
860:     # The signed file, judged on its own: every resolution must name a code that has a
861:     # Feature, that IS in dispute, and must point where AU5 points.  This loop is what
862:     # makes „a resolution against the witness“ and „a resolution for a code with no
863:     # dispute“ red, even if the artefact were written to agree with them.
864:     for code in sorted(resolutions):
865:         signed = resolutions[code]
866:         witness = witness_by_code.get(code)
867:         if witness is None:
868:             bad("C20 независим свидетел (АГКК AU5)",
869:                 f"{code}: подписано решение за район, а свидетелят няма такъв Feature")
870:             continue
871:         if signed.get("district") != witness:
872:             bad("C20 независим свидетел (АГКК AU5)",
873:                 f"{code}: подписаното решение дава район {signed.get('district')!r}, а АГКК AU5 "
874:                 f"казва {witness!r} — приемаме само решение, съгласно с AU5")
875:         if code not in disputed_codes:
876:             bad("C20 независим свидетел (АГКК AU5)",
877:                 f"{code}: подписано решение за код без спор в _meta.district_witness_disputes")
878: 
879: 
880: def check_no_cad_ids(path: Path) -> None:
881:     text = path.read_bytes().decode("utf-8", errors="replace")
882:     hits = CAD_ID.findall(text)
883:     if hits:
884:         bad("C15 кадастрални идентификатори", f"{len(hits)} срещания в подписания файл")
885: 
886: 
887: # ---------------------------------------------------------------------------
888: # Negative fixtures — one per check, each a real file this gate must reject
889: # ---------------------------------------------------------------------------
890: 
891: def degree_space_union(frozen_path: Path, wm_ids: list) -> dict:
892:     """The union of the SAME two rings, computed straight in WGS84 degrees.
893: 
894:     Used only to build the negative fixture of S23 F2: a geometry that is internally
895:     consistent (both of its own hashes recomputed) and still not the one Petar signed.
896:     """
897:     from shapely.geometry import mapping, shape
898:     from shapely.ops import unary_union
899:     from shapely.validation import make_valid
900: 
901:     frozen = json.loads(frozen_path.read_bytes().decode("utf-8"))
902:     parts = {f["properties"].get("wm_id"): f["geometry"] for f in frozen.get("features", [])}
903:     missing = [w for w in wm_ids if w not in parts]
904:     if missing:
905:         raise SystemExit(f"фикстури: обектите {missing} липсват в {frozen_path}")
906:     shapes = []
907:     for wm_id in wm_ids:
908:         piece = shape(parts[wm_id])
909:         if not piece.is_valid:
910:             piece = make_valid(piece)
911:         shapes.append(piece)
912:     merged = unary_union(shapes)
913:     if merged.geom_type == "MultiPolygon":
914:         merged = max(merged.geoms, key=lambda part: part.area)
915:     shape_back = mapping(merged)
916:     return {"type": shape_back["type"],
917:             "coordinates": json.loads(json.dumps(shape_back["coordinates"]))}
918: 
919: 
920: def make_fixtures(document: dict, out_dir: Path, frozen_path: Path) -> list[Path]:
921:     out_dir.mkdir(parents=True, exist_ok=True)
922:     written: list[Path] = []
923: 
924:     def emit(name: str, doc: dict, raw: bytes | None = None) -> None:
925:         path = out_dir / f"{name}.geojson"
926:         path.write_bytes(raw if raw is not None else canonical_bytes(doc))
927:         written.append(path)
928: 
929:     def clone() -> dict:
930:         return json.loads(json.dumps(document, ensure_ascii=False))
931: 
932:     def index_of(doc: dict, code: str) -> int:
933:         for i, f in enumerate(doc["features"]):
934:             if f["properties"]["code"] == code:
935:                 return i
936:         raise SystemExit(f"фикстури: няма Feature за {code}")
937: 
938:     # C1 — another artefact class (a candidate must never pass as signed).
939:     doc = clone()
940:     doc["_meta"]["artifact_class"] = "candidate_not_signed"
941:     emit("artifact_class_other", doc)
942: 
943:     # C1 — a different decisions blob than the one Petar signs.
944:     doc = clone()
945:     doc["_meta"]["decisions_sha256"] = "0" + doc["_meta"]["decisions_sha256"][1:]
946:     emit("decisions_sha_substituted", doc)
947: 
948:     # C2 — BOM, CRLF and unsorted keys (G30).
949:     doc = clone()
950:     text = json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=False)
951:     emit("bom_crlf_unsorted", doc, raw=b"\xef\xbb\xbf" + text.replace("\n", "\r\n").encode("utf-8"))
952: 
953:     # C3 — a missing D1 field.
954:     doc = clone()
955:     doc["features"][0]["properties"].pop("note")
149:def check_artifact_class(meta: dict) -> None:
179:def check_bytes(path: Path, document: dict) -> None:
191:def check_d1_schema(features: list) -> None:
221:def check_hashes_raw(features: list, rows_by_code: dict) -> None:
240:def check_hashes_d1(features: list) -> None:
252:def check_wm_id(features: list, rows_by_code: dict) -> None:
290:def check_bijection(features: list, rows: list, meta: dict) -> None:
325:def check_registry(meta: dict, registry: dict, rows: list) -> None:
346:def check_licence(features: list, meta: dict) -> None:
371:def check_attribution(features: list, meta: dict) -> None:
393:def check_unique_geometry(features: list) -> None:
414:def check_decisions_clean(decisions_doc, where: str) -> None:
434:def check_precision(features: list) -> None:
452:def check_method(features: list) -> None:
468:def check_parents(features: list, registry: dict, feature_codes: set) -> None:
496:def check_dag(meta: dict, registry: dict) -> None:
549:def check_district(features: list, districts_path: str, resolutions: dict) -> None:
603:def check_union_recipe(features: list, meta: dict) -> None:
684:def check_district_witness_au5(features: list, meta: dict, au5_path: str,
880:def check_no_cad_ids(path: Path) -> None:

 succeeded in 80ms:
696:     is a row Petar decides on (`resolution: "pending_petar"`), not an automatic
697:     correction.  Decision 9 (07.09) is the other half: where Petar HAS decided, the
698:     decision travels as a signed file, and this check accepts it only if
699:       * the file it reads hashes to the pin in `_meta.inputs` AND to the signed sha
700:         here — a substituted resolutions file is a red gate;
701:       * the code is really in dispute (a resolution without a dispute fails);
702:       * the resolved district is EXACTLY what this check's own AU5 point-in-polygon
703:         says — a resolution against the witness fails, whichever way it points.
704:     """
705:     from shapely.geometry import shape
706: 
707:     path = Path(au5_path)
708:     if not path.exists():
709:         bad("C20 независим свидетел (АГКК AU5)", f"липсва закотвеният слой: {path}")
814:             elif signed.get("district") != ours:
815:                 bad("C20 независим свидетел (АГКК AU5)",
816:                     f"{code}: написаният район {ours!r} не е подписаното решение "
817:                     f"{signed.get('district')!r}")
818:             if witness != ours:
819:                 bad("C20 независим свидетел (АГКК AU5)",
820:                     f"{code}: решеният район {ours!r} НЕ е свидетелството на АГКК AU5 "
821:                     f"({hits[0]} → {witness}) — приемаме само решение, съгласно с AU5")
822:             if row is None:
823:                 bad("C20 независим свидетел (АГКК AU5)",
824:                     f"{code}: районът е решен, а спорът не е записан в "
825:                     "_meta.district_witness_disputes — решението не трие разминаването")
826:                 continue
827:             if row.get("resolution") != RESOLUTION_RESOLVED:
828:                 bad("C20 независим свидетел (АГКК AU5)",
829:                     f"{code}: районът е заменен, а спорът още е {row.get('resolution')!r}")
830:             if row.get("agkk") != hits[0]:
831:                 bad("C20 независим свидетел (АГКК AU5)",
832:                     f"{code}: записаният свидетел {row.get('agkk')!r} не е измереният {hits[0]!r}")
833:             if row.get("ours") == ours:
834:                 bad("C20 независим свидетел (АГКК AU5)",
835:                     f"{code}: спорът твърди {row.get('ours')!r} и за нашия слой, и за решението — "
836:                     "запис на спор без разминаване")
837:             continue
838: 
839:         if witness == ours:
840:             if row is not None:
841:                 bad("C20 независим свидетел (АГКК AU5)",
842:                     f"{code}: записан спор, а свидетелят е СЪГЛАСЕН ({witness})")
843:             continue
844:         if row is None:
845:             bad("C20 независим свидетел (АГКК AU5)",

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; "'$env:GIT_CONFIG_COUNT='"'1'; "'$env:GIT_CONFIG_KEY_0='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_0='"'C:/git/varna_3d'; python src/qa_no_cad_ids.py; "'$cadExit=$LASTEXITCODE; python src/qa_no_extrude.py; $extrudeExit=$LASTEXITCODE; Write-Output "QA_EXIT_CODES cad_ids=$cadExit no_extrude=$extrudeExit"; if ($cadExit -ne 0 -or $extrudeExit -ne 0) { exit 1 }' in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; "'$env:GIT_CONFIG_COUNT='"'2'; "'$env:GIT_CONFIG_KEY_0='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_0='"'C:/git/Fire_Varna'; "'$env:GIT_CONFIG_KEY_1='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_1='"'C:/git/varna_3d'; @'
import importlib.util,pathlib,subprocess,sys
p=pathlib.Path('tests/test_quarters_signed_fixtures.py'); spec=importlib.util.spec_from_file_location('fixture_review',p); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
failed=[]
for name,check in mod.EXPECTED_CHECK.items():
 path=mod.FIXTURES/(name+'.geojson')
 if not path.is_file(): failed.append((name,'MISSING'));continue
 r=mod.gate(path);out=mod.text_of(r);ok=r.returncode"'!=0 and check in out
 print(f'"'{name}: exit={r.returncode}, expected={check}, matched={ok}')
 if not ok: failed.append((name,out[:500]))
print('TOTAL',len(mod.EXPECTED_CHECK),'unexpected',failed)
sys.exit(bool(failed))
'@ | python -" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "& 'C:/Program Files/GitHub CLI/gh.exe' repo view Petar1984/varna_3d --json visibility" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import subprocess,json,hashlib,pathlib
repo='C:/git/Fire_Varna';p='scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json';rev='3d747d3'
b=subprocess.check_output(['git','-C',repo,'cat-file','blob',rev+':'+p]);print('DECISIONS_BLOB',len(b),hashlib.sha256(b).hexdigest())
m=json.loads(pathlib.Path('data/quarters_signed.geojson').read_bytes())['_meta']
for k in ['district_witness_agkk','district_witness_disputes','excluded']:
 x=m[k]
 if k=='district_witness_agkk': x={a:b for a,b in x.items() if a"'!='"'by_code'}
 print(k,json.dumps(x,ensure_ascii=False))
r=pathlib.Path('C:/git/Varna_buildings/config/quarter_registry.json');print('REGISTRY',len(r.read_bytes()),hashlib.sha256(r.read_bytes()).hexdigest())
print('REGISTRY_STATUS',subprocess.check_output(['git','-C','C:/git/Varna_buildings','--no-optional-locks','status','--porcelain=v1','--','config/quarter_registry.json']).decode())
'@ | python -" in C:\git\varna_3d
 exited 1 in 60ms:
fatal: detected dubious ownership in repository at 'C:/git/Fire_Varna'
'C:/git/Fire_Varna' is owned by:
	BUILTIN/Administrators (S-1-5-32-544)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/Fire_Varna
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "C:\Program Files\Python310\lib\subprocess.py", line 420, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "C:\Program Files\Python310\lib\subprocess.py", line 524, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['git', '-C', 'C:/git/Fire_Varna', 'cat-file', 'blob', '3d747d3:scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json']' returned non-zero exit status 128.

 exited 1 in 1094ms:
HTTP 401: Requires authentication (https://api.github.com/graphql)
Try authenticating with:  gh auth login

 succeeded in 3115ms:
=== ПРОВЕРКА: нула кадастрални идентификатори (AGENTS.md, правило 2) ===

  ok  проследените файлове са прочетени · 2126 файла
  ok  нула кадастрални идентификатори извън изброените изключения

      изключения, изброени с довод: 9 · срещнати: 11
      · src/build_poi_names.py: ЖИВА СТОЙНОСТ: правилото У6 (кампусът на ТУ) стъпва на този имот. Махането му сменя поведение и 
      · src/qa_compare_kais_versions.py: ЖИВА СТОЙНОСТ: сравнението на двете КАИС извадки следи точно този обект; чака същото решение
      · src/qa_sections.py: ОТРИЦАТЕЛНА ПРОБА: низът НАРОЧНО е във формата на кадастрален идентификатор, за да докаже, че па
      · src/qa_d1.py: ОТРИЦАТЕЛНА ПРОБА: същото за пазача на Д1-обемите — --break-me подхвърля низа, за да докаже, че 
      · src/qa_bodies.py: ОТРИЦАТЕЛНА ПРОБА: и трети път, за пазача на телата по вход (Т, 24.08) — --break-me подхвърля ни
      · src/qa_no_extrude.py: ОТРИЦАТЕЛНА ПРОБА: и четвърти път, за пазача на присъдите „под платното“ (П, 26.08) — --break-me
      · src/qa_quarters_license.py: ОТРИЦАТЕЛНА ПРОБА: и пети път, за ЛИЦЕНЗНИЯ гейт на цикъла „кварталите“ (Г-К-0, 30.08) — --break
      · scratch/web_probes/_brk/cadids_върнат-идентификатор.new: ТЕКСТЪТ НА СЧУПВАНЕТО: подменя се в проследен файл, за да падне гейтът; стойността е синтетична 
      · scratch/web_probes/_pack_out/_breaks/src_qa_poi_names_чистка_върнат-идентификатор-в-проследен-файл.txt: АРТЕФАКТЪТ НА СЧУПВАНЕТО: дословният изход съдържа същия синтетичен низ — без него доказателство

минава — идентификатор напуска m6000_private само през изброените места
=== 1. форматът
  ✓ всички ключове по прецедента на фантомите: [] липсват
  ✓ contains_cadastral_id: false
  ✓ counts съвпада с масивите: {'verdicts': 31, 'absorbed': 34, 'terrain_gone': 27, 'list': 32, 'passages': 26} срещу {'verdicts': 31, 'absorbed': 34, 'terrain_gone': 27, 'list': 32, 'passages': 26}
  ✓ всеки ред носи присъда „под платното“, дата, източник и revoked-история: []
  ✓ и всеки absorbed-ред носи присъда „погълната от платното“, дата, довод, източник и revoked-история: []
  ✓ и всеки terrain_gone-ред носи присъда „оперативно скрита по нареждане на собственика“, дата, наблюдение, ОСНОВАНИЕ и revoked-история: []
  ✓ нула повторени i в трите класа присъди и в листа

=== 2. отпечатъкът срещу кадастъра, преизчислен сега
  ✓ отпечатъкът на всичките 150 реда пасва на КАИС: []

=== 3. листът е затворен
  ✓ нула присъди извън листа: []
  ✓ ядрото (26) носи кадастралния признак (вид ∧ Общинска публична ∧ 1 ет ∧ ≥150 m²): []
  ✓ поименните (6) са едноетажни: []
  ✓ всеки ред на листа казва КАК е влязъл
  ✓ присъдените и `judged`-редовете на листа са едно и също множество

=== 3б. а НА КАКВО ОСНОВАНИЕ — свидетелят, поименно
  ✓ всеки присъден ред стои на ОСНОВАНИЕ — ядро по клаузите (25) или собствен подземен свидетел ≥10 м (31); без основание: []
  ✓ двете множества затварят присъдите ТОЧНО: |ядро ∪ свидетел| = 31 срещу 31 присъди
  ✓ поименните (6) без изключение носят собствен свидетел над критерия: []
  ✓ и вътрешният одитен запис е чист от кадастрални номера

=== 3в. Условие 4 — нула OSM-стойности в ПУБЛИЧНИЯ файл
  ✓ нула OSM-полета: []
  ✓ нула измерени дължини в текста (метри): []

=== 3г. absorbed — вторият клас присъди, и четирите му конюнкта
  ✓ absorbed е ДИЗЮНКТЕН с присъдите, с листа и с проходните: []
  ✓ absorbed ⊆ класа „платно над петното“ (a≥0.5; 647 тела от 5798 мерени) — присъда извън класа ПАДА: []
  ✓ всеки absorbed-ред стои на ОЧЕН СВИДЕТЕЛ — кадър-файл, който наистина съществува на диска и е назован и в публичния ред: []

=== 3д. terrain_gone — третият клас, и петте му ключалки
  ✓ terrain_gone е ДИЗЮНКТЕН с присъдите, absorbed, листа и проходните: []
  ✓ всеки ред е В СЕСИЙНИЯ МАНИФЕСТ на подписания плана ([3111, 5592, 11041, 11776, 12374, 12377, 12754, 15778, 21801, 27038, 28103, 35731, 39534, 49747, 49748, 49749, 49750, 49751, 49752, 49753, 49815, 49816, 49817, 49818, 49820, 49822, 54579, 54580, 54581, 54582, 54583, 54584, 54585, 54586, 54587, 54588, 54589, 54590, 54591, 54592, 79090, 79091, 79092, 79093, 79094, 79102, 79105, 79121, 79122, 79123, 79124, 79125, 79126, 79127, 80400, 80401, 80424, 80492]): извън него []
  ✓ нула производни следи за 27 terrain_gone + 34 absorbed реда (units/секции/тела/Д1/врати/фантоми): []
  ✓ нито един terrain_gone ред не е върху платното (a≥0.5 → мястото му е в absorbed); мерени от 5798: [49753, 49817, 54579, 54585, 54589, 79092, 79093, 79094, 79122, 79123, 79124, 79125, 79126, 79127, 80400, 80401, 80424] · сгрешен клас: []
  ✓ кадърът на всеки ред съществува И отпечатъкът му съвпада с witness-а (27 terrain_gone + 34 absorbed): []
  ✓ дословната дума на Петър в `basis` е ПОДНИЗ на ПЛАН_П2в_терена.md: []

=== 3е. П2-г/П2-д — оградата на партидите (О1 на одита, 28.08)
  ✓ всеки ред на партидите П2-г/П2-д (57) е В МАНИФЕСТА — вече и `absorbed`, не само `terrain_gone`: извън него []
  ✓ един кадър — един ред: sha256 на свидетелите в партидата е УНИКАЛЕН (клониран кадър = клонирано основание): {}
  ✓ камерата на всеки кадър СОЧИ реда си (< 30 м от центроида, или колкото казва именуваната декларация за споделен кадър; преизчислен от geojson-а, не от манифеста): []

=== 4. проходните — път минава ПРЕЗ тях, значи са истински
  ✓ нула проходни в присъдите: []
  ✓ нула проходни в листа: []
  ✓ проходните са 26 (мереното от _probe_p_mat.py): 26

=== 5. бордът
  ✓ i=56508 стои В ЛИСТА (кандидат, не забравен)
  ✓ i=56508 е БЕЗ присъда — чака очите на Петър (Gate 2); присъда за него се вписва заедно с подписа му и с този ред

=== 6. Г-П-1 — нулев диф в данните
  ✓ varna_buildings_3d.geojson байт-идентичен: d0c8336061601cde… (еталон d0c8336061601cde…)
  ✓ varna_buildings_3d.manifest.json байт-идентичен: 29bbb28aa98fbb33… (еталон 29bbb28aa98fbb33…)
  ✓ varna_sections_3d.geojson байт-идентичен: e5a625b62e861ec0… (еталон e5a625b62e861ec0…)
  ✓ varna_section_bodies.json байт-идентичен: 4d22a89f7a48a4af… (еталон 4d22a89f7a48a4af…)
  ✓ varna_d1_volumes.geojson байт-идентичен: b4e509d51aaefe2a… (еталон b4e509d51aaefe2a…)
  ✓ varna_units_index.json байт-идентичен: 67cc8dc75da5cd98… (еталон 67cc8dc75da5cd98…)

=== 7. файлът не е сирак
  ✓ web/index.html тегли присъдите
  ✓ височината и полата минават през общите изрази (nxHeight/nxBase)
  ✓ страницата чете И ТРИТЕ класа — verdicts ∪ absorbed ∪ terrain_gone
  ✓ филтрите на kais-3d и kais-flat се пишат САМО от композера: kais-3d 1× · kais-flat 1×

=== 8. нула кадастрални номера
  ✓ нула кадастрални номера във файла: 0 съвпадения

минава — 31 „под платното“ · 34 „погълната от платното“ · 27 „оперативно скрита по нареждане на собственика“ · скрити общо 92 · лист 32 · проходни 26
QA_EXIT_CODES cad_ids=0 no_extrude=0

 succeeded in 10014ms:
artifact_class_other: exit=1, expected=C1, matched=True
decisions_sha_substituted: exit=1, expected=C1, matched=True
bom_crlf_unsorted: exit=1, expected=C2, matched=True
d1_field_missing: exit=1, expected=C3, matched=True
drawn_by_filled_on_import: exit=1, expected=C3, matched=True
d1_null_not_allowed: exit=1, expected=C3, matched=True
declared_local_knowledge: exit=1, expected=C3, matched=True
vertex_moved: exit=1, expected=C4, matched=True
hash_raw_substituted: exit=1, expected=C4, matched=True
hash_d1_substituted: exit=1, expected=C5, matched=True
wm_id_substituted: exit=1, expected=C6, matched=True
deferred_code_with_feature: exit=1, expected=C7, matched=True
feature_without_row: exit=1, expected=C7, matched=True
mladost2_missing: exit=1, expected=C7, matched=True
code_outside_registry_pending: exit=1, expected=C8, matched=True
bare_cc_by_sa: exit=1, expected=C9, matched=True
missing_terms: exit=1, expected=C9, matched=True
missing_attribution: exit=1, expected=C10, matched=True
osm_code_with_wikimapia_string: exit=1, expected=C10, matched=True
two_codes_one_geometry: exit=1, expected=C11, matched=True
precision_missing: exit=1, expected=C13, matched=True
precision_below_floor: exit=1, expected=C13, matched=True
street_method_other_code: exit=1, expected=C16, matched=True
parent_not_in_registry: exit=1, expected=C14, matched=True
dag_pair_removed: exit=1, expected=C17, matched=True
district_from_agkk: exit=1, expected=C18, matched=True
plan_sha_zeroed: exit=1, expected=C1, matched=True
district_spatially_wrong: exit=1, expected=C18, matched=True
excluded_code_with_feature: exit=1, expected=C7, matched=True
union_wm_ids_substituted: exit=1, expected=C6, matched=True
degree_union_self_rehashed: exit=1, expected=C4, matched=True
union_crs_substituted: exit=1, expected=C19, matched=True
au5_crosswalk_swapped: exit=1, expected=C20, matched=True
district_dispute_delisted: exit=1, expected=C20, matched=True
third_dispute_unlisted: exit=1, expected=C20, matched=True
au5_sha_substituted: exit=1, expected=C20, matched=True
resolutions_sha_substituted: exit=1, expected=C20, matched=True
resolved_district_contradicts_au5: exit=1, expected=C20, matched=True
resolution_without_dispute: exit=1, expected=C20, matched=True
TOTAL 39 unexpected []

mcp: codex_apps/github.get_repo started
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; "'$env:GIT_CONFIG_COUNT='"'3'; "'$env:GIT_CONFIG_KEY_0='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_0='"'C:/git/Fire_Varna'; "'$env:GIT_CONFIG_KEY_1='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_1='"'C:/git/varna_3d'; "'$env:GIT_CONFIG_KEY_2='"'safe.directory'; "'$env:GIT_CONFIG_VALUE_2='"'C:/git/Varna_buildings'; @'
import subprocess,json,hashlib,pathlib
repo='C:/git/Fire_Varna';p='scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json'
b=subprocess.check_output(['git','-C',repo,'cat-file','blob','3d747d3:'+p]);print('DECISIONS_BLOB',len(b),hashlib.sha256(b).hexdigest())
m=json.loads(pathlib.Path('data/quarters_signed.geojson').read_bytes())['_meta']
for k in ['district_witness_agkk','district_witness_disputes','excluded']:
 x=m[k]
 if k=='district_witness_agkk': x={a:b for a,b in x.items() if a"'!='"'by_code'}
 print(k,json.dumps(x,ensure_ascii=False))
r=pathlib.Path('C:/git/Varna_buildings/config/quarter_registry.json');print('REGISTRY',len(r.read_bytes()),hashlib.sha256(r.read_bytes()).hexdigest())
print('REGISTRY_STATUS',subprocess.check_output(['git','-C','C:/git/Varna_buildings','--no-optional-locks','status','--porcelain=v1','--','config/quarter_registry.json']).decode())
'@ | python -" in C:\git\varna_3d
 succeeded in 57ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
DECISIONS_BLOB 32129 74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b
district_witness_agkk {"crosswalk": {"10135-01": "odesos", "10135-02": "primorski", "10135-03": "mladost", "10135-04": "vladislav_varnenchik", "10135-05": "asparuhovo"}, "crosswalk_why": "подписаният превод национален код → нашите пет; АГКК НИКОГА не пише район (G22 заключен) — служи само за независимо свидетелство", "disputes": 2, "inside_one_district": 60, "outside_all": 0, "state": "свидетел: представителна точка на Feature-а срещу АГКК AU5"}
district_witness_disputes [{"agkk": "10135-03", "code": "kochmar", "ours": "vladislav_varnenchik", "resolution": "petar_agkk"}, {"agkk": "10135-03", "code": "vazrazhdane4", "ours": "vladislav_varnenchik", "resolution": "petar_agkk"}]
excluded [{"code": "vinitsa_sever", "display": "с.о. Виница-север", "kind": "с.о.", "registry_action": "сутрешен ход на Петър: деактивиране на кода в quarter_registry.json — регистърът НЕ се пипа от изпълнителя", "why": "Петър (07.09): „Виница-север го изключваме“ — кодът отпада от регистъра като квартал/с.о. (ход Р: деактивиране), не е второ име; площта е Добрева чешма"}]
REGISTRY 52299 7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6
REGISTRY_STATUS 

mcp: codex_apps/github.get_repo (failed)
codex
Всичките 39 налични negative fixtures падат с очакваната проверка. Две сглобявания в паметта възпроизвеждат staged blob-а байтово; петте read-only теста също минават. Трите minors не налагат промяна на тези bytes, но `ours` има доказан QA пропуск за бъдещи артефакти. Остава да разграничим тази механична годност от липсващия доказан подпис върху final decisions SHA.
mcp: codex_apps/github.get_repo started
mcp: codex_apps/github.get_repo (failed)
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=118; Get-Content -Encoding UTF8 -LiteralPath '"'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' | Select-Object -Skip 118 -First 35 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }; $i=0; Get-Content -Encoding UTF8 -LiteralPath scratch/places_search/granitsi_b1v2_astra_S23_07.09.md | Select-Object -First 100 | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\Fire_Varna
 succeeded in 32ms:
119: 
120: 
121: ## 6 · ЧАСТ Б — нощ от резултати (тръгва само с подписан блок Б0)
122: 
123: ### Б0 · Блокът решения, който Петър подписва тази вечер (препоръките са на архитекта; всяко „да“ е негово)
124: 1. **Схема за ВНЕСЕНА геометрия (промяна на D1, обявена).** За Feature с `source ∈ {wikimapia, declared_streets}` полетата `drawn_by · drawn_at · basemap · viewport · visible_layers · screenshot_sha256 · approval_digest` са `null` по договор (гейт за взаимна изключителност: или ръка, или внос); `approved_by = "Petar"`, `approved_at = decided_at` от решенията; `signed_by = "Petar"` става валидно с подписа на този план по sha на решенията (т. 8); `witnesses[]` = [{kind: "wikimapia_object", url, fetched_at, raw_response_sha256}] (за Младост 2: {kind: "osm_carriageways", ways по име, fetched: 2026-09-06}); `version: 1`; `note = reason`. Останалите 14 полета на D1 остават задължителни. **Делта спрямо амандамент №2 §4 (К22 П1):** §4 null-ва четири полета (`drawn_by/drawn_at/viewport/screenshot_sha256`); тук се добавят още три — `basemap`, `visible_layers` и `approval_digest`; дайджестът на D1 (връзката одобрение ↔ байтове) се замества от sha-веригата на т. 8 (решения по sha → Feature с `wm_polygon_sha256` → `_meta.decisions_sha256`). Препоръка: да.
125: 2. **`wm_polygon_sha256` = канонизацията на D1** (6 знака, външен пръстен обратно на часовника, ротация към лексикографски най-малкия връх; MultiPolygon по правилото на амандамент №2 §4). Суровият хеш от решенията се пренася като `raw_geometry_sha256` и гейтът сверява и двата. Препоръка: да.
126: 3. **Младост 2 — изричен подписан ключ по D2** за `code = mladost2`, `method = "street_bounded_face"`, лиценз `"ODbL © OpenStreetMap contributors"` (осите), `precision_m = 50`, четирите улици дословно в `witnesses`. Само този код; всеки друг Feature с този метод = червено. Препоръка: да.
127: 4. **Районът** се пише от НАШИЯ `district.code` на мястото (375/375 съгласие с АГКК, мерено 05.09), `district_src: "fire_varna_district"`; в Feature-ите на кварталите районът е изведен по представителна точка срещу същите наши 5 района, не от АГКК INSPIRE (G22 остава заключен). Резервата „място без квартал → районът“ пише `quarter = {name: <име на района>, code: <словесният код от DISTRICT_CODES>, src: "DISTRICT_FALLBACK"}` с три ограничения (К22 П3): (i) fallback-редовете **не са „написан квартал“** по D18/G17 — подписан полигон в бъдеща версия ги замества; (ii) място, което лежи в зона на код с `deferred`/`registry_pending` (16-те без решение, Ваялар, Младост 2 без ключа), **не получава fallback** — остава празно, поименно в леджера; (iii) място с `pin_outside_all` **или** чийто полигон противоречи на всеки наличен низов свидетел (кадастралният `quar` на тялото, адресният низ) отива в `disputed`, не се пише — координатата решава, но пин без нито един съгласен свидетел е подозрителен. Семантиката „quarter понякога е район“ е изрично „да“ тук, не само преизмерени пинове. Препоръка: да.
128: 5. **Десетият ключ на `_meta` се казва `quarter_attribution`** (името в §3.3 на амандамент №2 отпада); форма `{<code>: {src, url, label, licence}}` — независима от извора, носи Wikimapia, ODbL и бъдещи; UI редът се **рендерира от `label` и `url` на записа**, никога от фиксиран низ (К22 П2): за Wikimapia — „квартал по Wikimapia.org · обектът“ (двете като връзки по ToS §1.G); за `mladost2` — записът `{src: "openstreetmap", url: "https://www.openstreetmap.org/copyright", label: "© OpenStreetMap contributors", licence: "ODbL"}` (ODbL §4.3); без запис в картата — нищо. Отрицателна фикстура: код със `src: openstreetmap`, показан с Wikimapia-низ → ✗. Препоръка: да.
129: 6. **`precision_m`**: 100 за `wikimapia`, 50 за `street_bounded_face`; ръб = `max(50, precision_m)` по D7 → `edge_pending`. Препоръка: да.
130: 7. **`QUARTER_CODES` се разширява** с 41-те потвърдени кода, които днес липсват; `morska_gradina`, `sveti_nikola`, `zelenika` остават в `LOCALITY_CODES` (търсят се като местности); `QUARTER_SRC` получава `SIGNED_POLYGON` и `DISTRICT_FALLBACK`; `PLACES_CACHE` v6→v7; пиновете и `expectations.json` — в подредената доставка varna_3d → Fire_Varna. Препоръка: да.
131: 8. **Решенията**: Петър подписва `granitsi_decisions_3_2026-09-06_proba.json` **по sha256 на блоба в b6e627d** (`git show b6e627d:scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json | sha256sum`), с добавен от изпълнителя ред `attribution` (ToS §1.G) в СЪЩИЯ файл в нов комит, чийто sha той препотвърждава сутринта. Препоръка: да — това е Г2-б без нов блоб.
132: 9. **Родството — подписан DAG (измерен 06.09 вечерта, ≥ 98 % от детето вътре в родителя): 11 двойки** — abatko ⊂ kk_konstantin_elena · druzhba ⊂ asparuhovo · rozova_dolina ⊂ asparuhovo · kaisieva ⊂ vladislavovo · kokardzha_generic ⊂ izgrev_kv · mladost1 ⊂ mladost · mladost2 ⊂ mladost · saltanat ⊂ morska_gradina · vazrazhdane1 ⊂ vazrazhdane · vazrazhdane2 ⊂ vazrazhdane · vazrazhdane3 ⊂ vazrazhdane. **Частични припокривания (5–98 % от по-малкия), които НЕ са родство:** vazrazhdane4/vazrazhdane 72 % · pz_planova/vladislavovo 61 % · grackata_mahala/tsentar 52 % · vinitsa_sever/dobreva 51 % · maksuda/sv_ivan_rilski 39 % — място в такава двойна зона е `disputed`. Правилото е **транзитивно** по DAG-а (A ⊂ B ⊂ C → A печели пред B и C) и се подписва като геометричен факт за присвояването, без да се пипа регистърът (`parents` там е сутрешен дълг). Препоръка: да.
133: 10. **Ваялар** остава без граница тази нощ (`alias_of` → регистър сутринта); **Евксиноград** = 5729429 с бележката за конфликта на имена; **16-те без решение** → `deferred` в `_meta.registry_pending`. Препоръка: да.
134: 11. **Координатите на местата (промяна на D7/D10, обявена; Astra S21 т. 3).** D7 забранява изнесените координати за присвояване (кръгово), а `place_identity.json` има 0/375 lat/lon. Източникът става **представителната точка на кадастралното тяло, към което идентичността вече сочи** (`site_id`/`kais_i` → `web/varna_buildings_3d.geojson`), записана в `place_identity.json` от генератора (`coord_src: "kais_body_representative_point"`, `coord_precision_m: 20`); място без връзка към тяло → `no_coord`, остава празно и поименно в леджера. Ходът: резервно копие на `data/place_identity.json` в `C:/Users/Petar/AppData/Local/Temp/claude/C--git/26f42576-326e-4863-b700-f1e02c26a0c9/scratchpad/backup_place_identity_2026-09-06.json` (+ sha256 в пиновете; възстановяване: копиране обратно + проверка на sha), генериране в `data/place_identity.candidate.json`, G9 върху кандидата (байт-дифът спрямо основата е само в `lat`/`lon`/`coord_src`/`coord_precision_m`; `place_id` непроменени), подмяна САМО при зелено. Без това „да“ Б2 не тръгва и остава мярка Н2. Препоръка: да — това е „координатите не лъжат“, направено проверимо: координатата идва от кадастъра, не от нашия износ.
135: 12. **Изходите на присвояването — затворена, взаимно изключваща се таблица** (Astra S21 т. 6), в този ред: `written` (записан квартал, непроменен; ако полигонът е родител или дете на записания по DAG → `compatible`, иначе `disputed_written`) → `no_coord` → `pin_outside_all` → `edge_pending` (в ръба `max(50, precision_m)` на най-малкия съдържащ) → `disputed_overlap` (в ≥ 2 полигона без DAG връзка) → `deferred_zone` (полигон само на код от `registry_pending`/отложен) → `assigned_polygon` (най-малкият съдържащ по DAG) → `assigned_district` (само по т. 4 (i)–(iii)). Всяко място получава точно един изход; таблицата е гейт с фикстура за всяка клетка. Препоръка: да.
136: 
137: ### Б1 · Сглобяване (varna_3d, частно) — `data/quarters_signed.geojson`
138: Изпълнител: Claude Executor. Write-set: `src/build_quarters_signed.py`, `src/qa_quarters_signed.py`, `tests/test_quarters_signed_fixtures.py`, `.gitignore` (`!data/quarters_signed.geojson`), `data/quarters_signed.geojson`. Съобщения: `build: assemble quarters_signed.geojson from decisions 3 (sha <…>) with D1 schema for imported geometry` · `gates: qa_quarters_signed with negative fixtures`. Съдържание: 61 Feature (60 Уикимапия + Младост 2 по ключа от Б0 т. 3), полетата по Б0 т. 1–4, 6; `_meta`: `artifact_class: "signed_by_plan_signature"`, `decisions_sha256`, `decisions_commit`, манифест на входовете (frozen v2, extra 5729429, mladost2 face, agkk_au5 само като свидетел), `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict: "allowed_with_conditions", position}`, `parent_child[]` (Б0 т. 9), `registry_pending[]`. Байтове по G30 (UTF-8 без BOM, sorted keys, compact, финален LF; две сглобявания = байт-еднакви). **Гейт (червен):** предгейтове G19 (`gh repo view varna_3d --json visibility` = PRIVATE) и G3 (`qa_no_cad_ids.py`); G25-а (двата хеша поотделно, подменен връх → ✗, подменен `wm_id` → ✗), G26 (биекция решения ↔ трите множества на D4 с `declared_streets`→polygon, `alias_of`/`deferred`→`_meta`; всеки код от регистъра има решение или е в `registry_pending`, поименно), G27(а) (низът по амандамент №2 §3.8 във всеки Feature), D1 (21 полета, `null` само където Б0 т. 1 позволява; `drawn_*` непразно при внос → ✗), лиценз (голо „CC BY-SA“ → ✗), една геометрия към два кода → ✗, `precision_m` липсва → ✗, метод „по улици“ без `mladost2` → ✗. Комитът на `data/quarters_signed.geojson` е **на Петър** по D16/G4: изпълнителят го оставя стейджнат с готово съобщение (`data: signed quarter boundaries v1 (decisions 3, sha <…>)`) и го записва в доклада; всичко след Б1 чете файла по sha, не по комит.
139: 
140: ### Б2 · Присвояване P8-а (varna_3d) — тръгва само с подписано Б0 т. 11; изходите са КАНДИДАТИ за комита на Петър
141: Write-set: `src/fire_varna_locations.py` (каналът `SIGNED_POLYGON` + `DISTRICT_FALLBACK`, четене на `quarters_signed.geojson` по sha; `LEDGER` сочи НОВ датиран леджер `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` с `_meta.base_rev` = комитът на стария; старият не се пипа), `src/qa_p8a.py`, `data/fire_varna_places.json`, `data/fire_varna_hotels.json` (износът), `data/fire_varna_location_inputs.json` (пиновете, вкл. `quarters_signed.geojson` sha), новият леджер. Съобщения: `feat(p8a): SIGNED_POLYGON channel with district fallback, new dated ledger, written quarters untouched` · `data: places export with quarter_attribution (decisions 3)`. Правила: само ПРАЗЕН квартал се пише; най-малкият съдържащ полигон; двойка без подписано родство и място в двата → `disputed`, не се пише; ръб `max(50, precision_m)` → `edge_pending`; без полигон → районът само по Б0 т. 4 (i)–(iii): не в зони на отложени кодове, не при `pin_outside_all` без съгласен свидетел, и винаги заместим; записан ≠ полигон → леджер `disputed`, редът непроменен (G17). Гейт: fallback-ред в зона на отложен код → ✗; fallback-ред, защитен от G17 в следваща версия → ✗ (фикстура с втора версия, в която подписан полигон трябва да го замести). Координати: САМО от `place_identity.json` след хода по Б0 т. 11 (G9 зелен); изнесените координати са забранени за присвояване (D7) — гейт: скриптът не отваря `data/fire_varna_*.json` за четене на координати (AST-проверка като в Н4). Изходите на таблицата по Б0 т. 12 се броят и записват поименно. Десетият ключ по Б0 т. 5 във varna_3d: `META_KEYS` (places 9→10, hotels 7→8 — измерено от Astra), двата износителя (`export_fire_varna_places.py:816`, `export_fire_varna_hotels.py:420`), QA/M6 и `build_place_categories.py` (родители и полигонен провенанс) в един varna_3d комит на изпълнителя; **износените данни (`data/fire_varna_*.json`, новият леджер) остават стейджнати за комита на Петър** (D16/G4) с готово съобщение в доклада. **Гейт (червен):** G17 (всеки записан квартал в стария леджер-блоб `git show <base_rev>:…` е байт-равен в новия износ), G4 (fail-closed без подпис → тук подписът е този план + sha на решенията, записани в `_meta`), `qa_fire_varna_places_export.py` с 10 ключа, брой присвоени = броят „би получил“ от Н2 (мярката и резултатът трябва да съвпадат до място), `edge_pending` и `disputed` в леджера поименно, `python -m unittest` зелен.
142: 
143: ### Б3 · Търсене по квартал F13 (Fire_Varna) — СУТРИНТА, не нощес (Astra S21 т. 4–5: доставката е един атомен комит с подписи, които само Петър дава)
144: Write-set: `index.html` (`QUARTER_SRC`, `QUARTER_CODES` +41, `PLACES_CACHE` v7, нормализаторът D12 за новите имена, правилото родител/дете при търсене: дете → детето; родител → родителят и подписаните му деца; картончето: редът за атрибуция от `_meta.quarter_attribution`), `data/places.json`, `data/hotels.json` (доставката от Б2 по подредената тройка на D13: пинове + `expectations.json` + двата преписа), `tests/test_granitsi_fixtures.py` (шестте S17 фикстури, вкл. `client_cache_matrix` в node — изпълнителят назовава изпълнителя), `release/sign` артефактите по гейта на доставката от 05.09. Съобщения: `feat(search): quarter search over signed boundaries, attribution row, QUARTER_CODES +41, cache v7` · `data: places delivery with quarter_attribution (D13 ordered)` · `tests: S17 fixtures fail on broken candidates`. Пълният write-set по Astra S21 т. 4: трите data файла (`places.json`, `hotels.json`, **`place_categories.json`**), `index.html` (`PLACES_CACHE` v7, трите SHA, `LEGACY_BUNDLE_SHA`, затворените списъци `:6265`, зареждане/валидиране `:6528`, атрибуцията в паметта `:6657`, D12/индекс/търсене и картончето `:7253`; **типово правило за `DISTRICT_FALLBACK`** — районен код в `quarter` не бива да чупи `!quarter` условието на районното търсене `:7064`), двата bundle теста (`test_places_public_bundle.py:55`, `test_hotels_public_bundle.py:61`), `expectations.json`, трите манифеста, референтният/паритетният корпус и Python паритетът на търсенето (D13 `:62`). Нощес изпълнителят **подготвя** дифа като кръпка (`scratch/places_search/b3_patch_07.09.diff`, непроследена) и фикстурата `client_cache_matrix.foreign_code_while_other_bundle_valid` (Node: валидни хотели, кеш v6/v7, crypto on/off; приемане = двата булеви валидатора минават И 150+225 реда реално се индексират; чужд код → наблюдаем отказ, не `places2=[]` мълчаливо). **Гейт (сутрин, след комитите и подписите на Петър):** замразената референция (нула изгубени резултати), шестте фикстури падат на счупен кандидат и минават след, `python -m unittest discover -s tests` и `python -m gates.run_gates` зелени, размерът ≤ 5 MB, никаква геометрия в проследените `data/*.json` на Fire_Varna (grep за `coordinates` в тях → 0 извън `data/hydrants.json`).
145: 
146: ### Б4 · Одит на Б1–Б3 и докладът
147: Одитор (Opus, read-only, друг агент) на всеки лот: гейтовете преизпълнени, дифът срещу write-set-а (всеки допълнителен файл = находка), авторите, съобщенията, sha веригата решения → граници → леджер → износ → доставка. Докладът `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna) носи числата на А и Б, всички sha, спрелите лотове с причината, и §„Какво прави Петър сутринта“: комит на `quarters_signed.geojson` (G4), препотвърждаване на решенията по sha, преглед на дифа в трите репа, регистърът (Ваялар, Евксиноград/Траката, Цветен квартал, `parents`, 16-те), Gate 2, пуш.
148: 
149: **Ред на изпълнение при подписан Б0 (Astra S21 т. 7):** договорите от §2а (скриптове + отрицателни фикстури, всяка доказано падаща) → Н0 (основа: HEAD-ове, мръсният диф, пинове, G19/G29) → Н1 → Н2-0 → Н2 → Н4 (мерки) → Н3-а (независим) → **Б1** (кандидат-подписан файл, стейджнат) → **Б2** само с Б0 т. 11 (G9 зелен), изходите стейджнати → **подготовка на Б3** (кръпка + фикстурата за шумно падане) → Б4 (одит) → Н5 (докладът, винаги). **STOP преди Б2**, ако Б0 т. 11 не е подписан или G9 е червен. **Сутринта:** комитите на Петър (геометрия, решения по sha с реда за атрибуция, износът) → Б3 като един атомен комит → подписи/freeze → пълен набор + 7/7 → одит → пуш. При червено в 03:00: чуждият проследен диф и последният зелен release остават непокътнати; откатът е по write-set (стейджнатото се маха с `git restore --staged`, изходите се трият по назован път) — общ `git revert` не е договор за стейджната геометрия.
150: 
151: ## 7 · Конфликти и нормализация (мярка, влиза в Н2/Н4 и в доклада)
152: - **Леджер на конфликтите по поле** за всяко от 375-те места: какво твърди всеки извор за квартала — регистровият запис (REG/KAIS/НТР, ранг), адресният низ (парсиран: „бул. Владислав Варненчик“ ≠ „кв. Владиславово“ — булевард и квартал носят едно име), кадастралният `quar` на най-близкото тяло, потвърденият полигон (координата), районът; колона `resolution` по правилото „координатата решава квартала; името е свидетел“, и колона `conflict_kind` ∈ {none, name_vs_polygon, parent_vs_child, pin_outside_all, written_outside_polygon}. Изход: `scratch/granitsi/conflict_ledger_07.09.json` (varna_3d, непроследен) + числата по вид в доклада. Нищо не се презаписва от този леджер; той е списъкът за Петър.
153: - **Сградите (Н4)** носят същите колони: кадастрален `quar` срещу полигона по координатата на тялото; несъгласията по вид (адрес на булевард с име на квартал; Кайсиева/Владиславово; Акчелар/Виница; курорт/квартал Чайка).
1: Reading additional input from stdin...
2: OpenAI Codex v0.153.3
3: --------
4: workdir: C:\git
5: model: gpt-6-astra
6: provider: openai
7: approval: never
8: sandbox: read-only
9: reasoning effort: ultra
10: reasoning summaries: none
11: session id: 01a0786b-58a5-7fa1-bece-f1106e8bee44
12: --------
13: user
14: S23 — REVIEW (lens MECHANICS) of lot Б1 second run (07.09) in C:/git/varna_3d (private, branch rezhimi; read-only): commits 63d077d ('build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)') and 8c262e9 ('gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)'), the STAGED uncommitted data/quarters_signed.geojson (60 Features: 58 wikimapia + 1 wikimapia_union dobreva from wm_ids [5729380, 5729421] + 1 declared_streets mladost2; sha256 4930f2043438edb9…, 295 304 B), src/build_quarters_signed.py, src/qa_quarters_signed.py, tests/test_quarters_signed_fixtures.py. Inputs: C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json (blob 2c650160… in Fire_Varna commit 895e0d2, author Claude Architect), the signed plan C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md (Б0 т. 1–12; §Б1 still says 61 Features / decisions 3). Your own F2 asked for the exact plan pin and a spatial district check — verify both fixes and their negatives (run: python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna; python -m unittest tests.test_quarters_signed_fixtures; the fixture files under tests/fixtures or the paths the test names). The per-lot auditor found (all minor): signature chain reaches decisions 3, not 4 (Petar has not signed decisions 4 by sha); C18 imports district_of/load_our_districts from the builder itself and reads the same layer (C:/git/m6000_private/number_viewer/quarters_layer.geojson) — not independent; the АГКК witness disagrees for vazrazhdane4 and kochmar (ours: vladislav_varnenchik; АГКК: 10135-03); the union pin d6f367bd… reproduces only through EPSG:4326→32635→4326 with shapely 2.1.2/pyproj 3.6.1 (degree-space union gives bc92a76c…); .gitignore:26 comment still says 61; §Б1 text drift. Questions: (1) Are the two commits exactly within the Б1 write-set of the plan, with exact messages/author, nothing else touched (git show --stat), hard limits intact (no push; registry untouched; ledger/identity/exports sha unchanged)? (2) Is the union construction deterministic and honestly pinned — should the artefact pin the DEGREE-space union instead (library-independent) or pin both, and what negative fixture proves the choice? (3) Is C18 acceptable as a gate if it shares code with the builder — propose the minimal independent check (e.g. point-in-polygon against agkk_au5 with a signed crosswalk of the 5 codes) and say what to do with the 2 disagreeing codes. (4) What exactly must Petar sign/commit now, in which order, for the chain decisions → artefact to be honest (decisions 4 by sha; the geometry commit message; the .gitignore comment)? Verdict ГОДНО/НЕГОДНО for Б1 second run with named fixes; at most 1200 words; Bulgarian with English identifiers; cite file:line and shas.
15: warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
16: codex
17: Ще проверя read-only двата commit-а, staged артефакта и връзката им с подписания план, после ще изпълня QA и fixture тестовете. Ще използвам skill `engineering:code-review` и ще отделя независим преглед на union pin-а и C18.
18: exec
19: "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/Varna_buildings/scratch/hydrant_map_integration_frame.md'" in C:\git
20:  succeeded in 41ms:
21: # Hydrant Map Integration â€” Framing / Handoff (Phase 2 Reintegration)
22: 
23: **Status:** Framing draft (chat-Claude). Input for a new architecture cycle.
24: **Date:** 2026-06-21
25: 
26: This document is the handoff for integrating the hydrant app with the
27: buildings pipeline. It is the gated "Phase 2 reintegration" that
28: `docs/architecture_v2.md` deferred (requires an ADR 020 amendment). Start
29: the new Cowork session by reading this + both repos, then run the cycle.
30: 
31: ---
32: 
33: ## 1. Purpose
34: 
35: A firefighter searches an address â†’ finds the nearest hydrants; sees all
36: hydrants for field verification; the owner adds/edits hydrants, building
37: annotations, and the verification design **without touching core code**.
38: Mobile-first is the primary purpose.
39: 
40: ## 2. The two repos
41: 
42: - **Varna_buildings** (PRIVATE, Python) â€” KAIS address/building pipeline +
43: 
44: 1. **Private pipeline â†’ public app.** Varna_buildings stays PRIVATE and
45:    build-time; it emits **curated, safe** outputs that feed Fire_Varna.
46:    Raw KAIS, intel, and personal data never cross to the public side.
47: 2. **Host = Fire_Varna Pages.** All user-facing functionality lives in the
48:    public app.
49: 3. **Mobile-first, light payload.** Heavy layers (`strategic_intel` ~34MB,
50:    `section_units` ~17MB, raw geocoder ~19MB) NEVER go to mobile.
51: 4. **Config/data-driven editing.** Hydrants, building annotations, and the
52:    verification flow are editable without touching core app logic.
53: 
54: ## 4. The "one repo" reframe (important)
55: 
56: The private/public split means they **cannot** be one git repo (a public
57: GitHub Pages repo cannot contain the private KAIS pipeline). So:
58: 
59: - **Two repos, clean split.** Varna_buildings (private pipeline) +
60:   Fire_Varna (public app).
61: - **Your day-to-day "one repo to debug/edit" is Fire_Varna** â€” it holds
62:   everything user-facing (map, hydrants, building display, search,
63:   verification config, data). You rarely touch the pipeline; it just
64:   regenerates building data from KAIS.
65: - **"Merge" = integrate capabilities + a curated data handoff**, NOT a
66:   git-history merge.
67: 
68: ## 5. Two constraints to design around
69: 
70: - **Mobile weight.** Core GPS â†’ nearest-hydrant needs **nothing** from
71:   buildings (just `hydrants.json`, already on device, offline). Address
72:   search needs a geocoder: either a **slim on-device index** (address-tier,
73:   `{text, lat, lng}` only â†’ under 1MB gzip, lazy-loaded + service-worker
74:   cached â†’ offline search) or a **Worker-side geocoder** (ultra-light, needs
75:   signal to search). Likely: slim on-device default, Worker as fallback.
76: - **Public/private boundary.** The pipeline publishes ONLY the safe subset
77:   (no raw KAIS, no personal data, KAIS-license-clean). A **publish gate**
78:   defines what is safe to cross to the public app.
79: 
80: ## 6. Mobile-lightness strategy
81: 
82: - Core (offline): `hydrants.json` + GPS â†’ nearest, MarkerCluster for 6k
83:   points (already exists).
84: - Address search: slim geocoder (<1MB gzip, lazy, SW-cached) or Worker.
85: - Footprints: optional â€” simplified / viewport-only / lazy.
86: - Service worker: offline cache + fast repeat boot; hydrants-first boot.
87: 
88: ## 7. Config / data-driven layers (edit without code)
89: 
90: - **Hydrants:** curated dataset + the existing ðŸš¨ â†’ Worker â†’ GitHub flow
91:   (extend for add/edit).
92: - **Buildings:** an **override/annotation layer** (name / status / note) on
93:   top of pipeline-derived data; editable file or UI â†’ Worker â†’ GitHub; the
94:   pipeline regenerates under it and overrides persist. (Buildings are
95:   derived from KAIS â€” you cannot edit them like hydrants; you annotate via
96:   overrides, a pattern the pipeline already uses with sidecars.)
97: - **Verification:** a `verification_config.json` defining form fields,
98:   statuses, labels, and colors/icons; the app renders verification FROM it.
99:   Edit the config â†’ change the verification flow and look, no app-logic
100:   touch. Theming via CSS variables for visual changes; a ground-up layout

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$i=135; Get-Content -Encoding UTF8 -LiteralPath '"'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md' | Select-Object -Skip 135 -First 7 | ForEach-Object { "'$i++; '"'{0}: {1}' -f "'$i,$_ }; Get-Content -Encoding UTF8 -LiteralPath scratch/places_search/granitsi_b1v2_astra_S23_07.09.md -Tail 48' in C:\git\Fire_Varna
 succeeded in 14ms:
139: 
140: ### Б2 · Присвояване P8-а (varna_3d) — тръгва само с подписано Б0 т. 11; изходите са КАНДИДАТИ за комита на Петър
141: Write-set: `src/fire_varna_locations.py` (каналът `SIGNED_POLYGON` + `DISTRICT_FALLBACK`, четене на `quarters_signed.geojson` по sha; `LEDGER` сочи НОВ датиран леджер `scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` с `_meta.base_rev` = комитът на стария; старият не се пипа), `src/qa_p8a.py`, `data/fire_varna_places.json`, `data/fire_varna_hotels.json` (износът), `data/fire_varna_location_inputs.json` (пиновете, вкл. `quarters_signed.geojson` sha), новият леджер. Съобщения: `feat(p8a): SIGNED_POLYGON channel with district fallback, new dated ledger, written quarters untouched` · `data: places export with quarter_attribution (decisions 3)`. Правила: само ПРАЗЕН квартал се пише; най-малкият съдържащ полигон; двойка без подписано родство и място в двата → `disputed`, не се пише; ръб `max(50, precision_m)` → `edge_pending`; без полигон → районът само по Б0 т. 4 (i)–(iii): не в зони на отложени кодове, не при `pin_outside_all` без съгласен свидетел, и винаги заместим; записан ≠ полигон → леджер `disputed`, редът непроменен (G17). Гейт: fallback-ред в зона на отложен код → ✗; fallback-ред, защитен от G17 в следваща версия → ✗ (фикстура с втора версия, в която подписан полигон трябва да го замести). Координати: САМО от `place_identity.json` след хода по Б0 т. 11 (G9 зелен); изнесените координати са забранени за присвояване (D7) — гейт: скриптът не отваря `data/fire_varna_*.json` за четене на координати (AST-проверка като в Н4). Изходите на таблицата по Б0 т. 12 се броят и записват поименно. Десетият ключ по Б0 т. 5 във varna_3d: `META_KEYS` (places 9→10, hotels 7→8 — измерено от Astra), двата износителя (`export_fire_varna_places.py:816`, `export_fire_varna_hotels.py:420`), QA/M6 и `build_place_categories.py` (родители и полигонен провенанс) в един varna_3d комит на изпълнителя; **износените данни (`data/fire_varna_*.json`, новият леджер) остават стейджнати за комита на Петър** (D16/G4) с готово съобщение в доклада. **Гейт (червен):** G17 (всеки записан квартал в стария леджер-блоб `git show <base_rev>:…` е байт-равен в новия износ), G4 (fail-closed без подпис → тук подписът е този план + sha на решенията, записани в `_meta`), `qa_fire_varna_places_export.py` с 10 ключа, брой присвоени = броят „би получил“ от Н2 (мярката и резултатът трябва да съвпадат до място), `edge_pending` и `disputed` в леджера поименно, `python -m unittest` зелен.
142: 
Decisions 4 в `895e0d2651aac73516659f2a10ea5193b2be5d53`, автор `Claude Architect`, има точен SHA:
`2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89`.

[Б0.8:131](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:131) подписва decisions 3 (`ec2813e1c074…`). Builder constants, `based_on` и `signed_by:"Petar"` не разширяват този подпис. Твърдението в [builder:1152](C:/git/varna_3d/src/build_quarters_signed.py:1152) за подпис от 06.09 върху новите решения е неподкрепено.

Допълнително: decisions 4 има **0/68 `attribution`**, а Б0.8 изисква добавянето му. След тази поправка SHA ще бъде нов — подписът трябва да обхване окончателния blob.

4. **S23-F2: union pin и декларацията за построяване**

**Запазете projected union като авторитетен**: raw `d6f367bd…`, D1 `b42a74d11774…`. Degree-space дава raw `bc92a76c…`, D1 `fc1f72976ace…`. Degree-space `unary_union` също зависи от GEOS; не е library-independent.

Три повторения и обърнат ред на частите възпроизвеждат projected pin при Shapely **2.1.2/GEOS3.13.1**, pyproj **3.6.1/PROJ9.3.0**. Рецептата е [builder:551](C:/git/varna_3d/src/build_quarters_signed.py:551).

Обяснението „само `1e-14°`“ е невярно, включително в произведения [metadata:988](C:/git/varna_3d/src/build_quarters_signed.py:988): максималната координатна разлика е `4.177×10⁻⁷°`; различават се и D1 hashes. Поправете текста и запишете версията на рецептата/библиотеките. Degree pin може да остане диагностичен witness, без да става втори допустим резултат.

Доказателства:

- Degree geometry с преизчислени **и двата собствени hashes** пада по **C4** срещу decisions pin.
- Преместена union част с поправен собствен hash пада по **A9**.
- **Само `_meta.union_crs="EPSG:4326"` минава целия QA!**

Добавете `degree_union_self_rehashed → C4` и `union_crs_substituted → FAIL`. [QA:176](C:/git/varna_3d/src/qa_quarters_signed.py:176), [QA:732](C:/git/varna_3d/src/qa_quarters_signed.py:732).

5. **S23-F3: независим district witness**

C18 е приемлив като consistency gate; общите [imports:75](C:/git/varna_3d/src/qa_quarters_signed.py:75) оставят общ дефект в builder/слоя невидим.

Независим PIP срещу AU5 даде **58 съгласни, точно 2 спора, 0 неоднозначни**. `kochmar` и `vazrazhdane4` са `vladislav_varnenchik` в артефакта, но попадат в `10135-03`; точките са съответно **782 m/509 m** навътре от AU5 boundary.

Минимумът: отделна QA функция без builder district helpers; pinned AU5 SHA `78a2de59600eb…`; подписан crosswalk:

`10135-01→odesos; 02→primorski; 03→mladost; 04→vladislav_varnenchik; 05→asparuhovo`.

FAIL при неизвестен/дублиран код, 0/≥2 hits или неприет конфликт. Негативи: разменени `03/04`, нов трети конфликт.

Двата спора чакат поименно решение: подписани exceptions с geometry/source hashes и довод, или отделно одобрена корекция. **Без автоматична замяна с `mladost`** — [Б0.4:127](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:127) изисква нашия източник.

6. **Редът за Петър**

1. Подписан addendum: decisions 4, 60 Features, union/exclusion, действителните commit messages, union рецептата и district решенията. Старото подписано тяло се запазва.
2. Подготовка на окончателните decisions 4 с `attribution`; **Петър подписва окончателния SHA и комитва решенията**.
3. Одобрените code/QA/fixture поправки и [.gitignore:26](C:/git/varna_3d/.gitignore:26): 60 Features; поправка и на невярното „не се регенерира“. Обновяване на pins/signature metadata; rebuild и gates.
4. Петър преглежда новия artifact SHA и комитва геометрията:

   `data: signed quarter boundaries v1 (decisions 4, sha <final-decisions-12>)`

   Пълните decisions/artifact SHA в body. Днешният `4930…` неизбежно се сменя след metadata поправките.
5. Оригиналният suite в среда с разрешени тестови записи, независим одит, Gate 2; push само от Петър.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import subprocess,hashlib,json,pathlib
b=subprocess.check_output(['git','cat-file','blob',':data/quarters_signed.geojson'])
assert len(b)==301917 and hashlib.sha256(b).hexdigest()=='c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3'
assert pathlib.Path('data/quarters_signed.geojson').read_bytes()==b
print('FINAL_INDEX',len(b),hashlib.sha256(b).hexdigest())
print('STAGED',subprocess.check_output(['git','diff','--cached','--name-only']).decode())
print('HEAD',subprocess.check_output(['git','rev-parse','HEAD']).decode().strip())
'@ | python -" in C:\git\varna_3d
 succeeded in 51ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
FINAL_INDEX 301917 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3
STAGED data/quarters_signed.geojson

HEAD e2da30703e6a063aae6accfd2698dbe5c98b3d5f

codex
**Присъда: НЕГОДНО за commit сега.** Точният artefact е механично годен; остават недоказан final подпис, неприключил пълен `unittest` и непотвърден текущ G19. Нито един от трите minors не налага промяна на проверените bytes.

1. **S23 F1–F3**

- **F1: механичната верига е затворена.** Final decisions 4 blob в `Fire_Varna@3d747d3` е **32129 B**, SHA256 `74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b`; включва `attribution` и съвпада с `_meta.decisions_sha256`. [decisions:854](C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json:854), [tests:53](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:53). **Човешкият подпис остава незатворен:** commit-ът е на `Claude Executor`; subject „Petar signs…“ не удостоверява подпис. [Б0.8:131](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:131) изисква препотвърждаване на окончателния blob.
- **F2: затворено.** Авторитетен е projected union `EPSG:32635`, raw `d6f367bd…`, D1 `b42a74d1…`; degree union остава различна диагностика. Рецептата носи Shapely **2.1.2**, GEOS **3.13.1**, pyproj **3.6.1**, PROJ **9.3.0**. Двата negatives действително падат: `degree_union_self_rehashed → C4`, `union_crs_substituted → C19`. [QA:603](C:/git/varna_3d/src/qa_quarters_signed.py:603), [tests:109](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:109).
- **F3: технически затворено.** C20 прави собствен PIP срещу pinned AU5 `78a2de59600eb…`, с отделен crosswalk. `kochmar` и `vazrazhdane4` са `mladost`, `district_src=agkk_au5_confirmed_by_petar`; няма pending спор. Приемат се само AU5-consistent resolutions. [QA:684](C:/git/varna_3d/src/qa_quarters_signed.py:684), [QA:871](C:/git/varna_3d/src/qa_quarters_signed.py:871). Решение 9 е записано от Петър; отделен човешки подпис върху всичките пет crosswalk двойки не намерих — включен е в текста по-долу.

2. **Изпълнени проверки**

| Проверка | Резултат |
|---|---|
| Заявената `qa_quarters_signed.py … --registry … --decisions-repo …` | **exit 0**, C1–C20 зелени |
| `python -m unittest tests.test_quarters_signed_fixtures` | **exit 1**, **0 tests**: `PermissionError` при `shutil.rmtree(FIXTURES)` |
| 39 налични negative fixtures, без регенериране | Всяка **exit 1**, правилният check; runner **exit 0** |
| Пет read-only unittest метода | **5/5 PASS**, exit 0 |
| Две сглобявания изцяло в паметта | Байт-равни на index/worktree |
| `qa_no_cad_ids.py`, `qa_no_extrude.py` | **exit 0 / 0** |

Отказаният запис е в [tests:157](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:157). Допълнителните проверки **не превръщат пълния suite в PASS**. Първоначалният QA отказ за Git ownership беше отстранен само с process-scoped `safe.directory`, без редакция на Git config.

3. **Трите minors**

- **`ours`: може да чака този commit; поправка преди следващо генериране.** Доказан false-pass: само `ours→odesos` минава целия QA. C20 проверява различие от resolved district, без равенство с измерения наш район. Но независимо преизчислените **текущи** две стойности са правилните `vladislav_varnenchik`. [QA:579](C:/git/varna_3d/src/qa_quarters_signed.py:579), [QA:833](C:/git/varna_3d/src/qa_quarters_signed.py:833).
- **`features_with_our_district`: може да чака.** Новата семантика дава верни **58 от нашия слой + 2 resolved = 60**; не открих downstream consumer. Нужна е документация на семантиката. [builder:1193](C:/git/varna_3d/src/build_quarters_signed.py:1193).
- **Hardcoded resolutions SHA: допустим за този lot.** Това е независим trust anchor срещу подмяна на input и metadata едновременно. Да не се премахва като cleanup. [QA:126](C:/git/varna_3d/src/qa_quarters_signed.py:126), [QA:761](C:/git/varna_3d/src/qa_quarters_signed.py:761).

4. **Какво остава преди commit**

Петър трябва да получи пълен suite **exit 0** и G19 **PRIVATE / exit 0**. Моят `gh repo view Petar1984/varna_3d --json visibility` даде **401 / exit 1**. Последното записано PRIVATE е от 06.09; това не доказва текуща промяна на visibility. [pins:63](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:63), [G19 STOP:68](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:68).

Registry е чист и непроменен: SHA256 `7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6`. `vinitsa_sever` няма Feature; деактивирането в registry остава отделен ход. Геометрията остава частна; няма разрешение за push.

Точното commit message за Петър — subject и неговото лично подписно изречение като body:

```text
data: signed quarter boundaries v1 (decisions 4, sha 74f09d505e2b)

Подписвам окончателния Git blob scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json от Fire_Varna@3d747d3308bf31fe17add9a510ad97423adc672a със SHA256 74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b, включително attribution, union Добрева чешма и изключването vinitsa_sever; потвърждавам решение 9 със SHA256 d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc и AU5 crosswalk 10135-01→odesos, 10135-02→primorski, 10135-03→mladost, 10135-04→vladislav_varnenchik, 10135-05→asparuhovo; приемам Б1 с 60 Features, 301917 B и artifact SHA256 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3.
```

Непосредствено преди commit, **в Git Bash**, от `C:/git/varna_3d`:

```bash
git diff --cached --name-only
git cat-file -s :data/quarters_signed.geojson
git cat-file blob :data/quarters_signed.geojson | sha256sum
```

Очакване: само `data/quarters_signed.geojson`; **301917**; **`c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3`**. Това е повторно измереният staged SHA. След зелените проверки и личния подпис: **ГОДНО за този точен blob**.
tokens used
93,220
**Присъда: НЕГОДНО за commit сега.** Точният artefact е механично годен; остават недоказан final подпис, неприключил пълен `unittest` и непотвърден текущ G19. Нито един от трите minors не налага промяна на проверените bytes.

1. **S23 F1–F3**

- **F1: механичната верига е затворена.** Final decisions 4 blob в `Fire_Varna@3d747d3` е **32129 B**, SHA256 `74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b`; включва `attribution` и съвпада с `_meta.decisions_sha256`. [decisions:854](C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json:854), [tests:53](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:53). **Човешкият подпис остава незатворен:** commit-ът е на `Claude Executor`; subject „Petar signs…“ не удостоверява подпис. [Б0.8:131](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:131) изисква препотвърждаване на окончателния blob.
- **F2: затворено.** Авторитетен е projected union `EPSG:32635`, raw `d6f367bd…`, D1 `b42a74d1…`; degree union остава различна диагностика. Рецептата носи Shapely **2.1.2**, GEOS **3.13.1**, pyproj **3.6.1**, PROJ **9.3.0**. Двата negatives действително падат: `degree_union_self_rehashed → C4`, `union_crs_substituted → C19`. [QA:603](C:/git/varna_3d/src/qa_quarters_signed.py:603), [tests:109](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:109).
- **F3: технически затворено.** C20 прави собствен PIP срещу pinned AU5 `78a2de59600eb…`, с отделен crosswalk. `kochmar` и `vazrazhdane4` са `mladost`, `district_src=agkk_au5_confirmed_by_petar`; няма pending спор. Приемат се само AU5-consistent resolutions. [QA:684](C:/git/varna_3d/src/qa_quarters_signed.py:684), [QA:871](C:/git/varna_3d/src/qa_quarters_signed.py:871). Решение 9 е записано от Петър; отделен човешки подпис върху всичките пет crosswalk двойки не намерих — включен е в текста по-долу.

2. **Изпълнени проверки**

| Проверка | Резултат |
|---|---|
| Заявената `qa_quarters_signed.py … --registry … --decisions-repo …` | **exit 0**, C1–C20 зелени |
| `python -m unittest tests.test_quarters_signed_fixtures` | **exit 1**, **0 tests**: `PermissionError` при `shutil.rmtree(FIXTURES)` |
| 39 налични negative fixtures, без регенериране | Всяка **exit 1**, правилният check; runner **exit 0** |
| Пет read-only unittest метода | **5/5 PASS**, exit 0 |
| Две сглобявания изцяло в паметта | Байт-равни на index/worktree |
| `qa_no_cad_ids.py`, `qa_no_extrude.py` | **exit 0 / 0** |

Отказаният запис е в [tests:157](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:157). Допълнителните проверки **не превръщат пълния suite в PASS**. Първоначалният QA отказ за Git ownership беше отстранен само с process-scoped `safe.directory`, без редакция на Git config.

3. **Трите minors**

- **`ours`: може да чака този commit; поправка преди следващо генериране.** Доказан false-pass: само `ours→odesos` минава целия QA. C20 проверява различие от resolved district, без равенство с измерения наш район. Но независимо преизчислените **текущи** две стойности са правилните `vladislav_varnenchik`. [QA:579](C:/git/varna_3d/src/qa_quarters_signed.py:579), [QA:833](C:/git/varna_3d/src/qa_quarters_signed.py:833).
- **`features_with_our_district`: може да чака.** Новата семантика дава верни **58 от нашия слой + 2 resolved = 60**; не открих downstream consumer. Нужна е документация на семантиката. [builder:1193](C:/git/varna_3d/src/build_quarters_signed.py:1193).
- **Hardcoded resolutions SHA: допустим за този lot.** Това е независим trust anchor срещу подмяна на input и metadata едновременно. Да не се премахва като cleanup. [QA:126](C:/git/varna_3d/src/qa_quarters_signed.py:126), [QA:761](C:/git/varna_3d/src/qa_quarters_signed.py:761).

4. **Какво остава преди commit**

Петър трябва да получи пълен suite **exit 0** и G19 **PRIVATE / exit 0**. Моят `gh repo view Petar1984/varna_3d --json visibility` даде **401 / exit 1**. Последното записано PRIVATE е от 06.09; това не доказва текуща промяна на visibility. [pins:63](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:63), [G19 STOP:68](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:68).

Registry е чист и непроменен: SHA256 `7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6`. `vinitsa_sever` няма Feature; деактивирането в registry остава отделен ход. Геометрията остава частна; няма разрешение за push.

Точното commit message за Петър — subject и неговото лично подписно изречение като body:

```text
data: signed quarter boundaries v1 (decisions 4, sha 74f09d505e2b)

Подписвам окончателния Git blob scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json от Fire_Varna@3d747d3308bf31fe17add9a510ad97423adc672a със SHA256 74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b, включително attribution, union Добрева чешма и изключването vinitsa_sever; потвърждавам решение 9 със SHA256 d494d4d256aeb1e3115d01a97a422202eb7247934b2576996eb6159b169844dc и AU5 crosswalk 10135-01→odesos, 10135-02→primorski, 10135-03→mladost, 10135-04→vladislav_varnenchik, 10135-05→asparuhovo; приемам Б1 с 60 Features, 301917 B и artifact SHA256 c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3.
```

Непосредствено преди commit, **в Git Bash**, от `C:/git/varna_3d`:

```bash
git diff --cached --name-only
git cat-file -s :data/quarters_signed.geojson
git cat-file blob :data/quarters_signed.geojson | sha256sum
```

Очакване: само `data/quarters_signed.geojson`; **301917**; **`c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3`**. Това е повторно измереният staged SHA. След зелените проверки и личния подпис: **ГОДНО за този точен blob**.
