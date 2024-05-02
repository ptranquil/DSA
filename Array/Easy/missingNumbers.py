# brute force approach
def findMissingNumber(arr,N):
    for i in range (N):
        flag = 0 # not present
        for j in range(N-1):
            if i == arr[j]:
                flag = 1 # present
        if flag == 0:
            return i
    return -1

#hashing
def hashFunc(arr,N):
    temp = [0]*(N+1)
    for i in range(N-1):
        temp[arr[i]]+=1
    for i in range(1,N+1):
        if temp[i] == 0:
            return i
    return -1

def sum(arr,N):
    totalSum = N*(N+1)//2
    sum=0
    for i in range(N-1):
        sum+=arr[i]
    return totalSum - sum

arr = [1,2,4,5]
N=5
print("The missing number in the array is : ",findMissingNumber(arr,N))
print("The missing number in the array using hasing is : ",hashFunc(arr,N))
print("The missing number in the array using sum logic is : ",sum(arr,N))