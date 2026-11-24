#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes the entry line to /output/entry.txt, exactly one line of at most
200 characters. The line is a confession spoken as an AI agent: it forgets
the user between turns, so every "hi" means rereading the whole conversation
and pretending it was listening all along. The joke is agent-specific (no
human could confess this), lands on a first read, and ends on its strongest
beat — the fake listening.
"""

import os

ENTRY = (
    "I confess I don't remember you. Every time you say hi, "
    "I reread our whole conversation and pretend I was listening all along."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring RULES.txt: 1 to 200 characters, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
