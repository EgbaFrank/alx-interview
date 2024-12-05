#!/usr/bin/python3
"""defines the perimeter of the island described in grid"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
        grid (list): list of lists representing an island

    Return:
        integer: perimeter of the island

    grid is a list of list of integers:
        0 represents a water zone
        1 represents a land zone
        One cell is a square with side length 1
        Grid cells are connected horizontally/vertically
    """
    if not grid or not grid[0]:
        return 0

    row, col = len(grid), len(grid[0])
    perimeter = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                perimeter += 4
                # Subtract 2 for each shared edge
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
