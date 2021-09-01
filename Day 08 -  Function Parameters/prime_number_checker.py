# prime_number_checker.py
"""
    Is the number a prime number?
    I just read that the excerise was to write a prime number checker.
    Then got the head down to work on it without listening to the lesson.
    Got it! I wrote the code with an user input to test, then converted it into
    a function that accepts a parameter check_number.
    Finally, I added in a random list generator  and iterated over that list.
"""

from os import system
from random import randint


def main_function():
    system("cls")
    # Generate a list of 10 integers between 1 - 499
    random_list = [randint(1, 500) for i in range(10)]

    # Check each value in the list
    for i in random_list:
        prime_checker(i)


def prime_checker(check_number):
    print("***__Prime Number Checker__***")
    # check_number = int(input('Type in your number \n'))

    for i in range(2, check_number - 1):
        if check_number % i == 0:
            return print(f"Nope \n {check_number} is not prime \n")
            # exit()
    return print(f"The number {check_number} is a Prime Number \n")


if __name__ == "__main__":
    main_function()
