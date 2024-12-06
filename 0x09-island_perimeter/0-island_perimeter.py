#!/usr/bin/python3
"""
Module: island_perimeter

This module contains a function to calculate the perimeter of
an island in a 2D grid.
The grid is represented as a list of lists, where:
- 0 represents water
- 1 represents land

The function assumes the following:
- The grid is rectangular and does not exceed 100x100 in dimensions.
- The grid is completely surrounded by water.
- There is only one island or nothing in the grid.
- The island does not contain lakes (internal water not connected to
the grid's boundary).
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    The grid is represented as a list of lists of integers where:
    - 0 represents water
    - 1 represents land
    Each cell is square with a side length of 1, and cells are connected
    horizontally or vertically, not diagonally.

    Args:
        grid (list[list[int]]): A 2D list of integers representing the grid.

    Returns:
        int: The perimeter of the island.

    Example:
        >>> grid = [
        ...     [0, 1, 0, 0],
        ...     [1, 1, 1, 0],
        ...     [0, 1, 0, 0],
        ...     [0, 1, 0, 0]
        ... ]
        >>> island_perimeter(grid)
        16
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each horizontal neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                # Subtract 2 for each vertical neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
