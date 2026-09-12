# -*- coding: utf-8 -*-
"""Ф8 · ИБ1-Г9к/Г17/Г19к/Г22/Г23 — what the FOUR address surfaces say.

    python -m unittest tests.test_address_quarter_render

The coordinate decides the quarter WORD on four surfaces (план §0): the dropdown
row (`buildExactItem`), the panel (`selectResult` → `renderDetailSheet`), the popup
(`openSearchPopup`) and the GPS row (`coordMeta`); the fifth, the GPS popup, is
equal by construction because it calls the same `coordMeta`.

This gate drives `tests/address_slice_probe.mjs` (Ф9) as a SUBPROCESS — a harness
is not a gate (red line 7): the probe answers, THIS test judges. The slice is cut
by the markers of Т12; a missing marker is a named failure, never a silent skip.

The reference is not a retyped string but the SLICE AT `<БАЗА>` (Кими К44-2): for
every case the same query is run through the pinned older slice, and the verdict
is stated as a difference from it. That way "the word appeared", "the word went
out" and "nothing else moved" are measured against the delivery that is already
signed, not against a hope written into this file.

Coordinates are ASSEMBLED at runtime (О95, red line 5): the flagship's pin is read
out of `data/search_index.json` while the test runs; no tracked file of Fire_Varna
carries a coordinate pair in prose.

Червено по конструкция до К8/К9 (ИНТЕРВАЛ А): the markers are born in К9 and the
delivered payload in К8. Until then every method here fails with the reason.

Run: python -m unittest discover -s tests
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]

PROBE = REPO / "tests" / "address_slice_probe.mjs"
INDEX = pathlib.Path(os.environ.get("FIRE_VARNA_INDEX_HTML_PATH") or (REPO / "index.html"))
CORPUS = pathlib.Path(os.environ.get("FIRE_VARNA_CORPUS_PATH")
                      or (REPO / "scratch" / "places_search" / "ib_corpus_11.09.json"))
DELIVERED = pathlib.Path(os.environ.get("FIRE_VARNA_QUARTER_INDEX_PATH")
                         or (REPO / "data" / "address_quarters.json"))
SEARCH_INDEX = REPO / "data" / "search_index.json"
ADDRESS_ROWS = REPO / "data" / "address_rows.json"

# <БАЗА> — the pinned reference commit of the lot (план §4 стъпка 3а). `index.html`
# at this commit is the blob before К9: today's wording, the one the word replaces.
BASE = os.environ.get("FIRE_VARNA_BASE_COMMIT") or "73dfc91"
# The слайс of the BASE blob has no markers; it is cut by the measured line numbers
# of план §1.1 (`new Function` raises 4840–6198, measured, О123). One-based, both ends.
BASE_SLICE_LINES = (4840, 6198)

# Т12 — five markers, two cuts. The text is the plan's, inside a stable prefix.
MARK_SHARED_START = u"// IB1 shared quarter state start"
MARK_SHARED_END = u"// IB1 shared quarter state end"
MARK_SLICE_START = u"// IB1 address slice start"
MARK_SLICE_CORE_END = u"// IB1 address slice core end"
MARK_SLICE_END = u"// IB1 address slice end"

# The exports the probe asks the slice for. `quarterIndex`, `entriesDigest` and
# `rowsDigest` exist only after Т1–Т5; the base slice is raised without them.
EXPORTS = ["ensureSearchData", "runGeocoderSearch", "dedupeDisplayRows",
           "buildExactItem", "selectResult", "parseCoordQuery", "renderCoordRow",
           "coordTitle", "coordMeta", "openCoordPopup"]
EXPORTS_QUARTER = EXPORTS + ["quarterIndex", "entriesDigest", "rowsDigest",
                             "quarterOfHit", "quarterTitleWord"]

QUARTERS_URL = "data/address_quarters.json"
SEARCH_INDEX_URL = "data/search_index.json"
ADDRESS_ROWS_URL = "data/address_rows.json"

# The flagship (М): the one `mf` entry with exactly these tokens. Its written word
# says „кв. Чайка“ and the polygon says `levski1` — the whole lot in one row.
FLAGSHIP_TOKENS = ["studentska", "bl", "11"]
FLAGSHIP_QUERY = u"студентска бл 11"
WITNESS_PREFIX = u"написано: "
# §3.Д — the row the panel adds when the cell has a parent (ИБ1-О32).
PARENT_PREFIX = u"част от "

# ИБ1-О31/О33 — the class the dot-blind normalizer doubled: a written quarter
# that carries DOTS („ж.к. Възраждане“, „в.з. Варна“, „с.о. Ален Мак“) and, on
# the GPS surface, a DOT-LESS token run against a dotted name („жк бриз“ against
# „ж.к. Бриз“). Measured on the delivery: 597 records with a cell used to read
# their quarter twice without a witness, 3 484 GPS rows the same.
DOTTED_HEADS = (u"ж.к.", u"в.з.", u"с.о.", u"к.к.")
# The six queries К7в put into Ф11. They are named here as well ON PURPOSE: the
# first assertion of every method below is that the corpus still carries them,
# so a corpus that drifts away from the gate fails loudly instead of silently
# testing nothing.
DOTTED_QUERIES = (u"ана феликсова 18", u"бул народни будители 11",
                  u"22 ра 15", u"зл пясъци бл ф")
DOTLESS_QUERIES = (u"жк бриз", u"кк златни пясъци")
# §3.Д (д) — the closed DOT-LESS list the GPS label meets.
TOKEN_TYPES = (u"кв", u"жк", u"кк", u"вз", u"со", u"м", u"мт", u"местност",
               u"зона", u"пз", u"квартал")


def flat(text):
    """The client's `flat` after К9а: the dot is CUT, never replaced by a space.

    Replacing it was ИБ1-О31: „ж.к.“ became „ж к“, the lead word became „ж“ and
    no type ever matched. The test carries the same rule so it can count quarter
    words dot-blind — „ж.к. Бриз“ and „жк бриз“ are ONE word, said twice.
    """
    lowered = (text or u"").lower().replace(u".", u"")
    return re.sub(r"\s+", u" ", re.sub(r"[,-]", u" ", lowered)).strip()


def dotless_gps_rows(doc, rows, want):
    """Rows of §3.Д (д), found in the live payload — never written down here.

    A row qualifies when its cell's name carries dots, the label opens with a
    dot-less type token, the run spells that same name, and the label is
    „streetish“ enough for `nearestAddressTo` to prefer it (a digit, no trailing
    „ 0“). Each quarter is taken once, so the cases are not three copies of one.
    """
    found = []
    for index, row in enumerate(rows):
        cell = doc["row_cell"][index]
        if cell < 0:
            continue
        name = doc["names"][cell]
        if u"." not in name or name in [n for _, n in found]:
            continue
        label = row[0] or u""
        parts = label.split()
        if len(parts) < 2 or parts[0].lower() not in TOKEN_TYPES:
            continue
        if not re.search(r"\d", label) or re.search(r"\s0$", label):
            continue
        run = len(flat(name).split(u" "))
        if flat(u" ".join(parts[:run])) != flat(name):
            continue
        found.append((index, name))
        if len(found) >= want:
            break
    return found


def require_node(test):
    node = shutil.which("node")
    if not node:
        test.fail(u"node липсва — харнесът е гейт, не пропуснат тест")
    return node


def html_text(path=INDEX):
    return path.read_bytes().decode("utf-8")


def cut(text, first, last, test):
    i = text.find(first)
    if i < 0:
        test.fail(u"липсва маркер Т12: %s (ражда се в К9 — ИНТЕРВАЛ А)" % first)
    j = text.find(last, i)
    if j < 0:
        test.fail(u"липсва маркер Т12: %s" % last)
    return text[text.index("\n", i) + 1:j]


def client_slices(test):
    """(shared, slice) of the working `index.html`, cut by the five markers."""
    text = html_text()
    shared = cut(text, MARK_SHARED_START, MARK_SHARED_END, test)
    body = cut(text, MARK_SLICE_START, MARK_SLICE_END, test)
    if MARK_SLICE_CORE_END not in text:
        test.fail(u"липсва маркер Т12: %s" % MARK_SLICE_CORE_END)
    return shared, body


def base_slice(test):
    """The slice of `<БАЗА>:index.html`, cut by the measured line numbers."""
    proc = subprocess.run(["git", "-C", str(REPO), "show", "%s:index.html" % BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        test.fail(u"няма блоб %s:index.html" % BASE)
    lines = proc.stdout.decode("utf-8").split("\n")
    first, last = BASE_SLICE_LINES
    return "\n".join(lines[first - 1:last])


def delivered_doc(test, path=None):
    path = path or DELIVERED
    if not path.exists():
        test.fail(u"липсва %s — К8 още не е положен (ИНТЕРВАЛ А)" % path)
    return json.loads(path.read_text(encoding="utf-8"))


def corpus_doc(test):
    if not CORPUS.exists():
        test.fail(u"липсва корпусът Ф11: %s" % CORPUS)
    return json.loads(CORPUS.read_text(encoding="utf-8"))


def search_entries():
    return json.loads(SEARCH_INDEX.read_text(encoding="utf-8"))["entries"]


def flagship_index(entries):
    for i, entry in enumerate(entries):
        if entry.get("kind") == "mf" and entry.get("tk") == FLAGSHIP_TOKENS:
            return i
    raise AssertionError(u"флагманът изчезна от search_index.json")


def coordinate_query(pin):
    """The GPS query string, ASSEMBLED at runtime out of the pin (О95)."""
    return u"%s, %s" % (repr(float(pin[0])), repr(float(pin[1])))


def run_probe(test, payload, quarters_path=None):
    node = require_node(test)
    files = {SEARCH_INDEX_URL: str(SEARCH_INDEX), ADDRESS_ROWS_URL: str(ADDRESS_ROWS)}
    if quarters_path is not None:
        files[QUARTERS_URL] = str(quarters_path)
    payload = dict(payload)
    payload["payload_files"] = files
    proc = subprocess.run([node, str(PROBE)],
                          input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(REPO))
    out = proc.stdout.decode("utf-8", "replace")
    try:
        doc = json.loads(out)
    except ValueError:
        test.fail(u"Ф9 не върна json (rc=%d): %s | %s"
                  % (proc.returncode, out[:400],
                     proc.stderr.decode("utf-8", "replace")[:400]))
    if not doc.get("ok"):
        test.fail(u"Ф9 падна: %s" % json.dumps(doc, ensure_ascii=False)[:600])
    return doc["answers"]


def ask_client(test, asks, quarters_path=None):
    shared, body = client_slices(test)
    return run_probe(test, {"shared": shared, "slice": body,
                            "exports": EXPORTS_QUARTER, "asks": asks},
                     quarters_path=quarters_path or DELIVERED)


def ask_base(test, asks):
    return run_probe(test, {"slice": base_slice(test), "exports": EXPORTS, "asks": asks})


def doctored(tmp, doc, field, value):
    """A copy of the delivery with ONE field changed — written to a temp dir,
    never into `data/`."""
    out = dict(doc)
    meta = dict(out["generated_from"])
    meta[field] = value
    out["generated_from"] = meta
    path = pathlib.Path(tmp) / ("quarters_%s.json" % field)
    path.write_text(json.dumps(out, ensure_ascii=False, sort_keys=True,
                               separators=(",", ":")), encoding="utf-8")
    return path


def other_digest(value):
    """Another 8-hex digest of the same shape — a permutation, not a truncation."""
    return ("f" + value[1:]) if not value.startswith("f") else ("0" + value[1:])


class CorpusParityTest(unittest.TestCase):
    """Ф11 is a PROJECTION of the delivery — same entries, same order, same cells."""

    def test_corpus_matches_the_delivered_cells(self):
        doc = delivered_doc(self)
        corpus = corpus_doc(self)
        entries = search_entries()
        mine = [{"tk": e["tk"], "kind": e["kind"], "cell": doc["entry_cell"][i]}
                for i, e in enumerate(entries) if "studentska" in (e.get("tk") or [])]
        self.assertEqual(len(mine), len(corpus["entries"]))
        self.assertEqual(mine, corpus["entries"],
                         u"корпусът и доставката се разминават по клетка или по ред")


class FlagshipRowTest(unittest.TestCase):
    """ИБ1-Г9к — the row of the flagship speaks the POLYGON's word."""

    def test_row_title_and_witness(self):
        doc = delivered_doc(self)
        entries = search_entries()
        cell = doc["entry_cell"][flagship_index(entries)]
        self.assertNotEqual(cell, -1, u"флагманът е угасен в доставката")
        name = doc["names"][cell]

        base = ask_base(self, [{"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1}])[0]
        new = ask_client(self, [{"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1}])[0]
        self.assertTrue(base and new, u"нула редове за флагмана")

        self.assertIn(name, new[0]["title"],
                      u"редът не носи думата на полигона: %r" % new[0]["title"])
        self.assertNotEqual(new[0]["title"], base[0]["title"],
                            u"редът не се е променил спрямо <БАЗА>")
        self.assertIn(WITNESS_PREFIX, new[0]["meta"] or u"",
                      u"вторият ред няма свидетел: %r" % new[0]["meta"])
        self.assertIn(base[0]["title"].split(u",")[0], new[0]["meta"],
                      u"свидетелят не носи НАПИСАНАТА дума")
        self.assertTrue((new[0]["meta"] or u"").startswith(u"район "),
                        u"вторият ред не започва с района: %r" % new[0]["meta"])


class FourSurfacesTest(unittest.TestCase):
    """ИБ1-Г22 — the row, the panel, the popup and the GPS line say ONE word."""

    def test_one_word_on_every_surface(self):
        doc = delivered_doc(self)
        entries = search_entries()
        i = flagship_index(entries)
        cell = doc["entry_cell"][i]
        name = doc["names"][cell]
        pin = entries[i]["pin"]

        answers = ask_client(self, [
            {"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1},
            {"ask": "panel", "q": FLAGSHIP_QUERY, "pick": 0},
            {"ask": "coord", "q": coordinate_query(pin)},
        ])
        row, panel, coord = answers
        self.assertIn(name, row[0]["title"])
        surface = u" ".join(panel["popups"] + ([panel["sheet"]] if panel["sheet"] else []))
        self.assertIn(name, surface, u"панелът/попъпът мълчат: %r" % surface)
        self.assertIn(name, coord["meta"] or u"",
                      u"GPS-редът мълчи: %r" % coord["meta"])
        self.assertEqual(coord["meta"], coord["popup"].replace(u"GPS " + coord["title"], u"").strip(),
                         u"петата повърхност не е равна по конструкция на GPS-реда")


class PositionalJoinTest(unittest.TestCase):
    """ИБ1-Г17 — a moved payload silences the word instead of misnaming a place."""

    def test_a_foreign_entries_digest_silences_the_row(self):
        doc = delivered_doc(self)
        base = ask_base(self, [{"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1}])[0]
        with tempfile.TemporaryDirectory(prefix="ib1_render_") as tmp:
            path = doctored(tmp, doc, "entries_digest",
                            other_digest(doc["generated_from"]["entries_digest"]))
            new = ask_client(self, [{"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1}],
                             quarters_path=path)[0]
        self.assertEqual(new[0]["title"], base[0]["title"],
                         u"думата оцеля при разминал се entries_digest")
        self.assertEqual(new[0]["html"], base[0]["html"],
                         u"редът не е байт-равен на <БАЗА> при угасена дума")


class WitnessRulesTest(unittest.TestCase):
    """ИБ1-Г19к — „гр варна район X“, „неизвестна“ and the bare names."""

    def test_district_and_unknown_rows_keep_their_text(self):
        corpus = corpus_doc(self)
        picks = [q for q in corpus["queries"]
                 if q.startswith(u"гр варна район") or q == u"неизвестна"]
        self.assertTrue(picks, u"корпусът няма заявка за клон (в)")
        for query in picks:
            base = ask_base(self, [{"ask": "render", "q": query, "limit": 3}])[0]
            new = ask_client(self, [{"ask": "render", "q": query, "limit": 3}])[0]
            self.assertEqual([r["title"] for r in new], [r["title"] for r in base],
                             u"клон (в) е нарушен за %r" % query)

    def test_a_bare_name_is_never_written_twice(self):
        corpus = corpus_doc(self)
        doc = delivered_doc(self)
        names = set(doc["names"])
        for query in corpus["queries"]:
            new = ask_client(self, [{"ask": "render", "q": query, "limit": 3}])[0]
            for row in new:
                title = row["title"] or u""
                for name in names:
                    if name and title.count(name) > 1:
                        self.fail(u"името %r се повтаря в %r" % (name, title))

    def test_a_locality_cell_never_fills_the_word(self):
        """D6 (`010:48`) — a полигон-местност never fills `quarter`; the build
        silences it, and the row therefore reads exactly as it does at <БАЗА>."""
        corpus = corpus_doc(self)
        picks = [q for q in corpus["queries"] if q in (u"зпз", u"местност боровец юг")]
        self.assertTrue(picks, u"корпусът няма заявка за locality")
        for query in picks:
            base = ask_base(self, [{"ask": "render", "q": query, "limit": 3}])[0]
            new = ask_client(self, [{"ask": "render", "q": query, "limit": 3}])[0]
            self.assertEqual([r["title"] for r in new], [r["title"] for r in base],
                             u"locality-клетка пълни дума за %r" % query)


class GpsRowTest(unittest.TestCase):
    """ИБ1-Г23 — `row_cell` carries the GPS line, `rows_digest` guards it."""

    def test_the_gps_line_carries_one_word_and_falls_back(self):
        doc = delivered_doc(self)
        entries = search_entries()
        pin = entries[flagship_index(entries)]["pin"]
        query = coordinate_query(pin)

        base = ask_base(self, [{"ask": "coord", "q": query}])[0]
        new = ask_client(self, [{"ask": "coord", "q": query}])[0]
        self.assertNotEqual(new["meta"], base["meta"],
                            u"GPS-редът не е пипнат от row_cell")
        names = [n for n in doc["names"] if n and n in (new["meta"] or u"")]
        self.assertEqual(len(names), 1,
                         u"GPS-редът носи %d квартални думи: %r" % (len(names), new["meta"]))
        self.assertEqual((new["meta"] or u"").count(names[0]), 1,
                         u"кварталната дума се повтаря на GPS-реда: %r" % new["meta"])

        with tempfile.TemporaryDirectory(prefix="ib1_gps_") as tmp:
            path = doctored(tmp, doc, "rows_digest",
                            other_digest(doc["generated_from"]["rows_digest"]))
            silenced = ask_client(self, [{"ask": "coord", "q": query}], quarters_path=path)[0]
        self.assertEqual(silenced["meta"], base["meta"],
                         u"думата оцеля на GPS при разминал се rows_digest")


class DottedPrefixTest(unittest.TestCase):
    """ИБ1-О31/О32/О33 — the DOTTED prefixes: cut, confessed, and the parent row.

    Until К9а the closed list of §3.Д (а) was carried without its dots while the
    normalizer replaced every dot with a space: „ж.к. Възраждане“ flattened to
    „ж к възраждане“, the lead word was „ж“, no type matched and the row read
    „ж.к. Възраждане 1, ж.к. Възраждане, Ана Феликсова 18“ — the quarter twice,
    and no „написано:“ to confess it. These three methods are the gate for that
    class; they were RED on К9 and green on К9а.
    """

    def corpus_carries_the_class(self):
        corpus = corpus_doc(self)
        missing = [q for q in DOTTED_QUERIES + DOTLESS_QUERIES
                   if q not in corpus["queries"]]
        if missing:
            self.fail(u"Ф11 не носи заявките на класа: %s" % u", ".join(missing))

    def test_a_dotted_written_quarter_is_cut_and_confessed(self):
        self.corpus_carries_the_class()
        doc = delivered_doc(self)
        judged = 0
        for query in DOTTED_QUERIES:
            base = ask_base(self, [{"ask": "render", "q": query, "limit": 5}])[0]
            found, rows = ask_client(self, [{"ask": "search", "q": query, "limit": 5},
                                            {"ask": "render", "q": query, "limit": 5}])
            for i, row in enumerate(rows):
                if i >= len(base):
                    break
                written = base[i]["title"] or u""
                head = written.split(u", ")[0]
                if not head.startswith(DOTTED_HEADS):
                    continue
                position = found["rows"][i]["ord"]
                if position is None:
                    continue
                cell = doc["entry_cell"][position]
                if cell < 0:
                    continue
                name = doc["names"][cell]
                tail = written[len(head) + 2:]
                self.assertEqual(row["title"], name + u", " + tail,
                                 u"%r: заглавието не е „име + остатък“: %r"
                                 % (query, row["title"]))
                if flat(head) != flat(name):
                    # A DIFFERENT quarter was written: it leaves the title and
                    # goes to the second row as the witness of D18. (When the two
                    # agree the title legitimately re-opens with the same word.)
                    self.assertNotIn(head + u", ", row["title"] or u"",
                                     u"написаният квартал не е отрязан: %r" % row["title"])
                    self.assertIn(WITNESS_PREFIX + head, row["meta"] or u"",
                                  u"%r: няма свидетел за %r: %r"
                                  % (query, head, row["meta"]))
                judged += 1
        self.assertGreaterEqual(judged, len(DOTTED_QUERIES),
                                u"класът не е представен: съдени са %d реда" % judged)

    def test_the_gps_line_cuts_the_dotless_token(self):
        """§3.Д (д) — „жк бриз 2“ in „ж.к. Бриз“ says the quarter ONCE."""
        self.corpus_carries_the_class()
        doc = delivered_doc(self)
        rows = json.loads(ADDRESS_ROWS.read_text(encoding="utf-8"))["rows"]
        cases = dotless_gps_rows(doc, rows, 3)
        self.assertGreaterEqual(len(cases), 3,
                                u"живият товар няма редове от клас (д): %r" % cases)
        for index, name in cases:
            query = coordinate_query((rows[index][1], rows[index][2]))
            base = ask_base(self, [{"ask": "coord", "q": query}])[0]
            new = ask_client(self, [{"ask": "coord", "q": query}])[0]
            meta = new["meta"] or u""
            self.assertNotEqual(meta, base["meta"],
                                u"GPS-редът не е пипнат от row_cell: %r" % meta)
            present = [n for n in doc["names"] if n and n in meta]
            self.assertEqual(len(present), 1,
                             u"GPS-редът носи %d квартални думи: %r" % (len(present), meta))
            self.assertEqual(flat(meta).count(flat(name)), 1,
                             u"GPS-редът казва %r два пъти: %r" % (name, meta))

    def test_the_panel_says_what_the_quarter_is_part_of(self):
        """ИБ1-О32 · §3.Д — `parents[i]` непразно -> „част от <parent_display>“."""
        doc = delivered_doc(self)
        entries = search_entries()
        cell = doc["entry_cell"][flagship_index(entries)]
        self.assertNotEqual(cell, -1, u"флагманът е угасен в доставката")
        parent = doc["parents"][cell]
        if not parent:
            self.fail(u"клетката на флагмана няма родител — фикстурата е мръднала")
        panel = ask_client(self, [{"ask": "panel", "q": FLAGSHIP_QUERY, "pick": 0}])[0]
        surface = u" ".join(panel["popups"] + ([panel["sheet"]] if panel["sheet"] else []))
        self.assertIn(PARENT_PREFIX + parent, surface,
                      u"панелът не казва на кой квартал е част: %r" % surface)


if __name__ == "__main__":
    unittest.main()
