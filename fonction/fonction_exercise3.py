#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_CA1a_Dictionnaire-02.py
Author  : Vitor COVAL
Date    : 2024.10.10
Version : 0.01
Purpose : Programme qu'affiche les lettres en morse.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-10-03 01 VCL
  - Version initiale
"""

dictionnaire_morse = {
    'A' : ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
}

print (dictionnaire_morse["A"], end=" ")
print (dictionnaire_morse["H"], end=" ")
print (dictionnaire_morse["M"], end=" ")
print (dictionnaire_morse["E"], end=" ")
print (dictionnaire_morse["T"], end=" ")
print("--------------")

nom=input("saisir votre nom  svp :  ")
nom=nom.upper()
print(nom)
listmorse=()

print(dictionnaire_morse.keys())
print(dictionnaire_morse.values())
def fonction_traduit_en_morse(lettre):
    for i in nom:
        for x in dictionnaire_morse:
           if i== dictionnaire_morse.keys(x) :
            morse=morse+dictionnaire_morse.values(x)
            i+=1
    return morse

fonction_traduit_en_morse(nom)
print("end")
