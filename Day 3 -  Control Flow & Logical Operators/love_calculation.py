# love_calculation.py

"""
    Based on the childrens game of counting the number of times the letters from 'True Love'
    appear both the name of your crush and your name.
    This is use the lower() function and count () function
    Love scores <10 or >90, between 40 & 50, 

    Again I have worked on this to go beyond the lesson. Breaking out a few function calls and returned values
"""

from os import system


def enter_names():
    system('cls')
    name1 = input("What is your first name? \n").lower()
    system('cls')
    name2 = input("What is their first name? \n").lower()
    system('cls')
    love_score = love_calc(name1, name2)
    result(love_score)

def love_calc(name1, name2):
    true_love = set("truelove")
    total_score_name1 = 0
    total_score_name2 = 0
    for x in true_love:
        name1_count = name1.count(x)
        total_score_name1 = total_score_name1 + name1_count
        name2_count = name2.count(x)
        total_score_name2 = total_score_name2 + name2_count

    total_score_name1 = total_score_name1 * 10
    love_score = total_score_name1 + total_score_name2
    return love_score

def result(love_score):
    if love_score <10 or love_score > 90:
        print(f'Your score is {love_score}  , you go together like coke and mentos.')
    elif love_score >=40 and love_score <=50:
        print(f'Your score is {love_score}, you are alright together.')
    else:
        print(f'Your score is {love_score}')

if __name__ == "__main__":
    enter_names()
