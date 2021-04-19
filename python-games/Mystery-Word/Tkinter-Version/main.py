import tkinter as tk
import random
from functools import partial
# add way to update word display with a letter solved.


# selects a random word from text file
f = open('word.txt')
lines = f.readlines()
# (0, y) y = total lines in text file - 2(empty line at end included)
answer = lines[random.randint(0, 385)]
answer = list(answer[:len(answer) - 1].upper())
solved_so_far = ["_"] * len(answer)
lives = 7

root = tk.Tk()
root.title("Mystery Word")
root.geometry("605x365")
root.resizable(False, False)
root['bg'] = "#4FB0C6"


def guess_letter(letter, button):
    global lives
    if lives > 0:
        if letter in answer:
            solved_so_far[answer.index(letter)] = letter
            word['text'] = solved_so_far
            notify['text'] = 'Nice'
            winner()
        else:
            lives -= 1
            features['text'] = "Lives: {}".format(lives)
            if lives == 0:
                notify['text'] = "You lost."
                word['text'] = answer
            else:
                notify['text'] = "Not in"
        button['state'] = 'disabled'


def winner():
    if "_" not in solved_so_far:
        notify['text'] = "Winner!"


# two frames
topFrame = tk.Frame(root, bg="#4FB0C6")
topFrame.pack(side="top")
botFrame = tk.Frame(root, bg="#4FB0C6")
botFrame.pack(side="bottom")

# Top frame
# title of game
title = tk.Label(topFrame, text="Mystery Word", font=("System", 30), pady=10, bg="#4FB0C6", fg="white")
title.grid(row=1)
# label for word that is to be scrambled
word = tk.Label(topFrame, text="_ " * len(answer), font=("Verdana", 20), bg="#fff7c4", pady=20, padx=140)
word.grid(row=2, column=0)
# spacer
spacer5 = tk.Label(topFrame, bg='#4FB0C6', pady=5)
spacer5.grid(row=3)
# displays amount of lives
features = tk.Label(topFrame, text="Lives: {}".format(lives), bg='black', fg='white', font=('System', 14))
features.grid(row=0, column=0)

# Bottom Frame (buttons)
notify = tk.Label(botFrame, text="Use buttons", bg="white", fg='black', font=('System', 18))
notify.grid(row=0, columnspan=10, column=1)
buffer2 = tk.Label(botFrame, bg='#4FB0C6', pady=5)
buffer2.grid(row=1)

buttonA = tk.Button(botFrame, text="A", padx=9)
buttonA.grid(row=2, column=0)
buttonA.configure(command=partial(guess_letter, 'A', buttonA))
buttonB = tk.Button(botFrame, text="B", padx=9)
buttonB.grid(row=2, column=1)
buttonB.configure(command=partial(guess_letter, 'B', buttonB))
buttonC = tk.Button(botFrame, text="C", padx=9)
buttonC.grid(row=2, column=2)
buttonC.configure(command=partial(guess_letter, 'C', buttonC))
buttonD = tk.Button(botFrame, text="D", padx=9)
buttonD.grid(row=2, column=3)
buttonD.configure(command=partial(guess_letter, 'D', buttonD))
buttonE = tk.Button(botFrame, text="E", padx=9)
buttonE.grid(row=2, column=4)
buttonE.configure(command=partial(guess_letter, 'E', buttonE))
buttonF = tk.Button(botFrame, text="F", padx=9)
buttonF.grid(row=2, column=5)
buttonF.configure(command=partial(guess_letter, 'F', buttonF))
buttonG = tk.Button(botFrame, text="G", padx=9)
buttonG.grid(row=2, column=6)
buttonG.configure(command=partial(guess_letter, 'G', buttonG))
buttonH = tk.Button(botFrame, text="H", padx=9)
buttonH.grid(row=2, column=7)
buttonH.configure(command=partial(guess_letter, 'H', buttonH))
buttonI = tk.Button(botFrame, text="I", padx=11)
buttonI.grid(row=2, column=8)
buttonI.configure(command=partial(guess_letter, 'I', buttonI))
buttonJ = tk.Button(botFrame, text="J", padx=11)
buttonJ.grid(row=2, column=9)
buttonJ.configure(command=partial(guess_letter, 'J', buttonJ))
buttonK = tk.Button(botFrame, text="K", padx=9)
buttonK.grid(row=2, column=10)
buttonK.configure(command=partial(guess_letter, 'K', buttonK))
buttonL = tk.Button(botFrame, text="L", padx=9)
buttonL.grid(row=2, column=11)
buttonL.configure(command=partial(guess_letter, 'L', buttonL))
buttonM = tk.Button(botFrame, text="M", padx=7)
buttonM.grid(row=2, column=13)
buttonM.configure(command=partial(guess_letter, 'M', buttonM))
buttonN = tk.Button(botFrame, text="N", padx=9)
buttonN.grid(row=3, column=0)
buttonN.configure(command=partial(guess_letter, 'N', buttonN))
buttonO = tk.Button(botFrame, text="O", padx=9)
buttonO.grid(row=3, column=1)
buttonO.configure(command=partial(guess_letter, 'O', buttonO))
buttonP = tk.Button(botFrame, text="P", padx=9)
buttonP.grid(row=3, column=2)
buttonP.configure(command=partial(guess_letter, 'P', buttonP))
buttonQ = tk.Button(botFrame, text="Q", padx=9)
buttonQ.grid(row=3, column=3)
buttonQ.configure(command=partial(guess_letter, 'Q', buttonQ))
buttonR = tk.Button(botFrame, text="R", padx=9)
buttonR.grid(row=3, column=4)
buttonR.configure(command=partial(guess_letter, 'R', buttonR))
buttonS = tk.Button(botFrame, text="S", padx=9)
buttonS.grid(row=3, column=5)
buttonS.configure(command=partial(guess_letter, 'S', buttonS))
buttonT = tk.Button(botFrame, text="T", padx=9)
buttonT.grid(row=3, column=6)
buttonT.configure(command=partial(guess_letter, 'T', buttonT))
buttonU = tk.Button(botFrame, text="U", padx=9)
buttonU.grid(row=3, column=7)
buttonU.configure(command=partial(guess_letter, 'U', buttonU))
buttonV = tk.Button(botFrame, text="V", padx=9)
buttonV.grid(row=3, column=8)
buttonV.configure(command=partial(guess_letter, 'V', buttonV))
buttonW = tk.Button(botFrame, text="W", padx=9)
buttonW.grid(row=3, column=9)
buttonW.configure(command=partial(guess_letter, 'W', buttonW))
buttonX = tk.Button(botFrame, text="X", padx=9)
buttonX.grid(row=3, column=10)
buttonX.configure(command=partial(guess_letter, 'X', buttonX))
buttonY = tk.Button(botFrame, text="Y", padx=9)
buttonY.grid(row=3, column=11)
buttonY.configure(command=partial(guess_letter, 'Y', buttonY))
buttonZ = tk.Button(botFrame, text="Z", padx=9)
buttonZ.grid(row=3, column=13)
buttonZ.configure(command=partial(guess_letter, 'Z', buttonZ))
buffer = tk.Label(botFrame, pady=20, bg='#4FB0C6')
buffer.grid(row=4, columnspan=13)

root.mainloop()
