#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 27/2/2024
Purpose: Chapter 1 from the book Tiny Python Projects
"""

import argparse


def get_args():
    """Get the command line arguments"""

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        default="World",
        help="Name to greet",
    )
    return parser.parse_args()


def main():
    """The program"""

    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
