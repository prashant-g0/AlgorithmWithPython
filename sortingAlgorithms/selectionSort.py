"""
Selection Sort is a simple comparison-based sorting algorithm. 
It divides the array into two parts: the sorted part and the unsorted part. 
The algorithm repeatedly selects the smallest (or largest, depending on the order) 
element from the unsorted part and moves it to the end of the sorted part.

Time complexity : O(n*n)
Auxiliary space : O(1)
"""

# Code: 

class Solution():
    def selectionSort(self, arr):
        for i in range(len(arr)):
            small_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[small_idx]:
                    small_idx = j
            arr[i], arr[small_idx] = arr[small_idx], arr[i]
        return arr

arr = [15, 12, 17, 10, 5, 13]
sol = Solution()
print(sol.selectionSort(arr))