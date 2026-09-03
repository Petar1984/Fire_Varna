// Вреди ли „решението“? Две per-record реализации, мерени срещу живата.
// НИЩО не се пипа в C:/git — кръпката се прави върху ИЗВЛЕЧЕНОТО копие в scratchpad.
const fs = require('fs');
const ORIG = fs.readFileSync('./core.js', 'utf8');
const A3_LIVE = `      if (hasKey) {                              // А3′: key + a purely zone/kind rest = filtered list
        const zk = new Set(), nm = new Set();
        for (const r of cls) { for (const v of r.zkset) zk.add(v); for (const v of r.nset) nm.add(v); }
        if (R.every((t) => zk.has(t.s)) && !R.some((t) => nm.has(t.s))) {
          const flt = cls.filter((r) => R.every((t) => r.zkset.has(t.s)));
          if (flt.length) return { category: true, hasKey: hasKey, rows: orderCategory(flt, c) };
        }
      }`;
if (ORIG.indexOf(A3_LIVE) < 0) { console.error('А3′ блокът не е намерен дословно — HEAD се е раздвижил'); process.exit(2); }

const VAR_A = `      if (hasKey) {   // ВАРИАНТ А: чист per-record филтър (guard-2 отпада)
        const flt = cls.filter((r) => R.every((t) => r.zkset.has(t.s)));
        if (flt.length) return { category: true, hasKey: hasKey, rows: orderCategory(flt, c) };
      }`;
const VAR_B = `      if (hasKey) {   // ВАРИАНТ Б: филтърът СЕ СЛИВА с именните попадения
        const flt = cls.filter((r) => R.every((t) => r.zkset.has(t.s)));
        if (flt.length) {
          const byName = runScored(cls, R, hasKey, sk.dead, c);
          const seen = new Set(flt);
          const merged = orderCategory(flt, c).concat(byName.filter((r) => !seen.has(r)));
          return { category: true, hasKey: hasKey, rows: merged };
        }
      }`;
const mk = (src, name) => { const f = './core_' + name + '.js'; fs.writeFileSync(f, ORIG.replace(A3_LIVE, src)); return require(f); };

const FV='C:/git/Fire_Varna/';
const hotels=JSON.parse(fs.readFileSync(FV+'data/hotels.json','utf8')).hotels;
const places=JSON.parse(fs.readFileSync(FV+'data/places.json','utf8')).places;
const cats=JSON.parse(fs.readFileSync(FV+'data/place_categories.json','utf8'));
const KIND_WORD={'Хотел':'хотел','Семеен хотел':'хотел','хотел · без категоризация':'хотел','апарт-хотел':'хотел',
 'училище':'училище','университет':'университет','болница':'болница','ДКЦ':'дкц','хоспис':'хоспис','детска градина':'детска градина'};
const ZP=/^(ж\.к\.|к\.к\.|к\.з\.|с\.о\.|кв\.|м-т|м\.|район)\s+/;
const zb=z=>z.replace(ZP,'').trim();
// Q2/Q5-подобни: тук ме интересува само не-регресия по ИМЕ
const q2 = n => n.replace(/[„“”"'()]/g,' ').replace(/\s+/g,' ').trim();

function sweep(core, label) {
  core.buildIndex(hotels, places, cats);
  const RECS = core.RECSref();
  const res = { label, q4miss: 0, q1miss: 0, q3miss: 0, q1rank1: 0 };
  for (const rec of RECS) {
    const q4 = (KIND_WORD[rec.e.kind] + ' ' + zb(rec.e.zone)).trim();
    if (core.search(q4).rows.indexOf(rec) < 0) res.q4miss++;
    const r1 = core.search(rec.e.name).rows;
    if (r1.indexOf(rec) < 0) res.q1miss++; else if (r1[0] === rec) res.q1rank1++;
    const q3 = (KIND_WORD[rec.e.kind] + ' ' + q2(rec.e.name)).trim();
    if (core.search(q3).rows.indexOf(rec) < 0) res.q3miss++;
  }
  const probe = q => { const r = core.search(q); return r.rows.length + (r.rows.length ? ' | 1-ви: ' + r.rows[0].e.name + ' [' + r.rows[0].e.zone + ']' : ''); };
  res.probes = {
    'хотел одесос': probe('хотел одесос'),
    'хотел градина': probe('хотел градина'),
    'ГРАДИНА': probe('ГРАДИНА'),
    'хотел златни': probe('хотел златни'),
    'хотел приморски': probe('хотел приморски'),
    'училище морска градина': probe('училище морска градина'),
    'хотел зеленика': probe('хотел зеленика'),
    'хотел адмирал': probe('хотел адмирал'),
    'болница света марина': probe('болница света марина')
  };
  // колко от 22-та Одесос излизат
  const od = core.search('хотел одесос').rows.filter(r => r.e.zone === 'район Одесос').length;
  const park = core.search('хотел одесос').rows.some(r => r.e.name === 'ПАРК ХОТЕЛ ОДЕСОС');
  res.odesos = od; res.park = park;
  return res;
}
const rows = [sweep(require('./core.js'), 'ЖИВА (HEAD)'), sweep(mk(VAR_A,'a'), 'ВАРИАНТ А per-record'), sweep(mk(VAR_B,'b'), 'ВАРИАНТ Б сливане')];
for (const r of rows) {
  console.log('\n=== ' + r.label + ' ===');
  console.log('  Q4 не се намира: ' + r.q4miss + '/361   Q1 не се намира: ' + r.q1miss + '   Q1@1: ' + r.q1rank1 + '   Q3 не се намира: ' + r.q3miss);
  console.log('  „хотел одесос“: от 22-та в район Одесос излизат ' + r.odesos + '; ПАРК ХОТЕЛ ОДЕСОС в списъка: ' + r.park);
  for (const k of Object.keys(r.probes)) console.log('    ' + k.padEnd(24) + ' n=' + r.probes[k]);
}
