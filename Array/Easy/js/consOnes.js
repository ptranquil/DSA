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

arr = [1,1,1,1,1,1,1,1,1,4,5,1,1,1,4,3,1,1,1,1,1,5]
console.log("The maximum consecutive 1's is :",maxConsNums(arr))