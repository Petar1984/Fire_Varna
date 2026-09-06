# -*- coding: utf-8 -*-
"""Лот Н3-а — five S17 regression fixtures against TODAY'S frozen behaviour.

Plan: `docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md` §3 Н3-а and the script
contract in §2а. What this module is and — just as important — what it is not:

  * it FREEZES what the search answers TODAY, on today's delivery, for five
    queries that the SIGNED_POLYGON channel of Б2 is going to walk straight
    through (S7 а–ж of `ПЛАН_ЛОТ_Границите_v2_амандамент_1_05.09.md:25`);
  * it is NOT an acceptance criterion. Not one number here says what the answer
    OUGHT to be. Tomorrow F13 turns these rows into candidate expectations —
    signed by Petar — and until then a red test means „the behaviour moved“,
    never „the behaviour is wrong“.

The engine under test is the Python parity of the client search,
`scratch/places_search/recall_sweep.py` — the same reference the frozen gate in
`tests/test_places_search_gate.py` imports, with the same import guard (the
module writes not one byte on import).

The fixtures live in `scratch/places_search/granitsi_fixtures_06.09.json` and
every one of them carries a `_broken` variant: an explicitly named mutation of
the delivery — a quarter written the way Б2 would write it — that MUST make the
very same assertion fail. A fixture without a `_broken` variant is red, because
a green check that was never seen to fail is not evidence (§0 т. 6 of the plan).

How a candidate delivery is run: the reference builds its index at import time
out of `data/hotels.json` + `data/places.json`, so `reindex()` below rebuilds
exactly the six module-level structures that depend on the records (RECS,
EXACT_NAME, EXACT_ALIAS, STREET, CLASS_OF, GROUP_SIZE) over the mutated rows.
Nothing is written to disk, the module object is private to this test file, and
every measurement re-loads the untouched bundles first.

Run: python -m unittest tests.test_granitsi_fixtures
     python -m unittest discover -s tests
"""
import copy
import importlib.util
import json
import pathlib
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
REFERENCE = REPO / "scratch" / "places_search" / "recall_sweep.py"
FIXTURES = REPO / "scratch" / "places_search" / "granitsi_fixtures_06.09.json"

# The five the plan names. `client_cache_matrix` and the Възраждане variant of
# `parent_child` are deferred ON PURPOSE and the fixture file says why in words.
EXPECTED_NAMES = ("street_collision", "district_retention",
                  "mladost_kind_collision", "order_identity", "parent_child")


def load_reference():
    """Import the reference as a private module — its own guard makes it safe."""
    spec = importlib.util.spec_from_file_location("recall_sweep_granitsi", REFERENCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_bundles(reference):
    """The two delivered bundles, read the way the reference itself reads them."""
    hotels = json.loads(pathlib.Path(reference.HOTELS).read_text(encoding="utf-8"))
    places = json.loads(pathlib.Path(reference.PLACES2).read_text(encoding="utf-8"))
    return hotels["hotels"], places["places"]


def apply_ops(hotels, places, ops):
    """The mutation of a `_broken` candidate, by NAME — never by ordinal.

    An op that does not hit exactly one row is an error, not a silent no-op: a
    fixture that stops biting because the delivery was renamed underneath it
    would go green for the wrong reason.
    """
    hotels = copy.deepcopy(hotels)
    places = copy.deepcopy(places)
    for op in ops:
        rows = hotels if op["bundle"] == "hotels" else places
        hit = [row for row in rows if row["name"] == op["name"]]
        if len(hit) != 1:
            raise LookupError("mutation matches %d rows, expected 1: %s"
                              % (len(hit), op["name"]))
        for field, value in op["set"].items():
            hit[0][field] = value
    return hotels, places


def reindex(reference, hotels, places):
    """Rebuild every record-derived structure of the reference over `hotels`+`places`.

    1:1 with the module body of `recall_sweep.py` (RECS at :692, EXACT_NAME at
    :698, EXACT_ALIAS at :707, STREET at :722, CLASS_OF at :803, GROUP_SIZE at
    :834). The ordinals are kept, so the legacy words of a row — keyed by
    `bundle:ordinal` — stay on the row they belong to.
    """
    reference.hotels = hotels
    reference.places2 = places
    reference.RECS = ([reference.Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
                      + [reference.Rec(p, u"places", n) for n, p in enumerate(places)])
    reference.EXACT_NAME = {}
    for rec in reference.RECS:
        reference.EXACT_NAME.setdefault(u" ".join(rec.ntk), []).append(rec)
    reference.EXACT_ALIAS = {}
    for rec in reference.RECS:
        for index, old in enumerate(rec.old_names):
            key = reference.key_of(old)
            if not key:
                continue
            bucket = reference.EXACT_ALIAS.setdefault(key, [])
            if not any(other is rec for other, _i in bucket):
                bucket.append((rec, index))
    reference.STREET = {}
    for rec in reference.RECS:
        if rec.spk:
            reference.STREET.setdefault(rec.spk, []).append(rec)
    reference.CLASS_OF = {}
    for form_key in reference.FORM_IDX:
        reference.CLASS_OF[form_key] = [r for r in reference.RECS
                                        if reference.in_class(r, form_key)]
    reference.GROUP_SIZE = {}
    for rec in reference.RECS:
        group = reference.group_of(rec)
        reference.GROUP_SIZE[group] = reference.GROUP_SIZE.get(group, 0) + 1


def answer(reference, query, ops=()):
    """The measured answer of today's engine over a candidate delivery.

    `with_quarter` / `without_quarter` are part of the measurement because the
    whole Границите lot turns on that split: the bare-location branch reaches a
    район row ONLY while its `quarter` is null (`recall_sweep.py:1174`), so a
    written quarter is exactly what can make a row disappear.
    """
    hotels, places = base_bundles(reference)
    if ops:
        hotels, places = apply_ops(hotels, places, ops)
    reindex(reference, hotels, places)
    rows, branch = reference.search(query)
    measured = {
        "branch": branch,
        "n": len(rows),
        "with_quarter": sum(1 for r in rows if r.quarter),
        "without_quarter": sum(1 for r in rows if not r.quarter),
        "identities": [[r.name, r.zone] for r in rows],
    }
    reindex(reference, *base_bundles(reference))       # never leave a mutation behind
    return measured


def fixtures_doc():
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


class GranitsiFixturesTest(unittest.TestCase):
    """The five fixtures, their five broken candidates, and the file itself."""

    @classmethod
    def setUpClass(cls):
        cls.reference = load_reference()
        cls.doc = fixtures_doc()
        cls.cases = {case["name"]: case for case in cls.doc["fixtures"]}

    # ---- the file is a contract before it is a measurement --------------------
    def test_the_five_fixtures_are_there_and_each_carries_a_broken_variant(self):
        """§2а: a missing `_broken` is red — a check nobody saw fail proves nothing."""
        self.assertEqual(tuple(case["name"] for case in self.doc["fixtures"]),
                         EXPECTED_NAMES)
        for name, case in self.cases.items():
            with self.subTest(fixture=name):
                self.assertIn("_broken", case, "фикстура без `_broken` вариант")
                broken = case["_broken"]
                self.assertTrue(broken.get("ops"), "`_broken` без мутация")
                self.assertTrue(broken.get("mutation", "").strip(),
                                "мутацията трябва да е записана дословно")
                self.assertIn("observed", broken)
                for op in broken["ops"]:
                    self.assertIn(op["bundle"], ("hotels", "places"))
                    self.assertTrue(op["name"])
                    self.assertTrue(op["set"])

    def test_the_two_deferred_fixtures_are_named_with_their_reason(self):
        """Н3-а defers two of the six S17 fixtures; silence is not a deferral."""
        deferred = self.doc["_meta"]["deferred"]
        self.assertEqual(sorted(deferred), ["client_cache_matrix", "parent_child_vazrazhdane"])
        for name, reason in deferred.items():
            with self.subTest(deferred=name):
                self.assertTrue(reason.strip())

    def test_the_measured_inputs_are_the_delivery_this_repo_carries(self):
        """The frozen behaviour is worth the bytes it was measured on."""
        import hashlib
        for relative, recorded in self.doc["_meta"]["inputs"].items():
            with self.subTest(path=relative):
                raw = (REPO / relative).read_bytes().replace(b"\r\n", b"\n")
                self.assertEqual(hashlib.sha256(raw).hexdigest(), recorded)

    # ---- the assertion itself -------------------------------------------------
    def assert_case(self, case, measured):
        """The ONE comparison both halves use: branch, split and ORDERED identities."""
        self.assertEqual(measured["branch"], case["today"]["branch"])
        self.assertEqual(measured["n"], case["today"]["n"])
        self.assertEqual(measured["with_quarter"], case["today"]["with_quarter"])
        self.assertEqual(measured["without_quarter"], case["today"]["without_quarter"])
        self.assertEqual([list(row) for row in measured["identities"]],
                         [list(row) for row in case["today"]["identities"]])

    def test_todays_behaviour_is_what_the_fixture_file_recorded(self):
        for name in EXPECTED_NAMES:
            case = self.cases[name]
            with self.subTest(fixture=name):
                self.assert_case(case, answer(self.reference, case["query"]))

    def test_every_broken_candidate_makes_the_same_assertion_fail(self):
        """The negative half: each mutation MUST break its own fixture."""
        for name in EXPECTED_NAMES:
            case = self.cases[name]
            broken = case["_broken"]
            with self.subTest(fixture=name):
                measured = answer(self.reference, case["query"], broken["ops"])
                with self.assertRaises(AssertionError):
                    self.assert_case(case, measured)
                # and the damage itself is pinned, so the report can quote it
                self.assertEqual(measured["branch"], broken["observed"]["branch"])
                self.assertEqual(measured["n"], broken["observed"]["n"])
                self.assertEqual([list(row) for row in measured["identities"]],
                                 [list(row) for row in broken["observed"]["identities"]])
                self.assertEqual(
                    sorted(tuple(row) for row in measured["identities"])
                    == sorted(tuple(row) for row in case["today"]["identities"]),
                    broken["set_identical"])


if __name__ == "__main__":
    unittest.main()
