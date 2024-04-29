def insertionSort(arr):
    for i in range (1,len(arr)):
        j=i
        while(j>0 and arr[j] < arr[j-1]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    print(arr)


arr = [6,5,8,9,3,4,1]
insertionSort(arr)

"""
Algorithm
1. Loop over the array starting from the 1st index say i
2. Make inner loop say j initialsiez to i till 0 (decrement)
3. compare whether secondLast element is greater than last element if yes swap

Time Complexity: O(N^2)
Space Complexity: O(1)
"""