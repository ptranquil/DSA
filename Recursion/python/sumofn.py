def sumOfNNumber(sum,n):
    while(n!=0):
        sum+=n
        n-=1
        return sumOfNNumber(sum,n)
    return sum

def sumOfN(n):
    return n*(n+1)//2

if __name__ == '__main__':
    print("The sum is :",sumOfNNumber(0,10))
    print("The sum is :",sumOfN(10))