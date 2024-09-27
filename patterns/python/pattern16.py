'''
A
BB
CCC
DDDD
EEEEE
'''

n=5
start=65
for i in range(5):
    for j in range(i+1):
        print(chr(start+i), end=" ")
    print()