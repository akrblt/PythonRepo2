# labels example
# JCY jan 2023
# dynamic creation of labels (grid)
# pb, all column must have the same width

from tkinter import *
import tkinter.font

# 2 dimensions list with data
words= [["tu", "te", "toi"],
        ["vous", "votre", "vos"],
        ["sans", "que", "qui"]]

# 2 dimensions list (empty, with labels in the future)
labels=[[None,None,None],[None,None,None],[None,None,None]]

dx=10 # horizontal distance between labels
dy=10 # vertical distance between labels

# Windows creation
win = Tk()
win.geometry("800x480")
win.title(' exemple labels positionnés par .grid')

# Title
Label(text="Placement labels par .grid",width=25, height=3,  font=("Arial", 15)).grid(row=0,column=0,padx=10,pady=10)

#labels creation and position (1. Creation 2. position)
for line in range(len(words)):
    for col in range(len(words[line])):
        # creation without placement
        labels[line][col] = Label (win, text =words[line][col], width=15, height=3, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFF00")
        # label positionning in the windows
        labels[line][col].grid (row=line+1,column=col,padx=dx,pady=dy)

win.mainloop()
