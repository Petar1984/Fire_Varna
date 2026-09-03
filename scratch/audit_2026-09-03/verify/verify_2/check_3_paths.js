// (3) Which realistic queries DO reach hotel ГРАДИНА? (incremental typing + variants)
const H = require('./harness.js');
const target = H.RECS.find(r => r.e.name === 'ГРАДИНА' && r.e.kind === 'Хотел');
const qs = ['г','гр','гра','град','гради','градин','градина','градина ','градина чайка',
            'градина хотел','хотел градина','х-л градина','гардина','градина 280',
            'ГРАДИНА к.к. Чайка','хотел градина чайка','отел градина','gradina','hotel gradina',
            'градинa'];
for (const q of qs) {
  const r = H.search(q);
  const idx = r.rows.indexOf(target);
  console.log((idx >= 0 ? 'HIT  #' + String(idx + 1).padStart(3) : 'miss     ') +
              ' | n=' + String(r.rows.length).padStart(3) +
              ' cat=' + (r.category ? 'Y' : 'n') +
              ' | ' + JSON.stringify(q) +
              ' | first=' + (r.rows[0] ? r.rows[0].e.name + ' (' + r.rows[0].e.kind + ')' : '-'));
}
