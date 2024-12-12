#!/usr/bin/python3
"""
Prime game solution module
"""


def isWinner(x, nums):
    """
    Determines the winner of x rounds of prime game
    """
    if not nums or x < 1:
        return None

    # Determine the maximum value of n
    max_n = max(nums)

    # Precompute primes
    primes = [True for i in range(max_n + 1)]
    primes[0] = primes[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute cumulative prime counts
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    Ben = Maria = 0
    for n in nums:
        if prime_counts[n] % 2 == 0:  # Even number of primes means Ben wins
            Ben += 1
        else:  # Odd number of primes means Maria wins
            Maria += 1
    # Determine the overall winner
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
