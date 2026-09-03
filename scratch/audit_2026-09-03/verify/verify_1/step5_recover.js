// STEP 5 — can the firefighter reach the HIDDEN location by narrowing the query?
const E=require('./engine.js'); const fs=require('fs');
const FV='C:/git/Fire_Varna/';
const si=JSON.parse(fs.readFileSync(FV+'data/search_index.json','utf8'));
const ar=JSON.parse(fs.readFileSync(FV+'data/address_rows.json','utf8'));
const idx=E.setup(si,ar); const DN=si.district_names;
function show(q){
  const b=E.runGeocoderSearch(q,idx), a=E.dedupeDisplayRows(b);
  console.log('\nQ='+JSON.stringify(q)+'  ranked='+b.length+' shown='+a.length);
  a.slice(0,10).forEach(r=>console.log('   SHOWN  ',r.pin[0].toFixed(5),r.pin[1].toFixed(5),
     '['+(r.d!=null?DN[r.d]:'-')+']', JSON.stringify(E.formatAddressHit(r))));
  const aset=new Set(a);
  b.filter(r=>!aset.has(r)).forEach(r=>console.log('   hidden ',r.pin[0].toFixed(5),r.pin[1].toFixed(5),
     '['+(r.d!=null?DN[r.d]:'-')+']', JSON.stringify(E.formatAddressHit(r))));
}
['17 ta 16','17 ta 16 приморски','17 ta 16 владислав варненчик',
 'ул св константин и елена','ул св константин и елена приморски',
 'неизвестна','неизвестна аспарухово'].forEach(show);
