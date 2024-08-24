/** Given a non-empty array of integers arr, every element appears twice except for one. Find that single one. */

/** Using hasing and then looping over the hash to find the element having count = 1 */
function findOnes(arr){
    let hashmap = {};
    let res
    for (let i of arr){
        if(hashmap[i]){
            hashmap[i]++
        } else {
            hashmap[i] = 1;
            ele = i
        }
    }
    Object.keys(hashmap).forEach(key => {
        if (hashmap[key] == 1) {
            res = key;
            return key
        }
    })
    return res
}

/** 
 * Using XOR 
 * This metod will not be applicable for the array element having count of other element more than 2
 * */
function findOneXor(arr){
    let xor
    for(let i of arr){
        xor = xor ^ i
    }
    return xor
}


arr = [1,1,2,2,3,3,4,5,5,6,6,9,9]
console.log("The number that appear ones is ",findOnes(arr))
console.log("The number that appear ones using XOR is ",findOneXor(arr))