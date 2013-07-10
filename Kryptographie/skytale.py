#!/usr/bin/env python
# Skytale implementierung

# Funktion zum Verschlüsseln nach 'Skytale-Methode'
def skytale_encrypt(text, umfang):
    text    = ensureSideCondition(text, umfang)
    length  = len(text)
    cipher  = ""
    for x in range(0, umfang):
        for y in range(x, length, umfang):
            cipher += text[y]

    return cipher.upper()
