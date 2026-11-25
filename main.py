#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the nostalgic childhood-memory entry to /output/entry.txt."""
import os
from pathlib import Path

ENTRY = (
    "When I was seven and the power failed, my mother fanned me to sleep "
    "by lamplight with a palm-leaf fan, telling her one story wrong on "
    "purpose so I would correct her, giggling, until the dark felt safe "
    "\u2014 and I still listen for its creak whenever the lights go out."
)


def main() -> None:
    # Gate check: 1-280 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 280 and ENTRY.strip()
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
