# odd_or_even.py
'''
    Dividing a number to determine whether the input was odd or even
    This is making use of the modulo. A divider that gives the remainder value
    Dividing a number by 2 and determing whether there is a remainder either 0 or 1
    0 = Even
    1 = Odd
'''

from time import sleep

def odd_or_even():
    user_input = input('Input a number \n')
    try:
        int(user_input)
    except ValueError:
        print('It has to be a number')
        sleep(2)
        odd_or_even()

    odd_even = int(user_input) % 2
    if odd_even == 1:
        print(f'The number {user_input} is an odd number')    
    else:  
        print(f'The number {user_input} is an even number')    


if __name__ == "__main__":
    odd_or_even()