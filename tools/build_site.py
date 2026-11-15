"""Build the website's data files from questions/ and state/.

Usage: python3 tools/build_site.py [--out site/data]

Writes (each file is JSON {"gz": base64 of the gzipped JSON payload}):
  index.json      one compact row per question, used for filtering
  text/t<h>.json  metadata + question/solution LaTeX, 16 chunks by sha1(id)[0]
  svg/s<nn>.json  diagram previews, 64 chunks: nn = two-hex-digit int(sha1(id)[:2], 16) // 4
  base_state.json folders/placements/trash/flags from state/ (used by the
                     standalone page when no Claude database is available)
The page (site/index.html) loads index first, then text chunks in the
background, and diagram chunks only when a question is opened.
"""
import base64, gzip, json, os, shutil, sys, time
from collections import defaultdict
from qbcommon import ROOT, iter_questions, read_question, shard1, svgchunk, load_state

def gz(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    # The artifact host only serves a fixed set of file extensions (no .gz),
    # so each file is JSON of the form {"gz": "<base64 of gzipped JSON>"}.
    b64 = base64.b64encode(gzip.compress(data, 9, mtime=0)).decode("ascii")
    with open(path, "w", encoding="ascii") as f:
        f.write('{"gz":"' + b64 + '"}')
    return len(data)

def build(out):
    if os.path.isdir(out): shutil.rmtree(out)
    tags, tagi, comps, compi = [], {}, [], {}
    def ti(t):
        if t not in tagi: tagi[t] = len(tags); tags.append(t)
        return tagi[t]
    def ci(c):
        if c is None: return -1
        if c not in compi: compi[c] = len(comps); comps.append(c)
        return compi[c]
    rows, text, svg = [], defaultdict(dict), defaultdict(dict)
    for qid, d in iter_questions():
        meta, q, s, assets = read_question(d)
        src = meta.get("source") or {}
        rows.append([qid, [ti(t) for t in meta.get("tags", [])], meta.get("difficulty"),
                     ci(src.get("competition")), src.get("year"), src.get("division"),
                     src.get("question_number"), len(meta.get("diagram_previews", [])), shard1(qid)])
        text[shard1(qid)][qid] = {"m": meta, "q": q, "s": s}
        if assets:
            svg[svgchunk(qid)][qid] = assets
    raw = gz(os.path.join(out, "index.json"),
             {"built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "tags": tags, "comps": comps, "rows": rows})
    for h in "0123456789abcdef":
        raw += gz(os.path.join(out, "text", f"t{h}.json"), text.get(h, {}))
    for k in range(64):
        raw += gz(os.path.join(out, "svg", f"s{k:02x}.json"), svg.get(f"{k:02x}", {}))
    gz(os.path.join(out, "base_state.json"), {
        "folders": load_state("folders.json", {}),
        "placements": load_state("placements.json", {}),
        "trash": load_state("trash.json", {}),
        "flags": load_state("flags.json", {})})
    return len(rows), raw

if __name__ == "__main__":
    out = os.path.join(ROOT, "site", "data")
    if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
    n, raw = build(out)
    tot = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(out) for f in fs)
    print(f"{n} questions; {raw/1e6:.1f} MB raw -> {tot/1e6:.2f} MB gzipped in {out}")
