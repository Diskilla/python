#!/usr/bin/env python

# Autor: Josef Florian Sedlmeier
# Snake

livingSpaceWidth    = 60
livingSpaceHeight   = 80

NOCOLLISION =  0
COLLISION   = -1
EATAPPLE    = -2
PASSEXIT    = -3

livingSpace         = []
livingSpaceWidth    = 0
livingSpaceHeight   = 0
creatureSize        = 20
snakeDirection      = (0, 0)

applePositions = []
barPositions   = []
snakePosition  = []
exitPosition   = []

fileName = "level1.txt"

def loadLevel(fileName):
    global appleCount, livingSpace, livingSpaceWidth, livingSpaceHeight
    appleCount = 0
    livingSpace = []
    datei = open(fileName, "r")

    y = -1
    for zeile in datei:
        x = -1
        y += 1
        livingSpace.append([])
        for zeichen in zeile:
            if zeichen != '\n':
                x += 1
                livingSpace[y].append(zeichen)
                if zeichen == 'A':
                    applePositions.append((x, y))
                elif zeichen == 'S':
                    snakePosition.append((x, y))
                elif zeichen == 's':
                    snakePosition.insert(0, (x, y))
                elif zeichen == 'H':
                    barPosition.append((x, y))
                elif zeichen == 'E':
                    exitPosition.append((x, y))
    livingSpaceWidth = len(livingSpace[0])
    livingSpaceHeight = len(livingSpace)

def setRegardingColor(column, row):
    if livingSpace[row][column] == "H":
        glColor4f(0.5, 0.5, 0.5, 1.0)
    elif livingSpace[row][column] == "S" or livingSpace[row][column] == "s":
        glColor4f(0.0, 1.0, 0.0, 1.0)
    elif livingSpace[row][column] == "A":
        glColor4f(1.0, 0.0, 0.0, 1.0)
    elif livingSpace[row][column] == "E":
        glColor4f(0.0, 0.0, 1.0, 1.0)
    else:
        glColor4f(0.0, 0.0, 0.0, 1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, 3.0)
    glBegin(GL_QUADS)
    for column in range(livingSpaceWidth):
        for row in range(livingSpaceHeight):
            setRegardingColor(column, row)
            x = column * 10.0
            y = row * 10.0
            glVertex3f(x, y, 0.0)
            glVertex3f(9.0 + x, y, 0.0)
            glVertex3f(9.0 + x, 9.0 + y, 0.0)
            glVertex3f(x, 9.0 + y, 0.0)
    glEnd()

def handleEvent(event):
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        return False
    global snakeDirection
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            snakeDirection = (+1, 0)
        if event.key == K_LEFT:
            snakeDirection = (-1, 0)
        if event.key == K_UP:
            snakeDirection = (0, -1)
        if event.key == K_DOWN:
            snakeDirection = (0, +1)

    return True

def moveSnake():
    for snakePart in snakePosition:
        x, y = snakePart
        livingSpace[y][x] = ' '

    print snakePosition
    x, y    = snakePosition[0]
    dx, dy  = snakeDirection
    newHeadPosition = (x + dx, y + dy)
    collisionDetection(newHeadPosition)
    snakePosition.insert(0, newHeadPosition)
    snakePosition.pop()
    print snakePosition

    for snakePart in snakePosition:
        y, x = snakePart
        livingSpace[x][y] = 'S'

def collisionDetection(position):
    if position in snakePosition:
        print "self collision"
        return COLLISION

    if position in barPositions:
        print "bar collision"
        return COLLISION

    if position in applePositions:
        print "apple collision"
        return EATAPPLE

    if position in exitPosition:
        print "exit collision"
        return PASSEXIT

    return NOCOLLISION
