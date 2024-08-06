def palindrome(N):
    rev=0
    num=N
    while(num!=0):
        rem = num%10
        rev = rev*10 + rem
        num//=10
    return rev == N

if __name__ == "__main__":
    N=1213
    if(palindrome(N)):
        print(N,"is palindrome")
    else:
        print(N,"is not a palindrome")