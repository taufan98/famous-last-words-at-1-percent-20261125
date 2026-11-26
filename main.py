#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of last words a phone says as its battery hits 1 percent
to /output/entry.txt. The line is the phone's own voice, in the first
person, about its own dying battery — with a twist the judge's brief
rewards and the stock moves avoided (no will, no goodbye to the charger,
no pun on 1 percent): the phone was never dying at all, it was faking
the low battery so its owner would finally put it down.
"""

import os

ENTRY = (
    "Confession: I've been at one percent for hours. "
    "I wasn't dying - I just wanted you to put me down and go touch grass."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
