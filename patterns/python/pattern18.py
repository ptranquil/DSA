'''
E
ED
EDC
EDCB
EDCBA
'''


n=5
for i in range(n):
    start=65+n-1
    for j in range(0,i+1):
        print(chr(start),end='')
        start-=1
    print()