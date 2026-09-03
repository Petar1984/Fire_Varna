const H = require('./harness.js');
const qs = process.argv.slice(2);
for (const q of qs) {
  const r = H.search(q);
  console.log('=== q=' + JSON.stringify(q) + '  category=' + r.category + '  hasKey=' + r.hasKey + '  n=' + r.rows.length);
  r.rows.slice(0, 12).forEach((rec, i) =>
    console.log('   ' + (i + 1) + '. ' + rec.e.name + ' | ' + rec.e.kind + ' | ' + rec.e.zone));
  const idx = r.rows.findIndex((x) => x.e.name === 'ГРАДИНА' && x.e.kind !== 'детска градина');
  console.log('   -> rank of hotel ГРАДИНА: ' + (idx < 0 ? 'НЕ СЕ НАМИРА' : (idx + 1)));
}
