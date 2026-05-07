# Governance Proposal 2026-05-08

Target file: `docs/audits/governance_proposal_20260508.md`

Read in full: `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/activeContext.md`, `docs/plans/sprint_1_5_polish.md`, `docs/plans/commit_15_worker_get.md`.

Additional evidence read: `audit/apply_field_reports.py`, `geo_fire_hydrants.prj`, `wfsrequest.txt`.

## 1. Redundancy Audit

Canonical homes:

- `AGENTS.md`: stable project rules, constraints, data policy, tri-agent workflow.
- `docs/activeContext.md`: current live state, exact sizes/counts, deployed Worker version, sprint status.
- `CLAUDE.md`: Claude Code executor-only rules and verification checklist.
- `README.md`: public/user-facing overview, access/use instructions, and short developer pointer.

Diff-style proposals:

```diff
# AGENTS.md § Windows Dev Environment
  Keep full Defender exclusions, primary workflow, fallback recovery, and monthly check.

# CLAUDE.md § Windows Dev Environment
- Defender exclusions applied (2026-05-06): ...
+ See [AGENTS.md § Windows Dev Environment](AGENTS.md#windows-dev-environment).
```

Rationale: `AGENTS.md` and `CLAUDE.md` duplicate this section nearly verbatim; `activeContext.md` already uses the better pointer pattern.

```diff
# AGENTS.md § Report Flow
  Keep canonical Worker/report architecture.

# docs/activeContext.md
  Keep live endpoint/version/cache details only.

# CLAUDE.md § Report Flow
- Reports are submitted via `fetch` POST...
+ See [AGENTS.md § Report Flow](AGENTS.md#report-flow) and
+ [activeContext current state](docs/activeContext.md#current-state).

# README.md
- Signal is sent by Viber / Telegram / SMS.
+ Signal is submitted through the app report flow.
```

Rationale: README currently contains a factually wrong report transport; Worker details repeat across governance docs.

```diff
# AGENTS.md § Hard Constraints
- Current exact byte counts for `index.html`, `data/hydrants.json`, or first load.
+ Keep only size policy: first load <= 1 MB ideal, 2 MB hard cap.
+ Current byte counts are canonical in [docs/activeContext.md](docs/activeContext.md#current-state).

# CLAUDE.md § Hard Rules
- Duplicate static hosting / size / UI wording / dependency rules.
+ Project-wide constraints are canonical in
+ [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints).
+ Claude Code must stop if an approved plan violates them.
```

Rationale: exact byte counts drift. Petar decided current-state byte counts belong only in `docs/activeContext.md`; `AGENTS.md` keeps the stable policy.

```diff
# AGENTS.md § Tri-Agent Workflow
  Keep roles and approval gates.

# README.md
  Keep short public summary only.

# Future plan docs
+ Approval gates: follow
+ [AGENTS.md § Tri-Agent Workflow](AGENTS.md#tri-agent-workflow)
+ unless this plan explicitly adds narrower gates.
```

Rationale: approval gates are repeated in README, CLAUDE, and plan docs; one canonical rule makes silent divergence reviewable.

```diff
# AGENTS.md § Wrong-Location Ingest Rule
  Keep canonical table and wording.

# CLAUDE.md § Field Report Ingest Rules
- Duplicate wrong_location/new_hydrant bullets.
+ See [AGENTS.md § Wrong-Location Ingest Rule](AGENTS.md#wrong-location-ingest-rule).
+ Claude Code must stop before data edits unless the approved plan names affected report IDs.
```

Rationale: this rule is safety-critical and should not have multiple near-copies.

```diff
# README.md
- `index.html` is self-contained and opens directly in browser.
- One standalone HTML file (~672 KB).
- Total hydrants: 3,934.
+ App is static, but local testing must use HTTP because `data/hydrants.json`
+ is fetched at runtime.
+ Current technical counts/sizes live in
+ [docs/activeContext.md](docs/activeContext.md#current-state).
```

Rationale: README conflicts with current fetch architecture and 6,079-record runtime dataset. These diff lines are illustrative of meaning; final README edits must preserve Bulgarian prose.

## 2. README.md vs activeContext.md Role Separation

README representative excerpts: public Bulgarian description, mobile install/use steps, developer pointer to `AGENTS.md` / `CLAUDE.md`.

activeContext representative excerpts: last updated commit `7412878`, Worker deployed version `50c2b2d2`, Sprint 1.5 shipped state.

Finding: not inherently redundant, but README contains stale current-state facts.

Proposed headers:

```diff
# README.md, near top
+ > Audience: firefighters, volunteers, first-time repo visitors.
+ > Purpose: explain what the app does and how to access/use it. Not canonical
+ > for exact dataset counts, byte sizes, Worker versions, or sprint state.

# docs/activeContext.md, near top
+ > Audience: Petar and AI agents resuming work.
+ > Purpose: canonical current repo/runtime state. If this conflicts with README,
+ > AGENTS.md, or CLAUDE.md on current state, this file wins.
```

Rationale: README remains the approachable front door; activeContext remains the operational ledger.

## 3. Codex Operating Protocol

Placement: new section in `AGENTS.md` after `## Tri-Agent Workflow`.

```diff
+ ## Codex Operating Protocol
+
+ ### Scope Declaration
+ Codex may use a task-scoped inventory when the user request is narrow. The
+ preamble must declare the inventory scope and cite the user request or brief
+ that defines it. Files outside the declared scope may not be referenced unless
+ Codex explicitly expands the scope, explains why, and updates the inventory.
+ Verification: reviewer checks that all referenced files fit the declared scope.
+
+ ### Deterministic Inventory First
+ Before any plan/proposal that references files, run a deterministic filesystem
+ inventory for the declared scope and quote it verbatim in the preamble. No file
+ may be referenced unless it appears in that inventory.
+ Verification: reviewer checks every referenced path against the inventory.
+
+ ### Explicit Negative Findings
+ For every pattern/extension/category in scope, report matches or
+ `no files matching X found in scope Y`.
+ Verification: reviewer checks the request scope matrix for omissions.
+
+ ### Declared Metadata Beats Heuristics
+ Quote declared metadata verbatim and treat it as authoritative: `.prj` CRS,
+ headers, manifests, sidecars, request logs, provenance records. Heuristics are
+ fallback only when metadata is absent, unreadable, or contradicted.
+ Verification: metadata files in inventory must be quoted before inferred CRS,
+ schema, provenance, or lineage.
+
+ ### Binary File Reading Rule
+ Referencing a binary/source archive requires content inspection, not filename
+ inspection. KMZ means unzip/list archive and inspect inner KML/doc.kml. DBF/SHP
+ means inspect schema and metadata with `ogrinfo -al -so` / `ogrinfo -al` from
+ GDAL, QGIS equivalent tooling, or a documented DBF/SHP parser. If required
+ tooling is unavailable, state the file is unread and do not infer its contents.
+ Verification: plan lists tool used, command, and inspected inner files/layers.
+
+ ### Referenced Files Must Be Read
+ If a file is referenced, its content must have been read in the same session.
+ Path-name matching is not reading. Preamble must list `Files read`.
+ Verification: reviewer compares referenced paths against `Files read`.
+
+ ### Non-ASCII Encoding Gate
+ Before committing or handing off files containing non-ASCII text, especially
+ Cyrillic, verify UTF-8 round-trip integrity and scan for mojibake.
+
+ Per-file detection form:
+ `Select-String -Path <path> -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8`
+
+ Note: this regex uses Unicode escape notation (\u00D0 = Ð,
+ \u00D1 = Ñ, \u00C2 = Â) rather than literal characters so this
+ proposal file passes its own mojibake scan. When invoking the
+ scan from a shell, either form is functionally equivalent.
+
+ Repo-wide pre-commit detection form:
+ `git diff --cached --name-only --diff-filter=ACMR | ForEach-Object { Select-String -Path $_ -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8 }`
+
+ Also recommend adding `.editorconfig` with `charset = utf-8` and a git
+ pre-commit hook that blocks staged text files containing mojibake markers.
+ Verification: handoff notes include encoding check output; reviewer may rerun
+ the command or hook.
```

Rationale: addresses the 2026-05-08 failures: incomplete inventory, missing negative findings, metadata ignored, filename inference, and encoding risk. Current `audit/apply_field_reports.py` produced no output for the verified mojibake command; because it is untracked, repair history cannot be proven from git.

## 4. Tri-Agent Workflow Strengthening

```diff
# AGENTS.md § Tri-Agent Workflow
+ ### Codex Plan Preamble Checklist
+ Every Codex plan/proposal must include: request scope, deterministic inventory,
+ files read, negative-findings matrix, quoted declared metadata, decision ledger,
+ approval-gate check, and open questions.
+
+ Decision ledger schema:
+ | Decision | Source | Evidence | Reversibility | Approval status |
+ |---|---|---|---|---|
+ | Keep Worker source external until commit 17 | Repo evidence | `AGENTS.md` says live Worker is canonical; `activeContext.md` lists commit 17 optional extraction | Reversible by adding `worker/` later | Existing approved project state |
```

Rationale: “Codex cannot make architectural decisions silently” becomes auditable only when each decision has source, evidence, reversibility, and approval status.

## 5. CLAUDE.md Scope Reduction

Keep in `CLAUDE.md`: executor role, code style, implementation gotchas, verification checklist, commit/reporting expectations.

Move/cross-reference:

```diff
- Hard Rules duplicated from AGENTS.md
+ See [AGENTS.md § Hard Constraints](AGENTS.md#hard-constraints).

- Field Report Ingest Rules
+ See [AGENTS.md § Wrong-Location Ingest Rule](AGENTS.md#wrong-location-ingest-rule).

- Report Flow
+ See [AGENTS.md § Report Flow](AGENTS.md#report-flow) and
+ [activeContext](docs/activeContext.md#current-state).

- Windows Dev Environment
+ See [AGENTS.md § Windows Dev Environment](AGENTS.md#windows-dev-environment).

- What Requires Going Back To Humans
+ See [AGENTS.md § Tri-Agent Workflow](AGENTS.md#tri-agent-workflow).
```

Add linkrot rule:

```diff
+ After any governance section rename, run grep/rg for old section names and
+ update Markdown anchor links in the same docs pass.
```

Rationale: cross-references must be anchor links, and section renames need a required grep check.

## 6. Plan File Findings

`sprint_1_5_polish.md` finding: no major governance gap. It correctly used approval phases and named Petar approval for Bulgarian wording. Minor improvement: future plans should label byte budgets as hard or soft so a planning cap is not confused with the 2 MB hard constraint.

`commit_15_worker_get.md` finding: mostly sound historical plan. Governance improvement for future plans: avoid `git reset --hard` / `git clean -fd` rollback recipes unless Petar explicitly requests destructive cleanup; prefer `git revert` or dashboard rollback steps. The plan correctly stated Worker source remained in Cloudflare dashboard and extraction was out of scope.

## 7. Required README Corrections In Same Future Doc Pass

The approved doc-update pass must also update `README.md`. The examples below are illustrative of meaning; Claude Code must translate/preserve the final corrections in natural Bulgarian.

```diff
- Tap on 🚨 sends via Viber / Telegram / SMS.
+ Reports are submitted through the app report flow.

- `index.html` is self-contained and opens directly in browser.
+ Local testing must use HTTP because `data/hydrants.json` is fetched at runtime.

- One standalone HTML file (~672 KB).
+ Remove exact size or point to `docs/activeContext.md`.

- Total hydrants: 3,934.
+ Replace with 6,079 or remove exact count and point to `docs/activeContext.md`.
```

Rationale: these README facts are currently wrong and should not wait for a later cleanup.

## 8. Resolved Decisions

- Exact byte counts are removed from `AGENTS.md`; size policy remains there. Current byte counts are canonical only in `docs/activeContext.md`.
- Task-scoped inventory is acceptable when the preamble declares scope with explicit citation to the user request or brief. Outside-scope files cannot be referenced without scope expansion.
- README factual corrections happen in the same doc-update pass and preserve Bulgarian text.

## 9. Open Questions

1. `docs/audits/` does not exist. The executor should create it only when applying this approved proposal document.
2. The reported historical mojibake in `audit/apply_field_reports.py` is not reproducible in the current checkout; file is untracked, so git cannot prove repair timing.
3. `audit/apply_field_reports.py` writes to `index.html` embedded JSON plus `field_reports.json`, but canonical runtime is `data/hydrants.json`. Separate code audit needed before next data sprint.
