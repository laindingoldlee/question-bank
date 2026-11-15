"""Import a full export from the old website (import-ZIP format) as the master copy.

Usage: python3 tools/import_backup.py BACKUP.zip

Every question in the ZIP replaces the repo copy (the old site held the
latest edits). A "note" field already in the repo is kept when the
export has none, because the old site's export drops editorial notes.
"""
import json, os, shutil, sys, zipfile
from qbcommon import qpath

def main(path):
    z = zipfile.ZipFile(path)
    ids = json.loads(z.read("manifest.json"))["question_ids"]
    names = {}
    for n in z.namelist():
        p = n.split("/")
        if len(p) >= 3 and p[0] == "questions" and not n.endswith("/"):
            names.setdefault(p[1], []).append(n)
    added = replaced = kept_notes = 0
    for qid in ids:
        dest = qpath(qid)
        note = None
        if os.path.exists(dest):
            try: note = json.load(open(os.path.join(dest, "metadata.json"), encoding="utf-8")).get("note")
            except Exception: pass
            shutil.rmtree(dest); replaced += 1
        else:
            added += 1
        pre = f"questions/{qid}/"
        for n in names.get(qid, []):
            out = os.path.join(dest, n[len(pre):])
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, "wb") as f: f.write(z.read(n))
        if note:
            mp = os.path.join(dest, "metadata.json")
            m = json.load(open(mp, encoding="utf-8"))
            if not m.get("note"):
                m["note"] = note
                json.dump(m, open(mp, "w", encoding="utf-8"), indent=2, ensure_ascii=False); kept_notes += 1
    print(f"{len(ids)} questions: {added} added, {replaced} replaced, {kept_notes} notes kept")

if __name__ == "__main__":
    main(sys.argv[1])
