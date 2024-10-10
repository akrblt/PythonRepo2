# Name : fonction-exercise2.py
# Autor: akrblt
# Date:  10.10.2024
# Version : 0.1
# Purpose : Comprendre les fonctions



def fonction_addtion (arg_chiffre_1,arg_chiffre_2):
    resultat=print(f" addition :{(arg_chiffre_1)+(arg_chiffre_2)}")
    return resultat



def fonction_soustraction (arg_chiffre_1,arg_chiffre_2):
    resultat=print(f" soustraction : {(arg_chiffre_1)-(arg_chiffre_2)}")
    return resultat


def fonction_multiplication (arg_chiffre_1,arg_chiffre_2):
    resultat=print(f"multiplication : {(arg_chiffre_1)*(arg_chiffre_2)}")
    return resultat


def fonction_division (arg_chiffre_1,arg_chiffre_2):
    resultat=print(f" division : {(arg_chiffre_1)/(arg_chiffre_2)}")
    return resultat

global_chiffre_1=int(input("Saisir le premier chiffre : "))
global_chiffre_2=int(input("Saisir le deuxieme chiffre : "))


fonction_addtion(global_chiffre_1,global_chiffre_2)
fonction_soustraction(global_chiffre_1,global_chiffre_2)
fonction_multiplication(global_chiffre_1,global_chiffre_2)
fonction_division(global_chiffre_1,global_chiffre_2)

print(fonction_addtion(global_chiffre_1,global_chiffre_2))



