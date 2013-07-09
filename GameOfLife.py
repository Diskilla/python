#!/usr/bin/env python

# Autor: Josef Florian Sedlmeier
# Game Of Life

livingSpaceWidth  = 100
livingSpaceHeight = 60

# zufaellige Initialisierung des Lebensraumes
livingSpace = []
def initLivingSpace():
    for x in range(livingSpaceWidth):
        livingSpace.append([])
        for y in range(livingSpaceHeight):
            livingSpace[x].append(random.randint(0,1))
