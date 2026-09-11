// Ф9 (план §3.А) — the Node probe that runs the ADDRESS slice of index.html headless.
//
// Contract, so no test has to guess — the договор of tests/granitsi_client_probe.mjs
// (:3-7, :212-260) with THREE declared extensions, marked (+) below:
//   * the slice text, the payload map and the cases arrive as ONE json on STDIN;
//     the answers leave as ONE json on STDOUT. No Cyrillic on the command line, no
//     network — `fetch` is a stub and answers only from what the caller handed in.
//   * (+) `payload_files: {url: absolute path}` — the address payloads are 16 MB
//     together, and pushing them through STDIN twice (encode + parse) costs more
//     than the whole gate. The stub reads the file from disk instead; the PATHS are
//     ASCII, so the contract's reason (no Cyrillic on the command line) still holds.
//     `payloads: {url: text}` keeps working for the small ones.
//   * (+) `shared` — the slice of план Т12 is TWO cuts: the shared quarter block
//     (declarations only) and the address slice. They are concatenated in that
//     order before `new Function`, because the address slice READS the shared
//     block's bindings.
//   * (+) `strict: true` prepends "use strict" to the body. Needed by the third
//     negative half of ИБ1-Г23: without it an assignment to an undeclared name
//     leaks into `globalThis` and nothing ever throws (ИБ1-О8), and in a process
//     polluted by an earlier raise even a strict slice passes — so this probe is
//     started FRESH for every half.
//   * the slice is raised with `new Function(...params, body)`. The DEFAULT params
//     are the six the address slice really needs (М, срез 4840–6198: resultsEl 10 ·
//     anchorHydrantsAt 7 · buildNavActions 5 · inputEl 3 · WORKER_URL 1 ·
//     POPUP_AUTOPAN_TL 1; POPUP_AUTOPAN_BR is 0 and does not enter) plus the six
//     ambient ones the slice touches (map 46 · document 63 · caches 8 · fetch 7 ·
//     L 13 · window 2). `console` and `crypto` are NOT parameters: the slice uses
//     neither (measured 0 and 0).
//   * `inputEl` and `resultsEl` stay OUTSIDE the slice on purpose (Т12): they are
//     the two bindings `initAddressSearch` reads from the page, and as parameters
//     they become the probe's own handles on what the dropdown did.
//   * every export is returned as a ZERO-ARG GETTER, never as a value: `searchIndex`
//     is null until `ensureSearchData()` has run, and a value captured at return
//     time would pin the null.
//   * `map` is stubbed with the centre the app pins (index.html:1838). The numbers
//     are ASSEMBLED, never written as a pair (О95, red line 5 of the plan): no
//     tracked file of Fire_Varna carries a coordinate in prose.
//
// Asks (each returns one entry, in order, in `answers`):
//   {ask:"value", name}                    -> the exported value
//   {ask:"call", name, args:[…]}           -> the awaited return of a call
//   {ask:"ensure"}                         -> {ok, entries, rows, quarter, error}
//   {ask:"search", q}                      -> {n, deduped, rows:[{kind,en,d,_ord}…]}
//   {ask:"render", q, limit}               -> [{title, meta, html}] — the dropdown ROW
//   {ask:"panel", q, pick}                 -> {panel, popup, sheet} — the panel + popup
//   {ask:"coord", q}                       -> {title, meta, popup} — the GPS row
//   {ask:"collisions", queries:[…]}        -> [{q, ranked, shown, merged}]
//   {ask:"digests"}                        -> {entries_digest, rows_digest}
//
// Exit code: 0 when the run itself succeeded (an ask may still answer "false"),
// 1 when the slice could not be raised or an ask threw — the message travels in
// `error` so a red gate names its own reason.

import { readFileSync } from 'node:fs';

const DEFAULT_PARAMS = ['window', 'document', 'fetch', 'caches', 'map', 'L',
                        'inputEl', 'resultsEl', 'anchorHydrantsAt',
                        'buildNavActions', 'WORKER_URL', 'POPUP_AUTOPAN_TL'];

// index.html:1838 — the map centre, assembled from whole numbers so that this
// tracked file carries no coordinate pair (план red line 5).
const CENTRE_LAT = 43 + 2141 / 10000;
const CENTRE_LNG = 27 + 9147 / 10000;

function readStdin() {
  return new Promise((resolve, reject) => {
    let buf = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (d) => { buf += d; });
    process.stdin.on('end', () => resolve(buf));
    process.stdin.on('error', reject);
  });
}

// ---- the DOM stub: enough for the dropdown, the panel and the popup, and
// DETERMINISTIC — `outerHTML` is what Г12 compares byte for byte.
function escapeText(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function escapeAttr(s) {
  return escapeText(s).replace(/"/g, '&quot;');
}

function makeNode(tag) {
  const node = {
    tagName: tag, className: '', textContent: '', children: [],
    style: {}, dataset: {}, hidden: false, attributes: [],
    classList: {
      _set: new Set(),
      add(...c) { c.forEach((x) => { if (x) this._set.add(x); }); },
      remove(...c) { c.forEach((x) => this._set.delete(x)); },
      contains(c) { return this._set.has(c); },
      toggle(c, on) { if (on) this.add(c); else this.remove(c); }
    },
    appendChild(child) {
      if (child && child.tagName === '#fragment') {
        child.children.forEach((k) => node.children.push(k));
        child.children = [];
        return child;
      }
      node.children.push(child);
      return child;
    },
    replaceChildren(...kids) {
      node.children = [];
      kids.forEach((k) => node.appendChild(k));
    },
    setAttribute(name, value) { node.attributes.push([name, String(value)]); },
    removeAttribute() {}, addEventListener() {}, removeEventListener() {},
    querySelector: () => null, querySelectorAll: () => [], focus() {}, blur() {},
    remove() {},
    // the flattened text of the subtree — what a row really says
    text() {
      let out = node.textContent || '';
      for (const c of node.children) out += (out ? ' ' : '') + (c.text ? c.text() : (c.textContent || ''));
      return out;
    },
    // the serialization Г12 compares: attributes in the order they were set,
    // the class list after them, dataset keys sorted.
    get outerHTML() {
      if (node.tagName === '#text') return escapeText(node.textContent || '');
      const parts = [];
      const cls = [node.className]
        .concat(Array.from(node.classList._set))
        .filter(Boolean).join(' ').trim();
      if (cls) parts.push('class="' + escapeAttr(cls) + '"');
      for (const [name, value] of node.attributes) parts.push(name + '="' + escapeAttr(value) + '"');
      for (const key of Object.keys(node.dataset).sort()) {
        parts.push('data-' + key + '="' + escapeAttr(node.dataset[key]) + '"');
      }
      if (node.hidden) parts.push('hidden');
      const open = '<' + node.tagName + (parts.length ? ' ' + parts.join(' ') : '') + '>';
      let inner = escapeText(node.textContent || '');
      for (const c of node.children) inner += (c.outerHTML !== undefined ? c.outerHTML : escapeText(c.textContent || ''));
      return open + inner + '</' + node.tagName + '>';
    }
  };
  return node;
}

function makeInput() {
  const el = makeNode('input');
  el.value = '';
  return el;
}

function makeDocument() {
  return {
    createElement: (tag) => makeNode(tag),
    createTextNode: (t) => { const n = makeNode('#text'); n.textContent = t; return n; },
    createDocumentFragment: () => makeNode('#fragment'),
    getElementById: () => null,
    querySelector: () => null,
    addEventListener() {},
    body: makeNode('body')
  };
}

function makeEnv(input) {
  const payloads = input.payloads || {};
  const files = input.payload_files || {};
  const opened = [];          // every url the slice asked for, in order
  const panels = [];          // what showBuildingDetail / openSearchPopup received
  const anchors = [];

  const fetchStub = async (url) => {
    opened.push(url);
    let text = payloads[url];
    if (text === undefined && files[url] !== undefined) {
      try { text = readFileSync(files[url], 'utf8'); }
      catch (e) { text = undefined; }
    }
    if (text === undefined) return { ok: false, status: 404, text: async () => '', json: async () => { throw new Error('404'); }, clone() { return this; } };
    return {
      ok: true, status: 200,
      text: async () => text,
      json: async () => JSON.parse(text),
      clone() { return this; }
    };
  };

  const cachesStub = {
    async open() {
      return {
        async match() { return undefined; },
        async put() {},
        async delete() { return true; }
      };
    },
    async match() { return undefined; }
  };

  const windowStub = {
    addEventListener() {}, removeEventListener() {},
    location: { href: 'http://localhost/index.html', origin: 'http://localhost' },
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    matchMedia: () => ({ matches: false, addEventListener() {} }),
    innerWidth: 375, innerHeight: 812,
    setTimeout: (fn) => { fn(); return 0; }, clearTimeout() {}
  };

  const centre = Array.isArray(input.centre)
    ? { lat: input.centre[0], lng: input.centre[1] }
    : { lat: CENTRE_LAT, lng: CENTRE_LNG };

  const mapStub = {
    getCenter: () => centre,
    getZoom: () => 13,
    setView() { return mapStub; }, panTo() { return mapStub; },
    closePopup() {}, removeLayer() {}, addLayer() {}, hasLayer: () => false,
    on() {}, off() {}, getContainer: () => makeNode('div'),
    latLngToContainerPoint: () => ({ x: 0, y: 0 }),
    containerPointToLatLng: () => centre,
    getBounds: () => ({ contains: () => true }),
    getSize: () => ({ x: 375, y: 600 })
  };

  const layer = {
    addTo() { return layer; }, remove() { return layer; }, removeFrom() { return layer; },
    on() { return layer; }, off() { return layer; },
    setLatLng() { return layer; }, setIcon() { return layer; },
    bindPopup() { return layer; }, openPopup() { return layer; },
    setContent() { return layer; }, setLatLngs() { return layer; }, openOn() { return layer; },
    getElement: () => makeNode('div')
  };

  // A popup is where the САМОСТОЯТЕЛНИЯТ надпис lands (`openSearchPopup`,
  // `openCoordPopup`, `openEntrancePopup`): the stub keeps every node handed to
  // `setContent`, in order, so a gate can read what the surface really said.
  const popupStub = () => {
    const p = {
      setLatLng() { return p; },
      setContent(node) { panels.push(node); return p; },
      openOn() { return p; }, addTo() { return p; }, on() { return p; },
      update() { return p; }, getElement: () => makeNode('div')
    };
    return p;
  };

  const Lstub = {
    marker: () => layer, divIcon: () => ({}), popup: popupStub,
    latLng: (a, b) => ({ lat: a, lng: b }),
    tileLayer: () => layer, layerGroup: () => layer, polyline: () => layer,
    control: { attribution: () => layer, scale: () => layer },
    point: (x, y) => ({ x: x, y: y })
  };

  return {
    opened, panels, anchors,
    values: {
      window: windowStub, document: makeDocument(), fetch: fetchStub,
      caches: cachesStub, map: mapStub, L: Lstub,
      inputEl: makeInput(), resultsEl: makeNode('div'),
      anchorHydrantsAt: (lat, lng) => { anchors.push([lat, lng]); },
      buildNavActions: () => null,
      WORKER_URL: 'http://localhost/worker',
      POPUP_AUTOPAN_TL: [0, 0]
    }
  };
}

function buildBody(input) {
  const exports = input.exports || [];
  const head = input.strict ? '"use strict";\n' : '';
  const shared = input.shared ? input.shared + '\n' : '';
  let body = head + shared + input.slice;
  body += '\n;return {\n' + exports.map(
    (n) => '  ' + JSON.stringify(n) + ': function () { return ' + n + '; }'
  ).join(',\n') + '\n};';
  return body;
}

async function run(input) {
  const params = input.params || DEFAULT_PARAMS;
  const env = makeEnv(input);
  const args = params.map((n) => {
    if (n in env.values) return env.values[n];
    throw new Error('no stub for parameter ' + n);
  });
  const fn = new Function(...params, buildBody(input));
  const got = fn(...args);
  const value = (name) => {
    if (!(name in got)) throw new Error('not exported: ' + name);
    return got[name]();
  };

  const ensure = async () => {
    const index = await value('ensureSearchData')();
    return index;
  };

  const rowsFor = async (q) => {
    const index = await ensure();
    const ranked = value('runGeocoderSearch')(q, index);
    const shown = value('dedupeDisplayRows')(ranked);
    return { ranked, shown };
  };

  const answers = [];
  for (const ask of (input.asks || [])) {
    if (ask.ask === 'value') {
      answers.push(value(ask.name));
    } else if (ask.ask === 'call') {
      answers.push(await value(ask.name)(...(ask.args || [])));
    } else if (ask.ask === 'ensure') {
      try {
        const index = await ensure();
        let quarter = null;
        try { quarter = value('quarterIndex') === null ? false : !!value('quarterIndex'); }
        catch (e) { quarter = null; }   // the base slice has no quarter state at all
        answers.push({
          ok: true,
          entries: (index && index.entries) ? index.entries.length : 0,
          quarter: quarter,
          opened: env.opened.slice()
        });
      } catch (e) {
        answers.push({ ok: false, error: (e && e.message) || String(e) });
      }
    } else if (ask.ask === 'search') {
      const r = await rowsFor(ask.q);
      answers.push({
        n: r.ranked.length, deduped: r.shown.length,
        rows: r.shown.slice(0, ask.limit || 10).map((x) => ({
          kind: x.kind, en: x.en === undefined ? null : x.en,
          d: x.d === undefined ? null : x.d,
          ord: x._ord === undefined ? null : x._ord,
          display_id: x.display_id === undefined ? null : x.display_id
        }))
      });
    } else if (ask.ask === 'render') {
      const r = await rowsFor(ask.q);
      const buildExactItem = value('buildExactItem');
      const out = [];
      const limit = ask.limit === undefined ? 3 : ask.limit;
      r.shown.slice(0, limit).forEach((row, i) => {
        const node = buildExactItem(row, i);
        const title = findByClass(node, 'asr-title');
        const meta = findByClass(node, 'asr-meta');
        out.push({
          title: title ? title.text() : null,
          meta: meta ? meta.text() : null,
          html: node.outerHTML
        });
      });
      answers.push(out);
    } else if (ask.ask === 'panel') {
      const r = await rowsFor(ask.q);
      const row = r.shown[ask.pick || 0];
      if (!row) { answers.push({ error: 'no row for ' + ask.q }); continue; }
      const before = env.panels.length;
      await value('selectResult')(row);
      const sheet = findByClass(env.values.document.body, 'detail-sheet');
      answers.push({
        popups: env.panels.slice(before).map((n) => (n && n.text ? n.text() : String(n))),
        popups_html: env.panels.slice(before).map((n) => (n && n.outerHTML !== undefined ? n.outerHTML : '')),
        sheet: sheet ? sheet.text() : null,
        sheet_title: sheet ? (findByClass(sheet, 'ds-title') ? findByClass(sheet, 'ds-title').text() : null) : null
      });
    } else if (ask.ask === 'coord') {
      await ensure().catch(() => null);
      const parsed = value('parseCoordQuery')(ask.q);
      if (!parsed) { answers.push({ error: 'not a coordinate query' }); continue; }
      const row = value('renderCoordRow')(parsed);
      const before = env.panels.length;
      // The fifth surface (`openCoordPopup:5884-5900`, М): it hands its node to
      // `L.popup().setContent(...)` and returns nothing, so the stub is where the
      // words are read from.
      value('openCoordPopup')(row);
      const popupNode = env.panels[env.panels.length - 1];
      answers.push({
        title: value('coordTitle')(row),
        meta: value('coordMeta')(row),
        popup: (env.panels.length > before && popupNode && popupNode.text) ? popupNode.text() : null,
        html: env.values.resultsEl.outerHTML
      });
    } else if (ask.ask === 'collisions') {
      const out = [];
      for (const q of (ask.queries || [])) {
        const r = await rowsFor(q);
        out.push({ q: q, ranked: r.ranked.length, shown: r.shown.length,
                   merged: r.ranked.length - r.shown.length });
      }
      answers.push(out);
    } else if (ask.ask === 'digests') {
      await ensure();
      answers.push({ entries_digest: value('entriesDigest'),
                     rows_digest: value('rowsDigest') });
    } else {
      throw new Error('unknown ask: ' + ask.ask);
    }
  }
  return { ok: true, answers, opened: env.opened, anchors: env.anchors };
}

function findByClass(node, cls) {
  if (!node) return null;
  if (node.className === cls || (node.classList && node.classList.contains(cls))) return node;
  for (const child of (node.children || [])) {
    const hit = findByClass(child, cls);
    if (hit) return hit;
  }
  return null;
}

const raw = await readStdin();
let out;
try {
  out = await run(JSON.parse(raw));
} catch (e) {
  out = { ok: false, error: (e && e.message) || String(e),
          stack: (e && e.stack) ? String(e.stack).split('\n').slice(0, 4) : [] };
}
process.stdout.write(JSON.stringify(out));
process.exit(out.ok ? 0 : 1);
