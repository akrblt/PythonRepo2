import tkinter as tk
from tkinter import *


win = tk.Tk()
win.title("Login / Register avec grid")
win.geometry("400x700")
win.resizable(False, False)
win.configure(bg="#FFFFFF")


win.columnconfigure(0, weight=1)  # vide
win.columnconfigure(1, weight=2)  # contenu ici
win.columnconfigure(2, weight=1)  # vide

# title
label_title = Label(win, text="Login", font=("Arial", 30), bg="#FFFFFF", fg="#000000")
label_title.grid(column=1, row=0, pady=(30, 20))

# Email label
email_label = Label(win, text="Enter your email", font=("Arial", 15), bg="#FFFFFF", fg="#000000")
email_label.grid(column=1, row=1, sticky="nsew", padx=10)
# pour utilise sticky
#n (north) , s(south), e (east) , w (west)
# ns , ew , nsew , ne , sw
# nsew (remplit toute la cellule)

# Email entry
email_entry = Entry(win, width=40)
email_entry.grid(column=1, row=2, pady=5)

# Password label
password_label = Label(win, text="Enter your password", font=("Arial", 15), bg="#FFFFFF", fg="#000000")
password_label.grid(column=1, row=3, sticky="nsew", padx=10, pady=(30, 0))

# Password entry
password_entry = Entry(win, width=40, show="*")
password_entry.grid(column=1, row=4, pady=5)

# Login buton
btn_login = Button(win, text="Log in", width=15, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_login.grid(column=1, row=5, pady=(60, 10))

# Register buton
btn_register = Button(win, text="Register", width=15, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_register.grid(column=1, row=6, pady=10)

win.mainloop()
