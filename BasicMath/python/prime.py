
import math
def prime(N):
    if(N==1):
        return False
    for i in range(2,int(math.sqrt(N))):
        if(N%i == 0):
            return False
    return True

if __name__=="__main__":
    N=123
    if(prime(N)):
        print(N,"is prime")
    else:
        print(N,"is not prime")
