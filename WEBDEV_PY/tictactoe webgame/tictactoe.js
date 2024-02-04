function game(buttonId){
    var button = document.getElementById(buttonId);
    userchoice=document.getElementById(buttonId).innerHTML="X";
    computerchoice=Math.floor(Math.random(buttonId)*9)+1;
    document.getElementById(computerchoice).innerHTML='0'
}