# Fire_Varna Governance Migration — plan.md

> **Status:** ✅ SIGNED (Gate 1) by Petar — 2026-07-09. Executor may proceed. Local commits only — no push.
> **Risk class:** 🔴 Architectural (governance change → ADR) → **Variant A**, executed by the Executor after sign-off.
> **Model:** Opus everywhere. **Scope:** governance docs only — zero product code/data. **Never push** (Petar pushes after diff review).
> **Author:** Planner (Claude Code). Master model: `Varna_buildings/scratch/pipeline_reconfig_plan.md`.

Two commits in one cycle (cleaner diffs for review).

---

## Commit 1 — retire Codex planner → Claude-Code Planner

| File | Exact change |
|------|--------------|
| `CLAUDE.md` | Role matrix (~lines 10–19): replace the tri-agent Decides/Plans/Edits table with the 5-role table (Planner/Researcher/Executor/Auditor/Orchestrator). Line 20: "approved plan from **Codex**" → "approved plan from the **Planner** (Opus, read-only), signed by Petar". Line 123: "approved **Codex** plan" → "approved **Planner** plan signed by Petar". |
| `AGENTS.md` | "## Tri-Agent Workflow" table (~126–134): replace with new roles (drop the Codex row; Planner = Claude Code read-only). Approval gates (~140,142): "fresh **Codex** analysis" → "fresh **Planner** analysis"; "**Codex** plan" → "**Planner** plan (signed by Petar)". "Codex Operating Protocol" + "Codex Plan Preamble Checklist" (~144–201): **re-attribute** to "Planner …" (keep the discipline verbatim, swap the name). Fix the section anchors referenced from `CLAUDE.md` and `README`. |
| `README.md` | Lines ~85–93 (BG): remove Codex; describe the Planner/Executor Claude-Code split. **Bulgarian wording → Petar reviews.** |
| `docs/decisions/003_dual_claude_code_governance.md` | **NEW** — finalize from `Varna_buildings/scratch/fire_varna_adr_003_draft.md`. |
| `AGENTS.md` | Append the **System Invariants** section (from `Varna_buildings/scratch/system_invariants_section.md`). |

**Commit 1 message:**
`docs(governance): adopt dual-Claude-Code pipeline (ADR 003); retire Codex planner role`

## Commit 2 — harmonize Fire_Varna guardrails UP to Varna_buildings

Add to `CLAUDE.md` / `AGENTS.md` (each mirrors a rule Varna_buildings already has):
- 🔴 **Never-push rule** + re-attribute the § Windows Dev "edit + commit + **push**" line to Petar only.
- **PII gate** — field-report data reject-by-default / scrub before persist or issue creation.
- **Secrets hygiene** — "never commit secrets / verify `.gitignore`"; enumerate Worker credential files as ignored.
- **Destructive-op gate** — "investigate unexpected state before deleting/overwriting".
- **Cross-repo isolation** — symmetric "do not touch the other repo's checkout".
- **No automated commits** + minimal per-commit verification checklist.
- Reconcile the declared working dir to one canonical path (`C:\git\Fire_Varna`).
- **Fix defect:** first-load cap stated as both 5 MB (AGENTS.md) and 2 MB (CLAUDE.md) → reconcile to **5 MB** (Petar's Gate-1 decision): update `CLAUDE.md` 2 MB → 5 MB.

**Commit 2 message:**
`docs(governance): harmonize Fire_Varna guardrails to Varna_buildings (push/PII/secrets/destructive/cross-repo)`

## Acceptance gates (Executor must pass before reporting done)
1. `grep -ri "codex" Fire_Varna` (tracked) → only historical/scratch/ADR mentions remain; **zero** active governance references to Codex as planner.
2. Both commits **local only**; `git status` clean; **NO push**; **NO** product-code/data files changed (only `CLAUDE.md`, `AGENTS.md`, `README.md`, new ADR).
3. Diff presented to Petar for Gate-2 review before push.

## Gate-1 — SIGNED by Petar (2026-07-09)
1. ✅ Two-commit plan approved as written.
2. ✅ First-load cap = **5 MB** — reconcile `CLAUDE.md` 2 MB → 5 MB in Commit 2.
3. ✅ Rephrase README Bulgarian **now**; Petar reviews it at the Gate-2 diff.
