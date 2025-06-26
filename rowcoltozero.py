# Mark all rows and cols to 0 if there is a 0

a=[
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
row=4
col=4
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