# labels example
# JCY jan 2023
# dynamic creation of labels (pack)

from tkinter import *
import tkinter.font

# 2 dimensions list with data


game=[[2,2,4,8],[16,32,0,128],[256,512,1024,2048],[4096,8192,2,2]]
colors={
    0: "#fbf8f8",
    2: "#f7e50c",
    4: "#f5d99e",
    8: "#f7ac78",
    16: "#de876a",
    32: "#b35231",
    64: "#a40f26",
    128: "#c1efa8",
    256: "#348109",
    512: "#38761d",
    1024: "#9fc5f8",
    2048: "#6fa8dc",
    4096: "#b4a7d6",
    8192: "#c27ba0",
}

# 2 dimensions list (empty, with labels in the future)
labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

dx=10 # horizontal distance between labels
dy=10 # vertical distance between labels

# réaffiche les bons textes et couleurw
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            bg_color = colors.get(game[line][col], "#FFFFFF")
            labels[line][col].config( text=game[line][col], bg=bg_color)



# Windows creation
win = Tk()
win.geometry("800x480")
win.title(' 2048')

# Title
lbl_title=Label(win,text="2048", height=3,  font=("Arial", 15))
lbl_title.pack()

frm_main=Frame(win,bd=5, relief="ridge", bg="lightblue")
frm_main.pack()

for line in range(len(game)):
    frm= Frame(frm_main)# temporary frame
    frm.pack()

    # labels creation and position (1. Creation 2. position)
    for col in range(len(game[line])):
        # creation without placement
        labels[line][col] = Label (frm, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15))
        # label positionning in the windows
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)

display() #texte et couleurs


win.mainloop()
