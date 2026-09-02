// Fire_Varna · CDP probe for the ADDRESS search — G3 corpus + G6 first-load
// request list (plan docs/plans/places_search_plan_2026-09-02.md §5 G3/G6).
//
// Why it exists: the places (hotels) branch of C4 must not move a single byte of
// the address search. "Not moved" is only provable against a recording of what
// the address search does TODAY, so this probe records the full DOM sequence of
// #addrSearchResults for a fixed corpus, plus the backing identity of every
// visible row (popup/panel title, nav hrefs = the coordinate, the /detail/ URL,
// the pin rectangle). before.json (this lot, on HEAD) must equal after.json
// (C4, with the places branch in) byte for byte.
//
// Run:
//   node scratch/places_search/probe_places_fv.mjs --mode before
//   node scratch/places_search/probe_places_fv.mjs --mode after [--mob]
//   optional: --out <basename>   (default: the mode; used for the ×2 determinism run)
//
// It brings its OWN world up and takes it down again:
//   * python -m http.server 8000 --directory <repo>   (spawned, killed by PID)
//   * headless Chrome on a FRESH profile scratch/places_search/_cprof, killed by
//     PID only (never `taskkill /IM chrome.exe` — that would kill Petar's browser)
//
// Determinism (the gate is "two runs, byte-identical output"):
//   * no clock anywhere in the JSON — no Date, no durations; the MutationObserver
//     stamps a monotonic sequence number, not a timestamp;
//   * no fixed sleeps as waits: waitFor() polls a JS expression every 50 ms and
//     "settled" means 500 ms with no in-flight page request AND no new mutation
//     of #addrSearchResults;
//   * pin rectangles are read only once the map is still (same full-precision
//     rect and same map-pane transform three samples running, no Leaflet
//     animation class), and only then rounded to whole pixels;
//   * geolocation is denied up front (Browser.grantPermissions with an empty
//     list). Headless Chrome has no position provider, so the only question is
//     WHEN it fails; denying makes that instant and identical every run;
//   * "network activity" for the settle rule counts only page-relevant requests
//     (same-origin http://localhost:8000/… and the Worker's /detail/…). The
//     15 s issue poll and the OSM tiles never gate a settle — they are background
//     traffic that would otherwise make every wait a lottery — and in the G6 list
//     they appear as a set of HOSTS only (see runG6);
//   * held-request snapshots are collapsed to the sequence of DISTINCT states, so
//     the array length does not depend on how many polls fitted in the hold;
//   * the building-detail response is released only once the map's fly-to has
//     come to rest. Measured 02.09 on HEAD: selectResult starts an animated
//     setView, and renderDetailSheet then calls positionPinForSheet ->
//     positionPinInBand -> map.panTo, whose offset Leaflet truncates to whole
//     pixels against the map pane's CURRENT position. Fired mid-animation, that
//     truncation lands 1-2 px apart from run to run (5 of 76 pin rectangles
//     disagreed across two runs, every one of them on the async sheet path).
//     Holding the response until the pane is still makes the second pan start
//     from rest, and the resting position is then the same every time. It is the
//     app's own arithmetic that is timing-sensitive here, not the probe's
//     reading — the probe only removes the race from the recording.
//
// Console errors are collected from the PAGE's own reporting only
// (Runtime.exceptionThrown + console.error), not from browser-level network
// noise: the gate is "the app threw nothing", not "the satellite link was up".
import { spawn, spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

// --- paths and options ------------------------------------------------------
const HERE = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(HERE, "..", "..");
const OUT_DIR = path.join(HERE, "probe_out");
const PROFILE = path.join(HERE, "_cprof");
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const CDP_PORT = "9334";
const HTTP_PORT = "8000";
const BASE = `http://localhost:${HTTP_PORT}/`;
const PAGE_URL = BASE + "index.html";

function argOf(name, fallback) {
  const i = process.argv.indexOf(name);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}
const MODE = argOf("--mode", "");
const OUT_NAME = argOf("--out", MODE);
const MOB = process.argv.includes("--mob");
if (MODE !== "before" && MODE !== "after") {
  console.error("usage: node probe_places_fv.mjs --mode before|after [--mob] [--out name]");
  process.exit(2);
}

// --- the corpus (plan §5 G3; identical in --mode before and --mode after) ----
const G3_QUERIES = [
  "бл. 402 вх. 3",
  "макгахан 15",
  "макгахан 153",
  "кв владиславово бл 402",
  "бл. 402",
  "чайка",
  "виница",
  "43.2100, 27.9100",
  "ьььь",
];
// The query the single-scenario cases drive with. It is in the corpus above, so
// the two recordings can be read against each other.
const SCENARIO_QUERY = "бл. 402";

const MAX_CLICKS = 10;      // the dropdown itself caps at RESULT_LIMIT = 10
const POLL_MS = 50;
const SETTLE_QUIET_MS = 500;
const HOLD_MS = 3000;       // the deliberate hold of search_index.json (§5 G3)
const W = MOB ? 375 : 1400;
const H = MOB ? 812 : 900;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const isDetailUrl = (url) => /\/details?\//.test(url);
const warnings = [];
function warn(msg) { warnings.push(msg); console.log("  ! " + msg); }

// --- child processes we own -------------------------------------------------
let chrome = null;
let server = null;
let serverWasOurs = false;

function killByPid(proc, tag) {
  if (!proc || proc.killed) return;
  // BY PID ONLY, with the child tree. `taskkill /IM chrome.exe` would take
  // Petar's own browser down with it.
  try { spawnSync("taskkill", ["/PID", String(proc.pid), "/T", "/F"], { stdio: "ignore" }); }
  catch (e) { warn(`не можах да спра ${tag} (pid ${proc.pid})`); }
}

function wipeProfile(tag) {
  for (let i = 0; i < 12; i++) {
    try { fs.rmSync(PROFILE, { recursive: true, force: true }); return true; }
    catch (e) { spawnSync("cmd", ["/c", "timeout", "/t", "1"], { stdio: "ignore" }); }
  }
  warn(`профилът не се изтри (${tag})`);
  return false;
}

async function bye(code) {
  killByPid(chrome, "chrome");
  chrome = null;
  await sleep(1200);
  wipeProfile("край");
  if (serverWasOurs) killByPid(server, "http.server");
  process.exit(code);
}

// --- the local static server ------------------------------------------------
async function serverServesOurRepo() {
  try {
    const r = await fetch(PAGE_URL, { method: "HEAD" });
    if (!r.ok) return false;
    const len = Number(r.headers.get("content-length"));
    return len === fs.statSync(path.join(REPO, "index.html")).size;
  } catch (e) { return false; }
}

async function startServer() {
  if (await serverServesOurRepo()) {
    console.log(`  порт ${HTTP_PORT} вече сервира това репо — ползвам го, не го спирам`);
    return;
  }
  server = spawn("python", ["-m", "http.server", HTTP_PORT, "--directory", REPO],
                 { detached: false, stdio: "ignore" });
  serverWasOurs = true;
  for (let i = 0; i < 80; i++) {
    await sleep(250);
    if (await serverServesOurRepo()) { console.log(`  http.server на ${HTTP_PORT} вдигнат`); return; }
  }
  console.error(`ПАДА: http.server не вдигна на порт ${HTTP_PORT}`);
  await bye(2);
}

// --- the browser session ----------------------------------------------------
async function startChrome() {
  wipeProfile("старт");
  chrome = spawn(CHROME, [
    "--headless=new", "--disable-gpu", "--enable-unsafe-swiftshader",
    `--remote-debugging-port=${CDP_PORT}`, `--user-data-dir=${PROFILE}`,
    "--no-first-run", "--no-default-browser-check",
    `--window-size=${W},${H}`, "about:blank",
  ], { detached: false, stdio: "ignore" });
  for (let i = 0; i < 60; i++) {
    await sleep(250);
    try {
      const v = await (await fetch(`http://127.0.0.1:${CDP_PORT}/json/version`)).json();
      console.log(`  Chrome: ${v.Browser}`);
      return;
    } catch (e) { /* not up yet */ }
  }
  console.error(`ПАДА: свежият Chrome не вдигна порта ${CDP_PORT}`);
  await bye(2);
}

// One tab, one WebSocket, and all the bookkeeping the waits need.
async function openSession() {
  const mk = await (await fetch(
    `http://127.0.0.1:${CDP_PORT}/json/new?about:blank`, { method: "PUT" })).json();
  const ws = new WebSocket(mk.webSocketDebuggerUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

  const s = {
    errs: [],                 // page-level errors only (gate: empty)
    reqUrl: new Map(),        // requestId -> url (every request)
    status: new Map(),        // requestId -> status (or "failed:…")
    inflight: new Set(),      // requestIds of page-relevant requests still open
    lastNetAt: Date.now(),    // internal only; never written to JSON
    recordNet: false,         // the G6 window (navigate -> first focus)
    g6: [],                   // {requestId, url} STARTED inside that window
    finished: new Set(),      // urls that reached loadingFinished
    detailSeen: [],           // detail URLs seen since the last reset
    onPaused: null,           // Fetch.requestPaused hook
    indexMode: "pass",        // search_index.json: "pass" | "hold" | "fail"
    heldIndexId: null,        // the request id being held in "hold" mode
    indexFailed: false,       // set once an index request was failed in "fail" mode
  };

  // The building-detail request has two shapes: the Worker's /detail/{g} in
  // production and the local static details/buildings/v1/{g}.json on localhost
  // (index.html detailUrlFor). Both carry the same backing identity `g`.
  const isRelevant = (url) => url.startsWith(BASE) || isDetailUrl(url);

  let id = 0;
  const waiting = new Map();
  ws.onmessage = (m) => {
    const d = JSON.parse(m.data);
    if (d.id && waiting.has(d.id)) { waiting.get(d.id)(d); waiting.delete(d.id); }
    const p = d.params || {};
    switch (d.method) {
      case "Runtime.exceptionThrown":
        s.errs.push(p.exceptionDetails?.exception?.description || p.exceptionDetails?.text || "?");
        break;
      case "Runtime.consoleAPICalled":
        if (p.type === "error")
          s.errs.push((p.args || []).map((a) => a.value ?? a.description).join(" "));
        break;
      case "Network.requestWillBeSent": {
        const url = p.request?.url || "";
        s.reqUrl.set(p.requestId, url);
        if (isDetailUrl(url)) s.detailSeen.push(url);
        if (s.recordNet) s.g6.push({ requestId: p.requestId, url });
        if (isRelevant(url)) { s.inflight.add(p.requestId); s.lastNetAt = Date.now(); }
        break;
      }
      case "Network.responseReceived":
        s.status.set(p.requestId, p.response?.status ?? null);
        break;
      case "Network.loadingFinished": {
        const url = s.reqUrl.get(p.requestId);
        if (url) s.finished.add(url);
        if (s.inflight.delete(p.requestId)) s.lastNetAt = Date.now();
        break;
      }
      case "Network.loadingFailed": {
        s.status.set(p.requestId, "failed:" + (p.errorText || "?"));
        if (s.inflight.delete(p.requestId)) s.lastNetAt = Date.now();
        break;
      }
      case "Fetch.requestPaused":
        if (s.onPaused) s.onPaused(p);
        break;
      default: break;
    }
  };

  s.send = (method, params = {}) => new Promise((res) => {
    const i = ++id; waiting.set(i, res);
    ws.send(JSON.stringify({ id: i, method, params }));
  });
  s.ev = async (expression) => {
    const r = await s.send("Runtime.evaluate",
      { expression, awaitPromise: true, returnByValue: true });
    if (r.result?.exceptionDetails)
      throw new Error("Runtime.evaluate: " + JSON.stringify(r.result.exceptionDetails).slice(0, 300));
    return r.result?.result?.value;
  };

  await s.send("Runtime.enable");
  await s.send("Page.enable");
  await s.send("Network.enable");
  // Measured 02.09 on Chrome 152 headless: without these two, element.focus()
  // sets document.activeElement but fires NO focus event, because the tab never
  // holds system focus. The app lazy-loads search_index.json ON FOCUS, so the
  // whole first-focus half of the baseline would have been recorded against a
  // page that was never focused (the index would arrive on the first keystroke
  // instead, and Fetch could never pause a request that was not made).
  await s.send("Emulation.setFocusEmulationEnabled", { enabled: true });
  await s.send("Page.bringToFront");
  // ONE interception for the whole session: the scenarios switch s.indexMode
  // instead of enabling/disabling the domain, and the building detail is always
  // released at map rest (see the header).
  s.onPaused = async (p) => {
    const url = p.request?.url || "";
    try {
      if (url.includes("search_index.json")) {
        if (s.indexMode === "fail") {
          s.indexFailed = true;
          await s.send("Fetch.failRequest", { requestId: p.requestId, errorReason: "Failed" });
          return;
        }
        if (s.indexMode === "hold" && s.heldIndexId === null) {
          s.heldIndexId = p.requestId;     // released by the scenario itself
          return;
        }
        await s.send("Fetch.continueRequest", { requestId: p.requestId });
        return;
      }
      await waitMapStill(s);
      await s.send("Fetch.continueRequest", { requestId: p.requestId });
    } catch (e) { warn("Fetch.requestPaused: " + e); }
  };
  await s.send("Fetch.enable", { patterns: [
    { urlPattern: "*search_index.json*", requestStage: "Request" },
    { urlPattern: "*/details/*", requestStage: "Request" },
    { urlPattern: "*/detail/*", requestStage: "Request" },
  ] });
  await s.send("Emulation.setTouchEmulationEnabled", { enabled: MOB, maxTouchPoints: MOB ? 5 : 0 });
  await s.send("Emulation.setDeviceMetricsOverride",
               { width: W, height: H, deviceScaleFactor: MOB ? 2 : 1, mobile: MOB });
  // Deny everything for the page's origin — geolocation above all. See the header.
  await s.send("Browser.grantPermissions", { origin: BASE.replace(/\/$/, ""), permissions: [] });
  return s;
}

// --- waits (no fixed sleeps; 50 ms steps) -----------------------------------
async function waitFor(s, expression, timeoutMs = 20000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    let v = false;
    try { v = await s.ev(expression); } catch (e) { v = false; }
    if (v) return true;
    await sleep(POLL_MS);
  }
  warn(`waitFor изтече: ${expression.slice(0, 90)}`);
  return false;
}

async function waitNode(fn, timeoutMs = 20000, label = "") {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (fn()) return true;
    await sleep(POLL_MS);
  }
  warn(`waitNode изтече: ${label}`);
  return false;
}

// settled = SETTLE_QUIET_MS with no page-relevant request in flight and no new
// mutation of #addrSearchResults.
async function waitSettled(s, timeoutMs = 30000) {
  const deadline = Date.now() + timeoutMs;
  let lastSeq = -1;
  let quietSince = Date.now();
  while (Date.now() < deadline) {
    let seq = -1;
    try { seq = await s.ev("window.__probeSeq === undefined ? -1 : window.__probeSeq"); }
    catch (e) { seq = lastSeq; }
    const busy = s.inflight.size > 0;
    if (seq !== lastSeq || busy || Date.now() - s.lastNetAt < SETTLE_QUIET_MS) {
      lastSeq = seq;
      quietSince = Date.now();
    } else if (Date.now() - quietSince >= SETTLE_QUIET_MS) {
      return true;
    }
    await sleep(POLL_MS);
  }
  warn("waitSettled изтече");
  return false;
}

// True once the Leaflet map pane has held the same transform for three samples
// running and no pan/zoom animation class is on the page.
async function waitMapStill(s, timeoutMs = 15000) {
  const deadline = Date.now() + timeoutMs;
  let prev = null;
  let agree = 0;
  while (Date.now() < deadline) {
    let cur;
    try { cur = await s.ev(MAP_STILL_JS); } catch (e) { cur = { animating: true, transform: "" }; }
    const key = cur.animating ? null : cur.transform;
    if (key !== null && key === prev) { if (++agree >= 2) return true; } else { agree = 0; }
    prev = key;
    await sleep(POLL_MS);
  }
  warn("картата не се успокои");
  return false;
}

// --- page-side snippets -----------------------------------------------------
const MAP_STILL_JS = `(function () {
  var pane = document.querySelector('.leaflet-map-pane');
  return {
    animating: !!document.querySelector('.leaflet-pan-anim') ||
               !!document.querySelector('.leaflet-zoom-anim'),
    transform: pane ? pane.style.transform : ''
  };
})()`;

const OBSERVER_JS = `(function () {
  if (window.__probeObs) { try { window.__probeObs.disconnect(); } catch (e) {} }
  var el = document.getElementById('addrSearchResults');
  window.__probeLog = [];
  window.__probeSeq = 0;
  window.__probeObs = new MutationObserver(function () {
    window.__probeSeq++;
    if (window.__probeLog.length < 50) {
      window.__probeLog.push({ t: window.__probeSeq, html: el.outerHTML });
    }
  });
  window.__probeObs.observe(el, { childList: true, subtree: true, attributes: true, characterData: true });
  return true;
})()`;

const RESET_LOG_JS = "window.__probeLog = []; window.__probeSeq = 0; true";
const RESULTS_HTML_JS = "document.getElementById('addrSearchResults').outerHTML";
const RESULTS_VISIBLE_JS = "document.getElementById('addrSearchResults').classList.contains('visible')";
const INPUT_VALUE_JS = "document.getElementById('addrSearchInput').value";
const FOCUS_JS = "document.getElementById('addrSearchInput').focus(); true";

const ROWS_JS = `(function () {
  var el = document.getElementById('addrSearchResults');
  if (!el.classList.contains('visible')) return [];
  var out = [];
  var items = el.querySelectorAll('.asr-item');
  for (var i = 0; i < items.length; i++) {
    var it = items[i];
    var chip = it.querySelector('.asr-kind');
    var meta = it.querySelector('.asr-meta');
    out.push({
      idx: it.dataset.idx === undefined ? null : it.dataset.idx,
      text: it.textContent,
      chip: chip ? chip.textContent : null,
      meta: meta ? meta.textContent : null
    });
  }
  return out;
})()`;

const SURFACE_READY_JS =
  "!!document.querySelector('.search-popup') || " +
  "!!document.querySelector('#detailSheet:not([hidden])') || " +
  "!!document.querySelector('.leaflet-popup')";

const CAPTURE_JS = `(function () {
  var sheet = document.querySelector('#detailSheet:not([hidden])');
  var popup = document.querySelector('.search-popup');
  var leaflet = document.querySelector('.leaflet-popup');
  var scope = sheet || popup || leaflet || null;
  var surface = sheet ? 'sheet' : (popup ? 'popup' : (leaflet ? 'leaflet-popup' : 'none'));
  var titleEl = sheet ? sheet.querySelector('.ds-title')
                      : (scope ? scope.querySelector('.sp-title') : null);
  var hrefs = [];
  if (scope) {
    var links = scope.querySelectorAll('.nav-actions a');
    for (var i = 0; i < links.length; i++) hrefs.push(links[i].getAttribute('href'));
  }
  return { surface: surface, title: titleEl ? titleEl.textContent : null, navHrefs: hrefs };
})()`;

const PIN_RECT_JS = `(function () {
  var e = document.querySelector('.search-pin-wrapper');
  if (!e) return null;
  var r = e.getBoundingClientRect();
  return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
})()`;

// Full precision plus the map pane's own transform and Leaflet's animation
// classes: the stillness test must not be fooled by a pan whose last frames move
// less than half a pixel (measured 02.09 — two runs disagreed by 2 px on exactly
// one sample, and only where the pan started after the network had gone quiet).
const PIN_RECT_RAW_JS = `(function () {
  var pane = document.querySelector('.leaflet-map-pane');
  var animating = !!document.querySelector('.leaflet-pan-anim') ||
                  !!document.querySelector('.leaflet-zoom-anim');
  var e = document.querySelector('.search-pin-wrapper');
  return {
    animating: animating,
    transform: pane ? pane.style.transform : '',
    rect: e ? (function (r) { return { x: r.x, y: r.y, w: r.width, h: r.height }; })(e.getBoundingClientRect()) : null
  };
})()`;

const NO_PIN_JS = "!document.querySelector('.search-pin-wrapper')";

const READY_JS =
  "!!window.L && !!document.querySelector('.leaflet-container') && " +
  "!!document.getElementById('addrSearchInput')";

// --- page driving -----------------------------------------------------------
async function navigateFresh(s, label) {
  console.log(`  -> навигация (${label})`);
  s.finished.delete(BASE + "data/hydrants.json");
  await s.send("Page.navigate", { url: PAGE_URL });
  await waitFor(s, READY_JS, 60000);
  await waitNode(() => s.finished.has(BASE + "data/hydrants.json"), 60000, "hydrants.json");
  await waitSettled(s, 60000);
  await s.ev(OBSERVER_JS);
}

async function focusInput(s) { await s.ev(FOCUS_JS); }

async function clearField(s) {
  await focusInput(s);
  // select-all + delete through the input pipeline (the app listens to `input`)
  await s.send("Input.dispatchKeyEvent", {
    type: "rawKeyDown", key: "a", code: "KeyA", windowsVirtualKeyCode: 65,
    nativeVirtualKeyCode: 65, modifiers: 2, commands: ["selectAll"],
  });
  await s.send("Input.dispatchKeyEvent", {
    type: "keyUp", key: "a", code: "KeyA", windowsVirtualKeyCode: 65,
    nativeVirtualKeyCode: 65, modifiers: 2,
  });
  await pressKey(s, "Delete", 46);
  // Fallback for the case the edit command did not take: backspace it empty.
  for (let i = 0; i < 60; i++) {
    if (!(await s.ev(INPUT_VALUE_JS))) break;
    await pressKey(s, "Backspace", 8);
  }
  await waitFor(s, `!(${RESULTS_VISIBLE_JS})`, 15000);
}

async function pressKey(s, key, vk) {
  await s.send("Input.dispatchKeyEvent", {
    type: "rawKeyDown", key, code: key, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk,
  });
  await s.send("Input.dispatchKeyEvent", {
    type: "keyUp", key, code: key, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk,
  });
}

async function typeQuery(s, q) {
  await focusInput(s);
  await s.ev(RESET_LOG_JS);
  await s.send("Input.insertText", { text: q });
  const typed = await s.ev(INPUT_VALUE_JS);
  if (typed !== q) warn(`полето носи "${typed}" вместо "${q}"`);
  await waitSettled(s);
}

async function pressEscape(s) {
  await focusInput(s);
  await pressKey(s, "Escape", 27);
  await waitFor(s, NO_PIN_JS, 15000);
  await waitSettled(s);
}

// Reads the pin rectangle only once the map is demonstrably still: three
// consecutive samples with the SAME full-precision rect and the same map-pane
// transform, and no Leaflet pan/zoom animation class in sight. Rounded to whole
// pixels only on the way out.
async function stablePinRect(s, timeoutMs = 20000) {
  const deadline = Date.now() + timeoutMs;
  let prev = null;
  let agree = 0;
  while (Date.now() < deadline) {
    const cur = await s.ev(PIN_RECT_RAW_JS);
    const key = cur.animating ? null : JSON.stringify([cur.transform, cur.rect]);
    if (key !== null && key === prev) {
      if (++agree >= 2) {
        if (!cur.rect) return null;
        return { x: Math.round(cur.rect.x), y: Math.round(cur.rect.y),
                 w: Math.round(cur.rect.w), h: Math.round(cur.rect.h) };
      }
    } else { agree = 0; }
    prev = key;
    await sleep(POLL_MS);
  }
  warn("pinRect не се успокои");
  return await s.ev(PIN_RECT_JS);
}

async function clickRowAndCapture(s, idx) {
  s.detailSeen.length = 0;
  const clicked = await s.ev(
    `(function () { var e = document.querySelector('#addrSearchResults .asr-item[data-idx="${idx}"]');` +
    ` if (!e) return false; e.click(); return true; })()`);
  const surfaceAppeared = await waitFor(s, SURFACE_READY_JS, 25000);
  await waitSettled(s, 30000);
  const cap = await s.ev(CAPTURE_JS);
  const pinRect = await stablePinRect(s);
  return {
    idx: String(idx),
    clicked: !!clicked,
    surfaceAppeared,
    surface: cap.surface,
    title: cap.title,
    navHrefs: cap.navHrefs,
    detailUrl: s.detailSeen.length ? s.detailSeen[0] : null,
    pinRect,
  };
}

// --- G3: the address corpus -------------------------------------------------
async function runG3(s, label) {
  console.log(`  == G3 (${label}) ==`);
  const out = [];
  for (const q of G3_QUERIES) {
    await clearField(s);
    await typeQuery(s, q);
    const log = await s.ev("window.__probeLog");
    const rows = await s.ev(ROWS_JS);
    const rec = {
      query: q,
      intermediate: (log && log.length) ? log[0].html : null,
      settled: await s.ev(RESULTS_HTML_JS),
      rows,
      clicks: [],
    };
    const n = Math.min(rows.length, MAX_CLICKS);
    console.log(`     "${q}" · редове: ${rows.length} · кликове: ${n}`);
    for (let i = 0; i < n; i++) {
      if (i > 0) { await clearField(s); await typeQuery(s, q); }
      rec.clicks.push(await clickRowAndCapture(s, rows[i].idx));
      await pressEscape(s);
    }
    out.push(rec);
  }
  await clearField(s);
  return out;
}

// --- G6: the first-load request list ----------------------------------------
// The window opens before Page.navigate and is closed by the caller immediately
// before the first focus of the search box, which is what the gate is about:
// hotels.json / place_categories.json must be absent from this list in
// --mode after too (they are fetched on focus, never on first load).
//
// Two lists, for one measured reason. The page's own requests (same-origin +
// the Worker's /detail/) are deterministic: navigateFresh does not return until
// they are quiet, so URL *and* status are settled. Third-party traffic (OSM
// raster tiles, the 15 s issue poll) is not: how many tile responses land inside
// the window is a stopwatch question, and their statuses depend on a satellite
// link. Those are therefore reduced to the SET OF HOSTS the first load talks to
// -- the part a leak would change -- with no counts and no statuses.
function runG6(s) {
  const seen = new Set();
  const page = [];
  const hosts = new Set();
  for (const r of s.g6) {
    if (!(r.url.startsWith(BASE) || isDetailUrl(r.url))) {
      try { hosts.add(new URL(r.url).host); } catch (e) { hosts.add("?"); }
      continue;
    }
    const status = s.status.has(r.requestId) ? s.status.get(r.requestId) : null;
    const key = r.url + " | " + status;
    if (seen.has(key)) continue;
    seen.add(key);
    page.push({ url: r.url, status });
  }
  page.sort((a, b) => (a.url === b.url
    ? String(a.status).localeCompare(String(b.status))
    : a.url.localeCompare(b.url)));
  return {
    window: "Page.navigate -> first focus of #addrSearchInput",
    page,
    thirdPartyHosts: [...hosts].sort(),
  };
}

// --- G4: the intuitive-query gate — lands with the branch itself, in C4 ------
async function runG4(s) {
  // TODO(C4): the places corpus of §3 М5 + §10 А8 + §13 (hotel-first /
  // address-first, the orange .place-pin, the popup rows, the re-anchored
  // hydrants, П7) is written here, together with the branch it measures. It is
  // deliberately empty in C4-pre: this lot records the address search BEFORE a
  // single line of index.html changes, so there is nothing of ours to assert.
  return null;
}

// --- the single-behaviour scenarios ----------------------------------------
// Collapse a polled series of snapshots to the sequence of DISTINCT states, so
// the record does not depend on how many polls fitted into the window.
function distinct(series) {
  const out = [];
  for (const v of series) if (!out.length || out[out.length - 1] !== v) out.push(v);
  return out;
}

async function scenarioHeldIndex(s) {
  await navigateFresh(s, "held-index");
  s.heldIndexId = null;
  s.indexMode = "hold";                 // the first index request waits for us
  await focusInput(s);
  const paused = await waitNode(() => s.heldIndexId !== null, 25000, "search_index.json paused");
  await s.ev(RESET_LOG_JS);
  await s.send("Input.insertText", { text: SCENARIO_QUERY });
  const held = [];
  const until = Date.now() + HOLD_MS;   // the hold IS the scenario, not a wait
  while (Date.now() < until) {
    held.push(await s.ev(RESULTS_HTML_JS));
    await sleep(POLL_MS * 4);
  }
  s.indexMode = "pass";
  if (paused) await s.send("Fetch.continueRequest", { requestId: s.heldIndexId });
  s.heldIndexId = null;
  await waitSettled(s, 60000);
  const rec = {
    query: SCENARIO_QUERY,
    indexHeld: paused,
    duringHold: distinct(held),
    settled: await s.ev(RESULTS_HTML_JS),
    rows: await s.ev(ROWS_JS),
  };
  await clearField(s);
  return rec;
}

async function scenarioOfflineIndex(s) {
  // Warm profile by construction (the cold pass already filled the Cache API
  // namespace fire-varna-search-v2), so this measures the offline fallback.
  // EVERY index request fails, not just the first: ensureSearchData clears its
  // in-flight promise on failure, so a later keystroke asks again.
  await navigateFresh(s, "offline-index");
  s.indexFailed = false;
  s.indexMode = "fail";
  await focusInput(s);
  const blocked = await waitNode(() => s.indexFailed, 25000, "search_index.json failed");
  await s.ev(RESET_LOG_JS);
  await s.send("Input.insertText", { text: SCENARIO_QUERY });
  await waitSettled(s, 60000);
  const rec = {
    query: SCENARIO_QUERY,
    indexRequestFailed: blocked,
    settled: await s.ev(RESULTS_HTML_JS),
    rows: await s.ev(ROWS_JS),
  };
  s.indexMode = "pass";
  await clearField(s);
  return rec;
}

async function scenarioEnterBeforeFetch(s) {
  // Fresh navigation => the in-memory index is empty and the 11 MB payload is
  // still being fetched/prepared when Enter arrives.
  await navigateFresh(s, "enter-before-fetch");
  await focusInput(s);
  await s.ev(RESET_LOG_JS);
  await s.send("Input.insertText", { text: SCENARIO_QUERY });
  await pressKey(s, "Enter", 13);
  await waitSettled(s, 90000);
  const cap = await s.ev(CAPTURE_JS);
  const rec = {
    query: SCENARIO_QUERY,
    settled: await s.ev(RESULTS_HTML_JS),
    rows: await s.ev(ROWS_JS),
    surface: cap.surface,
    title: cap.title,
    navHrefs: cap.navHrefs,
    pinRect: await stablePinRect(s),
  };
  await pressEscape(s);
  await clearField(s);
  return rec;
}

async function scenarioOutsideClick(s) {
  await navigateFresh(s, "outside-click");
  await clearField(s);
  await typeQuery(s, SCENARIO_QUERY);
  const before = {
    visible: await s.ev(RESULTS_VISIBLE_JS),
    html: await s.ev(RESULTS_HTML_JS),
  };
  const pt = await s.ev(`(function () {
    var r = document.querySelector('.leaflet-container').getBoundingClientRect();
    return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
  })()`);
  await s.send("Input.dispatchMouseEvent",
    { type: "mousePressed", x: pt.x, y: pt.y, button: "left", clickCount: 1 });
  await s.send("Input.dispatchMouseEvent",
    { type: "mouseReleased", x: pt.x, y: pt.y, button: "left", clickCount: 1 });
  await waitSettled(s, 30000);
  const rec = {
    query: SCENARIO_QUERY,
    clickPoint: pt,
    visibleBefore: before.visible,
    htmlBefore: before.html,
    visibleAfter: await s.ev(RESULTS_VISIBLE_JS),
    htmlAfter: await s.ev(RESULTS_HTML_JS),
    leafletPopupAfter: await s.ev("!!document.querySelector('.leaflet-popup')"),
  };
  await clearField(s);
  return rec;
}

async function scenarioEmptyField(s) {
  await navigateFresh(s, "empty-field");
  await clearField(s);
  await typeQuery(s, SCENARIO_QUERY);
  const rows = await s.ev(ROWS_JS);
  let clicked = null;
  if (rows.length) clicked = await clickRowAndCapture(s, rows[0].idx);
  const pinBefore = await s.ev(PIN_RECT_JS);
  await clearField(s);
  await waitSettled(s, 30000);
  const rec = {
    query: SCENARIO_QUERY,
    selected: clicked,
    pinBeforeClear: pinBefore,
    visibleAfterClear: await s.ev(RESULTS_VISIBLE_JS),
    htmlAfterClear: await s.ev(RESULTS_HTML_JS),
    pinAfterClear: await s.ev(PIN_RECT_JS),
  };
  return rec;
}

// --- main -------------------------------------------------------------------
async function main() {
  console.log(`=== ПРОБА: адресната търсачка · режим ${MODE} · ${W}×${H}${MOB ? " (мобилен)" : ""} ===`);
  fs.mkdirSync(OUT_DIR, { recursive: true });
  await startServer();
  await startChrome();
  const s = await openSession();

  // G6 window: everything from Page.navigate to the first focus of the box.
  s.recordNet = true;
  await navigateFresh(s, "cold");
  const requests = runG6(s);
  s.recordNet = false;

  const scenarios = {};
  scenarios.cold = { profileWarm: false, g3: await runG3(s, "cold") };

  await navigateFresh(s, "warm");
  scenarios.warm = { profileWarm: true, g3: await runG3(s, "warm") };

  scenarios.heldIndex = await scenarioHeldIndex(s);
  scenarios.offlineIndex = await scenarioOfflineIndex(s);
  scenarios.enterBeforeFetch = await scenarioEnterBeforeFetch(s);
  scenarios.outsideClick = await scenarioOutsideClick(s);
  scenarios.emptyField = await scenarioEmptyField(s);

  const out = {
    mode: MODE,
    viewport: { width: W, height: H, mobile: MOB },
    pageUrl: PAGE_URL,
    corpus: G3_QUERIES,
    scenarios,
    errs: s.errs,
  };

  const mainPath = path.join(OUT_DIR, `${OUT_NAME}.json`);
  const reqPath = path.join(OUT_DIR, `${OUT_NAME}_requests.json`);
  fs.writeFileSync(mainPath, JSON.stringify(out, null, 2) + "\n");
  fs.writeFileSync(reqPath, JSON.stringify(requests, null, 2) + "\n");
  console.log(`  записах ${mainPath} (${fs.statSync(mainPath).size} B)`);
  console.log(`  записах ${reqPath} (${fs.statSync(reqPath).size} B, ` +
              `${requests.page.length} заявки на страницата, ${requests.thirdPartyHosts.length} чужди хоста)`);

  if (MODE === "after") {
    const g4 = await runG4(s);
    const g4Path = path.join(OUT_DIR, `${OUT_NAME}_g4.json`);
    fs.writeFileSync(g4Path, JSON.stringify(g4, null, 2) + "\n");
    console.log(`  записах ${g4Path} (кука за C4)`);
  }

  console.log(`  конзолни грешки: ${s.errs.length}`);
  if (s.errs.length) for (const e of s.errs) console.log(`     ${String(e).slice(0, 200)}`);
  console.log(`  предупреждения на пробата: ${warnings.length}`);
  await bye(s.errs.length ? 1 : 0);
}

process.on("unhandledRejection", async (e) => {
  console.error("ПАДА (unhandledRejection): " + (e && e.stack ? e.stack : e));
  await bye(2);
});
main().catch(async (e) => {
  console.error("ПАДА: " + (e && e.stack ? e.stack : e));
  await bye(2);
});
