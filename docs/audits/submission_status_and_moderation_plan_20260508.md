# Submission Status, Moderation, And Operational Taxonomy Plan 2026-05-08

## Required Preamble

Request scope: read-only investigation and replacement plan for submission status, moderation, and operational taxonomy. Intended write target: `docs/audits/submission_status_and_moderation_plan_20260508.md`.

Deterministic inventory used: `AGENTS.md`, `CLAUDE.md`, `README.md`, `index.html`, `data/hydrants.json`, `field_reports.json`, `audit/apply_field_reports.py`, Worker audit snapshots, `docs/activeContext.md`, `docs/architecture/data_roadmap_20260508.md`, and related audit/plan docs.

Files read: same as inventory.

Negative findings: no `worker/` source directory, no `scripts/` directory, no dormant runtime status values beyond `verified` / `reported` plus absent fallback, no water-flow evidence in `field_reports.json`.

Declared metadata: `AGENTS.md` defines `verified` as physically confirmed, `reported` as damaged/missing/needs attention, absent as canonical; `docs/activeContext.md` records 23 verified, 2 reported, 6,057 canonical; roadmap already proposes `operational_status`.

Approval-gate check: Section A is current-sprint frontend fix. Section B is future Worker architecture. Section E is future schema/UI work. One logical change per commit remains required.

## Section A: Status Fix

`applyReports()` currently inserts polled `new_hydrant` reports with `status: 'verified'`, making unreviewed reports look trusted.

Patch for current sprint Commit 3:

```diff
-          status: 'verified'
+          status: 'reported'
```

Test: submit `new_hydrant`, wait for polling, confirm temporary pin is yellow and dedupe still works.

## Section B: Moderation Architecture

Current Worker GET `/issues` exposes open GitHub issues labeled `report`, including `pending-review`; frontend applies all returned reports.

Accepted architecture: M1 label gate.

- Add GitHub label `approved`.
- Public `/issues` returns only open issues with `report` + `approved`.
- `approved` wins even if `pending-review` remains.
- Prep commit extracts Worker source to `worker/`.
- Worker commit adds filter and bumps KV cache key.
- Optional frontend defense skips reports lacking `approved` if labels are present.

Test pending hidden, approved visible, closed hidden, CORS/cache/`since`/`limit` unchanged. Rollback via Cloudflare Worker version plus optional frontend revert.

## Section E: Status Taxonomy Expansion

### E1. Current Taxonomy

Current effective states:

| State | Data | Meaning |
|---|---|---|
| canonical | absent `status` | source record, not field-confirmed |
| reported | `status:"reported"` | needs attention |
| verified | `status:"verified"` | physically confirmed |
| unknown fallback | unrecognized status | canonical rendering |

The 23 verified records do not prove water flow. `field_reports.json` has no operational/water-flow field. Current `operational` form field exists only in damaged reports and is not mapped into marker state.

### E2. Options

Recommended option is T3: separate operational state from visual/existence status.

Rejected for v1: adding `operational` or `tested-*` directly to `status`, because that mixes existence trust with tactical function and makes the 23 verified records ambiguous.

### E3. Recommendation

Add flat optional fields:

```text
operational_status: "operational" | "non_operational" | "unknown"
last_inspection_date: "YYYY-MM-DD" | absent/null
```

Absence means unknown. Existing 23 verified records remain red and are not assumed tested.

### E4. Submission Flow

Extend both:

- `exists_confirmed`
- `new_hydrant`

Both flows ask `Работи ли?` with options:

```text
да
не
не съм проверявал, само видимо
```

Mapping:

```text
да -> operational_status="operational"
не -> operational_status="non_operational"
не съм проверявал, само видимо -> operational_status="unknown"
```

Rationale: firefighters confirming or discovering a hydrant may test it during the same visit; skipping the question loses valuable field data.

### E5. Existing Data Migration

No bulk update. Existing verified records stay `status:"verified"` with absent/unknown `operational_status`. Imported canonical records remain absent status and unknown operational state until future reports update them.

### E6. Implementation Plan

Files likely touched in taxonomy sprint:

- `index.html`: form fields, report object, polling merge, marker rendering, card detail.
- Worker: only if dashboard source does not preserve normalized `details.operational`.
- Docs: `AGENTS.md` and `activeContext.md` after implementation.

Rendering mapping for v1:

```text
operational_status="operational" -> green (.h-pin.operational)
operational_status="non_operational" -> yellow (.h-pin.reported)
status="reported" -> yellow (.h-pin.reported)
status="verified" with unknown operational_status -> red (.h-pin.verified)
absent status with unknown operational_status -> gray (.h-pin.canonical)
```

Both yellow states intentionally coexist in v1. They share the tactical meaning “needs attention, do not rely on it.” The distinction is shown in card detail after tap. Future shade differentiation can be considered if field feedback shows confusion.

New CSS class:

```css
.h-pin.operational { background:#2e7d32; color:white; }
```

Bulgarian legend/card wording is deferred to the Section E implementation sprint and is not a blocker for ratifying this architecture.

### E7. Test Plan

- `exists_confirmed` + `да`: approved poll makes pin green.
- `exists_confirmed` + `не`: approved poll makes pin yellow and card shows non-operational detail.
- `new_hydrant` + `да`: after approval, temporary/new pin can become green.
- visible-only option leaves operational state unknown.
- Existing 23 verified stay red.
- Canonical records stay gray.
- Old app builds ignore `operational_status`.

### E8. Rollback

Revert taxonomy sprint commits. Since no bulk migration is planned, rollback is mostly code-only. Any records with new operational fields can keep them harmlessly or have fields removed in a small cleanup commit.

## Section F: Sequencing

1. Current sprint Commit 3: Section A one-line `reported` fix.
2. Separate moderation sprint: Worker extraction plus M1 approval gate.
3. Separate taxonomy sprint: T3 operational fields plus presence/new-hydrant flow extension.

Section A still ships now. It remains correct after taxonomy expansion because unreviewed `new_hydrant` reports are neither verified nor operational. Do not introduce a placeholder value and do not block current sprint completion on Section E.

## Section G: Taxonomy Decisions

Resolved:

- Simple 3-state operational model.
- Extend `exists_confirmed`.
- Also extend `new_hydrant`.
- Track last test date only; no automatic expiry yet.
- `reported` and `non_operational` share yellow in v1.

Deferred but not gating:

- Exact Bulgarian legend/card wording.
- Future shade differentiation for yellow states.
- Future expiry rule, such as six months.
