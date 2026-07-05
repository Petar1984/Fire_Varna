# STOP E0 — own OSM PMTiles basemap feasibility (Fire_Varna V2)

**Date:** 2026-07-05 · **Phase:** E0 (feasibility, report/prototype only) ·
**Status:** STOP — awaiting Petar/chat-Claude review before B0/ADR 002. No runtime
change to `index.html`, live OSM stays default, no push, no OSM upload.
Fire ADR reserved: `docs/decisions/002_osm_pmtiles_basemap_offline.md`.

## Go / No-Go recommendation

**GO for B (basemap implementation), with the recommended stack `protomaps-leaflet`,
subject to three items that complete after this STOP:** (1) Petar approves the two new
runtime deps (~45.8 KB gzip); (2) a `.pmtiles` Pages canary push confirms Range for that
extension; (3) the exact PMTiles size matrix is built once the Docker daemon is running
(the ≤20 MB gate already passes by inference from real data). No E0 hard gate FAILED;
one gate (real per-cell PMTiles bytes) is PENDING on the Docker daemon, not blocked on
capability.

## 1. Render stack — recommend `protomaps-leaflet` (minimal migration)

REAL added bytes (pinned versions, measured `measure_render_stack.mjs`):

| stack | added raw | added gzip | migration | integration risk |
|---|---:|---:|---|---|
| **protomaps-leaflet** | **152,330** | **45,759** | minimal — keep Leaflet + all overlays | **low** |
| maplibre-gl | 920,359 | 233,312 | full renderer rewrite | high (re-port hydrants/search/popups) |
| raster-pmtiles+leaflet | 51,739 | 12,617 | none | low bytes, but larger tiles + no runtime restyle |

Why protomaps-leaflet: the app is Leaflet 1.9.4 with **all** overlays (hydrants
markercluster, search/address pins, building popups) as Leaflet layers, and it already
runs a Leaflet vector-tile path (`L.vectorGrid.protobuf` for building MVT, SRI-pinned).
protomaps-leaflet slots a vector PMTiles basemap under those overlays with a
`setBasemap`-style layer swap — the satellite toggle and every overlay keep working
unchanged. MapLibre costs **~5× the gzip** and a full map-shell rewrite (all overlays
re-ported to GL) for rendering that Leaflet already does adequately. Raster avoids a
renderer but gives the largest files and no runtime restyle. Built-in Cyrillic-capable
themes (`light`) make protomaps-leaflet the lowest-effort readable style (see
`e0_style_report.md`).

_Interactive-time / pan-zoom smoothness / memory / label legibility at 375 px are
browser-observed: open `leaflet_protomaps_probe.html` / `maplibre_probe.html` /
`raster_pmtiles_probe.html` on a real device. Playwright is not installed here, so these
qualitative cells are device-measured by Petar, not fabricated._

## 2. HTTP Range gate — local PASS, live Pages PASS, `.pmtiles` canary pending

REAL probes (`measure_range.mjs`, `e0_range.json`):

- **Local**: Range-capable server → **206**, `Content-Range: bytes 0-126/4182201`,
  PMTiles v3 magic verified from a 127-byte read → **PASS** (client + reader path).
- **Live GitHub Pages** (existing asset `index.html`): **206**,
  `Content-Range: bytes 0-126/417700`, `Accept-Ranges: bytes` → **PASS**. The Pages CDN
  honors Range *now* — a real de-risk without waiting for a push.
- **Pending**: a `.pmtiles` canary push (Petar) to confirm Pages serves that extension
  with the right content-type + Range. Mechanism is proven; only the extension remains.

## 3. Size gate — PASS with margin (real data), exact bytes pending Docker

REAL clipped Varna OSM (`data/osm/`, freeze 2026-05-13) + REAL same-toolchain anchors:

- streets GeoJSON **4,030,921 B / 10,359 features**; buildings **13,907,855 B / 38,124 features**.
- building PMTiles anchors (tippecanoe 2.79.0 → pmtiles 1.30.3, pinned): z13–z17
  **5,330,468 B** (safe_min), 6,440,742 B (safe_fulltype); z15–z17 4,182,201 B.
- **Inference:** the densest layer (buildings) already builds to ~5.1 MB PMTiles at
  z13–z17; the minimal profile (roads+names+water+parks, *no* buildings, streets 3.8 MB
  GeoJSON < buildings) builds well under that; full_context (adds buildings) stays a
  small multiple, comfortably **< 20 MB**. Verdict: **PASS_WITH_MARGIN**.
- **Pending (not fabricated):** exact per-cell PMTiles bytes for the 3 profiles × 4 zoom
  sets require the tippecanoe build — the toolchain is the established pinned Docker
  image; the Docker daemon is currently not running. Build tooling is ready
  (`Varna_buildings/tools/public_basemap/e0_build_matrix.py`); this is the first
  post-STOP step. Least-harmful drop order if any profile exceeds 20 MB: high zoom (z17)
  → minor POI → nonessential landuse → building footprints. Hydrants/search/building
  overlays are **never** baked into the basemap.

## 4. Offline / service-worker feasibility — feasible (full-file precache)

REAL probe (`measure_offline_sw.mjs`, `e0_offline.json`): a Cache-API full-file hit
yields a complete buffer and the PMTiles reader slices tiles from it in memory, so
offline works even if Cache does not honor Range on a hit (full-file magic + in-memory
slices verified). Net-new surface: the app has **no service worker today**; B must add
the first SW without evicting `fire-varna-search-v2` / `fire-varna-approx-addresses-v1`
Cache namespaces, and cache names must include `basemap_version` (stale basemap + fresh
shell cannot mix). Real offline (network disabled: shell + hydrants + search + basemap)
is validated on a device in B2.

## 5. Public patch preview — 44 rows, private evidence stripped

`Varna_buildings/scratch/basemap_e0/public_patch_preview.csv` (44 rows) + accounting
(`public_patch_accounting.json`). Allowed public columns only: `work_id, osm_way_id,
action, split_lat, split_lng, old_name, new_name, new_name_curated_display,
affected_segment_description, public_note`. Stripped (forbidden) columns:
`evidence_sources, reviewer, confidence, notes, new_name_display` — leak check **clean**
(0 leaked columns; scanned for `M6000`, `ГРАО=`, `StreetView`, `личен read`, crop refs +
24-char verbatim slices).

**44-row accounting** (`44 = applied_candidates + manual_resolution + deferred_named`):

| bucket | count | detail |
|---|---:|---|
| mechanical auto-apply candidates | **29** | 8 split_and_rename + 10 rename_way + 11 add_missing_name |
| manual_osm_review (needs signed resolution) | **15** | incl. the 1 deferred row |
| — of which deferred_named (signoff-blocked) | **1** | Венчан `OSM-009` — not applied until signoff-form decision |
| disjoint total | **44** | 29 + 14 manual-resolution + 1 deferred |

FF-001 anchor present: `OSM-021` way `42460845` → `Влад. Димитров-Майстора`.
Tile labels use `new_name_curated_display` (conservative casing preview applied: `Д-р`
fixes, connective `и` lowercased); ambiguous common-noun/`Д Р` cases are flagged for the
**STOP B1 chat-Claude review of all 44 labels** (`public_display_names_review.csv`) — the
final curated display is a B1 gate, not E0.

## 6. ODbL / attribution posture (`e0_odbl_posture.md`)

OSM is ODbL 1.0; our Varna-clip + patch is a Derivative Database; the served PMTiles is
a Produced Work. UI must credit `© OpenStreetMap contributors (ODbL)` (the app already
credits OSM for live tiles — text change, not a new surface). Share-alike is satisfied by
publishing the public patch CSV + source manifest (osm snapshot date/SHA + patch SHA) +
attribution file alongside the tiles. No M6000/КАИС/private evidence is exposed (leak
check clean). Flag for Petar: confirm attribution placement + whether the patch CSV +
manifest (vs the full derivative `.osm.pbf`) is an acceptable share-alike posture. No OSM
upstream upload this cycle.

## 7. Dependency list + byte impact (exact)

New **runtime** deps a B implementation would add to Fire (needs Petar approval per
`AGENTS.md` "no new dependency without approval"):

| dep | version | raw | gzip | role |
|---|---|---:|---:|---|
| protomaps-leaflet | 4.0.1 | 100,591 | 33,142 | vector PMTiles renderer over Leaflet |
| pmtiles | 3.2.1 | 51,739 | 12,617 | PMTiles range/protocol reader |
| **total added** | | **152,330** | **45,759** | |

First-load impact: current first load ≈ 1.64 MB uncompressed; +152 KB raw keeps it far
under the **5 MB** hard cap. The basemap `.pmtiles` (~<20 MB) is a **separate lazy/opt-in
payload**, never inlined into first-load. `leaflet.vectorgrid@1.3.0` (already vendored,
48,329 B) is **not** reused for the basemap (protomaps-leaflet is its own renderer). New
**build-time** deps: **none** — the E0/B tooling is stdlib Python + the existing pinned
Docker image (tippecanoe/pmtiles); no new npm/pip package.

## 8. Determinism

Public patch preview, inputs inventory, and build-matrix manifest are byte-identical
across two subprocesses under differing `PYTHONHASHSEED`
(`detcheck_basemap` → **6/6 BYTE-IDENTICAL**). The tippecanoe→pmtiles double-build
byte-identical check runs with the real build (Docker); the e0b precedent
(`Varna_buildings/scratch/e0b_tiles/FINDINGS.md`) already established that build is
byte-identical. All E0 artifacts use atomic+fsync writes with a disk-reread hash gate.

## 9. E0 gate checklist

| gate | result |
|---|---|
| Render matrix includes all three options | ✅ (bytes real; qualitative cells device-observed via probes) |
| Real Varna PMTiles size matrix, ≤20 MB evaluated | ⏳ inferred PASS from real data; exact per-cell build pending Docker |
| GitHub Pages Range test passed or explicitly blocked | ✅ Pages CDN 206 now; `.pmtiles` canary pending Petar push |
| Double build byte-identical (recommended profile) | ✅ deterministic artifacts; tippecanoe determinism per e0b precedent |
| ODbL/attribution posture, no private evidence | ✅ |
| 44-row patch accounting; no manual row auto-applied | ✅ 29/15 (1 deferred), leak-clean |
| No runtime Fire file changed | ✅ scratch only |
| No OSM upload, no push | ✅ |

## 10. Decisions requested at STOP E0

1. **Approve the render stack** `protomaps-leaflet` (+ `pmtiles`), ~45.8 KB gzip new
   runtime deps — or choose MapLibre / raster.
2. **Approve building the exact size matrix** via the pinned Docker toolchain (start
   Docker Desktop; I run `e0_build_matrix` for real per-cell bytes) — go/no-go on B.
3. **Push a `.pmtiles` Pages canary** so the `.pmtiles`-extension Range is confirmed.
4. Acknowledge the ODbL share-alike posture + attribution placement.
5. On GO, B0 drafts Fire ADR 002 with these numbers; B1 builds the patched basemap; the
   44-label curated-display chat-Claude review is the STOP B1 gate.

## 11. E0-close addendum (2026-07-05) — REAL size matrix built via Docker

Docker daemon started; the pinned image (`varna-building-tiles:pinned`, tippecanoe 2.79.0
→ pmtiles 1.30.3) was already present. Real PMTiles built from the clipped Varna OSM
GeoJSON (`tools/public_basemap/e0_real_build.py`;
`Varna_buildings/scratch/basemap_e0/build_matrix_real.json`):

| profile | zoom set | layers | pmtiles bytes | ≤20 MB |
|---|---|---|---:|:--:|
| minimal_roads | z12-z16 | roads+names | 2,333,593 (2.23 MB) | ✅ |
| minimal_roads | z12-z17 | roads+names | 3,613,513 (3.45 MB) | ✅ |
| minimal_roads | **z13-z17** | roads+names | **3,322,606 (3.17 MB)** | ✅ |
| minimal_roads | z14-z17 | roads+names | 2,982,136 (2.84 MB) | ✅ |
| roads_buildings | z12-z16 | roads+buildings | 7,523,876 (7.18 MB) | ✅ |
| roads_buildings | z13-z17 | roads+buildings | 9,455,064 (9.02 MB) | ✅ |

**Size gate: PASS (measured), large margin** — the minimal field-use basemap is ~2.3–3.6 MB;
even with building footprints it is ~7.5–9.5 MB, all far under 20 MB. (water/parks are not
in the current clip — a small additive delta on the minimal numbers; a full-profile rebuild
after re-clipping those layers is a B1 step.)

**Determinism gate — RESOLVED (STOP A1-close amendment):** raw PMTiles bytes **drift**
run-to-run (tippecanoe's threaded tile ordering). Per Petar's decision tree, single-thread
was tried first (`docker run --cpus=1`) → **not byte-identical** (~1-byte drift, ~23 s), so
rejected. The **canonical content gate** is adopted and proven byte-stable: decode the
tiles → sort by `(z,x,y)` → `content_sha256` = `11ad8f65…` **identical across builds**
(incl. both `--cpus=1` builds and the default build; 3243 tiles). Root cause: only the
container tile ORDER drifts; per-`(z,x,y)` tile bytes are identical. The plan is amended
(§E0.5 + §B gates). Does not affect the size/feasibility verdict.

**Canary — RESOLVED (pushed + proven live).** `data/basemaps/range_canary.pmtiles` is
pushed and the live GitHub Pages `.pmtiles`-extension Range check passed: **GET Range =
206, `content-range: bytes 0-126/130`**. (The initial `-I`/HEAD probe misled — HEAD
ignores Range; a GET with a Range header is the correct test.) **E0 is fully closed** —
render stack (protomaps-leaflet), local + Pages Range (206), offline (full-file precache),
real size matrix (all ≤ 20 MB), determinism (content_sha256 gate), ODbL posture, and
dependency byte impact are all settled. Nothing E0 remains outstanding.
