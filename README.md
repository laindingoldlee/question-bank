# Question Bank

A private bank of competition-maths questions (AoPS middle-school forum problems, cleaned, solved, tagged and rated), with a browsing website.

- **This repo is the master copy.** Every question lives here as plain files, in the same format as the import ZIPs.
- **The website** is a single HTML page (`site/index.html`) plus data files generated from this repo. It is currently hosted as a private Claude artifact, but it runs anywhere that can serve static files.

Start with **HANDOVER.md** if you are taking over maintenance. **SCHEMA.md** describes every file format.

## Layout

```
questions/<hh>/<question-id>/     one folder per question; <hh> = first 2 hex digits of sha1(id)
    metadata.json                 tags, difficulty, source, diagram previews, ...
    question.tex                  question body (LaTeX)
    solution.tex                  solution body (LaTeX, may contain \begin{asy} diagrams)
    assets/*.svg                  rendered previews of the Asymptote diagrams
state/                            things changed on the website (copied back by the maintainer)
    folders.json  placements.json  trash.json  flags.json
site/index.html                   the whole website (HTML + CSS + JS in one file)
site/data/                        generated, not committed: run tools/build_site.py
tools/                            Python scripts (no dependencies beyond the standard library)
```

## Common tasks

```bash
python3 tools/import_zip.py path/to/question_bank_import.zip   # add questions (existing IDs are skipped)
python3 tools/build_site.py                                     # regenerate site/data/
python3 -m http.server -d site 8000                             # open http://localhost:8000 (standalone mode)
```

## Features of the website

- Filter by tags (has all / has any, click twice to exclude), difficulty, competition and year, "has a diagram"; every option shows a live count.
- Full-text search over questions and solutions; pasting a question ID opens it.
- Folders (nested), move questions between them, Trash with restore, "Flag for Claude" notes.
- Export any selection as a ZIP in the import format, or as a ready-to-compile `.tex` problem set.
- Import ZIPs in the import format from the page.
