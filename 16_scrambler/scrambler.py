#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-26
Purpose: Chapter 16 form the book Tiny Python Porjects
"""

import argparse
import random
import re
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text of file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
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

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    #for line in args.text.splitlines():
    #    result = []
    #    for word in splitter.split(line):
    #        if splitter.match(word):
    #            result.append(scramble(word))
    #        else:
    #            result.append(word)
    #    print(''.join(result))

    for line in args.text.splitlines():
        result = [
            scramble(word) if splitter.match(word) else word
            for word in splitter.split(line)
        ]
        print(''.join(result))


def scramble(word):
    """Scramble a word"""

    first = word[0]
    last = word[-1]
    middle = list(word[1:-1])
    random.shuffle(middle)
    middle = ''.join(middle)

    if len(word) < 4:
        return word
    return first + middle + last


def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


if __name__ == '__main__':
    main()
