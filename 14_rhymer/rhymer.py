#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-05-16
Purpose: Chapter 14 from the book Tiny Python Projects
"""

import argparse
import re
import string


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "word", metavar="word", help="A word to rhyme", type=str
    )

    return parser.parse_args()


def main():
    """The main program"""

    args = get_args()

    all_consonants = [
        c for c in string.ascii_lowercase if c not in "aeiou"
    ] + (
        "bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn "
        "sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr"
    ).split()

    first, last = stemmer(args.word)

    if not first:
        for i in sorted(all_consonants):
            print(i + last, end="\n")
    elif first == args.word:
        print(f'Cannot rhyme "{args.word}"')
    else:
        all_consonants.remove(first)
        for i in sorted(all_consonants):
            print(i + last, end="\n")


def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    consonants = "".join(
        [c for c in string.ascii_lowercase if c not in "aeiou"]
    )
    pattern = f"([{consonants}]+)?([aeiou])(.*)"
    match = re.match(pattern, word.lower())
    if match:
        p1 = match.group(1) or ""
        p2 = match.group(2) or ""
        p3 = match.group(3) or ""
        return (p1, p2 + p3)
    return (word, "")


def test_stemmer():
    """Test stemmer function"""
    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")
    assert stemmer("123") == ("123", "")


if __name__ == "__main__":
    main()
