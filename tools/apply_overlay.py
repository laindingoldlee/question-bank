"""Fold the website's overlay (changes made on the page) into this repo.

Usage: python3 tools/apply_overlay.py dump.json

dump.json is a copy of the page database, shaped as
  {"folders": {fid: {...}}, "place": {h: {"m": {qid: fid|null}}},
   "trash": {h: {"m": {qid: {"at": iso, "purged": bool}|null}}},
   "flags": {qid: {"note": str, "at": iso}}, "imported": {qid: {"m","q","s","assets"}}}
(With Claude's artifact tools: db_list each collection and save the docs.)

Effects:
  * state/folders.json, placements.json, trash.json, flags.json are rewritten
  * imported questions are written into questions/ (existing IDs are kept)
  * purged questions are deleted from questions/ and from state
Prints what to clean up in the database afterwards (imported docs to
delete, purged trash entries to remove).
"""
import json, os, shutil, sys
from qbcommon import qpath, save_state

def main(path):
    d = json.load(open(path, encoding="utf-8"))
    folders = d.get("folders", {})
    place, trash, purged = {}, {}, []
    for h, doc in d.get("place", {}).items():
        for q, f in (doc.get("m") or {}).items():
            if f: place[q] = f
    for h, doc in d.get("trash", {}).items():
        for q, t in (doc.get("m") or {}).items():
            if not t: continue
            if t.get("purged"): purged.append(q)
            else: trash[q] = t
    added = []
    for qid, doc in d.get("imported", {}).items():
        dest = qpath(qid)
        if os.path.exists(dest):
            continue
        m = doc["m"]
        os.makedirs(dest)
        json.dump(m, open(os.path.join(dest, "metadata.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        open(os.path.join(dest, m.get("question_file", "question.tex")), "w", encoding="utf-8").write(doc.get("q", ""))
        open(os.path.join(dest, m.get("solution_file", "solution.tex")), "w", encoding="utf-8").write(doc.get("s", ""))
        for p, svg in (doc.get("assets") or {}).items():
            os.makedirs(os.path.dirname(os.path.join(dest, p)), exist_ok=True)
            open(os.path.join(dest, p), "w", encoding="utf-8").write(svg)
        added.append(qid)
    for qid in purged:
        if os.path.exists(qpath(qid)): shutil.rmtree(qpath(qid))
        place.pop(qid, None); d.get("flags", {}).pop(qid, None)
    known = set(folders)
    place = {q: f for q, f in place.items() if f in known}
    save_state("folders.json", folders)
    save_state("placements.json", place)
    save_state("trash.json", trash)
    save_state("flags.json", d.get("flags", {}))
    print(json.dumps({"imported_into_repo": added, "purged_from_repo": purged,
                      "db_cleanup": {"delete_imported_docs": list(d.get("imported", {})),
                                     "remove_trash_entries": purged}}, indent=1))

if __name__ == "__main__":
    main(sys.argv[1])
