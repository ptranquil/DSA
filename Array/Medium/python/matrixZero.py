'''
Set Matrix Zero
Problem Statement: 
    Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
'''

def matrix(arr,r,c):
    temp = arr
    for i in range( 0,r):
        for j in range(0,c):
            if arr[i][j] == 0:
                # arr = makeRowZero(arr,i,j)
                for row in range(0,r):
                    temp[row][i] = -1
                for col in range(0,c):
                    temp[j][col] = -1
    for i in range( 0,r):
        for j in range(0,c):
            if arr[i][j] == -1:
                temp[i][j] = 0
    return temp

# def makeRowZero(arr,rows,columns):
#     for column in range(0,columns):
#         arr[rows][columns] = 0
#         return arr

# def makeColumnZero(arr,rows,columns):
#     for i in range(0,rows):
#         arr[rows][columns] = 0
#         return arr

arr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(arr)
m = len(arr[0])
ans = matrix(arr, n, m)

print("The Final matrix is:")
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print(end="\n")

