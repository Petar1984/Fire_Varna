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

// ===========================================================================
// E2 — Safe building-tile gateway (/tiles/*). Isolated, anti-scrape serving of
// the E1 "safe_min" PMTiles from R2 via per-tile ranged reads. Wired into
// fetch() BEFORE the existing routes; the OPTIONS / GET /issues / POST /
// handlers below are unchanged. Production deploy stays dashboard-paste of this
// single file (see README.md) — so the PMTiles reader is hand-rolled inline
// with no imports/bundler. The HMAC secret comes from env only
// (TILES_HMAC_SECRET); no token literal ever appears in source.
// ===========================================================================

const TILE_SCOPE = "buildings:v1";
const TILE_PATH_RE = /^\/tiles\/buildings\/v1\/(\d+)\/(\d+)\/(\d+)\.mvt$/;

// Exact served-tile headers mandated by the E2 plan / ADR, kept as literals so
// the bytes can never drift from the contract.
const TILE_CONTENT_TYPE = "application/vnd.mapbox-vector-tile";
const TILE_CACHE_CONTROL = "public, max-age=86400, s-maxage=604800, immutable";

// Varna x/y bounds for the pre-R2 anti-scrape gate. Derived from the E1
// safe_min archive's own data extent (probe 2026-06-22: z15 x[18917..18937]
// y[12002..12026]) plus a 2-tile margin, scaled by 2^(z-15). This rejects
// world-wide probing cheaply before any R2 read; an in-box tile that simply has
// no buildings still resolves to 404 via the directory gap.
const VARNA_BASE_Z = 15;
const VARNA_X_MIN = 18915;
const VARNA_X_MAX = 18939;
const VARNA_Y_MIN = 12000;
const VARNA_Y_MAX = 12028;

// Best-effort, per-isolate IP rate limiter. NOT authoritative — a Worker isolate
// is one of many and is recycled, so the Cloudflare dashboard rate-limit / bot
// rules are the production source of truth (documented in README + runbook).
const tileRateBuckets = new Map();

// Per-isolate cache of the parsed PMTiles header + root directory (small, stable
// per object key) so a warm isolate ranged-reads only the tile body.
let tileArchiveCache = { key: null, header: null, rootEntries: null };

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // ===== E2 building-tile gateway — isolated, BEFORE the existing routes. =====
    // These three checks are scoped to /tiles/* only, so OPTIONS / GET /issues /
    // POST / fall through to the unchanged handlers below.
    if (request.method === "OPTIONS" && url.pathname.startsWith("/tiles/")) {
      return handleTilesOptions(request);
    }
    if (request.method === "GET" && url.pathname === "/tiles/buildings/token") {
      return handleTileToken(request, env);
    }
    if (request.method === "GET" && TILE_PATH_RE.test(url.pathname)) {
      return handleBuildingTile(request, env, ctx, url);
    }
    // ===== end E2 block =====

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
    return jsonResponse(request, { error: "PAT not configured" }, 500, {
      cacheControl: "no-store"
    });
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse(request, { error: "Invalid JSON" }, 400, {
      cacheControl: "no-store"
    });
  }

  if (!body.title || !body.body) {
    return jsonResponse(request, { error: "Missing title or body" }, 400, {
      cacheControl: "no-store"
    });
  }

  const githubUrl = `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/issues`;

  const githubResponse = await fetch(githubUrl, {
    method: "POST",
    headers: githubHeaders(env, "application/vnd.github+json"),
    body: JSON.stringify({
      title: body.title,
      body: body.body,
      labels: body.labels || []
    })
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
    type: canonicalHydrantType(data),
    operational_status: canonicalOperationalStatus(data),
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

function canonicalHydrantType(data) {
  // Prefer the canonical YAML key (`type`); fall back to the legacy key
  // (`hydrant_type`) for issues created before the contract update.
  // Unknown values and the "не знам" opt-out collapse to null so that
  // downstream record updates only see authoritative values.
  const fromCanonical = textOrNull(data.type);
  if (fromCanonical) {
    if (fromCanonical === "надземен" || fromCanonical === "подземен") return fromCanonical;
    return null;
  }

  const fromLegacy = textOrNull(data.hydrant_type);
  if (fromLegacy === "надземен" || fromLegacy === "подземен") return fromLegacy;
  return null;
}

function canonicalOperationalStatus(data) {
  // Prefer the canonical YAML key (`operational_status`, English vocabulary
  // matching the hydrant-record schema); fall back to the legacy key
  // (`operational`, Bulgarian picker value) for old issues. The legacy
  // ", само видимо" suffix is the pre-amendment damaged-modal variant.
  const fromCanonical = textOrNull(data.operational_status);
  if (fromCanonical) {
    if (fromCanonical === "works" || fromCanonical === "not_working" || fromCanonical === "not_tested") {
      return fromCanonical;
    }
    return null;
  }

  const fromLegacy = textOrNull(data.operational);
  if (!fromLegacy) return null;
  if (fromLegacy === "да") return "works";
  if (fromLegacy === "не") return "not_working";
  if (fromLegacy === "не съм проверявал") return "not_tested";
  if (fromLegacy === "не съм проверявал, само видимо") return "not_tested";
  return null;
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

// ===========================================================================
// E2 — building-tile gateway helpers. Everything below is additive; none of the
// functions above are referenced or modified by this block (it only reuses the
// existing ALLOWED_ORIGINS allowlist).
// ===========================================================================

// --- request gating -------------------------------------------------------

// CORS preflight for any /tiles/* route, gated by the same origin allowlist.
function handleTilesOptions(request) {
  const origin = effectiveAllowedOrigin(request);
  const headers = new Headers();
  headers.set("Vary", "Origin");
  if (!origin) return new Response(null, { status: 403, headers });
  headers.set("Access-Control-Allow-Origin", origin);
  headers.set("Access-Control-Allow-Methods", "GET, OPTIONS");
  headers.set(
    "Access-Control-Allow-Headers",
    request.headers.get("Access-Control-Request-Headers") || "Content-Type"
  );
  headers.set("Access-Control-Max-Age", "86400");
  return new Response(null, { status: 204, headers });
}

// The allowed origin for this request, or null. A present-but-disallowed Origin
// is rejected outright; only when Origin is absent do we fall back to the
// Referer's origin (covers same-site navigations that omit Origin).
function effectiveAllowedOrigin(request) {
  const origin = request.headers.get("Origin");
  if (origin) return ALLOWED_ORIGINS.has(origin) ? origin : null;
  const referer = request.headers.get("Referer");
  if (referer) {
    try {
      const refererOrigin = new URL(referer).origin;
      if (ALLOWED_ORIGINS.has(refererOrigin)) return refererOrigin;
    } catch (_) {}
  }
  return null;
}

function clientIp(request) {
  const cf = request.headers.get("CF-Connecting-IP");
  if (cf) return cf;
  const forwarded = request.headers.get("X-Forwarded-For");
  if (forwarded) return forwarded.split(",")[0].trim();
  return "0.0.0.0";
}

function tileEnvInt(env, name, fallback) {
  const raw = env && env[name];
  if (raw == null) return fallback;
  const parsed = parseInt(raw, 10);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function tileObjectKey(env) {
  return env && env.BUILDING_TILES_OBJECT_KEY;
}

// Best-effort per-isolate fixed-window limiter. Returns {ok} or {ok:false,retryAfter}.
function tileRateLimit(kind, ip, env) {
  const now = Date.now();
  const windowMs = tileEnvInt(env, "TILES_RATE_WINDOW_S", 60) * 1000;
  const max = kind === "token"
    ? tileEnvInt(env, "TILES_TOKEN_RATE_MAX", 30)
    : tileEnvInt(env, "TILES_TILE_RATE_MAX", 600);
  const mapKey = kind + ":" + ip;
  let bucket = tileRateBuckets.get(mapKey);
  if (!bucket || now - bucket.start >= windowMs) {
    bucket = { start: now, count: 0 };
    tileRateBuckets.set(mapKey, bucket);
  }
  bucket.count++;
  if (tileRateBuckets.size > 5000) {
    for (const [key, value] of tileRateBuckets) {
      if (now - value.start >= windowMs) tileRateBuckets.delete(key);
    }
    // Hard ceiling: under a single-window flood of distinct IPs none of the
    // above are evictable, so bound memory by dropping everything. Best-effort
    // only — the CF dashboard limiter is authoritative.
    if (tileRateBuckets.size > 20000) tileRateBuckets.clear();
  }
  if (bucket.count > max) {
    return { ok: false, retryAfter: Math.max(1, Math.ceil((bucket.start + windowMs - now) / 1000)) };
  }
  return { ok: true };
}

// --- token endpoint -------------------------------------------------------

async function handleTileToken(request, env) {
  const origin = effectiveAllowedOrigin(request);
  if (!origin) return tilesError(null, 403, "origin_not_allowed");

  const limit = tileRateLimit("token", clientIp(request), env);
  if (!limit.ok) return tilesError(origin, 429, "rate_limited", limit.retryAfter);

  if (!env.TILES_HMAC_SECRET) return tilesError(origin, 500, "secret_not_configured");

  const ttl = tileEnvInt(env, "TILES_TOKEN_TTL_S", 600);
  const iat = Math.floor(Date.now() / 1000);
  const exp = iat + ttl;
  const token = await signTileToken(env, { v: 1, scope: TILE_SCOPE, origin, iat, exp });

  const headers = new Headers();
  headers.set("Content-Type", "application/json; charset=utf-8");
  headers.set("Cache-Control", "no-store");
  headers.set("Access-Control-Allow-Origin", origin);
  headers.set("Vary", "Origin");
  return new Response(JSON.stringify({ token, scope: TILE_SCOPE, exp }), { status: 200, headers });
}

// --- tile endpoint --------------------------------------------------------

async function handleBuildingTile(request, env, ctx, url) {
  // Validation order is fixed by the plan: origin -> rate-limit -> token ->
  // z/x/y bounds, ALL before any cache or R2 access.
  const origin = effectiveAllowedOrigin(request);
  if (!origin) return tilesError(null, 403, "origin_not_allowed");

  const limit = tileRateLimit("tile", clientIp(request), env);
  if (!limit.ok) return tilesError(origin, 429, "rate_limited", limit.retryAfter);

  const verdict = await verifyTileToken(env, url.searchParams.get("token"));
  if (!verdict.ok) return tilesError(origin, 401, "invalid_token");
  const payload = verdict.payload;
  if (payload.v !== 1 || payload.scope !== TILE_SCOPE) return tilesError(origin, 401, "invalid_scope");
  if (payload.origin !== origin) return tilesError(origin, 401, "origin_mismatch");
  if (typeof payload.exp !== "number" || Math.floor(Date.now() / 1000) > payload.exp) {
    return tilesError(origin, 401, "token_expired");
  }

  const match = url.pathname.match(TILE_PATH_RE);
  const z = Number(match[1]);
  const x = Number(match[2]);
  const y = Number(match[3]);
  const minZ = tileEnvInt(env, "TILES_MIN_Z", 15);
  const maxZ = tileEnvInt(env, "TILES_MAX_Z", 17);
  if (z < minZ || z > maxZ) return tilesError(origin, 404, "zoom_out_of_range");
  const dimension = Math.pow(2, z);
  if (x < 0 || y < 0 || x >= dimension || y >= dimension) return tilesError(origin, 404, "xy_out_of_range");
  const bounds = varnaBoundsAtZoom(z);
  if (x < bounds.xMin || x > bounds.xMax || y < bounds.yMin || y > bounds.yMax) {
    return tilesError(origin, 404, "xy_out_of_range");
  }

  if (!tileObjectKey(env) || !env.BUILDING_TILES) return tilesError(origin, 500, "tiles_not_configured");

  // Worker Cache API — key is pathname only (excludes the token query + origin),
  // so one cached tile serves every allowed origin / token. Per-request CORS is
  // layered on at send time and never stored in the cache.
  const cache = caches.default;
  const cacheKey = new Request(url.origin + url.pathname);
  const cached = await cache.match(cacheKey);
  if (cached) {
    return tileResponse(new Uint8Array(await cached.arrayBuffer()), origin, "HIT");
  }

  let archive;
  try {
    archive = await getArchive(env);
  } catch (_) {
    return tilesError(origin, 503, "tiles_unavailable");
  }

  let entry;
  try {
    // Wrapped defensively: with leaf directories this reads + decodes from R2.
    entry = await lookupTile(env, archive, zxyToTileId(z, x, y));
  } catch (_) {
    return tilesError(origin, 503, "tiles_unavailable");
  }
  if (!entry) return tilesError(origin, 404, "not_found");

  let tileBytes;
  try {
    const compressed = await r2Range(env, archive.header.tileDataOffset + entry.offset, entry.length);
    if (!compressed) return tilesError(origin, 404, "not_found");
    tileBytes = await gunzipMaybe(compressed, archive.header.tileCompression);
  } catch (_) {
    return tilesError(origin, 503, "tiles_unavailable");
  }

  ctx.waitUntil(cache.put(cacheKey, new Response(tileBytes, { headers: tileContentHeaders() })));
  return tileResponse(tileBytes, origin, "MISS");
}

function varnaBoundsAtZoom(z) {
  const scale = Math.pow(2, z - VARNA_BASE_Z);
  return {
    xMin: VARNA_X_MIN * scale,
    xMax: VARNA_X_MAX * scale + (scale - 1),
    yMin: VARNA_Y_MIN * scale,
    yMax: VARNA_Y_MAX * scale + (scale - 1),
  };
}

function tileContentHeaders() {
  const headers = new Headers();
  headers.set("Content-Type", TILE_CONTENT_TYPE);
  headers.set("Cache-Control", TILE_CACHE_CONTROL);
  headers.set("X-Robots-Tag", "noindex");
  return headers;
}

function tileResponse(bytes, origin, cacheStatus) {
  const headers = tileContentHeaders();
  headers.set("Access-Control-Allow-Origin", origin);
  headers.set("Vary", "Origin");
  headers.set("X-Cache", cacheStatus);
  return new Response(bytes, { status: 200, headers });
}

function tilesError(origin, status, code, retryAfter) {
  const headers = new Headers();
  headers.set("Content-Type", "application/json; charset=utf-8");
  headers.set("Cache-Control", "no-store");
  headers.set("X-Robots-Tag", "noindex");
  if (origin) {
    headers.set("Access-Control-Allow-Origin", origin);
    headers.set("Vary", "Origin");
  }
  if (retryAfter) headers.set("Retry-After", String(retryAfter));
  return new Response(JSON.stringify({ error: code }), { status, headers });
}

// --- HMAC token (compact base64url(payload).base64url(hmac-sha256)) ---------

function tileHmacKey(env) {
  return crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(env.TILES_HMAC_SECRET),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign", "verify"]
  );
}

async function signTileToken(env, payload) {
  const body = base64urlEncode(new TextEncoder().encode(JSON.stringify(payload)));
  const key = await tileHmacKey(env);
  const signature = new Uint8Array(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(body)));
  return body + "." + base64urlEncode(signature);
}

async function verifyTileToken(env, token) {
  if (!env.TILES_HMAC_SECRET || typeof token !== "string") return { ok: false };
  const dot = token.indexOf(".");
  if (dot <= 0 || dot === token.length - 1) return { ok: false };
  const body = token.slice(0, dot);
  const signature = token.slice(dot + 1);

  let signatureBytes;
  let payload;
  try {
    signatureBytes = base64urlDecode(signature);
    payload = JSON.parse(new TextDecoder().decode(base64urlDecode(body)));
  } catch (_) {
    return { ok: false };
  }

  const key = await tileHmacKey(env);
  let valid;
  try {
    // crypto.subtle.verify is a constant-time comparison.
    valid = await crypto.subtle.verify("HMAC", key, signatureBytes, new TextEncoder().encode(body));
  } catch (_) {
    return { ok: false };
  }
  if (!valid) return { ok: false };
  return { ok: true, payload };
}

function base64urlEncode(bytes) {
  let binary = "";
  for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function base64urlDecode(value) {
  const normalized = value.replace(/-/g, "+").replace(/_/g, "/");
  const padded = normalized + "=".repeat((4 - (normalized.length % 4)) % 4);
  const binary = atob(padded);
  const out = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) out[i] = binary.charCodeAt(i);
  return out;
}

// --- PMTiles v3 reader (no dependencies; ranged reads only) -----------------
// Validated against the E1 safe_min archive (probe 2026-06-22): gzip internal +
// tile compression, single root directory (no leaves), MVT tile type.

async function r2Range(env, offset, length) {
  const object = await env.BUILDING_TILES.get(tileObjectKey(env), { range: { offset, length } });
  if (!object) return null;
  return new Uint8Array(await object.arrayBuffer());
}

async function gunzipMaybe(bytes, compression) {
  if (compression === 1) return bytes;          // none
  if (compression === 2) {                      // gzip
    const stream = new Response(bytes).body.pipeThrough(new DecompressionStream("gzip"));
    return new Uint8Array(await new Response(stream).arrayBuffer());
  }
  throw new Error("unsupported_compression:" + compression);
}

function parsePmtilesHeader(bytes) {
  let magic = "";
  for (let i = 0; i < 7; i++) magic += String.fromCharCode(bytes[i]);
  if (magic !== "PMTiles" || bytes[7] !== 3) throw new Error("bad_pmtiles_header");
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  // DataView has no native uint64; compose two uint32 with a multiply (never a
  // shift) so offsets past 2^32 (z17 tile data) stay exact.
  const u64 = (offset) => view.getUint32(offset, true) + view.getUint32(offset + 4, true) * 4294967296;
  return {
    rootDirOffset: u64(8),
    rootDirLength: u64(16),
    leafDirOffset: u64(40),
    leafDirLength: u64(48),
    tileDataOffset: u64(56),
    tileDataLength: u64(64),
    internalCompression: bytes[97],
    tileCompression: bytes[98],
    tileType: bytes[99],
    minZoom: bytes[100],
    maxZoom: bytes[101],
  };
}

// 53-bit-safe unsigned varint: accumulates with multiplication, not <<, so
// tile ids above 2^32 (which occur from z17) decode exactly.
function readPmtilesVarint(bytes, pos) {
  let result = 0;
  let shift = 0;
  for (;;) {
    if (pos.i >= bytes.length) throw new Error("varint_overrun"); // truncated/corrupt dir
    const byte = bytes[pos.i++];
    result += (byte & 0x7f) * Math.pow(2, shift);
    if ((byte & 0x80) === 0) break;
    shift += 7;
  }
  return result;
}

function deserializeDirectory(bytes) {
  const pos = { i: 0 };
  const numEntries = readPmtilesVarint(bytes, pos);
  const entries = new Array(numEntries);
  let lastId = 0;
  for (let i = 0; i < numEntries; i++) {
    lastId += readPmtilesVarint(bytes, pos);
    entries[i] = { tileId: lastId, offset: 0, length: 0, runLength: 0 };
  }
  for (let i = 0; i < numEntries; i++) entries[i].runLength = readPmtilesVarint(bytes, pos);
  for (let i = 0; i < numEntries; i++) entries[i].length = readPmtilesVarint(bytes, pos);
  for (let i = 0; i < numEntries; i++) {
    const value = readPmtilesVarint(bytes, pos);
    // Offset encoding: 0 => contiguous with previous (prev.offset+prev.length);
    // otherwise the stored value is realOffset + 1.
    if (value === 0 && i > 0) entries[i].offset = entries[i - 1].offset + entries[i - 1].length;
    else entries[i].offset = value - 1;
  }
  return entries;
}

function findTileEntry(entries, tileId) {
  let low = 0;
  let high = entries.length - 1;
  let floor = -1;
  while (low <= high) {
    const mid = (low + high) >> 1;
    if (entries[mid].tileId <= tileId) { floor = mid; low = mid + 1; }
    else high = mid - 1;
  }
  if (floor === -1) return null;
  const entry = entries[floor];
  if (entry.runLength === 0) return entry;                 // leaf directory pointer
  if (tileId - entry.tileId < entry.runLength) return entry; // inside a tile run
  return null;                                             // gap -> not found
}

// ZXY -> Hilbert tile id. Base term is (4^z - 1)/3 accumulated as a float so it
// stays exact; all bitwise ops act on values < 2^17 (z <= 17).
function zxyToTileId(z, x, y) {
  let acc = 0;
  for (let t = 0; t < z; t++) acc += Math.pow(4, t);
  const n = 1 << z;
  let d = 0;
  let xx = x;
  let yy = y;
  for (let s = n >> 1; s > 0; s = s >> 1) {
    const rx = (xx & s) > 0 ? 1 : 0;
    const ry = (yy & s) > 0 ? 1 : 0;
    d += s * s * ((3 * rx) ^ ry);
    if (ry === 0) {
      if (rx === 1) { xx = s - 1 - xx; yy = s - 1 - yy; }
      const swap = xx; xx = yy; yy = swap;
    }
  }
  return acc + d;
}

async function getArchive(env) {
  const key = tileObjectKey(env);
  if (tileArchiveCache.key === key && tileArchiveCache.header) return tileArchiveCache;
  const headerBytes = await r2Range(env, 0, 127);
  if (!headerBytes) throw new Error("pmtiles_object_missing");
  const header = parsePmtilesHeader(headerBytes);
  const rootCompressed = await r2Range(env, header.rootDirOffset, header.rootDirLength);
  const rootEntries = deserializeDirectory(await gunzipMaybe(rootCompressed, header.internalCompression));
  tileArchiveCache = { key, header, rootEntries };
  return tileArchiveCache;
}

async function lookupTile(env, archive, tileId) {
  let entries = archive.rootEntries;
  // At most a handful of leaf levels; the spec discourages more than one.
  for (let depth = 0; depth < 4; depth++) {
    const entry = findTileEntry(entries, tileId);
    if (!entry) return null;
    if (entry.runLength !== 0) return entry;               // tile entry
    const compressed = await r2Range(env, archive.header.leafDirOffset + entry.offset, entry.length);
    entries = deserializeDirectory(await gunzipMaybe(compressed, archive.header.internalCompression));
  }
  return null;
}
