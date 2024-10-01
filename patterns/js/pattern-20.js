/**

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

 */

let line= '';
let N=5;
let end;
for(let i=1;i<=N;i++){
    for(let j=1;j<=i;j++){
        line+='*';
        end=j
    }
    let spaces = 2*(N-i);
    if(spaces){
        for(let j=0;j<spaces;j++){
            line+=' '
        }
    }
    for(let j=1;j<=i;j++){
        line+='*';
    }
    console.log(line);
    line='';
    end=''
}

for(let i=2;i<=N;i++){
    for(let j=i;j<=N;j++){
        line+=`*`;
        end=j
    }
    let spaces = 2*i-2;
    if(spaces){
        for(let j=0;j<spaces;j++){
            line+=' '
        }
    }
    
    for(let j=i;j<=N;j++){
        line+=`*`;
        end=''
    }
    console.log(line);
    line='';
    end=''
}