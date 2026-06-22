# E2 deploy runbook — building-tile gateway (PETAR'S HAND ONLY)

> **Every step below is Petar's hand. Claude Code did NOT execute any of these.**
> The executor produced and locally tested the code only. This runbook is the
> hand-off for the real deploy. Do the steps in order; nothing here is reversible
> for free, so confirm each before moving on.

Governing plan: `Varna_buildings/scratch/e2_serving_plan.md` (Codex-planned,
chat-Claude audited PASS + correction, Petar-signed 2026-06-22). Deploy stays a
**dashboard paste of `worker/index.js`** — `wrangler.toml` is local-dev only and
is NOT used to deploy.

Key facts the steps below depend on:

- PMTiles to publish: `Varna_buildings/output/building_tiles/safe_min/varna_buildings_safe_min_z15_z17.pmtiles`
- E1 manifest `gate.all_pass`: **true**; pmtiles SHA-256:
  `f1f92e297a9beacc0c3b46ae10032a0afd86f1a6b3e441e772eee7aeb9daffa1`
- R2 object key (matches `wrangler.toml` + what the upload script prints):
  `tiles/buildings_safe_vf1f92e297a9beacc0c3b46ae10032a0afd86f1a6b3e441e772eee7aeb9daffa1.pmtiles`

---

## Step 1 — Enable R2 + create a PRIVATE bucket (Petar's hand)

1. Cloudflare dashboard → R2 → enable R2 (if not already).
2. Create a **private** bucket, e.g. `varna-building-tiles`. 
   - **Do NOT** enable a public bucket URL or the `r2.dev` dev URL. The PMTiles
     must never be directly fetchable; only the Worker's z/x/y route serves it.

## Step 2 — Upload the PMTiles via the audited script (Petar's hand)

Review `worker/scripts/publish_building_tiles_r2.mjs` first, then from `worker/`:

```bash
# Dry-run first (default — verifies manifest gate + sha, prints the key, no upload):
node scripts/publish_building_tiles_r2.mjs

# Real upload (only after the dry-run looks right; uses YOUR wrangler auth):
node scripts/publish_building_tiles_r2.mjs --apply --remote --bucket varna-building-tiles
```

The script refuses to upload unless `manifest.gate.all_pass === true` and the
file's SHA-256 matches the manifest. It never creates the bucket, never sets a
secret/binding, never deploys. Confirm the printed object key equals the key
above.

## Step 3 — Bindings, secret, and vars in the dashboard (Petar's hand)

Worker → Settings → Variables and Secrets / Bindings. **Preserve the existing
`REPORTS_CACHE` KV binding and the `GITHUB_PAT` secret** — do not remove them.

Add:

- **R2 binding**: name `BUILDING_TILES` → the private bucket from Step 1.
- **Secret** `TILES_HMAC_SECRET` → a fresh long random string (Type: Secret).
  This signs/verifies tile tokens. Never paste it into source or this repo.
- **Vars** (plain text):
  - `BUILDING_TILES_OBJECT_KEY` = `tiles/buildings_safe_vf1f92e297a9beacc0c3b46ae10032a0afd86f1a6b3e441e772eee7aeb9daffa1.pmtiles`
  - `TILES_MIN_Z` = `15`
  - `TILES_MAX_Z` = `17`
  - `TILES_TOKEN_TTL_S` = `600`
  - `TILES_RATE_WINDOW_S` = `60`
  - `TILES_TOKEN_RATE_MAX` = `30`   (tune later; in-code limit is best-effort only)
  - `TILES_TILE_RATE_MAX` = `600`   (tune later; in-code limit is best-effort only)

## Step 4 — Dashboard rate-limit + bot rules (Petar's hand, AUTHORITATIVE layer)

The in-Worker per-IP limiter is best-effort per isolate only. The real
protection is here:

- Add Rate Limiting rules for `/tiles/buildings/token` and
  `/tiles/buildings/v1/*` (per-IP thresholds appropriate for one map session).
- Add a Bot Fight / WAF managed challenge for suspicious traffic to `/tiles/*`.

## Step 5 — Deploy = paste `worker/index.js` (Petar's hand)

1. Worker → Edit code → select all → paste the updated `worker/index.js` → Deploy.
   (This is the documented deploy workflow; `wrangler.toml` is NOT used here.)
2. Record the new version:
   - `worker/README.md` → bump *Active version* (move prior into *Previous deploy*).
   - `Fire_Varna/docs/activeContext.md` → *Worker version deployed*.

## Step 6 — Smoke-verify against the live URL (Petar's hand)

- `GET /issues` → 200 with `X-Cache-Status` and `X-Parse-Warnings: 0` (existing
  route still healthy).
- `POST /` (a throwaway test report) → creates the GitHub issue as before.
- `GET /tiles/buildings/token` with an allowed `Origin` → 200 + a token + 
  `Cache-Control: no-store`.
- `GET /tiles/buildings/v1/15/18926/12026.mvt?token=<token>` with that `Origin`
  → 200, `Content-Type: application/vnd.mapbox-vector-tile`,
  `Cache-Control: public, max-age=86400, s-maxage=604800, immutable`,
  `X-Robots-Tag: noindex`, non-empty body.
- Negative checks: same tile URL with **no token** → 401; with **no Origin and no
  Referer** → 403. Confirm a direct fetch of the bucket object URL is **not**
  possible (no public URL exists).

---

### Rollback

The `/tiles/*` routes are additive and isolated. If a tile problem appears,
re-paste the **previous** `worker/index.js` (per `worker/README.md` version
table) — the existing `OPTIONS` / `GET /issues` / `POST /` routes are unchanged
by E2, so a rollback does not affect the hydrants app. The R2 object + bindings
can stay; an old Worker version simply won't reference them.
