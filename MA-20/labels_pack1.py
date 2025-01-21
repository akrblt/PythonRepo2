# labels example
# JCY jan 2023
# dynamic creation of labels (pack)

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
win.title(' exemple labels positionnés par .pack and frame')

# Title
lbl_title=Label(win,text="Placement labels par .pack and frame", height=3,  font=("Arial", 15))
lbl_title.pack()

for line in range(len(words)):
    frm=Frame(win) # temporary frame
    frm.pack()

    for col in range(len(words[line])):
        # creation without placement
        labels[line][col] = Label (frm,text =words[line][col], width=15, height=3, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFF00")
        # label positionning in the windows
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)

#labels creation and position (1. Creation 2. position)


win.mainloop()
