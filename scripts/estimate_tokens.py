#!/usr/bin/env python3
"""Heuristic token estimate for comparing text before/after compression.

Approximation: each CJK character counts as 1 token; remaining non-whitespace
characters count as 1 token per 4 characters. This is not exact tokenizer
output; use it for relative savings, not billing.

Usage:
  estimate_tokens.py FILE
  estimate_tokens.py --text "some text"
  estimate_tokens.py --compare BEFORE AFTER
  cat file | estimate_tokens.py
"""

import argparse
import math
import re
import sys

CJK = re.compile(
    "["
    "\u3400-\u4dbf"
    "\u4e00-\u9fff"
    "\uf900-\ufaff"
    "\u3040-\u30ff"
    "\uac00-\ud7af"
    "]"
)


def estimate(text: str) -> int:
    cjk = len(CJK.findall(text))
    non_cjk = sum(1 for ch in CJK.sub("", text) if not ch.isspace())
    return cjk + math.ceil(non_cjk / 4)


def read_path(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="file to estimate, '-' for stdin")
    parser.add_argument("--text", help="estimate a literal string")
    parser.add_argument(
        "--compare",
        nargs=2,
        metavar=("BEFORE", "AFTER"),
        help="compare two files and report token savings",
    )
    args = parser.parse_args()

    if args.compare:
        before, after = (read_path(p) for p in args.compare)
        before_tokens, after_tokens = estimate(before), estimate(after)
        saved = before_tokens - after_tokens
        percent = (saved / before_tokens * 100) if before_tokens else 0.0
        print(f"before: {before_tokens} tokens")
        print(f"after:  {after_tokens} tokens")
        print(f"saved:  {saved} tokens ({percent:.1f}%)")
        return

    if args.text is not None:
        text = args.text
    elif args.path:
        text = read_path(args.path)
    else:
        text = sys.stdin.read()

    tokens = estimate(text)
    chars = len(text)
    print(f"{tokens} tokens (~{chars} chars)")


if __name__ == "__main__":
    main()
