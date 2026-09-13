# -*- coding: utf-8 -*-
"""Лот 4б · Г1-Г4 — a class word alone is not an address (T-01).

    python -m unittest tests.test_address_search_class_words

"хотел", "хотели", "семеен хотел" and "апартхотел" name a CATEGORY, not an
address. The places branch owns that word and has its own dictionary for it;
the address branch used to treat it as an ordinary token and put five address
rows under the hotel list. ADR 006a declares the one exception to D12:
`runGeocoderSearch` gains a closed set of class-word tokens, one guard right
after the tokens are computed and one qualification inside `scoreEntry`.

How this gate works, so no reader has to guess:

  * The client is raised HEADLESS through the flagship's own harness
    (`tests/address_slice_probe.mjs`): the probe answers, THIS file judges. The
    slice is cut by the five markers of Т12, never by a line number.
  * The reference is not a retyped string but the SAME slice at the BASE commit,
    pinned as a LITERAL under its own environment name (`FIRE_VARNA_LOT4B_BASE`),
    never as `merge-base`: a moving reference cannot prove that the untouched
    queries did not move. A base whose blob equals the TRACKED `index.html` is a
    dead reference and fails loud - the refusal compares the blob with the
    TRACKED file on purpose, so that a run with `FIRE_VARNA_INDEX_HTML_PATH`
    pointed at a copy of the base still fails for its OWN reason.
  * The signed set lives here in CYRILLIC (ADR 006a, 4б-D2); the Latin forms in
    the code are DERIVED from it by the client's own `skel`.
  * Nothing is read at module level and no git runs there.
  * "Nothing else moved" is NOT a method here. The whole-file comparison is the
    DELIVERY probe `gates/probe/lot_perimeter.py`, run by hand at the gate with
    the inserted lines named on the command line: a permanent whole-file pin
    freezes `index.html` against one commit and goes red at the next lot, which
    is exactly what lot 1's pin did to this one. What stays permanent here is the
    ANCHOR of each inserted line - that stays true forever.
  * The three negative halves run against DOCTORED copies of `index.html` under
    the temp root - never inside the repository - and demand exit 1 plus the name
    of the method that had to fail; the third one runs the probe itself and
    demands the probe's own reason.

Nine methods: five on the class words, one on the anchors of the five inserted
lines, three negative halves.

No row of `data/address_rows.json` is printed and no coordinate pair stands in
this file: the data guard names a row by its INDEX only.
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import test_address_quarter_render as flagship   # noqa: E402  (module import, never *)

# The base is a LITERAL with its OWN name (план §4 К3.2): not the merge-base and
# not `FIRE_VARNA_BASE_COMMIT`, which the flagship moves for its own reasons.
BASE = os.environ.get("FIRE_VARNA_LOT4B_BASE") or "c8ba4ba"

# The doctored copies of the negative halves live here - never in the tree.
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lot4b_fixtures"

MODULE = "tests.test_address_search_class_words"

# ADR 006a · 4б-D2 - the SIGNED set, in Cyrillic. Twelve forms from the signature
# plus seven added after it (declined forms of the same words and one word of the
# same class), each with zero address rows of its own at the base.
CLASS_WORDS = (u"хотел", u"хотела", u"хотели", u"хотелите", u"хотелът",
               u"апартхотел", u"апартаментен", u"семеен", u"семейни",
               u"семейните", u"семейният", u"апарт",
               u"апартхотели", u"апартхотела", u"апартхотелите",
               u"апартаментна", u"апартаментни", u"мотел", u"мотели")
# The DERIVED spelling: `skel` of each form above, in the same order. Fixing a
# derived spelling is a spelling fix, never a change of the signed decision.
DERIVED_TOKENS = ("hotel", "hotela", "hoteli", "hotelite", "hotelat",
                  "aparthotel", "apartamenten", "semen", "semeini",
                  "semeinite", "semeiniat", "apart",
                  "aparthoteli", "aparthotela", "aparthotelite",
                  "apartamentna", "apartamentni", "motel", "moteli")
# Deliberately NOT class words (ADR 006a): they carry live address rows.
NOT_CLASS_WORDS = ("park", "kompleks")

# --------------------------------------------------------------------------
# The five inserted lines and their anchors - the perimeter of the lot
# --------------------------------------------------------------------------

COMMENT_LINE = (u"    // A class word names a CATEGORY, not an address; "
                u"the places branch owns it (ADR 006a).\n")
CONST_LINE = (u"    const CLASS_WORD_TOKENS = new Set(['hotel','hotela','hoteli',"
              u"'hotelite','hotelat','aparthotel','apartamenten','semen','semeini',"
              u"'semeinite','semeiniat','apart','aparthoteli','aparthotela',"
              u"'aparthotelite','apartamentna','apartamentni','motel','moteli']);\n")
GUARD_LINE = (u"      if (toks.every(function (t) { return CLASS_WORD_TOKENS.has(t); }))"
              u" return [];\n")
COUNTER_LINE = u"        let matchedOutsideClass = 0;\n"
INCREMENT_LINE = u"          if (!CLASS_WORD_TOKENS.has(toks[qi])) matchedOutsideClass += 1;\n"
RETURN_LINE = u"        if (matched > 0 && matchedOutsideClass === 0) return;\n"
INSERTED_LINES = (COMMENT_LINE, CONST_LINE, GUARD_LINE, COUNTER_LINE,
                  INCREMENT_LINE, RETURN_LINE)

ANCHOR_FUNCTION = u"    function runGeocoderSearch(query, index){\n"
ANCHOR_TOKENS = u"      if (toks.length === 0) return [];\n"
ANCHOR_COUNTERS = (u"        let matched = 0, exactName = 0, exactNum = 0, prefix = 0,"
                   u" fuzzy = 0, matchedCore = 0, matchedViaDtk = 0, matchedViaStk = 0;\n")
ANCHOR_MATCHED = u"          matched += 1;\n"
ANCHOR_BLOCK_TYPED = u"          if (blockTyped && toks[qi] === qBlk) qBlkMatched = true;\n"
ANCHOR_SCORED = u"        if (matched > 0) {\n"
ANCHOR_DEM = u"          const dem = e.quarter_assignment_trust"
# Each pair is the anchor and the inserted line as ONE string: a line that stands
# once but inside a foreign function would keep the byte perimeter green (Astra).
ANCHORED_PAIRS = (COMMENT_LINE + CONST_LINE + ANCHOR_FUNCTION,
                  ANCHOR_TOKENS + GUARD_LINE,
                  ANCHOR_COUNTERS + COUNTER_LINE,
                  ANCHOR_MATCHED + INCREMENT_LINE + ANCHOR_BLOCK_TYPED,
                  RETURN_LINE + ANCHOR_SCORED + ANCHOR_DEM)

# A function of `initAddressSearch` the lot never touches - the byte of half 3.
UNTOUCHED_LINE = u"function dedupeDisplayRows(rows) {"

# --------------------------------------------------------------------------
# The queries, pinned by measurement at the base (план §1)
# --------------------------------------------------------------------------

RENDER_LIMIT = 10
# (query, rows the BASE draws) - the base count is asserted too, so a base that
# stops carrying the defect fails loud instead of testing nothing.
BARE_QUERIES = ((u"хотел", 5), (u"хотели", 5), (u"семеен хотел", 5), (u"апартхотел", 1))
BRIZ_QUERY = u"хотел бриз"
SHIPKA_QUERY = u"хотел шипка"
UNCHANGED_MIXED = (u"парк хотел одесос", u"хотел мак")
MAK_ROW = u"хотел мак"
BRIZ_ROW = u"хотел бриз"
BRIZ_THIRD_WORD = u"бриз"
# "хостел" left this tuple for the class-like gate of ADR 006b - pinned at zero rows.
ORDINARY_QUERIES = (u"бриз", u"парк", u"комплекс", flagship.FLAGSHIP_QUERY, u"акация 2",
                    u"ж к бриз бл в", u"с о боровец север", u"бл 307 вх 9",
                    u"левски бл 11", u"11")

# `norm` turns each of these characters into a space before the query is split.
NORM_SEPARATORS = re.compile(u"[.№,'\"-]")


# --------------------------------------------------------------------------
# Reading the two texts - inside a method, never at import
# --------------------------------------------------------------------------

def index_text(test):
    """The bytes of the candidate `index.html` (`FIRE_VARNA_INDEX_HTML_PATH` wins)."""
    if not flagship.INDEX.is_file():
        test.fail(u"липсва index.html: %s" % flagship.INDEX)
    return flagship.INDEX.read_bytes().decode("utf-8")


def tracked_text(test):
    """The TRACKED `index.html` of the repository - what the base is refused against."""
    path = flagship.REPO / "index.html"
    if not path.is_file():
        test.fail(u"липсва проследеният index.html: %s" % path)
    return path.read_bytes().decode("utf-8")


def base_text(test):
    """The blob of `<BASE>:index.html`. A dead reference is a failure, not a skip."""
    proc = subprocess.run(["git", "-C", str(flagship.REPO), "show", "%s:index.html" % BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        test.fail(u"няма блоб %s:index.html — базата е неразрешима: %s"
                  % (BASE, proc.stderr.decode("utf-8", "replace")[:300]))
    text = proc.stdout.decode("utf-8")
    if text == tracked_text(test):
        test.fail(u"base equals candidate — базата %s е равна на проследения index.html"
                  % BASE)
    return text


# --------------------------------------------------------------------------
# The two askers: the candidate through the flagship, the base through its blob
# --------------------------------------------------------------------------

def render(query):
    return {"ask": "render", "q": query, "limit": RENDER_LIMIT}


def ask_pinned_base(test, asks):
    """The same five markers, cut out of `<BASE>:index.html`, raised in the probe."""
    text = base_text(test)
    shared = flagship.cut(text, flagship.MARK_SHARED_START, flagship.MARK_SHARED_END, test)
    body = flagship.cut(text, flagship.MARK_SLICE_START, flagship.MARK_SLICE_END, test)
    if flagship.MARK_SLICE_CORE_END not in text:
        test.fail(u"липсва маркер Т12 в блоба %s: %s" % (BASE, flagship.MARK_SLICE_CORE_END))
    return flagship.run_probe(test, {"shared": shared, "slice": body,
                                     "exports": flagship.EXPORTS_QUARTER, "asks": asks},
                              quarters_path=flagship.DELIVERED)


def frozen(rows):
    """One comparable string per answer - compared, never printed."""
    return json.dumps(rows, sort_keys=True, ensure_ascii=False)


def carries(rows, needle):
    return needle in frozen(rows)


# --------------------------------------------------------------------------
# Г1 · the class words
# --------------------------------------------------------------------------

class BareClassWordTest(unittest.TestCase):

    def test_a_bare_class_word_returns_no_address_rows(self):
        asks = [render(q) for q, _ in BARE_QUERIES]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for (query, at_base), was, now in zip(BARE_QUERIES, reference, candidate):
            self.assertEqual(len(was), at_base,
                             u"базата %s вече не дава %d адресни реда за %r (дава %d) — "
                             u"пинът е мъртъв" % (BASE, at_base, query, len(was)))
            self.assertEqual(len(now), 0,
                             u"голата класова дума %r още дава %d адресни реда"
                             % (query, len(now)))

    def test_every_declared_form_is_covered(self):
        self.assertEqual(len(CLASS_WORDS), 19, u"наборът не носи деветнайсетте форми")
        self.assertEqual(len(set(CLASS_WORDS)), len(CLASS_WORDS), u"повторена форма")
        self.assertEqual(len(DERIVED_TOKENS), len(CLASS_WORDS),
                         u"производните форми не са колкото подписаните")
        asks = [render(q) for q in CLASS_WORDS]
        candidate = flagship.ask_client(self, asks)
        for query, rows in zip(CLASS_WORDS, candidate):
            self.assertEqual(len(rows), 0,
                             u"подписаната форма %r още дава %d адресни реда — "
                             u"производната латиница е сгрешена" % (query, len(rows)))

    def test_no_address_row_is_made_only_of_class_words(self):
        """The guard for FUTURE data: today no address row consists only of class
        words, so the guard hides nothing real. The day an ingest brings such a
        row in, this method turns red and the decision is reconsidered (план §9)."""
        if not flagship.ADDRESS_ROWS.is_file():
            self.fail(u"липсва %s" % flagship.ADDRESS_ROWS)
        doc = json.loads(flagship.ADDRESS_ROWS.read_bytes().decode("utf-8"))
        rows = doc["rows"] if isinstance(doc, dict) else doc
        self.assertTrue(rows, u"нула адресни реда — гейтът щеше да е вакуумен")
        words = set(CLASS_WORDS) | set(DERIVED_TOKENS)
        only_class, carrying = [], 0
        for position, row in enumerate(rows):
            label = row[0] if isinstance(row, (list, tuple)) else row
            tokens = NORM_SEPARATORS.sub(u" ", (label or u"").lower()).split()
            if not tokens:
                continue
            if any(token in words for token in tokens):
                carrying += 1
            if all(token in words for token in tokens):
                only_class.append(position)
        # A row is named by its INDEX: no address and no coordinate is printed.
        self.assertEqual(only_class, [],
                         u"адресни редове само от класови думи (по индекс): %r — "
                         u"гардът би ги скрил" % (only_class[:10],))
        self.assertTrue(carrying > 0,
                        u"нула адресни реда носят класова дума — пазачът е вакуумен")
        sys.stderr.write(u"[лот 4б] адресни реда с класова дума: %d\n" % carrying)

    def test_a_class_word_with_a_name_drops_only_the_class_only_rows(self):
        """а2: an entry that matched ONLY through class words does not qualify."""
        queries = (BRIZ_QUERY, SHIPKA_QUERY) + UNCHANGED_MIXED
        asks = [render(q) for q in queries]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        briz_was, shipka_was, odesos_was, mak_was = reference
        briz_now, shipka_now, odesos_now, mak_now = candidate

        self.assertTrue(carries(briz_was, MAK_ROW),
                        u"базата %s вече не носи %r за %r — пинът е мъртъв"
                        % (BASE, MAK_ROW, BRIZ_QUERY))
        self.assertEqual(len(briz_now), 3,
                         u"%r дава %d реда вместо трите измерени"
                         % (BRIZ_QUERY, len(briz_now)))
        self.assertTrue(briz_now[:2] == briz_was[:2],
                        u"%r: първите два реда не са байт-равни на базата %s"
                        % (BRIZ_QUERY, BASE))
        self.assertFalse(carries(briz_now, MAK_ROW),
                         u"%r още носи ред, съвпаднал само през класовата дума"
                         % BRIZ_QUERY)
        self.assertIn(BRIZ_THIRD_WORD, (briz_now[2].get("title") or u"").lower(),
                      u"%r: третият ред не е адресът на самия квартал" % BRIZ_QUERY)

        self.assertTrue(carries(shipka_was, BRIZ_ROW) and carries(shipka_was, MAK_ROW),
                        u"базата %s вече не носи хотелските редове за %r — пинът е мъртъв"
                        % (BASE, SHIPKA_QUERY))
        self.assertTrue(shipka_now[:2] == shipka_was[:2],
                        u"%r: първите два реда не са байт-равни на базата %s"
                        % (SHIPKA_QUERY, BASE))
        for needle in (BRIZ_ROW, MAK_ROW):
            self.assertFalse(carries(shipka_now, needle),
                             u"%r още носи ред, съвпаднал само през класовата дума"
                             % SHIPKA_QUERY)

        for query, was, now in zip(UNCHANGED_MIXED, (odesos_was, mak_was),
                                   (odesos_now, mak_now)):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            self.assertTrue(frozen(now) == frozen(was),
                            u"%r не е байт за байт равна на базата %s" % (query, BASE))

    def test_ordinary_queries_are_byte_equal_to_the_base(self):
        asks = [render(q) for q in ORDINARY_QUERIES]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for query, was, now in zip(ORDINARY_QUERIES, reference, candidate):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            self.assertTrue(frozen(now) == frozen(was),
                            u"заявката без класова дума %r не е байт за байт равна "
                            u"на базата %s" % (query, BASE))


# --------------------------------------------------------------------------
# Г2 · the perimeter inside index.html
# --------------------------------------------------------------------------

class PerimeterTest(unittest.TestCase):

    # The whole file is compared with the base by the DELIVERY probe
    # `gates/probe/lot_perimeter.py` (план §4 К3.5), never by a method here: such a
    # pin is true exactly once, at the delivery of this lot. What is pinned below is
    # the ANCHOR of each inserted line, which stays true for every later lot.

    def test_the_five_lines_are_the_signed_ones(self):
        candidate = index_text(self)
        for pair in ANCHORED_PAIRS:
            self.assertEqual(candidate.count(pair), 1,
                             u"двойката котва + вмъкнат ред стои %d пъти, не веднъж: %r"
                             % (candidate.count(pair), pair[:60]))
        self.assertEqual(candidate.count(u"CLASS_WORD_TOKENS"), 5,
                         u"константата се споменава %d пъти, не пет"
                         % candidate.count(u"CLASS_WORD_TOKENS"))
        declared = tuple(re.findall(r"'([a-z]+)'", CONST_LINE))
        self.assertEqual(declared, DERIVED_TOKENS,
                         u"декларацията не носи дословно производните форми")
        for word in NOT_CLASS_WORDS:
            self.assertNotIn(u"'%s'" % word, CONST_LINE,
                             u"%r е обявена за класова дума, а носи живи адресни редове"
                             % word)


# --------------------------------------------------------------------------
# Г3/Г3б/Г4 · the three negative halves - each RUNS and each FALLS
# --------------------------------------------------------------------------

def remove_once(test, text, line):
    if text.count(line) != 1:
        test.fail(u"котвата на половината стои %d пъти, не веднъж: %r"
                  % (text.count(line), line[:60]))
    return text.replace(line, u"")


def replace_once(test, text, needle, value):
    if text.count(needle) != 1:
        test.fail(u"котвата на половината стои %d пъти, не веднъж: %r"
                  % (text.count(needle), needle[:60]))
    return text.replace(needle, value)


class NegativeHalfTest(unittest.TestCase):

    def doctored(self, name, text):
        """A doctored copy of `index.html` under the temp root - never in the tree."""
        root = FIXTURES / name
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)
        path = root / "index.html"
        path.write_bytes(text.encode("utf-8"))
        return path

    def run_half(self, path, method, needle):
        environment = dict(os.environ, PYTHONIOENCODING="utf-8",
                           FIRE_VARNA_INDEX_HTML_PATH=str(path))
        proc = subprocess.run([sys.executable, "-m", "unittest", method],
                              cwd=str(flagship.REPO), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, env=environment, timeout=900)
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace")
        self.assertEqual(proc.returncode, 1,
                         u"половината не падна: изход %d\n%s"
                         % (proc.returncode, out[-800:]))
        self.assertNotIn(u"base equals candidate", out,
                         u"половината падна по грешна причина — мъртва база\n%s"
                         % out[-800:])
        self.assertIn(needle, out,
                      u"половината падна, но не по своята причина\n%s" % out[-800:])

    def test_removing_both_guards_turns_the_class_word_method_red(self):
        """ONE of the two guards is not enough: the other one covers the same query."""
        text = index_text(self)
        text = remove_once(self, text, GUARD_LINE)
        text = remove_once(self, text, RETURN_LINE)
        path = self.doctored("both_guards_gone", text)
        self.run_half(path, MODULE + ".BareClassWordTest."
                      "test_a_bare_class_word_returns_no_address_rows",
                      "test_a_bare_class_word_returns_no_address_rows")

    def test_removing_the_a2_return_turns_the_named_query_method_red(self):
        text = remove_once(self, index_text(self), RETURN_LINE)
        path = self.doctored("a2_return_gone", text)
        self.run_half(path, MODULE + ".BareClassWordTest."
                      "test_a_class_word_with_a_name_drops_only_the_class_only_rows",
                      "test_a_class_word_with_a_name_drops_only_the_class_only_rows")

    def test_a_byte_in_an_untouched_function_turns_the_perimeter_probe_red(self):
        """The half of the DELIVERY probe: one byte in a function this lot never
        touches has to turn `gates/probe/lot_perimeter.py` red, with its own reason
        and never with the refusal of a dead base."""
        text = replace_once(self, index_text(self), UNTOUCHED_LINE,
                            UNTOUCHED_LINE.replace(u") {", u")  {"))
        path = self.doctored("untouched_function_byte", text)
        allow = path.parent / "allow_lines.txt"
        # The declared rows already carry their trailing newline - written as they are.
        allow.write_bytes(u"".join(INSERTED_LINES).encode("utf-8"))
        environment = dict(os.environ, PYTHONIOENCODING="utf-8")
        proc = subprocess.run([sys.executable, "gates/probe/lot_perimeter.py",
                               "--base", BASE, "--allow", str(allow),
                               "--path", str(path)],
                              cwd=str(flagship.REPO), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, env=environment, timeout=300)
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace")
        self.assertEqual(proc.returncode, 1,
                         u"пробата не падна: изход %d\n%s"
                         % (proc.returncode, out[-800:]))
        self.assertNotIn(u"base equals candidate", out,
                         u"пробата падна по грешна причина — мъртва база\n%s"
                         % out[-800:])
        self.assertIn(u"first difference at line", out,
                      u"пробата падна, но не по своята причина\n%s" % out[-800:])


if __name__ == "__main__":
    unittest.main()
