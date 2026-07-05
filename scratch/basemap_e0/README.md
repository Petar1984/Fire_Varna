# Fire_Varna basemap E0 probes (V2 feasibility)

Scratch-only feasibility probes for an OSM-derived vector PMTiles basemap (offline,
GitHub Pages). **No runtime change** to `index.html`; live OSM tiles stay the default.
No push, no OSM upload. Read the STOP report first: `e0_stop_report.md`.

## Files

| file | what |
|---|---|
| `e0_stop_report.md` | **the STOP E0 deliverable** — render/range/size/offline/ODbL/deps + go/no-go |
| `measure_render_stack.mjs` | REAL added JS/CSS raw+gzip bytes per stack → `e0_render_matrix.csv`, `e0_render_bytes.json` |
| `measure_range.mjs` | REAL HTTP Range probe (local server + live Pages) → `e0_range_report.md`, `e0_range.json` |
| `measure_offline_sw.mjs` | REAL full-file-precache offline check → `e0_offline_report.md`, `e0_offline.json` |
| `leaflet_protomaps_probe.html` | render probe — vector PMTiles over Leaflet (minimal migration) |
| `maplibre_probe.html` | render probe — MapLibre GL (full migration) |
| `raster_pmtiles_probe.html` | render probe — raster PMTiles over Leaflet |
| `e0_odbl_posture.md` | ODbL/attribution/share-alike posture |
| `e0_style_report.md` | Cyrillic style gate + effort |
| `e0_size_matrix.csv` | size anchors + gate verdict (build matrix lives in Varna_buildings) |

The PMTiles build tooling + patch preview live in
`Varna_buildings/tools/public_basemap/` and `Varna_buildings/scratch/basemap_e0/`.

## Run

```powershell
# byte + range + offline measurements (Node)
cd C:\git\Fire_Varna
node scratch/basemap_e0/measure_render_stack.mjs --all
node scratch/basemap_e0/measure_range.mjs --local --pages-existing
node scratch/basemap_e0/measure_offline_sw.mjs --local

# render probes: open the *.html on a real 375px device; pass ?pmtiles=URL once a
# basemap .pmtiles is built and served (python -m http.server 8000)
```

Interactive-time / pan-zoom / memory / label-legibility are browser-observed on a real
device (Playwright is not installed here — see the STOP report). The byte, Range, and
offline numbers are measured programmatically and are real.
