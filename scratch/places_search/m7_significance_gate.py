"""F12-е gate: the М7 branch fires only on SIGNIFICANT tokens.

  python m7_significance_gate.py            # the engine as committed  -> expect PASS
  python m7_significance_gate.py --literal  # the F12-б literal branch -> expect FAIL

The second form is the deliberately broken input: the branch that filters numbers
only. A gate that has never failed is not a gate.
"""
import importlib.util
import pathlib
import sys

# Runnable from the folder it lives in: the checkout is found relative to
# this file, never through a fixed path pinned to one machine (F12-ж).
REPO = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "rs", str(REPO / "scratch" / "places_search" / "recall_sweep.py"))
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)

# The type prefixes the location NAMES carry („к.к.“, „кв.“, „ж.к.“, „м-т“, „с.о.“)
# and the ordinals of „Възраждане 1/2“ — every one of them reaches `qtk`/`ltk` as a
# token of its own, and not one of them is a place.
PREFIXES = ["k", "kv", "zh", "m", "s", "o", "t", "i", "1", "2"]
# A place a human really types.
PLACES = ["zlatni", "mladost", "chaika", "zpz", "vilite", "златни пясъци", "младост"]


def literal_branch(R):
    if not rs.M7_ENABLED or not R:
        return False
    if any(t.orig == rs.DISTRICT_MARK for t in R):
        return False
    if any(t.orig in rs.STREET_MARK for t in R):
        return False
    return not any(t.num for t in R)


if "--literal" in sys.argv:
    rs.bare_location_query = literal_branch

bad = []
for q in PREFIXES:
    rows, branch = rs.search(q)[:2]
    print("  prefix  %-4s -> %-18s %4d rows" % (q, branch, len(rows)))
    if branch == "M7-bare-location":
        bad.append("„%s“ е типов префикс, а задейства М7 с %d реда" % (q, len(rows)))
for q in PLACES:
    rows, branch = rs.search(q)[:2]
    print("  place   %-16s -> %-18s %4d rows" % (q, branch, len(rows)))
    if branch != "M7-bare-location":
        bad.append("„%s“ е място, а НЕ задейства М7 (клон %s)" % (q, branch))

if bad:
    print("ЧЕРВЕНО (%d):" % len(bad))
    for line in bad:
        print("  ✗ " + line)
    raise SystemExit(2)
print("ЗЕЛЕНО: 0 типови префикса задействат М7 · %d места задействат" % len(PLACES))
