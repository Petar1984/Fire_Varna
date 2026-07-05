# ADR 002 — own OSM-derived PMTiles basemap + offline

**Date:** 2026-07-05 · **Status:** DRAFT — STOP B0, pending Petar signature · follows the
closed E0 feasibility (`scratch/basemap_e0/e0_stop_report.md`) · references ADR 020
Amendment 2 (public-safe bundle + publish gate) · precedes B1 (build artifacts) / B2
(runtime integration) · report/flag-gated until signed

## Context

Fire_Varna renders a Leaflet 1.9.4 map with live OSM raster tiles as the default basemap
(+ an Esri satellite toggle). Petar decided (2026-07-05) NOT to upload the M3b name fixes
to OSM upstream, and instead to ship an **own basemap**: a hash-locked OSM snapshot of
Varna + our 44 curated patches, compiled to **PMTiles**, served from GitHub Pages, with
**full offline** (service worker: basemap + hydrants + search). This ADR decides the Fire
runtime map shell, basemap delivery, offline strategy, and mobile budgets. E0 is closed and
supplies the numbers below.

## Decision

- **D1 — Render stack: `protomaps-leaflet`** (vector PMTiles over the existing Leaflet).
  E0-measured added bytes: **~152 KB raw / ~45.8 KB gzip** (`protomaps-leaflet@4.0.1` +
  `pmtiles@3.2.1`), vs MapLibre GL ~233 KB gzip + a full renderer rewrite, vs raster
  ~12.6 KB gzip but larger tiles + no runtime restyle. protomaps-leaflet keeps Leaflet and
  every existing overlay (hydrants markercluster, search/address pins, building popups) and
  slots the basemap under them with a `setBasemap`-style layer swap. The two deps are
  **vendored/pinned** (SRI), not live CDN (Petar, STOP E0). No hydrant/search/building data
  is ever baked into the basemap.

- **D2 — Hosting: static GitHub Pages PMTiles with HTTP Range.** E0 proved the Pages CDN
  honors Range: local Range-capable server and the live Pages `.pmtiles` canary both return
  **206** (`content-range: bytes 0-126/130`; a GET-with-Range, since HEAD ignores Range).
  Fallback (only if a future Pages change breaks Range): Worker/R2 basemap serving, as a
  separate ADR change.

- **D3 — Feature flag + rollout: `BASEMAP_PMTILES_ENABLED = false` until all B2 gates pass.**
  Live OSM raster stays the default while the flag is false; the satellite toggle keeps its
  exact current behavior; the PMTiles basemap is a third mutually-exclusive layer in the
  same switcher. Flip is a signed field-pilot step (STOP B2).

- **D4 — Offline strategy: full-file PMTiles precache (SW), reader tolerates full-file
  reads.** E0 proved a Cache-API full-file hit yields a complete buffer the PMTiles reader
  slices in memory (offline works even if Cache does not honor Range on a hit). The app has
  **no service worker today** — B introduces the first one; it must NOT evict the existing
  `fire-varna-search-v2` / `fire-varna-approx-addresses-v1` Cache namespaces. "Full offline"
  = app shell + hydrants + search + basemap answer with the network disabled (validated on a
  real device at STOP B2).

- **D5 — Cache versioning: `basemap_version` in every cache name + manifest.** A stale
  basemap and a fresh app shell can never mix. Version string:
  `osm_varna_<snapshot_date>_m3b_r102dde00f86b_patch_<sha12>_style_<sha12>_tiles_<sha12>`.

- **D6 — Determinism gate: canonical tile-content hash, not raw bytes.** E0 measured that
  tippecanoe's threaded tile ordering drifts the raw PMTiles/mbtiles bytes run-to-run while
  the per-`(z,x,y)` tile bytes are identical. So the B1 signed-reproducible gate asserts a
  `content_sha256` (decode tiles → sort by `(z,x,y)` → hash), proven byte-stable
  (`11ad8f65…`); single-thread (`--cpus=1`) was tried first and rejected as non-byte-identical.

- **D7 — Size budget: measured PASS with margin.** Real Varna builds (pinned tippecanoe
  2.79.0 → pmtiles 1.30.3): minimal roads+names **2.2–3.6 MB** (z12-16…z12-17),
  roads+buildings **7.2–9.0 MB** — all far under the 20 MB target. The basemap is a separate
  lazy/opt-in payload, never inlined into the 5 MB first-load. Least-harmful drop order if a
  profile ever exceeds 20 MB: high zoom (z17) → minor POI → nonessential landuse → building
  footprints.

- **D8 — ODbL / attribution.** OSM is ODbL 1.0; our clip+patch is a Derivative Database; the
  served PMTiles is a Produced Work. The UI credits **`© OpenStreetMap contributors (ODbL)`**
  (the app already credits OSM for live tiles — a text change, not a new surface).
  Share-alike is satisfied by publishing the public patch CSV + source manifest (snapshot
  date/SHA + patch SHA) + attribution file alongside the tiles. No M6000/КАИС/private
  evidence is exposed (E0 leak check clean). The 44-row patch is 29 mechanical auto-apply +
  15 manual_osm_review (1 deferred: Венчан OSM-009); tile labels use
  `new_name_curated_display` (chat-Claude review of all 44 = STOP B1 gate). No OSM upstream
  upload this cycle.

## Upstream refresh doctrine (implementation = B4, after B2; not this cycle)

The own basemap must not go stale. Refresh pulls only the NEW that does not conflict with
our verified truth. Mechanism: **three-way diff** (old snapshot ↔ new snapshot ↔ patch) +
an **Engine-1-lite guard**. Each patch row classifies mechanically:

| class | condition | action |
|---|---|---|
| `clean_reapply` | way present, old (wrong) name present | re-apply, automatic |
| `upstream_adopted` | the new snapshot already carries OUR name | retire the patch row with a dated note |
| `conflict` | third name / way split/deleted / geometry changed | conflict queue → human verdict |
| `free_flow` | zones/objects with no patch and no verified truth | admitted freely (the new streets — the point) |

The Engine-1-lite guard re-runs against the new snapshot and diffs the discrepancy report vs
the previous refresh baseline → catches OSM regressions on OUR verified streets outside the
patch (e.g. Срацимир→Страцимир reverting); new divergences → a mini M3b review (crops if
needed). Requirements (inherit the V2 doctrine): hash-locked snapshots; refresh report is a
run-dir artifact with a class balance (conflicts named); atomic writes + disk-reread; no
auto-apply of the `conflict` class (`upstream_adopted` retirement is automatic but visible);
`basemap_version` rotates + the SW cache updates by the B3 versioning scheme; **manual
trigger only** (Petar, ~quarterly or on a field signal) — no cron/autopush. Field-feedback
rows may inject new patch rows in the same cycle. Generalization (separate ADR after V2, not
B4): the same diff filter applies to КАИС and ГРАО refreshes (verified M3b verdicts are the
veto layer for all three).

Open points for signature: (1) which tool does way-level diff (osmium-based vs own —
E0 inheritance); (2) how many old basemap versions the repo keeps (size — likely current +
manifest history only); (3) Engine-1-lite guard scope (fast = patch+verified streets each
refresh; full = whole-city M3b re-sweep once a year).

## Consequences

- Smallest-migration vector basemap; live OSM + satellite untouched until the flag flips.
- First service worker in the app — a real new surface, scoped to not disturb search caches.
- A signed, reproducible, offline-capable basemap with a refresh path that keeps it fresh
  without silent OSM regressions.

## Decision requested at STOP B0

Sign the runtime direction (D1–D8) + the refresh doctrine section, or send back. On sign:
B1 builds the patched basemap artifacts (STOP B1 = patch/label proof + determinism); B2
wires the flag-gated runtime + offline on a real device (STOP B2 = go/no-go for a field
pilot).

## Alternatives considered

- **MapLibre GL** — rejected: ~5× the gzip + a full renderer rewrite (re-port all overlays)
  for rendering Leaflet already does adequately (E0).
- **Raster PMTiles** — rejected as the primary: smallest JS but largest tiles and no runtime
  restyle; kept only as the fallback if vector Range/size ever fails.
- **Keep live OSM tiles only** — rejected: no offline, and it re-introduces the OSM name
  errors M3b fixed (the patch is the point).
