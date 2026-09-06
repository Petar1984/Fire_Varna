#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gate for lot Н0 of the night plan "Границите" (06->07.09.2026).

Contract (plan §2а, row 1):
    python scratch/places_search/qa_night_pins.py --pins scratch/places_search/noshtna_pins_06.09.json
exit 0 means:
  * every sha256 in the pins is recomputed and equal (worktree files and git blobs),
  * `git check-ignore` says "ignored" for every declared geometry path,
  * `git ls-files scratch/boundary_gallery` returns 0 paths,
  * `base_rev` equals the recorded HEAD of varna_3d.

Negative fixtures (both MUST exit != 0):
  * --pins <copy with one flipped hex character>  -> a recomputed sha stops matching,
  * --worktree-negative -> a throw-away worktree where a geometry file is force-added
    with `git add -f`; the G29 check must fail THERE while staying green in the real tree.

Why a separate mode for the worktree: `git add -n` is a dry run and proves nothing, so the
fixture has to produce a really tracked geometry file, and it may only do that in a
throw-away worktree that is removed again in the same run.

Re-runnability after the lot is committed: the pins are written before the commit, so the
HEAD of the lot repository moves. Check C7 accepts that move only when the pinned head is
an ancestor of the current one and the commits in between touch nothing outside
`plan.lot_write_set` (see `lot_commit_allowance`); anything else is still red.

The gate reads only; it never writes into any of the three repositories.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

# stdout carries Bulgarian text; Windows consoles default to cp1252 without this.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CHUNK = 1024 * 1024


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def run(args, cwd=None):
    """Run a git/gh command and return (exit_code, stdout, stderr) as text."""
    proc = subprocess.run(
        args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return (
        proc.returncode,
        proc.stdout.decode("utf-8", "replace"),
        proc.stderr.decode("utf-8", "replace"),
    )


def git_show_sha256(repo_path, rev, rel_path):
    """sha256 of a blob as git stores it (LF), not of the working copy."""
    proc = subprocess.run(
        ["git", "-C", repo_path, "show", "%s:%s" % (rev, rel_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        return None, proc.stderr.decode("utf-8", "replace").strip()
    return hashlib.sha256(proc.stdout).hexdigest(), None


class Report(object):
    """Collects the verdict of every check so one run shows every failure at once."""

    def __init__(self):
        self.checks = []

    def add(self, name, ok, detail):
        self.checks.append((name, bool(ok), detail))
        print(u"%s %s — %s" % (u"[ЗЕЛЕНО]" if ok else u"[ЧЕРВЕНО]", name, detail))

    @property
    def failed(self):
        return [c for c in self.checks if not c[1]]


def repo_path_of(pins, repo_key):
    repos = pins.get("repos", {})
    if repo_key not in repos:
        raise KeyError(u"непознато репо в пиновете: %s" % repo_key)
    return repos[repo_key]["path"]


def check_shas(pins, report):
    """Every sha256 in the pins is recomputed from the bytes on disk / in git."""
    ok_all = True
    checked = 0
    for entry in pins["inputs"]:
        repo = repo_path_of(pins, entry["repo"])
        for rel in entry.get("worktree_paths", []):
            abs_path = os.path.join(repo, rel)
            if not os.path.isfile(abs_path):
                report.add(u"sha:%s:%s" % (entry["id"], rel), False, u"файлът липсва: %s" % abs_path)
                ok_all = False
                continue
            got = sha256_of_file(abs_path)
            want = entry["worktree_sha256"]
            checked += 1
            if got != want:
                report.add(
                    u"sha:%s:%s" % (entry["id"], rel),
                    False,
                    u"пинато %s, преизчислено %s" % (want, got),
                )
                ok_all = False
        blob = entry.get("blob")
        if blob:
            blob_repo = repo_path_of(pins, blob.get("repo", entry["repo"]))
            got, err = git_show_sha256(blob_repo, blob["rev"], blob["path"])
            checked += 1
            if got is None:
                report.add(u"sha-blob:%s" % entry["id"], False, u"git show падна: %s" % err)
                ok_all = False
            elif got != blob["sha256"]:
                report.add(
                    u"sha-blob:%s" % entry["id"],
                    False,
                    u"пинато %s, преизчислено %s" % (blob["sha256"], got),
                )
                ok_all = False
    report.add(
        u"C1 sha256 на всички пинати входове",
        ok_all,
        u"преизчислени %d стойности" % checked,
    )
    return ok_all


def check_dirty_baseline(pins, report):
    """The dirty tracked files are part of the base and are pinned by sha as well."""
    ok_all = True
    n = 0
    for repo_key, rows in pins.get("dirty_tracked", {}).items():
        repo = repo_path_of(pins, repo_key)
        code, out, _ = run(["git", "-C", repo, "status", "--porcelain", "--untracked-files=no"])
        observed = sorted(line[3:].strip() for line in out.splitlines() if line.strip())
        expected = sorted(row["path"] for row in rows)
        if observed != expected:
            report.add(
                u"мръсни файлове:%s" % repo_key,
                False,
                u"очаквани %s, намерени %s" % (expected, observed),
            )
            ok_all = False
            continue
        for row in rows:
            abs_path = os.path.join(repo, row["path"])
            got = sha256_of_file(abs_path)
            n += 1
            if got != row["worktree_sha256"]:
                report.add(
                    u"мръсен sha:%s:%s" % (repo_key, row["path"]),
                    False,
                    u"пинато %s, преизчислено %s" % (row["worktree_sha256"], got),
                )
                ok_all = False
            head_sha, err = git_show_sha256(repo, "HEAD", row["path"])
            n += 1
            if head_sha != row["head_blob_sha256"]:
                report.add(
                    u"мръсен blob:%s:%s" % (repo_key, row["path"]),
                    False,
                    u"пинато %s, преизчислено %s (%s)" % (row["head_blob_sha256"], head_sha, err),
                )
                ok_all = False
    report.add(
        u"C2 мръсният проследен диф е част от основата",
        ok_all,
        u"проверени %d стойности" % n,
    )
    return ok_all


def geometry_paths(pins):
    """(repo_key, relative path) for every input the pins declare as geometry."""
    out = []
    for entry in pins["inputs"]:
        if not entry.get("is_geometry_file"):
            continue
        for rel in entry.get("worktree_paths", []):
            out.append((entry["repo"], rel, entry["id"]))
    return out


def check_ignore(pins, report):
    """Every declared geometry path must be covered by an ignore rule."""
    ok_all = True
    rows = geometry_paths(pins)
    for repo_key, rel, ident in rows:
        repo = repo_path_of(pins, repo_key)
        code, out, _ = run(["git", "-C", repo, "check-ignore", "-v", "--", rel])
        if code != 0:
            report.add(
                u"check-ignore:%s:%s" % (repo_key, rel),
                False,
                u"НЕ Е игнориран (вход %s); една команда `git add` го прави проследен" % ident,
            )
            ok_all = False
    report.add(
        u"C3 git check-ignore за всеки геометричен път",
        ok_all,
        u"проверени %d пътя" % len(rows),
    )
    return ok_all


def check_not_tracked(pins, report):
    """G29: no declared geometry path may be tracked in Fire_Varna."""
    ok_all = True
    rows = geometry_paths(pins)
    for repo_key, rel, ident in rows:
        repo = repo_path_of(pins, repo_key)
        code, out, _ = run(["git", "-C", repo, "ls-files", "--error-unmatch", "--", rel])
        if code == 0 and out.strip():
            report.add(
                u"G29:%s:%s" % (repo_key, rel),
                False,
                u"ПРОСЛЕДЕНА геометрия (вход %s)" % ident,
            )
            ok_all = False
    report.add(u"C4 G29 нула проследена геометрия", ok_all, u"проверени %d пътя" % len(rows))
    return ok_all


def check_ls_files_gallery(pins, report):
    repo = repo_path_of(pins, "fire_varna")
    code, out, _ = run(["git", "-C", repo, "ls-files", "scratch/boundary_gallery"])
    n = len([line for line in out.splitlines() if line.strip()])
    ok = n == 0
    report.add(u"C5 git ls-files scratch/boundary_gallery", ok, u"%d проследени файла" % n)
    return ok


def check_base_rev(pins, report):
    base = pins["base_rev"]
    repo = repo_path_of(pins, base["repo"])
    code, out, _ = run(["git", "-C", repo, "rev-parse", "HEAD"])
    head = out.strip()
    ok = code == 0 and head == base["commit"]
    report.add(
        u"C6 base_rev == HEAD на %s" % base["repo"],
        ok,
        u"пинато %s, измерено %s" % (base["commit"], head),
    )
    branch_code, branch_out, _ = run(["git", "-C", repo, "rev-parse", "--abbrev-ref", "HEAD"])
    ok_branch = branch_out.strip() == base["branch"]
    report.add(
        u"C6б клонът на base_rev",
        ok_branch,
        u"пинато %s, измерено %s" % (base["branch"], branch_out.strip()),
    )
    return ok and ok_branch


def lot_commit_allowance(repo, pins, pinned_head, current_head):
    """How many commits of THIS lot sit between the pinned head and the current one.

    The pins are written before the lot is committed, so in the repository that
    receives the commit the HEAD moves by exactly the commits of the lot. The gate
    stays re-runnable after the commit only under two provable conditions: the
    pinned head is an ancestor of the current one, and the commits in between touch
    nothing outside `plan.lot_write_set`. Anything else is a failure.
    Returns (number of commits, explanation) or (None, reason for the failure).
    """
    code, _, _ = run(["git", "-C", repo, "merge-base", "--is-ancestor", pinned_head, current_head])
    if code != 0:
        return None, u"пинатият HEAD не е предшественик на текущия"
    _, names, _ = run(["git", "-C", repo, "diff", "--name-only", "%s..%s" % (pinned_head, current_head)])
    changed = sorted(p.strip() for p in names.splitlines() if p.strip())
    allowed = set(pins["plan"].get("lot_write_set", []))
    extra = [p for p in changed if p not in allowed]
    if extra:
        return None, u"пипнати файлове извън write-set-а на лота: %s" % extra
    _, cnt, _ = run(["git", "-C", repo, "rev-list", "--count", "%s..%s" % (pinned_head, current_head)])
    return int(cnt.strip() or 0), u"само write-set-ът на лота: %s" % changed


def check_heads_and_counts(pins, report):
    """HEAD, ahead and behind of the three repositories must match the pins."""
    ok_all = True
    lot_repo = pins["plan"].get("lot_repo")
    for repo_key, info in pins["repos"].items():
        repo = info["path"]
        _, head, _ = run(["git", "-C", repo, "rev-parse", "HEAD"])
        head = head.strip()
        extra_commits = 0
        if head != info["head"]:
            if repo_key != lot_repo:
                report.add(u"HEAD:%s" % repo_key, False, u"пинато %s, измерено %s" % (info["head"], head))
                ok_all = False
            else:
                extra_commits, why = lot_commit_allowance(repo, pins, info["head"], head)
                if extra_commits is None:
                    report.add(
                        u"HEAD:%s" % repo_key,
                        False,
                        u"пинато %s, измерено %s — %s" % (info["head"], head, why),
                    )
                    ok_all = False
                    extra_commits = 0
                else:
                    report.add(
                        u"HEAD:%s след комита на лота" % repo_key,
                        True,
                        u"%s → %s, %d комита, %s" % (info["head"][:7], head[:7], extra_commits, why),
                    )
        upstream = info["upstream"]
        branch = info["branch"]
        _, ahead, _ = run(["git", "-C", repo, "rev-list", "--count", "%s..%s" % (upstream, branch)])
        _, behind, _ = run(["git", "-C", repo, "rev-list", "--count", "%s..%s" % (branch, upstream)])
        want_ahead = info["ahead"] + extra_commits
        if int(ahead.strip() or -1) != want_ahead or int(behind.strip() or -1) != info["behind"]:
            report.add(
                u"ahead/behind:%s" % repo_key,
                False,
                u"очаквано %d/%d, измерено %s/%s" % (want_ahead, info["behind"], ahead.strip(), behind.strip()),
            )
            ok_all = False
    report.add(u"C7 HEAD и ahead/behind на трите репа", ok_all, u"%d репа" % len(pins["repos"]))
    return ok_all


def check_g19(pins, report):
    """G19: varna_3d must be PRIVATE, otherwise the whole varna_3d front stops."""
    g19 = pins["g19"]
    exe = g19["gh_path"]
    if not os.path.isfile(exe):
        report.add(u"C8 G19", False, u"gh липсва: %s" % exe)
        return False
    code, out, err = run([exe, "repo", "view", g19["repo"], "--json", "visibility"])
    visibility = None
    if code == 0 and out.strip():
        try:
            visibility = json.loads(out).get("visibility")
        except ValueError:
            visibility = None
    ok = visibility == g19["expected"]
    report.add(
        u"C8 G19 видимост на %s" % g19["repo"],
        ok,
        u"очаквано %s, измерено %r (изход %d) %s" % (g19["expected"], visibility, code, err.strip()),
    )
    return ok


def check_no_coordinates(pins, pins_path, report):
    """The pins file itself must carry zero geometry (red line 2)."""
    with open(pins_path, "rb") as fh:
        raw = fh.read().decode("utf-8")
    bad = [word for word in ("\"coordinates\"", "\"geometry\":", "LineString", "MultiPolygon") if word in raw]
    ok = not bad
    report.add(u"C9 нула геометрия в самите пинове", ok, u"намерени ключове: %s" % (bad or u"няма"))
    return ok


def normal_mode(pins_path):
    with open(pins_path, "rb") as fh:
        pins = json.loads(fh.read().decode("utf-8"))
    report = Report()
    check_shas(pins, report)
    check_dirty_baseline(pins, report)
    check_ignore(pins, report)
    check_not_tracked(pins, report)
    check_ls_files_gallery(pins, report)
    check_base_rev(pins, report)
    check_heads_and_counts(pins, report)
    check_g19(pins, report)
    check_no_coordinates(pins, pins_path, report)
    failed = report.failed
    print(u"")
    if failed:
        print(u"ГЕЙТ Н0: ЧЕРВЕН — паднали проверки: %d" % len(failed))
        for name, _, detail in failed:
            print(u"  · %s — %s" % (name, detail))
        return 1
    print(u"ГЕЙТ Н0: ЗЕЛЕН — %d проверки" % len(report.checks))
    return 0


def worktree_negative(pins_path):
    """Force-add a geometry file in a throw-away worktree; G29 must fail there."""
    with open(pins_path, "rb") as fh:
        pins = json.loads(fh.read().decode("utf-8"))
    repo = repo_path_of(pins, "fire_varna")
    rows = [r for r in geometry_paths(pins) if r[0] == "fire_varna"]
    if not rows:
        print(u"фикстурата няма геометричен път в Fire_Varna")
        return 4
    _, rel, ident = rows[0]
    source = os.path.join(repo, rel)

    base = tempfile.mkdtemp(prefix="qa_night_pins_wt_")
    work = os.path.join(base, "wt")
    detected_in_worktree = False
    green_in_real_tree = False
    try:
        code, out, err = run(["git", "-C", repo, "worktree", "add", "--detach", work, "HEAD"])
        if code != 0:
            print(u"не можах да създам worktree: %s" % err.strip())
            return 4
        target = os.path.join(work, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copyfile(source, target)
        code, out, err = run(["git", "-C", work, "add", "-f", "--", rel])
        if code != 0:
            print(u"git add -f падна: %s" % err.strip())
            return 4
        # G29 inside the throw-away worktree: the geometry file is now tracked there.
        code, out, _ = run(["git", "-C", work, "ls-files", "--error-unmatch", "--", rel])
        detected_in_worktree = code == 0 and bool(out.strip())
        # The same check in the real tree must stay green.
        code, out, _ = run(["git", "-C", repo, "ls-files", "--error-unmatch", "--", rel])
        green_in_real_tree = not (code == 0 and out.strip())
    finally:
        run(["git", "-C", repo, "worktree", "remove", "--force", work])
        run(["git", "-C", repo, "worktree", "prune"])
        shutil.rmtree(base, ignore_errors=True)

    print(u"фикстура G29: геометричен път %s (вход %s)" % (rel, ident))
    print(u"  проследен в еднократното worktree: %s" % (u"ДА" if detected_in_worktree else u"НЕ"))
    print(u"  реалното дърво остава чисто: %s" % (u"ДА" if green_in_real_tree else u"НЕ"))
    if detected_in_worktree and green_in_real_tree:
        print(u"ГЕЙТ G29 в worktree-то: ЧЕРВЕН, както изисква фикстурата (изход 3)")
        return 3
    print(u"ФИКСТУРАТА НЕ ДОКАЗА НИЩО — счупена фикстура (изход 4)")
    return 4


def main():
    parser = argparse.ArgumentParser(description="Гейт Н0: пинове, sha-та и доказателства за игнориране.")
    parser.add_argument("--pins", default="scratch/places_search/noshtna_pins_06.09.json")
    parser.add_argument(
        "--worktree-negative",
        action="store_true",
        help="еднократно worktree с git add -f върху геометрия; G29 трябва да падне ТАМ",
    )
    args = parser.parse_args()
    if args.worktree_negative:
        return worktree_negative(args.pins)
    return normal_mode(args.pins)


if __name__ == "__main__":
    sys.exit(main())
