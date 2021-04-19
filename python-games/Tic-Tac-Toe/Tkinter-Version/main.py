import tkinter as tk
# font on buttons
import tkinter.font as font
# importing partial to use parameters
from functools import partial
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#000000")
root.resizable(False, False)
root.geometry("800x800")
myFont = font.Font(family='Arial', size=15, weight='normal')

# variables
turn = 0


def assign_spot(spot_name):
    global turn
    if turn % 2 != 0:
        spot_name.configure(
            text="X", state=tk.DISABLED, disabledforeground="black")
    else:
        spot_name.configure(
            text="O", state=tk.DISABLED, disabledforeground="black")
    turn += 1
    message.configure(text="Turn: {}".format(turn))
    checkWin()
    call_bot()

def assign_spot_for_bot(spot_name):
    global turn
    if turn % 2 != 0:
        spot_name.configure(
            text="X", state=tk.DISABLED, disabledforeground="black")
    else:
        spot_name.configure(
            text="O", state=tk.DISABLED, disabledforeground="black")
    turn += 1
    message.configure(text="Turn: {}".format(turn))
    checkWin()

def call_bot():
  available_spots = []
  for spot in [A1, A2, A3, B1, B2, B3, C1, C2, C3]:
    if spot['text'] == "":
      available_spots.append(spot)
  if len(available_spots) == 0:
    return
  # first row
  if A1['text'] == "O" and A2['text'] == "O" and A3 in available_spots:
    assign_spot_for_bot(A3)
    return
  if A2['text'] == "O" and A3['text'] == "O" and A1 in available_spots:
    assign_spot_for_bot(A1)
    return
  if A1['text'] == "O" and A3['text'] == "O" and A2 in available_spots:
    assign_spot_for_bot(A2)
    return
  # second row
  if B1['text'] == "O" and B2['text'] == "O" and B3 in available_spots:
    assign_spot_for_bot(B3)
    return
  if B1['text'] == "O" and B3['text'] == "O" and B2 in available_spots:
    assign_spot_for_bot(B2)
    return
  if B3['text'] == "O" and B2['text'] == "O" and B1 in available_spots:
    assign_spot_for_bot(B1)
    return
  # third row
  if C1['text'] == "O" and C2['text'] == "O" and C3 in available_spots:
    assign_spot_for_bot(C3)
    return
  if C1['text'] == "O" and C3['text'] == "O" and C2 in available_spots:
    assign_spot_for_bot(C2)
    return
  if C3['text'] == "O" and C2['text'] == "O" and C1 in available_spots:
    assign_spot_for_bot(C1)
    return
  # first column
  if A1['text'] == "O" and B1['text'] == "O" and C1 in available_spots:
    assign_spot_for_bot(C1)
    return
  if A1['text'] == "O" and C1['text'] == "O" and B1 in available_spots:
    assign_spot_for_bot(B1)
    return
  if C1['text'] == "O" and B1['text'] == "O" and A1 in available_spots:
    assign_spot_for_bot(A1)
    return
  # second column
  if A2['text'] == "O" and B2['text'] == "O" and C2 in available_spots:
    assign_spot_for_bot(C2)
    return
  if A2['text'] == "O" and B2['text'] == "O" and B2 in available_spots:
    assign_spot_for_bot(B2)
    return
  if C2['text'] == "O" and B2['text'] == "O" and A2 in available_spots:
    assign_spot_for_bot(A2)
    return
  # third column
  if A3['text'] == "O" and B3['text'] == "O" and C3 in available_spots:
    assign_spot_for_bot(C3)
    return
  if A3['text'] == "O" and C3['text'] == "O" and B3 in available_spots:
    assign_spot_for_bot(B3)
    return
  if C3['text'] == "O" and B3['text'] == "O" and A3 in available_spots:
    assign_spot_for_bot(A3)
    return
  # top left to bottom right
  if A1['text'] == "O" and B2['text'] == "O" and C3 in available_spots:
    assign_spot_for_bot(C3)
    return
  if A1['text'] == "O" and C3['text'] == "O" and B2 in available_spots:
    assign_spot_for_bot(B2)
    return
  if C3['text'] == "O" and B2['text'] == "O" and A1 in available_spots:
    assign_spot_for_bot(A1)
    return
  # top right to bottom left
  if A3['text'] == "O" and B2['text'] == "O" and C1 in available_spots:
    assign_spot_for_bot(C1)
    return
  if A3['text'] == "O" and C1['text'] == "O" and B2 in available_spots:
    assign_spot_for_bot(B2)
    return
  if C1['text'] == "O" and B2['text'] == "O" and A3 in available_spots:
    assign_spot_for_bot(A3)
    return
  assign_spot_for_bot(random.choice(available_spots))



# Clears all spots
def clear(list_of_spots):
    global turn
    for button in list_of_spots:
        button.configure(state=tk.NORMAL)
        button['text'] = ""
    turn = 0
    message.configure(text="Turn: {}".format(turn))
    try:
      pop_up.destroy()
      message_popup.destroy()
    except:
      pass


def checkCol():
    if A1['text'] == B1['text'] and C1['text'] == A1[
            'text'] and A1['text'] != "":
        return True
    if A2['text'] == B2['text'] and B2['text'] == C2[
            'text'] and C2['text'] != "":
        return True
    if A3['text'] == B3['text'] and B3['text'] == C3[
            'text'] and C3['text'] != "":
        return True
    return False


def checkRow():
    if A1['text'] == A2['text'] and A2['text'] == A3[
            'text'] and A3['text'] != "":
        return True
    if B1['text'] == B2['text'] and B2['text'] == B3[
            'text'] and B3['text'] != "":
        return True
    if C1['text'] == C2['text'] and C2['text'] == C3[
            'text'] and C3['text'] != "":
        return True
    return False


def checkDiagonal():
    if A1['text'] == B2['text'] and C3['text'] == B2[
            'text'] and A1['text'] != "":
        return True
    if C1['text'] == B2['text'] and A3['text'] == C1[
            'text'] and C1['text'] != "":
        return True
    return False


def checkWin():
  if checkCol() or checkRow() or checkDiagonal():
      message.configure(text="Winner")
      for spot in [A1, A2, A3, B1, B2, B3, C1, C2, C3]:
          spot.configure(state=tk.DISABLED)
      winner_message()

  elif turn == 9 and (checkCol() or checkRow() or checkDiagonal()) == False:
      message.configure(text="TIE")
      for spot in [A1, A2, A3, B1, B2, B3, C1, C2, C3]:
          spot.configure(state=tk.DISABLED)


def winner_message():
  global pop_up
  global message_popup
  x = root.winfo_x()
  y = root.winfo_y()
  pop_up = tk.Toplevel(width=200, height=200, bg="black")
  pop_up.geometry("+%d+%d" % (x + 200, y + 200))
  
  if turn % 2 != 0:
    message_popup = tk.Label(pop_up, text='O Wins!', font=("Arial", 50), fg='white', bg='black').pack()
  else:
    message_popup = tk.Label(pop_up, text='X Wins!', font=("Arial", 50), fg='white', bg="black").pack()

# Making the 9 buttons
A1 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
A1.configure(
    command=partial(assign_spot, A1),
    highlightbackground="white",
    borderwidth=3)
A1['font'] = myFont
A1.grid(row=1, column=0)

A2 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
A2.configure(
    command=partial(assign_spot, A2),
    highlightbackground="white",
    borderwidth=3)
A2['font'] = myFont
A2.grid(row=1, column=1)

A3 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
A3.configure(
    command=partial(assign_spot, A3),
    highlightbackground="white",
    borderwidth=3)
A3['font'] = myFont
A3.grid(row=1, column=2)

B1 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
B1.configure(
    command=partial(assign_spot, B1),
    highlightbackground="white",
    borderwidth=3)
B1['font'] = myFont
B1.grid(row=2, column=0)

B2 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
B2.configure(
    command=partial(assign_spot, B2),
    highlightbackground="white",
    borderwidth=3)
B2['font'] = myFont
B2.grid(row=2, column=1)

B3 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
B3.configure(
    command=partial(assign_spot, B3),
    highlightbackground="white",
    borderwidth=3)
B3['font'] = myFont
B3.grid(row=2, column=2)

C1 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
C1.configure(
    command=partial(assign_spot, C1),
    highlightbackground="white",
    borderwidth=3)
C1['font'] = myFont
C1.grid(row=3, column=0)

C2 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
C2.configure(
    command=partial(assign_spot, C2),
    highlightbackground="white",
    borderwidth=3)
C2['font'] = myFont
C2.grid(row=3, column=1)

C3 = tk.Button(root, text="", width=15, height=5, bg="white", fg="white")
C3.configure(
    command=partial(assign_spot, C3), highlightbackground="white", borderwidth=3)
C3['font'] = myFont
C3.grid(row=3, column=2)

# label to show winner and turn
message = tk.Label(
    root,
    text="Turn: {}".format(turn),
    height=2,
    bg="black",
    fg="white",
    padx=30)
message['font'] = myFont
message.grid(row=0, column=0, columnspan=3)

# button to restart
restart = tk.Button(
    root,
    text="Clear",
    width=30,
    bg="#e5e5e5",
    fg="black",
    command=partial(clear, [A1, A2, A3, B1, B2, B3, C1, C2, C3]))
restart['font'] = myFont
restart.grid(row=4, column=0, columnspan=3)

# end of buttons

root.mainloop()
