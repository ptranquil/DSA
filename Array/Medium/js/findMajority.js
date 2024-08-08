/** Find the Majority Element that occurs more than N/2 times 
 * !Moores Vorting Algorithm
*/

arr = [1, 1, 1,1,1,1, 1,1,1, 3, 3, 5, 6, 8, 4, 3, 8, 1]

/** 
 * Brute Force: Naives Approach
 * TC: O(N) * (O2N) = O(N^2)
 * SC: O(N) if we use done, removing it will reduce the space complexity by O(1), TC remains O(N^2)
 *  */
function findMajortiy(arr) {
    let N = arr.length
    let done = []
    for (let i = 0; i < N; i++) {
        if (!done.includes(arr[i])) {
            done.push(arr[i])
            let cnt = 0
            for (let j = 0; j < N; j++) {
                if (arr[i] == arr[j]) {
                    cnt++
                }
            }
            if (cnt > N / 2) {
                return arr[i]
            }
        }
    }
}
console.log('BruteForce: The element that occurs more then N/2 times is :', findMajortiy(arr))


/** 
 * Using Hashing
 * TC: =~ O(2N)
 * SC: O(N)
 *  */
function findMajorityHash(arr) {
    let hashMap = {}
    let N = arr.length
    let majority
    for (ele of arr) {
        if (hashMap[ele]) {
            hashMap[ele]++
        } else {
            hashMap[ele] = 1
        }
    }
    console.log(hashMap)
    Object.keys(hashMap).forEach(ele => {
        if (hashMap[ele] > (N / 2)) {
            majority = ele
        }
    })
    return majority
}
console.log('Hashing: The element that occurs more then N/2 times is :', findMajorityHash(arr))

/** 
 * Using Moores Voting Algorithm
 * TC: O(N)
 * SC: O(1)
 *  */
function findMajority(arr) {
    let cnt = 0
    let curr
    for (let ele of arr) {
        if (cnt == 0) {
            curr = ele
            cnt++
        } else if (curr == ele) {
            cnt++
        } else {
            cnt--
        }
        return ele
    }
}
console.log('MVA: The element that occurs more then N/2 times is :', findMajortiy(arr))