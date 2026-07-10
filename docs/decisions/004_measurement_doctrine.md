# ADR 004 — Measurement Doctrine (references Varna_buildings ADR 058)

- **Status:** Accepted (Petar), 2026-07-10
- **Date:** 2026-07-10
- **Authors:** Petar (decision authority), Claude Code (draft & audit)
- **References:** Varna_buildings ADR 058 — the shared Measurement Doctrine (source authority model, terrain-eyes ToS, street-name dispute rule)

## Context

Fire_Varna and Varna_buildings share a measurement / authority discipline: how source disagreements are escalated, what confidence a canonical data mutation requires, and how private aids (municipal map, Google Street View terrain-eyes) may and may not be used. Varna_buildings canonized this as ADR 058 (Measurement Doctrine), with the per-source authority table living once in its `architecture_v2.md` § Per-attribute authority and the protocol in its `AGENTS.md` § Measurement Doctrine. To keep the two repos structurally identical in governance — as ADR 003 did for the pipeline — Fire_Varna adopts the same doctrine **by reference**, not by copy, and specializes the source palette per-repo.

## Decision

Adopt the Measurement Doctrine of Varna_buildings ADR 058 as the shared protocol for Fire_Varna, with the source palette specialized to this repo.

- **D1 — Shared protocol (by reference, not copy).** The discrepancy / escalation chain (live registers → m6000 → Google terrain-eyes → Petar), the confidence rubric (HIGH / HIGH-dispute-class / MEDIUM / LOW), the acceptance floor (Option A: HIGH, or MEDIUM + per-item Petar sign-off, or STOP → Petar), the UNRESOLVED branch, and the gates MD-1…MD-5 are defined once in Varna_buildings ADR 058 + its AGENTS.md § Measurement Doctrine. Fire_Varna does **not** restate the authority table (Inv-10).
- **D2 — Terrain-eyes ToS (identical, non-negotiable).** Google Street View is a break-glass, read-only, Petar-supervised aid that may only REFUTE / DOWNGRADE confidence or TRIGGER a field re-check — never the sole/decisive basis for a stored-value change, never lifted / traced / cached, never fed back to OSM. Fire_Varna IS a mapping service, so the consumer-ToS constraint binds here too.
- **D3 — Fire palette (per-repo).** Ingested / canonical Fire sources: `vik`, `national`, the `etr_*` municipal hydrant registers, and `field_report` submissions (PII-gated, reject-by-default). Rendering: the OSM PMTiles offline basemap (ADR 002). Aids (never canonical, never a determinism artifact): Google terrain-eyes and field site-photos. A hydrant coordinate mutates only on the acceptance floor; a terrain observation may trigger or refute a `wrong_location` review but never silently rewrites `coords`.
- **D4 — Gates carry over.** MD-1 (clear the floor before a canonical mutation), MD-2 (no aid-derived coordinate in the shipped `data/hydrants.json`), MD-3 (≥2-source HIGH), MD-4 (external claim carries source + date), MD-5 (terrain text-only, PII-clean, no lifted Google geometry) apply to `data/hydrants.json` mutations exactly as they do in Varna_buildings.

## Consequences

**Positive:** one measurement discipline across both repos; field-report and terrain observations have an explicit, ToS-safe authority ceiling; the acceptance floor makes a canonical hydrant-coordinate change auditable and reversible.

**Neutral:** the authority table is not duplicated here (Inv-10) — read Varna_buildings ADR 058 + its `architecture_v2.md` § Per-attribute authority for the canonical allocation.

## Rollout

Adopt immediately as governance (docs only; no product code, dataset, or Worker change). `AGENTS.md` and `CLAUDE.md` gain a pointer to this ADR. Local commit only; Petar pushes.
