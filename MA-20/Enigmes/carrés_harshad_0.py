# recherche de solutions
# problème des carrés harshad (ex: 2025, carré et divisible par la somme de ses chiffres)
# JCY pour illustration étudiants

import tkinter as tk
from tkinter import messagebox
import time
import math

def find_square_harshad():
    try:
        # Récupérer les bornes min et max
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise ValueError("Les bornes doivent être des entiers positifs et min ≤ max.")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []


        # Trouver les carrés harshad (ex: 2025)
        # Solution brute force un peu stupide
        for a in range(min_val, max_val + 1):

            numbers_tested += 1
            square_a = int(math.sqrt(a)) # prendre la racine de a (entière)
            # somme des chiffres
            sum_of_digits=0
            for digit in str(a):
                sum_of_digits +=int(digit) # calculer la somme des chiffres

            if a % sum_of_digits==0 and square_a ** 2 == a: #si carré harshad
                    solutions.append(a)

        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Carrés harshad trouvés : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun carré harshad trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def find_square_harshad_smart():
    try:
        # Récupérer les bornes min et max
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise ValueError("Les bornes doivent être des entiers positifs et min ≤ max.")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []

        # Trouver carrés harshad
        # solution plus maline à programmer ici
        for n in range(int(math.sqrt(min_val)), int(math.sqrt(max_val ))+1):

            numbers_tested += 1

            a=n**2
            sum_of_digits=0
            for digit in str(a):
                sum_of_digits +=int(digit)
            if a % sum_of_digits==0 and n ** 2 == a: solutions.append(a)



        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Carrés harshad trouvés : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions:
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun carré harshad trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


# Interface tkinter
root = tk.Tk()
root.title("Recherche de carrés harshad")

# Labels et champs d'entrée
tk.Label(root, text="Valeur minimale (min):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_min = tk.Entry(root)
entry_min.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Valeur maximale (max):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_max = tk.Entry(root)
entry_max.grid(row=1, column=1, padx=10, pady=5)
entry_min.insert(0, "1000")  # Valeur par défaut pour min
entry_max.insert(0, "1000000")  # Valeur par défaut pour max

# Boutons pour calculer
btn_calculate = tk.Button(root, text="Carrés harshad bruts", command=find_square_harshad)
btn_calculate.grid(row=2, column=0,  pady=10)
btn_calculate_smart = tk.Button(root, text="Carrés harshad malins", command=find_square_harshad_smart)
btn_calculate_smart.grid(row=2, column=1,  pady=10)

# Zone de texte pour afficher les résultats (dans un frame)
frame_output = tk.Frame(root)
frame_output.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

text_output = tk.Text(frame_output, width=50, height=15, wrap=tk.WORD)
scrollbar = tk.Scrollbar(frame_output, command=text_output.yview)
text_output.config(yscrollcommand=scrollbar.set)

text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lancement de l'application
root.mainloop()
