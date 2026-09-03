// READ-ONLY harness: lifts the LIVE search core out of C:/git/Fire_Varna/index.html
// (initPlacesSearch), strips only the 4 DOM lines, and runs it over the real data.
const fs = require('fs'), path = require('path');
const ROOT = 'C:/git/Fire_Varna';
const src = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8').split(/\r?\n/);
// 1-based line numbers, verified by grep at HEAD:
const L_START = 6246;            // const HOTELS_SEARCH_ENABLED = true;
const L_DOM_A = 6248, L_DOM_B = 6251;   // the 4 document.getElementById lines + early return
const L_END   = 6682;            // last line of function search(){...}
const body = src.slice(L_START - 1, L_END)
  .filter((_, i) => { const ln = L_START + i; return !(ln >= L_DOM_A && ln <= L_DOM_B); })
  .join('\n');

const code = `(function () {
${body}
  return { buildIndex: buildIndex, search: search, placeTokens: placeTokens,
           keyOf: keyOf, splitKeys: splitKeys, recs: () => RECS,
           classOf: () => CLASS_OF, forms: () => FORMS, groupOf: groupOf,
           groupSize: () => GROUP_SIZE };
})()`;
global.window = {};
global.map = { getCenter: () => (global.__CENTER || null) };
const api = eval(code);
const hotels = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/hotels.json'), 'utf8')).hotels;
const places2 = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/places.json'), 'utf8')).places;
const cats = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/place_categories.json'), 'utf8'));
api.buildIndex(hotels, places2, cats);
module.exports = api;
