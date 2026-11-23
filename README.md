[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Elies87/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Elies87/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

# The Joke About the Demo

A tiny entry for the make.fun competition "The joke about the demo".
The whole program is a single Python script, `main.py`, that writes one
joke — a single line about what it is like to work beside AI coding
agents — to a text file. That is all it does, and it does it the same
way every time: no network, no randomness, no clock, just the standard
library.

The joke:

> Working beside an AI coding agent taught me a brand-new skill: nodding confidently at 4,000 lines of code it wrote in the time it took me to name one variable.

## How to run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt`. To write it somewhere
else, point the `MAKEFUN_OUTPUT_DIR` environment variable at the
directory you want:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# the joke lands in /tmp/out/entry.txt
```

The output is UTF-8 text, 159 characters, and byte-identical on every
run.

## License

MIT — see the `LICENSE` file in this repository.
