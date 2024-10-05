# Book allocation problem:

# Question: You are given an array arr[] of size n, where each element of the array represents 
# the number of pages in a book. There are m students, and the task is to allocate the books 
# to these students such that:
# 1. Each student gets at least one book.
# 2. The maximum number of pages assigned to a student is minimized.
# 3. The pages allocated should be in contiguous manner
# Write a function bookAllocate(arr, n, m) that returns the minimum 
# possible value of the maximum number of pages a student has to read, 
# given the constraints. If it's not possible to allocate books, return -1.

# Time complexity : O(logN*n) where n is total number of books and N is range of binary search

# Example:
# arr = [2, 1, 3, 4]
# n,m = 4,2
# n is total number of books and m is total number of students

# Output: 6
# Explanation: Pages can be allocated such that; 
# Student 1 reads 2 and other reads 8
# Or student 1 reads 3 and other reads 7
# Or student 1 reads 6 and other reads 4
# So maxinum number of pages one can read is 8,7,6 and the minimum of maximum is 6 and hence satisfy the output

# Code:

class Solution:
    def isValid(self, arr, n, m, maxAllowed):
        student, pages = 1,0
        for i in range (len(arr)):
            if arr[i] > maxAllowed: return False
            if pages + arr[i] <= maxAllowed:
                pages += arr[i]
            else:
                student += 1
                pages = arr[i]
        return False if student > m else True

    def bookAllocate(self, arr, n,m):
        if m>n: return False
        ans = -1
        st, end = 0,sum(arr)

        while st<=end:
            mid = st + (end-st)//2
            if self.isValid(arr,n,m,mid):
                ans = mid
                end = mid - 1
            else: st = mid + 1

        return ans

arr = [2,1,3,4]
n = 4
m = 2
sol = Solution()
print(sol.bookAllocate(arr,n,m))