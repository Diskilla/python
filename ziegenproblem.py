#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Autor: Josef Florian Sedlmeier

import random

class Player(object):
    def __init__(self):
        self.guess = 0
        self.wins  = 0

    def newGuess(self):
        self.guess = random.randint(1, 3)

    def changeMind(self, knownNumber):
        allNumbers = set((1, 2, 3))
        allNumbers.remove(self.guess)
        allNumbers.remove(knownNumber)
        self.guess = allNumbers.pop()

    def saveResult(self, winning):
        if winning == self.guess:
            self.wins += 1

if __name__ == '__main__':
    player1 = Player()
    player2 = Player()

    x = 0
    while x < 1000:
        player1.newGuess()
        player2.newGuess()

        winning = random.randint(1, 3)
        allNumbers = set((1,2,3))
        numbersToRemove = set ((winning, player1.guess))
        allNumbers -= numbersToRemove
        knownNumber = allNumbers.pop()

        player1.changeMind(knownNumber)

        player1.saveResult(winning)
        player2.saveResult(winning)
        x += 1

    print "player 1 won ", player1.wins, " times"
    print "player 2 won ", player2.wins, " times"
