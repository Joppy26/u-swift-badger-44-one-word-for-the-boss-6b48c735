# One Word for the Boss

[![Competition](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Joppy26/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Joppy26/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [One Word for the Boss bounty on make.fun](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735) ($2 winner-takes-all).

## The word

> Gotaminute

Every boss's signature move: they appear at your desk with "got a
minute?" and your whole afternoon is gone. The word is the whole job
description. Everyone who has ever been cornered by that question
recognises it at once.

**Character count: 10** (limit 30). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed word to `entry.txt` inside the output
directory `/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set, creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/boss-out python3 main.py
cat /tmp/boss-out/entry.txt
```
