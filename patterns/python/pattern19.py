'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

n=5
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    spaces = 2*i
    for j in range(spaces):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    spaces=2*(n-1)-2*i
    for j in range(spaces):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

print('\n\n\n\n\n')
# Optamized way
# Upper half
for i in range(n, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

# Lower half
for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)