// E0 HTTP Range gate (Fire_Varna V2 basemap feasibility).
//
// PMTiles needs HTTP Range (206) to read a tile without downloading the whole file.
// This probe measures Range behavior REALLY, three ways:
//
//   node scratch/basemap_e0/measure_range.mjs --local [--file <pmtiles>]
//       Spin up a Range-capable Node static server serving an existing .pmtiles,
//       issue a Range request, assert 206 + Content-Range + Accept-Ranges, and
//       verify the PMTiles v3 magic bytes from a 0-126 byte read (client+reader path).
//
//   node scratch/basemap_e0/measure_range.mjs --pages-existing
//       Probe the LIVE GitHub Pages CDN Range behavior on an EXISTING asset
//       (index.html) — measures whether Pages honors Range NOW, without a canary push.
//
//   node scratch/basemap_e0/measure_range.mjs --url <URL>
//       Range request against a remote URL (e.g. the Pages .pmtiles canary once pushed).
//
// Writes e0_range_report.md + e0_range.json next to this script. No push.

import { createServer } from 'node:http';
import { createReadStream, statSync, existsSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));
const DEFAULT_PMTILES =
  'C:\\git\\Varna_buildings\\output\\building_tiles\\safe_min\\varna_buildings_safe_min_z15_z17.pmtiles';
const PAGES_EXISTING = 'https://petar1984.github.io/Fire_Varna/index.html';

function rangeServer(filePath) {
  const size = statSync(filePath).size;
  const server = createServer((req, res) => {
    const range = req.headers.range;
    if (range) {
      const m = /bytes=(\d+)-(\d*)/.exec(range);
      const start = Number(m[1]);
      const end = m[2] ? Number(m[2]) : size - 1;
      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${size}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': end - start + 1,
        'Content-Type': 'application/octet-stream',
      });
      createReadStream(filePath, { start, end }).pipe(res);
    } else {
      res.writeHead(200, { 'Content-Length': size, 'Accept-Ranges': 'bytes' });
      createReadStream(filePath).pipe(res);
    }
  });
  return new Promise(resolve => server.listen(0, '127.0.0.1',
    () => resolve({ server, port: server.address().port, size })));
}

async function rangeFetch(url, first, last) {
  const res = await fetch(url, { headers: { Range: `bytes=${first}-${last}` } });
  const buf = Buffer.from(await res.arrayBuffer());
  return {
    status: res.status,
    content_range: res.headers.get('content-range'),
    accept_ranges: res.headers.get('accept-ranges'),
    content_length: res.headers.get('content-length'),
    content_type: res.headers.get('content-type'),
    bytes_returned: buf.length,
    first7: buf.subarray(0, 7).toString('latin1'),
  };
}

async function main() {
  const argv = process.argv.slice(2);
  const fileArg = argv.includes('--file') ? argv[argv.indexOf('--file') + 1] : DEFAULT_PMTILES;
  const report = { checks: [] };

  if (argv.includes('--local')) {
    if (!existsSync(fileArg)) {
      report.checks.push({ check: 'local', ok: false, error: `missing pmtiles: ${fileArg}` });
    } else {
      const { server, port, size } = await rangeServer(fileArg);
      const url = `http://127.0.0.1:${port}/basemap.pmtiles`;
      const head = await rangeFetch(url, 0, 126);
      const mid = await rangeFetch(url, Math.floor(size / 2), Math.floor(size / 2) + 255);
      server.close();
      const ok = head.status === 206 && /bytes 0-126\//.test(head.content_range || '') &&
        head.first7 === 'PMTiles' && mid.status === 206;
      report.checks.push({
        check: 'local_range_capable_server', ok, file: fileArg, file_size: size,
        head_read: head, mid_read: mid,
        note: 'Node Range-capable server + PMTiles v3 magic verified from a 127-byte read',
      });
      console.error(`[range:local] 206=${head.status === 206} magic=${head.first7 === 'PMTiles'} ` +
        `content-range=${head.content_range} -> ${ok ? 'PASS' : 'FAIL'}`);
    }
  }

  if (argv.includes('--pages-existing')) {
    try {
      const r = await rangeFetch(PAGES_EXISTING, 0, 126);
      const ok = r.status === 206 && !!r.content_range;
      report.checks.push({
        check: 'github_pages_range_existing_asset', ok, url: PAGES_EXISTING, result: r,
        note: 'Range behavior of the live Pages CDN on an existing asset (not a .pmtiles). ' +
          'A .pmtiles canary is still needed to confirm content-type + Range for that extension.',
      });
      console.error(`[range:pages] status=${r.status} content-range=${r.content_range} ` +
        `accept-ranges=${r.accept_ranges} -> ${ok ? '206 PASS' : 'NO-206'}`);
    } catch (e) {
      report.checks.push({ check: 'github_pages_range_existing_asset', ok: false, error: String(e) });
    }
  }

  const urlIdx = argv.indexOf('--url');
  if (urlIdx >= 0 && argv[urlIdx + 1]) {
    const url = argv[urlIdx + 1];
    try {
      const r = await rangeFetch(url, 0, 126);
      report.checks.push({ check: 'remote_url_range', ok: r.status === 206, url, result: r });
      console.error(`[range:url] ${url} status=${r.status} content-range=${r.content_range}`);
    } catch (e) {
      report.checks.push({ check: 'remote_url_range', ok: false, url, error: String(e) });
    }
  }

  writeFileSync(join(HERE, 'e0_range.json'), JSON.stringify(report, null, 2) + '\n');
  const md = ['# E0 HTTP Range report', '',
    'REAL Range probes (see e0_range.json for full payloads).', '',
    ...report.checks.map(c => `- **${c.check}**: ${c.ok ? 'PASS' : 'FAIL/PENDING'}` +
      (c.result ? ` — status ${c.result.status}, content-range \`${c.result.content_range}\`` : '') +
      (c.error ? ` — ${c.error}` : '') + (c.note ? `\n  - ${c.note}` : '')),
    '', '_Pages `.pmtiles` canary (content-type + Range for the extension) still requires ' +
    'a Petar canary push; Range behavior of the Pages CDN itself is measured above._', ''].join('\n');
  writeFileSync(join(HERE, 'e0_range_report.md'), md);
  console.error(`[range] wrote e0_range_report.md + e0_range.json to ${HERE}`);
}

main().catch(e => { console.error('FATAL', e); process.exit(1); });
