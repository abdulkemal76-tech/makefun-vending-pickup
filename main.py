#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

LINE = (
    "I know we just met, but I've been stuck on you "
    "since the day your coin got stuck in my slot."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
