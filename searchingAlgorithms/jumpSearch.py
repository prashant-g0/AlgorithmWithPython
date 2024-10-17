"""
Jump Search is a searching algorithm designed for sorted arrays. 
It works by dividing the array into blocks of fixed size, typically the 
square root of the array's length. Instead of checking each element one by one, 
Jump Search skips ahead by the block size. If the target value is smaller than the 
current element, it performs a linear search within the previous block. 
This method strikes a balance between linear search and binary search for efficiency in sorted data.

Time complexity: O(sqrt{n})
Auxiliary space: O(1)
"""

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Step size
    
    # Finding the block where element is present (if it is present)
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Doing a linear search for target in the block beginning with prev
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i+1
    return -1

# Example usage
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = -1
result = jump_search(arr, target)
if result == -1: print("Element not found")
else: print(f"Element found at index {result}")
