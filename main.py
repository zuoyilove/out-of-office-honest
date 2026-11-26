#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one painfully honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to entry.txt inside the
output directory named by MAKEFUN_OUTPUT_DIR (default: ./output).

The reply is a fixed string: no clock, no randomness, no network, no
input files, so every run produces byte-identical output.
"""

import os

MESSAGE = (
    "I'm away until Monday, and honestly your email will join the 312 "
    "unread messages I've been avoiding since Tuesday \u2014 I'll reply "
    "once I'm back, rested, and brave enough to open my inbox."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
