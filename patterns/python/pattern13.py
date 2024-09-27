'''
1        1
12      21
123    321
1234  4321
1234554321
'''

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    spaces=2*(n-i)
    for k in range(spaces):
        print(" ",end="")
    for l in range(j,0,-1):
        print(l,end="")
    print()