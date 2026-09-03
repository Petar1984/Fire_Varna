// STEP 2 — what the firefighter ACTUALLY sees: run the real matcher, then the real dedupe.
const E = require('./engine.js'); const fs=require('fs');
const FV='C:/git/Fire_Varna/';
const si=JSON.parse(fs.readFileSync(FV+'data/search_index.json','utf8'));
const ar=JSON.parse(fs.readFileSync(FV+'data/address_rows.json','utf8'));
const idx=E.setup(si,ar);
const R=6371008.8, rad=x=>x*Math.PI/180;
const hav=(a,b)=>{const p1=rad(a[0]),p2=rad(b[0]);
  const x=Math.sin((p2-p1)/2)**2+Math.cos(p1)*Math.cos(p2)*Math.sin(rad(b[1]-a[1])/2)**2;
  return 2*R*Math.asin(Math.sqrt(x));};
const key=r=>E.norm(E.formatAddressHit(r))+'||'+(r.g!=null?String(r.g):'');
function probe(q){
  const t0=Date.now();
  const before=E.runGeocoderSearch(q, idx);
  const after=E.dedupeDisplayRows(before);
  const survivors=new Map(); for(const r of after) survivors.set(key(r), r);
  const dropped=[]; const seen=new Set();
  // replay the fold to attribute each drop
  const labels=before.map(r=>String(E.formatAddressHit(r)));
  const afterSet=new Set(after);
  for(let i=0;i<before.length;i++){
    const r=before[i]; if(afterSet.has(r)) continue;
    const k=key(r); const s=survivors.get(k);
    dropped.push({label:labels[i], kind:r.kind,
      reason: s? 'key-collision':'block-suppression',
      dist: s? Math.round(hav(r.pin, s.pin)) : null});
  }
  return {q, before:before.length, after:after.length, dropped, ms:Date.now()-t0};
}
const qs=process.argv.slice(2);
for(const q of qs){ const p=probe(q);
  console.log('\nQ='+JSON.stringify(q), ' ranked='+p.before, '-> shown='+p.after, ' ('+p.ms+' ms)');
  for(const d of p.dropped) console.log('    DROPPED', d.reason, 'dist='+d.dist+'m', d.kind, JSON.stringify(d.label));
}
