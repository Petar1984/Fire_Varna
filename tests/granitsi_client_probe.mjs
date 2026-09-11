// Б3 (план §3.6) — the Node probe that runs a SLICE of index.html headless.
//
// Contract, so no test has to guess:
//   * the slice text, the payloads and the cases arrive as ONE json on STDIN;
//     the answers leave as ONE json on STDOUT. No temp file, no Cyrillic on the
//     command line, no network — `fetch` is a stub and answers only from the
//     payloads the caller hands in.
//   * the slice is raised with `new Function(...params, slice + ';return {…}')`.
//     The ten parameters of план §3.6 are the DEFAULT list:
//       window, caches, document, map, fetch, attribCtrl, __calls, L, console, crypto
//     `params` may override it, and it HAS to for the attribution slice
//     (index.html:1900-1918): that slice declares `const attribCtrl` itself, and a
//     lexical declaration collides with a parameter of the same name — measured:
//     `new Function('attribCtrl', 'const attribCtrl = 1; …')` throws
//     "SyntaxError: Identifier 'attribCtrl' has already been declared".
//   * every export is returned as a ZERO-ARG GETTER, never as a value: `RECS` is
//     empty until `ensurePlaces()` has run, and a value captured at return time
//     would pin the empty array.
//   * `map` is stubbed with the centre the reference pins (recall_sweep.py:102-104
//     = index.html:1838, 43.2141 / 27.9147). Without it `centre()` (index.html:6952-6955)
//     catches, `distOf` returns 0 and the ORDER of every answer collapses.
//   * `crypto` is a SEPARATE stub from `window.crypto` on purpose: `accept`
//     (index.html:6605) reads `window.crypto && crypto.subtle` — two different
//     names that are one object in a browser. In Node the bare `crypto` is the
//     environment's WebCrypto, so shadowing only `window.crypto` would measure the
//     ON path while the case says OFF.
//   * `__calls` counts the WRAPPED validators, because `null` out of `accept` does
//     not by itself prove the validator refused (плана 1.8.11): with crypto ON and a
//     mismatching sha the digest refuses first and the validator is never called.
//
// Asks (each returns one entry, in order, in `answers`):
//   {ask:"value", name}                                  -> the exported value
//   {ask:"validate", fn, url}                            -> boolean (payload parsed here)
//   {ask:"accept", url, sha, validate}                   -> {result:"null"|"object"}
//   {ask:"ensurePlaces"}                                 -> {ok,recs} | {threw}
//   {ask:"search", q}                                    -> {n, category, hasKey, names}
//   {ask:"cards", forbidden:[…]}                         -> {n, hits:[…], sample}
//   {ask:"attributions"}                                 -> {added:[…], removed:[…]}
//   {ask:"calls"}                                        -> the counter object
//   {ask:"call", name, args:[…]}                         -> the raw return of a nullary/simple call
//
// Exit code: 0 when the run itself succeeded (an ask may still answer "false"),
// 1 when the slice could not be raised or an ask threw — the message travels in
// `error` so a red gate names its own reason.

import { webcrypto } from 'node:crypto';

const DEFAULT_PARAMS = ['window', 'caches', 'document', 'map', 'fetch',
                        'attribCtrl', '__calls', 'L', 'console', 'crypto'];

function readStdin() {
  return new Promise((resolve, reject) => {
    let buf = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (d) => { buf += d; });
    process.stdin.on('end', () => resolve(buf));
    process.stdin.on('error', reject);
  });
}

// ---- the DOM stub: enough for span()/popupFor and nothing more
function makeNode(tag) {
  const node = {
    tagName: tag, className: '', textContent: '', children: [],
    style: {}, dataset: {},
    classList: {
      _set: new Set(),
      add(...c) { c.forEach((x) => this._set.add(x)); },
      remove(...c) { c.forEach((x) => this._set.delete(x)); },
      contains(c) { return this._set.has(c); }
    },
    appendChild(child) { node.children.push(child); return child; },
    replaceChildren(...kids) { node.children = kids; },
    setAttribute() {}, addEventListener() {},
    // the flattened text of the subtree — what a card really says
    text() {
      let out = node.textContent || '';
      for (const c of node.children) out += (out ? ' ' : '') + (c.text ? c.text() : (c.textContent || ''));
      return out;
    }
  };
  return node;
}

function makeDocument() {
  return {
    createElement: (tag) => makeNode(tag),
    createTextNode: (t) => { const n = makeNode('#text'); n.textContent = t; return n; },
    getElementById: () => null,
    addEventListener() {},
    body: makeNode('body')
  };
}

function makeEnv(input) {
  const calls = {};
  const warnings = [];
  const attribAdded = [], attribRemoved = [];
  const payloads = input.payloads || {};
  const cacheStore = input.cache || {};
  const cacheName = input.cache_name || null;

  const cryptoStub = (input.crypto === 'off') ? undefined : { subtle: webcrypto.subtle };
  const windowStub = {
    crypto: cryptoStub,
    AbortController: globalThis.AbortController,
    addEventListener() {}, removeEventListener() {},
    location: { href: 'http://localhost/index.html', origin: 'http://localhost' },
    localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
    matchMedia: () => ({ matches: false, addEventListener() {} })
  };

  const cachesStub = {
    async open(name) {
      const live = (cacheName === null) || (name === cacheName);
      return {
        async match(url) {
          if (!live) return undefined;
          const text = cacheStore[url];
          if (text === undefined) return undefined;
          return { text: async () => text };
        },
        async put() { /* best effort, as in the page */ },
        async delete() { return true; }
      };
    },
    async match() { return undefined; }
  };

  const fetchStub = async (url) => {
    const text = payloads[url];
    if (text === undefined) return { ok: false, status: 404, text: async () => '' };
    return { ok: true, status: 200, text: async () => text };
  };

  const attribCtrl = {
    addAttribution(s) { attribAdded.push(s); return this; },
    removeAttribution(s) { attribRemoved.push(s); return this; },
    addTo() { return this; }
  };

  const mapStub = {
    getCenter: () => ({ lat: 43.2141, lng: 27.9147 }),
    getZoom: () => 13,
    zoomControl: { setPosition() {} },
    closePopup() {}, removeLayer() {}, addLayer() {},
    on() {}, off() {}, hasLayer: () => false
  };

  const layer = { addTo() { return layer; }, remove() { return layer; }, setUrl() { return layer; } };
  const Lstub = {
    tileLayer: () => layer,
    control: { attribution: () => attribCtrl, scale: () => layer },
    popup: () => ({ setLatLng() { return this; }, setContent() { return this; }, openOn() { return this; } }),
    marker: () => ({ addTo() { return this; }, on() { return this; } }),
    divIcon: () => ({}), latLng: (a, b) => ({ lat: a, lng: b })
  };

  const consoleStub = {
    log: (...a) => warnings.push(['log', a.map(String).join(' ')]),
    warn: (...a) => warnings.push(['warn', a.map(String).join(' ')]),
    error: (...a) => warnings.push(['error', a.map(String).join(' ')]),
    info: () => {}, debug: () => {}
  };

  const extras = {
    // index.html:4255 — it lives OUTSIDE every slice; popupFor calls it last.
    buildNavActions: () => null
  };

  return { calls, warnings, attribAdded, attribRemoved, extras,
           values: { window: windowStub, caches: cachesStub, document: makeDocument(),
                     map: mapStub, fetch: fetchStub, attribCtrl, __calls: calls,
                     L: Lstub, console: consoleStub, crypto: cryptoStub } };
}

function buildBody(input) {
  const wrap = input.wrap || [];
  const exports = input.exports || [];
  let body = input.slice;
  for (const name of wrap) {
    // A function DECLARATION is a re-assignable binding, and ensurePlaces reads the
    // binding at call time — so the counter sees every call the page makes.
    body += '\n;{ const __orig_' + name + ' = ' + name + ';\n  ' + name +
            ' = function () { __calls[' + JSON.stringify(name) + '] = (__calls[' +
            JSON.stringify(name) + '] || 0) + 1; return __orig_' + name +
            '.apply(null, arguments); }; }';
  }
  body += '\n;return {\n' + exports.map(
    (n) => '  ' + JSON.stringify(n) + ': function () { return ' + n + '; }'
  ).join(',\n') + '\n};';
  return body;
}

async function run(input) {
  const params = input.params || DEFAULT_PARAMS;
  const env = makeEnv(input);
  const names = params.concat(input.extra_stubs || []);
  const args = names.map((n) => {
    if (n in env.values) return env.values[n];
    if (n in env.extras) return env.extras[n];
    throw new Error('no stub for parameter ' + n);
  });
  const fn = new Function(...names, buildBody(input));
  const got = fn(...args);
  const value = (name) => {
    if (!(name in got)) throw new Error('not exported: ' + name);
    return got[name]();
  };

  const answers = [];
  for (const ask of (input.asks || [])) {
    if (ask.ask === 'value') {
      answers.push(value(ask.name));
    } else if (ask.ask === 'validate') {
      const text = (input.payloads || {})[ask.url];
      if (text === undefined) throw new Error('no payload for ' + ask.url);
      let data = null;
      try { data = JSON.parse(text); } catch (e) { answers.push({ parse_error: String(e) }); continue; }
      answers.push(!!value(ask.fn)(data, text));
    } else if (ask.ask === 'accept') {
      const text = (input.payloads || {})[ask.url];
      const out = await value('accept')(text, ask.sha, value(ask.validate));
      answers.push({ result: out === null ? 'null' : typeof out });
    } else if (ask.ask === 'ensurePlaces') {
      try {
        await value('ensurePlaces')();
        answers.push({ ok: true, recs: value('RECS').length });
      } catch (e) {
        answers.push({ ok: false, threw: (e && e.message) || String(e) });
      }
    } else if (ask.ask === 'search') {
      // A row of the client is the WRAPPER `{e: record, ...}` (index.html makeRec),
      // so the identity of an answer is `x.e.name` — `x.name` is undefined and a
      // parity fixture built on it would compare [null, null, ...] with itself.
      const r = value('search')(ask.q);
      answers.push({ n: r.rows.length, category: r.category, hasKey: r.hasKey,
                     names: r.rows.map((x) => (x.e ? x.e.name : x.name)) });
    } else if (ask.ask === 'cards') {
      // `records` = the DELIVERED rows, handed in by the caller: popupFor takes a
      // raw record (index.html:7298 passes the very object the payload carries), so
      // the card gate does not have to go through the validators to be non-vacuous.
      const forbidden = ask.forbidden || [];
      const recs = ask.records || value('RECS');
      const popupFor = value('popupFor');
      const hits = [];
      let sample = null;
      for (const rec of recs) {
        const node = popupFor(rec.e !== undefined ? rec.e : rec);
        const text = node.text();
        if (sample === null) sample = text;
        for (const bad of forbidden) if (text.indexOf(bad) >= 0) hits.push([rec.name, bad]);
      }
      answers.push({ n: recs.length, hits, sample });
    } else if (ask.ask === 'attributions') {
      answers.push({ added: env.attribAdded, removed: env.attribRemoved });
    } else if (ask.ask === 'calls') {
      answers.push(Object.assign({}, env.calls));
    } else if (ask.ask === 'call') {
      answers.push(await value(ask.name)(...(ask.args || [])));
    } else {
      throw new Error('unknown ask: ' + ask.ask);
    }
  }
  return { ok: true, answers, calls: env.calls, warnings: env.warnings,
           attributions: { added: env.attribAdded, removed: env.attribRemoved } };
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
