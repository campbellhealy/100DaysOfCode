# bmi_2.py
"""
    A BMI Calculator v2
    A simple calculator with interpretation

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.
"""
from os import system


def bmi_calculator(weight, height):
    bmi = round(weight / (height ** 2), 1)  # Last value is to the # of decmal places
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi >= 25 and bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi >= 30 and bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")


system("cls")
weight = float(input("What is you weight in kg? \n"))
height = float(input("What is your height (m)? \n"))
bmi_calculator(weight, height)
