# -*- coding: utf-8 -*-
"""Lot 5 - the entrances open under the building (T-01).

    python -m unittest tests.test_address_entrances_under_building

A colleague who types "бл 408" saw the building and вх. 1 to 9 and nothing else,
while the block has twenty-three entrances: `runGeocoderSearch` already groups a
parent with its children, `projectRow` flattens them into one list and
`renderResults` draws that flat list up to `RESULT_LIMIT`. ADR 012 folds the
children AT DRAWING TIME only: the ranked rows, `dedupeDisplayRows`,
`buildExactItem` and `currentResults` stay byte-equal, so not one pinned answer of
the flagship or of the four foreign gates moves.

How this gate works, so that no reader has to guess:

  * The client is raised HEADLESS through the flagship's own harness
    (`tests/address_slice_probe.mjs`): the probe answers, THIS file judges. The
    slice is cut by the five markers of Т12, never by a line number.
  * The whole lot is INVISIBLE to every other gate we own: they render through
    `buildExactItem` directly, `renderResults` never runs in them and both click
    handlers sit outside the lifted slice. That is why the probe grew one ask of
    its own, `renderList` (ADR 012 D7, commit К3a), and why this file drives it:
    without it a green suite would prove nothing about the feature.
  * The reference is the SAME slice at the base commit of THIS lot, pinned as a
    LITERAL under its own environment name (`FIRE_VARNA_LOT5_BASE`) - never the
    merge-base, never the flagship's `FIRE_VARNA_BASE_COMMIT` and never the base of
    lot 4б, 4в or 4в-Б. A base whose blob equals the TRACKED `index.html` is a dead
    reference and fails loud; the refusal compares the blob with the TRACKED file on
    purpose, so a run with `FIRE_VARNA_INDEX_HTML_PATH` pointed at a copy of the
    base still fails for its OWN reason.
  * Every pinned BASE answer is asserted as well: a base that stops carrying the
    defect fails loud instead of testing nothing.
  * The pinned queries of the four foreign gates are IMPORTED from them, never
    copied: one source of truth for the hundred and thirty queries method 8 proves
    byte-equal.
  * The counter and the strip are judged against `data/search_index.json` itself,
    because the DRAWN rows lie: "студентска бл 14" draws five children while the
    index holds ten.
  * Nothing is read at module level and no git runs there.
  * The three negative halves run against DOCTORED copies of `index.html` under the
    temp root - never inside the repository - and demand exit 1 plus the REASON TEXT
    of the assertion that had to fail, never the name of the method: a method name
    also stands in the traceback of an error raised BEFORE the assertion. Each
    redness was MEASURED before the half was written (план §4 Ф0.7).

Twelve bodies: eight on the behaviour, one on the anchors of the five inserted
blocks, three negative halves.

No coordinate, no cadastral number and no reporter name stands in this file: a
building is named by its `ord` or by its title alone (план §0.5). The group key is
read out of the index at runtime, never typed here.
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import test_address_quarter_render as flagship          # noqa: E402  (module import, never *)
import test_address_search_class_words as lot4b         # noqa: E402  (one source of truth)
import test_address_search_class_like as lot4v          # noqa: E402  (one source of truth)
import test_address_search_polygon_quarter as lot4vb    # noqa: E402  (one source of truth)

# The base is a LITERAL with the name of THIS lot (plan §0.11).
BASE = os.environ.get("FIRE_VARNA_LOT5_BASE") or "134039c"

# The doctored copies of the negative halves live here - never in the tree.
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lot5" / "fixtures"

MODULE = "tests.test_address_entrances_under_building"

# `renderResults` is the function under test; `foldState`, `drawFoldedList` and
# `currentResults` are how the probe opens one strip along the badge's own path,
# without a click the stub cannot fire (ADR 012 D7).
EXPORTS = flagship.EXPORTS_QUARTER + ["renderResults", "foldState",
                                      "drawFoldedList", "currentResults"]

SEARCH_LIMIT = 20
RENDER_LIMIT = 10
LIST_LIMIT = 30

# --------------------------------------------------------------------------
# The five inserted blocks and their anchors - the perimeter of the lot (plan R9)
# --------------------------------------------------------------------------

# Each pair is the untouched ANCHOR line plus the first inserted line as ONE string:
# a line that stands once but in a foreign place would keep a bare byte perimeter
# green (Astra). All five are absent from the base by construction.
PAIR_CSS = (u"  .asr-status { padding: 10px 12px; color: #777; font-size: 13px; }\n"
            u"  /* --- Lot 5 / ADR 012: a building is ONE row with an entrance counter;\n")
PAIR_STATE = (u"    let currentResults = [];\n"
              u"    // Lot 5 / ADR 012 D5 - `query` is the text the DRAWN list was built "
              u"from, `open`\n")
PAIR_FUNCTIONS = (u"    // IB1 address slice core end\n"
                  u"    // ===================================================================\n"
                  u"    // Lot 5 / ADR 012 - entrance folding. Everything here is ADDITIVE:\n")
PAIR_RENDER = (u"      appendExactHeader(frag, rows);\n"
               u"      // Lot 5 / ADR 012 D2 - a building draws as ONE row plus (when open) "
               u"its strip.\n")
# The chip listener is inserted BEFORE the delivered one, so its pair is the last
# inserted line joined to the two anchor lines that follow it.
PAIR_LISTENER = (u"      return;\n"
                 u"    });\n"
                 u"    resultsEl.addEventListener('click', function (ev) {\n"
                 u"      const item = ev.target.closest('.asr-item');\n")
ANCHORED_PAIRS = (PAIR_CSS, PAIR_STATE, PAIR_FUNCTIONS, PAIR_RENDER, PAIR_LISTENER)

# The five new functions of ADR 012 D1, by signature.
NEW_SIGNATURES = (u"function typedEntranceQuery", u"function entrancesByGroup",
                  u"function entranceRow", u"function buildEntranceStrip",
                  u"function drawFoldedList")
# The functions of ADR 012 D8 that stay untouched - each still declared exactly once.
UNTOUCHED_SIGNATURES = (u"function dedupeDisplayRows", u"function buildExactItem",
                        u"function renderResults(rows) {")
# The new selector family, counted on the delivered file (plan §5, gate G2b).
ENT_MENTIONS = 8
# Absent from the WHOLE file, not from the inserted lines alone. The first two are
# the declared deviations from the specimen (plan §4, anchor 1): neither the name
# nor the rule ever shipped. The last two are the two scroll arrows of ADR 012 v1.1:
# they came OUT in lot 5в on Petar's word (plan §11), because on his phone an arrow
# lay over a chip - a silent return of either name has to fail here.
BANNED_IN_FILE = (u"ENT_STRIP_FADE_AFTER", u".asr-ent-chip.active",
                  u"ENT_STRIP_ARROWS_AFTER", u"asr-ent-arrow")
# Absent from the lot's OWN inserted lines. The whole file cannot be judged here: the
# two vendored minified bundles carry "prototype" of their own, and they stand in the
# base as well - an added line is one that the base does not carry at all.
BANNED_IN_ADDED = (u"prototype", u"Variant A1")

# --------------------------------------------------------------------------
# The three lines the negative halves doctor (each measured red in F0.7)
# --------------------------------------------------------------------------

HOOK_LINES = (
    u"      // Lot 5 / ADR 012 D2 - a building draws as ONE row plus (when open) its strip.\n"
    u"      // A NEW query text closes any open strip, and so does a list that was HIDDEN in\n"
    u"      // between: otherwise the same query typed again would come back already open,\n"
    u"      // without anybody having tapped the badge.\n"
    u"      if (foldState.query !== inputEl.value || "
    u"!resultsEl.classList.contains('visible')) {\n"
    u"        foldState.query = inputEl.value; foldState.open = null;\n"
    u"      }\n"
    u"      const foldedFrag = drawFoldedList(rows, foldState.query);\n"
    u"      if (foldedFrag) { resultsEl.replaceChildren(foldedFrag); "
    u"resultsEl.classList.add('visible'); return; }\n")
COUNTER_LINE = u"        const n = (byG.get(g) || []).length;\n"
COUNTER_FROM_ROWS = (u"        const n = rows.filter(function (rr) { return rr && rr.en != null"
                     u" && rr.g != null && String(rr.g) === g; }).length;\n")
GUARD_LINE = (u"      if (typedEntranceQuery(queryText)) return null;   "
              u"// an explicit entrance query is never folded\n")

# The needles of the halves: the REASON TEXT of the assertion that must fail, with
# the measured numbers kept OUT of the constant.
NEEDLE_ONE_ROW = u"сградата още не е един ред"
NEEDLE_COUNTER = u"броячът каза"
NEEDLE_TYPED = u"заявката с изписан вход се сгъна"

# --------------------------------------------------------------------------
# The queries, pinned by measurement at the base (plan §1, F0.2, F0.7)
# --------------------------------------------------------------------------

# BLOCK_QUERY - the maximum: one building and twenty-three entrances. The base draws
# ten rows, of which nine are entrances; the candidate draws ONE row with a counter.
BLOCK_QUERY = u"бл 408"
BLOCK_ORD = 37332
BLOCK_ENTRANCES = 23
BLOCK_ROWS_AT_BASE = 10
BLOCK_ENTRANCE_ROWS_AT_BASE = 9
# Its strip, measured chip by chip: twenty-three numbered entrances, 1 to 23.
BLOCK_CHIPS = tuple(u"вх. %d" % number for number in range(1, BLOCK_ENTRANCES + 1))

# The counter comes from the INDEX, never from the drawn rows (ADR 012 D4): these two
# are the measured witnesses of the lie - five drawn against ten, six against nine.
COUNTER_QUERY, COUNTER_ORD, COUNTER_DRAWN_AT_BASE = u"студентска бл 14", 49248, 5
SECOND_COUNTER_QUERY, SECOND_COUNTER_ORD, SECOND_DRAWN_AT_BASE = u"студентска бл 3", 49260, 6
# A group with exactly one entrance: the badge takes the singular form below.
SINGULAR_QUERY, SINGULAR_ORD = u"долина бл 3", 2346
SINGULAR_BADGE = u"1 вход"
# A CORNER building: two of its entrances carry the same letter on two different
# streets (forty-two such pairs, up to ~145 m apart). Every indexed entrance gets its
# own chip - folding them by the letter lost a real entrance and sent its chip to the
# neighbouring number, which is what audit pass 1 measured.
CORNER_QUERY, CORNER_ORD = u"генерал колев 16", 56617
CORNER_REPEATED_LETTER, CORNER_REPEATS = u"А", 2

# A query that spells an entrance is never folded and never gets a badge (rule 4).
# TYPED_WITNESS is the only one of the three that CAN fold - the other two draw
# entrances alone, with no building row to fold them under (R1 finding 2).
TYPED_QUERIES = (u"бл 408 вх 12", u"студентска бл 14 вх а", u"бл 307 вх 9")
TYPED_WITNESS = u"бл 307 вх 9"

# The other results stay visible: the bare surface refills the freed places, a narrow
# query does NOT (the honest price of ADR 012 D2, pinned so it cannot move silently).
BARE_QUERY, BARE_TOP_LEVEL_ROWS = u"бл 11", 10
PRICE_QUERY, PRICE_ROWS, PRICE_ROWS_AT_BASE = u"погреби бл 5", 2, 7
PRICE_ORD = 2452
PRICE_FIRST_BADGE = u"5 входа"

# An entrance whose parent is NOT on the list keeps its own row (rule 3). Both are
# NON-typed queries with an orphan among foldable rows (R2 finding 3).
ORPHAN_QUERIES = ((u"бриз бл 5", 32616, 8, 8), (u"гара бл 1", 39824, 6, 7))

# An entrance drawn BEFORE its parent keeps its row and the parent's strip repeats it
# (rule 2, the measured case of Astra point 4).
BEFORE_QUERY = u"10 бл 104"
BEFORE_ENTRANCE_ORD, BEFORE_PARENT_ORD = 34209, 34208
BEFORE_BADGE, BEFORE_CHIP = u"12 входа", u"вх. 10"
# The natural order of that strip, measured: a suffixed number follows its own number
# and not the whole run of numbers, which is what a plain string sort would do.
BEFORE_CHIPS = (u"вх. 1", u"вх. 1А", u"вх. 2", u"вх. 3", u"вх. 4", u"вх. 5", u"вх. 6",
                u"вх. 7", u"вх. 7А", u"вх. 8", u"вх. 9", u"вх. 10")

# The rows of an entrance carry this class in the kind chip - how a drawn row says
# "I am an entrance" without a coordinate or a cadastral number.
ENTRANCE_KIND = u"asr-kind entrance"
CHIP_PREFIX = u"вх. "

DATA_IDX = re.compile(u"data-idx=\"(\\d+)\"")


# --------------------------------------------------------------------------
# Reading the two texts - inside a method, never at import
# --------------------------------------------------------------------------

def index_text(test):
    """The bytes of the candidate `index.html` (`FIRE_VARNA_INDEX_HTML_PATH` wins)."""
    return lot4b.index_text(test)


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


def slices(test, text):
    """The two cuts of Т12, out of whichever text is handed in."""
    shared = flagship.cut(text, flagship.MARK_SHARED_START, flagship.MARK_SHARED_END, test)
    body = flagship.cut(text, flagship.MARK_SLICE_START, flagship.MARK_SLICE_END, test)
    if flagship.MARK_SLICE_CORE_END not in text:
        test.fail(u"липсва маркер Т12: %s" % flagship.MARK_SLICE_CORE_END)
    return shared, body


def ask_candidate(test, asks):
    shared, body = slices(test, index_text(test))
    return flagship.run_probe(test, {"shared": shared, "slice": body,
                                     "exports": EXPORTS, "asks": asks},
                              quarters_path=flagship.DELIVERED)


def ask_pinned_base(test, asks):
    """The same five markers, cut out of `<BASE>:index.html`. The base slice has no
    `foldState`, so no ask handed here may carry `open`."""
    shared, body = slices(test, base_text(test))
    return flagship.run_probe(test, {"shared": shared, "slice": body,
                                     "exports": EXPORTS, "asks": asks},
                              quarters_path=flagship.DELIVERED)


# --------------------------------------------------------------------------
# The asks and small readers
# --------------------------------------------------------------------------

def search(query):
    return {"ask": "search", "q": query, "limit": SEARCH_LIMIT}


def render(query):
    return {"ask": "render", "q": query, "limit": RENDER_LIMIT}


def drawn(query, open_group=None):
    ask = {"ask": "renderList", "q": query, "limit": LIST_LIMIT}
    if open_group is not None:
        ask["open"] = open_group
    return ask


def badges(answer):
    return [row["badge"] for row in answer["rows"] if row["badge"]]


def strips(answer):
    return [row["chips"] for row in answer["rows"] if row["chips"]]


def htmls(answer):
    return [row["html"] for row in answer["rows"]]


def entrance_rows(answer):
    return [row for row in answer["rows"] if ENTRANCE_KIND in row["html"]]


def idx_of(row):
    """The `data-idx` a drawn row carries - its position in `currentResults` (D9)."""
    hit = DATA_IDX.search(row["html"])
    return int(hit.group(1)) if hit else None


def added_lines(candidate, base):
    """The lines the lot inserted: every line of the candidate that the base does not
    carry at all. Coarse on purpose - it needs no diff and it cannot miss a new line."""
    known = set(base.split(u"\n"))
    return [line for line in candidate.split(u"\n") if line not in known]


def counted(entries, group):
    """The ords of EVERY entrance the index knows for `group`, in index order.

    Nothing is de-duplicated here either: a corner building carries two entrances with
    the same letter and both belong on the strip. The ORDER the strip draws is not
    recomputed in this file - a second copy of the comparator would only ever agree
    with itself; the order is pinned by measurement instead.
    """
    return [i for i, e in enumerate(entries)
            if e.get("en") is not None and e.get("g") is not None
            and str(e["g"]) == str(group)]


# --------------------------------------------------------------------------
# G1 - what the dropdown DRAWS (eight bodies)
# --------------------------------------------------------------------------

class EntranceFoldTest(unittest.TestCase):

    def test_the_building_is_one_row_with_a_counter(self):
        """"бл 408": one row, "23 входа", and twenty-three chips when it is open."""
        entries = flagship.search_entries()
        group = entries[BLOCK_ORD]["g"]
        ords = counted(entries, group)
        self.assertEqual(len(ords), BLOCK_ENTRANCES,
                         u"индексът вече не носи %d входа за ord %d, а %d — пинът е мъртъв"
                         % (BLOCK_ENTRANCES, BLOCK_ORD, len(ords)))
        was = ask_pinned_base(self, [drawn(BLOCK_QUERY)])[0]
        self.assertEqual(len(was["rows"]), BLOCK_ROWS_AT_BASE,
                         u"базата %s вече не рисува %d реда за %r, а %d — пинът е мъртъв"
                         % (BASE, BLOCK_ROWS_AT_BASE, BLOCK_QUERY, len(was["rows"])))
        self.assertEqual(len(entrance_rows(was)), BLOCK_ENTRANCE_ROWS_AT_BASE,
                         u"базата %s вече не блъска %d входа в списъка за %r"
                         % (BASE, BLOCK_ENTRANCE_ROWS_AT_BASE, BLOCK_QUERY))
        self.assertEqual(badges(was), [],
                         u"базата %s вече носи значка — пинът е мъртъв" % BASE)
        # the CLOSED draw is judged first and in its own call: a slice without the lot
        # has no `foldState` for the probe to open, so the reason must be ours.
        closed = ask_candidate(self, [drawn(BLOCK_QUERY)])[0]
        self.assertEqual(len(closed["rows"]), 1,
                         u"%s: %r рисува %d реда от горно ниво, не един"
                         % (NEEDLE_ONE_ROW, BLOCK_QUERY, len(closed["rows"])))
        self.assertEqual(badges(closed), [u"%d входа" % BLOCK_ENTRANCES],
                         u"%s: значката е %s" % (NEEDLE_ONE_ROW, badges(closed)))
        self.assertEqual(strips(closed), [],
                         u"%s: лентата е отворена без да е поискана" % NEEDLE_ONE_ROW)
        now = ask_candidate(self, [drawn(BLOCK_QUERY, group)])[0]
        chips = now["rows"][0]["chips"]
        self.assertEqual(len(chips), BLOCK_ENTRANCES,
                         u"отворената лента носи %d бутона, не %d"
                         % (len(chips), BLOCK_ENTRANCES))
        self.assertEqual([chip["text"] for chip in chips], list(BLOCK_CHIPS),
                         u"бутоните не са двайсет и трите входа по реда си")
        self.assertEqual(sorted(int(chip["ord"]) for chip in chips), sorted(ords),
                         u"бутоните не сочат входовете, които индексът дава за групата")
        # the strip carries chips and NOTHING else (lot 5в: the arrows came out)
        self.assertEqual(now["rows"][0]["strangers"], 0,
                         u"лентата носи %d елемента извън бутоните-входове"
                         % now["rows"][0]["strangers"])
        short = ask_candidate(self, [drawn(PRICE_QUERY, entries[PRICE_ORD]["g"]),
                                     drawn(SINGULAR_QUERY, entries[SINGULAR_ORD]["g"])])
        priced, single = short[0]["rows"][0], short[1]["rows"][0]
        self.assertEqual((len(priced["chips"]), priced["strangers"]), (5, 0),
                         u"лентата с пет входа носи %d бутона и %d елемента извън тях"
                         % (len(priced["chips"]), priced["strangers"]))
        self.assertEqual((len(single["chips"]), single["strangers"]), (1, 0),
                         u"лентата с един вход носи %d бутона и %d елемента извън тях"
                         % (len(single["chips"]), single["strangers"]))

    def test_the_counter_and_the_strip_come_from_the_index(self):
        """The rows lie: five children drawn against ten in the index (ADR 012 D4)."""
        entries = flagship.search_entries()
        # (query, ord of the building row, children the BASE draws, expected badge)
        cases = [(COUNTER_QUERY, COUNTER_ORD, COUNTER_DRAWN_AT_BASE, None),
                 (SECOND_COUNTER_QUERY, SECOND_COUNTER_ORD, SECOND_DRAWN_AT_BASE, None),
                 (SINGULAR_QUERY, SINGULAR_ORD, None, SINGULAR_BADGE),
                 (CORNER_QUERY, CORNER_ORD, None, None)]
        groups, folded = [], []
        for query, ord_, drawn_at_base, _ in cases:
            group = entries[ord_]["g"]
            ords = counted(entries, group)
            groups.append(group)
            folded.append(ords)
            if drawn_at_base is not None:
                was = ask_pinned_base(self, [drawn(query)])[0]
                self.assertEqual(len(entrance_rows(was)), drawn_at_base,
                                 u"базата %s рисува %d деца за %r, не %d — пинът е мъртъв"
                                 % (BASE, len(entrance_rows(was)), query, drawn_at_base))
        self.assertEqual(len(folded[2]), 1,
                         u"ord %d вече не е група с един вход — пинът е мъртъв" % SINGULAR_ORD)
        letters = [u"%s" % entries[o]["en"] for o in folded[3]]
        self.assertEqual(letters.count(CORNER_REPEATED_LETTER), CORNER_REPEATS,
                         u"ord %d вече не е ъглова сграда с два входа %r — "
                         u"пинът е мъртъв" % (CORNER_ORD, CORNER_REPEATED_LETTER))
        # the CLOSED draws first, in their own call: the badge alone already answers
        # "does the counter come from the index", and a slice without the lot has no
        # `foldState` for the probe to open.
        closed = ask_candidate(self, [drawn(query) for query, _, _, _ in cases])
        for (query, _, _, wanted), ords, answer in zip(cases, folded, closed):
            wanted = wanted or (u"%d входа" % len(ords))
            self.assertIn(wanted, badges(answer),
                          u"%s %s при %d в индекса за %r — значката не идва от индекса"
                          % (NEEDLE_COUNTER, badges(answer), len(ords), query))
        opened = ask_candidate(self, [drawn(query, group)
                                      for (query, _, _, _), group in zip(cases, groups)])
        for (query, _, _, _), ords, answer in zip(cases, folded, opened):
            chips = [row["chips"] for row in answer["rows"] if row["chips"]]
            self.assertEqual(len(chips), 1,
                             u"%r рисува %d ленти, не една" % (query, len(chips)))
            self.assertEqual(len(chips[0]), len(ords),
                             u"%s %s при %d бутона за %r — значката и лентата се разминаха"
                             % (NEEDLE_COUNTER, badges(answer), len(chips[0]), query))
        # the corner building: the repeated letter keeps BOTH of its chips
        corner = [chip["text"] for chip in opened[3]["rows"][0]["chips"]]
        wanted = CHIP_PREFIX + CORNER_REPEATED_LETTER
        self.assertEqual(corner.count(wanted), CORNER_REPEATS,
                         u"ъгловата сграда показва %d пъти %r, не %d — един вход изчезна"
                         % (corner.count(wanted), wanted, CORNER_REPEATS))
        self.assertEqual(len(set(chip["ord"] for chip in opened[3]["rows"][0]["chips"])),
                         len(corner),
                         u"два бутона на ъгловата сграда сочат един и същ ord")

    def test_a_typed_entrance_is_never_folded(self):
        """Rule 4: a query that spells an entrance keeps every row it draws today."""
        asks = [drawn(query) for query in TYPED_QUERIES]
        was = ask_pinned_base(self, asks)
        now = ask_candidate(self, asks)
        for query, before, after in zip(TYPED_QUERIES, was, now):
            self.assertEqual(badges(after), [],
                             u"%s: %r носи значка %s"
                             % (NEEDLE_TYPED, query, badges(after)))
            self.assertEqual(strips(after), [],
                             u"%s: %r носи лента с бутони" % (NEEDLE_TYPED, query))
            self.assertEqual(htmls(after), htmls(before),
                             u"%s: редовете на %r не са байт-равни на базата %s"
                             % (NEEDLE_TYPED, query, BASE))
        # the only one of the three that HAS something to fold - the witness of half 3
        witness = now[list(TYPED_QUERIES).index(TYPED_WITNESS)]
        self.assertTrue(entrance_rows(witness),
                        u"%s вече не рисува входове — свидетелят е мъртъв" % TYPED_WITNESS)

    def test_the_other_results_stay_visible(self):
        """The bare surface refills the freed places; a narrow query does not (D2)."""
        now = ask_candidate(self, [drawn(BARE_QUERY), drawn(PRICE_QUERY)])
        bare, price = now[0], now[1]
        self.assertEqual(len(bare["rows"]), BARE_TOP_LEVEL_ROWS,
                         u"%r рисува %d реда от горно ниво, не %d"
                         % (BARE_QUERY, len(bare["rows"]), BARE_TOP_LEVEL_ROWS))
        self.assertEqual(entrance_rows(bare), [],
                         u"%r още рисува вход като отделен ред" % BARE_QUERY)
        # D9: `data-idx` keeps the ORIGINAL position in `currentResults`
        indexes = [idx_of(row) for row in bare["rows"]]
        self.assertEqual(indexes, sorted(indexes),
                         u"data-idx не расте по реда на рисуването: %s" % indexes)
        self.assertEqual(len(set(indexes)), len(indexes),
                         u"два реда носят един и същ data-idx: %s" % indexes)
        was = ask_pinned_base(self, [drawn(PRICE_QUERY)])[0]
        self.assertEqual(len(was["rows"]), PRICE_ROWS_AT_BASE,
                         u"базата %s рисува %d реда за %r, не %d — пинът е мъртъв"
                         % (BASE, len(was["rows"]), PRICE_QUERY, PRICE_ROWS_AT_BASE))
        self.assertEqual(len(price["rows"]), PRICE_ROWS,
                         u"обявената цена мръдна: %r рисува %d реда, не %d"
                         % (PRICE_QUERY, len(price["rows"]), PRICE_ROWS))
        self.assertEqual(price["rows"][0]["badge"], PRICE_FIRST_BADGE,
                         u"първият ред на %r носи значка %r, не %r"
                         % (PRICE_QUERY, price["rows"][0]["badge"], PRICE_FIRST_BADGE))

    def test_the_orphan_entrance_keeps_its_row(self):
        """Rule 3: an entrance whose parent is not on the list stays a row of its own."""
        for query, orphan_ord, rows_now, rows_at_base in ORPHAN_QUERIES:
            answers = ask_candidate(self, [search(query), drawn(query)])
            ords = [row["ord"] for row in answers[0]["rows"]]
            self.assertIn(orphan_ord, ords,
                          u"%r вече не класира сирака ord %d — пинът е мъртъв"
                          % (query, orphan_ord))
            was = ask_pinned_base(self, [drawn(query)])[0]
            self.assertEqual(len(was["rows"]), rows_at_base,
                             u"базата %s рисува %d реда за %r, не %d — пинът е мъртъв"
                             % (BASE, len(was["rows"]), query, rows_at_base))
            now = answers[1]
            self.assertEqual(len(now["rows"]), rows_now,
                             u"%r рисува %d реда от горно ниво, не %d"
                             % (query, len(now["rows"]), rows_now))
            orphans = [row for row in entrance_rows(now) if ords[idx_of(row)] == orphan_ord]
            self.assertEqual(len(orphans), 1,
                             u"сиракът ord %d вече не е ред за %r" % (orphan_ord, query))
            self.assertTrue(badges(now),
                            u"%r няма нито една значка — свидетелят не съди сгъването"
                            % query)

    def test_an_entrance_before_its_parent_keeps_its_row(self):
        """Rule 2: the entrance the ranking put first stays a row, the strip repeats it."""
        entries = flagship.search_entries()
        group = entries[BEFORE_PARENT_ORD]["g"]
        self.assertEqual(entries[BEFORE_ENTRANCE_ORD]["g"], group,
                         u"ord %d вече не е вход на ord %d — пинът е мъртъв"
                         % (BEFORE_ENTRANCE_ORD, BEFORE_PARENT_ORD))
        answers = ask_candidate(self, [search(BEFORE_QUERY), drawn(BEFORE_QUERY)])
        ords = [row["ord"] for row in answers[0]["rows"]]
        self.assertEqual(ords[:2], [BEFORE_ENTRANCE_ORD, BEFORE_PARENT_ORD],
                         u"класирането на %r вече не слага входа пред родителя му: %s"
                         % (BEFORE_QUERY, ords[:2]))
        now = answers[1]
        self.assertEqual(len(now["rows"]), 2,
                         u"%r рисува %d реда от горно ниво, не два"
                         % (BEFORE_QUERY, len(now["rows"])))
        first, second = now["rows"][0], now["rows"][1]
        self.assertIn(ENTRANCE_KIND, first["html"],
                      u"ред 0 на %r вече не е входът ord %d"
                      % (BEFORE_QUERY, BEFORE_ENTRANCE_ORD))
        self.assertEqual(ords[idx_of(first)], BEFORE_ENTRANCE_ORD,
                         u"ред 0 на %r сочи ord %s, не %d"
                         % (BEFORE_QUERY, ords[idx_of(first)], BEFORE_ENTRANCE_ORD))
        self.assertEqual(ords[idx_of(second)], BEFORE_PARENT_ORD,
                         u"ред 1 на %r сочи ord %s, не родителя %d"
                         % (BEFORE_QUERY, ords[idx_of(second)], BEFORE_PARENT_ORD))
        self.assertEqual(second["badge"], BEFORE_BADGE,
                         u"родителят носи значка %r, не %r" % (second["badge"], BEFORE_BADGE))
        # the strip is asked for in its OWN call, after the row shape is already judged
        opened = ask_candidate(self, [drawn(BEFORE_QUERY, group)])[0]
        chips = [chip["text"] for chip in opened["rows"][1]["chips"]]
        self.assertIn(BEFORE_CHIP, chips,
                      u"лентата на родителя не повтаря %r" % BEFORE_CHIP)
        self.assertEqual(chips, list(BEFORE_CHIPS),
                         u"редът на бутоните не е естественият: %s" % chips)

    def test_every_chip_resolves_to_its_entrance(self):
        """Each chip carries the numeric `ord` of an entrance of the OPEN group."""
        entries = flagship.search_entries()
        cases = ((BLOCK_QUERY, BLOCK_ORD), (COUNTER_QUERY, COUNTER_ORD),
                 (BEFORE_QUERY, BEFORE_PARENT_ORD), (CORNER_QUERY, CORNER_ORD))
        # a badge has to exist before a strip can be opened: judged in its own call, so
        # a slice without the lot fails here and not inside the probe.
        closed = ask_candidate(self, [drawn(query) for query, _ in cases])
        for (query, _), answer in zip(cases, closed):
            self.assertTrue(badges(answer),
                            u"%r няма значка — няма какво да се отвори" % query)
        for query, ord_ in cases:
            group = entries[ord_]["g"]
            now = ask_candidate(self, [drawn(query, group)])[0]
            open_rows = [row for row in now["rows"] if row["chips"]]
            self.assertEqual(len(open_rows), 1,
                             u"%r рисува %d ленти, не една" % (query, len(open_rows)))
            self.assertTrue(open_rows[0]["open"],
                            u"лентата на %r е отворена, но значката не го казва" % query)
            for row in now["rows"]:
                if row is open_rows[0]:
                    continue
                self.assertEqual(row["chips"], [],
                                 u"%r рисува бутони извън отворената група" % query)
            for chip in open_rows[0]["chips"]:
                text = u"%s" % chip["ord"]
                self.assertTrue(text.isdigit(),
                                u"бутон без числов data-ord за %r: %r" % (query, chip["ord"]))
                entry = entries[int(text)]
                self.assertIsNotNone(entry.get("en"),
                                     u"бутон за %r сочи ord %s — сграден ред, не вход"
                                     % (query, chip["ord"]))
                self.assertEqual(u"%s" % entry.get("g"), u"%s" % group,
                                 u"бутон за %r сочи ord %s от чужда група"
                                 % (query, chip["ord"]))
                self.assertEqual(chip["text"], CHIP_PREFIX + u"%s" % entry["en"],
                                 u"бутонът казва %r, а входът е %r"
                                 % (chip["text"], entry["en"]))

    def test_the_row_list_is_byte_equal_to_the_base(self):
        """The compensation for the blindness: ranking and row html did not move.

        `ask search` and `ask render` for all hundred and thirty pinned queries of the
        flagship and of the three foreign lots - so the green of those gates is green
        for the RIGHT reason and `dedupeDisplayRows` / `buildExactItem` are untouched.
        """
        queries = pinned_queries(self)
        self.assertEqual(len(queries), 130,
                         u"пиновите заявки са %d, не 130 — обединението мръдна"
                         % len(queries))
        asks = []
        for query in queries:
            asks.append(search(query))
            asks.append(render(query))
        was = ask_pinned_base(self, asks)
        now = ask_candidate(self, asks)
        moved = [(asks[i]["ask"], asks[i]["q"])
                 for i in range(len(asks))
                 if lot4b.frozen(was[i]) != lot4b.frozen(now[i])]
        self.assertEqual(moved, [],
                         u"%d от %d отговора мръднаха спрямо базата %s: %s"
                         % (len(moved), len(asks), BASE, moved[:8]))


def pinned_queries(test):
    """The union of the pinned queries of the four gates - imported, never copied."""
    def flat(values):
        out = []
        for item in values:
            out.append(item[0] if isinstance(item, (list, tuple)) else item)
        return [q for q in out if isinstance(q, str)]

    corpus = flagship.corpus_doc(test)["queries"]
    listed = ([flagship.FLAGSHIP_QUERY, flagship.PARENT_WRITTEN_QUERY,
               flagship.NAMED_CHILD_QUERY, flagship.SPACED_MERGED_QUERY]
              + list(flagship.SPACED_LIVE_QUERIES) + list(flagship.DOTTED_QUERIES)
              + list(flagship.DOTLESS_QUERIES) + list(corpus)
              + flat(lot4b.BARE_QUERIES) + [lot4b.BRIZ_QUERY, lot4b.SHIPKA_QUERY]
              + list(lot4b.UNCHANGED_MIXED) + list(lot4b.ORDINARY_QUERIES)
              + list(lot4b.CLASS_WORDS)
              + flat(lot4v.CLASS_LIKE_QUERIES) + flat(lot4v.PRICE_QUERIES)
              + flat(lot4v.RESIDUE_QUERIES) + flat(lot4v.MIXED_QUERIES)
              + list(lot4v.EXACT_QUERIES) + [lot4v.YALTA_QUERY, lot4v.BENDITA_QUERY]
              + list(lot4vb.STREET_QUERIES) + list(lot4vb.UNMOVED_QUERIES)
              + list(lot4vb.NARROWED_QUERIES) + flat(lot4vb.SIGNED_DELTAS)
              + flat(lot4vb.CLASS_WORD_ROWS) + flat(lot4vb.FAMILY)
              + [lot4vb.FINDER_QUERY])
    seen, out = set(), []
    for query in listed:
        if query in seen:
            continue
        seen.add(query)
        out.append(query)
    return out


# --------------------------------------------------------------------------
# G2b - the perimeter: five anchors, only insertion
# --------------------------------------------------------------------------

class PerimeterTest(unittest.TestCase):

    def test_the_five_anchors_are_the_signed_ones(self):
        candidate = index_text(self)
        base = base_text(self)
        for pair in ANCHORED_PAIRS:
            self.assertEqual(candidate.count(pair), 1,
                             u"двойката котва + вмъкнат ред стои %d пъти, не веднъж: %r"
                             % (candidate.count(pair), pair[:60]))
            self.assertEqual(base.count(pair), 0,
                             u"базата %s вече носи двойката %r — пинът е мъртъв"
                             % (BASE, pair[:60]))
        for signature in NEW_SIGNATURES + UNTOUCHED_SIGNATURES:
            self.assertEqual(candidate.count(signature), 1,
                             u"%r се декларира %d пъти, не веднъж"
                             % (signature, candidate.count(signature)))
        self.assertEqual(candidate.count(u"asr-ent-"), ENT_MENTIONS,
                         u"новото селекторно семейство се споменава %d пъти, не %d"
                         % (candidate.count(u"asr-ent-"), ENT_MENTIONS))
        for text in BANNED_IN_FILE:
            self.assertEqual(candidate.count(text), 0,
                             u"доставеният файл още носи %r — обявеното отклонение не е "
                             u"направено" % text)
        added = added_lines(candidate, base)
        self.assertTrue(added, u"нула вмъкнати реда спрямо базата %s" % BASE)
        for text in BANNED_IN_ADDED:
            guilty = [line for line in added if text in line]
            self.assertEqual(guilty, [],
                             u"вмъкнат ред още носи %r: %r" % (text, guilty[:1]))
        # the three lines the halves doctor stand exactly once each
        for line in (HOOK_LINES, COUNTER_LINE, GUARD_LINE):
            self.assertEqual(candidate.count(line), 1,
                             u"котвата на половината стои %d пъти, не веднъж: %r"
                             % (candidate.count(line), line[:60]))
        # the pairs of the three earlier lots stand once each: this lot inserted around
        # them, never between an earlier anchor and its own line.
        for name, pairs in ((u"4б", lot4b.ANCHORED_PAIRS), (u"4в", lot4v.ANCHORED_PAIRS),
                            (u"4в-Б", lot4vb.ANCHORED_PAIRS)):
            for pair in pairs:
                self.assertEqual(candidate.count(pair), 1,
                                 u"двойка на лот %s стои %d пъти, не веднъж: %r"
                                 % (name, candidate.count(pair), pair[:60]))


# --------------------------------------------------------------------------
# G3 - the three negative halves - each RUNS and each FALLS
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
                           FIRE_VARNA_LOT5_BASE=BASE)
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

    def test_removing_the_fold_hook_turns_the_one_row_method_red(self):
        """Without the five lines inside `renderResults` the dropdown draws the old flat
        list again: "бл 408" is back to ten rows (measured in Ф0.7 before this half)."""
        text = lot4b.remove_once(self, index_text(self), HOOK_LINES)
        path = self.doctored("hook_gone", text)
        self.run_half(path, MODULE + ".EntranceFoldTest."
                      "test_the_building_is_one_row_with_a_counter", NEEDLE_ONE_ROW)

    def test_a_counter_read_from_the_rows_turns_the_index_method_red(self):
        """With the counter read from the DRAWN children instead of the index,
        "студентска бл 14" says five while the strip and the index say ten."""
        text = lot4b.replace_once(self, index_text(self), COUNTER_LINE, COUNTER_FROM_ROWS)
        path = self.doctored("counter_from_rows", text)
        self.run_half(path, MODULE + ".EntranceFoldTest."
                      "test_the_counter_and_the_strip_come_from_the_index", NEEDLE_COUNTER)

    def test_removing_the_typed_guard_turns_the_typed_method_red(self):
        """Without the guard "бл 307 вх 9" is folded: its building row takes a badge and
        its rows stop being byte-equal to the base. The other two typed queries draw
        entrances alone, with nothing to fold - they are not witnesses (R1)."""
        text = lot4b.remove_once(self, index_text(self), GUARD_LINE)
        path = self.doctored("typed_guard_gone", text)
        self.run_half(path, MODULE + ".EntranceFoldTest."
                      "test_a_typed_entrance_is_never_folded", NEEDLE_TYPED)


if __name__ == "__main__":
    unittest.main()
