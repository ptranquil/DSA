/** Stock Buy And Sell */

arr = [7,1,5,3,6,4]

/** Brute Froce Approach */
function stocks(arr){
    profit = 0
    N=arr.length
    buy=sell=-1
    max=-Infinity
    for(let i=0;i<N;i++){
        for(let j=i;j<N;j++){
            if(max < (arr[j]-arr[i])){
                max = arr[j]-arr[i]
                buy=i
                sell=j
            }
        }
    }
    console.log(`Bus stock at ${arr[buy]} & sell at ${arr[sell]} with prifit of ${max}`)
}
stocks(arr)


/** Optimal Approach */
function stocksOptimal(arr){
    maxProfit = 0
    minPrice = Infinity
    for(let ele of arr){
        minPrice = Math.min(minPrice, ele)
        maxProfit = Math.max(maxProfit, ele-minPrice)
    }
    return maxProfit
}

console.log('The maxProfit is :',stocksOptimal(arr))
