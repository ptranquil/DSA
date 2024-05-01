#Brute Force approach only work if there is no duplicate element
def findLargestElement(arr):
    if len(arr) == 1: return arr
    secLargest = float('-inf') 
    max=float('-inf') 
    for i in range(0,len(arr)):
        if max < arr[i]:
            secLargest = max
            max = arr[i]
    return secLargest

arr = [1,2,3,4,5,6,7,8,8,9]
print('The second largest element in the array is:',findLargestElement(arr))

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""