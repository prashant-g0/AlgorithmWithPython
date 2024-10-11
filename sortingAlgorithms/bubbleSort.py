""" 
Bubble Sort Algorithm: Bubble Sort is a simple comparison-based sorting algorithm. 
It works by repeatedly stepping through the list, comparing adjacent elements, 
and swapping them if they are in the wrong order. This process repeats until the list is sorted.

Time complexity : O(n*n)
Auxiliary space : O(1)
"""

# Code: 

class Solution():
    def bubbleSort(self, arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
arr = [11, 13, 15, 21, 10]
sol = Solution()
print(sol.bubbleSort(arr)) # Output: [10, 11, 13, 15, 21]