#The idea is to store the maximum sum of contiguous subarray.

#For example:
#array = [-2,-3,4,-1,-2,1,5,-3]
#For this given array the subarray(s) will be [-2], [-2,-3,4], [-3,4,-1].....
#Subarray(s) are smaller parts of original array.

#Contiguous memory refers to a block of memory addresses that are sequentially 
# next to each other, without any gaps. This means that the data is stored in adjacent memory locations.

#For our example array the subarray with maximu sum is [4,-1,-2,1,5]
#For which the sum is = 7

#Time complexity: O(n), Auxiliary space: O(1)

#Code:

#Taking array from user
arr = [-2,-3,4,-1,-2,1,5,-3]
print("Array: ",arr)

#Defining some variables
max_num = -2147483648 #minimum of interger number
totalSum = 0

#traversing through array and finding for subarray with maximum sum
for i in range(len(arr)):
    totalSum += arr[i]

    if(max_num < totalSum):
        max_num = totalSum

    if(totalSum < 0):
        totalSum = 0
#print the output
print("Subarray with max sum is: ",max_num)
