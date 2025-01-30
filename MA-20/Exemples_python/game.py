# 2048
# Ahmet KARABULUT
# creation de jeu 2048
# version 1.0
# date 28.01.2025

from tkinter import *
import tkinter.font

# 2 dimensions list with data


game=[[0,2,4,8],
      [16,32,2048,128],
      [256,512,1024,2048],
      [4096,8192,0,0]]
colors={
    0: "#ffffff",
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
labels=[[None,None,None,None],
        [None,None,None,None],
        [None,None,None,None],
        [None,None,None,None]]

dx=10 # horizontal distance between labels
dy=10 # vertical distance between labels

# réaffiche les bons textes et couleurw
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            bg_color = colors[game[line][col]]
            if game[line][col] >0:
                labels[line][col].config( text=game[line][col], bg=bg_color , borderwidth=1)
            else:
                labels[line][col].config( text="", bg=bg_color, borderwidth=0)



# Windows creation
win = Tk()
win.geometry("800x480")
win.title('2048')

# Title
lbl_title=Label(win,text="2048", height=3,   font=("Arial", 15))
lbl_title.pack()

frm_main=Frame(win,bd=5, relief="ridge", bg="lightblue")
frm_main.pack()


#ce boucle pour le game
for line in range(len(game)):
    frm= Frame(frm_main)# temporary frame
    frm.pack()

    # labels creation and position (1. Creation 2. position)
    for col in range(len(game[line])):
        # creation without placement
        labels[line][col] = Label (frm, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15))
        # label positionning in the windows
        labels[line][col].pack (side=LEFT, padx=dx, pady=dy)
        #print(labels[line][col])

display() #texte et couleurs


win.mainloop()
