import pandas as pd
from sqlalchemy import create_engine

# 1️⃣ Lire le fichier Excel
chemin_fichier = "C:/Users/pr08glt/Desktop/Module 1/PythonRepo2/ICT_164/xlsx/sectors.xlsx"  # Mettez ici le chemin de votre fichier
df = pd.read_excel(chemin_fichier)

print("Le fichier Excel a été lu avec succès !")
print(df.head())

# 2️⃣ Se connecter à la base de données MySQL
utilisateur = "root"          # Votre nom d'utilisateur MySQL
mot_de_passe = "root"         # Votre mot de passe MySQL
hote = "localhost"            # Adresse du serveur (généralement localhost)
base_de_donnees = "school"    # Nom de la base de données

# Créer la connexion
engine = create_engine(f"mysql+pymysql://{utilisateur}:{mot_de_passe}@{hote}/{base_de_donnees}")

print("Connexion à la base de données réussie !")

# 3️⃣ Transférer les données vers MySQL
nom_table = "tab2"  # Nom de la table MySQL
df.to_sql(nom_table, con=engine, if_exists='append', index=False)

print(f"Les données ont été transférées avec succès vers la table {nom_table} !")

# 4️⃣ Vérifier si les données ont été correctement transférées
requete = f"SELECT * FROM {nom_table} LIMIT 5"
resultats = pd.read_sql(requete, con=engine)

print("Données extraites de la table :")
print(resultats)

# Fermer la connexion (optionnel)
engine.dispose()
