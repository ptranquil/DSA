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

/** Another approach by making use of temp
 * store d element in temp
 * move remaining element at first
 * again move temp ele back to array
 */
function rotateArr(arr, d){
    let temp = []
    let N = arr.length
    for(let i=0;i<d;i++){
        temp[i] = arr[i]
    }

    for(let i=d;i<N;i++){
        arr[i-d] = arr[i]
    }
    
    for(let i=0;i<temp.length;i++){
        // arr[]
        arr[N-d+i] = temp[i]
    }
    console.log(arr)
}

/** 2 pointer approach using reverse , simplest and easiest and best*/
function rotatereverse(arr, d){
    let N = arr.length;
    d=d%N
    reverse(0, d-1, arr)
    reverse(d, N-1, arr)
    reverse(0,N,arr)
}

function reverse(start, end, arr){
    console.log(start,end,arr)
    while(start < end){
        [arr[start], arr[end]] = [arr[end], arr[start]]
        start++
        end--
    }
    return arr
}


arr = [1, 2, 3, 4, 5]
k = 4
leftRotate(arr, k)
console.log("Array after left rotation:", arr)