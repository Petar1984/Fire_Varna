// (4) Is the proposed cure harmful? Blast radius of (a) "pin the exact name on top"
//     and of (b) "drop 'градина' from the dictionary".
const H = require('./harness.js');
const fs = require('fs');

// --- (a): every populated dictionary key whose text equals some record's OWN name
const byKey = new Map();
for (const rec of H.RECS) {
  const k = H.keyOf(rec.e.name);
  if (!byKey.has(k)) byKey.set(k, []);
  byKey.get(k).push(rec);
}
console.log('--- (a) records whose WHOLE name is a populated category key:');
let n = 0;
for (const fk of H.CLASS_OF.keys()) {
  const hits = byKey.get(fk);
  if (!hits) continue;
  n++;
  console.log('  key ' + JSON.stringify(fk) + ' (class n=' + H.CLASS_OF.get(fk).length + ') <- ' +
              hits.map(r => r.e.name + ' [' + r.e.kind + ', ' + r.e.zone + ']').join(' ; '));
}
console.log('  total such keys =', n);

// --- (b): what does the dictionary say about "градина"?
const cats = H.cats;
const formsWithGradina = Object.keys(cats.forms).filter(f => /градин/i.test(f));
console.log('--- (b) dictionary forms containing "градин":');
for (const f of formsWithGradina) console.log('  ' + JSON.stringify(f) + ' -> ' + JSON.stringify(cats.forms[f]));
// what would be lost: which queries currently resolve via the bare key "gradina"?
console.log('  keyOf("градина") =', JSON.stringify(H.keyOf('градина')));
console.log('  keyOf("детска градина") =', JSON.stringify(H.keyOf('детска градина')));
// zone "Морска градина" — does dropping/keeping the key disturb it?
for (const q of ['Морска градина', 'морска градина', 'детска градина', 'градини', 'детски градини']) {
  const r = H.search(q);
  console.log('  q=' + JSON.stringify(q) + ' cat=' + r.category + ' n=' + r.rows.length +
              ' first=' + (r.rows[0] ? r.rows[0].e.name + ' (' + r.rows[0].e.kind + ')' : '-'));
}
