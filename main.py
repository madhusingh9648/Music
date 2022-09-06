from msilib.schema import ListBox
import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg='black')

rootpath = "C:\\Users\hp\Desktop\song"
pattern = "*.mp3"

mixer.init()


prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

def select():
    label.config(text = ListBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + ListBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    ListBox.select_clear('active')

def play_next():
    next_song = ListBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = ListBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    ListBox.select_clear(0, 'end')
    ListBox.activate(next_song)
    ListBox.select_set(next_song)

def play_prev():
    next_song = ListBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = ListBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    ListBox.select_clear(0, 'end')
    ListBox.activate(next_song)
    ListBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


ListBox = tk.Listbox(canvas, fg= "cyan", bg="black", width = 100)
ListBox.pack(padx = 15, pady = 15) 

label = tk.Label(canvas, text ='',bg= 'black', fg = 'yellow')
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth= 0, command= play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left') 

stopButton = tk.Button(canvas, text = "Stop", image = stop_img, bg = 'black', borderwidth= 0, command= stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play", image = play_img, bg = 'black', borderwidth= 0, command= select)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", image = pause_img, bg = 'black', borderwidth= 0, command= pause_song)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image = next_img, bg = 'black', borderwidth= 0, command= play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')



for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        ListBox.insert('end',filename)

canvas.mainloop() 