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
session id: 01a079e7-ed37-78d1-9b7b-da0c12b82ac6
--------
user
S26 — POST-EXECUTION REVIEW (lens MECHANICS) of lot Б2 rerun under signed amendment 3, before Petar commits. Repos read-only: C:/git/varna_3d (branch rezhimi): commits since 6486b48 — 3de6661, 5c6fdd0, da77ff2, 0ecd814, a28edc2, 8a60972, 7bac5e5, bb09535, 4bdcc7c, 36e8513, 679451d, 2624218, 822656d, bd00c2c, 0c1ed71, 26da605, plus an architect .gitignore commit 1217dc4 (!data/zone_alias_overrides.json). STAGED uncommitted (for Petar): data/place_identity.json (4819ab3e…), data/fire_varna_location_inputs.json (c7450ded…), data/fire_varna_places.json (3dffc264…), data/fire_varna_hotels.json (eb8fa85c…), data/place_categories.json (9064705a…), data/registry_manifest.json (bb04640e…, 9 rows changed per decision 6), scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json (5ec64c68…, force-added). Amendment: C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md (§3 write-set/messages, §4 order, §5 gates, §6 Petar commits, §9 П1–П5, §10 A1–A7). State: C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md §5–§6. Verify: (1) every commit vs the amendment write-set and messages (six verbatim rows; the extra commits carry §9/§10 conditions — acceptable?), author, no canonical data commits (reflog); (2) run at HEAD with the staged data: python src/qa_p8a.py, python src/qa_fire_varna_places_export.py, python src/qa_fixed_point.py (as documented), python src/qa_place_zone_aliases.py, python src/qa_fire_varna_m6.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json (expect fails 0, exit 3 with exactly eight pending ids), python src/qa_identity_rekey.py with tests/fixtures/identity_rekey_base_2026-09-07.json, python -m unittest discover -s tests, python src/qa_no_cad_ids.py — exit codes; (3) G17: written quarters byte-equal vs git show 8d60aebb:scratch/refactor/_addr/lot1v_locations_375.json; П4: 57 zone changes only on empty rows; place_id 375/375 vs the fixture; pins in fire_varna_location_inputs.json consistent with the staged identity sha and the ledger path/sha; (4) the exact three commits for Petar per §6 — messages (name all payloads: coordinates Б0 т. 11, re-key, 57 refreshed zones, pins, manifest 9 rows), pathspecs so that each commit takes only its files from the index (git commit -F <file> -- <paths>), and the pre-commit byte checks (git cat-file blob :path | sha256sum); (5) anything unsafe for the later publication of varna_3d (private remote) — e.g. the force-added ledger under an ignored path, the dirty scratch/place_bodies/qa_place_bodies.md overwritten by the aborted first Б2 run (Petar decides), dangling commits in reflog. Verdict ГОДНО/НЕГОДНО for Petar to commit now; at most 1300 words; Bulgarian with English identifiers; cite file:line and shas.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще сверя amendment 3 със състоянието на index, commit историята и QA резултатите. Ще разделя проверката на механиката на commit-ите и целостта на данните между независими агенти; всички действия остават read-only.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/Varna_buildings/scratch/hydrant_map_integration_frame.md' -Raw" in C:\git
 succeeded in 127ms:
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Location; rg --files -g AGENTS.md -g CLAUDE.md -g '*амандамент_3*' -g '*СЪСТОЯНИЕ_Границите*' 'C:/git/varna_3d' 'C:/git/Fire_Varna'" in C:\git
 succeeded in 140ms:
C:/git/varna_3d\CLAUDE.md
C:/git/varna_3d\AGENTS.md
C:/git/Fire_Varna\docs\sessions\СЪСТОЯНИЕ_Границите_06.09.md
C:/git/Fire_Varna\docs\plans\ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md
C:/git/Fire_Varna\docs\plans\ПЛАН_ИЗЧИСТВАНЕ_v2_амандамент_3_05.09.md
C:/git/Fire_Varna\CLAUDE.md
C:/git/Fire_Varna\AGENTS.md
Path  
----  
C:\git



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/code-review/SKILL.md' -Raw" in C:\git
 succeeded in 0ms:
---
name: code-review
description: Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.
argument-hint: "<PR URL, diff, or file path>"
---

# /code-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review code changes with a structured lens on security, performance, correctness, and maintainability.

## Usage

```
/code-review <PR URL or file path>
```

Review the provided code changes: @$1

If no specific file or URL is provided, ask what to review.

## How It Works

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                      CODE REVIEW                                   â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  STANDALONE (always works)                                       â”‚
â”‚  âœ“ Paste a diff, PR URL, or point to files                      â”‚
â”‚  âœ“ Security audit (OWASP top 10, injection, auth)               â”‚
â”‚  âœ“ Performance review (N+1, memory leaks, complexity)           â”‚
â”‚  âœ“ Correctness (edge cases, error handling, race conditions)    â”‚
â”‚  âœ“ Style (naming, structure, readability)                        â”‚
â”‚  âœ“ Actionable suggestions with code examples                    â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  SUPERCHARGED (when you connect your tools)                      â”‚
â”‚  + Source control: Pull PR diff automatically                    â”‚
â”‚  + Project tracker: Link findings to tickets                     â”‚
â”‚  + Knowledge base: Check against team coding standards           â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## Review Dimensions

### Security
- SQL injection, XSS, CSRF
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure deserialization
- Path traversal
- SSRF

### Performance
- N+1 queries
- Unnecessary memory allocations
- Algorithmic complexity (O(nÂ²) in hot paths)
- Missing database indexes
- Unbounded queries or loops
- Resource leaks

### Correctness
- Edge cases (empty input, null, overflow)
- Race conditions and concurrency issues
- Error handling and propagation
- Off-by-one errors
- Type safety

### Maintainability
- Naming clarity
- Single responsibility
- Duplication
- Test coverage
- Documentation for non-obvious logic

## Output

```markdown
## Code Review: [PR title or file]

### Summary
[1-2 sentence overview of the changes and overall quality]

### Critical Issues
| # | File | Line | Issue | Severity |
|---|------|------|-------|----------|
| 1 | [file] | [line] | [description] | ðŸ”´ Critical |

### Suggestions
| # | File | Line | Suggestion | Category |
|---|------|------|------------|----------|
| 1 | [file] | [line] | [description] | Performance |

### What Looks Good
- [Positive observations]

### Verdict
[Approve / Request Changes / Needs Discussion]
```

## If Connectors Available

If **~~source control** is connected:
- Pull the PR diff automatically from the URL
- Check CI status and test results

If **~~project tracker** is connected:
- Link findings to related tickets
- Verify the PR addresses the stated requirements

If **~~knowledge base** is connected:
- Check changes against team coding standards and style guides

## Tips

1. **Provide context** â€” "This is a hot path" or "This handles PII" helps me focus.
2. **Specify concerns** â€” "Focus on security" narrows the review.
3. **Include tests** â€” I'll check test coverage and quality too.


exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); Get-Content -Encoding utf8 -LiteralPath '"'C:/git/varna_3d/AGENTS.md','C:/git/varna_3d/CLAUDE.md','C:/git/Fire_Varna/AGENTS.md','C:/git/Fire_Varna/CLAUDE.md'" in C:\git
 succeeded in 0ms:
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
# CLAUDE.md — Executor guide for Varna 3D

Read [AGENTS.md](AGENTS.md) first for roles and gates, [DATA.md](DATA.md) for
what the data actually contains, [README.md](README.md) for scope.

## Orientation — what · trunk · forbidden · entry point · live numbers

- **What this repo is** — `AGENTS.md`, section *What this repo is*.
- **Trunk** — `AGENTS.md`, section *The trunk*. Whichever branch it turns out to be, an
  agent never pushes it (`AGENTS.md`, hard rule 1).
- **Forbidden here** — the hard rules are in `AGENTS.md`; the executor-side list is
  *Before you build a mesh* and *When to stop and ask* below.
- **Entry point** — `AGENTS.md`, section *Entry point*. Today it is `СЪСТОЯНИЕ.md` in
  the repo root; LOT 4 of the plan of 2026-09-01 moves it to `docs/СЪСТОЯНИЕ.md`, and
  after LOT 5 the entry point becomes `docs/activeContext.md`.
- **Live numbers** — `AGENTS.md`, section *Live numbers*. The rule for this file: **no
  state number enters it** — no count of buildings, sections, entrances, commits, QA
  scripts or tracked files. A number the work needs is measured with its own command
  (`AGENTS.md`, hard rule 5); it is never copied out of a document.

## Where things are

| What | Path |
|---|---|
| KAIS shapefiles (BGS2005) | `C:\git\Varna_buildings\data\extracted\` |
| Derived outputs (age, OSM links, clusters) | `C:\git\Varna_buildings\output\` |
| Quarter/district layer | `C:\git\m6000_private\number_viewer\quarters_layer.geojson` |
| Sensitive (cadnum-bearing) | `C:\git\m6000_private\` — **stays there** |
| Bridge to Sol | `C:\git\bridge\` (`to_gpt/`, `from_gpt/`, `ЖУРНАЛ.md`) |
| State (entry point) | `СЪСТОЯНИЕ.md` in the repo root — see **Orientation** above (LOT 4 moves it to `docs/СЪСТОЯНИЕ.md`) |
| Repo gates | `src/qa_*.py`. Mandatory before every commit under a signed plan: `qa_no_cad_ids.py`, which judges every tracked file (`git ls-files`) for cadastral identifiers — the exceptions are enumerated with their reason in its `ALLOW` block — and `qa_no_extrude.py`, which judges `data/no_extrude_verdicts.json`. `scrub_cad_ids.py` masks identifiers and keeps the audit trail |
| Map, locally | `Varna 3D.bat` → `serve.py` on port 8791, serving `C:\git`, opens `web/index.html`. Not `python -m http.server`: PMTiles needs HTTP Range (byte serving) |

## Reading the shapefiles — the two traps

```python
# UTF-8, not cp1251. Wrong encoding renders Cyrillic as "Р–РёР»РёС‰РЅР°".
r = shapefile.Reader(path, encoding="utf-8", encodingErrors="replace")
```

Coordinates are **BGS2005**. Reproject with `pyproj` before anything else, and
validate the result against the Varna bounding box — stop the build if it fails.

## Style

- **Python 3.10+**, `pyshp` / `pyproj` / `shapely` / `trimesh` / `numpy` /
  `scipy` / `Pillow` / `mapbox_earcut` / `rasterio`. No system GDAL of its own; `rasterio` ships GDAL inside its wheel.
- **Code and comments in English.** Bulgarian only in docs and UI text.
- **One concern per script.** Pipeline scripts in `src/`, probes in `scratch/`.
- **Reproducible.** Everything regenerable from the KAIS extract + free sources.
- **No silent failure.** Validate, then write. Never write, then hope.

## Before you build a mesh

1. Is Phase 0 (licensing) signed? If not, stop and say so.
2. Does the step have a signed plan? If not, you are the Planner, not the
   Executor — write the plan, do not edit.
3. Does the output contain any `cadnum`? If yes, it stays in `m6000_private`.

## When to stop and ask

- An acceptance check fails and there is no obvious safe fix.
- A licence turns out to forbid the intended use.
- A step would touch `Varna_buildings`, `Fire_Varna`, or anything outside this
  folder.
- You find state you did not create — investigate before overwriting; it may be
  Petar's work in progress.
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=0; Get-Content -Encoding utf8 -LiteralPath '"'C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md' | ForEach-Object { "'$n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git
 succeeded in 0ms:
1: # Амандамент №3 към ЛОТ „Границите" (07.09.2026) — самоличността на местата срещу квартала
2: 
3: **§0 · Място в редицата.** Продължава редицата на ЛОТА: `ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md` → `_2_06.09.md` → този, №3. Изменя **Б2** от подписания `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md`; не редактира нито един подписан ред.
4: 
5: **Клас: 🔴 Архитектурен.** Спуснати спусъци: променя подписан договор за данните (ключът на самоличността) · мутира каноничното `data/place_identity.json` · пипа данни, които пътуват към Fire_Varna · сменя и добавя гейтове. **Топология: Вариант А.** **Статус: ЗА ПОДПИС (Gate 1). НЕПОДПИСАН.**
6: **Не отваря нищо ново:** Б3/търсенето, регистърът, `quarters_signed.geojson`, написаните 201 квартала и живата карта не се пипат. Нула пуш.
7: 
8: ## 1 · Мярката (read-only, 07.09)
9: 
10: 1. **Ключът и котвите.** `src/place_identity.py:207,222`: `base = "<файл>|skel(име)|zone"`. `anchors_of()` (`:569-583`) дава четири нива: `reg` · `ntr` · `kais` · и чак после `key`, в който седи зоната (`:582`). Стара самоличност, която нищо не намира, е „оттеглена БЕЗ решение" и СПИРА билда (`:813-816`). `site_id` НЕ е котва (`:623-659`).
11: 2. **Кой виси на крехкия ключ.** `scratch/granitsi/aud_regen.log:3`: ntr 192 · kais 144 · reg 35 · **key 4**. 371/375 не зависят от зоната. Четирите са две двойки върху едно кадастрално тяло: ДГ№52 + Диспансерът (`kais_i` 1523) и III ПМГ + ОУ „П. Р. Славейков" (`kais_i` 39992).
12: 3. **Кои два реда падат.** В спрения износ втората двойка минава `район Одесос → кв. Тракия` (`SIGNED_POLYGON`); ключовете се менят, `kais` е двусмислена, `reg`/`ntr` ги няма → два сирака, генераторът пада. 55 от 57-те смени на зона се спасяват от reg/ntr/kais.
13: 4. **Присвояването вече носи `place_id`.** `fire_varna_locations.py:967-979` свързва по УИН, после по `(файл, skel(име))` — „by evidence, never by zone". Леджерът е `{_meta, rows, quarantine}`, като **`rows` е СПИСЪК от 375 реда**, всеки с `place_id`/`old_zone`/`new_zone`; `old_zone` идва от ЗАМРАЗЕНИЯ блок `legacy_zones` (`:886-893`, покрива 375/375), не от зоната в самоличността. Речник по `place_id` е само `book.rows` в паметта (`:1937`).
14: 5. **Износът не може да носи id.** `place_identity.py:38-40`: публичните `data/fire_varna_*.json` не носят id — подписан договор.
15: 6. **Стълкновения без зоната.** Мерено: местата дават 150 различни скелета от 150 (нула стълкновения); хотелите — четири двойки (`admiral`, `perla`, `roial`, `rusalka`), и осемте реда `matched_by: "ntr"`, решавани по УИН.
16: 7. **Речникът на търсенето.** `qa_place_zone_aliases.py` пада на проверка (а) (`:213-217`). Числото в СЪСТОЯНИЕ §5 („три зони") е ОТРЯЗАН текст (`lost[:3]`): доставените непознати зони са **ОСЕМ** — Гръцката махала, Долна Трака, Колхозен пазар, Център, кв. Левски, кв. Св. Иван Рилски, кв. Тракия, кв. Христо Ботев. И осемте са ДОСЛОВНИ `display` низове в `quarter_registry.json`, а `build_place_categories.py:300-329` строи псевдонимите САМО от регистъра → лекът е прегенериране, нула ръчни низове.
17: 8. **М6 и формата на свидетеля (D6).** `CH_SIGNED_POLYGON` не е в `CHANNELS` (`:173-180`), затова редът носи `witness.quarter = ["SIGNED_POLYGON"]` без код в `channels` → проверка (б) (`qa_fire_varna_m6.py:304-308`) обявява 57 нарушители. Мерено днес: `qa_fire_varna_m6.py` връща **изход 3** („ЧАКА ПОДПИС: 8 реда", `:367`), не 0; спреният леджер носи същите 8 (`_meta.counts.pending_signature = 8`).
18: 9. **Пиновете.** `_check_pins` (`:922-949`) сверява НТР, двете таблици, `quarters_signed` и базата на леджера — но НЕ блока `inputs` (`RECORDED_INPUTS :108`). Затова `data/fire_varna_location_inputs.json:51` пинва `e8b4c836…`, а стейджнатата самоличност е `1141bbc2…`. Отделно `web/varna_buildings_3d.geojson` — ИЗВОРЪТ на координатите (`place_identity.py:90`) — изобщо не е в `RECORDED_INPUTS`, макар D10 (`010:56`) да го иска.
19: 
20: ## 2 · Двата пътя и присъдата
21: 
22: **Път Б** (ключът остава; `place_id` се носи през леджера) е механично възможен, но (i) износът не може да носи id, значи единственият носител е леджерът; (ii) зоната остава В КЛЮЧА, значи всяко чисто `python src/place_identity.py` (командата от собствения докстринг `:60`) връща същите два сирака. Ред на действията не е гейт.
23: 
24: **Път А** (`<файл>|skel(име)`): измерено — **375/375 `place_id` остават същите**; сменя се само полето `key` на 375-те живи обекта (оттеглените пазят записаните си ключове, уникалността `:668-672` остава); двата сирака изчезват по конструкция; появяват се 4 стълкновения при хотелите, за които ключът и без това не решава. `qa_place_sites.py:165-168` свързва по ключ, пресметнат от същия код от двете страни → прекодирането му е невидимо.
25: 
26: **Присъда: път А.** Ред в `RENAMES` не се съчинява от изпълнител: сирак → СТОП и имената при Петър.
27: 
28: ## 3 · Write-set и дословни съобщения (varna_3d, автор `Claude Executor <executor@local>`)
29: 
30: | # | Файлове | Съобщение |
31: |---|---|---|
32: | 1 | `src/place_identity.py` (`base` `:207,222`; `anchors_of:582`; `rule_key` в `_meta`; докстринг `:26,:176`) + `src/place_addresses.py:377` (второто копие на договора) | `fix(identity): drop the zone from the identity key, anchor on file and name skeleton` |
33: | 2 | `src/qa_identity_rekey.py` + `scratch/granitsi/rekey_negatives.py` и фикстурите | `gates: qa_identity_rekey with negative fixtures for the zone-free key` |
34: | 3 | **`src/qa_identity_refresh.py`** (G9-base: `KEY_PARTS` 3→2; C6 става „при освежаване ключът НЕ се мени"; C7 отпада — режимите „само key" и „само zone" са раздѐлни) + обновените `scratch/granitsi/identity_refresh_negatives.py` | `gates: qa_identity_refresh follows the zone-free key` |
35: | 4 | `src/fire_varna_locations.py` (`CH_DISTRICT_FALLBACK`; двата канала се пишат и в `channels` с `ids`/`raw` — изпълнение на D6) | `feat(m6): write the signed-polygon and district-fallback witnesses into the ledger channels` |
36: | 5 | `src/qa_fire_varna_m6.py` (**константата `LEDGER` НЕ се пипа**; нов `--ledger <път>`; ранг 3/4 за двата канала; полигонът пише само където петте низови канала мълчат; резервата иска районен код) | `gates: qa_fire_varna_m6 judges a ledger given as an explicit input` |
37: | 6 | `src/fire_varna_locations.py` (`_check_pins` сверява `inputs["data/place_identity.json"]`; нов `--accept-identity <sha>`, който пропуска ТАЗИ проверка ПРЕДИ строенето на книгата; `web/varna_buildings_3d.geojson` влиза в `RECORDED_INPUTS` като записан) | `fix(pins): verify the place identity pin on every run, refresh only with --accept-identity` |
38: 
39: Данните остават СТЕЙДЖНАТИ за комитите на Петър (D16/G4). Fire_Varna получава само този документ и реда в доклада.
40: **Записан дълг (датиран 07.09):** `lot1v_v_manifest.py:30` продължава да чете стария леджер по константа — изричен вход при следващия лот; `web/varna_buildings_3d.geojson` се записва, но още не се сверява в `_check_pins`; износителите продължават да пишат стенен часовник (`export_fire_varna_places.py:822`, `export_fire_varna_hotels.py:427`).
41: 
42: ## 4 · Ред на изпълнение
43: 
44: 1. **прекодиране:** генераторът върху ДНЕШНИТЕ износи → `data/place_identity.candidate.json`; `qa_identity_rekey` срещу база = стейджнатия блоб `1141bbc2…` (обектите: само `key`; `_meta`: само `rule_key`);
45: 2. **пиновете (веднага):** `python src/fire_varna_locations.py --inputs --accept-identity <sha от 1>` — без флага стъпка 2 умира в конструктора (`:903`), защото `--inputs` също минава през `load()` (`:1913-1916`);
46: 3. **присвояване:** `fire_varna_locations` → нови износи + датиран леджер;
47: 4. **освежаване на зоната:** генераторът върху НОВИТЕ износи → `qa_identity_refresh` (позволено поле: само `zone`; 0 нови, 0 оттеглени) → пиновете пак (`--inputs --accept-identity <нов sha>`);
48: 5. **речникът:** `build_place_categories.py`;
49: 6. **неподвижна точка:** присвояването се пуска втори път върху освежената самоличност → **леджерът излиза БАЙТ-ЕДНАКЪВ** (`_meta` му няма часовник — проверено), а двата износа са еднакви **след изключване на единствения назован ключ `_meta.generated`**. Сравнението прави гейтът, не окото.
50: 
51: ## 5 · Гейтове и отрицателни фикстури (всяка ТРЯБВА да падне)
52: 
53: - `qa_identity_rekey.py`: 375/375 `place_id` еднакви · 0 нови · 0 оттеглени · всеки нов ключ = `<файл>|skel(име)`(`#N`) · два прогона байт-еднакви. Отрицателни: подменен `place_id`; изтрит обект; ключ със зона; сменена и зона в режим „само ключ".
54: - `qa_identity_refresh.py` (обновен) зелен на стъпка 4; отрицателни: сменен ключ при освежаване; чуждо поле.
55: - `qa_place_sites.py` зелен (0 сираци в двете посоки); червено = СТОП с имената.
56: - `qa_place_zone_aliases.py` = 0 след прегенерирането. Отрицателни по **всичките осем** зони: изтрит ред за нова зона; ръчен псевдоним извън регистъра; застоял `legacy_bundle_sha`.
57: - `qa_fire_varna_m6.py --ledger <датирания>`: **`fails = 0` (изход 1 е забраненият) И изход 3 с ТОЧНО тези 8 поименни `pending_signature` реда** (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата), нито един повече. `--break-me witness` пада. Нови отрицателни: `SIGNED_POLYGON` в свидетеля без кода в `channels`; низов канал предлага код, а полигонът пише; резерва с код извън петте района.
58: - **Гейтовете на прегенерираните артефакти:** `qa_fire_varna_places_export.py`, `qa_fire_varna_export.py` (затвореният набор `_meta` ключове, вече 10 с `quarter_attribution`), `qa_fire_varna_location_isolation.py` — поименно, с командите.
59: - **Пинът:** обърнат hex знак в `inputs` → СТОП; освежаване без `--accept-identity` → СТОП.
60: - **Неподвижната точка:** отрицателна фикстура „подменен ред при еднакъв часовник → червено".
61: - `qa_p8a.py` (G17), `qa_no_cad_ids.py`, `python -m unittest` — зелени.
62: 
63: ## 6 · Комитите на Петър, в този ред
64: 
65: 1. `data/place_identity.json` + `data/fire_varna_location_inputs.json` — `data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned` (файлът носи ДВА товара: 1664/164 реда, от които 375-те координати на Б2-0)
66: 2. `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `data/place_categories.json` — `data: places and hotels with quarter by signed polygon, search dictionary regenerated`
67: 3. новият леджер — `data: p8a quarter assignment ledger 07.09`
68: 
69: ## 7 · STOP
70: 
71: Лотът спира и пита Петър при: сирак след прекодирането (поименно) · неподвижната точка различна извън `_meta.generated` · G17 показва променен написан квартал · зона без регистров запис след прегенерирането · опит да се впише ред в `RENAMES`/`MERGES` · комит на данни от агент · зелен гейт без доказано падаща отрицателна фикстура · `--inputs` без `--accept-identity`.
72: **Не е червен гейт, а грешка на оператора:** `qa_place_identity_coords.py` (G9) съди лот Б2-0 и по конструкция забранява смяна на `key`/`zone` — в този лот НЕ се пуска.
73: 
74: ## 8 · Решенията за Петър
75: 
76: **Р1** Ключът без зоната (път А) вместо пренасяне през леджера (път Б) — **препоръка: А**.
77: **Р2** Нов механизъм `--accept-identity`: пинът на самоличността се сверява при всяко пускане, освежава се само с изричния флаг (изпълнение на D10) — **препоръка: да**.
78: **Р3** `web/varna_buildings_3d.geojson` се ЗАПИСВА в пиновете сега, а сверяването му остава датиран дълг за следващия лот — **препоръка: да** (алтернативата, пълна проверка сега, разширява обхвата в нощта).
79: **Р4** Редът на трите му комита по §6, като самоличността и пинът пътуват в ЕДИН комит с двойното съобщение — **препоръка: да**.
80: 
81: (D6 — свидетелят в `channels` — и смяната на 8-те зони не са решения: те са изпълнение на подписан ADR.)
82: 
83: **§8 допълнение (К26 П3):**
84: 5. **`vinitsa_sever` в речника на зоните** — alias „Виница-север“ → `dobreva` (препоръка: да), или деактивиран, но видим запис. Без решение прегенерирането спира.
85: 
86: 6. **Манифестът на регистъра** (`registry_manifest.json`, скрит изход на генератора: 9 промени на зони — 3 grandfathered + 6 board_queue) — приема ли се и пинва ли се в същия комит със самоличността (препоръка: да, след преглед на деветте реда в доклада на изпълнителя), или се отлага (тогава пинът му остава стар и се записва като дълг).
87: 
88: ## 9 · Оборване — Кими К26 (леща данни/самоличност), приложено като условия на амандамента
89: Присъда: ГОДНО при пет задължителни поправки — всичките влизат тук:
90: - **П1 · Стълкновения при ключ без зоната.** Измерено: местата дават 150 различни скелета от 150; хотелите — четири двойки (admiral, perla, roial, rusalka), всичките с `matched_by: ntr`, разрешими по УИН. Правило за `#N`, дословно: при два и повече живи обекта с еднакъв `<файл>|skel(име)` номерацията се раздава по **възходящ `place_id`** (`#1`, `#2`, …); гейтът изисква двата реда да се различават по `kais_i` или УИН (иначе СТОП); отрицателна фикстура: разменени номера → ✗. `site_id` **не е котва** днес (`place_identity.py:623-659`) — текстът на амандамента се чете с котви `kais_i` + УИН (`ntr`); ако `site_id` трябва да стане котва, това е отделен подписан ред.
91: - **П2 · Речникът на зоните.** `qa_place_zone_aliases` изисква покритие не само на доставените зони, а на **всичките 60 подписани кода** (по `data/quarters_signed.geojson`), **петте района** (за DISTRICT_FALLBACK) и **резервата за Перчемлията** (район Приморски по регистъра) — всеки `display` низ трябва да е в регистъра или в подписана таблица; липсващ → ✗ поименно.
92: - **П3 · `vinitsa_sever` в речника.** Решение на Петър (§8 т. 5): alias „Виница-север“ → `dobreva` (препоръка), или деактивиран запис, който остава видим за `build_place_categories.py`; без едно от двете прегенерирането е обвързано с нерешения регистров ход Р, а 23-те кадастрални адреса „зона Виница-север“ губят зоновата си дума.
93: - **П4 · Гейт срещу мълчалив презапис (G17).** Нов гейт в `qa_p8a`: **всеки ред със сменена зона доказано е имал ПРАЗЕН написан квартал** в основата (или е fallback-ред по Б0 т. 4(i)); броят на сменените зони ≤ 174 (празните); фикстура: сменена зона на ред със записан квартал → ✗. Довод: `old_zone` идва от замразения `legacy_zones` (375/375), тоест зоната на самоличността ≠ написаният квартал — това трябва да е число, не проза.
94: - **П5 · Обявени отклонения в подписа.** Временното неизпълнение на `qa_place_identity_coords.py` (G9 на Б2-0, който по конструкция забранява смяна на key/zone) и отпадането/обръщането на C7 в `qa_identity_refresh.py` (KEY_PARTS 3 → 2) се изреждат **поименно в подписа на Петър** като обявени отклонения.
95: 
96: ## 10 · Оборване — Astra S25 (леща механика), приложено като задължителни условия
97: Присъда на Astra: „негодно за изпълнение в сегашния текст; път А работи“. Измерено от нея с реалната логика на генератора и износителите (в паметта): път А запазва **375/375 `place_id`**, координатите, доказателствата и осемте вече оттеглени записа; прекодирането мени само 375 `key` и `_meta.rule_key`, освежаването само 57 `zone`; двата сирака (III ПМГ „Акад. Методий Попов“, ОУ „П. Р. Славейков“ — едно тяло 39992) се възстановяват; повторните прогони са байт-еднакви; **26 позиции в `objects` се пренареждат** → гейтът на прекодирането сравнява обектите **по `place_id`**, с отделна проверка за уникалност. Условията:
98: - **A1 · Договорът на `--accept-identity` (F1).** Редът е: успешен гейт → **кандидатът се повишава в каноничен** `data/place_identity.json` → едва тогава `fire_varna_locations.py --inputs --accept-identity <sha256 на каноничния файл>`; аргументът се сверява по съществуващото правило (CRLF→LF, SHA-256, `fire_varna_locations.py:1781`) срещу реално прочетения файл; грешен аргумент = СТОП; останалите пинове остават активни. **Три доказателства**: застоял записан пин без флага → СТОП; грешен sha като аргумент → СТОП; правилно приемане → следващият нормален прогон минава. (Днес обърнат hex знак в пина на самоличността **се приема** и `load()` строи 375 реда — това е дупката, която се затваря.)
99: - **A2 · `qa_identity_refresh.py`**: `KEY_PARTS` 3 → 2, C6 = „ключът НЕ се мени при освежаване“, C7 отпада; основата на освежаването е **приетата прекодирана самоличност**, `ALLOWED_FIELDS = {"zone"}`, задължителен втори кандидат за детерминизъм.
100: - **A3 · Неподвижната точка (F2), дословно:** JSON parse → изтриване само на `_meta.generated` → `json.dumps(doc, ensure_ascii=False, indent=1) + "\n"` → UTF-8 → сравнение на байтове; масивите пазят реда си; леджерът се сравнява директно без изключения. Измерено: вторият леджер след освежаването е байт-еднакъв с първия и с паркирания (958 449 B, `fba94bf8…`); двата износа при различни часовници дават еднакъв нормализиран резултат. Компараторът получава име и CLI в write-set-а (`src/qa_fixed_point.py --a <път> --b <път> [--ignore _meta.generated]`).
101: - **A4 · Редът на прегенериране (блокер):** `build_place_categories.py` се пуска **СЛЕД последния износ** (иначе `legacy_bundle_sha`, който хешира целите байтове с часовника, се обезсилва от самата стъпка 6), после гейтът на alias-ите. Осемте нови зони съществуват в регистъра и се извеждат автоматично.
102: - **A5 · Скритият изход на генератора (F3):** генераторът винаги строи и пише `registry_manifest.json`; при освежаването са измерени **9 допълнителни промени на зони в манифеста (3 `grandfathered` + 6 `board_queue`)**. Всеки кандидат-прогон задава `--manifest-out` към `scratch/granitsi/`; дали полученият манифест се приема и пинва е **решение на Петър (§8 т. 6)**; приетият манифест влиза в същия комит като самоличността и пина.
103: - **A6 · M6 и D6-формата:** при успешно присвояване писачът на леджера добавя `channels.SIGNED_POLYGON = {"ids": [winner], "raw": [safe_witness]}`, при резерва — `DISTRICT_FALLBACK` с районния код; петте изборни `CHANNELS` остават пет; приемането на M6 сравнява **точните осем `place_id`** на pending-редовете (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата), не броя; отделна проверка на района преди общата квартална за fallback-редове и **положителна fallback-фикстура** (днес такива редове са нула).
104: - **A7 · Изпълнимият ред:** замразена основа → два кандидата за прекодиране + гейт → повишаване + пинове (`--accept-identity`) → двата износителя и `fire_varna_locations.py --ledger` → два кандидата за освежаване + гейт → повишаване + пинове → повторни износи/леджер + гейтът на неподвижната точка → категории → всички финални гейтове (alias-и, M6 с точното множество, `qa_p8a` вкл. П4, G17, пълният набор). Всеки неочакван неуспех спира. **Комитите на Петър:** (1) окончателната самоличност **заедно с пиновете (и приетия манифест) в един комит**, чието съобщение назовава и трите товара (координати от Б0 т. 11, прекодиране без зоната, 57 освежени зони); (2) двата износа + `place_categories.json`; (3) датираният леджер.
105: - **Съгласуване с К26 П1:** правилото за `#N` при стълкновение е **днешното** на генератора — по координатен ранг (`place_identity.py:225`), детерминирано и измерено; записва се дословно, а отрицателната фикстура „разменени номера“ от П1 важи както е.
106: 
107: ## 11 · Статус
108: **ПОДПИСАН от Петър (07.09.2026): „подписвам амендамент 3 с решения 1-6 по препоръките“.** Подписаното тяло: ревизия 2, sha256 на blob-а в комит 4e9606c = `cf919f178462dd832581b7abf8aba1dae2ab6bd326f2f90919f659d5a7ab2ebc`. Обявените отклонения (G9 на Б2-0 не се пуска в този лот; C7 на qa_identity_refresh отпада) са покрити от подписа.
109: 
110: Преди подписа: Минал през: два вътрешни Opus лещи (чернова → синтез), Кими К26 (ГОДНО с П1–П5, вградени в §9), Astra S25 (условията A1–A7, вградени в §10). Изпълнението (повторение на Б2) тръгва след подписа, с изпълнител и одитор на всеки ход, без пуш, с локален преглед на картата от Петър преди каквато и да е доставка.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=0; Get-Content -Encoding utf8 -LiteralPath '"'C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md' | ForEach-Object { "'$n++; '"'{0}: {1}' -f "'$n,$_ }; git -C C:/git/varna_3d --no-optional-locks status --short --branch; git -C C:/git/varna_3d rev-parse HEAD; git -C C:/git/varna_3d diff --cached --stat; git -C C:/git/varna_3d diff --stat' in C:\git
 succeeded in 104ms:
6: - **Изворът на границите е решен от Петър:** човешките полигони от Уикимапия („точно това е границата“ за Кайсиева; „прегледах районите — нека ползваме тях“). Стълбата на изворите v3 и всичко около нея е в `docs/plans/ПЛАН_ЛОТ_Границите_v2_амандамент_2_06.09.md` (ревизия 2б; минал Кими К15–К21 и Astra S14–S20; **неподписан**).
7: - **Замразено тяло:** обходът на Уикимапия (667 проби, 11 303 места) → извод v2 288 полигона, sha256 `b53a3322…` (`scratch/boundary_gallery/frozen_2026-09-06/`, игнорирана папка; отпечатъците и броевете в `scratch/places_search/wikimapia_frozen_measure_06.09.md`).
8: - **Решенията на Петър:** `scratch/places_search/granitsi_decisions_3_2026-09-06_proba.json` (проба, без геометрия): **61 граници** — 32 квартала/комплекса, 26 местности/с.о., 3 зони/паркове/курорти; Младост 2 по четирите му улици (оси от OSM); Бриз = големият полигон (измерен 0 m до четирите страни, които описа); Акчелар = уикимапийската „Белица“ (94 % от кадастралната обвивка); Евксиноград = 5729429 (EN „Euxinograd“ = BG „Траката - разширение“). Без граница: 6 отложени, Ваялар (второ име на Средна Трака), 16 без решение.
9: - **Ефект върху 375-те места** (координати от пробата, правило „най-малкият съдържащ полигон, ръб 100 m“): получават квартал 71 · съгласие 186 · спор 7 · ръб 62 · извън 49.
10: - **Пробите за гледане** (локален сървър `granitsi-preview`, порт 8792, игнорирана папка `scratch/boundary_gallery/granitsi_preview_05.09/`): `wikimapia.html` (събраното), `board.html` (бордът: да/не/отложи, износ JSON), `result.html` (картата на резултата).
11: 
12: ## 2 · Защо ни бяха кварталите (замисълът от `ПРОМПТ_нова_тема_Границите.md` и `ПЛАН_ЛОТ_Границите.md`)
13: Търсачката на Fire_Varna намира места по име и адрес; кварталът е начинът, по който хората (обаждащият се, колегата) назовават мястото. Мярката от 05.09: **174 от 375 места без квартал; 14 от 32 квартала без нито едно място; търсенето пада на съюзи/точки и на 7 думи, които са и имена; „Цветен квартал“ не беше в регистъра.** Целта: всяко място да има квартал по един и същ, проверим начин, и търсене „училище Възраждане 3“ / „Кайсиева градина“ да връща всичко ВЪТРЕ в границата, не само местата с този квартал в адреса. Границата е човешкото понятие, превърнато във факт, който машината проверява.
14: 
15: ## 3 · Как продължаваме (редът от амандамент №2, ревизия 2б)
16: 1. **Gate 1** — Петър подписва амандамент №2 (8 решения; повечето вече взети на практика: стълбата v3, лиценз на ниво Feature, обхватът = регистърът с местностите, атрибуцията по ToS §1.G). Открито: текстът на реда „квартал по Wikimapia.org“ в картата на мястото; реален API ключ (негов акт); редът на М2-3.
17: 2. **Г2-б** — Петър комитва сам файла с решенията (решения 3, след преглед) като подписани решения; бордът-проба е свършил работата на борда.
18: 3. **Г2-в** — изпълнител (Opus) сглобява `varna_3d/data/quarters_signed.geojson` с провенанс (wm_id, отпечатъци, потвърждение, лиценз на ниво Feature), гейтове G25–G30; одитор проверява.
19: 4. **Р** — регистърът: Ваялар → alias на Средна Трака; Евксиноград/Траката конфликтът; Цветен квартал; 16-те без решение.
20: 5. **P8-а** — присвояване: 71-те празни места получават квартал, записаните не се променят (G17), ръбът чака, споровете се показват.
21: 6. **F13** — търсене по квартал + редът за атрибуция; регресионните фикстури (S17) минават.
22: 7. **Gate 2 + пуш** (Петър).
23: Паркирано зад Границите: Ред (Фаза E), Ф0-б, амандамент №10 (A.2-11).
24: 
25: 
26: ## 4 · Нощната смяна 06→07.09 — резултат (добавено сутринта на 07.09 по часовника на машината)
27: - Планът `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md` (v2, подписан от Петър) е изпълнен от Opus изпълнители с одитор на всеки ход: **част А 7/7 зелени**, **Б1 зелен** (`varna_3d/data/quarters_signed.geojson`, 61 граници, СТЕЙДЖНАТ за комита на Петър, sha `3f423898…`), **Б2-0 червен на G9** (основата на самоличността от 04.09 се е разместила → отделно освежаване сутринта), Б2/Б3 не са тръгвали. Докладът: `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (§6 = прегледът от три ъгъла: архитект, Кими К23, Astra S22). Първата стъпка на Петър е §6.4 на доклада.
28: 
29: - **Решения 4 (07.09, Петър, след нощта):** площта „Виница - север“ в Уикимапия е част от Добрева чешма → `dobreva` = обединението на двата полигона (1,43 km²), `vinitsa_sever` = **изключен** (регистърът го деактивира, ход Р). Файл: `scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json`; обединената геометрия в `granitsi_preview_05.09/unions_2026-09-07.geojson`. Следствие за сутринта: Б1 се пресглобява от решения 4 (строителят трябва да поддържа `wikimapia_union` с два свидетеля); нито едно от 375-те места не е в засегнатата площ. Картата на резултата вече го показва (60 граници).
30: 
31: - **Решение 8 (07.09, Петър):** в картончето на мястото НЯМА ред за извора на квартала („квартал по Wikimapia.org · обектът · потвърдено от Петър“ — „това можеш да го махнеш“). Кварталът се показва само в реда „вид · квартал · район“. Споменаването на Wikimapia отива в дребния надпис в долния край на картата (Leaflet attribution), до „© OpenStreetMap contributors“. Следствие за Б3: G27(б) се изпълнява чрез надписа на картата, не чрез ред в картончето; `quarter_attribution` остава в `_meta` (машинен запис), UI низ в картончето няма.
32: 
33: - **Решение 9 (07.09, Петър):** „Кочмар и Възраждане 4 не са във Владиславово“ → районът на двата квартал-полигона е **Младост**, както казва официалната граница на АГКК (AU5 10135-03; представителните точки са 782 m и 509 m навътре в Младост). Причина за грешката: районът на кварталите в артефакта се извежда от НАШИЯ слой с районите по представителна точка, а той се разминава с официалната граница около бул. „Трети март“. Местата не са засегнати (district.code на местата е 375/375 с АГКК). Следствие: (а) двата спора в `_meta.district_witness_disputes` получават `resolution: "petar_agkk"` и `district = mladost`, `district_src = "agkk_au5_confirmed_by_petar"`; (б) мярка сутринта: нашият слой с районите срещу AU5 по цялата граница Владиславово/Младост (и петте граници) — къде още се разминават; (в) сградната мярка Н4 „само район“ да ползва AU5, не нашия слой.
34: 
35: - **Мярка 07.09 (архитект): нашият слой с районите (m6000_private/number_viewer/quarters_layer.geojson, authority OSM) срещу официалните пет района на АГКК (AU5):** Приморски IoU 0,995 (0,24 km² разминаване) · Аспарухово 0,960 (2,74 km²: петно 137 ha „наш излишък“ при 43,1815 N 27,9165 E, 82 ha „липсва при нас“ при 43,1968 N 27,9001 E — зоната на пристанището/езерото между Аспарухово и Одесос) · Одесос 0,799 (1,36 km²) · **Владиславово 0,790 (4,54 km²: 404 ha наш излишък при 43,2463 N 27,8804 E — точно зоната на Кочмар и Възраждане 4, която АГКК дава на Младост)** · **Младост 0,692 (4,17 km²)**. Изводът: OSM-слоят с районите не е годен за районна граница; официалният е AU5. Кочмар и Възраждане 4: наш слой → Владиславово, АГКК → Младост (решение 9 на Петър съвпада с АГКК). **Предложение за решение 10:** районът на квартал-полигоните да се извежда от AU5 (официално, с подписан crosswalk 10135-0N → словесен код), а OSM-слоят с районите да отпадне като извор за район навсякъде (3D картата: дълг).
36: 
37: - **Мярка 07.09 (архитект) за решение 10:** представителните точки на 60-те граници срещу AU5 и срещу нашия OSM слой: **57 съгласни, точно 2 флипа (Кочмар, Възраждане 4 — вече решени по решение 9), 1 извън всичките пет района на АГКК: с.о. Перчемлията** (не е и в нашия слой). Следствие: гейтът на решение 10 „60/60 в AU5“ иска поименен, подписан резерв за Перчемлията (район Приморски по регистъра/адресите, `district_src: "registry_declared"`), иначе е червен. Други флипове край пристанището/Одесос НЯМА при днешните полигони.
38: 
39: - **Б1 ЗАТВОРЕН (07.09):** Петър комитна `varna_3d/data/quarters_signed.geojson` — **6486b48 (Petar1984)**, „data: signed quarter boundaries v1 (decisions 4, sha 74f09d505e2b)“, с подписното изречение в тялото (решения 4 блоб 74f09d50…, решение 9 d494d4d2…, AU5 crosswalk, артефакт c1551d24…, 60 граници, 301 917 B). Предхождащи изпълнителски комити: 63d077d, 8c262e9, 6dde0a5, 7fb0e92, e2da307 (varna_3d); 3d747d3, e6c706d (Fire_Varna). Прегледи: Кими К24/К25, Astra S23/S24 (записите в scratch/places_search/). Дребни дългове: `ours` в решен спор не се сверява (false-pass), семантиката на `counts.features_with_our_district`, закованият sha на resolutions; `vinitsa_sever` нормализаторен път в регистъра; решение 10 (район от AU5 навсякъде; Перчемлията извън AU5 → подписан резерв) чака Петър.
40: 
41: ## 5 · Б2 (07.09, Workflow granitsi-b2) — резултат
42: - **Б2-0а (освежаване на основата на самоличностите): ЗЕЛЕН, одит ГОДНО** — 77 реда (72 хотела + 5 места) с променени `zone`/`key`, произходът доказан 1:1 срещу комит e613089 от 05.09; 0 нови/изчезнали place_id; гейт `src/qa_identity_refresh.py` (varna_3d 3de6661). Заварената червена мярка `qa_place_sites.py` става зелена.
43: - **Б2-0 (координати от кадастралните тела, Б0 т. 11): ЗЕЛЕН, одит ГОДНО** — 375/375 с координата, 0 без; G9 срещу освежената основа само в четирите координатни ключа; генераторът + гейт (varna_3d 5c6fdd0). `data/place_identity.json` е **СТЕЙДЖНАТ** (sha `1141bbc2…`) за комита на Петър — но виж дълга за пина по-долу.
44: - **Б2 (присвояване P8-а): изпълнител зелен, одитори НЕГОДНО (2 блокера, 2 major)** — числата съвпадат с нощната мярка (written 201; assigned_polygon 65; edge 63; pin_outside_all 41; disputed_overlap 5; SIGNED_POLYGON пише 57: 42 места + 15 хотела; DISTRICT_FALLBACK 0), леджерът на конфликтите е произведен (286/33/49/7). **Блокер 1:** ключът на самоличността е `file|skeleton|zone` (`src/place_identity.py:207,222`) — присвояването сменя `zone` на 57 реда и **57 места губят place_id**; генераторът пада (2 реда „оттеглени без решение“). Това е дефект на дизайна на D10 (зоната е част от ключа), открит от гейта, не от кода на лота. **Major 2:** `qa_place_zone_aliases.py` 0 → 1: три доставени зони липсват в речника на търсенето (Гръцката махала, Долна Трака, Колхозен пазар), `place_categories.json` не е прегенериран, `legacy_bundle_sha` сочи стария износ. **Major 3:** `qa_fire_varna_m6.py` чете стария леджер (write-set-ът „QA/M6“ не е изпълнен); новият леджер не спазва буквата на D6 за свидетеля. Комитите с код (da77ff2, 0ecd814) остават — с данните на HEAD всички гейтове са зелени (проверено от архитекта).
45: - **Паркиране (архитект):** четирите изхода са копирани в `scratchpad/b2_outputs_2026-09-07/` (places 89e60d2e…, hotels b4f1f0bb…, inputs c06b93ab…, леджер fba94bf8…), махнати от индекса и работното дърво (HEAD износите върнати: 329310f5…, 46a44ce8…); стейджнат остава само `data/place_identity.json`. Гейтове след паркирането: `qa_place_zone_aliases` 0, пълният набор OK.
46: - **Дълг за пина:** `data/fire_varna_location_inputs.json` пинва старата самоличност (e8b4c836…), а стейджнатата е 1141bbc2… — никой гейт не го лови (`_check_pins` сверява само NTR/M6). Пинът се пренаписва в Б2; до тогава комитът на самоличността носи застоял пин. Препоръка: самоличността остава стейджната до Б2-повторението.
47: - **Следва:** амандамент №3 (малък): ключ на самоличността без зоната (или ре-закотвяне при смяна на зона), прегенериране на `place_categories.json` и речника на зоните (alias-и за трите нови имена), `qa_fire_varna_m6.py` към новия леджер, D6-формата на свидетеля; оборване (Opus → Кими/Astra) → подпис → Б2 повторение.
48: 
49: - **Находка (одитор Б2-R1-fix, 07.09):** проследеният `varna_3d/scratch/place_bodies/qa_place_bodies.md` (заварен мръсен преди нощта, пинат sha 51b0f4d9…) е бил ПРЕЗАПИСАН от прекратения първи прогон на Б2 (07.09 02:25; сега sha 2633e165…, 153 разменени реда със зоните на онзи прогон). Файлът е генериран QA-отчет (колона „зона“); предишното мръсно съдържание няма копие никъде. Архитектът НЕ го пипа: след успешния Б2 отчетът се прегенерира от актуалните данни и разликата спрямо HEAD ще е легитимна; решението (прегенерирай / върни HEAD) е на Петър при Gate 2.
50: 
51: ## 6 · Б2 ПОВТОРЕНИЕ по амандамент №3 — ЗЕЛЕНО (07.09, Workflow granitsi-b2-rerun-3)
52: - **Б2-R1** (прекодиране): varna_3d a28edc2 (ключ без зоната), 8a60972, 7bac5e5, bb09535 (`--accept-identity`), 4bdcc7c (харнеси, utf-8), 36e8513 (замразената основа като фикстура `tests/fixtures/identity_rekey_base_2026-09-07.json`, доказано от чисто дърво). 375/375 place_id непроменени.
53: - **Б2-R2** (присвояване): 679451d (свидетели в леджера, A6), 2624218 (M6 с изричен леджер), 822656d (неподвижна точка, A3), bd00c2c (подписан alias override, решение 5), 0c1ed71 (речник: 60 кода + 5 района + Перчемлията, П2), 26da605 (П4 в qa_p8a). Архитектът: `.gitignore` изключение за `data/zone_alias_overrides.json` (major на общия одит).
54: - **Числата:** таблица 201 written / 41 pin_outside_all / 63 edge_pending / 5 disputed_overlap / 65 assigned_polygon / 0 assigned_district = 375; SIGNED_POLYGON пише 57 (всичките върху празни записани квартали, П4); G17 201/201; неподвижна точка: места, хотели, леджер байт-еднакви; M6 fails 0, exit 3 с точно осемте pending; речник: 32 доставени зони, 28 съвпадат, 4 „unmatched“ (за преглед), override „Виница-север“ приложен 0 пъти (няма доставена такава зона — очаквано).
55: - **СТЕЙДЖНАТИ за Петър (7 файла):** place_identity 4819ab3e… · fire_varna_location_inputs c7450ded… · fire_varna_places 3dffc264… · fire_varna_hotels eb8fa85c… · place_categories 9064705a… · registry_manifest bb04640e… (решение 6: 9 реда със сменена зонова дума) · леджер lot1v_locations_375_p8a_07.09 5ec64c68…. Одити: R1-fixture ГОДНО, R2 ГОДНО, общ ГОДНО (2 major: .gitignore — поправен; манифестът не е байт-еднакъв — очаквано по решение 6, 9 реда).
56: - **Следва:** Кими/Astra преглед → трите комита на Петър (§6 на амандамента) → Б3 → локален преглед → пуш.
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
## rezhimi...origin/rezhimi [ahead 70]
M  data/fire_varna_hotels.json
M  data/fire_varna_location_inputs.json
M  data/fire_varna_places.json
M  data/place_categories.json
M  data/place_identity.json
M  data/registry_manifest.json
 M scratch/place_bodies/qa_place_bodies.md
A  scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json
?? docs/sessions/ПРОМПТ_20.08.md
?? scratch/refactor/_addr/_measure_pal13.py
?? scratch/refactor/_addr/_measure_tu_campus.py
?? scratch/refactor/_addr/f0b_join_375.json
?? scratch/refactor/_addr/f0b_join_375_pass2.json
?? scratch/refactor/_addr/kimi_атака_имена_бунгала.txt
?? scratch/refactor/_addr/kimi_атака_планове.txt
?? scratch/refactor/_addr/kimi_атака_смяна2.txt
?? scratch/refactor/_addr/osm_poi_varna.md
?? scratch/refactor/_addr/post_codes_all_2018.pdf
?? scratch/refactor/_addr/post_codes_varna_2018.json
?? scratch/refactor/_addr/БОРД_противоречия.md
?? scratch/refactor/_addr/БОРД_част_от_сграда.md
?? scratch/refactor/_addr/МЯРКА_курорти_повторно.md
?? scratch/refactor/_addr/МЯРКА_хотели.md
?? scratch/refactor/_addr/ОТЧЕТ_A1_05.09.md
?? scratch/refactor/_addr/ОТЧЕТ_P7_05.09.md
?? scratch/refactor/_addr/ОТЧЕТ_P7e_05.09.md
?? scratch/refactor/_addr/ПОДГОТОВКА_адреси.md
?? scratch/refactor/_addr/РАЗСЛЕДВАНЕ_адрес.md
?? scratch/refactor/_addr/СВЕРКА_живата_карта.md
?? scratch/refactor/_addr/Т7_недовършено_19.08.patch
?? scratch/refactor/_pubbldg/func/extras_log.txt
?? scratch/refactor/_pubbldg/func/run_log.txt
?? scratch/refactor/_pubbldg/join/check_log.txt
?? scratch/refactor/_pubbldg/join/extras_log.txt
?? scratch/refactor/_pubbldg/join/run_log.txt
?? scratch/refactor/_pubbldg/join/sample.json
?? scratch/refactor/_pubbldg/plan/kimi_plan_stderr.log
?? scratch/refactor/_pubbldg/plan/sol_plan_stderr.log
?? scratch/refactor/_pubbldg/plots/plots_by_class.json
?? scratch/refactor/_pubbldg/plots/plots_pooled.json
?? scratch/refactor/_pubbldg/plots/run_log.txt
?? scratch/refactor/_pubbldg/sources/check_log.txt
?? scratch/refactor/_pubbldg/sources/measure_osm_log.txt
?? scratch/refactor/_pubbldg/sources/measure_outside_log.txt
?? scratch/refactor/_pubbldg/sources/measure_sources_log.txt
?? scratch/refactor/_pubbldg/sources/name_channels.json
?? scratch/refactor/_pubbldg/sources/osm_named_features.json
?? scratch/refactor/_pubbldg/verify/kimi_stderr.log
?? scratch/refactor/_pubbldg/verify/sol_stderr.log
1217dc494ebd1ce16f1cbd90e73f202dec206b1e
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
 data/fire_varna_hotels.json                        |   169 +-
 data/fire_varna_location_inputs.json               |    32 +-
 data/fire_varna_places.json                        |   427 +-
 data/place_categories.json                         |   320 +-
 data/place_identity.json                           |  2808 +-
 data/registry_manifest.json                        |    18 +-
 .../_addr/lot1v_locations_375_p8a_07.09.json       | 34669 +++++++++++++++++++
 7 files changed, 37555 insertions(+), 888 deletions(-)
 scratch/place_bodies/qa_place_bodies.md | 306 ++++++++++++++++----------------
 1 file changed, 153 insertions(+), 153 deletions(-)

codex
Прилагам skill `engineering:code-review` с фокус MECHANICS. Базовото състояние съвпада със заявеното: HEAD е `1217dc4`, в index има седемте payload файла, а `qa_place_bodies.md` е отделна unstaged промяна.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=0; Get-Content -Encoding utf8 -LiteralPath '"'C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md' | Select-Object -First 150 | ForEach-Object { "'$n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git
 succeeded in 17ms:
4: 
5: **Клас: 🔴 Архитектурен.** Спуснати спусъци: променя подписан договор за данните (ключът на самоличността) · мутира каноничното `data/place_identity.json` · пипа данни, които пътуват към Fire_Varna · сменя и добавя гейтове. **Топология: Вариант А.** **Статус: ЗА ПОДПИС (Gate 1). НЕПОДПИСАН.**
6: **Не отваря нищо ново:** Б3/търсенето, регистърът, `quarters_signed.geojson`, написаните 201 квартала и живата карта не се пипат. Нула пуш.
7: 
8: ## 1 · Мярката (read-only, 07.09)
9: 
10: 1. **Ключът и котвите.** `src/place_identity.py:207,222`: `base = "<файл>|skel(име)|zone"`. `anchors_of()` (`:569-583`) дава четири нива: `reg` · `ntr` · `kais` · и чак после `key`, в който седи зоната (`:582`). Стара самоличност, която нищо не намира, е „оттеглена БЕЗ решение" и СПИРА билда (`:813-816`). `site_id` НЕ е котва (`:623-659`).
11: 2. **Кой виси на крехкия ключ.** `scratch/granitsi/aud_regen.log:3`: ntr 192 · kais 144 · reg 35 · **key 4**. 371/375 не зависят от зоната. Четирите са две двойки върху едно кадастрално тяло: ДГ№52 + Диспансерът (`kais_i` 1523) и III ПМГ + ОУ „П. Р. Славейков" (`kais_i` 39992).
12: 3. **Кои два реда падат.** В спрения износ втората двойка минава `район Одесос → кв. Тракия` (`SIGNED_POLYGON`); ключовете се менят, `kais` е двусмислена, `reg`/`ntr` ги няма → два сирака, генераторът пада. 55 от 57-те смени на зона се спасяват от reg/ntr/kais.
13: 4. **Присвояването вече носи `place_id`.** `fire_varna_locations.py:967-979` свързва по УИН, после по `(файл, skel(име))` — „by evidence, never by zone". Леджерът е `{_meta, rows, quarantine}`, като **`rows` е СПИСЪК от 375 реда**, всеки с `place_id`/`old_zone`/`new_zone`; `old_zone` идва от ЗАМРАЗЕНИЯ блок `legacy_zones` (`:886-893`, покрива 375/375), не от зоната в самоличността. Речник по `place_id` е само `book.rows` в паметта (`:1937`).
14: 5. **Износът не може да носи id.** `place_identity.py:38-40`: публичните `data/fire_varna_*.json` не носят id — подписан договор.
15: 6. **Стълкновения без зоната.** Мерено: местата дават 150 различни скелета от 150 (нула стълкновения); хотелите — четири двойки (`admiral`, `perla`, `roial`, `rusalka`), и осемте реда `matched_by: "ntr"`, решавани по УИН.
16: 7. **Речникът на търсенето.** `qa_place_zone_aliases.py` пада на проверка (а) (`:213-217`). Числото в СЪСТОЯНИЕ §5 („три зони") е ОТРЯЗАН текст (`lost[:3]`): доставените непознати зони са **ОСЕМ** — Гръцката махала, Долна Трака, Колхозен пазар, Център, кв. Левски, кв. Св. Иван Рилски, кв. Тракия, кв. Христо Ботев. И осемте са ДОСЛОВНИ `display` низове в `quarter_registry.json`, а `build_place_categories.py:300-329` строи псевдонимите САМО от регистъра → лекът е прегенериране, нула ръчни низове.
17: 8. **М6 и формата на свидетеля (D6).** `CH_SIGNED_POLYGON` не е в `CHANNELS` (`:173-180`), затова редът носи `witness.quarter = ["SIGNED_POLYGON"]` без код в `channels` → проверка (б) (`qa_fire_varna_m6.py:304-308`) обявява 57 нарушители. Мерено днес: `qa_fire_varna_m6.py` връща **изход 3** („ЧАКА ПОДПИС: 8 реда", `:367`), не 0; спреният леджер носи същите 8 (`_meta.counts.pending_signature = 8`).
18: 9. **Пиновете.** `_check_pins` (`:922-949`) сверява НТР, двете таблици, `quarters_signed` и базата на леджера — но НЕ блока `inputs` (`RECORDED_INPUTS :108`). Затова `data/fire_varna_location_inputs.json:51` пинва `e8b4c836…`, а стейджнатата самоличност е `1141bbc2…`. Отделно `web/varna_buildings_3d.geojson` — ИЗВОРЪТ на координатите (`place_identity.py:90`) — изобщо не е в `RECORDED_INPUTS`, макар D10 (`010:56`) да го иска.
19: 
20: ## 2 · Двата пътя и присъдата
21: 
22: **Път Б** (ключът остава; `place_id` се носи през леджера) е механично възможен, но (i) износът не може да носи id, значи единственият носител е леджерът; (ii) зоната остава В КЛЮЧА, значи всяко чисто `python src/place_identity.py` (командата от собствения докстринг `:60`) връща същите два сирака. Ред на действията не е гейт.
23: 
24: **Път А** (`<файл>|skel(име)`): измерено — **375/375 `place_id` остават същите**; сменя се само полето `key` на 375-те живи обекта (оттеглените пазят записаните си ключове, уникалността `:668-672` остава); двата сирака изчезват по конструкция; появяват се 4 стълкновения при хотелите, за които ключът и без това не решава. `qa_place_sites.py:165-168` свързва по ключ, пресметнат от същия код от двете страни → прекодирането му е невидимо.
25: 
26: **Присъда: път А.** Ред в `RENAMES` не се съчинява от изпълнител: сирак → СТОП и имената при Петър.
27: 
28: ## 3 · Write-set и дословни съобщения (varna_3d, автор `Claude Executor <executor@local>`)
29: 
30: | # | Файлове | Съобщение |
31: |---|---|---|
32: | 1 | `src/place_identity.py` (`base` `:207,222`; `anchors_of:582`; `rule_key` в `_meta`; докстринг `:26,:176`) + `src/place_addresses.py:377` (второто копие на договора) | `fix(identity): drop the zone from the identity key, anchor on file and name skeleton` |
33: | 2 | `src/qa_identity_rekey.py` + `scratch/granitsi/rekey_negatives.py` и фикстурите | `gates: qa_identity_rekey with negative fixtures for the zone-free key` |
34: | 3 | **`src/qa_identity_refresh.py`** (G9-base: `KEY_PARTS` 3→2; C6 става „при освежаване ключът НЕ се мени"; C7 отпада — режимите „само key" и „само zone" са раздѐлни) + обновените `scratch/granitsi/identity_refresh_negatives.py` | `gates: qa_identity_refresh follows the zone-free key` |
35: | 4 | `src/fire_varna_locations.py` (`CH_DISTRICT_FALLBACK`; двата канала се пишат и в `channels` с `ids`/`raw` — изпълнение на D6) | `feat(m6): write the signed-polygon and district-fallback witnesses into the ledger channels` |
36: | 5 | `src/qa_fire_varna_m6.py` (**константата `LEDGER` НЕ се пипа**; нов `--ledger <път>`; ранг 3/4 за двата канала; полигонът пише само където петте низови канала мълчат; резервата иска районен код) | `gates: qa_fire_varna_m6 judges a ledger given as an explicit input` |
37: | 6 | `src/fire_varna_locations.py` (`_check_pins` сверява `inputs["data/place_identity.json"]`; нов `--accept-identity <sha>`, който пропуска ТАЗИ проверка ПРЕДИ строенето на книгата; `web/varna_buildings_3d.geojson` влиза в `RECORDED_INPUTS` като записан) | `fix(pins): verify the place identity pin on every run, refresh only with --accept-identity` |
38: 
39: Данните остават СТЕЙДЖНАТИ за комитите на Петър (D16/G4). Fire_Varna получава само този документ и реда в доклада.
40: **Записан дълг (датиран 07.09):** `lot1v_v_manifest.py:30` продължава да чете стария леджер по константа — изричен вход при следващия лот; `web/varna_buildings_3d.geojson` се записва, но още не се сверява в `_check_pins`; износителите продължават да пишат стенен часовник (`export_fire_varna_places.py:822`, `export_fire_varna_hotels.py:427`).
41: 
42: ## 4 · Ред на изпълнение
43: 
44: 1. **прекодиране:** генераторът върху ДНЕШНИТЕ износи → `data/place_identity.candidate.json`; `qa_identity_rekey` срещу база = стейджнатия блоб `1141bbc2…` (обектите: само `key`; `_meta`: само `rule_key`);
45: 2. **пиновете (веднага):** `python src/fire_varna_locations.py --inputs --accept-identity <sha от 1>` — без флага стъпка 2 умира в конструктора (`:903`), защото `--inputs` също минава през `load()` (`:1913-1916`);
46: 3. **присвояване:** `fire_varna_locations` → нови износи + датиран леджер;
47: 4. **освежаване на зоната:** генераторът върху НОВИТЕ износи → `qa_identity_refresh` (позволено поле: само `zone`; 0 нови, 0 оттеглени) → пиновете пак (`--inputs --accept-identity <нов sha>`);
48: 5. **речникът:** `build_place_categories.py`;
49: 6. **неподвижна точка:** присвояването се пуска втори път върху освежената самоличност → **леджерът излиза БАЙТ-ЕДНАКЪВ** (`_meta` му няма часовник — проверено), а двата износа са еднакви **след изключване на единствения назован ключ `_meta.generated`**. Сравнението прави гейтът, не окото.
50: 
51: ## 5 · Гейтове и отрицателни фикстури (всяка ТРЯБВА да падне)
52: 
53: - `qa_identity_rekey.py`: 375/375 `place_id` еднакви · 0 нови · 0 оттеглени · всеки нов ключ = `<файл>|skel(име)`(`#N`) · два прогона байт-еднакви. Отрицателни: подменен `place_id`; изтрит обект; ключ със зона; сменена и зона в режим „само ключ".
54: - `qa_identity_refresh.py` (обновен) зелен на стъпка 4; отрицателни: сменен ключ при освежаване; чуждо поле.
55: - `qa_place_sites.py` зелен (0 сираци в двете посоки); червено = СТОП с имената.
56: - `qa_place_zone_aliases.py` = 0 след прегенерирането. Отрицателни по **всичките осем** зони: изтрит ред за нова зона; ръчен псевдоним извън регистъра; застоял `legacy_bundle_sha`.
57: - `qa_fire_varna_m6.py --ledger <датирания>`: **`fails = 0` (изход 1 е забраненият) И изход 3 с ТОЧНО тези 8 поименни `pending_signature` реда** (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата), нито един повече. `--break-me witness` пада. Нови отрицателни: `SIGNED_POLYGON` в свидетеля без кода в `channels`; низов канал предлага код, а полигонът пише; резерва с код извън петте района.
58: - **Гейтовете на прегенерираните артефакти:** `qa_fire_varna_places_export.py`, `qa_fire_varna_export.py` (затвореният набор `_meta` ключове, вече 10 с `quarter_attribution`), `qa_fire_varna_location_isolation.py` — поименно, с командите.
59: - **Пинът:** обърнат hex знак в `inputs` → СТОП; освежаване без `--accept-identity` → СТОП.
60: - **Неподвижната точка:** отрицателна фикстура „подменен ред при еднакъв часовник → червено".
61: - `qa_p8a.py` (G17), `qa_no_cad_ids.py`, `python -m unittest` — зелени.
62: 
63: ## 6 · Комитите на Петър, в този ред
64: 
65: 1. `data/place_identity.json` + `data/fire_varna_location_inputs.json` — `data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned` (файлът носи ДВА товара: 1664/164 реда, от които 375-те координати на Б2-0)
66: 2. `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `data/place_categories.json` — `data: places and hotels with quarter by signed polygon, search dictionary regenerated`
67: 3. новият леджер — `data: p8a quarter assignment ledger 07.09`
68: 
69: ## 7 · STOP
70: 
71: Лотът спира и пита Петър при: сирак след прекодирането (поименно) · неподвижната точка различна извън `_meta.generated` · G17 показва променен написан квартал · зона без регистров запис след прегенерирането · опит да се впише ред в `RENAMES`/`MERGES` · комит на данни от агент · зелен гейт без доказано падаща отрицателна фикстура · `--inputs` без `--accept-identity`.
72: **Не е червен гейт, а грешка на оператора:** `qa_place_identity_coords.py` (G9) съди лот Б2-0 и по конструкция забранява смяна на `key`/`zone` — в този лот НЕ се пуска.
73: 
74: ## 8 · Решенията за Петър
75: 
76: **Р1** Ключът без зоната (път А) вместо пренасяне през леджера (път Б) — **препоръка: А**.
77: **Р2** Нов механизъм `--accept-identity`: пинът на самоличността се сверява при всяко пускане, освежава се само с изричния флаг (изпълнение на D10) — **препоръка: да**.
78: **Р3** `web/varna_buildings_3d.geojson` се ЗАПИСВА в пиновете сега, а сверяването му остава датиран дълг за следващия лот — **препоръка: да** (алтернативата, пълна проверка сега, разширява обхвата в нощта).
79: **Р4** Редът на трите му комита по §6, като самоличността и пинът пътуват в ЕДИН комит с двойното съобщение — **препоръка: да**.
80: 
81: (D6 — свидетелят в `channels` — и смяната на 8-те зони не са решения: те са изпълнение на подписан ADR.)
82: 
83: **§8 допълнение (К26 П3):**
84: 5. **`vinitsa_sever` в речника на зоните** — alias „Виница-север“ → `dobreva` (препоръка: да), или деактивиран, но видим запис. Без решение прегенерирането спира.
85: 
86: 6. **Манифестът на регистъра** (`registry_manifest.json`, скрит изход на генератора: 9 промени на зони — 3 grandfathered + 6 board_queue) — приема ли се и пинва ли се в същия комит със самоличността (препоръка: да, след преглед на деветте реда в доклада на изпълнителя), или се отлага (тогава пинът му остава стар и се записва като дълг).
87: 
88: ## 9 · Оборване — Кими К26 (леща данни/самоличност), приложено като условия на амандамента
89: Присъда: ГОДНО при пет задължителни поправки — всичките влизат тук:
90: - **П1 · Стълкновения при ключ без зоната.** Измерено: местата дават 150 различни скелета от 150; хотелите — четири двойки (admiral, perla, roial, rusalka), всичките с `matched_by: ntr`, разрешими по УИН. Правило за `#N`, дословно: при два и повече живи обекта с еднакъв `<файл>|skel(име)` номерацията се раздава по **възходящ `place_id`** (`#1`, `#2`, …); гейтът изисква двата реда да се различават по `kais_i` или УИН (иначе СТОП); отрицателна фикстура: разменени номера → ✗. `site_id` **не е котва** днес (`place_identity.py:623-659`) — текстът на амандамента се чете с котви `kais_i` + УИН (`ntr`); ако `site_id` трябва да стане котва, това е отделен подписан ред.
91: - **П2 · Речникът на зоните.** `qa_place_zone_aliases` изисква покритие не само на доставените зони, а на **всичките 60 подписани кода** (по `data/quarters_signed.geojson`), **петте района** (за DISTRICT_FALLBACK) и **резервата за Перчемлията** (район Приморски по регистъра) — всеки `display` низ трябва да е в регистъра или в подписана таблица; липсващ → ✗ поименно.
92: - **П3 · `vinitsa_sever` в речника.** Решение на Петър (§8 т. 5): alias „Виница-север“ → `dobreva` (препоръка), или деактивиран запис, който остава видим за `build_place_categories.py`; без едно от двете прегенерирането е обвързано с нерешения регистров ход Р, а 23-те кадастрални адреса „зона Виница-север“ губят зоновата си дума.
93: - **П4 · Гейт срещу мълчалив презапис (G17).** Нов гейт в `qa_p8a`: **всеки ред със сменена зона доказано е имал ПРАЗЕН написан квартал** в основата (или е fallback-ред по Б0 т. 4(i)); броят на сменените зони ≤ 174 (празните); фикстура: сменена зона на ред със записан квартал → ✗. Довод: `old_zone` идва от замразения `legacy_zones` (375/375), тоест зоната на самоличността ≠ написаният квартал — това трябва да е число, не проза.
94: - **П5 · Обявени отклонения в подписа.** Временното неизпълнение на `qa_place_identity_coords.py` (G9 на Б2-0, който по конструкция забранява смяна на key/zone) и отпадането/обръщането на C7 в `qa_identity_refresh.py` (KEY_PARTS 3 → 2) се изреждат **поименно в подписа на Петър** като обявени отклонения.
95: 
96: ## 10 · Оборване — Astra S25 (леща механика), приложено като задължителни условия
97: Присъда на Astra: „негодно за изпълнение в сегашния текст; път А работи“. Измерено от нея с реалната логика на генератора и износителите (в паметта): път А запазва **375/375 `place_id`**, координатите, доказателствата и осемте вече оттеглени записа; прекодирането мени само 375 `key` и `_meta.rule_key`, освежаването само 57 `zone`; двата сирака (III ПМГ „Акад. Методий Попов“, ОУ „П. Р. Славейков“ — едно тяло 39992) се възстановяват; повторните прогони са байт-еднакви; **26 позиции в `objects` се пренареждат** → гейтът на прекодирането сравнява обектите **по `place_id`**, с отделна проверка за уникалност. Условията:
98: - **A1 · Договорът на `--accept-identity` (F1).** Редът е: успешен гейт → **кандидатът се повишава в каноничен** `data/place_identity.json` → едва тогава `fire_varna_locations.py --inputs --accept-identity <sha256 на каноничния файл>`; аргументът се сверява по съществуващото правило (CRLF→LF, SHA-256, `fire_varna_locations.py:1781`) срещу реално прочетения файл; грешен аргумент = СТОП; останалите пинове остават активни. **Три доказателства**: застоял записан пин без флага → СТОП; грешен sha като аргумент → СТОП; правилно приемане → следващият нормален прогон минава. (Днес обърнат hex знак в пина на самоличността **се приема** и `load()` строи 375 реда — това е дупката, която се затваря.)
99: - **A2 · `qa_identity_refresh.py`**: `KEY_PARTS` 3 → 2, C6 = „ключът НЕ се мени при освежаване“, C7 отпада; основата на освежаването е **приетата прекодирана самоличност**, `ALLOWED_FIELDS = {"zone"}`, задължителен втори кандидат за детерминизъм.
100: - **A3 · Неподвижната точка (F2), дословно:** JSON parse → изтриване само на `_meta.generated` → `json.dumps(doc, ensure_ascii=False, indent=1) + "\n"` → UTF-8 → сравнение на байтове; масивите пазят реда си; леджерът се сравнява директно без изключения. Измерено: вторият леджер след освежаването е байт-еднакъв с първия и с паркирания (958 449 B, `fba94bf8…`); двата износа при различни часовници дават еднакъв нормализиран резултат. Компараторът получава име и CLI в write-set-а (`src/qa_fixed_point.py --a <път> --b <път> [--ignore _meta.generated]`).
101: - **A4 · Редът на прегенериране (блокер):** `build_place_categories.py` се пуска **СЛЕД последния износ** (иначе `legacy_bundle_sha`, който хешира целите байтове с часовника, се обезсилва от самата стъпка 6), после гейтът на alias-ите. Осемте нови зони съществуват в регистъра и се извеждат автоматично.
102: - **A5 · Скритият изход на генератора (F3):** генераторът винаги строи и пише `registry_manifest.json`; при освежаването са измерени **9 допълнителни промени на зони в манифеста (3 `grandfathered` + 6 `board_queue`)**. Всеки кандидат-прогон задава `--manifest-out` към `scratch/granitsi/`; дали полученият манифест се приема и пинва е **решение на Петър (§8 т. 6)**; приетият манифест влиза в същия комит като самоличността и пина.
103: - **A6 · M6 и D6-формата:** при успешно присвояване писачът на леджера добавя `channels.SIGNED_POLYGON = {"ids": [winner], "raw": [safe_witness]}`, при резерва — `DISTRICT_FALLBACK` с районния код; петте изборни `CHANNELS` остават пет; приемането на M6 сравнява **точните осем `place_id`** на pending-редовете (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата), не броя; отделна проверка на района преди общата квартална за fallback-редове и **положителна fallback-фикстура** (днес такива редове са нула).
104: - **A7 · Изпълнимият ред:** замразена основа → два кандидата за прекодиране + гейт → повишаване + пинове (`--accept-identity`) → двата износителя и `fire_varna_locations.py --ledger` → два кандидата за освежаване + гейт → повишаване + пинове → повторни износи/леджер + гейтът на неподвижната точка → категории → всички финални гейтове (alias-и, M6 с точното множество, `qa_p8a` вкл. П4, G17, пълният набор). Всеки неочакван неуспех спира. **Комитите на Петър:** (1) окончателната самоличност **заедно с пиновете (и приетия манифест) в един комит**, чието съобщение назовава и трите товара (координати от Б0 т. 11, прекодиране без зоната, 57 освежени зони); (2) двата износа + `place_categories.json`; (3) датираният леджер.
105: - **Съгласуване с К26 П1:** правилото за `#N` при стълкновение е **днешното** на генератора — по координатен ранг (`place_identity.py:225`), детерминирано и измерено; записва се дословно, а отрицателната фикстура „разменени номера“ от П1 важи както е.
106: 
107: ## 11 · Статус
108: **ПОДПИСАН от Петър (07.09.2026): „подписвам амендамент 3 с решения 1-6 по препоръките“.** Подписаното тяло: ревизия 2, sha256 на blob-а в комит 4e9606c = `cf919f178462dd832581b7abf8aba1dae2ab6bd326f2f90919f659d5a7ab2ebc`. Обявените отклонения (G9 на Б2-0 не се пуска в този лот; C7 на qa_identity_refresh отпада) са покрити от подписа.
109: 
110: Преди подписа: Минал през: два вътрешни Opus лещи (чернова → синтез), Кими К26 (ГОДНО с П1–П5, вградени в §9), Astra S25 (условията A1–A7, вградени в §10). Изпълнението (повторение на Б2) тръгва след подписа, с изпълнител и одитор на всеки ход, без пуш, с локален преглед на картата от Петър преди каквато и да е доставка.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); Get-Content -Encoding utf8 -LiteralPath '"'C:/git/varna_3d/docs/activeContext.md' -TotalCount 90; Get-Content -Encoding utf8 -LiteralPath 'C:/git/Fire_Varna/docs/activeContext.md' -TotalCount 70" in C:\git
 succeeded in 0ms:
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=87; Get-Content -Encoding utf8 -LiteralPath '"'C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md' | Select-Object -Skip 87 -First 100 | ForEach-Object { "'$n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git
 succeeded in 14ms:
88: ## 9 · Оборване — Кими К26 (леща данни/самоличност), приложено като условия на амандамента
89: Присъда: ГОДНО при пет задължителни поправки — всичките влизат тук:
90: - **П1 · Стълкновения при ключ без зоната.** Измерено: местата дават 150 различни скелета от 150; хотелите — четири двойки (admiral, perla, roial, rusalka), всичките с `matched_by: ntr`, разрешими по УИН. Правило за `#N`, дословно: при два и повече живи обекта с еднакъв `<файл>|skel(име)` номерацията се раздава по **възходящ `place_id`** (`#1`, `#2`, …); гейтът изисква двата реда да се различават по `kais_i` или УИН (иначе СТОП); отрицателна фикстура: разменени номера → ✗. `site_id` **не е котва** днес (`place_identity.py:623-659`) — текстът на амандамента се чете с котви `kais_i` + УИН (`ntr`); ако `site_id` трябва да стане котва, това е отделен подписан ред.
91: - **П2 · Речникът на зоните.** `qa_place_zone_aliases` изисква покритие не само на доставените зони, а на **всичките 60 подписани кода** (по `data/quarters_signed.geojson`), **петте района** (за DISTRICT_FALLBACK) и **резервата за Перчемлията** (район Приморски по регистъра) — всеки `display` низ трябва да е в регистъра или в подписана таблица; липсващ → ✗ поименно.
92: - **П3 · `vinitsa_sever` в речника.** Решение на Петър (§8 т. 5): alias „Виница-север“ → `dobreva` (препоръка), или деактивиран запис, който остава видим за `build_place_categories.py`; без едно от двете прегенерирането е обвързано с нерешения регистров ход Р, а 23-те кадастрални адреса „зона Виница-север“ губят зоновата си дума.
93: - **П4 · Гейт срещу мълчалив презапис (G17).** Нов гейт в `qa_p8a`: **всеки ред със сменена зона доказано е имал ПРАЗЕН написан квартал** в основата (или е fallback-ред по Б0 т. 4(i)); броят на сменените зони ≤ 174 (празните); фикстура: сменена зона на ред със записан квартал → ✗. Довод: `old_zone` идва от замразения `legacy_zones` (375/375), тоест зоната на самоличността ≠ написаният квартал — това трябва да е число, не проза.
94: - **П5 · Обявени отклонения в подписа.** Временното неизпълнение на `qa_place_identity_coords.py` (G9 на Б2-0, който по конструкция забранява смяна на key/zone) и отпадането/обръщането на C7 в `qa_identity_refresh.py` (KEY_PARTS 3 → 2) се изреждат **поименно в подписа на Петър** като обявени отклонения.
95: 
96: ## 10 · Оборване — Astra S25 (леща механика), приложено като задължителни условия
97: Присъда на Astra: „негодно за изпълнение в сегашния текст; път А работи“. Измерено от нея с реалната логика на генератора и износителите (в паметта): път А запазва **375/375 `place_id`**, координатите, доказателствата и осемте вече оттеглени записа; прекодирането мени само 375 `key` и `_meta.rule_key`, освежаването само 57 `zone`; двата сирака (III ПМГ „Акад. Методий Попов“, ОУ „П. Р. Славейков“ — едно тяло 39992) се възстановяват; повторните прогони са байт-еднакви; **26 позиции в `objects` се пренареждат** → гейтът на прекодирането сравнява обектите **по `place_id`**, с отделна проверка за уникалност. Условията:
98: - **A1 · Договорът на `--accept-identity` (F1).** Редът е: успешен гейт → **кандидатът се повишава в каноничен** `data/place_identity.json` → едва тогава `fire_varna_locations.py --inputs --accept-identity <sha256 на каноничния файл>`; аргументът се сверява по съществуващото правило (CRLF→LF, SHA-256, `fire_varna_locations.py:1781`) срещу реално прочетения файл; грешен аргумент = СТОП; останалите пинове остават активни. **Три доказателства**: застоял записан пин без флага → СТОП; грешен sha като аргумент → СТОП; правилно приемане → следващият нормален прогон минава. (Днес обърнат hex знак в пина на самоличността **се приема** и `load()` строи 375 реда — това е дупката, която се затваря.)
99: - **A2 · `qa_identity_refresh.py`**: `KEY_PARTS` 3 → 2, C6 = „ключът НЕ се мени при освежаване“, C7 отпада; основата на освежаването е **приетата прекодирана самоличност**, `ALLOWED_FIELDS = {"zone"}`, задължителен втори кандидат за детерминизъм.
100: - **A3 · Неподвижната точка (F2), дословно:** JSON parse → изтриване само на `_meta.generated` → `json.dumps(doc, ensure_ascii=False, indent=1) + "\n"` → UTF-8 → сравнение на байтове; масивите пазят реда си; леджерът се сравнява директно без изключения. Измерено: вторият леджер след освежаването е байт-еднакъв с първия и с паркирания (958 449 B, `fba94bf8…`); двата износа при различни часовници дават еднакъв нормализиран резултат. Компараторът получава име и CLI в write-set-а (`src/qa_fixed_point.py --a <път> --b <път> [--ignore _meta.generated]`).
101: - **A4 · Редът на прегенериране (блокер):** `build_place_categories.py` се пуска **СЛЕД последния износ** (иначе `legacy_bundle_sha`, който хешира целите байтове с часовника, се обезсилва от самата стъпка 6), после гейтът на alias-ите. Осемте нови зони съществуват в регистъра и се извеждат автоматично.
102: - **A5 · Скритият изход на генератора (F3):** генераторът винаги строи и пише `registry_manifest.json`; при освежаването са измерени **9 допълнителни промени на зони в манифеста (3 `grandfathered` + 6 `board_queue`)**. Всеки кандидат-прогон задава `--manifest-out` към `scratch/granitsi/`; дали полученият манифест се приема и пинва е **решение на Петър (§8 т. 6)**; приетият манифест влиза в същия комит като самоличността и пина.
103: - **A6 · M6 и D6-формата:** при успешно присвояване писачът на леджера добавя `channels.SIGNED_POLYGON = {"ids": [winner], "raw": [safe_witness]}`, при резерва — `DISTRICT_FALLBACK` с районния код; петте изборни `CHANNELS` остават пет; приемането на M6 сравнява **точните осем `place_id`** на pending-редовете (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата), не броя; отделна проверка на района преди общата квартална за fallback-редове и **положителна fallback-фикстура** (днес такива редове са нула).
104: - **A7 · Изпълнимият ред:** замразена основа → два кандидата за прекодиране + гейт → повишаване + пинове (`--accept-identity`) → двата износителя и `fire_varna_locations.py --ledger` → два кандидата за освежаване + гейт → повишаване + пинове → повторни износи/леджер + гейтът на неподвижната точка → категории → всички финални гейтове (alias-и, M6 с точното множество, `qa_p8a` вкл. П4, G17, пълният набор). Всеки неочакван неуспех спира. **Комитите на Петър:** (1) окончателната самоличност **заедно с пиновете (и приетия манифест) в един комит**, чието съобщение назовава и трите товара (координати от Б0 т. 11, прекодиране без зоната, 57 освежени зони); (2) двата износа + `place_categories.json`; (3) датираният леджер.
105: - **Съгласуване с К26 П1:** правилото за `#N` при стълкновение е **днешното** на генератора — по координатен ранг (`place_identity.py:225`), детерминирано и измерено; записва се дословно, а отрицателната фикстура „разменени номера“ от П1 важи както е.
106: 
107: ## 11 · Статус
108: **ПОДПИСАН от Петър (07.09.2026): „подписвам амендамент 3 с решения 1-6 по препоръките“.** Подписаното тяло: ревизия 2, sha256 на blob-а в комит 4e9606c = `cf919f178462dd832581b7abf8aba1dae2ab6bd326f2f90919f659d5a7ab2ebc`. Обявените отклонения (G9 на Б2-0 не се пуска в този лот; C7 на qa_identity_refresh отпада) са покрити от подписа.
109: 
110: Преди подписа: Минал през: два вътрешни Opus лещи (чернова → синтез), Кими К26 (ГОДНО с П1–П5, вградени в §9), Astra S25 (условията A1–A7, вградени в §10). Изпълнението (повторение на Б2) тръгва след подписа, с изпълнител и одитор на всеки ход, без пуш, с локален преглед на картата от Петър преди каквато и да е доставка.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'write|open\\(|Temporary|tempfile|subprocess|ArgumentParser|add_argument|def main|__main__' src/qa_p8a.py src/qa_fire_varna_places_export.py src/qa_place_zone_aliases.py src/qa_fire_varna_m6.py src/qa_no_cad_ids.py" in C:\git\varna_3d
 succeeded in 0ms:
src/qa_no_cad_ids.py:22:import subprocess
src/qa_no_cad_ids.py:116:def main() -> None:
src/qa_no_cad_ids.py:123:    r = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True)
src/qa_no_cad_ids.py:182:if __name__ == "__main__":
src/qa_fire_varna_m6.py:244:def main(argv: list[str]) -> None:
src/qa_fire_varna_m6.py:247:    ap = argparse.ArgumentParser()
src/qa_fire_varna_m6.py:248:    ap.add_argument("--ledger", default=str(LEDGER),
src/qa_fire_varna_m6.py:251:    ap.add_argument("--break-me", choices=("table", "witness", "resort",
src/qa_fire_varna_m6.py:257:    ap.add_argument("--fixture", choices=("fallback",),
src/qa_fire_varna_m6.py:531:if __name__ == "__main__":
src/qa_place_zone_aliases.py:229:                       "(DISTRICT_FALLBACK writes a district code into "
src/qa_place_zone_aliases.py:294:def main() -> None:
src/qa_place_zone_aliases.py:405:if __name__ == "__main__":
src/qa_fire_varna_places_export.py:587:def main() -> None:
src/qa_fire_varna_places_export.py:588:    ap = argparse.ArgumentParser(description="гейт на местата за Fire_Varna")
src/qa_fire_varna_places_export.py:589:    ap.add_argument("--places", default=None,
src/qa_fire_varna_places_export.py:591:    ap.add_argument("--hotels", default=None,
src/qa_fire_varna_places_export.py:924:if __name__ == "__main__":
src/qa_p8a.py:45:import subprocess
src/qa_p8a.py:118:    got = subprocess.run(["git", "show", target], cwd=str(ROOT),
src/qa_p8a.py:287:def main() -> int:
src/qa_p8a.py:288:    ap = argparse.ArgumentParser(description="гейт P8-а · лот Б2")
src/qa_p8a.py:289:    ap.add_argument("--ledger", default=str(
src/qa_p8a.py:292:    ap.add_argument("--places", default=str(ROOT / "data" / "fire_varna_places.json"))
src/qa_p8a.py:293:    ap.add_argument("--hotels", default=str(ROOT / "data" / "fire_varna_hotels.json"))
src/qa_p8a.py:294:    ap.add_argument("--conflicts", default=str(
src/qa_p8a.py:296:    ap.add_argument("--signed", default=str(ROOT / "data" / "quarters_signed.geojson"))
src/qa_p8a.py:297:    ap.add_argument("--source", default=str(SRC / "fire_varna_locations.py"))
src/qa_p8a.py:298:    ap.add_argument("--base-rev", default=BASE_REV)
src/qa_p8a.py:616:if __name__ == "__main__":

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); Get-Content -Encoding utf8 -LiteralPath src/qa_fixed_point.py -TotalCount 135; Get-Content -Encoding utf8 -LiteralPath src/qa_identity_rekey.py -TotalCount 85; rg -n --max-count 20 --max-columns 200 '"'qa_fixed_point|identity_rekey_base|qa_identity_rekey' scratch/granitsi/*.md" in C:\git\varna_3d
 exited 1 in 0ms:
"""Неподвижната точка (амандамент №3 §4 т. 6 · A3): два прогона, едни байтове.

Присвояването на квартал пише в `data/place_identity.json` (зоната), а
самоличността е ВХОД на същото присвояване.  Такъв кръг е здрав само ако е
НЕПОДВИЖНА ТОЧКА: вторият прогон върху освежената самоличност трябва да върне
СЪЩИЯ резултат.  Ако не го връща, конвейерът има памет — а памет, която никой
не е обявил, е дефект.

Сравнението прави ГЕЙТЪТ, не окото, и правилото е дословно това на A3:

    JSON parse → изтриване САМО на изрично назованите ключове
    (`--ignore _meta.generated`) → `json.dumps(doc, ensure_ascii=False,
    indent=1) + "\\n"` → UTF-8 → сравнение на БАЙТОВЕ.

Масивите пазят реда си: пренареден масив НЕ е същият документ.  Леджерът се
сравнява ДИРЕКТНО, без нито едно изключение — `_meta`-то му няма часовник, и
точно затова няма какво да му се прощава.  Двата износа носят стенен часовник в
`_meta.generated` (записан дълг 07.09) и това е ЕДИНСТВЕНИЯТ назован ключ, който
се маха; всяка друга разлика е червено.

    python src/qa_fixed_point.py --a <път> --b <път>
    python src/qa_fixed_point.py --a <път> --b <път> --ignore _meta.generated

Изход 0 = байт-еднакви след нормализацията · 1 = различни (с първата разлика
поименно) · 2 = липсващ вход.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def drop(doc, dotted: str) -> bool:
    """Изтрива ЕДИН назован ключ по път `a.b.c`; връща дали го е намерил.

    Никакви шаблони и никакво „по подразбиране“: гейт, който сам решава кое да
    прости, не е гейт.  Пътят се изрича на командния ред.
    """
    parts = dotted.split(".")
    node = doc
    for p in parts[:-1]:
        if not isinstance(node, dict) or p not in node:
            return False
        node = node[p]
    if isinstance(node, dict) and parts[-1] in node:
        del node[parts[-1]]
        return True
    return False


def normalise(path: Path, ignore: list[str]) -> tuple[bytes, list[str]]:
    doc = json.loads(path.read_text(encoding="utf-8"))
    dropped = [key for key in ignore if drop(doc, key)]
    text = json.dumps(doc, ensure_ascii=False, indent=1) + "\n"
    return text.encode("utf-8"), dropped


def first_difference(a: bytes, b: bytes) -> str:
    """Първата различна позиция, показана като редове — не като байтова каша."""
    la = a.decode("utf-8").splitlines()
    lb = b.decode("utf-8").splitlines()
    for n, (x, y) in enumerate(zip(la, lb), start=1):
        if x != y:
            return f"ред {n}:\n    A: {x.strip()[:200]}\n    B: {y.strip()[:200]}"
    if len(la) != len(lb):
        return f"еднакви до ред {min(len(la), len(lb))}, но A има {len(la)} " \
               f"реда, а B — {len(lb)}"
    return "различни байтове при еднакви редове (край на файла)"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="неподвижната точка: два документа, едни байтове (A3)")
    ap.add_argument("--a", required=True, help="първият прогон")
    ap.add_argument("--b", required=True, help="вторият прогон")
    ap.add_argument("--ignore", action="append", default=[],
                    metavar="a.b.c",
                    help="ЕДИН назован ключ, който се маха преди сравнението "
                         "(например _meta.generated); може да се повтори")
    ap.add_argument("--label", default="", help="име за печата")
    a = ap.parse_args(argv)

    pa, pb = Path(a.a), Path(a.b)
    for p in (pa, pb):
        if not p.exists():
            print(f"ГРЕШКА: липсва {p}", file=sys.stderr)
            return 2

    label = a.label or f"{pa.name} ↔ {pb.name}"
    ba, dropped_a = normalise(pa, a.ignore)
    bb, dropped_b = normalise(pb, a.ignore)
    said = (" · махнати ключове: " + ", ".join(sorted(set(dropped_a + dropped_b)))
            if a.ignore else " · без изключения (директно сравнение)")
    if ba == bb:
        print(f"  ok    неподвижна точка · {label} · {len(ba)} байта{said}")
        return 0
    print(f"ПАДА   неподвижна точка · {label}{said}")
    print("       " + first_difference(ba, bb))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
"""Гейтът на ПРЕКОДИРАНЕТО: ключът без зоната (амандамент №3, път А, 07.09).

Амандамент №3 към ЛОТ „Границите“ сваля зоната от ключа на самоличността
(`<файл>|<скелет>|<зона>` → `<файл>|<скелет>`), защото присвояването на квартал
мени точно зоната и с нея чупеше ключа — 57 реда сменяха зона, 2 стари
самоличности излизаха „оттеглени без решение“ и генераторът падаше.

Този гейт казва ЕДНО нещо:

    прекодирането мени САМО полето `key` на живите обекти и САМО
    `_meta.rule_key` — нито един `place_id`, нито един оттеглен запис, нито
    едно друго поле, — и го прави детерминирано.

Обектите се сравняват ПО `place_id`, а не по ред: измерено 07.09, 26 позиции в
`objects` се пренареждат, защото файлът се подрежда по ключ (Astra S25).

    python src/qa_identity_rekey.py \
        --base tests/fixtures/identity_rekey_base_2026-09-07.json \
        --candidate scratch/granitsi/place_identity.rekey.json \
        --candidate2 scratch/granitsi/place_identity.rekey.run2.json \
        --expect-base-sha 1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761 \
        [--review <out.json>]

ЗАМРАЗЕНАТА ОСНОВА живее В ДЪРВОТО: `tests/fixtures/identity_rekey_base_2026-09-07.json`
е байт-копие на предпрекодираната самоличност (`1141bbc2…`, LF).  Дотук тя
лежеше в игнорирания `scratch/`, тоест гейтът не можеше да се пусне от чисто
изтегляне; амандамент №3 §3 ред 2 я праща в комита изрично („и фикстурите“) —
тя е тестов материал, а не доставка по D16/G4.

`--expect-base-sha` е ЗАДЪЛЖИТЕЛЕН: основата се ОБЯВЯВА, а не се подразбира,
за да тича C0 при всеки прогон — гейт срещу застояла или подменена основа
съди празно.

Изход 0 = зелен.  Всяка паднала проверка печата `✗` и връща 1 — гейт, който не
е ПАДАЛ на счупен вход, не е гейт, затова отрицателните фикстури живеят в
`scratch/granitsi/rekey_negatives.py`.

Само за четене: скриптът не пише нищо в `data/`; единственият файл, който може
да напише, е прегледът, назован на командния ред.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
# Скелетът е ПРАВИЛОТО на генератора, не негов препис: ключът се проверява с
# точно същата функция, с която е построен, иначе гейтът съди по свой език.
from place_identity import skel                            # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
PLACES_EXPORT = ROOT / "data" / "fire_varna_places.json"
HOTELS_EXPORT = ROOT / "data" / "fire_varna_hotels.json"

# Прекодирането има право да пипне ЕДНО поле на обекта и ЕДИН ключ на `_meta`.
ALLOWED_OBJECT_FIELDS = {"key"}
ALLOWED_META_KEYS = {"rule_key"}
KEY_PARTS = 2                       # <файл>|<скелет на името>
# Измерено 07.09 (амандамент №3 §1 т. 6 и §9 П1): местата дават 150 различни
# скелета от 150; хотелите — четири двойки, и осемте реда с котва УИН.
EXPECT_COLLISIONS = ("hotels|admiral", "hotels|perla", "hotels|roial",
                     "hotels|rusalka")
CAD = re.compile(r"\b\d{4,5}\.\d+\.\d+")


class Gate:
    def __init__(self) -> None:
        self.fails: list[str] = []
        self.checks: list[tuple[str, bool, str]] = []

    def check(self, name: str, ok: bool, detail: str = "") -> bool:
        self.checks.append((name, bool(ok), detail))
        if not ok:
            self.fails.append(f"{name}: {detail}")
        print(f"{'✓' if ok else '✗'} {name}" + (f" — {detail}" if detail else ""))
        return bool(ok)


rg: scratch/granitsi/*.md: IO error for operation on scratch/granitsi/*.md: The filename, directory name, or volume label syntax is incorrect. (os error 123)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git -C C:/git/Fire_Varna log -3 --format='%h %an <%ae> %s' -- 'docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md'; git -C C:/git/varna_3d diff --numstat -- src tests; Get-Command sha256sum -ErrorAction SilentlyContinue | Select-Object Source; Get-Command python | Select-Object Source" in C:\git
 succeeded in 10ms:
Source                                    
------                                    
C:\Program Files\Git\usr\bin\sha256sum.exe
C:\Program Files\Python310\python.exe     



codex
Подписът в §11 покрива решения 1–6 и условията П1–П5/A1–A7. За първия комит A7 изисква допълнение към текста на §6: да назове и 57-те освежени зони; приетият манифест с деветте промени трябва да е в същия комит.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_p8a.py" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_fire_varna_places_export.py" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_place_zone_aliases.py" in C:\git\varna_3d
 succeeded in 0ms:
=== ГЕЙТ P8-а: подписаният полигон, написаният квартал и затворената таблица ===

  ok  подписаните граници са блобът на Петър (6486b48) · c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3 срещу закования c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3
  ok  60 подписани Feature-а с клас signed_by_plan_signature · 60 · signed_by_plan_signature
  ok  precision_m ≥ 50 m във всеки Feature (D7) · [50, 100] m
  ok  базата е блобът d5050f1cfb3d… с 375 реда (git show 8d60aebb365fb8e74ccc863d3b3db90b74180a3b:scratch/refactor/_addr/lot1v_locations_375.json) · d5050f1cfb3d… · 375 реда
  ok  базата носи 201 написани квартала · 201
  ok  старият леджер в дървото е БАЙТ-РАВЕН на блоба — този лот не го пипа · d5050f1cfb3d…
  ok  новият леджер е ДРУГ файл (датиран), не презапис на базата · lot1v_locations_375_p8a_07.09.json
  ok  новият леджер назовава базата си (`_meta.base_rev` + sha на блоба) · 8d60aebb365fb8e74ccc863d3b3db90b74180a3b · d5050f1cfb3d…
  ok  новият леджер има 375 реда · 375
  ok  G17 · всеки от 201-те написани квартала е БАЙТ-РАВЕН в новия леджер (D18) · 201/201
  ok  двата износа заедно носят 375 реда · 375
  ok  всеки изнесен ред се намира в леджера по (файл, име) · 375 реда
  ok  G17 · кварталът в износа е байт-равен на този в леджера · 375 реда
  ok  G17 · множеството написани квартали в ИЗНОСА е точно базовото (201 реда) · еднакви
  ok  всеки ред носи ТОЧНО един изход от затворената таблица · written 201 · no_coord 0 · pin_outside_all 41 · edge_pending 63 · disputed_overlap 5 · deferred_zone 0 · assigned_polygon 65 · assigned_district 0
  ok  таблицата покрива всичките 375 места · 375
  ok  `_meta.outcomes` == преброеното по редовете · {'written': 201, 'no_coord': 0, 'pin_outside_all': 41, 'edge_pending': 63, 'disputed_overlap': 5, 'deferred_zone': 0, 'assigned_polygon': 65, 'assigned_district': 0} срещу {'written': 201, 'no_coord': 0, 'pin_outside_all': 41, 'edge_pending': 63, 'disputed_overlap': 5, 'deferred_zone': 0, 'assigned_polygon': 65, 'assigned_district': 0}
  ok  редът на таблицата е подписаният (Б0 т. 12) · written · no_coord · pin_outside_all · edge_pending · disputed_overlap · deferred_zone · assigned_polygon · assigned_district
  ok  фикстура на всяка от 8-те клетки на затворената таблица (12 състояния) · written · no_coord · pin_outside_all · edge_pending · disputed_overlap · deferred_zone · assigned_polygon · assigned_district
  ok  фикстурите покриват ВСИЧКИ клетки и нито една извън таблицата · 8/8
  ok  Б0 т. 4 (i)–(iii): нито едно състояние не дава районна резерва днес, и всеки отказ носи довод · 5 състояния, 5 отказа
  ok  ръбът е max(50, precision_m) и разделя edge_pending от присвоеното (D7 · Б0 т. 6) · 375 реда
  ok  родството в леджера е ПРЕПИС на подписания DAG (Б0 т. 9) · 11
  ok  отложените кодове са тези на подписания файл (17) · akchelar_vinitsa_seam · borovets · byalata_cheshma
  ok  нито едно място с ДВА присвоени квартала: точно един канал пише на ред и никога върху написан · полигон 57 · резерва 0
  ok  `_meta` брои същото, което носят редовете · 57 · 0
  ok  всеки квартал по полигон носи код от ПОДПИСАНИЯ файл · 57 реда
  ok  Б0 т. 4 (i)–(iii) държат за всеки ред с районна резерва (0) · 0 реда днес — таблицата слага pin_outside_all преди резервата
  ok  П4 · всеки ред със сменена зона е имал ПРАЗЕН написан квартал в базата (57 сменени) · 57/57 върху празни редове
  ok  П4 · сменените зони са най-много 174 (празните в базата) · 57 ≤ 174
  ok  П4 · множеството сменени зони е ТОЧНО множеството редове, в които канал на P8-а е писал · 57 реда
  ok  леджерът носи атрибуция за всеки код по подписан полигон (Б0 т. 5) · 18 кода
  ok  местата: десетият ключ носи точно кодовете на доставката · 14 кода
  ok  хотелите: десетият ключ носи точно кодовете на доставката · 7 кода
  ok  леджерът на конфликтите покрива 375 места, всяко с твърдения по извор, резолюция и вид на спора · 375 реда
  ok  броевете по вид конфликт са преизчислими от редовете · none 286 · name_vs_polygon 33 · parent_vs_child 0 · pin_outside_all 49 · written_outside_polygon 7
  ok  полигонният канал не чете изнесените координати (D7) — 4 възела обходени · SignedPolygons · _polygon_block · classify_outcome · district_fallback_allowed
  ok  изнесените файлове се четат само от ['comparison_columns'] (сравнителни колони, никога решение) · comparison_columns
  ok  и четирите възела на канала съществуват в модула (гейт срещу преименуване) · 4/4

      затворената таблица: written 201 · no_coord 0 · pin_outside_all 41 · edge_pending 63 · disputed_overlap 5 · deferred_zone 0 · assigned_polygon 65 · assigned_district 0
      написани (непроменени): 201 · квартал по полигон: 57 · районна резерва: 0
      конфликти по вид: none 286 · name_vs_polygon 33 · parent_vs_child 0 · pin_outside_all 49 · written_outside_polygon 7

минава — присвояването по подписани граници е годно за комита на Петър

 succeeded in 0ms:
=== ПРОВЕРКА: местата за Fire_Varna (фаза 2) ===

  ok  файлът е UTF-8 без BOM и с LF · UTF-8, без BOM, LF
  ok  всяко ново/преименувано име стъпва на регистров ред (21 нови + 9 преименувани) · 53 ДГ · 12 ясли · 69 училища в преписа
  ok  нито едно доставено име не носи признака „яслена група“ · 150 имена проверени
  ok  всеки кандидат от двата извора е изнесен или назован (230 кандидата) · 150 изнесени + 80 назовани
  ok  всеки ред в изхода има извор · 150 реда
  ok  _meta.count == действителния брой · _meta.count=150 · редове=150
  ok  файлът има точно два ключа · _meta · places
  ok  _meta има точно 10 ключа · by_kind · by_zone_src · count · excluded · generated · licence_address · licence_osm · licence_registry · licence_wikidata · quarter_attribution
  ok  всеки ред има точно 13-те ключа · address · district · kind · lat · locality · lon · name · old_names · old_names_src · quarter · src · status · zone
  ok  _meta.generated носи дата и команда · 2026-09-07 05:41:25 · python src/export_fire_varna_places.py
  ok  quarter/district/locality са null или {name, src, code} · 150 реда с трите полета
  ok  изворите са от затворените списъци · DISTRICT_FALLBACK · KAIS · REG · SIGNED_OVERRIDE · SIGNED_POLYGON
  ok  районът е от петте и носи името си · Аспарухово · Владислав Варненчик · Младост · Одесос · Приморски
  ok  кодовете на квартала/допълнителното са от регистъра и името е неговият дословен показ (районната резерва — от петте района и от СОБСТВЕНИЯ район на реда) · 84 записа в регистъра
  ok  нула DROP-име и нула разменен клас в показвано поле · 11 записа падат по таблицата и нито един не е доставен
  ok  `zone` е съвместимост: quarter?.name ?? „район X“ · 150 реда
  ok  _meta.by_zone_src == броенето по извор на зоната · _meta={'KAIS': 10, 'REG': 39, 'SIGNED_POLYGON': 42, 'district': 59} · изворът брои {'SIGNED_POLYGON': 42, 'district': 59, 'REG': 39, 'KAIS': 10}
  ok  местата: `_meta.quarter_attribution` е речник · dict
  ok  местата: всеки запис носи {src, url, label, licence} и низът, лицензът и връзката са на СВОЯ извор · 14 кода · openstreetmap · wikimapia
  ok  местата: биекция между кодовете по подписан полигон и записите (14 кода) · 14 кода в доставката
  ok  пинът на подписаните граници в data/fire_varna_location_inputs.json == sha256 на самия файл · пин c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3 · файл c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3
  ok  хотелите: `_meta` има точно 8 ключа · by_zone_src · count · excluded · generated · licence · licence_address · licence_osm · quarter_attribution
  ok  хотелите: `_meta.quarter_attribution` е речник · dict
  ok  хотелите: всеки запис носи {src, url, label, licence} и низът, лицензът и връзката са на СВОЯ извор · 7 кода · wikimapia
  ok  хотелите: биекция между кодовете по подписан полигон и записите (7 кода) · 7 кода в доставката
  ok  quarter/district/locality са null или {name, src, code} · 225 реда с трите полета
  ok  изворите са от затворените списъци · DISTRICT_FALLBACK · KAIS · REG · SIGNED_OVERRIDE · SIGNED_POLYGON
  ok  районът е от петте и носи името си · Аспарухово · Владислав Варненчик · Младост · Одесос · Приморски
  ok  кодовете на квартала/допълнителното са от регистъра и името е неговият дословен показ (районната резерва — от петте района и от СОБСТВЕНИЯ район на реда) · 84 записа в регистъра
  ok  нула DROP-име и нула разменен клас в показвано поле · 11 записа падат по таблицата и нито един не е доставен
  ok  `zone` е съвместимост: quarter?.name ?? „район X“ · 225 реда
  ok  _meta.by_zone_src == броенето по извор на зоната · _meta={'KAIS': 25, 'REG': 115, 'SIGNED_OVERRIDE': 12, 'SIGNED_POLYGON': 15, 'district': 58} · изворът брои {'SIGNED_OVERRIDE': 12, 'REG': 115, 'district': 58, 'KAIS': 25, 'SIGNED_POLYGON': 15}
  ok  _meta.by_kind == броенето по клас · училище 57 · университет 7 · болница 11 · ДКЦ 7 · хоспис 6 · детска градина 51 · детска ясла 10 · общежитие 1
  ok  клас · източник · статус · зона · old_names са от речника · 150 реда
  ok  всеки псевдоним носи извор от затворения списък (65 псевдонима)
  ok  Wikidata псевдонимите са толкова, колкото id-та носи лицензът (3) · носи 3
  ok  всеки адрес: извор от списъка · непразен текст · съгласувани улична фраза и номер (115 адреса · KAIS 96 · OSM 1 · REG 18)
  ok  лицензният ред за адресите стои в _meta, дословно · дословен
  ok  нула имотни токени в целия blob · чисто
  ok  всяка координата в кутията (43.13–43.35, 27.65–28.1) · 150 координати
  ok  нула кадастрални идентификатори · чисто
  ok  думата „кадаст…“ не се среща никъде · чисто
  ok  нула телефони · имейли · десетцифрени числа · 150 реда
  ok  „д-р/доктор + дума“ винаги в институционално име (К7) · 8 имена с „д-р“, всичките институционални
  ok  нула неназовани дублети (skel(име), зона) · 150 ключа за 150 реда · назовани близнаци: 
  ok  класът е този на извора, освен 7-те поименни пречипвания · II ДКЦ Св. Иван Рилски → ДКЦ · Диспансер за белодробни заболявания → ДКЦ · Морска гимназия "Св. Николай Чудотворец" → училище
  ok  „бивш“ стои точно там, където го иска изворът · иска ['бивше ОУ „Д-р Никола Димитров“'] · носи ['бивше ОУ „Д-р Никола Димитров“']
  ok  всяко изключване е поименно, с клас, източник и довод (80) · всичките с довод
  ok  licence_osm стои дословно и цитира атрибуцията на извора · дословен
  ok  licence_registry стои дословно (образецът на НТР) · дословен
  ok  licence_wikidata стои дословно и назовава своите id-та · дословен

      места: 150 · училище 57 · университет 7 · болница 11 · ДКЦ 7 · хоспис 6 · детска градина 51 · детска ясла 10 · общежитие 1
      назовани изключения: 80 · със стари имена: 58

минава — артефактът може да тръгне към Fire_Varna

 succeeded in 0ms:
=== GATE: the quarter aliases of the search dictionary (П7) ===

  ok    (e) schema is still 1 · 1
  ok    (e) the category part is present · 57 chips · 283 forms
  ok    (e) `zones` is a non-empty object · 28 zones
  ok    (e) every zone is {family: str, aliases: [str]}
  ok    (a) every delivered zone is either matched or named as unmatched
  ok    (a) no zone key that the exports do not deliver
  ok    (a) no zone is matched and unmatched at once
  ok    (b) every alias is a verbatim display/alias of the registry
  ok    (i) the override table is signed (`signed_by` + `signed_at`) · Petar (amendment 3 decision 5) · 2026-09-07
  ok    (i) every override KEY is a verbatim registry string · 1 реда
  ok    (i) every override VALUE is a registry id · dobreva
  ok    (i) the dictionary records the SAME signed table it was built from · Petar (amendment 3 decision 5) · 1 реда
  ok    (i) every APPLIED override really is the family of its zone · 0 приложени
  ok    (i) a delivered zone that the table names is APPLIED, never silently skipped
  ok    (i) the unused overrides are named (a signed row that changes nothing today still has to be visible) · Виница-север
  ok    (h) the signed file carries 60 codes · 60
  ok    (h) П2 · every one of the 60 signed codes has a verbatim registry `display` · 60/60
  ok    (h) П2 · all five districts answer in the dictionary (DISTRICT_FALLBACK writes a district code into `quarter`) · asparuhovo · mladost · odesos · primorski · vladislav_varnenchik
  ok    (h) П2 · the named reserve (с.о. Перчемлията → район Приморски) is signed, named and answerable · perchemliyata → primorski
  ok    (c) every `family` is a registry id
  ok    (c) the zone is a display/alias of its own family (освен подписаните изключения)
  ok    (c) no alias comes from another family
  ok    (c) no zone is its own alias
  ok    (d) no alias is address-like (digit , / № ул. бул. roman м.р)
  ok    (d) no alias is on the ghost/typo list
  ok    (d) every skipped string carries a known reason
  ok    (d) every reason is the one the rule gives
  ok    (f) `locations` has exactly the three classes · district · locality · quarter
  ok    (f) every entry is {name: str, aliases: [str]}
  ok    (f) quarter/locality codes are registry ids and carry its verbatim display
  ok    (f) every quarter/locality alias is a verbatim registry string
  ok    (f) no alias comes from another family
  ok    (f) the district book is exactly the five, each answering „район X“
  ok    (f) no code answers as both quarter and locality
  ok    (g) `legacy_by_row` is an object · dict
  ok    (g) every legacy key points inside its bundle · 18 реда · places 150 · hotels 225
  ok    (g) every legacy value is a non-empty list of words
  ok    (g) the bundle SHA that protects the ordinals is current (LF-нормализиран, както го пази git) · hotels · places
  ok    (g) no legacy word is the row's delivered zone

      delivered zones: 32 · matched: 28 · unmatched: 4
      aliases: 48 · skipped strings: 20 in 7 zones
      unmatched: район Аспарухово · район Младост · район Одесос · район Приморски
      signed overrides: 0 applied

passes — every quarter alias is a verbatim string of the registry

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_fire_varna_m6.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json" in C:\git\varna_3d
 exited 1 in 27ms:
=== G-M6: свидетелят, полето и затворените таблици ===

  леджерът, който се съди: lot1v_locations_375_p8a_07.09.json
  ok    НТР пинът се възпроизвежда (222 реда · 219 УИН · 3 дублирани групи)
  ok    пиновете на двете затворени таблици съвпадат в ledger-а и в закованите входове
  ok    G-ISO 1–3: BASE-ът е байт-равен на закованото (7 файла)
        (проверка 4 на G-ISO — прегенерирането — не се повтаря тук: тя е в src/qa_fire_varna_location_isolation.py без --skip-regen)
  ok    затворените таблици са затворени (3 града · 4 канона)
  ok    всяко попълнено поле сочи класифициран свидетел от най-силния ранг
  ok    нито един хотел с курортен НТР етикет не е останал без квартал мълчаливо
  ok    никой подписан ред не се разминава със свидетелите си
  ok    блокът `pending_signature` брои същото, което носят редовете · 8 срещу 8
  ok    чакащите подпис са ТОЧНО подписаните 8 `place_id` · ДАЛИЯ ГАРДЪН · МАГНОЛИЯ 1 И 2 · Маяк · НЕПТУН · РУСАЛКА · Романтика · СТРАНДЖА · Фрегата

ЧАКА ПОДПИС: 8 реда с `pending_signature` — билдът е здрав, но ПУБЛИКАЦИЯ и `--freeze` са забранени, докато Петър не се произнесе:
    ДАЛИЯ ГАРДЪН (hotels) — quarter: REG-TOCity: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка
    МАГНОЛИЯ 1 И 2 (hotels) — quarter: REG-TOCity: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка
    Маяк (hotels) — quarter: REG-TOCity: к.к. Св. Св. Константин и Елена срещу KAIS-quar: с.о. Манастирски рид
    НЕПТУН (hotels) — quarter: REG-TOCity: к.к. Св. Св. Константин и Елена / REG-TOAddress: с.о. Манастирски рид срещу KAIS-quar: кв. Виница
    РУСАЛКА (hotels) — quarter: REG-TOCity: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка
    Романтика (hotels) — quarter: REG-TOAddress: кв. Галата срещу KAIS-quar: с.о. Прибой
    СТРАНДЖА (hotels) — quarter: REG-TOCity: к.к. Златни пясъци / REG-TOAddress: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка
    Фрегата (hotels) — quarter: REG-TOCity: к.к. Св. Св. Константин и Елена / REG-TOAddress: к.к. Св. Св. Константин и Елена срещу KAIS-quar: с.о. Манастирски рид

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_no_cad_ids.py" in C:\git\varna_3d
 succeeded in 1167ms:
=== ПРОВЕРКА: нула кадастрални идентификатори (AGENTS.md, правило 2) ===

  ok  проследените файлове са прочетени · 2139 файла
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

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import subprocess,json
cmd=['python','-B','src/qa_fire_varna_m6.py','--ledger','scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json']
r=subprocess.run(cmd,capture_output=True)
print(json.dumps({'cmd':cmd,'exit_code':r.returncode,'output':r.stdout.decode('utf-8'),'stderr':r.stderr.decode('utf-8')},ensure_ascii=False))
'@ | python -B -" in C:\git\varna_3d
 succeeded in 93ms:
{"cmd": ["python", "-B", "src/qa_fire_varna_m6.py", "--ledger", "scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json"], "exit_code": 3, "output": "=== G-M6: свидетелят, полето и затворените таблици ===\r\n\r\n  леджерът, който се съди: lot1v_locations_375_p8a_07.09.json\r\n  ok    НТР пинът се възпроизвежда (222 реда · 219 УИН · 3 дублирани групи)\r\n  ok    пиновете на двете затворени таблици съвпадат в ledger-а и в закованите входове\r\n  ok    G-ISO 1–3: BASE-ът е байт-равен на закованото (7 файла)\r\n        (проверка 4 на G-ISO — прегенерирането — не се повтаря тук: тя е в src/qa_fire_varna_location_isolation.py без --skip-regen)\r\n  ok    затворените таблици са затворени (3 града · 4 канона)\r\n  ok    всяко попълнено поле сочи класифициран свидетел от най-силния ранг\r\n  ok    нито един хотел с курортен НТР етикет не е останал без квартал мълчаливо\r\n  ok    никой подписан ред не се разминава със свидетелите си\r\n  ok    блокът `pending_signature` брои същото, което носят редовете · 8 срещу 8\r\n  ok    чакащите подпис са ТОЧНО подписаните 8 `place_id` · ДАЛИЯ ГАРДЪН · МАГНОЛИЯ 1 И 2 · Маяк · НЕПТУН · РУСАЛКА · Романтика · СТРАНДЖА · Фрегата\r\n\r\nЧАКА ПОДПИС: 8 реда с `pending_signature` — билдът е здрав, но ПУБЛИКАЦИЯ и `--freeze` са забранени, докато Петър не се произнесе:\r\n    ДАЛИЯ ГАРДЪН (hotels) — quarter: REG-TOCity: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка\r\n    МАГНОЛИЯ 1 И 2 (hotels) — quarter: REG-TOCity: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка\r\n    Маяк (hotels) — quarter: REG-TOCity: к.к. Св. Св. Константин и Елена срещу KAIS-quar: с.о. Манастирски рид\r\n    НЕПТУН (hotels) — quarter: REG-TOCity: к.к. Св. Св. Константин и Елена / REG-TOAddress: с.о. Манастирски рид срещу KAIS-quar: кв. Виница\r\n    РУСАЛКА (hotels) — quarter: REG-TOCity: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка\r\n    Романтика (hotels) — quarter: REG-TOAddress: кв. Галата срещу KAIS-quar: с.о. Прибой\r\n    СТРАНДЖА (hotels) — quarter: REG-TOCity: к.к. Златни пясъци / REG-TOAddress: к.к. Златни пясъци срещу KAIS-quar: к.к. Чайка\r\n    Фрегата (hotels) — quarter: REG-TOCity: к.к. Св. Св. Константин и Елена / REG-TOAddress: к.к. Св. Св. Константин и Елена срещу KAIS-quar: с.о. Манастирски рид\r\n", "stderr": ""}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -l --max-count 20 --max-columns 200 -g '*.md' -g '*.json' -g '*.log' 'qa_fixed_point|place_identity.rekey.run2|run1' scratch/granitsi" in C:\git\varna_3d
 exited 1 in 0ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'rg --files --hidden --no-ignore scratch/granitsi | Select-Object -First 95' in C:\git\varna_3d
 succeeded in 12ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=135; Get-Content -Encoding utf8 -LiteralPath tests/test_quarters_signed_fixtures.py | Select-Object -Skip 135 -First 40 | ForEach-Object { $n++; '"'{0}: {1}' -f "'$n,$_ }; rg -l --max-count 20 --max-columns 200 '"'write_text|write_bytes|rmtree|mkdir|open\\(.*[\"'']w|TemporaryDirectory' tests -g '*.py'" in C:\git\varna_3d
 exited 1 in 23ms:
169:         meta = document["_meta"]
170:         self.assertEqual(meta["artifact_class"], "signed_by_plan_signature")
171:         # Decisions 4: 58 single Wikimapia polygons + 1 union + Младост 2.
172:         self.assertEqual(len(document["features"]), 60)
173:         methods = [f["properties"]["method"] for f in document["features"]]
174:         self.assertEqual(methods.count("street_bounded_face"), 1)
175:         self.assertEqual(methods.count("human_polygon"), 58)

codex
G17, П4, export QA, alias QA и `qa_no_cad_ids` минават; M6 връща точно `3` с очакваните осем pending IDs. Има и две съществени находки: reflog съдържа отменени агентски комити на каноничната самоличност, а `unittest` има setup, който изтрива и пресъздава fixtures в repo-то. Проверявам какво може да се изпълни при read-only ограничението.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_identity_rekey.py --base tests/fixtures/identity_rekey_base_2026-09-07.json --candidate scratch/granitsi/place_identity.rekey.json --candidate2 scratch/granitsi/place_identity.rekey.run2.json --expect-base-sha 1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761; exit "'$LASTEXITCODE' in C:\git\varna_3d
 succeeded in 35ms:
✓ C0 основата е замразената — 1141bbc2f6ff vs 1141bbc2f6ff
✓ C1 еднакви върхови ключове — ['_meta', 'objects', 'retired', 'sites'] vs ['_meta', 'objects', 'retired', 'sites']
✓ C2 броят обекти — основа 375 · кандидат 375 · очаквани 375
✓ C3 нула нови/изчезнали place_id (сравнение ПО place_id) — нови 0 · изчезнали 0
✓ C4 place_id са уникални в кандидата — 0 повторени · 383 проверени id
✓ C5 по обект се мени САМО `key` — 0 чужди промени · 375 реда с нов ключ
✓ C6 в `_meta` се мени само `rule_key` — променени: ['rule_key']
✓ C7 sites непроменен (0 оттеглени без решение) — равен
✓ C7 retired непроменен (0 оттеглени без решение) — равен
✓ C8 всеки ключ е `<файл>|skel(име)`(#N), без зона — 0 счупени · 375 проверени
✓ C9-а стълкновенията са точно очакваните — ['hotels|admiral', 'hotels|perla', 'hotels|roial', 'hotels|rusalka'] vs ['hotels|admiral', 'hotels|perla', 'hotels|roial', 'hotels|rusalka']
✓ C9-б `#N` е по възходящ координатен ранг — 0 разминавания · 8 реда в стълкновение
✓ C9-в всяка двойка се различава по `kais_i` или УИН — 0 слепи
✓ C10 два кандидата байт-еднакви — b72cbe2f6d46 vs b72cbe2f6d46
✓ C11 нула кадастрални идентификатори — чисто

редове с нов ключ: 375 · полета: key 375 · нови/изчезнали id: 0/0 · пренаредени позиции: 26

✓ ПРЕКОДИРАНЕТО ЗЕЛЕНО · 15 проверки

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_fixed_point.py --a scratch/granitsi/fixpoint/places_run1.json --b data/fire_varna_places.json --ignore _meta.generated; exit "'$LASTEXITCODE' in C:\git\varna_3d
 succeeded in 23ms:
  ok    неподвижна точка · places_run1.json ↔ fire_varna_places.json · 128321 байта · махнати ключове: _meta.generated

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_fixed_point.py --a scratch/granitsi/fixpoint/hotels_run1.json --b data/fire_varna_hotels.json --ignore _meta.generated; exit "'$LASTEXITCODE' in C:\git\varna_3d
 succeeded in 7ms:
  ok    неподвижна точка · hotels_run1.json ↔ fire_varna_hotels.json · 151183 байта · махнати ключове: _meta.generated

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; python -B src/qa_fixed_point.py --a scratch/granitsi/fixpoint/ledger_run1.json --b scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json; exit "'$LASTEXITCODE' in C:\git\varna_3d
 succeeded in 51ms:
  ok    неподвижна точка · ledger_run1.json ↔ lot1v_locations_375_p8a_07.09.json · 965388 байта · без изключения (директно сравнение)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); Get-Content -Encoding utf8 -LiteralPath scratch/granitsi/COMMIT_MSG_b2_1_identity.txt,scratch/granitsi/COMMIT_MSG_b2_2_exports.txt,scratch/granitsi/COMMIT_MSG_b2_3_ledger.txt' in C:\git\varna_3d
 succeeded in 0ms:
data: place identity — coordinates from KAIS bodies (Б0 т. 11), re-keyed without the zone (375 place_id unchanged), 57 zones refreshed, inputs pinned, registry manifest accepted (decision 6, 9 rows)

Подписвам по амандамент №3 (решения 1–6): data/place_identity.json SHA256 4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2 (ключ <файл>|skel(име), котви kais_i и УИН, 375/375 place_id непроменени спрямо tests/fixtures/identity_rekey_base_2026-09-07.json, 57 зони освежени само върху редове с празен записан квартал); data/fire_varna_location_inputs.json SHA256 c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee (пиновете, приети с --accept-identity); data/registry_manifest.json SHA256 bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb (девет реда със сменена зонова дума, приети по решение 6).
data: places and hotels exports with quarters from the signed boundaries (P8-а: 57 assigned, 201 written unchanged), quarter_attribution, categories regenerated

Подписвам по нощния план (Б2, Б0 т. 4/5/6/9/12) и амандамент №3: data/fire_varna_places.json SHA256 3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66; data/fire_varna_hotels.json SHA256 eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51; data/place_categories.json SHA256 9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231. Таблица на изходите: 201 записани непроменени (G17), 65 присвоени по полигон (57 написани от SIGNED_POLYGON, 8 честно неписани), 63 в ръба, 41 с пин извън всяка граница, 5 в двойна зона; районна резерва 0. Неподвижна точка: места, хотели и леджер байт-еднакви при повторен прогон.
data: dated ledger lot1v_locations_375_p8a_07.09 (base_rev 8d60aebb, SIGNED_POLYGON and DISTRICT_FALLBACK witnesses in the channels)

Подписвам: scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json SHA256 5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94; _meta.base_rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b; старият леджер lot1v_locations_375.json е непроменен (SHA256 d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075). M6 върху този леджер: нула падания, точно осемте pending_signature реда (ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import pathlib,hashlib,json,subprocess
r=pathlib.Path('.')
a=(r/'scratch/granitsi/fixpoint/ledger_run1.json').read_bytes(); b=subprocess.check_output(['git','cat-file','blob',':scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json'])
print('ledger RAW equality',a==b,'lengths',len(a),len(b),'sha256',hashlib.sha256(a).hexdigest(),hashlib.sha256(b).hexdigest())
print('testfiles',*[str(p) for p in pathlib.Path('tests').glob('test*.py')],sep='\\n')
'@ | python -B -" in C:\git\varna_3d
 succeeded in 40ms:
ledger RAW equality True lengths 965388 965388 sha256 5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94 5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94
testfiles
tests\test_quarters_signed_fixtures.py

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); rg -n --no-ignore --max-count 20 --max-columns 200 '"'write_text|write_bytes|rmtree|mkdir|TemporaryDirectory|NamedTemporaryFile|subprocess.run' tests -g '*.py'; rg -n --max-count 20 --max-columns 200 'read_bytes|normalise\\(' src/qa_fixed_point.py" in C:\git\varna_3d
 succeeded in 0ms:
tests\test_quarters_signed_fixtures.py:125:    return subprocess.run(
tests\test_quarters_signed_fixtures.py:157:            shutil.rmtree(FIXTURES)
tests\test_quarters_signed_fixtures.py:262:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:272:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:284:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:296:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:318:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:330:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:340:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:350:        with tempfile.TemporaryDirectory() as tmp:
tests\test_quarters_signed_fixtures.py:355:        with tempfile.TemporaryDirectory() as tmp:
56:def normalise(path: Path, ignore: list[str]) -> tuple[bytes, list[str]]:
95:    ba, dropped_a = normalise(pa, a.ignore)
96:    bb, dropped_b = normalise(pb, a.ignore)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import sys,runpy
blocked={'shutil.rmtree','os.remove','os.rmdir','os.rename','os.mkdir','os.link','os.symlink','os.truncate'}
def read_only(event,args):
    if event in blocked:
        raise PermissionError('S26 read-only guard: denied '+event)
    if event=='open':
        mode=args[1]
        flags=args[2]
        if (isinstance(mode,str) and any(x in mode for x in 'wax+')) or (isinstance(flags,int) and flags & (1|2|64|512|1024)):
            raise PermissionError('S26 read-only guard: denied writable open')
sys.addaudithook(read_only)
sys.argv=['python -m unittest','discover','-s','tests']
runpy.run_module('unittest',run_name='__main__')
'@ | python -B -; exit "'$LASTEXITCODE' in C:\git\varna_3d
 exited 1 in 53ms:
E
======================================================================
ERROR: setUpClass (test_quarters_signed_fixtures.SignedQuartersFixtures)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\git\varna_3d\tests\test_quarters_signed_fixtures.py", line 157, in setUpClass
    shutil.rmtree(FIXTURES)
  File "C:\Program Files\Python310\lib\shutil.py", line 698, in rmtree
    sys.audit("shutil.rmtree", path)
  File "<stdin>", line 5, in read_only
PermissionError: S26 read-only guard: denied shutil.rmtree

----------------------------------------------------------------------
Ran 0 tests in 0.008s

FAILED (errors=1)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import importlib.util,pathlib,contextlib,io
p=pathlib.Path('src/qa_fixed_point.py'); spec=importlib.util.spec_from_file_location('qfp',p); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
a=pathlib.Path('a.json'); b=pathlib.Path('b.json')
class MemPath:
    def __init__(self,x): self.x=x; self.name=x
    def exists(self): return True
    def read_text(self,encoding=None): return '{\"rows\":[1]}\\n' if self.x=='a' else '{ \"rows\" : [1] }\\n'
    def __str__(self): return self.x
m.Path=MemPath
print('A3 negative probe: raw bytes differ only in whitespace; comparator no --ignore:')
code=m.main(['--a','a','--b','b']); print('actual exit',code,'expected per raw-byte A3=1')
'@ | python -B -" in C:\git\varna_3d
 succeeded in 14ms:
codex
Намерих дефект в `qa_fixed_point.py`: и без `--ignore` той нормализира JSON, макар A3 да изисква директно сравнение на байтовете на ledger-а. Проба само с различни интервали минава погрешно. Реалните два ledger файла са byte-equal; дефектът е в гейта. `unittest` беше спрян от read-only защитата при `rmtree`: exit `1`, изпълнени `0` теста.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=38; Get-Content -Encoding utf8 -LiteralPath data/fire_varna_location_inputs.json | Select-Object -Skip 38 -First 75 | ForEach-Object { $n++; '"'{0}: {1}' -f "'$n,$_ }; rg -n --max-count 20 --max-columns 200 '"'PENDING|EXPECTED|pending_ids|place_id' src/qa_fire_varna_m6.py" in C:\git\varna_3d
 succeeded in 28ms:
48:  },
49:  "inputs": {
50:   "data/place_identity.json": {
51:    "sha256": "4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2",
52:    "bytes": 228980
53:   },
54:   "data/registry_manifest.json": {
55:    "sha256": "bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb",
56:    "bytes": 142309
57:   },
58:   "web/varna_buildings_info.json": {
59:    "sha256": "f7ee3e072ee1d51f831f7067058e962e558f1c9daa8660ed4dcac6f6df27df20",
60:    "bytes": 3567341
61:   },
62:   "web/varna_buildings_3d.geojson": {
63:    "sha256": "d0c8336061601cdeba2d2905a19187bb052a4aae3f539797e7525bc1651ed1dc",
64:    "bytes": 29947902
65:   },
66:   "data/quarters_signed.geojson": {
67:    "sha256": "c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3",
68:    "bytes": 301917
69:   }
70:  },
71:  "registry": {
72:   "path": "C:/git/Varna_buildings/config/quarter_registry.json",
73:   "sha256": "7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6",
74:   "bytes": 52299,
75:   "entries": 84
76:  },
77:  "ntr": {
78:   "path": "scratch/refactor/_addr/ntr_hoteli_raw.json",
79:   "sha256": "3e6828ba4125dc6295cb16a88948fe6c58a2f348a31e9dd57d3114eab32e06ee",
80:   "bytes": 109764,
81:   "fetched": "2026-08-21 06:30:44",
82:   "rows": 222,
83:   "uins": 219,
84:   "dup_groups": 3
85:  },
86:  "quarters_signed": {
87:   "path": "data/quarters_signed.geojson",
88:   "sha256": "c1551d248e6450025664a4338cf7cb8a7e84e8275eba2ffd53b4a41990e871b3",
89:   "bytes": 301917,
90:   "features": 60,
91:   "commit": "6486b48 (Petar1984 — D16/G4: геометрията е негов комит)",
92:   "artifact_class": "signed_by_plan_signature",
93:   "decisions_sha256": "74f09d505e2b6b6a5ba0e5164d85f6e2e693f103b66d8cd46e1c22b56320726b"
94:  },
95:  "ledger": {
96:   "path": "scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json",
97:   "base_rev": "8d60aebb365fb8e74ccc863d3b3db90b74180a3b",
98:   "base_path": "scratch/refactor/_addr/lot1v_locations_375.json",
99:   "base_blob_sha256": "d5050f1cfb3d4289e62a288b64a4658b15106a7876f7aa8fb1d1a39980c76075",
100:   "rule": "старият леджер е базата на D18/G17 и остава непокътнат"
101:  },
102:  "m6_tables": {
103:   "NTR_CITY": "dcd300f4ed05174fcc9430c25a86ff0e4d856e2b8e44e3961427121937e46dec",
104:   "KAIS_ADDR_ABBREV": "ae443fb868d6731eebd334390b2d54babbf2c3613639275626936a8da390f8c3"
105:  },
106:  "kais_generation": {
107:   "generation": "2407",
108:   "published": "24.07.2026",
109:   "fetched": "2026-08-07 01:43:10",
110:   "phase0_quoted": "12.05.2026",
111:   "verdict": "поколението 24.07.2026 е ПО-НОВО от обновата, която ФАЗА_0 цитира (ZIP 12.05.2026) → пресваляне не се налага по критерия на К6-3. Дали КАИС е публикувал НОВА извадка след 24.07 не се проверява оттук: това е мрежова заявка, а мярката не гадае.",
112:   "expected_buildings": 80497,
113:   "source": "https://kais.cadastre.bg/bg/OpenData/Download"
41:  * приемането на `pending_signature` сравнява ТОЧНИТЕ осем `place_id`, не броя.
93:# `place_id`, защото името не е ключ.  Един ред повече или по-малко е промяна
95:PENDING_EXPECTED = {
494:    got_ids = {r["place_id"] for r in pending}
495:    surplus = sorted(got_ids - set(PENDING_EXPECTED))
496:    missing = sorted(f"{PENDING_EXPECTED[i]} ({i[:8]}…)"
497:                     for i in set(PENDING_EXPECTED) - got_ids)
499:          f"чакащите подпис са ТОЧНО подписаните {len(PENDING_EXPECTED)} "
500:          f"`place_id`",
503:          or " · ".join(sorted(PENDING_EXPECTED.values())))

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'; "'$env:PYTHONIOENCODING='"'utf-8'; @'
import json,subprocess,hashlib,pathlib
p=subprocess.check_output(['git','diff','--cached','--name-only','-z']).decode().split('\\0'); print('HEAD',subprocess.check_output(['git','rev-parse','HEAD']).decode().strip())
for f in filter(None,p):
 b=subprocess.check_output(['git','cat-file','blob',':'+f]); print(f,hashlib.sha256(b).hexdigest(),len(b))
print('unstaged tracked',subprocess.check_output(['git','diff','--name-only']).decode().strip())
'@ | python -B -" in C:\git\varna_3d
 succeeded in 135ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
HEAD 1217dc494ebd1ce16f1cbd90e73f202dec206b1e
data/fire_varna_hotels.json eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51 151263
data/fire_varna_location_inputs.json c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee 65111
data/fire_varna_places.json 3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66 128401
data/place_categories.json 9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231 77998
data/place_identity.json 4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2 228980
data/registry_manifest.json bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb 142309
scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json 5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94 965388
unstaged tracked scratch/place_bodies/qa_place_bodies.md

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git var GIT_AUTHOR_IDENT; git var GIT_COMMITTER_IDENT; git --no-optional-locks diff --exit-code -- data/place_identity.json data/fire_varna_location_inputs.json data/registry_manifest.json data/fire_varna_places.json data/fire_varna_hotels.json data/place_categories.json scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json; exit $LASTEXITCODE' in C:\git\varna_3d
 succeeded in 0ms:
Petar1984 <petar.dikov2019@gmail.com> 1788751978 +0300
Petar1984 <petar.dikov2019@gmail.com> 1788751978 +0300

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$OutputEncoding = [Console]::OutputEncoding = [Text.UTF8Encoding]::new(); $n=89; Get-Content -Encoding utf8 -LiteralPath src/qa_fire_varna_m6.py | Select-Object -Skip 89 -First 23 | ForEach-Object { $n++; '"'{0}: {1}' -f "'$n,$_ }; $n=300; Get-Content -Encoding utf8 -LiteralPath src/qa_identity_rekey.py | Select-Object -Skip 300 -First 42 | ForEach-Object { $n++; '"'{0}: {1}' -f "'$n,$_ }' in C:\git\varna_3d
 succeeded in 20ms:
90:              "mladost": "Младост", "asparuhovo": "Аспарухово",
91:              "vladislav_varnenchik": "Владислав Варненчик"}
92: # A6: приемането сравнява ТОЧНИТЕ осем реда, които чакат подписа на Петър — по
93: # `place_id`, защото името не е ключ.  Един ред повече или по-малко е промяна
94: # на въпроса, който му е зададен, и спира приемането.
95: PENDING_EXPECTED = {
96:     "8d6c4ffb-0dee-42c2-944b-3f90ff94008c": "ДАЛИЯ ГАРДЪН",
97:     "0e0cdbf1-e6b7-4ee7-993c-6f02cefc388a": "МАГНОЛИЯ 1 И 2",
98:     "7d446deb-64ff-4d19-89c4-6d9bf3c2548b": "Маяк",
99:     "47d2444b-42bb-43a4-98bc-e051e4d146ea": "НЕПТУН",
100:     "6f3e5127-70a4-42ed-a0f8-b89936985d75": "РУСАЛКА",
101:     "201cb44f-904e-4093-8a6b-056d2d09b47a": "Романтика",
102:     "459ad12b-561c-4644-8ab1-8b86a80d21be": "СТРАНДЖА",
103:     "081a7edc-6db9-4ed7-9f98-3762aec7e7f9": "Фрегата",
104: }
105: SIGNED_SRC = "SIGNED_OVERRIDE"
106: SIGNED_CODE = "zlatni_pyasatsi"
107: SIGNED_NAMES = {"ЕЛЕНА", "НИМФА", "ВИВА КЛУБ", "ПЛИСКА", "Вихрен", "ПРЕСЛАВ",
108:                 "ХОЛИДЕЙ ПАРК", "Империя", "ГРАДИНА", "ДОЛЧЕ ВИТА",
109:                 "ЛОТОС/LOTOS", "ОАЗИС/OAZIS"}
110: # The resort labels НТР may hand out: a hotel that carries one and still has no
111: # quarter has lost it somewhere between the witness and the field.
112: RESORT_CODES = {"zlatni_pyasatsi", "kk_konstantin_elena"}
301:         sha2 = sha256(Path(a.candidate2))
302:         g.check("C10 два кандидата байт-еднакви", cand_sha == sha2,
303:                 f"{cand_sha[:12]} vs {sha2[:12]}")
304:     else:
305:         g.check("C10 два кандидата байт-еднакви", False, "липсва --candidate2")
306: 
307:     # --- C11: поверителност ---------------------------------------------------
308:     text = cand_p.read_text(encoding="utf-8")
309:     hit = CAD.search(text)
310:     g.check("C11 нула кадастрални идентификатори",
311:             hit is None and "10135" not in text,
312:             hit.group(0) if hit else ("префиксът 10135" if "10135" in text
313:                                       else "чисто"))
314: 
315:     order_base = [o["place_id"] for o in base.get("objects") or []]
316:     order_cand = [o["place_id"] for o in cand.get("objects") or []]
317:     reordered = sum(1 for x, y in zip(order_base, order_cand) if x != y)
318:     summary = {
319:         "base": str(base_p).replace("\\", "/"), "base_sha256": sha256(base_p),
320:         "candidate": str(cand_p).replace("\\", "/"), "candidate_sha256": cand_sha,
321:         "candidate2_sha256": sha256(Path(a.candidate2)) if a.candidate2 else None,
322:         "rows_base": len(base.get("objects") or []),
323:         "rows_candidate": len(cand.get("objects") or []),
324:         "place_id_added": added, "place_id_removed": removed,
325:         "rows_changed": len(rows),
326:         "changed_fields": dict(sorted(changed_fields.items())),
327:         "meta_changed": meta_diff,
328:         "positions_reordered": reordered,
329:         "collisions": coll_rows,
330:         "checks": [{"name": n, "ok": ok, "detail": d} for n, ok, d in g.checks],
331:         "verdict": "green" if not g.fails else "red",
332:     }
333:     if a.review:
334:         doc = {
335:             "_meta": {
336:                 "what": "прекодиране на самоличността: ключ без зоната "
337:                         "(амандамент №3, път А)",
338:                 "lot": "Б2-R1",
339:                 "gate": "python src/qa_identity_rekey.py",
340:                 "rule": "мени се само `key` на обектите и `_meta.rule_key`; "
341:                         "375/375 place_id непроменени; обектите се сравняват "
342:                         "по place_id, не по ред; два прогона байт-еднакви",

codex
**НЕГОДНО за комит сега.** Staged данните издържат проверките, но гейтът за неподвижната точка нарушава A3, а пълният `unittest` набор не е потвърден в тази read-only сесия. HEAD остана `1217dc494ebd1ce16f1cbd90e73f202dec206b1e`; index не е променян.

**Блокерът:** [qa_fixed_point.py:95](C:/git/varna_3d/src/qa_fixed_point.py:95) нормализира JSON и без `--ignore`. Проба с различни сурови байтове, но еднакъв JSON, връща `0`; [A3:100](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:100) изисква директно byte comparison за ledger-а. Реалните ledger файлове са byte-equal; това не отстранява false-pass дефекта на гейта.

Проверени са всичките **17 комита** след `6486b48`. Шестте пълни съобщения съвпадат дословно с [§3:32](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:32). Първите 16 имат author **и committer** `Claude Executor <executor@local>`; последният — `Claude Architect <architect@local>`.

| SHA | Проверен write-set и основание |
|---|---|
| `3de6661` | `qa_identity_refresh.py`; предходен Б2-0а, State:42 |
| `5c6fdd0` | `place_identity.py`, `qa_place_identity_coords.py`; Б2-0, State:43 |
| `da77ff2` | `fire_varna_locations.py`, `qa_p8a.py`; първият Б2, изрично запазен, State:44 |
| `0ecd814` | categories builder, двата exporters и двата export QA; същият предходен Б2 |
| `a28edc2` | `place_identity.py`, `place_addresses.py`; **§3/1, дословно** |
| `8a60972` | `qa_identity_rekey.py`; **§3/2, дословно** |
| `7bac5e5` | `qa_identity_refresh.py`; **§3/3, дословно** |
| `bb09535` | `fire_varna_locations.py`; **§3/6, дословно**; ранното изпълнение съответства на A1/A7 |
| `4bdcc7c` | rekey/refresh negative harnesses и rekey QA; довършва §3/2–3 |
| `36e8513` | двата harnesses, двата identity QA, замразената fixture; §3/2, A2/A7 |
| `679451d` | `fire_varna_locations.py`; **§3/4, дословно**, A6 |
| `2624218` | `qa_fire_varna_m6.py`; **§3/5, дословно**, A6 |
| `822656d` | comparator и negatives; A3, с установения дефект |
| `bd00c2c` | categories builder, `zone_alias_overrides.json`; решение 5/П3 |
| `0c1ed71` | alias QA и negatives; П2 |
| `26da605` | P8-а QA и negatives; П4 |
| `1217dc4` | само `.gitignore`; изключението на [ред 238](C:/git/varna_3d/.gitignore:238) |

Допълнителните изпълнителски комити са обосновани от подписаните условия; отделните им съобщения не са предписани дословно. `.gitignore` остава ограничено процедурно отклонение извън write-set-а, отчетено в [State:53](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:53).

**Исторически твърдението „няма agent canonical-data commits“ е невярно:** `58c75ed6` и `85ef6368` съдържат `place_identity.json`, SHA256 `1141bbc2…`, от Executor. Последващите resets са записани като Petar1984 ([reflog:78](C:/git/varna_3d/.git/logs/HEAD:78), [reflog:85](C:/git/varna_3d/.git/logs/HEAD:85)). Те и `95414d3`/`85bb4fd` нямат съдържащи refs; обикновен branch push не ги включва. Текущата ancestry няма комити на седемте canonical payloads.

Реално измерените QA резултати са:

| Команда/проверка | Exit |
|---|---:|
| `python -B src/qa_p8a.py` | 0 |
| `python -B src/qa_fire_varna_places_export.py` | 0 |
| `python -B src/qa_place_zone_aliases.py` | 0 |
| `python -B src/qa_no_cad_ids.py` | 0 |
| `qa_fixed_point.py` — трите сравнения | 0/0/0 |
| `qa_identity_rekey.py` — документираните аргументи | 0 |
| `qa_fire_varna_m6.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` | **3**, fails **0** |
| `unittest discover -s tests`, под read-only защита | **1**, 0 tests, setup ERROR |

Rekey използва fixture `tests/fixtures/identity_rekey_base_2026-09-07.json`, двата `scratch/granitsi/place_identity.rekey{,.run2}.json` кандидата и очакван SHA `1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761`, съгласно [докстринга:17](C:/git/varna_3d/src/qa_identity_rekey.py:17). Fixed-point сравнява `scratch/granitsi/fixpoint/{places,hotels,ledger}_run1.json` с окончателните файлове; само exports ползват `--ignore _meta.generated`.

M6 потвърди точно осемте IDs от [PENDING_EXPECTED:95](C:/git/varna_3d/src/qa_fire_varna_m6.py:95): ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата.

`unittest` setup опитва `shutil.rmtree(FIXTURES)` ([test:157](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:157)); защитата го спря преди промяна. Това е ограничение на изпълнението, не доказан дефект на тестовете. Нужен е успешен прогон в разрешено изолирано копие.

Независимата проверка на данните потвърди:

- **G17: 201/201** quarter JSON tokens byte-equal срещу `8d60aebb:…/lot1v_locations_375.json`, SHA `d5050f1c…`.
- **П4: 57 = 42 places + 15 hotels**, всички сред 174 празни квартала; нула върху написаните.
- **375/375 place_id** срещу fixture; само `key×375`, `zone×57`, `_meta.rule_key`; координатите, `sites` и осемте retired са запазени.
- Manifest: само **9 zone стойности = 3 grandfathered + 6 board_queue**, по решение 6.
- [Inputs:51](C:/git/varna_3d/data/fire_varna_location_inputs.json:51) и [:55](C:/git/varna_3d/data/fire_varna_location_inputs.json:55) пинват staged identity/manifest. [:96](C:/git/varna_3d/data/fire_varna_location_inputs.json:96) сочи новия ledger; [:99](C:/git/varna_3d/data/fire_varna_location_inputs.json:99) съдържа SHA на **базовия** ledger. Собственият нов SHA не е поле в този договор.
- Двата реални ledger файла са директно byte-equal: **965388 B**, `5ec64c68…`.

След поправката и зелените гейтове трите комита на Петър трябва да използват следните message-file текстове, в реда на [§6/A7](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:104):

```text
data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned

57 identity zones refreshed; registry manifest accepted and pinned (decision 6: 9 zone rows, 3 grandfathered + 6 board_queue).
```

```text
data: places and hotels with quarter by signed polygon, search dictionary regenerated
```

```text
data: p8a quarter assignment ledger 07.09
```

Готовите `COMMIT_MSG_b2_2_exports.txt` и `COMMIT_MSG_b2_3_ledger.txt` съдържат парафрази; трябва да получат горните дословни текстове. Командите са:

```bash
git commit -F scratch/granitsi/COMMIT_MSG_b2_1_identity.txt -- data/place_identity.json data/fire_varna_location_inputs.json data/registry_manifest.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_2_exports.txt -- data/fire_varna_places.json data/fire_varna_hotels.json data/place_categories.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_3_ledger.txt -- scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json
```

**Механична уговорка:** `git commit -- paths` взема избраните **worktree contents**, като изключва останалите staged файлове. Затова непосредствено преди всеки комит: `git diff --exit-code -- <същите paths>` трябва да е `0`, плюс за всеки path **в Git Bash**:

```bash
git cat-file blob :path | sha256sum
```

Проверените index SHA256 са:

| Файл | SHA256 |
|---|---|
| identity | `4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2` |
| inputs | `c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee` |
| places | `3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66` |
| hotels | `eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51` |
| categories | `9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231` |
| manifest | `bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb` |
| ledger | `5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94` |

Hotels/categories имат CRLF в worktree, но LF-normalized bytes съвпадат с index; текущият `git diff` е `0`.

За последващата публикация: [ledger:6](C:/git/varna_3d/scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:6) изрично е **частен**; `qa_no_cad_ids=0` не разрешава публичност на целия repo. Repo `.gitignore:79` освобождава `scratch/refactor/`; ignored-path твърдението не се потвърди, а глобалният ignore е недостъпен. Dirty `qa_place_bodies.md` остава извън трите комита: `2633e165…`, 153+/153−; възстановяване/регенериране решава Петър по [State:49](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:49).
tokens used
78,798
**НЕГОДНО за комит сега.** Staged данните издържат проверките, но гейтът за неподвижната точка нарушава A3, а пълният `unittest` набор не е потвърден в тази read-only сесия. HEAD остана `1217dc494ebd1ce16f1cbd90e73f202dec206b1e`; index не е променян.

**Блокерът:** [qa_fixed_point.py:95](C:/git/varna_3d/src/qa_fixed_point.py:95) нормализира JSON и без `--ignore`. Проба с различни сурови байтове, но еднакъв JSON, връща `0`; [A3:100](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:100) изисква директно byte comparison за ledger-а. Реалните ledger файлове са byte-equal; това не отстранява false-pass дефекта на гейта.

Проверени са всичките **17 комита** след `6486b48`. Шестте пълни съобщения съвпадат дословно с [§3:32](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:32). Първите 16 имат author **и committer** `Claude Executor <executor@local>`; последният — `Claude Architect <architect@local>`.

| SHA | Проверен write-set и основание |
|---|---|
| `3de6661` | `qa_identity_refresh.py`; предходен Б2-0а, State:42 |
| `5c6fdd0` | `place_identity.py`, `qa_place_identity_coords.py`; Б2-0, State:43 |
| `da77ff2` | `fire_varna_locations.py`, `qa_p8a.py`; първият Б2, изрично запазен, State:44 |
| `0ecd814` | categories builder, двата exporters и двата export QA; същият предходен Б2 |
| `a28edc2` | `place_identity.py`, `place_addresses.py`; **§3/1, дословно** |
| `8a60972` | `qa_identity_rekey.py`; **§3/2, дословно** |
| `7bac5e5` | `qa_identity_refresh.py`; **§3/3, дословно** |
| `bb09535` | `fire_varna_locations.py`; **§3/6, дословно**; ранното изпълнение съответства на A1/A7 |
| `4bdcc7c` | rekey/refresh negative harnesses и rekey QA; довършва §3/2–3 |
| `36e8513` | двата harnesses, двата identity QA, замразената fixture; §3/2, A2/A7 |
| `679451d` | `fire_varna_locations.py`; **§3/4, дословно**, A6 |
| `2624218` | `qa_fire_varna_m6.py`; **§3/5, дословно**, A6 |
| `822656d` | comparator и negatives; A3, с установения дефект |
| `bd00c2c` | categories builder, `zone_alias_overrides.json`; решение 5/П3 |
| `0c1ed71` | alias QA и negatives; П2 |
| `26da605` | P8-а QA и negatives; П4 |
| `1217dc4` | само `.gitignore`; изключението на [ред 238](C:/git/varna_3d/.gitignore:238) |

Допълнителните изпълнителски комити са обосновани от подписаните условия; отделните им съобщения не са предписани дословно. `.gitignore` остава ограничено процедурно отклонение извън write-set-а, отчетено в [State:53](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:53).

**Исторически твърдението „няма agent canonical-data commits“ е невярно:** `58c75ed6` и `85ef6368` съдържат `place_identity.json`, SHA256 `1141bbc2…`, от Executor. Последващите resets са записани като Petar1984 ([reflog:78](C:/git/varna_3d/.git/logs/HEAD:78), [reflog:85](C:/git/varna_3d/.git/logs/HEAD:85)). Те и `95414d3`/`85bb4fd` нямат съдържащи refs; обикновен branch push не ги включва. Текущата ancestry няма комити на седемте canonical payloads.

Реално измерените QA резултати са:

| Команда/проверка | Exit |
|---|---:|
| `python -B src/qa_p8a.py` | 0 |
| `python -B src/qa_fire_varna_places_export.py` | 0 |
| `python -B src/qa_place_zone_aliases.py` | 0 |
| `python -B src/qa_no_cad_ids.py` | 0 |
| `qa_fixed_point.py` — трите сравнения | 0/0/0 |
| `qa_identity_rekey.py` — документираните аргументи | 0 |
| `qa_fire_varna_m6.py --ledger scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json` | **3**, fails **0** |
| `unittest discover -s tests`, под read-only защита | **1**, 0 tests, setup ERROR |

Rekey използва fixture `tests/fixtures/identity_rekey_base_2026-09-07.json`, двата `scratch/granitsi/place_identity.rekey{,.run2}.json` кандидата и очакван SHA `1141bbc2f6ffd8795155728798132f0aff2e79ac53dd8aa4b9285c95b0bd9761`, съгласно [докстринга:17](C:/git/varna_3d/src/qa_identity_rekey.py:17). Fixed-point сравнява `scratch/granitsi/fixpoint/{places,hotels,ledger}_run1.json` с окончателните файлове; само exports ползват `--ignore _meta.generated`.

M6 потвърди точно осемте IDs от [PENDING_EXPECTED:95](C:/git/varna_3d/src/qa_fire_varna_m6.py:95): ДАЛИЯ ГАРДЪН, МАГНОЛИЯ 1 И 2, Маяк, НЕПТУН, РУСАЛКА, Романтика, СТРАНДЖА, Фрегата.

`unittest` setup опитва `shutil.rmtree(FIXTURES)` ([test:157](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:157)); защитата го спря преди промяна. Това е ограничение на изпълнението, не доказан дефект на тестовете. Нужен е успешен прогон в разрешено изолирано копие.

Независимата проверка на данните потвърди:

- **G17: 201/201** quarter JSON tokens byte-equal срещу `8d60aebb:…/lot1v_locations_375.json`, SHA `d5050f1c…`.
- **П4: 57 = 42 places + 15 hotels**, всички сред 174 празни квартала; нула върху написаните.
- **375/375 place_id** срещу fixture; само `key×375`, `zone×57`, `_meta.rule_key`; координатите, `sites` и осемте retired са запазени.
- Manifest: само **9 zone стойности = 3 grandfathered + 6 board_queue**, по решение 6.
- [Inputs:51](C:/git/varna_3d/data/fire_varna_location_inputs.json:51) и [:55](C:/git/varna_3d/data/fire_varna_location_inputs.json:55) пинват staged identity/manifest. [:96](C:/git/varna_3d/data/fire_varna_location_inputs.json:96) сочи новия ledger; [:99](C:/git/varna_3d/data/fire_varna_location_inputs.json:99) съдържа SHA на **базовия** ledger. Собственият нов SHA не е поле в този договор.
- Двата реални ledger файла са директно byte-equal: **965388 B**, `5ec64c68…`.

След поправката и зелените гейтове трите комита на Петър трябва да използват следните message-file текстове, в реда на [§6/A7](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_амандамент_3_07.09.md:104):

```text
data: place coordinates from KAIS bodies (Б0 т. 11) and identity re-keyed without the zone (375 place_id unchanged), inputs pinned

57 identity zones refreshed; registry manifest accepted and pinned (decision 6: 9 zone rows, 3 grandfathered + 6 board_queue).
```

```text
data: places and hotels with quarter by signed polygon, search dictionary regenerated
```

```text
data: p8a quarter assignment ledger 07.09
```

Готовите `COMMIT_MSG_b2_2_exports.txt` и `COMMIT_MSG_b2_3_ledger.txt` съдържат парафрази; трябва да получат горните дословни текстове. Командите са:

```bash
git commit -F scratch/granitsi/COMMIT_MSG_b2_1_identity.txt -- data/place_identity.json data/fire_varna_location_inputs.json data/registry_manifest.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_2_exports.txt -- data/fire_varna_places.json data/fire_varna_hotels.json data/place_categories.json
git commit -F scratch/granitsi/COMMIT_MSG_b2_3_ledger.txt -- scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json
```

**Механична уговорка:** `git commit -- paths` взема избраните **worktree contents**, като изключва останалите staged файлове. Затова непосредствено преди всеки комит: `git diff --exit-code -- <същите paths>` трябва да е `0`, плюс за всеки path **в Git Bash**:

```bash
git cat-file blob :path | sha256sum
```

Проверените index SHA256 са:

| Файл | SHA256 |
|---|---|
| identity | `4819ab3e1d74f516de051b5f05abf4721c6f8c42cf2c5c2a293ba95eedc7d0c2` |
| inputs | `c7450ded1b8ade5bdb3b63924971d2be0d9b9ea1a792175df0331526ed4679ee` |
| places | `3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66` |
| hotels | `eb8fa85cbb67265ad99cacbf12a7f9ccb84bb5431b27b6446837318e1ccfee51` |
| categories | `9064705a06477c1a89079616ba7545ca8f51b08220a90b9cad9a915ec232b231` |
| manifest | `bb04640e9762a12a5028b99ee70b1053687cfa4ed55b6e7e2f4c2e191b114abb` |
| ledger | `5ec64c682a46463c1f4890510736a13a5766ada61fcc757af281f6c82d3a7d94` |

Hotels/categories имат CRLF в worktree, но LF-normalized bytes съвпадат с index; текущият `git diff` е `0`.

За последващата публикация: [ledger:6](C:/git/varna_3d/scratch/refactor/_addr/lot1v_locations_375_p8a_07.09.json:6) изрично е **частен**; `qa_no_cad_ids=0` не разрешава публичност на целия repo. Repo `.gitignore:79` освобождава `scratch/refactor/`; ignored-path твърдението не се потвърди, а глобалният ignore е недостъпен. Dirty `qa_place_bodies.md` остава извън трите комита: `2633e165…`, 153+/153−; възстановяване/регенериране решава Петър по [State:49](C:/git/Fire_Varna/docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md:49).
