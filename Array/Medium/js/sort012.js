/** Sort an array of 0s, 1s and 2s without using inbuilt sort method*/
arr = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

/** Brute Force Approach 
 * 1. using sort() method : Not applicable here but can be used tod get the solution
 * 2. by counting the occurence of 0,1,2 and reinserting it in the array   
 * TC: O(2N)
 * SC: O(1)
 * */

function sort(arr){
    let zeros = ones = twos = 0
    for(let ele of arr){
        if(ele === 0) zeros++
        else if(ele === 1) ones++
        else twos++
    }
    for (let i=0;i<zeros;i++){
        arr[i] = 0
    }
    for (let i=zeros;i<(zeros + ones);i++){
        arr[i] = 1
    }
    for (let i=(zeros + ones);i<(zeros + ones + twos);i++){
        arr[i] = 2
    }
    console.log('Array sorting using count method :: ',arr)
}
sort(arr)


/** Using 3 pointers approach OR
 * !Dutch National Flag Algorithm 
 * */
function sortDNFA(arr){
    let N = arr.length
    let low = mid = 0
    let high = N-1
    while(mid<=high){
        if(arr[mid] == 0){
            [arr[low],arr[mid]] = [arr[mid],arr[low]]
            mid++
            low++
        }
        else if(arr[mid] == 1){
            mid++
        } else {
            [arr[mid],arr[high]] = [arr[high],arr[mid]]
            high--
        }
    }
    console.log('Array sorting using DNFA method :: ',arr)
}
sortDNFA(arr)
