// Кои точно записа губи ВАРИАНТ А (чист per-record) — цената на „решението“ както е формулирано.
const fs=require('fs');
const live=require('./core.js'), a=require('./core_a.js'), b=require('./core_b.js');
const FV='C:/git/Fire_Varna/';
const hotels=JSON.parse(fs.readFileSync(FV+'data/hotels.json','utf8')).hotels;
const places=JSON.parse(fs.readFileSync(FV+'data/places.json','utf8')).places;
const cats=JSON.parse(fs.readFileSync(FV+'data/place_categories.json','utf8'));
const KIND_WORD={'Хотел':'хотел','Семеен хотел':'хотел','хотел · без категоризация':'хотел','апарт-хотел':'хотел',
 'училище':'училище','университет':'университет','болница':'болница','ДКЦ':'дкц','хоспис':'хоспис','детска градина':'детска градина'};
const q2=n=>n.replace(/[„“”"'()]/g,' ').replace(/\s+/g,' ').trim();
for(const [core,label] of [[live,'ЖИВА'],[a,'ВАР.А'],[b,'ВАР.Б']]){
  core.buildIndex(hotels,places,cats);
  const R=core.RECSref(); const lost=[];
  for(const rec of R){
    const q=(KIND_WORD[rec.e.kind]+' '+q2(rec.e.name)).trim();
    const rows=core.search(q).rows;
    if(rows.indexOf(rec)<0) lost.push([rec.e.name, rec.e.zone, q, rows.length, rows.length?rows[0].e.name:'—']);
  }
  console.log('\n'+label+' · Q3 („вид + име“) губи '+lost.length+' записа:');
  for(const l of lost) console.log('   „'+l[0]+'“ ['+l[1]+']  заявка „'+l[2]+'“ → n='+l[3]+', 1-ви: '+l[4]);
}
// и по име, без вид
for(const [core,label] of [[live,'ЖИВА'],[a,'ВАР.А'],[b,'ВАР.Б']]){
  core.buildIndex(hotels,places,cats);
  const r=core.search('хотел градина').rows;
  const has=r.some(x=>x.e.name==='ГРАДИНА');
  console.log(label+' · „хотел градина“ n='+r.length+'  съдържа ли хотел ГРАДИНА: '+has);
}
