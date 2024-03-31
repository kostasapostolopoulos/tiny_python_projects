#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-03-31
Purpose: Chapter 6 of Tiny Python Projects
"""

import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        type=argparse.FileType("rt"),
        metavar="FILE",
        nargs="*",
        default=[sys.stdin],
        help="Input file(s)",
    )

    return parser.parse_args()


def main():
    """The main program"""

    args = get_args()

    total_lines_number, total_words_number, total_bytes_number = 0, 0, 0

    for fh in args.file:
        lines_number, words_number, bytes_number = 0, 0, 0
        for line in fh:
            if not line:
                break
            lines_number += 1
            words_number += len(line.split())
            bytes_number += len(line)

        total_lines_number += lines_number
        total_words_number += words_number
        total_bytes_number += bytes_number

        print(f"{lines_number:8}{words_number:8}{bytes_number:8} {fh.name}")

    if len(args.file) > 1:
        print(f"{total_lines_number:8}"
              f"{total_words_number:8}{total_bytes_number:8} total")


if __name__ == "__main__":
    main()
