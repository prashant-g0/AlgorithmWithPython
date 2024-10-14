"""
Binary Search is an efficient searching algorithm that works on sorted arrays. 
It repeatedly divides the search interval in half. Starting with the middle element, 
it compares the target value with the middle value: if they are equal, the search is complete. 
If the target is smaller, it continues the search on the left half; if larger, it searches the right half. 
This process continues until the element is found or the search interval becomes empty.

Time complexity: \(O(\log n)\)  
Auxiliary space: \(O(1)\)
"""

class Solution():
    def binarySearch(self, arr, target):
        st, end = 0, len(arr)
        arr.sort()
        print("Your search space: ",arr)

        while st <= end:
            mid = st + (end-st)//2
            if arr[mid] == target:
                return mid + 1
            elif arr[mid] > target:
                end = mid - 1
            else: st = mid + 1
        return -1
    
arr = [23, 45, 6, 78, 32]
target = 4
sol = Solution()
BS = sol.binarySearch(arr, target)

if BS == -1:
    print("target is not found.")
else:
    print("target found at ", BS)
    