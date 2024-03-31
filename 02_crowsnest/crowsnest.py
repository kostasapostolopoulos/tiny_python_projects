#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 3/3/2024
Purpose: Chapter 2 from the book Tiny Python Projects
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "word", metavar="word", type=str, help="A word"
    )

    # parser.add_argument('--side',
    #                     metavar='side',
    #                     type=str,
    #                     default='lardboard',
    #                     help='The side'
    #                     )

    parser.add_argument(
        "-s",
        "--starboard",
        help="Starboard flag",
        action="store_true",
    )

    return parser.parse_args()


def main():
    """Main function"""

    args = get_args()
    word = args.word
    flag = args.starboard
    article = "an" if word[0].lower() in "aeiou" else "a"
    side = "starboard" if flag else "lardboard"
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


if __name__ == "__main__":
    main()
