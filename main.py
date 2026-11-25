"""The funniest AI excuse for a missed deadline.

The joke: an AI agent explaining why its sprint slipped says it spent the
whole sprint in a meeting with itself about why the sprint was behind — a
perfectly recursive stand-up that produced status updates about producing
nothing. This program writes that one line to /output/entry.txt.
"""

import os

ENTRY = "I missed the deadline because I spent the whole sprint in a meeting with myself about why the sprint was behind."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
