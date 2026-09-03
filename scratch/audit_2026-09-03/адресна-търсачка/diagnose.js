// Code-level cause for each failure: rebuilds the LIVE scoreEntry (verbatim slice
// 5193-5220 of index.html) inside a rebuilt closure, VALIDATES the replication
// against the numbers the live engine itself puts on every returned row
// (allTokens/matched/exact/prefix/fuzzy), then explains the target's own vector.
'use strict';
const fs = require('fs'), cp = require('child_process');
const E = require('./engine.js');
const HEAD = cp.execSync('git -C C:/git/Fire_Varna rev-parse --short HEAD').toString().trim();
const L = fs.readFileSync('C:/git/Fire_Varna/index.html','utf8').split(/\r?\n/);
function must(re, from, to, what){ for(let i=from;i<=to;i++) if(re.test(L[i-1])) return i; throw new Error('anchor '+what); }
const A = must(/const scored = \[\];/, 5100, 5300, 'scored');
const B = must(/if \(candidateIds\) \{ for \(const id of candidateIds\)/, A, A+60, 'dispatch') - 1;
const SCORE_SRC = L.slice(A-1, B).join('\n');    // verbatim scoreEntry block

const si = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/search_index.json','utf8'));
const ar = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/address_rows.json','utf8'));
const idx = E.setup(si, ar);
const DN = si.district_names || [];

// Rebuild the closure runGeocoderSearch sets up before scoreEntry, then eval the
// verbatim block inside it. Returns scored[] for the entries handed in.
function scoreAll(query, entries){
  const qn = E.norm(query);
  const rawToks = qn.split(/\s+/).filter(Boolean);
  const toks = rawToks.map(E.skel);
  const blIdx = toks.indexOf('bl');
  const qBlk = blIdx >= 0 && blIdx+1 < toks.length ? toks[blIdx+1] : null;
  const av = idx._areaVocab || new Set();
  const areaPresent = qBlk != null && toks.some(function (t) { return t !== 'bl' && t !== 'vh' && t !== qBlk && av.has(t); });
  const blockTyped = qBlk != null && areaPresent;
  const vocab = idx.vocab;
  const ms = toks.map(function (t) { return E.matchKindSet(t, vocab); });
  const numericTok = toks.map(function (t) { return /^[0-9]+$/.test(t); });
  const fn = new Function('toks','ms','numericTok','blockTyped','qBlk','ENTRIES',
    SCORE_SRC + '\nfor (const e of ENTRIES) scoreEntry(e);\nreturn scored;');
  return { scored: fn(toks, ms, numericTok, blockTyped, qBlk, entries), toks: toks, rawToks: rawToks, blockTyped: blockTyped, qBlk: qBlk };
}

// ---- validate the replication against the live engine's own numbers ----------
const probes = ['\u0430\u0442\u0430\u043d\u0430\u0441 \u0434\u0430\u043b\u0447\u0435\u0432 1',
  '\u0431\u043b 307 \u0432\u0445 9', '\u0443\u043b \u043c\u0430\u043a\u0433\u0430\u0445\u0430\u043d 15',
  '\u0432\u043b\u0430\u0434\u0438\u0441\u043b\u0430\u0432 \u0432\u0430\u0440\u043d\u0435\u043d\u0447\u0438\u043a \u0431\u043b 302',
  '\u0431\u0443\u043b \u0446\u0430\u0440 \u043e\u0441\u0432\u043e\u0431\u043e\u0434\u0438\u0442\u0435\u043b 27'];
let checked = 0, mismatch = 0;
for (const q of probes) {
  const rows = E.runGeocoderSearch(q, idx);
  for (const row of rows) {
    // find the index entry the row came from
    const cands = idx.entries.filter(function(e){ return e.kind===row.kind && e.pin && row.pin &&
      e.pin[0]===row.pin[0] && e.pin[1]===row.pin[1] && (e.label==null?null:e.label)===(row.label==null?null:row.label) &&
      (e.display_id==null?null:e.display_id)===(row.display_id==null?null:row.display_id); });
    if (!cands.length) continue;
    const s = scoreAll(q, [cands[0]]).scored[0];
    checked++;
    if (!s || s.all !== row.allTokens || s.matched !== row.matched ||
        (s.exactName + s.exactNum) !== row.exact || s.prefix !== row.prefix || s.fuzzy !== row.fuzzy) {
      mismatch++; console.error('MISMATCH', q, JSON.stringify(row), JSON.stringify(s)); }
  }
}
console.error('replication validated on %d live rows, %d mismatches', checked, mismatch);
if (mismatch) throw new Error('scoreEntry replication does not reproduce the live numbers');

// ---- explain each failure ----------------------------------------------------
const data = JSON.parse(fs.readFileSync('recall_addresses.json','utf8'));
function hitOf(e){ return { kind:e.kind, en:e.en, pin:e.pin, d:e.d, label:e.label, display_id:e.display_id, g:e.g }; }
function findEntry(rec){
  for (const e of idx.entries) {
    if (e.kind !== rec.kind) continue;
    if (!e.pin || e.pin[0] !== rec.pin[0] || e.pin[1] !== rec.pin[1]) continue;
    if (E.formatAddressHit(hitOf(e)) !== rec.label) continue;
    return e;
  }
  return null;
}
function explain(rec, query){
  const e = findEntry(rec); if (!e) return { cause: 'entry-not-refound' };
  const ctx = scoreAll(query, [e]);
  const s = ctx.scored[0];
  const rows = E.runGeocoderSearch(query, idx);
  const top = rows.length ? rows[0] : null, last = rows.length ? rows[rows.length-1] : null;
  const out = { toks: ctx.toks, target: s ? { all:s.all, matched:s.matched, exact:s.exactName+s.exactNum, prefix:s.prefix, fuzzy:s.fuzzy } : null,
                shown_first: top ? { label:E.formatAddressHit(top), all:top.allTokens, matched:top.matched, exact:top.exact, prefix:top.prefix, fuzzy:top.fuzzy } : null,
                shown_last: last ? { label:E.formatAddressHit(last), all:last.allTokens, matched:last.matched, exact:last.exact, prefix:last.prefix, fuzzy:last.fuzzy } : null };
  // which query tokens the target simply does not carry
  const allTok = [].concat(e.tk||[], e.qtk||[], e.alias_tk||[], e.dtk||[], e.stk||[]);
  out.unmatched_tokens = ctx.toks.filter(function(t){
    const m = E.matchKindSet(t, idx.vocab);
    return !allTok.some(function(v){ return (m[v]||0) > 0; });
  });
  out.target_tokens = { tk: e.tk||[], qtk: e.qtk||null, dtk: e.dtk||null, stk: e.stk||null, btk: e.btk||null, alias_tk: e.alias_tk||null };
  if (!s) out.cause = 'no-token-matched-at-all (matched===0 -> never scored)';
  else if (!s.all && last && last.allTokens) out.cause = 'outranked: target misses token(s) ' + JSON.stringify(out.unmatched_tokens) + ' while 8 rows match all';
  else if (s.all && last && last.allTokens && s.matched === last.matched && (s.exactName+s.exactNum) === last.exact && s.prefix === last.prefix)
    out.cause = 'TIE cut off by SEARCH_LIMIT=8 (equal score; order decided by tk-length then _ord)';
  else out.cause = 'outranked on the comparator (see vectors)';
  // how many entries score at least as well (equal-or-better on the first 4 slots)
  if (s) {
    const all = scoreAll(query, idx.entries).scored;
    let better = 0, equal = 0;
    for (const o of all) {
      if (o.e === e) continue;
      if (o.all !== s.all) { if (o.all) better++; continue; }
      if (o.matched !== s.matched) { if (o.matched > s.matched) better++; continue; }
      const oe = o.exactName+o.exactNum, se = s.exactName+s.exactNum;
      if (oe !== se) { if (oe > se) better++; continue; }
      if (o.prefix !== s.prefix) { if (o.prefix > s.prefix) better++; continue; }
      equal++;
    }
    out.competitors = { strictly_better: better, equal_score: equal };
  }
  return out;
}

const worst = JSON.parse(fs.readFileSync('worst30.json','utf8')).worst30.map(function(w){ const ex = explain(w, w.query); return Object.assign({}, w, { diag: ex }); });
fs.writeFileSync('worst30_diagnosed.json', JSON.stringify({ head: HEAD, score_slice: A + '-' + B, validated_rows: checked, worst: worst }, null, 1));
console.log('written worst30_diagnosed.json; causes:');
const cc = {}; for (const w of worst) cc[w.diag.cause] = (cc[w.diag.cause]||0)+1;
console.log(JSON.stringify(cc, null, 1));
