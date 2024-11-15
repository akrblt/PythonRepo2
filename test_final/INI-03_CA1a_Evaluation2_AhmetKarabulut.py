"""
Name    : INI-03_CA1a_Evaluation2_AhmetKarabulut.py
Author  : Ahmet KARABULUT
Date    : 2024.11.01
Version : 0.01
Purpose : Programme qu'affiche un pays atteindra un certain nombre d'habitants

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-11-01
  - Version initiale
"""
# Demander l'année de depart du calcul
while True:
    anne_depart = input("Entrez l'année de depart du calcul : ")
    if anne_depart.isdigit():
        if int(anne_depart) > 0:
         break

#Demander la population
while True:
    population = input("Entrez la population , doit etre plus ou egal 1.000.000 : ")
    if population.isdigit():
        if int(population)>=1000000:
         break

#Demander l'inroduction du pourcentage d'augmentation annuelle de la population
while True:
    pourcentage = float(input("Entrez l'introduction du pourcentage d'augmentation annuelle de la population , doit etre plus 0 : "))
    #if pourcentage.isdigit():
    if  float(pourcentage)>0:
         break

#calculer  total population
print(f"{float(population)+float(population)*pourcentage}  en {anne_depart} ")
resultat=population
list_population=[]

list_population.append(float(population)+float(population)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)
list_population.append(float(resultat)+float(resultat)*pourcentage)







#Demander ensuite le nombre d'habitatnts visé
while True:
    habitatnt_vise = float(input("Entrez ensuite le nombre d'habitatnts visé : "))
    #if pourcentage.isdigit():
    if  float(habitatnt_vise)>=float(population)+1000000:
         break

#La program affiche la population pour chaque année et l'année la quelle le nombre cible est atteint ou depassé

