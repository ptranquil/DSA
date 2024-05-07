#brute force
def twoSum(arr, k):
    for i in range(len(arr)-1):
        for j in range (i+1,len(arr)):
            if arr[i]+arr[j] == k:
                return [i,j]
    return [-1,-1]

arr = [2,6,5,8,11]
k=15
print(twoSum(arr,k))


#using hashing
def twoSum(arr, k):
    hashdata= {}
    for i in range(len(arr)):
        rem = k - arr[i]
        if rem in hashdata:
            return [hashdata[rem], i]
        else:
           hashdata[arr[i]] = i
    return [-1,-1]

arr = [2,6,5,8,11]
k=14
print(twoSum(arr,k))

#two pointer
def twoSum(arr, k):
    left = 0
    right = len(arr)-1
    while(left<right):
        if arr[left]+arr[right] == k:
            return [left, right]
        left+=1
        right-=1
    return [-1,-1]

arr = [2,6,5,8,11]
k=14
print(twoSum(arr,k))