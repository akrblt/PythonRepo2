import hashlib
import os
import subprocess

# Chemin du répertoire contenant les copies de MyApp
repertoire = "C:\\Users\\pr08glt\\Desktop\\Applications"

# Empreinte SHA-256 de référence
empreinte_reference = "4DB96A6E213ED1E549BDA728AFB21E7EE55403ACE0BF52F249304B929C6858A8"


def calculer_empreinte_sha256(fichier):
    """Calcule l'empreinte SHA-256 d'un fichier."""
    sha256 = hashlib.sha256()
    with open(fichier, "rb") as f:
        for bloc in iter(lambda: f.read(4096), b""):
            sha256.update(bloc)
    return sha256.hexdigest().upper()


def identifier_fichiers_propres(repertoire, empreinte_reference):
    """Identifie les fichiers propres dans un répertoire."""
    fichiers_propres = []
    for fichier in os.listdir(repertoire):
        chemin_fichier = os.path.join(repertoire, fichier)
        if os.path.isfile(chemin_fichier):
            empreinte = calculer_empreinte_sha256(chemin_fichier)
            print(f"Fichier : {fichier}, Empreinte calculée : {empreinte}")
            if empreinte == empreinte_reference:
                fichiers_propres.append(chemin_fichier)
    return fichiers_propres


def executer_fichiers(fichiers):
    """Exécute les fichiers fournis."""
    for fichier in fichiers:
        print(f"Exécution de {fichier}...")
        try:
            subprocess.run([fichier], check=True)
        except Exception as e:
            print(f"Erreur lors de l'exécution de {fichier} : {e}")


# Étapes principales
fichiers_propres = identifier_fichiers_propres(repertoire, empreinte_reference)
if fichiers_propres:
    print(f"Fichiers propres identifiés : {fichiers_propres}")
    executer_fichiers(fichiers_propres)
else:
    print("Aucun fichier propre trouvé.")
