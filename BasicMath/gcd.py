def findgcd(a,b):
    result = 1
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0):
            result = i
    return result

def gcdOptimal(a,b):
    if(b==0):
        return b
    else:
        return(gcdOptimal(b,a%b))


if __name__ == '__main__':
    num1=81
    num2=27
    print("The GCD of",num1,"and",num2,"is :",findgcd(num1,num2))
    print("The GCD of",num1,"and",num2,"using optimal solution is :",findgcd(num1,num2))
    