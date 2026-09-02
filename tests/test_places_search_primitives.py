"""Plan §5 G12а/G12б — the two primitive gates the places search stands on.

(a) VERBATIM PRIMITIVES. The places branch of the search may not invent its own
    normalisation: plan §3 Т1(4)/(5) says it copies `norm()` and `skel()` (and `lev()`
    for the fuzzy step) out of the address search word for word, because the address
    IIFE keeps them private. This test pulls every one-line definition of the three out
    of index.html and asserts all copies are byte-identical. There are exactly two of
    each: the address search (index.html:4786-4788) and the places IIFE that C4 landed
    under it. The day someone "improves" one copy, the two branches start
    disagreeing about which hotel a query finds — silently. This makes it loud.

(b) placeTokens REPLICA. The tokenizer of plan §3 Т1, as refined by §11 Б1, written
    once in Python here and once in JS in C4 — one table, two implementations. The
    EXPECTATIONS table below is the contract C4 copies 1:1; if a row of it ever has to
    change, the rule changed, and that needs a signed plan.

(c) SHA-PINNED PAYLOADS (plan §12 В7 + §14, gate G12г). The places branch trusts only
    the bytes the plan pinned, so the two constants in index.html must equal the sha256
    of the two tracked files. A regenerated bundle that forgets to re-pin would switch
    the whole branch off in the browser without a word; this makes it a red build.

    Order matters and is the plan's, not a convenience:
      1. lower-case, then strip only what `norm()` itself would destroy — typographic
         quotes/dashes, "/", "(", ")" -> space; "д-р"/"х-л"/"к-с" -> the long form;
         the ordinal suffix "7-мо" -> "7" (norm() turns the hyphen into a space, so
         this cannot wait until after it);
      2. `norm()` verbatim, then split;
      3. token-level rules: "св" -> "свети", "др" -> "доктор", "апартхотел" ->
         "апарт"+"хотел", Cyrillic І/і -> Latin i, Roman numeral -> Arabic, ordinal
         word 1-12 -> digit, attached ordinal suffix -> digit;
      4. `skel()` verbatim.

Run: python -m unittest discover -s tests
"""
import hashlib
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
INDEX = REPO / "index.html"

# G12г — the payloads the places branch is allowed to trust: the constant in
# index.html, and the tracked file whose bytes it pins (plan §12 В7, §14).
SHA_PINS = (
    ("HOTELS_SHA256", "data/hotels.json"),
    ("PLACES2_SHA256", "data/places.json"),      # phase 2: the third payload
    ("CATS_SHA256", "data/place_categories.json"),
)

# The three private helpers of the address search that the places branch must copy.
PRIMITIVES = ("norm", "skel", "lev")


def definitions_of(text, name):
    """Every definition of `name` in `text`, from the marker to the end of its line.

    All three primitives are written as one-liners in index.html, so "to the end of the
    line" is the whole definition; a multi-line rewrite would be caught by the identity
    assertion below rather than silently truncated.
    """
    marker = "function " + name + "("
    found = []
    for match in re.finditer(re.escape(marker), text):
        end = text.find("\n", match.start())
        if end == -1:
            end = len(text)
        found.append(text[match.start():end].rstrip("\r"))
    return found


# --- the two primitives, replicated from index.html:4786-4787 -----------------------

# skel() transliterates Cyrillic, then folds y/j onto i and collapses doubled letters.
_CYRILLIC_TO_LATIN = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ж": "zh", "з": "z",
    "и": "i", "й": "i", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
    "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts", "ч": "ch",
    "ш": "sh", "щ": "sht", "ъ": "a", "ь": "", "ю": "yu", "я": "ya",
}
_FOLD_TO_I_RE = re.compile("[yj]")
_COLLAPSE_RE = re.compile(r"(\D)\1+")

# norm() strips exactly these six characters. chr(0x2116) is № and chr(0x22) is the
# straight double quote — spelled out so this file stays plain ASCII where it can.
_NORM_PUNCT_RE = re.compile("[" + re.escape("." + chr(0x2116) + ",'" + chr(0x22) + "-") + "]")
_WHITESPACE_RE = re.compile(r"\s+")


def norm(value):
    """Byte-for-byte replica of norm() at index.html:4786."""
    text = ("" if value is None else str(value)).lower()
    text = text.replace("блок", "бл").replace("вход", "вх")
    text = _NORM_PUNCT_RE.sub(" ", text)
    return _WHITESPACE_RE.sub(" ", text).strip()


def skel(word):
    """Byte-for-byte replica of skel() at index.html:4787."""
    word = word.lower()
    out = "".join(_CYRILLIC_TO_LATIN.get(ch, ch) for ch in word)
    return _COLLAPSE_RE.sub(r"\1", _FOLD_TO_I_RE.sub("i", out))


# --- placeTokens (plan §3 Т1 + §11 Б1) ----------------------------------------------

# Cleaned before norm(), because norm() would turn them into word breaks or drop them:
# „ “ ” ‚ ‘ ’ « » – —  and  /  (  )
_TYPOGRAPHIC = "".join(chr(code) for code in (
    0x201e, 0x201c, 0x201d, 0x201a, 0x2018, 0x2019, 0x00ab, 0x00bb, 0x2013, 0x2014))
_TYPO_RE = re.compile("[" + re.escape(_TYPOGRAPHIC + "/()") + "]")

# Abbreviations that norm() would split on the hyphen; expanded to the long form first.
_ABBREVIATIONS = (("д-р", "доктор "), ("х-л", "хотел "), ("к-с", "комплекс "))

# "7-мо", "7 мо", "7мо" -> "7". Must run before norm(), which eats the hyphen.
_ORDINAL_SUFFIX_RE = re.compile(r"(\d+)\s*-?\s*(ми|ма|мо|ти|та|то|ви|ва|во|ри|ра|ро)(?![а-яa-z])")
# The same suffix once norm() has already run and left it glued to the digit.
_TOKEN_ORDINAL_RE = re.compile(r"^(\d+)(ми|ма|мо|ти|та|то|ви|ва|во|ри|ра|ро)$")

# І/і (U+0406/U+0456) are visually identical to Latin I/i and reach us from registry
# spellings such as "І ОУ"; they must become the Latin letter before the Roman check.
CYRILLIC_I_UPPER = chr(0x0406)
CYRILLIC_I_LOWER = chr(0x0456)

_ROMAN_RE = re.compile(r"^[ivx]{1,5}$")


def _roman_numerals():
    """Valid I/V/X Roman numerals up to five characters -> their Arabic value."""
    units = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV",
             5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    table = {}
    for number in range(1, 40):
        written = ("X" * (number // 10)) + units[number % 10]
        if 1 <= len(written) <= 5:
            table[written.lower()] = number
    return table


ROMAN_NUMERALS = _roman_numerals()


def _ordinal_words():
    """Bulgarian ordinal words 1-12, in the forms a query actually carries."""
    stems = ((1, "първ"), (2, "втор"), (3, "трет"), (4, "четвърт"), (5, "пет"),
             (6, "шест"), (7, "седм"), (8, "осм"), (9, "девет"), (10, "десет"),
             (11, "единадесет"), (11, "единайсет"), (12, "дванадесет"), (12, "дванайсет"))
    endings = ("и", "а", "о", "ият", "ия", "ата", "ото", "ите")
    return {stem + ending: number for number, stem in stems for ending in endings}


ORDINAL_WORDS = _ordinal_words()

# Compounds norm() cannot split, because they carry no separator at all.
_COMPOUNDS = {"апартхотел": ["апарт", "хотел"], "апарткомплекс": ["апарт", "комплекс"]}


def _rewrite_token(token):
    """The token-level rules of plan §11 Б1, applied before skel()."""
    token = token.replace(CYRILLIC_I_LOWER, "i").replace(CYRILLIC_I_UPPER, "i")
    if token == "св":
        return "свети"
    if token == "др":
        return "доктор"
    if _ROMAN_RE.match(token) and token in ROMAN_NUMERALS:
        return str(ROMAN_NUMERALS[token])
    if token in ORDINAL_WORDS:
        return str(ORDINAL_WORDS[token])
    attached = _TOKEN_ORDINAL_RE.match(token)
    if attached:
        return attached.group(1)
    return token


def place_tokens(value):
    """Plan §3 Т1 + §11 Б1: query and name go through the very same pipeline."""
    text = ("" if value is None else str(value)).lower()
    text = _TYPO_RE.sub(" ", text)
    for short, long in _ABBREVIATIONS:
        text = text.replace(short, long)
    text = _ORDINAL_SUFFIX_RE.sub(r"\1", text)
    tokens = []
    for word in norm(text).split(" "):
        if not word:
            continue
        for part in _COMPOUNDS.get(word, [word]):
            tokens.append(skel(_rewrite_token(part)))
    return tokens


# The contract C4 copies 1:1 into JS. Measured against this replica, not hand-written:
# "княз" skeletonises to "kniaz", not "knyaz" — skel() maps я -> ya and then folds
# every y onto i (index.html:4787). The row was corrected to the measurement.
EXPECTATIONS = (
    ("VII СУ „Найден Геров“", ["7", "su", "naiden", "gerov"]),
    ("седмо су", ["7", "su"]),
    ("7-мо су", ["7", "su"]),
    (CYRILLIC_I_UPPER + " ОУ „Свети княз Борис I“", ["1", "ou", "sveti", "kniaz", "boris", "1"]),
    ("св. марина", ["sveti", "marina"]),
    ("д-р иванов", ["doktor", "ivanov"]),
    ("БОНИТА/BONITA", ["bonita", "bonita"]),
    ("х-л романтика", ["hotel", "romantika"]),
    ("ДКЦ 2", ["dkts", "2"]),
    ("II ДКЦ", ["2", "dkts"]),
    ("Зл.котва", ["zl", "kotva"]),
    ("Иглика-2", ["iglika", "2"]),
    ("ХОТЕЛ  ХЕЛИОС СПА", ["hotel", "helios", "spa"]),
    # Plan §11 Б1 names these three explicitly as additions to the table.
    ("Св.Николай", ["sveti", "nikolai"]),
    ("Св.св.Кирил", ["sveti", "sveti", "kiril"]),
    ("Др Хараламбиев", ["doktor", "haralambiev"]),
    # The two compounds no separator can split.
    ("апартхотел", ["apart", "hotel"]),
    ("апарткомплекс", ["apart", "kompleks"]),
)


class VerbatimPrimitivesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = INDEX.read_text(encoding="utf-8")

    def test_every_primitive_is_defined_in_index_html(self):
        for name in PRIMITIVES:
            copies = definitions_of(self.index, name)
            # EXACTLY two since C4: the address search and the places branch. A third
            # copy means a third matcher nobody is comparing against the other two.
            self.assertEqual(len(copies), 2, "expected 2 definitions of " + name + "()")

    def test_all_copies_of_each_primitive_are_byte_identical(self):
        for name in PRIMITIVES:
            copies = definitions_of(self.index, name)
            distinct = sorted(set(copies))
            self.assertEqual(
                len(distinct), 1,
                "%s() has %d definitions in %d variants:\n%s"
                % (name, len(copies), len(distinct), "\n".join(distinct)))


class ShaPinTest(unittest.TestCase):
    """G12г — the constants in index.html against the bytes on disk."""

    def test_pinned_hashes_match_the_tracked_payloads(self):
        index = INDEX.read_text(encoding="utf-8")
        for constant, relative in SHA_PINS:
            match = re.search(r"const\s+" + constant + r"\s*=\s*'([0-9a-f]{64})'", index)
            self.assertIsNotNone(match, constant + " is not pinned in index.html")
            digest = hashlib.sha256((REPO / relative).read_bytes()).hexdigest()
            self.assertEqual(match.group(1), digest, relative + " no longer matches " + constant)


class PlaceTokensTest(unittest.TestCase):
    def test_expectations_table(self):
        for query, expected in EXPECTATIONS:
            self.assertEqual(place_tokens(query), expected, query)

    def test_empty_and_punctuation_only_queries_yield_no_tokens(self):
        for query in ("", "   ", "()", "-", "„“"):
            self.assertEqual(place_tokens(query), [], repr(query))

    def test_a_name_and_the_query_for_it_tokenise_the_same_way(self):
        # The whole point of one tokenizer for both sides (plan §3 Т1).
        self.assertEqual(place_tokens("ХОТЕЛ  ХЕЛИОС СПА"), place_tokens("хотел хелиос спа"))


if __name__ == "__main__":
    unittest.main()
