#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys

def initialise_board(n):
    """Initializes an `n`x`n` sized chessboard with ' 's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """Creates and Returns a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [board_deepcopy(row) for row in board]
    return board

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    soln = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                soln.append([r, c])
    return soln

def crossed_out(board, row, col):
    """
    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    num = len(board)
    # X out all forward spots
    for c in range(col + 1, num):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, num):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, num):
        if c >= num:
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= num:
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, num):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def solve_recursively(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for c in range(n):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            crossed_out(tmp_board, row, c)
            solutions = solve_recursively(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialise_board(int(sys.argv[1]))
    solutions = solve_recursively(board, 0, 0, [])
    for sol in solutions:
        print(sol)
