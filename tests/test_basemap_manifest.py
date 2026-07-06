"""Static gates for the Basemap B2 runtime integration (plan §7.1 + audit addendum).

Asserts the copied B1 artifacts, the Fire runtime manifest, the vendored deps, and the
index.html / sw.js wiring are internally consistent and B1-hash-locked, WITHOUT touching
any hydrant/search data. Pure stdlib; runnable via `python -m unittest discover -s tests`.
"""
import base64
import hashlib
import json
import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASEMAPS = os.path.join(REPO, "data", "basemaps")

VERSION = "osm_varna_2026-05-13_m3b_r102dde00f86b_patch_4bae3267f0de_style_36171a920333_tiles_8a15054e722b"

# B1-locked expectations.
PMTILES_BYTES = 5748578
PMTILES_SHA256 = "29a8dee66465bed3eabaa2afa70efbe703b9e63b9cde84d4dcadb2436435f1b8"
CONTENT_SHA256 = "8a15054e722b12cb31afbc6cc3ff13a4cb7401dda7a8291f139794ac286fc3b8"
STYLE_SHA256 = "62cc123ee2227c4a95a249a2f788010eee57067a5ce72c594b4318834fc69135"
PATCH_CSV_SHA256 = "4bae3267f0dea83ca753f61ef19750d059967f7dc2e1555ba4848f6b53b0b6d8"
SOURCE_MANIFEST_SHA256 = "427842588c77264ef8d891294cffbb5a0870f2f873c6a69bbe92cdf73304cf7a"

PROTECTED_CACHES = ["fire-varna-search-v2", "fire-varna-approx-addresses-v1"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sri384(path):
    with open(path, "rb") as f:
        return "sha384-" + base64.b64encode(hashlib.sha384(f.read()).digest()).decode()


class TestBasemapManifest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(BASEMAPS, "basemap_manifest.json"), encoding="utf-8") as f:
            cls.manifest = json.load(f)
        cls.vdir = os.path.join(BASEMAPS, VERSION)

    # ---- manifest identity ----
    def test_active_version(self):
        self.assertEqual(self.manifest["active_version"], VERSION)
        self.assertEqual(self.manifest["cache_version"], VERSION)

    def test_exactly_one_version_dir(self):
        dirs = [n for n in os.listdir(BASEMAPS)
                if n.startswith("osm_varna_") and os.path.isdir(os.path.join(BASEMAPS, n))]
        self.assertEqual(dirs, [VERSION], "must be exactly one osm_varna_* version dir")

    def test_canary_ignored_by_version_check(self):
        # range_canary.pmtiles may exist and must NOT be counted as a version dir.
        canary = os.path.join(BASEMAPS, "range_canary.pmtiles")
        if os.path.exists(canary):
            self.assertTrue(os.path.isfile(canary))

    # ---- copied B1 artifacts ----
    def test_pmtiles_bytes_and_hash(self):
        p = os.path.join(self.vdir, "varna_basemap.pmtiles")
        self.assertEqual(os.path.getsize(p), PMTILES_BYTES)
        self.assertEqual(sha256(p), PMTILES_SHA256)
        b = self.manifest["basemap"]
        self.assertEqual(b["pmtiles_bytes"], PMTILES_BYTES)
        self.assertEqual(b["pmtiles_sha256"], PMTILES_SHA256)
        self.assertEqual(b["content_sha256"], CONTENT_SHA256)

    def test_style_hash(self):
        p = os.path.join(self.vdir, "style.json")
        self.assertEqual(sha256(p), STYLE_SHA256)
        self.assertEqual(self.manifest["basemap"]["style_sha256"], STYLE_SHA256)

    def test_b1_manifest_fields(self):
        with open(os.path.join(self.vdir, "varna_basemap_manifest.json"), encoding="utf-8") as f:
            b1 = json.load(f)
        self.assertEqual(b1["basemap_version"], VERSION)
        self.assertEqual(b1["content_sha256"], CONTENT_SHA256)
        self.assertEqual(b1["pmtiles_sha256"], PMTILES_SHA256)
        self.assertEqual(b1["style_sha256"], STYLE_SHA256)
        self.assertEqual(b1["tiles"], 3333)

    def test_odbl_files_and_patch_hash(self):
        odbl = os.path.join(self.vdir, "odbl")
        for name in ("ATTRIBUTION.txt", "README_ODbL.md",
                     "osm_varna_patch_v1.csv", "osm_varna_source_manifest.json"):
            self.assertTrue(os.path.exists(os.path.join(odbl, name)), name)
        self.assertEqual(sha256(os.path.join(odbl, "osm_varna_patch_v1.csv")), PATCH_CSV_SHA256)
        self.assertEqual(sha256(os.path.join(odbl, "osm_varna_source_manifest.json")), SOURCE_MANIFEST_SHA256)

    # ---- vendored runtime deps ----
    def test_runtime_deps_exist_and_match_manifest(self):
        names = set()
        for dep in self.manifest["runtime_deps"]:
            p = os.path.join(REPO, dep["path"])
            self.assertTrue(os.path.exists(p), dep["path"])
            self.assertEqual(os.path.getsize(p), dep["bytes"])
            self.assertEqual(sha256(p), dep["sha256"])
            self.assertEqual(sri384(p), dep["sri_sha384"])
            names.add(dep["name"])
        self.assertEqual(names, {"pmtiles", "protomaps-leaflet"})

    def test_cache_names_include_version(self):
        for key in ("core", "offline_pack", "basemap"):
            self.assertIn(VERSION, self.manifest["cache_names"][key])


class TestIndexAndServiceWorkerStatic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(REPO, "index.html"), encoding="utf-8") as f:
            cls.index = f.read()
        with open(os.path.join(REPO, "sw.js"), encoding="utf-8") as f:
            cls.sw = f.read()

    def test_flag_committed_false(self):
        self.assertRegex(self.index, r"const\s+BASEMAP_PMTILES_ENABLED\s*=\s*false\s*;")

    def test_no_basemap_dep_cdn_in_index(self):
        # The pmtiles / protomaps-leaflet deps must never be loaded from a CDN in index.html.
        for cdn in ("unpkg.com/pmtiles", "unpkg.com/protomaps",
                    "jsdelivr.net/npm/pmtiles", "jsdelivr.net/npm/protomaps",
                    "cdnjs.cloudflare.com/ajax/libs/pmtiles",
                    "cdnjs.cloudflare.com/ajax/libs/protomaps"):
            self.assertNotIn(cdn, self.index, cdn)
        self.assertIn("data/basemaps/basemap_manifest.json", self.index)

    def test_offline_install_gated_on_capability(self):
        # addendum П2: ?offline=install only takes effect when the capability is active.
        m = re.search(r"function basemapWantsOfflineInstall\(\)\s*\{.*?\}", self.index, re.S)
        self.assertIsNotNone(m)
        self.assertIn("isBasemapPmtilesActive()", m.group(0))

    # ---- sw.js ----
    def test_sw_cache_names_include_version(self):
        # Cache names are composed at runtime as `'<prefix>' + BASEMAP_VERSION`, so assert
        # the version constant and each owned prefix are present (not a joined literal).
        self.assertIn(VERSION, self.sw)
        self.assertRegex(self.sw, r"BASEMAP_VERSION\s*=\s*\n?\s*'" + re.escape(VERSION) + r"'")
        for prefix in ("fire-varna-core-", "fire-varna-offline-pack-", "fire-varna-basemap-"):
            self.assertIn("'" + prefix + "'", self.sw, prefix)

    def test_sw_never_deletes_protected_caches(self):
        # The two app search namespaces must be an explicit PROTECTED skip list, and the
        # deletion path must guard on it — never a member of the owned B2 prefixes.
        for name in PROTECTED_CACHES:
            self.assertIn(name, self.sw, name)
        m = re.search(r"PROTECTED_CACHES\s*=\s*\[([^\]]*)\]", self.sw)
        self.assertIsNotNone(m, "PROTECTED_CACHES list missing")
        for name in PROTECTED_CACHES:
            self.assertIn(name, m.group(1), name + " not in PROTECTED_CACHES")
        # activate() must skip PROTECTED before any delete.
        self.assertRegex(self.sw, r"PROTECTED_CACHES\.includes\(name\)\s*\)\s*return")

    def test_sw_strategy_per_path_class(self):
        # addendum Поправка 1: mutating data is network-first; versioned/vendor is cache-first.
        for f in ("data/hydrants.json", "data/search_index.json",
                  "data/address_rows.json", "data/basemaps/basemap_manifest.json"):
            self.assertIn(f, self.sw, f)
        self.assertIn("networkFirst(req, CACHE_OFFLINE_PACK)", self.sw)
        self.assertIn("cacheFirst(req, CACHE_BASEMAP)", self.sw)
        # PMTiles Range slicing must emit a 206.
        self.assertIn("status: 206", self.sw)


if __name__ == "__main__":
    unittest.main()
