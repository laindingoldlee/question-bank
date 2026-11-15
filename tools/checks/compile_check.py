"""Compile every question/solution body with pdflatex and attribute errors to IDs.
Usage: python3 check.py REPO_ROOT OUTDIR [ids.txt]"""
import sys, os, re, json, subprocess, concurrent.futures as cf
sys.path.insert(0, os.path.join(sys.argv[1], "tools")); import qbcommon as qc
OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
only = set(open(sys.argv[3]).read().split()) if len(sys.argv) > 3 else None
PRE = r"""\documentclass[11pt]{article}
\usepackage{amsmath,amssymb,textcomp,enumitem,verbatim}
\newenvironment{asy}{\comment}{\endcomment}
\setlength{\parindent}{0pt}\hbadness=10000\vbadness=10000\hfuzz=\maxdimen
\begin{document}
"""
items = []
for qid, d in qc.iter_questions():
    if only and qid not in only: continue
    m, q, s, a = qc.read_question(d)
    items.append((qid, "question", q)); items.append((qid, "solution", s))
def strip(t):  # drop comment-only header lines; keep body
    return "\n".join(l for l in t.split("\n") if not l.lstrip().startswith("%"))
CH = 400
chunks = [items[i:i+CH] for i in range(0, len(items), CH)]
def run(k):
    name = f"c{k:03d}"; body = []
    for qid, f, t in chunks[k]:
        body.append(f"\\typeout{{@@Q {qid} {f}}}\n{strip(t)}\n\\par\\typeout{{@@E}}\n")
    open(f"{OUT}/{name}.tex", "w").write(PRE + "\n".join(body) + "\n\\end{document}\n")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "-draftmode", name + ".tex"], cwd=OUT,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
    log = open(f"{OUT}/{name}.log", encoding="latin-1").read().split("\n")
    errs = []; cur = None
    for i, l in enumerate(log):
        mm = re.match(r"@@Q (\S+) (\S+)", l)
        if mm: cur = (mm.group(1), mm.group(2)); continue
        if l.startswith("! "):
            ctx = " ".join(x.strip() for x in log[i+1:i+3])
            errs.append({"id": cur[0] if cur else None, "file": cur[1] if cur else None, "err": l[2:], "ctx": ctx[:200]})
    if "Emergency stop" in "\n".join(log) or "end of file" in "\n".join(log[-30:]):
        errs.append({"id": cur[0] if cur else None, "file": cur[1] if cur else None, "err": "CHUNK ABORTED", "ctx": ""})
    return errs
allerr = []
with cf.ThreadPoolExecutor(8) as ex:
    for e in ex.map(run, range(len(chunks))): allerr += e
json.dump(allerr, open(f"{OUT}/errors.json", "w"), indent=1)
ids = sorted({(e["id"], e["file"]) for e in allerr if e["id"]})
print(len(items), "bodies;", len(allerr), "errors in", len({i for i, _ in ids}), "questions;",
      sum(e["err"] == "CHUNK ABORTED" for e in allerr), "aborted chunks")
