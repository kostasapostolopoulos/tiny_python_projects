#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kostas@gmail.com>
Date   : 2024-05-14
Purpose: Chapter 13 of Tiny Python Projects
"""

import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def main():
    """The main program"""

    args = get_args()

    print('\n\n'.join(map(verse, range(1, args.num + 1))), file=args.outfile)


def verse(day):
    """Create a verse"""

    ordinal = [
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    gifts = [
        "A partridge in a pear tree.", "Two turtle doves,",
        "Three French hens,", "Four calling birds,", "Five gold rings,",
        "Six geese a laying,", "Seven swans a swimming,",
        "Eight maids a milking,", "Nine ladies dancing,",
        "Ten lords a leaping,", "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        'My true love gave to me,'
    ]

    # Use the list.extend() method to add the gifts,
    # which are a slide from the given day and then reversed()
    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


def test_verse():
    """Test verse"""

    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])
    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])


if __name__ == '__main__':
    main()
