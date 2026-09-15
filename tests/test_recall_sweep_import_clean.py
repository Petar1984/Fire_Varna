# -*- coding: utf-8 -*-
"""H-1 — importing the places engine must not leak a file handle.

`scratch/places_search/recall_sweep.py` is imported by three callers that run
inside the suite: `tests/test_places_search_gate.py:146`,
`tests/test_granitsi_fixtures.py:54` and `gates/release.py:353`. Until lot 6 it
read its three delivered payloads with `json.load(open(...))` at module level, so
every one of those runs dropped three file objects on the floor and printed a
ResourceWarning into the output Petar reads at the push hook.

The gate imports the engine in a CHILD interpreter under
`-X dev -W always::ResourceWarning`, because ResourceWarning is silenced by
default and a warning nobody can see is a gate that cannot fail. It demands four
things: exit 0, an `IMPORTED` sentinel on stdout, a `STDERR_ALIVE` sentinel the
child writes to stderr as its LAST action, and not one stderr line carrying the
category form Python prints for an unclosed file, `: ResourceWarning: unclosed
file`. Neither sentinel is decoration: a child that died early prints no warning
either, and a module that replaces `sys.stderr` at import time hands the gate an
empty stream, so without them a crash or a swallowed stream would pass for a
clean import. The needle is that category form and not the bare word, because
under `-X dev` every warning prints a second line — the "Enable tracemalloc"
hint, which names the class too, so three handles were counted as six — and
because a foreign warning whose TEXT merely mentions ResourceWarning is not a
leaked file.

`FIRE_VARNA_RECALL_SWEEP_PATH` points these assertions at another copy of the
engine and defaults to the tree's file. It exists for one reason: the negative
half of плана §2 К2 runs THIS module against a doctored copy outside the tree
(one `json.load(open(...))` restored) and was measured to fall.

Run: python -m unittest tests.test_recall_sweep_import_clean
     python -m unittest discover -s tests
"""
import os
import pathlib
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
ENGINE = pathlib.Path(os.environ.get("FIRE_VARNA_RECALL_SWEEP_PATH")
                      or (REPO / "scratch" / "places_search" / "recall_sweep.py"))

# The needle is the CATEGORY form Python prints for an unclosed file. The bare
# word stands in the "Enable tracemalloc" hint line too, and inside the text of
# foreign warnings; neither of those is a leaked handle.
NEEDLE = ": ResourceWarning: unclosed file"
# The child's last word, on stderr: proof the stream this gate reads is alive.
STDERR_SENTINEL = "STDERR_ALIVE"

# The child imports the engine under its own private module name, so nothing of
# the suite's state can hide a leak, prints the stdout sentinel out of a
# structure the engine builds at import time, and signs stderr last of all.
CHILD_SOURCE = (
    "import importlib.util, sys\n"
    "spec = importlib.util.spec_from_file_location('recall_sweep_import_probe',"
    " sys.argv[1])\n"
    "module = importlib.util.module_from_spec(spec)\n"
    "spec.loader.exec_module(module)\n"
    "print('IMPORTED', len(module.cats['chips']))\n"
    "sys.stderr.write('" + STDERR_SENTINEL + "\\n')\n"
)

CHILD_TIMEOUT = 600


class RecallSweepImportsWithoutLeaking(unittest.TestCase):
    """One child run, two verdicts: the import lives, and its stderr is alive
    and silent."""

    @classmethod
    def setUpClass(cls):
        cls.child = subprocess.run(
            [sys.executable, "-X", "dev", "-W", "always::ResourceWarning",
             "-c", CHILD_SOURCE, str(ENGINE)],
            cwd=str(REPO), capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=CHILD_TIMEOUT)

    def test_the_import_succeeds_and_says_so(self):
        self.assertEqual(
            self.child.returncode, 0,
            "importing %s exited %d; stderr:\n%s"
            % (ENGINE, self.child.returncode, self.child.stderr))
        self.assertIn(
            "IMPORTED", self.child.stdout,
            "the child did not reach the sentinel, so a silent stderr would "
            "prove nothing; stdout:\n%s\nstderr:\n%s"
            % (self.child.stdout, self.child.stderr))

    def test_the_import_prints_no_resource_warning(self):
        self.assertIn(
            STDERR_SENTINEL, self.child.stderr,
            "the child's stderr does not carry the %s sentinel, so its silence "
            "proves nothing: %s replaced sys.stderr at import, or the child "
            "never reached its last line; stderr:\n%s"
            % (STDERR_SENTINEL, ENGINE, self.child.stderr))
        noisy = [line for line in self.child.stderr.splitlines()
                 if NEEDLE in line]
        self.assertEqual(
            [], noisy,
            "importing %s leaked %d file object(s); every caller of the engine "
            "prints this on every run:\n%s"
            % (ENGINE, len(noisy), "\n".join(noisy)))


if __name__ == "__main__":
    unittest.main()
