"""Plan §5 G1/G2 — SHA-pinned gate for the two published place payloads.

Guards `data/hotels.json` (the 226-record hotel delivery exported from varna_3d on
23.08.2026, re-exported on 02.09.2026 with quarter/district zones — phase-2 plan §8)
and `data/place_categories.json` (the 264-form / 55-chip category
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

Plan §5 G9 adds one more: both README mirrors (Български / English) must quote that same
licence line byte for byte, and must carry the honest note that the bundle is online-only.

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

# The tracked LF blobs. The dictionary was measured at C2 (varna_3d HEAD 9f55c08, branch
# rezhimi); the hotels were RE-measured at C11 (HEAD ba78a25, same branch), because
# phase-2 plan §8 had the delivery regenerated so every hotel carries the quarter/district
# of the signed `zone_label` ladder instead of one of the six old boxes. Only `zone` moved:
# comparing the 226 records without that key against the previous blob gives 0 differences
# (45 zones re-labelled, 10 distinct values → 24).
#   git -C ../varna_3d show HEAD:data/fire_varna_hotels.json > data/hotels.json
#   git -C ../varna_3d show HEAD:data/place_categories.json  > data/place_categories.json
# ЛОТ 1 (F1-д, varna_3d dee1f76 „P2-д“, branch rezhimi): the delivery is 225 now —
# decision 10 merged „Явор“ into „ГОЛДЪН ЛАЙН“ (one building, two records at 0,00 m;
# the old name lives on as an alias) and the reason line moved into `_meta.excluded`.
# The three numbers below are re-measured on that blob; nothing else in it moved.
HOTELS_SHA256 = "c30f7333d1a9a845b90ca46db0e41496cb722aa2640b6c862ccb8b211bd30100"
HOTELS_BYTES = 142543
HOTELS_GZIP9 = 13004
# C16 (§11 П7): the dictionary was re-delivered with a `zones` key — the quarter
# aliases of the zones that carry a registry entry, schema still 1.
# ЛОТ 1 (F1-д, varna_3d dee1f76 „P2-д“) then moved the dictionary itself: chips
# 55 → 57, forms 264 → 276, zones 28 → 30, so the „`chips` and `forms` are
# byte-identical to the previous blob“ of C16 stopped being true. Re-measured
# with the sha256 of this file, over the UTF-8 bytes of
# json.dumps({"chips": …, "forms": …}, ensure_ascii=False, sort_keys=True):
# 30 570 B / 87f35e90ac206ab3… at 23af63f → 32 188 B / 27fe1ca178c7cf17… now.
#   git -C ../varna_3d show HEAD:data/place_categories.json > data/place_categories.json
# ЛОТ 1в-В (ADR 008 D9): the dictionary answers with THREE (class, code) dictionaries
# — `locations.quarter|district|locality` — and with `legacy_by_row`: the old zone
# word of every row whose label changed, keyed by that row's ordinal in its bundle
# and protected by the SHA of the bundle. chips 57, forms 276 → 283, zones 30 → 19.
CATEGORIES_SHA256 = "2d3d6af6909222b0e3fbb1af088e021edbc9c9c2dd6af140ab7a973b75c81289"
CATEGORIES_BYTES = 64424
CATEGORIES_GZIP9 = 8663
# The closed lists the dictionary and the two payloads have to AGREE on: a code in a
# record that the dictionary of the same delivery does not name is a broken delivery.
LOCATION_COUNTS = {"quarter": 19, "district": 5, "locality": 4}
LEGACY_ROWS = 209
BUNDLE_SIZES = {"places": 150, "hotels": 225}

EXPECTED_COUNT = 225
TOP_LEVEL_KEYS = {"_meta", "hotels"}
# Plan §2 Д2 + ЛОТ 1в (ADR 008 D1/S2): exactly these FOURTEEN keys on every record,
# no more and no less. `old_names_src` is the thirteenth — a parallel array of the
# same length and order, so every old name names its own source instead of
# inheriting the record's register; `address` (ЛОТ 1в-Б, ADR 008 D5) is the fourteenth.
RECORD_KEYS = {"address", "beds", "cat", "district", "kind", "lat", "locality",
               "lon", "name", "no_uin", "old_names", "old_names_src", "quarter",
               "src", "status", "uins", "zone"}
# ЛОТ 1в-В (ADR 008 D9, план §3г/§3ж S1/S4/S6) — the three TYPED location fields.
# Each is `null` or EXACTLY {name, src, code}; the district is the one field that is
# never null, because „район X“ is the honest answer when nothing else can be
# sourced. The code lists are CLOSED: a public row may carry no location that the
# dictionary of the same delivery does not name.
LOCATION_KEYS = {"name", "src", "code"}
QUARTER_SRC = {"REG", "KAIS", "SIGNED_OVERRIDE"}
DISTRICT_SRC = {"KAIS", "SIGNED_OVERRIDE"}
DISTRICT_CODES = {"primorski", "odesos", "mladost", "asparuhovo", "vladislav_varnenchik"}
QUARTER_CODES = {"asparuhovo", "borovets_yug", "chaika_kk", "chaika_kv", "druzhba",
                 "galata", "izgrev_kv", "kk_konstantin_elena", "manastirski_rid",
                 "mladost2", "pobeda", "priboy", "troshevo", "vazrazhdane",
                 "vazrazhdane1", "vazrazhdane2", "vinitsa", "vladislavovo",
                 "zlatni_pyasatsi"}
LOCALITY_CODES = {"sveti_nikola", "vilite", "zelenika", "zpz"}
QUARTER_BY_SRC = {"KAIS": 84, "SIGNED_OVERRIDE": 12}
LOCALITY_COUNT = 4
# ЛОТ 1в-Б (ADR 008 D5) — `address` is `null` or EXACTLY these four keys, and its
# source is its OWN closed list: a hotel named by the НТР can carry a КАИС address
# (К7 (4): a hotel with no НТР address falls back on the body under the pin), so
# the card names the source of THAT string and not the register of the record.
ADDRESS_KEYS = {"text", "src", "street_phrase", "house_key"}
ADDRESS_SRC = {"KAIS", "REG", "NTR", "OSM"}
# The measured coverage of the signed list, re-measured on the P5 delivery: 75 of
# the 225 hotels carry an address that meets the strict criterion. The 150 without
# one are mostly the resort hotels, where КАИС holds a landmark ("х-л …"), not a
# street and a number — and a landmark is not an address (план §2в).
ADDRESS_COUNT = 75
ADDRESS_BY_SRC = {"KAIS": 55, "NTR": 20}
# ЛОТ 1в (ADR 008 D1, амандамент А3) — the CLOSED list of alias sources.
ALIAS_SRC = {"OSM", "REG", "NTR", "WD", "WEB", "KAIS", "CUR"}
ALLOWED_KIND = {"Хотел", "Семеен хотел", "хотел · без категоризация", "апарт-хотел"}
ALLOWED_SRC = {"НТР УИН", "Sol/OSM идентификация", "КАИС адресно поле"}
ALLOWED_STATUS = {"", "бивш"}
# The delivery bbox (canon of varna_3d qa_fire_varna_export.py), plan §2 Д2.
BBOX = (43.13, 43.35, 27.65, 28.10)  # min_lat, max_lat, min_lon, max_lon

# Copied byte-for-byte out of data/hotels.json with python — never retyped by hand.
LICENCE = 'Имената и регистровите данни: отделни факти от Националния туристически регистър (чл. 4 ЗАПСП; без масово копиране на регистъра). Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md). Старите имена: кадастрални адресни полета + публични източници, всяко с ред в присъдния документ на З1 (22.08.2026). Имената от публична идентификация (OSM, официални сайтове, общински регистри): отделни факти, а не извадка от база — източникът на всеки ред стои в `src` (цикълът „дупката“, 23.08.2026).'

# The second licence line, added by ЛОТ 1в: one expanded name travels as a search
# alias from OpenStreetMap (way 199237000), so it gets its own sentence.
LICENCE_OSM = 'Разгърнати имена (псевдоними за търсене) от OpenStreetMap: „© OpenStreetMap contributors, ODbL“ — лиценз ODbL 1.0, снапшот 2026-08-10. Днес е един такъв псевдоним (way 199237000); изворът на всеки псевдоним стои в `old_names_src`.'

# The third licence line, added by ЛОТ 1в-Б: the sources of an ADDRESS.
LICENCE_ADDRESS = 'Адресите: КАИС адресното поле на тялото под пина (© АГКК — отворените данни, върху които стоят и координатите; условията на ФАЗА_0_лицензи.md); регистровите адреси (Община Варна, МОН/НЕИСПУО, ИАМН) и Националният туристически регистър: отделни факти от регистрите (чл. 4 ЗАПСП), не копие на регистър; адресите от OpenStreetMap: „© OpenStreetMap contributors, ODbL“ — лиценз ODbL 1.0. Изворът на всеки адрес стои в `address.src`; токени за собственост не влизат в адреса.'

# ЛОТ 1в-Б (ADR 008 D5, план §2в + К5(г)): the PROPERTY tokens. The raw НТР
# addresses carry "ПИ № …", "УПИ …", "кв. 20", "поземлен имот 583" — measured,
# 21 delivered hotels used to carry one. The masking lives in the exporter and
# THIS is the publish gate: over the whole blob, minus the licence sentences,
# which name cadastral address fields as a source on purpose. Every token is
# matched as a WORD — measured 04.09, a naive substring "ПИ" fires on "КАПИТАН
# РАЙЧО" and a case-blind one on "Пирот", and both false alarms are real.
_LETTER = "А-Яа-яA-Za-z"
_PROPERTY_RE = re.compile(
    "(?<![%s])(?:У?ПИ(?![%s])|(?:парцел|имот)(?![%s]))"
    "|кадастр|кад[.][ ]*ид|кв[.]?[ ]*[0-9]"
    % (_LETTER, _LETTER, _LETTER), re.IGNORECASE)
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
#
# К2 (plan §12, closing C14 finding 6): the mobile rule above cannot see a VARNA
# LANDLINE — nine digits, "052 123 456" / "052/123-456" / "052123456" — which is
# exactly the number a hotel or a practice publishes. Measured 03.09 over the free
# text of all three delivered files (data/hotels.json 467 values, data/places.json
# 314, data/place_categories.json 1732 strings) and over their raw bytes: zero hits,
# so the rule costs nothing today: the longest digit run anywhere in the three
# files is FOUR („ЧОУ "Феникс 2020"“; „ж.к. ИЗГРЕВ 552-2“ has three, „ЦДГ 43
# "Пинокио"“ two), five short of the nine the pattern needs, so no house number
# and no school number can trip it. The doctor rule likewise becomes the WHOLE WORD
# „д-р“/„доктор“/„dr“ standing IN FRONT OF a name — the sibling gate's pattern
# verbatim (test_places_public_bundle._DOCTOR_RE), so "доктор Иванов" is caught
# here too, where "\bд-р\b" alone let it through. Zero hits on the hotels
# delivery before and after.
# ЛОТ 1в-Б (план §2г S5): the address text is scanned like every other free
# string, and the doctor rule fires on a STREET named after a doctor — measured
# 04.09 on the delivery: „ул. „Д-р Василаки Пападопулу“ 54“, „ул. Д-Р БАСАНОВИЧ
# 29“, „ул. Д-р Любен Лазаров № 115“, „ул. Д-Р ЛЮДВИГ ЗАМЕНХОФ 38“ (five rows in
# the two files). The excuse is as narrow as institutional(): the title must stand
# IMMEDIATELY after the prefix the SOURCE wrote, at the very START of the address
# (an optional quote between them). A second title anywhere else in the same
# string, or a title without a street prefix, is still a red row.
_DOCTOR_STREET_RE = re.compile(
    "^(?:ул|бул|пл)[.]?[ ]*[\"„]?[ ]*(?:д-?р|доктор|dr)[ .]", re.I)
_PII_PATTERNS = {
    "phone": re.compile(r"(\+359|\b0)8\d(?:[\s-]?\d){7}"),
    "landline": re.compile(r"0\d{2}[\s/-]?\d{3}[\s-]?\d{3}"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "ten_digit_run": re.compile(r"\d{10}"),
    "doctor": re.compile(r"(?:^|[^а-яА-Яa-zA-Z])(?:д-?р|доктор|dr)\b\.?\s+\S", re.I),
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

    def test_every_record_carries_exactly_the_fourteen_keys(self):
        for rec in self.records:
            self.assertEqual(set(rec.keys()), RECORD_KEYS, rec.get("name"))

    def test_every_alias_carries_its_own_source(self):
        # ADR 008 D1: same length, same order, every letter from the closed list.
        # The 15 КАИС address-field names and the one OSM string used to travel
        # under the record's own `src`; now each says where it came from.
        for rec in self.records:
            self.assertIsInstance(rec["old_names_src"], list, rec.get("name"))
            self.assertEqual(len(rec["old_names_src"]), len(rec["old_names"]),
                             rec.get("name"))
            for code in rec["old_names_src"]:
                self.assertIn(code, ALIAS_SRC, rec.get("name"))

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

    def test_zone_is_a_quarter_or_district_label(self):
        # Phase-2 plan §8: the zone is no longer one of the six closed boxes the old
        # `zone_of` returned — it is the quarter or district resolved by the `zone_label`
        # ladder signed at Gate 1b (resort box → the КАИС quarter of the anchored building
        # → the drawn envelope → the district). 24 distinct values over these 226 records,
        # and the list moves with every КАИС generation, so pinning them as an enumeration
        # would pin the generation instead of the contract. What the delivery owes is the
        # SHAPE: a non-empty label short enough to sit on the meta row of a result.
        for rec in self.records:
            zone = rec["zone"]
            self.assertIsInstance(zone, str, rec.get("name"))
            self.assertTrue(zone.strip(), rec.get("name"))
            self.assertLessEqual(len(zone), 60, rec.get("name"))

    def test_every_typed_location_is_null_or_the_closed_three_key_object(self):
        """ЛОТ 1в-В (S1): {name, src, code}, all three non-empty, from closed lists."""
        for rec in self.records:
            for field, srcs, codes in (("quarter", QUARTER_SRC, QUARTER_CODES),
                                       ("locality", QUARTER_SRC, LOCALITY_CODES),
                                       ("district", DISTRICT_SRC, DISTRICT_CODES)):
                value = rec[field]
                if value is None:
                    self.assertNotEqual(field, "district", rec["name"])
                    continue
                self.assertIsInstance(value, dict, rec["name"])
                self.assertEqual(set(value), LOCATION_KEYS, rec["name"])
                for key in LOCATION_KEYS:
                    self.assertIsInstance(value[key], str, rec["name"])
                    self.assertTrue(value[key].strip(), rec["name"])
                self.assertIn(value["src"], srcs, rec["name"])
                self.assertIn(value["code"], codes, rec["name"])

    def test_the_compat_label_follows_from_the_typed_fields(self):
        """S1: `zone` === quarter?.name ?? „район “ + district.name — nothing else."""
        for rec in self.records:
            want = rec["quarter"]["name"] if rec["quarter"] else "район " + rec["district"]["name"]
            self.assertEqual(rec["zone"], want, rec["name"])

    def test_the_district_covers_every_record(self):
        """S4: 100 % and the five city districts, measured — not assumed."""
        self.assertEqual(sum(1 for r in self.records if r["district"]), len(self.records))
        self.assertEqual({r["district"]["code"] for r in self.records} - DISTRICT_CODES, set())

    def test_the_typed_coverage_is_the_measured_one(self):
        """The numbers of the manifest Petar signs — a drift is a re-delivery."""
        by_src = {}
        for rec in self.records:
            if rec["quarter"]:
                by_src[rec["quarter"]["src"]] = by_src.get(rec["quarter"]["src"], 0) + 1
        self.assertEqual(by_src, QUARTER_BY_SRC)
        self.assertEqual(sum(1 for r in self.records if r["locality"]), LOCALITY_COUNT)

    def test_no_cadastral_identifier_reaches_the_public_payload(self):
        self.assertEqual(sorted(set(_CADASTRAL_RE.findall(self.text))), [])
        self.assertNotIn("10135", self.text)

    def test_no_property_token_reaches_the_public_payload(self):
        # К5 (г) + план §2в: the publish gate over the whole blob, by word. The three
        # licence sentences are lifted out first — they name cadastral address fields
        # as a SOURCE, which is the one legitimate place for the word.
        rest = self.text
        for line in (LICENCE, LICENCE_OSM, LICENCE_ADDRESS):
            rest = rest.replace(json.dumps(line, ensure_ascii=False)[1:-1], "")
        self.assertEqual([m.group(0) for m in _PROPERTY_RE.finditer(rest)], [])

    def test_every_address_is_null_or_the_closed_four_key_object(self):
        # ADR 008 D5 / план §2г S5. `null` is an answer, not a gap.
        for rec in self.records:
            addr = rec["address"]
            if addr is None:
                continue
            self.assertIsInstance(addr, dict, rec["name"])
            self.assertEqual(set(addr.keys()), ADDRESS_KEYS, rec["name"])
            for key in ADDRESS_KEYS:
                self.assertIsInstance(addr[key], str, (rec["name"], key))
                self.assertTrue(addr[key].strip(), (rec["name"], key))
            self.assertIn(addr["src"], ADDRESS_SRC, rec["name"])

    def test_the_address_coverage_is_the_measured_one(self):
        # The numbers Gate 1-Б was signed on, re-measured against the P5 delivery.
        with_address = [rec for rec in self.records if rec["address"]]
        self.assertEqual(len(with_address), ADDRESS_COUNT)
        by_src = {}
        for rec in with_address:
            code = rec["address"]["src"]
            by_src[code] = by_src.get(code, 0) + 1
        self.assertEqual(by_src, ADDRESS_BY_SRC)

    def test_the_street_phrase_and_the_house_key_are_read_back_out_of_the_text(self):
        # К7 (1): the canonicalisation is an INDEPENDENT transcript. The exporter emits
        # the three fields TOGETHER and its own QA checks them; this reads them back the
        # other way round, with a normaliser written for this test alone. The client
        # never parses `text` either (ADR 008 D6), so a drift between the three would be
        # invisible in the browser and loud only here.
        for rec in self.records:
            addr = rec["address"]
            if not addr:
                continue
            flat = " ".join("".join(c if c.isalnum() else " "
                                    for c in addr["text"].lower()).split())
            phrase = addr["street_phrase"]
            self.assertIn(" %s " % phrase, " %s " % flat, rec["name"])
            tail = "".join(flat[flat.index(phrase) + len(phrase):].split())
            self.assertTrue(tail.startswith(addr["house_key"]),
                            (rec["name"], addr["text"], addr["house_key"]))

    def test_the_address_licence_line_is_verbatim(self):
        # ADR 008 D5: the sources of an ADDRESS get their own sentence. Not one of them
        # is new to this delivery (план §2 т. 5), so the README licence table is
        # untouched and the line itself is pinned right here.
        self.assertEqual(self.doc["_meta"]["licence_address"], LICENCE_ADDRESS)
        self.assertIn("ODbL 1.0", LICENCE_ADDRESS)
        self.assertIn("`address.src`", LICENCE_ADDRESS)

    def test_the_cadastral_word_appears_only_inside_the_licence_line(self):
        # The licence sentence names cadastral address fields as a source; nowhere else
        # in the payload may the word appear, because no record may carry a cadnum.
        self.assertIn(LICENCE, self.text)
        rest = self.text.replace(LICENCE, "").replace(LICENCE_OSM, "")
        rest = rest.replace(LICENCE_ADDRESS, "")
        # ЛОТ 1в: 15 old names come from the КАИС address field, so the word rides
        # the CODE `KAIS`, never the free text — the assertion below still holds.
        self.assertNotIn("кадаст", rest)

    def test_licence_line_is_verbatim(self):
        self.assertEqual(self.doc["_meta"]["licence"], LICENCE)

    def test_the_osm_alias_licence_line_is_verbatim(self):
        # Амандамент А4 т. 3 (К4): a NEW OSM alias outside the 29 grandfathered ones
        # is a line in the licences, not just a letter in a row. One such alias today,
        # and the sentence's own count is measured against the payload.
        self.assertEqual(self.doc["_meta"]["licence_osm"], LICENCE_OSM)
        self.assertIn("ODbL 1.0", LICENCE_OSM)
        osm = [rec["name"] for rec in self.records if "OSM" in rec["old_names_src"]]
        self.assertEqual(len(osm), 1, osm)

    def test_readme_carries_licence_line(self):
        # Plan §5 G9. The licence travels with the data: whoever reads the repo's front
        # page must see the same sentence the payload carries, in both mirrors, unedited
        # — a paraphrase would be a different licence. Each README quote therefore sits
        # on ONE line; wrapping it would break the byte equality this asserts.
        readme = (REPO / "README.md").read_text(encoding="utf-8")
        licence = self.doc["_meta"]["licence"]
        self.assertGreaterEqual(readme.count(licence), 2, "licence quoted in BG and EN")
        self.assertGreaterEqual(readme.count(self.doc["_meta"]["licence_osm"]), 2,
                                "OSM alias licence line quoted in BG and EN")
        # The bundle is not in the sw.js offline pack; the README says so out loud.
        # assertTrue, not assertIn: a failing assertIn would dump the whole README.
        self.assertTrue("не са част от офлайн пакета" in readme,
                        "README.md lost the offline note about the hotels bundle")

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
            # ЛОТ 1в-Б (план §2г S5): an address text is free text too — with the ONE
            # measured exception above. A phone, an e-mail, a ten-digit run or a sole
            # trader inside an address stays as red as it is inside a name.
            addr = rec["address"]
            if not addr:
                continue
            excused = _DOCTOR_STREET_RE.sub("ул. ", addr["text"])
            for label, pattern in _PII_PATTERNS.items():
                probe = excused if label == "doctor" else addr["text"]
                if pattern.search(probe):
                    hits.append((label, addr["text"]))
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

    def test_the_three_location_dictionaries_are_closed_and_typed(self):
        """ЛОТ 1в-В (S3): three (class, code) dictionaries, each entry {name, aliases}."""
        locs = self.doc["locations"]
        self.assertEqual({k: len(v) for k, v in locs.items()}, LOCATION_COUNTS)
        for entries in locs.values():
            for code, entry in entries.items():
                self.assertEqual(set(entry), {"name", "aliases"}, code)
                self.assertIsInstance(entry["name"], str, code)
                self.assertTrue(entry["name"].strip(), code)
                self.assertIsInstance(entry["aliases"], list, code)
                for alias in entry["aliases"]:
                    self.assertIsInstance(alias, str, code)
                    self.assertTrue(alias.strip(), code)
        self.assertEqual({e["name"] for e in locs["district"].values()},
                         {"Приморски", "Одесос", "Младост", "Аспарухово",
                          "Владислав Варненчик"})

    def test_the_legacy_words_are_keyed_by_an_ordinal_inside_its_bundle(self):
        """S2: `places:<n>` / `hotels:<n>` — indexed, never shown, never a district alias."""
        legacy = self.doc["legacy_by_row"]
        self.assertEqual(len(legacy), LEGACY_ROWS)
        for key, words in legacy.items():
            bundle, _, ordinal = key.partition(":")
            self.assertIn(bundle, BUNDLE_SIZES, key)
            self.assertTrue(ordinal.isdigit() and int(ordinal) < BUNDLE_SIZES[bundle], key)
            self.assertIsInstance(words, list, key)
            self.assertTrue(words, key)
            for word in words:
                self.assertIsInstance(word, str, key)
                self.assertTrue(word.strip(), key)

    def test_the_legacy_bundle_sha_is_the_content_of_the_two_payloads(self):
        """S2: the ordinals are only as true as the bundle they were built against.

        The exporter digests its own WORKING-TREE file and that checkout stores the
        hotels export with CRLF, so one content has two digests (measured 04.09).
        Both spellings of THIS content pass and nothing else does — a dictionary
        built against another generation of the payloads is a broken delivery.
        """
        shas = self.doc["_meta"]["legacy_bundle_sha"]
        for key, path in (("places", REPO / "data" / "places.json"), ("hotels", HOTELS)):
            lf = pathlib.Path(path).read_bytes().replace(b"\r\n", b"\n")
            self.assertIn(shas[key],
                          {hashlib.sha256(lf).hexdigest(),
                           hashlib.sha256(lf.replace(b"\n", b"\r\n")).hexdigest()}, key)

    def test_encoding_is_utf8_without_bom_and_free_of_mojibake(self):
        self.assertFalse(self.raw.startswith(b"\xef\xbb\xbf"))
        self.assertEqual(_MOJIBAKE_RE.findall(self.text), [])


if __name__ == "__main__":
    unittest.main()
