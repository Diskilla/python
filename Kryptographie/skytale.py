#!/usr/bin/env python
# Skytale implementierung

# Funktion zum Verschlüsseln nach 'Skytale-Methode'
# Die Textlänge muss glatt (ohne Rest) durch den Umfang teilbar sein.
# Dies wird mit der Funktion EnsureSideCondition überprüft
def skytale_encrypt(text, umfang):
    text    = ensureSideCondition(text, umfang)
    length  = len(text)
    cipher  = ""
    for x in range(0, umfang):
        for y in range(x, length, umfang):
            cipher += text[y]

    return cipher.upper()

# Prüft, ob die Länge des Strings ohne Rest durch den Umfang teilbar ist.
# Falls nicht wird der Rest des Strings mit Leerzeichen aufgefüllt.
def ensureSideCondition(text, umfang):
    length      = len(text)
    remainder   = length % umfang
    while remainder != 0:
        text    += " "
        length   = len(text)
        remainder = length % umfang

    return text

# Funktion zum Entschlüsseln nach 'Skytale-Methode'
def skytale_decrypt(text, umfang):
    length      = len(text)
    umfang      = length/umfang
    print umfang, length
    plaintext = skytale_encrypt(text, umfang)

    return plaintext.lower()
