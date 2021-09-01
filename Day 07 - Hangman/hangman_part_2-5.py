# hangman.py
'''

'''

from random import randint, shuffle
from os import system
from hang_me import HANGMANPICS
from time import sleep

def hangman():
    # Generate the Random word
    system('cls')
    word_list = ['aardvark', 'baboon', 'camel','rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
    shuffle(word_list) # Shuffle the word list 
    x = randint(0,len(word_list)-1)
    tries = 0


    the_word = word_list[x] # Grab a word from the shuffled list
    # the_word = 'choco'
    word_length = len(the_word)
    the_word_list = [i for i in the_word]

    # Create the blanks template for the word
    blank_string = []
    for i in range(word_length):
        blank_string.append(' _')
    print(blank_string, '\n')

    while the_word_list != blank_string:
        if tries != 6:
            system('cls')
            print(blank_string)
            print(HANGMANPICS[tries])

            # Get User Guess
            guess = input('Guess a  letter that may be in the word: \n').lower()
            # guess = 'a'
            # Check the guess
            if guess in the_word_list:
                print(f'The letter "{guess}" is in the word. \n')
                for i in range(word_length):
                    letter  = the_word[i]
                    if letter == guess:
                        blank_string[i] = letter
                

            else:
                tries += 1
                if tries != 6:
                    print(f'Wrong, that was guess {tries} of 6')
                    sleep(1.5)

            # print(blank_string)
        else:
            system('cls')
            print(HANGMANPICS[tries])
            print('You Lose!')
            exit()
    system('cls')        
    print(HANGMANPICS[tries])
    print('You Win')
    print(f'The word was "{the_word}"')


if __name__ == '__main__':
    hangman()