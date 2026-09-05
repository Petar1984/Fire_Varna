"""F12-ж gate: a manifest anchor that names a commit carries the BLOB's bytes.

  python manifest_anchor_gate.py               # the tracked manifests -> expect PASS
  python manifest_anchor_gate.py --broken DIR  # write disk-byte copies into DIR
                                               # and gate THOSE  -> expect FAIL (exit 2)

The second form is the deliberately broken input: every commit-named anchor is
recomputed from the file on disk, exactly as the generator did before F12-ж. On
a Windows worktree the reference is the CRLF twin of its blob (266 021 B against
256 070 B, same OID, `git status` clean), so the disk anchor is a different claim
about the same commit — and the gate has to say so. A gate that has never failed
is not a gate.

The rule itself lives in recall_sweep.py (`check_manifest_anchors`), which is
what the generator calls on what it has just written. One rule, one place.
"""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]

spec = importlib.util.spec_from_file_location("rs", str(HERE / "recall_sweep.py"))
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)

# The manifests Petar is asked to sign, plus the лот 1в-В one that carries the
# same anchor and was corrected by hand in F11-х — the gate now holds all three
# to the same rule instead of trusting the hand.
MANIFESTS = [u"lot1v_v_manifest_BASE_P7.json",
             u"lot1v_v_manifest_P7_F12.json",
             u"lot1v_v_reference_manifest.json"]


def break_anchors(src_dir, dst_dir):
    """Rewrite every commit-named anchor with the bytes of the file on disk."""
    dst_dir.mkdir(parents=True, exist_ok=True)
    out, broken = [], 0
    for name in MANIFESTS:
        doc = json.loads((src_dir / name).read_text(encoding="utf-8"))
        for _where, anchor in rs.commit_anchors(doc):
            on_disk = rs.sha_and_bytes(str(REPO / anchor["path"]))
            anchor["sha256"] = on_disk["sha256"]
            anchor["bytes"] = on_disk["bytes"]
            broken += 1
        target = dst_dir / name
        target.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
                          encoding="utf-8", newline="\n")
        out.append(str(target))
    return out, broken


def main():
    if "--broken" in sys.argv:
        dst = pathlib.Path(sys.argv[sys.argv.index("--broken") + 1]).resolve()
        paths, broken = break_anchors(HERE, dst)
        print(u"счупен вход: %d котви преписани с байтовете от диска -> %s"
              % (broken, dst))
    else:
        paths = [str(HERE / name) for name in MANIFESTS]

    anchors = 0
    for path in paths:
        doc = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
        for where, anchor in rs.commit_anchors(doc):
            anchors += 1
            print(u"  %-34s %-14s %s:%s -> %s / %d B"
                  % (pathlib.Path(path).name, where, anchor["commit"],
                     anchor["path"].rsplit(u"/", 1)[-1],
                     anchor["sha256"][:12], anchor["bytes"]))
    complaints = rs.check_manifest_anchors(paths)
    if complaints:
        print(u"ЧЕРВЕНО (%d):" % len(complaints))
        for line in complaints:
            print(u"  x " + line)
        return 2
    print(u"ЗЕЛЕНО: %d котви, всяка = блобът на назования комит (%d манифеста)"
          % (anchors, len(paths)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
