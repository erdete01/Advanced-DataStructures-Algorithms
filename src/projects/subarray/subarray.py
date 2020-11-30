#!/usr/bin/env python3
"""Subarray"""

# Time Complexity --> O(n)
def kadane(array: list) -> int:
    """Implementation of Kadane's algorithm"""
    # If there is nothing, there will be no subarrays and return 0
    if len(array) == 0:
        return 0
    # else get the first items and then iterate from the index 1
    best_sum = array[0]  # or: float('-inf')
    current_sum = array[0]
    for i in range(1, len(array)):
        # max of both current array[i] and array[i-1] gives my current_sum
        current_sum = max(array[i], current_sum + array[i])
        # same as max(current_sum, best_sum). Update the best_sum
        if current_sum > best_sum:
            best_sum = current_sum
    return best_sum
        

def main():
    """This is the main function"""
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane(array))


if __name__ == "__main__":
    main()
