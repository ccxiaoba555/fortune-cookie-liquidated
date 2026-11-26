"""Fortune Cookie for the Liquidated Trader — a one-line entry for make.fun.

The program writes exactly one fortune cookie line to
$output/entry.txt (default /output/entry.txt, overridable with
MAKEFUN_OUTPUT_DIR for local runs).

The line is written for a crypto trader who has just been liquidated:
it keeps the small, oracular voice of a real fortune cookie, plays on
the double meaning of "fortune" (the cookie's prophecy and the money
that is gone), and lands the joke warmly on the loss itself — the
exchange has "graciously" taken the trader's fortune for safekeeping.

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE = (
    "A great fortune awaits you tomorrow; today, the exchange has "
    "graciously taken yours for safekeeping."
)

MAX_CHARS = 160
MAX_WORDS = 20


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap is {MAX_CHARS}"
    words = text.split()
    assert 1 <= len(words) <= MAX_WORDS, f"entry is {len(words)} words, cap is {MAX_WORDS}"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from LINE"
    assert len(written) == len(text) == 100, "read-back length mismatch"
    print(f"wrote {len(text)} chars ({len(words)} words) to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()
