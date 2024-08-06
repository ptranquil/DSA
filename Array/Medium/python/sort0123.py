#Sort an array of 0s, 1s and 2s

# Brute force using normal sorting algo or any other sorting algorithm

def sortArray(arr):
    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]

# arr = [2,0,2,1,1,0]
# sortArray(arr)
# print(arr)
    

'''
Better Approch: Counting the 0,1,2, followed by inseting the number of counts in the array
Time Complexity: O(2N)
    - O(N) by the first loop
    - Overall O(N) by the second loop
Space Compelxit O(1)
'''
def sortArrayOpt(arr):
    zero = ones = twos = 0
    n=len(arr)
    for i in range(n):
        if arr[i] == 0:
            zero = zero + 1
        elif arr[i] == 1:
            ones = ones + 1
        else:
            twos = twos + 1
    for i in range(zero):
        arr[i] = 0
    for j in range(zero,zero+ones):
        arr[j]=1
    for k in range(zero+ones, n):
        arr[k]=2

# arr = [2,0,2,1,1,0]
# sortArrayOpt(arr)
# print(arr)

'''
Optimal Approach
using 3 pointers OR Dutch National Flag Algorithm
Time Complexity: O(N)
Space Complexity: O(1)
'''

def dutchNFA(arr):
    low = mid = 0
    n = len(arr)
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low=low+1
            mid=mid+1
        elif arr[mid] == 1:
            mid = mid+1
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high -1

arr = [0,1,1,0,1,2,1,2,0,0,2]
dutchNFA(arr)
print(arr)
    