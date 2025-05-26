#snake.py 01.05.2025
#joue snake
#Ahmet Karabulut
#version 0.1

import turtle
import time
import random

# Fenêtre
ws = turtle.Screen() # crée un nouvelle fenetre graphique
ws.title("Jeu Snake en Python") # le titre
ws.bgcolor("white")
ws.setup(width=600, height=600) # definit la taille de la fenetre
ws.tracer(0) # desactive raffaichissement automatique de l'ecran . on met à jour l'ecran manuellement avec ws.update()

# Serpent (tête)
head = turtle.Turtle() # crée un nouve object pour la tete de serpent
head.speed(0) # Définit la vitesse maximale d'animation (instantanée). 0 signifie "pas d’animation", pour une exécution rapide.
head.shape("carre") # Change la forme de la tortue en carré.
head.color("black")
head.penup()  # permet de effacer le trace
head.goto(0, 0) # Place la tête du serpent au centre de l'écran.
head.direction = "stop" # Définit la direction initiale à "stop", donc pas de mouvement au début.

# Nourriture
food = turtle.Turtle() # crée un nourriture
food.speed(0) # crée rapide
food.shape("circle") # change la forme de nourriture
food.color("red")
food.penup()
food.goto(0, 100) # Place la nourriture à la position (0, 100) sur l’écran.

# creation de corps du serpent
# body creat
segments = []



# Fonctions de déplacement
def go_up():
   # if head.direction != "down":
        head.direction = "up"

def go_down():
   # if head.direction != "up":
        head.direction = "down"

def go_left():
   # if head.direction != "right":
        head.direction = "left"

def go_right():
   # if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor() # ycor = coordinate  retourne la position
        head.sety(y + 20) # déplace la tête du serpent de 20 pixels vers la haut
    if head.direction == "down":  #Le chiffre 20 correspond à la taille d’un segment du serpent (20x20 pixels).
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
# Chaque segment du serpent (tête, nourriture, corps) est un carré et la taille de ces carrés est de 20x20 pixels.
# Si chaque pas n'est pas de 20 pixels mais plus petit (par exemple 5), le serpent ne s'insérera pas proprement dans les segments et les phénomènes suivants se produiront :
# Les segments du corps ne sont pas alignés → ils ont l'air emmêlés.
# La détection de l'auto-collision ne fonctionne pas correctement.
# Les performances se dégradent → le jeu commence à traîner.



# Contrôles
ws.listen() # en mode ecoute de clavier . Nécessaire pour détecter quand une touche est pressée.
ws.onkeypress(go_up, "Up")
ws.onkeypress(go_down, "Down")
ws.onkeypress(go_left, "Left")
ws.onkeypress(go_right, "Right")

# Boucle principale
while True: # boucle infini , le coeur du jeu , tourne sans arret
    ws.update() # Met à jour manuellement l’écran (puisque tracer(0) line: 15  désactive le rafraîchissement automatique).

    # Collision avec les murs
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290: # notre fenetre 600*600 pixel abs() prend la valeur absolue, pour détecter à gauche/droite/haut/bas.
        time.sleep(1) # apres le collision attendre 1 seconde
        head.goto(0, 0) # Replace la tête du serpent au centre de l’écran.
        head.direction = "stop" # arrete le mouvement
        for segment in segments:
            segment.goto(1000,1000)  # est une méthode simple et efficace pour s'assurer que les segments sont totalement invisibles hors de l'écran.
        segments.clear() #  le serpent recommence à zéro.


    # Collision avec nourriture
    if head.distance(food) < 20:  #  Si la tête du serpent est à moins de 20 pixels de la nourriture, cela signifie qu’il l’a mangée.
        x = random.randint(-280, 280) # On choisit une position aléatoire pour la nourriture, entre -280 et 280 sur chaque axe.
        y = random.randint(-280, 280)
        food.goto(x, y) # La nourriture est déplacée vers cette nouvelle position aléatoire.

        new_segment = turtle.Turtle() # On crée un nouveau segment pour agrandir le corps du serpent.
        new_segment.speed(0) #On désactive l’animation de création pour plus vite
        new_segment.shape("square") # Le segment prend une forme carrée.
        new_segment.color("lightgreen")  #Le segment est coloré en vert clair.
        new_segment.penup() # effacer le trace
        segments.append(new_segment) # Le segment est ajouté à la liste du corps du serpent.

    # deplacer segmets
    for i in reversed(range(1, len(segments))): # Génère les indices des segments, à partir de 1 jusqu'à la fin de la liste.
        # si on a 4 segments, on obtient [1, 2, 3].  reversed [3,2,1] On boucle du dernier segment vers le premier.
        segments[i].goto(segments[i - 1].pos()) # Chaque segment va se déplacer à la position du segment juste avant lui.
        # par example
        # for i in [3,2,1]
        # segments[3].goto(segments[2].pos())
        # segments[2].goto(segments[1].pos())
        # segments[1].goto(segments[0].pos())

    # aller là où se trouve la tête
    if segments:
        segments[0].goto(head.pos())

    # déplacer la tête du serpent
    move() # line 56

    # Collision avec soi-même
    for segment in segments:
        if segment.distance(head) < 20: #  contrôle si la distance entre la tête du serpent et n'importe quel segment de son corps est inférieure à 20 pixels.
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()


    time.sleep(0.1)
