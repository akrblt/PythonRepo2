# recherche de solutions
# problème des briques
# ahmet

import tkinter as tk
import bisect
from tkinter import messagebox
import time
import math


def find_brique():
    try:
        # Récupérer les bornes min et max
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise ValueError("Les bornes doivent être des entiers positifs et min ≤ max.")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = set()



        # Trouver les triangles rectangles(ex: 2025)
        # Solution brute force un peu stupide
        for a in range(1, max_val + 1):
            for b in range(a, max_val + 1):
                numbers_tested += 1

                d2 = a ** 2 + b ** 2
                if math.isqrt(d2) ** 2 == d2:  # (a, b) kenarı tam sayı köşegen oluşturuyor mu?
                    for c in range(b, max_val + 1):
                        e2 = a ** 2 + c ** 2
                        f2 = b ** 2 + c ** 2


                        if math.isqrt(e2) ** 2 == e2 and math.isqrt(f2) ** 2 == f2:
                            solutions.add((a, b, c))

        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun carré harshad trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def find_brique_vite():
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



        # Trouver les triangles rectangles(ex: 2025)
        # Solution brute force un peu vite

        pythagorean_triples = []
        max=int(math.sqrt(max_val))
        for m in range(1, max + 1):
            for n in range(1, m):
                if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    c = m ** 2 + n ** 2
                    if c <= max_val:
                        pythagorean_triples.append((a, b, c))


        for a, b, d in pythagorean_triples:
            for c in range(1, max_val + 1):
                numbers_tested += 1
                if math.isqrt(a ** 2 + c ** 2) ** 2 == a ** 2 + c ** 2 and \
                        math.isqrt(b ** 2 + c ** 2) ** 2 == b ** 2 + c ** 2 and \
                        math.isqrt(a ** 2 + b ** 2 + c ** 2) ** 2 == a ** 2 + b ** 2 + c ** 2:
                    solutions.add(tuple(sorted((a, b, c))))



        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun triange rectangle trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

 # Solution brute force un peu vite




        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions: # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun brique trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def find_brique_advance():
    try:
        # Récupérer les bornes min et max
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        if min_val < 0 or max_val < 0 or min_val > max_val:
            raise ValueError("Les bornes doivent être des entiers positifs et min ≤ max.")

        # Initialiser les compteurs
        start_time = time.time()  # Début du chronomètre
        numbers_tested = 0
        solutions = set()



        # Trouver les triangles rectangles(ex: 2025)
        # Solution brute force un peu advancé

        for a in range (1, max_val+1):
            for b in range (a, max_val+1):
                for c in range (b, max_val+1):
                    numbers_tested += 1
                    ab=a**2 + b**2
                    if (math.isqrt(ab)**2 == ab):
                        bc=c**2 + b**2
                        if (math.isqrt(bc)**2 == bc):
                            ac=a**2+c**2
                            if (math.isqrt(ac)**2 == ac):
                                solutions.add(tuple((a, b, c)))








        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions:  # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun triange rectangle trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

        # Solution brute force un peu vite

        # Calcul du temps d'exécution
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # En millisecondes

        # Afficher les résultats dans la Text box
        text_output.delete("1.0", tk.END)  # Effacer les résultats précédents
        text_output.insert(tk.END, f"Couples testés : {numbers_tested}\n")
        text_output.insert(tk.END, f"Solutions trouvées : {len(solutions)}\n")
        text_output.insert(tk.END, f"Temps de calcul : {elapsed_time:.2f} ms\n\n")

        if solutions:  # si solution n'est pas vide
            for sol in solutions:
                text_output.insert(tk.END, f"{sol}\n")
        else:
            text_output.insert(tk.END, "Aucun triange rectangle trouvé.\n")

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


# Interface tkinter
root = tk.Tk()
root.title("Triangles Rectangles entiers")

# Labels et champs d'entrée
tk.Label(root, text="Valeur minimale (min):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_min = tk.Entry(root)
entry_min.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Valeur maximale (max):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_max = tk.Entry(root)
entry_max.grid(row=1, column=1, padx=10, pady=5)
entry_min.insert(0, "1")  # Valeur par défaut pour min
entry_max.insert(0, "10000")  # Valeur par défaut pour max

# Boutons pour calculer
btn_calculate = tk.Button(root, text="Trouver les triangles rectangles", command=find_brique)
btn_calculate.grid(row=2, column=0,  pady=10)

# Boutons pour calculer
btn_calculate = tk.Button(root, text="Trouver les triangles rectangles vite", command=find_brique_vite)
btn_calculate.grid(row=2, column=1,  pady=10)

# Boutons pour calculer
btn_calculate = tk.Button(root, text="Trouver les triangles rectangles advancé", command=find_brique_advance)
btn_calculate.grid(row=2, column=2,  pady=10)


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
