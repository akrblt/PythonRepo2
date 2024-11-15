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
print("--------------LIST------------------")
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

#print(f" fruits :  {fruits}") # listeyi direk olarak print ile yazdiramayiz. bir dongunun icinde yazdirmamiz gerekir

# Initialisation de ma variable de type List
liste = [2, 4, 6, 8]
print("-------------")

print(f"typde de list : +{type(liste)}") #typde de list : +<class 'list'>

# Affichage de la position de ma valeur
print (liste.index(6))

# Affichage de la position d'une valeur qui n'est pas dans la liste
# (!!! Doit provoquer une erreur !!!)
#print (liste.index(5))

print("--------------------TUPLE-----------------------------")
# Initialisation de ma variable de type Tuple
tuple1 = (2, 4, 6, 8)

# Affichage de ma variable
print (tuple1)
print(f" typde de :  {type(tuple1)}") #typde de :  <class 'tuple'>

# Affichage d'un élément de mon Tuple
print (tuple1[3])

# Affichage de la position de ma valeur
print (tuple1.index(6))

# Affichage de la position d'une valeur qui n'est pas dans la liste
# (!!! Doit provoquer une erreur !!!)
#print (tuple1.index(5))

print("---------------DICTIONARIE------------------")

# Initialisation du dictionnaire
dictionnaire = {
    1: "un",
    2: "deux",
    3: "trois",
    6: "six",
    4: "quatre",
    5: "cinq",
}

# Affiche le mot "un" du chiffre 1
print (dictionnaire[1])
print(f"afficahage : {dictionnaire}")

# List toutes les clés d'un dictionnaire
dict_keys = dictionnaire.keys()
for dict_key in dict_keys:
    print (dict_key,end=" , ")
print("")

#List toutes les values d'un dictionnaire

dict_values=dictionnaire.values()
for dict_value in dict_values:
    print(dict_value,end=" , ")
print("")

# Lit toutes les clés et valeurs d'un dictionnaire
for dict_key in dictionnaire.keys():
    print ("La valeur de la clé '", dict_key, "' est '",
           dictionnaire[dict_key], "'")

print("-------------3 LANGUEGE----------------")

# Initialisation du dictionnaire
dictionnaire = {
    "langues": ["FR", "EN", "DE"],
    1: ["un", "one", "eins"],
    2: ["deux", "two", "zwei"],
    3: ["trois", "three", "drei"]
}

# Demande à l'utilisateur de choisir un chiffre parmis ceux existants
# dans le dictionnaire
chiffre = int(input("Choisissez un chiffre "
                + str(list(dictionnaire.keys())[1:]) + " : "))

# Demande à l'utilisateur de choisir la langue dans laquelle il veut
# que le chiffre soit affiché
langue = input("Choisissez la langue " + str(dictionnaire["langues"]) + " : ")

# Determine la position de la langue dans la liste
pos_langue = dictionnaire["langues"].index(langue)

# Affiche le mot en fonction du chiffre et de la langue
print(dictionnaire[chiffre][pos_langue])