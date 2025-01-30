#
# Name:			python_to_sql_TK.py
# Author:		Nathan Filipowitz
# Date:			Thu Jan 30 2025
# Version:		1.0
# Description:	Programme capable de charger un fichier, convertir les données en syntaxe SQL, puis sauver la conversion en script .sql.	
#

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

def headers_to_sql(list):
    return str(list).replace(";", "").replace("'", "").replace("[", "").replace("]", "")

def data_to_sql(string):
    return (string).replace(";", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "") 

# Cette fonction traite chaque ligne (tableau lines)
# headers est un tableau qui contient la première ligne (entêtes splités par ";")
# data_rows est un tableau dont le premier indice est la ligne, et le second l'indice de colonne
# un traitement spécial est fait pour NULL et les nombres pour ne pas mettre de "'"
def generate_sql_from_text():
    print(data_to_sql('Bonjour'))
    table_name = entry_table.get()  # Vous pouvez personnaliser ou demander une saisie
    sql_queries = []
    # prendre le contenu de text_widget dans une variable
    content = text_widget.get("1.0", tk.END).strip()
    # prendre un tableau des lignes (on split sur \n)
    content_rows = content.split('\n')
    # on éclate la première ligne (split sur ;) dans un tableau (headers)
    headers = content_rows[0].split(';')
    # pour chaque ligne de data_rows
    for line in content_rows[1:]:
    #   si la longueur est celle de headers (notamment à cause de la fin de fichier)
        if len(line) > 0:
    #   on génère l'entête INSERT INTO table (champ1,champ2...)
            sql_widget.insert(tk.END, f"INSERT INTO {table_name}({headers_to_sql(headers)}) VALUES (")
    #   pour chaque données
        cols=line.split(';');
        for data in cols:
    #       si c'est NULL ou un nombre
            if data == "NULL" or is_number(data):
    #           on insère donnée, (sans apostrophe)
                sql_widget.insert(tk.END, f"{data},")
    #       sinon
            else:
    #           on insère "donnée", (avec apostrophe)
                sql_widget.insert(tk.END, f"'{data}',")
        sql_widget.insert(tk.END, f");\n")
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
