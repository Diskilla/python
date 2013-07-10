#!/usr/bin/env python
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
