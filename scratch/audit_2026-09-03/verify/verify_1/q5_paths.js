const api = require('./harness.js');
function line(q) {
  const r = api.search(q);
  const idx = r.rows.findIndex((rec) => rec.e.name === 'ГРАДИНА' && rec.e.kind === 'Хотел');
  // what the SCREEN shows: <=8 per group, <=16 in all, groups in order of best row
  const order = [], byG = new Map();
  for (const rec of r.rows) { const g = api.groupOf(rec); if (!byG.has(g)) { byG.set(g, []); order.push(g); } byG.get(g).push(rec); }
  let shown = [], visible = false;
  for (const g of order) { if (shown.length >= 16) break;
    const b = byG.get(g), take = Math.min(8, 16 - shown.length, b.length);
    for (let i = 0; i < take; i++) shown.push(b[i]); }
  visible = shown.some((rec) => rec.e.name === 'ГРАДИНА' && rec.e.kind === 'Хотел');
  console.log([q.padEnd(24), 'n=' + String(r.rows.length).padStart(3),
    'cat=' + (r.category ? 'Y' : 'n'), 'key=' + (r.hasKey ? 'Y' : 'n'),
    'rank=' + (idx < 0 ? '-' : idx + 1), 'ON SCREEN=' + (visible ? 'YES' : 'no'),
    '| ' + shown.slice(0, 3).map((x) => x.e.name).join(' / ')].join('  '));
}
console.log('--- typing the name letter by letter (MIN_Q=2) ---');
for (const p of ['гр', 'гра', 'град', 'гради', 'градин', 'градина']) line(p);
console.log('--- other ways to the record ---');
for (const q of ['хотел градина', 'х-л градина', 'хотел чайка', 'чайка', 'хотели чайка',
                 'градина к.к. чайка', 'гардина', 'градинa'/*latin a*/, 'ГРАДИНА хотел']) line(q);
console.log('--- does the rule bite the ZONE "Морска градина"? ---');
for (const q of ['морска градина', 'хотел морска градина', 'училище морска градина']) line(q);
