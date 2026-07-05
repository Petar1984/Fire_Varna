# E0 ODbL / attribution posture

**Status:** planning/legal-posture only — NOT legal advice. Where the ODbL
share-alike boundary for a tiled derivative is unclear, STOP and route to Petar for
a manual license confirmation before B proceeds.

## Source and derivative chain

```
OpenStreetMap (ODbL 1.0 database)
  -> date-pinned Geofabrik Bulgaria PBF (hash-locked)
  -> osmium clip to Varna boundary (data/osm/*.geojson, freeze 2026-05-13)
  -> apply 29 mechanical patch rows (rename_way / split_and_rename / add_missing_name)
  -> tippecanoe vector tiles -> PMTiles  (a Produced Work rendered from the DB)
```

OSM is licensed **ODbL 1.0** (the database) with **DbCL 1.0** on the contents. The
Varna clip + our patch is a **Derivative Database**; the PMTiles served to users is a
**Produced Work** created from that database.

## Answers to the E0.6 questions

1. **Exact attribution text for the Fire UI.** Every view that shows the basemap must
   credit: **`© OpenStreetMap contributors`** (linking to
   `https://www.openstreetmap.org/copyright`), plus a note that the data is under
   **ODbL**. Recommended one-line UI string:
   `© OpenStreetMap contributors (ODbL) · Fire_Varna local corrections`.
   The current app already credits `© OpenStreetMap` for live tiles
   (`index.html` `OSM_ATTRIB`); the PMTiles basemap reuses the same attribution
   control, so this is a text change, not a new surface.

2. **What public derivative files must be shared (share-alike).** Because we
   distribute a Produced Work (tiles) made from a Derivative Database, ODbL §4.6
   share-alike attaches to the **Derivative Database**. We satisfy it by publishing,
   alongside the tiles: the **public patch CSV** (`osm_varna_patch_v1.csv`), the
   **source manifest** (OSM snapshot date + SHA-256 + patch SHA), and an
   **attribution/licence file**. That lets anyone reconstruct our derivative database
   from public OSM + our documented changes.

3. **Is the public patch CSV enough for the patch component?** Yes. The patch CSV is
   the curated worklist reduced to the allowed public columns (`work_id, osm_way_id,
   action, split_lat, split_lng, old_name, new_name, new_name_curated_display,
   affected_segment_description, public_note`) — every change is a documented,
   reproducible operation against the dated OSM snapshot. It carries **no** M6000 crop
   refs, private reviewer notes, raw КАИС evidence, cadnum, or private run paths (the
   E0 patch-preview leak check is clean).

4. **What manifest/licence files travel with the PMTiles.** At minimum:
   `odbl_attribution.txt` (the OSM/ODbL credit + link), `source_manifest.json`
   (osm_snapshot_date, osm_pbf_sha256, patch_sha256, basemap_version), and the
   `osm_varna_patch_v1.csv` itself. These accompany `varna_basemap.pmtiles` in the
   release directory and are copied into `Fire_Varna/data/basemaps/ATTRIBUTION.txt` +
   `basemap_manifest.json`.

5. **Is any M6000-specific evidence field accidentally exposed?** **No.** The public
   patch preview strips all forbidden columns and the leak check (distinctive-fragment
   scan for `M6000`, `ГРАО=`, `StreetView`, `личен read`, `crop review`, `6 subagents`,
   plus a 24-char verbatim slice of each forbidden field) reports **0 leaked columns**.

## Open posture flags for Petar (manual confirmation before B)

- Confirm the attribution **placement** (persistent on-map credit vs an "i" panel) is
  acceptable for ODbL on a mobile emergency UI.
- Confirm that publishing the patch CSV + source manifest (not the full derivative
  `.osm.pbf`) is an acceptable share-alike posture for our distribution, or whether the
  patched extract should also be published.
- No OSM **upstream upload** in this cycle (Petar's standing decision); the worklist
  stays a local derivative artifact.
