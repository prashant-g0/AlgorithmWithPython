"""
Insertion sort: For arrays with more than one element, the function proceeds to iterate over the array 
starting from the second element. It takes the current element (key) and compares it with the elements in the 
sorted portion of the array that precede it. If the key is smaller than an element in the sorted portion, 
the function shifts that element to the right, creating space for the key. This process continues until the 
correct position for the key is found, and it is then inserted in that position.

# Time Complexity: O(N*N) 
# Auxiliary Space: O(1)
"""

# Code
def insertionSort(arr):
    # If the array has 0 or 1 element; sorted
    if len(arr) <= 1:
        return arr

    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element as the key 
        current = arr[i]
        j = i - 1
        
        # Shift elements to the right until the correct position for current is found
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key in the correct position
        arr[j + 1] = current

    return arr

# driver code
arr = [21, 11, 31, 15, 61]
print(insertionSort(arr))





