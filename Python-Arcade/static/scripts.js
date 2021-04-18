var tags = {"anagrams": "game, tkinter", "mystery-word": "game, tkinter", "tic-tac-toe": "game, tkinter, bot", "discord-bot": "bot, other", "decision-tree-and-knn-models": "other, machine learning", "covid-19-stats": "other, tkinter", "to-do-list": "other, tkinter", "music-player": "other, tkinter", "classify-graph": "other, machine learning, tkinter", "follow-the-light": "game", "paint": "game, tkinter", "soccer": "game, tkinter", "quiztime": "website"};

function filter_search(){
  var keyword = document.getElementsByClassName("search-input")[0].value.toLowerCase() // getting the text in input
  for(var tag in tags){ // looping through project names
    if(tag.indexOf(keyword) == -1){
      document.getElementsByClassName(tag)[0].style.display = "none";
      document.getElementsByClassName(tag)[1].style.display = "none";
    }
    else{
      document.getElementsByClassName(tag)[0].style.display = "inline";
      document.getElementsByClassName(tag)[1].style.display = "inline";
    }
  }
}

function reset()
{
  for (var tag in tags)
  {
    document.getElementsByClassName(tag)[0].style.display = 'inline';
    document.getElementsByClassName(tag)[1].style.display = 'inline';
  }
  document.getElementsByClassName("search-input")[0].value = "";
}

function filter_tags(desired_tag)
{
  reset()
  for(var tag in tags)
  {
    if(tags[tag].indexOf(desired_tag) == -1)
    {
      document.getElementsByClassName(tag)[0].style.display = "none";
      document.getElementsByClassName(tag)[1].style.display = "none";
    }
  }
}