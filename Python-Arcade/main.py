from flask import Flask, render_template

app = Flask("")

# information about projects (for flask variables)
index_projects = [
  [
    {'Link': 'https://replit.com/@OctavioLomeli/covid-stats', 'Img': "../static/assets/covid_gui.png", 'Description': 'COVID-19 Stats. This project is a GUI in which there are buttons to display bar graphs. The bar graphs display data relating to the number of COVID-19 cases and deaths in U.S.A. states.'},

    {'Link': 'https://replit.com/@OctavioLomeli/Mystery-Word', 'Img': "../static/assets/mystery_word.png", 'Description': 'Mystery Word. This project is a game in which a word is randomly chosen and the user must guess what the word is.'},

    {'Link': 'https://replit.com/@OctavioLomeli/Paint', 'Img': "../static/assets/paint.png", 'Description': 'Paint. This project is a program which allows the user to paint on a canvas. There are features such as an eraser, the ability to change brush size, and to clear the canvas.'}
  ],

  [
    {'Link': 'https://replit.com/@OctavioLomeli/June', 'Img': "../static/assets/bot_discord.png", 'Description': 'Discord bot. This project is a bot I created for a club that I am in. It contains commands to show covid-19 statistics as well as commands for the club.'},

    {'Link': 'https://replit.com/@OctavioLomeli/to-do-list', 'Img': "../static/assets/to_do.png", 'Description': 'To Do List. This project is a GUI in which the user is able to add and delete tasks. It also stores the tasks in a file so when you close the program and return, the tasks will be saved.'},

    {'Link': 'https://replit.com/@OctavioLomeli/Decision-Tree-and-KNN', 'Img': "../static/assets/tree_knn.png", 'Description': 'Decision Tree & KNN Models. This project contains four datasets which the user can select. Upon selecting a dataset, the user is asked to select a target to predict.'},
  ],  
]

project_projects = [
  {'Link': 'https://replit.com/@OctavioLomeli/Anagrams', 'Class_Name': 'project-card-image', 'Img': '../static/assets/anagram.png', 'Title': 'Anagrams', 'Description': 'This project is a game in which the user is shown a word that is scrambled and the user must input what they think the word unscrambled is. They start off with 2 lives and the goal of the game is to get the highest score you can.', 'project_class': 'anagrams', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/python-games/Anagrams', 'tags': 'game, tkinter',
  
  'Title2': 'Mystery Word', 'Description2': 'This project is a game in which the user is shown the length of a word and they must guess letters that are in the word. The user cannot make more than 7 mistakes or else they lose.', 'Link2': "https://replit.com/@OctavioLomeli/Mystery-Word?lite=true", 'Class_Name2':'project-card-image', 'Img2':'../static/assets/mystery_word.png', 'project_class2': "mystery-word", 'github2': "https://github.com/OctavioLomeli/High-School/tree/main/python-games/Mystery-Word", 'tags2': 'game, tkinter'
  },
  {'Link': 'https://replit.com/@OctavioLomeli/Tic-Tac-Toe', 'Class_Name': 'project-card-image', 'Img': '../static/assets/tic_tac_toe.png', 'Title': 'Tic-Tac-Toe', 'Description': 'This project is a game in which the user can pick spots within a grid to leave a mark. The first person to make three marks touching wins.', 'project_class': 'tic-tac-toe', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/python-games/Tic-Tac-Toe', 'tags':
  'game, tkinter, bot',
    
  'Title2': 'Discord Bot', 'Description2': 'This project is a bot named June. The bot has commands to display COVID-19 statistics as well as commands to help a club that I am in. Made with the Discord API.', 'Link2': "https://replit.com/@OctavioLomeli/June#main.py", 'Class_Name2':'project-card-image', 'Img2':'../static/assets/bot_discord.png', 'project_class2': 'discord-bot', 'external': 'https://discord.gg/wdsmhsncsp', 'github2': 'https://replit.com/@OctavioLomeli/June#main.py', 'tags2':'other, bot'
  },
  {'Link': "https://replit.com/@OctavioLomeli/Decision-Tree-and-KNN", 'Class_Name': 'special-image-large', 'Img': '../static/assets/tree_knn.png', 'Title': 'Decision Tree and KNN Models', 'Description': 'This project contains four datasets which the user can select. Upon selecting a dataset, the user is asked to select a target to predict. The predictions are made by using a decision tree and KNN model.', 'project_class': 'decision-tree-and-knn-models', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/python-other/decision-tree-knn', 'tags': 'other, machine learning',
    
  'Title2': 'COVID-19 Stats', 'Description2': 'This project is a GUI in which there are buttons to display bar graphs. The bar graphs display data relating to the number of COVID-19 cases and deaths in U.S.A. states.', 'Link2': "https://replit.com/@OctavioLomeli/covid-stats", 'Class_Name2':'project-card-image', 'Img2':'../static/assets/covid_gui.png', 'project_class2': 'covid-19-stats', 'github2': 'https://github.com/OctavioLomeli/High-School/tree/main/python-other/covid-stats', 'tags2':'other, tkinter'
  },
  {'Link': "https://replit.com/@OctavioLomeli/to-do-list", 'Class_Name': 'special-image-large', 'Img': '../static/assets/to_do.png', 'Title': 'To Do List', 'Description': 'This project is a GUI in which the user is able to add and delete tasks. It also stores the tasks in a file so when you close the program and return, the tasks will be saved. Pretty simple since it was one of the first GUIs I built.', 'project_class': 'to-do-list', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/python-other/to-do-list', 'tags': 'other, tkinter',
    
  'Title2': 'Music Player', 'Description2': 'This project is a GUI in which the user is able to select a music file of theirs to play. There are buttons to pause/unpause the song and to increase/decrease the volume. (Does not work properly on repl.it but if you paste the code on computer it will work.)', 'Link2': "https://replit.com/@OctavioLomeli/Music-Player", 'Class_Name2':'special-image-large', 'Img2':'../static/assets/music_player.png', 'project_class2': 'music-player', 'github2': 'https://github.com/OctavioLomeli/High-School/tree/main/python-other/music-player', 'tags2':'other, tkinter'
  },
  {'Link': "https://replit.com/@OctavioLomeli/Classify-Graph", 'Class_Name': 'project-card-image', 'Img': '../static/assets/classify_graph.png', 'Title': 'Classifying Graph', 'Description': 'This project is a visualisation of a graph which consists of two different coloured points. The user can add a point and the program will try to classify it based off the neighbor points. You can change the amount of neighbors it takes in consideration.', 'project_class': 'classify-graph', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/python-other/classify-graph', 'tags': 'other, machine learning, tkinter',
    
  'Title2': 'Follow The Light', 'Description2': 'This project is a game made with Pygame which randomly glows a square and the user has to match the order it glowed. As you go higher in rounds, the pattern increases.', 'Link2': "https://replit.com/@OctavioLomeli/Follow-The-Light", 'Class_Name2':'special-image-large', 'Img2':'../static/assets/follow_the_light.png', 'project_class2': 'follow-the-light', 'github2': 'https://github.com/OctavioLomeli/High-School/tree/main/python-games/Follow-the-light', 'tags2':'game'
  },
  {'Link': "https://replit.com/@OctavioLomeli/Paint", 'Class_Name': 'project-card-image', 'Img': '../static/assets/paint.png', 'Title': 'Paint', 'Description': 'This project is a program which allows the user to paint on a canvas. There are features such as an eraser, the ability to change brush size, and to clear the canvas. There are a total of nine colours the user can paint with.', 'project_class': 'paint', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/python-other/paint', 'tags':'game, tkinter',
    
  'Title2': '1v1 Soccer', 'Description2': 'This project is a game which resembles the popular game soccer. This program allows you to play with a friend who is local. A score system is present and there is a window to see the controls if you are new.', 'Link2': "https://replit.com/@OctavioLomeli/1v1-Soccer", 'Class_Name2':'project-card-image', 'Img2':'../static/assets/1v1_soccer.png', 'project_class2': 'soccer', 'github2': 'https://github.com/OctavioLomeli/High-School/tree/main/python-games/Soccer', 'tags2': 'game, tkinter'
  },
  {'Link': "https://quiz-time.octaviolomeli.repl.co/", 'Class_Name': 'project-card-image', 'Img': '../static/assets/quiztime.png', 'Title': 'Quiz Time', 'Description': 'This project is a website made with Flask that contains three quizzes for the user to try. Math, programming, and a random quiz.', 'project_class': 'quiztime', 'github': 'https://github.com/OctavioLomeli/High-School/tree/main/Quiz-Time', 'tags':'website'}
]

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html", index_projects=index_projects)

@app.route("/projects")
def projects():
    return render_template("projects.html", project_projects=project_projects)

app.run(host='0.0.0.0',port=8080)

# paste the link below into your search engine/bar
# also, if the program is not already running click run
# https://python-portfolio.octaviolomeli.repl.co