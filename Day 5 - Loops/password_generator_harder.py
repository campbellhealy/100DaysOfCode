# password_generator.py
"""
    The generator should ask for:
        The number of letters, number of integers and special characters.
        Add in a method to shuffle up the characters in the password.
        When using the string to hold the characters,random.shuffle gives an error, 
        but random.sample can be used to split and join the characters into a new string. 
        The offical doc, directs the coder from using shuffle to sample.
        https://docs.python.org/3/library/random.html
"""
from random import randint, sample


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
    password = ""

    # number_of_letters = int(input("How many letters do you want in the password? \n"))
    # number_of_integers = int(input("How many numbers do you want in the password? \n"))
    # number_of_special = int(
    #     input("How many special characters do you want in the password? \n")
    # )

    number_of_letters = 3
    number_of_integers = 3
    number_of_special = 3

    for i in range(0, number_of_letters):
        x = randint(0, (len(letters) - 1))
        password = password + letters[x]

    for i in range(0, number_of_integers):
        x = randint(0, (len(integers) - 1))
        password = password + str(integers[x])

    for i in range(0, number_of_special):
        x = randint(0, (len(specials) - 1))
        password = password + specials[x]

    print(f"Before the shuffle {password}")
    sample_password = "".join(sample(password, len(password)))
    print(f"After the shuffle original is still accessible {password}")
    print(f"After the shuffle the new string {sample_password}")


if __name__ == "__main__":
    password_generator()
