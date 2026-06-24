// Local test harness for the Varna hydrants Worker — dependency-free.
//
// Runs the REAL worker/index.js fetch handler against mocked bindings:
//   * R2 (BUILDING_TILES) seeded with the actual E1 safe_min PMTiles, with a
//     ranged-get read counter so we can prove "2nd request avoids R2".
//   * KV (REPORTS_CACHE) + a stubbed global fetch for the GitHub-backed routes.
//   * A Worker Cache API shim (caches.default) keyed by request URL.
//
// No deploy, no live R2, no network. Each test loads a FRESH module instance
// (cache-busting import query) so module-level state (rate-limit map, archive
// cache, issues memory cache) is isolated per test.
//
// Run: node test/run_tests.mjs   (from worker/)  — or `npm test`.

import { readFileSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, resolve } from "node:path";

const HERE = dirname(fileURLToPath(import.meta.url));
const INDEX_URL = pathToFileURL(resolve(HERE, "..", "index.js")).href;
const PMTILES = resolve(
  HERE, "..", "..", "..",
  "Varna_buildings", "output", "building_tiles", "safe_min",
  "varna_buildings_safe_min_z15_z17.pmtiles"
);

const OBJECT_KEY = "tiles/buildings_safe_vf1f92e297a9beacc0c3b46ae10032a0afd86f1a6b3e441e772eee7aeb9daffa1.pmtiles";
const SECRET = "test-hmac-secret-not-a-real-one";
const ORIGIN = "https://petar1984.github.io";
const ORIGIN2 = "http://localhost:8000";        // also allowlisted
const BAD_ORIGIN = "https://evil.example";
const WORKER_BASE = "https://worker.example";
const ALLOWED_KEYS = new Set(["bt", "en", "fl", "fl_min", "fl_max", "u", "bd"]);

// Known-present tiles (from the PMTiles probe, 2026-06-22).
const T15 = "/tiles/buildings/v1/15/18926/12026.mvt";
const T16 = "/tiles/buildings/v1/16/37852/24052.mvt";
const T17 = "/tiles/buildings/v1/17/75704/48104.mvt";
const GAP = "/tiles/buildings/v1/15/18915/12000.mvt";   // in Varna bounds, no data
const OOB_XY = "/tiles/buildings/v1/15/0/0.mvt";          // valid zoom, outside Varna
const OOB_Z_LO = "/tiles/buildings/v1/14/100/100.mvt";
const OOB_Z_HI = "/tiles/buildings/v1/18/100/100.mvt";

const PMTILES_BYTES = readFileSync(PMTILES);

// ---------------------------------------------------------------------------
// test plumbing
// ---------------------------------------------------------------------------
let passed = 0;
let failed = 0;
const failures = [];

function check(name, cond, detail) {
  if (cond) { passed++; console.log("  PASS  " + name); }
  else { failed++; failures.push(name + (detail ? " — " + detail : "")); console.log("  FAIL  " + name + (detail ? " — " + detail : "")); }
}

function makeR2(buffer, key, extra) {
  const store = new Map([[key, buffer]]);
  if (extra) for (const [k, v] of extra) store.set(k, v);
  return {
    reads: 0,
    async get(objectKey, options) {
      const buf = store.get(objectKey);
      if (!buf) return null;
      this.reads++;
      let slice = buf;
      if (options && options.range) {
        const { offset, length } = options.range;
        slice = buf.subarray(offset, offset + length);
      }
      const view = new Uint8Array(slice);
      return { size: view.length, async arrayBuffer() { return view.slice().buffer; } };
    },
  };
}

function makeEnv(opts = {}) {
  const extra = opts.detail
    ? [["details/buildings/v1/" + opts.detail.bd + ".json", opts.detail.bytes]]
    : null;
  const r2 = makeR2(PMTILES_BYTES, opts.objectKey || OBJECT_KEY, extra);
  const kv = opts.kv || { async get() { return null; }, async put() {} };
  const env = {
    BUILDING_TILES: opts.noR2 ? undefined : r2,
    REPORTS_CACHE: kv,
    BUILDING_TILES_OBJECT_KEY: opts.noKey ? undefined : (opts.objectKey || OBJECT_KEY),
    TILES_HMAC_SECRET: "secret" in opts ? opts.secret : SECRET,
    TILES_MIN_Z: "15",
    TILES_MAX_Z: "17",
    TILES_TOKEN_TTL_S: String(opts.ttl || 600),
    TILES_RATE_WINDOW_S: String(opts.window || 60),
    TILES_TOKEN_RATE_MAX: String(opts.tokenMax || 1000),
    TILES_TILE_RATE_MAX: String(opts.tileMax || 1000),
  };
  if ("pat" in opts) env.GITHUB_PAT = opts.pat;
  return { env, r2, kv };
}

function installCaches() {
  const map = new Map();
  globalThis.caches = {
    default: {
      async match(req) {
        const stored = map.get(typeof req === "string" ? req : req.url);
        return stored ? stored.clone() : undefined;
      },
      async put(req, res) {
        map.set(typeof req === "string" ? req : req.url, res.clone());
      },
    },
  };
  return map;
}

function makeCtx() {
  const promises = [];
  return { waitUntil: (p) => promises.push(p), settle: () => Promise.all(promises) };
}

async function loadFreshModule(tag) {
  return import(INDEX_URL + "?case=" + encodeURIComponent(tag));
}

function buildRequest(path, opts = {}) {
  const headers = new Headers(opts.headers || {});
  if (opts.origin !== null) headers.set("Origin", opts.origin || ORIGIN);
  if (opts.referer) headers.set("Referer", opts.referer);
  if (opts.ip !== null) headers.set("CF-Connecting-IP", opts.ip || "1.2.3.4");
  const init = { method: opts.method || "GET", headers };
  if (opts.body !== undefined) init.body = typeof opts.body === "string" ? opts.body : JSON.stringify(opts.body);
  return new Request(WORKER_BASE + path, init);
}

async function callWorker(mod, env, path, opts = {}) {
  const ctx = makeCtx();
  const res = await mod.default.fetch(buildRequest(path, opts), env, ctx);
  await ctx.settle();
  return res;
}

// ---------------------------------------------------------------------------
// token minting (mirrors the worker; used for malformed/expired/scope cases,
// and cross-checked against the live token endpoint in the happy-path test)
// ---------------------------------------------------------------------------
function b64url(bytes) {
  let binary = "";
  for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

async function mintToken(secret, payload) {
  const enc = new TextEncoder();
  const body = b64url(enc.encode(JSON.stringify(payload)));
  const key = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", key, enc.encode(body)));
  return body + "." + b64url(sig);
}

function nowS() { return Math.floor(Date.now() / 1000); }

// ---------------------------------------------------------------------------
// minimal MVT (protobuf) decoder — enough to prove decodability + whitelist
// ---------------------------------------------------------------------------
function readPbVarint(bytes, p) {
  let result = 0, shift = 0;
  for (;;) {
    const byte = bytes[p.i++];
    result += (byte & 0x7f) * Math.pow(2, shift);
    if ((byte & 0x80) === 0) break;
    shift += 7;
  }
  return result;
}
function skipPb(bytes, p, wire) {
  // NB: read the length into a local BEFORE advancing p.i — `p.i += readPbVarint(p)`
  // would capture the old p.i for the += and drop the varint's own bytes.
  if (wire === 0) readPbVarint(bytes, p);
  else if (wire === 2) { const len = readPbVarint(bytes, p); p.i += len; }
  else if (wire === 5) p.i += 4;
  else if (wire === 1) p.i += 8;
  else throw new Error("bad wire type " + wire);
}
function decodeMvtLayer(bytes, start, end) {
  const p = { i: start };
  let name = null, version = null, extent = null, features = 0;
  const keys = [];
  const dec = new TextDecoder();
  while (p.i < end) {
    const tag = readPbVarint(bytes, p), field = tag >> 3, wire = tag & 7;
    if (field === 15 && wire === 0) version = readPbVarint(bytes, p);
    else if (field === 1 && wire === 2) { const len = readPbVarint(bytes, p); name = dec.decode(bytes.subarray(p.i, p.i + len)); p.i += len; }
    else if (field === 2 && wire === 2) { const len = readPbVarint(bytes, p); features++; p.i += len; }
    else if (field === 3 && wire === 2) { const len = readPbVarint(bytes, p); keys.push(dec.decode(bytes.subarray(p.i, p.i + len))); p.i += len; }
    else if (field === 5 && wire === 0) extent = readPbVarint(bytes, p);
    else skipPb(bytes, p, wire);
  }
  return { name, version, extent, features, keys };
}
function decodeMvt(bytes) {
  const p = { i: 0 };
  const layers = [];
  while (p.i < bytes.length) {
    const tag = readPbVarint(bytes, p), field = tag >> 3, wire = tag & 7;
    if (field === 3 && wire === 2) { const len = readPbVarint(bytes, p); layers.push(decodeMvtLayer(bytes, p.i, p.i + len)); p.i += len; }
    else skipPb(bytes, p, wire);
  }
  return layers;
}

// ---------------------------------------------------------------------------
// GitHub fetch stub (for the existing GET /issues + POST / routes)
// ---------------------------------------------------------------------------
const ISSUE_BODY = [
  "---",
  "report_type: wrong_location",
  "hydrant_ref: H-001",
  "reported_coord: [27.91, 43.21]",
  'timestamp: "2026-06-20T10:00:00Z"',
  "free_text: до училището",
  "---",
  "free text body",
].join("\n");

const GITHUB_ISSUES = [{
  number: 101,
  html_url: "https://github.com/Petar1984/Fire_Varna/issues/101",
  created_at: "2026-06-20T10:00:00Z",
  updated_at: "2026-06-20T10:05:00Z",
  labels: [{ name: "report" }],
  body: ISSUE_BODY,
}];

function installGithubFetch() {
  const real = globalThis.fetch;
  globalThis.fetch = async (input, init) => {
    const u = typeof input === "string" ? input : input.url;
    if (u.startsWith("https://api.github.com/")) {
      const method = (init && init.method) || "GET";
      if (method === "POST") {
        return new Response(JSON.stringify({ number: 202, html_url: "https://github.com/Petar1984/Fire_Varna/issues/202" }), {
          status: 201, headers: { "Content-Type": "application/json; charset=utf-8" },
        });
      }
      return new Response(JSON.stringify(GITHUB_ISSUES), { status: 200, headers: { "Content-Type": "application/json; charset=utf-8" } });
    }
    return real(input, init);
  };
  return () => { globalThis.fetch = real; };
}

// ===========================================================================
// TEST GROUPS
// ===========================================================================

async function testHappyPath() {
  console.log("\n[happy] token issuance + z15/z16/z17 tiles");
  const mod = await loadFreshModule("happy");
  installCaches();
  const { env, r2 } = makeEnv();

  // token endpoint
  const tokenRes = await callWorker(mod, env, "/tiles/buildings/token", { origin: ORIGIN });
  check("token endpoint 200", tokenRes.status === 200, "status=" + tokenRes.status);
  check("token Cache-Control no-store", tokenRes.headers.get("Cache-Control") === "no-store");
  check("token ACAO echoes origin", tokenRes.headers.get("Access-Control-Allow-Origin") === ORIGIN);
  const tokenBody = await tokenRes.json();
  check("token scope buildings:v1", tokenBody.scope === "buildings:v1");
  check("token string present", typeof tokenBody.token === "string" && tokenBody.token.includes("."));

  // each zoom -> decodable MVT
  for (const [label, path] of [["z15", T15], ["z16", T16], ["z17", T17]]) {
    const res = await callWorker(mod, env, path + "?token=" + tokenBody.token, { origin: ORIGIN });
    check(label + " tile 200", res.status === 200, "status=" + res.status);
    check(label + " Content-Type vnd.mapbox-vector-tile", res.headers.get("Content-Type") === "application/vnd.mapbox-vector-tile");
    check(label + " Cache-Control exact", res.headers.get("Cache-Control") === "public, max-age=86400, s-maxage=604800, immutable");
    check(label + " X-Robots-Tag noindex", res.headers.get("X-Robots-Tag") === "noindex");
    check(label + " ACAO echoes origin", res.headers.get("Access-Control-Allow-Origin") === ORIGIN);
    const bytes = new Uint8Array(await res.arrayBuffer());
    check(label + " non-empty body", bytes.length > 0, "len=" + bytes.length);
    const layers = decodeMvt(bytes);
    const buildings = layers.find((l) => l.name === "buildings");
    check(label + " has buildings layer", !!buildings, "layers=" + layers.map((l) => l.name).join(","));
    check(label + " buildings has features", buildings && buildings.features > 0, buildings && "features=" + buildings.features);
    const badKeys = buildings ? buildings.keys.filter((k) => !ALLOWED_KEYS.has(k)) : ["<no layer>"];
    check(label + " keys within safe whitelist", badKeys.length === 0, "offending=" + JSON.stringify(badKeys));
  }

  // parity: a test-minted token is accepted exactly like the endpoint's token
  const minted = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
  const parityRes = await callWorker(mod, env, T15 + "?token=" + minted, { origin: ORIGIN });
  check("test-minted token accepted (signing parity)", parityRes.status === 200, "status=" + parityRes.status);

  // OPTIONS /tiles/* preflight
  const opt = await callWorker(mod, env, "/tiles/buildings/v1/15/18926/12026.mvt", { method: "OPTIONS", origin: ORIGIN });
  check("OPTIONS /tiles 204", opt.status === 204, "status=" + opt.status);
  check("OPTIONS /tiles allow GET, OPTIONS", opt.headers.get("Access-Control-Allow-Methods") === "GET, OPTIONS");

  check("R2 was actually read on cold isolate", r2.reads > 0, "reads=" + r2.reads);
}

async function testRejections() {
  console.log("\n[reject] origin / token / bounds");
  const mod = await loadFreshModule("reject");
  installCaches();
  const { env } = makeEnv();
  const goodToken = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });

  // no origin + no referer -> 403 on both endpoints
  const noOriginTok = await callWorker(mod, env, "/tiles/buildings/token", { origin: null, ip: "9.9.9.1" });
  check("token: no origin/referer -> 403", noOriginTok.status === 403, "status=" + noOriginTok.status);
  const noOriginTile = await callWorker(mod, env, T15 + "?token=" + goodToken, { origin: null, ip: "9.9.9.2" });
  check("tile: no origin/referer -> 403", noOriginTile.status === 403, "status=" + noOriginTile.status);

  // disallowed origin -> 403
  const badOrigin = await callWorker(mod, env, T15 + "?token=" + goodToken, { origin: BAD_ORIGIN, ip: "9.9.9.3" });
  check("tile: disallowed origin -> 403", badOrigin.status === 403, "status=" + badOrigin.status);

  // missing token -> 401
  const noToken = await callWorker(mod, env, T15, { origin: ORIGIN, ip: "9.9.9.4" });
  check("tile: missing token -> 401", noToken.status === 401, "status=" + noToken.status);

  // malformed token -> 401
  const malformed = await callWorker(mod, env, T15 + "?token=not-a-token", { origin: ORIGIN, ip: "9.9.9.5" });
  check("tile: malformed token -> 401", malformed.status === 401, "status=" + malformed.status);

  // tampered signature -> 401. Flip the FIRST signature char (always significant
  // bits); the LAST char of a 32-byte HMAC only carries base64 padding bits that
  // decode away, so flipping it would not change the decoded signature.
  const dotIdx = goodToken.indexOf(".");
  const sigPart = goodToken.slice(dotIdx + 1);
  const tampered = goodToken.slice(0, dotIdx + 1) + (sigPart[0] === "A" ? "B" : "A") + sigPart.slice(1);
  const tamperedRes = await callWorker(mod, env, T15 + "?token=" + tampered, { origin: ORIGIN, ip: "9.9.9.6" });
  check("tile: tampered signature -> 401", tamperedRes.status === 401, "status=" + tamperedRes.status);

  // wrong scope -> 401
  const wrongScope = await mintToken(SECRET, { v: 1, scope: "buildings:v0", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
  const wrongScopeRes = await callWorker(mod, env, T15 + "?token=" + wrongScope, { origin: ORIGIN, ip: "9.9.9.7" });
  check("tile: wrong scope -> 401", wrongScopeRes.status === 401, "status=" + wrongScopeRes.status);
  check("tile: wrong scope body invalid_scope", (await wrongScopeRes.json()).error === "invalid_scope");

  // expired token -> 401 token_expired
  const expired = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS() - 700, exp: nowS() - 100 });
  const expiredRes = await callWorker(mod, env, T15 + "?token=" + expired, { origin: ORIGIN, ip: "9.9.9.8" });
  check("tile: expired token -> 401", expiredRes.status === 401, "status=" + expiredRes.status);
  check("tile: expired body token_expired", (await expiredRes.json()).error === "token_expired");

  // origin mismatch (token for ORIGIN, request from ORIGIN2 — both allowlisted) -> 401
  const mismatchRes = await callWorker(mod, env, T15 + "?token=" + goodToken, { origin: ORIGIN2, ip: "9.9.9.9" });
  check("tile: origin mismatch -> 401", mismatchRes.status === 401, "status=" + mismatchRes.status);
  check("tile: origin mismatch body", (await mismatchRes.json()).error === "origin_mismatch");

  // out-of-range zoom -> 404
  const zlo = await callWorker(mod, env, OOB_Z_LO + "?token=" + goodToken, { origin: ORIGIN, ip: "9.9.9.10" });
  check("tile: zoom 14 -> 404 zoom_out_of_range", zlo.status === 404 && (await zlo.json()).error === "zoom_out_of_range");
  const zhi = await callWorker(mod, env, OOB_Z_HI + "?token=" + goodToken, { origin: ORIGIN, ip: "9.9.9.11" });
  check("tile: zoom 18 -> 404 zoom_out_of_range", zhi.status === 404 && (await zhi.json()).error === "zoom_out_of_range");

  // out-of-range x/y (valid zoom) -> 404
  const oobxy = await callWorker(mod, env, OOB_XY + "?token=" + goodToken, { origin: ORIGIN, ip: "9.9.9.12" });
  check("tile: x/y outside Varna -> 404 xy_out_of_range", oobxy.status === 404 && (await oobxy.json()).error === "xy_out_of_range");

  // in-bounds but no data -> 404 not_found (exercises the R2/directory gap)
  const gap = await callWorker(mod, env, GAP + "?token=" + goodToken, { origin: ORIGIN, ip: "9.9.9.13" });
  check("tile: in-bounds gap -> 404 not_found", gap.status === 404 && (await gap.json()).error === "not_found");
}

async function testRateLimit() {
  console.log("\n[rate-limit] 429 + Retry-After on token + tile endpoints");

  // token endpoint
  {
    const mod = await loadFreshModule("rl-token");
    installCaches();
    const { env } = makeEnv({ tokenMax: 2, window: 60 });
    const ip = "5.5.5.1";
    const r1 = await callWorker(mod, env, "/tiles/buildings/token", { origin: ORIGIN, ip });
    const r2 = await callWorker(mod, env, "/tiles/buildings/token", { origin: ORIGIN, ip });
    const r3 = await callWorker(mod, env, "/tiles/buildings/token", { origin: ORIGIN, ip });
    check("token: 1st ok", r1.status === 200);
    check("token: 2nd ok", r2.status === 200);
    check("token: 3rd -> 429", r3.status === 429, "status=" + r3.status);
    check("token: 429 has Retry-After", !!r3.headers.get("Retry-After"));
  }

  // tile endpoint
  {
    const mod = await loadFreshModule("rl-tile");
    installCaches();
    const { env } = makeEnv({ tileMax: 2, tokenMax: 1000, window: 60 });
    const token = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
    const ip = "5.5.5.2";
    const a = await callWorker(mod, env, T15 + "?token=" + token, { origin: ORIGIN, ip });
    const b = await callWorker(mod, env, T16 + "?token=" + token, { origin: ORIGIN, ip });
    const c = await callWorker(mod, env, T17 + "?token=" + token, { origin: ORIGIN, ip });
    check("tile: 1st ok", a.status === 200, "status=" + a.status);
    check("tile: 2nd ok", b.status === 200, "status=" + b.status);
    check("tile: 3rd -> 429", c.status === 429, "status=" + c.status);
    check("tile: 429 has Retry-After", !!c.headers.get("Retry-After"));
  }
}

async function testCache() {
  console.log("\n[cache] pathname-only key dedups tokens; 2nd avoids R2");
  const mod = await loadFreshModule("cache");
  installCaches();
  const { env, r2 } = makeEnv();
  const t1 = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
  const t2 = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS() + 1, exp: nowS() + 601 });
  check("two distinct tokens", t1 !== t2);

  const r0 = r2.reads;
  const first = await callWorker(mod, env, T15 + "?token=" + t1, { origin: ORIGIN, ip: "7.7.7.1" });
  const afterFirst = r2.reads;
  check("first request 200 MISS", first.status === 200 && first.headers.get("X-Cache") === "MISS", "x-cache=" + first.headers.get("X-Cache"));
  check("first request read R2 (header+root+tile = 3)", afterFirst - r0 === 3, "delta=" + (afterFirst - r0));

  // different token, same tile path -> HIT, no new R2 reads
  const second = await callWorker(mod, env, T15 + "?token=" + t2, { origin: ORIGIN, ip: "7.7.7.2" });
  check("second request 200 HIT", second.status === 200 && second.headers.get("X-Cache") === "HIT", "x-cache=" + second.headers.get("X-Cache"));
  check("second request avoided R2 (reads unchanged)", r2.reads === afterFirst, "reads=" + r2.reads + " expected=" + afterFirst);

  // a different tile reuses the cached header+root directory (1 R2 read only)
  const third = await callWorker(mod, env, T16 + "?token=" + t1, { origin: ORIGIN, ip: "7.7.7.3" });
  check("third (new tile) 200 MISS", third.status === 200 && third.headers.get("X-Cache") === "MISS");
  check("third reused cached directory (only 1 R2 read)", r2.reads - afterFirst === 1, "delta=" + (r2.reads - afterFirst));
}

async function testRegression() {
  console.log("\n[regression] existing OPTIONS / + GET /issues + POST / unchanged");
  const restore = installGithubFetch();
  try {
    // OPTIONS / (generic) — must NOT be captured by the /tiles OPTIONS branch
    {
      const mod = await loadFreshModule("reg-opt");
      installCaches();
      const { env } = makeEnv({ pat: "fake-pat" });
      const ok = await callWorker(mod, env, "/", { method: "OPTIONS", origin: ORIGIN });
      check("OPTIONS / -> 204", ok.status === 204, "status=" + ok.status);
      check("OPTIONS / allow GET, POST, OPTIONS", ok.headers.get("Access-Control-Allow-Methods") === "GET, POST, OPTIONS", "got=" + ok.headers.get("Access-Control-Allow-Methods"));
      check("OPTIONS / ACAO echoes origin", ok.headers.get("Access-Control-Allow-Origin") === ORIGIN);
      const bad = await callWorker(mod, env, "/", { method: "OPTIONS", origin: BAD_ORIGIN });
      check("OPTIONS / disallowed origin -> 403", bad.status === 403, "status=" + bad.status);
    }

    // GET /issues — response shape unchanged
    {
      const mod = await loadFreshModule("reg-issues");
      installCaches();
      const { env } = makeEnv({ pat: "fake-pat" });
      const res = await callWorker(mod, env, "/issues", { origin: ORIGIN });
      check("GET /issues -> 200", res.status === 200, "status=" + res.status);
      check("GET /issues X-Cache-Status present", !!res.headers.get("X-Cache-Status"), "hdr=" + res.headers.get("X-Cache-Status"));
      check("GET /issues X-Parse-Warnings 0", res.headers.get("X-Parse-Warnings") === "0", "hdr=" + res.headers.get("X-Parse-Warnings"));
      const body = await res.json();
      const shapeOk = Array.isArray(body.reports) && "cached_at" in body && "ttl_seconds" in body && "stale" in body;
      check("GET /issues response shape {reports,cached_at,ttl_seconds,stale}", shapeOk, "keys=" + Object.keys(body).join(","));
      check("GET /issues report normalized", body.reports.length === 1 && body.reports[0].id === "github_issue_101", JSON.stringify(body.reports[0] && body.reports[0].id));
      check("GET /issues report has expected fields", body.reports[0] && body.reports[0].report_type === "wrong_location" && Array.isArray(body.reports[0].coords));

      // query params still honored
      const since = await callWorker(mod, env, "/issues?since=2026-06-21T00:00:00Z", { origin: ORIGIN });
      const sinceBody = await since.json();
      check("GET /issues?since filters out older report", since.status === 200 && sinceBody.reports.length === 0, "len=" + sinceBody.reports.length);
      const badLimit = await callWorker(mod, env, "/issues?limit=abc", { origin: ORIGIN });
      check("GET /issues?limit=abc -> 400 invalid_limit", badLimit.status === 400 && (await badLimit.json()).error === "invalid_limit");
    }

    // POST / — create issue passthrough
    {
      const mod = await loadFreshModule("reg-post");
      installCaches();
      const { env } = makeEnv({ pat: "fake-pat" });
      const created = await callWorker(mod, env, "/", { method: "POST", origin: ORIGIN, body: { title: "t", body: "b", labels: ["report"] }, headers: { "Content-Type": "application/json" } });
      check("POST / -> 201 passthrough", created.status === 201, "status=" + created.status);
      check("POST / returns GitHub body", (await created.json()).number === 202);
      const missing = await callWorker(mod, env, "/", { method: "POST", origin: ORIGIN, body: { title: "only title" }, headers: { "Content-Type": "application/json" } });
      check("POST / missing body -> 400", missing.status === 400, "status=" + missing.status);
    }

    // POST / with no PAT -> 500 (unchanged behavior)
    {
      const mod = await loadFreshModule("reg-nopat");
      installCaches();
      const { env } = makeEnv({}); // no GITHUB_PAT
      const res = await callWorker(mod, env, "/", { method: "POST", origin: ORIGIN, body: { title: "t", body: "b" }, headers: { "Content-Type": "application/json" } });
      check("POST / without PAT -> 500", res.status === 500, "status=" + res.status);
    }

    // unknown route -> 404 not_found (unchanged)
    {
      const mod = await loadFreshModule("reg-404");
      installCaches();
      const { env } = makeEnv({ pat: "fake-pat" });
      const res = await callWorker(mod, env, "/nope", { origin: ORIGIN });
      check("GET /nope -> 404 not_found", res.status === 404 && (await res.json()).error === "not_found");
    }
  } finally {
    restore();
  }
}

async function testCacheObjectKeyVersioning() {
  console.log("\n[cache-objkey] tile cache key is versioned by object key -> no stale tile after a key bump");
  const mod = await loadFreshModule("cache-objkey");
  installCaches(); // ONE shared cache across both envs (simulates the same isolate across a redeploy)
  const token = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
  const K1 = OBJECT_KEY; // current build's object key
  const K2 = "tiles/buildings_safe_v0000000000000000000000000000000000000000000000000000000000000000.pmtiles"; // a redeploy
  const { env: envA, r2: r2A } = makeEnv({ objectKey: K1 });
  const { env: envB, r2: r2B } = makeEnv({ objectKey: K2 }); // same PMTiles bytes seeded under the new key

  const a1 = await callWorker(mod, envA, T15 + "?token=" + token, { origin: ORIGIN, ip: "6.6.6.1" });
  check("objkey: A first MISS", a1.status === 200 && a1.headers.get("X-Cache") === "MISS", "x-cache=" + a1.headers.get("X-Cache"));
  check("objkey: A read R2", r2A.reads > 0, "reads=" + r2A.reads);

  // Same tile PATH, NEW object key (redeploy): must be a MISS (fresh cache key),
  // NOT a stale HIT of A's cached bytes.
  const r2bBefore = r2B.reads;
  const b1 = await callWorker(mod, envB, T15 + "?token=" + token, { origin: ORIGIN, ip: "6.6.6.2" });
  check("objkey: B (new key) MISS not stale", b1.status === 200 && b1.headers.get("X-Cache") === "MISS", "x-cache=" + b1.headers.get("X-Cache"));
  check("objkey: B read R2 under new key", r2B.reads > r2bBefore, "reads=" + r2B.reads);

  // Dedup still holds WITHIN a key: re-request under K1 -> HIT, no new R2 read.
  const r2aBefore = r2A.reads;
  const a2 = await callWorker(mod, envA, T15 + "?token=" + token, { origin: ORIGIN, ip: "6.6.6.3" });
  check("objkey: A second HIT (dedup within key)", a2.status === 200 && a2.headers.get("X-Cache") === "HIT", "x-cache=" + a2.headers.get("X-Cache"));
  check("objkey: A second avoided R2", r2A.reads === r2aBefore, "reads=" + r2A.reads + " expected=" + r2aBefore);
}

async function testDetailRoute() {
  console.log("\n[detail] GET /tiles/buildings/v1/detail/{bd}.json — token-gated, fail-closed, cached");
  const BD = "b0123456789abcdef";
  const D_OK = "/tiles/buildings/v1/detail/" + BD + ".json";
  const D_MISSING = "/tiles/buildings/v1/detail/b0000000000000000.json"; // valid format, no object
  const D_BADFMT = "/tiles/buildings/v1/detail/babc.json";               // routes here, fails bd regex
  const detailJson = JSON.stringify({
    v: 1, bd: BD, type: { code: "110", label: "Жилищна сграда - многофамилна", class: "block" },
    apartment_count: 18, data_confidence: { entrance_coverage: 0.94 },
    entrances: [{ en: "А", pin: { lat: 43.2061, lng: 27.89209 }, floors: 5, apartment_count: 17, breakdown: { apartment: 17 } }],
  });
  const detailBytes = new TextEncoder().encode(detailJson);
  const seed = () => ({ detail: { bd: BD, bytes: detailBytes } });

  // --- happy path ---
  {
    const mod = await loadFreshModule("detail-happy");
    installCaches();
    const { env, r2 } = makeEnv(seed());
    const token = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
    const res = await callWorker(mod, env, D_OK + "?token=" + token, { origin: ORIGIN, ip: "8.8.8.1" });
    check("detail happy 200", res.status === 200, "status=" + res.status);
    check("detail Content-Type application/json", res.headers.get("Content-Type") === "application/json; charset=utf-8");
    check("detail Cache-Control immutable", res.headers.get("Cache-Control") === "public, max-age=86400, s-maxage=604800, immutable");
    check("detail X-Robots-Tag noindex", res.headers.get("X-Robots-Tag") === "noindex");
    check("detail ACAO echoes origin", res.headers.get("Access-Control-Allow-Origin") === ORIGIN);
    check("detail X-Cache MISS first", res.headers.get("X-Cache") === "MISS");
    const body = await res.json();
    check("detail body bd matches", body.bd === BD, "bd=" + body.bd);
    check("detail body has entrances", Array.isArray(body.entrances) && body.entrances.length === 1);
    check("detail read R2 once", r2.reads === 1, "reads=" + r2.reads);
    const opt = await callWorker(mod, env, D_OK, { method: "OPTIONS", origin: ORIGIN });
    check("detail OPTIONS 204 (via /tiles/* branch)", opt.status === 204, "status=" + opt.status);
  }

  // --- rejections: origin / token / scope / expiry / bd format / missing object ---
  {
    const mod = await loadFreshModule("detail-reject");
    installCaches();
    const { env } = makeEnv(seed());
    const good = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });

    const noOrigin = await callWorker(mod, env, D_OK + "?token=" + good, { origin: null, ip: "8.8.9.1" });
    check("detail no origin -> 403", noOrigin.status === 403, "status=" + noOrigin.status);
    check("detail 403 no-store", noOrigin.headers.get("Cache-Control") === "no-store");

    const badOrigin = await callWorker(mod, env, D_OK + "?token=" + good, { origin: BAD_ORIGIN, ip: "8.8.9.2" });
    check("detail disallowed origin -> 403", badOrigin.status === 403, "status=" + badOrigin.status);

    const noToken = await callWorker(mod, env, D_OK, { origin: ORIGIN, ip: "8.8.9.3" });
    check("detail missing token -> 401", noToken.status === 401, "status=" + noToken.status);

    const malformed = await callWorker(mod, env, D_OK + "?token=not-a-token", { origin: ORIGIN, ip: "8.8.9.4" });
    check("detail malformed token -> 401", malformed.status === 401, "status=" + malformed.status);

    const wrongScope = await mintToken(SECRET, { v: 1, scope: "buildings:v0", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
    const wsRes = await callWorker(mod, env, D_OK + "?token=" + wrongScope, { origin: ORIGIN, ip: "8.8.9.5" });
    check("detail wrong scope -> 401 invalid_scope", wsRes.status === 401 && (await wsRes.json()).error === "invalid_scope");

    const expired = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS() - 700, exp: nowS() - 100 });
    const expRes = await callWorker(mod, env, D_OK + "?token=" + expired, { origin: ORIGIN, ip: "8.8.9.6" });
    check("detail expired -> 401 token_expired", expRes.status === 401 && (await expRes.json()).error === "token_expired");

    const mism = await callWorker(mod, env, D_OK + "?token=" + good, { origin: ORIGIN2, ip: "8.8.9.7" });
    check("detail origin mismatch -> 401", mism.status === 401 && (await mism.json()).error === "origin_mismatch");

    const badFmt = await callWorker(mod, env, D_BADFMT + "?token=" + good, { origin: ORIGIN, ip: "8.8.9.8" });
    check("detail bad bd format -> 404 not_found", badFmt.status === 404 && (await badFmt.json()).error === "not_found");
    check("detail 404 no-store", badFmt.headers.get("Cache-Control") === "no-store");

    const missing = await callWorker(mod, env, D_MISSING + "?token=" + good, { origin: ORIGIN, ip: "8.8.9.9" });
    check("detail valid-but-missing -> 404 not_found", missing.status === 404 && (await missing.json()).error === "not_found");
  }

  // --- rate-limit (shares the 'tile' bucket) ---
  {
    const mod = await loadFreshModule("detail-rl");
    installCaches();
    const { env } = makeEnv({ ...seed(), tileMax: 2, tokenMax: 1000, window: 60 });
    const token = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
    const ip = "8.8.10.1";
    const a = await callWorker(mod, env, D_OK + "?token=" + token, { origin: ORIGIN, ip });
    const b = await callWorker(mod, env, D_MISSING + "?token=" + token, { origin: ORIGIN, ip });
    const c = await callWorker(mod, env, D_OK + "?token=" + token, { origin: ORIGIN, ip });
    check("detail rl 1st ok", a.status === 200, "status=" + a.status);
    check("detail rl 2nd (missing) 404", b.status === 404, "status=" + b.status);
    check("detail rl 3rd -> 429", c.status === 429, "status=" + c.status);
    check("detail rl 429 Retry-After", !!c.headers.get("Retry-After"));
  }

  // --- cache dedup: different token, same path -> HIT, no new R2 read ---
  {
    const mod = await loadFreshModule("detail-cache");
    installCaches();
    const { env, r2 } = makeEnv(seed());
    const t1 = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS(), exp: nowS() + 600 });
    const t2 = await mintToken(SECRET, { v: 1, scope: "buildings:v1", origin: ORIGIN, iat: nowS() + 1, exp: nowS() + 601 });
    const r0 = r2.reads;
    const first = await callWorker(mod, env, D_OK + "?token=" + t1, { origin: ORIGIN, ip: "8.8.11.1" });
    check("detail cache first MISS", first.status === 200 && first.headers.get("X-Cache") === "MISS");
    check("detail cache first read R2 (1)", r2.reads - r0 === 1, "delta=" + (r2.reads - r0));
    const second = await callWorker(mod, env, D_OK + "?token=" + t2, { origin: ORIGIN, ip: "8.8.11.2" });
    check("detail cache second HIT", second.status === 200 && second.headers.get("X-Cache") === "HIT", "x-cache=" + second.headers.get("X-Cache"));
    check("detail cache second avoided R2", r2.reads - r0 === 1, "reads delta=" + (r2.reads - r0));
  }
}

// ===========================================================================
async function main() {
  console.log("Worker local tests (dependency-free; real index.js, mocked R2/KV/Cache/fetch)");
  console.log("PMTiles seed:", PMTILES);
  await testHappyPath();
  await testRejections();
  await testRateLimit();
  await testCache();
  await testCacheObjectKeyVersioning();
  await testDetailRoute();
  await testRegression();

  console.log("\n========================================");
  console.log(`RESULT: ${passed} passed, ${failed} failed`);
  if (failed) {
    console.log("\nFailures:");
    for (const f of failures) console.log("  - " + f);
    process.exit(1);
  }
  console.log("ALL TESTS PASSED");
}

main().catch((err) => { console.error("HARNESS ERROR:", err); process.exit(1); });
