#!/usr/bin/env python3
"""Copy the signed B1 basemap release into Fire_Varna runtime (Basemap B2 §6.2).

Stdlib only. Verifies the source manifest hashes BEFORE copying, copies exactly the
runtime/ODbL deliverables (never the mbtiles build artifact or review/gate scratch),
writes each file durably (temp -> flush -> fsync -> os.replace), re-reads every copied
file from disk and re-hashes it, and prunes stale osm_varna_* version dirs while
preserving range_canary.pmtiles. Writes a JSON copy report.

STOP conditions (non-zero exit, nothing partially left in place beyond verified files):
  - basemap_version mismatch
  - tiles.content_sha256 / tiles.pmtiles_sha256 / style_sha256 mismatch
  - any reread sha256 != source sha256
"""
import argparse
import hashlib
import json
import os
import shutil
import sys

# B1-locked expectations (Basemap B2 plan §2 / §6.2). These are asserted against the
# source manifest before a single byte is copied.
EXPECT_CONTENT_SHA256 = "8a15054e722b12cb31afbc6cc3ff13a4cb7401dda7a8291f139794ac286fc3b8"
EXPECT_PMTILES_SHA256 = "29a8dee66465bed3eabaa2afa70efbe703b9e63b9cde84d4dcadb2436435f1b8"
EXPECT_STYLE_SHA256 = "62cc123ee2227c4a95a249a2f788010eee57067a5ce72c594b4318834fc69135"

# Runtime + ODbL deliverables copied into data/basemaps/<version>/. Paths are relative
# to the source release dir (values) and the destination version dir (keys equal values).
COPY_FILES = [
    "varna_basemap.pmtiles",
    "varna_basemap_manifest.json",
    "style.json",
    "odbl/ATTRIBUTION.txt",
    "odbl/README_ODbL.md",
    "odbl/osm_varna_patch_v1.csv",
    "odbl/osm_varna_source_manifest.json",
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def durable_copy(src, dst):
    """Copy src -> dst via a temp file in the destination dir, flush+fsync, os.replace."""
    dst_dir = os.path.dirname(dst)
    os.makedirs(dst_dir, exist_ok=True)
    tmp = dst + ".tmp"
    with open(src, "rb") as fsrc, open(tmp, "wb") as fdst:
        shutil.copyfileobj(fsrc, fdst, length=1024 * 1024)
        fdst.flush()
        os.fsync(fdst.fileno())
    os.replace(tmp, dst)


def try_fsync_dir(path):
    """Fsync a directory where the platform allows it. On Windows os.open of a dir
    typically raises PermissionError; record that honestly rather than swallow it."""
    try:
        fd = os.open(path, os.O_RDONLY)
    except (PermissionError, OSError):
        return "not_supported_on_windows"
    try:
        os.fsync(fd)
        return "ok"
    except OSError:
        return "not_supported_on_windows"
    finally:
        os.close(fd)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="B1 release dir in Varna_buildings")
    ap.add_argument("--target-root", required=True, help="Fire data/basemaps root")
    ap.add_argument("--version", required=True, help="basemap version string")
    ap.add_argument("--report", required=True, help="path to write copy_report.json")
    args = ap.parse_args()

    report = {
        "source": os.path.abspath(args.source),
        "target_root": os.path.abspath(args.target_root),
        "version": args.version,
        "manifest_check": {},
        "files": [],
        "pruned_dirs": [],
        "preserved": [],
        "parent_dir_fsync": None,
        "ok": False,
    }

    # --- Verify source manifest BEFORE copying anything ---
    src_manifest_path = os.path.join(args.source, "varna_basemap_manifest.json")
    with open(src_manifest_path, "r", encoding="utf-8") as f:
        m = json.load(f)

    checks = {
        "basemap_version": (m.get("basemap_version"), args.version),
        "content_sha256": (m.get("content_sha256"), EXPECT_CONTENT_SHA256),
        "pmtiles_sha256": (m.get("pmtiles_sha256"), EXPECT_PMTILES_SHA256),
        "style_sha256": (m.get("style_sha256"), EXPECT_STYLE_SHA256),
    }
    for key, (got, want) in checks.items():
        ok = got == want
        report["manifest_check"][key] = {"got": got, "want": want, "ok": ok}
        if not ok:
            _fail(report, args.report,
                  "manifest %s mismatch: got %r want %r" % (key, got, want))

    dest_version_dir = os.path.join(args.target_root, args.version)

    # --- Copy exactly the runtime/ODbL deliverables ---
    all_ok = True
    for rel in COPY_FILES:
        src = os.path.join(args.source, rel)
        dst = os.path.join(dest_version_dir, rel)
        src_sha = sha256_file(src)
        src_bytes = os.path.getsize(src)
        durable_copy(src, dst)
        reread_sha = sha256_file(dst)  # re-open from disk and hash after copy
        reread_bytes = os.path.getsize(dst)
        file_ok = (reread_sha == src_sha and reread_bytes == src_bytes)
        all_ok = all_ok and file_ok
        report["files"].append({
            "rel": rel,
            "src": os.path.abspath(src),
            "dst": os.path.abspath(dst),
            "bytes": src_bytes,
            "src_sha256": src_sha,
            "reread_sha256": reread_sha,
            "ok": file_ok,
        })
        if not file_ok:
            _fail(report, args.report,
                  "reread mismatch for %s: %s != %s" % (rel, reread_sha, src_sha))

    # Fsync the destination version dir where the platform allows it.
    report["parent_dir_fsync"] = try_fsync_dir(dest_version_dir)

    # --- Prune stale osm_varna_* version dirs; preserve the canary ---
    if os.path.isdir(args.target_root):
        for name in sorted(os.listdir(args.target_root)):
            full = os.path.join(args.target_root, name)
            if name == "range_canary.pmtiles":
                report["preserved"].append(name)
                continue
            if os.path.isdir(full) and name.startswith("osm_varna_") and name != args.version:
                shutil.rmtree(full)
                report["pruned_dirs"].append(name)

    report["ok"] = all_ok
    _write_report(args.report, report)
    print("copy_basemap_release: OK" if all_ok else "copy_basemap_release: FAIL")
    print("  version:", args.version)
    print("  files copied:", len(report["files"]))
    print("  pruned dirs:", report["pruned_dirs"])
    print("  preserved:", report["preserved"])
    print("  parent_dir_fsync:", report["parent_dir_fsync"])
    print("  report:", os.path.abspath(args.report))
    sys.exit(0 if all_ok else 1)


def _write_report(path, report):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def _fail(report, report_path, msg):
    report["ok"] = False
    report["error"] = msg
    _write_report(report_path, report)
    print("copy_basemap_release: STOP —", msg, file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
