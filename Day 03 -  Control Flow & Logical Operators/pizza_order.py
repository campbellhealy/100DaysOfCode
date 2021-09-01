# pizza_order.py

"""
    What size of pizza and what additions to the base pizza
    Sizes Small, Medium and Large
    Prices 15,20,25
    Add Pepperoni 2,3,3
    Extra Cheese 1,1,1
"""
from os import system


def pizza_order():
    size = input("Which size of Pizza would you like? \n(S/M/L) \n").lower()

    if size == "s":
        sub_total = 15
        pepperoni(size, sub_total)
    elif size == "m":
        sub_total = 20
        pepperoni(size, sub_total)
    elif size == "l":
        sub_total = 25
        pepperoni(size, sub_total)
    else:
        print("Error in size choice")


def pepperoni(size, sub_total):
    system("cls")
    print(f"The sub-total for your pizza is currently £{sub_total}")
    pepperoni = input("Would you like to add pepperoni? \n(Y/N) \n").lower()
    if pepperoni == "y" and size == "s":
        sub_total += 2
        extra_cheese(sub_total)
    elif pepperoni == "y" and size == "m" or size == "l":
        sub_total += 3
        extra_cheese(sub_total)


def extra_cheese(sub_total):
    system("cls")
    print(f"The sub-total for your pizza is currently £{sub_total}")
    cheese = input("Would you like extra cheese? \n (Y/N) \n").lower()
    if cheese == "y":
        sub_total += 1
        final_bill(sub_total)
    elif cheese == "n":
        final_bill(sub_total)


def final_bill(sub_total):
    system("cls")
    print(f"The total cost of your pizza is £{sub_total}")


if __name__ == "__main__":
    pizza_order()
