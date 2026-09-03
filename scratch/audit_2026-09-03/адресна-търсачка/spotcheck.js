// Hand-checkable spot checks: prints the dropdown EXACTLY as renderResults would
// build it (dedupeDisplayRows -> formatAddressHit + chip + район meta), for queries
// Petar can retype in the live search box.
'use strict';
const fs = require('fs');
const E = require('./engine.js');
const si = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/search_index.json','utf8'));
const ar = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/address_rows.json','utf8'));
const idx = E.setup(si, ar);
const DN = si.district_names || [];
function chip(h){ if (h.kind==='mf' && h.en!=null) return '\u0432\u0445\u043e\u0434';
  if (h.kind==='parcel') return '\u043f\u0430\u0440\u0446\u0435\u043b';
  if (h.kind==='mf') return '\u0441\u0433\u0440\u0430\u0434\u0430'; return '\u0430\u0434\u0440\u0435\u0441'; }
console.log('vocab has "kv"? ', idx.vocab.indexOf('kv') >= 0, ' | "zh"? ', idx.vocab.indexOf('zh') >= 0,
            ' | "adres:"? ', idx.vocab.indexOf('adres:') >= 0, ' | "\u00b7"? ', idx.vocab.indexOf('\u00b7') >= 0);
const QS = process.argv.slice(2);
for (const q of QS) {
  const raw = E.runGeocoderSearch(q, idx);
  const ded = E.dedupeDisplayRows(raw);
  console.log('\n=== ' + JSON.stringify(q) + '   raw=' + raw.length + ' -> shown=' + ded.length +
    (ded.blockHeader ? '  header: ' + ded.blockHeader.count + ' \u0431\u043b\u043e\u043a\u0430 \u2116 ' + ded.blockHeader.block : ''));
  ded.forEach(function(r,i){
    console.log('  ' + (i+1) + '. [' + chip(r) + '] ' + E.formatAddressHit(r) +
      (r.d!=null&&DN[r.d]?('   \u2014 \u0440\u0430\u0439\u043e\u043d ' + DN[r.d]):'') +
      '   pin=' + JSON.stringify(r.pin));
  });
  if (!ded.length) console.log('  (\u041d\u044f\u043c\u0430 \u0441\u044a\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u044f)');
}
