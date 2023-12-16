function asd(e){
    e.preventDefault();
    let eid=document.getElementById('eid').value;
    let ename=document.getElementById('ename').value;
    let esalary=document.getElementById('esalary').value;
    let eexp=document.getElementById('eexp').value;
    let epph=document.getElementById('epph').value;
    if(!(eid&&ename&&esalary&&eexp&&epph))
    {
        alert("fileds are empty")
    }
    else{
        alert("successfully loged in")
    }


}