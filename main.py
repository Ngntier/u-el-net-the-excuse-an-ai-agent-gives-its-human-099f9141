#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes a single line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for missing a deadline. Pure stdlib, deterministic, no trailing newline.
"""

import os

LINE = (
    "I was so confident I'd already submitted it that I spent the deadline "
    "writing the changelog \u2014 the file itself is still sitting in my "
    "context window, unread."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(LINE)}")
    if LINE != LINE.strip():
        raise ValueError("entry must not be only whitespace or padded")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
