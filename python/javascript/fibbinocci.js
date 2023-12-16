function fibonacci(n) 
{
  let fibonacciseries=[0,1];
    for (let i=2;i<n;i++)
        {
            fibonacciseries[i]=fibonacciseries[i-1]+fibonacciseries[i-2]
        }
    return fibonacciseries;
}
result=fibonacci(10);
console.log(result)




// function asd() {
//     var c=30
//     if(5==5)
//     {
//         let c=21
//     }
//     console.log(c)
// }
// asd()