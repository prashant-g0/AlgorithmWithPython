#The Boyer-Moore voting algorithm is one of the popular optimal algorithms
#  which is used to find the majority element among the given elements
#  that have more than N/ 2 occurrences.
# Time complexity : O(n)
# Auxiliary space : O(1)

# Examples: 
# Input :{1,1,1,1,2,3,5}
# Output : 1
# Explanation : 1 occurs more than 3 times.
# Input : {1,2,3}
# Output : -1
# Explanation : None of the element occurs more than 3 times.

# Brute-force method
# Explanation: Traverse through the given list and store count for each element, elements having count >= n/2 is the majority element.
# Code:
# Function to find the Majority element in an array
def majorityElement(arr):
    n = len(arr)  

    # Loop to consider each element as a candidate for majority
    for i in range(n):
        count = 0

        # Inner loop to count the frequency of arr[i]
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        # Check if count of arr[i] is more than half the size of the array
        if count > n // 2:
            return arr[i]

    # If no majority element found, return -1
    return -1

# Better and optimal approach using "Moore's voting Algorithm"
# Code:
# Function to find the Majority element in an array
def majorityElement(arr):
    freq, ans = 0,0
    # Loop to find the element with majority frequency
    for i in range(len(arr)):
        if freq == 0:
            ans = arr[i]
        if ans == arr[i]:
            freq += 1
        else:
            freq -= 1
    # Validate the count 
    count = 0
    for num in arr:
        if num == ans:
            count += 1
    # If count is greater than len(arr) / 2, return the element; otherwise, return -1
    if count > len(arr)//2:
        return ans
    else:
        return -1
    