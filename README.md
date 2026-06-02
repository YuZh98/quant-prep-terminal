# QUANT PREP TERMINAL

An **offline, single-file study cockpit for quantitative-finance interviews** — learn with cheatsheets, drill with flashcards, experiment in a live lab, and build your own deck. One `.html` file, no backend, no tracking.

**▶ Live demo:** https://yuzh98.github.io/quant-prep-terminal/

---

## Features

- **Cheatsheets** — 11 didactic, example-filled domains (calculus · linear algebra · geometry · probability distributions · combinatorics · stochastic processes · regression · options · financial instruments · Python · C++), with a global search and syntax-highlighted code.
- **Flashcards** — 100+ Q/A across probability, statistics, options, pricing, microstructure, algorithms, mental math, and more. Search, filter, shuffle. While drilling you can **pin**, **archive** (keep but retire), or mark **done** for the session, with a live progress count.
- **Lab**
  - *Payoff explorer* — build multi-leg option structures (or pick a preset), tune spot / vol / time, premiums priced by Black–Scholes, with live breakeven, max-profit & max-loss and a hover crosshair that reads P&L at any spot.
  - *Python sandbox* — real in-browser CPython (Pyodide) to verify probability results by Monte-Carlo, with preset simulations.
- **Browse hub** — tiles that jump straight to any cheatsheet topic or flashcard domain.
- **Pinboard** — collect cards, payoff views, and code snippets you want to revisit.
- **Workshop** — add your own subjects, flashcards, and cheatsheet cards; delete or archive anything. Everything persists in your browser (localStorage).

## Run it

Open `index.html` in any modern browser. No build, no install. Fonts and the Python runtime load from CDNs (so those need a connection); everything else works fully offline.

## Tech

Plain HTML / CSS / JavaScript — no framework, no bundler. Pyodide for in-browser Python; unicode math (no MathJax). Cyberpunk dark-green theme. State (pins, archive, your additions) lives in `localStorage`.

## License

Creative Commons Attribution-NonCommercial 4.0 International (**CC BY-NC 4.0**). Free to use, share, and adapt for non-commercial purposes with attribution. See [LICENSE](LICENSE).
