/**

*********
 *******
  *****
   ***
    *

 */

let line = '';
let N=50;
for(let i=N;i>0;i--){
    for(let j=0;j<N-i;j++){
        line+=' '
    }
    for(let j=0;j<2*i-1;j++){
        line+='*';
    }
    for(let j=0;j<N-i;j++){
        line+=' '
    }
    console.log(line);
    line=''
}