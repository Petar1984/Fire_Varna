// Q4 ("вид + квартал") reproduced against the LIVE index.html core, independently
// of the audit's recall_all.py / recall_sweep.py reference.
const fs = require('fs'), core = require('./core.js');
const FV = 'C:/git/Fire_Varna/';
const hotels = JSON.parse(fs.readFileSync(FV + 'data/hotels.json', 'utf8')).hotels;
const places = JSON.parse(fs.readFileSync(FV + 'data/places.json', 'utf8')).places;
const cats   = JSON.parse(fs.readFileSync(FV + 'data/place_categories.json', 'utf8'));
core.buildIndex(hotels, places, cats);
const RECS = core.RECSref();

const KIND_WORD = {'Хотел':'хотел','Семеен хотел':'хотел','хотел · без категоризация':'хотел',
  'апарт-хотел':'хотел','училище':'училище','университет':'университет','болница':'болница',
  'ДКЦ':'дкц','хоспис':'хоспис','детска градина':'детска градина'};
const ZONE_PREFIX = /^(ж\.к\.|к\.к\.|к\.з\.|с\.о\.|кв\.|м-т|м\.|район)\s+/;
const zoneBare = z => z.replace(ZONE_PREFIX, '').trim();

let miss = 0, hit1 = 0, hit3 = 0, hit8 = 0;
const byQuery = new Map();                 // query -> {missed:[], n, first, firstZone}
for (const rec of RECS) {
  const q = (KIND_WORD[rec.e.kind] + ' ' + zoneBare(rec.e.zone)).trim();
  let s = byQuery.get(q);
  if (!s) { const r = core.search(q);
            s = { rows: r.rows, category: r.category, missed: [], total: 0 }; byQuery.set(q, s); }
  s.total++;
  const rank = s.rows.indexOf(rec);
  if (rank < 0) { miss++; s.missed.push(rec); }
  else { if (rank === 0) hit1++; if (rank < 3) hit3++; if (rank < 8) hit8++; }
}
console.log('Q4 върху 361 записа (жив index.html):');
console.log('  @1 = %d (%s%%)  @3 = %d  @8 = %d  НЕ СЕ НАМИРА = %d (%s%%)',
  hit1, (100*hit1/RECS.length).toFixed(1), hit3, hit8, miss, (100*miss/RECS.length).toFixed(1));

console.log('\nзаявки, при които поне един запис изобщо не излиза:');
let sum = 0;
const bad = [...byQuery.entries()].filter(([q,s]) => s.missed.length).sort((a,b)=>b[1].missed.length-a[1].missed.length);
for (const [q, s] of bad) {
  sum += s.missed.length;
  console.log('  ' + q.padEnd(32) + ' n=' + String(s.rows.length).padStart(3) +
    ' category=' + String(s.category).padEnd(5) + ' скрити=' + s.missed.length + '/' + s.total +
    '  първи: ' + (s.rows.length ? s.rows[0].e.name + ' [' + s.rows[0].e.zone + ']' : '—'));
}
console.log('  СБОР на скритите =', sum, ' (заявки:', bad.length + ')');

// колко записа НОСИ зоната на всяка от тези заявки (не само тези, които я търсят)
console.log('\nколко записа от СЪЩИЯ вид реално стоят в тази зона:');
for (const [q, s] of bad) {
  const kw = q.split(' ')[0];
  const same = RECS.filter(r => (KIND_WORD[r.e.kind] + ' ' + zoneBare(r.e.zone)).trim() === q).length;
  const inZone = s.rows.filter(r => (KIND_WORD[r.e.kind] + ' ' + zoneBare(r.e.zone)).trim() === q).length;
  console.log('  ' + q.padEnd(32) + ' в зоната: ' + String(same).padStart(3) +
    '   търсачката връща: ' + String(s.rows.length).padStart(3) + ', от тях в зоната: ' + inZone);
}
