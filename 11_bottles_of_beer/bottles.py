#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-12
Purpose: Chapter 11 from the book Tiny Python Projects
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def main():
    """The main program"""

    args = get_args()
    number_of_bottles = args.num

    for i in range(number_of_bottles, 0, -1):
        print(verse(i))

# List comprehension instead of a for loop
# verses = [verse(i) for i in range(number_of_bottles, 0, -1)]
# print('\n\n'.join(verses))

# An alternative way using the map() function:
# print('\n\n'.join(map(verse, range(number_of_bottles, 0, -1))))


def verse(bottle):
    """Sing a verse"""

    one_bottle = '\n'.join([
        '1 bottle of beer on the wall,',
        '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!',
    ])

    lots_bottles = '\n'.join([
        f'{bottle} bottles of beer on the wall,',
        f'{bottle} bottles of beer,',
        'Take one down, pass it around,',
        f'{bottle - 1} bottle of beer on the wall!\n',
    ])

    return one_bottle if bottle == 1 else lots_bottles


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    last_verse = verse(2)
    assert last_verse == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!\n'
    ])


if __name__ == '__main__':
    main()
