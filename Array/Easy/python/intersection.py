#find intersection of 2 sorted array
a = [1,1,2,3,4,5]
b = [2,3,4,4,5,6]

'''
bruteForce
TC: O(n1 *  n2)
SC: O(n2)
'''
intersection1=[]
visited = [0]*len(b)
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] == b[j] and visited[j] == 0):
            intersection1.append(a[i])
            visited[j]=1
            break
        elif b[j] > a[i]: break

print(intersection1)


#optimal approach
intersection=[]
i =0
j=0
while(i<len(a) and j < len(b)):
    if a[i] < b[j]:
        i+=1
    if a[i] > b[j]:
        j+=1
    elif(a[i] == b[j]):
        intersection.append(a[i])
        i+=1
        j+=1
print(intersection)


