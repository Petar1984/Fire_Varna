// Solution (a) — for EVERY dictionary key: which records carry that key as their
// WHOLE name and are absent from the class list it returns?
const api = require('./harness.js');
const recs = api.recs(), CLASS_OF = api.classOf();
const byKey = new Map();
for (const rec of recs) {
  const k = api.keyOf(rec.e.name);
  if (!byKey.has(k)) byKey.set(k, []);
  byKey.get(k).push(rec);
}
let hits = 0;
for (const [fk, cls] of CLASS_OF) {
  const same = byKey.get(fk) || [];
  const outside = same.filter((r) => cls.indexOf(r) < 0);
  if (same.length) {
    hits++;
    console.log('key "' + fk + '" (class n=' + cls.length + ') <- exact-name records: ' +
      same.map((r) => r.e.name + '[' + r.e.kind + ']' + (cls.indexOf(r) < 0 ? ' OUTSIDE' : ' inside')).join(', '));
  }
}
console.log('dictionary keys that are ALSO somebody\'s whole name:', hits, 'of', CLASS_OF.size);
