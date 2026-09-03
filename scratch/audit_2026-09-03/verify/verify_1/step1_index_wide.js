// STEP 1 — reproduce the finding's index-wide numbers with the REAL JS renderer.
const E = require('./engine.js');
const fs = require('fs');
const FV = 'C:/git/Fire_Varna/';
const si = JSON.parse(fs.readFileSync(FV+'data/search_index.json','utf8'));
const ar = JSON.parse(fs.readFileSync(FV+'data/address_rows.json','utf8'));
E.setup(si, ar);
const ents = si.entries;
console.log('entries =', ents.length, ' district_names =', si.district_names.length);
const key = e => E.norm(E.formatAddressHit(e)) + '||' + (e.g != null ? String(e.g) : '');
const R=6371008.8, rad=x=>x*Math.PI/180;
function hav(a,b){const p1=rad(a[0]),p2=rad(b[0]);
  const x=Math.sin((p2-p1)/2)**2+Math.cos(p1)*Math.cos(p2)*Math.sin(rad(b[1]-a[1])/2)**2;
  return 2*R*Math.asin(Math.sqrt(x));}
const by = new Map();
for (const e of ents){ const k=key(e); if(!by.has(k)) by.set(k,[]); by.get(k).push(e); }
let keys=0, entries=0; const hist={'<5':0,'5-50':0,'50-200':0,'>200':0}; const byKind={};
const rowsOut=[];
for (const [k,arr] of by){
  const pins=[...new Set(arr.map(e=>e.pin[0]+','+e.pin[1]))].map(s=>s.split(',').map(Number));
  if (pins.length<2) continue;
  keys++; entries+=arr.length;
  let m=0;
  if (pins.length<=300){ for(let i=0;i<pins.length;i++) for(let j=i+1;j<pins.length;j++){const d=hav(pins[i],pins[j]); if(d>m)m=d;} }
  else { const la=pins.map(p=>p[0]), lo=pins.map(p=>p[1]);
         m=hav([Math.min(...la),Math.min(...lo)],[Math.max(...la),Math.max(...lo)]); }
  hist[m<5?'<5':m<50?'5-50':m<200?'50-200':'>200']++;
  const kd=arr[0].kind; byKind[kd]=(byKind[kd]||0)+1;
  rowsOut.push({label:E.formatAddressHit(arr[0]), entries:arr.length, pins:pins.length, spread:Math.round(m), kind:kd, hasLabel: arr[0].label!=null, hasDid: arr[0].display_id!=null});
}
console.log('keys_affected =',keys,' entries_affected =',entries);
console.log('histogram =',hist);
console.log('by_kind(keys) =',byKind);
// --- informativeness of the label: does it carry a house number? ------------
const hasNum = s => /(^|\s)\d+[а-яa-z]?(\s|$)/.test(E.norm(s));
const far = rowsOut.filter(r=>r.spread>=200);
console.log('>200m keys =',far.length,' of which label WITH a number =',far.filter(r=>hasNum(r.label)).length,
            ' without =',far.filter(r=>!hasNum(r.label)).length);
console.log('>200m entries =',far.reduce((a,r)=>a+r.entries,0),
            ' entries in numberless labels =',far.filter(r=>!hasNum(r.label)).reduce((a,r)=>a+r.entries,0));
far.sort((a,b)=>b.spread-a.spread);
console.log('--- top 12 by spread ---');
for (const r of far.slice(0,12)) console.log(String(r.spread).padStart(6), 'm  entries='+String(r.entries).padStart(5), 'pins='+String(r.pins).padStart(4), r.kind, hasNum(r.label)?'NUM':'---', JSON.stringify(r.label));
const mid = rowsOut.filter(r=>r.spread>=50&&r.spread<200);
console.log('50-200m keys =',mid.length,' with number =',mid.filter(r=>hasNum(r.label)).length);
fs.writeFileSync(__dirname+'/step1_keys.json', JSON.stringify(rowsOut,null,1));
