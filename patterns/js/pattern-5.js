/**

*****
****
***
**
*

 */
let line=''
for(let i=1;i<=5;i++){
    for(let j=5;j>=i;j--){
        line+='*'
    }
    console.log(line);
    line=''
}