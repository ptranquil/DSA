def quickSort(arr, low,high):
    if low < high:
            partitionIndex = makePartition(arr, low, high)
            quickSort(arr,low, partitionIndex-1)
            quickSort(arr, partitionIndex+1,high)

def makePartition(arr, low, high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while arr[i] <= pivot and i<=high-1:
            i+=1
        while arr[j] > pivot and j>=low+1:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low],arr[j] = arr[j],arr[low]
    return j

arr = [23,425,35,465,57,6,787,908,0,78,5,63,542,342,5,46]
quickSort(arr,0, len(arr)-1)
print(arr)