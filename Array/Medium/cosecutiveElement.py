"""
Longest Consecutive Sequence in an Array
Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.
"""

def findCons(arr):
    left = right = 0
    arr.sort()
    maxi = 1
    curr = 0
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i] == 1):
            curr+=1
            maxi = max(maxi,curr)
        else:
            curr = 0
    print(maxi+1)
arr =   [3, 8, 5, 7, 6]
findCons(arr)
