/**

A
BB
CCC
DDDD
EEEEE
 */

let N=5;
let line='';
for(let i=0;i<N;i++){
    for(let j=0;j<=i;j++){
        line+=String.fromCharCode(65+i)
    }
    console.log(line)
    line=''
}