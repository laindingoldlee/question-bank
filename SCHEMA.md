# Schema

## Question folder (`questions/<hh>/<id>/`)

Identical to a question folder inside `question_bank_import.zip` (schema 1.0); the full spec is `Question_Bank_Import_Prompt_Complete_Detailed.md` in the owner's project files.

- **ID**: `aops-topic-<topic_id>-q<part:02>` for AoPS questions. IDs are permanent and never reused; re-imports of an existing ID are skipped.
- **`<hh>`**: first two hex digits of `sha1(id)` (UTF-8). Only there to keep directories small.
- **metadata.json** (main fields):

```json
{
  "id": "aops-topic-2887230-q01",
  "source": {"competition": "AMC 8", "year": 2019, "division": null, "paper": null, "round": null, "question_number": 12},
  "tags": ["Equilateral triangles", "Pythagorean theorem"],
  "difficulty": 1,
  "difficulty_rationale": "Immediate application of a definition or basic fact.",
  "question_file": "question.tex",
  "solution_file": "solution.tex",
  "latex_dependencies": {"packages": [{"name": "amsmath", "options": []}], "tikz_libraries": [], "preamble_commands": []},
  "assets": [{"path": "assets/<id>-solution-diagram-01.svg", "type": "image", "usage": "..."}],
  "diagram_previews": [{"file": "solution.tex", "index": 1, "path": "assets/...svg", "source_sha256": "...", "alt": "..."}],
  "note": "editorial changes, if any"
}
```

- **question.tex / solution.tex**: LaTeX body only (no preamble). The first lines are `%` comments with the AoPS URL and ID. Diagrams are inline `\begin{asy} ... \end{asy}`; `diagram_previews[i].index` is the 1-based position of that block within its file.
- Tags come from a controlled vocabulary; difficulty is an integer 1 to 7 (8 allowed with a rationale).

## State files (`state/`)

Changes made on the website, copied back into the repo by `tools/apply_overlay.py`.

| File | Shape |
|---|---|
| folders.json | `{folderId: {"name": str, "parent": folderId or null, "created": iso}}` |
| placements.json | `{questionId: folderId}`; a question is in at most one folder; absent = Unfiled |
| trash.json | `{questionId: {"at": iso}}` deleted but recoverable |
| flags.json | `{questionId: {"note": str, "at": iso}}` problems the owner wants fixed |

## Website data files (`site/data/`, generated)

Each file is JSON `{"gz": "<base64 of gzipped JSON>"}`, because the artifact host does not serve `.gz` files. The page also accepts plain JSON.

| File | Payload |
|---|---|
| index.json | `{"built", "tags": [names], "comps": [competition names], "rows": [[id, [tag indexes], difficulty, comp index or -1, year, division, question_number, n_diagrams, sha1(id)[0]]]}` |
| text/t<h>.json (16 files, h = sha1(id)[0]) | `{id: {"m": metadata, "q": question.tex, "s": solution.tex}}` |
| svg/s<nn>.json (64 files, nn = int(sha1(id)[:2], 16) // 4 as 2 hex digits) | `{id: {asset path: svg text}}` |
| base_state.json | `{"folders", "placements", "trash", "flags"}` from `state/` (used in standalone mode) |

## Website database (Claude artifact mode)

The page keeps only what changes on the page in the artifact database (limit: 25,000 documents, 256 KiB each, 100 MB total). Overlay maps are sharded by `h = sha1(id)[0]` so each document stays small.

| Path | Body |
|---|---|
| `folders/<folderId>` | `{"name", "parent", "created"}` |
| `place/<h>` | `{"m": {questionId: folderId or null}}` (null = Unfiled) |
| `trash/<h>` | `{"m": {questionId: {"at", "purged"?} or null}}`; `purged: true` = deleted forever, removed from the repo at the next backup |
| `flags/<questionId>` | `{"note", "at"}` |
| `imported/<questionId>` | `{"m": metadata, "q", "s", "assets": {path: svg}, "at", "from"}` questions imported on the page, not yet in the repo |
| `meta/backup` | `{"at", "repo", "note"}` time of the last copy into GitHub |

Write access is limited to the artifact's owner (`rules: [{path: "", read: "view", write: "owner"}]`).
