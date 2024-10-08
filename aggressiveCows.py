# Problem: Maximum Minimum Distance for Placing Cows
# Farmer John has built n stalls along a straight line at different positions. He wants to assign c cows 
# to these stalls. However, he wants to maximize the minimum distance between any two cows to ensure they 
# are as comfortable as possible.

# Time complexity : O(n log(n) + n log(d)) 
# Space complexity : O(1)

class Solution:
    def isPossible(self, arr, c,mid): # O(n log(n))
        cow, position = 1, arr[0]
        for i in range(1,len(arr)):
            if arr[i]-position >= mid:
                cow += 1
                position = arr[i]
            if cow == c:
                return True
        return False
    
    def getDistance(self, arr, c): # n log(d) where d is the range of binary search
        st, end, ans = 0, max(arr)-min(arr), -1
        arr.sort()
        while st<=end:
            mid = st + (end-st)//2
            if self.isPossible(arr,c,mid):
                ans = mid
                st = mid + 1
            else:
                end = mid - 1
        return ans

arr = [1,2,8,4,9]
c = 3
sol = Solution()
print(sol.getDistance(arr,c))
