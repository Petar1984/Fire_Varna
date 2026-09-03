const fs=require('fs'); const E=require('./engine.js');
const keys=JSON.parse(fs.readFileSync(__dirname+'/step1_keys.json','utf8'));
const hasNum=s=>/(^|\s)\d+[а-яa-z]?(\s|$)/.test(E.norm(s));
const B=[['<5',0,5],['5-50',5,50],['50-200',50,200],['>200',200,1e9]];
let tk=0,te=0;
console.log('bucket        keys   entries |  keys w/ house number  entries');
for(const [n,lo,hi] of B){
  const g=keys.filter(k=>k.spread>=lo&&k.spread<hi);
  const gn=g.filter(k=>hasNum(k.label));
  tk+=g.length; te+=g.reduce((a,k)=>a+k.entries,0);
  console.log(n.padEnd(8), String(g.length).padStart(6), String(g.reduce((a,k)=>a+k.entries,0)).padStart(9), '  | ',
    String(gn.length).padStart(6), String(gn.reduce((a,k)=>a+k.entries,0)).padStart(9));
}
console.log('TOTAL   ', String(tk).padStart(6), String(te).padStart(9));
const real=keys.filter(k=>k.spread>=50 && hasNum(k.label));
console.log('\n"real hidden second address" (>=50 m AND label carries a number):',
  real.length,'keys /', real.reduce((a,k)=>a+k.entries,0),'entries');
const real200=keys.filter(k=>k.spread>=200 && hasNum(k.label));
console.log('  of them >=200 m:', real200.length,'keys /', real200.reduce((a,k)=>a+k.entries,0),'entries');
console.log('\nthe 5 biggest numberless far labels (no way to type them apart at all):');
keys.filter(k=>k.spread>=200&&!hasNum(k.label)).sort((a,b)=>b.entries-a.entries).slice(0,5)
  .forEach(k=>console.log('   entries='+String(k.entries).padStart(5),'spread='+String(k.spread).padStart(6)+'m',JSON.stringify(k.label)));
