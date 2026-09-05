#!/usr/bin/env python3
"""The single executable the push waits on.

    python -m gates.run_gates [--base git:<rev>] [--allow <path>]

Seven checks, one table, one exit code:

  1. sha pins        the three SHA256 constants in `index.html` against the
                     LF-normalised bytes of the three delivered blobs — exactly
                     the bytes `fetchValidatedJson` digests in the browser
  2. key sets        every row carries exactly EXPECT_KEYS / EXPECT2_KEYS
                     (hotels 17, places 13) — the count and the names
  3. qa_no_cad_ids   no cadastral identifier ever rides a public blob
  4. coverage        gates/coverage.py against the last signed baseline
                     (gates/baseline/MANIFEST.json); no baseline = STOP
  5. signed_facts    data/signed_facts.json — the small judging file
  6. release         gates/release.py — the frozen reference, the engine
                     candidate, the pinned inputs and the manifests bound by
                     digest; every delta covered by a signed queue row
  7. authorship      every `signed_by: "Петър"` was introduced by a commit of
                     Petar1984, never by an agent (`git log -S`) — AND the body
                     it protects has not been rewritten since: the newest commit
                     on a signed artefact is Petar's too, or he recorded the
                     digest of the resulting body himself (амандамент №5 т. 3),
                     on a queue whose own authorship was settled first
                     (амандамент №6 т. 3) and with HIS commit as the one that
                     introduced the number (амандамент №8 т. 2)

The gate never imports `unittest` and never reads `tests/`: a check that shares
code with the suite it guards cannot fail independently of it.

Every check runs, always: the table is written for the human, not stopped at
the first mark. Exit code: 0 only when every check is green; 1 when any check
is red OR yellow — "pending — Петър" is not a signature (Амандамент №1, т. 8),
and neither is "Петърчо Иванов": the signature is compared exactly, by
`coverage.is_signed_by_petar`, for the baseline manifest and the allow-file
alike. `--base` replaces the signed baseline with an ad-hoc revision and is
therefore ⚠ by construction: it measures, it does not absolve.
One number for the pre-push hook to read.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from gates import coverage
from gates import release

REPO_ROOT = Path(__file__).resolve().parent.parent

INDEX_HTML = "index.html"
BASELINE_PATH = "gates/baseline/MANIFEST.json"
ALLOW_DIR = "gates/allow"
SIGNED_FACTS_PATH = "data/signed_facts.json"
# The only author whose commit may INTRODUCE a signature (§0.5) — one string,
# kept in `gates.release` and read by every gate that asks whose hand it was.
HUMAN_AUTHOR = release.HUMAN_AUTHOR

# (constant in index.html, delivered blob)
SHA_PINS = (
    ("HOTELS_SHA256", "data/hotels.json"),
    ("PLACES2_SHA256", "data/places.json"),
    ("CATS_SHA256", "data/place_categories.json"),
)

ROW_FILES = (
    ("hotels", "data/hotels.json", "hotels", "EXPECT_KEYS", 17),
    ("places", "data/places.json", "places", "EXPECT2_KEYS", 13),
)

# A cadastral id never rides a public bundle (ADR 008 Д2) — the same regex the
# client applies to the fetched text, applied here to the tracked bytes.
CADASTRAL_RE = re.compile(r"\b\d{4,5}\.\d+\.\d+")
PUBLIC_BLOBS = (
    "data/hotels.json",
    "data/places.json",
    "data/place_categories.json",
    SIGNED_FACTS_PATH,
)

OK, WARN, BAD = "✓", "⚠", "✗"


class Check:
    """One row of the table: a mark, a name, and the words behind it."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.mark = OK
        self.lines: list[str] = []

    def say(self, text: str) -> None:
        self.lines.append(text)

    def fail(self, text: str) -> None:
        self.mark = BAD
        self.lines.append(text)

    def warn(self, text: str) -> None:
        if self.mark == OK:
            self.mark = WARN
        self.lines.append(text)


def read_text(rel: str) -> str:
    return (REPO_ROOT / rel).read_text(encoding="utf-8")


def lf_bytes(rel: str) -> bytes:
    """The bytes the browser sees: the tracked LF blob, whatever the checkout wrote."""
    return (REPO_ROOT / rel).read_bytes().replace(b"\r\n", b"\n")


def js_const_string(html: str, name: str) -> str | None:
    m = re.search(r"const\s+%s\s*=\s*'([0-9a-f]{64})'" % re.escape(name), html)
    return m.group(1) if m else None


def js_const_array(html: str, name: str) -> list[str] | None:
    """Read a JS array of single-quoted strings out of index.html.

    The closed lists live in the app shell and nowhere else; duplicating them
    here would create a second truth that drifts.
    """
    m = re.search(r"const\s+%s\s*=\s*\[(.*?)\]\s*;" % re.escape(name), html, re.S)
    if not m:
        return None
    return re.findall(r"'([^']*)'", m.group(1))


def check_sha_pins() -> Check:
    check = Check("1 · sha пинове (index.html ↔ LF байтовете)")
    html = read_text(INDEX_HTML)
    for const_name, rel in SHA_PINS:
        pinned = js_const_string(html, const_name)
        if not pinned:
            check.fail("%s: константата липсва в %s" % (const_name, INDEX_HTML))
            continue
        actual = hashlib.sha256(lf_bytes(rel)).hexdigest()
        if actual == pinned:
            check.say("%s = %s ✓ %s" % (const_name, pinned[:12], rel))
        else:
            check.fail("%s: пин %s ≠ %s (%s)" % (const_name, pinned[:12], actual[:12], rel))
    return check


def check_key_sets() -> Check:
    check = Check("2 · ключовите набори на редовете")
    html = read_text(INDEX_HTML)
    for label, rel, array_key, const_name, expected_len in ROW_FILES:
        keys = js_const_array(html, const_name)
        if keys is None:
            check.fail("%s: липсва в %s" % (const_name, INDEX_HTML))
            continue
        if len(keys) != expected_len:
            check.fail("%s: %d ключа, планът казва %d" % (const_name, len(keys), expected_len))
            continue
        expected = set(keys)
        rows = json.loads(read_text(rel))[array_key]
        bad = 0
        for i, row in enumerate(rows):
            if len(row) != expected_len or set(row) != expected:
                bad += 1
                if bad <= 3:
                    check.fail(
                        "%s ред %d (%s): %d ключа, разлика %s"
                        % (label, i, row.get("name"), len(row), sorted(set(row) ^ expected))
                    )
        if bad:
            check.fail("%s: %d реда с грешен набор" % (label, bad))
        else:
            check.say("%s: %d реда × %d ключа ✓" % (label, len(rows), expected_len))
    return check


def check_no_cad_ids() -> Check:
    check = Check("3 · qa_no_cad_ids върху публичните blob-ове")
    for rel in PUBLIC_BLOBS:
        path = REPO_ROOT / rel
        if not path.exists():
            check.say("%s: липсва (не се проверява)" % rel)
            continue
        hits = sorted(set(CADASTRAL_RE.findall(path.read_text(encoding="utf-8"))))
        if hits:
            check.fail("%s: %d кадастрални идентификатора, напр. %s" % (rel, len(hits), hits[:3]))
        else:
            check.say("%s ✓" % rel)
    return check


def pick_allow_file(explicit: str | None, check: Check) -> str | None:
    """One allow-file, named explicitly or the only one in gates/allow/.

    Never merge several signed lists silently: two signatures for one delivery
    is exactly the ambiguity the gate exists to remove.
    """
    if explicit:
        return explicit
    allow_dir = REPO_ROOT / ALLOW_DIR
    found = sorted(p for p in allow_dir.glob("*.json")) if allow_dir.exists() else []
    if not found:
        return None
    if len(found) > 1:
        check.fail(
            "повече от един allow-файл в %s (%s) — подай --allow изрично"
            % (ALLOW_DIR, ", ".join(p.name for p in found))
        )
        return None
    return str(found[0].relative_to(REPO_ROOT))


def check_coverage(base_override: str | None, allow_override: str | None) -> Check:
    check = Check("4 · покритие спрямо подписания baseline")
    manifest_path = REPO_ROOT / BASELINE_PATH
    if base_override:
        rev = base_override[len("git:"):] if base_override.startswith("git:") else base_override
        # An ad-hoc base is a measurement, never a verdict: the run says
        # nothing about the bytes Petar signed, and a green table here would
        # read as if it did (одит ЛОТ 0-fix, бележка „е“).
        check.warn(
            "подписаният baseline НЕ е проверен — base по команден ред: %s (%s не е четен)"
            % (rev, BASELINE_PATH)
        )
    else:
        if not manifest_path.exists():
            check.fail("няма подписан baseline (%s липсва)" % BASELINE_PATH)
            return check
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        rev = manifest.get("rev")
        if not rev:
            check.fail("няма подписан baseline (%s без `rev`)" % BASELINE_PATH)
            return check
        signed_by = manifest.get("signed_by")
        # The same exact comparison the allow-file gets — one rule, one place.
        if not coverage.is_signed_by_petar(signed_by):
            check.warn("baseline `signed_by` = %r — още НЕ е подпис на Петър" % signed_by)
        # The baseline names the bytes it was signed on; if the rev no longer
        # carries them, the signature is on something else.
        for rel, want in (manifest.get("files") or {}).items():
            try:
                blob = coverage.read_source("git:%s:%s" % (rev, rel)).encode("utf-8")
            except ValueError as exc:
                check.fail(str(exc))
                continue
            got = hashlib.sha256(blob).hexdigest()
            if got != want:
                check.fail("%s@%s: %s ≠ подписаното %s" % (rel, rev[:7], got[:12], want[:12]))

    allow_path = pick_allow_file(allow_override, check)
    check.say("allow-файл: %s" % (allow_path or "няма"))
    try:
        result = coverage.run(
            places_base="git:%s:data/places.json" % rev,
            places_candidate="data/places.json",
            hotels_base="git:%s:data/hotels.json" % rev,
            hotels_candidate="data/hotels.json",
            allow_path=str(REPO_ROOT / allow_path) if allow_path else None,
            out_dir=str(REPO_ROOT / "gates" / "out"),
        )
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        check.fail("coverage: %s" % exc)
        return check

    allow_meta = result.get("allow") or {}
    if allow_meta:
        check.say(
            "allow подпис: signed_by=%r date=%r → %s"
            % (allow_meta.get("signed_by"), allow_meta.get("date"), allow_meta.get("signature"))
        )
    for file_key in coverage.FILES:
        block = result["files"].get(file_key)
        if not block:
            continue
        # The row counts are part of the verdict: a delivery that lost a hundred
        # rows can otherwise show a clean field table (одит 05.09, дефект 2).
        check.say(
            "%s: rows_base=%d rows_candidate=%d сдвоени=%d липсващи=%d нови=%d пренаредени=%d"
            % (
                file_key,
                block["rows_base"],
                block["rows_candidate"],
                block["compared"],
                len(block["missing_rows"]),
                len(block["added_rows"]),
                block["file_reordered"],
            )
        )
        for field in coverage.FIELDS:
            c = block["fields"][field]["counts"]
            if c["lost"] or c["changed"] or c["after"] < c["before"]:
                check.say(
                    "%s %s: before=%d after=%d lost=%d changed=%d gained=%d"
                    % (file_key, field, c["before"], c["after"], c["lost"], c["changed"], c["gained"])
                )
    if result["exit_code"] == coverage.EXIT_ALLOW_UNSIGNED:
        check.warn("coverage изход %d — %s (жълто блокира пуша)" % (result["exit_code"], result["verdict"]))
    elif result["exit_code"] != coverage.EXIT_OK:
        check.fail("coverage изход %d — %s (виж gates/out/coverage.md)" % (result["exit_code"], result["verdict"]))
    else:
        check.say("coverage изход 0 — %s" % result["verdict"])
    return check


def normalise_uin(value: str) -> str:
    """Registry numbers are compared without their separators and in upper case."""
    return re.sub(r"[^0-9A-ZА-Я]", "", (value or "").upper())


def check_signed_facts() -> Check:
    check = Check("5 · signed_facts (малкият съдещ файл)")
    path = REPO_ROOT / SIGNED_FACTS_PATH
    if not path.exists():
        check.fail("липсва %s" % SIGNED_FACTS_PATH)
        return check
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        check.fail("%s: невалиден JSON — %s" % (SIGNED_FACTS_PATH, exc))
        return check

    html = read_text(INDEX_HTML)
    code_lists = {
        "quarter": js_const_array(html, "QUARTER_CODES") or [],
        "locality": js_const_array(html, "LOCALITY_CODES") or [],
        "district": js_const_array(html, "DISTRICT_CODES") or [],
    }
    rows = {
        "hotels": json.loads(read_text("data/hotels.json"))["hotels"],
        "places": json.loads(read_text("data/places.json"))["places"],
    }

    facts = doc.get("facts")
    if not isinstance(facts, list):
        check.fail("%s: няма масив `facts`" % SIGNED_FACTS_PATH)
        return check

    green = 0
    for n, fact in enumerate(facts, 1):
        label = "факт %d (%s)" % (n, fact.get("name"))
        file_key = fact.get("file")
        if file_key not in rows:
            check.fail("%s: непознат файл %r" % (label, file_key))
            continue
        anchor = fact.get("anchor") or {}
        src, ident = anchor.get("src"), anchor.get("id")
        if src == "NTR":
            key = normalise_uin(ident)
            hits = [r for r in rows[file_key] if any(normalise_uin(u) == key for u in r.get("uins", []))]
        elif src == "REG":
            hits = [r for r in rows[file_key] if r.get("name") == fact.get("name")]
            check.warn("%s: слаба котва (REG по (файл, име), не по УИН)" % label)
        else:
            check.fail("%s: непозната котва %r" % (label, src))
            continue
        if len(hits) != 1:
            check.fail("%s: котвата резолвира %d реда, а трябва точно 1" % (label, len(hits)))
            continue
        row = hits[0]
        if row.get("name") != fact.get("name"):
            check.warn("%s: котвата сочи ред с име %r" % (label, row.get("name")))
        for field, claim in (fact.get("expect") or {}).items():
            if field not in code_lists:
                check.fail("%s: непознато поле %r" % (label, field))
                continue
            value = row.get(field)
            actual = value.get("code") if isinstance(value, dict) else None
            if "is" in claim:
                want = claim["is"]
                if want not in code_lists[field]:
                    check.fail("%s: код %r извън затворения списък %s" % (label, want, field))
                    continue
                if actual == want:
                    green += 1
                else:
                    check.fail("%s: %s = %r, подписано е %r" % (label, field, actual, want))
            elif "not" in claim:
                forbidden = claim["not"]
                bad = [c for c in forbidden if c not in code_lists[field]]
                if bad:
                    check.fail("%s: кодове извън затворения списък %s: %s" % (label, field, bad))
                    continue
                if actual in forbidden:
                    check.fail("%s: %s = %r, подписано е „не е %s“" % (label, field, actual, forbidden))
                else:
                    green += 1
            else:
                check.fail("%s: твърдение без `is`/`not`" % label)

    check.say("%d факта, %d потвърдени твърдения" % (len(facts), green))

    candidates = doc.get("candidates") or []
    for n, cand in enumerate(candidates, 1):
        # Candidates never touch the exit code (Амандамент №2, A.8): they carry
        # no signature, so their weak anchors and unknown codes are notes for
        # the human, not marks that hold the push. ⚠ stays for `facts`.
        anchor_src = (cand.get("anchor") or {}).get("src")
        if anchor_src != "NTR":
            check.say(
                "кандидат %d (%s): слаба котва (%s) — бележка, не ⚠"
                % (n, cand.get("name"), anchor_src)
            )
        for field, claim in (cand.get("expect") or {}).items():
            wanted = [claim["is"]] if "is" in claim else list(claim.get("not") or [])
            unknown = [c for c in wanted if c not in code_lists.get(field, [])]
            if unknown:
                check.say(
                    "кандидат %d (%s): код %s извън затворения списък %s — чака подпис И код"
                    % (n, cand.get("name"), unknown, field)
                )
    check.say("%d кандидата без подпис (никога не влияят на изхода)" % len(candidates))
    return check


def check_release(queue_override: str | None) -> Check:
    """Проверка 6 — gates/release.py, run here so the push waits on it too.

    The gate lives in its own module because it is the one check that imports
    the search engine: keeping it out of this file leaves `run_gates` importable
    even when the reference is mid-edit, and the failure is then this row, not
    an ImportError before the table."""
    check = Check("6 · release (референция ↔ двигател ↔ подписана опашка)")
    try:
        result = release.run(queue_override)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        check.fail("release: %s" % exc)
        return check
    for line in result["lines"]:
        check.say(line)
    if result["exit_code"] != release.EXIT_OK:
        check.fail("release изход %d — %s" % (result["exit_code"], result["verdict"]))
    return check


def git_lines(*args: str) -> list[str]:
    out = subprocess.run(["git", "-C", str(REPO_ROOT)] + list(args),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError("git %s: %s" % (" ".join(args),
                                         out.stderr.decode("utf-8", "replace").strip()))
    return out.stdout.decode("utf-8", "replace").splitlines()


def last_commit_on(rel: str) -> tuple[str, str] | None:
    """(hash, author) of the NEWEST commit that touched a path."""
    lines = git_lines("log", "-1", "--format=%H\t%an", "--", rel)
    if not lines:
        return None
    parts = lines[0].split("\t", 1)
    return (parts[0], parts[1] if len(parts) > 1 else "")


BODY_DIGEST_RE = re.compile(r"body-sha256:\s*([0-9a-f]{64})")


def digests_in_commit_message(commit: str) -> set[str]:
    """Every `body-sha256: <hex>` Petar wrote into a commit message.

    The escape hatch of амандамент №5 т. 3: the freeze rewrites the signed body
    AFTER Petar's signing commit, so the newest commit on that path can be an
    agent's. It is accepted only when the human recorded the digest of the
    resulting body himself — in his own commit or on his own queue row."""
    body = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "-1", "--format=%B", commit],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if body.returncode != 0:
        return set()
    return set(BODY_DIGEST_RE.findall(body.stdout.decode("utf-8", "replace")))


def queue_digest_commit(queue_rel: str, body_digest: str) -> tuple[str, str] | None:
    """(hash, author) of the commit that INTRODUCED this digest into the queue.

    Амандамент №7 т. 2: a digest is Petar's word only where his own commit put
    it. `git log -S<digest> -- <queue>` lists the commits where the number of
    occurrences of that string moved, so the OLDEST of them is the one that
    wrote the number down; the newest would be whoever touched it last, which is
    the opposite question. `None` means no commit carries it — the number lives
    in the worktree, and the worktree is nobody's word."""
    try:
        lines = git_lines("log", "-S" + body_digest, "--format=%H\t%an", "--", queue_rel)
    except ValueError:
        return None
    if not lines:
        return None
    commit, _tab, who = lines[-1].partition("\t")
    return (commit, who)


def queue_authorship(rel: str) -> tuple[str, str | None]:
    """(author, complaint) — whose commit the queue is, or why it is nobody's.

    The complaint is None only for a committed queue whose newest commit is
    Petar's. Everything else — dirty in the worktree, in no commit at all, last
    touched by an agent — is a queue this gate reads for its rows and trusts for
    nothing (амандамент №6 т. 3)."""
    try:
        dirty = git_lines("status", "--porcelain", "--", rel)
        last = git_lines("log", "-1", "--format=%H\t%an", "--", rel)
    except ValueError as exc:
        return "", str(exc)
    if dirty:
        return "", "%s: не е комитнат — пушът праща блоба на HEAD" % rel
    if not last:
        return "", "%s: няма комит с този файл" % rel
    who = last[0].split("\t", 1)[1] if "\t" in last[0] else ""
    if who != HUMAN_AUTHOR:
        return who, ("%s: последният комит е на %r, а подписва само %s"
                     % (rel, who, HUMAN_AUTHOR))
    return who, None


def check_signature_authorship() -> Check:
    """Проверка 7 — a signature is worth the hand that committed it.

    План v2 §0.5 and амандамент №4 т. 6: the executors commit as `Claude
    Executor`, the architect as `Claude Architect`, and only Petar's own commit
    may INTRODUCE `signed_by: "Петър"`. Without this the barrier is a habit; with
    it, an agent that writes the signature itself is red on the next push, and
    the check names the commit and the author.

    The queue is read FIRST (амандамент №6 т. 3), because it is the document
    that can excuse everything else: a digest on one of its rows is what lets a
    body through after an agent rewrote it. Its authorship is therefore settled
    before a digest is taken out of it, and an untrusted queue hands over
    none — no row of this table says „Петър записа“ about a body he did not.

    And a queue that IS his is still only his word about the rows his own
    commits wrote (амандамент №8 т. 2). A digest introduced by an agent commit
    on a queue Petar later touched used to pass with the words „приет по
    опашка“; the auditor's scenario — agent rewrites the signed body, agent
    writes the digest of its result on the row, Petar makes one trivial commit
    to the queue — turned that sentence into a way through. It fails now."""
    check = Check("7 · авторството на подписите и на тялото (git log -S)")
    needle = release.SIGNATURE_NEEDLE
    targets = dict(release.SIGNABLE)
    allow_dir = REPO_ROOT / ALLOW_DIR
    for path in sorted(allow_dir.glob("*.json")) if allow_dir.exists() else []:
        targets["allow:" + path.name] = str(path.relative_to(REPO_ROOT)).replace("\\", "/")

    # --- the QUEUE first (амандамент №6 т. 3) -------------------------------
    # A digest Petar recorded on his row is what lets a body pass after an agent
    # rewrote it, so the queue is the one document that must be his BEFORE a
    # single digest is read out of it. A queue whose newest commit is an agent's
    # can carry any number at all — it hands over nothing here, and no line of
    # this table then says „Петър записа“ about a body it blessed.
    signed = 0
    # Амандамент №8 т. 2: `row_digests` holds ONLY the digests a commit of
    # Petar's put on the queue. The rest are not simply absent — a digest an
    # agent typed onto his row is an attempt, and the attempt is named — so they
    # are kept apart in `foreign_digests` as {artefact: {digest: (commit, who)}}.
    row_digests: dict[str, set[str]] = {}
    foreign_digests: dict[str, dict[str, tuple[str | None, str | None]]] = {}
    # {artefact: {digest: commit}} — where Petar's own accepted digest was
    # written down, for the line that says so.
    digest_origin: dict[str, dict[str, str]] = {}
    queue_trusted = False
    queue_rel = None
    try:
        queue_path = release.find_queue(None)
    except ValueError as exc:
        check.fail(str(exc))
        queue_path = None
    if queue_path is not None and queue_path.exists():
        queue_rel = str(queue_path.relative_to(REPO_ROOT)).replace("\\", "/")
        # The rows come out of the BLOB, never off the disk (амандамент №7 т. 2):
        # what a push publishes is the commit, and a digest read from a working
        # body is a number this gate has no author for. `queue_authorship` below
        # refuses a dirty queue anyway; reading the blob makes that refusal a
        # property of the reading, not a check somebody could reorder away.
        try:
            queue_rows = release.parse_queue_text(
                release.blob_at("HEAD", queue_rel).decode("utf-8"))
        except (ValueError, OSError, UnicodeDecodeError):
            # No blob at all — the queue is not committed. The rows are still
            # read, so the count below can say how many signatures are at stake;
            # `queue_authorship` refuses such a queue, so no digest of it is ever
            # taken.
            queue_rows = release.parse_queue(queue_path)
        yes_rows = [r for r in queue_rows if r["decision"] == release.YES]
        with_digest = [r for r in yes_rows if r["artefact"] and r.get("digest")]
        who, complaint = queue_authorship(queue_rel)
        queue_trusted = complaint is None
        if yes_rows:
            signed += len(yes_rows)
            if complaint:
                check.fail("%s (%d подписани реда)" % (complaint, len(yes_rows)))
            else:
                check.say("%s: %d подписани реда, комит на %s ✓"
                          % (queue_rel, len(yes_rows), who))
        if queue_trusted:
            for row in with_digest:
                # WHO introduced the number, not who committed the document it
                # sits in (амандамент №8 т. 2). A queue Petar committed is his
                # word about the ROWS he wrote; a digest an agent added to it in
                # an earlier commit rode in on his signature of the file.
                origin = queue_digest_commit(queue_rel, row["digest"]) or (None, None)
                if origin[1] == HUMAN_AUTHOR:
                    row_digests.setdefault(row["artefact"], set()).add(row["digest"])
                    digest_origin.setdefault(row["artefact"], {})[row["digest"]] = origin[0]
                else:
                    foreign_digests.setdefault(
                        row["artefact"], {})[row["digest"]] = origin
        elif with_digest:
            check.fail("%s: дайджестите на %d реда НЕ се приемат — авторството на "
                       "опашката не е потвърдено" % (queue_rel, len(with_digest)))

    for name in sorted(targets):
        rel = targets[name]
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            check.fail("%s: невалиден JSON — %s" % (rel, exc))
            continue
        if not coverage.is_signed_by_petar(release.signed_by_of(doc)):
            continue
        signed += 1
        try:
            if git_lines("status", "--porcelain", "--", rel):
                check.fail("%s: подписан, но НЕ е комитнат — пушът праща блоба на HEAD" % rel)
                continue
            author = release.introduced_by(rel, needle)
        except ValueError as exc:
            check.fail(str(exc))
            continue
        if author is None:
            check.fail("%s: подписът не е въведен от нито един комит" % rel)
            continue
        if author[1] != HUMAN_AUTHOR:
            check.fail("%s: подписът е въведен от %r в %s — подписва само %s"
                       % (rel, author[1], author[0][:7], HUMAN_AUTHOR))
            continue
        check.say("%s: подписан в %s от %s ✓" % (rel, author[0][:7], author[1]))

        # …and the BODY (амандамент №5 т. 3). A signature protects the bytes it
        # was given to: an agent commit that rewrites a signed artefact
        # afterwards leaves the `signed_by` literal untouched, so `git log -S`
        # never sees it. The newest commit on that path must therefore be
        # Petar's too — or he must have recorded the digest of the body that
        # came out, in his signing commit or on his queue row.
        try:
            newest = last_commit_on(rel)
            body = hashlib.sha256(release.blob_at("HEAD", rel)).hexdigest()
        except ValueError as exc:
            check.fail(str(exc))
            continue
        if newest is None:
            check.fail("%s: няма комит с този файл" % rel)
        elif newest[1] == HUMAN_AUTHOR:
            check.say("%s: тялото %s, последен комит %s от %s ✓"
                      % (rel, body[:12], newest[0][:7], newest[1]))
        else:
            in_message = digests_in_commit_message(author[0])
            artefact = name.split(":", 1)[0]
            on_row = row_digests.get(artefact, set())
            foreign = foreign_digests.get(artefact, {})
            # Where the number came from decides whether this line may PASS
            # (амандамент №8 т. 2). His own signing-commit message is his hand,
            # full stop; a number on a queue row is his hand only if his commit
            # is the one that introduced it. Until now the third case — a digest
            # an agent wrote onto his row — was accepted with the words „приет
            # по опашка“, which is exactly the attack: an agent rewrites the
            # signed body, writes the digest of its own result on the row, and
            # one trivial commit of Petar's on the queue makes the check green.
            # It is a failure now, and it names the hand and the commit.
            if body in in_message:
                check.say("%s: тялото %s е дайджестът, който Петър записа в %s ✓"
                          % (rel, body[:12], author[0][:7]))
            elif body in on_row:
                where = (digest_origin.get(artefact, {}).get(body) or "")[:7]
                check.say("%s: тялото %s е дайджестът, който Петър записа на "
                          "опашката в %s ✓" % (rel, body[:12], where))
            elif body in foreign:
                commit, who = foreign[body]
                check.fail("%s: дайджестът на тялото %s е въведен в опашката от "
                           "%r в %s, а подписва само %s"
                           % (rel, body[:12], who or "—",
                              commit[:7] if commit else "работното дърво",
                              HUMAN_AUTHOR))
            else:
                check.fail("%s: подписан, но последният комит по него е на %r "
                           "(%s), а дайджестът на тялото %s не е записан от %s"
                           % (rel, newest[1], newest[0][:7], body[:12], HUMAN_AUTHOR))

    check.say("%d подписани артефакта/реда проверени" % signed)
    return check


def main(argv: list[str]) -> int:
    # Without this the table dies with UnicodeEncodeError on a cp1252 console
    # before the first row — a crash that reads like a pass (одит 05.09, дефект 4).
    coverage.use_utf8_console()

    ap = argparse.ArgumentParser(description="Fire_Varna gates — one exit code")
    ap.add_argument("--base", help="git:<rev> — вместо подписания baseline")
    ap.add_argument("--allow", help="gates/allow/<ГГГГ-ММ-ДД>_<тема>.json")
    ap.add_argument("--queue", help="scratch/places_search/ЗА_ПОДПИС_<дата>.md")
    args = ap.parse_args(argv)

    checks = [
        check_sha_pins(),
        check_key_sets(),
        check_no_cad_ids(),
        check_coverage(args.base, args.allow),
        check_signed_facts(),
        check_release(args.queue),
        check_signature_authorship(),
    ]

    out = sys.stdout
    out.write("\n")
    for check in checks:
        out.write("%s %s\n" % (check.mark, check.name))
        for line in check.lines:
            out.write("      %s\n" % line)
    red = [c for c in checks if c.mark == BAD]
    yellow = [c for c in checks if c.mark == WARN]
    out.write("\n")
    if red:
        out.write("⛔ ЧЕРВЕНО: %s\n" % "; ".join(c.name for c in red))
        return 1
    if yellow:
        # Yellow blocks exactly like red: an unsigned baseline or allow-file is
        # not a lighter signature, it is no signature (Амандамент №1, т. 8).
        out.write("⚠ ЖЪЛТО — блокира пуша като червено: %s\n" % "; ".join(c.name for c in yellow))
        return 1
    out.write("✓ всички гейтове зелени\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
