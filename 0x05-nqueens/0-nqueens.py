#!/usr/bin/python3
"""
This module provides a solution to the N-queens puzzle.
The N-queens puzzle is the problem
of placing N non-attacking queens on an N×N chessboard.
This module takes an integer N (greater than or equal to 4)
and finds all possible solutions to place N queens on an N×N board.

Usage:
    python3 nqueens.py N

Where:
    - N must be an integer greater than or equal to 4.
    - If called with incorrect arguments, it prints a
        usage message and exits with status 1.
    - If N is not a valid integer, it prints an error and exits with status 1.
    - If N is less than 4, it prints an error message and exits with status 1.

Example:
    python3 nqueens.py 4
    Outputs all possible solutions for a 4x4 board.
"""

import sys


def solve_nqueens(n):
    """Solves the N-queens puzzle for a given N and prints each solution."""
    def is_safe(board, row, col):
        """Check if a queen can be safely placed at board[row][col]."""
        for i in range(row):
            if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
                return False
        return True

    def place_queen(board, row):
        """Recursively place queens on the board and print solutions."""
        if row == n:
            print([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(board, row + 1)
                board[row] = -1

    board = [-1] * n
    place_queen(board, 0)


def main():
    """Entry point of the program, handles input and validates arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
