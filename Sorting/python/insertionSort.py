def insertionSort(arr,i,n):
    if i == n: return
    j=i
    while j>0 and arr[j] < arr[j-1]:
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j-=1
    insertionSort(arr,i+1,n)

arr = [3, 4, 5, 2, 1, 3, 5, 6, 7, 8, 6, 4, 2]
insertionSort(arr, 0, len(arr)-1)
print(arr)

"""
Algorithm

1. Start from 0 i.e i to n-1 as n and repeat untill i == n as base condition met i.e. we end the last element
2. Initialize i to j and repeat untill j < 0, decrement...
3. swap is last element is smaller than second last element
4. call the function recursively with by increement i

Time Complexity: O(N^2)
Space Complexity: O(1)
"""