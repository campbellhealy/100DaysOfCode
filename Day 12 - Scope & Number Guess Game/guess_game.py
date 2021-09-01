# guess_game.py
"""
    Initialiser - guesser()
    Add in a header logo  header ()
    Thinking of a number between 1 and 100 number_generator()
    Choose Difficulty - Easy or Hard difficulty()
        You have H - 5 guesses and E - 10 guesses
    Make a guess:
        too high, too low or Correct?
        Guess Again, You Win or You Lose -  your_guess()
    Count down the number of guesses left - guess_counter()
"""
from header import logo
from os import system
from random import randint


def header():
    system("cls")
    print(logo)


def number_generator():
    the_number = randint(1, 100)
    return the_number
    # pass


def difficulty():
    difficulty = input("Choose a difficulty. [E]asy or [H]ard \n").lower()
    if difficulty == "e":
        number_of_guesses = 10
    elif difficulty == "h":
        number_of_guesses = 5
    return number_of_guesses


def guess_counter(guess, the_number):
    if guess == 0:
        print(f"You lose. \nThe number I was thinking of was {the_number}")
        exit()
    else:
        return


def your_guess(the_number, number_of_guesses):
    the_guess = int(input("What is your guess? \n"))
    if the_guess == the_number:
        header()
        print(f"Well done \nYour guess of {the_guess} was correct. \n")
        exit()
    elif the_guess > the_number:
        header()
        number_of_guesses -= 1
        print(f"That guess of {the_guess} was too high.")
        print(
            f"You have {number_of_guesses}  attempts remaining to guess the number \n"
        )
        guess_counter(number_of_guesses, the_number)
        your_guess(the_number, number_of_guesses)
    elif the_guess < the_number:
        header()
        number_of_guesses -= 1
        print(f"That guess of {the_guess} was too low.")
        print(
            f"You have {number_of_guesses}  attempts remaining to guess the number \n"
        )
        guess_counter(number_of_guesses, the_number)
        your_guess(the_number, number_of_guesses)


def guesser():
    header()
    print("Welcome!!")
    print("I am thinking of a number between 1 and 100 \n")
    the_number = number_generator()
    # print(the_number)
    number_of_guesses = difficulty()
    header()
    print(f"You have {number_of_guesses} attempts remaining to guess the number \n")
    your_guess(the_number, number_of_guesses)


if __name__ == "__main__":
    guesser()
