# cipher.py
"""
    create a simple cipher coder/decoder
"""
from header import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cypher(start_text, off_set, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
        off_set *= -1
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + off_set
            end_text += alphabet[new_position]
        else:
            end_text += i
    print(f"Here's the {cypher_direction}d result: {end_text}")


print(logo)

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    cypher(start_text=text, off_set=shift, cypher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
