"""
Leaders in an Array
Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.
"""

"""
Brute Force Approach
Time Complexity: O(N2)
Space Complexity: O(N)
"""
def findLeader(arr):
    res=[]
    for i in range(len(arr)):
        leader= True
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                leader = False
                break
        if leader:
            res.append(arr[i])
    print(res)

# arr = [4,7,1,0]
# findLeader(arr)

"""
Optimal Approach
Time Complexity: O(N)
Space Complexity: O(N)
"""

def findLeaderOpt(arr):
    currLeader = arr[len(arr)-1]
    res=[]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > currLeader:
            res.append(currLeader)
            currLeader = arr[i]
    res.append(currLeader)
    print(res)

arr = [16, 17, 4, 3, 5, 2]
findLeaderOpt(arr)
