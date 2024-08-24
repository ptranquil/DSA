#Stock Buy And Sell

def stock(arr):
    P = 0
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            P = max(arr[j] - arr[i], P)
    print(P)

def stockTwoP(arr):
    left = right = 0
    P = 0
    n = len(arr)
    while(left < n and right < n) :
        cP =  arr[right] - arr[left] 
        if cP > 0:
            P = max (cP,P)
            right+=1
        elif cP==0:
            right+=1
        else:
            left+=1
            right+=1
    print(P)
arr = [7,1,5,3,6,4]
stockTwoP(arr)

#another optimal approach
def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)