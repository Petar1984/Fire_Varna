# -*- coding: utf-8 -*-
"""D-25 — a ring of NAMED points is geometry too (B3 G11).

    python -m unittest tests.test_b3_g11_named_ring

Measured at 37db9ca: `gates/probe/b3_g11.py` judged a payload by three key NAMES
(`GEO`, :37), so a polygon serialised as `[{"lat": …, "lon": …}, …]` under a
harmless key walked straight through the privacy gate. The third declared
extension of the signed S29-4 script, `named_ring()`, flags a list of `RING_MIN`
or more dicts whose keys are a SUBSET of the lat/lon vocabulary.

What the four tests pin, and why each one is needed:

  1. the hit itself, with the JSON pointer of the LIST — a rule that fires with a
     wrong pointer sends the reader to the wrong place;
  2. the threshold is honest — three points are not a ring, so the rule cannot be
     quietly turned into "any pair of coordinates";
  3. the shape of the LIVE payloads stays green — `data/places.json`,
     `data/hotels.json` and `data/removed_hydrants.json` carry `lat`/`lon`
     lawfully, and a row that also carries a `name` key is not a vertex. This is
     the test that would go red if somebody widened the rule to the key names;
  4. the extension is ADDITIVE — `walk()` and `GEO` still flag what they flagged,
     `named_ring()` adds nothing of its own to that verdict, and a ring that sits
     UNDER a GEO key, which both judges see, is reported ONCE: `main()` drops the
     duplicate hits in order and this test pins the single hit.

`FIRE_VARNA_B3_G11_PATH` points the assertions at another copy of the gate and
defaults to the tree's file; the negative half of плана §2 К6 runs them against a
copy outside the tree whose `RING_MIN` is 99 and was measured to fall.

Every number below is obviously fake (1.0 / 2.0 and counters) — плана §0.6: a
tracked file of this repo carries no real coordinate.
"""
import importlib.util
import os
import pathlib
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
GATE_PATH = pathlib.Path(os.environ.get("FIRE_VARNA_B3_G11_PATH")
                         or (REPO / "gates" / "probe" / "b3_g11.py"))


def load_gate():
    spec = importlib.util.spec_from_file_location("b3_g11_under_test", GATE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fake_vertex(step):
    """A vertex with no information in it: the pair (1.0, 2.0) walked by `step`."""
    return {"lat": 1.0 + step, "lon": 2.0 + step}


class NamedRingIsGeometry(unittest.TestCase):

    def setUp(self):
        self.gate = load_gate()

    def test_a_ring_of_four_named_points_is_a_hit(self):
        doc = {"_meta": {"outline": [fake_vertex(i) for i in range(4)]}}
        hits = []
        self.gate.named_ring(doc, "", hits)
        self.assertEqual(
            [("/_meta/outline", list)], hits,
            "named_ring did not flag the ring of four named points at "
            "/_meta/outline; got %r" % (hits,))

    def test_three_named_points_are_not_a_ring(self):
        doc = {"_meta": {"outline": [fake_vertex(i) for i in range(3)]}}
        hits = []
        self.gate.named_ring(doc, "", hits)
        self.assertEqual([], hits, "the threshold is not honest: %r" % (hits,))

    def test_a_long_list_of_named_rows_stays_green(self):
        rows = [dict(fake_vertex(i), name="row %d" % i) for i in range(150)]
        hits = []
        self.gate.named_ring({"rows": rows}, "", hits)
        self.assertEqual(
            [], hits,
            "a row with a name key is not a vertex; this shape is the one "
            "places.json, hotels.json and removed_hydrants.json deliver: %r"
            % (hits,))

    def test_the_extension_is_additive(self):
        doc = {"_meta": {"geometry": "заявена форма"}}
        walk_hits = []
        self.gate.walk(doc, "", walk_hits)
        self.assertEqual([("/_meta/geometry", str)], walk_hits,
                         "the signed GEO rule no longer fires: %r" % (walk_hits,))
        ring_hits = []
        self.gate.named_ring(doc, "", ring_hits)
        self.assertEqual([], ring_hits,
                         "named_ring invented a hit of its own: %r" % (ring_hits,))
        # A ring UNDER a GEO key is the one shape both judges flag; main() keeps
        # the first of the duplicates, so the reader is sent there exactly once.
        under_geo = {"geometry": [fake_vertex(i) for i in range(4)]}
        both = []
        self.gate.walk(under_geo, "", both)
        self.gate.named_ring(under_geo, "", both)
        self.assertEqual(
            [("/geometry", list)], list(dict.fromkeys(both)),
            "a ring under a GEO key must be reported once, not twice: %r"
            % (both,))


if __name__ == "__main__":
    unittest.main()
