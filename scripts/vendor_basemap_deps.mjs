#!/usr/bin/env node
// Vendor the pinned basemap runtime deps into Fire_Varna (Basemap B2 §6.3).
//
// Node stdlib only. Downloads the two pinned files from unpkg, writes them under
// vendor/basemap/ durably (temp -> fsync -> rename), re-reads each from disk, computes
// bytes + sha256 + sha384 SRI, asserts the raw byte counts against the E0-pinned anchors
// (npm pinned versions are immutable, so a mismatch means a bad/tampered download -> STOP),
// writes scratch/basemap_b2/vendor_report.json, and creates/updates
// data/basemaps/basemap_manifest.json with the computed hashes/SRI. No CDN at runtime:
// these files are served same-origin; the manifest carries their SRI for the loader.

import { createHash } from 'node:crypto';
import { promises as fs } from 'node:fs';
import * as fssync from 'node:fs';
import * as https from 'node:https';
import * as path from 'node:path';

const DEPS = [
  {
    name: 'pmtiles',
    version: '3.2.1',
    url: 'https://unpkg.com/pmtiles@3.2.1/dist/pmtiles.js',
    out: 'vendor/basemap/pmtiles-3.2.1.js',
    expect_bytes: 51739, // E0 anchor (§6.3)
  },
  {
    name: 'protomaps-leaflet',
    version: '4.0.1',
    url: 'https://unpkg.com/protomaps-leaflet@4.0.1/dist/protomaps-leaflet.js',
    out: 'vendor/basemap/protomaps-leaflet-4.0.1.js',
    expect_bytes: 100591, // E0 anchor (§6.3)
  },
];

// B1-locked basemap facts (mirror of the copied B1 manifest; asserted by the static gate).
const BASEMAP_LOCK = {
  pmtiles_bytes: 5748578,
  pmtiles_sha256: '29a8dee66465bed3eabaa2afa70efbe703b9e63b9cde84d4dcadb2436435f1b8',
  content_sha256: '8a15054e722b12cb31afbc6cc3ff13a4cb7401dda7a8291f139794ac286fc3b8',
  style_sha256: '62cc123ee2227c4a95a249a2f788010eee57067a5ce72c594b4318834fc69135',
};

function arg(flag, required = true) {
  const i = process.argv.indexOf(flag);
  if (i === -1 || i + 1 >= process.argv.length) {
    if (required) { console.error(`missing ${flag}`); process.exit(2); }
    return undefined;
  }
  return process.argv[i + 1];
}

function download(url, redirects = 0) {
  return new Promise((resolve, reject) => {
    if (redirects > 5) return reject(new Error('too many redirects: ' + url));
    https.get(url, { headers: { 'User-Agent': 'fire-varna-vendor/1' } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        res.resume();
        const next = new URL(res.headers.location, url).toString();
        return resolve(download(next, redirects + 1));
      }
      if (res.statusCode !== 200) {
        res.resume();
        return reject(new Error(`HTTP ${res.statusCode} for ${url}`));
      }
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => resolve(Buffer.concat(chunks)));
      res.on('error', reject);
    }).on('error', reject);
  });
}

async function durableWrite(outPath, buf) {
  await fs.mkdir(path.dirname(outPath), { recursive: true });
  const tmp = outPath + '.tmp';
  const fh = await fs.open(tmp, 'w');
  try {
    await fh.write(buf);
    await fh.sync();
  } finally {
    await fh.close();
  }
  await fs.rename(tmp, outPath);
}

function sha256hex(buf) { return createHash('sha256').update(buf).digest('hex'); }
function sri384(buf) { return 'sha384-' + createHash('sha384').update(buf).digest('base64'); }

async function main() {
  const manifestPath = arg('--manifest');
  const reportPath = arg('--report');
  const version = arg('--basemap-version');

  const report = { version, deps: [], ok: false };
  const depEntries = [];
  let allOk = true;

  for (const d of DEPS) {
    const buf = await download(d.url);
    await durableWrite(d.out, buf);
    const reread = fssync.readFileSync(d.out); // re-open from disk
    const bytes = reread.length;
    const sha256 = sha256hex(reread);
    const sri = sri384(reread);
    const bytesMatch = bytes === d.expect_bytes;
    allOk = allOk && bytesMatch;
    report.deps.push({
      name: d.name, version: d.version, source_url: d.url, path: d.out,
      bytes, expect_bytes: d.expect_bytes, bytes_match: bytesMatch,
      sha256, sri_sha384: sri,
    });
    depEntries.push({
      name: d.name, version: d.version, path: d.out, source_url: d.url,
      bytes, sha256, sri_sha384: sri,
    });
    console.log(`${d.name}@${d.version}: ${bytes} bytes (expect ${d.expect_bytes}, ${bytesMatch ? 'MATCH' : 'MISMATCH'}) sha256 ${sha256.slice(0, 12)}`);
  }

  report.ok = allOk;
  await durableWriteJson(reportPath, report);

  if (!allOk) {
    console.error('vendor_basemap_deps: STOP — byte anchor mismatch (immutable pinned version should match E0).');
    process.exit(1);
  }

  // --- Build/update the Fire runtime basemap manifest ---
  const manifest = {
    schema_version: 'fire_varna_basemap_manifest_v1',
    active_version: version,
    cache_version: version,
    basemap: {
      pmtiles_path: `data/basemaps/${version}/varna_basemap.pmtiles`,
      style_path: `data/basemaps/${version}/style.json`,
      b1_manifest_path: `data/basemaps/${version}/varna_basemap_manifest.json`,
      odbl_readme_path: `data/basemaps/${version}/odbl/README_ODbL.md`,
      odbl_patch_csv_path: `data/basemaps/${version}/odbl/osm_varna_patch_v1.csv`,
      pmtiles_bytes: BASEMAP_LOCK.pmtiles_bytes,
      pmtiles_sha256: BASEMAP_LOCK.pmtiles_sha256,
      content_sha256: BASEMAP_LOCK.content_sha256,
      style_sha256: BASEMAP_LOCK.style_sha256,
    },
    runtime_deps: depEntries,
    cache_names: {
      core: `fire-varna-core-${version}`,
      offline_pack: `fire-varna-offline-pack-${version}`,
      basemap: `fire-varna-basemap-${version}`,
    },
  };
  await durableWriteJson(manifestPath, manifest);
  console.log('vendor_basemap_deps: OK');
  console.log('  manifest:', path.resolve(manifestPath));
  console.log('  report:', path.resolve(reportPath));
}

async function durableWriteJson(p, obj) {
  await fs.mkdir(path.dirname(path.resolve(p)), { recursive: true });
  const tmp = p + '.tmp';
  const fh = await fs.open(tmp, 'w');
  try {
    await fh.write(JSON.stringify(obj, null, 2) + '\n');
    await fh.sync();
  } finally {
    await fh.close();
  }
  await fs.rename(tmp, p);
}

main().catch((e) => { console.error('vendor_basemap_deps: ERROR', e); process.exit(3); });
