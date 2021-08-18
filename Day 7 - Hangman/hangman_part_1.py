# hangman.py
'''

'''

from random import randint, shuffle
from os import system

# Generate the Random word
system('cls')
word_list = ['aardvark', 'baboon', 'camel','rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
shuffle(word_list) # Shuffle the word list 
x = randint(0,len(word_list)-1)

# Get User Guess
# guess = input('Guess a  letter that may be in the word: \n').lower()
guess = 'a'
the_word = word_list[x] # Grab a word from the shuffled list

if guess in the_word:
    print('The letter is in the word')
else:
    print('This letter is not in the word')


# system('cls')
# print(f'Your guess was {guess}')
print(f'The word letters were {the_word}')