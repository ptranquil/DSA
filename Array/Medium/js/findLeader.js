/** 
 * Leaders in an Array 
 * Problem Statement: Given an array, print all the elements which are leaders. 
 * A Leader is an element that is greater than all of the elements on its right side in the array.
 * */
arr = [4, 7, 1, 0]

/** Brute Force
 * TC: O(N^2)
 * SC: O(N)
*/
function findLeader(arr) {
    N = arr.length
    leaders = []
    for (let i = 0; i < N; i++) {
        isLeader = true
        for (let j = i + 1; j < N - 1; j++) {
            if (arr[i] <= arr[j]) {
                isLeader = false
            }
        }
        if (isLeader) {
            leaders.push(arr[i])
        }
    }

    console.log('The leaders are : ', leaders)
}
findLeader(arr)

/**
 * Optimal Approach
 * Staring from reverse
 * TC: O(N)
 * SC: O(N)
 */
arr = [4, 7, 1, 0]
function findLeaderOpt(arr) {
    N = arr.length
    leaders = []
    max = arr[N - 1]
    leaders.push(arr[N - 1])
    for (let i = N - 2; i >= 0; i--) {
        if (arr[i] > max) {
            leaders.push(arr[i])
            max = arr[i]
        }
    }
    console.log('Optimal Approach:: The leaders are : ', leaders)
}
findLeaderOpt(arr)
