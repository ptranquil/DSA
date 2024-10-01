'''
Name as 'Alpha Hill'

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''

n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    start = 65
    breakpoint = i+1
    for j in range(1,breakpoint):
        print(chr(start),end='')
        start+=1
    for j in range(breakpoint,0,-1):
        print(chr(start),end='')
        start-=1
    print()

'''
Approach followed here is
1. Printing the starting spaces (4->3->2->1->0)
2. Creating the breakpoint from where we need to print reverse
3. print the starting character
4. printing the character after the breakpoint
'''