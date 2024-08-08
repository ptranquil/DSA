/** Array Union */

let arr1=[1,2,3,4,5]
let arr2=[5,6,7]

function unionArray(arr1, arr2){
    for (let i=0;i<arr2.length;i++){
        if (!arr1.includes(arr2[i])){
            arr1.push(arr2[i])
        }
    }
    return arr1;
}

console.log(unionArray(arr1,arr2))