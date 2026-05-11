# varna-hydrants-proxy (Cloudflare Worker)

Submission and polling proxy for the Varna hydrants app. Source of truth
for the Worker code lives here; deploys to Cloudflare are manual.

## Endpoints

- `POST /` — `{ title, body, labels }` → creates a labeled GitHub issue
  in `Petar1984/Fire_Varna`. Used by the in-app report flow.
- `GET /issues` — returns the parsed open `report`-labeled issues as a
  JSON feed. Two-layer cache (in-process memory + KV, 30 s TTL).
  Supports `?since=<ISO timestamp>` and `?limit=<1..100>`. Used by
  client polling at 15 s cadence.

## Deployed instance

| | Value |
|---|---|
| URL | `https://varna-hydrants-proxy.petar-dikov2019.workers.dev` |
| Active version | `50c2b2d2` (manually deployed 2026-05-07) |
| Rollback target | `e86c90a6` (earliest pre-KV deploy, POST-only) |
| Custom domain | none — only the default `*.workers.dev` |

Update the active version line above whenever a new version is deployed,
and mirror it in `docs/activeContext.md` under *Worker version deployed*.

## Bindings

- KV namespace `REPORTS_CACHE` → `varna_hydrants_reports_cache`. Used
  by `GET /issues` as the second cache layer (key `issues:report:v1`,
  TTL 30 s, written via `ctx.waitUntil`).

## Secrets

- `GITHUB_PAT` — GitHub fine-grained PAT with `Issues: write` on
  `Petar1984/Fire_Varna`. Set via Cloudflare dashboard → the Worker →
  Settings → Variables and Secrets → Add → Type: Secret. Never appears
  in source; only referenced as `env.GITHUB_PAT`.

## Deploy workflow

Cloudflare does not auto-deploy from this repo. The repo is the source
of truth; the dashboard receives a paste.

1. Edit `worker/index.js` locally and commit.
2. Push to `main`.
3. Cloudflare dashboard → Workers & Pages → `varna-hydrants-proxy` →
   Edit code → select all → paste the new `worker/index.js` → Deploy.
4. Record the new version ID in `docs/activeContext.md` and update the
   *Active version* row above in the same commit.
5. Smoke-verify against the live URL: a `GET /issues` returning 200
   with `X-Cache-Status` and `X-Parse-Warnings: 0` is sufficient.

## Stop and ask

- **Literal token committed by accident** — anything matching `ghp_*`,
  `github_pat_*`, or a raw `Bearer <value>` outside the
  `` `Bearer ${env.GITHUB_PAT}` `` template. If this happens:
  0. If the commit is still local (not yet pushed), discard with
     `git reset --soft HEAD~1` first to prevent the push. Only rotate
     the token after determining whether the commit is local or pushed.
  1. Rotate the PAT in GitHub immediately. Do this regardless of step 0
     — assume the token has leaked.
  2. Store the fresh value as the `GITHUB_PAT` secret in Cloudflare and
     redeploy.
  3. Rewrite the offending commit and force-push if it already reached
     the remote.
- **Worker contract changes** — request/response shape, new endpoints,
  removed fields, header changes. The frontend (`index.html` polling
  + report submission) and the planned ingest scripts both depend on
  the response shape. Forward the proposed `worker/index.js` diff to
  Petar before pasting into the Cloudflare editor.
- **CORS allowlist changes** (`ALLOWED_ORIGINS`). Each new origin
  widens attack surface; treat as a Petar-approval gate.
- **Cache TTL or `MAX_REPORTS` changes** (`CACHE_TTL_SECONDS = 30`,
  `MAX_REPORTS = 100`). These are coupled with the client polling
  interval (`POLL_INTERVAL_MS = 15000`); see `CLAUDE.md` § Specific
  Gotchas before touching either.
