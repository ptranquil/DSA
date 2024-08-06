import math;

def allDivisor(n):
    for i in range(1,n+1):
        if(n%i == 0):
            print(i)

def allDivisorOptimal(n):
    for i in range(1, int(math.sqrt(n))+1):
        if(n%i == 0):
            print(i)
            if(i != n/i):
                print (n//i)

allDivisor(6)
print("Using optimal solution")
allDivisorOptimal(6)