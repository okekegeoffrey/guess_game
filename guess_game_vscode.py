# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:15:31 2019

@author: UHS
"""

from random import randint

# func that generates random integer
def random_num():
    """this func generates random integer"""
    return randint(0, 10)

def right_guess(guess, generated_int):
    """this function checks if guessed int is equal to generated in"""
    return guess == generated_int

name: str = input('Hello, enter your name: ')

print(f'\nWelcome to the Guess Game, {name.capitalize()}\n')

print("Let's see how many steps it will take to guess the right number between 0 and 10\n")

# generate the random number
gen_ran = random_num()

# request input from the user
answer: int = int(input('Make a guess! '))

COUNT = 1

game_on = True

while game_on:
    if right_guess(answer, gen_ran):
        game_on = False
    else:
        answer: int = int(input('Guess again: '))
        COUNT += 1
        continue


print(f'Weldone {name.capitalize()}. You won after {COUNT} steps.')