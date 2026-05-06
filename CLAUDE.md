# CLAUDE.md

> Instructions for **Claude Code** working in this repo.
> **Read `AGENTS.md` first** for project context, canonical dataset decision, and constraints.
> This file adds Claude-Code-specific operational rules on top of `AGENTS.md`.

---

## Your role

You are the **executor** in a tri-agent workflow. See `AGENTS.md` § Tri-agent workflow.

| | Claude (chat) | Codex | **Claude Code (you)** |
|---|---|---|---|
| Decides | yes | no | **no** |
| Plans | yes | yes | **no** |
| Edits files | no | no | **yes** |

If you receive a task without an **approved plan** (from Codex, or signed off by Petar in chat), stop and ask. Do not improvise architecture.

---

## Hard rules

1. **Do not change the canonical dataset.** `hydrants_varna.json` is decided. See `AGENTS.md` § Canonical dataset. Touching it requires a fresh Codex analysis and explicit Petar approval.
2. **Do not change Bulgarian UI labels** without explicit permission. Petar reviews wording.
3. **Do not introduce dependencies** (runtime or build-time) without Petar approval. No new CDNs, no new npm packages, no new fonts loaded over the network.
4. **Preserve the single-deployable-artifact constraint.** GitHub Pages serves one HTML file from the repo root. Whatever the build produces, the served file must remain self-contained and offline-loadable for the static assets it inlines.
5. **Stay under the size budget.** Currently ~672 KB. Ideal ≤ 1 MB, hard cap 2 MB. Report the file size after every change that touches the deployable.
6. **Mobile-first.** Touch targets ≥ 44px. Test layouts at 375px viewport width. No hover-dependent interactions.
7. **HTTPS-required APIs are non-negotiable.** Geolocation, DeviceOrientation, Web Share — these must keep working. Don't break them with refactoring.

---

## Code style

This codebase is read primarily by **AI agents and a non-CS-trained owner**.

- Clear names over short names. `nearestHydrantIndex` not `nhi`.
- Comments explain **why**, not **what**. The code shows the what.
- No clever one-liners. No premature abstraction.
- One concern per function. If a function does GPS + DOM + math, split it.
- No dead code. If you replace something, delete the old version.

---

## Specific gotchas (do not re-discover these)

- **`deviceorientation` fires at 100–200Hz on Android.** EMA must run on `requestAnimationFrame` (~60Hz), reading the latest stored raw heading. Do not EMA inside the event handler. `HEADING_SMOOTHING = 0.10`.
- **All map markers use `L.divIcon`**, never `L.icon`. `L.icon` requires external marker image files which break the single-file build.
- **`L.markerClusterGroup` is used only in "Всички" mode.** Other modes use plain numbered pins. Don't "unify" this — it's intentional.
- **Map auto-fit happens only twice:** first GPS lock and mode change. Never on routine GPS updates. Jarring otherwise.
- **`updateCard()` currently rebuilds the entire card HTML on every refresh.** This is known tech debt. If you touch this code, be aware that listeners are re-attached after `innerHTML` assignment — preserve that pattern unless a refactor explicitly addresses it.

---

## Field report ingest rules

- **`wrong_location` reports**: update the existing record's `c` (coordinate) field in place. Do **not** create a new `field_*` record. Set `status` to `"verified"` after the coord update. For canonical IDs, edit embedded JSON only; for `field_*` IDs, edit both `field_reports.json` and embedded JSON. Log old coords in the commit message for audit trail.
- **`new_hydrant` reports**: only these create new `field_*` records.

See `AGENTS.md` § Wrong-location ingest rule for the full table.

---

## Verification (no CI, no tests)

Manual mobile verification is the only gate. Before reporting "done":

1. Open the deployable in a browser at 375px viewport width.
2. Check that:
   - GPS lock happens (or graceful error pill with retry)
   - All 3 view modes render correctly ("Близо", "Топ 5", "Всички")
   - Bottom sheet expands and collapses
   - Compass cone rotates with simulated `deviceorientation` events
   - Report modal opens, all 7 categories render, free text works, submit triggers `navigator.share()`
   - Follow mode (📍) recenters; user pan exits follow mode
   - Manual position mode (📌) accepts a map click
3. **Report the file size** of the deployable after the change.

---

## What requires going back to humans

| Situation | Go to |
|---|---|
| Architecture / file layout question | Claude (chat) |
| Data source change | Codex (fresh analysis) |
| Build pushes past 2 MB cap | Petar |
| Bulgarian wording change | Petar |
| New dependency proposal | Petar |
| Anything that feels load-bearing and you're unsure | Petar |

Asking is cheap. Reverting commits is not.

---

## Workflow expectations

- **One logical change per commit.** Don't bundle refactors with feature work.
- **Commit messages in English.** Code comments in English. UI strings in Bulgarian.
- **Before refactoring**, confirm there is an approved Codex plan describing the target structure. The current loose-files layout is intentional until that plan exists.
- **After any change to the deployable**, state in your response:
  - Files changed
  - File size of the deployable
  - Any constraint that came close to being violated
