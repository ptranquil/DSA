/**

12345
1234
123
12
1

 */
let line=''
for(let i=5;i>=1;i--){
    for(let j=1;j<=i;j++){
        line+=`${j}`
    }
    console.log(line);
    line=''
}