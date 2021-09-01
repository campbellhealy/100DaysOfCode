# calculator.py
"""
    What is the first number?
    What is the second number?
    What is the operator?
"""
from os import system


def calculator():
    system("cls")
    first_number, second_number, operator_choice = 0,0,''
    possible_operators = ["+", "-", "*", "/"]
    first_number = int(input("What is the first number? \n"))
    second_number = int(input("What is the second number? \n"))
    operator_choice = input("Which operator? \n + - * / \n")

    if operator_choice not in possible_operators:
        print("The operator choice is not  valid.")
        exit()
    else:
        if operator_choice == "+":
            return first_number + second_number
        elif operator_choice == "-":
            return first_number - second_number
        elif operator_choice == "*":
            return first_number * second_number
        elif operator_choice == "/":
            return first_number / second_number
        else:
            return


print(calculator())
another_calculation = input("Do you want another calculation? \n (Y/N)").lower()
if another_calculation == "y":
    calculator()
else:
    exit()


if __name__ == "__main__":
    calculator()
