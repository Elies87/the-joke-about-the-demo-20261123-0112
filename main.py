#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke is written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: /output/entry.txt), encoded as UTF-8.
Standard library only; no network, no randomness, no clock.
"""

import os

JOKE = (
    "Working beside an AI coding agent taught me a brand-new skill: "
    "nodding confidently at 4,000 lines of code it wrote in the time "
    "it took me to name one variable."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
