#!/usr/bin/python3
"""Change comes from within;
coin change problem solution
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins
    needed to meet a given amount
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    coins.sort(reverse=True)
    count = 0

    # Threshold for switching to dynamic programming
    greed_limit = max(coins) * 2

    change = total

    # Greedy phase
    while change > greed_limit:
        change -= coins[0]
        count += 1

    # Dynamic phase
    dp = [float('inf')] * (change + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if a solution exists
    if dp[change] == float('inf'):
        return -1

    return dp[change] + count
