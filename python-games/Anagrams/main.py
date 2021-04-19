import tkinter as tk
import random

f = open('word.txt')
lines = f.readlines()
answer = lines[random.randint(0, 28)]
answer = answer[:len(answer) - 1].upper()
scrambled = "".join(random.sample(answer, len(answer)))
lives = 2
score = 0

# restarts everything
def restart():
    global lives
    global score
    global answer
    lives = 2
    score = 0
    submit.configure(text='Try', command=grade)
    features['text'] = "Lives: {}   Score: {}".format(lives, score)
    answer = lines[random.randint(0, 28)]
    answer = answer[:len(answer) - 1].upper()
    word['text'] = "".join(random.sample(answer, len(answer)))


# compares text in input to the answer
def grade():
    guess = prompt.get().upper()
    global lives
    global score
    global answer
    if guess == answer and lives > 0:
        correct['text'] = "Correct!"
        score += 1
        answer = lines[random.randint(0, 28)]
        answer = answer[:len(answer) - 1].upper()
        word['text'] = "".join(random.sample(answer, len(answer)))
    elif lives > 1:
        correct['text'] = "Incorrect!"
        lives -= 1
    else:
        if lives == 1:
            lives -= 1
        correct['text'] = 'It was "{}"'.format(answer)
        submit.configure(text='Restart', command=restart)
    features['text'] = "Lives: {}   Score: {}".format(lives, score)


root = tk.Tk()
root.title("Anagrams")
root.geometry("605x365")
root.resizable(False, False)
root['bg'] = "#4FB0C6"

# two frames
topFrame = tk.Frame(root, bg="#4FB0C6")
topFrame.pack(side="top")
botFrame = tk.Frame(root, bg="#4FB0C6")
botFrame.pack(side="bottom")

# Top frame
    # title of game
title = tk.Label(topFrame, text="Anagrams", font=("System", 30), pady=10, bg="#4FB0C6", fg="white")
title.grid(row=1)
# label for word that is to be scrambled
word = tk.Label(topFrame, text=scrambled, font=("Verdana", 20), bg="#fff7c4", pady=20, padx=140)
word.configure(highlightbackground='black', highlightcolor='black')
word.grid(row=2, column=0)
# spacer
spacer5 = tk.Label(topFrame, bg='#4FB0C6', pady=5)
spacer5.grid(row=3)
# correct box
correct = tk.Label(topFrame, text="Start", bg='#aa8181', fg='white', font=('Verdana', 16), padx=70)
correct.grid(row=4)

# Bottom Frame
    # label for input
promptLabel = tk.Label(botFrame, text="Guess: ", font=("System", 15), bg="white", fg='black')
promptLabel.grid(row=0, column=0)
# input field
prompt = tk.Entry(botFrame, width=16, font=("Verdana", 15))
prompt.grid(row=0, column=1)
# space between input and button
buffer2 = tk.Label(botFrame, pady=5, bg="#4FB0C6")
buffer2.grid(row=1)
# button for input
submit = tk.Button(botFrame, text='Try', font=("Comic Sans MS", 15), width=6, bg="#4F86C6", fg="white", command=grade)
submit.grid(row=2, column=0, columnspan=2)
# space for bottom
buffer = tk.Label(botFrame, pady=3, bg="#4FB0C6")
buffer.grid(row=3)
# label for bottom
features = tk.Label(topFrame, text="Lives: {}   Score: {}".format(lives, score), bg='black', fg='white', font='System')
features.grid(row=0, column=0)

root.mainloop()
