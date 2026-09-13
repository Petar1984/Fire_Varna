# -*- coding: utf-8 -*-
"""Lot 4v-A - a class-like token is not an address either (T-01).

    python -m unittest tests.test_address_search_class_like

Lot 4b (ADR 006a) closed an EXACT set of class words, but `matchKindSet` also has
a prefix arm and a Levenshtein arm: while the colleague was still typing "хотел",
the intermediate "хот", "хоте", "хотек" and "хостел" reached `hotel` through those
arms and still put the five hotel address rows under the hotel list. ADR 006b
widens that same exception of D12: `runGeocoderSearch` derives a `classLike`
vector over the match kinds it already computes, and one compensating decrement
makes an entry matched ONLY through class-like tokens leave the ranking through
the a2 return of lot 4b.

How this gate works, so that no reader has to guess:

  * The client is raised HEADLESS through the flagship's own harness
    (`tests/address_slice_probe.mjs`): the probe answers, THIS file judges. The
    slice is cut by the five markers of Т12, never by a line number.
  * The reference is not a retyped string but the SAME slice at the base commit of
    THIS lot, pinned as a LITERAL under its own environment name
    (`FIRE_VARNA_LOT4V_BASE`) - never the merge-base and never the flagship's
    `FIRE_VARNA_BASE_COMMIT`, which moves for its own reasons. A base whose blob
    equals the TRACKED `index.html` is a dead reference and fails loud; the refusal
    compares the blob with the TRACKED file on purpose, so that a run with
    `FIRE_VARNA_INDEX_HTML_PATH` pointed at a copy of the base still fails for its
    OWN reason.
  * Every pinned base count is asserted as well: a base that stops carrying the
    defect fails loud instead of testing nothing.
  * The signed class words, their derived Latin spelling and the ordinary queries
    are IMPORTED from the lot 4b gate - one source of truth, never a second copy.
  * The declared price of 4в-D3 is pinned here, the gain included: the thirteen
    prefix and fuzzy forms that fall to zero, the residue the signature accepted,
    the three real rows the four-letter "апар" loses and the rows a mixed query
    loses and wins.
  * Nothing is read at module level and no git runs there.
  * "Nothing else moved" is NOT a method here. The whole-file comparison is the
    DELIVERY probe `gates/probe/lot_perimeter.py`, run by hand at the gate with the
    inserted lines named on the command line: a whole-file pin is true exactly once,
    at the delivery of the lot that wrote it. What stays permanent here is the
    ANCHOR of each inserted line.
  * The three negative halves run against DOCTORED copies of `index.html` under the
    temp root - never inside the repository - and demand exit 1 plus the REASON TEXT
    of the assertion that had to fail, never the name of the method: a method name
    also stands in the traceback of an error raised BEFORE the assertion.

Eleven methods: seven on the queries and the two data guards, one on the anchors of
the three inserted lines, three negative halves.

No coordinate, no cadastral number and no reporter name stands in this file.
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
import test_address_quarter_render as flagship        # noqa: E402  (module import, never *)
import test_address_search_class_words as lot4b       # noqa: E402  (one source of truth)

# The base is a LITERAL with the name of THIS lot (план §0.11): not the merge-base,
# not `FIRE_VARNA_BASE_COMMIT` and not the base of lot 4b.
BASE = os.environ.get("FIRE_VARNA_LOT4V_BASE") or "59ffc4e"

# The doctored copies of the negative halves live here - never in the tree.
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lot4v_fixtures"

MODULE = "tests.test_address_search_class_like"

# --------------------------------------------------------------------------
# The three inserted lines and their anchors - the perimeter of the lot
# --------------------------------------------------------------------------

COMMENT_LINE = (u"      // A query token is class-like when every vocabulary word it can "
                u"reach names a CATEGORY too (ADR 006b).\n")
CLASS_LIKE_LINE = (u"      const classLike = toks.map(function (t, qi) { "
                   u"if (CLASS_WORD_TOKENS.has(t)) return false; "
                   u"let seen = false, near = false, far = true; "
                   u"for (const v in ms[qi]) { const isClass = CLASS_WORD_TOKENS.has(v);"
                   u" seen = true; "
                   u"if (ms[qi][v] >= 2) { if (!isClass) return false; near = true; } "
                   u"else if (!isClass) { far = false; } } "
                   u"return seen && (near || far); });\n")
DECREMENT_LINE = u"          if (classLike[qi]) matchedOutsideClass -= 1;\n"
INSERTED_LINES = (COMMENT_LINE, CLASS_LIKE_LINE, DECREMENT_LINE)

ANCHOR_NUMERIC = (u"      const numericTok = toks.map(function (t) { "
                  u"return /^[0-9]+$/.test(t); });\n")
# The line that FOLLOWS the decrement: an inserted line that stands once, but inside
# a foreign function, would keep a bare byte perimeter green.
ANCHOR_BEST = u"          if (best === 3) {"
ANCHORED_PAIRS = (ANCHOR_NUMERIC + COMMENT_LINE + CLASS_LIKE_LINE,
                  lot4b.ANCHOR_BLOCK_TYPED + DECREMENT_LINE + ANCHOR_BEST)

# --------------------------------------------------------------------------
# The queries, pinned by measurement at the base (план §1, ADR 006b 4в-D3)
# --------------------------------------------------------------------------

# (query, rows the BASE draws) - the gain of the lot: the candidate draws zero.
CLASS_LIKE_QUERIES = ((u"хот", 5), (u"хоте", 5), (u"хотек", 5), (u"хостел", 5),
                      (u"апартамент", 1), (u"апартаменти", 1), (u"апартх", 1),
                      (u"апартхот", 1))
# 4в-D3 (б): every prefix or fuzzy form of a class word WITHOUT a non-class
# neighbour falls to zero as well. "апар" is 4в-D3 (г) - the only real loss.
PRICE_QUERIES = ((u"хотелск", 5), (u"хостели", 5), (u"хостела", 5), (u"апа", 2),
                 (u"апар", 5), (u"апарта", 1), (u"апартам", 1), (u"апартаме", 1),
                 (u"апартамен", 1), (u"апартаменте", 1), (u"апартамента", 1),
                 (u"апартхо", 1), (u"апартхоте", 1))
APAR_QUERY = u"апар"
APAR_NEEDLE = u"par stoianov"
# 4в-D3 (а): the residue the signature accepted - byte for byte as it was.
RESIDUE_QUERIES = ((u"х", 3), (u"хо", 5), (u"ап", 3), (u"хотев", 5), (u"семее", 1))
# 4в-D3 (в): the mixed queries that move, with the row each one keeps or wins.
YALTA_QUERY, YALTA_AT_BASE, YALTA_ROWS = u"хоте ялта", 5, 1
YALTA_ROW = u"апартаментен хотел ялта"
BENDITA_QUERY, BENDITA_AT_BASE, BENDITA_ROWS = u"хоте бендита", 7, 5
BENDITA_GAIN = u"бонита"
BRIZ_MIXED_QUERY, BRIZ_MIXED_AT_BASE = u"хоте бриз", 3
MIXED_QUERIES = ((YALTA_QUERY, YALTA_AT_BASE), (BENDITA_QUERY, BENDITA_AT_BASE),
                 (BRIZ_MIXED_QUERY, BRIZ_MIXED_AT_BASE))
# The four mixed queries with a WHOLE class word: the behaviour of lot 4b, untouched.
UNCHANGED_MIXED = (lot4b.BRIZ_QUERY, lot4b.SHIPKA_QUERY) + lot4b.UNCHANGED_MIXED
ORDINARY_AFTER_THE_RESET = 10
# The exact set of lot 4b keeps its own words - a regression pin, green at the base.
EXACT_QUERIES = (u"мотел", u"мотела", u"семеен", u"апарт")

# --------------------------------------------------------------------------
# The two data guards (ADR 006b 4в-D5)
# --------------------------------------------------------------------------

VOCAB_PROBES = ("hot", "hote", "hostel", "apar")
# `data/address_quarters.json` carries the polygon names in `names`: one row per
# polygon, parallel to `codes` and `parents`.
POLYGON_NAMES_FIELD = "names"
FROZEN_COLLIDING_NAMES = [u"Бизнес хотел"]
CYRILLIC_WORD = re.compile(u"[а-я]+")


# --------------------------------------------------------------------------
# The base of THIS lot - read inside a method, never at import
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
    """The same five markers of Т12, cut out of `<BASE>:index.html`, raised in the probe."""
    text = base_text(test)
    shared = flagship.cut(text, flagship.MARK_SHARED_START, flagship.MARK_SHARED_END, test)
    body = flagship.cut(text, flagship.MARK_SLICE_START, flagship.MARK_SLICE_END, test)
    if flagship.MARK_SLICE_CORE_END not in text:
        test.fail(u"липсва маркер Т12 в блоба %s: %s" % (BASE, flagship.MARK_SLICE_CORE_END))
    return flagship.run_probe(test, {"shared": shared, "slice": body,
                                     "exports": flagship.EXPORTS_QUARTER, "asks": asks},
                              quarters_path=flagship.DELIVERED)


# --------------------------------------------------------------------------
# Г1 · the class-like tokens, the declared price and the two data guards
# --------------------------------------------------------------------------

class ClassLikeTest(unittest.TestCase):

    def test_a_class_like_token_returns_no_address_rows(self):
        """The eight queries of the complaint: a token that can only reach category
        words carries no address row any more (ADR 006b 4в-D3, the gain)."""
        asks = [lot4b.render(query) for query, _ in CLASS_LIKE_QUERIES]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for (query, at_base), was, now in zip(CLASS_LIKE_QUERIES, reference, candidate):
            self.assertEqual(len(was), at_base,
                             u"базата %s вече не дава %d адресни реда за %r (дава %d) — "
                             u"пинът е мъртъв" % (BASE, at_base, query, len(was)))
            self.assertEqual(len(now), 0,
                             u"класоподобният токен %r още дава %d адресни реда"
                             % (query, len(now)))

    def test_the_declared_price_is_pinned(self):
        """4в-D3: the thirteen prefix and fuzzy forms fall to zero, the four-letter
        "апар" loses the three REAL rows it carried through the token `par`, and the
        residue the signature accepted stays byte for byte as it was. The price cannot
        change in silence: every base count is asserted too."""
        queries = ([query for query, _ in PRICE_QUERIES]
                   + [query for query, _ in RESIDUE_QUERIES])
        asks = [lot4b.render(query) for query in queries]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for (query, at_base), was, now in zip(PRICE_QUERIES, reference, candidate):
            self.assertEqual(len(was), at_base,
                             u"базата %s вече не дава %d адресни реда за %r (дава %d) — "
                             u"пинът е мъртъв" % (BASE, at_base, query, len(was)))
            self.assertEqual(len(now), 0,
                             u"обявената цена мърда: %r още дава %d адресни реда"
                             % (query, len(now)))
        apar = queries.index(APAR_QUERY)
        self.assertTrue(lot4b.carries(reference[apar], APAR_NEEDLE),
                        u"базата %s вече не носи истинските редове %r за %r — "
                        u"пинът е мъртъв" % (BASE, APAR_NEEDLE, APAR_QUERY))
        self.assertFalse(lot4b.carries(candidate[apar], APAR_NEEDLE),
                         u"%r още носи %r — обявената загуба не се е случила"
                         % (APAR_QUERY, APAR_NEEDLE))
        tail = len(PRICE_QUERIES)
        for (query, at_base), was, now in zip(RESIDUE_QUERIES, reference[tail:],
                                              candidate[tail:]):
            self.assertEqual(len(was), at_base,
                             u"базата %s вече не дава %d адресни реда за %r (дава %d) — "
                             u"пинът е мъртъв" % (BASE, at_base, query, len(was)))
            self.assertTrue(lot4b.frozen(now) == lot4b.frozen(was),
                            u"остатъкът %r не е байт за байт равен на базата %s"
                            % (query, BASE))

    def test_ordinary_queries_are_byte_equal_to_the_base(self):
        """The ordinary queries of lot 4b after "хостел" left them for the class-like
        method (ADR 006b 4в-D4), plus the four mixed queries with a WHOLE class word:
        nothing outside the declared price moved."""
        self.assertEqual(len(lot4b.ORDINARY_QUERIES), ORDINARY_AFTER_THE_RESET,
                         u"обикновените заявки на 4б са %d, не %d — пренастройката на "
                         u"006b е разместена" % (len(lot4b.ORDINARY_QUERIES),
                                                 ORDINARY_AFTER_THE_RESET))
        queries = tuple(lot4b.ORDINARY_QUERIES) + UNCHANGED_MIXED
        asks = [lot4b.render(query) for query in queries]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for query, was, now in zip(queries, reference, candidate):
            self.assertTrue(was, u"базата %s дава нула реда за %r — пинът е мъртъв"
                            % (BASE, query))
            self.assertTrue(lot4b.frozen(now) == lot4b.frozen(was),
                            u"заявката без класоподобна дума %r не е байт за байт равна "
                            u"на базата %s" % (query, BASE))

    def test_a_class_like_word_with_a_name_drops_only_the_class_like_rows(self):
        """4в-D3 (в): a mixed query loses the rows that entered ONLY through the
        class-like word and WINS real addresses under the cap; a mixed query whose
        rows stand on their own name does not move by a single byte."""
        asks = [lot4b.render(query) for query, _ in MIXED_QUERIES]
        reference = ask_pinned_base(self, asks)
        candidate = flagship.ask_client(self, asks)
        for (query, at_base), was in zip(MIXED_QUERIES, reference):
            self.assertEqual(len(was), at_base,
                             u"базата %s вече не дава %d адресни реда за %r (дава %d) — "
                             u"пинът е мъртъв" % (BASE, at_base, query, len(was)))
        yalta_was, bendita_was, briz_was = reference
        yalta_now, bendita_now, briz_now = candidate

        self.assertEqual(len(yalta_now), YALTA_ROWS,
                         u"смесената заявка %r дава %d адресни реда вместо измерения един"
                         % (YALTA_QUERY, len(yalta_now)))
        self.assertTrue(lot4b.carries(yalta_was, lot4b.MAK_ROW),
                        u"базата %s вече не носи %r за %r — пинът е мъртъв"
                        % (BASE, lot4b.MAK_ROW, YALTA_QUERY))
        self.assertFalse(lot4b.carries(yalta_now, lot4b.MAK_ROW),
                         u"%r още носи ред, съвпаднал само през класоподобната дума"
                         % YALTA_QUERY)
        self.assertTrue(lot4b.carries(yalta_now, YALTA_ROW),
                        u"%r загуби и реда %r, който стои на собственото си име"
                        % (YALTA_QUERY, YALTA_ROW))

        self.assertEqual(len(bendita_now), BENDITA_ROWS,
                         u"смесената заявка %r дава %d адресни реда вместо измерените пет"
                         % (BENDITA_QUERY, len(bendita_now)))
        self.assertTrue(lot4b.carries(bendita_now, BENDITA_GAIN),
                        u"%r не носи печалбата %r под тавана — обявената цена е друга"
                        % (BENDITA_QUERY, BENDITA_GAIN))

        self.assertTrue(lot4b.frozen(briz_now) == lot4b.frozen(briz_was),
                        u"смесената заявка %r не е байт за байт равна на базата %s"
                        % (BRIZ_MIXED_QUERY, BASE))

    def test_the_exact_set_still_owns_its_words(self):
        """A REGRESSION pin, green at the base as well (план §8, фолд на атаки №2/№7):
        the exact set of lot 4b keeps its own words at zero address rows. The proof
        that the new rule is a UNION with that set is the structural pin of the
        predicate in `PerimeterTest`, not a negative half - the owner of "мотел" is
        the a2 return of lot 4b, measured, so a half here would be green forever."""
        asks = [lot4b.render(query) for query in EXACT_QUERIES]
        candidate = flagship.ask_client(self, asks)
        for query, rows in zip(EXACT_QUERIES, candidate):
            self.assertEqual(len(rows), 0,
                             u"подписаната класова дума %r още дава %d адресни реда"
                             % (query, len(rows)))

    def test_the_vocabulary_carries_nothing_class_like_outside_the_class(self):
        """4в-D5 (а), the guard for FUTURE data: for `hot`, `hote`, `hostel` and
        `apar` no token of the shipped vocabulary OUTSIDE the signed set is equal to
        the probe or starts with it - that is exactly the arm "a match of kind >= 2
        outside the class". Pure string operations: `lev` is not ported here. Red
        means an ingest brought in a word (a street "Хотелска") that makes the
        class-like token ambiguous, the cure of "хот"/"хоте" stops in silence and the
        lot is reconsidered - the test is not "fixed". Declared boundary: the fuzzy
        arm is invisible to this guard; its detector is the functional pin above."""
        if not flagship.SEARCH_INDEX.is_file():
            self.fail(u"липсва %s" % flagship.SEARCH_INDEX)
        vocabulary = json.loads(flagship.SEARCH_INDEX.read_bytes().decode("utf-8"))["vocab"]
        self.assertTrue(vocabulary, u"нула токена в речника — пазачът е вакуумен")
        self.assertIn("hotel", vocabulary,
                      u"речникът вече не носи `hotel` — пазачът е вакуумен")
        signed = set(lot4b.DERIVED_TOKENS)
        for probe in VOCAB_PROBES:
            outside = sorted(token for token in vocabulary
                             if token not in signed
                             and (token == probe or token.startswith(probe)))
            self.assertEqual(outside, [],
                             u"речникът носи токени извън класа, които %r достига като "
                             u"представка: %r — класоподобното правило става двусмислено"
                             % (probe, outside[:10]))

    def test_no_polygon_name_collides_with_the_signed_class_set(self):
        """4в-D5 (б), the guard for FUTURE data: the FROZEN list of polygon names that
        carry a signed class word. The names stand in the `names` array of
        `data/address_quarters.json` - one row per polygon, parallel to `codes` and
        `parents`. Red at a second name means sub-lot 4в-Б, which puts the polygon
        names into `qtk`, MUST exclude the class words first, or the polygon becomes
        unreachable by its own name."""
        if not flagship.DELIVERED.is_file():
            self.fail(u"липсва %s" % flagship.DELIVERED)
        document = json.loads(flagship.DELIVERED.read_bytes().decode("utf-8"))
        names = document[POLYGON_NAMES_FIELD]
        self.assertTrue(names, u"нула полигонни имена — пазачът е вакуумен")
        words = set(word.lower() for word in lot4b.CLASS_WORDS)
        colliding = sorted(name for name in names
                           if any(part in words
                                  for part in CYRILLIC_WORD.findall((name or u"").lower())))
        self.assertEqual(colliding, FROZEN_COLLIDING_NAMES,
                         u"полигонните имена с класова дума са %r, а замразеният списък "
                         u"е %r" % (colliding, FROZEN_COLLIDING_NAMES))


# --------------------------------------------------------------------------
# Г2 · the perimeter inside index.html
# --------------------------------------------------------------------------

class PerimeterTest(unittest.TestCase):

    # The whole file is compared with the base by the DELIVERY probe
    # `gates/probe/lot_perimeter.py`, never by a method here. The count of
    # `CLASS_WORD_TOKENS` is pinned ONLY in the lot 4b file (:335) - no second truth.

    def test_the_three_lines_are_the_signed_ones(self):
        candidate = lot4b.index_text(self)
        for pair in ANCHORED_PAIRS:
            self.assertEqual(candidate.count(pair), 1,
                             u"двойката котва + вмъкнат ред стои %d пъти, не веднъж: %r"
                             % (candidate.count(pair), pair[:60]))
        self.assertEqual(candidate.count(u"classLike"), 2,
                         u"`classLike` се споменава %d пъти, не два"
                         % candidate.count(u"classLike"))


# --------------------------------------------------------------------------
# Г3/Г3б/Г4 · the three negative halves - each RUNS and each FALLS
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

    def without_the_decrement(self):
        """The SAME doctored copy for both decrement halves: one line removed once."""
        return self.doctored("decrement_gone",
                             lot4b.remove_once(self, lot4b.index_text(self), DECREMENT_LINE))

    def run_half(self, path, method, needle):
        """The needle is the REASON TEXT of the assertion that has to fail, never the
        name of the method: the name also stands in the traceback of an ImportError
        raised long before the assertion."""
        self.assertTrue(path.is_file(), u"копието на половината липсва: %s" % path)
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

    def test_removing_the_decrement_turns_the_class_like_method_red(self):
        """Without the compensating decrement "хот"/"хоте"/"хостел" draw their five
        hotel rows again - measured before the line was written."""
        self.run_half(self.without_the_decrement(),
                      MODULE + ".ClassLikeTest."
                      "test_a_class_like_token_returns_no_address_rows",
                      u"класоподобният токен")

    def test_removing_the_decrement_turns_the_mixed_method_red(self):
        """The same doctored copy, a different method: without the decrement
        "хоте ялта" draws five rows again instead of the one measured."""
        self.run_half(self.without_the_decrement(),
                      MODULE + ".ClassLikeTest."
                      "test_a_class_like_word_with_a_name_drops_only_the_class_like_rows",
                      u"смесената заявка")

    def test_a_byte_in_an_untouched_function_turns_the_delivery_probe_red(self):
        """The half of the DELIVERY probe: one byte in a function this lot never
        touches has to turn `gates/probe/lot_perimeter.py` red, with its own reason
        and never with the refusal of a dead base."""
        text = lot4b.replace_once(self, lot4b.index_text(self), lot4b.UNTOUCHED_LINE,
                                  lot4b.UNTOUCHED_LINE.replace(u") {", u")  {"))
        path = self.doctored("untouched_function_byte", text)
        allow = path.parent / "allow_lines.txt"
        # The declared rows already carry their trailing newline - written as they are.
        allow.write_bytes(u"".join(INSERTED_LINES).encode("utf-8"))
        self.assertTrue(path.is_file() and allow.is_file(),
                        u"копието или allow-файлът на половината липсва: %s" % path.parent)
        environment = dict(os.environ, PYTHONIOENCODING="utf-8")
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
