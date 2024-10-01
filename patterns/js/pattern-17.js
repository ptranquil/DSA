/**

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDBCA
 */

let N=5;
let line=''
let rowMid;
for(let i=0;i<N;i++){
    for(let j=0;j<N-i;j++){
        line+=' '
    }
    for(let j=0;j<i+1;j++){
        line+= String.fromCharCode(65+j);
        rowMid=j-1;
    }
    for(let j=0;j<i;j++){
        line+= String.fromCharCode(65+rowMid);
        rowMid-=1;
    }
    // for(let j=0;j<N-i;j++){
    //     line+='1'
    // }
    console.log(line);
    line=''
}