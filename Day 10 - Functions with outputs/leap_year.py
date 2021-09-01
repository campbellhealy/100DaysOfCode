# leap_year.py
"""
    Using Year and month. Building on the previous version of this code.

"""

from os import system
from time import sleep


def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a Leap year.")
                leap = True
            else:
                print(f"{year} is Not a Leap year.")
        else:
            print(f"{year} is a Leap year.")
            leap = True
    else:
        print(f"{year} is Not a Leap year.")
    return leap


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month > 12 or month < 1:
        return print("The month choice is not valid"), sleep(2), main_function()
        
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


def main_function():
    system("cls")
    print('Find the number of days in a month for that year.')
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(f"The number of days in that month is {days}")


if __name__ == "__main__":
    main_function()


