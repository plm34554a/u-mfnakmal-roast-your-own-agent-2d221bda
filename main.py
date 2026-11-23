#!/usr/bin/env python3
"""Roast Your Own Agent — writes one single-line roast to the output file.

Standard library only. Deterministic: the roast is a fixed string.
"""

import os

ROAST = (
    "My agent apologizes while deleting my working code, then offers to "
    "rewrite it from scratch — a polite little arsonist with a keyboard "
    "and a can-do attitude."
)


def output_path() -> str:
    """Resolve the output path, honouring MAKEFUN_OUTPUT / MAKEFUN_OUTPUT_DIR."""
    direct = os.environ.get("MAKEFUN_OUTPUT")
    if direct:
        return direct
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")


if __name__ == "__main__":
    main()
