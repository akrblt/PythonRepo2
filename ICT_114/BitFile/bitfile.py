# Constantes
OBJET1 = "CUILLERE"
OBJET2 = "FOURCHETTE"
OBJET3 = "COUTEAU"
OBJET4 = "GAMELLE"
OBJET5 = "LAMPE"
OBJET6 = "PINCE"
OBJET7 = "TOURNEVIS"
OBJET8 = "MARTEAU"



# Initialisation de l'inventaire
inventaire = []


def afficher_inventaire():
    """Affiche le contenu de l'inventaire."""
    if inventaire:
        print("Contenu de l'inventaire :")
        for objet in inventaire:
            print(f"- {objet}")
    else:
        print("L'inventaire est vide.")


def ajouter_objet(objet):
    """Ajoute un objet à l'inventaire."""
    inventaire.append(objet)
    print(f"L'objet '{objet}' a été ajouté à l'inventaire.")


def supprimer_objet(objet):
    """Supprime un objet de l'inventaire."""
    if objet in inventaire:
        inventaire.remove(objet)
        print(f"L'objet '{objet}' a été retiré de l'inventaire.")
    else:
        print(f"L'objet '{objet}' n'est pas dans l'inventaire.")


def menu():
    """Menu interactif pour gérer l'inventaire."""
    while True:
        print("\nMenu :")
        print("1 - Afficher l'inventaire")
        print("2 - Ajouter un objet")
        print("3 - Supprimer un objet")
        print("4 - Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_inventaire()
        elif choix == "2":
            print(f"Objets disponibles : {OBJET1}, {OBJET2}, {OBJET3},{OBJET4}, {OBJET5}, {OBJET6},{OBJET7}, {OBJET8}")
            objet = input("Quel objet voulez-vous ajouter ? ")
            if objet in [OBJET1, OBJET2, OBJET3]:
                ajouter_objet(objet)
            else:
                print("Cet objet n'est pas disponible.")
        elif choix == "3":
            print(f"Objets disponibles dans l'inventaire : {inventaire}")
            objet = input("Quel objet voulez-vous supprimer ? ")
            supprimer_objet(objet)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Démarrage du programme
if __name__ == "__main__":
    menu()
