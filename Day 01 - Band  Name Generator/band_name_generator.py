# band_name_generator.py
'''
    A name generator using a couple of pieces of input from the user
'''
from os import system
def name_generator():
    system('cls')
    print('Band Name Generator')
    print('*******************')
    place = input('Name your favourite place: \n')
    food = input('What is your favourite food? \n')
    system('cls')
    print()
    print(place, food)
    print()



if __name__ == "__main__":
    name_generator()