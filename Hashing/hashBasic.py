#Brute force approch to find the existence of arr2 values in arr1
def basicHashing(arr, arr2):
    hash={}

    def getCount(arr, val):
        count=0
        for i in range (0,len(arr)):
            if arr[i] == val:
                count+=1
        return count

    for i in range(0,len(arr2)):
        count = getCount(arr,arr2[i])
        hash[arr2[i]] = count
    return hash

def hashingChar(str,arr):
    char_count={}
    for char in arr:
        char_count[char]=0
    
    for char in str:
        if char in char_count:
            char_count[char] += 1
    return char_count

# ord() function return the unicode value of the characters
def hashingUnicode(str, arr):
    res = [0] * 26

    # preallocating and storing
    for i in str:
        print(ord(i) - ord('a'))
        res[ord(i) - ord('a')] +=1
    
    for i in arr:
        print(i,"appears",res[ord(i) - ord('a')],"times")
    
if __name__ == "__main__":
    arr1 = [1,1,5,3,2,1]
    arr2 = [0,1,2,3,4,5]
    print(basicHashing(arr1,arr2))

    hashingChar('abcbdbcs', ['a','b','c','e'])

    hashingUnicode('abcbdbcs', ['a','b','c','e'])




