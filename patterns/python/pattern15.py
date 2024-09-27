'''
ABCDE
ABCD
ABC
AB
A
'''

n=5
start=65
for i in range(n,0,-1):
    for j in range(0,i):
        print(chr(start+j),end=' ')
    print()