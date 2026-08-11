"""Static gate against ASCII-mojibake ('???' runs) in the app shell.

The classic mojibake scan catches UTF-8-decoded-as-cp1252 garbage; text that went
through a '?'-substituting encoder is plain ASCII and slips past it. This gate catches
that class: any run of 3+ question marks in index.html or sw.js. JS nullish coalescing
is exactly two question marks and never matches.

Documented instance: the hydrant-data error screen shipped as '?? ?????? ??? ?????????'
(flagged in docs/audits/data_audit_and_target_schema_20260508.md, fixed 2026-08-12).
Pure stdlib; runnable via `python -m unittest discover -s tests`.
"""
import io
import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The repaired error-screen strings; asserting them guards against a silent revert.
ERROR_SCREEN_STRINGS = [
    "Грешка при зареждане на данните",
    "Данните за хидрантите не се заредиха. Провери интернет връзката и опитай отново.",
    "Презареди",
]


def read(name):
    with io.open(os.path.join(REPO, name), encoding="utf-8") as f:
        return f.read()


class TestNoAsciiMojibake(unittest.TestCase):
    def test_no_question_mark_runs_in_shell_files(self):
        for name in ("index.html", "sw.js"):
            content = read(name)
            offsets = [m.start() for m in re.finditer(r"\?{3,}", content)]
            self.assertEqual(
                offsets, [],
                "%s: ASCII-mojibake ('???' run) at byte offsets %s" % (name, offsets[:5]),
            )

    def test_error_screen_strings_present(self):
        index = read("index.html")
        for s in ERROR_SCREEN_STRINGS:
            self.assertIn(s, index, "error-screen string missing: " + s)


if __name__ == "__main__":
    unittest.main()
