#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-13
Purpose: Chapter 12 of Tiny Python Projects
"""

import argparse
import os
import random


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    """The main program"""

    args = get_args()
    random.seed(args.seed)

    # A for loop example
    #
    #
    #    intermediate_list = list(args.text)
    #    for index, letter in enumerate(intermediate_list):
    #        intermediate_list[index] = choose(letter)
    #
    #    print(''.join(intermediate_list))

    print(''.join(map(choose, args.text)))

    #Alternative for loop
    #
    # result = []
    # for char in args.text:
    #     result.append(choose(char))
    # print(''.join(result))

    # List comprehension
    #
    #result = [choose(char) for char in args.text]
    #print(''.join(result))


def choose(char):
    """Randomly choose an upper or lowercase letter to return."""

    #    result = random.choice([False, True])
    #    return char.upper() if result else char.lower()
    return char.upper() if random.choice([False, True]) else char.lower()


def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


if __name__ == '__main__':
    main()
