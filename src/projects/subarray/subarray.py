#!/usr/bin/env python3
"""Subarray"""


def kadane(array: list) -> int:
    """Implementation of Kadane's algorithm"""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in array:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
        

def main():
    """This is the main function"""
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane(array))


if __name__ == "__main__":
    main()
