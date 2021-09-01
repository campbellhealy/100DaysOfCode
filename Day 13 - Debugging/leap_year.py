# leap_year.py

year = input("Which year do you want to check?")

# The input is a string and needs changed to an integer

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
