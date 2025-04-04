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

/** Using set DS */
function unionSet(a,b){
    let set = new Set();
    for(let val of a){
        set.add(val)
    }
    for(let val of b){
        set.add(val)
    }

    // let itr = set.entries();
    // for(let i=0;i<set.size();i++){

    // }
    console.log(set)
}

/** Using 2 pointer approach */
function union2P(a, b){
    let N1 = a.length;
    let N2 = b.length;
    let i = 0;
    let j=0;
    let union = []
    while(i<N1 && j<N2){
        if(a[i] <= b[j]){
            if(union.length == 0 || union[union.length-1] != a[i]) {
                union.push(a[i])
            }
            i++;
        } else if (a[i] >= b[j]){
            if(union.length == 0 || union[union.length-1] != b[j]) {
                union.push(b[j])
            }
            j++;
        }        
    }

    while(i<N1){
        if(union.length == 0 || union[union.length-1] != a[i]) {
            union.push(a[i])
        }
        i++;
    }

    while(j<N2){
        if(union.length == 0 || union[union.length-1] != b[i]) {
            union.push(b[i])
        }
        j++;
    }
    console.log(union)
}

console.log(unionArray(arr1,arr2))