#!/usr/bin/env python3
"""Entry for make.fun's "One Line, One Minute: The Vending Machine
Pickup Line Contest".

Writes a pickup line a vending machine would use on a passing human to
/output/entry.txt (UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "You've walked past me all week, so here it is: press my buttons "
    "right, and I promise everything between us stays in stock."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
