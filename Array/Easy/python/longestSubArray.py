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


arr = [2,3,5,1,9]
k = 10
print("The longest sub array with sum",k,"is",longestSubArray(arr))

# Longest Subarray with sum K | [Postives and Negatives]

def findSubArr(arr,K):
    sum = 0
    hashMap = {}
    maxLen = 0
    for i in range(len(arr)):
        sum+=arr[i]
        if(sum == K):
            maxLen = max(maxLen,i+1)
        rem = sum - K
        if (rem in hashMap):
            newLen = i - hashMap[rem]
            maxLen = max(maxLen,newLen)
        if sum not in hashMap:
            hashMap[sum] = i
    return maxLen
K = 5
# arr= {-1, 1, 1}
arr = [2,3,1,1,2,1,1,1,1,1]
print('The maximum subarray length is : ',findSubArr(arr,K))
arr = [1,1,1,1,1,4,5,3,3,2,4,56,7,76,65,5,6,7,7,7,8,8,8,8,8,8,8,8,8,8,8]
k = 64
print("The longest sub array with sum",k,"is",longestSubArray(arr,k))
