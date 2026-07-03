# ADR 001 — Fire_Varna approximate address search results

**Date:** 2026-07-03 · **Status:** Accepted (2026-07-03, Petar)

Supersedes nothing. First ADR in this repo. Materialises D1–D9 from the
Address-fill Phase-B plan (`Varna_buildings/scratch/address_fill_phase_b_codex_plan.md`
§8) after Petar signed the three B2 decisions (§9 of the B2 plan).

## Context

Address-fill Phase A measured `22,360` true-missing official ГРАО addresses that
are not discoverable as confirmed КАИС building addresses. Phase B B0/B1 produced
a public-safe `approx_addresses_v1` bundle carrying only GRAO street name, house
number, quarter, WGS84 candidate position, confidence, and source — no cadnum,
КАИС, or private evidence (B1 leak scan `public_safe=true`). The signed tranche
(`balanced_default`) is **8,802 rows** (raw 890,399 B, gzip9 92,506 B, SHA256
`0b21ed9acc918a1f7fc1009af1cee74682821df93d29f9681ffd91edfcc7ea8b`).

Fire_Varna is mobile-first, Bulgarian-only, static GitHub Pages, emergency-use.
Its address search already lazy-loads `data/search_index.json` + `data/address_rows.json`
on first focus (Cache API namespace `fire-varna-search-v2`). An approximate
candidate must never look like a verified building or a hydrant; a fire crew must
read it as under-stated confidence.

## Decision

**D1 — New result class.** A distinct search result class `kind:"approx"` /
"приблизителен адрес". It is not a building, entrance, parcel, or hydrant. Exact
existing search results keep their current ranking and display.

**D2 — Honest Bulgarian label (SIGNED, §9.3).** Dropdown chip: `прибл. адрес`.
Popup title: `≈ <улица> №<номер>`. Popup subtitle:
`Официален адрес без потвърдена сграда`. For low confidence, append
`Позицията е ориентировъчна.` These four strings are final; no further wording
approval is required.

**D3 — Distinct marker.** A visually distinct approximate-address `L.divIcon`
marker bearing `≈` — not the teal exact-search pin, not a hydrant pin. It opens a
small nav popup, not the building detail sheet.

**D4 — Navigation.** Waze / Пеша / Карта / Street View buttons navigate to the
candidate WGS84 position (the shared `buildNavActions`). No "Докладвай" action is
added for approximate addresses.

**D5 — Feature flag and fallback.** The feature is gated behind a single flag
`APPROX_ADDRESS_SEARCH_ENABLED`. If the flag is false, the file is missing, the
fetch fails, the JSON/schema is invalid, a leak/coordinate check fails, Fire_Varna
search behaves exactly as it does today ("Няма съвпадения").

**D6 — Lazy loading (B0 = lazy).** B0 measured lazy over inline. The approx
bundle is **not** fetched on focus and **not** fetched while exact search returns
matches. It loads only after exact search returns zero matches, is parsed once,
and is cached through the Cache API under a **new** namespace
`fire-varna-approx-addresses-v1`. It is never appended to `index.html` or to the
first-load hydrant data.

**D7 — Ranking.** Exact address/building/entrance/parcel results rank above
approximate results. Approximate results appear only when there is no exact
match. Within the approx set, ranking is match quality, then confidence, then
source, then stable order.

**D8 — Alias rows (`target_g`: approved v1.1 extension, PENDING re-sign).** Strict
v1 ships no public target id — the 176 alias rows render as approximate-address
results at the validated public pin (`source:"alias"`). Petar has approved a
public opaque `target_g` for validated alias rows, but only as a **v1.1** bundle
re-emit after a separate re-signing; until then `allow_public_target_g_for_alias`
stays false and the emitter refuses it. The opaque `g` is admissible only because
the same `g` already ships in Fire search results; cadnum/КАИС/private evidence
remain forbidden.

**D9 — Hydrant layer untouched.** No change to hydrant data, nearest-hydrant
ranking, report flow, or polling. Selecting an approximate address re-anchors the
Top-5 nearest hydrants at the candidate position via the existing
`anchorHydrantsAt` — the fire-relevant behaviour Petar signed (§9.2) — a
read-only use of the hydrant layer; the hydrant dataset is not mutated.

## Status (as-executed)

Accepted. Implemented in Fire_Varna B2 (this cycle): bundle published to
`data/approx_addresses_v1.json`; the approx result class wired into the existing
address-search IIFE behind `APPROX_ADDRESS_SEARCH_ENABLED`; exact search
unchanged; fallback = today's behaviour. See the B2 commit series below.

## Key invariants & commits

- Public bundle contains no cadnum/КАИС/raw/private fields (B1 leak scan + a
  client-side re-validation on load).
- Missing file or disabled flag equals today's behaviour; exact search never
  regresses (approx fires only on zero exact, and never fetches otherwise).
- First-load mobile budget unchanged: the approx bundle is lazy, never first-load
  or inlined into `index.html`.
- B2 commit series (LOCAL, not pushed): commit 0 baseline docs, commit 1 this
  ADR, commit 2 bundle publish, commit 3 search integration, commit 4 tests +
  verification.
- Source design: `Varna_buildings/scratch/address_fill_phase_b_codex_plan.md`
  (§6 bundle, §8 ADR) and the B2 plan
  `Varna_buildings/scratch/address_fill_phase_b2_codex_plan.md`.
