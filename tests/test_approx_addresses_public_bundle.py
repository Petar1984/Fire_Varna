"""ADR 001 — guard the published approximate-address bundle.

Asserts that data/approx_addresses_v1.json (the static, lazy-loaded B2 asset) is
byte-identical to the B1-emitted public-safe bundle and carries ONLY the seven
allowed public fields — no cadnum / КАИС / private token / target_g — with every
coordinate inside the Varna WGS84 bbox. If any of these break, the search must
fall back to today's behaviour (ADR 001 D5); this test makes a regression loud.

Run: python -m unittest discover -s tests
"""
import gzip
import hashlib
import json
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
BUNDLE = REPO / "data" / "approx_addresses_v1.json"

# The exact B1-emitted bundle (Address-fill B2 plan §Контекст).
# v1.0.2 (FF-002 hotfix — 375 street_key false-merge rows withheld; 8,802 -> 8,427).
EXPECTED_SHA256 = "39b1ad6505128ca0288538b70748c42eca8fc6a0d57587bb349b67c030b9fc39"
EXPECTED_GZIP9 = 89847
EXPECTED_RAW = 853791
EXPECTED_ROWS = 8427
ALLOWED_KEYS = {"schema_version", "kind", "coordinate_order", "field_order", "rows"}
FIELD_ORDER = ["street_name_bg", "number", "quarter", "lat", "lng", "confidence", "source"]
ALLOWED_CONF = {"high", "medium", "low"}
ALLOWED_SRC = {"interp", "nearest", "alias"}
# Varna WGS84 bbox (matches the B1 emitter's validate_wgs bounds).
BBOX = (43.00, 43.45, 27.60, 28.15)  # min_lat, max_lat, min_lng, max_lng

_CADNUM_RE = re.compile(r"\b10135\.\d+\.\d+(?:\.\d+)?\b")
_FORBIDDEN_RE = re.compile(
    r"cadnum|kais|КАИС|raw|m6000_private|grao_code|street_key|number_key|"
    r"cluster_id|ref_low|ref_high|ref_number|number_delta|source_fingerprints|"
    r"distance|target_g")


class ApproxBundleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = BUNDLE.read_bytes()
        cls.text = cls.raw.decode("utf-8")
        cls.doc = json.loads(cls.text)

    def test_bytes_sha_gzip_match_b1_emit(self):
        self.assertEqual(len(self.raw), EXPECTED_RAW)
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), EXPECTED_SHA256)
        self.assertEqual(len(gzip.compress(self.raw, 9, mtime=0)), EXPECTED_GZIP9)

    def test_schema_and_allowed_keys(self):
        self.assertEqual(set(self.doc.keys()), ALLOWED_KEYS)
        self.assertEqual(self.doc["kind"], "fire_varna_approx_addresses_v1")
        self.assertEqual(self.doc["schema_version"], "1.0.2")
        self.assertEqual(self.doc["field_order"], FIELD_ORDER)
        self.assertIsInstance(self.doc["rows"], list)

    def test_row_count_matches_approved_tranche(self):
        self.assertEqual(len(self.doc["rows"]), EXPECTED_ROWS)

    def test_no_forbidden_tokens_or_cadnum(self):
        self.assertEqual(sorted(set(_FORBIDDEN_RE.findall(self.text))), [])
        self.assertEqual(sorted(set(_CADNUM_RE.findall(self.text))), [])

    def test_no_target_g_key_anywhere(self):
        # target_g must be absent in strict v1 (D8 — v1.1 extension only).
        self.assertNotIn("target_g", self.text)

    def test_every_row_shape_values_and_coords(self):
        col = {n: FIELD_ORDER.index(n) for n in FIELD_ORDER}
        mn_lat, mx_lat, mn_lng, mx_lng = BBOX
        for r in self.doc["rows"]:
            self.assertIsInstance(r, list)
            self.assertEqual(len(r), len(FIELD_ORDER))
            lat, lng = r[col["lat"]], r[col["lng"]]
            self.assertIsInstance(lat, (int, float))
            self.assertIsInstance(lng, (int, float))
            self.assertTrue(mn_lat <= lat <= mx_lat, r)
            self.assertTrue(mn_lng <= lng <= mx_lng, r)
            self.assertIn(r[col["confidence"]], ALLOWED_CONF, r)
            self.assertIn(r[col["source"]], ALLOWED_SRC, r)
            self.assertTrue(str(r[col["street_name_bg"]]).strip(), r)
            self.assertTrue(str(r[col["number"]]).strip(), r)


if __name__ == "__main__":
    unittest.main()
