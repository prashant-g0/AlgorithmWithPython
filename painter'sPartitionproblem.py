# Question:
# You are given an array arr[] of size n where each element represents the amount of time 
# required to paint a board. There are m painters available, and each painter can only paint 
# contiguous sections of the board. All painters can paint simultaneously. 
# Find the minimum time required to paint all the boards if the painters can paint with equal speed.

# Explaination: 
# if there are 2 painters;
# painter 1 can take 40 mins and painter 2 can take 60
# painter 1 can take 70 mins and painter 2 can take 30
# painter 1 can take 80 mins and painter 2 can take 20
# The max time one can take is 60,70,80 and min of these is 60 which satisfies the answer.

# Time complexity : O(log(sum)*n)
# Space complexity : O(1)

# Code:
class Solution:
    def isPossible(self,arr,m,allowedTime):
        painter,time = 1,0
        for i in range(len(arr)):
            if time + arr[i] <= allowedTime:
                time += arr[i]
            else:
                painter += 1
                time = arr[i]
        return True if painter <= m else False

    def paintersPartition(self,arr,m):
        st,end,ans = max(arr),sum(arr),-1
        
        while st <= end:
            mid = st + (end-st)//2
            if self.isPossible(arr,m,mid):
                ans = mid
                end = mid -1
            else:
                st = mid +1
        return ans


arr = [40,30,10,20]
n,m = 4,2
sol = Solution()
print(sol.paintersPartition(arr,m))