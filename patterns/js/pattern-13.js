/**

1        1
12      21
123    321
1234  4321
1234554321

 */

let line= '';
let N=9;
let end;
for(let i=1;i<=N;i++){
    for(let j=1;j<=i;j++){
        line+=`${j}`;
        end=j
    }
    let spaces = 2*(N-i);
    if(spaces){
        for(let j=0;j<spaces;j++){
            line+=' '
        }
    }

    for(let j=end;j>=1;j--){
        line+=`${j}`;
        end=''
    }
    console.log(line);
    line='';
    end=''
}