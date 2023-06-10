from tkinter import *
from pygame import mixer
import os

root = Tk()
root.geometry('600x420')
root.resizable(0, 0)
root.title('Music Player')

states = StringVar()

mixer.init()


def playsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0', END)
    songtrack.insert('1.0', playlist.get(ACTIVE))
    songtrack.config(state=DISABLED)

    states.set("-Playing")

    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

def stopsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0', END)
    songtrack.config(state=DISABLED)

    states.set("-Stppped")

    mixer.music.stop()
    
def pausesong():
    states.set("-Paused")

    mixer.music.pause()

def unpausesong():
    states.set("-Playing")

    mixer.music.unpause()


trackframe = LabelFrame(root, text='Song Track', font=('Arial', 15, 'bold'), bg='#a887e0', fg='black', bd=5, relief=GROOVE)
trackframe.place(x=0, y=200, width=600, height=120)

songtrack = Text(trackframe, width=40, height=2, font=('Arial', 15), bg='#8a1553', fg='white', state=DISABLED)
songtrack.grid(row=0, column=0, padx=10, pady=5)

trackstates = Label(trackframe, textvariable=states, font=('Sans-serif', 12, 'bold'), bg='#8a1553', fg='white')
trackstates.grid(row=0, column=1, padx=10, pady=5)

buttonframe = LabelFrame(root, text='Control Panel', font=('Arial', 15, 'bold'), bg='#a887e0', fg='black', bd=5, relief=GROOVE, pady=10)
buttonframe.place(x=0, y=320, width=600, height=100)

playbtn = Button(buttonframe, text='Play', width=8, height=1, font=('Arial', 16), fg='white', bg='green', command=playsong)
playbtn.grid(row=0, column=0, padx=10, pady=5)

pasuebtn = Button(buttonframe, text='Pause', width=8, height=1, font=('Arial', 16), fg='white', bg='orange', command=pausesong)
pasuebtn.grid(row=0, column=1, padx=10, pady=5)

unpasuebtn = Button(buttonframe, text='UnPause', width=8, height=1, font=('Arial', 16), fg='white', bg='blue', command=unpausesong)
unpasuebtn.grid(row=0, column=2, padx=10, pady=5)

stopbtn = Button(buttonframe, text='Stop', width=8, height=1, font=('Arial', 16), fg='white', bg='red', command=stopsong)
stopbtn.grid(row=0, column=3, padx=10, pady=5)

songsframe = LabelFrame(root, text='Songs Playlist', font=('Arial', 16, 'bold'), bg='gray', fg='black', bd=5, relief=GROOVE)
songsframe.place(x=0, y=0, width=600, height=200)

scroll_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, selectbackground='gold', selectmode=SINGLE, font=('Arial', 12), bg='silver', fg='navyblue', bd=5, relief=GROOVE, yscrollcommand=scroll_y.set)
scroll_y.config(command=playlist.yview)
scroll_y.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH)

os.chdir(r"E:\Music")
songtracks = os.listdir()
for track in songtracks:
    if ".mp3" in track:
        playlist.insert(END, track)
    else:
        pass

root.mainloop()