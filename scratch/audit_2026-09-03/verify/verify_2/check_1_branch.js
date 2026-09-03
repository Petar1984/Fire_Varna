// (1) Which branch does "ГРАДИНА" take, and is the class really 46?
const H = require('./harness.js');
const q = 'ГРАДИНА';
const qt = H.placeTokens(q);
const sk = H.splitKeys(qt);
console.log('placeTokens =', JSON.stringify(qt.map(t => t.s)));
console.log('keys        =', JSON.stringify(sk.keys));
console.log('rest R      =', JSON.stringify(sk.slots.filter(x => x.ki !== 0).map(x => x.t.s)));
const cls = H.CLASS_OF.get(sk.keys[0]);
console.log('CLASS_OF[' + sk.keys[0] + '].length =', cls.length);
const kinds = {};
for (const r of cls) kinds[r.e.kind] = (kinds[r.e.kind] || 0) + 1;
console.log('kinds in class =', JSON.stringify(kinds, null, 0));
console.log('R empty -> branch index.html:6662 (M1 category) =', sk.slots.filter(x => x.ki !== 0).length === 0);
// the hotel record itself
const hot = H.RECS.filter(r => r.e.name === 'ГРАДИНА');
for (const r of hot) console.log('RECORD:', JSON.stringify(r.e));
