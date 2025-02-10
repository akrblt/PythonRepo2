def pack4(a, b, c, d):
    # 1. Adım: Sayıları sola kaydır (boşlukları doldur)
    if a == 0:
        a, b, c, d = b, c, d, 0  # Kaydırma
    if a == 0:
        a, b, c, d = b, c, d, 0  # Tekrar kaydırma
    if a == 0:
        a, b, c, d = b, c, d, 0  # Tekrar kaydırma

    if b == 0:
        b, c, d = c, d, 0  # Kaydırma
    if b == 0:
        b, c, d = c, d, 0  # Tekrar kaydırma

    if c == 0:
        c, d = d, 0  # Kaydırma

    # 2. Adım: Aynı olanları birleştir
    if a == b and a != 0:
        a *= 2
        b, c, d = c, d, 0  # Kaydırma
    if b == c and b != 0:
        b *= 2
        c, d = d, 0  # Kaydırma
    if c == d and c != 0:
        c *= 2
        d = 0  # Son birleşme işlemi

    return [a, b, c, d]

