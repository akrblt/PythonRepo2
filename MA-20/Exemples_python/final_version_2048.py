# 2048
# Ahmet KARABULUT
# creation de jeu 2048
# version 1.1
# date 04.03.2025

import random
from tkinter import *
import tkinter.font
from tkinter import messagebox

# 2 dimensions list with data
game = [
    [0, 2, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0]
]

colors = {
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
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

dx = 10  # horizontal distance between labels
dy = 10  # vertical distance between labels

score = 0  # Initial score
won = False  # Flag to check if the player has won

# Reaffiche les bons textes et couleurs
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            bg_color = colors[game[line][col]]
            if game[line][col] > 0:
                labels[line][col].config(text=game[line][col], bg=bg_color, borderwidth=1)
            else:
                labels[line][col].config(text="", bg=bg_color, borderwidth=0)


def pack4(a, b, c, d):
    nm = 0

    if c == 0 and d > 0:
        c, d = d, 0
        nm += 1
    if b == 0 and c > 0:
        b, c, d = c, d, 0
        nm += 1
    if a == 0 and b > 0:
        a, b, c, d = b, c, d, 0
        nm += 1

    if a == b and a > 0:
        nm += 1
        a *= 2
        global score
        score += a
        b, c, d = c, d, 0
    if b == c and b > 0:
        nm += 1
        b *= 2
        score += b
        c, d = d, 0
    if c == d and d > 0:
        nm += 1
        c *= 2
        score += c
        d = 0

    return [a, b, c, d], nm


def add_random_tile():
    # Adds a random tile (value 2) in an empty position.
    empty_cells = []
    for row in range(4):
        for col in range(4):
            if game[row][col] == 0:
                empty_cells.append((row, col))

    if len(empty_cells) != 0:
        (row, col) = random.choice(empty_cells)
        game[row][col] = 2 if random.random() < 0.7 else 4
    else:
        print("C'est fini")
    display()


def game_over():
    messagebox.showinfo("Game Over", "Vous avez perdu")


def check_win():
    global won
    if not won:
        # This function is called when a 2048 tile is reached.
        messagebox.showinfo("You Win!", "Congratulations, you reached 2048!")
        won = True  # Set the flag to True, indicating that the player has won
        display()  # Update display after winning


def move_down():
    tot_mov = 0
    for col in range(4):
        [game[3][col], game[2][col], game[1][col], game[0][col]], nmove = pack4(game[3][col], game[2][col], game[1][col], game[0][col])
        tot_mov = tot_mov + nmove
    return tot_mov


def move_up():
    tot_mov = 0
    for col in range(4):
        [game[0][col], game[1][col], game[2][col], game[3][col]], nmove = pack4(game[0][col], game[1][col], game[2][col], game[3][col])
        tot_mov = tot_mov + nmove
    return tot_mov


def move_left():
    tot_mov = 0
    for line in range(4):
        [game[line][0], game[line][1], game[line][2], game[line][3]], nmove = pack4(game[line][0], game[line][1], game[line][2], game[line][3])
        tot_mov += nmove
    return tot_mov


def move_right():
    tot_mov = 0
    for line in range(4):
        [game[line][3], game[line][2], game[line][1], game[line][0]], nmove = pack4(game[line][3], game[line][2], game[line][1], game[line][0])
        tot_mov += nmove
    return tot_mov


# Check if the game is lost
def lost():
    # Check if there are any empty tiles (i.e., if there are no 0s)
    def nb_empty_tiles():
        for row in range(4):
            for col in range(4):
                if game[row][col] == 0:  # Found an empty tile
                    return True
        return False

    # Check if there are any possible merges (if two adjacent tiles are the same)
    def no_merge_possible():
        for row in range(4):
            for col in range(4):
                # Check horizontal merge possibility
                if col < 3 and game[row][col] == game[row][col + 1]:
                    return True
                # Check vertical merge possibility
                if row < 3 and game[row][col] == game[row + 1][col]:
                    return True
        return False

    # If there are no empty tiles and no possible merges, the game is over
    if not nb_empty_tiles() and not no_merge_possible():
        game_over()


# Affectation des touches aux fonctions, q pour quitter, le reste pour "tasser" dans une certaine direction
def key_pressed(event):
    touche = event.keysym  # récupérer le symbole de la touche
    moved = False
    if touche == "Right" or touche == "d" or touche == "D":
        moved = move_right()
    elif touche == "Left" or touche == "a" or touche == "A":
        moved = move_left()
    elif touche == "Up" or touche == "w" or touche == "W":
        moved = move_up()
    elif touche == "Down" or touche == "s" or touche == "S":
        moved = move_down()
    elif touche == "Q" or touche == "q":
        result = messagebox.askokcancel("Confirmation", "Vraiment quitter ?")
        if result:
            quit()

    if moved:
        add_random_tile()  # Add a new tile after the move
        display()  # Update the display
        lost()  # Check if the game is over
        # Check for win condition
        for row in game:
            if 2048 in row:
                check_win()  # Call check_win function when 2048 tile is found


# Windows creation
win_window = Tk()  # Renaming 'win' to 'win_window' to avoid conflict with the 'win()' function
win_window.geometry("800x480")
win_window.title('2048')

# Skor
#score_label = Label(win_window, text=f"Skor: {score}", height=3, font=("Arial", 15))
#score_label.pack()

# Title
lbl_title = Label(win_window, text="2048", height=3, font=("Arial", 15))
lbl_title.pack()

frm_main = Frame(win_window, bd=5, relief="ridge", bg="lightblue")
frm_main.pack()

# Create game board grid
for line in range(len(game)):
    frm = Frame(frm_main)  # Temporary frame
    frm.pack()

    # Labels creation and position (1. Creation 2. position)
    for col in range(len(game[line])):
        # Create without placement
        labels[line][col] = Label(frm, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15))
        # Label positioning in the window
        labels[line][col].pack(side=LEFT, padx=dx, pady=dy)

# Display initial board
display()

win_window.bind('<Key>', key_pressed)  # Handle key events
win_window.mainloop()
