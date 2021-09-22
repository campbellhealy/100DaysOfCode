# main.py
"""
    Coffee Machine using predetermined modules for Machine & Stock management, and payment system
"""
from os import system
from time import sleep


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo


def header():
    # Clears Console and gives a fixed view to the coffee machine console
    system("cls")
    print(logo)


def main_function():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    is_on = True

    while is_on:
        header()
        options = menu.get_items()
        choice = input(f"Which coffee would you like? ({options}): ").lower()
        if choice == "q":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            drink_cost = "{:.2f}".format(drink.cost)  # Format cost to to decimal places
            print(f"\nThe cost of a {drink.name} is £{drink_cost}\n")
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            if not is_enough_ingredients:
                # is_on = coffee_maker.is_resource_sufficient(drink)
                print("Refilling the machine.")
                sleep(5)
                main_function()  # Refills the coffee machine

            is_payment_successful, change_statement = money_machine.make_payment(
                drink.cost
            )
            if is_enough_ingredients and is_payment_successful:
                header()
                print(change_statement)
                coffee_maker.make_coffee(drink)
                sleep(3)
            elif not is_payment_successful:
                header()
                print(change_statement)
                sleep(3)
                main_function()
            else:
                is_on = coffee_maker.is_resource_sufficient(drink)
                print("Refilling the machine.")
                sleep(3)


if __name__ == "__main__":
    main_function()
