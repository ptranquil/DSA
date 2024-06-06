#Kadane's Algorithm : Maximum Subarray Sum in an Array
import sys

"""
Brute Force
Time Complexity: O(N2)
Space Complexity: O(1)
"""
def maxSubArraySum():
    max = sum= -sys.maxsize - 1
    for i in range(len(nums)):
        sum = 0
        for j in range (i,len(nums)):
            sum = sum + nums[j]
            if max < sum:
                max = sum
    return max

"""
Kadane Algorithm
Time Complexity: O(N)
Space Complexity: O(1)
"""
def maxSubArraySum():
    max = -sys.maxsize - 1
    sum = 0
    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(len(nums)):
        if sum == 0:
            start = i
        sum += nums[i]
        if sum > max:
            max = sum
            ansStart = start
            ansEnd = i
        if sum < 0: 
            sum = 0
    print(f"Sum is {sum} Array is : {nums[ansStart:ansEnd+1]}")

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArraySum()