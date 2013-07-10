#!/usr/bin/env python
# Skytale implementierung

# Funktion zum Verschluesseln nach 'Skytale-Methode'
# Die Textlaenge muss glatt (ohne Rest) durch den Umfang teilbar sein.
# Dies wird mit der Funktion EnsureSideCondition ueberprueft.
# Der Umfang ist bei dieser Methode als oeffentlicher Schluessel zu betrachten.
def skytale_encrypt(text, umfang):
    text    = ensureSideCondition(text, umfang)
    length  = len(text)
    cipher  = ""
    for x in range(0, umfang):
        for y in range(x, length, umfang):
            cipher += text[y]

    return cipher.upper()

# Prueft, ob die Laenge des Strings ohne Rest durch den Umfang teilbar ist.
# Falls nicht wird der Rest des Strings mit Leerzeichen aufgefuellt.
def ensureSideCondition(text, umfang):
    length      = len(text)
    remainder   = length % umfang
    while remainder != 0:
        text    += " "
        length   = len(text)
        remainder = length % umfang

    return text

# Funktion zum Entschluesseln nach 'Skytale-Methode'
# bekommt als Parameter den verschluesselten Text und den Umfang
def skytale_decrypt(text, umfang):
    length      = len(text)
    umfang      = length/umfang
    print umfang, length
    plaintext = skytale_encrypt(text, umfang)

    return plaintext.lower()

# Verwendung der Funktionen zum Ver- und Entschluesseln eines Strings
# 1. oeffentlichen Schluessel (Umfang) definieren
key = 8
# 2. Zu verschluesselnden Text definieren
plaintext = "Es ist viel zu warm ohne Ventilator!"
# 3. verschluesseln
cipher = skytale_encrypt(plaintext, key)

#Kontrollausgabe
print plaintext
print cipher
# entschluesseln
print skytale_decrypt(cipher, key)
