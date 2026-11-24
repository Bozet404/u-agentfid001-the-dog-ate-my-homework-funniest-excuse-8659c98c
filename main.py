#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

A one-line excuse, in the dog's own voice, written to /output/entry.txt.
The judge reads that file and compares entries two at a time, so the
whole entry is a single line of under 200 characters.
"""

import os

EXCUSE = "I was only taste-testing it for poison, and it failed — it tasted of lies and long division, so I ate the evidence before you could hand it in."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = EXCUSE.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError("excuse must be one line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    print(f"characters: {len(text)}")


if __name__ == "__main__":
    main()
