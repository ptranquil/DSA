def mergeSort(arr, low, high):
    if low == high: return
    mid = (low+high) // 2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)
    print(arr)

def merge(arr, low, mid, high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if(arr[left] < arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1
    
    while right <= high:
        temp.append(arr[right])
        right+=1
    
    for i in range(low,high+1):
        print("i is",i,"and low is",low,"and i-low is ",i-low)
        arr[i] = temp[i-low]
        # arr[i] = temp[i]

arr = [12,345,47,789,234,3456,567,23,424,24,465,576,78]
mergeSort(arr,0, len(arr)-1)
print(arr)

"""
Algorithm
1. Merge sort depends on the two basic scenario (divide and merge)
2. divide the arrayComplexity: O(N * log2(N)) - Worst Case
Space Complexity: O(N) from its mid lenght and keep on dividing untill a divided array contains only 1 element
3. merge the array using a temporary array and put them back onto the old array

Time  Worst Case


REF: https://www.youtube.com/watch?v=ogjf7ORKfd8

"""