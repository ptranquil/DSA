/** Brute Force */

function findMissingNumber(arr){
    for(let i=1;i<=arr.length;i++){
        if(!arr.includes(i)){
            return i
        }
    }
}

/** Another approaches
 * 1. Hashing and return the key which has 0 count
 * 2. count the sum  from 1 .. N using summation of N formula 2(N+1)/2 and calculate the sum of the array
 * & return totalSum - calculated Sum
 */
let arr = [1,2,3,5]
console.log('The missing number in array is ',findMissingNumber(arr))