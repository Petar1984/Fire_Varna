const fs = require('fs'), path = require('path'), ROOT = 'C:/git/Fire_Varna';
// Re-create the harness with a MUTILATED dictionary: solution (b) - "градина" and
// its bare forms dropped, only "детска градина" left.
const src = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8').split(/\r?\n/);
const body = src.slice(6245, 6682).filter((_, i) => { const ln = 6246 + i; return !(ln >= 6248 && ln <= 6251); }).join('\n');
const code = `(function () {\n${body}\n  return { buildIndex, search, recs: () => RECS, groupOf, classOf: () => CLASS_OF };\n})()`;
global.window = {}; global.map = { getCenter: () => null };
function build(catsMut) {
  const api = eval(code);
  const hotels = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/hotels.json'), 'utf8')).hotels;
  const places2 = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/places.json'), 'utf8')).places;
  const cats = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/place_categories.json'), 'utf8'));
  if (catsMut) catsMut(cats);
  api.buildIndex(hotels, places2, cats);
  return api;
}
function report(api, tag, qs) {
  for (const q of qs) {
    const r = api.search(q);
    const kg = {};
    for (const rec of r.rows) kg[api.groupOf(rec)] = (kg[api.groupOf(rec)] || 0) + 1;
    const idx = r.rows.findIndex((x) => x.e.name === 'ГРАДИНА' && x.e.kind === 'Хотел');
    console.log(tag, '|', q.padEnd(20), 'n=' + String(r.rows.length).padStart(3),
      'cat=' + (r.category ? 'Y' : 'n'), 'ГРАДИНА rank=' + (idx < 0 ? '-' : idx + 1), JSON.stringify(kg));
  }
}
const QS = ['градина', 'градини', 'градината', 'детска градина', 'детски градини',
            'детска градина чайка', 'хотел градина', 'градина дружба'];
report(build(null), 'NOW  ', QS);
console.log('');
report(build((c) => { for (const f of ['градина', 'градини', 'градината', 'градините']) delete c.forms[f]; }), '(b)  ', QS);
console.log('');
// how many of the 46 kindergartens does the KEYLESS branch still reach on "градина"?
const b = build((c) => { for (const f of ['градина', 'градини', 'градината', 'градините']) delete c.forms[f]; });
const r = b.search('градина');
const dg = r.rows.filter((x) => x.e.kind === 'детска градина');
console.log('(b) "градина" reaches', dg.length, 'of 46 kindergartens; total rows', r.rows.length);
console.log('(b) rows:', r.rows.slice(0, 12).map((x) => x.e.name + '[' + x.e.kind + ']').join(' / '));
