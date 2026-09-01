# Plan — Service-worker cache lifecycle fixes (B2, pre-flag-flip)

**File:** `docs/plans/sw_cache_lifecycle_fixes.md`
**Date:** 2026-08-11 · **Status:** DRAFT — AWAITING PETAR SIGNATURE (Gate 1)
**ADR:** new ADR 005 (`docs/decisions/005_sw_cache_lifecycle.md`, drafted alongside) — amends ADR 002 D4/D5, does not supersede it.
**Authors:** Planner (Claude Code, read-only). Executor/Auditor to follow after signature.

---

## 1. Risk classification

**🔴 Architectural.** Escalation-dominant; rounded up.

| Trigger | Fired? | Evidence |
|---|---|---|
| ADR / architecture-doc change | **YES** | This task creates `docs/decisions/005_*` and changes a cross-artifact contract (`index.html` ⇄ `sw.js` cache lifecycle + message schema). |
| New pattern / governance-relevant safety property | **YES** | Cache-retention + update discipline must hold *before* a future flag flip; it is a pre-condition of STOP B2. |
| Core pipeline logic / multi-file in one subsystem | YES (would be 🟠 alone) | `sw.js` + `index.html` + `tests/test_basemap_manifest.py`. |
| Flag flip / publish / release / upload | NO | `BASEMAP_PMTILES_ENABLED` stays `false`; no push, no deploy. |
| Irreversible canonical mutation / new external source / cross-repo | NO | Zero writes to `data/hydrants.json`; no new source; work stays in `C:\git\Fire_Varna`. |

**Topology:** Variant A (separate Planner / Executor / Auditor sessions). **Gates:** Petar signs (Gate 1) → Executor local commits → Auditor → Petar reviews diff (Gate 2) → Petar pushes. Agents never push.

## 2. Request scope

**In scope:** three confirmed cache-lifecycle defects in the flag-gated service worker (`sw.js`), their page-side counterpart in `index.html`, static gates in `tests/`, one ADR, one plan doc.
**Ordering constraint (recorded here so it is durable):** the side-feature framework in `scratch/additive_features_frame.md` must **not** launch into a world with an active service worker before this repair lands — that file says so itself at lines 103-106, and its "the file enters `SHELL_ASSETS` in the same commit" discipline assumes the lifecycle decided here.

**Out of scope (explicit):** flipping `BASEMAP_PMTILES_ENABLED`; any basemap rebuild or `BASEMAP_VERSION` bump (D7 lands the *policy* and the *gate* that will permit a retired version dir at the next bump; the bump itself is a separate signed cycle); ADR 002 signature or B4 upstream-refresh work; PWA manifest; `data/**` mutation (incl. the dirty `data/search_index.json`); Worker changes; approx-address flag; new runtime deps; navigation preload / Background Fetch; auto-downloading the offline pack without opt-in; `git push`, deploy, or any device flag flip.

## 3. Deterministic inventory + files read

Planner tooling this session = Read/Glob/Grep only (no shell) → byte-level inventory (sha256/size) is **delegated to Executor gate M1** and must be recorded before the first edit.

**Ground input (constraining, read first):** `scratch/sw_fix_facts.md` — measured Pages headers (Sol urlscan traces 08.03.2026 / 20.05.2026), W3C SW-update spec facts (CR draft 04.08.2026), and the two documented versioned-asset traps. Its statements constrain the design; they are not proposals.

Files read in this session: `scratch/sw_fix_facts.md`, `scratch/additive_features_frame.md` (lines 90-118), `data/basemaps/basemap_manifest.json`, `AGENTS.md`, `CLAUDE.md`, `sw.js` (281 lines, full), `index.html` (lines 940-957, 4480-4560, 4558-4628, 4640-4756 + `BASEMAP_VERSION` grep), `docs/decisions/002_osm_pmtiles_basemap_offline.md`, `003_dual_claude_code_governance.md`, `004_measurement_doctrine.md`, `docs/plans/h1_shared_core_spatial_dedup.md`, `docs/plans/commit_15_worker_get.md`, `docs/activeContext.md`, `tests/test_basemap_manifest.py`, `scratch/basemap_b2/stop_b2_local.md`, `scratch/basemap_b2/index_smoke.mjs` (head).

## 4. Measured baseline (re-verified line-by-line today, 2026-08-11)

| # | Claim | Verified evidence in the current worktree |
|---|---|---|
| F1 | Offline shell freezes forever | `sw.js:205-214` `navigationHandler` returns `await fetch(req)` with **no cache write**; the only writer of `index.html` into `CACHE_CORE` is `sw.js:85-86` (`core.addAll(SHELL_ASSETS.core)`) inside `install`, which runs only when `sw.js` bytes change. Meanwhile `sw.js:191-193` routes `MUTATING_DATA` (incl. `data/search_index.json`, `sw.js:51-56`) to `networkFirst` (`216-229`), which **does** `c.put` on every online hit. → shell and data drift apart by construction. |
| F2 | Version bump silently deletes the downloaded pack | `sw.js:99-111` `activate` deletes **every** cache with a B2 prefix (`38-42`) not ending in `BASEMAP_VERSION`, with no exception for `fire-varna-basemap-<old>` holding the opt-in `varna_basemap.pmtiles` (`installOfflinePack`, `127-149`) **or** for `fire-varna-offline-pack-<old>` holding hydrants/search/address rows. No user notice exists (page handles only `offline-pack-ready|status|error`, `index.html:4696-4707`). |
| F2b | *(Planner addition)* the same delete also drops the offline **data** pack | `PACK_DATA` (`sw.js:76`) lives in `CACHE_OFFLINE_PACK`; `hydrants.json` self-heals on the next online load (network-first put), `search_index.json`/`address_rows.json` are lazy (`index.html:5269-5270`) and may not. |
| F3 | Post-deploy version-mix window | `install` calls `self.skipWaiting()` (`sw.js:92`) and `activate` calls `self.clients.claim()` (`sw.js:109`) → a new SW can control a page running the HTTP-cached old `index.html`, whose `BASEMAP_VERSION` is hardcoded at `index.html:4508` and used to build the pmtiles URL at `index.html:4599`. The new SW's cache-first route matches only the new prefix (`sw.js:197`) and `pmtilesHandler` looks only in the current `CACHE_BASEMAP` (`sw.js:243-247`) → old-version URL falls through to network: dead offline, 404 online once the old version dir is removed (`tests/test_basemap_manifest.py:55-58` enforces exactly one version dir). |

**Blast radius today: zero live users.** `ensureBasemapServiceWorker` returns before `register()` unless the capability is active (`index.html:4680-4682`), and `BASEMAP_PMTILES_ENABLED = false` (`index.html:4507`, asserted by `tests/test_basemap_manifest.py:123-124`).

**Quoted declared metadata (authoritative):** ADR 002 D5 — *"`basemap_version` in every cache name + manifest. A stale basemap and a fresh app shell can never mix."* ADR 002 D4 — *"it must NOT evict the existing `fire-varna-search-v2` / `fire-varna-approx-addresses-v1` Cache namespaces."* Measured pack size: `PMTILES_BYTES = 5748578` (`tests/test_basemap_manifest.py:20`) → retaining one previous generation costs **≈ 11.0 MB** of pmtiles, plus `data/hydrants.json` 1,221,809 B (`docs/activeContext.md`) ×2. This is the quota-cost answer the audit asked for: the "2× pmtiles" objection is ~5.5 MB, not a blocker.

### Negative findings matrix

| Checked | Finding |
|---|---|
| index.html-specific byte budget in AGENTS.md | **None exists.** Binding constraint is first load ≤ 3 MB ideal / 5 MB hard cap (`AGENTS.md § Hard Constraints`). Current first load ≈ `index.html` (436,822 B at `2eb370d`, `scratch/basemap_b2/stop_b2_local.md §6`) + `data/hydrants.json` 1,221,809 B ≈ 1.66 MB — ample headroom. Executor re-measures (M1). |
| `Cache-Control: max-age=600` on Pages HTML **and JS** | **MEASURED, not assumed** — Sol urlscan traces 08.03.2026 and 20.05.2026, recorded in `scratch/sw_fix_facts.md`: `max-age=600` on both HTML and JS, no `public` / `immutable` / `must-revalidate`, weak per-resource ETags (`W/"…"`), `Vary: Accept-Encoding`, working 304, `Age` counted. Long-observed but **not an officially guaranteed Pages policy**, so the design must not depend on the TTL staying 600 s — and does not: D1/D2/D3/D7 hold for any TTL ≥ 0. Gate M4 re-confirms at execution time, now for `index.html` **and** `sw.js`. |
| CI | Absent (`AGENTS.md § Known Tech Debt` 7). Gates are run manually by the Executor and re-run by the Auditor. |
| Existing SW-lifecycle tests | Only the 5 static assertions in `tests/test_basemap_manifest.py:142-170`; nothing asserts navigation caching, retention, or update discipline. |
| Playwright smoke (`scratch/basemap_b2/index_smoke.mjs`) | Present but hard-codes a global install path (`C:/Users/Petar/AppData/Roaming/npm/...playwright`). Treated as **optional**; DevTools protocol below is the required gate. |
| Repo state | The session-start snapshot reported `Current branch: HEAD` (detached?) and an empty recent-commit list. **Must be resolved before any commit** — gate M0. *[Orchestrator-session measurement, 2026-08-11: `git branch -a --contains HEAD` prints `* main` at `227e595`; the anomaly was in the harness session header, not the repo. M0 still re-verifies.]* |

## 5. Chosen design (decision ledger)

| # | Decision | Rationale | Rejected alternative (why) | Reversibility |
|---|---|---|---|---|
| **D1** | `navigationHandler(event, req)`: on a successful online navigation, `event.waitUntil` a `CACHE_CORE.put('index.html', res.clone())`, guarded by `res.status === 200 && !res.redirected && content-type startsWith 'text/html'`; quota errors swallowed like the other handlers. | Makes the offline shell track the last online visit, so shell code and network-first data can no longer drift. Key must be the literal `'index.html'` — the fallback reads `core.match('index.html')` (`sw.js:210`) and a navigation to `/Fire_Varna/` would otherwise be stored under a different key and never found. `!res.redirected` avoids storing a redirect body; the type guard avoids caching an error page. Known, accepted side effect: inside the measured ~600 s HTML window a new worker may write an *old*-version shell into the new `CACHE_CORE`. It is bounded (the next online navigation overwrites it), offline-servable (D2+D3 keep that shell's asset URLs alive) and self-healing — it must **not** be read as a Test C failure. | (a) Re-fetch with `cache:'no-cache'` to defeat the 600 s HTML TTL — **rejected:** rebuilding a `mode:'navigate'` Request changes redirect semantics and a `redirected` response is illegal to return from `respondWith`; a per-navigation revalidation also adds latency on flaky mobile links. (b) Key `CACHE_CORE` to an app version — **rejected:** adds a second version axis and a build step the repo does not have. | `git revert` of one commit. |
| **D2** | `activate` retains **one previous generation**: keep the old `fire-varna-basemap-*` cache that actually holds a pmtiles entry (if several, the last in `caches.keys()` order) plus the `fire-varna-offline-pack-*` cache with the same version suffix; delete every other non-current owned cache (all old `fire-varna-core-*` always go — a stale shell is the F1 defect). Retained caches are pruned only when `installOfflinePack` for the current version **succeeds**, or by the existing `?basemap_pmtiles=0` revert. A failed pack install — quota or otherwise — **deletes nothing**: the worker fails loud with `offline-pack-error { quota, retained: true }` and the retained generation stands. It is dropped only on an explicit user act: the page posts `prune-retained-pack`, the worker prunes the retained pair and immediately retries the install in the same handler (one tap = the whole "изтрий стария и опитай пак" semantics; no ack race, no second confirmation). The `/quota/i` error heuristic (`sw.js:141-142`) is a string match that can misfire on a mislabeled network error — it may only choose the wording of a message, never authorize a deletion. | Deferred pruning = the user's opt-in download survives a version bump; the cap bounds storage at ≈ 11.0 MB of pmtiles **total** (2 × 5,748,578 B measured), i.e. **+5.75 MB incremental** over holding one pack. PROTECTED guard stays first and untouched. | (a) Migrate old pack bytes to the new URL — **rejected:** that is exactly the "stale basemap + fresh shell mix" ADR 002 D5 forbids. (b) Prompt-before-delete as the *routine* bump policy — **rejected:** delete-then-ask cannot be undone offline; retention is strictly safer and costs +5.75 MB. Note this is not in tension with the quota path: there, deletion is the only way forward, so it happens **only** after the explicit consent tap — never automatically. (c) Keep every generation — rejected: unbounded storage. | `git revert`; retained caches are additive, never destructive. |
| **D3** | Version-agnostic *lookup* (never version-agnostic *content*): `cacheFirst`, `networkFirst`-fallback and `pmtilesHandler` first check their current cache, then the other caches sharing the same B2 prefix, matching by **exact URL** only. Route condition widens to `/^data\/basemaps\/osm_varna_[^/]+\//`. Call-site literals `cacheFirst(req, CACHE_BASEMAP)` / `networkFirst(req, CACHE_OFFLINE_PACK)` are preserved. | Because the version is in the path, an exact-URL hit can only ever return the bytes that URL was built from — no cross-version substitution is possible. This is what makes a retained old pack actually servable to an old page (F3's real harm). | Global `caches.match(req)` — **rejected:** it searches *all* caches, including `fire-varna-search-v2` / `fire-varna-approx-addresses-v1`, violating the PROTECTED boundary. | One commit. |
| **D4** | Remove `self.skipWaiting()` (`sw.js:92`) and `self.clients.claim()` (`sw.js:109`). | The standard lifecycle is the only structural guarantee that a worker does not seize a page it did not install for. It **bounds but does not eliminate** shell/worker disagreement — see the rejected column. Registration stays `register('sw.js')` with no options (`index.html:4683`): the default `updateViaCache: 'imports'` keeps the main script always revalidated, Chrome 68+ bypasses a fresh HTTP cache for the update check, and a registration older than 86,400 s is forced to `no-cache` (`scratch/sw_fix_facts.md`) — that is what keeps propagation bounded without extra machinery; adding `importScripts` or an explicit `updateViaCache` later must revisit ADR 005. Verified no page-side breakage: first-ever registration activates regardless (nothing to wait for), and `ensureBasemapServiceWorker` messages `navigator.serviceWorker.controller || reg.active` (`index.html:4689`), so opt-in install still works uncontrolled; `install` still precaches `index.html`, so the STOP B2 airplane-mode protocol still passes on first session. **Accepted cost:** a fixed SW reaches an existing device only after all its tabs close (a reload does not release a controlled client). This does **not** stale-lock data — hydrants/search stay network-first. | (a) Keep `skipWaiting` and rely on D3 alone — **rejected:** D3 mitigates the symptom for already-open clients; D4 removes the takeover itself. Neither removes *every* mismatch: a **fresh** navigation inside the 600 s HTML window still pairs the new worker with a stale cached shell, because an `index.html` change never triggers an install (SW update = byte-compare of `sw.js` only) and the navigation honours the HTTP cache. That residual is covered by D1 + D2/D3 + D7, not by D4. (b) Add an "update ready, restart" UI — deferred: new UI surface + wording gate for a benefit that is nil while the flag is false. | One commit; restoring two lines. |
| **D5** | Notification contract: `offline-pack-status` gains `outdated: <bool>` (retained pack exists && current pack missing); `offline-pack-error` gains `retained: <bool>`; new broadcast `offline-pack-outdated` at activate; new page→worker message `prune-retained-pack` (the consent act: prune the retained pair, then retry the install). Page surfaces a Bulgarian re-download control in the basemap selector; tapping it calls the existing `ensureBasemapServiceWorker(true)` opt-in path (`index.html:4622` precedent). | The status reply covers the "no client open at activate" case; the broadcast covers the open-page case; both funnel to one page-side handler. Re-download stays explicit opt-in (addendum П2) — never automatic on mobile data. | Auto re-download — rejected (opt-in doctrine + mobile data). | One commit each side. |
| **D7** | *(numbering follows ADR 005; ADR D6 = unchanged invariants, no plan action.)* Server-side retention: at a `BASEMAP_VERSION` bump the previous `data/basemaps/osm_varna_<old>/` directory stays in the deployed tree for **≥ 1 further deploy**; `data/basemaps/basemap_manifest.json` gains `previous_version` at that bump; the retired dir is deleted only in a later, separate commit. Versioning stays **in the path** — `?v=` remains forbidden. **This cycle lands the policy + the gate only, not a bump.** | Client-side retention only helps a client that holds the old cache. An old HTML page whose worker never cached the pack, or an uncontrolled/online-only client, still fetches `data/basemaps/<old>/…` from the origin → 404 once the deploy drops the dir (Cloudflare-documented class, 03.07.2026, `scratch/sw_fix_facts.md`). The current gate `tests/test_basemap_manifest.py:55-58` (`dirs == [VERSION]`) actively **forbids** the mandated retention, so it must be widened now, before the first bump. Feasibility verified: the B1 hash locks pin only `cls.vdir` (`tests:20-25, 48, 67-96`); AGENTS.md has no repo-size cap and first load is unaffected (the pack is never part of it); repo-verified zero `?v=` occurrences in `*.html\|js\|json\|py`. | `?v=` query versioning — rejected: unreliable through intermediaries (AWS/Cloudflare). Deleting the retired dir in the same deploy — rejected: that *is* the 404 defect. | Policy is doc-only; the gate widening is one commit. |

**Bulgarian UI strings — require Petar approval at Gate 1** (wording change gate, `AGENTS.md § Dual-Claude-Code Workflow`):
- selector button: `Офлайн пакетът е остарял — обнови`
- flash on detection: `Офлайн пакетът е остарял — обновете го, докато има интернет` (4000 ms)
- flash on tap: `Свалянето започна…` (2500 ms)
- **consent control** (shown only after an `offline-pack-error` with `retained: true`; tapping it deletes the retained old pack and retries): `Няма място — изтрий стария пакет и опитай пак`

## 6. Commit-by-commit specification

Every commit: stage **explicit paths only** (never `git add -A`), use the **exact** message below, then `git status --short` to prove pre-existing dirt (e.g. `data/search_index.json`, `scratch/*`) was untouched. A failed gate **STOPS and asks Petar**.

**M0 — pre-flight (no commit).** `git rev-parse --abbrev-ref HEAD` must print `main` (session snapshot suggested a detached HEAD — if detached or unexpected, STOP, do not commit); record `git rev-parse HEAD`; `git status --short` recorded verbatim as the dirt baseline.
**M1 — baseline measurement (no commit).** Record bytes+sha256 of `sw.js`, `index.html`, `tests/test_basemap_manifest.py`; `python -m unittest discover -s tests` (expect the current all-green count, 110 at `2eb370d`); `node --check sw.js`. Written into the STOP report before the first edit.

**C1 — `docs(adr): add ADR 005 service worker cache lifecycle`**
Files: `docs/decisions/005_sw_cache_lifecycle.md` (new, content = ADR draft), `docs/decisions/002_osm_pmtiles_basemap_offline.md` (add exactly one blockquote line under Decision: `> **Amended by ADR 005** — cache lifecycle (shell refresh, pack retention, no skipWaiting/claim).`).
Gate: file exists; `Select-String -Path docs\decisions\005_sw_cache_lifecycle.md -Pattern 'Status:\*\* Proposed'` matches; mojibake scan clean on both files (`AGENTS.md § Non-ASCII Encoding Gate`); `git status --short` shows only these two paths.

**C2 — `plan: service worker cache lifecycle fixes before basemap flag flip`**
Files: `docs/plans/sw_cache_lifecycle_fixes.md` (this document, with Petar's signature line appended).
Gate: file exists; mojibake scan clean; `git status --short` shows only this path.

**C3 — `fix(sw): refresh the cached app shell on every online navigation`**
Files: `sw.js`, `tests/test_basemap_manifest.py`.
Change: D1. Pass the `FetchEvent` into `navigationHandler` so the put runs in `event.waitUntil`. New test `test_navigation_writes_shell_to_core` asserting: `navigationHandler(event` present, `put('index.html'` present, `res.redirected` guard present, `status === 200` present.
Gate: `node --check sw.js` → OK; `python -m unittest tests.test_basemap_manifest` → all pass, count = baseline+1; `python -m unittest discover -s tests` → all pass; Test A (§7) passes with the fix and fails on the pre-fix control.

**C4 — `fix(sw): keep the previous offline pack until the new one installs`**
Files: `sw.js`, `tests/test_basemap_manifest.py`.
Change: D2 + D7's gate + the `outdated` half of D5 — retention at `activate`; prune-on-confirmed-install only; `offline-pack-error` gains `retained`; new `prune-retained-pack` handler (prune the retained pair, then retry `installOfflinePack()` in the same handler); `offline-pack-status.outdated`; `offline-pack-outdated` broadcast. **No `caches.delete` may be reachable from `installOfflinePack`'s `catch`.** D7 gate widening in the same commit: `test_exactly_one_version_dir` (`tests:55-58`) is **renamed** to `test_version_dirs_current_plus_at_most_one_retired` and widened to `assertIn(VERSION, dirs)` + `assertLessEqual(len(dirs), 2)` + if 2, `manifest["previous_version"] == the other dir` and `!= manifest["active_version"]`. It must pass byte-for-byte on today's tree (one dir, no `previous_version` key). The rename is an intentional gate change and must be called out in the STOP report and to the Auditor. **The `PROTECTED_CACHES.includes(name)) return` shape must survive verbatim** — `tests/test_basemap_manifest.py:160` asserts that regex; if the Executor must restructure it, the test is updated in the same commit and the change is called out to the Auditor.
Gate: `node --check sw.js`; new tests `test_activate_retains_previous_pack`, `test_pack_install_prunes_retained`, `test_outdated_message_contract`, `test_quota_never_autoprunes` (asserts no `caches.delete` inside `installOfflinePack`'s `catch` block and that `prune-retained-pack` is the only path to it) and the renamed `test_version_dirs_current_plus_at_most_one_retired` all pass; `test_sw_never_deletes_protected_caches` still passes **unmodified** (or its modification is justified in the STOP report); full suite green; Test B (§7) passes.

**C5 — `fix(sw): serve basemap assets from any retained version cache`**
Files: `sw.js`, `tests/test_basemap_manifest.py`.
Change: D3. New test `test_cross_version_lookup`: helper name present, `pmtilesHandler` uses it, and `assertNotIn("caches.match(", sw)` (global cross-cache match forbidden — PROTECTED boundary). Existing assertions `networkFirst(req, CACHE_OFFLINE_PACK)` / `cacheFirst(req, CACHE_BASEMAP)` (`tests:167-168`) must still pass → keep both call-site literals byte-identical.
Gate: `node --check sw.js`; full suite green; Test C (§7) passes.

**C6 — `fix(sw): stop claiming pages a new worker did not install for`**
Files: `sw.js`, `tests/test_basemap_manifest.py`.
Change: D4 — delete `await self.skipWaiting();` and `await self.clients.claim();` and rewrite the two stale comment blocks (`sw.js:79-82`, `96-97`) to explain *why* (no dead comments). New test `test_no_skip_waiting_or_claim`: `assertNotIn('skipWaiting', sw)`, `assertNotIn('clients.claim', sw)`.
Gate: `node --check sw.js`; full suite green; Test B step 3 (new SW activates only after all tabs close) observed in DevTools.

**C7 — `feat(basemap): offer re-download when the offline pack is outdated`**
Files: `index.html`, `tests/test_basemap_manifest.py`.
Change: D5 page side — one `let offlinePackOutdated = false` at `index.html:4627`; one `let offlinePackRetained = false`; `onBasemapSwMessage` branches for `offline-pack-outdated`, for `offline-pack-status && !ready && outdated`, and for `offline-pack-error && retained`; a `.basemap-refresh` button rendered in `toggleBasemapSelector` in place of the ready row when outdated, `min-height: 44px` (mobile-first constraint), handler = `ensureBasemapServiceWorker(true)` + flash; **and** a distinct consent button (4th string) rendered only while `offlinePackRetained` is set, same 44 px target, handler = post `prune-retained-pack` to `navigator.serviceWorker.controller || reg.active` + flash `Свалянето започна…`; one CSS rule beside `.basemap-ready` (`index.html:956`). `unregisterBasemapServiceWorker` (`4716-4733`) **must not change** — it is prefix-based and already covers retained caches.
Gate: `python -m unittest tests.test_basemap_manifest` incl. new `test_outdated_ui_strings` (asserts all **four** approved Bulgarian strings, the `prune-retained-pack` post, and `min-height: 44px` on both controls); mojibake scan on `index.html` clean; `index.html` growth ≤ 3,500 bytes vs M1 and first load still < 2 MB; Test B step 5-6 and Test D/E (§7) pass; flag still `false` (`test_flag_committed_false`).

## 7. Verification protocol

**All destructive simulation happens in a throwaway copy, never in the worktree.** Copy `index.html`, `sw.js`, `vendor/`, `data/` into the session scratchpad (`swlife/`), serve it with `python -m http.server 8001` from that directory, and drive Chrome DevTools (Application → Service Workers / Cache Storage, Network → Offline). Repo-root serving (`python -m http.server 8000`) is used only for the untouched-behavior check (Test E).

- **Test A (F1).** Open `http://127.0.0.1:8001/?basemap_pmtiles=1`, reload once (page now controlled). Insert `<!-- SHELL_MARKER_V2 -->` near `<title>` in the sandbox `index.html`; do **not** touch `sw.js`. Reload online. Go offline, reload. **PASS:** the marker is present in the served HTML and in the `fire-varna-core-<v>` entry for `index.html`. **Control:** same steps against a copy carrying the pre-fix `sw.js` → marker absent (the frozen shell).
- **Test B (F2 + F3 lifecycle + D5 UI).** Select `Карта Варна (офлайн)`, wait for `✓ Офлайн пакетът е готов`, confirm a ~5.75 MB pmtiles entry in `fire-varna-basemap-<v>`. Simulate the bump: rename `data/basemaps/<v>` → `<v2>` (change only the `tiles_` segment) and replace the version string in the sandbox `sw.js` **and** `index.html`. Close **all** tabs of the origin, reopen. **PASS:** new SW activated only after the tabs closed (D4); Cache Storage shows the three `<v2>` caches **plus** retained `fire-varna-basemap-<v>` and `fire-varna-offline-pack-<v>`; old `fire-varna-core-<v>` gone; the Bulgarian outdated control is shown. Tap it → after `✓ Офлайн пакетът е готов`, the retained pair is gone (deferred prune). **Control:** pre-fix build loses the pack at reopen, silently.
- **Test B-quota (D2 consent path).** Repeat Test B up to the outdated prompt, but first set DevTools → Application → Storage → *Simulate custom storage quota* to ~8 MB (enough for one pack, not two). Tap the re-download control. **PASS:** the install fails with the Bulgarian quota message, **both retained caches are still present** in Cache Storage, and the consent control (`Няма място — изтрий стария пакет и опитай пак`) appears. Tap it → the retained pair is deleted **and** the new pack downloads in the same act; end state = three current caches, `✓ Офлайн пакетът е готов`. **Fail-loud check:** at no point between the failure and the consent tap may the retained pair disappear.
- **Test C (F3 mix window).** Before closing tabs in Test B, use DevTools → Service Workers → *Update* then *skipWaiting* to force the new worker onto the old page (this reproduces the flag-flip-era HTTP-cache mix on purpose). Go offline, pan the map in offline mode. **PASS:** the old-path `varna_basemap.pmtiles` request is served by the ServiceWorker (206 from the retained cache) and tiles keep rendering. **Control:** pre-fix → request fails, basemap blank.
- **Test D (revert path).** Use the address search first so `fire-varna-search-v2` exists, then open `?basemap_pmtiles=0`. **PASS:** zero SW registrations; zero caches with any of the three B2 prefixes (including retained); `fire-varna-search-v2` and `fire-varna-approx-addresses-v1` untouched.
- **Test E (no live-user change).** Repo root on :8000, `localStorage` cleared, no query flag. **PASS:** no request to `sw.js`, `vendor/basemap/*`, `*.pmtiles`, `data/basemaps/<version>/*`; `navigator.serviceWorker.getRegistrations().length === 0`; hydrants load; console clean; the OSM⇄satellite toggle behaves exactly as before. Optional: `scratch/basemap_b2/index_smoke.mjs` Case A if Playwright is present.
- **M4 (re-confirm the measured Pages headers).** If network is available: `curl.exe -I https://petar1984.github.io/Fire_Varna/` **and** `curl.exe -I https://petar1984.github.io/Fire_Varna/sw.js`; record `cache-control`, `etag`, `age`, `vary` verbatim in the STOP report and flag any drift from the measured baseline in `scratch/sw_fix_facts.md`. If unavailable, record "not re-confirmed this cycle; measured baseline stands (08.03.2026 / 20.05.2026)". Either way the design stands — no decision depends on the exact TTL.
- **Regression suite:** `python -m unittest discover -s tests` after every commit; `node --check sw.js` after every `sw.js` edit; mojibake scan on every staged text file.

## 8. Rollback

Nothing is pushed, so rollback is local and total. Per commit: `git revert <hash>` (each commit is independently revertible; C7 depends on C4's message fields — revert C7 before C4). Whole cycle: `git reset --hard <M0 HEAD hash>` provided no unrelated commits intervened. Device-level: `?basemap_pmtiles=0` unregisters the worker and drops all B2 caches. No dataset, Worker, or published artifact is touched, so there is no external rollback surface.

## 9. Approval-gate check

| Gate | Status |
|---|---|
| Architecture change | **Yes** → ADR 005 (C1) is the approval artifact. |
| Bulgarian UI wording | **Yes** → **four** strings in §5 (incl. the deletion-consent control) need Petar's sign-off before C7. |
| Deploy-tree retention policy (D7) + widened/renamed version-dir gate | **Yes** → ADR 005 D7 is the approval artifact; binds the next bump, no bump here. |
| Data-source / canonical dataset change | No. |
| New runtime or build dependency | No (stdlib `unittest`, `node --check`, DevTools only). |
| Flag flip / publish / push | No — forbidden by this plan. |
| Commit authority | Only the seven commits above, exact messages, explicit paths. |

## 10. STOP report (Executor writes, untracked, `scratch/basemap_b2/stop_sw_lifecycle.md`)

M0 branch + HEAD hash + dirt baseline; M1 byte/sha/test baseline; per-commit hash + staged paths + gate output; `index.html` before/after bytes and first-load total; Test A-E outcomes incl. the two pre-fix controls; M4 header capture or the explicit "unverified" note; any existing gate that had to be modified and why — explicitly including the `test_exactly_one_version_dir` → `test_version_dirs_current_plus_at_most_one_retired` rename (D7) and its byte-for-byte pass on today's one-dir tree; the Test B-quota evidence that the retained pair survived a failed install until the consent tap; explicit statement that the flag is still `false`, no data file changed, and nothing was pushed.

## 11. Open questions for Petar (Gate 1)

1. Approve the **four** Bulgarian strings in §5 (or supply replacements). The fourth is a *consent* control: tapping it deletes the retained old pack and immediately retries the download.
2. Confirm D2's quota rule: a failed pack install **never** deletes anything; the retained generation dies only on that explicit consent tap or on `?basemap_pmtiles=0`. Accepted consequence: a device at its quota ceiling keeps the OLD working pack and shows an error until the user chooses.
3. Confirm D4 (no `skipWaiting` / `claim`) and its cost: a future SW fix reaches an existing device only after all its tabs close. D4 does **not** remove the stale-shell/new-worker pairing inside the ~600 s HTML window; D1 + D2/D3 + D7 cover that residual.
4. Confirm the client retention cap of one previous generation (≈ 11.0 MB of pmtiles total on device, +5.75 MB incremental) **and** that, because re-download is opt-in and Cache API entries never expire on their own, the retained generation can persist indefinitely until the user acts.
5. **New — approve D7:** a retired `data/basemaps/osm_varna_<old>/` directory stays in the deployed tree for ≥ 1 deploy, `previous_version` is declared in `basemap_manifest.json` at the bump, and the `test_exactly_one_version_dir` gate is widened **and renamed** accordingly. Cost: ~5.75 MB extra in the repo/deploy for one cycle. The bump itself stays out of scope.
6. ~~Resolve the repo-state anomaly (detached HEAD / empty log in the session snapshot) before the Executor starts.~~ *Resolved in-session 2026-08-11: repo is on `main` at `227e595`; the anomaly was in the harness session header. M0 still re-verifies.*

**Signature line (to be filled by Petar):** `SIGNED: ______________  date: __________`

## 12. Planner notes to the Executor

- `tests/test_basemap_manifest.py:160` asserts the literal shape `PROTECTED_CACHES.includes(name)) return` and lines 167-168 assert the literals `networkFirst(req, CACHE_OFFLINE_PACK)` / `cacheFirst(req, CACHE_BASEMAP)` — refactors that change those call sites will break existing gates, which must be noticed and justified rather than quietly rewritten.
- Files that matter: `sw.js`, `index.html`, `tests/test_basemap_manifest.py`, `docs/decisions/002_osm_pmtiles_basemap_offline.md`, `scratch/basemap_b2/stop_b2_local.md`.
