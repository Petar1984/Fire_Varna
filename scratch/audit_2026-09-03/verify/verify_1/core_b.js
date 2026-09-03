var map = null;
// ---- constants lifted verbatim
    const TOP = 8, MIN_Q = 2, DEBOUNCE_MS = 120, FETCH_TIMEOUT_MS = 8000;
    const TOP_TOTAL = 16, GEN_CAP = 300;               // фаза 2 С3: per group / per class
    const MX = 81152, MY = 110574;               // metres per degree of lon/lat in Varna (М1)
    const KIND_GROUP = {
      'Хотел': 'Хотели', 'Семеен хотел': 'Хотели',
      'хотел · без категоризация': 'Хотели', 'апарт-хотел': 'Хотели',
      'училище': 'Училища', 'университет': 'Университети', 'болница': 'Болници',
      'ДКЦ': 'ДКЦ', 'хоспис': 'Хосписи', 'детска градина': 'Детски градини'
    };
// ---- primitives + tokenizer + state (verbatim 6309-6455)
    // ---- primitives: VERBATIM copies of the address search (index.html:4786-4788).
    // Theirs are private to their IIFE, and a copy that drifts would make the two
    // branches disagree in silence — tests/test_places_search_primitives.py pulls
    // every definition out of this file and compares them byte for byte.
    function norm(s){return (''+(s||'')).toLowerCase().replace(/блок/g,'бл').replace(/вход/g,'вх').replace(/[.№,'"-]/g,' ').replace(/\s+/g,' ').trim();}
    function skel(w){w=w.toLowerCase();var C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'};var o='';for(var i=0;i<w.length;i++){o+=(C[w[i]]!==undefined?C[w[i]]:w[i]);}return o.replace(/[yj]/g,'i').replace(/(\D)\1+/g,'$1');}
    function lev(a,b,cap){var la=a.length,lb=b.length;if(Math.abs(la-lb)>cap)return cap+1;var prev=[];for(var j=0;j<=lb;j++)prev[j]=j;for(var i=1;i<=la;i++){var cur=[i],best=i;for(var j=1;j<=lb;j++){var v=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));cur[j]=v;if(v<best)best=v;}if(best>cap)return cap+1;prev=cur;}return prev[lb];}

    // ---- Т1/Б1 tokenizer: query and name go through the very same pipe ----------
    const TYPO = /[„“”‚‘’«»–—/()]/g;             // norm() keeps these; they are word breaks
    // ТА1(2): the markers are a PRE-norm rewrite of the text, so the word that comes
    // out is the long one and ITS length is the original the cap reads. „св.“/„св“
    // belong here, not to the token step: as a 2-letter original „св марина“ could
    // never reach „Света Марина“ (measured 03.09: 25 rows against the
    // reference's 33, and the УМБАЛ missing altogether). 1:1 with recall_sweep.py MARKERS.
    const ABBR = [[/д-р/g, 'доктор '], [/х-л/g, 'хотел '], [/к-с/g, 'комплекс '],
                  [/(?<![а-яa-z])св\./g, ' свети '], [/(?<![а-яa-z])св(?![а-яa-z])/g, ' свети ']];
    const ORD_SUFFIX = /(\d+)\s*-?\s*(ми|ма|мо|ти|та|то|ви|ва|во|ри|ра|ро)(?![а-яa-z])/g;
    const TOKEN_ORD = /^(\d+)(ми|ма|мо|ти|та|то|ви|ва|во|ри|ра|ро)$/;
    const CYRILLIC_I = /[Іі]/g;                  // І/і read as the Latin letter they look like
    const COMPOUNDS = { 'апартхотел': ['апарт', 'хотел'], 'апарткомплекс': ['апарт', 'комплекс'] };
    const ADDR = ['бл', 'блок', 'вх', 'вход', 'ул', 'бул', 'кв', 'жк', '№'];   // never significant (А5)
    const ORD_STEMS = { 'първ': 1, 'втор': 2, 'трет': 3, 'четвърт': 4, 'пет': 5, 'шест': 6, 'седм': 7,
                        'осм': 8, 'девет': 9, 'десет': 10, 'единадесет': 11, 'единайсет': 11,
                        'дванадесет': 12, 'дванайсет': 12 };
    const ORD_WORDS = {};
    for (const stem of Object.keys(ORD_STEMS))
      for (const end of ['и', 'а', 'о', 'ият', 'ия', 'ата', 'ото', 'ите']) ORD_WORDS[stem + end] = String(ORD_STEMS[stem]);
    function romanValue(w) {
      if (!/^[ivx]{1,5}$/.test(w) || !/^(x{0,3})(ix|iv|v?i{0,3})$/.test(w)) return null;
      const V = { i: 1, v: 5, x: 10 };
      let total = 0, prev = 0;
      for (let i = w.length - 1; i >= 0; i--) { const v = V[w[i]]; total += v < prev ? -v : v; if (v > prev) prev = v; }
      return String(total);
    }
    function rewriteToken(w) {
      w = w.replace(CYRILLIC_I, 'i');
      if (w === 'св') return 'свети';
      if (w === 'др') return 'доктор';
      const roman = romanValue(w);
      if (roman !== null) return roman;
      if (ORD_WORDS[w] !== undefined) return ORD_WORDS[w];
      const attached = TOKEN_ORD.exec(w);
      return attached ? attached[1] : w;
    }
    function placeTokens(s) {
      let text = String(s == null ? '' : s).toLowerCase().replace(TYPO, ' ');
      for (const pair of ABBR) text = text.replace(pair[0], pair[1]);
      text = text.replace(ORD_SUFFIX, '$1');     // "7-мо" -> "7": norm() would split it
      const out = [];
      for (const word of norm(text).split(' ')) {
        if (!word) continue;
        for (const part of (COMPOUNDS[word] || [word])) {
          const t = skel(rewriteToken(part));
          if (t) out.push({ s: t, orig: word, num: /^\d+$/.test(t) });
        }
      }
      return out;
    }
    const keyOf = (s) => placeTokens(s).map((t) => t.s).join(' ');

    // ---- Д2/Д3/В7: load once, validate before trusting, cache only what validated
    let RECS = [], FORMS = null, CLASS_OF = null, placesPromise = null, GROUP_SIZE = null;
    const groupOf = (rec) => KIND_GROUP[rec.e.kind] || rec.e.kind;
    const colourOf = (kind) => GROUP_COLOUR[KIND_GROUP[kind]] || 'hotel';   // К1
    // С3 - the bug Sol found: the <=300 generosity of М3/Б2 was read off the WHOLE
    // index. With 361 records that would switch the keyless branch off entirely, so
    // it is decided per CLASS: a record is generous if its own group is <= GEN_CAP.
    const genOk = (rec) => (GROUP_SIZE.get(groupOf(rec)) || 0) <= GEN_CAP;
    function validateHotels(d, text) {
      if (!d || !d._meta || !Array.isArray(d.hotels)) return false;
      if (d.hotels.length !== EXPECT_COUNT || d._meta.count !== EXPECT_COUNT) return false;
      if (typeof d._meta.licence !== 'string' || !d._meta.licence || CADASTRAL.test(text)) return false;
      for (const h of d.hotels) {
        if (Object.keys(h).length !== EXPECT_KEYS.length) return false;
        for (const k of EXPECT_KEYS) if (!(k in h)) return false;
        for (const k of ['old_names', 'cat', 'beds', 'uins']) if (!Array.isArray(h[k])) return false;
        if (typeof h.name !== 'string' || !h.name || typeof h.zone !== 'string' || !h.zone) return false;
        if (typeof h.no_uin !== 'boolean') return false;
        if (KINDS.indexOf(h.kind) < 0 || STATUSES.indexOf(h.status) < 0 || !SRC_LINE[h.src]) return false;
        if (!isFinite(h.lat) || !isFinite(h.lon)) return false;
        if (h.lat < LAT_MIN || h.lat > LAT_MAX || h.lon < LON_MIN || h.lon > LON_MAX) return false;
      }
      return true;
    }
    function validatePlaces2(d, text) {           // фаза 2 Д3: 8 keys, enums, box, count
      if (!d || !d._meta || !Array.isArray(d.places)) return false;
      if (d.places.length !== EXPECT2_COUNT || d._meta.count !== EXPECT2_COUNT) return false;
      if (typeof d._meta.licence_osm !== 'string' || !d._meta.licence_osm) return false;
      if (typeof d._meta.licence_registry !== 'string' || !d._meta.licence_registry) return false;
      if (CADASTRAL.test(text)) return false;
      for (const p of d.places) {
        if (Object.keys(p).length !== EXPECT2_KEYS.length) return false;
        for (const k of EXPECT2_KEYS) if (!(k in p)) return false;
        if (!Array.isArray(p.old_names)) return false;
        if (typeof p.name !== 'string' || !p.name || typeof p.zone !== 'string' || !p.zone) return false;
        if (KINDS2.indexOf(p.kind) < 0 || STATUSES.indexOf(p.status) < 0 || !SRC_LINE[p.src]) return false;
        if (!isFinite(p.lat) || !isFinite(p.lon)) return false;
        if (p.lat < LAT_MIN || p.lat > LAT_MAX || p.lon < LON_MIN || p.lon > LON_MAX) return false;
      }
      return true;
    }
    const validateCats = (d) => !!(d && d._meta && d._meta.schema === 1 && d.forms &&
                                   typeof d.forms === 'object' && Array.isArray(d.chips));
    const raced = (p) => Promise.race([p, new Promise((res) => setTimeout(() => res(null), CACHE_TIMEOUT_MS))]);
    async function cacheText(url) {              // В7: only OUR open namespace, never caches.match
      if (typeof caches === 'undefined') return null;
      try {
        return await raced((async function () {
          const hit = await (await caches.open(PLACES_CACHE)).match(url);
          return hit ? await hit.text() : null;
        })());
      } catch (e) { return null; }
    }
    async function cachePut(url, text) {         // best-effort: the cache never blocks the parse
      if (typeof caches === 'undefined') return;
      try {
        await raced((async function () {
          const c = await caches.open(PLACES_CACHE);
          await c.put(url, new Response(text, { headers: { 'Content-Type': 'application/json' } }));
        })());
      } catch (e) { /* ignored on purpose */ }
    }
    async function accept(text, sha, validate) {
      if (typeof text !== 'string' || !text || text.length > MAX_BODY) return null;
      try {
        if (window.crypto && crypto.subtle) {    // В7: content check; structure is the fallback
          const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
          if (Array.from(new Uint8Array(digest)).map((b) => b.toString(16).padStart(2, '0')).join('') !== sha) return null;
        }
        const data = JSON.parse(text);
        return validate(data, text) ? data : null;
      } catch (e) { return null; }
    }
    async function fetchValidatedJson(url, sha, validate) {
      const ac = ('AbortController' in window) ? new AbortController() : null;
      const timer = setTimeout(function () { if (ac) ac.abort(); }, FETCH_TIMEOUT_MS);   // covers text() too
      let text = null;
      try {
        const resp = await fetch(url, ac ? { cache: 'no-cache', signal: ac.signal } : { cache: 'no-cache' });
        if (resp.ok) text = await resp.text();
      } catch (e) { text = null; }
      clearTimeout(timer);
      const fresh = await accept(text, sha, validate);
      if (fresh) { cachePut(url, text); return fresh; }
      return await accept(await cacheText(url), sha, validate);   // В7: a bad cache is ignored, not deleted
    }
// ---- buildIndex .. search .. hasKeyFor (verbatim 6478-6683)
    function buildIndex(hotels, places2, cats) {
      // П7 (§11 v2.1) — the registry's OTHER spellings of a quarter become ZONE
      // tokens, so „владиславово“ reaches both cadastral spellings of one place.
      // Steps (а)-(е) + (д′) are per zone, step (ж) per record below; the result
      // enters ztk/zkset ONLY, never ntk/nset/aset, so the name path is untouched.
      // Fail-soft (С7′): a `zones` that is not an object, or aliases that are not
      // strings, switch П7 off — nothing throws and the rest of the index stands.
      const zdict = (cats && cats.zones && typeof cats.zones === 'object') ? cats.zones : {};
      const famOf = (z) => (zdict[z] && zdict[z].family) || z;   // no entry = own family
      const zones = [...new Set(hotels.concat(places2).map((h) => h.zone))];
      const ownTk = new Map(zones.map((z) => [z, new Set(placeTokens(z).map((t) => t.s))]));
      // (д′) Р1: every own token of length >=3 with the family it belongs to. The
      // floor is mandatory — without it `zpz` would die against „zh“.
      const ownAll = zones.flatMap((z) => [...ownTk.get(z)].filter((v) => v.length >= 3).map((v) => [v, famOf(z)]));
      const generic = new Set();                 // (г) the dictionary's own word list
      for (const word of ((cats && cats._meta && cats._meta.zone_generic_words) || []))
        for (const t of placeTokens(word)) generic.add(t.s);
      const zoneExtra = new Map();
      for (const z of zones) {
        const aliases = (zdict[z] || {}).aliases, own = ownTk.get(z), keep = [];
        if (!Array.isArray(aliases)) continue;
        for (const alias of aliases)
          if (typeof alias === 'string')
            for (const t of placeTokens(alias))
              if (!t.num && t.orig.length > 2 && t.s.length > 2 && ADDR.indexOf(t.orig) < 0
                  && !generic.has(t.s) && !own.has(t.s) && !keep.some((k) => k.s === t.s)
                  && !ownAll.some((p) => p[1] !== famOf(z) && (p[0] === t.s || lev(t.s, p[0], 2) <= 2)))
                keep.push(t);
        if (keep.length) zoneExtra.set(z, keep);
      }
      RECS = hotels.concat(places2).map(function (h) {
        const ntk = placeTokens(h.name).map((t) => t.s);
        const ztk = placeTokens(h.zone).map((t) => t.s);
        const ktk = placeTokens(h.kind).map((t) => t.s);
        // П7 step (ж): a quarter alias never displaces a NAME path of THIS record
        for (const t of (zoneExtra.get(h.zone) || []))
          if (ztk.indexOf(t.s) < 0 && !ntk.some((v) => quality(t, v) > 0)) ztk.push(t.s);
        const aset = new Set();                  // А6: old names are name tokens, minus the noise
        for (const old of h.old_names)
          for (const t of placeTokens(old))
            if (!t.num && t.orig.length > 2 && ADDR.indexOf(t.orig) < 0) aset.add(t.s);
        return { e: h, ntk: ntk, ktk: ktk, nset: new Set(ntk), aset: aset, kkey: ktk.join(' '),
                 zkset: new Set(ztk.concat(ktk)) };
      });
      GROUP_SIZE = new Map();                    // С3: the size of every class
      for (const rec of RECS) GROUP_SIZE.set(groupOf(rec), (GROUP_SIZE.get(groupOf(rec)) || 0) + 1);
      FORMS = new Map();
      CLASS_OF = new Map();
      if (!cats) return;                         // С3: the dictionary is optional
      const head = {};
      for (const chip of cats.chips) head[chip.chip] = chip.head || chip.chip;
      for (const form of Object.keys(cats.forms)) {
        const fk = keyOf(form);
        if (!fk) continue;
        let entry = FORMS.get(fk);
        if (!entry) { entry = { chips: new Set(), heads: new Set() }; FORMS.set(fk, entry); }
        for (const chip of cats.forms[form]) { entry.chips.add(keyOf(chip)); entry.heads.add(keyOf(head[chip] || chip)); }
      }
      for (const fk of FORMS.keys()) CLASS_OF.set(fk, RECS.filter((r) => inClass(r, fk)));
    }
    function inClass(rec, fk) {                  // К2 (а)/(б) + А2 (the chip's head word)
      const entry = FORMS.get(fk);
      if (entry.chips.has(rec.kkey)) return true;
      const parts = fk.split(' ');
      if (parts.length !== 1) return false;
      if (rec.ktk.indexOf(parts[0]) >= 0) return true;
      for (const hk of entry.heads) if (hk && hk.split(' ').every((p) => rec.ktk.indexOf(p) >= 0)) return true;
      return false;
    }

    // ---- the matcher (§3 М1-М4 + §10 А1-А8 + §13 П2-П5 + §9 П6), 1:1 with recall_sweep.py
    function quality(t, v) {                     // М2: 3 exact / 2 prefix / 1 fuzzy within the cap
      if (t.num) return v === t.s ? 3 : 0;
      const len = t.orig.length;
      if (len <= 1) return 0;
      if (v === t.s) return 3;
      if (v.indexOf(t.s) === 0) return 2;
      return len <= 3 ? 0 : (lev(t.s, v, 2) <= 2 ? 1 : 0);
    }
    function tokenMatch(rec, t) {                // А4: one token, one match, best by priority
      if (rec.nset.has(t.s)) return { cat: 'name', q: 3 };
      if (!t.num && t.orig.length > 2 && rec.aset.has(t.s)) return { cat: 'alias', q: 3 };
      if (rec.zkset.has(t.s)) return { cat: 'zk', q: 3 };   // an exact zone/kind hit EATS the token
      let best = 0;
      for (const v of rec.ntk) { const k = quality(t, v); if (k > best) { best = k; if (best === 2) break; } }
      return best ? { cat: 'name', q: best } : { cat: null, q: 0 };
    }
    function significant(t, m, hasKey, rec, R) {  // А5 + П5 + П6: what makes a hit worth a row
      if (m.cat !== 'name' && m.cat !== 'alias') return false;
      if (ADDR.indexOf(t.orig) >= 0) return false;
      if (t.num) return hasKey && m.q === 3;
      if (t.orig.length >= 3) return true;
      if (hasKey && m.q >= 2) return true;
      if (!hasKey && m.cat === 'name' && m.q === 3 && rec.ntk.length === 1) return true;   // П5
      // П6 (§9 v1.4, signed): without a key a 2-char token that hits a NAME token
      // EXACTLY becomes significant when the query carries at least one MORE token
      // matching THIS record exactly — „7 су“ → VII СУ, „1 ег“ → I ЕГ. The number
      // is conjunctive anyway (П3), so it is the second exact match, not the first.
      if (!hasKey && m.cat === 'name' && m.q === 3 && t.orig.length === 2 && R) {
        for (const t2 of R) {
          if (t2 === t) continue;
          const m2 = tokenMatch(rec, t2);
          if (m2.q === 3 && (m2.cat === 'name' || m2.cat === 'alias')) return true;
        }
      }
      return false;
    }
    function scoreRec(rec, R, hasKey) {
      let bestName = 0, named = 0, total = 0, sum = 0, qual = false, numFail = false;
      for (const t of R) {
        const m = tokenMatch(rec, t);
        if (!m.cat) { if (t.num) numFail = true; continue; }   // П3: numbers are conjunctive
        total++;
        if (m.cat === 'zk') { sum += 3; continue; }            // М4 weights: zone/kind ×1, name ×2
        named++;
        sum += 2 * m.q;
        if (m.q > bestName) bestName = m.q;
        if (significant(t, m, hasKey, rec, R)) qual = true;
      }
      let uncovered = 0;                         // П2: name coverage — untouched own tokens sink
      for (const v of new Set(rec.ntk)) if (!R.some((t) => quality(t, v))) uncovered++;
      return { rec: rec, ok: qual && !numFail,
               k: [-bestName, -named, -total, -sum, rec.e.status === 'бивш' ? 1 : 0, uncovered] };
    }
    const cmp = (a, b) => (a < b ? -1 : (a > b ? 1 : 0));
    const tail = (a, b) => (a.d - b.d) || (a.rec.e.name.length - b.rec.e.name.length) ||
                           cmp(a.rec.e.name.toLowerCase(), b.rec.e.name.toLowerCase());
    function orderNamed(rows) {                  // А7: quality, then coverage, then the tail
      rows.sort(function (a, b) {
        for (let i = 0; i < a.k.length; i++) if (a.k[i] !== b.k[i]) return a.k[i] - b.k[i];
        return tail(a, b);
      });
      return rows.map((x) => x.rec);
    }
    const orderCategory = (recs, c) =>           // М1: nearest to the centre of the frame first
      recs.map((r) => ({ rec: r, d: distOf(r, c) })).sort(tail).map((x) => x.rec);
    function centre() {
      try { const c = map.getCenter(); if (c && isFinite(c.lat) && isFinite(c.lng)) return c; } catch (e) {}
      return null;
    }
    const distOf = (rec, c) => (c ? Math.hypot((rec.e.lon - c.lng) * MX, (rec.e.lat - c.lat) * MY) : 0);
    function splitKeys(qt) {                     // Т2 + А1 + П4
      const keys = [], slots = [], dead = [];
      let i = 0;
      while (i < qt.length) {
        const form = (len) => qt.slice(i, i + len).map((t) => t.s).join(' ');
        let hit = 0;
        for (let len = Math.min(3, qt.length - i); len > 0 && !hit; len--) {
          const cls = CLASS_OF.get(form(len));
          if (cls && cls.length) { hit = len; keys.push(form(len)); }   // А1: only a populated class
        }
        if (hit) {
          for (let j = 0; j < hit; j++) slots.push({ t: qt[i + j], ki: keys.length - 1 });
          i += hit;
          continue;
        }
        for (let len = Math.min(3, qt.length - i); len > 0; len--)      // П4: a form with an EMPTY class
          if (FORMS.has(form(len))) { for (let j = 0; j < len; j++) dead.push(qt[i + j]); break; }
        slots.push({ t: qt[i], ki: null });
        i++;
      }
      return { keys: keys, slots: slots, dead: dead };
    }
    function runScored(cls, R, hasKey, dead, c) {
      const out = [];
      for (const rec of cls) {
        // П4: such a word is also a FILTER — the row must carry it exactly by name or
        // alias, or a fuzzy coincidence (болница ~ БОНИТА) would pass for proof.
        if (dead.length && !dead.every(function (t) {
          const m = tokenMatch(rec, t);
          return m.q === 3 && (m.cat === 'name' || m.cat === 'alias');
        })) continue;
        const s = scoreRec(rec, R, hasKey);
        if (s.ok) { s.d = distOf(rec, c); out.push(s); }
      }
      return orderNamed(out);
    }
    function search(q) {
      if (!RECS.length) return { category: false, hasKey: false, rows: [] };
      const qt = placeTokens(q);
      if (!qt.length) return { category: false, hasKey: false, rows: [] };
      const c = centre(), sk = splitKeys(qt), hasKey = sk.keys.length > 0;
      let cls = hasKey ? CLASS_OF.get(sk.keys[0]) : RECS;     // А1: the leftmost key is the class
      const R = sk.slots.filter((x) => x.ki !== 0).map((x) => x.t);
      if (!R.length) return { category: true, hasKey: hasKey, rows: orderCategory(cls, c) };  // М1: the key alone
      if (!hasKey) {                             // М3/Б2 generosity gate, PER CLASS (С3)
        cls = cls.filter(genOk);
        if (!cls.length) return { category: false, hasKey: false, rows: [] };
      }
      if (hasKey) {   // ВАРИАНТ Б: филтърът СЕ СЛИВА с именните попадения
        const flt = cls.filter((r) => R.every((t) => r.zkset.has(t.s)));
        if (flt.length) {
          const byName = runScored(cls, R, hasKey, sk.dead, c);
          const seen = new Set(flt);
          const merged = orderCategory(flt, c).concat(byName.filter((r) => !seen.has(r)));
          return { category: true, hasKey: hasKey, rows: merged };
        }
      }
      let rows = runScored(cls, R, hasKey, sk.dead, c);
      if (!rows.length && hasKey)                // А1 fail-open: the keys become plain names
        rows = runScored(RECS, sk.slots.map((x) => x.t), false, sk.dead, c);
      return { category: false, hasKey: hasKey, rows: rows };
    }
    // С1: does THIS text carry a key? A few tokens against the dictionary -- cheap
    // enough to answer SYNCHRONOUSLY on every keystroke, which is what lets the
    // inline remainder go before their 120 ms debounce mutates anything.
    const hasKeyFor = (q) => !!(RECS.length && CLASS_OF && splitKeys(placeTokens(q)).keys.length);

module.exports = { buildIndex, search, splitKeys, placeTokens, tokenMatch, RECSref: () => RECS, CLASSref: () => CLASS_OF };