/** 
 * Brute force approach 
 * It can be used for all the array types
 * TC: O(N)
 * SC: O(N)
 * */
function removeDup(arr){
    let hashMap = {}
    for (let ele of arr){
        if (hashMap[ele]){
            hashMap[ele]++
        } else {
            hashMap[ele]=1
        }
    }
    console.log('Array after removing duplicate element is :',Object.keys(hashMap))
}
// Object.keys returns array of keys

arr=[1,2,3,3,4,4,5,5,6]
removeDup(arr)

/** 
 * Another Method
 * Useful for doing modification on the same array
 * TC: O(N)
 * SC: O(1)
 *  */
function removeDuplicate(arr){
    /** As the Array is sorted */
    let i=0
    for(let j=1;j<arr.length;j++){
        if(arr[i] != arr[j]){
            i++
            arr[i] = arr[j]
        }
    }
    arr.length=i+1
    console.log(arr)
}

arr=[1,2,3,3,4,4,5,5,6]
removeDuplicate(arr)