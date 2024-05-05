#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-05
Purpose: Chapter 8 from the book Tiny Python Projects
"""

import argparse
import sys
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and Bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text",
                        metavar="text",
                        help="Input text of file",
                        type=str)

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitue",
        metavar="vowel",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    """The main program"""

    table = {"a": "a", "e": "a", "i": "a", "o": "a", "u": "a"}

    args = get_args()

    fh = args.text

    if args.vowel:
        table.update((k, args.vowel) for k in table)

    if fh.isupper():
        fh = fh.lower()
        output = fh.translate(str.maketrans(table))
        sys.stdout.write(f"{output.upper()}\n")
    else:
        output = fh.translate(str.maketrans(table))
        sys.stdout.write(f"{output}\n")


if __name__ == "__main__":
    main()
