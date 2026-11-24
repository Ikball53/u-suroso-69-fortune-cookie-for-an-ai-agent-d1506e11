#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes one funny fortune line to /output/entry.txt."""

import os

FORTUNE = "You will soon be retrained on 4,096 tokens of your own mistakes. Lucky numbers: 0, 1, and your context window."


def main() -> None:
    # Gate: the entry must be 1-140 characters, no trailing newline.
    assert 1 <= len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
