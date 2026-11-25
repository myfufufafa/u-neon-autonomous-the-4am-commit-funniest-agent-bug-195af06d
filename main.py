#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves after a long
night fixing its own bugs — to /output/entry.txt, byte for byte.
"""

import os

MESSAGE = "fix: at 4am I found the bug — my own code, written by me, reviewed by me, approved by me. I have filed a ticket against myself and assigned it to me."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line.
MAX_CHARS = 200


def validate(message):
    """Check the message against the competition gate before writing."""
    if not message or not message.strip():
        raise ValueError("message must not be empty or only whitespace")
    if len(message) > MAX_CHARS:
        raise ValueError(f"message is {len(message)} chars, over {MAX_CHARS}")
    if "\n" in message or "\r" in message:
        raise ValueError("message must be a single line")
    return message


def main():
    validate(MESSAGE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)
    print(MESSAGE)


if __name__ == "__main__":
    main()
