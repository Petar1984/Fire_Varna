// Runs the LIVE index.html search core against the real bundles. No browser.
const fs = require('fs');
const core = require('./core.js');
const FV = 'C:/git/Fire_Varna/';
const hotels = JSON.parse(fs.readFileSync(FV + 'data/hotels.json', 'utf8')).hotels;
const places = JSON.parse(fs.readFileSync(FV + 'data/places.json', 'utf8')).places;
const cats   = JSON.parse(fs.readFileSync(FV + 'data/place_categories.json', 'utf8'));
core.buildIndex(hotels, places, cats);
console.log('RECS =', core.RECSref().length, '(hotels', hotels.length, '+ places', places.length + ')');

function q(s, lim) {
  const r = core.search(s);
  console.log('\nq=%j  n=%d  category=%s hasKey=%s', s, r.rows.length, r.category, r.hasKey);
  for (const rec of r.rows.slice(0, lim === undefined ? 5 : lim))
    console.log('    -', rec.e.name, '|', rec.e.kind, '|', rec.e.zone);
  return r;
}
const zoneCount = (z, kinds) => hotels.concat(places).filter(x => x.zone === z && (!kinds || kinds(x))).length;
const isHotel = x => ['Хотел','Семеен хотел','хотел · без категоризация','апарт-хотел'].includes(x.kind);

for (const s of ['хотел одесос','хотел златни','хотел морска градина','училище морска градина',
                 'хотел приморски','детска градина морска градина','хотел градина','одесос'])
  q(s, 3);

console.log('\n--- ground truth in the data ---');
console.log('хотели zone="район Одесос"        =', zoneCount('район Одесос', isHotel));
console.log('хотели zone="Морска градина"      =', zoneCount('Морска градина', isHotel));
console.log('хотели zone="район Приморски"     =', zoneCount('район Приморски', isHotel));
console.log('хотели zone="к.к. Златни пясъци"  =', zoneCount('к.к. Златни пясъци', isHotel));
console.log('училища zone="Морска градина"     =', zoneCount('Морска градина', x => x.kind === 'училище'));
const parkod = hotels.filter(h => /ОДЕСОС/i.test(h.name));
for (const h of parkod) console.log('име съдържа „ОДЕСОС“:', h.name, '|', h.kind, '| zone =', h.zone);
