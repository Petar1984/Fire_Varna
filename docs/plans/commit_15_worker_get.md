# Commit 15 plan: Worker GET `/issues` + KV cache

## Overview

Commit 15 adds a backend-only `GET /issues` endpoint to the live Cloudflare Worker at:

```text
https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
```

The endpoint returns recent open GitHub Issues labeled `report`, normalized into JSON for commit 16 client polling. It uses a three-layer cache:

```text
L1: module-scope memory cache
L2: Workers KV binding env.REPORTS_CACHE
L3: GitHub Issues API
```

Scope boundaries:

- No frontend changes.
- No changes to `data/hydrants.json` or `field_reports.json`.
- Existing `POST /` issue creation behavior must remain compatible.
- Worker source remains in Cloudflare dashboard; extraction to repo is commit 17.

## Pre-implementation: Petar's Cloudflare steps

1. In Cloudflare Dashboard, create KV namespace:

   ```text
   varna_hydrants_reports_cache
   ```

2. Bind it to Worker `varna-hydrants-proxy`:

   ```js
   env.REPORTS_CACHE
   ```

3. Confirm existing secret is present:

   ```js
   env.GITHUB_PAT
   ```

4. Note the current Worker deployment/version for rollback.

5. Confirm labels exist in GitHub:

   ```text
   report
   pending-review
   exists-confirmed
   missing
   wrong-location
   damaged
   new-hydrant
   ```

6. Before replacing Worker code, compare the reconstructed `POST /` handler below with the dashboard source. If the dashboard POST has extra behavior, preserve it verbatim and merge only the CORS/router/GET helpers.

## Worker code changes

Use modern module Worker syntax. This is a complete drop-in candidate based on the confirmed current behavior: hardcoded repo, `env.GITHUB_PAT`, pass-through GitHub POST status/body, and shaped GET responses.

```js
const GITHUB_OWNER = "Petar1984";
const GITHUB_REPO = "Fire_Varna";
const GITHUB_API_VERSION = "2022-11-28";

const CACHE_KEY = "issues:report:v1";
const CACHE_TTL_SECONDS = 30;
const MAX_REPORTS = 100;

const ALLOWED_ORIGINS = new Set([
  "https://petar1984.github.io",
  "http://localhost:8000",
  "http://127.0.0.1:8000",
  "http://localhost:8080",
  "http://127.0.0.1:8080"
]);

const EXPOSED_HEADERS = [
  "X-Cache-Status",
  "X-Cache-Layer",
  "X-Cached-At",
  "X-Parse-Warnings",
  "X-Cache-Warning"
].join(", ");

let memoryCache = null;
let refreshPromise = null;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return handleOptions(request);
    }

    if (request.method === "GET" && url.pathname === "/issues") {
      return handleGetIssues(request, env, ctx);
    }

    if (request.method === "POST" && url.pathname === "/") {
      return handlePostIssue(request, env);
    }

    return jsonResponse(request, { error: "not_found" }, 404, { cacheControl: "no-store" });
  }
};

function handleOptions(request) {
  const origin = request.headers.get("Origin");
  const headers = corsHeaders(request);

  if (origin && !ALLOWED_ORIGINS.has(origin)) {
    return new Response(null, { status: 403, headers });
  }

  headers.set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  headers.set(
    "Access-Control-Allow-Headers",
    request.headers.get("Access-Control-Request-Headers") || "Content-Type"
  );
  headers.set("Access-Control-Max-Age", "86400");

  return new Response(null, { status: 204, headers });
}

async function handlePostIssue(request, env) {
  if (!env.GITHUB_PAT) {
    return jsonResponse(request, { message: "Missing GITHUB_PAT" }, 401, {
      cacheControl: "no-store"
    });
  }

  const bodyText = await request.text();
  const githubUrl = `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/issues`;

  const githubResponse = await fetch(githubUrl, {
    method: "POST",
    headers: githubHeaders(env, "application/vnd.github+json"),
    body: bodyText
  });

  const responseText = await githubResponse.text();
  const headers = corsHeaders(request);
  headers.set(
    "Content-Type",
    githubResponse.headers.get("Content-Type") || "application/json; charset=utf-8"
  );

  return new Response(responseText, {
    status: githubResponse.status,
    headers
  });
}

async function handleGetIssues(request, env, ctx) {
  const query = parseIssuesQuery(request.url);
  if (query.error) {
    return jsonResponse(request, {
      error: query.error,
      retry_after_seconds: 0
    }, 400, { cacheControl: "no-store" });
  }

  try {
    return await getIssuesWithCache(request, env, ctx, query);
  } catch (err) {
    const publicError = toPublicError(err);
    return jsonResponse(request, {
      error: publicError.code,
      stale_cache: false,
      retry_after_seconds: publicError.retryAfterSeconds,
      details: publicError.details || undefined
    }, publicError.status, {
      cacheStatus: "miss",
      retryAfterSeconds: publicError.retryAfterSeconds,
      cacheControl: "no-store"
    });
  }
}

async function getIssuesWithCache(request, env, ctx, query) {
  const nowMs = Date.now();

  if (isFresh(memoryCache, nowMs)) {
    return entryResponse(request, memoryCache, query, {
      cacheStatus: "hit",
      cacheLayer: "memory",
      stale: false
    });
  }

  let staleCandidate = memoryCache || null;

  if (env.REPORTS_CACHE) {
    try {
      const kvEntry = await env.REPORTS_CACHE.get(CACHE_KEY, {
        type: "json",
        cacheTtl: CACHE_TTL_SECONDS
      });

      if (kvEntry) staleCandidate = kvEntry;

      if (isFresh(kvEntry, nowMs)) {
        memoryCache = kvEntry;
        return entryResponse(request, kvEntry, query, {
          cacheStatus: "hit",
          cacheLayer: "kv",
          stale: false
        });
      }
    } catch (err) {
      console.warn("KV read failed", err);
    }
  }

  try {
    if (!refreshPromise) {
      refreshPromise = fetchNormalizeAndCacheReports(env, ctx, staleCandidate)
        .finally(() => {
          refreshPromise = null;
        });
    }

    const freshEntry = await refreshPromise;
    memoryCache = freshEntry;

    return entryResponse(request, freshEntry, query, {
      cacheStatus: "miss",
      cacheLayer: "github",
      stale: false
    });
  } catch (err) {
    if (staleCandidate) {
      const publicError = toPublicError(err);
      return entryResponse(request, staleCandidate, query, {
        cacheStatus: "stale",
        cacheLayer: "stale",
        stale: true,
        warning: publicError.code
      });
    }

    throw err;
  }
}

async function fetchNormalizeAndCacheReports(env, ctx, previousEntry) {
  const issues = await fetchGitHubIssues(env);
  const reportIssues = issues.filter(issue => !issue.pull_request);

  const reports = [];
  let parseWarnings = 0;

  for (const issue of reportIssues) {
    const normalized = normalizeIssue(issue);
    if (normalized) {
      reports.push(normalized);
    } else {
      parseWarnings++;
    }
  }

  if (reportIssues.length > 0 && reports.length === 0) {
    throw new PublicError(
      "github_parse_failed",
      502,
      CACHE_TTL_SECONDS,
      "No parseable report frontmatter found in fetched report issues."
    );
  }

  const freshEntry = buildCacheEntry(reports, parseWarnings);
  memoryCache = freshEntry;

  if (
    env.REPORTS_CACHE &&
    (!previousEntry || previousEntry.signature !== freshEntry.signature)
  ) {
    ctx.waitUntil(
      env.REPORTS_CACHE.put(CACHE_KEY, JSON.stringify(freshEntry))
        .catch(err => console.warn("KV put failed", err))
    );
  }

  return freshEntry;
}

async function fetchGitHubIssues(env) {
  if (!env.GITHUB_PAT) {
    throw new PublicError("github_auth_failed", 503, CACHE_TTL_SECONDS);
  }

  const url = new URL(`https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/issues`);
  url.searchParams.set("state", "open");
  url.searchParams.set("labels", "report");
  url.searchParams.set("sort", "created");
  url.searchParams.set("direction", "desc");
  url.searchParams.set("per_page", String(MAX_REPORTS));

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 8000);

  let response;
  try {
    response = await fetch(url.toString(), {
      headers: githubHeaders(env, "application/vnd.github.raw+json"),
      signal: controller.signal
    });
  } catch (err) {
    throw new PublicError("github_unavailable", 503, CACHE_TTL_SECONDS);
  } finally {
    clearTimeout(timeoutId);
  }

  const text = await response.text();
  let body = null;
  try {
    body = text ? JSON.parse(text) : null;
  } catch (_) {}

  if (isGitHubRateLimited(response, body)) {
    throw new PublicError("rate_limited", 429, retryAfterSeconds(response));
  }

  if (response.status === 401 || response.status === 403) {
    throw new PublicError("github_auth_failed", 503, CACHE_TTL_SECONDS);
  }

  if (!response.ok) {
    throw new PublicError("github_unavailable", 503, CACHE_TTL_SECONDS);
  }

  if (!Array.isArray(body)) {
    throw new PublicError("github_parse_failed", 502, CACHE_TTL_SECONDS);
  }

  return body;
}

function githubHeaders(env, accept) {
  return {
    "Accept": accept,
    "Authorization": `Bearer ${env.GITHUB_PAT}`,
    "Content-Type": "application/json",
    "User-Agent": "varna-hydrants-worker",
    "X-GitHub-Api-Version": GITHUB_API_VERSION
  };
}

function normalizeIssue(issue) {
  const data = parseReportFrontmatter(issue.body || "");
  if (!data || !data.report_type) return null;

  const expectedCoord = normalizeCoord(data.expected_coord);
  const reportedCoord = normalizeCoord(data.reported_coord);
  const coords = reportedCoord || expectedCoord || null;

  const labels = (issue.labels || [])
    .map(label => typeof label === "string" ? label : label && label.name)
    .filter(Boolean);

  const details = {
    free_text: textOrNull(data.free_text),
    terrain_description: textOrNull(data.terrain_description),
    description: textOrNull(data.description),
    damage_description: textOrNull(data.damage_description),
    hydrant_type_at_location: textOrNull(data.hydrant_type_at_location),
    hydrant_type: textOrNull(data.hydrant_type),
    operational: textOrNull(data.operational)
  };

  return {
    id: textOrNull(data.report_id) || `github_issue_${issue.number}`,
    issue_number: issue.number,
    issue_url: issue.html_url,
    hydrant_id: textOrNull(data.hydrant_ref),
    report_type: data.report_type,
    coords,
    expected_coord: expectedCoord,
    reported_coord: reportedCoord,
    address: null,
    comment: firstText(
      details.damage_description,
      details.description,
      details.terrain_description,
      details.free_text
    ),
    details,
    reported_at: validTimestamp(data.timestamp) || issue.created_at || null,
    github_created_at: issue.created_at || null,
    github_updated_at: issue.updated_at || null,
    labels,
    pending_review: labels.includes("pending-review")
  };
}

function parseReportFrontmatter(body) {
  const normalized = body.replace(/\r\n/g, "\n");
  const match = normalized.match(/^---\n([\s\S]*?)\n---(?:\n|$)/);
  if (!match) return null;

  const data = {};
  for (const line of match[1].split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;

    const key = line.slice(0, idx).trim();
    const rawValue = line.slice(idx + 1).trim();
    if (!key) continue;

    data[key] = parseSimpleYamlValue(rawValue);
  }

  return data;
}

function parseSimpleYamlValue(raw) {
  if (raw === "null") return null;
  if (raw === "true") return true;
  if (raw === "false") return false;

  if (
    (raw.startsWith('"') && raw.endsWith('"')) ||
    (raw.startsWith("[") && raw.endsWith("]"))
  ) {
    try {
      return JSON.parse(raw);
    } catch (_) {
      return raw;
    }
  }

  if (/^-?\d+(\.\d+)?$/.test(raw)) return Number(raw);
  return raw;
}

function buildCacheEntry(reports, parseWarnings) {
  const cachedAt = new Date().toISOString();

  return {
    schema_version: 1,
    cached_at: cachedAt,
    ttl_seconds: CACHE_TTL_SECONDS,
    signature: buildSignature(reports),
    parse_warnings: parseWarnings,
    reports
  };
}

function buildSignature(reports) {
  return reports
    .map(report => `${report.issue_number}:${report.github_updated_at || report.reported_at || ""}`)
    .join("|");
}

function parseIssuesQuery(rawUrl) {
  const url = new URL(rawUrl);
  const limitRaw = url.searchParams.get("limit");
  const sinceRaw = url.searchParams.get("since");

  let limit = MAX_REPORTS;
  if (limitRaw != null) {
    if (!/^\d+$/.test(limitRaw)) return { error: "invalid_limit" };
    limit = Number(limitRaw);
    if (limit < 1 || limit > MAX_REPORTS) return { error: "invalid_limit" };
  }

  let sinceMs = null;
  if (sinceRaw != null) {
    sinceMs = Date.parse(sinceRaw);
    if (Number.isNaN(sinceMs)) return { error: "invalid_since" };
  }

  return { limit, sinceMs };
}

function entryResponse(request, entry, query, options) {
  let reports = entry.reports || [];

  if (query.sinceMs != null) {
    reports = reports.filter(report => {
      const reportedAtMs = Date.parse(report.reported_at || report.github_created_at || "");
      return !Number.isNaN(reportedAtMs) && reportedAtMs > query.sinceMs;
    });
  }

  reports = reports.slice(0, query.limit);

  return jsonResponse(request, {
    reports,
    cached_at: entry.cached_at,
    ttl_seconds: CACHE_TTL_SECONDS,
    stale: !!options.stale
  }, 200, {
    cacheStatus: options.cacheStatus,
    cacheLayer: options.cacheLayer,
    cachedAt: entry.cached_at,
    parseWarnings: entry.parse_warnings || 0,
    warning: options.warning
  });
}

function jsonResponse(request, body, status, options = {}) {
  const headers = corsHeaders(request);
  headers.set("Content-Type", "application/json; charset=utf-8");
  headers.set(
    "Cache-Control",
    options.cacheControl || (status === 200 ? `public, max-age=${CACHE_TTL_SECONDS}` : "no-store")
  );

  if (options.cacheStatus) headers.set("X-Cache-Status", options.cacheStatus);
  if (options.cacheLayer) headers.set("X-Cache-Layer", options.cacheLayer);
  if (options.cachedAt) headers.set("X-Cached-At", options.cachedAt);
  if (options.parseWarnings != null) headers.set("X-Parse-Warnings", String(options.parseWarnings));

  if (options.warning) {
    headers.set("X-Cache-Warning", options.warning);
    headers.set("Warning", `110 - "${options.warning}"`);
  }

  if (options.retryAfterSeconds) {
    headers.set("Retry-After", String(options.retryAfterSeconds));
  }

  return new Response(JSON.stringify(body), { status, headers });
}

function corsHeaders(request) {
  const headers = new Headers();
  const origin = request.headers.get("Origin");

  headers.set("Vary", "Origin");
  headers.set("Access-Control-Expose-Headers", EXPOSED_HEADERS);

  if (origin && ALLOWED_ORIGINS.has(origin)) {
    headers.set("Access-Control-Allow-Origin", origin);
  }

  return headers;
}

function isFresh(entry, nowMs = Date.now()) {
  if (!entry || !entry.cached_at) return false;
  const cachedAtMs = Date.parse(entry.cached_at);
  if (Number.isNaN(cachedAtMs)) return false;
  return nowMs - cachedAtMs < CACHE_TTL_SECONDS * 1000;
}

function normalizeCoord(value) {
  if (!Array.isArray(value) || value.length !== 2) return null;

  const lon = Number(value[0]);
  const lat = Number(value[1]);

  if (!Number.isFinite(lon) || !Number.isFinite(lat)) return null;
  return [lon, lat];
}

function textOrNull(value) {
  if (typeof value !== "string") return null;
  const trimmed = value.trim();
  return trimmed ? trimmed : null;
}

function firstText(...values) {
  return values.find(value => typeof value === "string" && value.trim()) || null;
}

function validTimestamp(value) {
  if (typeof value !== "string") return null;
  return Number.isNaN(Date.parse(value)) ? null : value;
}

function isGitHubRateLimited(response, body) {
  if (response.status === 429) return true;
  if (response.headers.get("retry-after")) return true;
  if (response.headers.get("x-ratelimit-remaining") === "0") return true;

  const message = body && typeof body.message === "string" ? body.message : "";
  return response.status === 403 && /rate limit|secondary rate/i.test(message);
}

function retryAfterSeconds(response) {
  const retryAfter = Number(response.headers.get("retry-after"));
  if (Number.isFinite(retryAfter) && retryAfter > 0) return Math.ceil(retryAfter);

  const reset = Number(response.headers.get("x-ratelimit-reset"));
  if (Number.isFinite(reset) && reset > 0) {
    return Math.max(1, reset - Math.floor(Date.now() / 1000));
  }

  return 60;
}

class PublicError extends Error {
  constructor(code, status = 503, retryAfterSeconds = CACHE_TTL_SECONDS, details = null) {
    super(code);
    this.code = code;
    this.status = status;
    this.retryAfterSeconds = retryAfterSeconds;
    this.details = details;
  }
}

function toPublicError(err) {
  if (err instanceof PublicError) return err;
  return new PublicError("github_unavailable", 503, CACHE_TTL_SECONDS);
}
```

## GET `/issues` contract

### Request

```text
GET /issues
GET /issues?limit=20
GET /issues?since=2026-05-06T09:00:00Z
GET /issues?since=2026-05-06T09:00:00Z&limit=20
```

Query behavior:

- No query params returns the latest cached open report issues, up to 100.
- `limit` is applied after cache read; default `100`, max `100`.
- `since` returns reports whose `reported_at` is newer than the ISO timestamp.
- Query params do not change the KV key and do not trigger separate GitHub fetches.
- Invalid `since` returns `400 invalid_since`.
- Invalid `limit` returns `400 invalid_limit`.

### Success headers

```http
Content-Type: application/json; charset=utf-8
Cache-Control: public, max-age=30
Vary: Origin
Access-Control-Allow-Origin: <allowed origin echo>
Access-Control-Expose-Headers: X-Cache-Status, X-Cache-Layer, X-Cached-At, X-Parse-Warnings, X-Cache-Warning
X-Cache-Status: hit | miss | stale
X-Cache-Layer: memory | kv | github | stale
X-Cached-At: <ISO timestamp>
X-Parse-Warnings: <number>
```

CORS allowlist:

```text
https://petar1984.github.io
http://localhost:8000
http://127.0.0.1:8000
http://localhost:8080
http://127.0.0.1:8080
```

The port `8000` origins are intentionally added because repo docs and local verification use `python -m http.server 8000`.

### Success body

```json
{
  "reports": [
    {
      "id": "report uuid or github_issue_123",
      "issue_number": 123,
      "issue_url": "https://github.com/Petar1984/Fire_Varna/issues/123",
      "hydrant_id": "VIK-12345",
      "report_type": "exists_confirmed",
      "coords": [27.847417, 43.250208],
      "expected_coord": [27.847417, 43.250208],
      "reported_coord": null,
      "address": null,
      "comment": "string or null",
      "details": {
        "free_text": null,
        "terrain_description": null,
        "description": null,
        "damage_description": null,
        "hydrant_type_at_location": null,
        "hydrant_type": null,
        "operational": null
      },
      "reported_at": "2026-05-06T09:15:00+03:00",
      "github_created_at": "2026-05-06T06:15:02Z",
      "github_updated_at": "2026-05-06T06:15:02Z",
      "labels": ["report", "exists-confirmed", "pending-review"],
      "pending_review": true
    }
  ],
  "cached_at": "2026-05-06T09:15:30.000Z",
  "ttl_seconds": 30,
  "stale": false
}
```

Field rules:

- `report_type` uses existing frontend values: `exists_confirmed`, `missing`, `wrong_location`, `damaged`, `new_hydrant`.
- `coords` is `reported_coord` when present, otherwise `expected_coord`.
- `address` is always `null` in commit 15 because current issue bodies do not include address and the Worker does not load the hydrant dataset.
- `comment` is the first non-empty value from `damage_description`, `description`, `terrain_description`, `free_text`.
- `reporter` is intentionally omitted from the public GET response.

### Error bodies

Invalid query:

```json
{ "error": "invalid_since", "retry_after_seconds": 0 }
```

```json
{ "error": "invalid_limit", "retry_after_seconds": 0 }
```

GitHub unavailable with no stale cache:

```json
{
  "error": "github_unavailable",
  "stale_cache": false,
  "retry_after_seconds": 30
}
```

Rate limited with no stale cache:

```json
{
  "error": "rate_limited",
  "retry_after_seconds": 60
}
```

Parse failed with no stale cache:

```json
{
  "error": "github_parse_failed",
  "details": "No parseable report frontmatter found in fetched report issues.",
  "retry_after_seconds": 30
}
```

When stale cache exists, return `200` with normal success body and:

```http
X-Cache-Status: stale
X-Cache-Layer: stale
X-Cache-Warning: github_unavailable | rate_limited | github_auth_failed | github_parse_failed
Warning: 110 - "<reason>"
```

## Cache behavior

Cache key:

```text
issues:report:v1
```

Cache flow:

```text
GET /issues
  -> Check L1 memory cache
  -> If fresh, return hit/memory
  -> Read L2 KV with cacheTtl=30
  -> If fresh, hydrate L1 and return hit/kv
  -> Keep stale L1/L2 candidate if present
  -> Fetch L3 GitHub Issues API
  -> Filter out pull_request items
  -> Parse YAML frontmatter
  -> Normalize reports
  -> Hydrate L1
  -> Write KV only if missing or signature changed
  -> Return miss/github
  -> On GitHub failure with stale candidate, return 200 stale
  -> On GitHub failure without stale candidate, return structured error
```

GitHub endpoint:

```text
GET https://api.github.com/repos/Petar1984/Fire_Varna/issues?state=open&labels=report&sort=created&direction=desc&per_page=100
```

Rate math:

```text
30s TTL => max 120 GitHub fetches/hour per cache key
GitHub authenticated REST limit => 5000/hour
120 / 5000 = 2.4%
```

KV write protection:

```text
Literal write every 30s all day = 2880 writes/day
Cloudflare KV Free = 1000 writes/day
```

Therefore, write KV only when the normalized report signature changes or when no KV entry exists.

## Testing plan

1. Before deploy, save/record current Worker version in Cloudflare dashboard.

2. Deploy the Worker code with `REPORTS_CACHE` binding and `GITHUB_PAT`.

3. Smoke test GET:

   ```powershell
   curl.exe -i https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
   ```

   Expect `200`, JSON body, `reports`, `cached_at`, `ttl_seconds`.

4. Test GitHub Pages CORS:

   ```powershell
   curl.exe -i -H "Origin: https://petar1984.github.io" https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
   ```

   Expect `Access-Control-Allow-Origin: https://petar1984.github.io`.

5. Test local CORS ports:

   ```powershell
   curl.exe -i -H "Origin: http://localhost:8000" https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
   curl.exe -i -H "Origin: http://127.0.0.1:8000" https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
   curl.exe -i -H "Origin: http://localhost:8080" https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
   curl.exe -i -H "Origin: http://127.0.0.1:8080" https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues
   ```

6. Verify exposed headers are present:

   ```text
   Access-Control-Expose-Headers
   X-Cache-Status
   X-Cache-Layer
   X-Cached-At
   X-Parse-Warnings
   ```

7. Verify cache behavior:
   - First request after deploy/TTL should be `X-Cache-Status: miss`.
   - Immediate second request should be `hit` from `memory` or `kv`.
   - After 30 seconds, a request may be `miss` and refresh from GitHub.

8. Test query params:

   ```powershell
   curl.exe -i "https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues?limit=1"
   curl.exe -i "https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues?since=2026-05-06T00:00:00Z"
   curl.exe -i "https://varna-hydrants-proxy.petar-dikov2019.workers.dev/issues?limit=999"
   ```

   Expect `limit=999` to return `400 invalid_limit`.

9. Submit a normal frontend report via existing POST flow:
   - Verify POST still returns `201` and JSON containing `number`.
   - Verify report appears in `GET /issues` within 30 seconds.

10. Submit or inspect a report with multi-line `free_text` or another multi-line volunteer text field:
    - Verify the YAML frontmatter still parses correctly.
    - The current parser should handle frontend-generated JSON-quoted strings with escaped `\n`.
    - If testing shows real embedded newline parsing fails, enhance `parseReportFrontmatter` before production deploy.

11. Temporarily test invalid `GITHUB_PAT` only after a good cache exists:
    - Change secret to invalid value.
    - Request `/issues`.
    - Expect `200` stale response if cache exists, or structured `503/429` if not.
    - Restore `GITHUB_PAT` immediately.

12. Confirm Cloudflare logs have no uncaught exceptions or raw 500s.

## Rollback plan

Cloudflare rollback:

1. Open Worker `varna-hydrants-proxy` in Cloudflare dashboard.
2. Go to Deployments / Versions.
3. Roll back to the version recorded before commit 15.
4. Re-test existing POST report submission from the live frontend.
5. Keep the KV namespace; it is harmless if unused.

Git rollback for the plan document, if later committed incorrectly:

```powershell
cd C:\Projects\Varna_hydrants
git status
git reset --hard dffc634
```

Only use `git clean -fd` if an execution session created unwanted untracked files and Petar explicitly approves. Do not force-push without explicit approval.

## Resolved notes and assumptions

- Rollback anchor for commit 15 is `dffc6346d490d8b8d5ccd401d7a60776a81b8999`, the current HEAD before this plan commit.
- The `2535920` hash in `docs/activeContext.md` is not a conflicting rollback anchor. It is an audit-trail reference to the stable doc-sync state before new sprint work.
- The exact dashboard Worker POST source is not in the repo. The code above reconstructs the confirmed pass-through behavior. If dashboard POST has extra hardening, preserve it verbatim and merge the GET code around it.
- Existing Worker CORS allowlist is expanded in this plan to include port `8000` because repo docs use `python -m http.server 8000`.

## Implementation handoff to Claude Code

Claude Code should execute from this plan only after Petar approval in a fresh execution-capable session.

For Worker deployment, Petar will paste/update code in the Cloudflare dashboard. No frontend, dataset, or repo Worker-source extraction is part of commit 15. Worker source extraction remains commit 17.

For the planning repo commit, create only:

```text
docs/plans/commit_15_worker_get.md
```

Do not modify files outside `docs/plans/`.
