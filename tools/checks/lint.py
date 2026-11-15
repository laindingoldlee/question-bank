"""Semantic LaTeX lint mirroring the website renderer's math detection."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")); import qbcommon as qc
MATH_RE = re.compile(r"\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$(?:\\.|[^$\\])+?\$|\\begin\{(equation|align|gather|multline|eqnarray|alignat|array|aligned|cases|pmatrix|bmatrix|vmatrix|matrix|smallmatrix|gathered)(\*?)\}[\s\S]*?\\end\{\1\2\}")
MATHONLY = set("""dfrac frac tfrac sqrt cdot times div le ge leq geq ne neq pm mp infty sum prod int alpha beta gamma delta epsilon varepsilon zeta eta theta lambda mu nu xi pi rho sigma tau phi varphi chi psi omega Gamma Delta Theta Lambda Pi Sigma Phi Omega angle triangle circ equiv pmod bmod binom lfloor rfloor lceil rceil cdots overline overrightarrow left right mathbb mathbf mathrm mathcal boxed implies iff Rightarrow rightarrow to in notin subset subseteq cup cap emptyset perp parallel cong sim approx log ln sin cos tan gcd lcm max min vdots ddots mid nmid geqslant leqslant displaystyle""".split())
def clean(t):
    t = "\n".join(l for l in t.split("\n") if not l.lstrip().startswith("%"))
    t = re.sub(r"(^|[^\\])%[^\n]*", r"\1", t)
    t = re.sub(r"\\begin\{asy\}[\s\S]*?\\end\{asy\}", " ", t)
    t = re.sub(r"\\begin\{verbatim\}[\s\S]*?\\end\{verbatim\}", " ", t)
    t = re.sub(r"\\verb(.)[\s\S]*?\1", " ", t)
    t = t.replace(r"\$", " ")
    return t
def strip_text_args(m):
    # remove \text{...}, \mbox{...}, \textbf{...}, \mathrm{...}, \operatorname{...} contents (one level of nesting)
    return re.sub(r"\\(?:text|mbox|textbf|textit|textrm|mathrm|operatorname|texttt|emph)\s*\{(?:[^{}]|\{[^{}]*\})*\}", " ", m)
def lint(t):
    issues = []
    c = clean(t)
    parts = []; last = 0
    for mm in MATH_RE.finditer(c):
        parts.append(("text", c[last:mm.start()])); parts.append(("math", mm.group(0))); last = mm.end()
    parts.append(("text", c[last:]))
    for kind, seg in parts:
        if kind == "text":
            if "$" in seg: issues.append(("stray $", seg[max(0, seg.index('$')-50):seg.index('$')+50]))
            if re.search(r"\\\[|\\\]", seg) and not re.search(r"\\\\\[", seg): issues.append(("stray \\[", seg[:100]))
            cmds = [x for x in re.findall(r"\\([A-Za-z]+)", seg) if x in MATHONLY]
            if cmds: 
                i = seg.index("\\" + cmds[0]); issues.append(("math command in text: \\" + cmds[0], seg[max(0, i-50):i+60]))
            # ^ or _ in text (not escaped)
            mm = re.search(r"(?<!\\)[\^_]", re.sub(r"\\begin\{[^}]*\}|\\end\{[^}]*\}|\\(?:label|ref|url|href)\{[^}]*\}", "", seg))
            if mm: issues.append(("^ or _ in text", seg[max(0, mm.start()-50):mm.start()+50]))
        else:
            inner = strip_text_args(seg)
            inner = re.sub(r"\\(?:begin|end)\{[^}]*\}(\{[^}]*\})?", " ", inner)
            words = [w for w in re.findall(r"(?<![\\A-Za-z])[a-z]{4,}(?![A-Za-z])", inner)]
            # words not part of a command
            if len(words) >= 3: issues.append(("words in math", seg[:160]))
    return issues
res = {}; cnt = collections.Counter()
for qid, d in qc.iter_questions():
    m, q, s, a = qc.read_question(d)
    for f, t in (("question", q), ("solution", s)):
        iss = lint(t)
        if iss:
            res.setdefault(qid, {})[f] = iss
            for k, _ in iss: cnt[k.split(":")[0]] += 1
json.dump(res, open("lint.json", "w"), indent=1)
print(len(res), "questions flagged"); print(cnt.most_common())
