"""Static gate against ASCII-mojibake ('???' runs) in the built public data payloads.

Sibling of tests/test_ui_ascii_mojibake.py, which guards the app shell. This one guards
the two browser-shipping payloads produced by the Varna_buildings address pipeline:
data/search_index.json and data/address_rows.json. Text that went through a
'?'-substituting encoder is plain ASCII and slips past a classic mojibake scan, so it
has to be caught by its own signature: a run of 3+ question marks.

Baseline: EMPTY -- the upstream fix landed (13.08.2026)
------------------------------------------------------
This gate used to pin eight address labels in data/search_index.json whose street name
shipped as '?????'. The upstream fix landed with the Varna_buildings quarters-v1.1
cycle (ADR 062 there: the AGKK export's literal '?????' placeholder is repaired from
the row's OWN source -- sibling sections on the same parcel plus the parcel's strename
-- behind a sha256 lock, and a corrupt member no longer speaks for its cluster). The
regenerated payloads carry ZERO runs, measured over both files, so the baseline is now
empty and the assertions below read as a plain "zero runs anywhere".

KNOWN_BROKEN_LABELS is deliberately KEPT as an empty frozenset rather than deleted: the
byte-exact model stays in place, so re-pinning a future regression is a one-line change
and the gate's shape still documents how a known defect would be recorded.

Pure stdlib; runnable via `python -m unittest discover -s tests`.
"""
import io
import json
import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The two built payloads the browser downloads. address_rows.json carries no street
# names at all (rows are [house_number, lat, lng]), so it must be clean outright.
SEARCH_INDEX = "data/search_index.json"
ADDRESS_ROWS = "data/address_rows.json"

QUESTION_RUN = re.compile(r"\?{3,}")

# EMPTY as of 13.08.2026: the eight upstream defects are repaired and the payloads
# carry no '???' runs at all. Byte-exact by design -- if a run ever comes back, pin the
# exact label here and the gate reports any OTHER run as new.
KNOWN_BROKEN_LABELS = frozenset()


def read_text(rel_path):
    with io.open(os.path.join(REPO, rel_path), encoding="utf-8") as f:
        return f.read()


def count_runs(text):
    return len(QUESTION_RUN.findall(text))


def walk_strings(node, path):
    """Yield (json_path, key, value) for every string in the parsed payload.

    Recursing over the parsed structure -- rather than grepping the raw text -- is what
    lets the gate say *where* a run sits: an entry label is the known defect, a vocab
    token or a district name would be a new one.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            for found in walk_strings(value, "%s.%s" % (path, key)):
                yield found
    elif isinstance(node, list):
        for i, value in enumerate(node):
            for found in walk_strings(value, "%s[%d]" % (path, i)):
                yield found
    elif isinstance(node, str):
        key = path.rsplit(".", 1)[-1].split("[")[0]
        yield (path, key, node)


def broken_strings(rel_path):
    payload = json.loads(read_text(rel_path))
    return [(p, k, v) for p, k, v in walk_strings(payload, "$") if QUESTION_RUN.search(v)]


class TestNoAsciiMojibakeInDataPayloads(unittest.TestCase):
    def test_address_rows_is_clean(self):
        hits = broken_strings(ADDRESS_ROWS)
        self.assertEqual(
            [], hits,
            "%s: ASCII-mojibake ('???' run) at %s" % (ADDRESS_ROWS, [h[0] for h in hits[:5]]),
        )

    def test_search_index_runs_are_only_known_broken_labels(self):
        unknown = [(p, k, v) for p, k, v in broken_strings(SEARCH_INDEX)
                   if not (k == "label" and v in KNOWN_BROKEN_LABELS)]
        self.assertEqual(
            [], unknown,
            "%s: new ASCII-mojibake ('???' run) outside the known baseline: %s"
            % (SEARCH_INDEX, [(p, v) for p, _, v in unknown[:5]]),
        )

    def test_known_broken_baseline_does_not_grow(self):
        hits = broken_strings(SEARCH_INDEX)
        self.assertLessEqual(
            len(hits), len(KNOWN_BROKEN_LABELS),
            "%s: %d strings carry a '???' run, baseline allows at most %d"
            % (SEARCH_INDEX, len(hits), len(KNOWN_BROKEN_LABELS)),
        )

    def test_structural_walk_sees_every_run_in_the_raw_text(self):
        # Guards the gate itself: if the walker ever misses a container type, the raw
        # scan still counts the run and this comparison fails instead of passing quietly.
        for rel_path in (SEARCH_INDEX, ADDRESS_ROWS):
            raw = count_runs(read_text(rel_path))
            structural = sum(count_runs(v) for _, _, v in broken_strings(rel_path))
            self.assertEqual(
                raw, structural,
                "%s: raw scan found %d '???' runs, structural walk found %d -- the "
                "walker is missing part of the payload" % (rel_path, raw, structural),
            )


if __name__ == "__main__":
    unittest.main()
