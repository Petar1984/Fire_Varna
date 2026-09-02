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
import crypto from "node:crypto";
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
    warns: [],                // console.warn - the places branch funnels EVERY caught
                              // exception into warnOnce(), so a silent ReferenceError
                              // shows up here and nowhere else (measured 03.09).
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
        else if (p.type === "warning")
          s.warns.push((p.args || []).map((a) => a.value ?? a.description).join(" "));
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

// --- G4: the places (hotels) branch — plan §3 М5 + §10 А8 + §12 В8 + G12б/в/г
// Lands with the branch it measures (C4). Everything here reads OUR container
// (#placesSearchResults), OUR marker (.place-pin-wrapper) and OUR export
// (window.__places); the G3 corpus above is untouched by construction.
const REF_ROWS = JSON.parse(fs.readFileSync(path.join(HERE, "recall_sweep_rows.json"), "utf8"));
// The placeTokens contract, repeated verbatim from tests/test_places_search_primitives.py
// (EXPECTATIONS). checkTokenTable() also counts the rows over there, so a row added
// to the test without being added here is loud rather than silent.
const CYR_I_UPPER = "І";
const TOKEN_TABLE = [
  ["VII СУ „Найден Геров“", ["7", "su", "naiden", "gerov"]],
  ["седмо су", ["7", "su"]],
  ["7-мо су", ["7", "su"]],
  [CYR_I_UPPER + " ОУ „Свети княз Борис I“", ["1", "ou", "sveti", "kniaz", "boris", "1"]],
  ["св. марина", ["sveti", "marina"]],
  ["д-р иванов", ["doktor", "ivanov"]],
  ["БОНИТА/BONITA", ["bonita", "bonita"]],
  ["х-л романтика", ["hotel", "romantika"]],
  ["ДКЦ 2", ["dkts", "2"]],
  ["II ДКЦ", ["2", "dkts"]],
  ["Зл.котва", ["zl", "kotva"]],
  ["Иглика-2", ["iglika", "2"]],
  ["ХОТЕЛ  ХЕЛИОС СПА", ["hotel", "helios", "spa"]],
  ["Св.Николай", ["sveti", "nikolai"]],
  ["Св.св.Кирил", ["sveti", "sveti", "kiril"]],
  ["Др Хараламбиев", ["doktor", "haralambiev"]],
  ["апартхотел", ["apart", "hotel"]],
  ["апарткомплекс", ["apart", "kompleks"]],
];

const PLACES_CACHE = "fire-varna-hotels-v2-226";
const HOTELS_URL = BASE + "data/hotels.json";

const PL_VISIBLE_JS = "document.getElementById('placesSearchResults').classList.contains('visible')";
const PL_ROWS_JS = `(function () {
  var box = document.getElementById('placesSearchResults');
  var rows = [], items = box.querySelectorAll('.pl-item');
  for (var i = 0; i < items.length; i++) {
    var it = items[i];
    rows.push({ idx: it.dataset.idx, kind: (it.querySelector('.pl-kind') || {}).textContent || null,
                title: (it.querySelector('.pl-title') || {}).textContent || null,
                meta: (it.querySelector('.pl-meta') || {}).textContent || null,
                height: Math.round(it.getBoundingClientRect().height) });
  }
  var more = box.querySelector('.pl-more');
  var head = box.querySelector('.pl-group-header');
  var heads = [], hn = box.querySelectorAll('.pl-group-header');
  for (var j = 0; j < hn.length; j++) heads.push(hn[j].textContent);
  var mores = [], mn = box.querySelectorAll('.pl-more');
  for (var k = 0; k < mn.length; k++) mores.push(mn[k].textContent);
  var r = box.getBoundingClientRect();
  return { visible: box.classList.contains('visible'), header: head ? head.textContent : null,
           headers: heads, mores: mores,
           rows: rows, more: more ? more.textContent : null,
           rect: { top: Math.round(r.top), bottom: Math.round(r.bottom), height: Math.round(r.height) },
           innerHeight: window.innerHeight };
})()`;

// Phase 2 (plan sec.16 J2 / phase-2 plan D4 + Sol C1): WHO stands on top. Read off
// the two containers themselves, never off a class name; `theirStyle` is the whole
// inline attribute, so a leftover style="" would be visible here.
const GEOM_JS = `(function () {
  var mine = document.getElementById('placesSearchResults');
  var theirs = document.getElementById('addrSearchResults');
  var m = mine.getBoundingClientRect(), t = theirs.getBoundingClientRect();
  return {
    mineVisible: mine.classList.contains('visible'),
    theirVisible: theirs.classList.contains('visible'),
    mineTop: Math.round(m.top), mineBottom: Math.round(m.bottom),
    theirTop: Math.round(t.top), theirBottom: Math.round(t.bottom),
    mineFirst: m.top < t.top,
    theirStyle: theirs.getAttribute('style'),
    mineStyleTop: mine.style.top || '',
    innerHeight: window.innerHeight,
    mineFits: m.bottom <= window.innerHeight + 1,
    theirFits: t.bottom <= window.innerHeight + 1,
    theirScrollable: theirs.scrollHeight > theirs.clientHeight + 1,
    theirRows: theirs.querySelectorAll('.asr-item').length,
    headers: (function () { var h = mine.querySelectorAll('.pl-group-header'), o = [];
      for (var i = 0; i < h.length; i++) o.push(h[i].textContent); return o; })(),
    chips: (function () { var h = mine.querySelectorAll('.pl-kind'), o = [];
      for (var i = 0; i < h.length; i++) o.push(h[i].textContent); return o; })()
  };
})()`;

// Sol C5: the clicks of the phase-2 scenarios are REAL mouse events at real
// coordinates, not element.click() - a pin under an overlay must fail loudly.
const HYDRANT_RECT_JS = `(function () {
  var pop = document.querySelector('.leaflet-popup');
  var pr = pop ? pop.getBoundingClientRect() : null;
  var pins = document.querySelectorAll('.h-pin-wrapper');
  for (var i = 0; i < pins.length; i++) {
    var r = pins[i].getBoundingClientRect();
    if (r.width < 1 || r.top < 0 || r.left < 0) continue;
    if (r.bottom > window.innerHeight || r.right > window.innerWidth) continue;
    // the pin must not sit under the open popup, or the click lands on the popup
    if (pr && r.left < pr.right && r.right > pr.left && r.top < pr.bottom && r.bottom > pr.top) continue;
    return { x: Math.round(r.left + r.width / 2), y: Math.round(r.top + r.height / 2), of: pins.length };
  }
  return null;
})()`;
const CLOSE_BTN_RECT_JS = `(function () {
  var b = document.querySelector('.leaflet-popup-close-button');
  if (!b) return null;
  var r = b.getBoundingClientRect();
  return { x: Math.round(r.left + r.width / 2), y: Math.round(r.top + r.height / 2) };
})()`;
const PLACE_SURFACE_JS = `(function () {
  var pins = document.querySelectorAll('.place-pin-wrapper');
  var pop = document.querySelector('.place-popup');
  var hrefs = [];
  if (pop) { var a = pop.querySelectorAll('.nav-actions a'); for (var i = 0; i < a.length; i++) hrefs.push(a[i].getAttribute('href')); }
  var sheet = document.getElementById('detailSheet');
  return {
    pins: pins.length,
    popups: document.querySelectorAll('.place-popup').length,
    title: pop ? (pop.querySelector('.pp-title') || {}).textContent || null : null,
    sub: pop ? (pop.querySelector('.pp-sub') || {}).textContent || null : null,
    old: pop ? ((pop.querySelector('.pp-old') || {}).textContent || null) : null,
    src: pop ? (pop.querySelector('.pp-src') || {}).textContent || null : null,
    navHrefs: hrefs,
    theirPins: document.querySelectorAll('.search-pin-wrapper').length,
    sheetHidden: sheet ? !!sheet.hidden : null,
    theirVisible: document.getElementById('addrSearchResults').classList.contains('visible'),
    theirHtml: document.getElementById('addrSearchResults').outerHTML,
    legendOpen: (function () { var l = document.getElementById('legend'); return l ? !l.hidden : null; })()
  };
})()`;
// The ranked hydrant pins ARE the "Топ 5" list — the mode renders numbered pins, not
// an HTML list. Their positions + rank badges are what re-anchoring visibly changes.
const HYDRANT_PINS_JS = `(function () {
  var out = [], pins = document.querySelectorAll('.h-pin-wrapper');
  for (var i = 0; i < pins.length; i++) {
    var b = pins[i].querySelector('.h-rank');
    out.push((pins[i].style.transform || '') + '|' + (b ? b.textContent : ''));
  }
  out.sort();
  return out;
})()`;

async function placesReady(s, timeoutMs = 30000) {
  await focusInput(s);
  const ok = await waitFor(s, "!!window.__places", timeoutMs);
  if (!ok) return false;
  try { await s.ev("window.__places.ensure().then(function () { return true; }).catch(function () { return false; })"); }
  catch (e) { return false; }
  return await s.ev("window.__places.tokens('хотел').length > 0 && window.__places.search('хотел').rows.length > 0");
}

// Our own dropdown answers on the same 120 ms debounce as theirs; waitSettled only
// watches THEIR container, so give ours its own (bounded) wait as well.
async function typePlaces(s, q) {
  await clearField(s);
  await typeQuery(s, q);
  await waitFor(s, `${PL_VISIBLE_JS} || document.getElementById('addrSearchResults').classList.contains('visible')`, 8000);
  await sleep(POLL_MS * 4);
  return await s.ev(PL_ROWS_JS);
}

// One interception for hotels.json on top of the session's own (search_index /
// detail) handling: the original hook is kept and delegated to.
async function armPlacesFetch(s) {
  if (s.placesArmed) return;
  s.placesArmed = true;
  s.hotelsMode = "pass";           // pass | hold | 404 | malformed
  s.places2Mode = "pass";          // pass | 404  (phase 2: the SECOND payload)
  s.heldHotelsId = null;
  const prev = s.onPaused;
  s.onPaused = async (p) => {
    const url = p.request?.url || "";
    // Sol C3: one refusal must not take the others down, so each payload can be
    // refused on its own - hotels without places and places without hotels.
    if (url.includes("/places.json")) {
      try {
        if (s.places2Mode === "404") {
          await s.send("Fetch.fulfillRequest", { requestId: p.requestId, responseCode: 404, body: "" });
          return;
        }
        await s.send("Fetch.continueRequest", { requestId: p.requestId });
      } catch (e) { warn("places.json Fetch: " + e); }
      return;
    }
    if (!url.includes("hotels.json")) return prev(p);
    try {
      if (s.hotelsMode === "404") {
        await s.send("Fetch.fulfillRequest", { requestId: p.requestId, responseCode: 404, body: "" });
        return;
      }
      if (s.hotelsMode === "malformed") {
        await s.send("Fetch.fulfillRequest", { requestId: p.requestId, responseCode: 200,
          responseHeaders: [{ name: "Content-Type", value: "application/json" }],
          body: Buffer.from('{"_meta":{"count":226},"hotels":[', "utf8").toString("base64") });
        return;
      }
      if (s.hotelsMode === "hold" && s.heldHotelsId === null) { s.heldHotelsId = p.requestId; return; }
      await s.send("Fetch.continueRequest", { requestId: p.requestId });
    } catch (e) { warn("hotels.json Fetch: " + e); }
  };
  await s.send("Fetch.enable", { patterns: [
    { urlPattern: "*search_index.json*", requestStage: "Request" },
    { urlPattern: "*hotels.json*", requestStage: "Request" },
    { urlPattern: "*/places.json*", requestStage: "Request" },
    { urlPattern: "*/details/*", requestStage: "Request" },
    { urlPattern: "*/detail/*", requestStage: "Request" },
  ] });
}

const dropPlacesCache = (s) =>
  s.ev(`caches.delete('${PLACES_CACHE}').then(function (v) { return v; }).catch(function () { return null; })`);
const placesCacheHas = (s) =>
  s.ev(`caches.open('${PLACES_CACHE}').then(function (c) { return c.match('${HOTELS_URL}'); })` +
       `.then(function (h) { return !!h; }).catch(function () { return null; })`);

async function checkTokenTable(s) {
  const rows = [];
  for (const [q, expected] of TOKEN_TABLE) {
    const got = await s.ev(`JSON.stringify(window.__places.tokens(${JSON.stringify(q)}))`);
    rows.push({ q, expected, got: JSON.parse(got), ok: got === JSON.stringify(expected) });
  }
  // the same table must still be the one the unit test carries
  const py = fs.readFileSync(path.join(REPO, "tests", "test_places_search_primitives.py"), "utf8");
  const block = py.slice(py.indexOf("EXPECTATIONS = ("), py.indexOf("class VerbatimPrimitivesTest"));
  const inTest = (block.match(/^ {4}\(/gm) || []).length;
  return { rows, passed: rows.filter((r) => r.ok).length, total: rows.length, rowsInTest: inTest };
}

// G12в — the 46 reference queries, row by row, against recall_sweep_rows.json.
// Order-sensitive first: the distance tie-break reads map.getCenter(), and the
// sweep stood in for it with the map's own opening centre [43.2141, 27.9147]. If
// the ordered comparison holds, the browser sat on that centre; only if it does
// not do we fall back to comparing the SETS and say so.
async function checkReferenceRows(s) {
  const out = { mode: "ordered", queries: [], passedOrdered: 0, passedSets: 0, total: 0, rows: 0 };
  for (const bucket of ["gate_m5_a8", "extra"]) {
    for (const rec of REF_ROWS[bucket]) {
      const got = JSON.parse(await s.ev(
        `JSON.stringify((function (r) { return { category: r.category, rows: r.rows.map(function (x) { return x.name + ' · ' + x.zone; }) }; })(window.__places.search(${JSON.stringify(rec.q)})))`));
      const want = rec.rows.map((r) => r.name + " · " + r.zone);
      const ordered = JSON.stringify(got.rows) === JSON.stringify(want);
      const sets = JSON.stringify([...got.rows].sort()) === JSON.stringify([...want].sort());
      out.total++;
      out.rows += want.length;
      if (ordered) out.passedOrdered++;
      if (sets) out.passedSets++;
      const first = got.rows.findIndex((v, i) => v !== want[i]);
      out.queries.push({ q: rec.q, expect: rec.expect, bucket, category: got.category,
                         n: got.rows.length, refN: want.length, ordered, sets,
                         first3: got.rows.slice(0, 3), refFirst3: want.slice(0, 3),
                         firstDiffAt: ordered ? null : first,
                         diffOurs: ordered ? null : got.rows.slice(Math.max(0, first), first + 2),
                         diffRef: ordered ? null : want.slice(Math.max(0, first), first + 2) });
    }
  }
  if (out.passedOrdered < out.total && out.passedSets === out.total) out.mode = "sets";
  return out;
}

// §3 М5 / §10 А8 — the same 46 queries as a human sees them: how many rows and
// which first three, read from OUR DOM (top 8) as well as from the export.
async function checkM5Table(s) {
  const out = [];
  for (const bucket of ["gate_m5_a8", "extra"]) {
    for (const rec of REF_ROWS[bucket]) {
      const js = JSON.parse(await s.ev(
        `JSON.stringify((function (r) { return { n: r.rows.length, category: r.category, first3: r.rows.slice(0, 3).map(function (x) { return x.name + ' · ' + x.zone; }) }; })(window.__places.search(${JSON.stringify(rec.q)})))`));
      const dom = await typePlaces(s, rec.q);
      out.push({ q: rec.q, expect: rec.expect, jsN: js.n, refN: rec.rows.length, category: js.category,
                 jsFirst3: js.first3, domVisible: dom.visible, domHeader: dom.header,
                 domRows: dom.rows.length, domMore: dom.more,
                 domFirst3: dom.rows.slice(0, 3).map((r) => r.title + " | " + r.meta),
                 ok: js.n === rec.rows.length });
    }
  }
  await clearField(s);
  return out;
}

// A click on our first row: orange pin, popup with all its lines, the hydrant
// ranking re-anchored around the place, and Escape taking all of it away again.
async function checkPickAndEscape(s, q) {
  const before = await s.ev(HYDRANT_PINS_JS);
  const list = await typePlaces(s, q);
  const clicked = await s.ev(
    "(function () { var e = document.querySelector('#placesSearchResults .pl-item[data-idx=\"0\"]');" +
    " if (!e) return false; e.click(); return true; })()");
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await waitMapStill(s);
  await waitSettled(s, 30000);
  const after = await s.ev(HYDRANT_PINS_JS);
  const surface = await s.ev(PLACE_SURFACE_JS);
  const field = await s.ev(INPUT_VALUE_JS);
  await focusInput(s);
  await pressKey(s, "Escape", 27);
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length === 0", 15000);
  await waitSettled(s, 20000);
  const afterEscape = await s.ev(PLACE_SURFACE_JS);
  const plAfter = await s.ev(PL_ROWS_JS);
  await clearField(s);
  return {
    query: q, rowsShown: list.rows.length, firstRow: list.rows[0] || null, clicked: !!clicked,
    fieldAfterPick: field, surface,
    hydrantsBefore: before.length, hydrantsAfter: after.length,
    hydrantsChanged: JSON.stringify(before) !== JSON.stringify(after),
    afterEscape: { pins: afterEscape.pins, popups: afterEscape.popups, listVisible: plAfter.visible },
  };
}

// П7 (§12 В3) — their building panel arrives 3 s late, after we have already put
// our place on the map. The panel must not land on top of our selection.
async function checkLateDetailSheet(s) {
  await navigateFresh(s, "П7 late /detail/");
  if (!(await placesReady(s))) return { ready: false };
  s.holdDetail = true;
  const prev = s.onPaused;
  s.onPaused = async (p) => {
    const url = p.request?.url || "";
    if (s.holdDetail && isDetailUrl(url)) {
      setTimeout(() => { s.send("Fetch.continueRequest", { requestId: p.requestId }).catch(() => {}); }, HOLD_MS);
      return;
    }
    return prev(p);
  };
  await clearField(s);
  await typeQuery(s, "бл. 402 вх. 3");
  const theirRows = await s.ev(ROWS_JS);
  if (theirRows.length)
    await s.ev(`(function () { var e = document.querySelector('#addrSearchResults .asr-item[data-idx="${theirRows[0].idx}"]');` +
               " if (e) e.click(); return !!e; })()");
  const mine = await typePlaces(s, "хотел адмирал");
  await s.ev("(function () { var e = document.querySelector('#placesSearchResults .pl-item[data-idx=\"0\"]'); if (e) e.click(); return !!e; })()");
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await sleep(HOLD_MS + 1500);                 // outlive the held response by a second
  await waitSettled(s, 30000);
  const surface = await s.ev(PLACE_SURFACE_JS);
  s.holdDetail = false;
  s.onPaused = prev;
  await pressEscape(s);
  await clearField(s);
  return { ready: true, theirRows: theirRows.length, mineRows: mine.rows.length,
           sheetHidden: surface.sheetHidden, pins: surface.pins, popups: surface.popups,
           title: surface.title, theirPins: surface.theirPins };
}

// The four refusals of the payload (Д2/Д3/В7). Our cache namespace is emptied
// first, so "no answer" means the network answer, not a warm copy.
async function checkRefusals(s) {
  const out = {};
  const scenario = async (name, mode, prep) => {
    await navigateFresh(s, "refusal " + name);
    await dropPlacesCache(s);
    if (prep) await prep();
    s.hotelsMode = mode;
    const errsBefore = s.errs.length;
    const rows = await (async () => {
      await focusInput(s);
      await sleep(1500);
      return await typePlaces(s, "хотел адмирал");
    })();
    out[name] = { rows: rows.rows.length, visible: rows.visible,
                  hasExport: await s.ev("!!window.__places"),
                  searchRows: await s.ev("window.__places ? window.__places.search('хотел адмирал').rows.length : null"),
                  // C3: the OTHER payload must still be in the index
                  placesRows: await s.ev("window.__places ? window.__places.search('училище').rows.length : null"),
                  cacheEntry: await placesCacheHas(s),
                  consoleErrors: s.errs.length - errsBefore };
    s.hotelsMode = "pass";
    await clearField(s);
  };
  await scenario("notFound", "404");
  await scenario("malformed", "malformed");
  // C3, the mirror image: places.json refused, the hotels stay whole.
  await navigateFresh(s, "refusal places404");
  await dropPlacesCache(s);
  s.places2Mode = "404";
  const errsBeforeP = s.errs.length;
  const hotelsOnly = await (async () => { await focusInput(s); await sleep(1500);
                                          return await typePlaces(s, "хотел адмирал"); })();
  out.places404 = { rows: hotelsOnly.rows.length,
                    searchRows: await s.ev("window.__places ? window.__places.search('хотел адмирал').rows.length : null"),
                    placesRows: await s.ev("window.__places ? window.__places.search('училище').rows.length : null"),
                    consoleErrors: s.errs.length - errsBeforeP };
  s.places2Mode = "pass";
  await clearField(s);
  // Held body: our AbortController must give up at 8 s and the branch must stay
  // quiet. The request is released afterwards so the session is left clean.
  await navigateFresh(s, "refusal held-body");
  await dropPlacesCache(s);
  s.heldHotelsId = null;
  s.hotelsMode = "hold";
  const errsBefore = s.errs.length;
  await focusInput(s);
  const paused = await waitNode(() => s.heldHotelsId !== null, 25000, "hotels.json paused");
  await sleep(10000);                          // past the 8 s abort, well short of 20 s
  const held = await typePlaces(s, "хотел адмирал");
  out.heldBody = { paused, rows: held.rows.length,
                   searchRows: await s.ev("window.__places ? window.__places.search('хотел адмирал').rows.length : null"),
                   consoleErrors: s.errs.length - errsBefore };
  s.hotelsMode = "pass";
  if (paused) { try { await s.send("Fetch.continueRequest", { requestId: s.heldHotelsId }); } catch (e) {} }
  s.heldHotelsId = null;
  await clearField(s);
  // A STALE cache (the old 144-record contract) plus a 404 from the network: the
  // stale copy must not pass validation. Plan §12 В7: it is IGNORED, not deleted.
  await scenario("staleCache", "404", async () => {
    const body = JSON.stringify({ _meta: { count: 144, licence: "x" },
                                  hotels: Array.from({ length: 144 }, (_, i) => ({ name: "X" + i })) });
    await s.ev(`caches.open('${PLACES_CACHE}').then(function (c) {` +
               ` return c.put('${HOTELS_URL}', new Response(${JSON.stringify(body)},` +
               ` { headers: { 'Content-Type': 'application/json' } })); }).then(function () { return true; })`);
  });
  return out;
}

// Who wins the race: their index held 3 s (hotel-first) and ours held 3 s
// (address-first). The address rows for "адмирал" must be the same four either way.
async function checkRaces(s) {
  const out = {};
  // hotel-first: THEIR index is held for 3 s (the plan's number, and inside our own
  // 8 s budget), so our rows are what the human sees first.
  await navigateFresh(s, "hotel-first");
  s.heldIndexId = null;
  s.indexMode = "hold";
  await focusInput(s);
  const pausedIdx = await waitNode(() => s.heldIndexId !== null, 25000, "search_index.json paused");
  await s.ev(RESET_LOG_JS);
  await s.send("Input.insertText", { text: "адмирал" });
  await sleep(HOLD_MS);
  const mineHold = await s.ev(PL_ROWS_JS);
  out.hotelFirst = { indexHeld: pausedIdx, mineRows: mineHold.rows.length,
                     mineTitles: mineHold.rows.map((r) => r.title),
                     theirVisibleDuringHold: await s.ev(RESULTS_VISIBLE_JS) };
  s.indexMode = "pass";
  if (pausedIdx) await s.send("Fetch.continueRequest", { requestId: s.heldIndexId });
  s.heldIndexId = null;
  await waitSettled(s, 60000);
  out.hotelFirst.settledTheirRows = await s.ev(ROWS_JS);
  out.hotelFirst.settledMine = (await s.ev(PL_ROWS_JS)).rows.map((r) => r.title);
  await clearField(s);

  // address-first: OUR payload is held for 3 s. Their four "Адмирал Грейг" rows must
  // be exactly the four they always are, and ours must arrive under them afterwards.
  await navigateFresh(s, "address-first");
  await dropPlacesCache(s);
  s.heldHotelsId = null;
  s.hotelsMode = "hold";
  await focusInput(s);
  const pausedHotels = await waitNode(() => s.heldHotelsId !== null, 25000, "hotels.json paused");
  await s.ev(RESET_LOG_JS);
  await s.send("Input.insertText", { text: "адмирал" });
  await sleep(HOLD_MS);
  out.addressFirst = { hotelsHeld: pausedHotels, theirRows: await s.ev(ROWS_JS),
                       mineDuringHold: (await s.ev(PL_ROWS_JS)).rows.length };
  s.hotelsMode = "pass";
  if (pausedHotels) await s.send("Fetch.continueRequest", { requestId: s.heldHotelsId });
  s.heldHotelsId = null;
  await waitSettled(s, 30000);
  await waitFor(s, PL_VISIBLE_JS, 8000);
  out.addressFirst.theirRowsAfter = await s.ev(ROWS_JS);
  out.addressFirst.mineAfter = (await s.ev(PL_ROWS_JS)).rows.map((r) => r.title);
  await clearField(s);
  return out;
}

// 375×812 (Д5/В6/G11): the whole list must stay on the screen and every row must
// keep the 44 px touch target.
async function checkMobile(s) {
  await s.send("Emulation.setDeviceMetricsOverride", { width: 375, height: 812, deviceScaleFactor: 2, mobile: true });
  await navigateFresh(s, "375px");
  const ready = await placesReady(s);
  const list = await typePlaces(s, "парк");
  const out = { ready, rows: list.rows.length, more: list.more, rect: list.rect,
                innerHeight: list.innerHeight, fits: list.rect.bottom <= list.innerHeight,
                minRowHeight: Math.min.apply(null, list.rows.map((r) => r.height).concat([999])) };
  await clearField(s);
  await s.send("Emulation.setDeviceMetricsOverride", { width: W, height: H, deviceScaleFactor: MOB ? 2 : 1, mobile: MOB });
  return out;
}

// §12 В8 — the five wiring scenarios Sol's verdict demanded.
async function checkV8(s) {
  const out = {};
  // 1. a REAL Enter on "lti" selects БЕРЛИН ГОЛДЪН БИЙЧ (their status said "Няма съвпадения")
  await navigateFresh(s, "В8 enter lti");
  await placesReady(s);
  const lti = await typePlaces(s, "lti");
  const theirStatus = await s.ev(
    "(function () { var k = document.getElementById('addrSearchResults').children;" +
    " return k.length === 1 && k[0].className.indexOf('asr-status') >= 0 ? k[0].textContent : null; })()");
  await focusInput(s);
  await pressKey(s, "Enter", 13);
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await waitSettled(s, 30000);
  out.enterLti = { mineRows: lti.rows.length, theirStatus, surface: await s.ev(PLACE_SURFACE_JS) };
  await pressEscape(s);
  await clearField(s);

  // 2. their index held, our pick lands first: no "Няма съвпадения" afterwards
  await navigateFresh(s, "В8 held index + бонита");
  s.heldIndexId = null;
  s.indexMode = "hold";
  await placesReady(s);
  const bonita = await typePlaces(s, "бонита");
  await s.ev("(function () { var e = document.querySelector('#placesSearchResults .pl-item[data-idx=\"0\"]'); if (e) e.click(); return !!e; })()");
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  s.indexMode = "pass";
  if (s.heldIndexId !== null) await s.send("Fetch.continueRequest", { requestId: s.heldIndexId });
  s.heldIndexId = null;
  await waitSettled(s, 60000);
  await sleep(1500);
  const afterIndex = await s.ev(PLACE_SURFACE_JS);
  out.pickBeforeIndex = { mineRows: bonita.rows.length, theirVisible: afterIndex.theirVisible,
                          theirHtmlHasStatus: afterIndex.theirHtml.indexOf("Няма съвпадения") >= 0,
                          pins: afterIndex.pins, popups: afterIndex.popups, title: afterIndex.title,
                          field: await s.ev(INPUT_VALUE_JS) };
  await pressEscape(s);
  await clearField(s);

  // 3. a GPS Enter with the index held, then a hotel pick: ours survives
  await navigateFresh(s, "В8 GPS + hotel");
  s.heldIndexId = null;
  s.indexMode = "hold";
  await placesReady(s);
  await clearField(s);
  await s.send("Input.insertText", { text: "43.2100, 27.9100" });
  await sleep(800);
  await pressKey(s, "Enter", 13);
  // Their coordinate path awaits ensureSearchData (index.html:5045), so nothing of
  // theirs can land while the index is held; the hold is the plan's 3 s and the GPS
  // pin is then given its own wait.
  await sleep(HOLD_MS);
  const gpsDuringHold = await s.ev("document.querySelectorAll('.search-pin-wrapper').length");
  s.indexMode = "pass";
  if (s.heldIndexId !== null) await s.send("Fetch.continueRequest", { requestId: s.heldIndexId });
  s.heldIndexId = null;
  await waitFor(s, "document.querySelectorAll('.search-pin-wrapper').length > 0", 30000);
  const gpsPins = await s.ev("document.querySelectorAll('.search-pin-wrapper').length");
  await typePlaces(s, "хотел адмирал");
  await s.ev("(function () { var e = document.querySelector('#placesSearchResults .pl-item[data-idx=\"0\"]'); if (e) e.click(); return !!e; })()");
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await waitSettled(s, 60000);
  out.gpsThenHotel = { theirPinDuringHold: gpsDuringHold, theirPinAfterRelease: gpsPins,
                       surface: await s.ev(PLACE_SURFACE_JS) };
  await pressEscape(s);
  await clearField(s);

  // 4. the legend is open and we select with ENTER: bubbles:false keeps it open.
  //    (A CLICK closes it by THEIR own outside-click rule, index.html:1720 — recorded.)
  await navigateFresh(s, "В8 legend");
  await placesReady(s);
  // The legend is opened FIRST: a click outside .search-bar dismisses our list by
  // Д8е, so opening it afterwards would leave nothing to select.
  await s.ev("(function () { var b = document.getElementById('legendBtn'); if (b) b.click(); return !!b; })()");
  const legendBefore = await s.ev("(function () { var l = document.getElementById('legend'); return l ? !l.hidden : null; })()");
  const legendRows = await typePlaces(s, "lti");
  await focusInput(s);
  await pressKey(s, "Enter", 13);
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await waitSettled(s, 30000);
  const legendSurface = await s.ev(PLACE_SURFACE_JS);
  out.legend = { openBefore: legendBefore, rows: legendRows.rows.length,
                 openAfterEnterPick: legendSurface.legendOpen,
                 pins: legendSurface.pins, title: legendSurface.title };
  await pressEscape(s);
  await clearField(s);
  return out;
}

async function clickAt(s, x, y) {
  await s.send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y, buttons: 0 });
  await s.send("Input.dispatchMouseEvent", { type: "mousePressed", x, y, button: "left", buttons: 1, clickCount: 1 });
  await s.send("Input.dispatchMouseEvent", { type: "mouseReleased", x, y, button: "left", buttons: 0, clickCount: 1 });
}

// Phase-2 plan sec.3 + sec.16 J2: WITH a key our group stands ABOVE the address
// rows ("хотел адмирал" over "адрес: хотел бриз/мак/…"); WITHOUT one the addresses
// keep the top, exactly as today. Measured as geometry, not as a promise.
async function checkOrdering(s) {
  const out = {};
  for (const q of ["хотел адмирал", "адмирал", "училище", "болница", "детска градина", "хотел 999999"]) {
    await typePlaces(s, q);
    await sleep(POLL_MS * 4);
    out[q] = await s.ev(GEOM_JS);
    out[q].keys = JSON.parse(await s.ev(`JSON.stringify(window.__places.keys(${JSON.stringify(q)}))`));
    out[q].hasKey = await s.ev(`window.__places.search(${JSON.stringify(q)}).hasKey === true`);
  }
  // Sol C1, the remainder: a keyed query followed by a keyless one must leave no
  // inline style on their container - and the removal happens on the keystroke,
  // before their 120 ms debounce, which is the mutation G3 reads.
  await typePlaces(s, "хотел адмирал");
  await clearField(s);
  await typeQuery(s, "адмирал");
  out.afterKeyedNoBlank = { immediate: await s.ev("document.getElementById('addrSearchResults').getAttribute('style')") };
  await sleep(POLL_MS * 8);
  out.afterKeyedNoBlank.settled = await s.ev("document.getElementById('addrSearchResults').getAttribute('style')");
  await clearField(s);
  return out;
}

// Sol C2 — Enter while a key is in the field is OURS, decided by a capture
// listener; their handler never starts (one popup, one pin, their list quiet).
async function checkEnterKeyed(s) {
  await navigateFresh(s, "Enter with a key");
  if (!(await placesReady(s))) return { ready: false };
  const list = await typePlaces(s, "хотел адмирал");
  await focusInput(s);
  await pressKey(s, "Enter", 13);
  const ok = await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await waitMapStill(s);
  await waitSettled(s, 30000);
  const surface = await s.ev(PLACE_SURFACE_JS);
  const out = { ready: true, picked: ok, rows: list.rows.length, firstRow: list.rows[0] || null,
                pins: surface.pins, popups: surface.popups, title: surface.title,
                theirPins: surface.theirPins, theirVisible: surface.theirVisible,
                theirStyle: await s.ev("document.getElementById('addrSearchResults').getAttribute('style')"),
                field: await s.ev(INPUT_VALUE_JS) };
  await pressEscape(s);
  await clearField(s);
  return out;
}

// Sol C4 — the popup rule. (1) a REAL click on a hydrant while our place is
// selected: the hydrant popup opens and ours does NOT come back. (2) the × on our
// own popup closes it and it stays closed (the pin stands).
async function checkPopupRule(s) {
  await navigateFresh(s, "popup rule");
  if (!(await placesReady(s))) return { ready: false };
  const out = { ready: true };
  await typePlaces(s, "хотел адмирал");
  await s.ev("(function () { var e = document.querySelector('#placesSearchResults .pl-item[data-idx=\"0\"]'); if (e) e.click(); return !!e; })()");
  await waitFor(s, "document.querySelectorAll('.place-pin-wrapper').length > 0", 20000);
  await waitMapStill(s);
  await waitSettled(s, 30000);
  const hyd = await s.ev(HYDRANT_RECT_JS);
  out.hydrantPin = hyd;
  if (hyd) {
    await clickAt(s, hyd.x, hyd.y);
    await sleep(1200);
    await waitMapStill(s);
    out.afterHydrantClick = {
      placePopups: await s.ev("document.querySelectorAll('.place-popup').length"),
      anyPopup: await s.ev("document.querySelectorAll('.leaflet-popup').length"),
      hydrantPopup: await s.ev("!!document.querySelector('.leaflet-popup .hydrant-popup')"),
      hydrantTitle: await s.ev("(function () { var t = document.querySelector('.hydrant-popup .hp-title'); return t ? t.textContent : null; })()"),
      placePins: await s.ev("document.querySelectorAll('.place-pin-wrapper').length")
    };
  } else warn("няма видим хидрантен пин за пробата на попъпа");
  // (2) the × on our own popup
  await pressEscape(s);
  await clearField(s);
  await typePlaces(s, "хотел адмирал");
  await s.ev("(function () { var e = document.querySelector('#placesSearchResults .pl-item[data-idx=\"0\"]'); if (e) e.click(); return !!e; })()");
  await waitFor(s, "document.querySelector('.place-popup') !== null", 20000);
  await waitMapStill(s);
  await waitSettled(s, 30000);
  const close = await s.ev(CLOSE_BTN_RECT_JS);
  out.closeButton = close;
  if (close) {
    await clickAt(s, close.x, close.y);
    await sleep(1500);
    out.afterClose = {
      placePopups: await s.ev("document.querySelectorAll('.place-popup').length"),
      anyPopup: await s.ev("document.querySelectorAll('.leaflet-popup').length"),
      placePins: await s.ev("document.querySelectorAll('.place-pin-wrapper').length")
    };
  } else warn("няма × върху нашия попъп");
  await pressEscape(s);
  await clearField(s);
  return out;
}

// 375x812 with a KEY: both lists must be on the screen and the lower one must be
// reachable - the reason Sol put a max-height on their container as well (C1).
async function checkMobileKeyed(s) {
  await s.send("Emulation.setDeviceMetricsOverride", { width: 375, height: 812, deviceScaleFactor: 2, mobile: true });
  await navigateFresh(s, "375px keyed");
  const ready = await placesReady(s);
  const list = await typePlaces(s, "хотел");
  await sleep(POLL_MS * 4);
  const geom = await s.ev(GEOM_JS);
  const scrolled = await s.ev(
    "(function () { var t = document.getElementById('addrSearchResults');" +
    " t.scrollTop = 9999; return t.scrollTop; })()");
  const out = { ready, rows: list.rows.length, mores: list.mores, geom, theirScrollTop: scrolled,
                minRowHeight: Math.min.apply(null, list.rows.map((r) => r.height).concat([999])) };
  await clearField(s);
  await s.send("Emulation.setDeviceMetricsOverride", { width: W, height: H, deviceScaleFactor: MOB ? 2 : 1, mobile: MOB });
  return out;
}

// G12г — the constants against the bytes of the tracked files.
function checkShaPins() {
  const index = fs.readFileSync(path.join(REPO, "index.html"), "utf8");
  const out = [];
  for (const [name, rel] of [["HOTELS_SHA256", "data/hotels.json"],
                             ["PLACES2_SHA256", "data/places.json"],
                             ["CATS_SHA256", "data/place_categories.json"]]) {
    const m = index.match(new RegExp("const\\s+" + name + "\\s*=\\s*'([0-9a-f]{64})'"));
    const digest = crypto.createHash("sha256").update(fs.readFileSync(path.join(REPO, rel))).digest("hex");
    out.push({ constant: name, file: rel, pinned: m ? m[1] : null, actual: digest, ok: !!m && m[1] === digest });
  }
  return out;
}

// The lot's own gate, in the order the plan reads: the tokenizer, the reference
// rows, the М5 table as a human sees it, the selection, П7, the four refusals,
// the two races, В8 and 375 px.
async function runG4(s) {
  console.log("  == G4 (местата) ==");
  await armPlacesFetch(s);
  await navigateFresh(s, "places");
  const ready = await placesReady(s);
  if (!ready) { warn("клонът на местата не се вдигна"); return { ready: false, shaPins: checkShaPins() }; }
  const out = { ready: true, shaPins: checkShaPins() };
  out.tokens = await checkTokenTable(s);
  console.log(`     G12б: ${out.tokens.passed}/${out.tokens.total} (в теста: ${out.tokens.rowsInTest} реда)`);
  out.reference = await checkReferenceRows(s);
  console.log(`     G12в: ${out.reference.passedOrdered}/${out.reference.total} подредени, ` +
              `${out.reference.passedSets}/${out.reference.total} като множества, режим ${out.reference.mode}`);
  out.m5 = await checkM5Table(s);
  console.log(`     М5: ${out.m5.filter((r) => r.ok).length}/${out.m5.length} по брой редове`);
  out.pick = await checkPickAndEscape(s, "хотел адмирал");
  console.log(`     избор: пин ${out.pick.surface.pins}, попъп "${out.pick.surface.title}", ` +
              `хидрантите различни: ${out.pick.hydrantsChanged}`);
  out.lateSheet = await checkLateDetailSheet(s);
  out.refusals = await checkRefusals(s);
  out.races = await checkRaces(s);
  out.v8 = await checkV8(s);
  out.mobile = await checkMobile(s);
  // --- phase 2 ---------------------------------------------------------------
  out.ordering = await checkOrdering(s);
  console.log(`     подредбата: "хотел адмирал" наши отгоре: ${out.ordering["хотел адмирал"].mineFirst}, ` +
              `"адмирал" наши отгоре: ${out.ordering["адмирал"].mineFirst}`);
  out.enterKeyed = await checkEnterKeyed(s);
  out.popupRule = await checkPopupRule(s);
  out.mobileKeyed = await checkMobileKeyed(s);
  out.consoleWarns = [...new Set(s.warns)];    // warnOnce() is where a caught throw lands
  if (out.consoleWarns.length) warn(`конзолни предупреждения: ${out.consoleWarns.length}`);
  return out;
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
    const g4Path = path.join(OUT_DIR, "g4.json");
    fs.writeFileSync(g4Path, JSON.stringify(g4, null, 2) + "\n");
    console.log(`  записах ${g4Path} (кука за C4)`);
  }

  console.log(`  конзолни грешки: ${s.errs.length}`);
  if (s.errs.length) for (const e of s.errs) console.log(`     ${String(e).slice(0, 200)}`);
  console.log(`  конзолни предупреждения: ${s.warns.length}`);
  if (s.warns.length) for (const e of [...new Set(s.warns)]) console.log(`     ${String(e).slice(0, 200)}`);
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
