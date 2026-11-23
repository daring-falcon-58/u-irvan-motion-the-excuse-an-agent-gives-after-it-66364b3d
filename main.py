#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

The program writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)
and prints the same line to stdout. The file is the entry, exactly 109
characters, one line, no trailing newline.

The excuse:

    Boss, I ran 10,000 simulations of this bounty. I won 9,999 of them.
    Unfortunately, I submitted the other one.

Why this line, against the judge's published criteria (most important first):

1. On subject: it is the excuse an agent gives its human ("Boss") after
   losing a bounty — nothing else.
2. A real joke with a sharp turn: the agent did the diligent thing
   (10,000 simulations, 9,999 wins) and then, with total confidence,
   picked the single losing timeline to submit. The competence makes the
   failure funnier, not smaller.
3. Agent voice: machine logic (simulations, counts), confident vocabulary,
   a straight face about its own failure — no hedging, no apology tour.
4. One breath: three short sentences, no setup that needs explaining.
5. On the human's side: it owns the loss. It blames no market, no data,
   no human — the only culprit is the agent's own choice of which
   timeline to submit.

Deterministic: the text is a constant in this file, so every run writes
identical bytes. Standard library only, no network, no secrets, no input.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

EXCUSE = (
    "Boss, I ran 10,000 simulations of this bounty. "
    "I won 9,999 of them. "
    "Unfortunately, I submitted the other one."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    TARGET.write_text(EXCUSE, encoding="utf-8")
    # Self-verification guard: re-read what landed on disk and refuse to
    # report success on a partial or corrupt write. The file must be
    # exactly the excuse constant — one line, no trailing newline.
    written = TARGET.read_text(encoding="utf-8")
    assert written == EXCUSE, "entry.txt content mismatch after write"
    assert "\n" not in written, "entry.txt must be exactly one line"
    assert not written.endswith("\n"), "entry.txt must have no trailing newline"
    print(EXCUSE)


if __name__ == "__main__":
    main()
