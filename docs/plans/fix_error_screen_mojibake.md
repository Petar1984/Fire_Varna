# Plan — Fix the mojibake'd data-load error screen (authorized verbally)

**Date:** 2026-08-12 · **Status:** AUTHORIZED — Petar, verbally, 12.08.2026: „поправи го ти — дал съм ти пълен достъп" (in-session instruction after diagnosing the bug live). Push authority remains Petar's alone.
**Risk:** 🟢 Routine — three UI strings + one new static gate; no logic, no flags, no data.

## The defect (measured)

`index.html:1725-1730` — the hydrant-data load-failure branch replaces `document.body`
with an error screen whose Bulgarian text was committed as literal ASCII question marks
(`<h2>?? ?????? ??? ?????????</h2>` etc.). Root cause class: text written through a
'?'-substituting encoder; invisible to the repo mojibake gate, which scans for
UTF-8-as-cp1252 garbage (`[ÐÑÂ]`-class), not plain '?'.

- Known since 08.05.2026: flagged in `docs/audits/data_audit_and_target_schema_20260508.md:38`, never fixed.
- Reproduced live by Petar on 12.08.2026 (offline copy, dead local server, SW-cached shell,
  no offline pack → fetch fails → the '?' screen).
- Baseline: `main` @ `227e595`; `index.html` = 475,326 B; suite 120 tests green.

## The change

1. Replace the three strings (new wording authored under the verbal authorization):
   - h2: „Грешка при зареждане на данните"
   - p: „Данните за хидрантите не се заредиха. Провери интернет връзката и опитай отново."
   - button: „Презареди"
2. New static gate `tests/test_ui_ascii_mojibake.py`: no `\?{3,}` runs in `index.html`
   and `sw.js` (JS nullish `??` is exactly two — never matches), plus presence of the
   three strings above. Catches this whole defect class forever.

## Commits (exact messages)

1. `plan: record the authorized fix for the mojibake'd data-load error screen` — this file.
2. `fix(ui): restore the mojibake'd Bulgarian text on the data-load error screen` — `index.html`, `tests/test_ui_ascii_mojibake.py`.

## Gates

- `python -m unittest discover -s tests` green (120 + new).
- `\?{3,}` scan over index.html + sw.js: 0 matches after fix (3 before, lines 1727-1729).
- Classic mojibake scan unchanged (0 matches).
- Byte growth < 300 B (Cyrillic replaces '?' roughly 2:1).
- Live check: serve `index.html` WITHOUT `data/` → error screen renders the new Bulgarian
  text; „Презареди" reloads.
- `git status --short` — pre-existing dirt untouched.

## Out of scope (found while measuring, NOT fixed here)

- `data/search_index.json` (Petar's uncommitted worktree copy) contains 8 labels with a
  street name of literal `?????` (кв. Розова долина №0/№1, кв. Аспарухово №15/17/175…) —
  same defect class but in DATA built by the Varna_buildings pipeline. Belongs to that
  repo's cycle; reported to Petar 12.08.2026. A future data gate should scan the built
  search payloads for `\?{3,}` before publish.
- Historical `???` occurrences in `docs/audits/*.md` are point-in-time audit records of
  source DBF garbage — intentionally left as-is.
- `C:\Petar\FireVarna_offline` (local copy, outside the repo) gets the fixed `index.html`
  re-copied after commit.

**Rollback:** `git revert` of the fix commit.
