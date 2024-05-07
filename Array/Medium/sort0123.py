#Sort an array of 0s, 1s and 2s

#brute force
def sortArray(arr):
    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]

arr = [2,0,2,1,1,0]
sortArray(arr)
print(arr)
    