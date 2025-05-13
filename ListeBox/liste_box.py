import tkinter as tk
from tkinter import messagebox

def listbox_example():
    def on_select(event):
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            selected = concerts[index]
            messagebox.showinfo("Selection", f"Selected concert:\n{selected}")

    concerts = ["Rock Night - June 12", "Jazz Evening - July 1", "Pop Fest - August 20"]

    win = tk.Tk()
    win.title("Listbox Example")

    label = tk.Label(win, text="Select a concert from the list:")
    label.pack(pady=10)

    listbox = tk.Listbox(win, width=40, height=5)
    for concert in concerts:
        listbox.insert(tk.END, concert)
    listbox.pack(pady=10)
    listbox.bind("<<ListboxSelect>>", on_select)

    win.mainloop()

# Bu satır olmazsa pencere açılmaz
listbox_example()
