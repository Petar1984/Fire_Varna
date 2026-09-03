// STEP 3 — battery: A = the 545 far labels; B = every 86th entry label (1003 realistic queries).
const E=require('./engine.js'); const fs=require('fs');
const FV='C:/git/Fire_Varna/';
const si=JSON.parse(fs.readFileSync(FV+'data/search_index.json','utf8'));
const ar=JSON.parse(fs.readFileSync(FV+'data/address_rows.json','utf8'));
const idx=E.setup(si,ar);
const DN=si.district_names;
const R=6371008.8, rad=x=>x*Math.PI/180;
const hav=(a,b)=>{const p1=rad(a[0]),p2=rad(b[0]);
  const x=Math.sin((p2-p1)/2)**2+Math.cos(p1)*Math.cos(p2)*Math.sin(rad(b[1]-a[1])/2)**2;
  return 2*R*Math.asin(Math.sqrt(x));};
const key=r=>E.norm(E.formatAddressHit(r))+'||'+(r.g!=null?String(r.g):'');
function probe(q){
  const before=E.runGeocoderSearch(q, idx);
  const after=E.dedupeDisplayRows(before);
  const surv=new Map(); for(const r of after) surv.set(key(r), r);
  const aset=new Set(after); const drops=[];
  for(const r of before){ if(aset.has(r)) continue;
    const s=surv.get(key(r));
    drops.push({reason: s?'key':'block', dist: s?hav(r.pin,s.pin):null,
                dDiff: s? (r.d!==s.d):null, label:E.formatAddressHit(r),
                d: r.d!=null?DN[r.d]:'-', sd: s&&s.d!=null?DN[s.d]:'-'});
  }
  return {q, before:before.length, after:after.length, drops};
}
function report(name, qs){
  let nDrop=0,nFar=0,nMid=0,nCross=0,tot=0,dropRows=0, worst=[];
  for(const q of qs){ const p=probe(q); tot++;
    const kd=p.drops.filter(d=>d.reason==='key');
    if(kd.length){nDrop++; dropRows+=kd.length;}
    const mx=kd.reduce((a,d)=>Math.max(a,d.dist||0),0);
    if(mx>=200) nFar++; else if(mx>=50) nMid++;
    if(kd.some(d=>d.dDiff)) nCross++;
    if(mx>0) worst.push({q,mx:Math.round(mx),before:p.before,after:p.after,
      cross:kd.filter(d=>d.dDiff).map(d=>d.d+'->'+d.sd)[0]||'-'});
  }
  worst.sort((a,b)=>b.mx-a.mx);
  console.log('\n=== '+name+' ('+tot+' queries) ===');
  console.log('  queries where the dedupe drops >=1 row (key-collision):', nDrop, '('+(100*nDrop/tot).toFixed(1)+'%)  dropped rows total:', dropRows);
  console.log('  ... of them the dropped row sits >=200 m away:', nFar, '('+(100*nFar/tot).toFixed(1)+'%)');
  console.log('  ... 50-200 m away:', nMid);
  console.log('  ... a dropped row was in ANOTHER район than the survivor:', nCross, '('+(100*nCross/tot).toFixed(1)+'%)');
  console.log('  worst 8:'); for(const w of worst.slice(0,8))
    console.log('   ', String(w.mx).padStart(6)+' m  '+w.before+'->'+w.after+'  ['+w.cross+']  '+JSON.stringify(w.q));
  return {tot,nDrop,nFar,nMid,nCross,dropRows};
}
const keys=JSON.parse(fs.readFileSync(__dirname+'/step1_keys.json','utf8'));
const A=keys.filter(k=>k.spread>=200).map(k=>k.label);
const ents=si.entries; const B=[];
for(let i=0;i<ents.length;i+=86) B.push(E.formatAddressHit(ents[i]));
const out={};
out.A=report('A · the 545 far labels typed verbatim', A);
out.B=report('B · every 86th entry label (realistic mix)', B);
fs.writeFileSync(__dirname+'/step3_battery.json', JSON.stringify(out,null,1));
