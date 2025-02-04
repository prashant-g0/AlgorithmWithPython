#binary search on smaller range and not on complete array
def binarySearch(arr, st, end, key):
    if end >= st: mid = st + (end-st)//2
    if arr[mid] == key: return mid+1
    if arr[mid] > key: return binarySearch(arr, st, end, key)
    return binarySearch(arr, st, end, key)
    return -1
#finding the smaller range to apply binary search
def Targetrange(arr, key):
    st, end = 0, 1
    val = arr[0]
    
    while val < key:
        st = end
        end = 2*end
        val = arr[end]
    return binarySearch(arr, st, end, key)
#starting point of program
if __name__ == "__main__":
    arr = [3, 5, 6, 7, 12, 14, 17, 20, 25, 28, 33, 45, 67, 63, 64, 72]
    k = 17
    ans = Targetrange(arr, k)
    print(f"key is present at position {ans}")
