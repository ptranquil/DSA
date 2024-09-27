'''
1
01
101
0101
10101
'''

n=5
row=0
for i in range(n):
    col = (1,0)[row]
    for j in range(i+1):
        print(col,end=' ')
        col = (1,0)[col]
    row = (1,0)[row]
    print()
