// STEP 6 — the sharpest case: a NUMBERED label whose copies sit >=200 m apart INSIDE one район.
// Can the second location be reached at all?
const E=require('./engine.js'); const fs=require('fs');
const FV='C:/git/Fire_Varna/';
const si=JSON.parse(fs.readFileSync(FV+'data/search_index.json','utf8'));
const ar=JSON.parse(fs.readFileSync(FV+'data/address_rows.json','utf8'));
const idx=E.setup(si,ar); const DN=si.district_names;
const R=6371008.8,rad=x=>x*Math.PI/180;
const hav=(a,b)=>{const p1=rad(a[0]),p2=rad(b[0]);const x=Math.sin((p2-p1)/2)**2+Math.cos(p1)*Math.cos(p2)*Math.sin(rad(b[1]-a[1])/2)**2;return 2*R*Math.asin(Math.sqrt(x));};
const hasNum=s=>/(^|\s)\d+[а-яa-z]?(\s|$)/.test(E.norm(s));
const by=new Map();
for(const e of si.entries){const k=E.norm(E.formatAddressHit(e))+'||'+(e.g!=null?String(e.g):'');
  if(!by.has(k))by.set(k,[]);by.get(k).push(e);}
const cands=[];
for(const [k,arr] of by){
  if(arr.length<2) continue;
  const lab=E.formatAddressHit(arr[0]); if(!hasNum(lab)) continue;
  const ds=new Set(arr.map(e=>e.d));
  let m=0;const pins=arr.map(e=>e.pin);
  for(let i=0;i<pins.length;i++)for(let j=i+1;j<pins.length;j++)m=Math.max(m,hav(pins[i],pins[j]));
  if(m>=200) cands.push({lab,m:Math.round(m),n:arr.length,sameD:ds.size===1,d:DN[arr[0].d]});
}
const same=cands.filter(c=>c.sameD).sort((a,b)=>b.m-a.m);
console.log('numbered keys >=200 m:',cands.length,' of them ALL copies inside ONE район:',same.length);
console.log('top 10 same-район numbered splits:');
same.slice(0,10).forEach(c=>console.log('  ',String(c.m).padStart(6)+'m', 'copies='+c.n, '['+c.d+']', JSON.stringify(c.lab)));
console.log('\n--- probe of the top 3 (bare query, then + район) ---');
for(const c of same.slice(0,3)){
  for(const q of [c.lab, c.lab+' '+c.d]){
    const b=E.runGeocoderSearch(q,idx),a=E.dedupeDisplayRows(b);
    const aset=new Set(a);
    console.log('\nQ='+JSON.stringify(q)+' ranked='+b.length+' shown='+a.length);
    a.slice(0,8).forEach(r=>console.log('   SHOWN ',r.pin[0].toFixed(5),r.pin[1].toFixed(5),'['+DN[r.d]+']',JSON.stringify(E.formatAddressHit(r))));
    b.filter(r=>!aset.has(r)).forEach(r=>console.log('   hidden',r.pin[0].toFixed(5),r.pin[1].toFixed(5),'['+DN[r.d]+']',JSON.stringify(E.formatAddressHit(r))));
  }
}
