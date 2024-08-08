/** Two Sum : Check if a pair with given sum exists in Array */
arr = [2,6,5,8,11]
target = 14
/** 
 * Brute Force
 * TC: O(N)^2
 * SC: O(1)
 *  */
function calculate2Sum(arr, target){
    let N = arr.length
    for (let i=0;i<N;i++){
        for( let j=i;j<N;j++){
            if((arr[i] + arr[j]) == target){
                return `YES : ${arr[i]},${arr[j]}`
            }
        }
    }
    return 'NO'
}
console.log('Brute Froce:: ',calculate2Sum(arr,target))


/** 
 * Using hashing & reverse mathematics
 * Calculating the remaining = target - currentElement, if that exist in hashMap means we got 2 sum
 * else store the current element in hashmap {element: key} 
 * SC: O(N)
 * TC: O(N)
 *  */
function calculate2SumOp(arr, target){
    let hashMap = {}
    for(let i=0;i<arr.length;i++){
        let rem = target - arr[i]
        if(hashMap[rem]){
            return `YES : ${rem},${arr[i]}`
        }
        hashMap[arr[i]] = i
    }
    console.log(hashMap)
    return 'NO'
}
console.log('Using Hashing :: ',calculate2SumOp(arr,target))


/** 
 * Using 2 pointers
 * Required the array to be sorted. Here we are sorting the array first
 * TC: O(N)
 * SC: O(NlogN)
 *  */

function calculate2Sum2P(arr,target){
    let N = arr.length
    let left = 0;
    let right = N-1;
    arr = arr.sort((a,b) => a-b)

    while(left < right ){
        let sum = arr[left] + arr[right]
        if (sum == target){
            return `YES : ${arr[left], arr[right]}`
        } else if (sum > target){
            right--
        } else {
            left++
        }
    }
    return 'NO';
}
console.log('Using 2 pointers :: ',calculate2SumOp(arr,target))