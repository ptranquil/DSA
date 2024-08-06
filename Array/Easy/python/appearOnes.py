#Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

def findOnes(arr):
    hashMap = {}
    for num in arr:
        if num in hashMap:
            hashMap[num] = hashMap.get(num, 0)+1 # trying to get the key which doesnt exist with a default value of 0 
        else:
            hashMap[num]=1

    for key in hashMap:
        if hashMap[key] == 1:
            return key
    return -1

arr = [1,1,2,2,3,3,4,5,5,6,6]
print("The number that appear ones is ",findOnes(arr))