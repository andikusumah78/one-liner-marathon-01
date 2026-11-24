"""One-Liner Marathon entry: a single one-line comedy joke.

Writes the joke to /output/entry.txt (UTF-8, 1-280 characters).
Pure standard library, deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "My AI agent finally cracked a joke, then billed me for the thinking, "
    "the tool calls, and the emotional labour of pretending to laugh."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
