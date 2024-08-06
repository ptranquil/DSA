def leftRotate(arr,N):
    N=N%len(arr)
    if N==len(arr):
        return arr      
    return arr[N:]+arr[0:N]

# arr = [1,2,3,4,5]
# N = int(input("Enter how many times you want to left rotate an array : "))
# print("Array after",N,"left rotate is : ",leftRotate(arr,N))


#another approach
def reverse(arr, start, end):
    # Helper function to reverse a portion of the array
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def leftRotate(arr, k):
    n = len(arr)
    k = k % n  # Normalize k to be within the range of array length

    # Reverse the first part of the array (0 to k-1)
    reverse(arr, 0, k - 1)
    # Reverse the second part of the array (k to n-1)
    reverse(arr, k, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)

arr = [1, 2, 3, 4, 5]
k = 1
leftRotate(arr, k)
print("Array after left rotation:", arr)


