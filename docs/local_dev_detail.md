# Local-dev: building detail panel without deploying the Worker

The search→detail panel (C4) fetches a building's safe detail JSON. In production that
comes from the Cloudflare Worker route `GET /detail/{g}` (private R2). For **local
development you do NOT need the Worker or R2** — on `localhost` / `127.0.0.1` the app
fetches the detail from a **static file** instead:

```
details/buildings/v1/{g}.json      (served by http.server, relative to Fire_Varna/)
```

(See `detailUrlFor()` in `index.html`. On any non-localhost host it uses the Worker.)

## Steps

1. **Build the detail records** (in `Varna_buildings`, with the stable salt):
   ```powershell
   cd C:\git\Varna_buildings
   $env:VARNA_BD_SALT='<the same stable secret used everywhere>'
   npm run build:building-details
   ```
   This writes `output/building_tiles/details/buildings/v1/{g}.json` (one per building).

2. **Copy them into Fire_Varna** (the `details/` tree is gitignored — never commit it):
   ```powershell
   $src = 'C:\git\Varna_buildings\output\building_tiles\details\buildings\v1'
   $dst = 'C:\git\Fire_Varna\details\buildings\v1'
   New-Item -ItemType Directory -Force $dst | Out-Null
   Copy-Item "$src\*.json" $dst
   ```

3. **Serve Fire_Varna over HTTP** and open it via localhost:
   ```powershell
   cd C:\git\Fire_Varna
   python -m http.server 8000
   ```
   Open <http://localhost:8000> (use `localhost`, not the `file://` path).

4. **Try it:** search a block (e.g. `владиславово бл 306`) and select the result. The
   detail panel lights up from the local static file — bottom sheet on a narrow window,
   right side panel on a wide one. The entrance pin stays visible (the map pans so the
   sheet/panel never covers it).

## Notes

- The `g` in the filename is the SAME opaque key the public search index carries on a
  block/MF row. The detail files are keyed by it 1:1 (Phase-2: `g == detail key`).
- `details/` is **gitignored** (`.gitignore`): the per-building JSONs are private and are
  uploaded to R2 by Petar — they must never be committed to the public repo.
- The records must be built with the SAME `VARNA_BD_SALT` as the public `search_index.json`,
  otherwise the `g` in search won't match the detail filenames and every lookup 404s.
- Production: Petar deploys the Worker (dashboard-paste of `worker/index.js`) and uploads
  the `details/buildings/v1/` subtree to the private R2 bucket. No agent deploys or uploads.
