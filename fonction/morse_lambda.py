# Mors alfabesi
alfabe = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "ı": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": " / ",
    # Mors alfabesine ait sayılar.
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


metin = input("Yazı: ")
metin=metin.lower()
islem = list(map(lambda x: alfabe[x] if x in alfabe else "EROR({x}) ".format(x), list(metin)))
print(metin+ " => "+" ".join(islem))


# Morse kodundan harfe çevirme işlemi için ters sözlük oluşturuyoruz
ters_alfabe = {v: k for k, v in alfabe.items()}

# Kullanıcıdan Morse alfabesi girişi alalım
mors_metin = input("Morse kodunu giriniz (her harf arasında boşluk, kelimeler arasında '/' olacak şekilde): ")

# Girdiği Morse kodunu boşluklar ve '/' işaretine göre ayıralım
kelimeler = mors_metin.split(" / ")  # Kelimeleri '/' işaretine göre ayırıyoruz
cozum = []

for kelime in kelimeler:
    harfler = kelime.split()  # Harfleri boşluklara göre ayırıyoruz
    cozum.append(''.join([ters_alfabe[harf] if harf in ters_alfabe else "?" for harf in harfler]))

# Sonucu birleştirip ekrana yazdıralım
print(mors_metin + " => " + " ".join(cozum))

