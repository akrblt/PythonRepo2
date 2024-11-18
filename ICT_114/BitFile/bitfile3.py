def main():
    # Octet d'inventaire (déjà initialisé avec un contenu)
    inventaire = 0xA2

    # Déclaration des constantes qui définissent le bitfield
    CUILLERE = 0b00000001  # Bit 0
    FOURCHETTE = 0b00000010  # Bit 1
    COUTEAU = 0b00000100  # Bit 2
    GAMELLE = 0b00001000  # Bit 3
    LAMPE = 0b00010000  # Bit 4
    PINCE = 0b00100000  # Bit 5
    TOURNEVIS = 0b01000000  # Bit 6
    MARTEAU = 0b10000000  # Bit 7

    objets = {
        1: ("Cuillère", CUILLERE),
        2: ("Fourchette", FOURCHETTE),
        3: ("Couteau", COUTEAU),
        4: ("Gamelle", GAMELLE),
        5: ("Lampe", LAMPE),
        6: ("Pince", PINCE),
        7: ("Tournevis", TOURNEVIS),
        8: ("Marteau", MARTEAU),
    }

    choix = 0  # Pour les menus
    while choix != 9:
        print("\n\nMenu:")
        print("  1) Afficher l'inventaire")
        print("  2) Mettre un couteau dans l'inventaire")
        print("  3) Supprimer le couteau de l'inventaire")
        print("  4) Ajouter ou supprimer un objet de l'inventaire")
        print("  9) Quitter")
        print("\nVotre choix ? ")

        try:
            choix = int(input())
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choix == 1:
            print("Contenu de l'inventaire:")
            for index, (nom, masque) in objets.items():
                print(f"  {nom:<10}: {'Oui' if inventaire & masque else 'Non'}")

        elif choix == 2:
            inventaire |= COUTEAU  # Ajouter le couteau
            print("Mis un couteau dans l'inventaire")

        elif choix == 3:
            inventaire &= ~COUTEAU  # Supprimer le couteau
            print("Supprimé le couteau de l'inventaire")

        elif choix == 4:
            print("\nChoisissez un objet :")
            for index, (nom, _) in objets.items():
                print(f"  {index}) {nom}")

            try:
                objet_choix = int(input("Numéro de l'objet : "))
                if objet_choix not in objets:
                    print("Numéro invalide.")
                    continue

                nom_objet, masque = objets[objet_choix]
                if inventaire & masque:
                    inventaire &= ~masque
                    print(f"{nom_objet} retiré de l'inventaire.")
                else:
                    inventaire |= masque
                    print(f"{nom_objet} ajouté à l'inventaire.")

            except ValueError:
                print("Veuillez entrer un numéro valide.")

        elif choix == 9:
            print("Bye...")

        else:
            print("Réessayez")

if __name__ == "__main__":
    main()
