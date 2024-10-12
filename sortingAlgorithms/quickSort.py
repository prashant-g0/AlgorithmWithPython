"""
Quick Sort is a highly efficient, comparison-based sorting algorithm that follows 
the divide-and-conquer approach. It works by selecting a 'pivot' element from the array 
and partitioning the other elements into two sub-arrays: those less than the pivot and those greater than 
the pivot. The pivot is then placed in its correct position. This process is recursively applied 
to the sub-arrays until the entire array is sorted.

Time complexity (average case): O(n*log n)  
Auxiliary space: O(log n)
"""

# Code:

class Solution:
    def pivot(self, arr, low, high):
        pivotIDX = arr[low]
        i, j = low, high
        while i < j:
            # Move i to the right until we find an element greater than the pivot
            while arr[i] <= pivotIDX and i < high:
                i += 1
            # Move j to the left until we find an element less than or equal to the pivot
            while arr[j] > pivotIDX and j > low:
                j -= 1
            if i < j:
                # Swap elements at i and j
                arr[i], arr[j] = arr[j], arr[i]
        # Swap pivot element with element at j (final position of the pivot)
        arr[low], arr[j] = arr[j], arr[low]
        return j  # Return the partition index
    
    def quickSort(self, arr, low, high):
        if low < high:
            pivotIDX = self.pivot(arr, low, high)
            self.quickSort(arr, low, pivotIDX - 1)  # Sort elements before pivot
            self.quickSort(arr, pivotIDX + 1, high)  # Sort elements after pivot

# Test the code
arr = [17, 12, 5, 6, 3, 10, 7]
sol = Solution()
sol.quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output the sorted array
