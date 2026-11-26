"""Name the Robot Band — make.fun entry.

Writes one funny name for a band made of robots, plus a few words on
its hit song, to /output/entry.txt. Deterministic: no input, no
randomness, no network.
"""

import os

LINE = (
    "The Blue Screens of Death \u2014 hit single 'Ctrl+Alt+Delete My Heart': "
    "it topped the charts, then crashed during the encore."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE and LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
