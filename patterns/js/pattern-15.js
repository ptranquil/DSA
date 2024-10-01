/**

ABCDE
ABCD
ABC
AB
A

 */

let N=5;
let line='';
for(let i=N;i>0;i--){
    for(let j=0;j<=i;j++){
        line+=String.fromCharCode(65+j)
    }
    console.log(line)
    line=''
}