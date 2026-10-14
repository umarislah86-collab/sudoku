# Ego Check — Extreme Sudoku

An English Sudoku game with 10 distinct puzzles, unique solutions, pencil notes, undo, on-demand checking, a teasing fake Hint button, pause, timer, and browser-local progress. It works on phone and desktop without frontend dependencies, accounts, APIs, or external fonts.

## Run locally

```sh
cd /workspace/sudoku
python3 -m http.server 3000 --bind 0.0.0.0
```

No build is required. `puzzles.js` is ready-to-use puzzle data and does not need to be regenerated during startup.

## Puzzles

`generate.mjs` creates complete grids, removes clues only while preserving a unique solution, then filters out puzzles that can be finished with naked or hidden singles. The solver threshold is 5,000 search nodes and at least 45 unsolved cells after singles. Search nodes are a computational filter, not a standard human difficulty rating.

Run `python3 validate.py` to independently verify all 10 puzzles. Regeneration is optional: `node generate.mjs`.

Progress is stored only in the current browser. The timer stops when the tab is hidden, the game is paused, or a dialog is open. The Hint button shows a rotating tease and never reveals an answer. Each puzzle also shows four timed taunts (5, 15, 30, and 45 minutes) and four completion taunts (25%, 50%, 75%, and 90%). Each one appears once per puzzle.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` publishes the static frontend on pushes to `main`. GitHub Pages must use **Settings → Pages → Source → GitHub Actions**. Browser tests are not run automatically; the owner checks the UI manually.
