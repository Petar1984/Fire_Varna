const api = require('./harness.js');
function run(q, label) {
  const r = api.search(q);
  const rows = r.rows;
  const kinds = {};
  for (const rec of rows) kinds[api.groupOf(rec)] = (kinds[api.groupOf(rec)] || 0) + 1;
  const idx = rows.findIndex((rec) => rec.e.name === 'ГРАДИНА' && rec.e.kind === 'Хотел');
  console.log(JSON.stringify({
    q, label, n: rows.length, category: r.category, hasKey: r.hasKey,
    groups: kinds, hotel_GRADINA_rank: idx < 0 ? null : idx + 1,
    first5: rows.slice(0, 5).map((x) => x.e.name + ' [' + x.e.kind + ']')
  }, null, 0));
}
for (const q of ['ГРАДИНА', 'градина', 'Градина', 'ГРАДИНА ', 'градината', 'градини',
                 'хотел градина', 'х-л градина', 'градина чайка', 'градина хотел',
                 'детска градина', 'гардина', 'градин', 'градина 280']) run(q);
