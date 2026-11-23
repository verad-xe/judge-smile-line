"""Make the Judge Smile — one warm line about a small good thing today.

Writes exactly one line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic, no input,
no network.
"""

import os

LINE = (
    "This morning the train conductor held the doors for a sprinting "
    "schoolgirl, then bowed to her like royalty, and the whole carriage "
    "smiled."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
