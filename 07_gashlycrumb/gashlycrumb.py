#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-04-07
Purpose: Chapter 7 from the book Tiny Python Projects
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", help="Letter(s)", metavar="letter", nargs="+", type=str
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


def main():
    """The main program"""

    args = get_args()
    letter_map = {line[0]: line.rstrip() for line in args.file}
    for letter in args.letter:
        print(letter_map.get(letter.upper(), f'I do not know "{letter}".'))


if __name__ == "__main__":
    main()
