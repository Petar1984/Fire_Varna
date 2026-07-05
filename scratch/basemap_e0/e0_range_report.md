# E0 HTTP Range report

REAL Range probes (see e0_range.json for full payloads).

- **local_range_capable_server**: PASS
  - Node Range-capable server + PMTiles v3 magic verified from a 127-byte read
- **github_pages_range_existing_asset**: PASS — status 206, content-range `bytes 0-126/417700`
  - Range behavior of the live Pages CDN on an existing asset (not a .pmtiles). A .pmtiles canary is still needed to confirm content-type + Range for that extension.

_Pages `.pmtiles` canary (content-type + Range for the extension) still requires a Petar canary push; Range behavior of the Pages CDN itself is measured above._
