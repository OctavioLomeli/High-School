import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title("1v1 Soccer")
root['bg'] = "#2A3439"

# canvas
screen = tk.Canvas(root, width=800, height=500, bg="green")
screen.pack()

# goals
goal_1 = screen.create_rectangle(0, 0, 60, 500, fill='brown')
goal_2 = screen.create_rectangle(740, 0, 800, 500, fill='grey')

# soccer ball
soccer_ball = screen.create_oval(400, 250, 400, 250, width=20, outline='black')

# players
player_1 = screen.create_oval(100, 250, 100, 250, width=30, outline='grey')

player_2 = screen.create_oval(700, 250, 700, 250, width=30, outline='brown')

# variables
score_p1 = 0
score_p2 = 0

# labels
label_score_p1 = tk.Label(root, text=f"P1: {score_p1}", font=("Arial", 35), bg="grey", fg="white", pady=20)
label_score_p1.pack(side=tk.LEFT)
label_score_p2 = tk.Label(root, text=f'P2: {score_p2}', font=("Arial", 35), bg="brown", fg="white", pady=20, padx=3)
label_score_p2.pack(side=tk.RIGHT)
label_controls = tk.Button(root, text="Controls", font=("Arial", 20), bg="black", fg="white", pady=20, padx=67)
label_controls.pack(pady=20)


# functions

# makes new window open to show Controls
def show_controls():
  controls = tk.Toplevel(bg="#2A3439")
  controls.title("1v1 Soccer - Controls")
  p1_controls = tk.Label(controls, text="Player 1 Controls", font=("Arial", 25), bg="#2A3439", fg="white")
  p1_controls.pack(padx=20)
  p1_more = tk.Label(controls, text="A: Left\nw: Up\nS: Down\nD: Right\nQ: Kick", font=("Arial", 15), bg="#2A3439", fg="white")
  p1_more.pack()

  p2_controls = tk.Label(controls, text="Player 2 Controls", font=("Arial", 25), bg="#2A3439", fg="white")
  p2_controls.pack()
  p2_more = tk.Label(controls, text="Left Arrow: Left\nUp Arrow: Up\nDown Arrow: Down\nRight Arrow: Right\n\\: Kick", font=("Arial", 15), bg="#2A3439", fg="white")
  p2_more.pack()
  remove = tk.Button(controls, text="Close", font=("System", 25), command=controls.destroy)
  remove.pack(pady=10)

# moves ball back to place
def return_ball():
  y = screen.coords(soccer_ball)[1]
  if y < 250:
    while screen.coords(soccer_ball)[1] - 250 > 30:
      screen.move(soccer_ball, 0, 50)
      print("return ball if")
  else:
    while screen.coords(soccer_ball)[1] - 250 > 30 :
      screen.move(soccer_ball, 0, -50)
      print("return ball else")

# checks if goal was made 
def goal():
  global score_p1, score_p2
  if screen.coords(soccer_ball)[0] <= 60:
    score_p2 += 1
    label_score_p2.configure(text=f'P2: {score_p2}')
    return_ball()
    while screen.coords(soccer_ball)[0] != 400:
      screen.move(soccer_ball, 50, 0)
      print("goal if")

  elif screen.coords(soccer_ball)[0] >= 740:
    score_p1 += 1
    label_score_p1.configure(text=f'P1: {score_p1}')
    return_ball()
    while screen.coords(soccer_ball)[0] != 400:
      screen.move(soccer_ball, -50, 0)
      print("goal elif")

# kicking mechanic
def kick(player_y, ball_y, player_x, ball_x):
  # player on left or right of ball
  if player_y == ball_y and abs(ball_x - player_x) <= 40:
    if player_x - ball_x < 0:
      screen.move(soccer_ball, 100, 0)
    else:
      screen.move(soccer_ball, -100, 0)

  # player above or below ball
  elif player_x == ball_x and abs(ball_y - player_y) <= 40:
    if player_y - ball_y < 0:
      screen.move(soccer_ball, 0, 100)
    else:
      screen.move(soccer_ball, 0, -100)
  # player diagonal from ball
  elif abs(player_x - ball_x) <= 30 and abs(player_y - ball_y) <= 30:
    # player top left of ball
    if player_x < ball_x and player_y > ball_y:
      screen.move(soccer_ball, 100, -100)
    # player bottom left of ball
    elif player_x < ball_x and player_y < ball_y:
      screen.move(soccer_ball, 100, 100)
    # player top right of ball
    elif player_x > ball_x and player_y > ball_y:
      screen.move(soccer_ball, -100, -100)
    # player bottom right of ball
    else:
      screen.move(soccer_ball, -100, 100)
  # checks ball position
  goal()
  while screen.coords(soccer_ball)[1] > 470:
    screen.move(soccer_ball, 0, -10)
    print("kick first")
  while screen.coords(soccer_ball)[1] < 30:
    screen.move(soccer_ball, 0, 10)
    print("kick second")
  
  
# makes sure that players are within the stadium
def check_players():
  player1_x, player1_y = screen.coords(player_1)[0], screen.coords(player_1)[1]
  player2_x, player2_y = screen.coords(player_2)[0], screen.coords(player_2)[1]
  if player1_x < 10:
    screen.move(player_1, 10, 0)
  elif player1_x > 790:
    screen.move(player_1, -10, 0)
  elif player1_y < 20:
    screen.move(player_1, 0, 10)
  elif player1_y > 490:
    screen.move(player_1, 0, -10)
  elif player2_x < 10:
      screen.move(player_2, 10, 0)
  elif player2_x > 790:
    screen.move(player_2, -10, 0)
  elif player2_y < 20:
    screen.move(player_2, 0, 10)
  elif player2_y > 490:
    screen.move(player_2, 0, -10)

# controls for movement
def movement(event):
  if event.char == 'w':
    screen.move(player_1, 0, -20)
  elif event.char == "a":
    screen.move(player_1, -20, 0)
  elif event.char == "d":
    screen.move(player_1, 20, 0)
  elif event.char == "s":
    screen.move(player_1, 0, 20)
  elif event.keysym == "Up":
    screen.move(player_2, 0, -20)
  elif event.keysym == "Left":
    screen.move(player_2, -20, 0)
  elif event.keysym == "Right":
    screen.move(player_2, 20, 0)
  elif event.keysym == "Down":
    screen.move(player_2, 0, 20)
  elif event.char == "c":
    show_controls()
  # player 1 kick
  elif event.char == "q":
    ball_x, ball_y = screen.coords(soccer_ball)[0], screen.coords(soccer_ball)[1]
    player_x, player_y = screen.coords(player_1)[0], screen.coords(player_1)[1]
    kick(player_y, ball_y, player_x, ball_x)

  # player 2 kick
  elif event.char == "\\":
    ball_x, ball_y = screen.coords(soccer_ball)[0], screen.coords(soccer_ball)[1]
    player_x, player_y = screen.coords(player_2)[0], screen.coords(player_2)[1]
    kick(player_y, ball_y, player_x, ball_x)
    
  check_players()


# binding
root.bind('<KeyPress>', movement)
label_controls.configure(command=show_controls)

root.mainloop()
