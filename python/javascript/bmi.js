function calculate(){
    let w=document.getElementById('weight').value
    let h=document.getElementById('height').value
    let h1=h/100
    let c=w/(h1**2)
    if (c<18.5){
        a="underweight"
    }
    else if (c<24.9)
    {
        a="normalweight"
    }
    else if (c<29.9)
    {
        a="overweight"
    }
    else if (c<30)
    {
        a="30"
    }
    else
    {
        a="error"
    }
    let x=document.getElementById('ans')
    x.innerHTML=c+a
}