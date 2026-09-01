# STOP B2 (local) — offline OSM/PMTiles basemap runtime integration

Date: 2026-07-06
Executor: Claude Code (CC)
Plan: `Varna_buildings/scratch/basemap_b2_plan.md` + `basemap_b2_plan_audit_addendum.md` (addendum wins).
Repo: `C:\git\Fire_Varna`. **No push. No flag flip. No data mutation.**

---

## 0. Verdict

B2 executed locally per plan v1 + audit addendum. All static + data-integrity gates green;
the render stack and the full `index.html` wiring were verified end-to-end with a headless
Chrome smoke (flag-false fully inert; flag-on renders below the overlays, 206 Range, no CDN).
Local commits are staged with explicit paths only (no parked dirt). **Awaiting: chat-Claude
audit → Petar sign → Petar push → production Range 206 gate + real-phone offline gate → STOP
B2 final → separate signed flag-flip commit.**

## 1. HEAD / commits

- Fire HEAD before work: `44321c6` (matches plan; `git show HEAD:index.html` sha256
  `e66403ec…` == plan §1 planning-time sha, so no unreconciled user edits).
- Local commits created by CC (NOT pushed; `main` ahead 2 of `origin/main`):
  - Commit 1 `chore(basemap): add signed B1 basemap artifacts and pinned deps` — `cca9d04`
  - Commit 2 `feat(basemap): wire flag-gated offline PMTiles layer` — `2eb370d`

## 2. Staged file list per commit

Commit 1 (artifacts + deps + copy/vendor scripts + static test):
```
scripts/copy_basemap_release.py
scripts/vendor_basemap_deps.mjs
data/basemaps/basemap_manifest.json
data/basemaps/osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b/**
vendor/basemap/pmtiles-3.2.1.js
vendor/basemap/protomaps-leaflet-4.0.1.js
tests/test_basemap_manifest.py
```
Commit 2 (runtime wiring + service worker):
```
index.html
sw.js
```
Parked dirty files (scratch/basemap_e0/*, dev_notice_*, marker_redesign_frame.md,
docs/plans/h2_kmz*, h4_kmz*, verify_*.py) were NOT staged. `scratch/basemap_b2/*` local
evidence NOT staged.

## 3. Artifact copy report (§6.2)

`scratch/basemap_b2/copy_report.json` — 7 files copied durably (temp→fsync→os.replace),
each re-read from disk and re-hashed; all `ok:true`. Manifest verified BEFORE copy.

| file | bytes | reread sha256 |
|---|---|---|
| varna_basemap.pmtiles | 5748578 | 29a8dee66465bed3eabaa2afa70efbe703b9e63b9cde84d4dcadb2436435f1b8 |
| varna_basemap_manifest.json | 1930 | 05dbfcf7d178206a5a89acb6c2e75d444377e8796c2486e74ce7137d00dc98ad |
| style.json | 1719 | 62cc123ee2227c4a95a249a2f788010eee57067a5ce72c594b4318834fc69135 |
| odbl/ATTRIBUTION.txt | 37 | 3090178a62e6ecfb19e20931f59609418360d9745963bc4cd91652c30f9431a0 |
| odbl/README_ODbL.md | 1276 | 71db0bb8aba80497e47c14467958aeab95d8ca8e91ad439be36172d3245cf620 |
| odbl/osm_varna_patch_v1.csv | 8045 | 4bae3267f0dea83ca753f61ef19750d059967f7dc2e1555ba4848f6b53b0b6d8 |
| odbl/osm_varna_source_manifest.json | 1684 | 427842588c77264ef8d891294cffbb5a0870f2f873c6a69bbe92cdf73304cf7a |

- B1 **content_sha256** confirmed `8a15054e722b12cb31afbc6cc3ff13a4cb7401dda7a8291f139794ac286fc3b8`.
- `pmtiles_sha256` `29a8dee6…`, `style_sha256` `62cc123e…` — all match B1 manifest.
- `parent_dir_fsync: "not_supported_on_windows"` (recorded honestly, not swallowed).
- Pruned dirs: none. Preserved: `range_canary.pmtiles`. **mbtiles NOT copied** (build artifact).
  Build-only `gate_report.md` / review CSV NOT copied.

## 4. Vendor report (§6.3)

`scratch/basemap_b2/vendor_report.json` — both deps downloaded durably, re-read, hashed;
raw byte counts MATCH the E0 anchors exactly (immutable pinned npm versions).

| dep | bytes (E0 anchor) | sha256 | SRI (sha384) |
|---|---|---|---|
| pmtiles@3.2.1 | 51739 (51739 ✓) | 367c19f8936d1d6c1b1820b0dee053f793fc29277655c3e471f5ed4d37b5f045 | sha384-QfbOCebHNw8pQiPAOd2IFee2v2A5VYZxBk0+JGZ5H+3mfzVIp6zsQNkTsfGJot93 |
| protomaps-leaflet@4.0.1 | 100591 (100591 ✓) | 8e3d2aa0f5a2fd46871ff9c6ed47fdcdb969bc6ed10bf6719dee507b46a2ec9e | sha384-GmP3jXNYFGjRNEfk47lHCeBRIf+V8dRyuQ6B+yJ6TPhOXIg7vpYy1CTKEnE8B84s |

## 5. Cache names (versioned; from `data/basemaps/basemap_manifest.json`)

```
fire-varna-core-osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b
fire-varna-offline-pack-osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b
fire-varna-basemap-osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b
```
The SW `activate()` prunes ONLY caches beginning with these B2 prefixes whose version is
not current, and explicitly SKIPS `fire-varna-search-v2` / `fire-varna-approx-addresses-v1`
(PROTECTED, double-guarded).

## 6. index.html before/after

| | raw bytes | gzip-9 bytes | sha256 |
|---|---|---|---|
| before (HEAD) | 422490 | 120273 | e66403ecc8bf325456d655e2232d5debd32715b45ab4ca7693d342e518e0a79b |
| after | 436822 | 124468 | 6feb372dbffcead8eb64271d62c3f4a533cd76b2b6dd2538f18e0dd9e33bf6ce |
| delta | +14332 | +4195 | — |

## 7. Default-load network assertion (flag false)

Headless smoke `?basemap_pmtiles=0` (Case A): NO request to `vendor/basemap/*`, `*.pmtiles`,
`data/basemaps/<version>/*`, or `sw.js`; NO service worker registered; hydrants fetched; NO
console errors. `#basemapToggle` click path is byte-for-byte the prior OSM⇄satellite toggle.

## 8. `BASEMAP_PMTILES_ENABLED=false` proof

`index.html`: `const BASEMAP_PMTILES_ENABLED = false;` (asserted by
`tests/test_basemap_manifest.py::test_flag_committed_false`).

## 9. Data non-mutation proof (§7.2)

```
data/hydrants.json          OK 89ad7559e5cb
data/search_index.json      OK 76a9357b1a0a
data/address_rows.json      OK 31c26e5139cc
data/approx_addresses_v1.json OK 97ebe841c9ba
DATA NON-MUTATION: PASS
```

## 10. Test / gate outputs

- `python -m unittest tests.test_basemap_manifest` — 15/15 OK.
- `python -m unittest discover -s tests` — 110/110 OK.
- `node --check sw.js` — OK. `node --check scripts/vendor_basemap_deps.mjs` — OK.
- `python -m py_compile scripts/copy_basemap_release.py` — OK.
- Leak scan of copied Fire files — CLEAN (only ODbL "no personal data" disclaimer text +
  manifest dep `source_url` provenance).

### Render smoke (`scratch/basemap_b2/render_smoke_report.json`) — proves the custom-schema adapter
Standalone probe mirrors the exact `index.html` adapter config against the real pmtiles via
a Range-capable server, driven by headless Chrome:
- **z13**: roads render; `buildingFill=0`, `label=0` — correctly gated by the style's minzoom
  (buildings 14, labels 15).
- **FF-001 z17 / Venchan z17**: buildings + roads + labels all paint; pmtiles served **206 with
  Range**; vendored deps same-origin; **zero CDN** basemap requests; zero page errors.

### Full index.html smoke (`scratch/basemap_b2/index_smoke_report.json`)
Case A (flag-false): A_noSW, A_inert, A_hydrants, A_noErrors all ✓.
Case B (flag-on, FF-001 z17): SW registers ✓; 3-way selector ✓; OSM default (no pmtiles before
select) ✓; vendored same-origin (2) ✓; no CDN ✓; **8 basemap canvases rendered** ✓; pane
z-index **basemap 200 < overlay 400 < marker 600** (overlays above) ✓; no console errors ✓.

## 11. Explained index.html diff (grouped)

- **flag/override**: `BASEMAP_PMTILES_ENABLED=false`, `BASEMAP_VERSION`, `BASEMAP_MANIFEST_URL`,
  `BASEMAP_OVERRIDE_KEY`; `isBasemapPmtilesActive()`, `basemapWantsOfflineInstall()` (gated on
  active — addendum П2); `initBasemapB2()` parses `?basemap_pmtiles=1/0` (sticky localStorage),
  `?offline=install`, and the `bm_lat/bm_lng/bm_z` test-center (active only). `=0` fully reverts
  (unregister sw.js + drop only the 3 B2 caches).
- **dependency loader**: `loadBasemapManifest()`, `loadBasemapScript()` (same-origin `vendor/`
  path + `integrity=sri_sha384` + `crossOrigin=anonymous`), `loadBasemapDeps()` (pmtiles before
  protomaps-leaflet). No static `<script src=vendor…>`; no CDN.
- **basemap selector**: click handler branches — inactive → old `setBasemap` toggle; active →
  `toggleBasemapSelector()` (3-way OSM / Спътник / Карта Варна (офлайн) menu, OSM default).
- **PMTiles layer / style / attribution**: `createOfflineBasemapLayer()` maps B1 style.json 1:1
  to protomaps-leaflet symbolizers; `offlineBasemapPane` z-index **150** (base tier, strictly
  below tilePane 200 — see review finding R1), pointer-events none, `bringToBack()`; ODbL
  attribution links `README_ODbL.md`.
- **SW registration / offline install**: `ensureBasemapServiceWorker()` registers `sw.js` only
  when active; `install-offline-pack` posted on opt-in; readiness signal → row + flashStatus;
  `reportStorageEstimate()` logs usage/quota and tries `persist()`.

## 12. Manual smoke notes

- Flag-false local (Case A): OSM default, satellite toggle unchanged, no basemap/SW requests,
  hydrants load — automated PASS.
- Flag-on local (Case B): selector present, offline selection renders local PMTiles (no CDN),
  overlays above, FF-001 area at z17 renders roads+buildings+labels — automated PASS.
- **Visual FF-001 / Venchan Cyrillic label legibility is a human check** (chat-Claude Chrome +
  Petar phone). The render smoke proves label GEOMETRY + halo pixels paint at z17 from the
  `name` field; exact glyph legibility is confirmed visually.

## 13. Skipped gates (cannot run pre-push)

- Production Range 206 on GitHub Pages PMTiles path (§7.5) — needs Petar push.
- Real-phone offline gate (§7.6) — needs Petar push (iOS SW requires HTTPS Pages).

## 14. Open item for sign-off (airplane-mode default basemap)

Per plan §6.4 "OSM remains selected by default even when the capability is active", the app
does NOT persist the last-chosen basemap. Consequence for §7.6 step 9–10: after an
airplane-mode RELOAD, the map defaults to OSM (raster, cross-origin, not SW-cached) until the
user re-opens the selector and re-picks `Карта Варна (офлайн)` — which then works fully from
cache. If you want the offline basemap to auto-restore on reload (no OSM flash), that is a
small follow-up (persist `basemapMode`, restore when active). **Not implemented — flagged for
your decision** (kept faithful to the plan's "OSM default" line).

## 15. Petar post-push checklist (copied from plan §7.6)

1. Online, open: `https://petar1984.github.io/Fire_Varna/?basemap_pmtiles=1&offline=install`
2. Wait for "✓ Офлайн пакетът е готов" (selector readiness row / status) before airplane mode.
3. Open the basemap selector → choose `Карта Варна (офлайн)`.
4. Confirm the map renders and hydrant pins sit above the basemap.
5. Search a known Varna address, select a result — confirm search works.
6. Open `…/?basemap_pmtiles=1&bm_lat=43.204393&bm_lng=27.896573&bm_z=17` — confirm the FF-001
   street label is visible.
7. Open `…/?basemap_pmtiles=1&bm_lat=43.250046&bm_lng=27.985170&bm_z=17` — confirm Venchan is
   visible and Овеч still exists nearby.
8. Airplane mode ON. 9. Reload. 10. Confirm shell + hydrants + exact search + offline basemap
   (re-select per §14 note) — no blank canvas. 11. Airplane OFF.
12. To clear the device override later: `…/?basemap_pmtiles=0`.

Note (addendum Бележка 1): `?basemap_pmtiles=1` is STICKY on the device until an explicit `=0`;
anyone opening that URL self-enrolls in the pilot early — acceptable (signed artifact + "в
разработка" banner). Document in the field pilot briefing.

## 16. Statement

The field-pilot flag flip (`BASEMAP_PMTILES_ENABLED = true` or otherwise exposing the selector
to pilot users) is a SEPARATE signed commit AFTER STOP B2 final. This STOP does not flip it.

---

## Review outcome (adversarial multi-lens)

4 independent lenses (flag-safety, sw-cache-safety, adapter-fidelity, plan-compliance) ran in
parallel; every candidate finding was adversarially verified (try-to-refute). Result: **1
candidate, 1 CONFIRMED, 0 uncertain, 3 lenses clean.**

### R1 (CRITICAL, CONFIRMED, FIXED) — offline basemap pane tied the building-overlay tier
- **Defect:** `offlineBasemapPane` was set to z-index **200**, tying Leaflet's `.leaflet-tile-pane`
  (also 200). The Fire building overlay (`L.vectorGrid.protobuf`, no `pane:` option) inherits
  `pane:"tilePane"` (z 200). A custom pane created via `map.createPane` is appended LAST in
  `mapPane`, so at an equal z-index it wins the DOM tiebreak and paints ABOVE tilePane — the
  opaque offline base (`backgroundColor #f2f0e8`) would hide the building overlay. That is the
  plan §10 hard-STOP "building overlays render below the offline basemap." `bringToBack()`
  cannot fix it (it only reorders within the single-layer offline pane).
- **Why the first smoke missed it:** it asserted basemap < overlay(400)/marker(600) but did not
  cover tilePane(200) — the one tier the building overlay uniquely shares; and the buildings
  toggle is currently commented out (index.html:1515), so it is a LATENT violation that would
  surface the moment buildings are re-enabled (Т2).
- **Fix (applied):** `offlineBasemapPane` z-index → **150** (base tier, strictly below tilePane
  200 and below overlay/marker/popup). While offline is active, osm/sat are removed, so tilePane
  holds only the building overlay, which now correctly paints above the base.
- **Verification:** `index_smoke` now records `basemap 150 < tile 200 < overlay 400 < marker 600`
  and `B_overlaysAbove` additionally asserts `tileZ > basemapZ`. Re-run: render smoke ok=true,
  index smoke ok=true, 110/110 tests, data non-mutation PASS.

Lenses flag-safety / sw-cache-safety / plan-compliance returned **no findings**: flag-false
inertness, the PROTECTED-cache guard, the addendum П1 network-first split, П2 gating, the copy/
vendor hash discipline, and the no-leak/no-mbtiles/one-version-dir constraints all held.

