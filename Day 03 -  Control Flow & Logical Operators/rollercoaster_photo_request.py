# rollercoaster_photo_request.py
"""
    Adding to the rider_height_age.py code.
    The rider is allowed to ride they get asked if they want a photo of the trip.
    To reduce the repetative code, I have pushed the additional cost into a secondary function that adds
    the extra cost of the photo and returns the value of the bill to the original function.
    Note: I also dragged the age from the main function into this secondary function to tell the user the
    type of ticket they are purchasing.
"""
from os import system
from time import sleep


def rollercoaster():
    system("cls")
    print("Welcome to the Rollercoaster")
    height = int(input("What height are you?(cm) \n"))
    age = int(input("What age are you? \n"))

    if height >= 120:
        system("cls")
        print("You are Okay take a ride on the Rollercoaster.")
        if age >= 18:
            bill = 12
            photo_requested(bill, age)
        elif age < 18 and age >= 12:
            bill = 7
            photo_requested(bill, age)
        else:
            bill = 5
            photo_requested(bill, age)
    else:
        print("Sorry, you are not tall enough for this ride.")


def photo_requested(bill, age):
    # I added this, as it allows the value of the photo to be changed at the variable rather than in the code. 
    # Variables could be in an imported file, staying away from the main code.
    photo = 3  

    if age >= 18:
        print(f"The Adult ticket costs £{bill}")
    elif age < 18 and age >= 12:
        print(f"The Youth ticket is £{bill}")
    elif age < 12:
        print(f"The Child ticket is £{bill}")

    photo_requirement = input(
        f"Do you want a photo of the event? \nIt is an extra £{photo}. \n(y/n) \n"
    )
    if photo_requirement == "y":
        bill += photo
        system("cls")
        print(f"The total cost is £{bill}")
    elif photo_requirement == "n":
        system("cls")
        print(f"The total cost is £{bill}")
    else:
        print("Error")


if __name__ == "__main__":
    rollercoaster()
