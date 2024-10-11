"""
Longest Consecutive Sequence in an aay
Problem Statement: You are given an aay of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.
"""

a= [100,102,100,101,101,4,3,2,3,2,1,1,1,2]
n=len(a)
'''
Brute Force
TC: O(N^2)
SC: O(N)
'''
import math
def linearSearch(a, ele):
    for i in range(len(a)):
        if(a[i] == ele):
            return 1
    return 0

def findConsecutiveElement(a):
    maxi=-math.inf
    for i in range(n):
        ele=a[i]
        count=0
        while(linearSearch(a, ele)):
            count+=1
            ele+=1
        maxi = max(maxi, count)
    return maxi
print('The longest consecutive using brute force approach: ', findConsecutiveElement(a))

'''
Better Approach: (Sort & search)
TC: O(N * NlogN) 
SC: O(N)
'''
def longestConsecutiveBetter(a):
    import math
    a.sort()
    n=len(a)
    lastSmaller = -math.inf
    count=0
    longest=-math.inf
    for i in range(n):
        if(a[i]-1 == lastSmaller):
            count+=1
            lastSmaller=a[i]
        elif a[i] != lastSmaller:
            count=1
            lastSmaller = a[i]
        longest = max(longest, count)
    return longest

print('The longest consecutive using better approach: ', longestConsecutiveBetter(a))

'''
Optimal Approach using set
'''
def findCons(a):
    n = len(a)
    if n == 0:
        return 0
    longest = 1
    st = set()
    for i in range(n):
        st.add(a[i])
    
    for ele in st:
        if ele-1 not in st:
            count=1
            while(ele+1 in st):
                count+=1
                ele+=1
            longest= max(longest, count)
    return longest
print('The longest consecutive using better approach: ', findCons(a))