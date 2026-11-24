"""Famous Last Words at 1 Percent — make.fun bounty
u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.

Writes one line (at most 199 characters) to /output/entry.txt: the funniest
possible last words a phone would say as its battery hits 1 percent.

The line is written in the phone's own voice, about its own dying battery,
with the punch landing at the end: it survived every physical ordeal a phone
can face, only to be finished by something utterly ordinary — and its final
thought is for the cloud, the one thing it loved.
"""

import os

ENTRY = (
    "I survived three drops, one toilet, and a toddler, but a 4K video "
    "of a cat was my final boss. Tell the cloud I loved her."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 199:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-199")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # No trailing newline: the gate counts the file's characters (1-199),
        # so the file itself must stay inside the limit, not just the line.
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
