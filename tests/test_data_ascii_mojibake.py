"""Static gate against ASCII-mojibake ('???' runs) in the built public data payloads.

Sibling of tests/test_ui_ascii_mojibake.py, which guards the app shell. This one guards
the two browser-shipping payloads produced by the Varna_buildings address pipeline:
data/search_index.json and data/address_rows.json. Text that went through a
'?'-substituting encoder is plain ASCII and slips past a classic mojibake scan, so it
has to be caught by its own signature: a run of 3+ question marks.

Known-broken baseline (Petar's call, 12.08.2026)
------------------------------------------------
Eight address labels in data/search_index.json already ship with the street name
replaced by '?????' (measured live in HEAD 39d6846 and in the uncommitted worktree
rebuild alike, so the defect predates the street-model-v2 label refresh). The root
cause is upstream, in the pipeline that reads the address register, and the repaired
data can only come from a Varna_buildings build cycle -- see
scratch/basemap_rebuild_pure_osm_handoff_facts.md, section 3.

So the gate ships GREEN with those eight pinned as a baseline, and fails the moment a
ninth run appears, a run shows up in address_rows.json, or a run turns up anywhere
other than an entry label. When the upstream fix lands, delete KNOWN_BROKEN_LABELS;
the remaining assertions then read as a plain "zero runs anywhere".

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

# Baseline, not an allowance: every one of these is a live defect awaiting the upstream
# fix. Byte-exact so that a *changed* broken label is reported as a new one.
KNOWN_BROKEN_LABELS = frozenset([
    "кв. Аспарухово, ул. ????? №15",
    "кв. Аспарухово, ул. ????? №17",
    "кв. Аспарухово, ул. ????? №175",
    "кв. Розова долина, ул. ????? №0",
    "кв. Розова долина, ул. ????? №1",
    "кв. Розова долина, ул. ????? №175",
    "кв. Розова долина, ул. ????? №71",
    "кв. Трошево, ул. ????? №32",
])


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
