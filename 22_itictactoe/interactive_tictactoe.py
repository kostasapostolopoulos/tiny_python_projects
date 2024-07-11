#!/usr/bin/env python3
"""
Interactive Tic-Tac-Toe game using NamedTuple
"""

from typing import List, NamedTuple, Optional


class State(NamedTuple):
    """Represents the state of the game"""

    board: List[str] = list("." * 9)
    player: str = "X"
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


def main() -> None:
    """The main program"""

    state = State()

    while True:
        print("\033[H\033[J")
        print(format_board(state.board))

        if state.error:
            print(state.error)
        elif state.winner:
            print(f"{state.winner} has won!")
            break

        state = get_move(state)

        if state.quit:
            print("You lose!")
            break
        if state.draw:
            print("It's a draw")
            break


def get_move(state: State) -> State:
    """Get the player's move"""

    player = state.player
    cell = input(f"Player {player}, what is your move? [q to quit]: ")

    if cell == "q":
        return state._replace(quit=True)

    if not (cell.isdigit() and int(cell) in range(1, 10)):
        return state._replace(error=f'Invalid cell "{cell}", please use 1-9')

    cell_num = int(cell)
    if state.board[cell_num - 1] in "XO":
        return state._replace(error=f'Cell "{cell}" already taken')

    board = state.board
    board[cell_num - 1] = player
    return state._replace(board=board,
                          player="O" if player == "X" else "X",
                          winner=find_winner(board),
                          draw="." not in board,
                          error=None)


def format_board(board: List[str]) -> str:
    """Format the board"""

    cells = [str(i) if c == "." else c for i, c in enumerate(board, 1)]
    line = "-------------"
    cells_template = "| {} | {} | {} |"
    return '\n'.join([
        line,
        cells_template.format(*cells[:3]), line,
        cells_template.format(*cells[3:6]), line,
        cells_template.format(*cells[6:]), line
    ])


def find_winner(board: List[str]) -> Optional[str]:
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in list("XO"):
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player

    return None


if __name__ == "__main__":
    main()
