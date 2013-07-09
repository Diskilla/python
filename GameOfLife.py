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
        if event.type == QUIT or
         (event.type == KEYDOWN and event.key == K_ESCAPE):
             break

         draw()
         calculateNextGeneration()
         pygame.display.flip()

IF __name__ == '__main__': main()
