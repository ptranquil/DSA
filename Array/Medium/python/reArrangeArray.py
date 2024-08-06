#Rearrange Array Elements by Sign
"""
Brute Force
Time Complexity : O(N) + O(N) = O(2N)
Space Complexity : O(N/2) + O(N/2) = O(N)
"""
def reArrange(arr):
    pos = []
    neg = []
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    a = 0
    for i in range(len(pos)):
        arr[2 * i] = pos[i]
        arr[2 * i + 1] = neg[i]
    print(arr)
reArrange([1,2,-4,-5])

"""
Better approach using 2 pointers
Time Complexity : O(N)
Space Complexity : O(N)
"""
def reArrange2(arr):
    pos=0
    neg=1
    temp = [0]*len(arr)
    for i in range(0,len(arr)):
        if arr[i] > 0:
            temp[pos] = arr[i]
            pos+=2
        else:
            temp[neg]=arr[i]
            neg+=2
    print(temp)

reArrange2([1,2,-4,-5])


"""
Variety-2
Where lengt of positive and negative numbers ae not equal so we put make the alternate chain fo positive and negative and then we will put the remaining numbers at the end of the array
Time Complexity : O(N) + O(N) = O(2N)
Space Complexity : O(N/2) + O(N/2) = O(N)
"""

def diff(arr):
    pos=[]
    neg=[]
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    #if pos > neg then take the length of neg to be filled first for alternate position & then we will fill the remaining pos element at the end
    if (len(pos) > len(neg)):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        for i in range(len(neg)*2,len(arr)):
            arr[i] = pos[i-len(neg)]
    #eld if neg > pos then take the length of pos to be filled first for alternate position & then we will fill the remaining neg element at the end
    else:
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        for i in range(len(pos)*2,len(arr)):
            arr[i] = neg[i-len(pos)]
    print(arr)

diff([-1, -2, -4, -5, 3, 4])