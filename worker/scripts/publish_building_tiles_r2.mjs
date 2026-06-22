#!/usr/bin/env node
// publish_building_tiles_r2.mjs — upload the E1 "safe_min" building PMTiles to
// the private R2 bucket that the Worker's /tiles/* gateway reads from.
//
// SAFETY MODEL (read before running):
//   * DRY-RUN IS THE DEFAULT. With no flags it only verifies the E1 manifest and
//     prints the object key Petar should use. It NEVER touches the network.
//   * A real upload happens ONLY when BOTH --apply AND --remote are passed AND a
//     --bucket is given. That path shells out to `wrangler r2 object put` using
//     Petar's own wrangler auth. This script never creates a bucket, never sets
//     a secret/binding, never deploys the Worker, and never publishes a public
//     URL. Those remain Petar's-hand dashboard steps.
//   * It refuses to upload unless the E1 manifest gate is all_pass AND the
//     pmtiles file's SHA-256 matches the manifest. (Per E1 determinism: the
//     pmtiles byte hash is a determinism criterion; the mbtiles hash is not.)
//
// Usage:
//   node scripts/publish_building_tiles_r2.mjs                 # dry-run (default)
//   node scripts/publish_building_tiles_r2.mjs --manifest <p> --pmtiles <p>
//   node scripts/publish_building_tiles_r2.mjs --apply --remote --bucket <name>   # Petar's hand only

import { readFileSync, statSync } from "node:fs";
import { createHash } from "node:crypto";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
// scripts/ -> worker/ -> Fire_Varna/ -> c:\git\ -> Varna_buildings/output/...
const REPO_ROOT = resolve(SCRIPT_DIR, "..", "..", "..");
const DEFAULT_E1_DIR = resolve(
  REPO_ROOT,
  "Varna_buildings",
  "output",
  "building_tiles",
  "safe_min"
);

function parseArgs(argv) {
  const args = { apply: false, remote: false };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === "--apply") args.apply = true;
    else if (arg === "--remote") args.remote = true;
    else if (arg === "--manifest") args.manifest = argv[++i];
    else if (arg === "--pmtiles") args.pmtiles = argv[++i];
    else if (arg === "--bucket") args.bucket = argv[++i];
    else if (arg === "--key") args.key = argv[++i];
    else {
      console.error(`Unknown argument: ${arg}`);
      process.exit(2);
    }
  }
  return args;
}

function sha256File(path) {
  return createHash("sha256").update(readFileSync(path)).digest("hex");
}

function fail(message) {
  console.error(`\nABORT: ${message}`);
  process.exit(1);
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const manifestPath = resolve(args.manifest || resolve(DEFAULT_E1_DIR, "manifest.json"));
  const pmtilesPath = resolve(
    args.pmtiles || resolve(DEFAULT_E1_DIR, "varna_buildings_safe_min_z15_z17.pmtiles")
  );

  console.log("E2 R2 publish — verification");
  console.log("  manifest:", manifestPath);
  console.log("  pmtiles: ", pmtilesPath);

  let manifest;
  try {
    manifest = JSON.parse(readFileSync(manifestPath, "utf8"));
  } catch (err) {
    return fail(`cannot read/parse manifest: ${err.message}`);
  }

  // Gate 1: E1 publish gate must be all_pass.
  if (!manifest.gate || manifest.gate.all_pass !== true) {
    return fail("manifest.gate.all_pass is not true — E1 safety gate did not pass.");
  }

  // Gate 2: pmtiles file SHA-256 must match the manifest's recorded output hash.
  const expectedSha = manifest.output && manifest.output.pmtiles && manifest.output.pmtiles.sha256;
  if (!expectedSha) return fail("manifest has no output.pmtiles.sha256 to verify against.");

  let actualSize;
  try {
    actualSize = statSync(pmtilesPath).size;
  } catch (err) {
    return fail(`cannot stat pmtiles file: ${err.message}`);
  }
  const actualSha = sha256File(pmtilesPath);
  if (actualSha !== expectedSha) {
    return fail(
      `pmtiles SHA-256 mismatch.\n  manifest: ${expectedSha}\n  file:     ${actualSha}`
    );
  }

  // Belt-and-braces: warn (don't block) if determinism wasn't recorded as pass.
  if (!manifest.determinism || manifest.determinism.pass !== true) {
    console.warn("  WARNING: manifest.determinism.pass is not true (continuing; gate + sha are authoritative).");
  }

  const objectKey = args.key || `tiles/buildings_safe_v${actualSha}.pmtiles`;

  console.log("\nVerification PASSED:");
  console.log("  gate.all_pass:        ", manifest.gate.all_pass);
  console.log("  pmtiles sha256:       ", actualSha);
  console.log("  pmtiles bytes:        ", actualSize);
  console.log("  computed object key:  ", objectKey);

  const wantUpload = args.apply && args.remote;
  if (!wantUpload) {
    console.log("\nDRY-RUN — no upload performed (default).");
    console.log("To actually upload (Petar's hand only), re-run with:");
    console.log(`  node scripts/publish_building_tiles_r2.mjs --apply --remote --bucket <PRIVATE_BUCKET_NAME>`);
    console.log("This requires an already-created private R2 bucket and your wrangler auth.");
    return;
  }

  // ---- Real upload path: only reached with --apply --remote (Petar's hand). ----
  if (!args.bucket) return fail("--apply --remote requires --bucket <PRIVATE_BUCKET_NAME>.");

  const wranglerArgs = [
    "wrangler",
    "r2",
    "object",
    "put",
    `${args.bucket}/${objectKey}`,
    "--file",
    pmtilesPath,
    "--content-type",
    "application/octet-stream",
    "--remote",
  ];
  console.log("\n--apply --remote: uploading to the PRIVATE bucket via wrangler:");
  console.log("  npx " + wranglerArgs.join(" "));
  const result = spawnSync("npx", wranglerArgs, { stdio: "inherit", shell: process.platform === "win32" });
  if (result.status !== 0) {
    return fail(`wrangler upload exited with status ${result.status}.`);
  }
  console.log("\nUpload complete. Remember (Petar's hand, dashboard):");
  console.log("  - set BUILDING_TILES_OBJECT_KEY var to:", objectKey);
  console.log("  - confirm the R2 binding BUILDING_TILES points at this private bucket.");
}

main();
