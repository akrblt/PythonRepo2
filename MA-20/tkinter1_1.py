# intro à tkinter
# JP Chavey (20 jan 2025)
# pour classe SI-CA1a
from tkinter import *

# Fonction pour gérer le clic sur le bouton
def afficher_message():
    # Récupérer les valeurs des champs d'entrée
    prenom = entry_prenom.get()
    nom = entry_nom.get()
    # Modifier le texte du label (2 versions)
    # label_message.config(text=f"Bonjour {prenom} {nom}")
    label_message.config(text = "Bonjour " + prenom + " " + nom )

# Création de la fenêtre principale
root = Tk()
root.title("Exemple Tkinter")
root.geometry("600x400")

# Widgets
label_nom = Label(root, text="Nom :")
label_nom.grid(row=0, column=0, padx=10, pady=10)

entry_nom = Entry(root)
entry_nom.grid(row=0, column=1, padx=10, pady=10)

label_prenom = Label(root, text="Prénom :")
label_prenom.grid(row=1, column=0, padx=10, pady=10)

entry_prenom = Entry(root)
entry_prenom.grid(row=1, column=1, padx=10, pady=10)
entry_prenom.insert(0,"Sam")  # Valeur par défaut pour prénom

label_message = Label(root, text="", bg="lightblue", width=40, height=2)
label_message.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

bouton_afficher = Button(root, text="Afficher", command=afficher_message)
bouton_afficher.grid(row=3, column=0, columnspan=2, pady=10)

# Boucle principale
root.mainloop()