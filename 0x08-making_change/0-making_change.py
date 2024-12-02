#!/usr/bin/python3
"""
This module provides a solution for the "making change" problem.

The problem involves determining the fewest number of coins needed to meet a given total using coins of specified denominations. If it's impossible to meet the total using the available denominations, the function returns -1.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list of int): A list of the values of the coins available. Each value is an integer greater than 0.
        total (int): The target amount of money to meet using the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total is 0 or less, return 0.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order to use the largest denominations first
    coins.sort(reverse=True)

    count = 0  # Number of coins used
    for coin in coins:
        # Determine how many coins of this denomination can be used
        if total >= coin:
            count += total // coin
            total %= coin  # Update the remaining amount

        # If the total is met, return the count
        if total == 0:
            return count

    # If total is not 0 after iterating through all coins, return -1
    return -1
