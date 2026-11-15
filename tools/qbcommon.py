"""Shared helpers for the question bank tools.

Layout of the canonical store (this repo):
  questions/<hh>/<question-id>/metadata.json, question.tex, solution.tex, assets/*.svg
where <hh> = first two hex digits of sha1(question-id). This keeps every
directory small (~125 questions) for git and the GitHub web UI.
"""
import hashlib, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, "questions")
STATE = os.path.join(ROOT, "state")

def hx(qid):
    return hashlib.sha1(qid.encode("utf-8")).hexdigest()

def shard2(qid):   # repo directory + diagram chunk
    return hx(qid)[:2]

def shard1(qid):   # text chunk + database overlay shard
    return hx(qid)[0]

def svgchunk(qid):  # diagram chunk file used by the website (64 files)
    return f"{int(hx(qid)[:2], 16) // 4:02x}"

def qpath(qid):
    return os.path.join(QDIR, shard2(qid), qid)

def iter_questions():
    for sh in sorted(os.listdir(QDIR)):
        d = os.path.join(QDIR, sh)
        if not os.path.isdir(d):
            continue
        for qid in sorted(os.listdir(d)):
            yield qid, os.path.join(d, qid)

def read_question(qdir):
    with open(os.path.join(qdir, "metadata.json"), encoding="utf-8") as f:
        meta = json.load(f)
    def rd(name):
        p = os.path.join(qdir, name)
        return open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    q = rd(meta.get("question_file", "question.tex"))
    s = rd(meta.get("solution_file", "solution.tex"))
    assets = {}
    for a in meta.get("assets", []):
        p = os.path.join(qdir, a["path"])
        if os.path.exists(p) and p.endswith(".svg"):
            assets[a["path"]] = open(p, encoding="utf-8").read()
    return meta, q, s, assets

def load_state(name, default):
    p = os.path.join(STATE, name)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return default

def save_state(name, obj):
    os.makedirs(STATE, exist_ok=True)
    with open(os.path.join(STATE, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
