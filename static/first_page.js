var p1 = document.getElementById("op1");
var p2 = document.getElementById("op2");
var p4 = document.getElementById("op4");
var p5 = document.getElementById("op5");
var status= 'unsigned';

p2.style.color = "gray";
p4.style.color = "gray";
function clickfunc1(){
    p1.style.color = "white";
    p2.style.color = "gray";
}

function clickfunc2(){
    p2.style.color = "white";
    p1.style.color = "gray";
    var status= 'unsigned';
    if(status=='unsigned'){
        window.open("MLS.html","_self");
    }
    else{
        window.open("MLS2.html",'_self');
    }
}

function clickfunc3(){
    p4.style.color = "white";
    p5.style.color = "gray";
    window.open("first_page.html","_self");
}

function clickfunc4(){
    p5.style.color = "white";
    p4.style.color = "gray";
}

function refer(link){
    window.open(link, "_self");
}

function signin(){
    var creds=['appleID', 'AppleID', 'forcepage'];
    var name = document.getElementById("loginid").value;
    var status;
    if(name==''){
        alert("Please enter your Apple ID");
    }
    else{
        if(creds.includes(name)){
            //document.getElementById('signin').onclick="profile()";
            status= 'signed';
            window.open('first_page2.html','_self');
        }
        else{
            alert('Invalid Apple ID '+name+'. Sign up for an AppleID');
        }
    }

    function returncred(){
        return creds;
    }

    function returnstat(){
        return status;
    }
}

function signup(){
    var uid= document.getElementById("appleid").value;
    var pswd= document.getElementById("applepswd").value;
    var status;

    const ucreds=['cred1','cred2','cred3', "Apple"];
    const pcreds=['cred1','cred2','cred3', "Apple"];

    if(uid==''){
        alert("Please enter user ID.");
    }
    else{
        if(ucreds.includes(uid)){
            if(pcreds.includes(pswd)){
                alert('Apple ID created successfully')
                status= 'signed';
                window.open('first_page2.html','_self');
            }
            else{
                alert("Password did not meet requirements.");
            }
        }
        else{
            alert("ID did not meet requirements. Kindly re-enter the form.");
        }
    }
}