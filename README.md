# Sudoku Lab

A minimal, elegant Sudoku website built with **Python, FastAPI, and vanilla JavaScript**. Five difficulty presets, a unique solution for each generated puzzle, pencil notes, keyboard support, timer, local progress saving, and dark mode.

## Run locally

Requires Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Visit **http://127.0.0.1:8000**. API documentation: `/api/docs`.

Run tests: `pytest -q`.

## Project layout

```text
app/sudoku.py          Pure Python Sudoku engine
app/main.py            HTTP API and static file serving
app/static/index.html  Accessible page structure
app/static/style.css   Responsive design and themes
app/static/app.js      Browser interactions and local storage
tests/                 Engine and API tests
render.yaml            Render hosting configuration
.github/workflows/     GitHub Actions tests
```

## How generation works

1. Fill a blank grid using randomized backtracking and minimum-remaining-values selection.
2. Remove digits in random order.
3. After each removal, count solutions (stopping at two); restore any clue whose removal would make the puzzle ambiguous.
4. Stop at the target clue count or when no more clues can be removed safely.

**Difficulty caveat:** The five presets use clue-count targets (Easy 36, Medium 32, Hard 28, Expert 25, Master 22). They are **not** validated human-solving difficulty ratings. Some puzzles may be easier or harder than their label suggests. A future iteration could grade puzzles with human-style techniques.

## Public deployment

1. Push this repository to GitHub.
2. On [Render](https://render.com), choose **New > Blueprint**, connect your repository, and apply `render.yaml`.
3. Render will provide a `*.onrender.com` URL. The free service may sleep when idle; check current Render pricing and limits.
4. When you buy a domain, add it under **Render > Service > Settings > Custom Domains**, then configure DNS at your registrar according to Render's instructions. Your code and API paths do not need to change.

There are no secrets or database credentials. The frontend uses same-origin relative API paths. No account is required and progress is stored only in the current browser.

## Limitations and roadmap

- Generation uses backtracking and can take longer for sparse puzzles.
- No accounts or cloud synchronization.
- No image upload, PDF export, or hint engine in this first release.
- Client-side checks identify rule conflicts, not whether a move matches the hidden solution.
- For large-scale public traffic, add API rate limiting and generation caching.

## License

MIT — see `LICENSE`.
