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
session id: 01a0786b-58a5-7fa1-bece-f1106e8bee44
--------
user
S23 — REVIEW (lens MECHANICS) of lot Б1 second run (07.09) in C:/git/varna_3d (private, branch rezhimi; read-only): commits 63d077d ('build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)') and 8c262e9 ('gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)'), the STAGED uncommitted data/quarters_signed.geojson (60 Features: 58 wikimapia + 1 wikimapia_union dobreva from wm_ids [5729380, 5729421] + 1 declared_streets mladost2; sha256 4930f2043438edb9…, 295 304 B), src/build_quarters_signed.py, src/qa_quarters_signed.py, tests/test_quarters_signed_fixtures.py. Inputs: C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json (blob 2c650160… in Fire_Varna commit 895e0d2, author Claude Architect), the signed plan C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md (Б0 т. 1–12; §Б1 still says 61 Features / decisions 3). Your own F2 asked for the exact plan pin and a spatial district check — verify both fixes and their negatives (run: python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna; python -m unittest tests.test_quarters_signed_fixtures; the fixture files under tests/fixtures or the paths the test names). The per-lot auditor found (all minor): signature chain reaches decisions 3, not 4 (Petar has not signed decisions 4 by sha); C18 imports district_of/load_our_districts from the builder itself and reads the same layer (C:/git/m6000_private/number_viewer/quarters_layer.geojson) — not independent; the АГКК witness disagrees for vazrazhdane4 and kochmar (ours: vladislav_varnenchik; АГКК: 10135-03); the union pin d6f367bd… reproduces only through EPSG:4326→32635→4326 with shapely 2.1.2/pyproj 3.6.1 (degree-space union gives bc92a76c…); .gitignore:26 comment still says 61; §Б1 text drift. Questions: (1) Are the two commits exactly within the Б1 write-set of the plan, with exact messages/author, nothing else touched (git show --stat), hard limits intact (no push; registry untouched; ledger/identity/exports sha unchanged)? (2) Is the union construction deterministic and honestly pinned — should the artefact pin the DEGREE-space union instead (library-independent) or pin both, and what negative fixture proves the choice? (3) Is C18 acceptable as a gate if it shares code with the builder — propose the minimal independent check (e.g. point-in-polygon against agkk_au5 with a signed crosswalk of the 5 codes) and say what to do with the 2 disagreeing codes. (4) What exactly must Petar sign/commit now, in which order, for the chain decisions → artefact to be honest (decisions 4 by sha; the geometry commit message; the .gitignore comment)? Verdict ГОДНО/НЕГОДНО for Б1 second run with named fixes; at most 1200 words; Bulgarian with English identifiers; cite file:line and shas.
warning: Skill descriptions were shortened to fit the skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
codex
Ще проверя read-only двата commit-а, staged артефакта и връзката им с подписания план, после ще изпълня QA и fixture тестовете. Ще използвам skill `engineering:code-review` и ще отделя независим преглед на union pin-а и C18.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/git/Varna_buildings/scratch/hydrant_map_integration_frame.md'" in C:\git
 succeeded in 41ms:
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Content -LiteralPath 'C:/Users/Petar/.codex/plugins/cache/claude-cowork/engineering/1.2.0/skills/code-review/SKILL.md'" in C:\git
 succeeded in 16ms:
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
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "Get-Location
rg --files -g AGENTS.md -g CLAUDE.md -g '*S23*' -g '*S22*' C:/git/varna_3d C:/git/Fire_Varna C:/git/Varna_buildings" in C:\git
 succeeded in 36ms:

C:/git/Fire_Varna\CLAUDE.md
C:/git/Fire_Varna\AGENTS.md
C:/git/varna_3d\CLAUDE.md
C:/git/varna_3d\AGENTS.md
C:/git/Fire_Varna\scratch\places_search\granitsi_night_astra_S22_review_07.09.md
C:/git/Fire_Varna\scratch\places_search\granitsi_b1v2_astra_S23_07.09.md
C:/git/Varna_buildings\AGENTS.md
C:/git/Varna_buildings\CLAUDE.md
Path  
----  
C:\git



exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -Encoding UTF8 -LiteralPath C:/git/varna_3d/AGENTS.md,C:/git/varna_3d/CLAUDE.md,C:/git/Fire_Varna/AGENTS.md,C:/git/Fire_Varna/CLAUDE.md' in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git status --porcelain=v2 --branch
git show --stat --format=fuller 63d077d
git show --stat --format=fuller 8c262e9
git diff --cached --stat
git log -6 --format='%H %s'" in C:\git\varna_3d
 succeeded in 70ms:
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

 succeeded in 108ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
# branch.oid 8c262e9b272aceeb16d4f21503bd4ac92361f1e9
# branch.head rezhimi
# branch.upstream origin/rezhimi
# branch.ab +49 -0
1 A. N... 000000 100644 100644 0000000000000000000000000000000000000000 0fcd88b768d127194d0fa22be76f0822e2deccac data/quarters_signed.geojson
1 .M N... 100644 100644 100644 50698ef3ae628a1fe4cf46ecb4f04332d0252071 50698ef3ae628a1fe4cf46ecb4f04332d0252071 scratch/place_bodies/qa_place_bodies.md
? docs/sessions/ПРОМПТ_20.08.md
? scratch/refactor/_addr/_measure_pal13.py
? scratch/refactor/_addr/_measure_tu_campus.py
? scratch/refactor/_addr/f0b_join_375.json
? scratch/refactor/_addr/f0b_join_375_pass2.json
? scratch/refactor/_addr/kimi_атака_имена_бунгала.txt
? scratch/refactor/_addr/kimi_атака_планове.txt
? scratch/refactor/_addr/kimi_атака_смяна2.txt
? scratch/refactor/_addr/osm_poi_varna.md
? scratch/refactor/_addr/post_codes_all_2018.pdf
? scratch/refactor/_addr/post_codes_varna_2018.json
? scratch/refactor/_addr/БОРД_противоречия.md
? scratch/refactor/_addr/БОРД_част_от_сграда.md
? scratch/refactor/_addr/МЯРКА_курорти_повторно.md
? scratch/refactor/_addr/МЯРКА_хотели.md
? scratch/refactor/_addr/ОТЧЕТ_A1_05.09.md
? scratch/refactor/_addr/ОТЧЕТ_P7_05.09.md
? scratch/refactor/_addr/ОТЧЕТ_P7e_05.09.md
? scratch/refactor/_addr/ПОДГОТОВКА_адреси.md
? scratch/refactor/_addr/РАЗСЛЕДВАНЕ_адрес.md
? scratch/refactor/_addr/СВЕРКА_живата_карта.md
? scratch/refactor/_addr/Т7_недовършено_19.08.patch
? scratch/refactor/_pubbldg/func/extras_log.txt
? scratch/refactor/_pubbldg/func/run_log.txt
? scratch/refactor/_pubbldg/join/check_log.txt
? scratch/refactor/_pubbldg/join/extras_log.txt
? scratch/refactor/_pubbldg/join/run_log.txt
? scratch/refactor/_pubbldg/join/sample.json
? scratch/refactor/_pubbldg/plan/kimi_plan_stderr.log
? scratch/refactor/_pubbldg/plan/sol_plan_stderr.log
? scratch/refactor/_pubbldg/plots/plots_by_class.json
? scratch/refactor/_pubbldg/plots/plots_pooled.json
? scratch/refactor/_pubbldg/plots/run_log.txt
? scratch/refactor/_pubbldg/sources/check_log.txt
? scratch/refactor/_pubbldg/sources/measure_osm_log.txt
? scratch/refactor/_pubbldg/sources/measure_outside_log.txt
? scratch/refactor/_pubbldg/sources/measure_sources_log.txt
? scratch/refactor/_pubbldg/sources/name_channels.json
? scratch/refactor/_pubbldg/sources/osm_named_features.json
? scratch/refactor/_pubbldg/verify/kimi_stderr.log
? scratch/refactor/_pubbldg/verify/sol_stderr.log
commit 63d077d6f717ccb44b8cdc435969d60b13ec8865
Author:     Claude Executor <executor@local>
AuthorDate: Sun Sep 6 23:16:43 2026 +0300
Commit:     Claude Executor <executor@local>
CommitDate: Sun Sep 6 23:16:43 2026 +0300

    build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)

 src/build_quarters_signed.py | 380 ++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 356 insertions(+), 24 deletions(-)
commit 8c262e9b272aceeb16d4f21503bd4ac92361f1e9
Author:     Claude Executor <executor@local>
AuthorDate: Sun Sep 6 23:16:48 2026 +0300
Commit:     Claude Executor <executor@local>
CommitDate: Sun Sep 6 23:16:48 2026 +0300

    gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)

 src/qa_quarters_signed.py              | 118 ++++++++++++++++++++++++++++++---
 tests/test_quarters_signed_fixtures.py |  54 ++++++++++++++-
 2 files changed, 160 insertions(+), 12 deletions(-)
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
 data/quarters_signed.geojson | 1 +
 1 file changed, 1 insertion(+)
8c262e9b272aceeb16d4f21503bd4ac92361f1e9 gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)
63d077d6f717ccb44b8cdc435969d60b13ec8865 build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)
791b0cb2ccc509e5ff75bf195fe9806a1eaba0c6 gates: qa_quarters_signed with negative fixtures
2800a7cf3f8aa4d301956b7879c54bc35b8bb25b build: assemble quarters_signed.geojson from decisions 3 (sha ec2813e1c074) with D1 schema for imported geometry
5e468a11ec5bf5e79e54cf78ddd5257714b6c50d measure: KAIS quar vs candidate polygons, read-only
524fe313fe7c57fdab58fbc112fc59c35abcade5 measure: polygon-vs-written quarter, ledger untouched

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; '"'{0}: {1}' -f "'$i,$_ }' in C:\git\varna_3d
 succeeded in 33ms:
1: # ПЛАН НОЩНА СМЯНА · Границите (06→07.09.2026) — v2 за подпис (след Кими К22 и Astra S21)
2: 
3: **Клас: 🔴 Архитектурен. Статус: ПОДПИСАН от Петър (06.09.2026, вечерта; част А и част Б с блок Б0 т. 1–12 по препоръките).** Думите му: „подписвам и след изпълнението искам ти, кими и астра да прегледате изпълнението от различни ъгли“. Подписаното тяло: v2, sha256 на blob-а в комит 42b2635 = `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766`. Следизпълнителен преглед: архитект (Fable, дифът), Кими (данни/лиценз), Astra (механика) — записано като лот Б5. Топология: планировчик → три вътрешни оборвания (Opus) → Кими + Astra → подпис → изпълнител → независим одитор на всеки лот → Петър.
4: 
5: **Строеж на плана.** **ЧАСТ А** (лотове Н0–Н5) е нощ от **мерки** — тръгва при подпис на плана и не иска нито едно ново решение; така е след трите вътрешни оборвания (D1 е затворен набор от 21 полета; D2 заключва метода „по улици“; D13 затворени публични набори; G17). **ЧАСТ Б** (лотове Б1–Б4) е нощ от **резултати** — подписан файл с граници, присвояване на квартал, търсене по квартал — и тръгва САМО ако Петър подпише тази вечер и **блока решения Б0** (§6), защото всяко от тях е негово по ADR 010 и амандамент №2. Ако Б0 не е подписан, нощта е само А. Ако Б0 е подписан, А се изпълнява първа (числата ѝ де-рискуват Б), после Б.
6: 
7: **Принципът на Петър за данните (06.09, вечерта):** „дори имената на адресите да лъжат — геокоординатите не лъжат“. Кварталът на място се определя от координатата му спрямо потвърдените полигони; адресните низове са свидетели, не съдии; спор (записан ≠ полигон) е ред в леджер, никога презапис. Раздел §7 „Конфликти и нормализация“ прави от това мярка.
8: 
9: **Водещата промяна спрямо чернова 1:** тази нощ НЕ се ражда канонична подписана геометрия. Нощта произвежда **мерки и кандидати** — никой файл не се казва `quarters_signed.geojson` и никой не твърди „подписано“. Причината е измерена: D1 (`docs/decisions/010_signed_quarter_boundaries.md:38`) е ЗАТВОРЕН набор от 21 полета с „липсващо поле = STOP“, а внесен уикимапийски полигон няма `drawn_by/drawn_at/basemap/viewport/screenshot_sha256/approval_digest/witnesses`. Схемата за ВНЕСЕНА геометрия е амандамент за подпис, не решение на изпълнител.
10: 
11: ## 0 · Червени редове (важат за всеки лот, без изключение)
12: 
13: 1. **Агентите не пушат.** Никога, с никакъв флаг, без `--no-verify`.
14: 2. **Нула геометрия в проследен файл на Fire_Varna.** Публично пътуват само име, код и картата за атрибуция.
15: 3. **`Varna_buildings/config/quarter_registry.json` не се пипа.** Ваялар→alias, Евксиноград/Траката, Цветен квартал, 16-те без решение, липсващите `parents` — всичко отива в сутрешния списък (§5).
16: 4. **Написан квартал не се променя** (D18/G17). Спорът е ред в леджера, не редакция.
17: 5. **Малки, обратими комити**, изчерпателен write-set, дословно съобщение, автор `Claude Executor <executor@local>`; подписаната геометрия и решенията чакат комит на `Petar1984` (D16, G4 е fail-closed).
18: 6. **Всеки гейт е команда с изход ≠ 0 и с отрицателна фикстура, която ТРЯБВА да падне.** Паднал гейт СПИРА лота; нощта продължава само с лотовете, които не зависят от него.
19: 7. **Само Opus** — изпълнители и одитори; всеки `agent()` с `model: "opus"`.
20: 8. **Одиторът е друг агент** (read-only) за всеки лот. Самопотвърждение не е доказателство.
21: 
22: **Две обявени отклонения (искат подпис заедно с плана):** (а) `ПЛАН_ИЗЧИСТВАНЕ_v2_05.09.md §0.1` иска един лот в движение до пуш — измерено: Fire_Varna 37 ahead, varna_3d 41, Varna_buildings 1; нощта отваря шест лота в три репа, всичките мерки. (б) `§0.3` иска Kimi и Astra преди изпълнение — този план минава през Astra преди първия ред код; при недостъпност нощта се свива до Н0 и Н4.
23: 
24: ## 1 · Мярка преди плана (прочетено тази вечер, read-only)
25: 
26: - `granitsi_decisions_3_2026-09-06_proba.json`: 68 реда, `choice` = wikimapia 60 · deferred 6 · declared_streets 1 · alias_of 1. Ключове на реда: code, display, kind, choice, wm_id, wm_polygon_sha256, wm_title, reason, decided_by, decided_at. **`precision_m` — 0/68.** Договорът в амандамент №2 §4 не познава `declared_streets` и `alias_of` → G26 се разширява (обявено отклонение).
27: - Файлът е **ПРОСЛЕДЕН И КОМИТНАТ ОТ АГЕНТ**: `b6e627d`, автор `Claude Architect`. Значи състоянието не е „некомитнат“, а `agent_committed_proba` — амандамент №2 §4 иска блоб, комитнат от Петър.
28: - `wm_polygon_sha256` в решенията е **СУРОВ** хеш на компактния `{"type","coordinates"}`, не канонизацията по D1 (6 знака, CCW, ротация, подредба по площ). Мерено: `abatko` = `c2e0662d…`, `mladost2` = `80f40ee1…`.
29: - `agkk_au5_varna.geojson`: 5 Feature-а **без `properties`**; ключове `nationalcode` ("10135-01"…"10135-05"), `upper`, `area_km2`, `n_places`, `district_codes_inside`. **Словесен код на район в този файл НЯМА.** Словесните са `index.html:6315` (`DISTRICT_CODES`).
30: - `index.html:6313` `QUARTER_SRC`, `:6317-6321` `QUARTER_CODES` = **затворен списък от 20 кода**; **41 от 61-те потвърдени кода ги няма** в него, а `morska_gradina`, `sveti_nikola`, `zelenika` са в `LOCALITY_CODES` (`:6322`) — друг клас. Непознат код умира мълчаливо по същия път като непознат `src`.
31: - `varna_3d/src/fire_varna_locations.py:76`: `LEDGER = scratch/refactor/_addr/lot1v_locations_375.json` — **проследен**; той е базата на G17. Всеки прогон на канала го презаписва.
32: - `_meta.base_rev` **не съществува** в днешния леджер, а D18/G17 (`ADR:72,:131`) четат `git show <base_rev>:…`. Променливата е недефинирана.
33: - `varna_3d/.gitignore:4` `data/*`, `:23` `*.geojson` → `data/place_identity.json` е игнориран; `place_identity.py:602` чете предишния файл, `:1261` го презаписва — това е СЪСТОЯНИЕ, не производна.
34: - `web/varna_buildings_info.json` е таблица без геометрия; телата са `web/varna_buildings_3d.geojson` (29.9 MB).
35: - Вложеност между 60-те полигона: **10 вложени двойки, 7 НЕДЕКЛАРИРАНИ** (rozova_dolina⊂asparuhovo, kokardzha_generic⊂izgrev_kv, abatko⊂kk_konstantin_elena, saltanat⊂morska_gradina, vazrazhdane1/2/3⊂vazrazhdane). `parents` в регистъра са **дисплей-низове** и има само 6; `borovets` няма потвърден полигон.
36: - `varna_3d` = PRIVATE (`gh` не е в PATH; работи с `C:\Program Files\GitHub CLI\gh.exe`). `ФАЗА_0_лицензи.md:4` = „⏳ чака подпис“ → G21 държи заключено.
37: - Шестте фикстури S17 ги няма в `Fire_Varna/tests/`; днешният набор е 310 теста, зелен.
38: 
39: ## 2 · Лотовете
40: 
41: | Лот | Репо | Изчерпателен write-set | Дословно съобщение | Откат |
42: |---|---|---|---|---|
43: | Н0 пинове | Fire_Varna | `scratch/places_search/noshtna_pins_06.09.json`, `scratch/places_search/qa_night_pins.py` | `measure: pin night-shift inputs, base_rev and ignore proofs (06.09)` | `git revert <sha>` |
44: | Н1 кандидат | varna_3d | `src/build_quarters_candidate.py`, `src/qa_quarters_candidate.py` (изходът `scratch/granitsi/quarters_candidate_07.09.geojson` е игнориран по `.gitignore:23` и НЕ се стейджва) | `measure: candidate quarter geometry from pinned decisions (no signed artifact)` | `git revert <sha>` + изтриване на изхода по назован път |
45: | Н2-0 координати | varna_3d | `src/measure_place_coords.py` (изход `scratch/granitsi/place_coords_07.09.json`, непроследен) | `measure: derive place coordinates read-only, no identity mutation` | същото |
46: | Н2 присвояване | varna_3d | `src/measure_polygon_assign.py` (изход `scratch/granitsi/assign_measure_07.09.json`) | `measure: polygon-vs-written quarter, ledger untouched` | същото |
47: | Н3-а фикстури | Fire_Varna | `tests/test_granitsi_fixtures.py`, `scratch/places_search/granitsi_fixtures_06.09.json` | `tests: five S17 fixtures against today's frozen behaviour` | `git revert <sha>` |
48: | Н4 сгради | varna_3d | `src/measure_kais_quar_vs_polygons.py` | `measure: KAIS quar vs candidate polygons, read-only` | `git revert <sha>` |
49: | Н5 доклад | Fire_Varna | `docs/audits/ДОКЛАД_07.09_нощна_смяна.md` | `docs: night-shift report 07.09` | `git revert <sha>` |
50: 
51: Зависимости: Н0 → всичко. Н1 → Н2, Н4. Н2-0 → Н2. Н3-а е независим. Пада ли Н1 — Н2 и Н4 отпадат, Н3-а и Н5 продължават.
52: 
53: 
54: ### 2а · Договори на скриптовете (Astra S21 т. 1: „липсващ бъдещ скрипт е допустим deliverable, но с подписан интерфейс, точна команда, exit code и фикстура“)
55: | скрипт (нов, в write-set-а на лота) | команда (от корена на репото) | exit 0 означава | отрицателна фикстура (трябва да даде exit ≠ 0) |
56: |---|---|---|---|
57: | `scratch/places_search/qa_night_pins.py` (Fire_Varna) | `python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json` | всеки sha256 в пиновете е преизчислен и равен; `git check-ignore` за всеки геометричен път = игнориран; `git ls-files scratch/boundary_gallery` = 0; `base_rev` = записаният HEAD | `--pins <копие с един обърнат hex знак>` → ≠ 0; `--worktree-negative` (еднократно worktree с `git add -f` на копие на geometry-файл) → гейтът за G29 там ≠ 0 |
58: | `src/build_quarters_candidate.py` (varna_3d) | `python src/build_quarters_candidate.py --decisions <път> --frozen <път> --extra <път> --out scratch/granitsi/quarters_candidate_07.09.geojson` | файлът е написан, `_meta.artifact_class == "candidate_not_signed"`, две последователни сглобявания са байт-еднакви | `--decisions <файл с координата в ред>` → ≠ 0; `--frozen <файл с подменен връх>` → ≠ 0 |
59: | `src/qa_quarters_candidate.py` (varna_3d) | `python src/qa_quarters_candidate.py scratch/granitsi/quarters_candidate_07.09.geojson --registry <път> --decisions <път>` | всички проверки от Н1 минават; 16-те `registry_pending` са ИЗКЛЮЧЕНИЕТО, формализирано: код без решение е ✗ САМО ако не е в `_meta.registry_pending` (списъкът е затворен и се сверява срещу решенията) | `tests/fixtures/qa_quarters_candidate/*.geojson` — по една фикстура на проверка (подменен `wm_id`, `declared_local_knowledge`, голо „CC BY-SA“, две кода–една геометрия, `artifact_class` друг, код извън `registry_pending` без ред) → всяка ≠ 0 |
60: | `src/measure_place_coords.py` (varna_3d) | `python src/measure_place_coords.py --identity data/place_identity.json --bodies web/varna_buildings_3d.geojson --out scratch/granitsi/place_coords_07.09.json` | 375 реда; всяка координата в 43.13–43.35 / 27.65–28.10; `sha256(data/place_identity.json)` преди == след (проверява се в скрипта и се печата) | `--bodies <файл с тяло извън кутията>` → ≠ 0; `--identity <файл без place_id>` → ≠ 0 |
61: | `src/measure_polygon_assign.py` (varna_3d) | `python src/measure_polygon_assign.py --base-rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b --polygons <кандидат> --coords <place_coords> --parents <DAG от Б0 т. 12> --out scratch/granitsi/assign_measure_07.09.json` | чете леджера през `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json`; sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` преди == след; `git status --porcelain` без нови проследени промени извън write-set-а | `--polygons <кандидат с една координата, преместена в чужд квартал>` → числата се променят и `--expect <предишен изход>` дава ≠ 0; `--base-rev <несъществуващ>` → ≠ 0 |
62: | `tests/test_granitsi_fixtures.py` (Fire_Varna) | `python -m unittest tests.test_granitsi_fixtures` | петте фикстури минават върху днешното поведение | всяка фикстура има `_broken` вариант в `scratch/places_search/granitsi_fixtures_06.09.json`, който тестът пуска и очаква да ПАДНЕ (assertRaises); липсващ `_broken` = тестът е червен |
63: | `src/measure_kais_quar_vs_polygons.py` (varna_3d) | `python src/measure_kais_quar_vs_polygons.py --info web/varna_buildings_info.json --bodies web/varna_buildings_3d.geojson --polygons <кандидат>` | таблица на stdout (съвпада / не / няма полигон / само район), нула кадастрални идентификатори и координати; sha256-манифест на `data/` и `web/` преди == след | `python src/qa_readonly_ast.py src/measure_kais_quar_vs_polygons.py` (нов, в write-set-а на Н4): AST-обход за `open(...,'w')`, `Path.open`, `json.dump`, `shutil.*`, `os.replace/remove`, `subprocess` → ≠ 0; фикстура `tests/fixtures/readonly_ast_negative.py` с `json.dump` → ≠ 0 |
64: | Н5 (одит) | `python scratch/places_search/qa_night_acceptance.py --report docs/audits/ДОКЛАД_07.09_нощна_смяна.md` (Fire_Varna, в write-set-а на Н5) | всеки лот в доклада има: sha-та на write-set-а, exit кодовете на гейта и на всяка отрицателна фикстура (≠ 0), авторът на комита, съобщението дословно | доклад без ред за някой лот или с гейт без падаща фикстура → ≠ 0 |
65: 
66: **Базова ревизия (Astra S21 т. 2):** `base_rev` = **пълният HEAD на varna_3d, замразен в Н0 преди всяка промяна** — измерено сега `8d60aebb365fb8e74ccc863d3b3db90b74180a3b` (клон `rezhimi`); Н0 го записва в пиновете и проверява, че леджер-блобът и двата износа съвпадат с приетата основа; **не** се взима последният леджер-комит (`31db7b9…` — леджерът там е същият, но износите се различават). QA и манифестът (`qa_fire_varna_m6.py:48`, `lot1v_v_manifest.py:30`) четат стария леджер по константа — при Б2 кандидатът и основата се подават като изрични входове, не чрез смяна на константата. Н0 записва и **мръсния проследен диф във varna_3d** (1 файл сега) като част от основата; „празен `git status`“ не е гейт — гейтът е „нищо ново извън write-set-а“.
67: 
68: **G19 команда (Windows):** `& "C:\Program Files\GitHub CLI\gh.exe" repo view Petar1984/varna_3d --json visibility` → `{"visibility":"PRIVATE"}`; друго или празно = СТОП за целия varna_3d фронт.
69: 
70: ## 3 · Лот по лот
71: 
72: ### Н0 · Предусловия и пинове
73: `noshtna_pins_06.09.json` (нула координати) пинва `sha256` на: решенията (**плюс комита `b6e627d` и автора `Claude Architect`**), `frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson` (`b53a3322…`) **и** `granitsi_preview_05.09/wikimapia_quarters_frozen_2026-09-06_v2.geojson` — двете копия са байт-еднакви, **веригата се доказва по sha, не по име**; суровия снапшот; `m2_1_candidates_v2.json` (`1331130e…`, обявен вход на решенията); `wikimapia_extra_2026-09-06.geojson` (Евксиноград 5729429, **извън обявения frozen манифест** — записва се изрично); `mladost2_streets_proposal.geojson`; `agkk_au5_varna.geojson`; `quarter_registry.json`; `lot1v_locations_375.json`; **`base_rev` = точният комит, от който се чете леджер-блобът**. Записва се и, че `based_on` предшественикът `granitsi_decisions_2_…` липсва на диска — веригата назад е скъсана (ред в доклада, не мълчание). Плюс `git rev-list --count origin/…` за трите репа и **G19**: `"C:\Program Files\GitHub CLI\gh.exe" repo view varna_3d --json visibility` → трябва `PRIVATE`; празен изход или `PUBLIC` = СТОП за целия varna_3d фронт.
74: 
75: **Гейт Н0 (червен).** `qa_night_pins.py` преизчислява всеки sha и повтаря git-проверките. Фикстури: обърнат hex знак → ≠ 0; **`git add -f` върху копие на geometry-файл в еднократно worktree → гейтът за G29 трябва да падне ТАМ и да е зелен в реалното дърво** (`git add -n` е dry-run и не доказва нищо); подменено ИМЕ при съвпадащ sha → зелено, подменен sha → червено.
76: 
77: ### Н1 · Кандидат-геометрия (varna_3d, частно, НЕподписано)
78: Един Feature на **уикимапийски** потвърден код: **60 кода** (59 + Евксиноград). **Младост 2 НЕ влиза** — D2 (`ADR:40`) казва „по улици“ → ЗАКЛЮЧЕН ВИНАГИ, отключва се само с изричен подписан ключ, а G1 има точно тази отрицателна фикстура; излиза като `deferred` и поименно в §5. Полета: `code`, `name`, `kind`, `source: "wikimapia"`, `wm_id`, **`raw_geometry_sha256`** (пренесен от решенията) **и** `wm_polygon_sha256_d1` (пресметнат по канонизацията на D1) — двете правила се записват отделно, разликата е обявено отклонение за Петър; `url`, `fetched_at`, `confirmed_by/at`, `chosen_reason`; **`licence` дословно** по амандамент №2 §3.8 и К21 т. 3–4: `"CC BY-SA (версия непосочена в ToS; прието 3.0; при конфликт по-строгото печели)"` + етикета за доброволци/неофициален извор/URL на условията/дата; `attribution` низът; `parent` от регистъра след **явна стъпка дисплей→код с гейт** (непознат дисплей = червено), а за код с родител без полигон (`borovets_sever`, `borovets_yug`) — `parent_geometry_check: "няма родителски полигон"`. **`precision_m` НЕ се измисля** (0/68 в решенията) — Feature-ът носи `precision_m: null` и лотът не го замества с литерал. **`district` НЕ се пише** (виж §5 т. 4); вместо това мярка: за всеки кандидат кой `nationalcode` го съдържа. `_meta`: `artifact_class: "candidate_not_signed"`, `decisions_state: "agent_committed_proba (b6e627d, Claude Architect)"`, манифест на входовете, `licences[]`, `source_terms.wikimapia {url, checked_on, quote, terms, verdict, position}`, `registry_pending` с **16-те кода без решение поименно**.
79: 
80: **Гейт Н1 (червен).** Предгейтове: **G19** (частно репо), **G3** (`qa_no_cad_ids.py` — задължителен преди всеки комит по CLAUDE.md на varna_3d). Фикстури: подменен връх при непроменен sha (за ВСЕКИ от двата хеш-ключа поотделно, всеки срещу своя източник) · подменен `wm_id` · `deferred` код с Feature и Feature без ред · **жилищен код от регистъра без ред в решенията → ✗, поименно** · координата във файла с решения · липсващ ред за атрибуция · **не-уикимапийски ред с непразно `wm_*` → ✗** · **входен Feature със `source: "declared_local_knowledge"` → ✗** (етикетът е отменен от амандамент №2 §3.7) · голо „CC BY-SA“ или липсващ `terms` → ✗ · една геометрия към два несравними кода · BOM/CRLF/несортирани ключове · две сглобявания дават байт-еднакъв файл · **`_meta.artifact_class ≠ "candidate_not_signed"` → ✗**.
81: 
82: ### Н2-0 · Координати — МЯРКА, без мутация
83: `place_identity.json` **не се докосва** (игнориран, състояние, генераторът чете сам себе си). Отделен скрипт извежда `place_id → lat/lon` от същите връзки, които идентичността вече носи (`site_id`/`kais_i` → представителна точка на тяло в `web/varna_buildings_3d.geojson`), и пише САМО в `scratch/granitsi/place_coords_07.09.json`. Място без връзка → `no_coord`, брои се, не се гади. **Гейт:** 375 реда; всяка координата в кутията 43.13–43.35 / 27.65–28.10; sha256 на `data/place_identity.json` идентичен преди и след. Фикстури: координата извън кутията → ✗; липсващ `place_id` → ✗.
84: 
85: ### Н2 · Присвояване — САМО ЧИСЛА, нула запис
86: Скриптът чете **блоба** `git show <base_rev>:scratch/refactor/_addr/lot1v_locations_375.json` (не работния файл), кандидат-полигоните и координатите, и брои. `fire_varna_locations.py` **не се редактира**; леджерът **не се презаписва**. Правила на мярката: празен квартал + точно един полигон → „би получил“; **място в ≥ 2 полигона БЕЗ декларирано родство → `disputed`** (7-те недекларирани вложености); „най-малкият печели, детето преди родителя“ важи САМО за 6-те декларирани двойки; написан ≠ полигон → `disputed`; **няма полигон → редът си остава с вече написания район** (нищо не се извежда от АГКК); ръбът се брои в **три ленти 50/100/250 m** и трите числа влизат в доклада, докато Петър не подпише `precision_m`. **Гейт:** sha256 на `data/fire_varna_places.json`, `data/fire_varna_hotels.json`, `scratch/refactor/_addr/lot1v_locations_375.json` **идентични преди и след**; `git status --porcelain` в varna_3d празен извън write-set-а.
87: 
88: **Десетият ключ на `_meta` НЕ се специфицира и НЕ се пуска.** Причина: подписваният източник го нарича с ДВЕ имена — амандамент №2 §3.3 (`licence_quarter_boundary`) и §5/G27 (`quarter_attribution`), а фикстурата на G27 отхвърля `_meta` с 11 ключа. Едното трябва да умре с думата на Петър (§5 т. 5).
89: 
90: ### Н3-а · Фикстури (Fire_Varna) — днешното поведение, не приемане
91: Пет фикстури: `street_collision`, `district_retention`, `mladost_kind_collision`, `order_identity`, **`parent_child` върху двойка с ДНЕС регистрирано родство** (`mladost`/`mladost2`) — версията с Възраждане се отлага, защото vazrazhdane1..4 нямат `parents`. **`client_cache_matrix` се отлага** с назована причина: браузърно поведение, а единственият node-изпълнител в `tests/` е `test_data_ascii_mojibake.py`; лотът не назовава втори. Всяка фикстура пада върху нарочно счупен кандидат и мутацията влиза дословно в доклада. **Гейт:** `python -m unittest discover -s tests` (310+ зелени) И `python -m gates.run_gates` без червено — иначе сутрешният пуш на Петър е блокиран от собствената му кука. Записва се изрично: **това фиксира ДНЕШНОТО поведение; утре F13 ще ги направи кандидат-очаквания, не приемане.**
92: 
93: **Н3-б СПИРА (нарочно).** Търсенето по квартал и редът за атрибуция в картончето не тръгват: нов `src` или нов код без подредената тройка на D13 изхвърля 150 места мълчаливо, а измереното е по-лошо от очакваното — **41 кода липсват в `QUARTER_CODES`**, три от тях са днес местности.
94: 
95: ### Н4 · Сградите — САМО мярка
96: Вход: `web/varna_buildings_info.json` (речниково кодирана колона `quar`, `build_places.py:78-96`) + **`web/varna_buildings_3d.geojson`** (телата, поименно) + кандидат-полигоните. За всяка сграда с непразен `quar`: съвпада / не съвпада / няма полигон / само район. Изход: **stdout**; нула кадастрални идентификатори, нула координати. **Гейт (червен):** AST-проверка за извикване на пишеща функция (не grep — `json.dump(obj, fp)`, `Path.open("w")`, `shutil.copy` минават през списък от низове), с фикстура-вариант, който пише през `json.dump` → ✗; плюс sha256-манифест на **всичко под `data/` и `web/`** преди и след и `git status --porcelain` празен.
97: 
98: ### Н5 · Одит и доклад
99: Одитор (Opus, read-only, различен агент) на всеки лот: преизпълнява гейтовете, сверява дифа срещу write-set-а (**всеки допълнителен файл = находка**), проверява автора, съобщението и `git log --format=%an -1 --` върху пътя на решенията срещу `_meta`. **Разделение:** одиторът дава числата, изпълнителят ги записва без да ги тълкува. Докладът носи: числата на Н1, Н2 (по трите ленти), Н3-а (5/5 + доказаните падания + двете отложени), Н4, всички sha, поименния списък на спрелите лотове с причината, и §„Какво прави Петър сутринта“.
100: 
101: **Атрибуция в проследените артефакти:** всеки нощен проследен файл на Fire_Varna, който назовава уикимапийски обект, носи ред за атрибуция по §3.8 (ключ `attribution` в JSON, заглавен ред в MD) — ToS §1.G важи и когато github.com рендерира файла в браузър. Вече комитнатият `granitsi_decisions_3_…json` (60 `wm_id` + заглавия) няма такъв ред: **това е сутрешен дълг, не нощна поправка.**
102: 
103: ## 4 · Нарушения, които спират нощта веднага
104: 
105: Опит за `git push` · геометрия в проследен файл на Fire_Varna · редакция на регистъра · промяна на написан квартал · запис в `lot1v_locations_375.json`, `place_identity.json` или `data/fire_varna_*.json` · файл на име `quarters_signed.geojson` · Feature по метод „по улици“ · нов публичен `src` **или нов квартален КОД** без разширен `QUARTER_CODES` и подредената тройка на D13 · низът `10135` в **публична** доставка (в частния провенанс и в мярката е позволен — иначе АГКК изворът е неназовим) · зелен гейт без падаща отрицателна фикстура.
106: 
107: ## 5 · Сутринта (решенията за Петър, ако Б0 НЕ е подписан тази вечер)
108: 
109: 1. **Схемата за ВНЕСЕНА геометрия** (кои от 21-те полета на D1 отпадат и с какво се заместват) — амандамент, без който няма подписан артефакт.
110: 2. **Кое правило е `wm_polygon_sha256`** — суровият хеш (днешният в решенията) или канонизацията на D1.
111: 3. **Младост 2**: подписан ключ по D2 + лиценз (ODbL, „© OpenStreetMap contributors“) + под на `precision_m` за уличен метод.
112: 4. **Районът**: от нашия `district.code` (375/375 съгласие) с явен `district_src`, или от АГКК — тогава `_meta.source_terms["agkk_inspire_au5"]` се попълва и G22/G23 стават червени предгейтове.
113: 5. **Едно име за десетия ключ** (`licence_quarter_boundary` или `quarter_attribution`) и низът за атрибуция; картата да е независима от извора `{code:{src,url,label,licence}}`, за да носи и ODbL, и АГКК.
114: 6. **`precision_m`** — стойност и довод (от нея зависи кой е `edge_pending`).
115: 7. **Разширяването на `QUARTER_CODES`** с 41-те кода и какво става с `morska_gradina`, `sveti_nikola`, `zelenika`, които днес са местности.
116: 8. **Решенията**: `git mv` на днешния блоб под подписан път (не втори блоб с втора sha) или подпис на днешния път.
117: 9. Регистърът: Ваялар→alias, Евксиноград/Траката, Цветен квартал, `parents` за Възраждане 1–4 и Розова долина, 16-те без решение.
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
154: - **Правилото за бъдещето** (в доклада, за амандамент): всеки нов извор влиза с ранг и с колона в леджера; никой извор не презаписва друг; координатата е арбитърът за полето „квартал“; имената се нормализират през регистъра (alias-и), не през редакции на данните.
155: 
156: ## Какво подписва Петър
157: 
158: **ЧАСТ А (винаги):** подписваш **една нощ от мерки**: шест лота, които четат — пинове с доказана верига (Н0), кандидат-геометрия от 60-те уикимапийски кода в частното репо, която НЕ е подписан артефакт и умира с една команда (Н1), координати и присвояване, преброени срещу непокътнат леджер и три ленти на неточността (Н2-0, Н2), пет фикстури, които фиксират ДНЕШНОТО поведение на търсенето (Н3-а), мярката за ~10k сгради (Н4) и доклад, чиито числа идват от одитора (Н5) — плюс двете обявени отклонения от `ПЛАН_ИЗЧИСТВАНЕ_v2 §0.1` и `§0.3` и десетте решения в §5, които остават твои и на които нито един агент няма право да отговори през нощта.
159: 
160: **ЧАСТ Б (само с блок Б0):** подписваш и дванадесетте решения в §6 Б0 — тогава нощта произвежда `quarters_signed.geojson` (стейджнат за твоя комит), координатите на местата от кадастралните тела (т. 11, с резервно копие и G9), присвояването на квартал за празните места като кандидат-износ (стейджнат), кръпката и шумната фикстура за търсенето (Б3 се комитва сутринта с твоите подписи), и одитиран доклад; всичко локално, обратимо, без пуш. Без т. 11 нощта спира преди Б2 и присвояването остава мярка.
161: 
162: ## Какво НЕ се пипа тази нощ (ЧАСТ А; при подписан Б0 изключенията са изброени в Б1–Б3)
163: 
164: `quarter_registry.json` · написаните 201 квартала · `lot1v_locations_375.json` · `place_identity.json` и `data/fire_varna_*.json` · `fire_varna_locations.py` и каналът `SIGNED_POLYGON` · `.gitignore` на varna_3d (разигнорирането чака комита на Петър по G4) · `index.html` (нито `QUARTER_SRC`, нито `QUARTER_CODES`, нито картончето, нито `PLACES_CACHE`) · `_meta` на износа и десетият ключ · Младост 2 като Feature · полето `district` в геометрията · `precision_m` като число · `origin` на което и да е от трите репа.

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "git status --porcelain=v2 --branch
git show --stat --format=fuller 63d077d
git show --stat --format=fuller 8c262e9
git diff --cached --stat
git log -6 --format='%H %s'" in C:\git\varna_3d
 succeeded in 36ms:
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
 data/quarters_signed.geojson | 1 +
 1 file changed, 1 insertion(+)
8c262e9b272aceeb16d4f21503bd4ac92361f1e9 gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)
63d077d6f717ccb44b8cdc435969d60b13ec8865 build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)
791b0cb2ccc509e5ff75bf195fe9806a1eaba0c6 gates: qa_quarters_signed with negative fixtures
2800a7cf3f8aa4d301956b7879c54bc35b8bb25b build: assemble quarters_signed.geojson from decisions 3 (sha ec2813e1c074) with D1 schema for imported geometry
5e468a11ec5bf5e79e54cf78ddd5257714b6c50d measure: KAIS quar vs candidate polygons, read-only
524fe313fe7c57fdab58fbc112fc59c35abcade5 measure: polygon-vs-written quarter, ledger untouched

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'Get-Content -Encoding UTF8 -LiteralPath C:/git/varna_3d/docs/activeContext.md -TotalCount 100
$p='"'C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -le 45 -or ($i -ge 108 -and $i -le 139)){ '"'{0}: {1}' -f "'$i,$_ } }' in C:\git
 succeeded in 4ms:
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'src/qa_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -le 150){ '"'{0}: {1}' -f "'$i,$_ } }
rg -n --max-count 20 --max-columns 200 '"'def test_|Temporary|write|fixtures|signed_plan|plan_pin|decisions_repo' tests/test_quarters_signed_fixtures.py" in C:\git\varna_3d
 succeeded in 28ms:
121:     if meta.get("decisions_commit") != DECISIONS_REV:
122:         bad("C1 клас на артефакта", f"decisions_commit = {meta.get('decisions_commit')!r}")
123: 
124: 
125: def check_bytes(path: Path, document: dict) -> None:
126:     raw = path.read_bytes()
127:     if raw.startswith(b"\xef\xbb\xbf"):
128:         bad("C2 байтове", "файлът започва с BOM")
129:     if b"\r" in raw:
130:         bad("C2 байтове", "файлът съдържа CR (CRLF)")
131:     if not raw.endswith(b"\n"):
132:         bad("C2 байтове", "липсва финален LF")
133:     if raw != canonical_bytes(document):
134:         bad("C2 байтове", "файлът не е каноничен по G30 (сортирани ключове, компактен, без BOM, финален LF)")
135: 
136: 
137: def check_d1_schema(features: list) -> None:
138:     for feature in features:
139:         props = feature.get("properties") or {}
140:         code = props.get("code")
141:         for field in D1_FIELDS:
142:             if field not in props:
143:                 bad("C3 D1 схема", f"{code}: липсва задължителното поле на D1 „{field}“")
144:         unknown = [k for k in props if k not in ALL_FIELDS]
145:         if unknown:
146:             bad("C3 D1 схема", f"{code}: полета извън затворения набор: {sorted(unknown)}")
147:         for field in D1_NULL_ON_IMPORT:
148:             if props.get(field) is not None:
149:                 bad("C3 D1 схема",
150:                     f"{code}: {field} = {props.get(field)!r} — при ВНЕСЕНА геометрия е null по договор (Б0 т. 1)")
1:"""Lot Б1 — the gate is only a gate if its negative fixtures have actually run and
8:top level of its own discovery — the write-set of the lot stays exactly the five
13:  * every fixture in `tests/fixtures/qa_quarters_signed/` makes it exit != 0, and
15:  * the two input-side fixtures make `src/build_quarters_signed.py` exit != 0;
19:The fixtures are regenerated here from the tracked code, never committed
20:(`.gitignore:23` — `*.geojson`), so the write-set of the lot stays exhaustive.
34:FIXTURES = ROOT / "tests" / "fixtures" / "qa_quarters_signed"
122:                    "--registry", REGISTRY, "--make-fixtures"])
126:    def test_gate_is_green_on_the_signed_artifact(self) -> None:
130:    def test_artifact_carries_the_signed_shape(self) -> None:
145:    def test_the_union_is_the_geometry_petar_signed(self) -> None:
161:    def test_every_negative_fixture_actually_fails(self) -> None:
171:    def test_build_refuses_a_moved_vertex_in_the_frozen_set(self) -> None:
172:        with tempfile.TemporaryDirectory() as tmp:
174:                       + ["--make-negative-fixtures", tmp])
181:    def test_build_refuses_a_moved_vertex_in_a_union_part(self) -> None:
184:        with tempfile.TemporaryDirectory() as tmp:
186:                       + ["--make-negative-fixtures", tmp])
193:    def test_build_refuses_a_moved_vertex_in_the_mladost2_face(self) -> None:
194:        with tempfile.TemporaryDirectory() as tmp:

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -le 20){ '"'{0}: {1}' -f "'$i,$_ } }
Get-Content -Encoding UTF8 -LiteralPath C:/git/Fire_Varna/scratch/places_search/granitsi_b1v2_astra_S23_07.09.md -TotalCount 110
rg -n --max-count 20 --max-columns 240 '"'S22|F2|sha|подпис' C:/git/Fire_Varna/scratch/places_search/granitsi_night_astra_S22_review_07.09.md" in C:\git
 succeeded in 3ms:
codex
Двата commit-а засягат само файлове от Б1 и са с правилния автор. Съобщенията обаче се различават от дословно зададените в плана, който още сочи decisions 3. Exact plan pin вече се проверява, но това само по себе си не подписва decisions 4.

Открих и че unittest suite изтрива и генерира fixture файлове. За да спазя read-only режима, ще изпълня проверките със забрана за файлови записи и ще проверя наличните отрицателни fixtures отделно.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'
python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 220 'PLAN =|DECISIONS_|signature|signed_by|d6f367|union|versions|plan_signature|read_decisions_blob|def assemble' src/build_quarters_signed.py
"'$p='"'src/build_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -ge 70 -and $i -le 158){ '"'{0}: {1}' -f "'$i,$_ } }' in C:\git\varna_3d
 exited 1 in 95ms:
✗ A1 блоб на решенията: git show 895e0d2651aac73516659f2a10ea5193b2be5d53:scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json падна (fatal: detected dubious ownership in repository at 'C:/git/Fire_Varna'
'C:/git/Fire_Varna' is owned by:
	BUILTIN/Administrators (S-1-5-32-544)
but the current user is:
	PETAR/CodexSandboxOffline (S-1-5-21-1992376794-12164101-10249461-1004)
To add an exception for this directory, call:

	git config --global --add safe.directory C:/git/Fire_Varna)

 succeeded in 54ms:
70:     LON_MIN,
71:     RESIDENTIAL_KINDS,
72:     SOURCE_TERMS_WIKIMAPIA,
73:     canonical_bytes,
74:     canonical_geometry_sha256,
75:     raw_geometry_sha256,
76: )
77: # The closed list of the five city districts (S4).  Read from the resolver, never
78: # re-typed here: a sixth district would have to be signed there first.
79: from fire_varna_locations import DISTRICTS  # noqa: E402
80: 
81: DEFAULT_REGISTRY = "C:/git/Varna_buildings/config/quarter_registry.json"
82: DEFAULT_AGKK = "C:/git/Fire_Varna/scratch/places_search/agkk_inspire_2026-09-05/agkk_au5_varna.geojson"
83: DEFAULT_DISTRICTS = r"C:\git\m6000_private\number_viewer\quarters_layer.geojson"
84: DEFAULT_UNIONS = ("C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/"
85:                   "unions_2026-09-07.geojson")
86: 
87: DECISIONS_REV = "895e0d2651aac73516659f2a10ea5193b2be5d53"
88: DECISIONS_PATH = "scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json"
89: DECISIONS_AUTHOR = "Claude Architect"
90: # Б0 т. 8: Petar signs the decisions by the sha256 of THIS blob.  A different blob
91: # is a different signature and the build stops.
92: DECISIONS_BLOB_SHA256 = "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89"
93: # The blob decisions 4 is based on — decisions 3, signed the same way.  Recorded so
94: # the chain 3 → 4 stays visible in the artefact; not a build input.
95: DECISIONS_BASED_ON = {
96:     "file": "granitsi_decisions_3_2026-09-06_proba.json",
97:     "rev": "b6e627d0fb19e039a062aba955d030301ae45b2e",
98:     "sha256": "ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6",
99: }
100: 
101: PLAN = {
102:     "file": "Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md",
103:     "signed_body_commit": "42b2635",
104:     "signed_body_sha256": "4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766",
105:     "signed_block": "§6 Б0 т. 1–12 (подписан от Петър, 06.09.2026 вечерта)",
106: }
107: 
108: ARTIFACT_CLASS = "signed_by_plan_signature"
109: OUT_NAME = "quarters_signed.geojson"
110: VERSION = 1
111: 
112: # D7: `_meta.precision_floor_m = 50`; the gate refuses `precision_m < 50`.
113: PRECISION_FLOOR_M = 50
114: # Б0 т. 6: 100 for wikimapia, 50 for the street-bounded face.  A union of human
115: # polygons is no more precise than the polygons it is made of → 100, same as one.
116: PRECISION_BY_METHOD = {"human_polygon": 100, "human_polygons_union": 100,
117:                        "street_bounded_face": 50}
118: 
119: # Amendment №2 §3.8 supplements D2 with the geometry classes and their licence:
120: # `official_polygon` → the licence of the source; `human_polygon` → CC BY-SA with
121: # the URI and the object URL; `georef_reconstruction` → the licence of the plan.
122: # Б0 т. 3 adds `street_bounded_face` → ODbL, for `mladost2` and nothing else.
123: METHOD_SOURCE = {"human_polygon": "wikimapia",
124:                  "human_polygons_union": "wikimapia_union",
125:                  "street_bounded_face": "declared_streets"}
126: STREET_METHOD = "street_bounded_face"
127: STREET_METHOD_ONLY_CODE = "mladost2"
128: 
129: # Decisions 4 (Petar, 07.09): one code is the UNION of two Wikimapia objects.  The
130: # geometry class stays human_polygon-grade (volunteers drew both rings), so licence,
131: # attribution and precision are the Wikimapia ones; only the method and the source
132: # label say that two objects were merged.
133: UNION_METHOD = "human_polygons_union"
134: UNION_SOURCE = "wikimapia_union"
135: # Both Wikimapia-derived sources, for the licence and the ToS §1.G attribution row.
136: WIKIMAPIA_SOURCES = ("wikimapia", UNION_SOURCE)
137: # MEASURED, 07.09: `unary_union` in WGS84 degrees gives `bc92a76c…`, while the union
138: # Petar looked at (`unions_2026-09-07.geojson`, `wm_polygon_sha256` pinned in the
139: # decisions row) is `d6f367bd…` — the difference is float noise of order 1e-14° from
140: # the metric round trip its producer used (the same round trip that yields the
141: # 1,426 km² in that file).  The pin is the signature, so the pin is what is
142: # reproduced: project to UTM 35N, union there, project back.  The A9 check below
143: # refuses any other result, so this constant can never drift silently.
144: UNION_CRS = "EPSG:32635"
145: 
146: # The abolished label of amendment №2 §3.7.  The mladost2 proposal file still
147: # carries it as an INPUT; it never reaches the output, and any other value stops
148: # the build.
149: ABOLISHED_SOURCE = "declared_local_knowledge"
150: 
151: ODBL_LICENSE = "ODbL © OpenStreetMap contributors"
152: ODBL_TERMS = "https://www.openstreetmap.org/copyright (Open Database License 1.0; https://opendatacommons.org/licenses/odbl/1-0/)"
153: ODBL_ATTRIBUTION = "© OpenStreetMap contributors · https://www.openstreetmap.org/copyright (ODbL)"
154: 
155: WIKIMAPIA_ATTRIBUTION = (
156:     "Граница по Wikimapia.org (© Wikimapia contributors) — връзка към обекта в полето url; "
157:     "CC BY-SA; ToS §1.G изисква и „Wikimapia.org“ с връзка към http://wikimapia.org"
158: )

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'tests/test_quarters_signed_fixtures.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -le 150){ '"'{0}: {1}' -f "'$i,$_ } }' in C:\git\varna_3d
 succeeded in 0ms:
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
15:   * the two input-side fixtures make `src/build_quarters_signed.py` exit != 0;
16:   * a fresh assembly into a temporary directory is byte-identical to the file on
17:     disk (G30 determinism), so the artefact can be rebuilt from its inputs.
18: 
19: The fixtures are regenerated here from the tracked code, never committed
20: (`.gitignore:23` — `*.geojson`), so the write-set of the lot stays exhaustive.
21: """
22: from __future__ import annotations
23: 
24: import hashlib
25: import json
26: import shutil
27: import subprocess
28: import sys
29: import tempfile
30: import unittest
31: from pathlib import Path
32: 
33: ROOT = Path(__file__).resolve().parent.parent
34: FIXTURES = ROOT / "tests" / "fixtures" / "qa_quarters_signed"
35: ARTIFACT = ROOT / "data" / "quarters_signed.geojson"
36: REGISTRY = "C:/git/Varna_buildings/config/quarter_registry.json"
37: FIRE_VARNA = Path("C:/git/Fire_Varna")
38: 
39: BOUNDARY = FIRE_VARNA / "scratch" / "boundary_gallery"
40: FROZEN = BOUNDARY / "frozen_2026-09-06" / "wikimapia_quarters_2026-09-06_v2.geojson"
41: RAW_SNAPSHOT = BOUNDARY / "frozen_2026-09-06" / "wikimapia_varna_places_raw_2026-09-06.json"
42: EXTRA = BOUNDARY / "granitsi_preview_05.09" / "wikimapia_extra_2026-09-06.geojson"
43: MLADOST2 = BOUNDARY / "granitsi_preview_05.09" / "mladost2_streets_proposal.geojson"
44: UNIONS_FILE = BOUNDARY / "granitsi_preview_05.09" / "unions_2026-09-07.geojson"
45: 
46: # The three signatures this artefact hangs on, written out here on purpose: the test
47: # must fail if any of them drifts in the code, not quote the code back at itself.
48: DECISIONS_BLOB_SHA256 = "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89"
49: PLAN_BODY_SHA256 = "4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766"
50: UNION_RAW_SHA256 = "d6f367bdf56671bf6ff2d59d587a6235d8f0cb34be4396ebe78ea8949f537014"
51: 
52: # fixture name → the check whose name must appear in the gate's output.
53: EXPECTED_CHECK = {
54:     "artifact_class_other": "C1",
55:     "decisions_sha_substituted": "C1",
56:     "bom_crlf_unsorted": "C2",
57:     "d1_field_missing": "C3",
58:     "drawn_by_filled_on_import": "C3",
59:     "d1_null_not_allowed": "C3",
60:     "declared_local_knowledge": "C3",
61:     "vertex_moved": "C4",
62:     "hash_raw_substituted": "C4",
63:     "hash_d1_substituted": "C5",
64:     "wm_id_substituted": "C6",
65:     "deferred_code_with_feature": "C7",
66:     "feature_without_row": "C7",
67:     "mladost2_missing": "C7",
68:     "code_outside_registry_pending": "C8",
69:     "bare_cc_by_sa": "C9",
70:     "missing_terms": "C9",
71:     "missing_attribution": "C10",
72:     "osm_code_with_wikimapia_string": "C10",
73:     "two_codes_one_geometry": "C11",
74:     "precision_missing": "C13",
75:     "precision_below_floor": "C13",
76:     "street_method_other_code": "C16",
77:     "parent_not_in_registry": "C14",
78:     "dag_pair_removed": "C17",
79:     "district_from_agkk": "C18",
80:     # Astra S22 F2 — the two weaknesses the gate used to let through.
81:     "plan_sha_zeroed": "C1",
82:     "district_spatially_wrong": "C18",
83:     # Decisions 4 — the union and the excluded code.
84:     "excluded_code_with_feature": "C7",
85:     "union_wm_ids_substituted": "C6",
86: }
87: 
88: 
89: def run(args: list[str]) -> subprocess.CompletedProcess:
90:     return subprocess.run(
91:         [sys.executable] + args, cwd=str(ROOT), capture_output=True,
92:     )
93: 
94: 
95: def text_of(result: subprocess.CompletedProcess) -> str:
96:     return (result.stdout + result.stderr).decode("utf-8", "replace")
97: 
98: 
99: def gate(path: Path) -> subprocess.CompletedProcess:
100:     return run(["src/qa_quarters_signed.py", str(path), "--registry", REGISTRY])
101: 
102: 
103: def build_args(out: Path, frozen: Path = FROZEN, mladost2: Path = MLADOST2) -> list[str]:
104:     return [
105:         "src/build_quarters_signed.py",
106:         "--frozen", str(frozen),
107:         "--raw-snapshot", str(RAW_SNAPSHOT),
108:         "--extra", str(EXTRA),
109:         "--mladost2", str(mladost2),
110:         "--out", str(out),
111:     ]
112: 
113: 
114: class SignedQuartersFixtures(unittest.TestCase):
115:     @classmethod
116:     def setUpClass(cls) -> None:
117:         if not ARTIFACT.exists():
118:             raise unittest.SkipTest(f"липсва {ARTIFACT} — лот Б1 не е сглобен")
119:         if FIXTURES.exists():
120:             shutil.rmtree(FIXTURES)
121:         made = run(["src/qa_quarters_signed.py", str(ARTIFACT),
122:                     "--registry", REGISTRY, "--make-fixtures"])
123:         if made.returncode != 0:
124:             raise AssertionError(f"генерирането на фикстурите падна:\n{text_of(made)}")
125: 
126:     def test_gate_is_green_on_the_signed_artifact(self) -> None:
127:         result = gate(ARTIFACT)
128:         self.assertEqual(result.returncode, 0, text_of(result))
129: 
130:     def test_artifact_carries_the_signed_shape(self) -> None:
131:         document = json.loads(ARTIFACT.read_bytes().decode("utf-8"))
132:         meta = document["_meta"]
133:         self.assertEqual(meta["artifact_class"], "signed_by_plan_signature")
134:         # Decisions 4: 58 single Wikimapia polygons + 1 union + Младост 2.
135:         self.assertEqual(len(document["features"]), 60)
136:         methods = [f["properties"]["method"] for f in document["features"]]
137:         self.assertEqual(methods.count("street_bounded_face"), 1)
138:         self.assertEqual(methods.count("human_polygon"), 58)
139:         self.assertEqual(methods.count("human_polygons_union"), 1)
140:         self.assertEqual(meta["decisions_sha256"], DECISIONS_BLOB_SHA256)
141:         self.assertEqual(meta["plan"]["signed_body_sha256"], PLAN_BODY_SHA256)
142:         self.assertEqual([item["code"] for item in meta["excluded"]], ["vinitsa_sever"])
143:         self.assertNotIn("vinitsa_sever", {f["properties"]["code"] for f in document["features"]})
144: 
145:     def test_the_union_is_the_geometry_petar_signed(self) -> None:
146:         """The pin travels: decisions row → Feature → the union file of the board."""
147:         document = json.loads(ARTIFACT.read_bytes().decode("utf-8"))
148:         union = [f for f in document["features"]
149:                  if f["properties"]["method"] == "human_polygons_union"]
150:         self.assertEqual(len(union), 1)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:PYTHONDONTWRITEBYTECODE='"'1'
"'$env:GIT_CONFIG_COUNT='"'1'
"'$env:GIT_CONFIG_KEY_0='"'safe.directory'
"'$env:GIT_CONFIG_VALUE_0='"'C:/git/Fire_Varna'
python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna" in C:\git\varna_3d
 succeeded in 196ms:
✓ ГЕЙТ Б1 ЗЕЛЕН · data\quarters_signed.geojson · 295304 B · sha256 4930f2043438edb9353fc5dc0f4d92cd92fc0248208c0f83783b991ca743f5c3
  Feature-и: 60 · решения: 68 · registry_pending: 16 · блоб на решенията 2c650160cebd…
  обединения: 1 · изключени: ['vinitsa_sever'] · подписано тяло на плана 4ce6ea842a0a… (42b2635)
  18 проверки: C1 клас/подпис (дословен sha на плана) · C2 байтове (G30) · C3 D1 схема (21 полета) · C4 суров хеш (G25-а) · C5 хеш по D1 (G25-а) · C6 wm_id (G25-а) · C7 биекция (G26) · C8 регистър (G26) · C9 лиценз · C10 атрибуция (G27-а) · C11 еднозначност · C12 решения · C13 precision_m · C14 родител · C15 кадастрални идентификатори · C16 метод · C17 DAG (Б0 т. 9) · C18 район ПРОСТРАНСТВЕНО (Б0 т. 4)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'src/qa_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -ge 484 -and $i -le 630){ '"'{0}: {1}' -f "'$i,$_ } }
$p='"'tests/test_quarters_signed_fixtures.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -ge 150 -and $i -le 225){ '"'{0}: {1}' -f "'$i,$_ } }' in C:\git\varna_3d
 succeeded in 33ms:
584:     doc = clone()
585:     doc["_meta"]["registry_pending"] = doc["_meta"]["registry_pending"][1:]
586:     emit("code_outside_registry_pending", doc)
587: 
588:     # C9 — a bare licence.
589:     doc = clone()
590:     doc["features"][10]["properties"]["license"] = "CC BY-SA"
591:     emit("bare_cc_by_sa", doc)
592: 
593:     # C9 — missing terms.
594:     doc = clone()
595:     doc["_meta"]["source_terms"]["wikimapia"]["terms"] = ""
596:     emit("missing_terms", doc)
597: 
598:     # C10 — a Feature without the attribution row.
599:     doc = clone()
600:     doc["features"][11]["properties"]["attribution"] = ""
601:     emit("missing_attribution", doc)
602: 
603:     # C10 — Б0 т. 5: an OSM-sourced code shown with the Wikimapia string.
604:     doc = clone()
605:     i = index_of(doc, STREET_METHOD_ONLY_CODE)
606:     doc["features"][i]["properties"]["attribution"] = (
607:         "Граница по Wikimapia.org (© Wikimapia contributors) — връзка към обекта в полето url"
608:     )
609:     emit("osm_code_with_wikimapia_string", doc)
610: 
611:     # C11 — one geometry, two codes.
612:     doc = clone()
613:     donor, victim = doc["features"][12], doc["features"][13]
614:     victim["geometry"] = json.loads(json.dumps(donor["geometry"], ensure_ascii=False))
615:     victim["properties"]["raw_geometry_sha256"] = donor["properties"]["raw_geometry_sha256"]
616:     victim["properties"]["wm_polygon_sha256"] = donor["properties"]["wm_polygon_sha256"]
617:     emit("two_codes_one_geometry", doc)
618: 
619:     # C13 — precision_m missing.
620:     doc = clone()
621:     doc["features"][14]["properties"].pop("precision_m")
622:     emit("precision_missing", doc)
623: 
624:     # C13 — precision_m below the floor of D7.
625:     doc = clone()
626:     doc["features"][15]["properties"]["precision_m"] = 25
627:     emit("precision_below_floor", doc)
628: 
629:     # C16 — the street method on a code other than mladost2.
630:     doc = clone()
150:         self.assertEqual(len(union), 1)
151:         props = union[0]["properties"]
152:         self.assertEqual(props["code"], "dobreva")
153:         self.assertEqual(props["wm_ids"], [5729380, 5729421])
154:         self.assertIsNone(props["wm_id"])
155:         self.assertEqual(props["raw_geometry_sha256"], UNION_RAW_SHA256)
156:         self.assertEqual(props["precision_m"], 100)
157:         self.assertEqual(len(props["witnesses"]), 2)
158:         witness = json.loads(UNIONS_FILE.read_bytes().decode("utf-8"))["features"][0]
159:         self.assertEqual(witness["properties"]["wm_polygon_sha256"], UNION_RAW_SHA256)
160: 
161:     def test_every_negative_fixture_actually_fails(self) -> None:
162:         found = sorted(p.stem for p in FIXTURES.glob("*.geojson"))
163:         self.assertEqual(found, sorted(EXPECTED_CHECK), "наборът фикстури се разминава с очаквания")
164:         for name, check in sorted(EXPECTED_CHECK.items()):
165:             with self.subTest(fixture=name):
166:                 result = gate(FIXTURES / f"{name}.geojson")
167:                 output = text_of(result)
168:                 self.assertNotEqual(result.returncode, 0, f"{name} НЕ падна:\n{output}")
169:                 self.assertIn(check, output, f"{name} падна, но не по {check}:\n{output}")
170: 
171:     def test_build_refuses_a_moved_vertex_in_the_frozen_set(self) -> None:
172:         with tempfile.TemporaryDirectory() as tmp:
173:             made = run(build_args(Path(tmp) / "quarters_signed.geojson")
174:                        + ["--make-negative-fixtures", tmp])
175:             self.assertEqual(made.returncode, 0, text_of(made))
176:             broken = Path(tmp) / "frozen_vertex_moved.geojson"
177:             result = run(build_args(Path(tmp) / "quarters_signed.geojson", frozen=broken))
178:             self.assertNotEqual(result.returncode, 0, text_of(result))
179:             self.assertIn("A9", text_of(result))
180: 
181:     def test_build_refuses_a_moved_vertex_in_a_union_part(self) -> None:
182:         """Decisions 4: move one vertex of one of the two rings and the union no longer
183:         equals the pin Petar signed — the build must stop, not quietly re-union."""
184:         with tempfile.TemporaryDirectory() as tmp:
185:             made = run(build_args(Path(tmp) / "quarters_signed.geojson")
186:                        + ["--make-negative-fixtures", tmp])
187:             self.assertEqual(made.returncode, 0, text_of(made))
188:             broken = Path(tmp) / "union_part_vertex_moved.geojson"
189:             result = run(build_args(Path(tmp) / "quarters_signed.geojson", frozen=broken))
190:             self.assertNotEqual(result.returncode, 0, text_of(result))
191:             self.assertIn("A9", text_of(result))
192: 
193:     def test_build_refuses_a_moved_vertex_in_the_mladost2_face(self) -> None:
194:         with tempfile.TemporaryDirectory() as tmp:
195:             made = run(build_args(Path(tmp) / "quarters_signed.geojson")
196:                        + ["--make-negative-fixtures", tmp])
197:             self.assertEqual(made.returncode, 0, text_of(made))
198:             broken = Path(tmp) / "mladost2_vertex_moved.geojson"
199:             result = run(build_args(Path(tmp) / "quarters_signed.geojson", mladost2=broken))
200:             self.assertNotEqual(result.returncode, 0, text_of(result))
201:             self.assertIn("A9", text_of(result))
202: 
203:     def test_build_refuses_any_other_output_name(self) -> None:
204:         with tempfile.TemporaryDirectory() as tmp:
205:             result = run(build_args(Path(tmp) / "quarters_candidate.geojson"))
206:             self.assertNotEqual(result.returncode, 0, text_of(result))
207: 
208:     def test_rebuild_is_byte_identical(self) -> None:
209:         with tempfile.TemporaryDirectory() as tmp:
210:             out = Path(tmp) / "quarters_signed.geojson"
211:             result = run(build_args(out))
212:             self.assertEqual(result.returncode, 0, text_of(result))
213:             self.assertEqual(
214:                 hashlib.sha256(out.read_bytes()).hexdigest(),
215:                 hashlib.sha256(ARTIFACT.read_bytes()).hexdigest(),
216:                 "повторното сглобяване не дава байт-еднакъв файл (G30)",
217:             )
218: 
219: 
220: if __name__ == "__main__":
221:     unittest.main()

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import sys, runpy
sys.dont_write_bytecode = True
def deny_writes(event, args):
    if event in {'os.remove','os.rmdir','os.mkdir','os.rename','os.replace','shutil.rmtree'}:
        raise PermissionError('S23 read-only: blocked ' + event)
    if event == 'open' and ((isinstance(args[1],str) and any(x in args[1] for x in 'wax+')) or (isinstance(args[2],int) and args[2] & 0x503)):
        raise PermissionError('S23 read-only: blocked file write')
sys.addaudithook(deny_writes)
sys.argv=['python -m unittest', 'tests.test_quarters_signed_fixtures']
runpy.run_module('unittest',run_name='__main__')
'@ | python -B -" in C:\git\varna_3d
 exited 1 in 61ms:
E
======================================================================
ERROR: setUpClass (tests.test_quarters_signed_fixtures.SignedQuartersFixtures)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\git\varna_3d\tests\test_quarters_signed_fixtures.py", line 120, in setUpClass
    shutil.rmtree(FIXTURES)
  File "C:\Program Files\Python310\lib\shutil.py", line 698, in rmtree
    sys.audit("shutil.rmtree", path)
  File "<stdin>", line 5, in deny_writes
PermissionError: S23 read-only: blocked shutil.rmtree

----------------------------------------------------------------------
Ran 0 tests in 0.001s

FAILED (errors=1)

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import sys,subprocess,hashlib,json,collections
sys.stdout.reconfigure(encoding='utf-8')
r='C:/git/Fire_Varna'
p='docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md'
for rev,path in [('42b2635',p),('895e0d2','scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json')]:
 b=subprocess.check_output(['git','-c','safe.directory='+r,'-C',r,'show',rev+':'+path]);print(rev,'sha256',hashlib.sha256(b).hexdigest(),'bytes',len(b))
 print(subprocess.check_output(['git','-c','safe.directory='+r,'-C',r,'log','-1','--format=%H%n%an <%ae>%n%s',rev]).decode('utf-8'))
a=subprocess.check_output(['git','show',':data/quarters_signed.geojson']);w=open('data/quarters_signed.geojson','rb').read();d=json.loads(a)
print('index/worktree equal',a==w,'bytes',len(a),'sha256',hashlib.sha256(a).hexdigest()); print('sources',collections.Counter(f['properties']['source'] for f in d['features']));print('META',json.dumps({k:v for k,v in d['_meta'].items() if k in ['plan','signature','union_construction','decisions_sha256','decisions_commit','decisions_based_on','inputs']},ensure_ascii=False))
'@ | python -B -" in C:\git\varna_3d
 succeeded in 122ms:
42b2635 sha256 b9ffc28c4c904664aaf5a60992287b723f8c5e10c432256021f6d4cea02deff9 bytes 204
42b26350c9dc7b235d8645f998c0b581198a7de0
Claude Architect <architect@local>
docs(plan): night plan v2 — Astra S21 applied: script interface contracts (command, exit code, negative fixture) for every lot, base_rev = varna_3d HEAD 8d60aebb frozen at Н0, Б0.11 coordinate source (KAIS body representative point into place_identity with backup + G9), Б0.12 closed outcome table, parent/child DAG of 11 measured pairs + 5 partial overlaps, Б2 only with Б0.11, Б3 moved to the morning (atomic commit with Petar's signatures), corrected acceptance criteria; for signature

895e0d2 sha256 2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89 bytes 31646
895e0d2651aac73516659f2a10ea5193b2be5d53
Claude Architect <architect@local>
record: decisions 4 — Виница-север excluded on Petar's word (registry: deactivate the code); Добрева чешма keeps the union

index/worktree equal True bytes 295304 sha256 4930f2043438edb9353fc5dc0f4d92cd92fc0248208c0f83783b991ca743f5c3
sources Counter({'wikimapia': 58, 'wikimapia_union': 1, 'declared_streets': 1})
META {"decisions_based_on": {"file": "granitsi_decisions_3_2026-09-06_proba.json", "rev": "b6e627d0fb19e039a062aba955d030301ae45b2e", "sha256": "ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6"}, "decisions_commit": "895e0d2651aac73516659f2a10ea5193b2be5d53", "decisions_sha256": "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89", "inputs": [{"bytes": 31646, "id": "decisions_4", "path": "Fire_Varna:895e0d2651aac73516659f2a10ea5193b2be5d53:scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json", "role": "решенията — подписани по sha256 на блоба (Б0 т. 8); четени от git, не от работното копие", "sha256": "2c650160cebd79d3404854d047d60422f4edf6de98e5ee5adb2589758d6a5c89"}, {"bytes": 589222, "id": "frozen_v2", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/wikimapia_quarters_2026-09-06_v2.geojson", "role": "замразеният уикимапийски набор — изворът на единичните геометрии и на двете части на обединението", "sha256": "b53a3322b1a6e5670ea17f7638ab77d198e120d108e623fa7bc78ae702daf976"}, {"bytes": 3713, "id": "wikimapia_extra_5729429", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/wikimapia_extra_2026-09-06.geojson", "role": "обектът 5729429 (Евксиноград/Траката), подаден от Петър след замразяването", "sha256": "b220423c6f954405fb0dbf94621fab30a8b6585e7156089c67e14dfa41382dd8"}, {"bytes": 5071516, "id": "raw_snapshot", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/frozen_2026-09-06/wikimapia_varna_places_raw_2026-09-06.json", "role": "суровият отговор на обхода — raw_response_sha256 в witnesses на уикимапийските Feature-и", "sha256": "1c0561cb7e612e72f291ca33d603cc6ef7713b88ab5af7cbd6d942fbc18a7fbe"}, {"bytes": 2971, "id": "mladost2_face", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/mladost2_streets_proposal.geojson", "role": "карето „Младост 2“ по четирите улици (оси от OSM) — подписаният ключ на Б0 т. 3", "sha256": "66fd3f57f76d4f104911dc2f7576f33e678435b6e1156a19d61c0bf34030f5b8"}, {"bytes": 52299, "id": "quarter_registry", "path": "C:/git/Varna_buildings/config/quarter_registry.json", "role": "регистърът — имена, вид и родство; ЧЕТЕН, никога пипан (червена черта 3)", "sha256": "7d21740101a2fc65ca0cb289fee10f8116e8505eec313c921252469ac236d4d6"}, {"bytes": 201130, "id": "our_districts", "path": "C:/git/m6000_private/number_viewer/quarters_layer.geojson", "role": "нашите пет административни района (слоят за сравнение на fire_varna_locations) — изворът на полето district по Б0 т. 4", "sha256": "26e39b001ce151203058d70bc53367a5b40c77c4b0dd7113cf2a7085c376cc22"}, {"bytes": 61469, "id": "agkk_au5", "path": "C:/git/Fire_Varna/scratch/places_search/agkk_inspire_2026-09-05/agkk_au5_varna.geojson", "role": "петте района на АГКК INSPIRE — САМО свидетел (G22 остава заключен, Б0 т. 4)", "sha256": "78a2de59600eb103719ca072b3963c6b7195598a65a66e4653c7cd53c966c669"}, {"bytes": 3921, "id": "unions_2026-09-07", "path": "C:/git/Fire_Varna/scratch/boundary_gallery/granitsi_preview_05.09/unions_2026-09-07.geojson", "role": "обединенията, както Петър ги видя — САМО свидетел; геометрията се преизчислява от замразения набор и сверява байт по байт срещу него", "sha256": "0fe781500725d78f46b9f931b66ad0267f782413f2c47f28a7669b68d1504080"}], "plan": {"file": "Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md", "signed_block": "§6 Б0 т. 1–12 (подписан от Петър, 06.09.2026 вечерта)", "signed_body_commit": "42b2635", "signed_body_sha256": "4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766"}, "signature": {"basis": "подписът на плана (§6 Б0 т. 1–12) върху решенията по sha256 на блоба; signed_by в Feature-ите става валидно точно с този подпис (Б0 т. 1)", "commit_of_this_file_belongs_to": "Petar1984 (D16 / G4 — изпълнителят го оставя стейджнат)", "signed_at": "2026-09-06", "signed_by": "Petar"}}

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import sys,subprocess,hashlib
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
r=Path('C:/git/Fire_Varna');p=next(p for p in (r/'docs/plans').glob('*.md') if '\\u041d\\u041e\\u0429\\u041d\\u0410' in p.name);b=subprocess.check_output(['git','-c','safe.directory='+str(r),'-C',str(r),'show','42b2635:'+p.relative_to(r).as_posix()]);print(p);print('bytes',len(b),'sha256',hashlib.sha256(b).hexdigest());print('blob',subprocess.check_output(['git','-c','safe.directory='+str(r),'-C',str(r),'rev-parse','42b2635:'+p.relative_to(r).as_posix()]).decode().strip());print('signature line',p.read_text(encoding='utf-8').splitlines()[2])
'@ | python -B -" in C:\git\varna_3d
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$env:GIT_CONFIG_COUNT='"'1'
"'$env:GIT_CONFIG_KEY_0='"'safe.directory'
"'$env:GIT_CONFIG_VALUE_0='"'C:/git/Fire_Varna'
"'$env:PYTHONDONTWRITEBYTECODE='"'1'
@'
import sys,unittest
from tests import test_quarters_signed_fixtures as t
sys.stdout.reconfigure(encoding='utf-8')
names=['test_gate_is_green_on_the_signed_artifact','test_artifact_carries_the_signed_shape','test_the_union_is_the_geometry_petar_signed','test_every_negative_fixture_actually_fails']
t.SignedQuartersFixtures.setUpClass=classmethod(lambda cls: None)
suite=unittest.TestSuite(t.SignedQuartersFixtures(n) for n in names)
result=unittest.TextTestRunner(verbosity=2).run(suite)
print('Expected negative fixtures:',len(t.EXPECTED_CHECK))
for name in ['plan_sha_zeroed','district_spatially_wrong','union_wm_ids_substituted']:
 r=t.gate(t.FIXTURES/(name+'.geojson'));print(name,'exit',r.returncode);print(t.text_of(r).splitlines()[-4:])
sys.exit(not result.wasSuccessful())
'@ | python -B -" in C:\git\varna_3d
 succeeded in 127ms:
C:\git\Fire_Varna\docs\plans\ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md
bytes 61697 sha256 4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766
blob 90837b7591008d618de24fe5a71479cd252d9bde
signature line **Клас: 🔴 Архитектурен. Статус: ПОДПИСАН от Петър (06.09.2026, вечерта; част А и част Б с блок Б0 т. 1–12 по препоръките).** Думите му: „подписвам и след изпълнението искам ти, кими и астра да прегледате изпълнението от различни ъгли“. Подписаното тяло: v2, sha256 на blob-а в комит 42b2635 = `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766`. Следизпълнителен преглед: архитект (Fable, дифът), Кими (данни/лиценз), Astra (механика) — записано като лот Б5. Топология: планировчик → три вътрешни оборвания (Opus) → Кими + Astra → подпис → изпълнител → независим одитор на всеки лот → Петър.

 succeeded in 9227ms:
test_gate_is_green_on_the_signed_artifact (tests.test_quarters_signed_fixtures.SignedQuartersFixtures) ... ok
test_artifact_carries_the_signed_shape (tests.test_quarters_signed_fixtures.SignedQuartersFixtures) ... ok
test_the_union_is_the_geometry_petar_signed (tests.test_quarters_signed_fixtures.SignedQuartersFixtures)
The pin travels: decisions row \u2192 Feature \u2192 the union file of the board. ... ok
test_every_negative_fixture_actually_fails (tests.test_quarters_signed_fixtures.SignedQuartersFixtures) ... ok

----------------------------------------------------------------------
Ran 4 tests in 8.289s

OK
Expected negative fixtures: 30
plan_sha_zeroed exit 1
['✗ ГЕЙТ Б1 ЧЕРВЕН — 1 находки:', '  ✗ C1 клас на артефакта: signed_body_sha256 000000000000… не е дословният sha на подписаното тяло на плана 4ce6ea842a0a… (git show 42b2635:docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md | sha256sum)']
district_spatially_wrong exit 1
['✗ ГЕЙТ Б1 ЧЕРВЕН — 1 находки:', "  ✗ C18 район: hristo_botev: district 'asparuhovo' не е районът, в който лежи представителната точка на Feature-а ('odesos') — позволен код не е доказан район"]
union_wm_ids_substituted exit 1
['✗ ГЕЙТ Б1 ЧЕРВЕН — 1 находки:', '  ✗ C6 wm_id: dobreva: обединение без списък от поне два обекта ([5729380])']

codex
QA е зелен; `plan_sha_zeroed` пада по C1, а `district_spatially_wrong` — по C18. Всичките 30 налични отрицателни fixtures падат по очакваната проверка.

Независимата пространствена проверка потвърди точно двата спора — `vazrazhdane4` и `kochmar`. При union-а има и неточен коментар: разликата между двете конструкции не е само шум около `1e-14°`; различават се и D1 hashes след закръгляне.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'src/qa_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if(($i -ge 200 -and $i -le 258) -or ($i -ge 698 -and $i -le 780)){ '"'{0}: {1}' -f "'$i,$_ } }
rg -n --max-count 20 --max-columns 220 '"'signature|source_union|union_crs|software|construction|versions|signed_at' src/build_quarters_signed.py
Get-Content -Encoding UTF8 -LiteralPath C:/git/Fire_Varna/scratch/places_search/granitsi_night_astra_S22_review_07.09.md -Tail 45" in C:\git\varna_3d
 succeeded in 63ms:
200:         props = feature.get("properties") or {}
201:         code = props.get("code")
202:         row = rows_by_code.get(code)
203:         if row is None:
204:             continue
205:         if props.get("wm_id") != row.get("wm_id"):
206:             bad("C6 wm_id", f"{code}: wm_id {props.get('wm_id')!r} не е този в решенията ({row.get('wm_id')!r})")
207:         if props.get("source") == "wikimapia":
208:             url = str(props.get("url") or "")
209:             if not props.get("wm_id") or str(props["wm_id"]) not in url:
210:                 bad("C6 wm_id", f"{code}: url {url!r} не сочи обекта {props.get('wm_id')!r}")
211:         elif props.get("wm_id") is not None:
212:             bad("C6 wm_id", f"{code}: не-уикимапийски Feature с непразен wm_id")
213:         # Decisions 4: the union carries the LIST of objects, never a single wm_id.
214:         if props.get("source") == UNION_SOURCE:
215:             wm_ids = props.get("wm_ids")
216:             if not isinstance(wm_ids, list) or len(wm_ids) < 2:
217:                 bad("C6 wm_id", f"{code}: обединение без списък от поне два обекта ({wm_ids!r})")
218:             elif wm_ids != row.get("wm_ids"):
219:                 bad("C6 wm_id", f"{code}: wm_ids {wm_ids!r} не са тези в решенията ({row.get('wm_ids')!r})")
220:             else:
221:                 witnesses = props.get("witnesses") or []
222:                 if sorted(w.get("wm_id") for w in witnesses) != sorted(wm_ids):
223:                     bad("C6 wm_id", f"{code}: свидетелите не покриват точно обектите {wm_ids!r}")
224:                 for witness in witnesses:
225:                     if str(witness.get("wm_id")) not in str(witness.get("url") or ""):
226:                         bad("C6 wm_id", f"{code}: свидетел с url, който не сочи обекта "
227:                                         f"{witness.get('wm_id')!r}")
228:                     if not witness.get("raw_geometry_sha256"):
229:                         bad("C6 wm_id", f"{code}: свидетел без собствен суров хеш на частта")
230:                 if str(wm_ids[0]) not in str(props.get("url") or ""):
231:                     bad("C6 wm_id", f"{code}: url {props.get('url')!r} не сочи първия обект {wm_ids[0]}")
232:         elif props.get("wm_ids") is not None:
233:             bad("C6 wm_id", f"{code}: Feature без обединение с непразен wm_ids")
234: 
235: 
236: def check_bijection(features: list, rows: list, meta: dict) -> None:
237:     """G26 — decisions ↔ the three sets of D4: wikimapia/declared_streets → polygon,
238:     alias_of/deferred → `_meta`."""
239:     feature_codes = [(f.get("properties") or {}).get("code") for f in features]
240:     if len(feature_codes) != len(set(feature_codes)):
241:         bad("C7 биекция", "повтарящ се код сред Feature-ите")
242:     polygon_rows = {r["code"] for r in rows if r.get("choice") in set(POLYGON_CHOICES)}
243:     missing = sorted(polygon_rows - set(feature_codes))
244:     if missing:
245:         bad("C7 биекция", "решение за полигон без Feature: " + ", ".join(missing))
246:     extra = sorted(set(feature_codes) - polygon_rows)
247:     if extra:
248:         bad("C7 биекция", "Feature без решение за полигон: " + ", ".join(str(c) for c in extra))
249:     without = meta.get("rows_without_feature") or {}
250:     for choice in ("deferred", "alias_of"):
251:         expected = sorted(r["code"] for r in rows if r.get("choice") == choice)
252:         listed = sorted(str(item.get("code")) for item in without.get(choice, []))
253:         if expected != listed:
254:             bad("C7 биекция", f"_meta.rows_without_feature.{choice}: {listed} вместо {expected}")
255:         for code in expected:
256:             if code in feature_codes:
257:                 bad("C7 биекция", f"{code}: choice={choice}, а има Feature")
258:     # Decisions 4 — `excluded` is its own set: no Feature, named in `_meta.excluded`.
698:     path = Path(args.path)
699:     if not path.exists():
700:         print(f"✗ вход: файлът липсва: {path}")
701:         return 1
702:     raw = path.read_bytes()
703:     try:
704:         document = json.loads(raw.decode("utf-8-sig"))
705:     except Exception as exc:  # noqa: BLE001
706:         print(f"✗ C2 байтове: файлът не е валиден UTF-8 JSON ({exc})")
707:         return 1
708: 
709:     registry_doc = json.loads(Path(args.registry).read_bytes().decode("utf-8"))
710:     registry = {e["id"]: e for e in registry_doc["entries"]}
711: 
712:     decisions_raw, decisions_sha = read_decisions_blob(
713:         Path(args.decisions_repo), args.decisions_rev, args.decisions_path)
714:     decisions_doc = json.loads(decisions_raw.decode("utf-8"))
715:     rows = decisions_doc["decisions"]
716:     rows_by_code = {r["code"]: r for r in rows}
717: 
718:     meta = document.get("_meta") or {}
719:     features = document.get("features") or []
720:     feature_codes = {(f.get("properties") or {}).get("code") for f in features}
721: 
722:     if args.make_fixtures:
723:         for item in make_fixtures(document, Path(args.fixtures_dir)):
724:             print(f"фикстура: {item}")
725:         return 0
726: 
727:     if decisions_sha != DECISIONS_BLOB_SHA256:
728:         bad("C1 клас на артефакта",
729:             f"прочетеният блоб на решенията {decisions_sha[:12]}… не е подписаният "
730:             f"{DECISIONS_BLOB_SHA256[:12]}…")
731: 
732:     check_artifact_class(meta)
733:     check_bytes(path, document)
734:     check_d1_schema(features)
735:     check_hashes_raw(features, rows_by_code)
736:     check_hashes_d1(features)
737:     check_wm_id(features, rows_by_code)
738:     check_bijection(features, rows, meta)
739:     check_registry(meta, registry, rows)
740:     check_licence(features, meta)
741:     check_attribution(features, meta)
742:     check_unique_geometry(features)
743:     check_decisions_clean(decisions_doc, f"{args.decisions_rev}:{args.decisions_path}")
744:     check_precision(features)
745:     check_method(features)
746:     check_parents(features, registry, feature_codes)
747:     check_dag(meta, registry)
748:     check_district(features, args.districts)
749:     check_no_cad_ids(path)
750: 
751:     if FAILURES:
752:         print(f"✗ ГЕЙТ Б1 ЧЕРВЕН — {len(FAILURES)} находки:")
753:         for item in FAILURES[:40]:
754:             print(f"  ✗ {item}")
755:         if len(FAILURES) > 40:
756:             print(f"  … и още {len(FAILURES) - 40}")
757:         return 1
758: 
759:     print(f"✓ ГЕЙТ Б1 ЗЕЛЕН · {path} · {len(raw)} B · sha256 {hashlib.sha256(raw).hexdigest()}")
760:     print(f"  Feature-и: {len(features)} · решения: {len(rows)} · registry_pending: "
761:           f"{len(meta.get('registry_pending', []))} · блоб на решенията {decisions_sha[:12]}…")
762:     print(f"  обединения: {sum(1 for f in features if (f.get('properties') or {}).get('method') == UNION_METHOD)}"
763:           f" · изключени: {[i.get('code') for i in meta.get('excluded') or []]}"
764:           f" · подписано тяло на плана {PLAN['signed_body_sha256'][:12]}… ({PLAN['signed_body_commit']})")
765:     print("  18 проверки: C1 клас/подпис (дословен sha на плана) · C2 байтове (G30) · C3 D1 схема (21 полета) · "
766:           "C4 суров хеш (G25-а) · C5 хеш по D1 (G25-а) · C6 wm_id (G25-а) · C7 биекция (G26) · "
767:           "C8 регистър (G26) · C9 лиценз · C10 атрибуция (G27-а) · C11 еднозначност · "
768:           "C12 решения · C13 precision_m · C14 родител · C15 кадастрални идентификатори · "
769:           "C16 метод · C17 DAG (Б0 т. 9) · C18 район ПРОСТРАНСТВЕНО (Б0 т. 4)")
770:     return 0
771: 
772: 
773: if __name__ == "__main__":
774:     sys.exit(main())
3:This IS the signed artefact.  It is signed by the signature of the night plan
91:# is a different signature and the build stops.
108:ARTIFACT_CLASS = "signed_by_plan_signature"
121:# the URI and the object URL; `georef_reconstruction` → the licence of the plan.
141:# 1,426 km² in that file).  The pin is the signature, so the pin is what is
1152:        "signature": {
1154:            "signed_at": "2026-09-06",
1160:        "union_crs": UNION_CRS,
1273:          f"обединения: {sorted(meta['union_witness'].get('by_code', {}))} в {meta['union_crs']}")

[Index и worktree](C:/git/varna_3d/data/quarters_signed.geojson:1) са байт-еднакви: **291024 B, 61 Features**, SHA256 `3f423898ec79aa7ba7ec26f14a55f8d43d8407f3f4e13913a568d1e9744426f1`. Две сглобявания в паметта възпроизвеждат същите байтове.

Потвърдени са:

- 21 D1 полета; седемте `null` са `drawn_by`, `drawn_at`, `basemap`, `viewport`, `visible_layers`, `screenshot_sha256`, `approval_digest`. `witnesses` е попълнен. [План:124](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:124).
- Каноничният `wm_polygon_sha256` и отделният `raw_geometry_sha256` са проверени независимо. [QA:145](C:/git/varna_3d/src/qa_quarters_signed.py:145).
- `mladost2`: подписаният `street_bounded_face`, четирите улици, `ODbL © OpenStreetMap contributors`, `precision_m:50`; останалите 60 имат precision 100. [Builder:457](C:/git/varna_3d/src/build_quarters_signed.py:457).
- Районът е изчислен срещу нашите пет района: **0/61 пространствени разминавания**. DAG — точно 11 двойки; `registry_pending` — точно 16; `artifact_class:"signed_by_plan_signature"`. [Builder:283](C:/git/varna_3d/src/build_quarters_signed.py:283), [QA:388](C:/git/varna_3d/src/qa_quarters_signed.py:388).

Изпълнената QA команда:

```text
python src/qa_quarters_signed.py data/quarters_signed.geojson --registry C:/git/Varna_buildings/config/quarter_registry.json --decisions-repo C:/git/Fire_Varna
```

**Exit 0**, 18 проверки. Всички **26 налични отрицателни fixtures дават exit 1** с очакваната проверка.

`python -m unittest tests.test_quarters_signed_fixtures`, изпълнен през wrapper със забрана на мутации: **exit 1, Ran 0 tests**. `setUpClass` опитва `shutil.rmtree(FIXTURES)` и пресъздаване на директорията — несъвместимо с този read-only преглед. [Tests:103](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:103). Еквивалентите на седемте сценария са проверени без записи; това **не е** оригинален unittest exit 0.

Две възпроизведени слабости в `791b0cb`: **C1 приема `signed_body_sha256` от 64 нули**, а **C18 приема допустим, но пространствено неверен район**. Текущият артефакт е правилен. **F2: exact plan pin и spatial district verification, с отрицателни fixtures; отделно успешно изпълнение на оригиналния suite в изолирана среда с разрешени тестови записи.** [QA:93](C:/git/varna_3d/src/qa_quarters_signed.py:93), [QA:398](C:/git/varna_3d/src/qa_quarters_signed.py:398).

3. **G9: преместен вход → реално разминаване със старата база**

Identity е tracked, последно променена в `756d166` от 04.09. `e613089` от 05.09 променя точно **5 places +72 hotels zones**. Генераторът чете тези `zone` и ги включва в `key`. [Generator:172](C:/git/varna_3d/src/place_identity.py:172), [Generator:187](C:/git/varna_3d/src/place_identity.py:187).

Паркираният G9 даде **exit 1: 77 `zone` +77 `key`, никакви други некоординатни промени**. Два no-coordinate прогона в паметта са еднакви и съвпадат с кандидата след премахване на четирите coordinate keys; **0 нови IDs**. Това отхвърля недетерминизма като причина.

Правилният сутрешен ход е **отделно подписано освежаване на identity базата**, review на 154-те промени, отделен commit, нов backup/SHA, после координатният кандидат и непроменен G9. Контролирайте и `registry_manifest.json`: обикновеното `main()` пише и него. [Generator:1259](C:/git/varna_3d/src/place_identity.py:1259).

Fresh no-coordinate comparison е полезен диагностичен контрол. Самостоятелната подмяна на comparator-а би прикрила реалния старо→ново delta; подписаният договор изисква сравнение с backup и допуска само четирите ключа. [План:134](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:134).

4. **F3: addendum към `c6c5d44`**

Н5 QA още дава **exit 0, 107 проверки**, въпреки остарелия разказ. Н4 е независимо преизпълнен: **exit 0**, същите числа; AST **0**, отрицателна fixture **1**. Следният един абзац трябва да замени текущото оперативно описание на Б2-0 и cleanup-а: [Доклад:236](C:/git/Fire_Varna/docs/audits/ДОКЛАД_07.09_нощна_смяна.md:236).

> След architect cleanup Б2-0 остава спрян на G9 заради 154 некоординатни промени от стара identity база спрямо обновените входове. `src/place_identity.py` е възстановен до HEAD; candidate, QA и diff са запазени в `scratchpad/b20_inflight_2026-09-07/`, кандидатът със SHA `1141bbc2…`. Живата identity остава `e8b4c836…`; подмяна няма. Tracked промените във varna_3d са само staged `quarters_signed.geojson` и завареният dirty `qa_place_bodies.md`. Н4 числата се възпроизвеждат; текущият data/web манифест е 466 файла, digest `a35a7a7f…`, след изнасянето на кандидата. Б1 QA и 26 отрицателни fixtures са независимо проверени; оригиналният unittest е блокиран от read-only защитата. Продължаването изисква одобрена нова identity база.

Коригирайте също броя commit-и и твърдението за липсващ predecessor: `decisions_2` съществува; прекъсването е неговото `based_on:null`. Б0 решенията вече са подписани и не трябва да се представят като нерешени.

5. **Сутрешният push и merge редът**

Fire е **48 ahead/2 behind**. Remote ingest `1af2140`/`18948de` са patch-идентични с локалните `b6866e5`/`fa7a6c0`. Петте ingest файла съвпадат между tips; read-only `merge-tree` даде **exit 0, празен резултат**.

Петър първо сверява remote и прави **обикновен merge на `origin/main`**, запазвайки pinned SHA; ingest не се повтаря. После поправките, актуалните gates и Gate 2. При нов attribution blob трябва да се обнови и провери производната SHA верига. Частният артефакт и евентуалният Б2 предхождат атомната публична доставка Б3; staged геометрията чака commit на Петър. [План:131](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:131), [План:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138).

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
import sys,json,hashlib,subprocess
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
p=Path('C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json');d=json.loads(p.read_bytes());print('keys',list(d));print('meta',json.dumps({k:v for k,v in d.items() if k"'!='"'decisions'},ensure_ascii=False));print('row attribution count',sum('attribution' in r for r in d['decisions']));print('row fields',list(d['decisions'][0]))
sys.path.insert(0,str(Path('src').resolve()));import qa_quarters_signed as q
fixture_bytes={}
class MemoryPath:
 def __init__(self,name=''): self.name=name
 def mkdir(self,**kw): pass
 def __truediv__(self,name): return MemoryPath(name)
 def write_bytes(self,b): fixture_bytes[self.name]=b
q.make_fixtures(json.loads(Path('data/quarters_signed.geojson').read_bytes()),MemoryPath())
print('Generated fixture bytes equal existing:',all((Path('tests/fixtures/qa_quarters_signed')/name).read_bytes()==b for name,b in fixture_bytes.items()),'count',len(fixture_bytes))
'@ | python -B -" in C:\git\varna_3d
 succeeded in 372ms:
keys ['schema_version', 'board', 'based_on', 'inputs', 'exported_at', 'changes', 'decisions']
meta {"schema_version": "0.1-proba", "board": "board.html (scratch preview, unsigned) + architect corrections on Petar's instruction", "based_on": {"file": "granitsi_decisions_3_2026-09-06_proba.json", "sha256_blob_b6e627d": "ec2813e1c074b9b623b153f9ee2a9b9c549f3ad27d806b6314642354a34356f6"}, "inputs": {"frozen_file": "wikimapia_quarters_frozen_2026-09-06_v2.geojson", "frozen_sha256": "b53a3322b1a6e5670ea17f7638ab77d198e120d108e623fa7bc78ae702daf976", "candidates_file": "m2_1_candidates_v2.json", "candidates_sha256": "1331130e5f113737dfe4e4354a69acb81ab0affd32b7747416da38c07a2e96bb"}, "exported_at": "2026-09-06T21:22:27", "changes": ["vazrazhdane1 → 13337602", "vayalar → alias_of sredna_traka", "akchelar → 1855512 (Белица)", "briz → 3710735 (кв. Бриз (кв. Почивка)) — Petar's four-sided description, measured 0 m to each side", "evksinograd → 5729429 (EN 'Euxinograd' = BG 'Траката - разширение'), Petar's URL", "dobreva → wikimapia_union [5729380, 5729421] (Petar 07.09)", "vinitsa_sever → excluded (Petar 07.09: „го изключваме“; registry: deactivate the code)"]}
row attribution count 0
row fields ['code', 'display', 'kind', 'choice', 'wm_id', 'wm_polygon_sha256', 'wm_title', 'reason', 'decided_by', 'decided_at']
Generated fixture bytes equal existing: True count 30

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'src/build_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if(($i -ge 972 -and $i -le 1003) -or ($i -ge 1132 -and $i -le 1173)){ '"'{0}: {1}' -f "'$i,$_ } }
$p='"'C:/git/Fire_Varna/scratch/places_search/granitsi_decisions_4_2026-09-07_proba.json'
rg -n --max-count 20 --max-columns 220 'based_on|decided_by|decided_at|union|attribution|signed|vinitsa_sever|dobreva' "'$p' in C:\git\varna_3d
 succeeded in 49ms:
972:                 "Б0 т. 1 (подписан): за Feature със source ∈ {wikimapia, declared_streets} седемте "
973:                 "полета на ръката са null по договор — взаимна изключителност „или ръка, или внос“. "
974:                 "Дайджестът на D1 се замества от sha-веригата на Б0 т. 8: решения по sha → Feature с "
975:                 "wm_polygon_sha256 → _meta.decisions_sha256."
976:             ),
977:         },
978:         "decisions_author": DECISIONS_AUTHOR,
979:         "decisions_based_on": DECISIONS_BASED_ON,
980:         "decisions_commit": args.decisions_rev,
981:         "decisions_path": args.decisions_path,
982:         "decisions_sha256": decisions_sha,
983:         "decisions_sha256_rule": "sha256 на БЛОБА (git show <rev>:<път>), не на работното копие — Б0 т. 8",
984:         "decisions_sha256_worktree": decisions_worktree,
985:         "declared_deviations": [
986:             {
987:                 "what": "choice: „wikimapia_union“ за кода dobreva (решения 4, Петър 07.09)",
988:                 "why": ("Площта, която Уикимапия нарича „Виница - север“ (5729421), е част от "
989:                         "Добрева чешма — границата е обединението на двата човешки полигона. "
990:                         "Обединението се смята в UTM 35N (EPSG:32635) и се връща в WGS84: така се "
991:                         "възпроизвежда БАЙТ ПО БАЙТ пинът в решенията (d6f367bd…), който Петър "
992:                         "видя; обединение направо в градуси дава bc92a76c… — разлика от порядъка "
993:                         "на 1e-14°, но друг подпис. A9 отказва всеки друг резултат."),
994:             },
995:             {
996:                 "what": "полето url на обединения Feature",
997:                 "why": ("Обединението има два изворни обекта. `url` носи ПЪРВИЯ от реда (този, "
998:                         "чието име носи кодът), а всички обекти с техните url-и и собствени сурови "
999:                         "хешове са в `witnesses` — ToS §1.G се изпълнява от реда за атрибуция плюс "
1000:                         "свидетелите."),
1001:             },
1002:             {
1003:                 "what": "choice: „excluded“ за кода vinitsa_sever",
1132:         ),
1133:         "registry_pending": [
1134:             {
1135:                 "code": code,
1136:                 "display": registry[code]["display"],
1137:                 "kind": registry[code]["kind"],
1138:                 "why": "регистров код без ред в решенията към 06.09 — отложен, поименно (Б0 т. 10)",
1139:             }
1140:             for code in pending_codes
1141:         ],
1142:         "rows_without_feature": {
1143:             "alias_of": [
1144:                 {"code": r["code"], "alias_of": r.get("alias_of"), "why": r.get("reason") or ""}
1145:                 for r in sorted(by_choice["alias_of"], key=lambda r: r["code"])
1146:             ],
1147:             "deferred": [
1148:                 {"code": r["code"], "why": r.get("reason") or "отложен на борда"}
1149:                 for r in sorted(by_choice["deferred"], key=lambda r: r["code"])
1150:             ],
1151:         },
1152:         "signature": {
1153:             "signed_by": "Petar",
1154:             "signed_at": "2026-09-06",
1155:             "basis": ("подписът на плана (§6 Б0 т. 1–12) върху решенията по sha256 на блоба; "
1156:                       "signed_by в Feature-ите става валидно точно с този подпис (Б0 т. 1)"),
1157:             "commit_of_this_file_belongs_to": "Petar1984 (D16 / G4 — изпълнителят го оставя стейджнат)",
1158:         },
1159:         "source_terms": {"openstreetmap": SOURCE_TERMS_OSM, "wikimapia": SOURCE_TERMS_WIKIMAPIA},
1160:         "union_crs": UNION_CRS,
1161:         "union_witness": union_witness,
1162:     }
1163: 
1164:     return {"type": "FeatureCollection", "_meta": meta, "features": features}
1165: 
1166: 
1167: # ---------------------------------------------------------------------------
1168: # Negative fixtures on the INPUT side
1169: # ---------------------------------------------------------------------------
1170: 
1171: def make_negative_fixtures(args: argparse.Namespace, out_dir: Path) -> list:
1172:     """Two input-side fixtures; each must make THIS script exit != 0."""
1173:     out_dir.mkdir(parents=True, exist_ok=True)
3: "board": "board.html (scratch preview, unsigned) + architect corrections on Petar's instruction",
4: "based_on": {
21:  "dobreva → wikimapia_union [5729380, 5729421] (Petar 07.09)",
22:  "vinitsa_sever → excluded (Petar 07.09: „го изключваме“; registry: deactivate the code)"
34:   "decided_by": "Petar (board, unsigned proba)",
35:   "decided_at": "2026-09-06T04:30:54.528Z"
46:   "decided_by": "Petar via Claude Architect (his instruction 06.09 ~07:00: „поправи ги заради мен“)",
47:   "decided_at": "2026-09-06T07:52:05"
58:   "decided_by": "Petar (board, unsigned proba)",
59:   "decided_at": "2026-09-06T04:31:09.909Z"
70:   "decided_by": "Petar (board, unsigned proba)",
71:   "decided_at": "2026-09-06T03:34:03.850Z"
82:   "decided_by": "Petar (board, unsigned proba)",
83:   "decided_at": "2026-09-06T04:34:24.138Z"
94:   "decided_by": "Petar (board, unsigned proba)",
95:   "decided_at": "2026-09-06T04:33:00.183Z"
106:   "decided_by": "Petar (board, unsigned proba)",
107:   "decided_at": "2026-09-06T04:34:27.453Z"
118:   "decided_by": "Petar (board, unsigned proba)",
119:   "decided_at": "2026-09-06T04:34:30.228Z"

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'src/build_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -ge 235 -and $i -le 287){ '"'{0}: {1}' -f "'$i,$_ } }
$p='"'.gitignore'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -ge 23 -and $i -le 30){ '"'{0}: {1}' -f "'$i,$_ } }' in C:\git\varna_3d
 succeeded in 62ms:
235:     "license_label", "license_terms", "parent_display", "parent_geometry_check",
236:     "raw_geometry_sha256", "url", "wm_id", "wm_ids", "wm_polygon_sha256", "wm_title",
237: )
238: ALL_FIELDS = tuple(sorted(set(D1_FIELDS) | set(EXTRA_FIELDS)))
239: 
240: 
241: def fail(check: str, message: str) -> None:
242:     print(f"✗ {check}: {message}")
243:     sys.exit(1)
244: 
245: 
246: def sha256_bytes(data: bytes) -> str:
247:     return hashlib.sha256(data).hexdigest()
248: 
249: 
250: def sha256_file(path: Path) -> str:
251:     return sha256_bytes(path.read_bytes())
252: 
253: 
254: def load_json_bytes(raw: bytes, what: str):
255:     if raw.startswith(b"\xef\xbb\xbf"):
256:         fail("вход", f"{what} започва с BOM")
257:     try:
258:         return json.loads(raw.decode("utf-8"))
259:     except Exception as exc:  # noqa: BLE001 - the reason must be visible
260:         fail("вход", f"{what} не е валиден UTF-8 JSON ({exc})")
261:     return None
262: 
263: 
264: def load_json_file(path: Path, what: str):
265:     if not path.exists():
266:         fail("вход", f"{what} липсва: {path}")
267:     return load_json_bytes(path.read_bytes(), f"{what} ({path})")
268: 
269: 
270: def read_decisions_blob(repo: Path, rev: str, path_in_repo: str) -> tuple[bytes, str]:
271:     """Read the exact blob Petar signs (Б0 т. 8).  Never the working tree."""
272:     try:
273:         raw = subprocess.run(
274:             ["git", "-C", str(repo), "show", f"{rev}:{path_in_repo}"],
275:             capture_output=True, check=True,
276:         ).stdout
277:     except subprocess.CalledProcessError as exc:
278:         fail("A1 блоб на решенията", f"git show {rev}:{path_in_repo} падна ({exc.stderr.decode('utf-8', 'replace').strip()})")
279:         raise
280:     digest = sha256_bytes(raw)
281:     return raw, digest
282: 
283: 
284: def git_author_of(repo: Path, rev: str, path_in_repo: str) -> str:
285:     out = subprocess.run(
286:         ["git", "-C", str(repo), "log", "--format=%an", "-1", rev, "--", path_in_repo],
287:         capture_output=True, check=False,
23: *.geojson
24: # ТРЕТОТО ИЗКЛЮЧЕНИЕ (ADR 010 D3, лот Б1): подписаните квартални граници. Стои
25: # СЛЕД `*.geojson`, иначе правилото на ред 23 го засенчва — същият капан като
26: # при `data/*` горе. Файлът е човешко решение, не производна: 61 полигона, всеки
27: # потвърден поименно от Петър на борда, вързани по sha към решенията. Загуби ли
28: # се, не се регенерира от нищо — сесията пред борда не се повтаря.
29: # Комитът му е на Petar1984 (D16 / G4); агент го оставя само стейджнат.
30: !data/quarters_signed.geojson

exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "rg -n --max-count 20 --max-columns 200 'write|unlink|open\\(' src/qa_no_cad_ids.py
"'$env:PYTHONDONTWRITEBYTECODE='"'1'
python src/qa_no_cad_ids.py" in C:\git\varna_3d
 succeeded in 1310ms:
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

codex
Две сглобявания в паметта възпроизвеждат staged SHA точно; трите input negatives падат по A9. Проверихме и неподписаната част на веригата: decisions 4 няма `attribution`, изискван от Б0.8. Добавянето му ще създаде нов SHA, който Петър трябва да подпише.

Остава и конкретна дупка в QA: подмяна само на `_meta.union_crs` с `EPSG:4326` минава зелено. Геометричният pin е защитен, но описанието на начина на построяване още не е.
exec
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$p='"'src/build_quarters_signed.py'
"'$i=0; Get-Content -Encoding UTF8 -LiteralPath $p | ForEach-Object { $i++; if($i -ge 1260 -and $i -le 1289){ '"'{0}: {1}' -f "'$i,$_ } }
git diff --name-only
git diff --cached --name-only' in C:\git\varna_3d
 succeeded in 52ms:
1265:     print(f"✓ {out_path} · {len(payload)} B · sha256 {sha256_bytes(payload)}")
1266:     print(f"  artifact_class = {meta['artifact_class']} · подпис: планът §6 Б0 + решения sha {meta['decisions_sha256'][:12]}…")
1267:     print(f"  Feature-и: {counts['features']} (wikimapia {counts['choice_wikimapia']} + "
1268:           f"обединение {counts['choice_wikimapia_union']} + "
1269:           f"declared_streets {counts['choice_declared_streets']}) · решения: {counts['decisions_rows']} "
1270:           f"(deferred {counts['choice_deferred']}, alias_of {counts['choice_alias_of']}, "
1271:           f"excluded {counts['choice_excluded']})")
1272:     print(f"  изключени поименно: {[e['code'] for e in meta['excluded']]} · "
1273:           f"обединения: {sorted(meta['union_witness'].get('by_code', {}))} в {meta['union_crs']}")
1274:     print(f"  registry_pending: {counts['registry_pending']} · родство по DAG: {len(meta['parent_child'])} двойки"
1275:           f" · без полигон: {meta['parent_child_without_polygon']}")
1276:     print(f"  район (нашите пет): {counts['features_with_our_district']}/{counts['features']}"
1277:           f" · свидетел АГКК: {meta['district_witness_agkk'].get('inside_one_district')} в точно един")
1278:     print(f"  автор на комита на този файл: Petar1984 (D16/G4) — изпълнителят го оставя стейджнат")
1279:     return 0
1280: 
1281: 
1282: if __name__ == "__main__":
1283:     sys.exit(main())
scratch/place_bodies/qa_place_bodies.md
warning: unable to access 'C:\Users\Petar/.config/git/ignore': Permission denied
data/quarters_signed.geojson

codex
**НЕГОДНО за приемане като подписан Б1 second run.** Двете поправки от S22 F2 работят, но подписът върху decisions 3 не подписва decisions 4. Има и възпроизведен пропуск в проверката на union provenance. Прегледът остана read-only.

1. **Write-set, commits и ограничения**

`git show --stat` потвърди:

| Commit | Променени файлове | Дословно съобщение |
|---|---|---|
| `63d077d6f717ccb44b8cdc435969d60b13ec8865` | само builder; +356/−24 | `build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)` |
| `8c262e9b272aceeb16d4f21503bd4ac92361f1e9` | QA и tests; общо +160/−12 | `gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)` |

И двата имат author/committer **`Claude Executor <executor@local>`**. Файловете са точно в разрешения write-set. **Съобщенията обаче не са дословните от подписания [план:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138)**; също `wikimapia_union`, `excluded` и 60 Features изискват изрично приемане на делтата.

[Index и worktree:1](C:/git/varna_3d/data/quarters_signed.geojson:1) са байт-еднакви: **295304 B; 60 Features = 58+1+1**, SHA256:
`4930f2043438edb9353fc5dc0f4d92cd92fc0248208c0f83783b991ca743f5c3`.

Спрямо `base_rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b`, worktree=HEAD=baseline за ledger `d5050f1cfb3d…`, identity `e8b4c836f602…`, places `329310f577e8…`, hotels `46a44ce82f15…`. Registry е чист и съвпада с pin `7d21740101a2…`; завареният чужд dirty файл също запазва началния SHA. [Пинове:55](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:55), [registry:242](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:242).

**Няма установено нарушение на no-push**, но локалното `49 ahead` не доказва историята на remote. `gh` върна HTTP401, `ls-remote` — authentication failure; текущият G19/PRIVATE остава непотвърден от тази сесия. G3 е зелен.

2. **S22 F2 и отрицателните проверки**

QA командата даде **exit 0, 18 проверки** след process-scoped `safe.directory`, без промяна на Git configuration.

Истинският blob на плана в `42b2635` възпроизвежда `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766`. C1 вече сравнява exact SHA, commit и path. `plan_sha_zeroed` дава **exit1/C1**; `district_spatially_wrong` — **exit1/C18**. [QA:105](C:/git/varna_3d/src/qa_quarters_signed.py:105), [fixtures:81](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:81).

Всички **30 отрицателни fixtures** падат по очаквания check; байтовете им съвпадат с генерираните в паметта.

Оригиналният unittest, със забрана за записи, завърши **exit1/Ran0**, защото [setUpClass:120](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:120) изтрива fixture директорията. Четирите read-only метода минаха; останалите пет сценария проверихме еквивалентно в паметта: две еднакви сглобявания, трите input negatives **A9/exit1**, неправилно output име **exit1**. Това не е оригинален suite exit0.

3. **S23-F1: честна signature chain**

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
tokens used
87,386
**НЕГОДНО за приемане като подписан Б1 second run.** Двете поправки от S22 F2 работят, но подписът върху decisions 3 не подписва decisions 4. Има и възпроизведен пропуск в проверката на union provenance. Прегледът остана read-only.

1. **Write-set, commits и ограничения**

`git show --stat` потвърди:

| Commit | Променени файлове | Дословно съобщение |
|---|---|---|
| `63d077d6f717ccb44b8cdc435969d60b13ec8865` | само builder; +356/−24 | `build: quarters_signed from decisions 4 (Добрева чешма union, Виница-север excluded)` |
| `8c262e9b272aceeb16d4f21503bd4ac92361f1e9` | QA и tests; общо +160/−12 | `gates: qa_quarters_signed — exact plan pin and spatial district check (Astra S22 F2)` |

И двата имат author/committer **`Claude Executor <executor@local>`**. Файловете са точно в разрешения write-set. **Съобщенията обаче не са дословните от подписания [план:138](C:/git/Fire_Varna/docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md:138)**; също `wikimapia_union`, `excluded` и 60 Features изискват изрично приемане на делтата.

[Index и worktree:1](C:/git/varna_3d/data/quarters_signed.geojson:1) са байт-еднакви: **295304 B; 60 Features = 58+1+1**, SHA256:
`4930f2043438edb9353fc5dc0f4d92cd92fc0248208c0f83783b991ca743f5c3`.

Спрямо `base_rev 8d60aebb365fb8e74ccc863d3b3db90b74180a3b`, worktree=HEAD=baseline за ledger `d5050f1cfb3d…`, identity `e8b4c836f602…`, places `329310f577e8…`, hotels `46a44ce82f15…`. Registry е чист и съвпада с pin `7d21740101a2…`; завареният чужд dirty файл също запазва началния SHA. [Пинове:55](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:55), [registry:242](C:/git/Fire_Varna/scratch/places_search/noshtna_pins_06.09.json:242).

**Няма установено нарушение на no-push**, но локалното `49 ahead` не доказва историята на remote. `gh` върна HTTP401, `ls-remote` — authentication failure; текущият G19/PRIVATE остава непотвърден от тази сесия. G3 е зелен.

2. **S22 F2 и отрицателните проверки**

QA командата даде **exit 0, 18 проверки** след process-scoped `safe.directory`, без промяна на Git configuration.

Истинският blob на плана в `42b2635` възпроизвежда `4ce6ea842a0acd12e4ed2005316190acdb032dec8191502696c3d0a249253766`. C1 вече сравнява exact SHA, commit и path. `plan_sha_zeroed` дава **exit1/C1**; `district_spatially_wrong` — **exit1/C18**. [QA:105](C:/git/varna_3d/src/qa_quarters_signed.py:105), [fixtures:81](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:81).

Всички **30 отрицателни fixtures** падат по очаквания check; байтовете им съвпадат с генерираните в паметта.

Оригиналният unittest, със забрана за записи, завърши **exit1/Ran0**, защото [setUpClass:120](C:/git/varna_3d/tests/test_quarters_signed_fixtures.py:120) изтрива fixture директорията. Четирите read-only метода минаха; останалите пет сценария проверихме еквивалентно в паметта: две еднакви сглобявания, трите input negatives **A9/exit1**, неправилно output име **exit1**. Това не е оригинален suite exit0.

3. **S23-F1: честна signature chain**

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
