import tkinter as tk
import random
import math

root = tk.Tk()
root.geometry("800x600")
root['bg'] = "#618B25"
root.resizable(False, False)

colors = ["blue", "green"]
all_points = []

# frames
topFrame = tk.Frame(root, bg="#618B25")
topFrame.pack(side="top")

bottomFrame = tk.Frame(root, bg="#618B25")
bottomFrame.pack(side="bottom", pady=20)

dimensions = tk.Label(topFrame, text="Dimensions: 550x320", font=("Arial", 15))
dimensions.pack()

# canvas
canvas = tk.Canvas(topFrame, width=550, height=320, bg="white")
canvas.pack()

# buttons
create_new_graph = tk.Button(bottomFrame, text="New Graph", font=("Arial", 15), width=10)
create_new_graph.grid(row=0, column=0, pady=4)
label_create_new_graph = tk.Label(bottomFrame, text="Total Dots(2-50):", font=("Arial", 15))
label_create_new_graph.grid(row=0, column=1, padx=4)
entry_create_new_graph = tk.Entry(bottomFrame, font=("Arial", 15), width=9)
entry_create_new_graph.grid(row=0, column=2, padx=4)

add_new_point = tk.Button(bottomFrame, text="Add Point", font=("Arial", 15), width=10)
add_new_point.grid(row=2, column=0, pady=4)
label_add_new_point = tk.Label(bottomFrame, text="Format: x, y", font=("Arial", 15))
label_add_new_point.grid(row=2, column=1, padx=4)
entry_add_new_point = tk.Entry(bottomFrame, font=("Arial", 15), width=9)
entry_add_new_point.grid(row=2, column=2, padx=4)

change_k = tk.Button(bottomFrame, text="Set K", font=("Arial", 15), width=10)
change_k.grid(row=4, column=0, pady=4)
label_change_k = tk.Label(bottomFrame, text="New K:", font=("Arial", 15))
label_change_k.grid(row=4, column=1, padx=4)
entry_change_k = tk.Entry(bottomFrame, font=("Arial", 15), width=9)
entry_change_k.grid(row=4, column=2, padx=4)

classification = tk.Label(bottomFrame, text="New Point classified as: ", font=("Arial", 15), padx=5)
classification.grid(row=5, column=0, columnspan=3, pady=10)


# # functions
# adds a point to the graph
def add_point_function():
    try:
        x, y = entry_add_new_point.get().split(",")
        x, y = x.strip(), y.strip()
        all_points.append([int(x), int(y)])
        canvas.create_oval(x, y, x, y, width=15, outline="red")
        add_new_point['state'] = tk.DISABLED
        entry_add_new_point.delete(0, "end")
    except:
        print("Not valid spot.")


# creates a new graph with an amount of dots equal to number in the input box
def change_set_function():
    canvas.delete("all")
    global all_points
    all_points = []
    add_new_point['state'] = tk.NORMAL
    classification.configure(text="New Point classified as: ")
    try:
        amount = int(entry_create_new_graph.get())
        if amount <= 1 or amount >= 51:
            amount = 25
    except:
        amount = 25
    for i in range(amount):
        ran_x = random.randint(50, 500)
        ran_y = random.randint(50, 300)
        color_choice = colors[random.randint(0, 1)]
        all_points.append([ran_x, ran_y, color_choice])
        canvas.create_oval(ran_x, ran_y, ran_x, ran_y, width=15, outline=color_choice)


# changes value of k
def change_k_function():
    global all_points
    try:
        if entry_change_k.get() != "":
            k = int(entry_change_k.get())
        else:
            k = 1
    except:
        k = 1

    for index in range(len(all_points) - 1):
        distance_from_user_point = math.sqrt(
            (all_points[-1][0] - all_points[index][0]) ** 2 + (all_points[-1][1] - all_points[index][1]) ** 2)
        all_points[index].append(distance_from_user_point)
    if len(all_points[-1]) == 2:
        all_points.pop()
    all_points.sort(key=lambda x: x[-1])
    for element in all_points:
        print(element)
    green_count = 0
    blue_count = 0
    for element in all_points[:k]:
        if element[-2] == "green":
            green_count += 1
        else:
            blue_count += 1
    if green_count > blue_count:
        classification.configure(text="New Point classified as: green")
    elif green_count < blue_count:
        classification.configure(text="New Point classified as: blue")
    else:
        classification.configure(text="New Point is undecided.")


# assigning commands to buttons
create_new_graph.configure(command=change_set_function)
add_new_point.configure(command=add_point_function)
change_k.configure(command=change_k_function)

change_set_function()

root.mainloop()
