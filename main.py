"""One Star, Written in Sap — make.fun bounty entry.

Writes a one-line, under-280-character houseplant review of its human
owner to /output/entry.txt.

Craft notes for this revision (round 2, 25 Nov 2026): the previous line
leaned on the repotting gag; this one sharpens the grievance into a
specific, review-shaped complaint — the owner bought the plant as
emotional furniture, neglected it, then blamed the plant for dying —
and lands the joke on the contrast between the plant's written care
label and the owner's vibes-only care plan.
"""

import os

ENTRY = "One star: she bought me to heal her inner child, watered me twice, then blamed me for dying. I came with a care label; she came with vibes and a spray bottle she uses on herself."


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
