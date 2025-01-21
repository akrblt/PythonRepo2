# labels example
# JCY jan 2023
# dynamic creation of labels

from tkinter import *
import tkinter.font

# 2 dimensions list with data
words= [["tu", "te", "toi"],
        ["vous", "votre", "vos"],
        ["sans", "que", "qui"]]

# 2 dimensions list (empty, with labels in the future)
labels=[[None,None,None],[None,None,None],[None,None,None]]

x0=25 # horizontal beginning of labels
y0=100 # vertical beginning of labels
width=200 # horizontal distance between labels
height=90 # vertical distance between labels

# Windows creation
win = Tk()
win.geometry("800x480")
win.title(' exemple labels positionnés par .place')
# Title
Label(text="Placement labels par .place",width=25, height=3, font=("Arial", 15)).place(x=50, y=25)

#labels creation and position (1. Creation 2. position)
for line in range(len(words)):
    for col in range(len(words[line])):
        # creation without placement
        labels[line][col] = Label (win,text =words[line][col], width=15, height=3, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFF00")
        # label positionning in the windows
        labels[line][col].place(x=x0 + width * col, y=y0 + height * line)

win.mainloop()
