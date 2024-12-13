"""
Module: 0-prime_game

This module contains a function that determines the winner of multiple
rounds of
a game played between Maria and Ben using sets of consecutive integers.
The game involves selecting prime numbers and removing their multiples,
with the player unable to make a move losing the round.
"""

def isWinner(x, nums):
    """
    Determines the winner of each game round and returns the overall winner.

    Args:
        x (int): The number of game rounds.
        nums (list): A list where each element represents
        the value of n for a game round.

    Returns:
        str: The name of the player ('Maria' or 'Ben')
        who won the most rounds.
             If the winner cannot be determined, returns None.
    """
    def sieve_of_eratosthenes(max_num):
        """
        Generates a list of booleans indicating whether each number is prime.

        Args:
            max_num (int): The maximum number to evaluate for primality.

        Returns:
            list: A list where True represents a prime number,
            and False represents a non-prime.
        """
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        for i in range(2, int(max_num ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_num + 1, i):
                    is_prime[multiple] = False
        return is_prime

    # Precompute primes up to the maximum number in nums
    max_n = max(nums) if nums else 0
    is_prime = sieve_of_eratosthenes(max_n)

    # Precompute the cumulative number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
