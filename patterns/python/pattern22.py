'''
4444444
4333334
4322234
4321234
4322234
4333334
4444444
'''

n=4
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        left=j
        right = 2*n-2 - i
        bottom = 2*n-2-j
        val = n - min(left, top, right, bottom)
        print(val, end=' ')
    print()

'''
Algorithm goes like subtract the n from each element to be formed, the new matrix created will be

0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 2 2 2 1 0
0 1 2 3 2 1 0
0 1 2 2 2 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

By observing this matrix we can say the the each element is the smallest distance from its top, left, bottom and right distance
and after finding the smallest distance we can subtract that value from n to get the desired result
'''