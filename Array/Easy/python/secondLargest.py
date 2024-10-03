#Brute Force approach only work if there is no duplicate element
def findLargestElement(arr):
    if len(arr) == 1: return arr
    secLargest = float('-inf') 
    max=float('-inf') 
    for i in range(0,len(arr)):
        if max < arr[i]:
            secLargest = max
            max = arr[i]
        elif (arr[i] > secLargest and arr[i] != max):
            secLargest = arr[i]
    return secLargest

arr = [234,56,72,31,31,324,3456,2,3121,1,4]
print('The second largest element in the array is:',findLargestElement(arr))

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""