# treasure_map.py
"""
    Marking X for the Treasure on a map. 
    This is using a list of lists and how to locate a specific item within the list of lists.
"""
from os import system


def x_spot():
    system("cls")
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    print("Where do you want to put the treasure?")

    the_row = (
        int(input("Choose the row: \n1,2 or 3 \n")) - 1
    )  # Minus one saves using 0 - 2 as locations.
    the_column = (
        int(input("Choose the column \n1,2 or 3 \n")) - 1
    )  # Minus one saves using 0 - 2 as locations.
    system("cls")

    # X Marks the Spot
    map[the_row][the_column] = "X"

    print(f"{row1}\n{row2}\n{row3}")


if __name__ == "__main__":
    x_spot()
