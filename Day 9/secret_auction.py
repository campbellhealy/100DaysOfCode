# secret_auction.py
"""
    Welcome screen 
    What is your name?
    What is your bid?
    Is there another bidder?
"""
from os import system
from art import logo

bidders = {}


def main_function():
    bidder_names = ""
    add_bid()
    for i in bidders.keys():
        bidder_names = bidder_names + " " + i + ", "

    if bidder_names == "":
        bidder_names = "none at present"

    system("cls")
    print(logo)
    print(f"The bidders: {bidder_names}") 
    print (calculate_winner()) 
    exit()


def add_bid():
    system("cls")
    print(logo)
    print("Welcome to the Silent Auction")
    bidder_name = input("What is your name? \n")
    bidder_amount = input("How much is the bid? :£")
    any_more_bidders = input("Does anyone else want to bid?\nYes/No \n").lower()
    bidders[bidder_name] = bidder_amount
    if any_more_bidders == "y":
        add_bid()
    return


def calculate_winner():
    highest_bidder = max(bidders, key= bidders.get)
    all_bids = bidders.values()
    highest_bid = max(all_bids)
    return print(f"The winner is {highest_bidder} with a bid of £{highest_bid}")

if __name__ == "__main__":
    main_function()
