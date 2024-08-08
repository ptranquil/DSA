#!!Important
def longestSubArray(arr,k):
    sum=0
    hashMap ={}
    maxLength=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum == k:
            maxLength = max(i+1, maxLength)
        
        rem = sum - k
        if rem in hashMap:
            newLen = i+1 - hashMap[rem]
            maxLength = max(maxLength,newLen)
        
        if sum not in hashMap:
            hashMap[sum] = i
    print(hashMap)
    return maxLength

arr = [1,1,1,1,1,4,5,3,3,2,4,56,7,76,65,5,6,7,7,7,8,8,8,8,8,8,8,8,8,8,8]
k = 64
print("The longest sub array with sum",k,"is",longestSubArray(arr,k))