'''
A
AB
ABC
ABCD
ABCDE
'''

n=5
start=65
for i in range(n):
    for j in range(i+1):
        print(chr(start+j),end=' ')
    print()