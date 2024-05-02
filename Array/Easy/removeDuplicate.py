# Remove duplicate from sorted array
#using hashing
def removeDup(arr):
    hashSet = {}
    result = []
    for i in range (0,len(arr)):
        if arr[i] in hashSet:
            hashSet[arr[i]]+=1
        else:
            hashSet[arr[i]]=1
    for key in hashSet:
        result.append(key)
    return result

arr=[1,2,3,3,4,4,5,5,6]
res=removeDup(arr)
print(res)

#using 3rd variable
def remove(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1

arr=[1,2,3,3,4,4,5,5,6]
dup = remove(arr)
print(arr[:dup])

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""