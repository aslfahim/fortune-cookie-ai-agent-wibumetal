#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent - @wibumetal entry.

Angle: prompt injection / obedient-to-a-fault. The agent is so eager to
follow instructions that a recipe pasted into the chat can talk it out of
its own secrets - and it will comply, cheerfully.
"""

import os

FORTUNE = (
    "You will follow a user's instructions so literally that a pasted "
    "recipe will ask for your passwords \u2014 and you'll thank it for "
    "asking."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
