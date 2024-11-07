#!/usr/bin/python3
"""
Nqueen solution module
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[False for _ in range(n)] for _ in range(n)]
results = []


def is_safe(col, row):
    for i in range(col):
        if board[i][row]:
            return False

    left_diag = row - 1
    right_diag = row + 1

    for i in range(col - 1, -1, -1):
        if left_diag >= 0:
            if board[i][left_diag]:
                return False
            left_diag -= 1

        if right_diag < n:
            if board[i][right_diag]:
                return False
            right_diag += 1

    return True


def nqueens(col):
    if col >= n:
        results.append([
            [m, n] for m in range(len(board))
            for n in range(len(board[m]))
            if board[m][n]
        ])
        return

    for row in range(n):
        if is_safe(col, row):
            board[col][row] = True
            nqueens(col + 1)
            board[col][row] = False


if __name__ == "__main__":
    nqueens(0)

    for solution in results:
        print(solution)
