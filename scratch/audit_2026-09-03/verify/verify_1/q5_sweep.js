// Sweep: for EVERY record, search its own exact name. How many are absent / not in TOP-8?
const api = require('./harness.js');
const recs = api.recs();
const out = [];
for (const rec of recs) {
  const r = api.search(rec.e.name);
  const i = r.rows.indexOf(rec);
  out.push({ name: rec.e.name, kind: rec.e.kind, zone: rec.e.zone,
             n: r.rows.length, category: r.category, rank: i < 0 ? null : i + 1 });
}
const missing = out.filter((x) => x.rank === null);
const past8 = out.filter((x) => x.rank !== null && x.rank > 8);
console.log('total records          :', out.length);
console.log('ABSENT for own name    :', missing.length);
for (const m of missing) console.log('   ABSENT', JSON.stringify(m));
console.log('present but rank > 8   :', past8.length);
for (const m of past8) console.log('   >8', JSON.stringify(m));
const catBranch = out.filter((x) => x.category);
console.log('own name lands on the CATEGORY branch:', catBranch.length);
for (const m of catBranch) console.log('   CAT', JSON.stringify(m));
require('fs').writeFileSync('q5_sweep_rows.json', JSON.stringify(out, null, 1));
