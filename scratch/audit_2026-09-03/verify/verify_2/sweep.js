// For each of the 157 cross-building duplicate-label groups, fire the NATURAL query
// (the rendered label itself, "·" removed) and count identical rendered rows that
// survive dedupeDisplayRows in one dropdown. Read-only.
const fs = require('fs');
let addressRows = null, addrFieldIdx = null, districtNames = [];
eval(fs.readFileSync(__dirname + '/_extract.js', 'utf8'));
const idx = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/search_index.json', 'utf8'));
const rp = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/address_rows.json', 'utf8'));
addressRows = rp.rows; addrFieldIdx = buildAddressFieldIndex(rp); districtNames = idx.district_names || [];
prepareIndex(idx);

const E = idx.entries;
const lab = new Map();
for (let i = 0; i < E.length; i++) {
  if (E[i].en == null) continue;
  const L = formatAddressHit(E[i]);
  if (!lab.has(L)) lab.set(L, []);
  lab.get(L).push(i);
}
const cross = [];
for (const [L, v] of lab) {
  if (v.length < 2) continue;
  const gs = new Set(v.map(i => E[i].g));
  if (gs.size > 1) cross.push({ label: L, entries: v.length, groups: gs.size });
}
const res = [];
let hit2 = 0, hitCapped = 0;
for (const c of cross) {
  const q = c.label.replace(/\u00b7/g, ' ').replace(/\s+/g, ' ').trim();
  let rows;
  try { rows = runGeocoderSearch(q, idx); } catch (e) { res.push({ label: c.label, error: String(e) }); continue; }
  rows = dedupeDisplayRows(rows);
  const shownLabels = rows.slice(0, 10).map(r => formatAddressHit(r) + '||' + (r.d != null && districtNames[r.d] ? districtNames[r.d] : ''));
  const counts = {};
  for (const s of shownLabels) counts[s] = (counts[s] || 0) + 1;
  const target = c.label + '||' + '';
  let maxSame = 0, maxKey = null;
  for (const k in counts) if (counts[k] > maxSame) { maxSame = counts[k]; maxKey = k; }
  const identicalForThis = Object.keys(counts).filter(k => k.split('||')[0] === c.label)
                                 .reduce((a, k) => Math.max(a, counts[k]), 0);
  if (identicalForThis >= 2) hit2++;
  if (identicalForThis >= 2 && rows.length >= 8) hitCapped++;
  res.push({ label: c.label, records: c.entries, buildings: c.groups, query: q,
             rows_shown: Math.min(rows.length, 10), identical_rows_on_screen: identicalForThis });
}
const dist = {};
for (const r of res) { const k = r.identical_rows_on_screen; dist[k] = (dist[k] || 0) + 1; }
const summary = { cross_groups: cross.length,
  groups_with_2plus_identical_rows_on_screen: hit2,
  distribution_identical_rows_on_screen: dist,
  worst: res.slice().sort((a, b) => b.identical_rows_on_screen - a.identical_rows_on_screen).slice(0, 12) };
fs.writeFileSync(__dirname + '/sweep.json', JSON.stringify({ summary, rows: res }, null, 1), 'utf8');
console.log(JSON.stringify(summary, null, 1));
