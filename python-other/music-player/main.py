from pygame import mixer
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.resizable(False, False)
root.title("Octavio's MP3")
root.geometry("400x500")
root['bg'] = "#bb4430"

current_volume = 0.5
option = 1

# functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Select a music file")
    song_name = filename.split("/")
    song_title.configure(text=song_name[-1])

    try:
        mixer.init()
        mixer.music.load(filename)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        volume.configure(text="Volume : {}".format(current_volume))
    except Exception as error:
        song_title.configure(text="Error Playing Song")
        print(error)


def decrease_volume():
    try:
        global current_volume
        if current_volume > 0:
            current_volume -= 0.1
        if current_volume < 0:
            current_volume = 0
        mixer.music.set_volume(current_volume)
        current_volume = round(current_volume, 1)
        volume.configure(text="Volume : {}".format(current_volume))
    except Exception as error:
        print(error)
        song_title.configure(text="Song not playing.")


def increase_volume():
    try:
        global current_volume
        if current_volume < 1:
            current_volume += 0.1
        if current_volume >= 1:
            current_volume = 1
        mixer.music.set_volume(current_volume)
        current_volume = round(current_volume, 1)
        volume.configure(text="Volume : {}".format(current_volume))
    except Exception as error:
        print(error)
        song_title.configure(text="Song not playing.")


def pause_res():
    global option
    try:
        if option == 1:
            mixer.music.pause()
            option -= 1
        else:
            mixer.music.unpause()
            option += 1

    except Exception:
        song_title.configure(text="No song is playing")


# bottom frame content
bottomFrame = tk.Frame(root, bg='#bb4430')
bottomFrame.pack(side="bottom")

# buttons
select = tk.Button(bottomFrame, text='Select Song', fg="#efe6dd", bg="#231f20", highlightbackground="#efe6dd", highlightthickness=6, font=("Verdana", 15), command=play_song)
select.grid(pady=20, row=4, columnspan=8)

vol_down = tk.Button(bottomFrame, text="-", fg='#efe6dd', bg="#231f20", font=("Verdana", 18), highlightthickness=0, command=decrease_volume)
vol_down.grid(row=3, column=0)

pause_res = tk.Button(bottomFrame, text="ll", fg='#efe6dd', bg="#231f20", font=("Verdana", 30), highlightthickness=0, command=pause_res)
pause_res.grid(row=3, column=3, padx=20)

vol_up = tk.Button(bottomFrame, text="+", fg='#efe6dd', bg="#231f20", font=("Verdana", 18), highlightthickness=0, command=increase_volume)
vol_up.grid(row=3, column=6)

volume = tk.Label(bottomFrame, text="Volume: ", font=("Verdana", 10), bg="#231f20", fg="#efe6dd")
volume.grid(row=5, column=3)

# top frame content
top_frame = tk.Frame(root, bg="#efe6dd", highlightbackground='#231f20', highlightthickness=3)
top_frame.pack(side="top", pady=60)

song_title = tk.Label(top_frame, text='Song Name Example', fg="#231f20", bg="white", font=('MS Sans Serif', 20))
song_title.pack(pady=70, padx=20)


root.mainloop()
