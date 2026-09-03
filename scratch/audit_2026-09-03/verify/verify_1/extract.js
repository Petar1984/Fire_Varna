// Extracts the LIVE search core from C:/git/Fire_Varna/index.html into a runnable module.
const fs = require('fs');
const SRC = 'C:/git/Fire_Varna/index.html';
const L = fs.readFileSync(SRC, 'utf8').split(/\r?\n/);
const slice = (a, b) => L.slice(a - 1, b).join('\n');   // 1-indexed inclusive

function must(re, from, to, what) {
  for (let i = from; i <= to; i++) if (re.test(L[i - 1])) return i;
  throw new Error('anchor not found: ' + what);
}
// anchors, re-derived every run so a moving HEAD cannot silently shift the slice
const A_PRIM  = must(/primitives: VERBATIM copies/, 6000, 7200, 'primitives');
const A_STATE = must(/let RECS = \[\], FORMS = null/, A_PRIM, 7200, 'state');
const A_ENSURE= must(/function ensurePlaces\(\)/, A_STATE, 7200, 'ensurePlaces');
const A_BUILD = must(/function buildIndex\(hotels, places2, cats\)/, A_ENSURE, 7200, 'buildIndex');
const A_HASKEY= must(/const hasKeyFor = /, A_BUILD, 7200, 'hasKeyFor');
const A_KG    = must(/const KIND_GROUP = \{/, 6000, A_PRIM, 'KIND_GROUP');
const A_CONST = must(/const TOP_TOTAL = 16, GEN_CAP = 300;/, 6000, A_PRIM, 'GEN_CAP');
const A_MXMY  = must(/const MX = 81152, MY = 110574;/, 6000, A_PRIM, 'MX/MY');
const A_TOP   = must(/const TOP = 8, MIN_Q = 2/, 6000, A_PRIM, 'TOP');

const parts = [
  '// ---- constants lifted verbatim',
  slice(A_TOP, A_TOP), slice(A_CONST, A_CONST), slice(A_MXMY, A_MXMY),
  slice(A_KG, must(/^\s*\};\s*$/, A_KG, A_KG + 20, 'KIND_GROUP end')),
  '// ---- primitives + tokenizer + state (verbatim ' + A_PRIM + '-' + (A_ENSURE - 1) + ')',
  slice(A_PRIM, A_ENSURE - 1),
  '// ---- buildIndex .. search .. hasKeyFor (verbatim ' + A_BUILD + '-' + A_HASKEY + ')',
  slice(A_BUILD, A_HASKEY),
  'const map = null;',                 // centre() is wrapped in try/catch -> returns null
  'module.exports = { buildIndex, search, splitKeys, placeTokens, tokenMatch, RECSref: () => RECS, CLASSref: () => CLASS_OF };'
];
let body = parts.join('\n');
// centre() reads `map`; declare it before use by hoisting our stub to the top
body = 'var map = null;\n' + body.replace('const map = null;', '');
fs.writeFileSync(process.argv[2], body);
console.log('anchors: prim=%d state=%d ensure=%d build=%d hasKeyFor=%d', A_PRIM, A_STATE, A_ENSURE, A_BUILD, A_HASKEY);
console.log('extracted bytes:', body.length);
