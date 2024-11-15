# Cesar
def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""
    for karakter in metin:

        if 'A' <= karakter <= 'Z':
            sifreli_metin += chr((ord(karakter) - ord('A') + kaydirma) % 26 + ord('A'))

        elif 'a' <= karakter <= 'z':
            sifreli_metin += chr((ord(karakter) - ord('a') + kaydirma) % 26 + ord('a'))

        else:
            sifreli_metin += karakter
    return sifreli_metin



metin = "Bonjour"
kaydirma = 3

sifreli_metin = sezar_sifrele(metin, kaydirma)
print("Texte crypé avec Cesar:", sifreli_metin)




# Vigenère
def vigenere_sifrele(metin, anahtar):
    sifreli_metin = ""
    anahtar_uzunluk = len(anahtar)
    for i, karakter in enumerate(metin):
        kaydirma = ord(anahtar[i % anahtar_uzunluk].lower()) - ord('a')

        if 'A' <= karakter <= 'Z':
            sifreli_metin += chr((ord(karakter) - ord('A') + kaydirma) % 26 + ord('A'))
        elif 'a' <= karakter <= 'z':
            sifreli_metin += chr((ord(karakter) - ord('a') + kaydirma) % 26 + ord('a'))
        else:
            sifreli_metin += karakter
    return sifreli_metin






metin = "Erqmrxu"
anahtar = "114"

sifreli_metin = vigenere_sifrele(metin, anahtar)
print("Texte crypté avec vigenere : ", "Dqmlqtt")

