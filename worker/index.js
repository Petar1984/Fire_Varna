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
