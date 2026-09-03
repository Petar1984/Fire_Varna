// Read-only harness: runs the LIVE index.html geocoder search + dedupeDisplayRows
// against the shipped data. Nothing in C:/git is written.
const fs = require('fs');
let addressRows = null, addrFieldIdx = null, districtNames = [];
const SRC = fs.readFileSync(__dirname + '/_extract.js', 'utf8');
eval(SRC);
const idx = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/search_index.json', 'utf8'));
const rowsPayload = JSON.parse(fs.readFileSync('C:/git/Fire_Varna/data/address_rows.json', 'utf8'));
addressRows = rowsPayload.rows;
addrFieldIdx = buildAddressFieldIndex(rowsPayload);
districtNames = idx.district_names || [];
prepareIndex(idx);

const queries = process.argv.slice(2);
const out = [];
for (const q of queries) {
  let rows = runGeocoderSearch(q, idx);
  const before = rows.length;
  const hdr = rows.blockHeader ? ('blockHeader: ' + rows.blockHeader.count + ' блока № ' + rows.blockHeader.block +
      (rows.blockHeader.district_enum != null ? ' в район ' + districtNames[rows.blockHeader.district_enum] : ''))
    : (rows.bareBlockHeader ? ('bareBlockHeader: ' + rows.bareBlockHeader.groups + ' блока № ' + rows.bareBlockHeader.block) : null);
  rows = dedupeDisplayRows(rows);
  const shown = rows.slice(0, 10).map(function (r, i) {
    return (i + 1) + '. [' + (r.kind === 'mf' && r.en != null ? 'вход' : r.kind) + '] "' + formatAddressHit(r) + '"' +
      (r.d != null && districtNames[r.d] ? ('  | район ' + districtNames[r.d]) : '') +
      '  | pin ' + r.pin[0] + ',' + r.pin[1] + '  | g=' + String(r.g);
  });
  out.push({ query: q, rows_before_dedupe: before, rows_after_dedupe: rows.length, header: hdr, shown: shown });
}
console.log(JSON.stringify(out, null, 1));
