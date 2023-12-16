function asd(e){
    e.preventDefault();
    let uname=document.getElementById('uname').value;
    let email=document.getElementById('email').value;
    let pwd=document.getElementById('pwd').value;
    let cpwd=document.getElementById('cpwd').value;
    if(pwd==cpwd)
    {
        if(!(email&&uname&&pwd&&cpwd))
        // if(email||=uname||=pwd||=cpwd)
        {
            alert("fileds are empty")
        }
        else{
            alert("successfully loged in")
        }

    }
    else{
        alert('password not match')
    }
}