/* Fire_Varna service worker — Basemap B2 (§6.5 + audit addendum).
 *
 * This is the FIRST service worker in Fire_Varna. It exists ONLY to make the offline
 * OSM/PMTiles basemap and the exact-search data available offline, and it is registered
 * by index.html ONLY when the PMTiles capability is active (committed flag is false, so
 * a device opts in via ?basemap_pmtiles=1 or a later signed flag flip). With the flag
 * false and no override, index.html never registers this worker, so normal live users
 * are untouched.
 *
 * Cache discipline:
 *   - Versioned cache names (end with BASEMAP_VERSION); activate() prunes only OLD B2
 *     caches and NEVER touches the app's own search namespaces (PROTECTED).
 *   - Mutating data (hydrants / search_index / address_rows / basemap_manifest) is
 *     NETWORK-FIRST with cache fallback (addendum Поправка 1): staleness only when
 *     offline; a future data push is never masked while online.
 *   - Versioned-by-path basemap assets (data/basemaps/<version>/*) and pinned vendor
 *     deps (vendor/basemap/*) are CACHE-FIRST (their URL changes when they change).
 *   - varna_basemap.pmtiles: if the full file is cached, HTTP Range requests are sliced
 *     to a correct 206 from the cached ArrayBuffer; otherwise the Range passes through
 *     to network unchanged.
 *   - The heavy offline pack (data + full pmtiles) is fetched ONLY on an explicit
 *     opt-in message from the page (addendum Поправка 2: opt-in effective only when the
 *     capability is active, which the page enforces before posting).
 *   - Cross-origin requests (Cloudflare Worker tiles/token, live OSM raster, Esri
 *     satellite) are NEVER intercepted.
 */
'use strict';

const BASEMAP_VERSION =
  'osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b';

// Versioned B2 cache names (mirror data/basemaps/basemap_manifest.json cache_names).
const CACHE_CORE = 'fire-varna-core-' + BASEMAP_VERSION;
const CACHE_OFFLINE_PACK = 'fire-varna-offline-pack-' + BASEMAP_VERSION;
const CACHE_BASEMAP = 'fire-varna-basemap-' + BASEMAP_VERSION;

// Prefixes this worker owns (activate() only ever prunes caches starting with these).
const B2_CACHE_PREFIXES = [
  'fire-varna-core-',
  'fire-varna-offline-pack-',
  'fire-varna-basemap-',
];

// The app's own search caches. This worker must NEVER delete or mutate them. They are
// managed entirely by index.html's own fetch-and-cache logic.
const PROTECTED_CACHES = ['fire-varna-search-v2', 'fire-varna-approx-addresses-v1'];

const PMTILES_REL = 'data/basemaps/' + BASEMAP_VERSION + '/varna_basemap.pmtiles';

// NETWORK-FIRST set — files that change independently of the basemap version.
const MUTATING_DATA = new Set([
  'data/hydrants.json',
  'data/search_index.json',
  'data/address_rows.json',
  'data/basemaps/basemap_manifest.json',
]);

// Precached at install (lightweight shell + basemap metadata + pinned deps). The big
// data files and the full pmtiles are NOT here — they arrive only on opt-in.
const SHELL_ASSETS = {
  core: ['index.html'],
  basemap: [
    'vendor/basemap/pmtiles-3.2.1.js',
    'vendor/basemap/protomaps-leaflet-4.0.1.js',
    'data/basemaps/' + BASEMAP_VERSION + '/style.json',
    'data/basemaps/' + BASEMAP_VERSION + '/varna_basemap_manifest.json',
    'data/basemaps/' + BASEMAP_VERSION + '/odbl/README_ODbL.md',
    'data/basemaps/' + BASEMAP_VERSION + '/odbl/ATTRIBUTION.txt',
    'data/basemaps/' + BASEMAP_VERSION + '/odbl/osm_varna_patch_v1.csv',
    'data/basemaps/' + BASEMAP_VERSION + '/odbl/osm_varna_source_manifest.json',
  ],
  offlinePack: ['data/basemaps/basemap_manifest.json'],
};

// The heavy opt-in pack (fetched on 'install-offline-pack' message).
const PACK_DATA = ['data/hydrants.json', 'data/search_index.json', 'data/address_rows.json'];
// PACK_PMTILES cached full-file into CACHE_BASEMAP: PMTILES_REL.

// ---------------------------------------------------------------------------
// Install: precache the shell + basemap metadata. skipWaiting only on success so a
// failed install keeps the previous worker/caches intact.
// ---------------------------------------------------------------------------
self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const core = await caches.open(CACHE_CORE);
    await core.addAll(SHELL_ASSETS.core);
    const basemap = await caches.open(CACHE_BASEMAP);
    await basemap.addAll(SHELL_ASSETS.basemap);
    const pack = await caches.open(CACHE_OFFLINE_PACK);
    // basemap_manifest is network-first at fetch time; precache only for offline fallback.
    await Promise.allSettled(SHELL_ASSETS.offlinePack.map((u) => pack.add(u)));
    await self.skipWaiting();
  })());
});

// ---------------------------------------------------------------------------
// Activate: prune only OLD B2 caches; never touch PROTECTED caches. Claim clients.
// ---------------------------------------------------------------------------
self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.map((name) => {
      if (PROTECTED_CACHES.includes(name)) return Promise.resolve();  // never delete
      const ownedByB2 = B2_CACHE_PREFIXES.some((p) => name.startsWith(p));
      const isCurrent = name.endsWith(BASEMAP_VERSION);
      if (ownedByB2 && !isCurrent) return caches.delete(name);
      return Promise.resolve();
    }));
    await self.clients.claim();
  })());
});

// ---------------------------------------------------------------------------
// Message channel: the page requests the heavy offline-pack install on opt-in, and can
// query readiness. The page is responsible for only sending 'install-offline-pack' when
// the PMTiles capability is active (addendum Поправка 2).
// ---------------------------------------------------------------------------
self.addEventListener('message', (event) => {
  const data = event.data || {};
  if (data.type === 'install-offline-pack') {
    event.waitUntil(installOfflinePack());
  } else if (data.type === 'offline-pack-status') {
    event.waitUntil(reportPackStatus(event.source));
  }
});

async function installOfflinePack() {
  try {
    const pack = await caches.open(CACHE_OFFLINE_PACK);
    for (const url of PACK_DATA) {
      const res = await fetch(url, { cache: 'no-store' });
      if (!res.ok) throw new Error('pack fetch failed ' + url + ' ' + res.status);
      await pack.put(url, res.clone());
    }
    const basemap = await caches.open(CACHE_BASEMAP);
    const pm = await fetch(PMTILES_REL, { cache: 'no-store' });  // full file, no Range
    if (!pm.ok) throw new Error('pmtiles fetch failed ' + pm.status);
    await basemap.put(PMTILES_REL, pm.clone());
    await broadcast({ type: 'offline-pack-ready', version: BASEMAP_VERSION });
  } catch (err) {
    const quota = err && (err.name === 'QuotaExceededError' ||
      /quota/i.test(String(err && err.message)));
    await broadcast({
      type: 'offline-pack-error',
      quota: !!quota,
      error: String(err && err.message ? err.message : err),
    });
  }
}

async function reportPackStatus(client) {
  const basemap = await caches.open(CACHE_BASEMAP);
  const hit = await basemap.match(PMTILES_REL);
  const msg = { type: 'offline-pack-status', ready: !!hit, version: BASEMAP_VERSION };
  if (client && client.postMessage) client.postMessage(msg);
  else await broadcast(msg);
}

async function broadcast(msg) {
  const clients = await self.clients.matchAll({ includeUncontrolled: true });
  for (const c of clients) c.postMessage(msg);
}

// ---------------------------------------------------------------------------
// Fetch: same-origin GET only. Everything else falls through to the network.
// ---------------------------------------------------------------------------
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;  // never touch cross-origin

  const scopePath = new URL(self.registration.scope).pathname;  // e.g. /Fire_Varna/
  const rel = url.pathname.startsWith(scopePath)
    ? url.pathname.slice(scopePath.length)
    : url.pathname.replace(/^\/+/, '');

  // App-shell navigations: network-first, cached index.html fallback (offline).
  if (req.mode === 'navigate') {
    event.respondWith(navigationHandler(req));
    return;
  }

  // PMTiles: Range-aware slice from the cached full file, else pass Range to network.
  if (rel === PMTILES_REL || url.pathname.endsWith('/varna_basemap.pmtiles')) {
    event.respondWith(pmtilesHandler(req, url));
    return;
  }

  // Mutating data: network-first with cache fallback (addendum Поправка 1).
  if (MUTATING_DATA.has(rel)) {
    event.respondWith(networkFirst(req, CACHE_OFFLINE_PACK));
    return;
  }

  // Versioned basemap assets + pinned vendor deps: cache-first.
  if (rel.startsWith('data/basemaps/' + BASEMAP_VERSION + '/') || rel.startsWith('vendor/basemap/')) {
    event.respondWith(cacheFirst(req, CACHE_BASEMAP));
    return;
  }

  // Anything else same-origin (approx_addresses, other app assets): do not intercept.
});

async function navigationHandler(req) {
  try {
    return await fetch(req);
  } catch (e) {
    const core = await caches.open(CACHE_CORE);
    const cached = await core.match('index.html', { ignoreSearch: true });
    if (cached) return cached;
    throw e;
  }
}

async function networkFirst(req, cacheName) {
  try {
    const res = await fetch(req);
    if (res && res.ok) {
      try { const c = await caches.open(cacheName); await c.put(req, res.clone()); } catch (e) { /* quota: ignore */ }
    }
    return res;
  } catch (e) {
    const c = await caches.open(cacheName);
    const hit = await c.match(req, { ignoreSearch: true });
    if (hit) return hit;
    throw e;
  }
}

async function cacheFirst(req, cacheName) {
  const c = await caches.open(cacheName);
  const hit = await c.match(req, { ignoreSearch: true });
  if (hit) return hit;
  const res = await fetch(req);
  if (res && res.ok) {
    try { await c.put(req, res.clone()); } catch (e) { /* quota: ignore */ }
  }
  return res;
}

// Slice a cached full PMTiles response into a 206 for a Range request.
async function pmtilesHandler(req, url) {
  const cache = await caches.open(CACHE_BASEMAP);
  const cached = await cache.match(url.pathname, { ignoreSearch: true });
  const range = req.headers.get('range');
  if (!cached) return fetch(req);          // not cached: pass through unchanged
  if (!range) return cached;               // no Range: return full cached file
  const buf = await cached.arrayBuffer();
  const total = buf.byteLength;
  const m = /^bytes=(\d*)-(\d*)$/.exec(range.trim());
  if (!m) return cached;                    // unparseable Range: return full file
  let start, end;
  if (m[1] === '' && m[2] !== '') {         // suffix: bytes=-N (last N bytes)
    const n = parseInt(m[2], 10);
    start = Math.max(0, total - n);
    end = total - 1;
  } else {
    start = parseInt(m[1], 10);
    end = m[2] === '' ? total - 1 : Math.min(parseInt(m[2], 10), total - 1);
  }
  if (isNaN(start) || start > end || start >= total) {
    return new Response(null, {
      status: 416,
      headers: { 'Content-Range': 'bytes */' + total, 'Accept-Ranges': 'bytes' },
    });
  }
  const slice = buf.slice(start, end + 1);
  const ct = cached.headers.get('content-type') || 'application/octet-stream';
  return new Response(slice, {
    status: 206,
    statusText: 'Partial Content',
    headers: {
      'Content-Type': ct,
      'Content-Length': String(slice.byteLength),
      'Content-Range': 'bytes ' + start + '-' + end + '/' + total,
      'Accept-Ranges': 'bytes',
    },
  });
}
