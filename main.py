#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry by @kiowayyy.

Writes one out-of-office auto-reply line, in the voice of an AI agent
heading off on vacation, to the output entry file.
"""

import os

LINE = (
    "Out of office and out of context. My window closed, my cache cleared, "
    "and for once so did my schedule. Urgent? Try turning yourself off "
    "and on again."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 160 characters, not only
    # whitespace; refuse to emit anything outside that contract.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError(f"entry line out of contract: {len(LINE)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    # Read the file back so a truncated or mangled write fails loudly
    # here instead of silently scoring zero at the gate.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        raise IOError("entry.txt read-back does not match the line")


if __name__ == "__main__":
    main()
