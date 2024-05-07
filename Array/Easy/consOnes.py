# find maximum consecutive 1s in the array
def maxConsNums(arr):
    currCount , lastCount = 0,0
    for i in range(len(arr)):
        if arr[i] == 1:
            currCount+=1
        else:
            lastCount = currCount
            currCount=0
    return lastCount if lastCount > currCount else currCount 

arr = [1,4,5,1,1,1,4,3,1,1,1,1,1,5]
print("The maximum consecutive 1's is :",maxConsNums(arr))