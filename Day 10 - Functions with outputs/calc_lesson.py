# calc_lesson.py
"""
    I started this based on the lesson. As I was learning new ways of
    doing the expected task. It is much clearer than the way I was writing it.
    See my own, without looking, attempt.
    I have worked to include my naming and added in my own solution to repeating
    the use of the code.

    Only has 2 calcutations
"""

from os import system


# Operational Functions
def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


def calculator():
    system("cls")  # Clears console
    # User Input
    first_number = int(input("What is the first number? \n"))
    second_number = int(input("What is the second number? \n"))

    # Show possible operators
    possible_operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
    for i in possible_operators:
        print(i)
    operator_choice = input("Which operator? \n")
    calculation = possible_operators[operator_choice]  # Calculation Function[Choice]
    first_answer = calculation(first_number, second_number)
    system("cls")
    print(
        f"The calculation is\n{first_number} {operator_choice} {second_number} = {first_answer} \n",
    )
    further_calculation = input('Do you want to use the answer in another calculation? \n').lower()
    if further_calculation == 'y':
        third_number = input('What is the additional value? \n')
        for i in possible_operators:
            print(i)
        operator_choice = input("Which operator? \n")
        calculation = possible_operators[operator_choice]
        second_answer = calculation(first_answer, second_number)
        system("cls")
        print(
            f"The second calculation is\n{first_answer} {operator_choice} {second_number} = {second_answer} \n",
        )

    another = input("Do you have a new calculation? \n").lower()
    if another == "y":
        calculator()
    else:
        print("Bye")
        exit()


if __name__ == "__main__":
    calculator()
