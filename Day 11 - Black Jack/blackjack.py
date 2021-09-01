# blackjack.py
"""
    Create a console blackjack game.
    ############### Blackjack Project #####################

    #Difficulty Normal 😎: Use all Hints below to complete the project.
    #Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
    #Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
    #Difficulty Expert 🤯: Only use Hint 1 to complete the project.

    ############### Our Blackjack House Rules #####################

    ## The deck is unlimited in size. 
    ## There are no jokers. 
    ## The Jack/Queen/King all count as 10.
    ## The the Ace can count as 11 or 1.
    ## Use the following list as the deck of cards:
    ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ## The cards in the list have equal probability of being drawn.
    ## Cards are not removed from the deck as they are drawn.
    ## The computer is the dealer.
"""

from logo import logo
from random import choice
from os import system
from time import sleep


def header():
    return system("cls"), print(logo)


def card_deal():
    # Random card choice
    dealt_card = key, val = choice(list(cards_dict.items()))
    return dealt_card


def dealers_request(dealers_hand):
    dealer_next_card = input("Dealer, do you want another card? \n").lower()
    while dealers_hand < 21 and dealer_next_card == "y":
        system("cls")
        next_deal = card_deal()
        print(dealers_hand)
        dealers_hand += next_deal[1]
        print(dealers_hand)
        if dealers_hand > 21 and next_deal[0] == "A":
            dealers_hand -= 10
        system("cls")
        print(f"Dealer gets a {next_deal[0]}")
        system("cls")
        print(logo)
        dealer_next_card = input(
            f"Dealer, your total is {dealers_hand}. Do you want another card? \n"
        ).lower()

    return dealers_hand


def users_request(users_hand):
    user_next_card = input("User, do you want another card? \n").lower()
    while users_hand < 21 and user_next_card == "y":
        system("cls")
        next_deal = card_deal()
        users_hand += next_deal[1]
        if users_hand > 21 and next_deal[0] == "A":
            users_hand -= 10
        system("cls")
        print(f"User gets a {next_deal[0]}")
        system("cls")
        print(logo)
        user_next_card = input(
            f"User, your total is {users_hand} Do you want another card? \n"
        ).lower()
    return users_hand


cards_dict = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}
dealers_hand = 0
users_hand = 0
number_of_cards_dealt = 1

# First card deals
header()
while number_of_cards_dealt == 1:
    # Random card choice  dealer
    deal = card_deal()
    dealers_hand += deal[1]
    print(f"Dealer gets a {deal[0]}")

    # Random card choice user
    deal = card_deal()
    users_hand += deal[1]
    print(f"User gets a {deal[0]}")
    number_of_cards_dealt += 1
    sleep(2)

# Next card deals
header()
dealers_hand = dealers_request(dealers_hand)
header()
users_hand = users_request(users_hand)


if dealers_hand > 21 and users_hand > 21:
    header()
    print("It's a bust for both")
elif users_hand > 21:
    header()
    print("Dealer wins, User hand is bust")
elif dealers_hand > 21:
    header()
    print("User wins, Dealer's hand is bust")
elif dealers_hand > users_hand or dealers_hand == users_hand:
    header()
    print("Dealer Wins!")
elif users_hand > dealers_hand:
    header()
    print("User Wins!")


print(f"\nDealer hand total is {dealers_hand}")
print(f"User hand total is {users_hand}")
