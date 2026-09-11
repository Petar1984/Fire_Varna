# -*- coding: utf-8 -*-
"""Ф7 · ИБ1-Г11 — the first-load budget, with an OPERATIONAL definition.

    python -m unittest tests.test_first_load_budget

AGENTS.md § Hard Constraints gives the app a 5 MB first-load hard cap and until
this lot the cap had no machine judge (М-о). The quarter index is the THIRD
payload of the address search, and the whole design rests on it being lazy — so
the gate is born here, together with it.

WHY THE RULE IS OPERATIONAL AND NOT "reachable from initialization" (ИБ1-О13):
reachability inside a 7 500-line HTML file is not machine-decidable, and a gate
that needs a solver is a gate that falls without a defect. The набор is therefore
defined by three mechanical rules, each fail-CLOSED:

  1. every LITERAL `fetch('data/…')` anywhere in the app scripts is eager. This is
     the rule that catches `index.html:1774` — the hydrant payload is fetched
     inside an IIFE that runs while the page parses, and an IIFE body is a
     function body for every syntactic rule below;
  2. every `fetch`/`fetchCachedJson` call on a URL CONSTANT that stands OUTSIDE
     a function body (brace depth 0 of the script) is eager. Without this rule
     `fetchCachedJson(ADDRESS_QUARTERS_URL)` written at init would pass the gate
     while the browser downloaded half a megabyte before the map drew — "an
     expression over the literal alone is fail-open" (О54);
  3. the closed lazy list below has to be DECLARED, name by name. It does not
     excuse anything by itself (rule 2 judges by position, not by name); it is
     the tripwire that says the file moved under the gate.

     Measured 12.09: the app binds five more `data/` urls to constants, and every
     one of them is fetched from inside a function — `BASEMAP_MANIFEST_URL`
     (`index.html:4586`, inside `loadBasemapManifest`) is the one outside the
     address search, and it stays out of the набор for that reason and no other.

The vendor blocks (`<script id="leaflet-js">`, `<script id="mc-js">`) are minified
third-party code and are stripped before the scan; they fetch nothing from `data/`.

The scanner is fail-loud: if the brace depth does not return to zero at the end of
a script block, the gate says so and falls — a scanner that lost the file may not
hand out a green verdict.

Two invariants, ZERO pinned byte counts (О57): the eager set is EXACTLY
`{data/hydrants.json}` and the sum of its delivered blobs is `≤ 5 242 880`. The
numbers before and after go into Д6, never into this file.

Червено по конструкция до К9 (ИНТЕРВАЛ А): rule 2 needs `ADDRESS_QUARTERS_URL` to
exist, and Т2 writes it in К9. Until then this gate is RED, by design.

Negative halves (план §5 Г11): an eager `fetch('data/address_quarters.json')` → 1;
`fetchCachedJson(ADDRESS_QUARTERS_URL)` at init → 1; the same test with a budget of
1 000 000 → 1. The first two are fed in through **FIRE_VARNA_INDEX_HTML_PATH**, the
third through **FIRE_VARNA_FIRST_LOAD_BUDGET**.

Run: python -m unittest discover -s tests
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
INDEX = pathlib.Path(os.environ.get("FIRE_VARNA_INDEX_HTML_PATH") or (REPO / "index.html"))

# AGENTS.md § Hard Constraints — 5 MB, in bytes.
HARD_CAP = int(os.environ.get("FIRE_VARNA_FIRST_LOAD_BUDGET") or 5242880)

# The one payload the app is allowed to fetch before the map draws.
EXPECTED_EAGER = {"data/hydrants.json"}

# The CLOSED lazy list (план §3.А Ф7, М): six constants measured in HEAD plus the
# one Т2 adds. Anything else that names a `data/` url is eager by rule 2.
LAZY_CONSTANTS = ("SEARCH_INDEX_URL", "ADDRESS_ROWS_URL", "APPROX_ADDRESS_URL",
                  "PLACES_URL", "CATS_URL", "PLACES2_URL", "ADDRESS_QUARTERS_URL")

VENDOR_SCRIPT_IDS = ("leaflet-js", "mc-js")

SCRIPT_RE = re.compile(r"<script\b([^>]*)>(.*?)</script>", re.S)
SCRIPT_ID_RE = re.compile(r"id\s*=\s*[\"']([^\"']+)[\"']")
LITERAL_FETCH_RE = re.compile(r"\bfetch\(\s*['\"](data/[^'\"]+)['\"]")
# Any binding of a `data/` url, not only `const NAME = …`: the app declares two of
# them in ONE statement (`const PLACES_URL = …, CATS_URL = …`, index.html:6256), so
# a rule that insists on the keyword misses the second name (measured 12.09).
CONST_URL_RE = re.compile(r"\b([A-Za-z_][A-Za-z_0-9]*)\s*=\s*['\"](data/[^'\"]+)['\"]")
CALL_RE = re.compile(r"\b(?:fetch|fetchCachedJson)\(\s*([A-Za-z_][A-Za-z_0-9]*)\s*[),]")


def app_scripts(html):
    """The non-vendor `<script>` bodies, with their offset inside the file."""
    out = []
    for match in SCRIPT_RE.finditer(html):
        ident = SCRIPT_ID_RE.search(match.group(1) or "")
        if ident and ident.group(1) in VENDOR_SCRIPT_IDS:
            continue
        out.append(match.group(2))
    return out


def brace_depths(source):
    """depth[i] = the brace depth of character i, strings and comments skipped.

    A minimal JS scanner: line and block comments, the three kinds of string
    literal (with `${}` inside templates) and regular-expression literals are
    stepped over, and only the braces outside all of them are counted. It is
    deliberately small; its one job is to tell "inside a function body" from "at
    the top level of the script", and `final_depth` lets the caller prove the
    scanner did not lose the file.
    """
    depths = [0] * (len(source) + 1)
    depth = 0
    i = 0
    template_stack = []
    previous_significant = ""
    while i < len(source):
        depths[i] = depth
        ch = source[i]
        two = source[i:i + 2]
        if two == "//":
            j = source.find("\n", i)
            i = len(source) if j < 0 else j
            continue
        if two == "/*":
            j = source.find("*/", i + 2)
            i = len(source) if j < 0 else j + 2
            continue
        if ch in "'\"":
            i += 1
            while i < len(source) and source[i] != ch:
                i += 2 if source[i] == "\\" else 1
            i += 1
            previous_significant = "x"
            continue
        if ch == "`":
            i += 1
            while i < len(source):
                if source[i] == "\\":
                    i += 2
                    continue
                if source[i] == "`":
                    i += 1
                    break
                if source[i:i + 2] == "${":
                    # A substitution is real code: leave the template, remember it.
                    template_stack.append(depth)
                    depth += 1
                    i += 2
                    break
                i += 1
            previous_significant = "x"
            continue
        if ch == "/" and previous_significant in ("", "(", ",", "=", ":", "[", "!",
                                                  "&", "|", "?", "{", "}", ";",
                                                  "+", "-", "*", "%", "~", "^",
                                                  "<", ">", "\n"):
            i += 1
            in_class = False
            while i < len(source):
                c = source[i]
                if c == "\\":
                    i += 2
                    continue
                if c == "[":
                    in_class = True
                elif c == "]":
                    in_class = False
                elif c == "/" and not in_class:
                    i += 1
                    break
                elif c == "\n":
                    break
                i += 1
            previous_significant = "x"
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if template_stack and depth == template_stack[-1]:
                # The substitution closed: back inside the template literal.
                template_stack.pop()
                i += 1
                while i < len(source):
                    if source[i] == "\\":
                        i += 2
                        continue
                    if source[i] == "`":
                        i += 1
                        break
                    if source[i:i + 2] == "${":
                        template_stack.append(depth)
                        depth += 1
                        i += 2
                        break
                    i += 1
                previous_significant = "x"
                continue
        if not ch.isspace():
            previous_significant = ch
        i += 1
    depths[len(source)] = depth
    return depths, depth


def eager_set(html):
    """The three rules, applied to every non-vendor script. Returns (set, notes)."""
    urls = set()
    notes = []
    lazy = set(LAZY_CONSTANTS)
    for source in app_scripts(html):
        depths, final = brace_depths(source)
        if final != 0:
            raise AssertionError(u"скенерът изгуби файла: крайна дълбочина %d" % final)
        constants = {name: url for name, url in CONST_URL_RE.findall(source)}
        for match in LITERAL_FETCH_RE.finditer(source):
            urls.add(match.group(1))
            notes.append(u"литерал %s" % match.group(1))
        for match in CALL_RE.finditer(source):
            name = match.group(1)
            if name not in constants:
                continue
            if depths[match.start()] == 0:
                urls.add(constants[name])
                notes.append(u"повикване на върхово ниво на <script>: %s%s"
                             % (name, u" (ленив по списък)" if name in lazy else u""))
    return urls, notes


def delivered_size(rel):
    """The size of the blob a push publishes; the working file only as a fallback."""
    for ref in ("HEAD:" + rel, ":" + rel):
        proc = subprocess.run(["git", "-C", str(REPO), "cat-file", "-s", ref],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode == 0:
            return int(proc.stdout.decode("ascii").strip())
    path = REPO / rel
    if path.exists():
        return len(path.read_bytes().replace(b"\r\n", b"\n"))
    raise AssertionError(u"липсва товар: %s" % rel)


class FirstLoadBudgetTest(unittest.TestCase):
    """ИБ1-Г11 — two invariants and not one pinned byte count."""

    def setUp(self):
        self.html = INDEX.read_bytes().decode("utf-8")

    def test_the_lazy_list_is_present(self):
        """Every name of the closed list is declared — a missing one means the
        file moved under the gate, and rule 2 would then silently pass."""
        bound = {name for name, _url in CONST_URL_RE.findall(self.html)}
        missing = [name for name in LAZY_CONSTANTS if name not in bound]
        self.assertEqual(missing, [],
                         u"липсват константи от затворения списък (Т2 ги ражда в К9)")

    def test_eager_set_is_exactly_the_hydrant_payload(self):
        urls, notes = eager_set(self.html)
        self.assertEqual(urls, EXPECTED_EAGER,
                         u"нетърпеливият набор не е {data/hydrants.json}: %s"
                         % json.dumps(notes, ensure_ascii=False))

    def test_first_load_is_under_the_hard_cap(self):
        urls, _ = eager_set(self.html)
        total = sum(delivered_size(rel) for rel in sorted(urls))
        self.assertLessEqual(total, HARD_CAP,
                             u"първото зареждане е %d B при таван %d B (STOP 16)"
                             % (total, HARD_CAP))


if __name__ == "__main__":
    unittest.main()
