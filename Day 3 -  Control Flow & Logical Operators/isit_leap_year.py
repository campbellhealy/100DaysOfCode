# isit_leap_year.py
"""
    Calculate if a year is a leap year.
    The lecture was using multiple if/else statements using division rather than modulo
    That is extra code that is not required, when it can be written like this.
    I found it a backward step from what was previously taught.
"""

from os import system
def leap_year_check(user_input):
    checker = int(user_input % 4) # Remember this is not a modulo of 2, there is more than 0 or 1 remainder
    # print(checker)
    if checker != 0:
        print(f"{user_input} is not a leap year.")
    else:
        print(f"{user_input} is a leap year.")

system('cls')
user_input = int(input("What Year do you want to check? \n"))
leap_year_check(user_input)
