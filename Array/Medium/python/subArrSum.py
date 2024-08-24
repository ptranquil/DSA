"""
Count Subarray sum Equals K
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
"""

"""
Brute Force Approach
Time Complexity: O(N3)
Space Complexity: O(1)
"""
def countSubArray(arr,k):
    N = len(arr)
    cnt = 0
    for i in range(N):
        for j in range(i,N):
            subArraySum = sum(arr[i:j+1])
            if subArraySum == k:
                cnt+=1
    return cnt

arr = [3,1,2,4]
k=6
res = countSubArray(arr,k)
print("BruteForce : The total no of subarray equals",k,"is",res)


"""
Better Approach
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

def countSubArrayBA(arr,k):
    N=len(arr)
    cnt=0
    for i in range(N):
        subArrSum = 0
        for j in range(i,N):
            subArrSum+=arr[j]
            if subArrSum == k:
                cnt+=1

arr = [3,1,2,4]
k=6
res = countSubArray(arr,k)
print("Better Approach : The total no of subarray equals",k,"is",res)
