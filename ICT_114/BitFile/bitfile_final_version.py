def afficher_inventaire(inventaire, objets):
    print("\nContenu de l'inventaire:")
    for nom, masque in objets.values():
        etat = "Oui" if inventaire & masque else "Non"
        print(f"  {nom:<10}: {etat}")

def gerer_objet(inventaire, masque, action):
    if action == "ajouter":
        inventaire |= masque
        print("Objet ajouté à l'inventaire.")
    elif action == "supprimer":
        inventaire &= ~masque
        print("Objet retiré de l'inventaire.")
    return inventaire

def choisir_objet(inventaire, objets):
    print("\nChoisissez un objet :")
    for index, (nom, _) in objets.items():
        print(f"  {index}) {nom}")

    try:
        choix = int(input("Numéro de l'objet : "))
        if choix in objets:
            nom, masque = objets[choix]
            action = "supprimer" if inventaire & masque else "ajouter"
            inventaire = gerer_objet(inventaire, masque, action)
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")
    return inventaire

def main():
    # Octet d'inventaire (déjà initialisé avec un contenu)
    inventaire = 0xA2

    # Déclaration des objets et masques
    objets = {
        1: ("Cuillère", 0b00000001),
        2: ("Fourchette", 0b00000010),
        3: ("Couteau", 0b00000100),
        4: ("Gamelle", 0b00001000),
        5: ("Lampe", 0b00010000),
        6: ("Pince", 0b00100000),
        7: ("Tournevis", 0b01000000),
        8: ("Marteau", 0b10000000),
    }

    while True:
        print("\n\nMenu:")
        print("  1) Afficher l'inventaire")
        print("  2) Ajouter un couteau")
        print("  3) Supprimer le couteau")
        print("  4) Ajouter ou supprimer un objet")
        print("  9) Quitter")
        choix = input("Votre choix ? ")

        match choix:
            case "1":
                afficher_inventaire(inventaire, objets)
            case "2":
                inventaire = gerer_objet(inventaire, objets[3][1], "ajouter")
            case "3":
                inventaire = gerer_objet(inventaire, objets[3][1], "supprimer")
            case "4":
                inventaire = choisir_objet(inventaire, objets)
            case "9":
                print("Bye...")
                break
            case _:
                print("Choix invalide,  réessayez.")

if __name__ == "__main__":
    main()
