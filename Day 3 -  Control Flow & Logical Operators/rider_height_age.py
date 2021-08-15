# rider_height_age.py

from os import system
from time import sleep


def rollercoaster():
    print('Welcome to the Rollercoaster')
    height = int(input('What height are you? \n'))
    age = int(input('What age are you? \n'))
    
    if height >= 120:
        print('You are tall enough to take a ride on the Rollercoaster.')
        if age >=18:
            print('The cost is £12')
        elif age < 18 and age >=12:
            print('The cost is £7')
        else:
            print('The cost is £5')
    else:
        print('Sorry, you are not tall enough for this ride')


if __name__ == "__main__":
    rollercoaster()
