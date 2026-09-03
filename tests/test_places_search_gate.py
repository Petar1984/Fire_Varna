# -*- coding: utf-8 -*-
"""The П7 gate in the suite — §11 Р7 of docs/plans/places_phase2_plan.md.

Until C16 nothing here could go red without a human reading a report:
`recall_sweep.py` always exited 0 and the probe only failed on a console error
(C14 finding 3 / §11 Р7). This module makes the reference itself the gate:

  1. importing `scratch/places_search/recall_sweep.py` must write NOT ONE BYTE
     (the `if __name__` guard) — measured in a subprocess, sha before/after;
  2. the П7 gains and controls of §11 Р3/С2′–С4′ — {name, zone, kind} AND the
     branch, not a row count; К2 (§12, д) replaced the differential control
     „училище бриз“, which did not differentiate, with „детска градина
     приморски“, which does (12 rows on M2-failopen with the guard, 4 on A3
     without it), and gates the guard itself here;
  3. `p7_added` is exactly the six tokens in five zones §11 v2.1 measured;
  4. the frozen diff: the 72 queries that existed before П7 give byte-identical
     ordered rows and the same branch as `git show 7a6ea1d:…rows.json` — with
     the ONE signed exception of ЛОТ 1 решение 2 („градина“), named below;
  5. ЛОТ 1 (решения 2 и 1, signed 03.09): the new gate, the four rows of the 103
     the two rules move, and the proof that each rule is load-bearing — inverted
     in place, the old answer comes back.

Read-only: it runs `git show` through subprocess and touches nothing on disk.
"""
import hashlib
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
REFERENCE = REPO / "scratch" / "places_search" / "recall_sweep.py"
ROWS = REPO / "scratch" / "places_search" / "recall_sweep_rows.json"
FROZEN_COMMIT = "7a6ea1d"          # C15 — the last HEAD before П7 was written
FROZEN_PATH = "scratch/places_search/recall_sweep_rows.json"
OLD_BUCKETS = ("gate_m5_a8", "extra")
# ЛОТ 1, the signed change list (docs/plans/recommendations_2026-09-03.md §1,
# решения 2 и 1): FOUR rows of the 103 move, and these are they. Решение 2 moves
# „градина“ inside the 72 frozen at 7a6ea1d; решение 1 moves three П7 controls.
LOT1_PREPENDED = {u"градина": (u"ГРАДИНА", u"к.к. Чайка")}
LOT1_MOVED_P7 = {
    u"хотел приморски": (u"A3-record+zone-phrase", 5,
                         [(u"ПРИМОРСКИ", u"к.к. Св. Константин"),
                          (u"Маргарита", u"район Приморски")]),
    u"училище свети никола": (u"A3-record+zone-phrase", 1,
                              [(u'Професионална гимназия по химични и хранително-вкусови '
                                u'технологии "Д. И. Менделеев"', u"м-т Свети Никола")]),
    u"хотел зеленика": (u"A3-record+zone-phrase", 2,
                        [(u"Зеленика", u"с.о. Зеленика"), (u"Джоя", u"м. Зеленика")]),
}


def load_reference():
    """Import the reference as a module. The guard is what makes this safe."""
    spec = importlib.util.spec_from_file_location("recall_sweep_gate", REFERENCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frozen_rows():
    """The baseline as git holds it — never as the working tree holds it."""
    out = subprocess.run(["git", "-C", str(REPO), "show",
                          FROZEN_COMMIT + ":" + FROZEN_PATH],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise AssertionError("git show %s:%s failed: %s"
                             % (FROZEN_COMMIT, FROZEN_PATH,
                                out.stderr.decode("utf-8", "replace")))
    return json.loads(out.stdout.decode("utf-8"))


REF = load_reference()


class ImportGuardTest(unittest.TestCase):
    """§11 Р9 / C14 finding 3: the module is a module, not a script."""

    def test_import_writes_nothing(self):
        before = hashlib.sha256(ROWS.read_bytes()).hexdigest()
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        # argv[1] is a lie the runner tells: on import the module must ignore it
        # and keep the signed default instead of raising SystemExit.
        proc = subprocess.run([sys.executable, "-c",
                               "import importlib.util,sys;"
                               "spec=importlib.util.spec_from_file_location('rs', sys.argv[1]);"
                               "m=importlib.util.module_from_spec(spec);"
                               "spec.loader.exec_module(m);"
                               "print(m.CAPMODE, len(m.RECS))",
                               str(REFERENCE), "discover"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
        self.assertEqual(proc.returncode, 0,
                         proc.stderr.decode("utf-8", "replace"))
        self.assertEqual(proc.stdout.decode("utf-8").split(), ["plan", "361"])
        after = hashlib.sha256(ROWS.read_bytes()).hexdigest()
        self.assertEqual(before, after, "importing recall_sweep.py rewrote the reference rows")

    def test_capmode_is_an_explicit_list(self):
        self.assertEqual(REF.CAPMODES, ("plan", "poi"))
        with self.assertRaises(SystemExit):
            REF.set_capmode(["recall_sweep.py", "cap_poi"])
        REF.set_capmode(["recall_sweep.py"])          # back to the signed default
        self.assertEqual(REF.CAPMODE, "plan")


class P7RuleTest(unittest.TestCase):
    """§11 v2.1: six tokens, five zones — and nothing in the name path."""

    def test_added_tokens_are_the_measured_six(self):
        self.assertEqual(REF.P7_ADDED, REF.P7_EXPECTED)
        self.assertEqual(sum(len(v) for v in REF.P7_ADDED.values()), 6)
        self.assertEqual(len(REF.P7_ADDED), 5)

    def test_no_added_token_is_a_name_token(self):
        """Р4: the claim holds for `nset`; `varnenchik` IS an old-name token of
        one hotel (КАРНИВАЛ) and that is accepted explicitly, with the measure."""
        added = set(t for tokens in REF.P7_ADDED.values() for t in tokens)
        names = set()
        for rec in REF.RECS:
            names |= rec.nset
        self.assertEqual(added & names, set())
        aliases = set()
        for rec in REF.RECS:
            aliases |= rec.aset
        self.assertEqual(added & aliases, {"varnenchik"})

    def test_added_tokens_are_zone_tokens_only(self):
        """The whole safety of П7: never ntk/nset/aset, only ztk/zkset."""
        for rec in REF.RECS:
            for token in rec.p7:
                self.assertIn(token, rec.zkset, rec.name)
                self.assertNotIn(token, rec.nset, rec.name)
                self.assertNotIn(token, rec.aset, rec.name)

    def test_the_foreign_token_guard_is_load_bearing(self):
        """К2 (§12, д): the guard of step (д)/(д′), measured instead of asserted.

        The replaced control („детска градина приморски“) differentiates because
        of this: the foreign-token step is the ONLY thing that keeps `primorski`
        and `primorskiat` (own tokens of район Приморски) out of the zone tokens
        of Морска градина, and `asparuhovo` (кв. Аспарухово) out of ж.к. Дружба.
        The guard is fed by the OTHER zones of the delivery, so it can be starved
        without editing one byte of it — a call with a single zone has nothing
        foreign to compare against. Measured 03.09; the same four tokens that a
        copy of the reference with the step cut out adds back."""
        cats = json.loads((REPO / "data" / "place_categories.json").read_text(encoding="utf-8"))
        _, added, dropped = REF.zone_alias_tokens(cats, REF.ZONES_IN)
        # the tag is `foreign:<the foreign token>:<the candidate>` — „primorskiat“
        # falls against „primorski“ through the lev<=2 step (д′) of §11 Р1.
        for zone, token, tag in (
                (u"Морска градина", "primorski", "foreign:primorski:primorski"),
                (u"Морска градина", "primorskiat", "foreign:primorski:primorskiat"),
                (u"м-т Салтанат", "primorski", "foreign:primorski:primorski"),
                (u"ж.к. Дружба", "asparuhovo", "foreign:asparuhovo:asparuhovo")):
            self.assertNotIn(token, added.get(zone, []), zone)
            self.assertIn(tag, dropped.get(zone, []), zone)
        _, alone, _ = REF.zone_alias_tokens(cats, [u"Морска градина"])
        self.assertEqual(alone.get(u"Морска градина"), ["primorski", "primorskiat"])
        _, alone, _ = REF.zone_alias_tokens(cats, [u"ж.к. Дружба"])
        self.assertEqual(alone.get(u"ж.к. Дружба"), ["asparuhovo"])

    def test_fail_soft_without_a_dictionary(self):
        """С7′: no `zones`, a `zones` that is not an object, aliases that are not
        a list of strings — П7 switches off, nothing raises."""
        zones = REF.ZONES_IN
        for doc in (None, {}, {"zones": None}, {"zones": []}, {"zones": "x"},
                    {"zones": {"кв. Изгрев": None}},
                    {"zones": {"кв. Изгрев": {"aliases": "ж.к. Изгрев"}}},
                    {"zones": {"кв. Изгрев": {"aliases": [1, None]}}}):
            extra, added, dropped = REF.zone_alias_tokens(doc, zones)
            self.assertEqual(added, {}, repr(doc))
            self.assertEqual(extra, {}, repr(doc))


class P7GateTest(unittest.TestCase):
    """§11 Р3/С2′–С4′ — the gains and the controls, branch included."""

    def test_gate(self):
        failures = REF.check_p7_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_gate_actually_covers_every_added_token(self):
        """С2′: one query per added token, or the parity proves nothing."""
        queries = " ".join(q for q, _, _, _, _ in REF.P7_GAINS)
        for tokens in REF.P7_ADDED.values():
            for token in tokens:
                self.assertTrue(
                    any(t.s == token for t in REF.place_tokens(queries)),
                    "no gate query exercises the added token " + token)


class FrozenDiffTest(unittest.TestCase):
    """С5′: the 72 queries that existed before П7 must not have moved."""

    @classmethod
    def setUpClass(cls):
        cls.frozen = frozen_rows()

    def test_seventy_two_queries_unchanged_live(self):
        """Re-run through the LIVE reference, not through the artefact.

        ЛОТ 1 решение 2 moves exactly ONE of the 72: „градина“ now carries the
        hotel ГРАДИНА above the 46 kindergartens, which keep their own order.
        The exception is named in LOT1_PREPENDED; any other movement is red."""
        compared, rows, prepended = 0, 0, 0
        for bucket in OLD_BUCKETS:
            for entry in self.frozen[bucket]:
                got, branch = REF.search(entry["q"])
                want = [(r["name"], r["zone"]) for r in entry["rows"]]
                if entry["q"] in LOT1_PREPENDED:
                    want = [LOT1_PREPENDED[entry["q"]]] + want
                    prepended += 1
                self.assertEqual(branch, entry["branch"], entry["q"])
                self.assertEqual([(r.name, r.zone) for r in got], want, entry["q"])
                compared += 1
                rows += len(want)
        self.assertEqual(compared, 72)
        self.assertEqual(prepended, 1)
        self.assertEqual(rows, 1338)

    def test_committed_rows_match_the_frozen_baseline(self):
        """And the artefact the probe replays says the same thing."""
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        for bucket in OLD_BUCKETS:
            self.assertEqual(
                [(e["q"], e["branch"], [(r["name"], r["zone"]) for r in e["rows"]])
                 for e in current[bucket]],
                [(e["q"], e["branch"], [(r["name"], r["zone"]) for r in e["rows"]])
                 for e in self.frozen[bucket]])

    def test_rows_carry_the_p7_measure(self):
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        self.assertEqual(current["_meta"]["p7_added"], REF.P7_EXPECTED)
        self.assertEqual(current["_meta"]["p7_tokens"], 6)
        self.assertEqual(current["_meta"]["p7_zones_with_aliases"], 5)
        self.assertEqual(len(current["gate_p7"]),
                         len(REF.P7_GAINS) + len(REF.P7_CONTROLS))
        for entry in current["gate_p7"]:
            self.assertTrue(entry["ok"], entry["q"])


class Lot1GateTest(unittest.TestCase):
    """ЛОТ 1 — the two client rules of решения 2 и 1, signed 03.09."""

    def test_gate(self):
        failures = REF.check_lot1_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_three_moved_p7_rows_and_no_others(self):
        """The П7 bucket of the frozen artefact, re-run live: exactly the three
        rows of the signed list answer differently, every other one is byte-equal
        (name, zone and branch). The artefact itself is re-frozen in F2, not here."""
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        moved = 0
        for entry in current["gate_p7"]:
            got, branch = REF.search(entry["q"])
            if entry["q"] in LOT1_MOVED_P7:
                want_branch, want_n, want_first = LOT1_MOVED_P7[entry["q"]]
                self.assertEqual(branch, want_branch, entry["q"])
                self.assertEqual(len(got), want_n, entry["q"])
                self.assertEqual([(r.name, r.zone) for r in got][:len(want_first)],
                                 want_first, entry["q"])
                moved += 1
            else:
                self.assertEqual(branch, entry["branch"], entry["q"])
                self.assertEqual([(r.name, r.zone) for r in got],
                                 [(r["name"], r["zone"]) for r in entry["rows"]],
                                 entry["q"])
        self.assertEqual(moved, 3)

    def test_the_exact_name_prepend_is_load_bearing(self):
        """Решение 2, inverted in place: with an empty exact-name index „градина“
        falls back to the 46 kindergartens. Restored, the hotel is first again."""
        saved = REF.EXACT_NAME
        try:
            REF.EXACT_NAME = {}
            rows, branch = REF.search(u"градина")
            self.assertEqual((branch, len(rows)), ("M1-category", 46))
        finally:
            REF.EXACT_NAME = saved
        rows, branch = REF.search(u"градина")
        self.assertEqual((branch, len(rows), rows[0].name), ("M1-category", 47, u"ГРАДИНА"))

    def test_the_zone_phrase_override_is_load_bearing(self):
        """Решение 1, inverted in place: with no phrase on any record the three
        moved rows fall back to the answers the frozen artefact holds."""
        queries = (u"хотел приморски", u"училище свети никола", u"хотел зеленика")
        saved = [(rec, rec.zph) for rec in REF.RECS]
        try:
            for rec in REF.RECS:
                rec.zph = set()
            self.assertEqual([(REF.search(q)[1], len(REF.search(q)[0])) for q in queries],
                             [("M2", 1), ("M2", 8), ("M2", 1)])
        finally:
            for rec, zph in saved:
                rec.zph = zph
        self.assertEqual([(REF.search(q)[1], len(REF.search(q)[0])) for q in queries],
                         [("A3-record+zone-phrase", 5), ("A3-record+zone-phrase", 1),
                          ("A3-record+zone-phrase", 2)])

    def test_a_phrase_is_the_canonical_zone_or_an_accepted_p7_form(self):
        """The admissibility rule, measured: „Приморски парк“ is an alias of
        Морска градина that П7 threw out as foreign, so it is NOT a phrase there
        — which is the whole difference between „хотел приморски“ = 5 and = 23.
        „кв. Владиславово“ was accepted by П7, so it IS one."""
        self.assertEqual(REF.ZONE_PHRASES[u"Морска градина"], {"morska gradina"})
        self.assertEqual(REF.ZONE_PHRASES[u"район Приморски"], {"primorski"})
        self.assertEqual(REF.ZONE_PHRASES[u"район Одесос"], {"odesos"})
        self.assertIn("vladislavovo", REF.ZONE_PHRASES[u"ж.к. Владислав Варненчик"])
        self.assertIn("zpz", REF.ZONE_PHRASES[u"Западна промишлена зона"])
        for zone, phrases in REF.ZONE_PHRASES.items():
            for phrase in phrases:
                for token in phrase.split(" "):
                    self.assertNotIn(token, ("raion", "kvartal", "kompleks", "zona",
                                             "mestnost", "park", "chast"), zone)

    def test_the_exact_index_carries_current_names_only(self):
        """Решение 2 and the data judge: old_names stay OUT of the exact index."""
        aliases = set()
        for rec in REF.RECS:
            aliases |= rec.aset
        for key, recs in REF.EXACT_NAME.items():
            for rec in recs:
                self.assertEqual(key, u" ".join(rec.ntk), rec.name)
        for token in aliases:
            if token in REF.EXACT_NAME:
                self.assertTrue(any(rec.ntk == [token] for rec in REF.EXACT_NAME[token]),
                                token)


if __name__ == "__main__":
    unittest.main()
