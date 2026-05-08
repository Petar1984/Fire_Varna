// Headless browser verify — load the merged HTML in Chromium, confirm
// the app initializes without JS errors and the meta line shows "6070 точки".
// Uses a local http.server so the page is served over http://localhost:PORT
// (matches the deploy origin model; file:// would suppress some CORS / fetch
// errors that we want to surface).

const path = require('path');
const fs = require('fs');
const http = require('http');

const REPO_ROOT = path.join(__dirname, '..');
const TARGET = 'hydrants_varna_merged.html';

(async () => {
  // 1) Tiny static server
  const server = http.createServer((req, res) => {
    let p = decodeURIComponent((req.url || '/').split('?')[0]);
    if (p === '/' || p === '') p = '/' + TARGET;
    const file = path.join(REPO_ROOT, p.replace(/^\/+/, ''));
    if (!file.startsWith(REPO_ROOT)) { res.statusCode = 403; res.end(); return; }
    fs.readFile(file, (err, data) => {
      if (err) { res.statusCode = 404; res.end(); return; }
      const ct = file.endsWith('.html') ? 'text/html; charset=utf-8' : 'application/octet-stream';
      res.setHeader('Content-Type', ct);
      res.end(data);
    });
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const url = 'http://127.0.0.1:' + port + '/' + TARGET;
  console.log('[INFO] serving on', url);

  // 2) Launch headless Chromium
  let chromium;
  try { chromium = require('playwright').chromium; }
  catch (e) {
    console.error('[FAIL] playwright not loadable:', e.message);
    server.close();
    process.exit(1);
  }
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 375, height: 740 },
    permissions: [],  // do NOT grant geolocation
  });
  const page = await context.newPage();

  const errors = [];
  const warnings = [];
  page.on('pageerror', err => errors.push(String(err)));
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push('[console.error] ' + msg.text());
    if (msg.type() === 'warning') warnings.push('[console.warn] ' + msg.text());
  });
  page.on('requestfailed', req => {
    // ignore tile / external 3rd-party failures, surface only same-origin
    const u = req.url();
    if (u.startsWith('http://127.0.0.1') || u.startsWith('http://localhost')) {
      errors.push('[reqfail same-origin] ' + u + ' :: ' + req.failure().errorText);
    }
  });

  await page.goto(url, { waitUntil: 'load', timeout: 20000 });
  await page.waitForTimeout(800);  // let init run

  const meta = await page.locator('#meta').textContent();
  console.log('[INFO] #meta =', JSON.stringify(meta));
  if (meta && meta.indexOf('6070') !== -1) console.log('[OK] meta shows 6070');
  else { console.error('[FAIL] meta does not show 6070'); process.exitCode = 1; }

  // probe global function existence inside the IIFE — they're not exposed.
  // Instead poke DOM elements created by the new feature.
  const addBtn = await page.locator('#addHydrantBtn').count();
  console.log('[INFO] addHydrantBtn count =', addBtn);
  if (addBtn !== 1) { console.error('[FAIL] addHydrantBtn missing'); process.exitCode = 1; }
  const placeBanner = await page.locator('#placementBanner').count();
  if (placeBanner !== 1) { console.error('[FAIL] placementBanner missing'); process.exitCode = 1; }
  const placeActions = await page.locator('#placementActions').count();
  if (placeActions !== 1) { console.error('[FAIL] placementActions missing'); process.exitCode = 1; }

  // open type picker by simulating cardReport click without GPS — the card is
  // empty until first GPS lock, so directly use HYDRANTS_BY_ID via debug eval.
  // Instead, just confirm modal opens via a test hook: simulate a popup click.
  // Easiest: dispatch a click on the hidden modalBackdrop close button to make
  // sure no exception is thrown.
  await page.evaluate(() => {
    const bd = document.getElementById('modalBackdrop');
    bd.classList.add('show');
    document.getElementById('modalClose').click();
    return bd.classList.contains('show');
  });

  if (errors.length === 0) {
    console.log('[OK] no runtime JS errors');
  } else {
    console.error('[FAIL] runtime errors:');
    for (const e of errors) console.error('  -', e);
    process.exitCode = 1;
  }
  if (warnings.length) {
    console.log('[INFO] warnings:');
    for (const w of warnings) console.log('  -', w);
  }

  await browser.close();
  server.close();
  console.log('Done.');
})().catch(err => {
  console.error('[FATAL]', err);
  process.exit(1);
});
