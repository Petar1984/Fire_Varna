// (5) Cheaper cure than the draft's (b): drop ONLY the singular ambiguous form
//     "градина" from the dictionary, keep "градини"/"детска градина".
//     Simulated in memory ONLY — nothing on disk is touched.
const fs = require('fs'), path = require('path');
const REPO = 'C:/git/Fire_Varna';
const src = fs.readFileSync(path.join(REPO, 'index.html'), 'utf8').split(/\r?\n/);
const RANGES = [[6256, 6259], [6288, 6310], [6313, 6377], [6478, 6683]];
const code = RANGES.map(([a, b]) => src.slice(a - 1, b).join('\n')).join('\n');
const hotels = JSON.parse(fs.readFileSync(path.join(REPO, 'data/hotels.json'), 'utf8')).hotels;
const places2 = JSON.parse(fs.readFileSync(path.join(REPO, 'data/places.json'), 'utf8')).places;
const factory = new Function('HOT', 'PL2', 'CATS', code +
  ';buildIndex(HOT, PL2, CATS); return { search: search, RECS: RECS };');

function run(label, mutate) {
  const cats = JSON.parse(fs.readFileSync(path.join(REPO, 'data/place_categories.json'), 'utf8'));
  mutate(cats);
  const H = factory(hotels, places2, cats);
  const tgt = H.RECS.find(r => r.e.name === 'ГРАДИНА' && r.e.kind === 'Хотел');
  console.log('--- ' + label);
  for (const q of ['градина', 'градини', 'детска градина', 'детски градини', 'детска градина Чайка', 'хотел градина']) {
    const r = H.search(q);
    const i = r.rows.indexOf(tgt);
    console.log('   q=' + JSON.stringify(q).padEnd(26) + ' cat=' + (r.category ? 'Y' : 'n') +
                ' n=' + String(r.rows.length).padStart(3) +
                ' hotel@' + (i < 0 ? '-' : i + 1) +
                ' first=' + (r.rows[0] ? r.rows[0].e.name : '-'));
  }
}
run('BASELINE (as shipped)', () => {});
run('CURE b\u2032: delete only the singular form "градина"', (c) => { delete c.forms['градина']; });
run('CURE b (draft): delete all 4 bare "градин*" forms', (c) => {
  for (const f of ['градина', 'градината', 'градини', 'градините']) delete c.forms[f];
});
