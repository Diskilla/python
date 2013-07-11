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
            self.win += 1
