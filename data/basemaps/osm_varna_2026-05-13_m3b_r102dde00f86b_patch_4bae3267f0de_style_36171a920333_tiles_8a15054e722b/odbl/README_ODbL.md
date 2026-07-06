# Varna basemap — ODbL package (B1 release candidate)

**License:** © OpenStreetMap contributors (ODbL)

This package contains a public OpenStreetMap-derived vector basemap of Varna and the
audited public patch applied to it. Data © OpenStreetMap contributors, licensed under the
Open Database License (ODbL). See https://www.openstreetmap.org/copyright.

## Contents
- `varna_basemap.pmtiles` — vector tiles (roads + building footprints, z13–z17).
- `osm_varna_patch_v1.csv` — the applied public patch operations (street name fixes).
- `osm_varna_source_manifest.json` — snapshot date, source/patch/style/tile hashes, toolchain.
- `ATTRIBUTION.txt` — required attribution.

## Provenance
- OSM snapshot: 2026-05-13 (Geofabrik Bulgaria extract, clipped to Varna).
- Patch: osm_varna_patch_v1.csv sha256 `4bae3267f0dea83ca753f61ef19750d059967f7dc2e1555ba4848f6b53b0b6d8`.
- Tiles content_sha256 `8a15054e722b12cb31afbc6cc3ff13a4cb7401dda7a8291f139794ac286fc3b8` (canonical, build-stable).
- Version: `osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b`.

No private/derived evidence (field survey internals, registry intel, personal data) is
included. Patch operations are limited to official street-name corrections.
