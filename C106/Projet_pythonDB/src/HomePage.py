import tkinter as tk
from tkinter import *

# title position
x0_title, y0_title = 80, 25

# homePage image position
x0_hp_image, y0_hp_image = 60, 100

# concerts button position
x0_btn_concerts, y0_btn_concerts = 140, 295

# bands button position
x0_btn_bands, y0_btn_bands = 140, 360

# my reservations button position
x0_btn_myRes, y0_btn_myRes = 110, 425

# login button position
x0_btn_login, y0_btn_login = 110, 530

# creating the window
win = tk.Tk()
win.title("Home Page")
win.geometry("400x700")
win.resizable(False, False)

# Title
label_title = Label(text="Festival_Title", width=10, height=1, font=("Arial", 30), bg="#FFFFFF", fg="#000000")
label_title.place(x=x0_title, y=y0_title)

# homePage image
hp_image = tk.Label(win, text="Image", width=25, height=7, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
hp_image.place(x=x0_hp_image, y=y0_hp_image)

# button to see all concerts
btn_concerts = tk.Button(win, text="Concerts", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_concerts.place(x=x0_btn_concerts, y=y0_btn_concerts)

# button to see all bands
btn_bands = tk.Button(win, text="Bands", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_bands.place(x=x0_btn_bands, y=y0_btn_bands)

# button to see my reservations
btn_myRes = tk.Button(win, text="My reservations", width=15, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_myRes.place(x=x0_btn_myRes, y=y0_btn_myRes)

# login button
btn_login = tk.Button(win, text="Log in / Register", width=15, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_login.place(x=x0_btn_login, y=y0_btn_login)

win.mainloop()