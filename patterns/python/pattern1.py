'''
*****
*****
*****
*****
*****

'''
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print('')

#optimized approach
for i in range(n):
    print("* " * n)
