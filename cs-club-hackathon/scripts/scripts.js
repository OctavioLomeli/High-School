// keeps track of points, used to determine if win or lost
var points = 0;

// counting variables to show statistics at the result page
var total_rounds = 0;
var ones = 0;
var halves = 0;
var neg_halves = 0;
var neg_ones = 0;

// store the questions that have yet to be asked
const available_questions = [
  [0, 2],
  [0, 4],
  [0, 6],
  [1, 0],
  [1, 2],
  [1, 4],
  [1, 6],
  [2, 0],
  [2, 2],
  [2, 4],
  [2, 6],
];
var aq_length = 11;

// update statistics
function update_stats(p) {
  points += p;
  total_rounds++;

  var face_image = document.getElementById("face");
  // update bot image + statistics
  if (p == 1) {
    ones++;
    face_image.src = "assets/full_point.png";
  } else if (p == 0.5) {
    halves++;
    face_image.src = "assets/half_point.png";
  } else if (p == -0.5) {
    neg_halves++;
    face_image.src = "assets/half_negative.png";
  } else if (p == -1) {
    neg_ones++;
    face_image.src = "assets/full_negative.png";
  }
}

// changes the page according to which scenario the user reached + shows statistics
function modify_page_content(head_text, body_text) {
  // change which content is being displayed
  document.getElementsByClassName("results")[0].style.display = "block";
  document.getElementsByClassName("not-results")[0].style.display = "none";

  document.getElementById("Result-Text").innerText = head_text;

  document.getElementById("Result-Body").innerText = body_text;

  document.getElementById("total_rounds").innerText ="Number of responses given: " + total_rounds;

  document.getElementById("total_ones").innerText = "Number of 1 point responses: " + ones;

  document.getElementById("total_halves").innerText = "Number of half point responses: " + halves;

  document.getElementById("total_neg_halves").innerText = "Number of negative half point responses: " + neg_halves;

  document.getElementById("total_neg_ones").innerText = "Number of negative 1 point responses: " + neg_ones;
}

// this function helps change the innerHTML for response
// answer_p = how many points that response gives
function form_response(answer1, answer1_p, answer2, answer_2p) {
  var first_half ='<button class="butt-bot col-md-5" onclick="toNext(' + answer1_p + ')">' + answer1;
  var middle = '</button> <div class="col-md-2"></div> <button class="butt-bot col-md-5" onclick="toNext(';
  var last = answer_2p + ')">' + answer2 + "</button>";
  return first_half + middle + last;
}

// changes displayed question
// p = how much points a response gives
function toNext(p) {
  // update statistics
  update_stats(p);

  // checks if user won, lost, or round is ongoing
  if (points <= -3) {
    modify_page_content("You lost!", "You did not speak using terms that the bot liked. Try to match its speaking style next time.");
  } 
  else if (points >= 6) {
    modify_page_content("Nice Work! You won!", "You spoke using the same style as the bot. Nice catch.");
  }
  else if (total_rounds >= 12) {
    modify_page_content("You lost!", "You were unable to get 6 points within 12 questions. Try again!");
  } 
  else {
    // update the text that displays points
    document.getElementById("pointDisplay").innerHTML = "<b>Points: </b>" + points;
    document.getElementById("roundDisplay").innerHTML = "<b>Current Round: </b>" + (total_rounds + 1);
  
    // randomly get an available question    
    const location = available_questions[Math.floor(Math.random() * aq_length)];
    aq_length--;
    available_questions.splice(available_questions.indexOf(location), 1);

    // change question
    document.getElementsByClassName("bot-speech")[0].innerText = sentences[location[0]][1][location[1]];
    // change responses
    var response_rows = document.getElementsByClassName("response-choices");
    var reduce = sentences[location[0]][1][location[1] + 1];
    response_rows[0].innerHTML = form_response(
      reduce[0][0],
      reduce[0][1],
      reduce[1][0],
      reduce[1][1]
    );
    response_rows[1].innerHTML = form_response(
      reduce[2][0],
      reduce[2][1],
      reduce[3][0],
      reduce[3][1]
    );
  }
}
