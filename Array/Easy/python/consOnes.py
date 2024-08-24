# find maximum consecutive 1s in the array
def maxConsNums(arr):
    curr , maxi = 0,0
    for i in range(len(arr)):
        if arr[i] == 1:
            curr+=1
        else:
            maxi = max(curr, maxi)
            curr=0
    return maxi

arr = [1,4,5,1,1,1,4,3,1,1,1,1,1,5]
print("The maximum consecutive 1's is :",maxConsNums(arr))