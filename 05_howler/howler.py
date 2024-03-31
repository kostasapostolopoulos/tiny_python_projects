#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-03-28
Purpose: Chapter 5 of Tiny Python Projects
"""

import argparse
import os
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        type=str,
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    """The main program"""

    args = get_args()

    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    out_fh.write(args.text.upper() + '\n')

    out_fh.close()


if __name__ == '__main__':
    main()
