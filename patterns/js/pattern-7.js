/**

    *
   ***
  *****
 *******
*********
 */
let N=10;
let line=''
for(let i=0;i<N;i++){
    for(let j=0;j<N-i;j++){
        line+=' '
    }
    for(let j=0;j<(2*i+1);j++){
        line+='*'
    }
    for(let j=0;j<N-i;j++){
        line+=' '
    }
    console.log(line);
    line=''
}