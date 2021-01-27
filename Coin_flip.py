# Simple Coin flip that allows a user to flip a 2-sided coin a chosen amount of times and returns the number of heads and tails received.

import random


def coin_flip(flips):
    heads = 0
    tails = 0
    for _ in range(flips):
        i = random.choice([0, 1])
        if i == 0:
            heads += 1
            print('Heads flipped')
        else:
            tails += 1
            print('Tails flipped')
    print("You flipped " + str(heads) + " heads and " + str(tails) + " tails! ")
