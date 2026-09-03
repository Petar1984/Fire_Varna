// STEP 7 — realistic battery restricted to labels that ARE an address (end in a house number).
const E=require('./engine.js'); const fs=require('fs');
const FV='C:/git/Fire_Varna/';
const si=JSON.parse(fs.readFileSync(FV+'data/search_index.json','utf8'));
const ar=JSON.parse(fs.readFileSync(FV+'data/address_rows.json','utf8'));
const idx=E.setup(si,ar); const DN=si.district_names;
const R=6371008.8,rad=x=>x*Math.PI/180;
const hav=(a,b)=>{const p1=rad(a[0]),p2=rad(b[0]);const x=Math.sin((p2-p1)/2)**2+Math.cos(p1)*Math.cos(p2)*Math.sin(rad(b[1]-a[1])/2)**2;return 2*R*Math.asin(Math.sqrt(x));};
const key=r=>E.norm(E.formatAddressHit(r))+'||'+(r.g!=null?String(r.g):'');
const isAddr=s=>{const t=E.norm(s).split(' ').filter(Boolean);return t.length>=2&&/^[0-9]+[а-яa-z]?$/.test(t[t.length-1]);};
const Q=[];
for(let i=0;i<si.entries.length;i+=53){const l=E.formatAddressHit(si.entries[i]); if(isAddr(l)) Q.push(l);}
let n=0,drop=0,far=0,mid=0,cross=0,rows=0;
const worst=[];
for(const q of Q){ n++;
  const b=E.runGeocoderSearch(q,idx), a=E.dedupeDisplayRows(b), aset=new Set(a);
  const surv=new Map(); for(const r of a) surv.set(key(r),r);
  let mx=0,cr=false,k=0;
  for(const r of b){ if(aset.has(r))continue; const s=surv.get(key(r)); if(!s)continue;
    k++; const d=hav(r.pin,s.pin); if(d>mx)mx=d; if(r.d!==s.d)cr=true; }
  if(k){drop++;rows+=k;}
  if(mx>=200)far++; else if(mx>=50)mid++;
  if(cr)cross++;
  if(mx>=200) worst.push([Math.round(mx),q]);
}
worst.sort((a,b)=>b[0]-a[0]);
console.log('B2 · address-shaped queries:',n);
console.log('  drop >=1 row:',drop,'('+(100*drop/n).toFixed(1)+'%)   rows dropped:',rows);
console.log('  worst drop >=200 m:',far,'('+(100*far/n).toFixed(1)+'%)   50-200 m:',mid,'('+(100*mid/n).toFixed(1)+'%)');
console.log('  a dropped row in ANOTHER район:',cross,'('+(100*cross/n).toFixed(1)+'%)');
console.log('  worst 10:'); worst.slice(0,10).forEach(w=>console.log('   ',String(w[0]).padStart(6)+'m',JSON.stringify(w[1])));
