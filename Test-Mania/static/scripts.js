var score = 0;
//Allows user to go to the next question
function toNext(quizLetter,hiding,showing,point){
    var hidden = document.getElementsByClassName(quizLetter + "Q" + hiding);
    hidden[0].style.display = "none";
    var show = document.getElementsByClassName(quizLetter + "Q" + showing);
    show[0].style.display = "block";
    score = score + point;
    document.getElementById(quizLetter + "scoreDisplay").innerText = "Score: " + score + "/13";
}