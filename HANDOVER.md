# Handover: maintaining the question bank

Written for whoever maintains this next: a person or an AI assistant. The owner is a maths teacher who does not write code; they say what to change in plain language and expect the maintainer to do it end to end.

## How the pieces fit

1. **This repo** holds every question (`questions/`) and the record of page-side changes (`state/`). It is the master copy; anything not here can be lost.
2. **`tools/build_site.py`** turns the repo into `site/data/` (compressed JSON chunks).
3. **`site/index.html` + `site/data/`** is the website. It is currently a private Claude artifact:
   - URL: https://claude.ai/artifact/K9r6j6DUpcm9aqkiTX3jog (slug `9300b446-791d-435f-889b-41a2cd0ddeab`)
   - Things the owner changes on the page (folders, moves, deletes, flags, ZIP imports) go to the artifact's database, not to `site/data/`. They reach the repo when the maintainer runs a backup (below).
4. **Without Claude**, the same page works from any static host (GitHub Pages, Netlify, `python3 -m http.server`). It then runs in *standalone mode*: it starts from `state/` and keeps page-side changes in the browser's localStorage. For multi-device editing, replace the `LocalStore` class in `site/index.html` with one backed by a real database; `ClaudeStore` shows the interface (start, writeShards, setFolder, deleteFolder, setFlag, clearFlag, putImported).

## Routine jobs

### Fix or edit questions ("the answer to X is wrong", "retag all ...")
1. Edit the files under `questions/<hh>/<id>/`. Keep the owner's content rules (see below).
2. `python3 tools/build_site.py`
3. Republish `site/` (Claude: `publish_files` with the list from `python3 tools/publish_list.py`, mode `replace`, slug above). The database is untouched by a republish.
4. Commit and push.

### "Fix the flagged questions"
Read the `flags` collection (Claude: `db_list` collection `flags`). Fix each question, then delete its flag doc and remove it from `state/flags.json`.

### Add a new batch
`python3 tools/import_zip.py <zip>`, then build, republish, push.

### Backup (copy page-side changes into the repo)
Do this at the start of any session that changes questions, and at least weekly.
1. Dump the database: `db_list` the collections `folders`, `place`, `trash`, `flags`, `imported` and save them as one JSON file shaped as described in `tools/apply_overlay.py`.
2. `python3 tools/apply_overlay.py dump.json`; it updates `state/`, writes imported questions into `questions/`, and deletes purged ones.
3. Clean the database as the script prints: delete the `imported/<id>` docs, and remove purged entries from `trash/<h>` (set them to null with an `update`, or rewrite the doc).
4. Build, republish, set `meta/backup` to `{"at": <now>, "repo": "laindingoldlee/question-bank"}`, commit and push.

## Owner's content rules (summary)

- Stable IDs `aops-topic-<topic_id>-q<part:02>`; never reuse or renumber.
- Maths questions only. Every question must be well posed with one verified answer (or a proof); fix wrong posted answers, typos and impossible conditions, and record each change in `metadata.note`.
- Tags only from the controlled vocabulary; difficulty 1 to 7 with a rationale.
- LaTeX: `\dfrac` for every fraction (no `\frac`, `\tfrac`, `/`), ASCII only, balanced braces and `$`.
- Diagrams: Asymptote only, inline in the .tex; each gets an SVG preview in `assets/` with sha256 and alt text. Geometry-tagged questions need a sketch in the solution.

The full spec is `Question_Bank_Import_Prompt_Complete_Detailed.md` in the owner's Claude project "Batches".

## Status

- All 32,212 questions imported on 2026-11-15 from the old site's full export (`aops_question_bank_backup_all_middle.zip`, import format) with `tools/import_backup.py`. That export had no folders and no editorial notes, so `state/` starts empty.
- Site data is about 38 MB; first results show in about 3 s and filters respond in under 0.5 s.
- LaTeX clean-up done 2026-11-15 (see docs/latex_cleanup_2026-11-15.md): all bodies compile with pdflatex and display correctly on the site. Re-run tools/checks/ after bulk edits.
