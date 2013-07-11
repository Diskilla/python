#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Autor: Josef Florian Sedlmeier

print "Welcome to Las Vegas!"
budget = 20

def readInput():
    guess = raw_input()
    number = -1
    if guess != '':
        try:
            number = int(guess)
        except Exception, arg:
            print "no valid number", arg

        return number

def askForBet(number):
    bet = 0
    if number != -1:
        print "Your bet: ",
        bet = readInput()

    return bet

def calculateBudget(budget, number, numberBet, color, colorBet, realityNumber, realityColor):
    if number != -1:
        budget -= numberBet
        if number == realityNumber:
            # 35-fach + Einsatz
            budget += numberBet*36
            print budget, "number"

    if color != -1:
        budget -= colorBet
        if color == realityColor:
            budget += colorBet*2

    return budget

while True:
    print "Choose a number: ",
    number      = readInput()
    numberBet   = askForBet(number)

    print "Red(1) or Black(0):",
    color       = readInput()
    colorBet    = askForBet(color)

    if number == -1 and color == -1:
        break

