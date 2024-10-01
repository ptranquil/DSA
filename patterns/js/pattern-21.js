/**

*****
*   *
*   *
*   *
*****

 */

let N=5;
let lines='';

for(let i=0;i<N;i++){
    // first or last element
    if(i === 0 || i === N-1){
        for(let j= 0;j<N;j++){
            lines+='*'
        }
    } else {
        lines+='*';
        for(let j=1;j<N-1;j++){
            lines+=' ';
        }
        lines+='*'
    }
    console.log(lines);
    lines=''
}