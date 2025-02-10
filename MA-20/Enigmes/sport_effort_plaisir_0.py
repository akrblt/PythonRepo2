# recherche de solutions
# problème de SPORT + EFFORT = PLAISIR
'''Chaque lettre est un chiffre différent''
# JCY pour illustration étudiants
'''
import tkinter as tk
from tkinter import messagebox
import time
import math

def sans_doublons(sequence):
    return len(sequence) == len(set(sequence))

def find_sep_smart_smart():
    try:

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []

        # Solution super smart
        p = 1
        e = 9
        l = 0
        for t in range(2, 9):
            r = (2 * t) % 10
            if r not in (p,e,l,t):
                i=(2*r+(2*t)//10)%10
                if i not in (p,e,l,t,r):
                    for o in range(2,9):
                        if o not in (p,e,l,t,r,i):
                            s=(2*o+(2*r)//10)%10
                            if s not in (p,e,l,t,r,i,o):
                                for a in range(2,9):
                                    if  a not in (p,e,l,t,r,i,o,s):
                                        for f in range(2,9):
                                            if f not in (p,e,l,t,r,i,o,s,a):


                                                            numbers_tested += 1
                                                            sport = t + 10 * r + 100 * o + 1000 * p + 10000 * s
                                                            effort = t + 10 * r + 100 * o + 11000 * f + 100000 * e
                                                            plaisir = r + 1010 * i + 100 * s + 10000 * a + 100000 * l + 1000000 * p
                                                            if sport + effort == plaisir:

                                                                # s'ils sont tous différents
                                                                solutions.append((sport, effort, plaisir))

        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Nombres trouvés : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun nombre trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def find_sep_smart():
    try:

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []


        # Solution brute mais améliorée
        p = 1
        e=9
        l=0

        for a in range(2, 9):
            for f in range(2, 9):
                if f !=a: # f different de a
                    for i in range(2, 9):
                        if i not in (f,a): # i doit etre different de f et a
                            for o in range(2, 9):
                                if o not in (f,a,i):
                                    for r in range(2, 9):
                                        if r not in (o,f,a,i):
                                            for s in range(2, 9):
                                                if s not in (r,o,f,a,i):
                                                    for t in range(2, 9):
                                                        if t not in (s,r,o,f,a,i):
                                                            numbers_tested += 1
                                                            sport = t + 10 * r + 100 * o + 1000 * p + 10000 * s
                                                            effort = t + 10 * r + 100 * o + 11000 * f + 100000 * e
                                                            plaisir = r + 1010 * i + 100 * s + 10000 * a + 100000 * l + 1000000 * p
                                                            if sport + effort == plaisir:
                                                                # s'ils sont tous différents
                                                                solutions.append((sport, effort, plaisir))

        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Nombres trouvés : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun nombre trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def find_sep():
    try:

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = []

        # Trouver la solution avec lettres a,e,f,i,l,o,p,r,s,t
        # Solution brute force un peu stupide
        p=1
        for e in range(0,10):
            for l in range(0,10):
                for a in range(0, 10):
                    for f in range(0, 10):
                        for i in range(0, 10):
                            for o in range(0, 10):
                                for r in range(0, 10):
                                    for s in range(0, 10):
                                        for t in range(0,10):
                                            numbers_tested += 1
                                            sport= t + 10*r + 100*o + 1000*p + 10000*s 
                                            effort = t + 10*r + 100*o + 11000 * f + 100000*e
                                            plaisir = r +1010*i + 100*s + 10000*a + 100000*l + 1000000 *p
                                            if sport + effort == plaisir :
                                                # s'ils sont tous différents
                                                solutions.append((sport, effort, plaisir))

        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Nombres testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"sport+effort=plaisir : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions:  # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun nombre trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))
# Interface tkinter
root = tk.Tk()
root.title("Recherche de sport + effort= plaisir")

# Labels et champs d'entrée

# Boutons pour calculer
btn_calculate = tk.Button(root, text="sport brut (9 chiffres)", command=find_sep)
btn_calculate.grid(row=2, column=0,  pady=10)
btn_calculate_smart = tk.Button(root, text="sport malins (7 chiffres)", command=find_sep_smart)
btn_calculate_smart.grid(row=2, column=1,  pady=10)
btn_calculate_smart_smart = tk.Button(root, text="sport très malin", command=find_sep_smart_smart)
btn_calculate_smart_smart.grid(row=3, column=0,  pady=10)

# Zone de texte pour afficher les résultats (dans un frame)
frame_output = tk.Frame(root)
frame_output.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

text_output = tk.Text(frame_output, width=50, height=15, wrap=tk.WORD)
scrollbar = tk.Scrollbar(frame_output, command=text_output.yview)
text_output.config(yscrollcommand=scrollbar.set)

text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lancement de l'application
root.mainloop()
