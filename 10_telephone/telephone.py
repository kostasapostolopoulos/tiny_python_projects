#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-10
Purpose: Chapter 10 of Tiny Python Projects
"""

import argparse
import os
import random
import string


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


def main():
    """The main program"""

    args = get_args()
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    sample_list = list(range(len(args.text)))
    mutations_number = round(len(args.text) * args.mutations)
    letters_to_replace = random.sample(sample_list, k=mutations_number)
    new_var = args.text
    for letter in letters_to_replace:
        # This ensures that the new character can't be the same as the one that we are replacing
        new_char = random.choice(alpha.replace(new_var[letter], ''))
        new_var = new_var[:letter] + new_char + new_var[letter + 1:]

    print(f'You said: "{args.text}"\nI heard : "{new_var}"')

# Below is another an example using a list instead of string slicing

# new_var = list(args.text)
# for letter in letters_to_replace:
#     new_char = random.choice(alpha.replace(new_var[letter], ''))
#      
# print(f'You said: "{args.text}"\nI heard : "{''.join(new_var)})    

if __name__ == '__main__':
    main()
