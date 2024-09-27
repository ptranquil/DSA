'''
1
22
333
4444
555555
'''

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()


for i in range(1,n+1):
    print(str(i)*i)