'''
*****
****
***
**
*
'''

n=5
for i in range(n):
    for j in range(n,i,-1):
        print('*',end="")
    print()

for i in range(n,-1,-1):
    print('*'*i)