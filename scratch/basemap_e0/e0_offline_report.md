# E0 offline / service-worker feasibility

REAL full-file-precache probe (see e0_offline.json).

- **Full-file precache path**: FEASIBLE — archive 3.99 MB, PMTiles magic true, in-memory tile slices OK.
  - A Cache API full-file hit yields a complete buffer; the PMTiles reader slices tiles from it in memory, so offline works even if Cache does not honor Range on the hit.
- **Budget**: basemap 3.99 MB (target ≤ 20 MB: true); separate from the 5 MB first-load.

## Service-worker design requirements (net-new; no SW today)
- introduce the FIRST service worker (none today) — new surface; must not evict fire-varna-search-v2 / fire-varna-approx-addresses-v1 Cache namespaces
- cache name MUST include basemap_version so a stale basemap + fresh shell cannot mix
- offline = app shell + hydrants.json + search bundles + basemap all answer with network disabled
- range-on-demand cache is an alternative to full precache — must prove returning coverage after partial use

_Full SW behavior (registration, install/activate, cross-origin, real offline toggle) is browser-only and is validated in B2 on a real device; this probe proves the reader path._
