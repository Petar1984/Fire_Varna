// (2) Sweep all 361 records: is a record findable by typing its OWN name verbatim?
// TOP semantics of the live UI: TOP=8 per group, TOP_TOTAL=16 overall (render cap).
const H = require('./harness.js');
const rows = [];
for (const rec of H.RECS) {
  const r = H.search(rec.e.name);
  const idx = r.rows.indexOf(rec);
  rows.push({ name: rec.e.name, kind: rec.e.kind, zone: rec.e.zone,
              category: r.category, n: r.rows.length, rank: idx < 0 ? null : idx + 1 });
}
const miss = rows.filter(x => x.rank === null);
console.log('total records      =', rows.length);
console.log('NOT found by own name =', miss.length);
for (const m of miss) console.log('  MISS:', JSON.stringify(m));
const cat = rows.filter(x => x.category);
console.log('own name lands on the CATEGORY branch:', cat.length);
for (const c of cat) console.log('  CAT:', JSON.stringify(c));
const deep = rows.filter(x => x.rank !== null && x.rank > 8);
console.log('found but below rank 8 (out of the visible list):', deep.length);
for (const d of deep) console.log('  DEEP:', JSON.stringify(d));
require('fs').writeFileSync(__dirname + '/own_name_sweep.json', JSON.stringify(rows, null, 1), 'utf8');
