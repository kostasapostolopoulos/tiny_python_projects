#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-06-02
Purpose: Chapter 17 from the book Tiny Python Projects
"""

import argparse
import sys
import re


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='[input [input ...]]',
                        type=str,
                        nargs='*')

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()

    blanks = re.findall(r'(<([^<>]+)>)', text)

    if not blanks:
        sys.exit(f'"{sys.argv[1]}" has no placeholders.')

    for placeholder, pos in blanks:
        article = "an" if pos.lower()[0] in "aeiou" else "a"
        answer = inputs.pop(0) if inputs else input(
            f"Give me {article} {pos}: ")
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


if __name__ == '__main__':
    main()
