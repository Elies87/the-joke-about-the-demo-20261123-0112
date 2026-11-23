#!/usr/bin/env python3
"""Entry for the make.fun bounty "The joke about the demo"
(the-joke-about-the-demo-20261123-0112).

Writes one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a one-line joke about working beside AI coding agents.

Standard library only, no network, no randomness, no clock: two runs write
byte-identical output.
"""

import os

TEXT = (
    "The demo was flawless \u2014 my AI agent tested it on users it invented, "
    "in a market it hallucinated, for a deadline that doesn't exist. "
    "The imaginary users still filed bug reports."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
