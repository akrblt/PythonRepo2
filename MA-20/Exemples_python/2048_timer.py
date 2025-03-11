# 2048
# Ahmet KARABULUT
# creation de jeu 2048
# version 1.1
# date 04.03.2025

import random
import time
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

# Timer variables
timer_label = None
start_time = None
timer_running = False

# Display the game board
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            bg_color = colors[game[line][col]]
            if game[line][col] > 0:
                labels[line][col].config(text=game[line][col], bg=bg_color, borderwidth=1)
            else:
                labels[line][col].config(text="", bg=bg_color, borderwidth=0)

# Timer functions
def update_timer():
    if timer_running:
        elapsed_time = int(time.time() - start_time)
        timer_label.config(text=f"Süre: {elapsed_time} saniye")
        win_window.after(1000, update_timer)

def start_timer():
    global start_time, timer_running
    start_time = time.time()
    timer_running = True
    update_timer()

def stop_timer():
    global timer_running
    timer_running = False

# Move and merge logic
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

# Add a random tile
def add_random_tile():
    empty_cells = [(row, col) for row in range(4) for col in range(4) if game[row][col] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        game[row][col] = 2 if random.random() < 0.7 else 4
    display()

# Game over
def game_over():
    stop_timer()
    messagebox.showinfo("Game Over", "Vous avez perdu")

# Check for win
def check_win():
    global won
    if not won:
        stop_timer()
        messagebox.showinfo("You Win!", "Congratulations, you reached 2048!")
        won = True
        display()

# Move functions
def move_down():
    return sum(pack4(game[3][col], game[2][col], game[1][col], game[0][col])[1] for col in range(4))

def move_up():
    return sum(pack4(game[0][col], game[1][col], game[2][col], game[3][col])[1] for col in range(4))

def move_left():
    return sum(pack4(game[line][0], game[line][1], game[line][2], game[line][3])[1] for line in range(4))

def move_right():
    return sum(pack4(game[line][3], game[line][2], game[line][1], game[line][0])[1] for line in range(4))

# Check if game is lost
def lost():
    if not any(0 in row for row in game) and not any(game[row][col] == game[row][col + 1] or game[row][col] == game[row + 1][col] for row in range(3) for col in range(3)):
        game_over()

# Key press handling
def key_pressed(event):
    touche = event.keysym
    moved = False
    if touche in ("Right", "d", "D"):
        moved = move_right()
    elif touche in ("Left", "a", "A"):
        moved = move_left()
    elif touche in ("Up", "w", "W"):
        moved = move_up()
    elif touche in ("Down", "s", "S"):
        moved = move_down()
    elif touche in ("Q", "q"):
        if messagebox.askokcancel("Confirmation", "Vraiment quitter ?"):
            quit()
    if moved:
        add_random_tile()
        display()
        lost()
        if any(2048 in row for row in game):
            check_win()

# Window setup
win_window = Tk()
win_window.geometry("800x480")
win_window.title('2048')

lbl_title = Label(win_window, text="2048", height=3, font=("Arial", 15))
lbl_title.pack()

timer_label = Label(win_window, text="Süre: 0 saniye", height=2, font=("Arial", 15))
timer_label.pack()

frm_main = Frame(win_window, bd=5, relief="ridge", bg="lightblue")
frm_main.pack()

for line in range(4):
    frm = Frame(frm_main)
    frm.pack()
    for col in range(4):
        labels[line][col] = Label(frm, width=6, height=3, font=("Arial", 15))
        labels[line][col].pack(side=LEFT, padx=dx, pady=dy)

display()
start_timer()

win_window.bind('<Key>', key_pressed)
win_window.mainloop()
