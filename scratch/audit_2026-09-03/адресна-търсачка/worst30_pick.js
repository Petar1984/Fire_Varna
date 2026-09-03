// Re-picks the 30 heaviest failures from recall_addresses.json, ONE PER RENDERED
// LABEL (the first run's list was swamped by 16 copies of a single label).
'use strict';
const fs = require('fs');
const d = JSON.parse(fs.readFileSync('recall_addresses.json','utf8'));
const QN = ['Q1','Q2','Q3','Q4a','Q4b'];
const fails = [];
for (const r of d.records) for (const q of QN) {
  const m = r.q[q]; if (!m || m.skipped) continue;
  if (m.labelRank < 0) {
    const sev = q==='Q1'?0 : q==='Q2'?1 : (q==='Q4a'||q==='Q4b')?2 : 4;
    fails.push({ sev: sev, qname: q, rec: r, m: m, why: 'label-not-in-dropdown' });
  } else if (q==='Q1' && m.rank<0 && m.labelDist_m!=null && m.labelDist_m>200) {
    fails.push({ sev: 3, qname: q, rec: r, m: m, why: 'same-label-other-pin-' + m.labelDist_m + 'm' });
  }
}
fails.sort(function(a,b){ return a.sev-b.sev || a.rec.label.localeCompare(b.rec.label,'bg') || a.rec.key.localeCompare(b.rec.key); });
const seen = new Set(); const picked = [];
for (const f of fails) { const k = f.rec.label + '||' + f.qname; if (seen.has(k)) continue; seen.add(k); picked.push(f); if (picked.length>=30) break; }
const worst30 = picked.map(function(f){ return { sev:f.sev, why:f.why, qname:f.qname, group:f.rec.group,
  kind:f.rec.kind, raion:f.rec.raion, label:f.rec.label, pin:f.rec.pin, query:f.m.q, n_ded:f.m.n_ded,
  rank:f.m.rank, rawRank:f.m.rawRank, labelRank:f.m.labelRank, labelDist_m:f.m.labelDist_m,
  folded:!!f.m.folded, fold_reason:f.m.fold_reason||null, absorbed_by:f.m.absorbed_by||null,
  fold_dist_m:(f.m.fold_dist_m===undefined?null:f.m.fold_dist_m), top1:f.m.top1 }; });
// how many DISTINCT labels are behind each severity
const distinct = {};
for (const f of fails) { distinct[f.sev] = distinct[f.sev] || new Set(); distinct[f.sev].add(f.rec.label); }
const distinctCounts = {}; for (const s in distinct) distinctCounts[s] = distinct[s].size;
fs.writeFileSync('worst30.json', JSON.stringify({ head: d.summary.head, total_fail_rows: fails.length,
  distinct_labels_by_sev: distinctCounts, worst30: worst30 }, null, 1));
console.log('total fail rows', fails.length, 'distinct labels by sev', JSON.stringify(distinctCounts));
