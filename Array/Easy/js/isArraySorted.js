function isArraySorted(arr){
    for(let i=0;i<arr.length;i++){
        if(arr[i]>arr[i+1]){
            return false;
        }
    }
    return true
}

arr = [1,2,3,4,3,5]
if(isArraySorted(arr)){
    console.log("The array is sorted")
} else{
    console.log("The array is not sorted")
}