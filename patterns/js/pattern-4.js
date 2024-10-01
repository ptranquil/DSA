/**

1
22
333
4444
555555

 */
let line=''
for(let i=1;i<=5;i++){
    for(let j=1;j<=i;j++){
        line+=`${i}`
    }
    console.log(line);
    line=''
}