// Controlled A/B probes for the causes the worst-30 diagnosis surfaced, plus the
// global counts behind them. Read-only; deterministic (same seed/sample as the
// main run, reconstructed from recall_addresses.json).
'use strict';
const fs = require('fs'), cp = require('child_process');
const E = require('./engine.js');
const HEAD = cp.execSync('git -C C:/git/Fire_Varna rev-parse --short HEAD').toString().trim();
const si = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/search_index.json','utf8'));
const ar = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/address_rows.json','utf8'));
const idx = E.setup(si, ar);
const DN = si.district_names || [];
const D = JSON.parse(fs.readFileSync('recall_addresses.json','utf8'));
function hitOf(e){ return { kind:e.kind, en:e.en, pin:e.pin, d:e.d, label:e.label, display_id:e.display_id, g:e.g }; }
function keyOf(e){ return [e.kind, e.pin?e.pin[0]:'', e.pin?e.pin[1]:'',
  (e.en===undefined||e.en===null)?'':e.en, e.label==null?'':e.label,
  e.display_id==null?'':e.display_id].join('|'); }
const byKey = new Map();
for (const e of idx.entries) { const k = keyOf(e); if (!byKey.has(k)) byKey.set(k, e); }

function rankOf(target, q){
  const raw = E.runGeocoderSearch(q, idx);
  const ded = E.dedupeDisplayRows(raw);
  const tk = keyOf(target);
  const r = ded.map(keyOf).indexOf(tk);
  const nl = E.norm(E.formatAddressHit(hitOf(target)));
  let lr = -1; for (let i=0;i<ded.length;i++) if (E.norm(E.formatAddressHit(ded[i]))===nl) { lr=i; break; }
  return { rank: r, labelRank: lr };
}
function tally(pairs){                       // pairs: [{a:{rank},b:{rank}}]
  const o = { n: pairs.length, a1:0, a8:0, b1:0, b8:0, aL8:0, bL8:0, improved:0, worsened:0 };
  for (const p of pairs) {
    if (p.a.rank===0) o.a1++; if (p.a.rank>=0&&p.a.rank<8) o.a8++;
    if (p.b.rank===0) o.b1++; if (p.b.rank>=0&&p.b.rank<8) o.b8++;
    if (p.a.labelRank>=0&&p.a.labelRank<8) o.aL8++;
    if (p.b.labelRank>=0&&p.b.labelRank<8) o.bL8++;
    const ra = p.a.rank<0?99:p.a.rank, rb = p.b.rank<0?99:p.b.rank;
    if (rb<ra) o.improved++; if (rb>ra) o.worsened++;
  }
  ['a1','a8','b1','b8','aL8','bL8'].forEach(function(k){ o[k+'_pct'] = o.n? +(100*o[k]/o.n).toFixed(2):null; });
  return o;
}

const out = { head: HEAD, probes: {}, globals: {}, examples: {} };

// ---- E1: the middle dot "·" that formatAddressHit itself prints --------------
// The engine renders an entrance as base + ' · вх. ' + en, but norm()'s strip class
// is [.№,'"-] — "·" survives as its own query token that no index token can match.
out.globals.norm_keeps_middle_dot = E.norm('\u0430 \u00b7 \u0431') ;      // -> "а · б"
out.globals.skel_of_middle_dot = E.skel('\u00b7');
{
  const pairs = [], ex = [];
  for (const r of D.records) { if (r.group !== 'entrance') continue;
    const t = byKey.get(r.key); if (!t) continue;
    const q1 = r.label;
    const q1nodot = r.label.replace(/\s*\u00b7\s*/g, ' ').replace(/\s+/g,' ').trim();
    if (q1nodot === q1) continue;
    const a = rankOf(t, q1), b = rankOf(t, q1nodot);
    pairs.push({ a:a, b:b });
    if (a.rank !== b.rank && ex.length < 8) ex.push({ label:r.label, raion:r.raion, pin:r.pin,
      q_with_dot:q1, rank_with_dot:a.rank, q_no_dot:q1nodot, rank_no_dot:b.rank });
  }
  out.probes.E1_middle_dot = tally(pairs); out.examples.E1_middle_dot = ex;
}

// ---- E2: the type word ("ж.к." -> tokens "zh"+"k", "кв." -> "kv") ------------
{
  const pairs = [], ex = [];
  const RX = /(\u0436\s*\.?\s*\u043a\s*\.?|\u043a\s*\.?\s*\u043a\s*\.?|\u043a\u0432\.?|\u0432\.\u0437\.?)/gi;   // ж.к. к.к. кв. в.з.
  for (const r of D.records) {
    if (!RX.test(r.label)) { RX.lastIndex = 0; continue; } RX.lastIndex = 0;
    const t = byKey.get(r.key); if (!t) continue;
    const q1 = r.label, q2 = r.label.replace(RX,' ').replace(/\s+/g,' ').replace(/^[,\s]+/,'').trim();
    if (q2 === q1 || !q2) continue;
    const a = rankOf(t, q1), b = rankOf(t, q2);
    pairs.push({ a:a, b:b });
    if (a.rank !== b.rank && ex.length < 8) ex.push({ label:r.label, raion:r.raion, pin:r.pin,
      q_with_type:q1, rank_with_type:a.rank, q_without_type:q2, rank_without_type:b.rank });
  }
  out.probes.E2_type_word = tally(pairs); out.examples.E2_type_word = ex;
}

// ---- E3: "Адрес:" leaked into the display label ------------------------------
{
  const pairs = [], ex = [];
  for (const r of D.records) {
    if (!/\u0410\u0434\u0440\u0435\u0441:/i.test(r.label)) continue;
    const t = byKey.get(r.key); if (!t) continue;
    const q1 = r.label, q2 = r.label.replace(/\u0410\u0434\u0440\u0435\u0441:\s*/gi,'').replace(/\s+/g,' ').trim();
    const a = rankOf(t, q1), b = rankOf(t, q2);
    pairs.push({ a:a, b:b });
    if (ex.length < 8) ex.push({ label:r.label, raion:r.raion, pin:r.pin, rank_as_shown:a.rank, rank_cleaned:b.rank });
  }
  out.probes.E3_adres_prefix = tally(pairs); out.examples.E3_adres_prefix = ex;
}

// ---- globals over the WHOLE index --------------------------------------------
{
  let latin=0, dot=0, adres=0, bareType=0, mixed=0, gorod=0;
  const exLatin=[], exAdres=[], exMixed=[], exBare=[];
  for (const e of idx.entries) {
    const l = E.formatAddressHit(hitOf(e));
    const hasCyr = /[\u0410-\u044f]/.test(l), hasLat = /[a-zA-Z]/.test(l);
    if (!hasCyr) { latin++; if (exLatin.length<8) exLatin.push({label:l,kind:e.kind,raion:e.d!=null?DN[e.d]:null,pin:e.pin}); }
    else if (hasLat) { mixed++; if (exMixed.length<8) exMixed.push({label:l,kind:e.kind,raion:e.d!=null?DN[e.d]:null,pin:e.pin}); }
    if (l.indexOf('\u00b7') >= 0) dot++;
    if (/\u0410\u0434\u0440\u0435\u0441:/i.test(l)) { adres++; if (exAdres.length<8) exAdres.push({label:l,kind:e.kind,raion:e.d!=null?DN[e.d]:null,pin:e.pin}); }
    if (/^(\u0443\u043b|\u0431\u0443\u043b|\u043a\u0432|\u0436\.?\u043a\.?|\u043c)\.?$/i.test(l.trim())) { bareType++; if (exBare.length<8) exBare.push({label:l,kind:e.kind,raion:e.d!=null?DN[e.d]:null,pin:e.pin}); }
    if (/^\u0433\u0440\s+\u0432\u0430\u0440\u043d\u0430\s+\u0440\u0430\u0439\u043e\u043d/i.test(l)) gorod++;
  }
  out.globals.entries = idx.entries.length;
  out.globals.label_latin_only = latin;
  out.globals.label_mixed_cyr_latin = mixed;
  out.globals.label_with_middle_dot = dot;
  out.globals.label_with_adres_prefix = adres;
  out.globals.label_bare_typeword = bareType;
  out.globals.label_gr_varna_raion_prefix = gorod;
  out.examples.latin_labels = exLatin;
  out.examples.mixed_labels = exMixed;
  out.examples.adres_labels = exAdres;
  out.examples.bare_typeword_labels = exBare;
}

// ---- E4: folding — what dedupeDisplayRows removes, and how far away ----------
{
  const dists = [], ex = [], reasons = {};
  for (const r of D.records) for (const q of ['Q1','Q2','Q3','Q4a','Q4b']) {
    const m = r.q[q]; if (!m || m.skipped || !m.folded) continue;
    reasons[m.fold_reason||'?'] = (reasons[m.fold_reason||'?']||0)+1;
    if (m.fold_dist_m != null) dists.push(m.fold_dist_m);
    if (q==='Q1' && m.fold_dist_m != null && m.fold_dist_m > 100 && ex.length < 8)
      ex.push({ label:r.label, raion:r.raion, pin:r.pin, query:m.q, reason:m.fold_reason,
                absorbed_by:m.absorbed_by, dist_m:m.fold_dist_m });
  }
  dists.sort(function(a,b){return a-b;});
  const pct = function(p){ return dists.length? dists[Math.min(dists.length-1, Math.floor(p*dists.length))] : null; };
  out.probes.E4_folding = { folded_rows: Object.values(reasons).reduce(function(a,b){return a+b;},0),
    reasons: reasons, dist_m: { n: dists.length, p50: pct(0.5), p90: pct(0.9), max: dists.length?dists[dists.length-1]:null,
      over_100m: dists.filter(function(d){return d>100;}).length, over_500m: dists.filter(function(d){return d>500;}).length } };
  out.examples.folded_far = ex;
}

// ---- E5: "first row is ANOTHER pin under the same label" ----------------------
{
  const ds = [], ex = [];
  for (const r of D.records) { const m = r.q.Q1; if (!m || m.skipped) continue;
    if (m.rank < 0 && m.labelRank >= 0 && m.labelDist_m != null) { ds.push(m.labelDist_m);
      if (m.labelDist_m > 500 && ex.length < 8) ex.push({ label:r.label, raion:r.raion, kind:r.kind,
        true_pin:r.pin, shown_at:m.labelRank, dist_m:m.labelDist_m, query:m.q }); } }
  ds.sort(function(a,b){return a-b;});
  const pct = function(p){ return ds.length? ds[Math.min(ds.length-1, Math.floor(p*ds.length))] : null; };
  out.probes.E5_same_label_other_pin = { n: ds.length, p50: pct(0.5), p90: pct(0.9),
    max: ds.length?ds[ds.length-1]:null, over_200m: ds.filter(function(d){return d>200;}).length,
    over_1000m: ds.filter(function(d){return d>1000;}).length };
  out.examples.same_label_other_pin_far = ex;
}

fs.writeFileSync('extra_measures.json', JSON.stringify(out, null, 1));
console.log(JSON.stringify({ globals: out.globals, probes: out.probes }, null, 1));
