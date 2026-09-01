# Marker redesign frame — hydrant glyph pins + entrance plates

**Status:** LIVE IN PRODUCTION 2026-07-02 — FV `020db19` pushed (c6b3130..020db19), production-verified (glyph pins + badges + statuses + ring on petar1984.github.io). Remaining owner check: "вх" 8px micro-label on a real phone (fallback = number-only plate, one CSS rule). Live-verified on localhost: glyph pins in all statuses (dark glyph on reported ✓), white rank badges Топ-5 only, Всички glyph-only + clusters untouched, entrance plates "вх N" with letters + amber active ring, mixed scene unambiguous, console clean. CC found+fixed a real plate-tail clipping bug; polling gate passed with a live setIcon status flip. Byte note: +4,037 exceeds Codex's +1,190 estimate (data-URI mask verbosity) — 1% of file, no hard constraint hit. Petar eyeball items: glyph technique (approved by audit) + "вх" 8px micro-label on a real phone post-push (fallback: number-only plate, one CSS rule).
**Tri-agent:** chat-Claude frames/audits → Codex plans → CC executes (local commit) → Petar signs + pushes. Never push.

## Problem
Hydrant markers and building-entrance markers are both "pin + number" — same silhouette, same text channel, only color differs. Color already carries hydrant STATUS, so it cannot carry the hydrant-vs-entrance distinction. Confusion confirmed on live use (two "2" pins side by side at бл.307).

## Approved design

### H — hydrants (teardrop pins stay; status colors stay EXACTLY as-is)
- Add a hydrant GLYPH inside the pin (white; dark `#333` on `.reported` yellow for contrast).
- Status classes and colors are FROZEN: `.canonical #757575` · `.verified #c41e3a` · `.reported #fdd835` · `.operational #2e7d32` · `.broken #212121`; `.first` amber ring and `.dim` opacity stay unchanged.
- **Топ-5 mode:** rank number moves OUT of the pin body into a NEUTRAL corner badge (white circle ~16 px, `#212121` text, thin gray border) — never colored, so it cannot collide with any status fill.
- **"Всички" mode:** glyph-only pins (no badge). Cluster behavior untouched.

### E — entrances (detail-panel markers)
- Replace numbered circles with a MINI ENTRANCE PLATE: rounded-rect + bottom pointer, fill `#0C447C` (blue-800; free color vs the status palette), white 1.5 px border, micro-label "вх" (top, ~7-8 px real size, `#B5D4F4`) + number/letter (white, 13 px). Letters (А/Б/В) supported natively.
- Active entrance = amber ring — SAME amber as `.first` (unify the two highlight styles into one convention; today's detail-marker highlight color to be reconciled to it).
- If 375 px testing shows the "вх" micro-label unreadable → fallback: plate + number only (shape still carries the distinction).

## Hard constraints
- `L.divIcon` ONLY (never `L.icon`); no image assets; no new network resources.
- **Perf: NO inline SVG per divIcon in "Всички" (7,238 pins).** Glyph via a single SVG `<symbol>` + `<use>`, or pure CSS (::before/::after) — CC/Codex pick; CSS budget ≈ 1.5 KB in index.html.
- Polling compatibility: markers update via `marker.setIcon` with `_pinKind`/`_rank`/`_isActivePin` tags (see CLAUDE.md gotchas) — new icons must flow through the SAME builders (`makePin` etc.); tag semantics untouched.
- Tap targets/tap-vs-long-press behavior, popup flows, cluster mode, auto-fit rules: untouched.
- Bulgarian UI strings; pin size stays ~28 px.

## Gates
- Screenshot regression: Топ-5 (ranks + first-ring), Всички (clusters + glyph pins in all 5 statuses + dim), detail panel (plates, letters, active ring), mixed scene.
- Polling survives icon swap (no leaked active-pin flags; setIcon paths intact).
- Console clean; index.html size before/after reported; 375 px checklist (badge readability, plate micro-label, tap targets).
- No change to hydrants.json, search index, detail JSONs — pure presentation.

## Sequencing
Plan NOW against the post-search-quality base: anchor by function names + CSS classes (`.h-pin`, `makePin`, detail entrance marker builder), NOT line numbers. Execution blocked on: search-quality landed + audited + signed.

## PROMPT FOR CODEX (paste)

> Plan (do not execute) the marker redesign per `Fire_Varna/scratch/marker_redesign_frame.md`.
> Design is FIXED (hydrant glyph in status-colored teardrop + neutral white rank badge in Топ-5;
> entrance plates "вх N" #0C447C with amber active ring unified with `.first`). Do not re-open
> the visual design; plan the implementation.
>
> Deliver: (1) touch points by FUNCTION/CLASS (`.h-pin` CSS block, `makePin`, the detail-panel
> entrance marker builder, polling `setIcon` paths) — no line-number anchors, the base will be
> post-search-quality; (2) the glyph delivery mechanism decision (SVG symbol+use vs pure-CSS)
> with the "Всички"-mode DOM/perf math for 7,238 pins; (3) exact CSS additions estimate vs the
> ~1.5 KB budget; (4) how `.reported` gets the dark glyph variant; (5) gates from the frame incl.
> polling-survival and 375 px checklist; (6) CC execution steps + rollback (pure-presentation
> revert = one commit); (7) explicit dependency: execution rebases on the landed search-quality
> commit. Never push.
