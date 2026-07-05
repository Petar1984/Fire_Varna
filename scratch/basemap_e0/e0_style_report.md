# E0 style gate — Bulgarian/Cyrillic basemap style

Goal (E0.7): a readable, emergency-appropriate Cyrillic style covering streets/roads,
water, parks, and (where the profile allows) building shapes — no dark/low-contrast
styling that hurts field use.

## Cyrillic labels — source is real and already Cyrillic

Varna street/place names in the clipped OSM extract carry Cyrillic `name` values
(`data/osm/varna_streets_2026-05-13.geojson`, 10,359 features). Labels come from the
tile `name` field, so **no transliteration layer is needed** — the labels render in
Bulgarian as-is. Our patch supplies `new_name_curated_display` for the 44 corrected
ways (curated casing, STOP B1 review) so corrected segments read cleanly.

## Style effort by render stack

| stack | ready style? | effort | note |
|---|---|---|---|
| protomaps-leaflet | **yes** — built-in themes (`light`, `white`, `grayscale`, `dark`, `black`) | **low** | pick `light`; label font is the page font, so Cyrillic renders via the system stack. Minimal custom tweak for emergency contrast. |
| MapLibre GL | needs a `style.json` | medium | requires a Protomaps-basemap or OpenMapTiles-compatible style.json authored for our layer names; more moving parts. |
| raster PMTiles | style baked at build time | build-time only | labels fixed in the raster; no runtime restyle; larger files. |

## Recommendation

Use the **protomaps-leaflet `light` theme** as the E0 baseline: it is Cyrillic-capable
out of the box (labels are the OSM `name`), high-contrast, and needs no custom style
authoring for E0. A small custom override (thicker road casings, larger label
minimum size for gloves/sunlight) is a low-effort B-phase polish, estimated separately
in ADR 002. No dark theme for emergency use.

## Contrast / field-use constraints (carry into ADR 002)

- Minimum label size tuned for 375 px + sunlight + gloves (mobile-first rule).
- Road hierarchy legible at field-use zooms (z14–z17).
- Water/parks muted so hydrants (red) and search pins stay the visual priority — the
  basemap must never compete with the emergency overlays.
