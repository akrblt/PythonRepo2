"""
Name    : INI-03_CA1a_Test_Final.py
Author  : Ahmet KARABULUT
Date    : 2024.11.01
Version : 0.01
Purpose : Programme qu'affiche les lettres en morse.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-11-01
  - Version initiale
"""

#définition de la liste
fruits = ["apple","banane","peche"]
#ajouter un élément à la liste
fruits.append("water melon")
#supprimer un element dans la liste
fruits.remove("apple")
print(fruits) #['banane', 'peche', 'water melon']
#Obtenir un élément à un index spécifique
fruits1=fruits[1] #peche
print(fruits1)
#imprimer la liste avec une boucle
for i in fruits:
    print(i,end="-")  #banane-peche-water melon-


