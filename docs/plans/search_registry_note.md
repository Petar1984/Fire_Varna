# Plan — Address-search registry note (one Bulgarian line in the results dropdown)

**File:** `docs/plans/search_registry_note.md` · **Date:** 2026-08-12 · **Status:** DRAFT — AWAITING PETAR SIGNATURE (Gate 1)
**Author:** Planner (Claude Code, read-only). The Planner cannot write this file; Petar/Executor saves the returned content verbatim, then the Executor implements it.
**Origin:** Petar's decision of 12.08.2026 recorded at `scratch/patch_live_osm_audit_20260811.md:3-10` — the 41-row street-name patch is rejected, the basemap is rebuilt pure-OSM at the next build, address search stays on the official register, and the name mismatch is accepted consciously. This plan only *tells the user* that.

## 1. Risk classification — 🟢 Routine

| Trigger | Fired? | Evidence |
|---|---|---|
| ADR / architecture / schema / governance / flag / publish / cross-repo | NO | One CSS rule. `BASEMAP_PMTILES_ENABLED` and `APPROX_ADDRESS_SEARCH_ENABLED` untouched; no push, no deploy, no basemap rebuild. |
| Core pipeline logic / data transform / committed data | NO | Zero writes under `data/**`; zero JS; search ranking, dedup and selection untouched. |
| Multi-file in one subsystem | NO | `index.html` (CSS block 1045-1119) + this plan doc. |
| Non-trivial logic that would not fail loudly | NO | Failure mode is purely visual and is caught by gate G6 at 375px. |
| UI wording change (Petar-approval gate, AGENTS.md § Dual-Claude-Code Workflow) | **YES** | Satisfied *by* the Gate-1 signature: Petar picks one wording from §4; the Executor may not invent or edit a string. |

**Topology:** Variant B. Chain: Petar signs (Gate 1) → Executor local commit → gates G0-G7 → Petar reviews diff (Gate 2) → Petar pushes. Agents never push.

## 2. Scope, inventory, files read, negative findings

**In scope:** one informative Bulgarian note inside the open address-search dropdown, in `index.html` CSS only. **Nothing else.**
**Files read this session:** `AGENTS.md`; `CLAUDE.md`; `scratch/patch_live_osm_audit_20260811.md` (1-80); `index.html` (758-822, 1020-1119, 1570-1599, 4975-5003, 5310-5340, 5340-5449, 6085-6190, 6228-6257 + greps for `resultsEl|showStatus|renderCombined|hideResults`, `search-bar|addrSearchResults|search-results`, `dev-notice|headerH`); `sw.js` (grep `CACHE|index.html|VERSION`); `docs/activeContext.md` (grep); `docs/plans/sw_cache_lifecycle_fixes.md` (1-40). Inventories: `docs/plans/*.md` (6 files), `tests/*.py` (6 files), root `*.js` (8 files).
**Negative findings:** no existing note/footer element in `.search-bar` (all 8 `search-bar|addrSearchResults|search-results` hits are accounted for above); **no test file reads `index.html`** (`tests/*.py` = hydrant core, apply-parity, ETR KMZ, approx bundle, basemap manifest, golden fixture) → the unittest gate G4 is a *non-regression* gate only and proves nothing about the note; **no `sw.js` change is needed** — the worker is registered only when the PMTiles capability is active (`sw.js:5-7`, flag false) and app-shell navigations are network-first (`sw.js:178`).
**Declared metadata (quoted, authoritative):** `docs/activeContext.md:12` — "index.html: ~417,5xx worktree bytes (2e2bb43 measured 417,515 + one-line flag flips)". The Planner has no shell this session, so the exact byte baseline is delegated to Executor gate **G0** and must be recorded before the first edit (measure-first).

**Decision ledger**

| Decision | Source | Evidence | Reversibility | Approval |
|---|---|---|---|---|
| Basemap stays pure OSM; search stays on the official register; mismatch accepted | Petar, 12.08.2026 | `scratch/patch_live_osm_audit_20260811.md:3-10` | n/a (decision, no code) | Given |
| Note rendered as CSS generated content, not a DOM node | Planner measurement | 5 `replaceChildren` wipe points: `:5000`, `:5320`, `:5323`, `:5382`, `:6100` | `git revert` of one commit | **Pending Gate 1** |

## 3. Placement — chosen, with rationale and rejected alternatives

**Chosen:** a muted footer line rendered as `.search-results::after` with `position: sticky; bottom: 0`, pinned to the bottom edge of the **open** dropdown (`#addrSearchResults`, `index.html:1592`; box styled at `:1060-1066`). One new CSS rule, placed immediately after `.search-results.visible { display: block; }` (`:1066`), with a short *why* comment.

**Rationale.** (a) *Survives re-renders by construction.* `renderResults` (`:5368-5384`), `renderCombined` (`:6100`), `showStatus` (`:5321-5324`), `renderCoordRow` (`:4993-5003`) and `hideResults` (`:5320`) each call `resultsEl.replaceChildren(...)`; a generated box is not a child node, so no render path — present or future — can drop it. (b) *Visible in every state that matters*, including the „Няма съвпадения" empty state reached from `:5374` and `:6093` — precisely the moment a firefighter wonders whether the street name is the problem. (c) *Zero JS, zero markup, zero layout math.* The header stack keeps its measured height, so the hard-coded overlay offsets (`--dev-banner-h` note at `:763-769`, `headerH = 150` at `:5727`) stay valid. (d) *Diff is additive and confined to one CSS block* → trivially auditable and `git revert`-able.
**375px:** dropdown box = 355px wide (`left/right: 10px` inside a full-bleed `.search-bar`), note padding 12px → ~331px of text at 12px/1.35 ⇒ 2 lines ≈ 36px, inside the existing `max-height: 50vh` box. The note is informational and not tappable, so the ≥44px touch-target rule does not apply.
**Byte cost:** rule + comment ≈ 420-600 B, plus the chosen wording (Cyrillic = 2 B/char, see §4) ⇒ **≈ 550-800 B**; cap set at 1,200 B (G2). Negligible against the 5 MB first-load cap.
**Accepted trade-offs:** generated text is not selectable, and Chrome exposes it to assistive tech as static text inside `role="listbox"` — the box already carries non-option children (`.asr-group-header`, `.asr-status`), so this adds no new class of a11y defect; the note also appears above a pasted-GPS row (`:4993`), where it is harmless.
**Authorized fallback (no re-plan needed):** if sticky misbehaves at 375px, delete `position: sticky; bottom: 0;` from the same rule — the note then sits at the end of the list. **Any other fix = STOP.**

**Rejected alternatives**
1. *Real DOM child appended by each render path* — 4 insertion points plus every future one; one forgotten path silently loses the note, and it drags the diff into the JS render layer. Rejected: fragile, wider blast radius.
2. *Wrapper `.search-panel` + sibling `.search-note`, shown via `.search-results.visible + .search-note`* — cleanest a11y (note outside the listbox), but it moves `top / left / right / z-index / max-height` geometry off `.search-results` and adds markup, i.e. real layout-regression risk for a one-line note. Rejected on cost/benefit; documented as the upgrade path if a11y ever demands a real node.
3. *Always-visible static line under `#addrSearchInput`* — grows `.search-bar` by ~20px, invalidating the hard-coded `150px` overlay offsets and `headerH = 150`, and it is permanent visual noise on a 3-row emergency header. Rejected.
4. *One-time dismissible hint (the `#devNotice` sessionStorage pattern, `:1570-1573` / `:6234-6257`)* — new JS, new state, new 44px dismiss target; once dismissed it is absent exactly when a mismatched result is being read. Rejected.
5. *`title` / `aria-label` on `#addrSearchInput` (`:1589-1591`)* — hover-dependent and invisible to a gloved touch user; violates AGENTS.md "no hover-dependent UX". Rejected.

## 4. Wording candidates — Petar picks exactly ONE at Gate 1

- **W1 (recommended; ~86 chars ≈ 165 B):** „Адресите са по официалния регистър — името може да се различава от надписа на картата."
- **W2 (shortest; ~69 chars ≈ 133 B):** „Адресите са по официалния регистър — възможно е друго име на картата."
- **W3 (operational, reassures that the pin is right; ~103 chars ≈ 198 B):** „Адресите са по официалния регистър. Името може да се различава от картата — точката е на вярното място."

All three wrap to 2 lines at 375px. The signed string is used **verbatim**; the Executor may not shorten, re-punctuate or translate it. No wording signed ⇒ no commit.

## 5. The single commit

**Files (staged with explicit paths):** `index.html`, `docs/plans/search_registry_note.md` (this signed plan; if it is already tracked and unchanged, stage `index.html` alone). Nothing else — `git status --short` must show every other dirty/untracked file untouched.
**Change:** exactly one CSS rule + its comment, inserted after `index.html:1066`; the wording from §4 goes in `content:`.
**Exact commit message (English, no Cyrillic in git metadata):**

```
Add address-registry note to the search results dropdown

The basemap is rebuilt pure OSM at the next build (12.08.2026 decision:
the 41-row street-name patch is rejected), while address search stays on
the official address register, so a street name in the results can differ
from the map label. Show one muted Bulgarian line at the bottom of the
open dropdown stating this, including in the empty-result state.

CSS only, as a sticky ::after on .search-results: renderResults,
renderCombined, showStatus, renderCoordRow and hideResults all rebuild the
box with replaceChildren, so a real child node would not survive a
re-render.

Plan: docs/plans/search_registry_note.md (Gate 1, signed by Petar).
```

**Gates — all machine-checkable; a failed gate STOPS and asks Petar**

| # | Gate | Command / check | Pass |
|---|---|---|---|
| G0 | Baseline (before any edit) | `git rev-parse HEAD`; `(Get-Item index.html).Length`; mojibake scan (G3 command); `python -m unittest discover -s tests` | All recorded; suite green and scan = 0 matches, else STOP (a pre-existing red baseline is not this commit's to absorb) |
| G1 | Additive, confined diff | `git diff --numstat -- index.html`; `git diff -U0 -- index.html` | deletions `0`; insertions ≤ 12; hunk header inside lines 1045-1125 |
| G2 | Byte-growth cap | `(Get-Item index.html).Length` minus G0 value | ≤ **1,200** bytes |
| G3 | Encoding (AGENTS.md § Non-ASCII Encoding Gate) | `Select-String -Path index.html -Pattern '[\u00D0\u00D1\u00C2][\u0080-\u00FF]' -Encoding UTF8` | 0 matches, same as G0 |
| G4 | Suite non-regression (CLAUDE.md § Verification) | `python -m unittest discover -s tests` | Green, identical to G0 |
| G5 | Wording exact and unique | `Select-String -Path index.html -Pattern '<signed W# string>' -Encoding UTF8` | Exactly 1 match, byte-identical to the signed string |
| G6 | 375px manual (CLAUDE.md § Verification) | `python -m http.server 8000`, 375px viewport | Query with hits → note pinned at the dropdown bottom while scrolling a long list; nonsense query → „Няма съвпадения" + note; Escape → dropdown and note both gone; header height and map top edge unchanged vs baseline; result click still flies to the pin; console 0 errors |
| G7 | No JS/markup touched | `git diff -- index.html \| Select-String 'function \|renderResults\|replaceChildren\|addEventListener\|<div\|<input'` | 0 matches |

**Rollback:** `git revert <commit>` — one additive, CSS-only commit; no data, no flag, no schema, nothing to unwind by hand.

## 6. STOP conditions (Executor)

- G0 baseline red or already showing mojibake → STOP before editing.
- Any gate G1-G7 fails → STOP; do not "fix forward".
- The sticky footer misrenders at 375px → apply only the §3 authorized fallback; anything else → STOP.
- Any temptation to touch JS, markup, `.search-results` geometry, or the header offsets → scope breach → STOP.
- No signed wording, or a wish to alter the signed string → STOP (Bulgarian UI text is Petar's gate).
- Unexpected worktree state (unfamiliar branch, files you did not create) → investigate, do not overwrite.

## 7. Explicitly out of scope

- **No search-logic change:** ranking, dedup, `resolveAndRender`, approx trigger, coordinate parsing, selection and Enter/click handlers stay byte-identical.
- **No flag change:** `BASEMAP_PMTILES_ENABLED`, `APPROX_ADDRESS_SEARCH_ENABLED` and every other flag remain as committed.
- **No coupling to the service-worker work:** `docs/plans/sw_cache_lifecycle_fixes.md` is a **separate signed cycle**. Do not touch `sw.js`, `SHELL_ASSETS`/`CACHE_*`, or `BASEMAP_VERSION`, and do not use this note as a reason to bump a cache version.
- **No basemap work:** removing the 41-row patch is a future signed build cycle in the Varna_buildings pipeline; nothing here touches `data/basemaps/**`.
- **No `data/**` mutation, no Worker change, no new dependency, no ADR, no `docs/activeContext.md` edit in this commit, no push or deploy.**

## 8. Open questions for Gate 1

1. Which wording — **W1**, W2, or W3?
2. Byte cap 1,200 B acceptable, or tighten to 900 B (would force W2 + a shorter comment)?

**Signature line (to be filled by Petar):** `SIGNED: ______________  date: __________  wording: W__`
