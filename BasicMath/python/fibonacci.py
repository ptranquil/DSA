n=10
if n==0:
    print('0',end='')
else:

    secondLast=0
    last=1
    print(secondLast, last, end=', ')
    for i in range(2,n):
        newEle = secondLast+last
        secondLast = last
        last = newEle
        print(newEle,end=', ')
    print()