# tip_calculator.py
'''
    Calculate the tip for the total of a bill.
    Bill Amount
    Number of Guests at the Table
    Percentage of the Tip (Choosing between three options)
    Calculate the Total Tip
    Calculate the tip per Guest
'''
from os import system

system('cls')
print('Welcome to the the Tip Calculator')
# Data entry
total_bill = int(input('What is the total of the bill for your table? \n'))
number_of_guests = int(input('How many guests are at your table? \n'))
percentage_tip = int(input('What Percentage Tip are you giving? \n10% ,15% or 20% \n'))

# Calculation  - Round down to the penny
tip_per_guest = round((total_bill/number_of_guests)*(percentage_tip/100),2)
tip_per_guest = "{:.2f}".format(tip_per_guest) # Ensure there are two decimal points when 00

# Output
print(f'Each guest should contribute £{tip_per_guest}')



