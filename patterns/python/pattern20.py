'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    spaces = 2*(n-1)-2*i
    for j in range(spaces):
        print(" ",end='')
    for j in range(i+1):
        print('*',end='')
    print()
n=n-1
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    spaces = 2*(i+1)
    for j in range(spaces):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    print()