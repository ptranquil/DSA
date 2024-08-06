'''
Find the Majority Element that occurs more than N/2 times
'''

'''
using hashing
Time Complexity: O(N log N)
Space Complexity: O(N) as using dictionary for storing
'''
def findMajority(arr):
    bound = len(arr) / 2
    tempDict = {}
    for i in range(0,len(arr)):
        if arr[i] in tempDict:
            tempDict[arr[i]] = tempDict[arr[i]] + 1
        else:
            tempDict[arr[i]] = 1
        if(tempDict[arr[i]] > bound):
            return arr[i]

# arr = [2,2,1,1,1,2,2]
# res = findMajority(arr)
# print(res)


'''
using moores voting algorithm
Time Complexity : 
Space Complexity: 
'''

def MVA(arr):
    count = 0
    ele = 0
    for i in range(len(arr)):
        if count == 0:
            ele = arr[i]
            count = 1
        elif ele == arr[i]:
            count = count + 1
        else:
            count = count -1 
    return ele

arrr = [7,7,5,7,5,4,4,5,6,7,7,5,3,5,7,45,5,5,3,5,5,55,5]
ele = MVA(arrr)
print(ele)