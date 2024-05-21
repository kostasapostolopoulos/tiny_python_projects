#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-19
Purpose: Chapter 15 from the book Tiny Python Projects
"""

import argparse
import re
import os

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text of file')
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def main():
    """The main program"""

    args = get_args()

    splitter = re.compile(r'(\W+)')

    #for line in args.text.splitlines():
    #    words = []
    #    for word in splitter.split(line.rstrip()):
    #        words.append(fry(word))
    #    print(''.join(words))

    #for line in args.text.splitlines():
    #    print(''.join([fry(w) for w in splitter.split(line.rstrip())]))

    for line in args.text.splitlines():
        print(''.join(map(fry, splitter.split(line.rstrip()))))


def fry(word):
    """Drop the `g` from `-ing` words, change `you` to `y'all`"""

    match1 = re.search(r'([yY])ou\b', word)
    match2 = re.search(r'(.+)ing$', word)
    if match1:
        return match1.group(1) + "'all"
    elif match2:
        if not re.search(r'[aeiouy]', match2.group(1), re.I):
            return word
        return match2.group(1) + "in'"
    else:
        return word

def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"

if __name__ == '__main__':
    main()
