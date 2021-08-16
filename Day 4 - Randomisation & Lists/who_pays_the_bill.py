# who_pays_the_bill.py

"""
    The game of chance for who is paying the bill at the cafe.
"""
from random import randint
from os import system


def bill_payer():
    system("cls")
    # names_string = input("Give me everybody's names, separated by a comma. ")
    names_string = "Bill,Ben,John,Paul,Peter"
    names = names_string.split(",")  # Removed the space used in the splitter
    # Number of names in list
    length_of_names = len(names)

    print("All the names are:")
    for x in range(0, length_of_names):
        print(names[x])

    random_choice = randint(0, (length_of_names - 1))  # Remember the minus one here
    print(f"The bill payer this time is {names[random_choice]}")


if __name__ == "__main__":
    bill_payer()
