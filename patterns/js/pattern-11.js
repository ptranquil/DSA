/**

1
01
101
0101
10101

 */
let line=''
let numRow= 0;
for(let i=1;i<=5;i++){
    let numCol = numRow ? 0: 1;
    for(let j=1;j<=i;j++){
        line+=`${numCol}`;
        numCol = numCol ? 0 : 1;
    }
    console.log(line);
    line='';
    numRow = numRow ? 0 : 1;
}

(function(){
    console.log("Hello")
})()