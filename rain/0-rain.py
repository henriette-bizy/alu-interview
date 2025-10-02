#!/usr/bin/python3
"""
The program to calculate the square units of the
water between the walls after it rains.
"""


def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    if n < 3:
        return 0

    # Arrays to store the maximum heights to the left and right
    left_max = [0] * n
    right_max = [0] * n

    # Fill the left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill the right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the total water retained
    total_water = 0
    for i in range(n):
        total_water += max(0, min(left_max[i], right_max[i]) - walls[i])

    return total_water
