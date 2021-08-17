# heads_tails.py
# A simple coin Toss tool

from random import randint

x = randint(0, 2)

if x == 1:
    print("Heads")
else:
    print("Tails")
