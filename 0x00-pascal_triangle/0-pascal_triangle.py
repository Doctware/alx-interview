#!/usr/bin/python3
"""
this module contains a function thats return pascal triangle
"""


def pascal_triangle(n):
    """
    this function returns a list of integers
    representing a pascal triangle

    if n <= 0 the return empty list
    """
    if n <= 0:
        return []

    triangle = [[1]]  # pascal triangle withh first row

    # building each row of pascal triangle
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
