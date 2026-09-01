// B2 full-index.html headless smoke. Validates: (A) flag-false inertness (no basemap
// deps / pmtiles / sw.js requested, no SW registered, no console errors, OSM default,
// hydrants load); (B) flag-on: SW registers, opening the selector + choosing the offline
// basemap loads vendored deps SAME-ORIGIN (no CDN), renders PMTiles canvases below the
// overlays, no console errors. Requires global playwright + system Chrome + running
// http-server on :8000. Writes index_smoke_report.json.
import { createRequire } from 'node:module';
import { writeFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/Petar/AppData/Roaming/npm/node_modules/playwright');

const APP = 'http://127.0.0.1:8000/Fire_Varna/';
const VERSION = 'osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b';
const isBasemapDepCdn = (u) => /(unpkg\.com|jsdelivr|cdnjs)/i.test(u) && /pmtiles|protomaps/i.test(u);

const report = { app: APP, ok: false };
const browser = await chromium.launch({ channel: 'chrome', headless: true });

async function trackers(page, reqs, errs) {
  // Serve /favicon.ico so Chrome's automatic favicon request is not a spurious 404
  // (index.html ships no icon link — pre-existing, unrelated to B2).
  await page.route('**/favicon.ico', (r) => r.fulfill({ status: 200, body: '' }));
  page.on('request', (r) => reqs.push(r.url()));
  page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
  page.on('pageerror', (e) => errs.push('pageerror: ' + e.message));
}

try {
  // ---------- Case A: flag-false inertness ----------
  {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 2 });
    const page = await ctx.newPage();
    const reqs = [], errs = [];
    await trackers(page, reqs, errs);
    await page.goto(`${APP}?basemap_pmtiles=0`, { waitUntil: 'networkidle', timeout: 40000 });
    await page.waitForTimeout(1500);
    const swRegs = await page.evaluate(async () => {
      if (!('serviceWorker' in navigator)) return 0;
      const r = await navigator.serviceWorker.getRegistrations();
      return r.length;
    });
    const hydrantPins = await page.evaluate(() => document.querySelectorAll('.h-pin, .h-pin-wrapper').length);
    const bad = reqs.filter((u) => /\/vendor\/basemap\//.test(u) || /\.pmtiles(\?|$)/.test(u)
      || new RegExp('/data/basemaps/' + VERSION + '/').test(u) || /\/sw\.js(\?|$)/.test(u));
    report.caseA = {
      swRegistrations: swRegs,
      hydrantPins,
      hydrantsFetched: reqs.some((u) => /\/data\/hydrants\.json/.test(u)),
      forbiddenRequests: bad,
      consoleErrors: errs,
    };
    await ctx.close();
  }

  // ---------- Case B: flag-on select offline ----------
  {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 2 });
    const page = await ctx.newPage();
    const reqs = [], errs = [];
    await trackers(page, reqs, errs);
    await page.goto(`${APP}?basemap_pmtiles=1&bm_lat=43.204393&bm_lng=27.896573&bm_z=17`,
      { waitUntil: 'networkidle', timeout: 40000 });
    await page.waitForTimeout(1200);
    const swRegd = await page.evaluate(async () => {
      const r = await navigator.serviceWorker.getRegistrations();
      return r.length > 0;
    });
    // Before selecting offline: OSM default ⇒ no pmtiles yet.
    const pmtilesBeforeSelect = reqs.some((u) => /\.pmtiles(\?|$)/.test(u));
    // Open selector + choose the offline option.
    await page.click('#basemapToggle');
    await page.waitForSelector('.basemap-selector', { timeout: 5000 });
    const optCount = await page.evaluate(() => document.querySelectorAll('.basemap-opt').length);
    await page.evaluate(() => {
      const opt = [...document.querySelectorAll('.basemap-opt')].find((b) => /офлайн/i.test(b.textContent));
      if (opt) opt.click();
    });
    // Wait for the basemap pane to paint canvases.
    await page.waitForFunction(() => {
      const p = document.querySelector('[class*="offlineBasemap"]');
      return p && p.querySelectorAll('canvas').length > 0;
    }, { timeout: 20000 }).catch(() => {});
    await page.waitForTimeout(1500);

    const paneInfo = await page.evaluate(() => {
      const bm = document.querySelector('[class*="offlineBasemap"]');
      const mk = document.querySelector('.leaflet-marker-pane');
      const ov = document.querySelector('.leaflet-overlay-pane');
      const tp = document.querySelector('.leaflet-tile-pane'); // building overlay lives here
      const zi = (el) => el ? parseInt(getComputedStyle(el).zIndex || '0', 10) : null;
      return {
        basemapCanvases: bm ? bm.querySelectorAll('canvas').length : 0,
        basemapZ: zi(bm), markerZ: zi(mk), overlayZ: zi(ov), tileZ: zi(tp),
      };
    });
    const vendorReqs = reqs.filter((u) => /\/vendor\/basemap\//.test(u));
    const cdnBad = reqs.filter(isBasemapDepCdn);
    const pmtilesReqs = reqs.filter((u) => /\.pmtiles(\?|$)/.test(u));

    report.caseB = {
      swRegistered: swRegd,
      selectorOptions: optCount,
      pmtilesBeforeSelect,
      vendorSameOriginReqs: vendorReqs.length,
      cdnBasemapReqs: cdnBad,
      pmtilesRequested: pmtilesReqs.length > 0,
      pane: paneInfo,
      overlaysAboveBasemap: paneInfo.basemapZ !== null && paneInfo.markerZ > paneInfo.basemapZ
        && paneInfo.overlayZ > paneInfo.basemapZ && paneInfo.tileZ > paneInfo.basemapZ,
      consoleErrors: errs,
    };
    await ctx.close();
  }

  const A = report.caseA, B = report.caseB;
  report.checks = {
    A_noSW: A.swRegistrations === 0,
    A_inert: A.forbiddenRequests.length === 0,
    A_hydrants: A.hydrantsFetched,
    A_noErrors: A.consoleErrors.length === 0,
    B_swRegistered: B.swRegistered === true,
    B_selector3: B.selectorOptions === 3,
    B_osmDefault: B.pmtilesBeforeSelect === false,
    B_vendored: B.vendorSameOriginReqs >= 2,
    B_noCdn: B.cdnBasemapReqs.length === 0,
    B_rendered: B.pane.basemapCanvases > 0,
    B_overlaysAbove: B.overlaysAboveBasemap === true,
    B_noErrors: B.consoleErrors.length === 0,
  };
  report.ok = Object.values(report.checks).every(Boolean);
} finally {
  await browser.close();
}

writeFileSync('C:/git/Fire_Varna/scratch/basemap_b2/index_smoke_report.json', JSON.stringify(report, null, 2));
console.log(JSON.stringify(report.checks, null, 2));
console.log('index_smoke ok =', report.ok);
process.exit(report.ok ? 0 : 1);
