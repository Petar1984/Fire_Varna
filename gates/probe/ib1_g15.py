# -*- coding: utf-8 -*-
"""Ф10 · ИБ1-Г15 — no coordinate pair in prose, and none in the new payloads.

    python gates/probe/ib1_g15.py <path> [<path> ...]
    python gates/probe/ib1_g15.py --added-lines <base> -- <path> [<path> ...]

Exit codes (план §3.А Ф10): 0 clean · 1 a hit · 2 an input problem. An input that
cannot be read is never a silent skip: a gate with nothing to look at is broken,
not green.

THE PATTERN IS DOUBLE AND VERBATIM (О80). Varna latitudes start with 42 or 43 and
longitudes with 27 or 28, so one expression catches one half of every pair and a
gate with only the first expression is fail-open: a lonely longitude walks past
it. Both expressions always run, never piped one into the other, and a line is a
hit when EITHER of them fires.

The separator is `.` or `,`: a Bulgarian document writes the decimal comma, a json
writes the point, and the two must not be two different rules.

Why `--added-lines` exists (М): `index.html` at HEAD already carries three
historical hits, so the whole file cannot be the operand. In that mode the gate
reads `git diff --unified=0 <base> -- <path>` and judges ONLY the added lines,
which is exactly what a commit contributes.

Ф10 is an operand of itself (О15): the two expressions above are written so they
cannot match their own source — after `4` and `3` comes `[`, never a separator.
"""
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# The two halves of a Varna coordinate. Both always run (О80).
PATTERNS = (re.compile(r"\b4[23][.,][0-9]{3,}\b"),
            re.compile(r"\b2[78][.,][0-9]{3,}\b"))

EXIT_CLEAN = 0
EXIT_HIT = 1
EXIT_INPUT = 2


def hits_in_line(line):
    """Every match of BOTH expressions — never the first one alone."""
    found = []
    for pattern in PATTERNS:
        found += pattern.findall(line)
    return found


def scan_text(name, text, hits):
    for number, line in enumerate(text.split("\n"), start=1):
        for hit in hits_in_line(line):
            hits.append((name, number, hit))


def read_file(path):
    """The bytes on disk, decoded as utf-8. A path that cannot be read is exit 2."""
    if not os.path.isfile(path):
        sys.stderr.write("missing operand: %s\n" % path)
        sys.exit(EXIT_INPUT)
    try:
        with open(path, "rb") as handle:
            return handle.read().decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        sys.stderr.write("unreadable operand: %s (%s)\n" % (path, error))
        sys.exit(EXIT_INPUT)


def added_lines(base, path):
    """The lines this working tree ADDS to <path> against <base>, without the
    `+++` header line. A failed git process is exit 2, never a clean gate."""
    proc = subprocess.run(["git", "diff", "--unified=0", base, "--", path],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        sys.stderr.write("git diff %s -- %s -> exit %d: %s\n"
                         % (base, path, proc.returncode,
                            (proc.stderr or b"").decode("utf-8", "replace").strip()))
        sys.exit(EXIT_INPUT)
    out = []
    for line in proc.stdout.decode("utf-8", "replace").split("\n"):
        if line.startswith("+") and not line.startswith("+++"):
            out.append(line[1:])
    return "\n".join(out)


def main(argv):
    if not argv:
        sys.stderr.write("usage: ib1_g15.py [--added-lines <base> --] <path> ...\n")
        sys.exit(EXIT_INPUT)
    base = None
    if argv[0] == "--added-lines":
        if len(argv) < 4 or argv[2] != "--":
            sys.stderr.write("usage: ib1_g15.py --added-lines <base> -- <path> ...\n")
            sys.exit(EXIT_INPUT)
        base, argv = argv[1], argv[3:]
    if not argv:
        sys.stderr.write("no operands\n")
        sys.exit(EXIT_INPUT)
    hits = []
    for path in argv:
        if base is None:
            scan_text(path, read_file(path), hits)
        else:
            scan_text(path + " (added lines vs %s)" % base, added_lines(base, path), hits)
    for name, number, hit in hits:
        print("HIT %s:%d %s" % (name, number, hit))
    print("IB1-G15 %s operands=%d hits=%d"
          % ("RED" if hits else "OK", len(argv), len(hits)))
    sys.exit(EXIT_HIT if hits else EXIT_CLEAN)


if __name__ == "__main__":
    main(sys.argv[1:])
