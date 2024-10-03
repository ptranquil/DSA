# The GCD of two numbers is the largest number that divides both of them without leaving a remainder. 

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


# Using Eucledean Algorithm
# The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers. 
# It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.

def gcdEA(a,b): 
    if a == 0: return b
    if b == 0: return a
    newNumber = max(a,b) - min(a,b)
    return gcdEA(newNumber, min(a,b))

if __name__ == '__main__':
    num1=81
    num2=27
    print("The GCD of",num1,"and",num2,"is :",findgcd(num1,num2))
    print("The GCD of",num1,"and",num2,"using optimal solution is :",findgcd(num1,num2))
    print("The GCD of",num1,"and",num2,"using Euclidean Algorithm is :",gcdEA(num1,num2))
    