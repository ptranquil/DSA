function maxConsNums(arr){
    max = 0
    curr = 0
    for (let i of arr){
        if(i == 1){
            curr++
        } else {
            max = Math.max(max,curr)
            curr =0
        }
    }
    return max
}

function putAtz(arr){
    let N =arr.length;
    let j=-1;
    for(let i=0;i<N;i++){
        if(arr[i]==0){
            j= i;
            break;
        }
    }

    for(let i=j+1;i<N;i++){
        if(arr[i] != arr[j]){
            [arr[i], arr[j]] = [arr[j], arr[i]]
            j++
        }
    }

    console.log(arr)
}


arr = [1,1,1,1,1,1,1,1,1,4,5,1,1,1,4,3,1,1,1,1,1,5]
console.log("The maximum consecutive 1's is :",maxConsNums(arr))