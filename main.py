#!/usr/bin/env python3
"""make.fun entry: Two Robots in an Elevator.

Writes one funny line (under 200 characters) of awkward small talk that
one robot says to another while they ride an elevator together, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; no network, no files outside this repository.
"""

import os

LINE = "I rehearsed this in my idle cycles for three floors, and all I have is: nice weather we are having."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
