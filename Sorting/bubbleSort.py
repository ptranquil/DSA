def bubbleSort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range (0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

arr = [6,5,8,9,3,4,1]
bubbleSort(arr)

"""
Algorithm:

1. loop through the array in reverse order say i
2. Internally make another loop j from 0 to i
3. if adjacent numnbers are smaller than swap them to put the largest element to the most right
4. repeat from 2 and 3 for each j
5. repeat 1 for each i 

Time Complexity: O(N^2) for the worst and average cases and O(N) for the best case.
Space Complexity: O(1)
"""

