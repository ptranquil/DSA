function leftRotate(arr,k){
    k = k%arr.length
    if(k == arr.length){
        return arr
    }
    while(k>0){
        reverse(arr)
        k--
    }
    return arr
}

function reverse(arr){
    let temp = arr[0]
    let i=0
    while(i<arr.length-1){
        arr[i] = arr[i+1]
        i++
    }
    arr[i] = temp
    return arr
}

arr = [1, 2, 3, 4, 5]
k = 4
leftRotate(arr, k)
console.log("Array after left rotation:", arr)