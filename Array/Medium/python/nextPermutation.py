'''
next_permutation : find next lexicographically greater permutation
Brute Force
TC: O(N * N!)
SC: O(N)
'''
def permute(arr):
    result = []

    # Base case: if the array is empty, return an empty list of list
    if len(arr) == 0:
        return [[]]

    for i in range(len(arr)):
        # Extract the current element
        current_element = arr[i]

        # Get the remaining elements by slicing
        remaining_elements = arr[:i] + arr[i+1:]
        # print('remaining_elements ', remaining_elements)

        # Recursively generate permutations of the remaining elements
        remaining_permutations = permute(remaining_elements)
        print('remaining_permutations ',arr[i] , remaining_permutations)

        # Add the current element to each of the remaining permutations
        for perm in remaining_permutations:
            result.append([current_element] + perm)
        print('result',result)

    return result

# Example usage:
array = [1, 2, 3]
permutations = permute(array)
for p in permutations:
    print(p)

'''
Optimal Approach

TC: O(3N) (1- for the breakpoint, 2- for the swap, 3 for the reversal)
SC: O(1)
'''
def findNextPermutation(a):
    n=len(a)
    breakpoint=  -1
    for i in range(n-2,-1, -1):
        if a[i] < a[i+1]:
            breakpoint=i
            break
    
    if breakpoint == -1:
        # reverse the whole array:
        a.reverse()
        return a
    
    for i in range(n-1, breakpoint, -1):
        if a[i] > a[breakpoint]:
            a[breakpoint], a[i] = a[i], a[breakpoint]
            break
    
    a[breakpoint+1:] = reversed(a[breakpoint+1:])

    return a

a = [1,3,2]
ans = findNextPermutation(a)

print("The next permutation is: [", end="")
for it in ans:
    print(it, end=" ")
print("]")