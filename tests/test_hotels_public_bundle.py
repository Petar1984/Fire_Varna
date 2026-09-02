"""Plan §5 G1/G2 — SHA-pinned gate for the two published place payloads.

Guards `data/hotels.json` (the 226-record hotel delivery exported from varna_3d on
23.08.2026) and `data/place_categories.json` (the 264-form / 55-chip category
dictionary) that the places branch of the search lazy-loads on first focus. Sibling of
tests/test_approx_addresses_public_bundle.py, which guards the approximate-address
bundle the same way.

What "SHA-pinned" means here (plan §14, v2.5): the pinned bytes are the TRACKED blob —
`.gitattributes` (`* text=auto eol=lf`) normalizes the delivery to LF on commit, so the
blob GitHub Pages serves and a clone checks out is the LF one. The CRLF sizes a Windows
working tree used to show (83 008 B / 17800b5d…) are NOT the published bytes and must
never be pinned again; a delivery sha is measured on `git show HEAD:…`.

Beyond the bytes the gate asserts the load-time contract of plan §2 Д2 (top-level
shape, exact record keys, closed enumerations, delivery bbox), the publish contract of
plan §2 Д1 / §5 G2 (no cadastral identifier leaks, verbatim licence line, no personal
data in the free text, unique (name, zone), no alias that shadows another record or a
dictionary form) and the dictionary contract the key model of plan §3 Т2 depends on.

G2 ("the test RUNS and FAILS") needs the gate pointed at a deliberately corrupted copy.
Set the environment variable **FIRE_VARNA_HOTELS_PATH** to an alternative hotels file
and every assertion below runs against it; unset, the gate reads `data/hotels.json`.
The category dictionary is never redirected — only the hotels file is corrupted in G2.

Run: python -m unittest discover -s tests
"""
import gzip
import hashlib
import json
import os
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
# G2 override: the corrupted copy is fed in through the environment, not by editing data/.
HOTELS = pathlib.Path(os.environ.get("FIRE_VARNA_HOTELS_PATH") or (REPO / "data" / "hotels.json"))
CATEGORIES = REPO / "data" / "place_categories.json"

# The tracked LF blobs, measured at C2 (varna_3d HEAD 9f55c08, branch rezhimi):
#   git -C ../varna_3d show HEAD:data/fire_varna_hotels.json > data/hotels.json
#   git -C ../varna_3d show HEAD:data/place_categories.json  > data/place_categories.json
HOTELS_SHA256 = "7205544432f8f4c28289da20eea83ab964b1936864e4922532b4cf4df10d4806"
HOTELS_BYTES = 78601
HOTELS_GZIP9 = 8979
CATEGORIES_SHA256 = "6bf5dd323370cb6be895979ae6a0144da1f29b9231cf684fee696f7cc8d26ce5"
CATEGORIES_BYTES = 36203
CATEGORIES_GZIP9 = 4009

EXPECTED_COUNT = 226
TOP_LEVEL_KEYS = {"_meta", "hotels"}
# Plan §2 Д2: exactly these twelve keys on every record, no more and no less.
RECORD_KEYS = {"beds", "cat", "kind", "lat", "lon", "name",
               "no_uin", "old_names", "src", "status", "uins", "zone"}
ALLOWED_KIND = {"Хотел", "Семеен хотел", "хотел · без категоризация", "апарт-хотел"}
ALLOWED_SRC = {"НТР УИН", "Sol/OSM идентификация", "КАИС адресно поле"}
ALLOWED_STATUS = {"", "бивш"}
# The delivery bbox (canon of varna_3d qa_fire_varna_export.py), plan §2 Д2.
BBOX = (43.13, 43.35, 27.65, 28.10)  # min_lat, max_lat, min_lon, max_lon

# Copied byte-for-byte out of data/hotels.json with python — never retyped by hand.
LICENCE = 'Имената и регистровите данни: отделни факти от Националния туристически регистър (чл. 4 ЗАПСП; без масово копиране на регистъра). Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md). Старите имена: кадастрални адресни полета + публични източници, всяко с ред в присъдния документ на З1 (22.08.2026). Имената от публична идентификация (OSM, официални сайтове, общински регистри): отделни факти, а не извадка от база — източникът на всеки ред стои в `src` (цикълът „дупката“, 23.08.2026).'

# A КАИС cadastral identifier is the one thing that must never reach a public payload.
_CADASTRAL_RE = re.compile(r"\b\d{4,5}\.\d+\.\d+")
# UTF-8 read back as cp1252 leaves these two-byte signatures (AGENTS.md § encoding).
_MOJIBAKE_RE = re.compile("[\u00d0\u00d1\u00c2][\u0080-\u00ff]")
# Personal data in the free text: phone, e-mail, a bare 10-digit run (ЕГН shape),
# a doctor practice, a sole trader. Plan §5 G2 / §11 Б4(3).
#
# The phone pattern is WIDER than the one the C3 brief spelled out
# ((\+359|\b0)8\d[\s-]?\d{3}[\s-]?\d{3,4}): that one pins the separators to a 3+3+3
# grouping and therefore does NOT match the canonical Bulgarian mobile "0888 123 456"
# (4+3+3) — measured in G2 (b) on 02.09.2026, where the corrupted copy carrying exactly
# that number came back GREEN. Plan §5 G2 demands the gate go red on a phone in
# old_names, so the rule was fixed rather than the expectation (plan §10 doctrine):
# "0, 8, any digit, then seven more digits, each optionally separated". Strictly more
# sensitive than the brief's pattern, and still zero hits on the delivery.
_PII_PATTERNS = {
    "phone": re.compile(r"(\+359|\b0)8\d(?:[\s-]?\d){7}"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "ten_digit_run": re.compile(r"\d{10}"),
    "doctor": re.compile(r"(?i)\bд-р\b|\bdr\.?\s"),
    "sole_trader": re.compile(r"\bЕТ\s"),
}


def read(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    return raw, text, json.loads(text)


class HotelsBundleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw, cls.text, cls.doc = read(HOTELS)
        cls.records = cls.doc.get("hotels", [])

    def test_bytes_sha_gzip_match_the_tracked_blob(self):
        self.assertEqual(len(self.raw), HOTELS_BYTES)
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), HOTELS_SHA256)
        self.assertEqual(len(gzip.compress(self.raw, 9, mtime=0)), HOTELS_GZIP9)

    def test_top_level_shape_and_count(self):
        self.assertEqual(set(self.doc.keys()), TOP_LEVEL_KEYS)
        self.assertIsInstance(self.records, list)
        self.assertEqual(self.doc["_meta"]["count"], EXPECTED_COUNT)
        self.assertEqual(len(self.records), EXPECTED_COUNT)

    def test_every_record_carries_exactly_the_twelve_keys(self):
        for rec in self.records:
            self.assertEqual(set(rec.keys()), RECORD_KEYS, rec.get("name"))

    def test_enumerations_are_closed(self):
        for rec in self.records:
            self.assertIn(rec["kind"], ALLOWED_KIND, rec.get("name"))
            self.assertIn(rec["src"], ALLOWED_SRC, rec.get("name"))
            self.assertIn(rec["status"], ALLOWED_STATUS, rec.get("name"))

    def test_names_non_empty_and_coordinates_inside_the_delivery_bbox(self):
        min_lat, max_lat, min_lon, max_lon = BBOX
        for rec in self.records:
            self.assertIsInstance(rec["name"], str)
            self.assertTrue(rec["name"].strip(), rec)
            lat, lon = rec["lat"], rec["lon"]
            self.assertIsInstance(lat, (int, float))
            self.assertIsInstance(lon, (int, float))
            self.assertTrue(min_lat <= lat <= max_lat, rec)
            self.assertTrue(min_lon <= lon <= max_lon, rec)

    def test_no_cadastral_identifier_reaches_the_public_payload(self):
        self.assertEqual(sorted(set(_CADASTRAL_RE.findall(self.text))), [])
        self.assertNotIn("10135", self.text)

    def test_the_cadastral_word_appears_only_inside_the_licence_line(self):
        # The licence sentence names cadastral address fields as a source; nowhere else
        # in the payload may the word appear, because no record may carry a cadnum.
        self.assertIn(LICENCE, self.text)
        self.assertNotIn("кадаст", self.text.replace(LICENCE, ""))

    def test_licence_line_is_verbatim(self):
        self.assertEqual(self.doc["_meta"]["licence"], LICENCE)

    def test_encoding_is_utf8_without_bom_and_free_of_mojibake(self):
        self.assertFalse(self.raw.startswith(b"\xef\xbb\xbf"))
        self.assertEqual(_MOJIBAKE_RE.findall(self.text), [])

    def test_free_text_carries_no_personal_data(self):
        hits = []
        for rec in self.records:
            for value in [rec["name"], rec["zone"]] + list(rec["old_names"]):
                for label, pattern in _PII_PATTERNS.items():
                    if pattern.search(value):
                        hits.append((label, value))
        self.assertEqual(hits, [])

    def test_name_and_zone_pairs_are_unique(self):
        seen, duplicates = set(), []
        for rec in self.records:
            key = (rec["name"].lower(), rec["zone"])
            if key in seen:
                duplicates.append(key)
            seen.add(key)
        self.assertEqual(duplicates, [])

    def test_no_alias_shadows_another_record_or_a_dictionary_form(self):
        # An old_name equal to another hotel current name — or to a category form —
        # would make the alias branch of plan §3 М2 / §10 А6 answer for the wrong record.
        names = {rec["name"].lower() for rec in self.records}
        forms = {form.lower() for form in json.loads(CATEGORIES.read_text(encoding="utf-8"))["forms"]}
        collisions = []
        for rec in self.records:
            for alias in rec["old_names"]:
                low = alias.lower()
                if low in names and low != rec["name"].lower():
                    collisions.append(("name", alias, rec["name"]))
                if low in forms:
                    collisions.append(("form", alias, rec["name"]))
        self.assertEqual(collisions, [])


class CategoryDictionaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw, cls.text, cls.doc = read(CATEGORIES)

    def test_bytes_sha_gzip_match_the_tracked_blob(self):
        self.assertEqual(len(self.raw), CATEGORIES_BYTES)
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), CATEGORIES_SHA256)
        self.assertEqual(len(gzip.compress(self.raw, 9, mtime=0)), CATEGORIES_GZIP9)

    def test_schema_and_shape(self):
        self.assertEqual(self.doc["_meta"]["schema"], 1)
        self.assertIsInstance(self.doc["forms"], dict)
        self.assertIsInstance(self.doc["chips"], list)

    def test_every_form_points_at_declared_chips(self):
        chips = {entry["chip"] for entry in self.doc["chips"]}
        for form, listed in self.doc["forms"].items():
            self.assertIsInstance(listed, list, form)
            self.assertTrue(listed, form)
            for chip in listed:
                self.assertIn(chip, chips, form)

    def test_every_chip_has_forms(self):
        referenced = set()
        for listed in self.doc["forms"].values():
            referenced.update(listed)
        for entry in self.doc["chips"]:
            self.assertTrue(entry.get("forms"), entry["chip"])
            self.assertIn(entry["chip"], referenced)

    def test_encoding_is_utf8_without_bom_and_free_of_mojibake(self):
        self.assertFalse(self.raw.startswith(b"\xef\xbb\xbf"))
        self.assertEqual(_MOJIBAKE_RE.findall(self.text), [])


if __name__ == "__main__":
    unittest.main()
