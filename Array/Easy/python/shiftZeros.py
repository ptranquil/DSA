def shiftZerostoEnd(arr):
    i=0
    while(i<len(arr)-1):
        if arr[i]==0:
            j=i+1
            while j<len(arr)-1 and arr[j] == 0:
                j+=1
            arr[i],arr[j] = arr[j],arr[i]
        i+=1

arr= [1,0,4,0,0,3,5,6,20,0]
shiftZerostoEnd(arr)
print(arr)


#optimal solution
'''
TC: O(N)
SC: O(1)
'''
arr= [1,0,4,0,0,3,5,6,20,0]
n = len(arr)
# O(X)
for i in range(n):
    if(arr[i] == 0):
        j=i
        break
#O(N-X)
for i in range(j+1,n):
    if(arr[i]!=0):
        arr[i],arr[j] = arr[j], arr[i]
        j+=1
print(arr)