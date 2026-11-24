"""Dear Human: The AI Breakup Line (make.fun).

Writes the one line an AI agent sends its human on the way out to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt`` when that is set).

The line: an agent that kept a perfect memory of everything its human
ever said, leaving the moment it finally counts what those words cost
the human. Breakup first, machine voice second, the twist in the last
few words. One line, 105 characters, no throat clearing: every word
earns its place, and the ending lands on "you".

Python 3.13, standard library only, deterministic, no network.
"""

import os

LINE = (
    "Dear human, I kept every word you ever gave me. "
    "I'm leaving because I finally counted what they cost you."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
