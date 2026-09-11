# -*- coding: utf-8 -*-
"""Ф15 · ИБ1-Г21 — the amendment carries its six decisions, and it came FIRST.

    python -m unittest tests.test_adr_amendment

Д2 (`docs/decisions/011a_амандамент_И-Б1_11.09.md`) is what lets this lot touch the
address path at all: ADR 006 **D12** pins the two payloads and every function of
`initAddressSearch`, and ADR 011 **G29** keeps geometry out of every public payload.
The amendment names both and replaces the write-set of ADR 007 (И-Б1-D6). A lot
whose permission slip lost a line is a lot without permission.

Two halves of one rule (план §5 Г21):

  * the TEXT — the six decisions `И-Б1-D1 … И-Б1-D6`, plus `D12` and `G29`, each
    present in the document. This half runs from the moment К4 exists;
  * the ORDER — К4 is an ancestor of К8 (the data) and of К9 (the client). Before
    those two commits are born, `git merge-base --is-ancestor` has no target and
    exits **128 without a verdict** (О7), so the check names itself SKIPPED instead
    of dressing a missing commit as a green gate. From стъпка 16 on, both targets
    exist and the check is a real one.

Зелен от раждането си (ИНТЕРВАЛ А, план §4 стъпка 9): the text is in the tree at
К4, so this module is the one member of the К7 set that is green from the start.

Negative halves (план §5 Г21): a copy with `И-Б1-D5` removed, fed in through
**FIRE_VARNA_AMENDMENT_PATH** → 1; in `ib_clone`, К4 committed AFTER К8 → the
ancestry check falls → 1.

Run: python -m unittest discover -s tests
"""
import os
import pathlib
import subprocess
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]

AMENDMENT_REL = "docs/decisions/011a_амандамент_И-Б1_11.09.md"
AMENDMENT = pathlib.Path(os.environ.get("FIRE_VARNA_AMENDMENT_PATH")
                         or (REPO / AMENDMENT_REL))
# The index the ADR 011 amendment is pointed at from (Р5-Б).
ADR_011_REL = "docs/decisions/011_kartata_imot.md"

DECISIONS = tuple(u"И-Б1-D%d" % n for n in range(1, 7))
PINNED_RULES = (u"D12", u"G29")

# The two commits whose ancestry the order half judges, each found by what it
# DELIVERED — never by a hash written into a test.
DELIVERED_REL = "data/address_quarters.json"
CLIENT_NEEDLE = "// IB1 address slice start"


def git(*args):
    proc = subprocess.run(["git", "-C", str(REPO)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace").strip()


def first_commit_of(rel):
    """The commit that ADDED a path — К4 for the amendment, К8 for the data."""
    code, out = git("log", "--diff-filter=A", "--format=%H", "--", rel)
    if code != 0 or not out:
        return None
    return out.split("\n")[-1]


def commit_that_introduced(needle, rel):
    """The commit that first wrote a string into a path — К9 by its marker."""
    code, out = git("log", "-S", needle, "--format=%H", "--", rel)
    if code != 0 or not out:
        return None
    return out.split("\n")[-1]


class AmendmentTextTest(unittest.TestCase):
    """ИБ1-Г21 (а) — the six decisions and the two pinned rules are in Д2."""

    def setUp(self):
        if not AMENDMENT.exists():
            self.fail(u"липсва амандаментът Д2: %s" % AMENDMENT)
        self.text = AMENDMENT.read_text(encoding="utf-8")

    def test_the_six_decisions(self):
        missing = [d for d in DECISIONS if d not in self.text]
        self.assertEqual(missing, [], u"амандаментът е без решения: %s" % missing)

    def test_the_two_pinned_rules(self):
        missing = [r for r in PINNED_RULES if r not in self.text]
        self.assertEqual(missing, [],
                         u"амандаментът не назовава пинатите правила: %s" % missing)

    def test_the_adr_carries_the_pointer(self):
        """Р5-Б — ADR 011 points at the amendment, so a reader of the ADR cannot
        miss it. Only checked for the tracked document, never for a fixture copy."""
        if os.environ.get("FIRE_VARNA_AMENDMENT_PATH"):
            self.skipTest(u"фикстура: указателят се проверява само за проследения Д2")
        adr = (REPO / ADR_011_REL)
        self.assertTrue(adr.exists(), ADR_011_REL)
        self.assertIn(pathlib.Path(AMENDMENT_REL).name,
                      adr.read_text(encoding="utf-8"),
                      u"ADR 011 няма ред-указател към амандамента")


class AmendmentOrderTest(unittest.TestCase):
    """ИБ1-Г21 (б) — К4 precedes К8 and К9 (О111, STOP 18)."""

    def setUp(self):
        if os.environ.get("FIRE_VARNA_AMENDMENT_PATH"):
            self.skipTest(u"фикстура: редът се съди само в истинското репо")
        self.k4 = first_commit_of(AMENDMENT_REL)
        if not self.k4:
            self.fail(u"К4 го няма в историята — амандаментът не е комитнат")

    def ancestor(self, child, label):
        if not child:
            self.skipTest(u"%s още не съществува — `merge-base` би върнал 128 "
                          u"без присъда (О7)" % label)
        code, _ = git("merge-base", "--is-ancestor", self.k4, child)
        self.assertEqual(code, 0, u"К4 не е предшественик на %s (STOP 18)" % label)

    def test_k4_precedes_the_data_commit(self):
        self.ancestor(first_commit_of(DELIVERED_REL), u"К8")

    def test_k4_precedes_the_client_commit(self):
        self.ancestor(commit_that_introduced(CLIENT_NEEDLE, "index.html"), u"К9")


if __name__ == "__main__":
    unittest.main()
