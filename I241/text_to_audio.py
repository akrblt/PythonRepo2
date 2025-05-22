from gtts import gTTS
import os

# Nom du dossier où les fichiers MP3 seront enregistrés
nom_du_dossier = "fichiers_audio"

# Créer le dossier s'il n'existe pas
if not os.path.exists(nom_du_dossier):
    os.makedirs(nom_du_dossier)

# Texte 1
texte_1 = "Ohhh Mon Dieu !  Tu me fais peur ! Heureusement c’est que le test. Je vais vérifier mon compte dans l’app."

# Texte 2
texte_2 = """
Oui, tu as eu de la chance cette fois-ci ! Ce test te permet de savoir qu’il ne faut pas cliquer sur tous les liens que tu reçois par mail.
Je suis Papa IA. J’analyse des millions de modèles de fraude, j’apprends chaque jour et veille à ce que les mails malicieux ne te piègent pas. 
De temps en temps je fais aussi des tests pour mettre en garde des utilisateurs.
"""

# Chemins des fichiers audio
chemin_fichier_1 = os.path.join(nom_du_dossier, "message_1.mp3")
chemin_fichier_2 = os.path.join(nom_du_dossier, "message_2.mp3")

# Création des fichiers audio
tts_1 = gTTS(text=texte_1, lang='fr')
tts_1.save(chemin_fichier_1)

tts_2 = gTTS(text=texte_2, lang='fr')
tts_2.save(chemin_fichier_2)

# Affichage d'information
print(f"Les fichiers audio ont été enregistrés dans le dossier '{nom_du_dossier}'.")
