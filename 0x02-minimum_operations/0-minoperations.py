#!/usr/bin/python3
"""
minOperations module

This module contains a function `minOperations` that calculates the fewest
number of operations (Copy All and Paste) required to achieve exactly n 'H'
characters in a text file, starting with a single 'H'. If n is impossible
to achieve, the function returns 0.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations required to reach n 'H'
    characters using Copy All and Paste operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
