def frequency(arr):
    freq = {}
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
        
        if max < freq[i]:
            max = i
        if min > freq[i]:
            min = i
    
    print(freq)
    print(max)
    print(min)

arr = [10,10,15,10,12,12,13]
frequency(arr)