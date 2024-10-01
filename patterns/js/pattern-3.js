/**

1
12
123
1234
12345

 */
let line=''
for(let i=1;i<=5;i++){
    for(let j=1;j<=i;j++){
        line+=`${j}`
    }
    console.log(line);
    line=''
}