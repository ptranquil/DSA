#Brute Force approach
def findLargestElement(arr):
    if len(arr) == 1: return arr
    max=arr[0]
    for i in range(0,len(arr)):
        if max <arr[i]:
            max = arr[i]
    return max

arr = [1,2,3,4,5]
print('The largest element in the array is:',findLargestElement(arr))

#using in built function
print(max(arr))

#another approach would be sort the array in asc order and return the last element

def sortArr(arr):
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] >arr[j]):
                arr[i],arr[j] = arr[j],arr[i]

arr = [1,2,3,4,5]
sortArr(arr)
print('The largest element in the array is:',arr[len(arr)-1])