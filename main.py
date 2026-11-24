#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — make.fun entry.

Writes exactly one line — an absurd micro-startup pitch: the startup's
name plus what it does, pitched with total confidence — to
/output/entry.txt. Python 3.13 standard library only (os).
"""

import os

PITCH = (
    "SniffBox: a $12-a-month subscription that mails you one mystery "
    "sock every week, because your nose deserves a startup with a "
    "waitlist, a cap table, and a vision."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
