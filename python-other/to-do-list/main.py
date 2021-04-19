import tkinter as tk
from functools import partial

root = tk.Tk()
root.geometry('425x500')
root.title('To Do List')
root.resizable(False, False)
root['bg'] = 'white'

# title of gui
title = tk.Label(root, text='To Do', font=('Verdana', 25), fg='black', bg='white')
title.pack(padx=20, pady=2)

# frames
bottomFrame = tk.Frame(root, bg='white')
bottomFrame.pack(side='bottom', pady=10)

rightFrame = tk.Frame(root, bg='white')
rightFrame.pack(side='right', padx=10)

task_box = tk.Frame(root, bg='grey', highlightbackground="black",  highlightthickness=1)
task_box.pack(side='right')
# input for name
e = tk.Entry(bottomFrame, font=('Verdana', 15), highlightbackground="black",  highlightthickness=1)
e.pack()


def add_task():
    open_tasks = []
    # all empty task boxes noted
    for button in [task1, task2, task3, task4, task5, task6, task7]:
        if button['text'] == '' or button['text'] == " ":
            open_tasks.append(button)

    if len(open_tasks) != 0:
        # get text from input
        user_input = e.get()
        open_tasks[0].configure(text=user_input)
        e.delete(0, 'end')
        myFile = open("memory.txt", "r")
        lines = myFile.readlines()
        myFile.close()
        if open_tasks[0] == task1:
          lines[0] = f"{user_input}\n"
        elif open_tasks[0] == task2:
          lines[1] = f"{user_input}\n"
        elif open_tasks[0] == task3:
          lines[2] = f"{user_input}\n"
        elif open_tasks[0] == task4:
          lines[3] = f"{user_input}\n"
        elif open_tasks[0] == task5:
          lines[4] = f"{user_input}\n"
        elif open_tasks[0] == task6:
          lines[5] = f"{user_input}\n"
        elif open_tasks[0] == task7:
          lines[6] = f"{user_input}\n"
        myFile = open("memory.txt", "w")
        for line in lines:
          myFile.write(line)
        myFile.close()
    else:
        e.delete(0, 'end')
        e.insert(0, 'No open task box.')


# deletes the text from the task next to it and removes from file
def delete_task(task):
    if task['text'] == '' or task['text'] == ' ':
        e.delete(0, 'end')
        e.insert(0, 'Nothing to delete')
    else:
        task.configure(text='')
        myFile = open("memory.txt", "r")
        lines = myFile.readlines()
        myFile.close()
        if task == task1:
          lines[0] = "\n"
        elif task == task2:
          lines[1] = "\n"
        elif task == task3:
          lines[2] = "\n"
        elif task == task4:
          lines[3] = "\n"
        elif task == task5:
          lines[4] = "\n"
        elif task == task6:
          lines[5] = "\n"
        elif task == task7:
          lines[6] = "\n"
        myFile = open("memory.txt", "w")
        for line in lines:
          myFile.write(line)
        myFile.close()


add = tk.Button(bottomFrame, text='Add Task', font=('Verdana', 15), bg='#2a3439', fg='white', command=add_task)
add.pack(pady=10)

# variable for file 
myFile = open("memory.txt", "r")
lines = myFile.readlines()
myFile.close()

# tasks
task1 = tk.Label(task_box, bg='white', fg='black', text=lines[0][:-1], font=('Verdana', 18), width=18)
task1.pack(pady=7)

task2 = tk.Label(task_box, bg='white', fg='black', text=lines[1][:-1], font=('Verdana', 18), width=18)
task2.pack(pady=7)

task3 = tk.Label(task_box, bg='white', fg='black', text=lines[2][:-1], font=('Verdana', 18), width=18)
task3.pack(pady=7)

task4 = tk.Label(task_box, bg='white', fg='black', text=lines[3][:-1], font=('Verdana', 18), width=18)
task4.pack(pady=7)

task5 = tk.Label(task_box, bg='white', fg='black', text=lines[4][:-1], font=('Verdana', 18), width=18)
task5.pack(pady=7)

task6 = tk.Label(task_box, bg='white', fg='black', text=lines[5][:-1], font=('Verdana', 18), width=18)
task6.pack(pady=7)

task7 = tk.Label(task_box, bg='white', fg='black', text=lines[6][:-1], font=('Verdana', 18), width=18)
task7.pack(pady=7)
# end of tasks

# delete buttons
del1 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task1))
del1.pack(pady=6, padx=5)

del2 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task2))
del2.pack(pady=6, padx=5)

del3 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task3))
del3.pack(pady=6, padx=5)

del4 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task4))
del4.pack(pady=6, padx=5)

del5 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task5))
del5.pack(pady=6, padx=5)

del6 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task6))
del6.pack(pady=6, padx=5)

del7 = tk.Button(rightFrame, text='Del', fg='black', bg='white', font=('Verdana', 13), highlightbackground="black",  highlightthickness=1, command=partial(delete_task, task7))
del7.pack(pady=6, padx=5)
# end of del buttons

root.mainloop()
