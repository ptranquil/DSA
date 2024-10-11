'''
Set Matrix Zero
Problem Statement: 
    Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
TC: O(n*m) * (O(n) + O(m)) + O(n*m) 
SC: O(n) + O(m)
'''

def matrix(a,row,col):
    def markRow(i):
        for j in range(col):
            if(a[i][j] != 0):
                a[i][j] = -1

    def markCol(j):
        for i in range(row):
            if(a[i][j] != 0):
                a[i][j]=-1

    for i in range(row):
        for j in range(col):
            if(a[i][j] == 0):
                markRow(i)
                markCol(j)

    for i in range(row):
        for j in range(col):
            if(a[i][j] == -1):
                a[i][j]=0

    for i in range(row):
        for j in range(col):
            print(a[i][j], end= ' ')
        print()

arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print("The Final matrix  using bruteForce is:")
n = len(arr)
m = len(arr[0])
ans = matrix(arr, n, m)



'''
Better
TC
SC
'''

def betterSol(arr, r, c):
    rows = [0] * r
    cols= [0] * c
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                rows[i] = 1
                cols[j] =1
    
    for i in range(r):
        for j in range(c):
            if(rows[i] or cols[j]):
                arr[i][j] ==0
    
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end= ' ')
        print()

print("The Final matrix  using better Solution is:")
ans = betterSol(arr, n, m)
