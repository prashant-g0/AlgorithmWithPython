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