// RECALL of the LIVE address path (initAddressSearch) over data/search_index.json
// + data/address_rows.json. Engine = engine.js (verbatim slices of index.html).
// Deterministic: fixed seed, no Date/Math.random in any decision.
'use strict';
const fs = require('fs'), cp = require('child_process');
const E = require('./engine.js');

const SEED = 20260903;                      // fixed, recorded
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function sampleDet(arr, n, seed){            // deterministic Fisher-Yates over indices
  const rnd = mulberry32(seed); const ix = arr.map(function(_,i){return i;});
  for (let i = ix.length - 1; i > 0; i--) { const j = Math.floor(rnd()*(i+1)); const t=ix[i]; ix[i]=ix[j]; ix[j]=t; }
  return ix.slice(0, Math.min(n, ix.length)).sort(function(a,b){return a-b;}).map(function(i){return arr[i];});
}
const HEAD = cp.execSync('git -C C:/git/Fire_Varna rev-parse --short HEAD').toString().trim();

const si = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/search_index.json','utf8'));
const ar = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/address_rows.json','utf8'));
const idx = E.setup(si, ar);
const DN = si.district_names || [];

// ---- record identity: what a result row can carry back -----------------------
function keyOf(e){ return [e.kind, e.pin?e.pin[0]:'', e.pin?e.pin[1]:'',
                    (e.en===undefined||e.en===null)?'':e.en,
                    e.label==null?'':e.label,
                    e.display_id==null?'':e.display_id].join('|'); }
function hitOf(e){ return { kind:e.kind, en:e.en, pin:e.pin, d:e.d, label:e.label, display_id:e.display_id, g:e.g }; }

function hav(a,b){const R=6371000,r=Math.PI/180;const dl=(b[0]-a[0])*r,dg=(b[1]-a[1])*r;
  const x=Math.pow(Math.sin(dl/2),2)+Math.cos(a[0]*r)*Math.cos(b[0]*r)*Math.pow(Math.sin(dg/2),2);
  return 2*R*Math.asin(Math.sqrt(x));}

// ---- query builders ----------------------------------------------------------
function stripTypeWords(s){
  let t = String(s).replace(/["'\u00ab\u00bb\u201c\u201d\u201e]/g,' ');
  t = t.replace(/\u0436\s*\.?\s*\u043a\s*\.?/gi,' ');            // "ж.к." / "жк"
  t = t.replace(/\u0430\u0434\u0440\u0435\u0441:\s*/gi,' ');      // "адрес:"
  const out = t.split(/\s+/).filter(Boolean).filter(function(w){
    const w2 = w.replace(/[.,]/g,'').toLowerCase();
    return !(w2==='\u0443\u043b'||w2==='\u0431\u0443\u043b'||w2==='\u043a\u0432'||w2==='\u0436\u043a'||w2==='\u0436'||w2==='\u043a'||w2==='\u043c');
  });
  return out.join(' ').replace(/\s+/g,' ').trim();
}
function dropTrailingNumber(s){
  const t=s.split(/\s+/).filter(Boolean); let end=t.length;
  while(end>0 && /^[0-9]+[\u0430-\u044fa-z]?$/i.test(t[end-1])) end--;
  return t.slice(0,end).join(' ').trim();
}
function blockNumFromLabel(label){       // display block number ("307") out of a rendered label
  const t = String(label).replace(/[.,\u00b7]/g,' ').split(/\s+/).filter(Boolean);
  for (let i=0;i<t.length;i++){ const w=t[i].toLowerCase();
    if ((w==='\u0431\u043b'||w==='\u0431\u043b\u043e\u043a'||w==='bl') && i+1<t.length && /[0-9]/.test(t[i+1])) return t[i+1]; }
  return null;
}
const BG2LAT={'\u0430':'a','\u0431':'b','\u0432':'v','\u0433':'g','\u0434':'d','\u0435':'e','\u0436':'zh','\u0437':'z','\u0438':'i','\u0439':'y','\u043a':'k','\u043b':'l','\u043c':'m','\u043d':'n','\u043e':'o','\u043f':'p','\u0440':'r','\u0441':'s','\u0442':'t','\u0443':'u','\u0444':'f','\u0445':'h','\u0446':'ts','\u0447':'ch','\u0448':'sh','\u0449':'sht','\u044a':'a','\u044c':'y','\u044e':'yu','\u044f':'ya'};
const ERR = {
  // "без диакритика": ъ/ь dropped, й -> и (the way people type in a hurry)
  noyer: function(s){ return s.replace(/\u044a/g,'').replace(/\u044c/g,'').replace(/\u0439/g,'\u0438'); },
  latin: function(s){ return s.toLowerCase().split('').map(function(c){return BG2LAT[c]!==undefined?BG2LAT[c]:c;}).join(''); },
  swap:  function(s){ const t=s.split(/\s+/).filter(Boolean); return t.length<2?s:[t[t.length-1]].concat(t.slice(0,t.length-1)).join(' '); },
  nonum: function(s){ return dropTrailingNumber(s); },
  typo:  function(s){ const t=s.split(/\s+/).filter(Boolean); if(!t.length) return s;
                 let bi=0; for(let i=1;i<t.length;i++) if(t[i].length>t[bi].length) bi=i;
                 const w=t[bi]; if(w.length<4) return s; t[bi]=w.slice(0,2)+w.slice(3); return t.join(' '); }
};

// ---- one measurement ---------------------------------------------------------
function measure(target, q){
  const tk = keyOf(target);
  const raw = E.runGeocoderSearch(q, idx);
  const ded = E.dedupeDisplayRows(raw);
  const rawKeys = raw.map(keyOf), dedKeys = ded.map(keyOf);
  const rank = dedKeys.indexOf(tk);
  const rawRank = rawKeys.indexOf(tk);
  const tLabel = E.formatAddressHit(hitOf(target));
  const r = { q: q, n_raw: raw.length, n_ded: ded.length, rank: rank, rawRank: rawRank,
              top1: ded.length ? E.formatAddressHit(ded[0]) : null };
  // LABEL recall: the человек cannot tell two records with the SAME rendered label
  // apart, so also record the first row whose rendered label equals the target's,
  // and how far its pin is from the true record.
  const nl = E.norm(tLabel);
  r.labelRank = -1; r.labelDist_m = null;
  for (let i = 0; i < ded.length; i++) {
    if (E.norm(E.formatAddressHit(ded[i])) === nl) {
      r.labelRank = i;
      r.labelDist_m = (ded[i].pin && target.pin) ? Math.round(hav(target.pin, ded[i].pin)) : null;
      break;
    }
  }
  if (rank < 0 && rawRank >= 0) {                       // folded away by dedupeDisplayRows
    r.folded = true;
    const lab = E.norm(tLabel) + '||' + (target.g!=null?String(target.g):'');
    let absorber = null;
    for (const row of ded) {
      const rl = E.norm(E.formatAddressHit(row)) + '||' + (row.g!=null?String(row.g):'');
      if (rl === lab) { absorber = row; r.fold_reason = 'identical-rendered-row'; break; }
    }
    if (!absorber && target.kind === 'address') {
      const bn = E.labelBlockNumber(tLabel);
      for (const row of ded) if (row.kind==='mf' && (row.en==null) && E.labelBlockNumber(E.formatAddressHit(row))===bn) {
        absorber = row; r.fold_reason='address-suppressed-by-sgrada'; break; }
    }
    if (absorber) { r.absorbed_by = E.formatAddressHit(absorber);
                    r.fold_dist_m = (target.pin&&absorber.pin)?Math.round(hav(target.pin,absorber.pin)):null; }
    else if (!r.fold_reason) r.fold_reason = 'unknown';
  }
  if (ded.length && rank !== 0) {                       // is row 1 the SAME label on ANOTHER pin?
    const t0 = ded[0];
    if (E.norm(E.formatAddressHit(t0)) === E.norm(tLabel) && t0.pin && target.pin) {
      const d = hav(target.pin, t0.pin);
      if (d > 0.5) { r.first_same_label_other_pin = true; r.first_dist_m = Math.round(d); }
    }
  }
  return r;
}

// ---- sample ------------------------------------------------------------------
const ents = idx.entries;
const poolAddr = ents.filter(function(e){ return (e.kind==='address' || e.kind==='mf') && (e.en===undefined||e.en===null); });
const poolEnt  = ents.filter(function(e){ return e.en!==undefined && e.en!==null; });
const poolPar  = ents.filter(function(e){ return e.kind==='parcel'; });
const S_ADDR = sampleDet(poolAddr, 2000, SEED);
const S_ENT  = sampleDet(poolEnt , 500 , SEED+1);
const S_PAR  = poolPar.slice();                          // ALL parcels
console.error('pools addr=%d ent=%d parcel=%d | sample %d/%d/%d',
  poolAddr.length, poolEnt.length, poolPar.length, S_ADDR.length, S_ENT.length, S_PAR.length);

const recs = [];
function runGroup(list, group){
  for (const e of list) {
    const hit = hitOf(e);
    const label = E.formatAddressHit(hit);
    const q1 = label;
    const q2 = stripTypeWords(label);
    const q3 = dropTrailingNumber(q2);
    const rec = { group: group, kind: e.kind, d: e.d, raion: (e.d!=null&&DN[e.d])?DN[e.d]:null,
                  pin: e.pin, label: label, key: keyOf(e), latinLabel: !/[\u0410-\u044f]/.test(label),
                  q: {} };
    rec.q.Q1 = measure(e, q1);
    rec.q.Q2 = (q2 && q2 !== q1) ? measure(e, q2) : { skipped: (q2===q1 ? 'identical-to-Q1' : 'empty'), q: q2 };
    rec.q.Q3 = (q3 && q3 !== q2) ? measure(e, q3) : { skipped: (q3===q2 ? 'no-number-to-drop' : 'empty'), q: q3 };
    if (group === 'entrance') {
      const bn = blockNumFromLabel(label), en = e.en;
      const base = q2.replace(/\s*\u00b7\s*\u0432\u0445\.?\s*\S+$/,'').trim();   // strip " · вх. N"
      const q4a = bn ? ('\u0431\u043b. ' + bn + ' \u0432\u0445. ' + en) : null;
      const q4b = base ? (base + ' \u0432\u0445. ' + en) : null;
      rec.q.Q4a = q4a ? measure(e, q4a) : { skipped: 'no-block-number-in-label' };
      rec.q.Q4b = (q4b && q4b !== q4a) ? measure(e, q4b) : { skipped: 'no-base-or-same-as-Q4a' };
    }
    recs.push(rec);
  }
}
runGroup(S_ADDR,'address'); console.error('addr done');
runGroup(S_ENT ,'entrance'); console.error('ent done');
runGroup(S_PAR ,'parcel'); console.error('parcel done');

// ---- Q5: 20 typical mistakes (4 real targets x 5 error families) -------------
// targets picked deterministically: first mf entry (по _ord) with a Cyrillic label,
// one per район.
const q5targets = [];
{ const seenD = {};
  for (const e of ents) {
    if (e.kind !== 'mf' || (e.en!==undefined && e.en!==null)) continue;
    if (!e.label || !/[\u0410-\u044f]/.test(e.label)) continue;
    if (e.d == null || seenD[e.d]) continue;
    seenD[e.d] = 1; q5targets.push(e);
    if (q5targets.length >= 4) break;
  } }
const q5 = [];
for (const t of q5targets) {
  const label = E.formatAddressHit(hitOf(t));
  const base = stripTypeWords(label);
  for (const fam of ['noyer','latin','swap','nonum','typo']) {
    const q = ERR[fam](base);
    const m = measure(t, q);
    m.family = fam; m.target_label = label; m.target_raion = t.d!=null?DN[t.d]:null; m.base = base;
    q5.push(m);
  }
}

// ---- aggregate ---------------------------------------------------------------
function agg(sel, qname){
  const out = { n:0, at1:0, at3:0, at8:0, notShown:0, folded:0, firstOtherPin:0, skipped:0,
                lab1:0, lab3:0, lab8:0, labNotShown:0, labFar50:0, labFar200:0 };
  for (const r of recs) { if (!sel(r)) continue; const m = r.q[qname]; if (!m) continue;
    if (m.skipped) { out.skipped++; continue; }
    out.n++;
    if (m.rank===0) out.at1++;
    if (m.rank>=0 && m.rank<3) out.at3++;
    if (m.rank>=0 && m.rank<8) out.at8++;
    if (m.rank<0) out.notShown++;
    if (m.folded) out.folded++;
    if (m.first_same_label_other_pin) out.firstOtherPin++;
    if (m.labelRank===0) out.lab1++;
    if (m.labelRank>=0 && m.labelRank<3) out.lab3++;
    if (m.labelRank>=0 && m.labelRank<8) out.lab8++;
    if (m.labelRank<0) out.labNotShown++;
    if (m.labelRank>=0 && m.labelDist_m!=null && m.labelDist_m>50) out.labFar50++;
    if (m.labelRank>=0 && m.labelDist_m!=null && m.labelDist_m>200) out.labFar200++;
  }
  ['at1','at3','at8','notShown','folded','firstOtherPin','lab1','lab3','lab8','labNotShown','labFar50','labFar200']
    .forEach(function(k){ out[k+'_pct'] = out.n? +(100*out[k]/out.n).toFixed(2) : null; });
  return out;
}
const QN = ['Q1','Q2','Q3','Q4a','Q4b'];
const summary = { head: HEAD, seed: SEED, engine_anchors: E.anchors, SEARCH_LIMIT: E.SEARCH_LIMIT,
  pools: { address_mf_nonentrance: poolAddr.length, entrance: poolEnt.length, parcel: poolPar.length },
  sample: { address: S_ADDR.length, entrance: S_ENT.length, parcel: S_PAR.length },
  by_query: {}, by_group: {}, by_raion: {}, by_kind: {} };
for (const q of QN) summary.by_query[q] = agg(function(){return true;}, q);
for (const g of ['address','entrance','parcel'])
  for (const q of QN) { summary.by_group[g] = summary.by_group[g]||{}; summary.by_group[g][q] = agg(function(r){return r.group===g;}, q); }
for (const dn of DN.concat([null])) {
  const kk = dn===null?'(без район)':dn;
  for (const q of ['Q1','Q2','Q3']) { summary.by_raion[kk] = summary.by_raion[kk]||{}; summary.by_raion[kk][q] = agg(function(r){return r.raion===dn;}, q); }
}
for (const k of ['address','mf','parcel'])
  for (const q of ['Q1','Q2','Q3']) { summary.by_kind[k] = summary.by_kind[k]||{}; summary.by_kind[k][q] = agg(function(r){return r.kind===k;}, q); }
summary.latin_label_share = { sampled: recs.length, latin: recs.filter(function(r){return r.latinLabel;}).length };

// worst 30 — severity by what the человек actually loses:
//  0: Q1 typed verbatim, NOTHING with that label shown at all
//  1: Q2 (street+number, no type word), nothing with that label shown
//  2: Q4a/Q4b entrance query, nothing with that label shown
//  3: Q1 shows the label but on a pin >200 m from the real record
//  4: Q3 street-only, nothing with that label shown
const fails = [];
for (const r of recs) for (const q of QN) {
  const m = r.q[q]; if (!m || m.skipped) continue;
  if (m.labelRank < 0) {
    const sev = q==='Q1'?0 : q==='Q2'?1 : (q==='Q4a'||q==='Q4b')?2 : 4;
    fails.push({ sev: sev, qname: q, rec: r, m: m, why: 'label-not-in-dropdown' });
  } else if (q==='Q1' && m.rank<0 && m.labelDist_m!=null && m.labelDist_m>200) {
    fails.push({ sev: 3, qname: q, rec: r, m: m, why: 'same-label-other-pin-' + m.labelDist_m + 'm' });
  }
}
fails.sort(function(a,b){ return a.sev-b.sev || a.rec.label.localeCompare(b.rec.label,'bg') || a.rec.key.localeCompare(b.rec.key); });
const worst30 = fails.slice(0,30).map(function(f){ return { sev:f.sev, why:f.why, qname:f.qname,
  group:f.rec.group, kind:f.rec.kind, raion:f.rec.raion, label:f.rec.label, pin:f.rec.pin,
  query:f.m.q, n_ded:f.m.n_ded, rank:f.m.rank, rawRank:f.m.rawRank, labelRank:f.m.labelRank,
  labelDist_m:f.m.labelDist_m, folded:!!f.m.folded, fold_reason:f.m.fold_reason||null,
  absorbed_by:f.m.absorbed_by||null, fold_dist_m:(f.m.fold_dist_m===undefined?null:f.m.fold_dist_m),
  top1:f.m.top1 }; });
summary.fail_counts = { total_fail_rows: fails.length,
  byQ: fails.reduce(function(a,f){ a[f.qname]=(a[f.qname]||0)+1; return a; }, {}),
  bySev: fails.reduce(function(a,f){ a[f.sev]=(a[f.sev]||0)+1; return a; }, {}) };

// ---- label ambiguity over the WHOLE index (why record-recall != label-recall) --
{
  const byLabel = new Map();
  for (const e of ents) { const l = E.norm(E.formatAddressHit(hitOf(e)));
    let a = byLabel.get(l); if (!a) byLabel.set(l, (a = [])); a.push(e); }
  let dup = 0, maxN = 0, maxLabel = null, spread200 = 0, spread1000 = 0;
  const worstSpread = [];
  for (const pair of byLabel) {
    const l = pair[0], a = pair[1];
    if (a.length > 1) dup += a.length;
    if (a.length > maxN) { maxN = a.length; maxLabel = l; }
    if (a.length > 1) {
      let mx = 0, pa = null, pb = null;
      const cap = Math.min(a.length, 40);           // bounded pairwise probe (deterministic prefix)
      for (let i=0;i<cap;i++) for (let j=i+1;j<cap;j++) {
        if (!a[i].pin || !a[j].pin) continue;
        const d = hav(a[i].pin, a[j].pin); if (d > mx) { mx = d; pa=a[i]; pb=a[j]; } }
      if (mx > 200) spread200++;
      if (mx > 1000) { spread1000++; worstSpread.push({ label: E.formatAddressHit(hitOf(a[0])), n: a.length,
        spread_m: Math.round(mx), pinA: pa?pa.pin:null, pinB: pb?pb.pin:null,
        raionA: pa&&pa.d!=null?DN[pa.d]:null, raionB: pb&&pb.d!=null?DN[pb.d]:null }); }
    }
  }
  worstSpread.sort(function(a,b){ return b.spread_m - a.spread_m || a.label.localeCompare(b.label,'bg'); });
  summary.label_ambiguity = { entries: ents.length, distinct_labels: byLabel.size,
    entries_in_duplicated_labels: dup, biggest_cluster: maxN, biggest_cluster_label: maxLabel,
    dup_labels_spread_gt_200m: spread200, dup_labels_spread_gt_1000m: spread1000 };
  summary.label_ambiguity_worst = worstSpread.slice(0, 15);
}

fs.writeFileSync('recall_addresses.json', JSON.stringify({ summary: summary, q5: q5, worst30: worst30, records: recs }, null, 1));
fs.writeFileSync('recall_summary_only.json', JSON.stringify({ summary: summary, q5: q5, worst30: worst30 }, null, 1));
console.log(JSON.stringify(summary.by_query, null, 1));
