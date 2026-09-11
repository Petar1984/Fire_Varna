# -*- coding: utf-8 -*-
"""Ф6 · ИБ1-Г8 — the delivered quarter index, pinned, and the hand that signed it.

    python -m unittest tests.test_quarter_index_bundle

Guards `data/address_quarters.json`: the byte copy of the artefact varna_3d builds
(`src/export_fire_varna_quarter_index.py`, commit 97e2432 on branch rezhimi,
11.09.2026) and Petar commits here with his own hand (К8). The sibling of
tests/test_places_public_bundle.py: every rule below has its twin there unless a
comment says why it cannot.

What "pinned" means (red line 14 of the plan): the pinned bytes are the TRACKED
blob. `.gitattributes` (`* text=auto eol=lf`) normalizes the delivery to LF on
commit, so the blob GitHub Pages serves is the LF one; the sha is measured on
`git show HEAD:…` (or on the index before the commit exists), never on a Windows
working tree.

Beyond the bytes this gate asserts:

  * the CLOSED schema of план §3.Г — exactly eight top-level keys, exactly eight
    keys in `generated_from`, `kind` verbatim, `quarters_version` == 2 as a VALUE;
  * the positional join (STOP 17): `entry_count` == the number of entries in
    `data/search_index.json` and `address_row_count` == the number of rows in
    `data/address_rows.json`, and the two payload sha256 of `generated_from` are
    the sha256 of THOSE two tracked blobs. A re-export of either payload without a
    re-export of this file is caught here, before the client ever sees it;
  * zero geometry and zero floats (план §3.Г): the whole document is strings and
    whole numbers, and none of the forbidden keys appears anywhere;
  * D16 AS A GATE (план §3.А Ф6): the commit that last touched the delivered path
    is `Petar1984`'s. The white list of `gates/release.py` has no `signed_by` for
    this file, so neither `signable()` nor проверка 7 of `run_gates.py` looks at
    it — without this test the rule "data is committed by Petar's hand" would have
    no machine judge for the quarter index;
  * the corpus Ф11 (`scratch/places_search/ib_corpus_11.09.json`) by sha256 and by
    its CLOSED two-storey shape — it is the fixture every client gate stands on.

Червено по конструкция до К8/К9 (ИНТЕРВАЛ А, план §4 стъпка 9): the delivered
path is born in К8 by Petar's hand, so every method here is RED until then. That
is the declared set of D19, not a surprise.

G2 ("the test RUNS and FAILS") needs the gate pointed at a deliberately corrupted
copy. Set **FIRE_VARNA_QUARTER_INDEX_PATH** (and/or **FIRE_VARNA_CORPUS_PATH**) to
an alternative file and every assertion below runs against it.

Run: python -m unittest discover -s tests
"""
import gzip
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from gates import release  # noqa: E402  (the repo root has to be on the path first)

DELIVERED_REL = "data/address_quarters.json"
SEARCH_INDEX_REL = "data/search_index.json"
ADDRESS_ROWS_REL = "data/address_rows.json"
CORPUS_REL = "scratch/places_search/ib_corpus_11.09.json"

# G2 override: the corrupted copy is fed in through the environment, never by
# editing data/.
OVERRIDE = os.environ.get("FIRE_VARNA_QUARTER_INDEX_PATH")
CORPUS_OVERRIDE = os.environ.get("FIRE_VARNA_CORPUS_PATH")

# Measured on the artefact of varna_3d 97e2432 (ИБ1-О19):
#   git -C C:/git/varna_3d show 97e2432:data/fire_varna_quarter_index.json
DELIVERED_SHA256 = "7642d3ec334bebbaf563dcf4dbf7c8aef403a49d3559d99a1a5e7354fc885a52"
DELIVERED_BYTES = 493305
DELIVERED_GZIP9 = 23400

# план §3.Г — the CLOSED white lists.
TOP_LEVEL_KEYS = {"schema_version", "kind", "generated_from", "codes", "names",
                  "parents", "entry_cell", "row_cell"}
GENERATED_FROM_KEYS = {"search_index_sha256", "entry_count", "address_rows_sha256",
                       "address_row_count", "entries_digest", "rows_digest",
                       "quarters_version", "snapshot_date"}
KIND = "fire_varna_quarter_index"
SCHEMA_VERSION = "1.0"
QUARTERS_VERSION = 2
SNAPSHOT_DATE = "2026-09-08"

# The measured shape of the delivery (М, 11.09): 90 leaf cells, one cell per
# entry, one per row.
CELL_COUNT = 90
ENTRY_COUNT = 86232
ROW_COUNT = 80510
# Гасенето живее при билда (план §3.Д): -1 for outside ∪ locality ∪ multi-cell key.
ENTRY_MINUS_ONE = 37839
ROW_MINUS_ONE = 17097

CODE_RE = re.compile(r"^[a-z0-9_]{1,64}$")
DIGEST_RE = re.compile(r"^[0-9a-f]{8}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
# Never a coordinate, never geometry (план §3.Г, ADR 011 G29).
FORBIDDEN_KEYS = {"coordinates", "geometry", "geometries", "centroid", "centroid_e7",
                  "n_pts", "precision_m", "advert_id", "raw_sha256", "pin", "bbox"}

# The corpus Ф11 (О98) — two top-level keys, three keys per entry, and nothing
# else: no `pin`, no `label`, no `d`, no `qtk`.
CORPUS_SHA256 = "67a65f07e5887b2d964645ce1a61d12a02f6f0fb48b00584ce754d265b41b974"
CORPUS_BYTES = 9175
CORPUS_TOP_KEYS = {"queries", "entries"}
CORPUS_ENTRY_KEYS = {"tk", "kind", "cell"}
CORPUS_QUERIES = 20
CORPUS_ENTRIES = 145


def git_bytes(*args):
    """The bytes of a git object, or None when the object does not exist."""
    proc = subprocess.run(["git", "-C", str(REPO)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.stdout if proc.returncode == 0 else None


def blob_bytes(rel):
    """The DELIVERED bytes of a tracked path: HEAD first, the index second.

    Red line 14: a delivery sha is measured on the blob, never on the working
    tree. Before К8 neither object exists — the caller turns that into a named
    failure, never into a skip.
    """
    for ref in ("HEAD:" + rel, ":" + rel):
        raw = git_bytes("show", ref)
        if raw is not None:
            return raw
    return None


def delivered_bytes(test):
    if OVERRIDE:
        return pathlib.Path(OVERRIDE).read_bytes()
    raw = blob_bytes(DELIVERED_REL)
    if raw is None:
        test.fail(u"%s няма нито в HEAD, нито в индекса — К8 още не е положен "
                  u"(ИНТЕРВАЛ А)" % DELIVERED_REL)
    return raw


def corpus_bytes(test):
    path = pathlib.Path(CORPUS_OVERRIDE) if CORPUS_OVERRIDE else (REPO / CORPUS_REL)
    if not path.exists():
        test.fail(u"липсва корпусът Ф11: %s" % path)
    return path.read_bytes().replace(b"\r\n", b"\n")


def walk_keys(node, out):
    if isinstance(node, dict):
        for key, value in node.items():
            out.add(key)
            walk_keys(value, out)
    elif isinstance(node, list):
        for value in node:
            walk_keys(value, out)


def walk_floats(node, path, out):
    if isinstance(node, dict):
        for key, value in node.items():
            walk_floats(value, path + "/" + str(key), out)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            walk_floats(value, path + "[%d]" % i, out)
    elif isinstance(node, float):
        out.append(path)


class QuarterIndexBytesTest(unittest.TestCase):
    """ИБ1-Г8 (а) — the bytes, the size and the compressed size are the delivery."""

    def test_sha256_and_size(self):
        raw = delivered_bytes(self)
        self.assertEqual(len(raw), DELIVERED_BYTES,
                         u"байтовете на доставката се разминават с пина")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), DELIVERED_SHA256,
                         u"sha256 на доставката се разминава с пина")
        self.assertEqual(len(gzip.compress(raw, 9)), DELIVERED_GZIP9,
                         u"gzip-9 на доставката се разминава с измереното")

    def test_no_carriage_return(self):
        """The blob is LF — a CRLF copy is a different payload for the browser."""
        self.assertNotIn(b"\r", delivered_bytes(self), u"доставката носи CR")


class QuarterIndexSchemaTest(unittest.TestCase):
    """ИБ1-Г8 (б) — the closed schema of план §3.Г, key by key."""

    def setUp(self):
        self.doc = json.loads(delivered_bytes(self).decode("utf-8"))

    def test_top_level_keys_are_exactly_eight(self):
        self.assertEqual(set(self.doc), TOP_LEVEL_KEYS)
        self.assertEqual(self.doc["kind"], KIND)
        self.assertEqual(self.doc["schema_version"], SCHEMA_VERSION)

    def test_generated_from_is_exactly_eight(self):
        meta = self.doc["generated_from"]
        self.assertEqual(set(meta), GENERATED_FROM_KEYS)
        self.assertEqual(meta["quarters_version"], QUARTERS_VERSION)
        self.assertEqual(meta["snapshot_date"], SNAPSHOT_DATE)
        for key in ("search_index_sha256", "address_rows_sha256"):
            self.assertRegex(meta[key], SHA256_RE, key)
        for key in ("entries_digest", "rows_digest"):
            self.assertRegex(meta[key], DIGEST_RE, key)

    def test_cells_names_and_parents(self):
        self.assertEqual(len(self.doc["codes"]), CELL_COUNT)
        self.assertEqual(len(self.doc["names"]), CELL_COUNT)
        self.assertEqual(len(self.doc["parents"]), CELL_COUNT)
        for code in self.doc["codes"]:
            self.assertRegex(code, CODE_RE, code)
        self.assertEqual(self.doc["codes"], sorted(self.doc["codes"]),
                         u"кодовете не са сортирани (О27)")
        for name in self.doc["names"] + self.doc["parents"]:
            self.assertIsInstance(name, str)

    def test_cell_arrays_are_whole_numbers_in_range(self):
        top = len(self.doc["codes"]) - 1
        for field, expected in (("entry_cell", ENTRY_COUNT), ("row_cell", ROW_COUNT)):
            values = self.doc[field]
            self.assertEqual(len(values), expected, field)
            bad = [v for v in values if not isinstance(v, int) or isinstance(v, bool)
                   or v < -1 or v > top]
            self.assertEqual(bad[:5], [], u"%s носи стойност извън [-1, %d]"
                             % (field, top))

    def test_the_measured_number_of_silenced_cells(self):
        """The word is silenced at the BUILD, and by exactly as much as measured."""
        self.assertEqual(sum(1 for v in self.doc["entry_cell"] if v == -1),
                         ENTRY_MINUS_ONE)
        self.assertEqual(sum(1 for v in self.doc["row_cell"] if v == -1),
                         ROW_MINUS_ONE)


class QuarterIndexPrivacyTest(unittest.TestCase):
    """ИБ1-Г8 (в) — zero geometry, zero floats, zero forbidden keys (§3.Г)."""

    def setUp(self):
        self.doc = json.loads(delivered_bytes(self).decode("utf-8"))

    def test_no_forbidden_key_anywhere(self):
        keys = set()
        walk_keys(self.doc, keys)
        self.assertEqual(sorted(keys & FORBIDDEN_KEYS), [])

    def test_no_float_anywhere(self):
        floats = []
        walk_floats(self.doc, "", floats)
        self.assertEqual(floats[:5], [], u"доставката носи float — §3.Г забранява")


class PositionalJoinTest(unittest.TestCase):
    """STOP 17 — the delivery and the two payloads are ONE delivery.

    `generated_from` names the sha256 and the length of both payloads; if either
    was re-exported without this file, the join is broken and every quarter word
    on the screen would belong to another address.
    """

    def setUp(self):
        self.meta = json.loads(delivered_bytes(self).decode("utf-8"))["generated_from"]

    def payload(self, rel):
        raw = blob_bytes(rel)
        if raw is None:
            self.fail(u"липсва блоб: %s" % rel)
        return raw

    def test_search_index_sha_and_count(self):
        raw = self.payload(SEARCH_INDEX_REL)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), self.meta["search_index_sha256"])
        self.assertEqual(len(json.loads(raw.decode("utf-8"))["entries"]),
                         self.meta["entry_count"])
        self.assertEqual(self.meta["entry_count"], ENTRY_COUNT)

    def test_address_rows_sha_and_count(self):
        raw = self.payload(ADDRESS_ROWS_REL)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), self.meta["address_rows_sha256"])
        self.assertEqual(len(json.loads(raw.decode("utf-8"))["rows"]),
                         self.meta["address_row_count"])
        self.assertEqual(self.meta["address_row_count"], ROW_COUNT)


class DeliveredByPetarTest(unittest.TestCase):
    """D16 as a GATE (план §3.А Ф6) — the hand on the data commit is Petar's.

    `gates/release.py` knows one human author and three readers of that rule; the
    quarter index is not in `signable()`, so this is its only machine judge.
    """

    def test_last_author_of_the_delivered_path(self):
        out = git_bytes("log", "-1", "--format=%an", "--", DELIVERED_REL)
        author = (out or b"").decode("utf-8", "replace").strip()
        self.assertTrue(author, u"%s няма комит — К8 още не е положен (ИНТЕРВАЛ А)"
                        % DELIVERED_REL)
        self.assertEqual(author, release.HUMAN_AUTHOR,
                         u"данните ги комитва ръката на Петър (D16), не %r" % author)


class CorpusTest(unittest.TestCase):
    """Ф11 — the fixture of every client gate, pinned by sha and closed in shape."""

    def setUp(self):
        self.raw = corpus_bytes(self)
        self.doc = json.loads(self.raw.decode("utf-8"))

    def test_sha256_and_size(self):
        self.assertEqual(len(self.raw), CORPUS_BYTES)
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), CORPUS_SHA256)

    def test_two_storey_white_list(self):
        self.assertEqual(set(self.doc), CORPUS_TOP_KEYS)
        self.assertEqual(len(self.doc["queries"]), CORPUS_QUERIES)
        self.assertEqual(len(self.doc["entries"]), CORPUS_ENTRIES)
        for query in self.doc["queries"]:
            self.assertIsInstance(query, str)
        for entry in self.doc["entries"]:
            self.assertEqual(set(entry), CORPUS_ENTRY_KEYS, entry)
            self.assertIsInstance(entry["kind"], str)
            self.assertIsInstance(entry["cell"], int)
            self.assertTrue(all(isinstance(t, str) for t in entry["tk"]), entry)

    def test_every_corpus_cell_matches_the_delivery(self):
        """The corpus is a PROJECTION of the delivery: same cells, same order.

        The 145 entries carrying the token `studentska` are the flagship's
        neighbourhood; their cell is the one the delivered file gives them.
        """
        doc = json.loads(delivered_bytes(self).decode("utf-8"))
        top = len(doc["codes"]) - 1
        for entry in self.doc["entries"]:
            self.assertTrue(-1 <= entry["cell"] <= top, entry)
        cells = {entry["cell"] for entry in self.doc["entries"]}
        self.assertTrue(cells - {-1}, u"корпусът не носи нито една клетка")


if __name__ == "__main__":
    unittest.main()
