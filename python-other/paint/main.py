import tkinter as tk
from functools import partial

root = tk.Tk()
# window settings
root.title("Paint")
root.geometry("800x600")
root.resizable(False, False)

# variables
color = "black"
    # color grid
red_color, blue_color, green_color, yellow_color, pink_color, purple_color, white_color, grey_color, black_color = 0, 0, 0, 0, 0, 0, 0, 0, 0
color_buttons = [[[red_color, 'red'], [blue_color, 'blue'], [green_color, 'green']], [[yellow_color, 'yellow'], [pink_color, 'pink'], [purple_color, 'purple']],
                 [[white_color, 'white'], [grey_color, 'grey'], [black_color, 'black']]]
eraser_on = False
brush_width = 15

# frames
rightFrame = tk.Frame(root, bg="black", pady=30)
rightFrame.pack(side=tk.RIGHT)

color_frame = tk.Frame(rightFrame, bg="black")
color_frame.grid(row=7, column=0, columnspan=3, padx=7)

# rightFrame content

    # buttons
draw_button = tk.Button(rightFrame, text="Brush", font=("Arial", 15), bg="white", fg="black", width=6)
draw_button.grid(row=0, column=0, pady=25, padx=3)

eraser_button = tk.Button(rightFrame, text="Eraser", font=("Arial", 15), bg="white", fg="black", width=6)
eraser_button.grid(row=0, column=1, pady=10, padx=3)

clear_button = tk.Button(rightFrame, text="Clear", font=("Arial", 15), bg="white", fg="black", width=5)
clear_button.grid(row=1, column=0, pady=25, padx=3)

change_button = tk.Button(rightFrame, text="Size: 15", font=("Arial", 15), bg="white", fg="black", width=5)
change_button.grid(row=1, column=1, pady=10, padx=3)

    # labels
current_color_label = tk.Label(rightFrame, text="Current Color", font=("Arial", 15), fg="white", bg="black")
current_color_label.grid(row=4, column=0, pady=15, columnspan=2)

current_color_box = tk.Canvas(rightFrame, width=50, height=50, bg="black")
current_color_box.grid(row=5, column=0, columnspan=2, pady=5)

colors_label = tk.Label(rightFrame, text="Colors", font=("Arial", 15), fg='white', bg='black').grid(row=6, column=0, columnspan=2, pady=25)


# creating buttons for colors
for i in range(3):
    for j in range(3):
        color_buttons[i][j][0] = tk.Button(color_frame, width=4, height=2, bg=color_buttons[i][j][1])
        color_buttons[i][j][0].grid(row=i, column=j)

# Canvas
paint_board = tk.Canvas(root, width=620, height=600, bg='#F0F0ED')
paint_board.pack()

# functions
def clear_canvas():
    paint_board.delete("all")
    paint_board['bg'] = "#F0F0ED"

def change_size():
    global brush_width
    brush_width += 5
    if brush_width > 35:
      brush_width = 15
    change_button.configure(text=f'Size:{brush_width}')



def select_color(button_color):
    global color
    color = button_color
    current_color_box['bg'] = color

def eraser():
    global color
    global eraser_on
    color, eraser_on = '#F0F0ED', True

def brush():
    global eraser_on
    eraser_on = False

def drawing(event):
    global color
    x, y = event.x, event.y
    if eraser_on:
      color = '#F0F0ED'
      paint_board.create_oval(x, y, x, y, width=brush_width, outline=color)
    else:
      color = current_color_box['bg']
      paint_board.create_oval(x, y, x, y, width=brush_width, outline=color)


# command assigning
clear_button.configure(command=clear_canvas)
change_button.configure(command=change_size)
eraser_button.configure(command=eraser)
draw_button.configure(command=brush)
    # adding commands to all 9 buttons
for i in range(3):
    for j in range(3):
        color_buttons[i][j][0].configure(command=partial(select_color, color_buttons[i][j][1]))

paint_board.bind('<B1-Motion>', drawing)

root.mainloop()
