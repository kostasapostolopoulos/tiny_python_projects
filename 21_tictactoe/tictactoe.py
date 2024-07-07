#!/usr/bin/env python3
"""
Author : Kostas Apostolopoulos <kapoath@gmail.com>
Date   : 2024-06-30
Purpose: Chapter 21 of Tiny Python Projects
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='State of the board',
                        metavar='str',
                        type=str,
                        default="." * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='str',
                        type=str,
                        choices=list("XO"),
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='int',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()

    if args.board:
        for char in args.board:
            if char not in list("XO.") or len(args.board) != 9:
                parser.error(
                    f'--board "{args.board}" must be 9 characters of ., X, O')

    if args.player and not args.cell:
        parser.error('Must provide both --player and --cell')

    if args.cell and not args.player:
        parser.error('Must provide both --player and --cell')

    # Another way to test that both argument are present or neither is:
    #
    # if any([args.player, args.cell]) and not all([args.player, args.cell]):
    # parser.error(f'Must provide both --player and --cell')

    if args.cell and args.player and args.board[args.cell - 1] in list("XO"):
        parser.error(f'--cell "{args.cell}" already taken')

    return args


def main():
    """The main program"""

    args = get_args()
    board = list(args.board)

    if args.player and args.cell:
        board[args.cell - 1] = args.player

    print(format_board(board))
    winner = find_winner(board)
    print(f'{winner} has won!' if winner else 'No winner.')


def format_board(board):
    """Format the board"""

    cells = [str(i) if c == '.' else c for i, c in enumerate(board, start=1)]
    line = '-------------'
    cells_template = '| {} | {} | {} |'
    return '\n'.join([
        line,
        cells_template.format(*cells[:3]), line,
        cells_template.format(*cells[3:6]), line,
        cells_template.format(*cells[6:]), line
    ])


def find_winner(board):
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in list("XO"):
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


if __name__ == '__main__':
    main()
