# bmi_calculator.py
'''
    A BMI Calculator
    A simple calculator with no error management
'''
from os import system

def bmi_calculator(weight, height):
    bmi = int(weight / ( height * height))
    print(f'Your BMI is {bmi}')


weight = int(input('What is you weight in kg? \n'))
height = float(input('What is your height (m)? \n') )
bmi_calculator(weight, height)