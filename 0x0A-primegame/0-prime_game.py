#!/usr/bin/python3
""" Prime Game Problem
    Topic: Eratosthenes algorithm
"""


def isWinner(x, nums):
    """
    Determines the winner in the prime game using
    Eratosthenes prime sieving algorithm
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        playing_numbers = [num for num in range(2, nums[round] + 1)]
        index = 0
        # Sieve prime numbers per round
        while (index < len(playing_numbers)):
            current_prime = playing_numbers[index]
            sieve_index = index + current_prime
            while(sieve_index < len(playing_numbers)):
                playing_numbers.pop(sieve_index)
                sieve_index += current_prime - 1
            index += 1
        # Determine winner - if number of primes is even player 1 wins
        # else player 2 wins. Player 2  also wins if there is only one
        # number to pick from
        prime_count = (len(playing_numbers))
        if prime_count and prime_count % 2:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    return 'Ben' if Ben > Maria else 'Maria'
