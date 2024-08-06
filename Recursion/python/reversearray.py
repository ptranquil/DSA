def reverse(arr):
    start = 0
    end = len(arr) - 1
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
    return arr

def reverseRec(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseRec(arr,start+1,end-1)
    return arr

print(reverse([1,2,3,4,5]))
arr = [4,5,3,2,7]
print(reverseRec(arr, 0, len(arr)-1))