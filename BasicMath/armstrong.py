def checkArmstrong(n):
    digit=0
    num=n
    while(num!=0):
        num//=10
        digit+=1
    
    num=n
    sum=0
    while(num!=0):
        rem = num%10
        sum+=rem**digit
        num//=10
    return sum == n

if __name__ == "__main__":
    print(checkArmstrong(153))