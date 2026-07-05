// E0 render-stack byte measurement (Fire_Varna V2 basemap feasibility).
//
// Measures the REAL added JS/CSS raw + gzip bytes of the three candidate render
// stacks against the SAME Varna fixture, so STOP E0 has real dependency-byte
// numbers (not estimates). Interactive-time / pan-zoom / memory / Cyrillic-label
// quality are browser-observable and are captured by the probe HTMLs on a real
// 375px device (Playwright is not installed here — see e0_stop_report.md).
//
//   node scratch/basemap_e0/measure_render_stack.mjs --all [--url http://127.0.0.1:8000]
//
// Downloads pinned dist files to the OS temp dir (NOT committed), measures bytes,
// writes e0_render_matrix.csv + e0_render_bytes.json next to this script.
// No push, no runtime change.

import { gzipSync } from 'node:zlib';
import { writeFileSync, mkdirSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));

// Pinned candidate stacks. Leaflet 1.9.4 + markercluster are ALREADY inlined in
// index.html (the shared baseline), so they are NOT counted as "added" bytes.
// leaflet.vectorgrid@1.3.0 is ALREADY an accepted SRI-pinned dep (building tiles).
const ASSETS = [
  // stack 1: protomaps-leaflet over existing Leaflet (minimal migration)
  { stack: 'protomaps-leaflet', role: 'renderer',
    url: 'https://unpkg.com/protomaps-leaflet@4.0.1/dist/protomaps-leaflet.js' },
  { stack: 'protomaps-leaflet', role: 'pmtiles-protocol',
    url: 'https://unpkg.com/pmtiles@3.2.1/dist/pmtiles.js' },
  // stack 2: MapLibre GL (full renderer migration)
  { stack: 'maplibre-gl', role: 'renderer-js',
    url: 'https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js' },
  { stack: 'maplibre-gl', role: 'renderer-css',
    url: 'https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.css' },
  { stack: 'maplibre-gl', role: 'pmtiles-protocol',
    url: 'https://unpkg.com/pmtiles@3.2.1/dist/pmtiles.js' },
  // stack 3: raster PMTiles over Leaflet (no new renderer)
  { stack: 'raster-pmtiles-leaflet', role: 'pmtiles-protocol',
    url: 'https://unpkg.com/pmtiles@3.2.1/dist/pmtiles.js' },
  // reference: the already-vendored vector-tile decoder (baseline, not "added")
  { stack: 'ref-leaflet-vectorgrid', role: 'already-vendored',
    url: 'https://unpkg.com/leaflet.vectorgrid@1.3.0/dist/Leaflet.VectorGrid.bundled.min.js' },
];

async function measure(url) {
  const res = await fetch(url, { redirect: 'follow' });
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
  const buf = Buffer.from(await res.arrayBuffer());
  return { raw: buf.length, gzip: gzipSync(buf, { level: 9 }).length, buf };
}

async function main() {
  const cacheDir = join(process.env.TEMP || '/tmp', 'fire_e0_libs');
  mkdirSync(cacheDir, { recursive: true });
  const rows = [];
  const byStack = {};
  for (const a of ASSETS) {
    let raw = null, gzip = null, err = null;
    try {
      const m = await measure(a.url);
      raw = m.raw; gzip = m.gzip;
      writeFileSync(join(cacheDir, a.url.split('/').pop()), m.buf);
    } catch (e) { err = String(e.message || e); }
    rows.push({ ...a, raw_bytes: raw, gzip_bytes: gzip, error: err });
    if (a.role !== 'already-vendored') {
      byStack[a.stack] = byStack[a.stack] || { raw: 0, gzip: 0, assets: [] };
      if (raw != null) { byStack[a.stack].raw += raw; byStack[a.stack].gzip += gzip; }
      byStack[a.stack].assets.push(`${a.role}:${a.url.split('/').pop()}`);
    }
    console.error(`[render-bytes] ${a.stack}/${a.role}: raw=${raw} gzip=${gzip}${err ? ' ERR ' + err : ''}`);
  }

  // qualitative fields are device-observed via the probes; recorded as pending here.
  const MATRIX = [
    { stack: 'protomaps-leaflet', migration: 'minimal (keeps Leaflet+overlays)',
      cyrillic: 'probe:leaflet_protomaps_probe.html', satellite_toggle: 'independent (L.tileLayer swap kept)',
      range_offline: 'PMTiles range + Cache API (see measure_range/measure_offline_sw)',
      integration_risk: 'low (Leaflet overlays unchanged; already run L.vectorGrid path)' },
    { stack: 'maplibre-gl', migration: 'full renderer swap (rewrite map shell + overlays)',
      cyrillic: 'probe:maplibre_probe.html', satellite_toggle: 'reimplement as GL raster source',
      range_offline: 'native PMTiles protocol + SW cache',
      integration_risk: 'high (hydrants/search/building popups re-port to GL)' },
    { stack: 'raster-pmtiles-leaflet', migration: 'none (L.tileLayer raster)',
      cyrillic: 'baked at build time (probe:raster_pmtiles_probe.html)', satellite_toggle: 'independent',
      range_offline: 'PMTiles range (raster tiles); larger files',
      integration_risk: 'low, but larger size + no runtime restyle' },
  ];
  const matrixRows = MATRIX.map(m => ({
    ...m,
    added_raw_bytes: byStack[m.stack]?.raw ?? '',
    added_gzip_bytes: byStack[m.stack]?.gzip ?? '',
    added_assets: (byStack[m.stack]?.assets || []).join(' + '),
  }));

  const header = ['stack', 'added_raw_bytes', 'added_gzip_bytes', 'added_assets',
    'migration', 'cyrillic_labels', 'satellite_toggle', 'range_offline', 'integration_risk'];
  const csv = [header.join(',')].concat(matrixRows.map(m => [
    m.stack, m.added_raw_bytes, m.added_gzip_bytes, q(m.added_assets), q(m.migration),
    q(m.cyrillic), q(m.satellite_toggle), q(m.range_offline), q(m.integration_risk),
  ].join(','))).join('\n') + '\n';
  writeFileSync(join(HERE, 'e0_render_matrix.csv'), csv);
  writeFileSync(join(HERE, 'e0_render_bytes.json'),
    JSON.stringify({ measured_utc_note: 'pinned versions; content-addressed by version',
      assets: rows, per_stack_added: byStack, matrix: matrixRows }, null, 2) + '\n');
  console.error(`[render-bytes] wrote e0_render_matrix.csv + e0_render_bytes.json to ${HERE}`);
}

function q(s) { return '"' + String(s).replace(/"/g, '""') + '"'; }

main().catch(e => { console.error('FATAL', e); process.exit(1); });
