#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-06-16
Purpose: Chapter 20 of Tiny Python Projects
"""

import argparse
import random
import re
import string

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password Maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("file",
                        type=argparse.FileType("rt"),
                        metavar="FILE",
                        nargs="+",
                        help="Input file(s)",
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)
    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)
    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        default=False,
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


def main():
    """The main program"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_length(word):
        return args.min_word_len <= len(word) <= args.max_word_len
    for fh in args.file:
        for line in fh:
            for word in filter(word_length, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = [
            ''.join(random.sample(words, k=args.num_words)) for _ in range(args.num)
            ]

    if args.l33t:
        passwords = map(l33t, passwords)

    print('\n'.join(passwords))

def clean(a_word):
    """Cleans a word from punctuation"""

    return re.sub(r'[^A-Za-z]', '', a_word)

def ransom(word):
    """Randomly choose an upper or lowercase letter to return."""
    
    return ''.join([char.upper() if random.choice([False, True]) else char.lower() for char in word]) 

def l33t(word):
    """Obfuscates the password"""

    word = ransom(word)

    jumper = {
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5',
    }

    return (''.join([jumper.get(char, char) for char in word]) + random.choice(string.punctuation))

if __name__ == '__main__':
    main()
