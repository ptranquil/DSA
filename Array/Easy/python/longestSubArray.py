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