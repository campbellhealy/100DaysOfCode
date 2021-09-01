# add_two_digits from a number.py
'''
    Get the user to input a two digit number
    Then add the two digits together
    Output the new value
    I have added in error management to this
'''
from os import system
from time import sleep

def two_digit_add():
    system('cls')
    two_digits = ''
    # Inputs
    two_digits = input('Enter a two digit number \n')
    try:
        int(two_digits)
    except ValueError:
        print('It has to be a number')
        sleep(2)
        two_digit_add()

    if len(two_digits) != 2:
        print('It has to be a two digit number')
        sleep(2)
        two_digit_add()

    digit_one = int(two_digits[0])
    digit_two = int(two_digits[1])

    # Calculation
    digit_sum = digit_one + digit_two

    # Output
    print(digit_sum)
    exit()
    
if __name__ == "__main__":
    two_digit_add()