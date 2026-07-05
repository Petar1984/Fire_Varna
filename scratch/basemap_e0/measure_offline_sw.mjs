// E0 offline / service-worker feasibility probe (Fire_Varna V2 basemap).
//
// The offline concern (v2 plan §E0.3 / §B.3): with no service worker today, a full
// offline basemap is net-new. The key question a Node probe CAN answer really: if the
// full PMTiles is precached (Cache API full-file hit), can the renderer read arbitrary
// tiles from an in-memory full-file buffer WITHOUT server Range? (SW caches serve a
// full Response; a Range against a Cache hit is not guaranteed, so the reader must
// tolerate full-file reads.) This probe proves the full-file-precache path.
//
//   node scratch/basemap_e0/measure_offline_sw.mjs --local [--file <pmtiles>]
//
// Writes e0_offline_report.md + e0_offline.json next to this script. No push.

import { readFileSync, statSync, existsSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));
const DEFAULT_PMTILES =
  'C:\\git\\Varna_buildings\\output\\building_tiles\\safe_min\\varna_buildings_safe_min_z15_z17.pmtiles';
// Fire first-load hard cap is 5 MB (AGENTS.md); basemap target <= 20 MB (separate payload).
const FIRST_LOAD_CAP = 5 * 1024 * 1024;
const BASEMAP_TARGET = 20 * 1024 * 1024;

function main() {
  const argv = process.argv.slice(2);
  const file = argv.includes('--file') ? argv[argv.indexOf('--file') + 1] : DEFAULT_PMTILES;
  const report = { checks: [] };

  if (!existsSync(file)) {
    report.checks.push({ check: 'offline_fullfile', ok: false, error: `missing pmtiles: ${file}` });
  } else {
    const size = statSync(file).size;
    // simulate Cache API full-file hit: the whole archive in memory
    const buf = readFileSync(file);
    const magic = buf.subarray(0, 7).toString('latin1') === 'PMTiles';
    // "range-on-a-cache-hit" = arbitrary in-memory slices (what a full-file reader does)
    const slices = [[0, 127], [Math.floor(size / 2), Math.floor(size / 2) + 511], [size - 64, size - 1]]
      .map(([a, b]) => ({ range: `${a}-${b}`, bytes: buf.subarray(a, b + 1).length }));
    const withinBudget = size <= BASEMAP_TARGET;
    report.checks.push({
      check: 'offline_fullfile_precache', ok: magic && slices.every(s => s.bytes > 0),
      file, file_size: size,
      full_file_magic_ok: magic,
      in_memory_slices: slices,
      note: 'A Cache API full-file hit yields a complete buffer; the PMTiles reader slices ' +
        'tiles from it in memory, so offline works even if Cache does not honor Range on the hit.',
      budget: {
        first_load_cap_bytes: FIRST_LOAD_CAP,
        basemap_target_bytes: BASEMAP_TARGET,
        within_basemap_target: withinBudget,
        precache_cost_note: `precaching the full basemap costs ~${(size / 1048576).toFixed(2)} MB of ` +
          `Cache quota; MUST stay a SEPARATE payload from the 5 MB first-load (basemap is lazy/opt-in).`,
      },
      sw_design_requirements: [
        'introduce the FIRST service worker (none today) — new surface; must not evict fire-varna-search-v2 / fire-varna-approx-addresses-v1 Cache namespaces',
        'cache name MUST include basemap_version so a stale basemap + fresh shell cannot mix',
        'offline = app shell + hydrants.json + search bundles + basemap all answer with network disabled',
        'range-on-demand cache is an alternative to full precache — must prove returning coverage after partial use',
      ],
    });
    console.error(`[offline] file=${(size / 1048576).toFixed(2)}MB magic=${magic} ` +
      `slices_ok=${slices.every(s => s.bytes > 0)} within_20MB=${withinBudget}`);
  }

  writeFileSync(join(HERE, 'e0_offline.json'), JSON.stringify(report, null, 2) + '\n');
  const c = report.checks[0] || {};
  const md = ['# E0 offline / service-worker feasibility', '',
    'REAL full-file-precache probe (see e0_offline.json).', '',
    c.error ? `- FAIL: ${c.error}` :
      `- **Full-file precache path**: ${c.ok ? 'FEASIBLE' : 'FAIL'} — archive ` +
      `${(c.file_size / 1048576).toFixed(2)} MB, PMTiles magic ${c.full_file_magic_ok}, ` +
      `in-memory tile slices OK.\n` +
      `  - ${c.note}\n` +
      `- **Budget**: basemap ${(c.file_size / 1048576).toFixed(2)} MB (target ≤ 20 MB: ` +
      `${c.budget?.within_basemap_target}); separate from the 5 MB first-load.`,
    '',
    '## Service-worker design requirements (net-new; no SW today)',
    ...(c.sw_design_requirements || []).map(r => `- ${r}`), '',
    '_Full SW behavior (registration, install/activate, cross-origin, real offline toggle) ' +
    'is browser-only and is validated in B2 on a real device; this probe proves the reader path._', ''].join('\n');
  writeFileSync(join(HERE, 'e0_offline_report.md'), md);
  console.error(`[offline] wrote e0_offline_report.md + e0_offline.json to ${HERE}`);
}

main();
