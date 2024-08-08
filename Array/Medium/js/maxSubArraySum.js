/** Maximum Subarray Sum in an Array
 * !Kadanes Algorithm
*/

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

/** Brute Force Approach */
function maxSubArraySum(arr) {
    let N = arr.length
    max = -Infinity
    for (let i = 0; i < N; i++) {
        sum = 0
        for (let j = i; j < N; j++) {
            sum += arr[j]
            if (sum > max) {
                max = sum
            }
        }
    }
    return max
}
console.log('The maximum subarray sum is : ', maxSubArraySum(arr))


/** Kadane Algorith
 * Using single loop, add the value to sum, find the max if sum > max
 * if sum < 0 : sum = 0
 */

function kadaneAlgo(arr) {
    sum = 0
    N= arr.length
    max = -Infinity
    for (let i = 0; i < N; i++) {
        sum += arr[i]
        max = (sum > max) ? sum : max
        if (sum < 0) {
            sum = 0
        }
    }
    return max
}
console.log('Kadane\'s Algorithm : ', kadaneAlgo(arr))

/** Using same kadane algorihtm to find the maximum sum of the subarray with the subarray */
function kadaneAlgoImprovised(){
    sum=0
    max=-Infinity
    start=0
    startIndex = endIndex = -1
    for(let i=0;i<arr.length;i++){
        if(sum == 0){
            start = i
        }
        sum+=arr[i]
        if(sum>max){
            max=sum
            startIndex=start
            endIndex = i
        }
        if(sum<0){
            sum=0
        }
    }
    console.log(startIndex, endIndex)
    return max
}
console.log('Kadane\'s Algorithm improvised : ', kadaneAlgoImprovised(arr))