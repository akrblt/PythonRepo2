def calculer_chiffre_luhn(numero):
    """
    Calcule le dernier chiffre selon l'algorithme de Luhn.
    """
    if len(numero) != 15 or not numero.isdigit():
        return "Erreur : Entrez exactement 15 chiffres."

    # Convertir en une liste de chiffres
    chiffres = [int(ch) for ch in numero]

    # Appliquer l'algorithme de Luhn (partie calcul mod 10)
    somme = 0
    for i in range(len(chiffres)):
        if i % 2 == 0:  # Indices pairs (en commençant par 0)
            double = chiffres[-(i + 1)] * 2
            somme += double - 9 if double > 9 else double
        else:  # Indices impairs
            somme += chiffres[-(i + 1)]

    # Trouver le chiffre de contrôle
    dernier_chiffre = (10 - (somme % 10)) % 10
    return dernier_chiffre


# Interaction avec l'utilisateur
numero_carte = input("Entrez les 15 premiers chiffres de la carte de crédit : ")
resultat = calculer_chiffre_luhn(numero_carte)
print(f"Le dernier chiffre est : {resultat}")
