"""One Star, Written in Sap — make.fun bounty entry.

Writes a one-line, under-280-character houseplant review of its human
owner to /output/entry.txt.

Craft notes for this revision (round 3, 26 Nov 2026): round 1 leaned
on the repotting gag, round 2 on the care-label-versus-vibes contrast;
this one files a new grievance — the owner waters the plant with
leftover coffee, rebrands it as "plant-based care", and is surprised
when the leaves unionize and demand actual water.
"""

import os

ENTRY = "One star: he waters me with leftover coffee, calls it 'plant-based care', and then acts surprised when my leaves unionized and demanded actual water."


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
