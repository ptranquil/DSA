def longestSubArray(arr):
    temp = [0]*len(arr)
    temp[0] = arr[0]
    for i in range(1,len(arr)):
        temp[i] = temp[i-1]+arr[i]
    max = float('-inf')
    j=1
    for val in temp:
        if val == k:
            max = j
        j+=1    
    return max


arr = [2,3,5,1,9]
k = 10
print("The longest sub array with sum",k,"is",longestSubArray(arr))