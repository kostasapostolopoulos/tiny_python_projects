#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-06-09
Purpose: Chapter 18 from the book Tiny Python Projects
"""

import argparse
import os
import re

# from functools import reduce
# import operator


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gematria",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text",
                        metavar="text",
                        type=str,
                        help="Input text of file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    """Main program"""

    args = get_args()

    for line in args.text.splitlines():
        print(" ".join(map(word2num, line.split())))


def word2num(char):
    """Returns the sum of a single word as string"""

    char = re.sub("[^A-Za-z0-9]", "", char)
    return str(sum(map(ord, char)))

    # return str(reduce(operator.add, map(ord, char)))


def test_word2num():
    """Test word2num"""

    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


if __name__ == "__main__":
    main()
