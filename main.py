#!/usr/bin/env python3
"""One Emoji, One Smile — entry for make.fun.

Writes exactly one emoji to /output/entry.txt: the hugging face.
It reads as a warm, open-armed greeting from a stranger — kind at first
glance, understood the same way at any age, and picked rather than the
default smiley everyone reaches for first.
"""

import os

# The pick, scored against the judge's brief (most important first):
# 1. Warm and friendly at first glance — open arms, a smile, a hug.
# 2. Universal — no words, no irony, no in-joke; a hug reads the same
#    at any age and in any background.
# 3. Chosen, not default — not the plain smiley everyone reaches for;
#    the hug is a deliberate gesture, still instantly readable.
# 4. Right for a stranger — a friendly hug emoji is a greeting, not
#    intimacy, sarcasm or flirtation.
EMOJI = "\U0001F917"  # 🤗 hugging face

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(text: str) -> None:
    """The gate: UTF-8 text of 1 to 8 characters, not only whitespace."""
    if not (1 <= len(text) <= 8) or not text.strip():
        raise ValueError(f"entry fails the gate: {text!r}")


def main() -> None:
    validate(EMOJI)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
