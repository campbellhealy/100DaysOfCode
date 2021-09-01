# higher_lower.py

from header import logo, vs
from game_data import data
from os import system
from random import randint


def header():
    system('cls')
    print(logo)

def random_choice():
    random_int = randint(0, len(data)-1)
    the_choice = data[random_int]
    return the_choice

def again():
    again = input('Do you want to try again? Y/N\n').lower()
    if again == 'y':
        higher_lower()
    else:    
        exit()


def higher_lower():
    header()

    choice_a = random_choice()
    name_a, descript_a, country_a, followers_a = choice_a['name'], choice_a['description'], choice_a['country'],choice_a['follower_count']
    choice_b = random_choice()
    name_b, descript_b, country_b, followers_b = choice_b['name'], choice_b['description'], choice_b['country'],choice_b['follower_count']

    # Set the answer to the user question
    if followers_a == followers_b:
        higher_lower()
    elif followers_a > followers_b:
        answer = 'a'
    elif followers_a < followers_b:
        answer = 'b'

    # Console Display
    print( f'Compare A:\n     Name: {name_a}, {descript_a}\n     from {country_a}')
    print(vs)
    print( f'Compare B:\n     Name: {name_b}, {descript_b}\n     from {country_b}\n')
    
    # User asked to guess
    the_guess = input('Who has the most Followers? A or B \n').lower()
    if the_guess != answer:
        print('Sorry you lose')
        if answer == 'a':
            print(f'{name_a} has more followers than {name_b}\nThey have {followers_a} followers\n')
        elif answer == 'b':
            print(f'{name_b} has more followers than {name_a}\nThey have{followers_b} followers\n')
        again()
    elif the_guess == answer and answer == 'a':
        win = f'You are correct. \n{name_a} has more followers than {name_b}\nThey have {followers_a} followers'
    elif the_guess == answer and answer == 'b':
        win = f'You are correct. \n{name_b} has more followers than {name_a}\nThey have{followers_b} followers'
    
    print(win)
    again()


if __name__ == '__main__':
    higher_lower()
