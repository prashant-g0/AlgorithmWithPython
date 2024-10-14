"""
Linear Search is a simple searching algorithm used to find an element in a list or array. 
It works by sequentially checking each element from the start of the list until the desired 
element is found or the end of the list is reached. 
It does not require the array to be sorted and is best suited for small datasets.

Time complexity: O(n)
Auxiliary space: O(1)
"""

# Code: 

class Solution():
    def linearSearch(self, arr, target):
        # Traverse through each element in the array
        for i in range(len(arr)):
            # check for target value
            if arr[i] == target:
                # return position when target is found
                return i+1
        # return -1 if target not found
        return -1
            
arr = [11, 34, 5, 7, 20, 22]
target  = 34
sol = Solution()
found = sol.linearSearch(arr, target)
if found == -1:
    print("target not found.")
else:
    print("target found at",found )