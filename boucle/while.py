"""
Name    : INI-03_CA1a_Boucles-01.py
Author  : Vitor COVAL
Date    : 2024.10.30
Version : 0.02
Purpose : Utilisation d'une boucle while.
          Le programme affiche les nombres depuis 1 jusqu'au chiffre
          entré par l'utilisateur.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-30 02 VCL
  - Ajout de commentaires
  - Revue du code pour qu'il soit en conformité avec la convention de
    codage Python
# 2024-09-26 01 VCL
  - Version initiale
"""

# Demande un entier à l'utilisateur
chiffre = int(input("Entrez un chiffre : "))

i = 0  # utilisation de la variable i comme compteur (souvent utilisée
       # comme cela)

# Affiche les nombres jusqu'au chiffre entré par l'utilisateur
while i < chiffre:
    i += 1

    if i ==5:
        continue
    if i ==10:
        break
    print(i)


# Demande un texte à l'utilisateur
texte = input("Entrez un texte : ")

i = 0  # Utilisation de la variable i comme compteur (souvent
       # utilisée comme cela)

# Prends la longueur du texte pour l'utiliser comme limite dans la
# boucle while
lenTexte = len(texte)

# Affiche le texte à la verticale
while i < lenTexte:
    print(texte[i])
    i += 1

#meme text avec boucle for
for i in texte:
    print(i,end=" ")
