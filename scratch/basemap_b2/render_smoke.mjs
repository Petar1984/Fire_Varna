// B2 headless render smoke (de-risks the custom-schema protomaps adapter).
// Requires the globally-installed playwright + system Chrome. Serves via the running
// http-server (Range-capable) on :8000. Writes render_smoke_report.json.
import { createRequire } from 'node:module';
import { writeFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/Petar/AppData/Roaming/npm/node_modules/playwright');

const BASE = 'http://127.0.0.1:8000/Fire_Varna/scratch/basemap_b2/render_probe.html';
const CASES = [
  { name: 'z13_default', q: 'bm_lat=43.2141&bm_lng=27.9147&bm_z=13' },
  { name: 'ff001_z17', q: 'bm_lat=43.204393&bm_lng=27.896573&bm_z=17' },
  { name: 'venchan_z17', q: 'bm_lat=43.250046&bm_lng=27.985170&bm_z=17' },
];

const isCdn = (u) => /unpkg\.com|jsdelivr|cdnjs|cloudflare/i.test(u);
const isBasemapDep = (u) => /pmtiles|protomaps/i.test(u);

const report = { base: BASE, cases: [], ok: false };

const browser = await chromium.launch({ channel: 'chrome', headless: true });
try {
  for (const c of CASES) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 780 }, deviceScaleFactor: 2 });
    const page = await ctx.newPage();
    const requests = [];
    const rangeStatuses = [];
    const consoleErrors = [];
    page.on('request', (r) => requests.push(r.url()));
    page.on('response', (res) => {
      const u = res.url();
      if (u.endsWith('.pmtiles')) {
        const reqHeaders = res.request().headers();
        rangeStatuses.push({ url: u, status: res.status(), hadRange: !!reqHeaders['range'] });
      }
    });
    page.on('console', (m) => { if (m.type() === 'error') consoleErrors.push(m.text()); });
    page.on('pageerror', (e) => consoleErrors.push('pageerror: ' + e.message));

    await page.goto(`${BASE}?${c.q}`, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForFunction('window.__probe && window.__probe.ready === true', { timeout: 30000 }).catch(() => {});
    const hist = await page.evaluate('window.__probe && window.__probe.sample ? window.__probe.sample() : null');
    const probeErrors = await page.evaluate('window.__probe ? window.__probe.errors : ["no __probe"]');

    const cdnBasemapReqs = requests.filter((u) => isCdn(u) && isBasemapDep(u));
    const vendorReqs = requests.filter((u) => /\/vendor\/basemap\//.test(u));
    const pmtiles206 = rangeStatuses.filter((r) => r.status === 206 || r.status === 200);

    report.cases.push({
      name: c.name,
      histogram: hist,
      probeErrors,
      consoleErrors,
      vendorSameOriginReqs: vendorReqs,
      cdnBasemapReqs,
      pmtilesResponses: rangeStatuses,
      pmtilesServedOk: pmtiles206.length > 0,
    });
    await ctx.close();
  }

  // Verdict: no CDN basemap deps anywhere; vendored deps loaded same-origin; pmtiles served;
  // z13 renders background+roads (roads prove custom-schema adapter works at initial zoom);
  // ff001/venchan render roads AND labels (labels prove LineLabelSymbolizer + name field).
  const z13 = report.cases.find((x) => x.name === 'z13_default');
  const ff = report.cases.find((x) => x.name === 'ff001_z17');
  const ven = report.cases.find((x) => x.name === 'venchan_z17');
  const noCdn = report.cases.every((x) => x.cdnBasemapReqs.length === 0);
  const vendored = report.cases.every((x) => x.vendorSameOriginReqs.length >= 2);
  const served = report.cases.every((x) => x.pmtilesServedOk);
  const noErrors = report.cases.every((x) => x.consoleErrors.length === 0 && (x.probeErrors || []).length === 0);
  const z13Roads = z13 && z13.histogram && z13.histogram.road > 50 && z13.histogram.background > 100;
  const ffRoadsLabels = ff && ff.histogram && ff.histogram.road > 50 && ff.histogram.label > 20;
  const venRoadsLabels = ven && ven.histogram && ven.histogram.road > 50 && ven.histogram.label > 20;

  report.checks = { noCdn, vendored, served, noErrors, z13Roads, ffRoadsLabels, venRoadsLabels };
  report.ok = noCdn && vendored && served && noErrors && z13Roads && ffRoadsLabels && venRoadsLabels;
} finally {
  await browser.close();
}

writeFileSync('C:/git/Fire_Varna/scratch/basemap_b2/render_smoke_report.json', JSON.stringify(report, null, 2));
console.log(JSON.stringify(report.checks, null, 2));
console.log('render_smoke ok =', report.ok);
process.exit(report.ok ? 0 : 1);
