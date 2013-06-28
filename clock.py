#!/usr/bin/env python

# Analoge Uhr in Python
# Kapitel 1 - Coding for Fun in Python

import pygame, sys, math, datetime

windowMargin        = 30
windowWidth         = 600
windowHeight        = windowWidth
windowCenter        = windowWidth/2, windowHeight/2
clockMarginWidth    = 20
secondColor         = (255, 0, 0)
minuteColor         = (100, 200, 0)
hourColor           = (100, 200, 0)
clockMarginColor    = (130, 130, 0)
clockBackroundColor = (20, 40, 30)
backgroundColor     = (255, 255, 255)
hourCursorLength    = windowWidth/2.0-windowMargin-140
minuteCursorLength  = windowWidth/2.0-windowMargin-40
secondCursorLength  = windowWidth/2.0-windowMargin-10

virtualSpeed        = 1
useVirtualTimer     = False

def getCursorPositionDegrees(position, scale):
    # 12 Uhr enstpricht -90 Grad
    cursorOffset = -90
    degrees = 360 / scale * position + cursorOffset
    return degrees

def gradToBogenmass(degrees):
    # zur Umrechung wird die Gradzahl durch 180 geteilt und mit Pi multipliziert
    # die Bibliothek 'math' bietet auch eine Funktion hierfuer namens
    # math.radians() bzw zum zurueckrechnen math.degrees()
    return degrees / 180.0 * math.pi

def getCirclePoint(position, scale, cursorLength):
    degrees = getCursorPositionDegrees(position, scale)
    bogenmass = gradToBogenmass(degrees)
    xPos = round(math.cos(bogenmass) * cursorLength+windowCenter[0])
    yPos = round(math.cos(bogenmass) * cursorLength+windowCenter[1])
    return(xPos, yPos)

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sys.event(0)

def drawBackground():
    screen.fill(backgroundColor)
    pygame.draw.ellipse( screen, clockMarginColor, (windowMargin, \
     windowMargin, windowWidth - 2 + windowMargin, \
     windowWidth - 2 * windowMargin) )
    pygame.draw.ellipse(screen, clockBackroundColor, \
     (windowMargin + clockMarginWidth / 2, \
     windowMargin + clockMarginWidth / 2, \
     windowWidth - (windowMargin + clockMarginWidth / 2) * 2, \
     windowWidth - (windowMargin + clockMarginWidth / 2) * 2) )

def drawForeground():
    pygame.draw.ellipse( screen, clockMarginColor, \
     (windowWidth / 2.0 - 9, windowHeight / 2.0 - 9, 18, 18 ) )

def drawCursor( color, width, length, position, scale ):
    end = getCirclePoint( position, scale, cursorLength );
    pygame.draw.line( screen, color, windowCenter, end, width )

def drawCurrentTime():
    if useVirtualTimer:
        global hour, minute, second, micro
        timeGoesOn()
    else:
        now     = datetime.datetime.now()
        micro   = now.microsecond
        hour    = now.hour
        minute  = now.minute
        second  = now.second

    drawCursor( hourColor, 15, hourCursorLength, hour + minute / 60.0, 12 )
    drawCursor( minuteColor, 8, minuteCursorLength, minute + second / 60.0, 60 )
    drawCursor( secondColor, 3, secondCursorLength, second + micro / 1000000.0, 60 )

hour                = 0
minute              = 0
second              = 0
micro               = 0
def timeGoesOn():
    global hour, minute, second, micro
    micro += virtualSpeed
    if micro >= 2:
        second += 1
        micro %= 2
    if second > 60:
        minute += 1
        second %= 60
    if minute > 60:
        hour += 1
        minute %= 60
    if hour > 12:
        hour %= 12

def main():
    # Initialisierung des Screens
    pygame.init()
    screen = pygame.display.set_mode(\
     (windowWidth, windowHeight)\
     , pygame.HWSURFACE | pygame.DOUBLEBUF);
    pygame.display.set_caption('Analog Clock');
    
    # Endlosschleife fuer den Hauptablauf der Uhr
    while True:
        handleEvents()
        screen.fill(backgroundColor)
        
        drawBackground()
        drawCurrentTime()
        drawForeground()
        
        pygame.display.flip()
        pygame.time.delay(10)
        
if __name__ == '__main__':
    main()
