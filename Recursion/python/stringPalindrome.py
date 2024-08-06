#using brute force
def stringPalindrome(str):
    new=''
    for i in range(len(str)-1,-1,-1):
        new+=str[i]
    return str == new

#using two pointer approach
def stringPalindromeTwoPointer(str):
    start = 0
    end=len(str)-1
    while start <end:
        if(str[start] != str[end]):
            return False
        else:
            start+=1
            end-=1
    return True

#using Recusrion
def stringPalindromeRec(i,str):
    if(i>len(str)//2):
        return True
    if(str[i] != str[len(str) - 1 - i]):
        return False
    return stringPalindromeRec(i+1,str)

if __name__ == "__main__":
    print(stringPalindrome("abhgfghba"))
    print(stringPalindromeTwoPointer("abhgfghba"))
    print(stringPalindromeRec(0,"abhgfghba"))