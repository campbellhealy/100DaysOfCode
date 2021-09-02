# coffee_machine.py
"""
    Print Report
    Detail what resources remain in the Coffee Machine
    Starting reosurce:
        Water: 300ml
        Milk: 200ml
        coffee: 100g
    Offer 3 Coffee Types,
        With differing ingredients and cost
    Accept 4 coins for payment  1,5,10, 25

    Which Coffee would you like or report?
    This will cost £x
        Take payment, 
        calculate the amount required, 
        Take Payment, 
        Calculate Change

    Say enjoy the coffee type
    Repeat the service/report
"""
from os import system
from time import sleep
from header import logo
from resources import MENU, resources

# Resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
total_input = 0.00  # Cash handed over by user
amount = 0.00  # Used to create takings string for report
takings = 0.00  # Addition to the till amount


def restart():
    # Tried to restart the main function from within the function, had to use this instead
    coffee_choice()


def machine_resource_check(coffee_available):
    # Determine if the coffee can be made
    water_cost = int(MENU[coffee_available]["ingredients"]["water"])
    coffee_cost = int(MENU[coffee_available]["ingredients"]["coffee"])
    if coffee_available != "espresso":
        milk_cost = int(MENU[coffee_available]["ingredients"]["milk"])
    else:
        milk_cost = 0.00

    if water < water_cost:
        print("There is not enough water \nPlease Report this\n")
        sleep(2)
        coffee_choice()
    elif milk < milk_cost:
        print("There is not enough milk \nPlease Report this\n")
        sleep(2)
        coffee_choice()
    elif coffee < coffee_cost:
        print("There is not enough coffee \nPlease Report this\n")
        sleep(2)
        coffee_choice()
    else:
        deduct_resources(water_cost, milk_cost, coffee_cost)
        return


def deduct_resources(water_cost, milk_cost, coffee_cost):
    # Remove used resoures
    global water, milk, coffee
    water -= water_cost
    milk -= milk_cost
    coffee -= coffee_cost
    return


def header():
    system("cls")
    print(logo)


def report():
    # Gather information from the coffee machine
    amount = "{:.2f}".format(takings)
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g\nMoney: £{amount}")
    sleep(5)
    restart()


def coffee_charge(coffee_choice):
    # Get cost of the coffee choice
    coffee_choice = MENU[coffee_choice]
    coffee_cost = coffee_choice["cost"]
    return coffee_cost


def payment_system(coffee_cost, coffee_choice):
    header()
    coffee_cost = "{:.2f}".format(coffee_cost)
    print(f"Your {coffee_choice} will cost £{coffee_cost}.")
    coffee_cost = float(coffee_cost)
    total_input = 0
    the_change = the_till(coffee_cost, total_input)
    return the_change


def the_till(coffee_cost, total_input):
    print("For Payment, I accept 1, 5, 10 & 25 cent coins")

    twenty_fives = int(input("How many 25 cent coins? "))
    tens = int(input("How many 10 cent coins? "))
    fives = int(input("How many 5 cent coins? "))
    ones = int(input("How many 1 cent coins? "))
    total_input = ((twenty_fives * 25) + (tens * 10) + (fives * 5) + ones) / 100
    cash_input = "{:.2f}".format(total_input)
    print(f"You inserted £{cash_input}")
    change_calculator = total_input - coffee_cost
    change_calculator = float("{:.2f}".format(change_calculator))
    if change_calculator < 0:
        print("You need to pay more")
        coffee_cost = coffee_cost - total_input
        the_till(coffee_cost, total_input)

    return change_calculator


def coffee_choice():
    global takings
    header()
    coffee_choice = input(
        "Which coffee would you like? \n([L]atte/[E]spresso/[C]appuccino) \n"
    ).lower()

    if coffee_choice == "report":
        report()
    elif coffee_choice == "e":
        coffee_choice = "espresso"
    elif coffee_choice == "l":
        coffee_choice = "latte"
    elif coffee_choice == "c":
        coffee_choice = "cappuccino"
    elif coffee_choice == "q": # Option to quit
        exit()
    else:
        restart()

    machine_resource_check(coffee_choice)
    coffee_cost = float(coffee_charge(coffee_choice))
    coffee_cost = float("{0:.2f}".format(coffee_cost))
    change_calculator = payment_system(coffee_cost, coffee_choice)

    if change_calculator < 0:
        header()
        takings += coffee_cost
        print(f"Enjoy your {coffee_choice}")
        print("Thank you for your business \n")
        sleep(4)
    else:
        header()
        takings += coffee_cost
        change_calculator = "{:.2f}".format(change_calculator)
        change_calculator = float(change_calculator)
        print(f"Enjoy your {coffee_choice}")
        if change_calculator > 0:
            print(f"Your change is £{change_calculator}")
        sleep(4)
    restart()


if __name__ == "__main__":
    coffee_choice()
