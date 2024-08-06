# Count digits in a number

# Brute Force Approach: divide by 10 & increment the counter
import math


n = 12345
def countDigit(n):
    count = 0
    while(n>0):
        count+=1
        n = n//10
    return count

print("(BFA) The count in ",n,"is : ",countDigit(n))


# Using log to the base 10
def countDigitOA(n):
    return int(math.log(n)+1)
n = 12345
print("(OA) The count in ",n,"is : ",countDigit(n))
