import sys, threading, http.server, functools, json
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8768), functools.partial(Q, directory=sys.argv[1]))
threading.Thread(target=srv.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(); pg.add_init_script(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "fakeclaude.js")).read())
    pg.goto("http://127.0.0.1:8768/index.html")
    pg.wait_for_function("document.querySelector('#searchhint').textContent.startsWith('Matches')", timeout=180000)
    pg.wait_for_function("window.MathJax && MathJax.typesetPromise && MathJax.startup.promise", timeout=60000)
    pg.evaluate("MathJax.startup.promise")
    res = pg.evaluate("""async () => {
      const out = []; const box = document.createElement('div'); document.body.append(box);
      for (const q of D.qs) {
        const t = textOf(q); if (!t) continue;
        for (const [f, src] of [['question.tex', t.q], ['solution.tex', t.s]]) {
          box.innerHTML = '<div class=tex>' + texToHtml(src, {}, t.m, f, true) + '</div>';
          await MathJax.typesetPromise([box]);
          const errs = [...box.querySelectorAll('mjx-merror')].map(e => e.getAttribute('data-mjx-error') || e.textContent);
          const txt = box.innerText;
          const raw = [...new Set([...txt.matchAll(/\\\\[a-zA-Z]+|\\$/g)].map(m => m[0]))];
          if (errs.length || raw.length) out.push({id: q.id, file: f, errs: errs.slice(0,3), raw});
          MathJax.typesetClear([box]);
        }
      }
      return out; }""")
    json.dump(res, open(sys.argv[2], "w"), indent=1)
    print(len(res), "bodies with display problems")
    b.close()
srv.shutdown()
