#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Caesar-Chiffre implementierung

def caesar(text, key):
    cipher = ""
    for letter in text:
        # index des aktuellen Klartextbuchstabens im Symbolvorrat bestimmen
        index   = symbols.index(letter)
        # Addition des Schluessels zum Index (um die Laenge des Index verschieben)
        # und Sicherstellung, dass der Index im gueltigen Bereich bleibt
        index   = (index + key) % len(symbols)
        cipher += symbols[index]

    return cipher

# diese Verschluesselungsmethode ist absolut nicht sicher, da sie mit einem
# simplen brute-force angriff geknackt werden kann
def caesar_brute(text):
    decrypted = ""
    for x in range (1, 25):
        decrypt = caesar(text, -x)
        decrypted += decrypt
    return decrypted
# Verwendung der Funktion caesar
# 'oeffentlichen' Schluessel festlegen
key = 4
symbols = "abcdefghijklmnopqrstuvwxyz "
plaintext = "diese nachricht kann im prinzip jeder knacken"

encrypted = caesar(plaintext, key)
# da beim entschluesseln der Index des Buchstaben um den Key reduziert wird, wird
# dieser einfach mit einem '-' aufgerufen
decrypted = caesar(encrypted, -key)

# mit bruteforce entschluesselt ohne den key zu kennen
brute = caesar_brute(encrypted)
print brute

#~ print plaintext
#~ print encrypted
#~ print decrypted
