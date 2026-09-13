# -*- coding: utf-8 -*-
"""Lot perimeter - "nothing else moved", as a DELIVERY probe (plan section 4 K3.5).

    python gates/probe/lot_perimeter.py --base <sha> --allow <file> [--path <file>]

The probe declares the lines a lot INSERTS into `index.html`, removes them from the
candidate and byte-compares the remainder with the blob of `<base>:index.html`.

Why this is a probe and NOT a permanent test. Lot 1 shipped the same comparison as a
unittest method pinned to its own base commit; from that moment the whole file was
frozen against that commit, so the very next lot - which is allowed to touch the file -
made it red for a reason that had nothing to do with lot 1. A whole-file pin is true
exactly once, at the delivery of the lot that wrote it. Therefore it runs at the gate,
by hand, with the inserted lines named on the command line, and what stays permanent in
`tests/` is only what remains true forever: the pins of the functions a lot must not
touch and the anchors of the lines it did insert.

Exit codes: 0 the remainder equals the base - 1 something else moved - 2 the input is
crooked (unreadable file, unresolvable base, empty allow list, a declared row that does
not stand exactly once in the candidate or that already stands in the base, or a
candidate equal to the base blob: there would be nothing to prove). A crooked input is
never a green gate.

The output is Latin only and carries no line CONTENT, only line numbers: `index.html`
is production code and this probe is quoted in reports. Nothing under `data/` is read.
"""
import argparse
import os
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = pathlib.Path(__file__).resolve().parents[2]

EXIT_OK = 0
EXIT_DIFF = 1
EXIT_INPUT = 2


def refuse(reason):
    """A crooked input fails loud on STDOUT and exits 2 - never 0."""
    print("LOT-PERIMETER INPUT %s" % reason)
    sys.exit(EXIT_INPUT)


def read_utf8(path, what):
    if not os.path.isfile(path):
        refuse("%s not found: %s" % (what, path))
    try:
        with open(path, "rb") as handle:
            return handle.read().decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        refuse("%s unreadable: %s (%s)" % (what, path, error))


def allow_rows(path):
    """One allowed INSERTED line per row, each carrying its trailing newline, so that
    removing a row removes a whole line and never a fragment of one. The split is on
    the newline character alone: a row left with a stray carriage return does not match
    an LF candidate and the probe says so instead of guessing. Blank rows are skipped -
    a blank line cannot be declared, because it never stands exactly once."""
    text = read_utf8(path, "allow file")
    rows = [piece + "\n" for piece in text.split("\n") if piece.strip()]
    if not rows:
        refuse("allow file carries no rows: %s" % path)
    return rows


def base_blob(base):
    """The bytes of `<base>:index.html`. A failed git process is exit 2, never a pass."""
    proc = subprocess.run(["git", "show", "%s:index.html" % base],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          cwd=str(REPO))
    if proc.returncode != 0:
        refuse("git show %s:index.html -> exit %d: %s"
               % (base, proc.returncode,
                  (proc.stderr or b"").decode("utf-8", "replace").strip()[:300]))
    try:
        return proc.stdout.decode("utf-8")
    except UnicodeDecodeError as error:
        refuse("blob %s:index.html is not utf-8 (%s)" % (base, error))


def first_difference_line(left, right):
    """The 1-based number of the first line where the two texts part."""
    a, b = left.split("\n"), right.split("\n")
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i + 1
    return min(len(a), len(b)) + 1


def main(argv):
    parser = argparse.ArgumentParser(
        description="Remove the declared inserted lines and byte-compare the rest "
                    "with the base blob of index.html.")
    parser.add_argument("--base", required=True,
                        help="the commit whose index.html is the reference")
    parser.add_argument("--allow", required=True,
                        help="file with the inserted lines, one per row")
    parser.add_argument("--path", default=str(REPO / "index.html"),
                        help="the candidate file (default: index.html of this tree)")
    args = parser.parse_args(argv)

    rows = allow_rows(args.allow)
    candidate = read_utf8(args.path, "candidate")
    base = base_blob(args.base)

    if candidate == base:
        refuse("base equals candidate - the base %s has nothing to prove" % args.base)

    stripped = candidate
    for number, row in enumerate(rows, start=1):
        here = stripped.count(row)
        if here != 1:
            refuse("row %d stands %d times in the candidate, not once: %s"
                   % (number, here, ascii(row[:60])))
        there = base.count(row)
        if there != 0:
            refuse("row %d already stands %d times in the base %s: %s"
                   % (number, there, args.base, ascii(row[:60])))
        stripped = stripped.replace(row, "", 1)

    if stripped != base:
        print("LOT-PERIMETER DIFF first difference at line %d"
              % first_difference_line(base, stripped))
        sys.exit(EXIT_DIFF)
    print("LOT-PERIMETER OK removed=%d base=%s" % (len(rows), args.base))
    sys.exit(EXIT_OK)


if __name__ == "__main__":
    main(sys.argv[1:])
