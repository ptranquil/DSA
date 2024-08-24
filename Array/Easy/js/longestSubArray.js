/**
 * 
 * Brute Force Approach
 * Finding all the subarray using 2 nested loop and calculating sum for the sub array 
 * find the max length if the sum == k  
 */

// arr = [1,2,3,1,1,1,1]
arr = [2,0,0,0,0,3]
k = 3

function findMaxSubArray(arr, k) {
    let maxLength = 0;
    for (let i = 0; i < arr.length; i++) {
        for (let j = i; j < arr.length; j++) {
            s=0
            for(let K=i;K<=j;K++){
                s+=arr[K]
            }
            if(s==k){
                maxLength = Math.max(maxLength, j-i+1)
            }
        }
    }
    console.log(`findMaxSubArray : The Longest Subarray with sum ${k} is : ${maxLength}`);
}
findMaxSubArray(arr,k)

/** Using two loops */
function findMaxSubArray2(arr, k) {
    let maxLength = 0;
    for (let i = 0; i < arr.length; i++) {
        s=0
        for (let j = i; j < arr.length; j++) {
            s+=arr[j]
            if(s==k){
                maxLength = Math.max(maxLength, j-i+1)
            }
        }
    }
    console.log(`findMaxSubArray2 : The Longest Subarray with sum ${k} is : ${maxLength}`);
}

findMaxSubArray2(arr,k)


/**
 * !#####################IMPORTANT#############################
 * Using hashing + Prefix sum and reverse mathematics
 * !This is an optimal solution if the array contains positive, negative or zeros
 */
function findSubArrOptimize(arr,k){
    let hashMap ={}
    let maxLen = 0
    let sum = 0
    for(let i=0;i<arr.length;i++){
        /** Calculating the prefix */
        sum+=arr[i]

        /** COnsidering the length if sum == k */
        if(sum ==k){
            maxLen = Math.max(maxLen,i+1)
        }

        /** Findind the remaining part which if exist signifes that there exist an another subaaray */
        let rem = sum-k
        if(hashMap[rem]){
            let newlen = i+1-hashMap[rem]
            maxLen = Math.max(newlen,maxLen)
        }

        /** Inserting the current sum as key and index as value to the map, for further processing */
        if(!hashMap[sum]){
            hashMap[sum] = i
        }
    }
    console.log(`findSubArrOptimize : The Longest Subarray with sum ${k} is : ${maxLen}`);
}
arr = [1,1,1,1,1,4,5,3,3,2,5,6,7,7,7,8,8,8,8,8,8,8,8,8,8,8]
k=64
findSubArrOptimize(arr,k)


/** 
 * !Using 2 pointers approach more optimized than the above code
 * Almost related to the sliding window algo + prefix Sum
 * starting from the 0th index & calculating the sum
 * if sum == k , storing the length
 * if sum exceeds the value of k, then decrement from the left, and simultaneously checking the value
 * if the value == k, and greater than the previous value, then updating the maxLength
 * !This solution is optimal for the array containing postives and zeros
 */

function findSubArr(arr,k){
    let left = 0
    let right = 0
    let maxLength = 0
    let sum = 0
    let n = arr.length
    while(right < n){
        while(sum > k && left <= right){
            sum -= arr[left]
            left++
        }
        if(sum == k){
            maxLength = Math.max(maxLength, right-left+1)
        }
        right++
        if (right < n){
            sum+=arr[right]
        }
    }
    console.log(`findSubArrOptimize : The Longest Subarray with sum ${k} is : ${maxLength}`);
}
findSubArr(arr,k)