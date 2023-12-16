function add(){
    let a=parseFloat(document.getElementById('fno').value)
    let b=parseFloat(document.getElementById('sno').value)
    let c=a+b
    let x=document.getElementById('answer')
    x.innerText=c
}