// Кой точно guard на А3′ пада за всяка от 11-те заявки — и КОЙ запис го поваля.
const fs = require('fs'), core = require('./core.js');
const FV='C:/git/Fire_Varna/';
const hotels=JSON.parse(fs.readFileSync(FV+'data/hotels.json','utf8')).hotels;
const places=JSON.parse(fs.readFileSync(FV+'data/places.json','utf8')).places;
const cats=JSON.parse(fs.readFileSync(FV+'data/place_categories.json','utf8'));
core.buildIndex(hotels,places,cats);
const RECS=core.RECSref(), CLASS_OF=core.CLASSref();

const QS=['хотел Одесос','хотел Морска градина','училище Морска градина','хотел Приморски',
 'детска градина Морска градина','училище Св. Константин','детска градина Чайка',
 'детска градина Дружба','хотел Зеленика','училище Изгрев 1','училище Свети Никола',
 'хотел златни'];
for(const q of QS){
  const qt=core.placeTokens(q), sk=core.splitKeys(qt);
  const hasKey=sk.keys.length>0;
  const cls=hasKey?CLASS_OF.get(sk.keys[0]):RECS;
  const R=sk.slots.filter(x=>x.ki!==0).map(x=>x.t);
  const zk=new Set(), nm=new Set();
  for(const r of cls){for(const v of r.zkset)zk.add(v);for(const v of r.nset)nm.add(v);}
  const gA=R.every(t=>zk.has(t.s)), gB=!R.some(t=>nm.has(t.s));
  const blockers=R.filter(t=>nm.has(t.s));
  const notZk=R.filter(t=>!zk.has(t.s));
  const culprits=[];
  for(const t of blockers) for(const r of cls) if(r.nset.has(t.s)) culprits.push(t.s+' ← '+r.e.name+' ['+r.e.zone+']');
  console.log('\nq=%s  key=%j  R=[%s]', JSON.stringify(q), sk.keys[0], R.map(t=>t.s).join(','));
  console.log('   клас=%d  guard-1 (всички токени са zone/kind в класа)=%s%s', cls.length, gA,
    gA?'':'  ← извън zk: '+notZk.map(t=>t.s).join(','));
  console.log('   guard-2 (нито един токен не е ИМЕ в класа)=%s%s', gB, gB?'':'  ← поваля го: '+[...new Set(culprits)].join(' | '));
  console.log('   А3′ гърми ли: %s', (gA&&gB)?'ДА (категориен филтър)':'НЕ → пада в runScored');
}
