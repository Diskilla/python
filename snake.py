#!/usr/bin/env python

# Autor: Josef Florian Sedlmeier
# Snake

livingSpaceWidth    = 60
livingSpaceHeight   = 80

def loadLevel(fileName):
    livingSpace = []
    datei = open(fileName, "r")
    
    x = -1
    y = -1
    for zeile in datei:
        y += 1
        livingSpace.append([])
        for zeichen in zeile:
            if zeichen != '\n':
                x += 1
                livingSpace[y].append(zeichen)
    print "Level loaded...(", len(livingSpace[0]), "x ", len(livingSpace), ")"

    return livingSpace
