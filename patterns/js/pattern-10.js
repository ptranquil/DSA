/**

*
**
***
****
*****
****
***
**
*

 */
let line=''
let N=5
for(let i=0;i<N;i++){
    for(let j=0;j<=i;j++){
        line+='*'
    }
    console.log(line);
    line=''
}
for(let i=N-2;i>=0;i--){
    for(let j=0;j<=i;j++){
        line+='*'
    }
    console.log(line);
    line=''
    
}