# calculator_while_loop.py
'''
    Using the previous calculator but with a while loop.
    Then using the artwork in a function to get a nice screen that holds the logo
    and asks the various quiestions.
'''


from os import system
from art import logo


# Operational Functions
def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number

def header():
    return system("cls"), print(logo)


def calculator():
    header()
    # User Input
    first_number = int(input("What is the first number? \n"))
    should_continue = True

    while should_continue:
        header()
        second_number = int(input("What is the next number? \n"))

        # Show possible operators
        possible_operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
        header()
        for i in possible_operators:
            print(i)
        operator_choice = input("Which operator? \n")
        calculation = possible_operators[operator_choice]  # Calculation Function[Choice]
        answer = calculation(first_number, second_number)

        header()
        print(
            f"The calculation is\n{first_number} {operator_choice} {second_number} = {answer} \n",
        )

        if input (f'Do you want to add to that value? "y" to continue or "n" to end \n') == 'y':
            first_number = answer
        else:
            header()
            again = input('Do you want a new calculation? \nY/N \n').lower()
            if again == 'y':
                calculator()
            else:
                exit()
calculator()