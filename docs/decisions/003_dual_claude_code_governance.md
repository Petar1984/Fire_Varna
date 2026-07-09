# ADR 003 — Dual-Claude-Code Governance (retire Codex planner)

- **Status:** Accepted (Petar), 2026-07-09
- **Date:** 2026-07-09
- **Authors:** Petar (decision authority), Claude Code (draft & audit)
- **Supersedes:** the tri-agent / four-actor workflow in AGENTS.md (Codex as repo-aware planner)

## Context

The project ran a four-actor pipeline: chat-Claude (architect/auditor) → Codex (repo-aware planner) → Petar (sign) → Claude Code (executor) → chat-Claude (audit) → Petar (push). Codex was cross-vendor (OpenAI, `gpt-5.5`, read-only sandbox in `~/.codex/config.toml`). The cross-vendor tier added real friction — separate keys/CLI/config, no shared memory, no native subagent integration, and every handoff was a lossy serialization to text — for a marginal capability delta over Opus 4.8. The chief thing Codex provided was an independent (different-vendor) perspective, which is needed only rarely.

## Decision

Retire Codex from the planner role and run an **all-Anthropic (Claude Code) pipeline**, with **planning and execution kept in separate agents** and human sign-off gates preserved.

Roles (constant): **Planner** (Opus, read-only), **Researcher** (planner sub-phase, read-only), **Executor** (Opus), **Auditor** (Opus, read-only, adversarial), **Orchestrator** (Petar — sole push authority).

Chain: `Planner → GATE 1 (Petar signs) → Executor (local commit) → Auditor → GATE 2 (Petar reviews diff) → Petar pushes`.

- **Model:** Opus 4.8 in every role.
- **Topology:** a single **Task Risk Class** (Routine / Sensitive / Architectural) selects Variant B (orchestrator + role-locked subagents) or Variant A (separate sessions), and the research depth. Roles never change with class.
- **Planner ≠ Executor** is enforced structurally (separate contexts + tool permissions), not by discipline.
- **Independent perspective** (formerly Codex's value) is recovered via the adversarial Auditor and, in rare high-stakes/low-confidence research, a Tier-2 multi-model research escalation (ChatGPT/Gemini via claude-in-chrome), treated as untrusted data.

Full operating manual: `scratch/pipeline_reconfig_plan.md` (Varna_buildings repo, committed there). System Invariants: added to AGENTS.md (see `scratch/system_invariants_section.md` — also in the Varna_buildings repo).

## Consequences

**Positive:** one vendor/config/memory/permission surface; native subagent + Workflow orchestration; no copy-paste relay (single-session plan→approve→execute or file handoff); sign-off gates unchanged; `~/.codex` and `scratch/*codex*` become historical.

**Negative / accepted:** loss of genuine cross-vendor model diversity (mitigated by adversarial Auditor + occasional Tier-2 research); role separation now depends on correct agent/tool configuration rather than a physical read-only sandbox — hence the invariants and, optionally, a `git push` deny rule + role-locked agent definitions.

**Neutral:** Codex artifacts retained as historical record; not deleted.

## Rollout

Pilot in Fire_Varna (this ADR). Port to Varna_buildings after one real cycle validates the model.
