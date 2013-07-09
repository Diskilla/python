#!/usr/bin/env python

# Autor: Josef Florian Sedlmeier
# Game Of Life

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, math, datetime, random
from pygame.locals import *

livingSpaceWidth  = 100
livingSpaceHeight = 60
livingSpaceDepth = 1
creatureSize = 10

# zufaellige Initialisierung des Lebensraumes
livingSpace = []
def initLivingSpace():
    for x in range(livingSpaceWidth):
        livingSpace.append([])
        for y in range(livingSpaceHeight):
            livingSpace[x].append([])
            for z in range(livingSpaceDepth):
                if random.randint(0, 1) == 1:
                    livingSpace[x][y].append(1000)
                else:
                    livingSpace[x][y].append(0)

def resize((width, height)):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10.0, livingSpaceWidth * 10.0 + 10.0, livingSpaceHeight * 10.0 + 10.0, -10.0, -6.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClearDepth(1.0)
    # Tiefenpruefung aktivieren
    glEnable(GL_DEPTH_TEST)
    # Art der Pruefung festlegen
    glDepthFunc(GL_LEQUAL)
    # Transparenz aktivieren
    glEnable (GL_BLEND);
    # Art der Transparenzberechnung festlegen
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    # Aktivierung der Beleuchtung
    glEnable(GL_LIGHTING)
    # eine Lichtquelle erstellen
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.6, 0.6, 0.6, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.4, 0.4, 0.4, 1.0])
    glLightfv(GL_LIGHT0, GL_POSITION, [(livingSpaceWidth * 20.0)/2.0, (livingSpaceHeight * 20.0)/2.0, -500.0, 1.0])
    # Aktivierung der erstellten Lichtquelle
    glEnable(GL_LIGHT0)
    # Aktivierung von Materialeigenschaften
    glEnable(GL_COLOR_MATERIAL)
    # diffuses, ambientes Licht fuer Vorder- und Rueckseite
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    # automatische Korrektur der Normalen aktivieren
    glEnable(GL_NORMALIZE)
    # bestmoeglich rendern
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

def drawCube(x, y, z, cubeSize):
    # vordere Seitenflaeche
    glNormal3f(0.0, 0.0, -1.0)
    glVertex3f(x, y, z)
    glVertex3f(cubeSize + x, y, z)
    glVertex3f(cubeSize + x, cubeSize + y, z)
    glVertex3f(x, cubeSize + y, z)

    # hintere Seitenflaeche
    glNormal3f(0.0, 0.0, +1.0)
    glVertex3f(x, y, z + cubeSize)
    glVertex3f(cubeSize + x, y, z + cubeSize)
    glVertex3f(cubeSize + x, cubeSize + y, z + cubeSize)
    glVertex3f(x, cubeSize + y, z + cubeSize)
    
    # linke Seitenflaeche
    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(x, y, z)
    glVertex3f(x, cubeSize + y, z)
    glVertex3f(x, cubeSize + y, z + cubeSize)
    glVertex3f(x, y, z + cubeSize)
    
    # rechte Seitenflaeche
    glNormal3f(+1.0, 0.0, 0.0)
    glVertex3f(cubeSize + x, y, z)
    glVertex3f(cubeSize + x, cubeSize + y, z)
    glVertex3f(cubeSize + x, cubeSize + y, z + cubeSize)
    glVertex3f(cubeSize + x, y, z + cubeSize)

    # obere Seitenflaeche
    glNormal3f(0.0, +1.0, 0.0)
    glVertex3f(x, cubeSize + y, z)
    glVertex3f(cubeSize + x, cubeSize + y, z)
    glVertex3f(cubeSize + x, cubeSize + y, z + cubeSize)
    glVertex3f(x, cubeSize + y, z + cubeSize)
    
    # untere Seitenflaeche
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(x, y, z)
    glVertex3f(cubeSize + x, y, z)
    glVertex3f(cubeSize + x, y, z + cubeSize)
    glVertex3f(x, y, z + cubeSize)

def isAlive(x, y, z):
    return livingSpace[x][y][z] == 1000

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    for column in range(livingSpaceWidth):
        for row in range(livingSpaceHeight):
            for depth in range(livingSpaceDepth):
                if livingSpace[column][row][depth] > 0:
                    healthStatus = float(livingSpace[column][row][depth]) / 1000.0
                    if depth % 2 == 0:
                        glColor4f(1.0, 0.0, 0.0, healthStatus)
                    elif depth % 3 == 0:
                        glColor4f(0.0, 1.0, 0.0, healthStatus)
                    else:
                        glColor4f(0.0, 0.0, 1.0, healthStatus)

            x = column * 20.0
            y = row * 20.0
            z = depth * 20.0
            drawCube(x, y, z, 15.0)
    glEnd()

def getNeighborCount(x, y, z):
    count = 0

    xpn = (x + 1) % livingSpaceWidth
    ypn = (y + 1) % livingSpaceHeight
    zpn = (z + 1) % livingSpaceDepth

    count += isAlive(x , ypn, z - 1)
    count += isAlive(xpn, ypn, z - 1)
    count += isAlive(xpn, y, z - 1)
    count += isAlive(xpn, y - 1, z - 1)
    count += isAlive(x , y - 1, z - 1)
    count += isAlive(x - 1, y - 1, z - 1)
    count += isAlive(x - 1, y, z - 1)
    count += isAlive(x - 1, ypn, z - 1)

    count += isAlive(x , ypn, z)
    count += isAlive(xpn, ypn, z)
    count += isAlive(xpn, y, z)
    count += isAlive(xpn, y - 1, z)
    count += isAlive(x , y - 1, z)
    count += isAlive(x - 1, y - 1, z)
    count += isAlive(x - 1, y, z)
    count += isAlive(x - 1, ypn, z)

    count += isAlive(x , ypn, zpn)
    count += isAlive(xpn, ypn, zpn)
    count += isAlive(xpn, y, zpn)
    count += isAlive(xpn, y - 1, zpn)
    count += isAlive(x , y - 1, zpn)
    count += isAlive(x - 1, y - 1, zpn)
    count += isAlive(x - 1, y, zpn)
    count += isAlive(x - 1, ypn, zpn)

    count += isAlive(x, y, zpn)
    count += isAlive(x, y, z - 1)

    return count

def calculateNextGeneration():
    neighborCount = []
    for column in range(livingSpaceWidth):
        neighborCount.append([])
        for row in range(livingSpaceHeight):
            neighborCount[column].append([])
            for depth in range(livingSpaceDepth):
                neighborCount[column][row].append(getNeighborCount(column, row, depth))

    for column in range(livingSpaceWidth):
        for row in range(livingSpaceHeight):
            for depth in range(livingSpaceDepth):
                if 6 <= neighborCount[column][row][depth] <= 11:
                    if neighborCount[column][row][depth] == 8:
                    # creature gets born
                        livingSpace[column][row][depth] = 1000
                    else:
                    # creature dies slowly
                        livingSpace[column][row][depth] = livingSpace[column][row][depth] / 1.5
                    if livingSpace[column][row][depth] < 200:
                        livingSpace[column][row][depth] = 0

def main():
    video_flags = OPENGL | HWSURFACE | DOUBLEBUF
    screenSize = (livingSpaceWidth * creatureSize,
     livingSpaceHeight * creatureSize)

    pygame.init()
    pygame.display.set_mode(screenSize, video_flags)

    initLivingSpace()
    resize(screenSize)
    init()

    frames = 0
    ticks = pygame.time.get_ticks()
    while True:
        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            break
        draw()
        calculateNextGeneration()
        pygame.display.flip()

if __name__ == '__main__': main()
