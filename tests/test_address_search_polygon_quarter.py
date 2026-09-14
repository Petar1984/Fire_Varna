# -*- coding: utf-8 -*-
"""Lot 4в-Б - the polygon quarter finds the block (T-01).

    python -m unittest tests.test_address_search_polygon_quarter

A colleague who types "левски бл 11" got eight rows and not one of them was the
seventeen-storey block on ул. Студентска: its WRITTEN quarter says "кв. Чайка" (a
measured nearest-node artefact) while the row on the screen already reads
"кв. Левски, бл. 11", because `data/address_quarters.json` feeds the title and never
the ranking. ADR 006c widens the exception of D12 that 006a opened and 006b widened:
`runGeocoderSearch` derives, lazily and once per loaded index, the `skel` tokens of
each polygon cell name and of its parent, and one line inside `scoreEntry` lets a
query token that names the polygon count as an exact match when no indexed field
carries it. Eighty-seven buildings share the defect.

How this gate works, so that no reader has to guess:

  * The client is raised HEADLESS through the flagship's own harness
    (`tests/address_slice_probe.mjs`): the probe answers, THIS file judges. The slice
    is cut by the five markers of Т12, never by a line number.
  * The reference is not a retyped string but the SAME slice at the base commit of
    THIS lot, pinned as a LITERAL under its own environment name
    (`FIRE_VARNA_LOT4VB_BASE`) - never the merge-base and never the flagship's
    `FIRE_VARNA_BASE_COMMIT`, which moves for its own reasons. A base whose blob
    equals the TRACKED `index.html` is a dead reference and fails loud; the refusal
    compares the blob with the TRACKED file on purpose, so that a run with
    `FIRE_VARNA_INDEX_HTML_PATH` pointed at a copy of the base still fails for its
    OWN reason.
  * Every pinned base answer is asserted as well: a base that stops carrying the
    defect fails loud instead of testing nothing.
  * The class words, their derived spelling, the ordinary queries and the anchors of
    the earlier lots are IMPORTED from the lot 4б and lot 4в gates - one source of
    truth, never a second copy.
  * The declared price of ADR 006c 4в-Б-D4 is pinned here query by query, with the
    reason of each one: the corpus of thirty-three queries does not move by a byte,
    the street queries and the bare-block surface are byte-equal, and every query
    that DOES move is named with its reason and asserted to move. Since v1.1 of the
    amendment that price is a RULE and not a list: a polygon word plus "бл N" may
    only pull in entries of that cell carrying block N in `btk`. The rule is pinned
    here by the nine queries that move, by the twelve the narrowing stopped, and at
    the delivery by the sweep of 118 polygon words × {1, 5, 11} - zero queries
    lose a row that reads both the word and "бл. N".
  * Nothing is read at module level and no git runs there.
  * "Nothing else moved" is NOT a method here. The whole-file comparison is the
    DELIVERY probe `gates/probe/lot_perimeter.py`, run by hand at the gate with the
    inserted lines named on the command line: a whole-file pin is true exactly once,
    at the delivery of the lot that wrote it. What stays permanent here is the ANCHOR
    of each inserted line.
  * The three negative halves run against DOCTORED copies of `index.html` under the
    temp root - never inside the repository - and demand exit 1 plus the REASON TEXT
    of the assertion that had to fail, never the name of the method: a method name
    also stands in the traceback of an error raised BEFORE the assertion.

Ten methods: six on the queries, one on the anchors of the eight inserted lines,
three negative halves.

No coordinate, no cadastral number and no reporter name stands in this file: a
building is named by its `ord` alone (план §0.5).
"""
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import test_address_quarter_render as flagship          # noqa: E402  (module import, never *)
import test_address_search_class_words as lot4b         # noqa: E402  (one source of truth)
import test_address_search_class_like as lot4v          # noqa: E402  (one source of truth)

# The base is a LITERAL with the name of THIS lot (план §0.11): not the merge-base,
# not `FIRE_VARNA_BASE_COMMIT` and not the base of lot 4б or lot 4в.
BASE = os.environ.get("FIRE_VARNA_LOT4VB_BASE") or "c684017"

# The doctored copies of the negative halves live here - never in the tree.
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lot4vb_fixtures"

MODULE = "tests.test_address_search_polygon_quarter"

# --------------------------------------------------------------------------
# The eight inserted lines and their anchors - the perimeter of the lot
# --------------------------------------------------------------------------

STOP_COMMENT_LINE = (u"    // Type prefixes, bare numbers and the signed class "
                     u"words of a polygon name are not searchable words (ADR 006c).\n")
STOP_SET_LINE = (u"    const POLY_STOP_TOKENS = new Set(['kv','kvartal','zhk','zh','k',"
                 u"'kk','v','z','vz','s','o','so','m','mt','t','pz','zona','mestnost']);\n")
POLY_COMMENT_LINE = (u"      // The polygon quarter the row already displays becomes "
                     u"searchable for an explicit \"бл N\" query (ADR 006c).\n")
POLY_CELL_LINE = (u"      const polyCell = (quarterIndex && quarterIndex.entry_cell && "
                  u"qBlk !== null && !bareBlockTyped) ? quarterIndex.entry_cell : null;\n")
LAZY_LINE = (u"      if (polyCell && !index._polyToks) { index._polyToks = "
             u"quarterIndex.names.map(function (n, ci) { const s = new Set(); "
             u"norm(n + ' ' + (quarterIndex.parents[ci] || '')).split(/\\s+/)"
             u".forEach(function (w) { const t = skel(w); if (t && "
             u"!/^[0-9]+$/.test(t) && !POLY_STOP_TOKENS.has(t) && "
             u"!CLASS_WORD_TOKENS.has(t)) s.add(t); }); "
             u"return s; }); }\n")
BY_CELL_LINE = u"      const polyToksByCell = polyCell ? index._polyToks : null;\n"
POLY_TOKS_LINE = (u"        const polyToks = (polyToksByCell !== null && "
                  u"typeof e._ord === 'number' && polyCell[e._ord] >= 0 && "
                  u"(e.btk || []).includes(qBlk)) ? "
                  u"(polyToksByCell[polyCell[e._ord]] || null) : null;\n")
VIRTUAL_MATCH_LINE = (u"          if (best === 0 && polyToks !== null && "
                      u"polyToks.has(toks[qi])) best = 3;\n")
INSERTED_LINES = (STOP_COMMENT_LINE, STOP_SET_LINE, POLY_COMMENT_LINE, POLY_CELL_LINE,
                  LAZY_LINE, BY_CELL_LINE, POLY_TOKS_LINE, VIRTUAL_MATCH_LINE)

# 4в-Б-D3 (v1.1) - the entry condition: the polygon tokens reach only an entry whose
# `btk` carries the typed block. Negative half 2 removes exactly this expression. The
# restrictor of D3 ("бл N" typed, plus one more word) stays in the code as the cheap
# early exit - it keeps a query without a block from building `index._polyToks` at all -
# but under the entry condition it no longer shows in the output (409 queries measured,
# not one differs without it), so it cannot carry a half. The expression also stands in
# the untouched `bmatch` line of the comparator, so the half doctors the inserted line
# through its own anchor, never the bare expression.
BLOCK_CONDITION = u" && (e.btk || []).includes(qBlk)"

ANCHOR_FIELDS = (u"        const tk = e.tk || [], qtk = e.qtk || null, atk = e.alias_tk "
                 u"|| null, dtk = e.dtk || null, stk = e.stk || null;\n")
ANCHOR_LOOP = u"        for (let qi = 0; qi < toks.length; qi++) {\n"
ANCHOR_STK = (u"          if (stk && best < 3) { for (let ti = 0; ti < stk.length; ti++) "
              u"{ const k = m[stk[ti]]||0; if (k > best) { best = k; matchedViaStk += 1; "
              u"if (best === 3) break; } } }\n")
ANCHOR_ZERO = u"          if (best === 0) { all = false; continue; }\n"
# Each pair is the anchor and the inserted lines as ONE string: a line that stands once
# but inside a foreign function would keep a bare byte perimeter green (Astra).
ANCHORED_PAIRS = (STOP_COMMENT_LINE + STOP_SET_LINE + lot4b.COMMENT_LINE,
                  lot4v.CLASS_LIKE_LINE + POLY_COMMENT_LINE + POLY_CELL_LINE
                  + LAZY_LINE + BY_CELL_LINE,
                  ANCHOR_FIELDS + POLY_TOKS_LINE + ANCHOR_LOOP,
                  ANCHOR_STK + VIRTUAL_MATCH_LINE + ANCHOR_ZERO)
# `polyToks` stands in the three code lines that use it and inside `polyToksByCell` and
# `index._polyToks` - measured on the delivered file, never guessed.
POLYTOKS_MENTIONS = 9
# The name the inserted lines must NOT carry: lot 4в pins `classLike` at two mentions.
# `CLASS_WORD_TOKENS` left this tuple with the knowledge of the signature (план v1.2):
# the lazy builder names it on purpose, because ADR 006c 4в-Б-D2 keeps the class words
# OUT of the polygon tokens - the pin of lot 4б counts six mentions now, not five.
FOREIGN_NAMES = (u"classLike",)

# --------------------------------------------------------------------------
# The queries, pinned by measurement at the base (план §1, ADR 006c 4в-Б-D4)
# --------------------------------------------------------------------------

SEARCH_LIMIT = 20
# The block on ул. Студентска: `ord` only - no street row, no coordinate, no cadastre.
TARGET_ORD = 49241
# The other row that reads "кв. Левски, бл. 11": the declared price of 4в-Б-D4 (а) -
# two rows with one title until the street enters the label (an index-side option).
TWIN_ORD = 32777
FINDER_QUERY = u"левски бл 11"
# The eight rows the BASE draws for it, in order: the pin is dead the day they change.
FINDER_AT_BASE = (4137, 6893, 32777, 2461, 33342, 47490, 6891, 33236)

# Byte-equal by construction and by measurement (4в-Б-D3): the street queries, the
# flagship's own query and the bare-block surface.
STREET_QUERIES = (u"студентска 11", u"бл 11 студентска", flagship.FLAGSHIP_QUERY, u"бл 11")
# Byte-equal by measurement as well: the bare quarter words and the quarter+block
# queries whose polygon word already stands in an indexed field.
UNMOVED_QUERIES = (u"чайка бл 11", u"левски", u"чайка", u"младост бл 100", u"левски 11")

# 4в-Б-D4 (v1.1) - the queries the narrowing of K3c stopped: seven "deltas" of plan
# v1.2 that no longer happen because the cell holds no such block, and the Auditor's
# own price queries, where K3b traded block rows for street numbers. Byte-equal now.
NARROWED_QUERIES = (u"бриз бл 5", u"аспарухово бл 11", u"изгрев бл 7", u"гара бл 1",
                    u"болница бл 1", u"мол бл 1", u"площад бл 1", u"погреби бл 1",
                    u"погреби бл 5", u"гранд бл 5", u"махала бл 5", u"автогара бл 5")

# 4в-Б-D4 - the signed list of deltas, query by query with its reason. Every query below
# is asserted to MOVE: a price that stops being paid is a dead pin too. Since v1.1 of the
# amendment the price is a RULE, not a list: a polygon word plus "бл N" may only pull in
# entries of that cell that carry block N in `btk`. These nine are a SAMPLE of the rule -
# the sweep of every polygon word at delivery judges the rule itself.
SIGNED_DELTAS = (
    (FINDER_QUERY,
     u"печалбата: блокът на ул. Студентска (ord 49241) влиза на първо място"),
    (u"левски студентска бл 11",
     u"печалбата: 49241 пръв, после серията Студентска бл. 12/13/14"),
    (u"хеи бл 11",
     u"печалбата: редовете на ХЕИ вместо случайни от Аспарухово - името ХЕИ го няма "
     u"в речника, точното сравнение го заобикаля"),
    (u"левски бл 3",
     u"цената: блокове от подклетки с родител кв. Левски (Базар Левски, Цветен "
     u"квартал) влизат в опашката"),
    (u"кино бл 1",
     u"цената по 4в-Б-D4 (в): родовата дума в име на клетка (Зимно кино Тракия) става "
     u"търсима за блокова заявка"),
    (u"пристанище бл 1",
     u"цената по 4в-Б-D4 (в): родовата дума в име на клетка (Пристанище Варна) става "
     u"търсима за блокова заявка"),
    (u"стадион бл 1",
     u"цената по 4в-Б-D4 (в): родовата дума в име на клетка (Стадион Спартак) става "
     u"търсима за блокова заявка"),
    (u"бизнес бл 5",
     u"цената по 4в-Б-D4 (в): клетката Бизнес хотел влиза през РОДОВАТА си дума "
     u"(бизнес), не през класовата - класовата е изключена от полигонните токени"),
    (u"левски 1 бл 11",
     u"цената: Цветен квартал, бл. 11 минава пред кв. Левски, бл. 11 - Цветен квартал "
     u"е подклетка с родител кв. Левски"),
)
# The corpus of thirty-three queries: ZERO deltas measured. A query that moves without
# standing here is exactly what план §7 STOP-11 forbids.
CORPUS_DELTAS = ()

# 4в-Б-D4 - five buildings of the eighty-seven-strong family, each with a different
# block number, written "Чайка" and standing inside the Левски polygon: absent from the
# base answer, present in the candidate one.
FAMILY = ((u"левски бл 11", 49241), (u"левски бл 12", 49243), (u"левски бл 13", 49245),
          (u"левски бл 9", 33015), (u"левски бл 10", 32948))

# Lots 4б and 4в keep their words: the rows each query draws, measured on both sides.
# The last two are the Auditor's finding of 14.09: before v1.2 a class word plus a
# block number returned six addresses of the "Бизнес хотел" cell, because the lot 4б
# guard fires only for an ALL-class query. With the class set out of the polygon
# tokens they are byte-equal to the base again - measured, not assumed.
CLASS_WORD_ROWS = ((u"хотел", 0), (u"хотели", 0), (u"хот", 0), (u"хоте", 0),
                   (u"хостел", 0), (u"апар", 0), (u"бизнес", 1),
                   (u"хотел бл 5", 8), (u"хотел бл 11", 7))
# 4в-Б-D5: "левски бл 11" leaves the ordinary queries of lot 4б and is pinned above.
ORDINARY_AFTER_THE_RESET = 9

# The needles of the negative halves: the REASON TEXT of the assertion that must fail.
NEEDLE_FINDER = u"още не носи ord"
NEEDLE_NARROWED = u"заявката без полигонна печалба"


# --------------------------------------------------------------------------
# Reading the two texts - inside a method, never at import
# --------------------------------------------------------------------------

def base_text(test):
    """The blob of `<BASE>:index.html`. A dead reference is a failure, not a skip."""
    proc = subprocess.run(["git", "-C", str(flagship.REPO), "show", "%s:index.html" % BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        test.fail(u"няма блоб %s:index.html — базата е неразрешима: %s"
                  % (BASE, proc.stderr.decode("utf-8", "replace")[:300]))
    text = proc.stdout.decode("utf-8")
    if text == lot4b.tracked_text(test):
        test.fail(u"base equals candidate — базата %s е равна на проследения index.html"
                  % BASE)
    return text


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


def search(query):
    return {"ask": "search", "q": query, "limit": SEARCH_LIMIT}


def ords(answer):
    return tuple(row["ord"] for row in answer["rows"])


# --------------------------------------------------------------------------
# Г1 · the block is found and the declared price is the signed one
# --------------------------------------------------------------------------

class PolygonQuarterTest(unittest.TestCase):

    def test_the_polygon_quarter_finds_the_block(self):
        asks = [search(FINDER_QUERY)]
        was = ask_pinned_base(self, asks)[0]
        now = flagship.ask_client(self, asks)[0]
        self.assertEqual(ords(was), FINDER_AT_BASE,
                         u"базата %s вече не дава осемте измерени реда за %r — "
                         u"пинът е мъртъв" % (BASE, FINDER_QUERY))
        self.assertNotIn(TARGET_ORD, ords(was),
                         u"базата %s вече носи ord %d за %r — пинът е мъртъв"
                         % (BASE, TARGET_ORD, FINDER_QUERY))
        self.assertIn(TARGET_ORD, ords(now),
                      u"заявката %r още не носи ord %d — блокът на ул. Студентска "
                      u"не се излъчва" % (FINDER_QUERY, TARGET_ORD))
        self.assertEqual(ords(now)[0], TARGET_ORD,
                         u"ord %d не е на измерената първа позиция за %r, а на %d"
                         % (TARGET_ORD, FINDER_QUERY, ords(now).index(TARGET_ORD)))
        # 4в-Б-D4 (а): the declared price - both rows read "кв. Левски, бл. 11".
        self.assertIn(TWIN_ORD, ords(now),
                      u"ord %d излезе от отговора за %r — обявената цена е друга"
                      % (TWIN_ORD, FINDER_QUERY))

    def test_the_street_queries_are_byte_equal(self):
        queries = (tuple(STREET_QUERIES) + tuple(UNMOVED_QUERIES)
                   + tuple(NARROWED_QUERIES))
        asks = [lot4b.render(query) for query in queries]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for query, was, now in zip(queries, reference, candidate):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            self.assertTrue(lot4b.frozen(now) == lot4b.frozen(was),
                            u"заявката без полигонна печалба %r не е байт за байт равна "
                            u"на базата %s" % (query, BASE))

    def test_the_corpus_deltas_are_the_signed_list(self):
        corpus = list(flagship.corpus_doc(self)["queries"])
        self.assertEqual(len(corpus), 33,
                         u"корпусът носи %d заявки, не 33 — мярката на §1 е друга"
                         % len(corpus))
        declared = dict(CORPUS_DELTAS)
        queries = corpus + [query for query, _ in SIGNED_DELTAS]
        asks = [lot4b.render(query) for query in queries]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        head = len(corpus)
        for query, was, now in zip(corpus, reference[:head], candidate[:head]):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            moved = lot4b.frozen(now) != lot4b.frozen(was)
            if query in declared:
                self.assertTrue(moved,
                                u"корпусната заявка %r е обявена за променена (%s), а не "
                                u"мърда — пинът е мъртъв" % (query, declared[query]))
            else:
                self.assertFalse(moved,
                                 u"корпусната заявка %r се промени, а не е в подписания "
                                 u"списък" % query)
        for (query, reason), was, now in zip(SIGNED_DELTAS, reference[head:],
                                             candidate[head:]):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            self.assertTrue(lot4b.frozen(now) != lot4b.frozen(was),
                            u"обявената делта %r (%s) вече не се случва — пинът е мъртъв"
                            % (query, reason))

    def test_the_family_is_reachable(self):
        asks = [search(query) for query, _ in FAMILY]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for (query, ordinal), was, now in zip(FAMILY, reference, candidate):
            self.assertNotIn(ordinal, ords(was),
                             u"базата %s вече носи ord %d за %r — пинът е мъртъв"
                             % (BASE, ordinal, query))
            self.assertIn(ordinal, ords(now),
                          u"сграда от семейството (ord %d) още не се намира по %r"
                          % (ordinal, query))

    def test_the_ordinary_queries_minus_the_one_that_moved(self):
        self.assertEqual(len(lot4b.ORDINARY_QUERIES), ORDINARY_AFTER_THE_RESET,
                         u"обикновените заявки на 4б са %d, не %d — пренастройката на "
                         u"006c е разместена" % (len(lot4b.ORDINARY_QUERIES),
                                                 ORDINARY_AFTER_THE_RESET))
        self.assertNotIn(FINDER_QUERY, lot4b.ORDINARY_QUERIES,
                         u"%r още стои в ORDINARY_QUERIES на 4б, а е пинована тук"
                         % FINDER_QUERY)
        asks = [lot4b.render(query) for query in lot4b.ORDINARY_QUERIES]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for query, was, now in zip(lot4b.ORDINARY_QUERIES, reference, candidate):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            self.assertTrue(lot4b.frozen(now) == lot4b.frozen(was),
                            u"обикновената заявка %r не е байт за байт равна на базата %s"
                            % (query, BASE))

    def test_the_class_words_still_own_their_words(self):
        """A regression pin, green at the base as well (план §4 К3.2, метод 6): the
        polygon rule REFUSES the class set when it derives its tokens (4в-Б-D2), so 4б
        and 4в keep their numbers and a class word with a block number stays put."""
        asks = [lot4b.render(query) for query, _ in CLASS_WORD_ROWS]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for (query, rows_measured), was, now in zip(CLASS_WORD_ROWS, reference, candidate):
            self.assertEqual(len(was), rows_measured,
                             u"базата %s вече дава %d реда за %r, не %d — пинът е мъртъв"
                             % (BASE, len(was), query, rows_measured))
            self.assertEqual(len(now), rows_measured,
                             u"класовата заявка %r дава %d реда вместо измерените %d"
                             % (query, len(now), rows_measured))
            self.assertTrue(lot4b.frozen(now) == lot4b.frozen(was),
                            u"класовата заявка %r не е байт за байт равна на базата %s"
                            % (query, BASE))


# --------------------------------------------------------------------------
# Г2 · the perimeter inside index.html
# --------------------------------------------------------------------------

class PerimeterTest(unittest.TestCase):

    # The whole file is compared with the base by the DELIVERY probe
    # `gates/probe/lot_perimeter.py`, never by a method here: such a pin is true exactly
    # once, at the delivery of this lot. What is pinned below is the ANCHOR of each
    # inserted line, which stays true for every later lot.

    def test_the_eight_lines_are_the_signed_ones(self):
        candidate = lot4b.index_text(self)
        for pair in ANCHORED_PAIRS:
            self.assertEqual(candidate.count(pair), 1,
                             u"двойката котва + вмъкнати редове стои %d пъти, не веднъж: "
                             u"%r" % (candidate.count(pair), pair[:60]))
        self.assertEqual(candidate.count(u"polyToks"), POLYTOKS_MENTIONS,
                         u"`polyToks` се споменава %d пъти, не %d"
                         % (candidate.count(u"polyToks"), POLYTOKS_MENTIONS))
        for name in FOREIGN_NAMES:
            for line in INSERTED_LINES:
                self.assertNotIn(name, line,
                                 u"вмъкнат ред споменава %r — ADR 006c 4в-Б-D2 го "
                                 u"забранява" % name)
        # The pairs of lot 4б and lot 4в still stand once each: this lot inserted around
        # them, never between an earlier anchor and its own line.
        for pair in lot4b.ANCHORED_PAIRS:
            self.assertEqual(candidate.count(pair), 1,
                             u"двойка на лот 4б стои %d пъти, не веднъж: %r"
                             % (candidate.count(pair), pair[:60]))
        for pair in lot4v.ANCHORED_PAIRS:
            self.assertEqual(candidate.count(pair), 1,
                             u"двойка на лот 4в стои %d пъти, не веднъж: %r"
                             % (candidate.count(pair), pair[:60]))


# --------------------------------------------------------------------------
# Г3 · the three negative halves - each RUNS and each FALLS
# --------------------------------------------------------------------------

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
        """The needle is the REASON TEXT of the assertion that has to fail, never the
        name of the method: the name also stands in the traceback of an ImportError
        raised long before the assertion."""
        self.assertTrue(path.is_file(), u"копието на половината липсва: %s" % path)
        environment = dict(os.environ, PYTHONIOENCODING="utf-8",
                           FIRE_VARNA_INDEX_HTML_PATH=str(path),
                           FIRE_VARNA_LOT4VB_BASE=BASE)
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

    def test_removing_the_virtual_match_turns_the_finder_red(self):
        """Without the one line inside `scoreEntry` the block stays invisible: measured
        on the copy before the half was written (план §4 Ф0.10)."""
        text = lot4b.remove_once(self, lot4b.index_text(self), VIRTUAL_MATCH_LINE)
        path = self.doctored("virtual_match_gone", text)
        self.run_half(path, MODULE + ".PolygonQuarterTest."
                      "test_the_polygon_quarter_finds_the_block", NEEDLE_FINDER)

    def test_removing_the_block_condition_turns_the_byte_equal_method_red(self):
        """Without the entry condition the polygon tokens reach every entry of the cell
        and the narrowed queries move again ("погреби бл 5" trades its block rows for
        street numbers) - the behaviour of K3b, measured."""
        text = lot4b.replace_once(self, lot4b.index_text(self), POLY_TOKS_LINE,
                                  POLY_TOKS_LINE.replace(BLOCK_CONDITION, u""))
        path = self.doctored("block_condition_gone", text)
        self.run_half(path, MODULE + ".PolygonQuarterTest."
                      "test_the_street_queries_are_byte_equal", NEEDLE_NARROWED)

    def test_a_byte_in_an_untouched_function_turns_the_delivery_probe_red(self):
        """The half of the DELIVERY probe: one byte in a function this lot never touches
        has to turn `gates/probe/lot_perimeter.py` red, with its own reason and never
        with the refusal of a dead base."""
        text = lot4b.replace_once(self, lot4b.index_text(self), lot4b.UNTOUCHED_LINE,
                                  lot4b.UNTOUCHED_LINE.replace(u") {", u")  {"))
        path = self.doctored("untouched_function_byte", text)
        allow = path.parent / "allow_lines.txt"
        # The declared rows already carry their trailing newline - written as they are.
        allow.write_bytes(u"".join(INSERTED_LINES).encode("utf-8"))
        self.assertTrue(path.is_file() and allow.is_file(),
                        u"копието или allow-файлът на половината липсва: %s" % path.parent)
        environment = dict(os.environ, PYTHONIOENCODING="utf-8",
                           FIRE_VARNA_LOT4VB_BASE=BASE)
        proc = subprocess.run([sys.executable, "gates/probe/lot_perimeter.py",
                               "--base", BASE, "--allow", str(allow),
                               "--path", str(path)],
                              cwd=str(flagship.REPO), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, env=environment, timeout=300)
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace")
        self.assertEqual(proc.returncode, 1,
                         u"пробата не падна: изход %d\n%s" % (proc.returncode, out[-800:]))
        self.assertNotIn(u"base equals candidate", out,
                         u"пробата падна по грешна причина — мъртва база\n%s" % out[-800:])
        self.assertIn(u"first difference at line", out,
                      u"пробата падна, но не по своята причина\n%s" % out[-800:])


if __name__ == "__main__":
    unittest.main()
