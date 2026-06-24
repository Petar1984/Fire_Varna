#!/usr/bin/env node
// publish_building_details_r2.mjs — bulk-upload the C per-building detail JSONs to
// the SAME private R2 bucket the Worker's /tiles/* gateway reads from, under
// details/buildings/v1/{bd}.json. Mirrors publish_building_tiles_r2.mjs.
//
// SAFETY MODEL (read before running):
//   * DRY-RUN IS THE DEFAULT. With no flags it only verifies the detail gate +
//     digests and prints what WOULD upload. It NEVER touches the network.
//   * A real upload happens ONLY when BOTH --apply AND --remote are passed AND a
//     --bucket is given. That path shells out to `wrangler r2 object put` using
//     Petar's own wrangler auth. This script never creates a bucket, never sets a
//     secret/binding, never deploys the Worker, and never publishes a public URL.
//   * It refuses to upload unless: the detail publish gate fully passed
//     (_gate.json), the salt fingerprints of _manifest.json and _bd_index.json
//     agree (so tile bd values match these detail keys), the file count matches
//     the manifest, every filename is a valid bd, AND a fresh digest over the
//     on-disk files equals _manifest.json content_digest (i.e. nothing changed
//     since the gate ran).
//   * Uploads are idempotent — a re-run simply re-PUTs, so an interrupted upload
//     resumes safely.
//
// NOTE: details go to the SAME private bucket as the PMTiles (the Worker reads
// both through the one BUILDING_TILES R2 binding). Use the same --bucket value as
// publish_building_tiles_r2.mjs. No dashboard var change is needed for details —
// the Worker reads details/buildings/v1/{bd}.json directly.
//
// Usage (from worker/):
//   node scripts/publish_building_details_r2.mjs                                   # dry-run (default)
//   node scripts/publish_building_details_r2.mjs --apply --remote --bucket <name>  # Petar's hand only
//   (optional) --concurrency <N>     parallel wrangler uploads (default 8)
//              --details-dir <path>  override the source dir

import { readFileSync, readdirSync } from "node:fs";
import { createHash } from "node:crypto";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve, join } from "node:path";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
// scripts/ -> worker/ -> Fire_Varna/ -> c:\git\ -> Varna_buildings/output/...
const REPO_ROOT = resolve(SCRIPT_DIR, "..", "..", "..");
const DEFAULT_DETAILS_DIR = resolve(
  REPO_ROOT, "Varna_buildings", "output", "building_tiles", "details"
);
const R2_SUBDIR = "details/buildings/v1"; // matches the Worker's DETAIL_R2_PREFIX
const BD_FILE_RE = /^b[0-9a-f]{16}\.json$/;

function parseArgs(argv) {
  const args = { apply: false, remote: false, concurrency: 8 };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--apply") args.apply = true;
    else if (a === "--remote") args.remote = true;
    else if (a === "--bucket") args.bucket = argv[++i];
    else if (a === "--details-dir") args.detailsDir = argv[++i];
    else if (a === "--concurrency") args.concurrency = Math.max(1, parseInt(argv[++i], 10) || 8);
    else { console.error(`Unknown argument: ${a}`); process.exit(2); }
  }
  return args;
}

function fail(message) { console.error(`\nABORT: ${message}`); process.exit(1); }

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const dir = resolve(args.detailsDir || DEFAULT_DETAILS_DIR);
  const r2Dir = join(dir, "buildings", "v1");
  const manifestPath = join(dir, "_manifest.json");
  const gatePath = join(dir, "_gate.json");
  const bdIndexPath = join(dir, "_bd_index.json");

  console.log("C detail R2 publish — verification");
  console.log("  details dir:   ", dir);
  console.log("  r2 key prefix: ", R2_SUBDIR + "/{bd}.json");

  let manifest, gate, bdIndex;
  try { manifest = JSON.parse(readFileSync(manifestPath, "utf8")); }
  catch (e) { return fail(`cannot read _manifest.json: ${e.message}`); }
  try { gate = JSON.parse(readFileSync(gatePath, "utf8")); }
  catch (e) { return fail(`cannot read _gate.json (run publish_gate_details.mjs first): ${e.message}`); }
  try { bdIndex = JSON.parse(readFileSync(bdIndexPath, "utf8")); }
  catch (e) { return fail(`cannot read _bd_index.json: ${e.message}`); }

  // Gate 1: every detail gate must have passed.
  const gatesOk = !!(gate.structural && gate.structural.pass && gate.referential && gate.referential.pass &&
    gate.determinism && gate.determinism.pass && gate.seeded_negative && gate.seeded_negative.pass);
  if (!gatesOk) {
    return fail(`detail gate did not fully pass (structural=${gate.structural && gate.structural.pass} ` +
      `referential=${gate.referential && gate.referential.pass} determinism=${gate.determinism && gate.determinism.pass} ` +
      `seeded_negative=${gate.seeded_negative && gate.seeded_negative.pass}). Re-run publish_gate_details.mjs.`);
  }

  // Gate 2: salt fingerprint consistency (manifest <-> bd-index; same salt as tiles).
  if (!manifest.salt_fingerprint || manifest.salt_fingerprint !== bdIndex.salt_fingerprint) {
    return fail(`salt_fingerprint mismatch: manifest=${manifest.salt_fingerprint} bd_index=${bdIndex.salt_fingerprint}.`);
  }

  // Enumerate + validate filenames.
  let files;
  try { files = readdirSync(r2Dir).filter((f) => f.endsWith(".json")).sort(); }
  catch (e) { return fail(`cannot read ${r2Dir}: ${e.message}`); }
  const bad = files.filter((f) => !BD_FILE_RE.test(f));
  if (bad.length) return fail(`${bad.length} file(s) have a non-bd name, e.g. ${bad.slice(0, 3).join(", ")}.`);
  const expectCount = (manifest.stats && manifest.stats.clusters) || bdIndex.count;
  if (files.length !== expectCount) return fail(`file count ${files.length} != expected ${expectCount} (manifest/_bd_index).`);

  // Gate 3: fresh digest over the on-disk files == manifest.content_digest.
  const lines = [];
  let bytes = 0;
  for (const f of files) {
    const raw = readFileSync(join(r2Dir, f));
    bytes += raw.length;
    lines.push(`${f.replace(/\.json$/, "")} ${createHash("sha256").update(raw).digest("hex")}`);
  }
  lines.sort();
  const filesDigest = createHash("sha256").update(lines.join("\n")).digest("hex");
  if (filesDigest !== manifest.content_digest) {
    return fail(`files digest ${filesDigest} != manifest.content_digest ${manifest.content_digest} ` +
      `(output changed since the gate ran — re-run build + gate).`);
  }

  console.log("\nVerification PASSED:");
  console.log("  gates all pass:    ", gatesOk);
  console.log("  salt_fingerprint:  ", manifest.salt_fingerprint, "(manifest == bd_index)");
  console.log("  detail files:      ", files.length);
  console.log("  total bytes:       ", bytes.toLocaleString());
  console.log("  content_digest:    ", manifest.content_digest);
  console.log("  sample keys:       ", files.slice(0, 3).map((f) => `${R2_SUBDIR}/${f}`).join("  "));

  const wantUpload = args.apply && args.remote;
  if (!wantUpload) {
    console.log("\nDRY-RUN — no upload performed (default).");
    console.log("To actually upload (Petar's hand only), re-run with:");
    console.log(`  node scripts/publish_building_details_r2.mjs --apply --remote --bucket <PRIVATE_BUCKET_NAME> [--concurrency 8]`);
    console.log(`This uploads ${files.length} objects to ${R2_SUBDIR}/{bd}.json via your wrangler auth (same bucket as the PMTiles).`);
    return;
  }

  // ---- Real upload: bounded-concurrency `wrangler r2 object put` (Petar's hand). ----
  if (!args.bucket) return fail("--apply --remote requires --bucket <PRIVATE_BUCKET_NAME>.");
  console.log(`\n--apply --remote: uploading ${files.length} objects to ${args.bucket}/${R2_SUBDIR}/ ` +
    `(concurrency ${args.concurrency}) via wrangler...`);

  const putOne = (f) => new Promise((res) => {
    const key = `${args.bucket}/${R2_SUBDIR}/${f}`;
    const wa = ["wrangler", "r2", "object", "put", key, "--file", join(r2Dir, f),
      "--content-type", "application/json", "--remote"];
    const cp = spawn("npx", wa, { stdio: ["ignore", "ignore", "pipe"], shell: process.platform === "win32" });
    let err = "";
    cp.stderr.on("data", (d) => { err += d; });
    cp.on("close", (code) => res({ f, ok: code === 0, err: err.trim() }));
    cp.on("error", (e) => res({ f, ok: false, err: e.message }));
  });

  let done = 0;
  const failed = [];
  const queue = files.slice();
  async function worker() {
    while (queue.length) {
      const f = queue.shift();
      const r = await putOne(f);
      done++;
      if (!r.ok) failed.push(r);
      if (done % 200 === 0 || done === files.length) {
        console.log(`  ${done}/${files.length} uploaded (${failed.length} failed)`);
      }
    }
  }
  await Promise.all(Array.from({ length: args.concurrency }, () => worker()));

  if (failed.length) {
    console.error(`\n${failed.length} upload(s) FAILED (re-run to resume — PUTs are idempotent). First few:`);
    for (const x of failed.slice(0, 5)) console.error(`  ${x.f}: ${(x.err || "").split("\n")[0]}`);
    process.exit(1);
  }
  console.log(`\nUpload complete: ${files.length} objects under ${R2_SUBDIR}/.`);
  console.log("Reminder (Petar's hand, dashboard): NO new var needed for details — the Worker");
  console.log("reads details/buildings/v1/{bd}.json directly. Just confirm the BUILDING_TILES R2");
  console.log("binding points at this same private bucket.");
}

main();
