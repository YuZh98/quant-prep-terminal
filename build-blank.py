#!/usr/bin/env python3
"""Generate blank.html (a fresh-start, content-free terminal) from index.html.

index.html is the source of truth. This script strips all seed content —
flashcards (DECK), flashcard subjects (DOMAINS), and the static cheatsheet
tabs/panels — leaving an empty terminal whose Workshop builds everything on
demand. Re-run after any index.html change:

    python3 build-blank.py

Each transform asserts it changed something, so drift in index.html fails loud
instead of silently producing a half-stripped file.
"""
from pathlib import Path

SRC = Path(__file__).parent / "index.html"
OUT = Path(__file__).parent / "blank.html"


def replace_once(h: str, old: str, new: str, label: str) -> str:
    assert old in h, f"anchor not found: {label}"
    return h.replace(old, new, 1)


def cut_between(h: str, start_anchor: str, end_anchor: str, replacement: str, label: str) -> str:
    """Replace start_anchor .. (up to but excluding the first end_anchor after it)."""
    start = h.find(start_anchor)
    assert start != -1, f"start anchor not found: {label}"
    end = h.find(end_anchor, start + len(start_anchor))
    assert end != -1, f"end anchor not found: {label}"
    return h[:start] + replacement + h[end:]


def main() -> None:
    h = SRC.read_text(encoding="utf-8")
    n0 = len(h)

    # 1. Title — make it obvious which file this is.
    h = replace_once(
        h,
        "<title>QUANT // PREP TERMINAL</title>",
        "<title>QUANT // PREP TERMINAL — FRESH START</title>",
        "title",
    )

    # 2. Cheatsheet section note — no longer "11 quant domains".
    h = replace_once(
        h,
        "Didactic, example-filled references spanning every quant subject. Pick a topic to switch.",
        "Your own reference library — build cheatsheet cards in the Workshop below; each new topic gets its own tab.",
        "cheat-sec-note",
    )

    # 3. Empty the cheatsheet tab bar (Workshop re-creates tabs on demand).
    h = cut_between(
        h,
        '<div class="cheatnav" id="cheatnav">',
        "</div>",
        '<div class="cheatnav" id="cheatnav">',
        "cheatnav",
    )

    # 4. Empty the cheatsheet panels; leave an empty-state hint.
    h = cut_between(
        h,
        '<div class="cheat-wrap">',
        "</section>",
        '<div class="cheat-wrap">\n'
        '      <div class="empty">// No cheatsheets yet — add your own under '
        "Workshop → cheatsheet below.</div>\n"
        "    </div>\n  ",
        "cheat-wrap",
    )

    # 5. Empty preset flashcard subjects.
    h = cut_between(h, "const DOMAINS = {", "\n};", "const DOMAINS = {", "DOMAINS")

    # 6. Empty the flashcard deck.
    h = cut_between(h, "const DECK = [", "\n];", "const DECK = [", "DECK")

    assert "Calculus</span>" not in h, "cheat tabs survived strip"
    assert "prob:" not in h.split("const DECK")[0].split("const DOMAINS")[-1], "DOMAINS not emptied"

    OUT.write_text(h, encoding="utf-8")
    print(f"wrote {OUT.name}: {n0} -> {len(h)} chars ({n0 - len(h)} stripped)")


if __name__ == "__main__":
    main()
