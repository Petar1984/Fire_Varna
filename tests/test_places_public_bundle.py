"""Phase-2 plan §2 Д1/Д2 + §5 G1/G2 — SHA-pinned gate for the places payload.

Guards `data/places.json`: the 135-record delivery of schools, universities, hospitals,
ДКЦ, hospices and kindergartens exported from varna_3d (`src/export_fire_varna_places.py`,
HEAD ba78a25 on branch rezhimi, 02.09.2026), which the places branch of the search
lazy-loads next to `data/hotels.json`. Sibling of tests/test_hotels_public_bundle.py: every
rule below has its twin there unless a comment says why it cannot.

What "SHA-pinned" means here (search plan §14, v2.5): the pinned bytes are the TRACKED
blob — `.gitattributes` (`* text=auto eol=lf`) normalizes the delivery to LF on commit, so
the blob GitHub Pages serves and a clone checks out is the LF one. A delivery sha is
measured on `git show HEAD:…`, never on a Windows working tree.

Beyond the bytes the gate asserts the publish contract of phase-2 plan §2 Д1: exactly the
eight record keys, closed enumerations for kind/src/status, the delivery bbox, no cadastral
identifier, both licence lines verbatim (§6 К8 ships two of them inside `_meta`: ODbL 1.0
for the OSM rows, "separate facts" for the registry rows), no personal data in the free
text, and unique (skeleton(name), zone).

Plan §5 G9 (phase-2 plan §4 C13) adds one more: both README mirrors (Български /
English) must quote BOTH licence lines byte for byte.

The doctor rule (§2 Д1 + §6 К7) is the one place this gate cannot copy its sibling. The
hotel gate treats any "д-р" as a personal datum; here ten of the 135 names carry a doctor's
name that IS the institution's name (ОУ „Д-р Никола Димитров“, Медицински университет
„Проф. д-р Параскев Стоянов“, СБАГАЛ „Проф. д-р Д. Стаматов“…). So a hit counts only when
no institutional word stands in the same string — the К7 list, matched as a word PREFIX.
A private practice ("д-р Иванов", no institution) still goes red.

G2 ("the test RUNS and FAILS") needs the gate pointed at a deliberately corrupted copy. Set
the environment variable **FIRE_VARNA_PLACES_PATH** to an alternative places file and every
assertion below runs against it; unset, the gate reads `data/places.json`.

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
PLACES = pathlib.Path(os.environ.get("FIRE_VARNA_PLACES_PATH") or (REPO / "data" / "places.json"))

# The tracked LF blob, measured at C11 (varna_3d HEAD ba78a25, branch rezhimi):
#   git -C ../varna_3d show HEAD:data/fire_varna_places.json > data/places.json
PLACES_SHA256 = "ef98624f2933d5191f927aaab303b248317ea92707be5c60fca5ccff0afa296a"
PLACES_BYTES = 76110
PLACES_GZIP9 = 9642

EXPECTED_COUNT = 150
TOP_LEVEL_KEYS = {"_meta", "places"}
# Phase-2 plan §2 Д1 + ЛОТ 1в (ADR 008 D1/S2): exactly these NINE keys on every
# record — no `i`, no notes, no cadastral identifier. `old_names_src` is the ninth.
RECORD_KEYS = {"kind", "lat", "lon", "name", "old_names", "old_names_src",
               "src", "status", "zone"}
# ЛОТ 1в (ADR 008 D1, амандамент А3) — the CLOSED list of alias sources. A place
# name that travels as an alias carries its own letter; `old_names_src` is a
# parallel array of the same length and order. Until this lot the card printed the
# RECORD's register for an alias that came from OSM — up to 47 rows of a lie.
ALIAS_SRC = {"OSM", "REG", "NTR", "WD", "WEB", "KAIS", "CUR"}
ALLOWED_KIND = {"училище", "университет", "болница", "ДКЦ", "хоспис", "детска градина",
                "детска ясла", "общежитие"}
ALLOWED_SRC = {"OSM",
               "Регистър на училищата (МОН/НЕИСПУО), одобрено 21.08",
               "Регистър на лечебните заведения (ИАМН)",
               "Регистър на училищата и детските заведения (Община Варна)"}
ALLOWED_STATUS = {"", "бивш"}
# The delivery bbox (canon of varna_3d qa_fire_varna_export.py), same box as the hotels.
BBOX = (43.13, 43.35, 27.65, 28.10)  # min_lat, max_lat, min_lon, max_lon

# Copied byte-for-byte out of data/places.json with python — never retyped by hand.
LICENCE_OSM = 'Имената от OpenStreetMap: „имена на обекти © OpenStreetMap contributors, ODbL“ — дословната атрибуция на web/varna_poi_names.json; лиценз ODbL 1.0. Самият пакет е производна база (систематична извадка) и се публикува под ODbL 1.0 — share-alike. Показването на един ред в попъп е Produced Work и за него атрибуцията стига (К8).'
LICENCE_WIKIDATA = 'Разгърнати имена (псевдоними за търсене) на 3 места: Wikidata Q7035695, Q12291800, Q12299161, CC0 1.0 Universal, достъп 03.09.2026. Низовете са зафиксирани с датата на достъп (снапшотът), не се теглят живо; изворът на всеки псевдоним стои в `old_names_src`.'
LICENCE_REGISTRY = 'Имената и регистровите данни: отделни факти от регистрите (чл. 4 ЗАПСП; без масово копиране на регистър) — Регистър на лечебните заведения (ИАМН), Регистър на училищата и детските заведения (Община Варна), Регистър на училищата (МОН/НЕИСПУО, одобрено 21.08); източникът на всеки ред стои в `src`. Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md).'

# A КАИС cadastral identifier is the one thing that must never reach a public payload.
_CADASTRAL_RE = re.compile(r"\b\d{4,5}\.\d+\.\d+")
# UTF-8 read back as cp1252 leaves these two-byte signatures (AGENTS.md § encoding).
_MOJIBAKE_RE = re.compile("[\u00d0\u00d1\u00c2][\u0080-\u00ff]")
# Personal data in the free text. The five patterns below are the hotel gate's, verbatim
# (its widened phone rule, which the 02.09 G2 run proved necessary, and the К2 landline
# below); the doctor rule is separate, see _DOCTOR_RE.
# К2 (plan §12, closing C14 finding 6): a VARNA LANDLINE is nine digits and the
# mobile rule above cannot see it ("052 123 456" / "052/123-456" / "052123456").
# Measured 03.09 over the free text of all three delivered files (hotels 467
# values, places 314, place_categories 1732 strings) and over their raw bytes:
# zero hits. The longest digit run anywhere in the three is FOUR („ЧОУ "Феникс
# 2020"“), five short of the nine this pattern needs — a school number („ЦДГ 43
# "Пинокио"“) or a block number can never trip it.
_PII_PATTERNS = {
    "phone": re.compile(r"(\+359|\b0)8\d(?:[\s-]?\d){7}"),
    "landline": re.compile(r"0\d{2}[\s/-]?\d{3}[\s-]?\d{3}"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "ten_digit_run": re.compile(r"\d{10}"),
    "sole_trader": re.compile(r"\bЕТ\s"),
}
# The exporter gate's pattern (varna_3d src/qa_fire_varna_places_export.py, DOCTOR) plus
# the Latin `dr` alternative the hotel gate carries. Measured on the delivery: the wider
# pattern finds the same ten names, all institutional, so it costs nothing and catches
# "Dr Ivanov" too.
#
# К2 (plan §12): „д-р“/„доктор“/„dr“ is matched as a WHOLE WORD standing in front of a
# name — no letter before it (the leading class), a word boundary after it, then a
# space and a following word. The same pattern now stands in the hotels gate, which
# until К2 only knew the hyphenated „д-р“ and missed „доктор Иванов“ altogether.
# Measured 03.09: ten hits on the delivery, the same ten as before, all institutional.
# NOT closed here, and named so it is not mistaken for closed: institutional() below
# matches its words as a PREFIX, so a private practice whose family name happens to
# start with an abbreviation of the list („д-р Мутафов“ — „МУ“) is still let through.
# Turning that prefix into a whole word is NOT free: measured, it turns one of the ten
# legitimate names red („ПГТ „Проф. д-р Асен Златаров"“ — „ПГТ“ is caught only by the
# „ПГ*“ prefix of §6 К7), so the repair needs its own measure and Petar's word.
_DOCTOR_RE = re.compile(r"(?:^|[^а-яА-Яa-zA-Z])(?:д-?р|доктор|dr)\b\.?\s+\S", re.I)
# §6 К7 ∪ plan §2 Д1 — the institutional words, matched as a PREFIX of a word. Copied from
# the exporter gate; not one word more, because every added word loosens the check.
INSTITUTIONAL = (
    "ОУ", "СУ", "СОУ", "НУ", "ПГ", "ДГ", "МГ", "МУ", "ЕГ", "ПМГ", "ВТГ",
    "ПГИ", "ЧОУ", "ЧСУ", "ЧДГ", "ЦДГ", "ОДЗ", "ДЯ", "СУУНЗ",
    "МБАЛ", "УМБАЛ", "СБАЛ", "СБАГАЛ", "УСБ", "АМЦСМП", "МЦ", "ДКЦ",
    "хоспис", "диспансер", "клиника", "академия", "институт", "гимназия",
    "училище", "университет", "болница", "градина", "ясла",
)
# §6 К1 — the one pair that shares a skeleton and a zone and is NOT a duplicate: the school
# and its branch. Named here exactly as the exporter gate names it, so an unnamed twin
# (a real duplicate) still goes red.
NAMED_TWINS = (
    ('ОУ "Константин Арабаджиев"', 'ОУ „Константин Арабаджиев“'),
)

# Transliteration skeleton, copied from the exporter gate: the same name written with
# ASCII or Bulgarian quotes, й/и, or a doubled letter collapses to one key.
_SKEL_MAP = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
             "ж": "zh", "з": "z", "и": "i", "й": "i", "к": "k", "л": "l",
             "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s",
             "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts", "ч": "ch",
             "ш": "sh", "щ": "sht", "ъ": "a", "ь": "", "ю": "yu", "я": "ya"}


def skel(name):
    words = []
    for raw in "".join(c if c.isalnum() else " " for c in name.lower()).split():
        word = "".join(_SKEL_MAP.get(c, c) for c in raw)
        word = re.sub(r"[yj]", "i", word)
        word = re.sub(r"(\D)\1+", r"\1", word)
        words.append(word)
    return " ".join(words)


def institutional(name):
    words = "".join(c if c.isalnum() else " " for c in name).split()
    return any(word.casefold().startswith(token.casefold())
               for word in words for token in INSTITUTIONAL)


def read(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    return raw, text, json.loads(text)


class PlacesBundleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw, cls.text, cls.doc = read(PLACES)
        cls.records = cls.doc.get("places", [])

    def test_bytes_sha_gzip_match_the_tracked_blob(self):
        self.assertEqual(len(self.raw), PLACES_BYTES)
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), PLACES_SHA256)
        self.assertEqual(len(gzip.compress(self.raw, 9, mtime=0)), PLACES_GZIP9)

    def test_top_level_shape_and_count(self):
        self.assertEqual(set(self.doc.keys()), TOP_LEVEL_KEYS)
        self.assertIsInstance(self.records, list)
        self.assertEqual(self.doc["_meta"]["count"], EXPECTED_COUNT)
        self.assertEqual(len(self.records), EXPECTED_COUNT)

    def test_every_record_carries_exactly_the_nine_keys(self):
        for rec in self.records:
            self.assertEqual(set(rec.keys()), RECORD_KEYS, rec.get("name"))

    def test_every_alias_carries_its_own_source(self):
        # ADR 008 D1: same length, same order, every letter from the closed list.
        # An alias without a source is a STOP in the exporter, a refusal in the
        # client validator and a red row here — never a blank line on the card.
        for rec in self.records:
            self.assertIsInstance(rec["old_names_src"], list, rec["name"])
            self.assertEqual(len(rec["old_names_src"]), len(rec["old_names"]),
                             rec["name"])
            for code in rec["old_names_src"]:
                self.assertIn(code, ALIAS_SRC, rec["name"])

    def test_the_wikidata_licence_line_is_verbatim(self):
        # Амандамент А4 т. 3 (К1/К4): Wikidata is a NEW source of names, so it gets a
        # line of its own — with the three ids, CC0 and the date of the snapshot the
        # strings were frozen at. The count in the sentence is measured, not claimed.
        self.assertEqual(self.doc["_meta"]["licence_wikidata"], LICENCE_WIKIDATA)
        self.assertIn("CC0 1.0 Universal", LICENCE_WIKIDATA)
        self.assertIn("достъп 03.09.2026", LICENCE_WIKIDATA)
        for qid in ("Q7035695", "Q12291800", "Q12299161"):
            self.assertIn(qid, LICENCE_WIKIDATA)
        wd = [rec["name"] for rec in self.records if "WD" in rec["old_names_src"]]
        self.assertEqual(len(wd), 3, wd)

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

    def test_the_cadastral_word_appears_nowhere(self):
        # Unlike the hotels licence, neither licence line here names cadastral address
        # fields, so the word has no legitimate place in this payload at all.
        self.assertNotIn("кадаст", self.text.lower())

    def test_both_licence_lines_are_verbatim(self):
        # §6 К8: one file, two licence notes — the OSM rows travel under ODbL 1.0
        # (share-alike, the bundle itself being a derivative database), the registry rows
        # as separate facts with the register named in every row's `src`.
        self.assertEqual(self.doc["_meta"]["licence_osm"], LICENCE_OSM)
        self.assertEqual(self.doc["_meta"]["licence_registry"], LICENCE_REGISTRY)
        self.assertIn("ODbL 1.0", LICENCE_OSM)

    def test_readme_carries_licence_lines(self):
        # §5 G9, phase-2 plan §4 C13. The licence travels with the data: whoever reads the
        # repo's front page must see the same two sentences the payload carries, in both
        # mirrors (Български / English), unedited — a paraphrase would be a different
        # licence. Each README quote therefore sits on ONE line; wrapping it would break
        # the byte equality this asserts.
        readme = (REPO / "README.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(readme.count(self.doc["_meta"]["licence_osm"]), 2,
                                "OSM licence line quoted in BG and EN")
        self.assertGreaterEqual(readme.count(self.doc["_meta"]["licence_registry"]), 2,
                                "registry licence line quoted in BG and EN")
        self.assertGreaterEqual(readme.count(self.doc["_meta"]["licence_wikidata"]), 2,
                                "Wikidata licence line quoted in BG and EN")

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

    def test_a_doctor_name_always_sits_inside_an_institution(self):
        # §6 К7. The class rules (К3) are what keep private practices out; this is the
        # second line behind them.
        hits = [value for rec in self.records
                for value in [rec["name"], rec["zone"]] + list(rec["old_names"])
                if _DOCTOR_RE.search(value) and not institutional(value)]
        self.assertEqual(hits, [])

    def test_name_skeleton_and_zone_pairs_are_unique(self):
        twins = {frozenset(pair) for pair in NAMED_TWINS}
        groups = {}
        for rec in self.records:
            groups.setdefault((skel(rec["name"]), rec["zone"]), []).append(rec["name"])
        duplicates = [(key, names) for key, names in groups.items()
                      if len(names) > 1 and frozenset(names) not in twins]
        self.assertEqual(duplicates, [])


if __name__ == "__main__":
    unittest.main()
