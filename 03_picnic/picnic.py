#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-03-10
Purpose: Chapter 3 of Tiny Python Projects
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str",
                        metavar="str",
                        nargs="+",
                        help="Item(s) to bring")

    parser.add_argument("-s",
                        "--sorted",
                        help="Sort the items",
                        default=False,
                        action="store_true")

    return parser.parse_args()


def main():
    """The main function"""

    args = get_args()
    food = args.str

    if args.sorted:
        food.sort()

    if len(food) == 1:
        print(f"You are bringing {food[0]}.")
    elif len(food) == 2:
        print(f"You are bringing {food[0]} and {food[1]}.")

    else:
        print(f'You are bringing {", ".join(food[:-1])}, and {food[-1]}.')


if __name__ == "__main__":
    main()
