/**

A
AB
ABC
ABCD
ABCDE
 */

let N=26;
let line='';
for(let i=0;i<N;i++){
    for(let j=0;j<=i;j++){
        line+=String.fromCharCode(65+j)
    }
    console.log(line)
    line=''
}