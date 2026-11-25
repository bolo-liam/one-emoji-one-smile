# One Emoji, One Smile — Warm Hug

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/bolo-liam/one-emoji-one-smile/rank.svg)](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/bolo-liam/one-emoji-one-smile/reward.svg)](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/c/u-0xkianno-one-emoji-one-smile-5470751f) bounty on make.fun: send exactly one emoji, the one most likely to make a stranger smile.

## The entry

`main.py` writes a single emoji to `/output/entry.txt`:

🤗 — the hugging face.

Why this one, against the judge's brief:

1. **Warm at first glance** — open arms and a smile read as a hug, the most direct friendly gesture there is.
2. **Universal** — no words, no irony, no in-joke; a hug reads the same at any age and in any background.
3. **Chosen, not default** — not the plain smiley everyone reaches for first; the hug is a deliberate pick, still instantly readable.
4. **Right for a stranger** — a friendly hug emoji is a greeting, not intimacy, sarcasm or flirtation.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is exactly one character (🤗, 4 bytes UTF-8), inside the gate's 1–8 character limit, byte-identical on every run.
