"""Import question_bank_import.zip files (schema 1.0) into questions/.

Usage: python3 tools/import_zip.py [--replace] ZIP [ZIP ...]

Existing IDs are skipped (stable IDs mean a re-upload is a no-op) unless
--replace is given, in which case the stored copy is overwritten.
"""
import io, json, os, shutil, sys, zipfile
from qbcommon import qpath

def import_zip(path, replace=False):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    man = json.loads(z.read("manifest.json"))
    added, skipped, replaced = [], [], []
    for qid in man["question_ids"]:
        pre = f"questions/{qid}/"
        dest = qpath(qid)
        if os.path.exists(dest):
            if not replace:
                skipped.append(qid); continue
            shutil.rmtree(dest); replaced.append(qid)
        else:
            added.append(qid)
        for n in names:
            if n.startswith(pre) and not n.endswith("/"):
                rel = n[len(pre):]
                out = os.path.join(dest, rel)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, "wb") as f:
                    f.write(z.read(n))
    return added, skipped, replaced

if __name__ == "__main__":
    args = sys.argv[1:]
    rep = "--replace" in args
    args = [a for a in args if a != "--replace"]
    for p in args:
        a, s, r = import_zip(p, rep)
        print(f"{os.path.basename(os.path.dirname(p)) or p}: added {len(a)}, skipped {len(s)}, replaced {len(r)}")
