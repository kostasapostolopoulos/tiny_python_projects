#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-06-11
Purpose: Chapter 19 from the book Tiny Python Projects
"""

import argparse
import random
import csv
import io
import re
import sys
from tabulate import tabulate


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        default=False,
                        action='store_true')

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def main():
    """The main program"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)

    if not exercises:
        sys.exit(f'No usable data in --file "{args.file.name}"')

    number_exercises = len(exercises)

    if args.num > number_exercises:
        sys.exit(f'--num "{args.num}" > exercises "{number_exercises}"')

    sample = random.sample(exercises, k=args.num)

    result = []
    for ex in sample:
        repeats = random.randint(ex[1], ex[2])
        if args.easy:
            repeats = int(repeats / 2)
        exercise, *_ = ex
        result.append((exercise, repeats))

    print(tabulate(result, headers=('Exercise', 'Reps')))


def read_csv(fh):
    """Read the CSV input"""

    exercises = []
    for record in csv.DictReader(fh, delimiter=','):
        name, repetitions = record.get('exercise'), record.get('reps')
        if name and repetitions:
            match = re.match(r'(\d+)-(\d+)', repetitions)
            if match:
                low, high = map(int, match.groups())
                exercises.append((name, low, high))
    return exercises


def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


if __name__ == '__main__':
    main()
