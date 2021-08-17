# password_generator_easy.py
"""
    The generator should ask for:
        The number of letters, number of integers and special characters.
    A pretty basic list of random characters.
    The lesson for the easy generator, creates a list, something
    that is easy to shuffle and convert into than a string. 
"""
from random import randint, shuffle
from typing import final


def password_generator():
    # Number of letters
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    # Number of integers
    integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Number of specials
    specials = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    password = []

    number_of_letters = int(input("How many letters do you want in the password? \n"))
    number_of_integers = int(input("How many numbers do you want in the password? \n"))
    number_of_special = int(
        input("How many special characters do you want in the password? \n")
    )

    # number_of_letters = 3
    # number_of_integers = 3
    # number_of_special = 3

    for i in range(0, number_of_letters + 1):
        x = randint(0, (len(letters) - 1))
        password.append(letters[x])

    for i in range(0, number_of_special + 1):
        x = randint(0, (len(specials) - 1))
        password.append(specials[x])

    for i in range(0, number_of_integers + 1):
        x = randint(0, (len(integers) - 1))
        password.append(str(integers[x]))

    # for i in range (0, number_of_letters):
    #     x = randint(0, (len(letters)-1))
    #     password = password + letters[x]

    #     x = randint(0, (len(integers)-1))
    #     password = password + str(integers[x])

    #     x = randint(0, (len(specials)-1))
    #     password = password + specials[x]

    shuffle(password)
    final_password = ''
    for i in password:
        final_password += i
    print(final_password)

if __name__ == "__main__":
    password_generator()
