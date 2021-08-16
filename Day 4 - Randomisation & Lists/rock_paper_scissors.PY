# rock_paper_scissors.PY
'''

'''
from os import system
from random import randint


# images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# As this is a lists lessons, create a list with the above images

choices_list = [rock, paper, scissors]


system('cls')
user_selects = (input('Make your choice! \nI won\'t tell the PC \n(R)ock, (P)aper or (S)cissors \n')).lower()
if user_selects == 'r':
    user_selects = choices_list[0]
    user_value = 0
elif user_selects == 'p':
    user_selects = choices_list[1]
    user_value = 1
elif user_selects == 's':
    user_selects = choices_list[2]
    user_value = 2
else:
    user_value = 100
    print('That wasn\'t an option. \nYou Lose!\n')
    exit()
    

computer_value = randint(0,2)
computer_selects = choices_list[computer_value]

# Print out Images
system('cls')
print(f'User Selects')
print(user_selects)
print('Computer Selects')
print(computer_selects)

if user_value >= 3 or user_value < 0: 
    print("You typed an invalid entry, you lose!") 
elif user_value == 0 and computer_value == 2:
    print("You win!")
elif computer_value == 0 and user_value == 2:
    print("You lose")
elif computer_value > user_value:
    print("You lose")
elif user_value > computer_value:
    print("You win!")
elif computer_value == user_value:
    print("It's a draw")

