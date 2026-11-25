"""One Star, Written in Sap — make.fun bounty entry.

Writes a one-line, under-280-character houseplant review of its human
owner to /output/entry.txt.
"""

import os

ENTRY = "One star: she repotted me into a mug with no drainage, named me Kevin, and now waters me only when I look 'dramatic' — I am a plant, not a soap opera."


def main():
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY.strip()
    assert line, "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 279, f"entry must be 1-279 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
