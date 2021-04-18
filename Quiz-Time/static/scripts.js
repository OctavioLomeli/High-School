var score = 0;
// Assigns a random href to the book image in index.html
function bookClick(){
    var decider = Math.floor(Math.random() * 11);
    if(decider > 6){
        document.getElementById("book").href="https://www.khanacademy.org";
    }else{
        document.getElementById("book").href="https://www.youtube.com/watch?v=dQw4w9WgXcQ";
    }
}
//Allows user to go to the next question
function toNext(quizLetter,hiding,showing,point){
    var hidden = document.getElementsByClassName(quizLetter + "Q" + hiding);
    hidden[0].style.display = "none";
    var show = document.getElementsByClassName(quizLetter + "Q" + showing);
    show[0].style.display = "block";
    score = score + point;
    document.getElementById(quizLetter + "scoreDisplay").innerText = "Score: " + score + "/13";
}