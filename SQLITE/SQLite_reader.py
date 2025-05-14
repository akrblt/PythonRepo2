# Exemple d'accès à SQLite
# JCY pour SI-CA1a
# 12.05.25

import sqlite3 # pas besoin de "piper", dispo dans python depuis version 2.5

# fonction qui exécute une requête SQL
def exec_SQL(sql):
    # l'utilisation de with ferme la BD en sortant du with
    with sqlite3.connect('20km_Lausanne_SAI2.db') as conn:
        conn.row_factory = sqlite3.Row #permettra l'appel des valeurs par runner["id"], en + de runner[0]
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall() #renvoie l'ensemble des enregistrements trouvés sous forme de tableau

# utilisation de la fonction pour afficher les coureurs
#runners= exec_SQL("SELECT id, lastname, firstname, birthYear as b_y FROM runners order by id")
#runners= exec_SQL("SELECT id, lastname, firstname, birthYear as b_y FROM runners order by id")
#for runner in runners:
#    print(runner["id"], runner["lastname"], runner["firstname"], runner["b_y"])


runs=exec_SQL("SELECT id, bib, rank, time FROM runs")
for run in runs:
    print(run["id"], run["bib"], run["rank"], run["time"])