#!/usr/bin/python3
"""
Minimum operations to reach n characters
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if impossible.

    Examples:
        >>> min_operations(9)
        6
        >>> min_operations(1)
        0
        >>> min_operations(0)
        0
        >>> min_operations(-12)
        0
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
