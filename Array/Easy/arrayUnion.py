#make array uinon of two sorted array
def unionArray(arr1,arr2):
    temp = set()
    res=[]
    for i in range(0,len(arr1)):
        temp.add(arr1[i])
    
    for i in range(0,len(arr2)):
        temp.add(arr2[i])
    
    for i in temp:
        res.append(i)
    return res

# arr1=[1,2,3,4,5]
# arr2=[5,6,7]
# print(unionArray(arr1,arr2))

def unionOptimize(arr1,arr2):
    i,j=0,0
    union=[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else :
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
    
    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1

    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return union
   
        
arr1=[1,2,3,4,5]
arr2=[5,6,7]
print(unionOptimize(arr1,arr2))