#!/usr/bin/env python3
"""One Word for the Boss: entry generator.

Writes exactly one word describing a boss to entry.txt inside the
output directory (/output by default, or MAKEFUN_OUTPUT_DIR when set).
Python 3 standard library only. No network, no clock, no randomness:
every run produces the exact same file.
"""

import os

WORD = "Gotaminute"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
