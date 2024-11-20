#!/usr/bin/python3
"""Rotate_2d matrix solution
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a n x n 2D matrix 90 degrees clockwise

    Args:
        matrix(list[list]): Matrix to be rotated
    """
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse row
    for row in matrix:
        row.reverse()
