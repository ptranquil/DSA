function findLargestElementInArray(arr){
    // return Math.max(...arr)
    // return arr.sort((a,b) => a-b)[arr.length-1]
    max = arr[0]
    sL = arr[1] // To get the second largest element in the Array
    for(i of arr){
        if(max < i) {
            sL = max
            max = i
        }
    }
    return [max, sL]
}

arr = [1,2,3,4,5]
const [largest, secondLargest] = findLargestElementInArray(arr) 
console.log(`The largest element in the array is ${largest} and Second Largest is : ${secondLargest}`)
