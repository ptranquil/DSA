/**

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

 */

let N=5;
let line = ''
let res = 1;
for(let i=0;i<N;i++){
    for(j=0;j<=i;j++){
        line += `${res} `;
        res+=1
    };
    console.log(line);
    line='';
}