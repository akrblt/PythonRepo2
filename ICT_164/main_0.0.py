# Convertisseur de csv en sql (insert)
# JP Chavey pour SI-CA1a
# 22 jan 2025

import tkinter as tk
from tkinter import filedialog, messagebox

# fonction qui renvoie true si la données est un nombre entier ou décimal
# (si la conversion en float n'échoue pas)
def is_number(element):
    try:
        float(element)  # Tente de convertir l'élément en float
        return True
    except ValueError:
        return False

# Cette fonction charge un fichier quelconque (en principe un csv, mais accepte tout)
# et l'affiche dans le widget text du haut.
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt *.csv"), ("All Files", "*.*")])
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
        messagebox.showinfo("Succès", "Fichier chargé avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de charger le fichier.\n{e}")


# Cette fonction traite chaque ligne (tableau lines)
# headers est un tableau qui contient la première ligne (entêtes splités par ";")
# data_rows est un tableau dont le premier indice est la ligne, et le second l'indice de colonne
# un traitement spécial est fait pour NULL et les nombres pour ne pas mettre de "'"
def generate_sql_from_text():

    #content= entry_table.get()  # Vous pouvez personnaliser ou demander une saisie
    sql_queries = []
    # prendre le contenu de text_widget dans une variable
    content=text_widget.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Attention" , "Le widget texte est vide")
        return
    # prendre un tableau des lignes (on split sur \n)
    lines = content.split("\n")
    if not lines:
        messagebox.showwarning("Attention" , "Le fichier est vide")
        return

    # on éclate la première ligne (split sur ;) dans un tableau (headers)
    headers = lines[0].split(";")
    # on éclate les lignes suivantes dans un tableau (data_rows)
    data_rows =[]
    for line in lines[1:]:
        if not line.strip():
            continue
    data = line.split(';')
    if len(data) != len(headers):
        messagebox.showwarning("Attention", f"La ligne '{line}' ne correspond pas au nombre d'en-têtes.")


    # pour chaque ligne de data_rows
    #   si la longueur est celle de headers (notamment à cause de la fin de fichier)
    #   on génère l'entête INSERT INTO table (champ1,champ2...)
    sql_query = f"INSERT INTO {lbl_table} ({', '.join(headers)}) VALUES ({', '.join()});"
    sql_queries.append(sql_query)
    #   pour chaque données
    #       si c'est NULL ou un nombre
    #           on insère donnée, (sans apostrophe)
    #       sinon
    #           on insère "donnée", (avec apostrophe)
    #   on retire la dernière virgule
    #   on ajoute ); la dernière parenthèse et le point virgule
    #   on ajoute la requête à la fin du sql_widget avec un \n

def save_sql():
    content = sql_widget.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Attention", "Le widget SQL est vide.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("SQL Files", "*.sql"), ("All Files", "*.*")])
    if not file_path:
        return

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Succès", "Fichier SQL enregistré avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'enregistrer le fichier.\n{e}")

# Initialisation de l'interface
root = tk.Tk()
root.title("Générateur SQL à partir de CSV")


# Widgets
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

load_button = tk.Button(button_frame, text="Charger fichier", command=load_file)
load_button.pack(side="left", padx=5)

generate_button = tk.Button(button_frame, text="Générer SQL", command=generate_sql_from_text)
generate_button.pack(side="left", padx=5)

save_button = tk.Button(button_frame, text="Enregistrer SQL", command=save_sql)
save_button.pack(side="left", padx=5)

lbl_table=tk.Label(button_frame, text="Nom de la table :")
lbl_table.pack(side="left", padx=5)

entry_table=tk.Entry(button_frame)
entry_table.insert(0,"matable")
entry_table.pack(side="left",padx=3)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

text_widget = tk.Text(frame, width=120, height=15, wrap="none")
text_widget.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

sql_widget = tk.Text(frame, width=120, height=15, wrap="none")
sql_widget.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")



root.mainloop()
