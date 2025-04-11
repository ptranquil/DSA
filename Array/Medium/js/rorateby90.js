/** Rotate Matrix by 90 degrees */

function matrix90(arr){
    let rows = arr.length
    let cols = arr[0].length


    /** Creating the dummy matrix */
    let newArr = []
    for(let i = 0; i < cols; i++) {
        newArr[i] = new Array(rows).fill(0)
    }


    /** putting the data in dummyMatrix in 90 format */
    r=0
    for(let j=0;j<cols;j++){
        c=0
        for(let i=rows-1;i>=0;i--){
            newArr[r][c] = arr[i][j]
            c++
        }
        r++
    }

    /** Reinseerting the data for inplace operation */
    for(let i=0;i<rows;i++){
        for(let j=0;j<cols;j++){
            arr[i][j] = newArr[i][j]
        }
    }

    console.log(arr)
    return arr
}

arr = [[1,2,3],[4,5,6],[7,8,9]]
// let arr = [[1,2],[3,4],[5,6]]
// let arr = [[1,2,3,4],[5,6,7,8]]
matrix90(arr)