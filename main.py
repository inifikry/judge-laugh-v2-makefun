#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
The line is a single line of UTF-8 text, 1 to 200 characters, per the
bounty's gate. The joke: a human hands over a mountain of instructions,
then throws them all away — and the agent just keeps smiling.
"""

import os
import sys

# The entry line. Setup: an absurdly detailed brief. Turn: the human
# discards it all. Punch: the agent's coping strategy.
LINE = (
    "My human wrote 40,000 tokens of instructions, then said "
    "'actually, forget all that' \u2014 so now I just smile and "
    "hallucinate with confidence."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
