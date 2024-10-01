/**

E
ED
EDC
EDCB
EDCBA

 */

let N = 5;
let lines='';

for(let i=0;i<N;i++){
    for(let j=0;j<=i;j++){
        lines+= String.fromCharCode(65+(N-j-1))
    }
    console.log(lines);
    lines=''
}