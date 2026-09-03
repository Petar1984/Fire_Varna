// Cuts the LIVE address-search engine VERBATIM out of C:/git/Fire_Varna/index.html.
// Anchors are re-derived on every run, so a moving HEAD cannot silently shift a slice.
const fs = require('fs'), cp = require('child_process');
const SRC = 'C:/git/Fire_Varna/index.html';
const L = fs.readFileSync(SRC, 'utf8').split(/\r?\n/);
const HEAD = cp.execSync('git -C C:/git/Fire_Varna rev-parse --short HEAD').toString().trim();
const slice = (a, b) => L.slice(a - 1, b).join('\n');       // 1-indexed inclusive
function must(re, from, to, what) {
  for (let i = from; i <= to; i++) if (re.test(L[i - 1])) return i;
  throw new Error('anchor not found: ' + what);
}
const A_IIFE  = must(/\(function initAddressSearch\(\) \{/, 4000, 6000, 'initAddressSearch');
const A_PRIM  = must(/---- skeleton primitives \(verbatim from app\/modules\/search\/skeleton\.js\) ----/, A_IIFE, A_IIFE + 100, 'primitives');
const A_GPS   = must(/GPS coordinate input \(kind:"coord"\)/, A_PRIM, A_PRIM + 200, 'gps');
const A_F2    = must(/F2 \(search-quality cycle, frame/, A_GPS, A_GPS + 400, 'F2 dedupe');
const A_GEO   = must(/---- ported runGeocoderSearch \(public-safe geocoder route\) ----/, A_F2, A_F2 + 200, 'runGeocoderSearch');
const A_LAZY  = must(/---- lazy load \+ cache \(memory for the session/, A_GEO, A_GEO + 400, 'lazy load');
// trim the two trailing blank/comment lines that separate blocks
const endPrim = A_GPS - 3;      // 4894 = last "}" of formatAddressHit
const endF2   = A_GEO - 2;      // last "}" of dedupeDisplayRows
const endGeo  = A_LAZY - 2;     // last "}" of runGeocoderSearch
for (const [n, ln] of [['prim end', endPrim], ['F2 end', endF2], ['geo end', endGeo]])
  if (!/^\s*\}\s*$/.test(L[ln - 1])) throw new Error('slice end is not "}" for ' + n + ' @ ' + ln + ': ' + L[ln - 1]);
const body = [
  '// AUTO-EXTRACTED VERBATIM from ' + SRC + ' @ HEAD ' + HEAD,
  "// slices: primitives+labels " + A_PRIM + '-' + endPrim + ', dedupeDisplayRows ' + A_F2 + '-' + endF2 + ', runGeocoderSearch ' + A_GEO + '-' + endGeo,
  "'use strict';",
  slice(A_PRIM, endPrim),
  slice(A_F2, endF2),
  slice(A_GEO, endGeo),
  '',
  '// ---- harness (NOT from index.html) ----------------------------------------',
  'function setup(si, ar) {',
  '  addressRows = ar.rows;',
  '  addrFieldIdx = buildAddressFieldIndex(ar);',
  '  districtNames = si.district_names || [];',
  '  return prepareIndex(si);',
  '}',
  'module.exports = { setup, runGeocoderSearch, dedupeDisplayRows, formatAddressHit,',
  '                   baseAddressLabel, labelBlockNumber, norm, skel, lev, matchKindSet,',
  '                   SEARCH_LIMIT, anchors: { A_PRIM: ' + A_PRIM + ', endPrim: ' + endPrim +
      ', A_F2: ' + A_F2 + ', endF2: ' + endF2 + ', A_GEO: ' + A_GEO + ', endGeo: ' + endGeo + ' },',
  '                   get districtNames(){ return districtNames; } };',
  ''
].join('\n');
fs.writeFileSync(process.argv[2] || 'engine.js', body);
console.log('HEAD=%s  prim=%d-%d  F2=%d-%d  geo=%d-%d  bytes=%d', HEAD, A_PRIM, endPrim, A_F2, endF2, A_GEO, endGeo, body.length);
