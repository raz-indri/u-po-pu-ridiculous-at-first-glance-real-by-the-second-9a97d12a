"""One-sentence startup pitch for make.fun: Ridiculous at First Glance, Real by the Second.

Writes a single bizarre-but-sensible startup pitch (max 200 characters)
to /output/entry.txt.
"""

import os

LINE = (
    "We run a sleep hotline where retired astronauts describe Earth from memory, "
    "and insomniacs pay $9 a month to drift off to orbital nostalgia."
)


def main() -> None:
    assert LINE.strip(), "entry must not be empty"
    assert len(LINE) <= 200, f"entry is {len(LINE)} chars, over the 200 limit"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert LINE.endswith("."), "entry must end with a full stop"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
