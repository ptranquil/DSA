def isArraySorted(arr):
    for i in range(0, len(arr)-1):
        if(arr[i] > arr[i+1]):
            return False
    return True

arr = [1,2,3,4,3,5]
if(isArraySorted(arr)):
    print("The array is sorted")
else:
    print("The array is not sorted")

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""