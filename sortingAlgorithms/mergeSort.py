"""
Merge Sort is a comparison-based sorting algorithm that uses the divide-and-conquer approach. 
It divides the array into two halves, recursively sorts each half, 
and then merges the two sorted halves into a single sorted array. 
The merging step ensures that the elements are combined in the correct order. 
This process continues until the array is fully sorted.

Time complexity: O(n*log n)
Auxiliary space: O(n)
"""

# Code:
class Solution():
    def merge_sort(self,arr):
        if len(arr) > 1:
            # Finding the middle of the array
            mid = len(arr) // 2

            # Dividing the array elements into two halves
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Recursively sorting the two halves
            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            # Copy data to the temporary arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Checking if any element is left in left_half[]
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Checking if any element is left in right_half[]
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

arr = [12, 11, 13, 5, 6, 7]
print("Given array:", arr)
sol = Solution()
sol.merge_sort(arr)
print("Sorted array:", arr)