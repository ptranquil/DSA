def selectionSort(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range (i,len(arr)):
            if(arr[min] > arr[j]):
                min = j
        
        #swap only if min is different
        if min != i:
            arr[i], arr[min] = arr[min],arr[i]

arr = [6,5,8,9,3,4,1]
selectionSort(arr)
print(arr)

"""
Algorithm
1. Starting from the first index to n-1 index, find the smallest element
2. swap the first element with the smallest element and increment the loop
3. do this till the end of the loop

Time Complexity: O(N^2)
Space Complexity: O(1)
"""