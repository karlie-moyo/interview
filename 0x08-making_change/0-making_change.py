#!/usr/bin/python3
"""
Make change task
"""


def makeChange(coins, total):

    """ Checks how minimum number of coins needed
        to meet the total amount.
        Args:
            - coins: list of coins denominations to use
            - total: amount of change required
        Return:
            - Minimum number of coins needed to make change.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coins_needed = 0
    for coin in coins:
        if total / coin > 0:
            coins_needed = coins_needed + (total // coin)
            total = total % coin
        if not total:
            break

    if total != 0 or coins_needed == 0:
        return -1
    return coins_needed
