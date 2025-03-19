import tkinter as tk
from tkinter import messagebox
from collections import Counter
from best_rummy_steps_0 import is_valid_sequence, is_valid_group, find_best
import random
import copy

# Données du jeu
j1 = [0x7, 0x9, 0xD, 0x1D, 0x21, 0x22, 0x27, 0x2B, 0x2C, 0x2D]
game = [
    [0x3, 0x4, 0x5, 0x6],
    [0x12, 0x13, 0x14],
    [0x1A, 0x1B, 0x1C],
    [0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A],
    [0x2A, 0x2B, 0x2C, 0x2D],
    [0x1, 0x11, 0x31],
    [0x2, 0x12, 0x22],
    [0x33, 0x34, 0x35]
]


colors = ["red", "blue", "orange", "black"]

selected_tile = None

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    """Dessine un rectangle avec des coins arrondis"""
    # Dessiner les quatre arcs pour les coins arrondis
    canvas.create_arc(x1, y1, x1 + 2*radius, y1 + 2*radius, start=90, extent=90, style=tk.PIESLICE, outline="", **kwargs)
    canvas.create_arc(x2 - 2*radius, y1, x2, y1 + 2*radius, start=0, extent=90, style=tk.PIESLICE, outline="", **kwargs)
    canvas.create_arc(x2 - 2*radius, y2 - 2*radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, outline="", **kwargs)
    canvas.create_arc(x1, y2 - 2*radius, x1 + 2*radius, y2, start=180, extent=90, style=tk.PIESLICE, outline="", **kwargs)
    
    # Dessiner les quatre rectangles pour les côtés du rectangle
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, outline="", **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, outline="", **kwargs)

# Afficher la réserve (tous les jetons restants en bas)
all_tiles = [i + (j << 4) for i in range(1, 14) for j in range(4)] * 2  # Deux fois les mêmes éléments
used_tiles = j1 + [tile for group in game for tile in group]
# Compter les occurrences des tuiles utilisées
used_counter = Counter(used_tiles)
remaining_counter = Counter(all_tiles)

# Soustraire les occurrences des tuiles utilisées une seule fois
for tile in used_counter:
    remaining_counter[tile] -= used_counter[tile]
    if remaining_counter[tile] < 0:
        remaining_counter[tile] = 0

# Générer la liste des tuiles restantes
remaining_tiles = list(remaining_counter.elements())
# Trier les tuiles restantes par valeur
remaining_tiles.sort(key=lambda x: (x // 16, x % 16))


def draw_tile(canvas, x, y, value, tag):
    """Dessine un jeton avec sa valeur hexadécimale"""
    val = value % 16
    color = colors[value // 16]
    create_rounded_rectangle(canvas, x, y, x+40, y+50, radius=6, fill="snow")
    arc = canvas.create_arc(x+3, y+3, x+37, y+37, start=0, extent=355, fill="#fef9e7", outline="#fef9e7", tags=tag)
    text = canvas.create_text(x+20, y+17, text=val, font=("Arial", 16, "bold"), fill=color, tags=tag)
    text2 = canvas.create_text(x+20, y+40, text="Rummikub", font=("Arial", 5, "bold"), fill="gray", tags=tag)
    return arc, text, text2

def draw_game(canvas):
    """Affiche la main du joueur, le plateau et la réserve"""
    canvas.delete("all")
    
    # Afficher la main du joueur (en haut à gauche)
    x_offset = 20
    for i, tile in enumerate(j1):
        tag = f"hand_{i}"
        draw_tile(canvas, x_offset + i * 50, 20, tile, tag)
        canvas.tag_bind(tag, "<Button-1>", lambda event, t=tile: move_tile_to_reserve(t))
        canvas.tag_bind(tag, "<Button-3>", lambda event, t=tile: select_tile(t))
    
    # Séparer les séquences et les groupes
    sequences = [group for group in game if is_sequence(group)]
    groups = [group for group in game if not is_sequence(group)]
    
    # Afficher les séquences (4 lignes, une par couleur)
    y_offset = 100
    for color_idx in range(4): # pour chaque couleur
        x_offset = 70
        for iss,seq in enumerate(sequences): # pour chaque séquence, garder le numéro de la séquence
            if all((tile >> 4) == color_idx for tile in seq): # si la couleur est la bonne
                for i, tile in enumerate(seq):
                    tag = f"seq_{color_idx}_{iss}_{i}" # tag pour chaque séquence avec couleur, index et index
                    draw_tile(canvas, x_offset, y_offset, tile, tag)
                    canvas.tag_bind(tag, "<Button-3>", create_add_tile_to_sequence_callback(tile,seq, i))
                    x_offset += 50
                x_offset += 50  # Espace entre les séquences
        y_offset += 60
    
    # Afficher les groupes (2 lignes)
    y_offset = 350
    for row_idx in range(2):
        x_offset = 70
        for group in groups[row_idx::2]:
            for i, tile in enumerate(group):
                tag = f"group_{row_idx}_{i}"
                draw_tile(canvas, x_offset, y_offset, tile, tag)
                canvas.tag_bind(tag, "<Button-3>", create_add_tile_to_group_callback(tile, group, i))
                x_offset += 50
            x_offset += 50  # Espace entre les groupes
        y_offset += 60

    # Afficher la réserve (tous les jetons restants en bas)
    y_offset = 500
    for i, tile in enumerate(remaining_tiles):
        tag = f"reserve_{i}"
        draw_tile(canvas, 20 + (i % 26) * 50, y_offset + (i // 26) * 60, tile, tag)
        canvas.tag_bind(tag, "<Button-1>", lambda event, t=tile: move_tile_to_hand(t))

def create_add_tile_to_sequence_callback(tile, sequence, index):
    """Crée une fonction de rappel pour ajouter une tuile à une séquence"""
    def callback(event):
        add_tile_to_sequence(event, tile, sequence, index)
    return callback

def create_add_tile_to_group_callback(tile, group, index):
    """Crée une fonction de rappel pour ajouter une tuile à un groupe"""
    def callback(event):
        add_tile_to_group(event, tile, group, index)
    return callback


def is_sequence(group):
    """Vérifie si un groupe est une séquence"""
    if len(group) < 3:
        return False
    group = sorted(group)
    return all((group[i] >> 4) == (group[0] >> 4) and (group[i] & 0xF) == (group[0] & 0xF) + i for i in range(len(group)))

def move_tile_to_hand(tile):
    """Déplace une tuile de la réserve à la main du joueur"""
    if tile in remaining_tiles:
        j1.append(tile)
        remaining_tiles.remove(tile)
        draw_game(canvas)

def move_tile_to_reserve(tile):
    """Déplace une tuile de la main du joueur à la réserve"""
    if tile in j1:
        remaining_tiles.append(tile)
        j1.remove(tile)
        draw_game(canvas)

def draw_tile_from_reserve():
    """Pioche une carte aléatoire de la réserve et l'ajoute à la main du joueur"""
    if remaining_tiles:
        drawn_tile = random.choice(remaining_tiles)
        j1.append(drawn_tile)
        remaining_tiles.remove(drawn_tile)
        draw_game(canvas)

def select_tile(tile):
    """Sélectionne une tuile de la main du joueur"""
    global selected_tile
    selected_tile = tile

def add_tile_to_sequence(event, tile, sequence, index):
    """Ajoute une tuile sélectionnée à une séquence"""
    global selected_tile
    print("add_tile_to_sequence",selected_tile, sequence, index)

    if selected_tile:
        if index < len(sequence) // 2:
            new_sequence = [selected_tile] + sequence
        else:
            new_sequence = sequence + [selected_tile]
        if is_valid_sequence(new_sequence):
            sequence.clear()
            sequence.extend(new_sequence)
            j1.remove(selected_tile)
            selected_tile = None
            draw_game(canvas)
        else:
            messagebox.showwarning("Invalid Move", "Impossible de déplacer ce jeton" + str(new_sequence))

def add_tile_to_group(event, tile, group, index):
    """Ajoute une tuile sélectionnée à un groupe"""
    global selected_tile
    if selected_tile:
        new_group = group + [selected_tile]
        if is_valid_group(new_group):
            group.append(selected_tile)
            j1.remove(selected_tile)
            selected_tile = None
            draw_game(canvas)
        else:
            messagebox.showwarning("Invalid Move", "Impossible de déplacer ce jeton" + st(new_sequence))

def best_play():
    """Détermine le meilleur coup à jouer"""
    global j1, game
    j1, game = find_best(j1, game)
    print("terminé")
    draw_game(canvas)

# Interface Tkinter
root = tk.Tk()
root.title("Rummy en Tkinter")

# Ajouter un bouton pour piocher une carte
frm_high = tk.Frame(root)
frm_high.pack()
draw_button = tk.Button(frm_high, text="Pioche", command=draw_tile_from_reserve)
draw_button.pack(side=tk.LEFT)
best_button = tk.Button(frm_high, text="Best play", command=best_play)
best_button.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=1350, height=700, bg="gray")
canvas.pack()

draw_game(canvas)

root.mainloop()